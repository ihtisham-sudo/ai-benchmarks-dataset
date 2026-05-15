# AI Benchmarks Dataset

A curated dataset of Solidity smart-contract protocols for AI benchmarking, audit analysis, and protocol structure exploration.

This repository contains tools to:
- collect smart-contract audit datasets from external sources,
- extract Solidity code into a normalized dataset layout,
- generate protocol-level contract catalogues,
- analyze common protocol building blocks,
- generate callpath trees for contract entry points.

## Repository Overview

The dataset is organized by protocol under `dataset/`, with each protocol typically containing:

- `code/` — extracted Solidity source files
- `vulnerabilities/` — saved audit findings
- `metadata.json` — protocol metadata
- generated analysis files such as `callpaths.md`

Supporting analysis outputs are stored in `analysis/`.

## Main Features

### 1. Dataset Collection
`collect_dataset.py` downloads protocol metadata and vulnerabilities from supported audit sources, then clones protocol repositories and extracts Solidity files into the dataset structure.

### 2. Contract Catalogue Generation
`list_contracts.py` analyzes a single protocol and produces a structured markdown catalogue of all concrete contracts, grouped by primitive type:
- Tokens
- Containers
- Minters
- Exchange
- Oracle
- Access Control
- Core / Factory
- Other

### 3. Component Presence Analysis
`analyze_components.py` scans all protocols under `dataset/` and generates summary reports showing which common protocol components are present in each repository.

### 4. Callpath Generation
`generate_callpaths.py` builds callpath trees for public/external functions in each protocol, showing which internal, library, and external calls they touch.

## Prerequisites

- Python 3.10+
- Git
- Access to the relevant audit data APIs
- Optional: a `SOLODIT_API_KEY` environment variable for Solodit fallback queries

## Installation

Install Python dependencies as needed:

```bash
pip install python-dotenv
```

If you plan to run repository cloning and analysis at scale, ensure `git` is available in your PATH.

## Dataset Layout

```text
dataset/
  <Protocol>/
    code/
      *.sol
    vulnerabilities/
      *.md
    metadata.json
    callpaths.md
```

Generated analysis artifacts are written to:

```text
analysis/
  component_presence_per_repo.csv
  component_presence_per_repo.md
  component_stats.json
```

## Usage

### List Available Protocols

```bash
python3 list_contracts.py --list
```

### Generate a Contract Catalogue for One Protocol

```bash
python3 list_contracts.py Dinari
python3 list_contracts.py Dinari --output analysis/Dinari_catalogue.md
```

### Collect the Dataset

```bash
python3 collect_dataset.py
```

Optional flags:

```bash
python3 collect_dataset.py --dry-run
python3 collect_dataset.py --protocol Dinari
python3 collect_dataset.py --skip-code
```

### Analyze Protocol Components

```bash
python3 analyze_components.py
python3 analyze_components.py --output analysis
```

### Generate Callpath Trees

```bash
python3 generate_callpaths.py
```

## Notes on Analysis

The analysis scripts use heuristic pattern matching to infer protocol structure from Solidity code. Results are useful for benchmarking and large-scale comparison, but they are not a substitute for manual code review.

## Output Examples

### Contract Catalogue
A generated catalogue describes each contract with:
- category
- file path
- inherited parents
- key public/external functions

### Component Analysis
Produces per-repo summaries of:
- exchanges
- vaults
- lending markets
- oracles
- bridges
- tokens
- governance
- smart wallets
- timelocks
- access control

### Callpaths
For each external/public function, the generated callpath output shows internal and external dependencies.

## Contributing

Contributions are welcome. If you add new analysis scripts or dataset-processing utilities, please update this README and document any new outputs or dependencies.

## License

No license file was present in the repository at the time this README was generated.
