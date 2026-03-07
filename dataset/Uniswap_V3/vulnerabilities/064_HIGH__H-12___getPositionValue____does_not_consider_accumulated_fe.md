# [H-12] `getPositionValue()` does not consider accumulated fees

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---

## Severity

**Impact:** High

**Likelihood:** Medium

## Description

The function `getPositionValue()` only retrieves the liquidity token amounts using `getLiquidityAmounts()` and converts them into the quote token value. But it does not account for accumulated fees.

```solidity

    function getPositionValue(
        address positionManager,
        uint256 tokenId,
        address quoteToken
    ) external view override returns (uint256) {
        // Get position details
        (,, address token0, address token1,,,, uint128 liquidity,,,,) = INonfungiblePositionManager(positionManager).positions(tokenId);

        // Get amounts
        (uint256 amount0, uint256 amount1) = getLiquidityAmounts(positionManager, tokenId, liquidity);

        // Convert to quote token value
        uint256 value0 = convertTokenValue(token0, amount0, quoteToken);
        uint256 value1 = convertTokenValue(token1, amount1, quoteToken);

        return value0 + value1;
    }
```

**Note**: Uniswap V3 positions earn fees over time, and these are claimable but not included in the liquidity calculation.

## Recommendations

- Include Accumulated Fees in Position Value Calculation
  - You can use `tokensOwed0` and `tokensOwed1` in response of `positions(tokenId)` to calculate how many uncollected tokens are owed to the position, as of the last computation
- Use `collect` function to collect fees for a specific position [Uniswap Doc](https://docs.uniswap.org/contracts/v3/reference/periphery/NonfungiblePositionManager#collect)
