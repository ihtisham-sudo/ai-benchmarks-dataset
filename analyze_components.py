#!/usr/bin/env python3
"""
Analyze protocol repos in dataset/*/code and infer presence of common protocol
building blocks. Outputs CSV, Markdown, and JSON summary reports.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from statistics import mean, median

COMPONENTS = [
    "exchanges",
    "vaults",
    "lending_market",
    "oracles",
    "bridge",
    "token",
    "governance",
    "smart_wallet",
    "timelock",
    "access_control",
]

COMPONENT_LABELS = {
    "exchanges": "Exchanges",
    "vaults": "Vaults",
    "lending_market": "Lending Market",
    "oracles": "Oracles",
    "bridge": "Bridge",
    "token": "Token",
    "governance": "Governance",
    "smart_wallet": "Smart Wallet",
    "timelock": "Timelock",
    "access_control": "Access Control",
}

SKIP_DIRS = {
    "node_modules",
    "lib",
    "forge-std",
    ".git",
    "test",
    "tests",
    "script",
    "scripts",
    "certora",
    "audits",
    "crytic",
    "dependencies",
    "vendor",
    "vendors",
    "third_party",
    "thirdparty",
    "openzeppelin",
}


def remove_comments(source: str) -> str:
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.DOTALL)
    source = re.sub(r"//[^\n]*", "", source)
    return source


def remove_string_literals(source: str) -> str:
    source = re.sub(r'"(?:[^"\\]|\\.)*"', '""', source)
    source = re.sub(r"'(?:[^'\\]|\\.)*'", "''", source)
    return source


def count_any(patterns: list[str], text: str) -> int:
    return sum(1 for pat in patterns if re.search(pat, text))


def find_all(pattern: str, text: str) -> set[str]:
    return {m.group(1).lower() for m in re.finditer(pattern, text)}


def has_token_signature(functions: set[str]) -> bool:
    required_any = {
        "totalsupply",
        "balanceof",
        "transfer",
        "approve",
        "transferfrom",
        "ownerof",
        "safetransferfrom",
    }
    return len(functions.intersection(required_any)) >= 3


def detect_components(clean_text: str) -> dict[str, bool]:
    names = find_all(r"\b(?:contract|interface|library)\s+([a-zA-Z_][\w]*)", clean_text)
    functions = find_all(r"\bfunction\s+([a-zA-Z_][\w]*)\s*\(", clean_text)

    names_blob = " ".join(sorted(names))
    funcs_blob = " ".join(sorted(functions))

    has_swap_func = any(f.startswith("swap") or f.startswith("exchange") or f.startswith("trade") for f in functions)
    has_router_name = bool(re.search(r"\b\w*(router|amm|pair|exchange|dex)\w*\b", names_blob))

    has_deposit = any(f.startswith("deposit") for f in functions)
    has_withdraw = any(f.startswith("withdraw") or f.startswith("redeem") for f in functions)
    has_share_signal = bool(
        re.search(
            r"\b(totalassets|converttoshares|converttoassets|previewdeposit|previewredeem|previewwithdraw|previewmint|exchangerate|shareprice)\b",
            funcs_blob,
        )
    )

    has_borrow = any(f.startswith("borrow") for f in functions)
    has_repay = any(f.startswith("repay") for f in functions)
    has_liquidate = any("liquidat" in f for f in functions)
    has_collateral_signal = bool(re.search(r"\b(collateral|ltv|healthfactor)\b", clean_text))

    has_oracle_name = bool(re.search(r"\b\w*(oracle|pricefeed|aggregator)\w*\b", names_blob))
    has_oracle_func = bool(
        re.search(r"\b(getprice|latestanswer|latestrounddata|peek|read|consult|setprice|updateanswer)\b", funcs_blob)
    )

    has_bridge_name = bool(re.search(r"\b\w*(bridge|messenger|gateway|portal)\w*\b", names_blob))
    has_bridge_func = bool(
        re.search(
            r"\b(sendmessage|sendcrossdomainmessage|relaymessage|receivemessage|depositeth|finalizewithdraw|finalizedeposit|withdrawto|initiatewithdrawal|bridge|bridgeto|xcall)\b",
            funcs_blob,
        )
    )
    has_xdomain_signal = bool(re.search(r"\b(xdomain|crosschain|l1|l2|chainid)\b", clean_text))

    has_token_name = bool(re.search(r"\b\w*(erc20|erc721|erc1155|ierc20|ierc721|ierc1155)\w*\b", names_blob))

    has_propose = any("propose" in f for f in functions)
    has_vote = any("vote" in f for f in functions)
    has_execute = any(f.startswith("execute") for f in functions)
    has_quorum = any("quorum" in f for f in functions)
    has_governance_name = bool(re.search(r"\b\w*(governor|governance|proposal)\w*\b", names_blob))

    has_wallet_exec_region = bool(
        re.search(
            r"\bcontract\s+\w*(wallet|multisig|signergate|smartaccount|gnosissafe)\w*"
            r"[\s\S]{0,3500}\bfunction\s+(execute|exectransaction|executetransaction)\s*\("
            r"[\s\S]{0,2500}(delegatecall\s*\(|\.call\s*\{|\.call\s*\()",
            clean_text,
        )
    )
    has_explicit_exec_tx = any(f in {"exectransaction", "executetransaction"} for f in functions)

    has_timelock_name = bool(re.search(r"\b\w*timelock\w*\b", names_blob))
    has_schedule_or_queue = bool(re.search(r"\b(schedule|queue|queuetransaction)\b", funcs_blob))
    has_delay_signal = bool(re.search(r"\b(minimumdelay|mindelay|delay|eta|timestamp)\b", clean_text))

    has_acl_signal = bool(
        re.search(r"\b(onlyowner|onlyrole|hasrole|accesscontrol|ownable|auth|authority|adminrole|pauserrole)\b", clean_text)
    )

    exchanges = has_swap_func or (has_router_name and bool(re.search(r"\bswap\w*\s*\(", clean_text)))
    vaults = (has_deposit and has_withdraw and has_share_signal) or (
        bool(re.search(r"\bvault\b", names_blob)) and has_deposit and has_withdraw
    )
    lending_market = has_borrow and (has_repay or has_liquidate or has_collateral_signal)
    oracles = (has_oracle_name and has_oracle_func) or count_any(
        [
            r"\blatestrounddata\b",
            r"\blatestanswer\b",
            r"\bgetprice\b",
            r"\bpricefeed\b",
            r"\boracle\b",
        ],
        clean_text,
    ) >= 2
    bridge = (has_bridge_name and has_bridge_func) or (has_bridge_func and has_xdomain_signal)
    token = has_token_name or has_token_signature(functions)
    governance = (has_propose and has_vote and (has_execute or has_quorum)) or (
        has_governance_name and count_any([r"\bpropose\b", r"\bvote\b", r"\bquorum\b", r"\bexecute\b"], clean_text) >= 2
    )
    smart_wallet = has_explicit_exec_tx or has_wallet_exec_region
    timelock = has_timelock_name or (has_schedule_or_queue and has_execute and has_delay_signal)
    access_control = has_acl_signal

    return {
        "exchanges": exchanges,
        "vaults": vaults,
        "lending_market": lending_market,
        "oracles": oracles,
        "bridge": bridge,
        "token": token,
        "governance": governance,
        "smart_wallet": smart_wallet,
        "timelock": timelock,
        "access_control": access_control,
    }


def load_repo_text(code_dir: Path) -> str:
    chunks: list[str] = []
    for sol_file in code_dir.rglob("*.sol"):
        if not sol_file.is_file():
            continue
        rel_parts = {p.lower() for p in sol_file.relative_to(code_dir).parts}
        if rel_parts.intersection(SKIP_DIRS):
            continue
        try:
            raw = sol_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        raw = remove_comments(raw)
        raw = remove_string_literals(raw)
        chunks.append(raw.lower())
    file_boundary = "\n" + ("#" * 10000) + "\n"
    return file_boundary.join(chunks)


def discover_repos(dataset_dir: Path) -> list[tuple[str, Path]]:
    repos: list[tuple[str, Path]] = []
    for protocol_dir in sorted(p for p in dataset_dir.iterdir() if p.is_dir()):
        code_dir = protocol_dir / "code"
        if code_dir.exists() and code_dir.is_dir():
            repos.append((protocol_dir.name, code_dir))
    return repos


def write_csv(rows: list[dict[str, object]], out_path: Path) -> None:
    fieldnames = ["repo", *COMPONENTS, "present_blocks", "present_block_names"]
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_markdown(rows: list[dict[str, object]], out_path: Path) -> None:
    lines = ["# Component Presence Per Repo", ""]
    header = ["Repo"] + [COMPONENT_LABELS[c] for c in COMPONENTS] + ["Present Blocks", "Present Names"]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "|".join(["---"] * len(header)) + "|")

    for row in rows:
        bool_cells = ["Y" if row[c] else "N" for c in COMPONENTS]
        present_names = row["present_block_names"]
        cells = [str(row["repo"]), *bool_cells, str(row["present_blocks"]), str(present_names)]
        lines.append("| " + " | ".join(cells) + " |")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_stats(rows: list[dict[str, object]]) -> dict[str, object]:
    component_counts = {c: 0 for c in COMPONENTS}
    per_repo_totals: list[int] = []

    for row in rows:
        repo_total = 0
        for comp in COMPONENTS:
            if bool(row[comp]):
                component_counts[comp] += 1
                repo_total += 1
        per_repo_totals.append(repo_total)

    total_detected = sum(per_repo_totals)
    sorted_components = sorted(component_counts.items(), key=lambda kv: kv[1], reverse=True)

    return {
        "repos_analyzed": len(rows),
        "total_detected_blocks": total_detected,
        "component_counts": component_counts,
        "most_present_components": sorted_components,
        "avg_blocks_per_repo": round(mean(per_repo_totals), 3) if per_repo_totals else 0,
        "median_blocks_per_repo": median(per_repo_totals) if per_repo_totals else 0,
        "min_blocks_per_repo": min(per_repo_totals) if per_repo_totals else 0,
        "max_blocks_per_repo": max(per_repo_totals) if per_repo_totals else 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze component presence across dataset repos")
    parser.add_argument("--dataset", type=Path, default=Path("dataset"), help="Dataset root (default: dataset)")
    parser.add_argument("--output", type=Path, default=Path("analysis"), help="Output directory (default: analysis)")
    args = parser.parse_args()

    repos = discover_repos(args.dataset)
    if not repos:
        raise SystemExit("No repos found under dataset/*/code")

    rows: list[dict[str, object]] = []
    for repo_name, code_dir in repos:
        clean_text = load_repo_text(code_dir)
        detected = detect_components(clean_text)
        present_names = [COMPONENT_LABELS[c] for c in COMPONENTS if detected[c]]
        row: dict[str, object] = {"repo": repo_name}
        row.update(detected)
        row["present_blocks"] = len(present_names)
        row["present_block_names"] = ", ".join(present_names)
        rows.append(row)

    # Determinism and structural sanity checks.
    for row in rows:
        missing = [c for c in COMPONENTS if c not in row]
        if missing:
            raise RuntimeError(f"Missing component columns for {row['repo']}: {missing}")

    stats = build_stats(rows)
    expected_total = sum(int(row["present_blocks"]) for row in rows)
    if stats["total_detected_blocks"] != expected_total:
        raise RuntimeError("Global totals do not match per-repo totals")

    args.output.mkdir(parents=True, exist_ok=True)
    csv_path = args.output / "component_presence_per_repo.csv"
    md_path = args.output / "component_presence_per_repo.md"
    json_path = args.output / "component_stats.json"

    write_csv(rows, csv_path)
    write_markdown(rows, md_path)
    json_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")

    print(f"Repos analyzed: {stats['repos_analyzed']}")
    print(f"Total detected blocks: {stats['total_detected_blocks']}")
    print(f"Top components: {stats['most_present_components'][:3]}")
    print(f"Wrote: {csv_path}")
    print(f"Wrote: {md_path}")
    print(f"Wrote: {json_path}")


if __name__ == "__main__":
    main()
