#!/usr/bin/env python3
"""
Protocol Generation Agent
=========================
Analyses 2-3 existing protocol codebases to extract patterns, then generates
a brand-new multi-contract Solidity protocol from scratch — no inheritance
from source protocols, no copied bodies.

Usage:
  python3 generate_protocol.py --protocols Aave_V3 Uniswap_V3 Telcoin
  python3 generate_protocol.py --protocols Dinari Midas --name MyStablecoin
  python3 generate_protocol.py --list
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

DATASET_DIR = Path("dataset")
DEFAULT_OUTPUT = Path("generated")

SKIP_DIRS = {
    "node_modules", "lib", "forge-std", ".git",
    "test", "tests", "script", "scripts",
    "certora", "audits", "crytic", "dependencies",
    "vendor", "vendors", "third_party", "thirdparty",
    "openzeppelin",
}

# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------

def remove_comments(src: str) -> str:
    src = re.sub(r'/\*.*?\*/', '', src, flags=re.DOTALL)
    src = re.sub(r'//[^\n]*', '', src)
    return src

def remove_strings(src: str) -> str:
    src = re.sub(r'"(?:[^"\\]|\\.)*"', '""', src)
    src = re.sub(r"'(?:[^'\\]|\\.)*'", "''", src)
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

# ---------------------------------------------------------------------------
# Stage 1 — Pattern Extractor
# ---------------------------------------------------------------------------

@dataclass
class FuncPattern:
    name: str
    params: str          # raw param string
    returns: str         # raw returns string
    visibility: str
    mutability: str      # view / pure / payable / ""
    modifiers: list[str]

@dataclass
class StateVarPattern:
    sol_type: str
    name: str
    visibility: str

@dataclass
class ComponentPattern:
    """Extracted patterns for a single detected component type."""
    kind: str                               # token | lending | exchange | oracle | acl | vault | …
    functions: list[FuncPattern] = field(default_factory=list)
    state_vars: list[StateVarPattern] = field(default_factory=list)
    events: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    source_protocol: str = ""

@dataclass
class ProtocolAnalysis:
    name: str
    components: dict[str, ComponentPattern] = field(default_factory=dict)   # kind -> pattern
    detected_flags: dict[str, bool] = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)

# --- regex patterns for extraction ---

CONTRACT_RE = re.compile(
    r'(?:abstract\s+)?(?P<kind>contract|library|interface)\s+(?P<name>\w+)'
    r'(?:\s+is\s+(?P<parents>[\w\s,]+?))?\s*\{',
    re.MULTILINE
)

FUNC_RE = re.compile(
    r'\bfunction\s+(?P<name>\w+)\s*\((?P<params>[^)]*)\)\s*(?P<rest>[^{;]*)',
    re.MULTILINE
)

STATEVAR_RE = re.compile(
    r'^\s*(?P<type>(?:mapping\s*\([^)]+\)|address|uint\w*|int\w*|bool|bytes\w*|string)'
    r'(?:\[\d*\])*)\s+'
    r'(?:public\s+|private\s+|internal\s+|constant\s+|immutable\s+)*'
    r'(?P<name>[a-z_]\w*)\s*[=;]',
    re.MULTILINE
)

EVENT_RE    = re.compile(r'\bevent\s+(\w+)\s*\(([^)]*)\)', re.MULTILINE)
ERROR_RE    = re.compile(r'\berror\s+(\w+)\s*\(([^)]*)\)', re.MULTILINE)
MODIFIER_RE = re.compile(r'\bmodifier\s+(\w+)', re.MULTILINE)


def _parse_func(m: re.Match) -> FuncPattern:
    rest = m.group("rest")
    vis = next((v for v in ("external","public","internal","private") if re.search(rf'\b{v}\b', rest)), "public")
    mut = next((v for v in ("view","pure","payable") if re.search(rf'\b{v}\b', rest)), "")
    mods = [w for w in re.findall(r'\b(\w+)\b', rest)
            if w not in {"external","public","internal","private","view","pure","payable",
                         "virtual","override","returns","memory","calldata","storage"}
            and not w[0].isupper()]
    rets_m = re.search(r'\breturns\s*\(([^)]*)\)', rest)
    rets = rets_m.group(1).strip() if rets_m else ""
    return FuncPattern(
        name=m.group("name"), params=m.group("params").strip(),
        returns=rets, visibility=vis, mutability=mut, modifiers=mods
    )


def _classify_contract(name: str, parents: list[str], funcs: list[FuncPattern], flags: dict) -> Optional[str]:
    nl = name.lower()
    fn_names = {f.name.lower() for f in funcs}

    if any(k in nl for k in ("token","erc20","erc721","coin","stable")) or \
       len({"totalsupply","balanceof","transfer","approve"} & fn_names) >= 3:
        return "token"
    if any(k in nl for k in ("lending","borrow","pool","market")) or \
       any(f in fn_names for f in ("borrow","repay","liquidate","getreservesdata")):
        return "lending"
    if any(k in nl for k in ("swap","router","exchange","dex","pair","amm")) or \
       any(f.startswith("swap") for f in fn_names):
        return "exchange"
    if any(k in nl for k in ("oracle","pricefeed","aggregator")) or \
       any(f in fn_names for f in ("getprice","latestrounddata","latestanswer")):
        return "oracle"
    if any(k in nl for k in ("vault","yield","strategy","depositor")) or \
       ("deposit" in fn_names and ("withdraw" in fn_names or "redeem" in fn_names)):
        return "vault"
    if any(k in nl for k in ("gov","proposal","vote")) or \
       ("propose" in fn_names and "vote" in fn_names):
        return "governance"
    if any(k in nl for k in ("timelock","scheduler")) or \
       ("schedule" in fn_names and "execute" in fn_names):
        return "timelock"
    if any(k in nl for k in ("bridge","gateway","messenger","portal")):
        return "bridge"
    if any(k in nl for k in ("access","ownable","auth","role","permission","acl")):
        return "acl"
    # parents hint
    for p in parents:
        pl = p.lower()
        if "acl" in pl or "ownable" in pl or "access" in pl:
            return "acl"
        if "erc20" in pl or "erc721" in pl:
            return "token"
    return None


def _detect_flags(text_low: str) -> dict[str, bool]:
    fn = set(re.findall(r'\bfunction\s+(\w+)\s*\(', text_low))
    nm = set(re.findall(r'\b(?:contract|interface|library)\s+(\w+)', text_low))
    return {
        "token":         len({"totalsupply","balanceof","transfer","approve"} & fn) >= 3,
        "lending":       "borrow" in fn and ("repay" in fn or "liquidat" in text_low),
        "exchange":      any(f.startswith("swap") for f in fn),
        "oracle":        "latestrounddata" in fn or "getprice" in fn,
        "vault":         "deposit" in fn and ("withdraw" in fn or "redeem" in fn),
        "governance":    "propose" in fn and "vote" in fn,
        "timelock":      any("timelock" in n for n in nm),
        "bridge":        any("bridge" in n for n in nm),
        "acl":           bool(re.search(r'\b(onlyowner|onlyrole|accesscontrol|ownable)\b', text_low)),
    }


def analyse_protocol(name: str) -> ProtocolAnalysis:
    proto_dir = DATASET_DIR / name
    if not proto_dir.exists():
        raise FileNotFoundError(f"Protocol '{name}' not found in dataset/")
    code_dir = proto_dir / "code"
    if not code_dir.exists():
        raise FileNotFoundError(f"No code/ directory for '{name}'")

    analysis = ProtocolAnalysis(name=name)
    meta_path = proto_dir / "metadata.json"
    if meta_path.exists():
        analysis.metadata = json.loads(meta_path.read_text("utf-8"))

    all_text = []

    for sol_file in sorted(code_dir.rglob("*.sol")):
        if not sol_file.is_file(): continue
        rel = sol_file.relative_to(code_dir).parts
        if any(p.lower() in SKIP_DIRS for p in rel): continue
        try:
            raw = sol_file.read_text("utf-8", errors="ignore")
        except OSError:
            continue

        clean = remove_comments(raw)
        all_text.append(clean.lower())

        for cm in CONTRACT_RE.finditer(clean):
            kind_kw = cm.group("kind")
            if kind_kw in ("interface", "library"):
                continue
            cname = cm.group("name")
            parents = [p.strip() for p in (cm.group("parents") or "").split(",") if p.strip()]

            brace = clean.find('{', cm.end() - 1)
            if brace == -1: continue
            body = extract_block(clean, brace)

            funcs = [_parse_func(m) for m in FUNC_RE.finditer(body)]
            s_vars = [
                StateVarPattern(sol_type=m.group("type"), name=m.group("name"),
                                visibility="public" if "public" in m.group(0) else "internal")
                for m in STATEVAR_RE.finditer(body)
            ]
            events = [f"{m.group(1)}({m.group(2)})" for m in EVENT_RE.finditer(body)]
            errors = [f"{m.group(1)}({m.group(2)})" for m in ERROR_RE.finditer(body)]

            comp_kind = _classify_contract(cname, parents, funcs, {})
            if comp_kind is None:
                continue   # skip unclassifiable contracts

            if comp_kind not in analysis.components:
                analysis.components[comp_kind] = ComponentPattern(
                    kind=comp_kind, source_protocol=name
                )
            cp = analysis.components[comp_kind]
            # Merge patterns — deduplicate function names
            existing_fn = {f.name for f in cp.functions}
            for f in funcs:
                if f.name not in existing_fn and f.visibility in ("external", "public"):
                    cp.functions.append(f)
                    existing_fn.add(f.name)
            existing_sv = {v.name for v in cp.state_vars}
            for sv in s_vars:
                if sv.name not in existing_sv:
                    cp.state_vars.append(sv)
                    existing_sv.add(sv.name)
            cp.events.extend(e for e in events if e not in cp.events)
            cp.errors.extend(e for e in errors if e not in cp.errors)

    full_low = "\n".join(all_text)
    analysis.detected_flags = _detect_flags(full_low)
    return analysis


# ---------------------------------------------------------------------------
# Stage 2 — Architect
# ---------------------------------------------------------------------------

@dataclass
class ContractSpec:
    filename: str
    contract_name: str
    kind: str                        # which component type
    state_vars: list[StateVarPattern]
    functions: list[FuncPattern]
    events: list[str]
    errors: list[str]
    natspec: str
    source_protocols: list[str]

def _merge_analyses(analyses: list[ProtocolAnalysis]) -> dict[str, ComponentPattern]:
    """Merge component patterns across all source protocols."""
    merged: dict[str, ComponentPattern] = {}
    for ana in analyses:
        for kind, cp in ana.components.items():
            if kind not in merged:
                merged[kind] = ComponentPattern(kind=kind, source_protocol=ana.name)
                merged[kind].functions = list(cp.functions)
                merged[kind].state_vars = list(cp.state_vars)
                merged[kind].events = list(cp.events)
                merged[kind].errors = list(cp.errors)
            else:
                existing_fn = {f.name for f in merged[kind].functions}
                for f in cp.functions:
                    if f.name not in existing_fn:
                        merged[kind].functions.append(f)
                        existing_fn.add(f.name)
                existing_sv = {v.name for v in merged[kind].state_vars}
                for sv in cp.state_vars:
                    if sv.name not in existing_sv:
                        merged[kind].state_vars.append(sv)
                        existing_sv.add(sv.name)
    return merged


def design_architecture(protocol_name: str, analyses: list[ProtocolAnalysis]) -> list[ContractSpec]:
    """Decide which contracts to generate and what goes in each."""
    merged = _merge_analyses(analyses)
    all_flags: set[str] = set()
    for ana in analyses:
        for k, v in ana.detected_flags.items():
            if v: all_flags.add(k)

    source_names = [a.name for a in analyses]
    specs: list[ContractSpec] = []

    # Always emit an errors + events library
    specs.append(_make_lib_spec(protocol_name, merged, source_names))

    # ACL contract (always useful)
    specs.append(_make_acl_spec(protocol_name, merged.get("acl"), source_names))

    # Component contracts based on detected flags
    kind_order = ["token", "vault", "lending", "exchange", "oracle", "governance", "timelock", "bridge"]
    for kind in kind_order:
        if kind in merged and kind in all_flags:
            specs.append(_make_component_spec(protocol_name, kind, merged[kind], source_names))

    # Core controller
    specs.append(_make_core_spec(protocol_name, specs, source_names))

    return specs


def _canon_type(t: str) -> str:
    """Normalise weird extracted types to clean Solidity."""
    t = t.strip()
    if re.match(r'^uint\d*$', t) or re.match(r'^int\d*$', t): return t
    if t in ("address", "bool", "bytes32", "bytes", "string"): return t
    if re.match(r'^mapping', t): return t
    if re.match(r'^bytes\d+$', t): return t
    return t if re.match(r'^\w[\w\[\]\.]*$', t) else "uint256"


def _make_lib_spec(proto_name: str, merged: dict, sources: list[str]) -> ContractSpec:
    events: list[str] = []
    errors: list[str] = []
    seen_e: set[str] = set()
    seen_err: set[str] = set()
    for cp in merged.values():
        for e in cp.events:
            n = e.split("(")[0]
            if n not in seen_e:
                seen_e.add(n); events.append(e)
        for e in cp.errors:
            n = e.split("(")[0]
            if n not in seen_err:
                seen_err.add(n); errors.append(e)
    return ContractSpec(
        filename=f"Events.sol", contract_name=f"{proto_name}Events",
        kind="library",
        state_vars=[], functions=[], events=events[:30], errors=errors[:20],
        natspec=f"@title {proto_name} — shared events and errors",
        source_protocols=sources,
    )


def _make_acl_spec(proto_name: str, cp: Optional[ComponentPattern], sources: list[str]) -> ContractSpec:
    base_vars = [
        StateVarPattern("address", "owner", "public"),
        StateVarPattern("mapping(address => mapping(bytes32 => bool))", "roles", "internal"),
        StateVarPattern("mapping(bytes32 => bytes32)", "roleAdmin", "internal"),
    ]
    base_fns = [
        FuncPattern("initialize", "address _owner", "", "public", "", []),
        FuncPattern("grantRole", "bytes32 role, address account", "", "external", "", ["onlyRole"]),
        FuncPattern("revokeRole", "bytes32 role, address account", "", "external", "", ["onlyRole"]),
        FuncPattern("hasRole", "bytes32 role, address account", "bool", "public", "view", []),
        FuncPattern("transferOwnership", "address newOwner", "", "external", "", ["onlyOwner"]),
    ]
    extra_fns: list[FuncPattern] = []
    if cp:
        seen = {f.name for f in base_fns}
        for f in cp.functions:
            if f.name not in seen and f.visibility in ("external","public"):
                extra_fns.append(f); seen.add(f.name)
    return ContractSpec(
        filename="AccessControl.sol", contract_name=f"{proto_name}AccessControl",
        kind="acl",
        state_vars=base_vars,
        functions=base_fns + extra_fns[:10],
        events=["RoleGranted(bytes32 indexed role, address indexed account, address indexed sender)",
                "RoleRevoked(bytes32 indexed role, address indexed account, address indexed sender)",
                "OwnershipTransferred(address indexed previousOwner, address indexed newOwner)"],
        errors=["Unauthorized()", "ZeroAddress()", "AlreadyHasRole(bytes32 role, address account)"],
        natspec=f"@title {proto_name} — role-based access control",
        source_protocols=sources,
    )


_KIND_META = {
    "token": {
        "filename": "Token.sol",
        "suffix": "Token",
        "natspec": "ERC-20 compatible token",
        "base_vars": [
            StateVarPattern("string","name","public"),
            StateVarPattern("string","symbol","public"),
            StateVarPattern("uint8","decimals","public"),
            StateVarPattern("uint256","totalSupply","public"),
            StateVarPattern("mapping(address => uint256)","balanceOf","public"),
            StateVarPattern("mapping(address => mapping(address => uint256))","allowance","public"),
        ],
        "base_fns": [
            FuncPattern("transfer","address to, uint256 amount","bool","external","",""),
            FuncPattern("transferFrom","address from, address to, uint256 amount","bool","external","",""),
            FuncPattern("approve","address spender, uint256 amount","bool","external","",""),
            FuncPattern("mint","address to, uint256 amount","","external","",["onlyRole"]),
            FuncPattern("burn","address from, uint256 amount","","external","",["onlyRole"]),
        ],
        "base_events": ["Transfer(address indexed from, address indexed to, uint256 amount)",
                        "Approval(address indexed owner, address indexed spender, uint256 amount)"],
        "base_errors": ["InsufficientBalance()", "InsufficientAllowance()", "TransferToZeroAddress()"],
    },
    "vault": {
        "filename": "Vault.sol",
        "suffix": "Vault",
        "natspec": "ERC-4626 inspired yield vault",
        "base_vars": [
            StateVarPattern("address","asset","public"),
            StateVarPattern("uint256","totalAssets","public"),
            StateVarPattern("uint256","totalShares","public"),
            StateVarPattern("mapping(address => uint256)","shares","public"),
        ],
        "base_fns": [
            FuncPattern("deposit","uint256 assets, address receiver","uint256 shares","external","",""),
            FuncPattern("withdraw","uint256 assets, address receiver, address owner","uint256 shares","external","",""),
            FuncPattern("redeem","uint256 shares, address receiver, address owner","uint256 assets","external","",""),
            FuncPattern("previewDeposit","uint256 assets","uint256","external","view",""),
            FuncPattern("previewWithdraw","uint256 assets","uint256","external","view",""),
            FuncPattern("convertToShares","uint256 assets","uint256","public","view",""),
            FuncPattern("convertToAssets","uint256 shares","uint256","public","view",""),
        ],
        "base_events": ["Deposit(address indexed caller, address indexed owner, uint256 assets, uint256 shares)",
                        "Withdraw(address indexed caller, address indexed receiver, address indexed owner, uint256 assets, uint256 shares)"],
        "base_errors": ["InsufficientAssets()", "ExceedsMaxDeposit()", "ZeroShares()"],
    },
    "lending": {
        "filename": "LendingPool.sol",
        "suffix": "LendingPool",
        "natspec": "Collateralised lending and borrowing pool",
        "base_vars": [
            StateVarPattern("address","oracle","public"),
            StateVarPattern("mapping(address => uint256)","collateral","public"),
            StateVarPattern("mapping(address => uint256)","debt","public"),
            StateVarPattern("uint256","liquidationThreshold","public"),
            StateVarPattern("uint256","interestRatePerSecond","public"),
        ],
        "base_fns": [
            FuncPattern("supplyCollateral","address asset, uint256 amount","","external","",""),
            FuncPattern("withdrawCollateral","address asset, uint256 amount","","external","",""),
            FuncPattern("borrow","address asset, uint256 amount","","external","",""),
            FuncPattern("repay","address asset, uint256 amount","","external","",""),
            FuncPattern("liquidate","address borrower, address asset, uint256 debtAmount","","external","",""),
            FuncPattern("getHealthFactor","address user","uint256","external","view",""),
            FuncPattern("setInterestRate","uint256 newRate","","external","",["onlyRole"]),
        ],
        "base_events": ["Borrowed(address indexed user, address indexed asset, uint256 amount)",
                        "Repaid(address indexed user, address indexed asset, uint256 amount)",
                        "Liquidated(address indexed borrower, address indexed liquidator, uint256 amount)"],
        "base_errors": ["InsufficientCollateral()", "HealthyPosition()", "UnauthorizedLiquidation()"],
    },
    "exchange": {
        "filename": "SwapRouter.sol",
        "suffix": "SwapRouter",
        "natspec": "Token swap router",
        "base_vars": [
            StateVarPattern("address","factory","public"),
            StateVarPattern("address","weth","public"),
            StateVarPattern("uint256","feeNumerator","public"),
            StateVarPattern("uint256","feeDenominator","public"),
        ],
        "base_fns": [
            FuncPattern("swapExactTokensForTokens","uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to","uint256 amountOut","external","",""),
            FuncPattern("swapTokensForExactTokens","uint256 amountOut, uint256 amountInMax, address[] calldata path, address to","uint256 amountIn","external","",""),
            FuncPattern("swapExactETHForTokens","uint256 amountOutMin, address[] calldata path, address to","uint256 amountOut","external","payable",""),
            FuncPattern("getAmountOut","uint256 amountIn, uint256 reserveIn, uint256 reserveOut","uint256","public","pure",""),
            FuncPattern("getAmountsOut","uint256 amountIn, address[] calldata path","uint256[] memory","external","view",""),
            FuncPattern("setFee","uint256 numerator, uint256 denominator","","external","",["onlyRole"]),
        ],
        "base_events": ["Swap(address indexed sender, uint256 amountIn, uint256 amountOut, address indexed tokenIn, address indexed tokenOut)"],
        "base_errors": ["InsufficientOutputAmount()", "ExcessiveInputAmount()", "InvalidPath()"],
    },
    "oracle": {
        "filename": "PriceOracle.sol",
        "suffix": "Oracle",
        "natspec": "On-chain price oracle with staleness check",
        "base_vars": [
            StateVarPattern("mapping(address => address)","feeds","public"),
            StateVarPattern("uint256","stalenessThreshold","public"),
        ],
        "base_fns": [
            FuncPattern("getPrice","address token","uint256 price","external","view",""),
            FuncPattern("setFeed","address token, address feed","","external","",["onlyRole"]),
            FuncPattern("removeFeed","address token","","external","",["onlyRole"]),
            FuncPattern("getPriceInETH","address token","uint256","external","view",""),
        ],
        "base_events": ["FeedSet(address indexed token, address indexed feed)",
                        "FeedRemoved(address indexed token)"],
        "base_errors": ["StalePriceFeed()", "NoFeedSet(address token)", "InvalidPrice()"],
    },
    "governance": {
        "filename": "Governance.sol",
        "suffix": "Governance",
        "natspec": "On-chain proposal-based governance",
        "base_vars": [
            StateVarPattern("uint256","proposalCount","public"),
            StateVarPattern("uint256","votingDelay","public"),
            StateVarPattern("uint256","votingPeriod","public"),
            StateVarPattern("uint256","quorumNumerator","public"),
            StateVarPattern("mapping(uint256 => Proposal)","proposals","public"),
        ],
        "base_fns": [
            FuncPattern("propose","address[] calldata targets, uint256[] calldata values, bytes[] calldata calldatas, string calldata description","uint256 proposalId","external","",""),
            FuncPattern("castVote","uint256 proposalId, uint8 support","","external","",""),
            FuncPattern("execute","uint256 proposalId","","external","",""),
            FuncPattern("cancel","uint256 proposalId","","external","",""),
            FuncPattern("state","uint256 proposalId","uint8","external","view",""),
            FuncPattern("quorum","uint256 blockNumber","uint256","external","view",""),
        ],
        "base_events": ["ProposalCreated(uint256 proposalId, address proposer, string description)",
                        "VoteCast(address indexed voter, uint256 proposalId, uint8 support, uint256 weight)",
                        "ProposalExecuted(uint256 indexed proposalId)"],
        "base_errors": ["ProposalNotFound()", "AlreadyVoted()", "VotingClosed()", "QuorumNotReached()"],
    },
    "timelock": {
        "filename": "Timelock.sol",
        "suffix": "Timelock",
        "natspec": "Time-delayed operation executor",
        "base_vars": [
            StateVarPattern("uint256","minDelay","public"),
            StateVarPattern("mapping(bytes32 => bool)","pendingOperations","public"),
        ],
        "base_fns": [
            FuncPattern("schedule","address target, uint256 value, bytes calldata data, bytes32 salt, uint256 delay","bytes32 id","external","",["onlyRole"]),
            FuncPattern("execute","address target, uint256 value, bytes calldata data, bytes32 salt","","external","payable",""),
            FuncPattern("cancel","bytes32 id","","external","",["onlyRole"]),
            FuncPattern("isOperationPending","bytes32 id","bool","external","view",""),
            FuncPattern("updateMinDelay","uint256 newDelay","","external","",["onlyRole"]),
        ],
        "base_events": ["OperationScheduled(bytes32 indexed id, address target, uint256 delay)",
                        "OperationExecuted(bytes32 indexed id)",
                        "OperationCancelled(bytes32 indexed id)"],
        "base_errors": ["OperationNotReady()", "OperationAlreadyExists()", "MinDelayNotMet()"],
    },
    "bridge": {
        "filename": "Bridge.sol",
        "suffix": "Bridge",
        "natspec": "Cross-chain token bridge",
        "base_vars": [
            StateVarPattern("uint256","chainId","public"),
            StateVarPattern("mapping(bytes32 => bool)","processedMessages","public"),
            StateVarPattern("address","messenger","public"),
        ],
        "base_fns": [
            FuncPattern("bridgeTo","address token, uint256 amount, uint256 targetChainId, address recipient","bytes32 messageId","external","",""),
            FuncPattern("receiveMessage","bytes calldata message, bytes calldata proof","","external","",["onlyRole"]),
            FuncPattern("setMessenger","address newMessenger","","external","",["onlyRole"]),
        ],
        "base_events": ["MessageSent(bytes32 indexed messageId, address indexed sender, uint256 targetChainId)",
                        "MessageReceived(bytes32 indexed messageId, address indexed recipient)"],
        "base_errors": ["MessageAlreadyProcessed()", "InvalidProof()", "UnsupportedChain()"],
    },
}


def _make_component_spec(proto_name: str, kind: str, cp: ComponentPattern, sources: list[str]) -> ContractSpec:
    meta = _KIND_META.get(kind, {})
    suffix = meta.get("suffix", kind.title())
    base_vars: list[StateVarPattern] = list(meta.get("base_vars", []))
    base_fns: list[FuncPattern] = list(meta.get("base_fns", []))
    base_events: list[str] = list(meta.get("base_events", []))
    base_errors: list[str] = list(meta.get("base_errors", []))

    # Fold in extra unique patterns from the analysis
    seen_fn = {f.name for f in base_fns}
    extra_fns: list[FuncPattern] = []
    for f in cp.functions:
        if f.name not in seen_fn and f.visibility in ("external", "public") and f.mutability != "pure":
            extra_fns.append(f)
            seen_fn.add(f.name)

    seen_sv = {v.name for v in base_vars}
    extra_vars: list[StateVarPattern] = []
    for sv in cp.state_vars:
        if sv.name not in seen_sv:
            extra_vars.append(sv)
            seen_sv.add(sv.name)

    return ContractSpec(
        filename=meta.get("filename", f"{suffix}.sol"),
        contract_name=f"{proto_name}{suffix}",
        kind=kind,
        state_vars=base_vars + extra_vars[:8],
        functions=base_fns + extra_fns[:12],
        events=base_events,
        errors=base_errors,
        natspec=f"@title {proto_name} — {meta.get('natspec', kind)}",
        source_protocols=sources,
    )


def _make_core_spec(proto_name: str, specs: list[ContractSpec], sources: list[str]) -> ContractSpec:
    """Central coordinator contract that wires everything together."""
    refs = [s.contract_name for s in specs if s.kind not in ("library",)]
    init_params = ", ".join(f"address _{r[len(proto_name):].lower()}" for r in refs)
    init_body_vars = "\n        ".join(
        f"{r[len(proto_name):].lower()} = {r}(_{r[len(proto_name):].lower()});"
        for r in refs
    )
    fns = [FuncPattern(
        name="initialize",
        params=init_params,
        returns="",
        visibility="external",
        mutability="",
        modifiers=[],
    )]
    state_vars = [
        StateVarPattern(cn, cn[len(proto_name):].lower(), "public")
        for cn in refs
    ]
    return ContractSpec(
        filename=f"{proto_name}.sol",
        contract_name=proto_name,
        kind="core",
        state_vars=state_vars,
        functions=fns,
        events=["Initialized(address indexed initializer)"],
        errors=["AlreadyInitialized()", "NotInitialized()"],
        natspec=f"@title {proto_name} — protocol core coordinator\n * @notice Synthesised from: {', '.join(sources)}",
        source_protocols=sources,
    )


# ---------------------------------------------------------------------------
# Stage 3 — Code Generator
# ---------------------------------------------------------------------------

SPDX = "// SPDX-License-Identifier: MIT"
PRAGMA = "pragma solidity ^0.8.20;"

def _fn_stub(f: FuncPattern, indent: str = "    ") -> str:
    mods_raw = f.modifiers if isinstance(f.modifiers, list) else (f.modifiers or "").split()
    clean_mods = [
        m for m in mods_raw
        if m and m not in {"external","public","internal","private","view","pure","payable",
                           "virtual","override","returns","memory","calldata","storage",
                           "address","string","bool","initializer","reinitializer"}
        and not re.match(r'^u?int\d*$', m)
        and not re.match(r'^bytes\d*$', m)
    ]

    sig = f"function {f.name}({f.params})"
    if f.visibility and f.visibility not in ("internal", "private"):
        sig += f" {f.visibility}"
    if f.mutability:
        sig += f" {f.mutability}"
    for m in clean_mods:
        sig += f" {m}"
    if f.returns:
        sig += f" returns ({f.returns})"
    if f.mutability in ("view", "pure"):
        if f.returns:
            ret_type = f.returns.split(",")[0].strip().split()[-1]
            default = _default_value(ret_type)
            body = f"return {default};"
        else:
            body = "// view: no side effects"
    elif f.name == "initialize":
        body = "// TODO: set module references\n        emit Initialized(msg.sender);"
    elif f.name in ("grantRole", "revokeRole"):
        action = "true" if f.name == "grantRole" else "false"
        body = f"roles[account][role] = {action};\n        emit Role{'Granted' if action=='true' else 'Revoked'}(role, account, msg.sender);"
    elif f.name == "transferOwnership":
        body = "emit OwnershipTransferred(owner, newOwner);\n        owner = newOwner;"
    elif f.name == "hasRole":
        body = "return roles[account][role];"
    elif f.name in ("transfer", "transferFrom"):
        body = "// TODO: balance accounting\n        return true;"
    elif f.name in ("approve",):
        body = "allowance[msg.sender][spender] = amount;\n        emit Approval(msg.sender, spender, amount);\n        return true;"
    elif f.name == "deposit":
        body = "// TODO: convert assets to shares\n        emit Deposit(msg.sender, receiver, assets, 0);\n        return 0;"
    elif f.name in ("withdraw", "redeem"):
        body = "// TODO: convert shares to assets\n        return 0;"
    elif f.name in ("borrow",):
        body = "// TODO: check collateral, update debt\n        emit Borrowed(msg.sender, asset, amount);"
    elif f.name == "liquidate":
        body = "// TODO: verify health factor, seize collateral\n        emit Liquidated(borrower, msg.sender, debtAmount);"
    elif f.name.startswith("swap"):
        body = "// TODO: compute amounts via AMM formula\n        emit Swap(msg.sender, 0, 0, path[0], path[path.length-1]);\n        return 0;"
    elif f.name == "propose":
        body = "proposalCount++;\n        emit ProposalCreated(proposalCount, msg.sender, description);\n        return proposalCount;"
    elif f.name == "castVote":
        body = "emit VoteCast(msg.sender, proposalId, support, 0);"
    elif f.name == "schedule":
        body = "bytes32 id = keccak256(abi.encode(target, value, data, salt));\n        require(!pendingOperations[id], 'exists');\n        require(delay >= minDelay, 'delay too short');\n        pendingOperations[id] = true;\n        emit OperationScheduled(id, target, delay);\n        return id;"
    elif f.name == "execute" and "delta" not in f.params:
        body = "// TODO: validate and execute scheduled operation"
    else:
        body = "// TODO: implement"

    lines = [f"{indent}{sig} {{"]
    for bl in body.splitlines():
        lines.append(f"{indent}    {bl.strip()}")
    lines.append(f"{indent}}}")
    return "\n".join(lines)


def _default_value(t: str) -> str:
    t = t.strip()
    if t in ("bool",): return "false"
    if t.startswith("address"): return "address(0)"
    if t.startswith("bytes"): return "bytes32(0)" if t == "bytes32" else '""'
    if t.startswith("string"): return '""'
    if "[]" in t: return "new uint256[](0)"
    return "0"


def _render_modifier(name: str) -> str:
    if name == "onlyOwner":
        return '    modifier onlyOwner() {\n        require(msg.sender == owner, "Not owner");\n        _;\n    }'
    if name == "onlyRole":
        return '    modifier onlyRole(bytes32 role) {\n        require(hasRole(role, msg.sender), "Missing role");\n        _;\n    }'
    if name == "nonReentrant":
        return '    uint256 private _status;\n    modifier nonReentrant() {\n        require(_status != 2, "Reentrant call");\n        _status = 2;\n        _;\n        _status = 1;\n    }'
    return f'    modifier {name}() {{\n        _;\n    }}'


def render_spec(spec: ContractSpec) -> str:
    lines: list[str] = [
        SPDX,
        PRAGMA,
        "",
        f"/**",
        f" * {spec.natspec}",
        f" * @dev Synthesised from: {', '.join(spec.source_protocols)}",
        f" */",
    ]

    is_lib = spec.kind == "library"
    kw = "library" if is_lib else "contract"
    lines.append(f"{kw} {spec.contract_name} {{")
    lines.append("")

    # Events block
    if spec.events:
        lines.append("    // ── Events ─────────────────────────────────────────────────────")
        for ev in spec.events:
            lines.append(f"    event {ev};")
        lines.append("")

    # Errors block
    if spec.errors:
        lines.append("    // ── Errors ─────────────────────────────────────────────────────")
        for er in spec.errors:
            lines.append(f"    error {er};")
        lines.append("")

    if is_lib:
        lines.append("}")
        return "\n".join(lines)

    # State vars
    if spec.state_vars:
        lines.append("    // ── State ──────────────────────────────────────────────────────")
        for sv in spec.state_vars:
            t = _canon_type(sv.sol_type)
            lines.append(f"    {t} public {sv.name};")
        lines.append("")

    # Modifiers (collect from functions)
    _INVALID_MODS = {
        "", "virtual", "override", "returns", "memory", "calldata", "storage",
        "address", "string", "bool", "initializer", "reinitializer",
        "external", "public", "internal", "private", "view", "pure", "payable",
    }
    needed_mods: set[str] = set()
    for f in spec.functions:
        mods_raw = f.modifiers if isinstance(f.modifiers, list) else (f.modifiers or "").split()
        for m in mods_raw:
            m = m.strip()
            if m and m not in _INVALID_MODS \
               and not re.match(r'^u?int\d*$', m) \
               and not re.match(r'^bytes\d*$', m):
                needed_mods.add(m)

    if needed_mods:
        lines.append("    // ── Modifiers ──────────────────────────────────────────────────")
        for mod in sorted(needed_mods):
            lines.append(_render_modifier(mod))
        lines.append("")

    # Functions
    if spec.functions:
        lines.append("    // ── Functions ──────────────────────────────────────────────────")
        for f in spec.functions:
            lines.append(_fn_stub(f))
            lines.append("")

    lines.append("}")
    return "\n".join(lines)


def render_interface(spec: ContractSpec) -> str:
    """Generate a clean interface for any non-library contract."""
    lines = [
        SPDX, PRAGMA, "",
        f"interface I{spec.contract_name} {{",
        "",
    ]
    if spec.events:
        for ev in spec.events:
            lines.append(f"    event {ev};")
        lines.append("")
    if spec.errors:
        for er in spec.errors:
            lines.append(f"    error {er};")
        lines.append("")
    for f in spec.functions:
        if f.visibility not in ("external", "public"):
            continue
        sig = f"function {f.name}({f.params}) external"
        if f.mutability: sig += f" {f.mutability}"
        if f.returns: sig += f" returns ({f.returns})"
        lines.append(f"    {sig};")
    lines.append("}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Output writer
# ---------------------------------------------------------------------------

def write_generated(
    out_dir: Path,
    specs: list[ContractSpec],
    analyses: list[ProtocolAnalysis],
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    src_dir = out_dir / "src"
    iface_dir = src_dir / "interfaces"
    src_dir.mkdir(exist_ok=True)
    iface_dir.mkdir(exist_ok=True)

    for spec in specs:
        sol = render_spec(spec)
        dest = src_dir / spec.filename
        dest.write_text(sol, encoding="utf-8")
        print(f"  ✓ src/{spec.filename}")

        if spec.kind not in ("library",):
            iface = render_interface(spec)
            iface_dest = iface_dir / f"I{spec.filename}"
            iface_dest.write_text(iface, encoding="utf-8")
            print(f"  ✓ src/interfaces/I{spec.filename}")

    # manifest
    all_flags: dict[str, list[str]] = defaultdict(list)
    for ana in analyses:
        for k, v in ana.detected_flags.items():
            if v: all_flags[k].append(ana.name)

    manifest = {
        "source_protocols": [a.name for a in analyses],
        "detected_components": dict(all_flags),
        "generated_contracts": [
            {
                "file": s.filename,
                "contract": s.contract_name,
                "kind": s.kind,
                "functions": len(s.functions),
                "state_vars": len(s.state_vars),
            }
            for s in specs
        ],
        "stats": {
            "total_contracts": len(specs),
            "total_functions": sum(len(s.functions) for s in specs),
            "total_state_vars": sum(len(s.state_vars) for s in specs),
        },
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"  ✓ manifest.json")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Protocol Generation Agent — analyse 2-3 protocols, generate a new one from scratch"
    )
    parser.add_argument("--protocols", nargs="+", metavar="PROTOCOL",
                        help="Protocol names from dataset/ (2 or 3)")
    parser.add_argument("--name", default=None,
                        help="Name for the generated protocol (PascalCase)")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT,
                        help=f"Root output directory (default: {DEFAULT_OUTPUT})")
    parser.add_argument("--list", action="store_true",
                        help="List available protocols and exit")
    args = parser.parse_args()

    if args.list:
        available = sorted(
            d.name for d in DATASET_DIR.iterdir()
            if d.is_dir() and (d / "code").exists()
        )
        print(f"Available protocols ({len(available)}):")
        for p in available: print(f"  {p}")
        return

    if not args.protocols or not (2 <= len(args.protocols) <= 3):
        parser.error("Provide 2 or 3 protocol names via --protocols")

    # Stage 1 — Analyse
    print("\n━━━ Stage 1: Analysing source protocols ━━━")
    analyses: list[ProtocolAnalysis] = []
    for pname in args.protocols:
        print(f"  Analysing {pname}...", end=" ", flush=True)
        try:
            ana = analyse_protocol(pname)
        except FileNotFoundError as e:
            print(f"\n  ERROR: {e}"); return
        analyses.append(ana)
        found = [k for k, v in ana.detected_flags.items() if v]
        print(f"done  (components: {', '.join(found) or 'none'}, "
              f"patterns: {sum(len(c.functions) for c in ana.components.values())} functions)")

    # Stage 2 — Design architecture
    print("\n━━━ Stage 2: Designing architecture ━━━")
    proto_name = args.name
    if not proto_name:
        proto_name = "".join(p.split("_")[0][:4].title() for p in args.protocols) + "Protocol"
    proto_name = re.sub(r'[^a-zA-Z0-9]', '', proto_name)
    if not proto_name[0].isalpha(): proto_name = "Synth" + proto_name

    specs = design_architecture(proto_name, analyses)
    for s in specs:
        print(f"  → {s.filename:30s}  [{s.kind}]  "
              f"{len(s.functions)} fns, {len(s.state_vars)} vars")

    # Stage 3 — Generate code
    run_name = "+".join(args.protocols)
    out_dir = args.output / run_name
    if out_dir.exists():
        shutil.rmtree(out_dir)

    print(f"\n━━━ Stage 3: Generating → {out_dir}/ ━━━")
    write_generated(out_dir, specs, analyses)

    print(f"\n✓ Done!  {len(specs)} contracts in {out_dir}/src/")


if __name__ == "__main__":
    main()
