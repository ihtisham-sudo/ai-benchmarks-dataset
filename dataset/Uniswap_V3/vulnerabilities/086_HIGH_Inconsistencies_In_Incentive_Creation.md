# Inconsistencies In Incentive Creation

**Severity:** HIGH
**Auditor:** OtterSec

---

## Current Issues with Incentive Modification

Currently, any user may call `createIncentive`, adding a small reward to an existing incentive before it starts and replacing the config, thereby interfering with the existing incentive, regardless of whether they are the original creators or stakeholders.

> _Uniswap V3 Staker.sol (Solidity)_
>
```solidity
function createIncentive(IncentiveKey memory key, IncentiveConfig memory config, uint128 reward) external override {
    [...]
    if (config.minTickWidth == 0) revert MinTickWidthMustBePositive();
    bytes32 incentiveId = IncentiveId.compute(key);
    incentives[incentiveId].remainingReward += reward;
    incentives[incentiveId].lastAccrueTime = uint32(key.startTime);
    incentiveConfigs[incentiveId] = config;
    TransferHelperExtended.safeTransferFrom(address(key.rewardToken), _msgSender(), address(this), reward);
    _grantRole(incentiveId, _msgSender());
    [...]
}
```

Furthermore, adding a small reward to an existing incentive grants the caller a role that enables them to change the `incentiveConfig`. This may be exploited by malicious users to manipulate incentive configurations for their advantage, allowing them to alter the configuration settings and potentially compromising the integrity and fairness of the incentive system.

## Remediation

Implement stricter access control mechanisms to restrict the ability to modify incentives and configurations to authorized parties only.

## Patch

Fixed in 108b3ba.

© 2024 Otter Audits LLC. All Rights Reserved. 8/14
