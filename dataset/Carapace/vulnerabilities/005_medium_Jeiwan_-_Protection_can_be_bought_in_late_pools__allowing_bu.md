# Jeiwan - Protection can be bought in late pools, allowing buyers to pay minimal premium and increase the chance of a compensation

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, protection pools, insurance, late payment, compensation, premium, malicious buyer, front running, lending pool, pool status, active state, default state, grace period, protection mechanism, manual review, protocol, risk, losses, transaction

---

Jeiwan

medium

# Protection can be bought in late pools, allowing buyers to pay minimal premium and increase the chance of a compensation

## Summary
A buyer can buy a protection for a pool that\u0027s already late on a payment. The buyer can pay the minimal premium and get a higher chance of getting a compensation. Protection sellers may bear higher losses due to reduced premium amounts and the increased chance of protection payments.
## Vulnerability Detail
The protocol allows lenders on Goldfinch to get an insurance on the funds they lent. The insurance is paid after [a repayment was late](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L324-L335). The protocol [doesn\u0027t allow protection buyers to buy protections for pools that\u0027s already late](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L407-L435) to disallow buyers abusing the protections payment mechanism. To do this, the \u0060_verifyLendingPoolIsActive\u0060 function [checks the current status of a pool](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L412-L415) and [reverts if it\u0027s late](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L421-L426).

However, \u0060poolStatus\u0060 is cached and can be outdated when the function is called, since it\u0027s not updated in the call. Pool statuses are updated in [assessStates](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L119) and [assessStateBatch](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L137), which are triggered on schedule separately. This allows buyers to buy protections in pools that\u0027s already late in Goldfinch but still active in Carapace.

Consider this scenario:
1. A pool is in the active state after \u0060assessStates\u0060 is run.
1. Before the next \u0060assessStates\u0060 call, the pool gets into the late state, due to a missed repayment. However, in the protocol, the pool is still in the active state since \u0060assessStates\u0060 hasn\u0027t been called.
1. The malicious buyer front runts the next \u0060assessStates\u0060 call and submits their transactions that buys a protection with the minimal duration for the pool. The \u0060_verifyLendingPoolIsActive\u0060 function passes because the pool\u0027s state hasn\u0027t been updated in the contracts yet.
1. The \u0060assessStates\u0060 call changes the status of the pool to \u0060LateWithinGracePeriod\u0060, which disallows buying protections for the pool.
1. If the pool eventually gets into the default state (chances of that is higher since there\u0027s already a late payment), the malicious buyer will be eligible for a compensation.
## Impact
Protection buyers can increase their chances of getting a compensation, while buying protections with the minimal duration and paying the minimal premium. Protection sellers will bear increased loses due to reduced premium amounts and the increased chance of a compensation.
## Code Snippet
1. \u0060_verifyLendingPoolIsActive\u0060 checks the current status of a pool and reverts if it\u0027s not active:
[ProtectionPoolHelper.sol#L412-L415](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L412-L415)
1. Pool statuses are cached and are stored in \u0060DefaultStateManager\u0060:
[DefaultStateManager.sol#L278-L280](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L278-L280)
1. Pool statuses are updated in \u0060DefaultStateManager.assessStates\u0060:
[DefaultStateManager.sol#L119](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L119)
1. \u0060DefaultStateManager.assessStates\u0060 is not called by \u0060ProtectionPool.buyProtection\u0060:
[ProtectionPool.sol#L162](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L162)
## Tool used
Manual Review
## Recommendation
In \u0060ProtectionPoolHelper._verifyLendingPoolIsActive\u0060, consider calling \u0060DefaultStateManager._assessState\u0060 to update the status of the pool for which a protection is bought.
