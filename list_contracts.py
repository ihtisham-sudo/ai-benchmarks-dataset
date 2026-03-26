#!/usr/bin/env python3
"""
Contract List Generator
=======================
Analyses a single protocol codebase from dataset/ and produces a
structured markdown catalogue of all contracts grouped by primitive type:

  Tokens · Containers · Minters · Exchange · Oracle · Access Control

No Solidity code is generated — this is a pure analysis, listing, and
relationship-mapping tool.

Usage:
  python3 list_contracts.py Dinari
  python3 list_contracts.py Dinari --output analysis/Dinari_catalogue.md
  python3 list_contracts.py --list
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from textwrap import dedent

DATASET_DIR = Path("dataset")

SKIP_DIRS = {
    "node_modules", "lib", "forge-std", ".git",
    "test", "tests", "script", "scripts",
    "certora", "audits", "crytic", "dependencies",
    "vendor", "vendors", "third_party", "thirdparty",
    "openzeppelin", "mock", "mocks",
    # Skip interface / abstract / tester sub-directories common in many repos
    "interfaces", "interface", "abstract", "abstracts",
    "testers", "tester", "helpers", "helper",
}

# ─── Primitive categories (in display order) ─────────────────────────────────

CATEGORIES = [
    "token",
    "container",
    "minter",
    "exchange",
    "oracle",
    "acl",
    "core",
    "other",
]

CATEGORY_LABELS = {
    "token":     "Tokens",
    "container": "Containers",
    "minter":    "Minters",
    "exchange":  "Exchange",
    "oracle":    "Oracle",
    "acl":       "Access Control",
    "core":      "Core / Factory",
    "other":     "Other",
}

CATEGORY_INTRO = {
    "token":     "utilises the following token contracts for accounting purposes:",
    "container": "stores assets in the following containers:",
    "minter":    "manages token supply through the following minter contracts:",
    "exchange":  "implements protocol operations as the following exchange contracts:",
    "oracle":    "uses the following oracle contracts to obtain external price data:",
    "acl":       "manages permissions through the following access-control contracts:",
    "core":      "wires components together through the following core contracts:",
    "other":     "includes the following auxiliary contracts:",
}


# ─── Regex helpers ────────────────────────────────────────────────────────────

def remove_comments(src: str) -> str:
    src = re.sub(r'/\*.*?\*/', '', src, flags=re.DOTALL)
    src = re.sub(r'//[^\n]*', '', src)
    return src

def skip_balanced(src: str, pos: int, o: str, c: str) -> int:
    depth, i = 0, pos
    while i < len(src):
        if src[i] == o: depth += 1
        elif src[i] == c:
            depth -= 1
            if depth == 0: return i + 1
        i += 1
    return i

def extract_block(src: str, pos: int) -> str:
    return src[pos:skip_balanced(src, pos, '{', '}')]

CONTRACT_RE = re.compile(
    r'(?:abstract\s+)?(?P<kw>contract|library|interface)\s+(?P<name>\w+)'
    r'(?:\s+is\s+(?P<parents>[\w\s,]+?))?\s*\{',
    re.MULTILINE,
)

FUNC_RE = re.compile(
    r'\bfunction\s+(?P<name>\w+)\s*\([^)]*\)\s*(?P<rest>[^{;]*)',
    re.MULTILINE,
)

NATSPEC_NOTICE_RE = re.compile(r'@notice\s+(.+?)(?=\n\s*\*|\n\s*/|\Z)', re.DOTALL)
NATSPEC_TITLE_RE  = re.compile(r'@title\s+(.+?)(?=\n\s*\*|\n\s*/|\Z)', re.DOTALL)
IMPORT_RE = re.compile(r'\bimport\s+.*?["\']([^"\']+\.sol)["\']', re.MULTILINE)


# ─── Data model ──────────────────────────────────────────────────────────────

@dataclass
class ContractInfo:
    name: str             # contract name as written in Solidity
    filename: str         # relative path inside code/
    category: str         # one of CATEGORIES
    description: str      # human-readable one-sentence purpose
    functions: list[str]  # public/external function names
    parents: list[str]    # inherited contracts
    imports: list[str]    # imported .sol filenames (basename)
    raw_source: str       # cleaned source for relationship analysis


# ─── Classification ───────────────────────────────────────────────────────────

def _classify(name: str, parents: list[str], fn_names: set[str]) -> str:
    nl = name.lower()
    pl = [p.lower() for p in parents]

    # Interfaces and libraries are skipped upstream — only concrete contracts reach here.

    # ── Minter: has mint/burn but is NOT the token itself ──────────────────
    has_erc20 = len({"totalsupply", "balanceof", "transfer", "approve"} & fn_names) >= 3
    has_mint_burn = "mint" in fn_names or "burn" in fn_names
    if has_mint_burn and not has_erc20 and any(
        k in nl for k in ("minter", "issuer", "controller", "manager")
    ) or (
        has_mint_burn and not has_erc20
        and any(k in nl for k in ("processor", "order", "fulfil", "fulfillment", "settlement"))
    ):
        return "minter"

    # ── Token ───────────────────────────────────────────────────────────────
    if has_erc20 or any(k in nl for k in ("token", "coin", "stable", "dshare", "erc20")):
        return "token"
    if any("erc20" in p or "erc721" in p or "erc1155" in p for p in pl):
        return "token"
    if any(k in nl for k in ("wrapped", "rebasing")) and has_mint_burn:
        return "token"

    # ── Container (vault / escrow / treasury) ───────────────────────────────
    if any(k in nl for k in ("vault", "escrow", "treasury", "safe", "depositor", "silo")):
        return "container"
    if "deposit" in fn_names and ("withdraw" in fn_names or "redeem" in fn_names):
        return "container"

    # ── Exchange ─────────────────────────────────────────────────────────────
    if any(k in nl for k in ("swap", "router", "dex", "pair", "amm", "exchange",
                              "orderprocessor", "order_processor", "fulfillment",
                              "fulfillmentrouter")):
        return "exchange"
    if any(f.startswith("swap") for f in fn_names) or "requestorder" in fn_names:
        return "exchange"

    # ── Oracle ───────────────────────────────────────────────────────────────
    if any(k in nl for k in ("oracle", "pricefeed", "aggregator", "pricehelper", "rate")):
        return "oracle"
    if any(f in fn_names for f in ("getprice", "latestrounddata", "latestanswer")):
        return "oracle"

    # ── ACL / Access Control ─────────────────────────────────────────────────
    if any(k in nl for k in ("access", "ownable", "auth", "role", "acl", "restrictor",
                              "operator", "permission", "transferrestrictor")):
        return "acl"
    if any("ownable" in p or "accesscontrol" in p for p in pl):
        return "acl"

    # ── Core / Factory / Proxy ───────────────────────────────────────────────
    if any(k in nl for k in ("factory", "registry", "proxy", "deployer", "upgradeable",
                              "config", "coordinator")):
        return "core"

    # ── Minter fallback (has mint or burn, not token) ────────────────────────
    if has_mint_burn and not has_erc20:
        return "minter"

    return "other"


# ─── Description synthesis ────────────────────────────────────────────────────

def _extract_natspec(raw_before_contract: str) -> str:
    """Pull @notice or @title from the comment block that precedes a contract."""
    # Grab the last block comment or line comment cluster before the keyword
    block = re.findall(r'/\*\*(.*?)\*/', raw_before_contract, re.DOTALL)
    if block:
        text = block[-1]
        m = NATSPEC_NOTICE_RE.search(text) or NATSPEC_TITLE_RE.search(text)
        if m:
            return re.sub(r'\s+', ' ', m.group(1).replace('*', '')).strip()
    # Try line comments
    lines = re.findall(r'///\s*@notice\s+(.+)', raw_before_contract)
    if lines:
        return lines[-1].strip()
    lines = re.findall(r'///\s*@title\s+(.+)', raw_before_contract)
    if lines:
        return lines[-1].strip()
    return ""


def _synthesise_description(name: str, category: str, fn_names: set[str]) -> str:
    """Fallback description built from category + notable function names."""
    notable = sorted(f for f in fn_names
                     if f not in {"constructor", "fallback", "receive", "version",
                                  "publicversion", "initialize", "upgradeto"})[:5]
    fns_str = ", ".join(f"`{f}`" for f in notable) if notable else "various operations"
    templates = {
        "token":     f"ERC-20 token contract exposing {fns_str}.",
        "container": f"Asset container that holds funds; exposes {fns_str}.",
        "minter":    f"Manages token supply by coordinating {fns_str}.",
        "exchange":  f"Handles on-chain order flow through {fns_str}.",
        "oracle":    f"Provides price data via {fns_str}.",
        "acl":       f"Enforces access control; implements {fns_str}.",
        "core":      f"Core coordinator or factory exposing {fns_str}.",
        "other":     f"Auxiliary contract implementing {fns_str}.",
    }
    return templates.get(category, f"Contract implementing {fns_str}.")


# ─── Parser ───────────────────────────────────────────────────────────────────

def parse_protocol(name: str) -> list[ContractInfo]:
    proto_dir = DATASET_DIR / name
    if not proto_dir.exists():
        raise FileNotFoundError(f"Protocol '{name}' not found in dataset/")
    code_dir = proto_dir / "code"
    if not code_dir.exists():
        raise FileNotFoundError(f"No code/ directory for protocol '{name}'")

    contracts: list[ContractInfo] = []

    for sol_file in sorted(code_dir.rglob("*.sol")):
        if not sol_file.is_file():
            continue
        rel = sol_file.relative_to(code_dir)
        parts = rel.parts
        if any(p.lower() in SKIP_DIRS for p in parts):
            continue

        try:
            raw = sol_file.read_text("utf-8", errors="ignore")
        except OSError:
            continue

        # Collect imports (for relationship analysis) from the raw source
        import_basenames = [Path(m.group(1)).name for m in IMPORT_RE.finditer(raw)]

        clean = remove_comments(raw)

        for cm in CONTRACT_RE.finditer(clean):
            kw = cm.group("kw")
            if kw in ("interface", "library"):
                continue   # skip — we only want concrete contracts

            cname = cm.group("name")
            parents_raw = cm.group("parents") or ""
            parents = [p.strip() for p in parents_raw.split(",") if p.strip()]

            brace = clean.find('{', cm.end() - 1)
            if brace == -1:
                continue
            body = extract_block(clean, brace)

            fn_names: set[str] = set()
            for fm in FUNC_RE.finditer(body):
                rest = fm.group("rest")
                if re.search(r'\b(external|public)\b', rest):
                    fn_names.add(fm.group("name").lower())

            category = _classify(cname, parents, fn_names)

            # NatSpec: search in the original raw source before the match position
            raw_before = raw[:cm.start()]
            natspec = _extract_natspec(raw_before)
            description = natspec if natspec else _synthesise_description(cname, category, fn_names)

            contracts.append(ContractInfo(
                name=cname,
                filename=str(rel),
                category=category,
                description=description,
                functions=sorted(fn_names),
                parents=parents,
                imports=import_basenames,
                raw_source=clean,
            ))

    return contracts


# ─── Relationship inference ────────────────────────────────────────────────────

def _cap_names(names: list[str], limit: int = 4) -> str:
    """Return up to `limit` names, with '…(+N more)' if truncated."""
    if len(names) <= limit:
        return ", ".join(names)
    return ", ".join(names[:limit]) + f" … (+{len(names) - limit} more)"


def _build_relationships(contracts: list[ContractInfo]) -> str:
    """Produce a short prose paragraph describing how categories relate."""
    by_cat: dict[str, list[ContractInfo]] = defaultdict(list)
    for c in contracts:
        by_cat[c.category].append(c)

    lines: list[str] = []

    # Exchange → Token
    if "exchange" in by_cat and "token" in by_cat:
        ex = _cap_names([c.name for c in by_cat["exchange"]])
        tok = _cap_names([c.name for c in by_cat["token"]])
        lines.append(
            f"**{ex}** interacts directly with token contracts "
            f"({tok}) to transfer and settle asset balances."
        )

    # Minter → Token
    if "minter" in by_cat and "token" in by_cat:
        mn = _cap_names([c.name for c in by_cat["minter"]])
        tok = _cap_names([c.name for c in by_cat["token"]])
        lines.append(
            f"**{mn}** holds the privileged minter/burner role on "
            f"{tok}, creating and destroying supply in response to user actions."
        )

    # Exchange → Container
    if "exchange" in by_cat and "container" in by_cat:
        ex = _cap_names([c.name for c in by_cat["exchange"]])
        ct = _cap_names([c.name for c in by_cat["container"]])
        lines.append(
            f"**{ex}** routes payment funds through "
            f"{ct}, keeping collateral segregated from the routing logic."
        )

    # Exchange / Core → Oracle
    callers = by_cat.get("exchange", []) + by_cat.get("core", [])
    if callers and "oracle" in by_cat:
        cal = _cap_names([c.name for c in callers])
        oracles = _cap_names([c.name for c in by_cat["oracle"]])
        lines.append(
            f"**{cal}** consults **{oracles}** "
            f"to obtain the latest asset prices for order fulfilment and fee calculations."
        )

    # ACL → everything
    if "acl" in by_cat:
        ac = _cap_names([c.name for c in by_cat["acl"]])
        lines.append(
            f"**{ac}** enforces permissioned access across all protocol "
            f"components — only approved operators and minters may trigger privileged functions."
        )

    # Core / Factory
    if "core" in by_cat:
        core = _cap_names([c.name for c in by_cat["core"]])
        lines.append(
            f"**{core}** acts as the deployment entry point or registry, "
            f"wiring together the token, container, and exchange layers."
        )

    if not lines:
        lines.append("No cross-component relationships could be inferred automatically.")

    return "\n\n".join(lines)


# ─── Renderer ─────────────────────────────────────────────────────────────────

def render_catalogue(protocol_name: str, contracts: list[ContractInfo]) -> str:
    by_cat: dict[str, list[ContractInfo]] = defaultdict(list)
    for c in contracts:
        by_cat[c.category].append(c)

    total = len(contracts)
    sections: list[str] = [
        f"# {protocol_name} — Contract Catalogue",
        f"",
        f"> {total} contract(s) identified across "
        f"{sum(1 for k in CATEGORIES if k in by_cat)} primitive categories.",
        f"",
        "---",
        "",
    ]

    for cat in CATEGORIES:
        if cat not in by_cat:
            continue
        group = by_cat[cat]
        label = CATEGORY_LABELS[cat]
        intro = CATEGORY_INTRO[cat]
        n = len(group)

        sections.append(f"## {label}")
        sections.append(f"")
        sections.append(f"The protocol {intro}")
        sections.append(f"")

        for c in group:
            # Bold name, dash, description
            sections.append(f"- **{c.name}** – {c.description}")
            # File path as a subtle sub-note
            sections.append(f"  *File: `{c.filename}`*")
            if c.parents:
                sections.append(f"  *Inherits: {', '.join(c.parents)}*")
            if c.functions:
                fn_preview = ", ".join(f"`{f}`" for f in sorted(c.functions))
                sections.append(f"  *Key functions: {fn_preview}*")
            sections.append("")

        sections.append("")

    # Relationships
    sections.append("---")
    sections.append("")
    sections.append("## Relationships")
    sections.append("")
    sections.append(_build_relationships(contracts))
    sections.append("")

    return "\n".join(sections)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="List all contracts in a protocol, grouped by primitive type."
    )
    parser.add_argument("protocol", nargs="?", metavar="PROTOCOL",
                        help="Protocol name from dataset/ (e.g. Dinari)")
    parser.add_argument("--output", "-o", metavar="FILE",
                        help="Write output to this file (default: stdout)")
    parser.add_argument("--list", action="store_true",
                        help="List available protocols and exit")
    args = parser.parse_args()

    if args.list:
        available = sorted(
            d.name for d in DATASET_DIR.iterdir()
            if d.is_dir() and (d / "code").exists()
        )
        print(f"Available protocols ({len(available)}):")
        for p in available:
            print(f"  {p}")
        return

    if not args.protocol:
        parser.error("Provide a protocol name, e.g.:  python3 list_contracts.py Dinari")

    print(f"Analysing {args.protocol}…", file=sys.stderr)
    try:
        contracts = parse_protocol(args.protocol)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    if not contracts:
        print("No concrete contracts found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(contracts)} contract(s).", file=sys.stderr)
    catalogue = render_catalogue(args.protocol, contracts)

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(catalogue, encoding="utf-8")
        print(f"Written to {out}", file=sys.stderr)
    else:
        print(catalogue)


if __name__ == "__main__":
    main()
