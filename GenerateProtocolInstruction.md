# Protocol Contract Catalogue Tool

> **One-line summary:** Give it a protocol codebase → get a structured markdown catalogue of every contract, grouped by primitive type.

---

## How to Run

```bash
# List all 62 available protocols
python3 list_contracts.py --list

# Catalogue a single protocol (prints to stdout)
python3 list_contracts.py Dinari

# Save to a file
python3 list_contracts.py Dinari --output analysis/Dinari_catalogue.md
python3 list_contracts.py Midas  --output analysis/Midas_catalogue.md
```

---

## What It Produces

The tool analyses `dataset/<Protocol>/code/`, picks up every concrete Solidity `contract` (interfaces and libraries are skipped), classifies each into a **primitive category**, and renders a markdown document like this:

```
# Dinari — Contract Catalogue

> 8 contract(s) identified across 5 primitive categories.

## Tokens
The protocol utilises the following token contracts for accounting purposes:
- **DShare** – Core token contract for bridged assets. Rebases on stock splits.
  File: `src/DShare.sol`
  Key functions: `balancePerShare`, `burn`, `mint`, `setName`, `setSymbol` …

## Containers
The protocol stores assets in the following containers:
- **Vault** – Managing and executing withdrawals of ERC20 tokens.
  File: `src/orders/Vault.sol`

## Exchange
The protocol implements protocol operations as the following exchange contracts:
- **OrderProcessor** – Core contract managing orders for dShare tokens.
  File: `src/orders/OrderProcessor.sol`

## Oracle
...

## Relationships
**OrderProcessor** interacts directly with token contracts (DShare, WrappedDShare) …
```

---

## Primitive Categories

| Category | What goes here |
|---|---|
| **Tokens** | ERC-20/721/rebasing tokens |
| **Containers** | Vaults, escrows, treasuries |
| **Minters** | Contracts with privileged mint/burn roles |
| **Exchange** | Order processors, swap routers, settlement contracts |
| **Oracle** | Price feeds, rate providers |
| **Access Control** | Role managers, transfer restrictors |
| **Core / Factory** | Factories, registries, proxies |
| **Other** | Utility/auxiliary contracts |

---

## Output Location

Results are printed to stdout by default. Use `--output <path>` to write to a file.
Suggested convention: `analysis/<Protocol>_catalogue.md`.