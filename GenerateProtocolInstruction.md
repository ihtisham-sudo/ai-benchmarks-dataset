# Protocol Generation Agent

> **One-line summary:** Give it 2-3 real protocol codebases → get a brand-new, multi-contract Solidity protocol back.

---

## How to Run

```bash
# See all 62 available protocols
python3 generate_protocol.py --list

# Two-protocol synthesis
python3 generate_protocol.py --protocols Aave_V3 Uniswap_V3 --name LendingDex

# Three-protocol synthesis with custom output
python3 generate_protocol.py --protocols FlatMoney GMX_V2 Olympus_Cooler \
  --name SyntheticVault --output ./generated/
```

---

## The Three Stages

```
dataset/Aave_V3/code/   ──┐
dataset/Uniswap_V3/code/ ─┤  Stage 1: Analyse
dataset/Telcoin/code/   ──┘
        │
        ▼  extracts: function signatures, state var shapes,
           events, errors ,  classified by component type
        │
        ▼  Stage 2: Architect
           decides which contracts to generate
           (token / lending / exchange / oracle / vault / …)
        │
        ▼  Stage 3: Generate
           writes fresh Solidity ^0.8.20 from scratch
           no inheritance from source contracts
           no copied bodies
        │
        ▼
generated/<Name>/
  manifest.json
  src/
    AccessControl.sol + interfaces/IAccessControl.sol
    Token.sol         + interfaces/IToken.sol
    LendingPool.sol   + interfaces/ILendingPool.sol
    SwapRouter.sol    + interfaces/ISwapRouter.sol
    PriceOracle.sol   + interfaces/IPriceOracle.sol
    Vault.sol         + interfaces/IVault.sol
    <Name>.sol        + interfaces/I<Name>.sol   ← core coordinator
```

---

## Real Example ,  `Aave_V3 + Uniswap_V3 → LendingDex`

```
━━━ Stage 1: Analysing source protocols ━━━
  Analysing Aave_V3...    done  (components: token, lending, oracle, vault, acl | 265 patterns)
  Analysing Uniswap_V3... done  (components: token, exchange              |  14 patterns)

━━━ Stage 2: Designing architecture ━━━
  → Events.sol         [library]    0 fns,  0 vars
  → AccessControl.sol  [acl]       15 fns,  3 vars
  → Token.sol          [token]     17 fns, 14 vars
  → Vault.sol          [vault]     19 fns, 12 vars
  → LendingPool.sol    [lending]   19 fns, 13 vars
  → SwapRouter.sol     [exchange]   9 fns,  5 vars
  → PriceOracle.sol    [oracle]    16 fns,  6 vars
  → LendingDex.sol     [core]       1 fns,  6 vars

━━━ Stage 3: Generating → generated/Aave_V3+Uniswap_V3/ ━━━
  ✓ 8 contracts  ✓ 7 interfaces  ✓ manifest.json

✓ Done!  96 total functions, 59 state vars
```

---