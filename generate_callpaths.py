#!/usr/bin/env python3
"""
Generate callpath trees for every external/public function in all dataset repos.
For each contract, traces which internal/private/library functions each external
entry point "touches".

Output: dataset/<Protocol>/callpaths.md
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

DATASET_DIR = Path("dataset")

# Skip directories that aren't real protocol code
SKIP_DIRS = {"node_modules", "lib", "forge-std", ".git", "test", "tests",
             "script", "scripts", "certora", "audits", "crytic"}

# ──────────────────────────────────────────────────────────────────────
# Regex patterns
# ──────────────────────────────────────────────────────────────────────

# Match contract/library/abstract declarations
CONTRACT_RE = re.compile(
    r'^\s*(?:abstract\s+)?(?:contract|library)\s+'
    r'(\w+)'
    r'(?:\s+is\s+([\w\s,]+?))?'
    r'\s*\{',
    re.MULTILINE
)

# Match interface declarations (to skip them)
INTERFACE_RE = re.compile(
    r'^\s*interface\s+(\w+)',
    re.MULTILINE
)

# Match function start: captures "function name"
FUNC_START_RE = re.compile(r'\bfunction\s+(\w+)\s*\(')

# Match visibility keywords
VISIBILITY_RE = re.compile(r'\b(external|public|internal|private)\b')

# Match "using X for Y" declarations
USING_RE = re.compile(
    r'using\s+(\w+)\s+for\s+([^;]+);'
)

# Match function calls: identifier.identifier( or just identifier(
CALL_RE = re.compile(
    r'(?<![.\w])(\w+)\.(\w+)\s*\('   # lib.func( or obj.func(
    r'|'
    r'(?<![.\w])(\w+)\s*\('           # func(
)


def remove_comments(source):
    """Strip single-line and multi-line comments from Solidity source."""
    source = re.sub(r'/\*.*?\*/', '', source, flags=re.DOTALL)
    source = re.sub(r'//[^\n]*', '', source)
    return source


def remove_string_literals(source):
    """Replace string literals with empty strings to avoid false matches."""
    source = re.sub(r'"(?:[^"\\]|\\.)*"', '""', source)
    source = re.sub(r"'(?:[^'\\]|\\.)*'", "''", source)
    return source


def skip_balanced_parens(source, pos):
    """Skip past a balanced parentheses block starting at '(' at pos.
    Returns index after the closing ')'."""
    depth = 0
    i = pos
    while i < len(source):
        if source[i] == '(':
            depth += 1
        elif source[i] == ')':
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return i


def extract_brace_block(source, start_pos):
    """Extract a brace-delimited block starting from the { at start_pos."""
    depth = 0
    i = start_pos
    while i < len(source):
        if source[i] == '{':
            depth += 1
        elif source[i] == '}':
            depth -= 1
            if depth == 0:
                return source[start_pos:i + 1]
        i += 1
    return source[start_pos:]


def parse_contract_blocks(source):
    """
    Split source into contract/library/interface blocks.
    Returns list of (kind, name, parents, body) tuples.
    """
    blocks = []

    interfaces = set()
    for m in INTERFACE_RE.finditer(source):
        interfaces.add(m.group(1))

    for m in CONTRACT_RE.finditer(source):
        name = m.group(1)
        parents_str = m.group(2) or ""
        parents = [p.strip() for p in parents_str.split(",") if p.strip()]

        brace_pos = source.find('{', m.end() - 1)
        if brace_pos == -1:
            continue

        body = extract_brace_block(source, brace_pos)
        kind = "library" if re.search(r'\blibrary\b', m.group(0)) else "contract"
        blocks.append((kind, name, parents, body))

    return blocks, interfaces


def parse_functions(body):
    """
    Parse all function definitions from a contract body.
    Handles multi-line parameter lists and returns clauses robustly.
    Returns dict: func_name -> {visibility, body_text}
    """
    functions = {}

    for m in FUNC_START_RE.finditer(body):
        func_name = m.group(1)
        paren_start = m.end() - 1  # position of '('

        # Skip past the parameter list parentheses
        after_params = skip_balanced_parens(body, paren_start)

        # Now scan forward for the opening '{', collecting modifiers/visibility/returns
        # We need to handle 'returns (...)' which has its own parentheses
        signature_text = ""
        i = after_params
        found_brace = False
        while i < len(body):
            ch = body[i]
            if ch == '{':
                found_brace = True
                break
            elif ch == '(':
                # This is likely a returns(...) block, skip it
                i = skip_balanced_parens(body, i)
                continue
            elif ch == ';':
                # Interface/abstract function declaration, no body
                break
            else:
                signature_text += ch
            i += 1

        if not found_brace:
            continue

        # Determine visibility from the signature between params and body
        vis_match = VISIBILITY_RE.search(signature_text)
        visibility = vis_match.group(1) if vis_match else "public"

        # Extract function body
        func_body = extract_brace_block(body, i)

        functions[func_name] = {
            "visibility": visibility,
            "body": func_body,
        }

    return functions


def parse_using_directives(body):
    """Parse 'using X for Y' directives. Returns list of (library_name, type_name)."""
    usings = []
    for m in USING_RE.finditer(body):
        lib_name = m.group(1).strip()
        type_name = m.group(2).strip()
        usings.append((lib_name, type_name))
    return usings


def extract_calls(func_body, own_functions, library_names, using_libs, all_contracts):
    """
    Extract function calls from a function body.
    Returns list of (call_type, label) tuples.

    call_type is one of:
        "internal" / "private" — function in the same contract
        "library"             — library call
        "external_callback"   — external contract/interface callback
        "view_call"           — reading state from another contract
    """
    calls = []
    seen = set()

    # Solidity built-ins and common keywords to ignore
    ignore = {
        "require", "assert", "revert", "emit", "keccak256", "abi",
        "msg", "block", "tx", "type", "address", "uint256", "uint128",
        "uint160", "uint32", "uint16", "uint8", "uint24", "int256",
        "int128", "int56", "int24", "bytes32", "bytes", "string",
        "bool", "this", "super", "new", "delete", "push", "pop",
        "encode", "encodePacked", "encodeWithSelector", "encodeWithSignature",
        "decode", "encodeCall", "selector",
        "add", "sub", "mul", "div", "mod",  # SafeMath ops we handle via using
        "staticcall", "call", "delegatecall",
        "transfer", "send", "balance",
        "length", "concat",
    }

    clean_body = remove_string_literals(func_body)

    for m in CALL_RE.finditer(clean_body):
        if m.group(1) and m.group(2):
            # Dotted call: X.func()
            prefix = m.group(1)
            func = m.group(2)
            key = f"{prefix}.{func}"

            if key in seen or func in ignore:
                continue
            seen.add(key)

            if prefix in library_names or prefix in {lib for lib, _ in using_libs}:
                calls.append(("library", f"{prefix}.{func}"))
            elif prefix in all_contracts:
                calls.append(("external_callback", f"{prefix}.{func}"))
            elif prefix.startswith("I") and prefix[1:2].isupper():
                # Interface call pattern: IContract.method()
                calls.append(("external_callback", f"{prefix}.{func}"))
            # else: could be state variable method call, skip

        elif m.group(3):
            # Simple call: func()
            func = m.group(3)
            if func in seen or func in ignore:
                continue
            seen.add(func)

            if func in own_functions:
                vis = own_functions[func]["visibility"]
                calls.append((vis, func))

    return calls


def build_callpath(func_name, own_functions, library_names, using_libs,
                   all_contracts, visited=None):
    """
    Recursively build callpath tree.
    Returns list of (depth, call_type, label) tuples.
    """
    if visited is None:
        visited = set()

    if func_name in visited:
        return []
    visited.add(func_name)

    if func_name not in own_functions:
        return []

    func_info = own_functions[func_name]
    calls = extract_calls(func_info["body"], own_functions, library_names,
                          using_libs, all_contracts)

    result = []
    for call_type, label in calls:
        result.append((0, call_type, label))

        # Recurse into internal/private functions
        actual_name = label.split(".")[-1] if "." in label else label
        if actual_name in own_functions and actual_name not in visited:
            sub = build_callpath(actual_name, own_functions, library_names,
                                 using_libs, all_contracts, visited.copy())
            for depth, ct, lb in sub:
                result.append((depth + 1, ct, lb))

    return result


def format_callpath(entry_name, visibility, callpath):
    """Format a callpath tree as markdown text."""
    lines = [f"### {visibility} {entry_name}"]
    if not callpath:
        lines.append("_(no internal calls)_\n")
        return "\n".join(lines) + "\n"

    for depth, call_type, label in callpath:
        indent = "  " * depth
        lines.append(f"{indent}-> {call_type} {label}")

    lines.append("")
    return "\n".join(lines) + "\n"


def analyze_protocol(protocol_dir):
    """Analyze all Solidity files in a protocol's code/ directory."""
    code_dir = protocol_dir / "code"
    if not code_dir.exists():
        return None

    # Collect all .sol files, skipping test/mock/etc directories
    sol_files = []
    for sol_file in code_dir.rglob("*.sol"):
        if not sol_file.is_file():
            continue
        rel_parts = sol_file.relative_to(code_dir).parts
        if any(p.lower() in SKIP_DIRS for p in rel_parts):
            continue
        if any(p.lower().startswith("mock") for p in rel_parts):
            continue
        sol_files.append(sol_file)

    if not sol_files:
        return None

    # Phase 1: Parse all files to collect contract names and library names
    file_sources = {}
    all_contract_names = set()
    all_library_names = set()
    all_interface_names = set()

    for sol_file in sol_files:
        try:
            source = sol_file.read_text(encoding="utf-8", errors="ignore")
            source = remove_comments(source)
            file_sources[sol_file] = source

            blocks, interfaces = parse_contract_blocks(source)
            all_interface_names.update(interfaces)

            for kind, name, parents, body in blocks:
                all_contract_names.add(name)
                if kind == "library":
                    all_library_names.add(name)
        except Exception:
            continue

    # Phase 2: Parse functions and build callpaths per contract
    output_sections = []

    # Collect all contracts with their functions for inheritance resolution
    all_parsed = {}  # contract_name -> {functions, parents, usings, kind}

    for sol_file, source in file_sources.items():
        blocks, _ = parse_contract_blocks(source)
        for kind, name, parents, body in blocks:
            functions = parse_functions(body)
            usings = parse_using_directives(body)
            all_parsed[name] = {
                "functions": functions,
                "parents": parents,
                "usings": usings,
                "kind": kind,
                "file": sol_file.relative_to(code_dir),
            }

    # Phase 3: Build callpaths with inheritance
    for contract_name, info in sorted(all_parsed.items()):
        if info["kind"] == "library":
            continue  # Libraries don't have external entry points in the same way

        # Merge parent functions (simple single-level inheritance)
        merged_functions = {}
        merged_usings = list(info["usings"])
        for parent_name in info["parents"]:
            if parent_name in all_parsed:
                parent = all_parsed[parent_name]
                for fn, fn_info in parent["functions"].items():
                    if fn not in merged_functions:
                        merged_functions[fn] = fn_info
                merged_usings.extend(parent["usings"])

        # Own functions override parents
        merged_functions.update(info["functions"])

        # Find external/public entry points
        entry_points = []
        for fn_name, fn_info in merged_functions.items():
            if fn_info["visibility"] in ("external", "public"):
                entry_points.append((fn_name, fn_info["visibility"]))

        if not entry_points:
            continue

        contract_lines = [f"## {contract_name}\n"]
        contract_lines.append(f"_File: {info['file']}_\n")

        for fn_name, vis in sorted(entry_points):
            callpath = build_callpath(
                fn_name, merged_functions, all_library_names,
                merged_usings, all_contract_names | all_interface_names
            )
            contract_lines.append(format_callpath(fn_name, vis, callpath))

        output_sections.append("\n".join(contract_lines))

    return output_sections


def main():
    protocol_dirs = sorted([
        d for d in DATASET_DIR.iterdir()
        if d.is_dir() and (d / "code").exists()
    ])

    if not protocol_dirs:
        print("No protocol directories found with code/")
        sys.exit(1)

    print(f"Found {len(protocol_dirs)} protocols to analyze\n")
    total_contracts = 0
    total_functions = 0

    for i, protocol_dir in enumerate(protocol_dirs):
        name = protocol_dir.name
        print(f"[{i+1}/{len(protocol_dirs)}] {name}...", end=" ")

        sections = analyze_protocol(protocol_dir)
        if not sections:
            print("no contracts found")
            continue

        # Write callpaths.md
        header = f"# Callpaths — {name}\n\n"
        header += "Each external/public function lists all internal functions, "
        header += "library calls, and external callbacks it touches.\n\n---\n\n"

        content = header + "\n---\n\n".join(sections)

        output_path = protocol_dir / "callpaths.md"
        output_path.write_text(content, encoding="utf-8")

        n_contracts = content.count("\n## ")
        n_functions = content.count("\n### ")
        total_contracts += n_contracts
        total_functions += n_functions
        print(f"{n_contracts} contracts, {n_functions} entry points")

    print(f"\n{'='*60}")
    print(f"DONE — {len(protocol_dirs)} protocols")
    print(f"Total contracts: {total_contracts}")
    print(f"Total entry points: {total_functions}")


if __name__ == "__main__":
    main()
