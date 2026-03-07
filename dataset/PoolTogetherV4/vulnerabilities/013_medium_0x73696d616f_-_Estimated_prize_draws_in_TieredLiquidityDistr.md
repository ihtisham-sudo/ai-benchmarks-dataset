# 0x73696d616f - Estimated prize draws in TieredLiquidityDistributor are off due to rounding down when calculating the sum, leading to incorrect prizes

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, TieredLiquidityDistributor, prize draws, rounding down, prize count, tiers, rewards distribution, impact, calculation error, precision, manual review, Vscode, odds, prizePool, computeNextNumberOfTiers, TierCalculationLib, estimated prizes, error margin, recommendation

---

0x73696d616f

medium

# Estimated prize draws in TieredLiquidityDistributor are off due to rounding down when calculating the sum, leading to incorrect prizes

## Summary

Estimated prize draws in \u0060TieredLiquidityDistributor\u0060 are off due to rounding down when calculating the expected prize count on each tier, leading to an incorrect next number of tiers and distribution of rewards.

## Vulnerability Detail

\u0060ESTIMATED_PRIZES_PER_DRAW_FOR_5_TIERS\u0060 and the other tiers are precomputed initially in \u0060TieredLiquidityDistributor::_sumTierPrizeCounts()\u0060. In [here](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/abstract/TieredLiquidityDistributor.sol#L574), it goes through all tiers and calculates the expected prize count per draw for each tier. However, when doing this [calculation](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/libraries/TierCalculationLib.sol#L113-L115) in \u0060TierCalculationLib.tierPrizeCountPerDraw()\u0060, \u0060uint32(uint256(unwrap(sd(int256(prizeCount(_tier))).mul(_odds))));\u0060, it rounds down the prize count of each tier. This will lead to an incorrect prize count calculation, for example:

\u0060\u0060\u0060solidity
grandPrizePeriodDraws == 8 days
numTiers == 5
prizeCount(tier 0) == 4**0 * 1 / 8 == 1 * 1 / 8 == 0.125 = 0
prizeCount(tier 1) == 4**1 * (1 / 8)^sqrt((1 + 1 - 3) / (1 - 3)) == 4 * 0.2298364718 ≃ 0.92 = 0
prizeCount(tier 2) == 4**2 * 1 == 16
prizeCount(tier 3) == 4**3 * 1 == 64
total = 80
\u0060\u0060\u0060
However, if we multiply the prize counts by a constant and then divide the sum in the end, the total count would be 81 instead, getting an error of 1 / 81 ≃ 1.12 %

## Impact

The estimated prize count will be off, which affects the calculation of the next number of tiers in [PrizePool::computeNextNumberOfTiers()](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/PrizePool.sol#L472). This modifies the whole rewards distribution for the next draw.

## Code Snippet

https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/abstract/TieredLiquidityDistributor.sol#L574
https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/libraries/TierCalculationLib.sol#L113-L115

## Tool used

Manual Review

Vscode

## Recommendation

Add some precision to the calculations by multiplying, for example, by \u00601e5\u0060 each count and then dividing the sum by \u00601e5\u0060. \u0060uint32(uint256(unwrap(sd(int256(prizeCount(_tier)*1e5)).mul(_odds))));\u0060 and \u0060return prizeCount / 1e5;\u0060.
