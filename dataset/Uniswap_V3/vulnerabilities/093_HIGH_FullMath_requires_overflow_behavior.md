# FullMath requires overflow behavior

**Severity:** HIGH
**Auditor:** Spearbit

---

## Security Audit Summary

## Severity
**High Risk**

## Context
`FullMath.sol#L2`

## Description
UniswapV3’s `FullMath.sol` is copied and migrated from an old solidity version to version 0.8, which reverts on overflows. However, the old `FullMath` relies on implicit overflow behavior. The current code will revert on overflows when it should not, which breaks the `SwapManagerUniV3` contract.

## Recommendation
Use the official `FullMath.sol` 0.8 branch that wraps the code in an unchecked statement. See #40.

## Spearbit
Fixed. The Uniswap V3 branch is added as a dependency in PR #550.
