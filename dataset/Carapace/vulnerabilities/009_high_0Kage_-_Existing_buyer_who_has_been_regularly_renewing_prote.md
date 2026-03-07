# 0Kage - Existing buyer who has been regularly renewing protection will be denied renewal even when she is well within the renewal grace period

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, renewal, grace period, protection, buyer, lending pool, NFT, verifyBuyerCanRenewProtection, LateWithinGracePeriod, Active, default, premium, loss event, manual review, verifyLendingPoolIsActive, renewProtection, protection payments, legitimate renewal, protection denial

---

0Kage

high

# Existing buyer who has been regularly renewing protection will be denied renewal even when she is well within the renewal grace period

## Summary
Existing buyers have an opportunity to renew their protection within grace period. If lending state update happens from \u0060Active\u0060 to \u0060LateWithinGracePeriod\u0060 just 1 second after a buyer\u0027s protection expires, protocol denies buyer an opportunity even when she is well within the grace period.

Since defaults are not sudden and an \u0060Active\u0060 loan first transitions into \u0060LateWithinGracePeriod\u0060, it is unfair to deny an existing buyer an opportunity to renew (its alright if a new protection buyer is DOSed). This is especially so because a late loan can become \u0060active\u0060 again in future (or move to \u0060default\u0060, but both possibilities exist at this stage).

All previous protection payments are a total loss for a buyer when she is denied a legitimate renewal request at the first sign of danger.

## Vulnerability Detail
\u0060renewProtection\u0060 first calls \u0060verifyBuyerCanRenewProtection\u0060 that checks if the user requesting renewal holds same NFT id on same lending pool address & that the current request is within grace period defined by protocol.

Once successfully verified, \u0060renewProtection\u0060 calls [\u0060_verifyAndCreateProtection\u0060](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L189) to renew protection. This is the same function that gets called when a new protection is created.

Notice that this function calls \u0060_verifyLendingPoolIsActive\u0060 as part of its verification before creating new protection - this check denies protection on loans that are in \u0060LateWithinGracePeriod\u0060 or \u0060Late\u0060 phase (see snippet below).

\u0060\u0060\u0060solidity
function _verifyLendingPoolIsActive(
    IDefaultStateManager defaultStateManager,
    address _protectionPoolAddress,
    address _lendingPoolAddress
  ) internal view {
    LendingPoolStatus poolStatus = defaultStateManager.getLendingPoolStatus(
      _protectionPoolAddress,
      _lendingPoolAddress
    );

    ...
    if (
      poolStatus == LendingPoolStatus.LateWithinGracePeriod ||
      poolStatus == LendingPoolStatus.Late
    ) {
      revert IProtectionPool.LendingPoolHasLatePayment(_lendingPoolAddress);
    }
    ...
}

\u0060\u0060\u0060

## Impact
User who has been regularly renewing protection and paying premium to protect against a future loss event will be denied that very protection when she most needs it.

If existing user is denied renewal, she can never get back in (unless the lending pool becomes active again). All her previous payments were a total loss for her.

## Code Snippet
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L189

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L407

## Tool used
Manual Review

## Recommendation
When a user is calling \u0060renewProtection\u0060, a different implementation of \u0060verifyLendingPoolIsActive\u0060 is needed that allows a user to renew even when lending pool status is \u0060LateWithinGracePeriod\u0060 or \u0060Late\u0060.

Recommend using \u0060verifyLendingPoolIsActiveForRenewal\u0060 function in renewal flow as shown below

\u0060\u0060\u0060solidity
  function verifyLendingPoolIsActiveForRenewal(
    IDefaultStateManager defaultStateManager,
    address _protectionPoolAddress,
    address _lendingPoolAddress
  ) internal view {
    LendingPoolStatus poolStatus = defaultStateManager.getLendingPoolStatus(
      _protectionPoolAddress,
      _lendingPoolAddress
    );

    if (poolStatus == LendingPoolStatus.NotSupported) {
      revert IProtectionPool.LendingPoolNotSupported(_lendingPoolAddress);
    }
    //------ audit - this section needs to be commented-----//
    //if (
    //  poolStatus == LendingPoolStatus.LateWithinGracePeriod ||
    //  poolStatus == LendingPoolStatus.Late
    //) {
    //  revert IProtectionPool.LendingPoolHasLatePayment(_lendingPoolAddress);
    //}
    // ---------------------------------------------------------//

    if (poolStatus == LendingPoolStatus.Expired) {
      revert IProtectionPool.LendingPoolExpired(_lendingPoolAddress);
    }

    if (poolStatus == LendingPoolStatus.Defaulted) {
      revert IProtectionPool.LendingPoolDefaulted(_lendingPoolAddress);
    }
  }
\u0060\u0060\u0060
