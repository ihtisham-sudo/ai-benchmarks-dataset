# Lack Of Adjustment For Refunded Rewards

**Severity:** HIGH
**Auditor:** OtterSec

---

## Unstake Token Function

The `unstakeToken` function deducts rewards distributed to both the owner and the liquidator from `incentive.accountedReward` to reflect their distribution from the total remaining reward pool. However, it overlooks adjusting the refunded value, which represents the reward amount returned to the incentive’s remaining reward pool upon unstaking. To maintain consistency, the program should also reduce the refunded value if the refunded amount is returned to the `remainingReward` pool.

> _Uniswap V3 Staker.sol - Solidity_

```solidity
/// @inheritdoc IUniswapV3Staker
function unstakeToken(IncentiveKey memory key, uint256 tokenId) external override {
    [...]
    {
        // remove unstaked liquidity
        incentive.totalLiquidityStaked -= stake.liquidity;
        // reward is never greater than total reward unclaimed
        incentive.accountedReward -= ownerReward + liquidatorReward;
        if (refunded > 0) incentive.remainingReward += refunded;
    }
    [...]
}
```

## Remediation

Reduce the refunded value if the refunded amount is returned to the `remainingReward` pool.

## Patch

Fixed in fe46563.

© 2024 Otter Audits LLC. All Rights Reserved. 9/14
