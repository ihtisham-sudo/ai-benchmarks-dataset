# chaduke - Some protection buyers might not be able to renew their protections due to delayed expiration processing.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, protection buyers, renewal, expiration processing, verifyAndAccruePremium, bug, grace period, verifyBuyerCanRenewProtection, expired protection, lending pool, position token ID, protectionBuyerAccounts, expireProtection, accruePremiumAndExpireProtections, payment, latest payment timestamp, active protections, manual review, recommendation

---

chaduke

medium

# Some protection buyers might not be able to renew their protections due to delayed expiration processing.

## Summary
Some protection buyers will never be able to renew their protection due to delayed expiration processing. 

## Vulnerability Detail
We show below how some buyers will not be able to renew their protection due to delayed expiration process caused by the the wrong implementation of \u0060\u0060verifyAndAccruePremium()\u0060\u0060.
Due to the bug, they might miss the deadline and grace period for renewal. 

1) First the \u0060\u0060verifyBuyerCanRenewProtection()\u0060\u0060 function checks whether it is too late to renew the protection (before the grace period expires).  In addition, \u0060\u0060verifyBuyerCanRenewProtection()\u0060\u0060 also checks whether there exists an expired protection with the same lending pool and position token ID at \u0060\u0060protectionBuyerAccounts[msg.sender].expiredProtectionIndexByLendingPool[_protectionPurchaseParams.lendingPoolAddress][_protectionPurchaseParams.nftLpTokenId]\u0060\u0060 in L371. If such an existing expired protection is not there, renewal will be rejected. 

[https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L360-L399](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L360-L399)

2) In order for the expired protection to be stored in \u0060\u0060protectionBuyerAccounts[msg.sender].expiredProtectionIndexByLendingPool[_protectionPurchaseParams.lendingPoolAddress][_protectionPurchaseParams.nftLpTokenId]\u0060\u0060, the \u0060\u0060expireProtection()\u0060\u0060 must be called at L1004 of function \u0060\u0060_accruePremiumAndExpireProtections()\u0060\u0060. 

[https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L963-L1021](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L963-L1021)

3) the \u0060\u0060expireProtection()\u0060\u0060 function stores such expired protection at L311-315: 

[https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L293-L321](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L293-L321)

4) However, before \u0060\u0060expireProtection()\u0060\u0060  can be called, function \u0060\u0060verifyAndAccruePremium()\u0060\u0060 needs to be called first to decide whether a protection has expired or not (L990).

[https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L963-L1021](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L963-L1021)

5) However, when there is no payment for a while, for example, when the last payment is made before a protection P starts (\u0060\u0060_latestPaymentTimestamp < _startTimestamp\u0060\u0060),  P will not be considered as \u0060\u0060expired\u0060\u0060 see L215-220 of \u0060\u0060verifyAndAccruePremium()\u0060\u0060  below:  

[https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L201-L284](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/libraries/ProtectionPoolHelper.sol#L201-L284)

6) Therefore, if there is no payment for a long time, then \u0060\u0060verifyAndAccruePremium()\u0060\u0060  will always consider a protection P has not expired. \u0060\u0060expireProtection()\u0060\u0060 will never process it. So the actually expired protection will not be stored in \u0060\u0060protectionBuyerAccounts[msg.sender].expiredProtectionIndexByLendingPool[_protectionPurchaseParams.lendingPoolAddress][_protectionPurchaseParams.nftLpTokenId]\u0060\u0060. The buyer for P will not be able to renew P because \u0060\u0060verifyBuyerCanRenewProtection()\u0060\u0060 will fail to find an existing expired protection P. If there is no payment for a long time, then the buyer for P might miss the deadline and grace period and will never be able to renew P anymore.

## Impact
Some protection buyers might never  be able to renew their protections due to delayed expiration processing as a result of a bug of \u0060\u0060verifyAndAccruePremium()\u0060\u0060.

\u0060\u0060getActiveProtections()\u0060\u0060 might return some protections that are supposed to have expired, but not processed due to the above bug. 

## Code Snippet
See above

## Tool used
VSCode

Manual Review

## Recommendation
We revise \u0060\u0060verifyAndAccruePremium()\u0060\u0060 so that it will process and return the right value when a protection expires. 

\u0060\u0060\u0060diff
 function verifyAndAccruePremium(
    ProtectionPoolInfo storage poolInfo,
    ProtectionInfo storage protectionInfo,
    uint256 _lastPremiumAccrualTimestamp,
    uint256 _latestPaymentTimestamp
  )
    external
    view
    returns (uint256 _accruedPremiumInUnderlying, bool _protectionExpired)
  {
    uint256 _startTimestamp = protectionInfo.startTimestamp;

+    uint256 _expirationTimestamp = protectionInfo.startTimestamp +
+      protectionInfo.purchaseParams.protectionDurationInSeconds;
+    _protectionExpired = block.timestamp > _expirationTimestamp;


    /// This means no payment has been made after the protection is bought or protection starts in the future.
    /// so no premium needs to be accrued.
-    if (
-      _latestPaymentTimestamp < _startTimestamp ||
-      _startTimestamp > block.timestamp
-    ) {
+    if (!_protectionExpired                                              // @audit: only if it has not expired
+      (_latestPaymentTimestamp < _startTimestamp ||
+      _startTimestamp > block.timestamp)
+    ) {
 
      return (0, false);
    }

    /// Calculate the protection expiration timestamp and
    /// Check if the protection is expired or not.
-    uint256 _expirationTimestamp = protectionInfo.startTimestamp +
-      protectionInfo.purchaseParams.protectionDurationInSeconds;
-    _protectionExpired = block.timestamp > _expirationTimestamp;

    /// Only accrue premium if the protection is expired
    /// or latest payment is made after the protection start & last premium accrual
    if (
      _protectionExpired ||
      (_latestPaymentTimestamp > _startTimestamp &&
        _latestPaymentTimestamp > _lastPremiumAccrualTimestamp)
    ) {
      /**
       * <-Protection Bought(second: 0) --- last accrual --- now(latestPaymentTimestamp) --- Expiration->
       * The time line starts when protection is bought and ends when protection is expired.
       * secondsUntilLastPremiumAccrual is the second elapsed since the last accrual timestamp.
       * secondsUntilLatestPayment is the second elapsed until latest payment is made.
       */

      // When premium is accrued for the first time, the _secondsUntilLastPremiumAccrual is 0.
      uint256 _secondsUntilLastPremiumAccrual;
      if (_lastPremiumAccrualTimestamp > _startTimestamp) {
        _secondsUntilLastPremiumAccrual =
          _lastPremiumAccrualTimestamp -
          _startTimestamp;
      }

      /// if loan protection is expired, then accrue premium till expiration and mark it for removal
      uint256 _secondsUntilLatestPayment;
      if (_protectionExpired) {
        _secondsUntilLatestPayment = _expirationTimestamp - _startTimestamp;
        console.log(
          "Protection expired for amt: %s",
          protectionInfo.purchaseParams.protectionAmount
        );
      } else {
        _secondsUntilLatestPayment = _latestPaymentTimestamp - _startTimestamp;
      }

      /// Calculate the accrued premium amount scaled to 18 decimals
      uint256 _accruedPremiumIn18Decimals = AccruedPremiumCalculator
        .calculateAccruedPremium(
          _secondsUntilLastPremiumAccrual,
          _secondsUntilLatestPayment,
          protectionInfo.K,
          protectionInfo.lambda
        );

      console.log(
        "accruedPremium from second %s to %s: ",
        _secondsUntilLastPremiumAccrual,
        _secondsUntilLatestPayment,
        _accruedPremiumIn18Decimals
      );

      /// Scale the premium amount to underlying decimals
      _accruedPremiumInUnderlying = scale18DecimalsAmtToUnderlyingDecimals(
        _accruedPremiumIn18Decimals,
        poolInfo.underlyingToken.decimals()
      );
    }
  }
\u0060\u0060\u0060
