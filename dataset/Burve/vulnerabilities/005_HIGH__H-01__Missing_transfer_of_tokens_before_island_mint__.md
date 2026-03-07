# [H-01] Missing transfer of tokens before island.mint()

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---

## Severity

**Impact:** Medium

**Likelihood:** High

## Description

The Burve contract allows users to provide liquidity to both the island pool and Uniswap V3 pools. When adding liquidity to the island pool, it will transfer tokens in from the sender (which is the Burve contract itself) before providing liquidity to Uniswap.

```solidity
    function mint(address recipient, uint128 liq) external {
        for (uint256 i = 0; i < distX96.length; ++i) {
            uint128 liqAmount = uint128(shift96(liq * distX96[i], true));
            mintRange(ranges[i], recipient, liqAmount);
        }

        _mint(recipient, liq);
    }
```

However, when users call `Burve.mint()`, it does not transfer the necessary tokens beforehand. This results in a failed transaction, preventing users from successfully providing liquidity to the island pool through the Burve contract.

## Recommendations

Ensure the required tokens are transferred and approved before calling `island.mint()`.
