# unforgiven - function lockCapital() doesn\u0027t filter the expired protections first and code may lock more funds than required and expired defaulted protections may funded

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cyber security, vulnerability, lockCapital, expired protections, funds locking, defaulted protections, ProtectionPool, accruePremiumAndExpireProtections, active protection array, lending pool, protection sellers, token payment, manual review, code review, fund loss, protection calculation, expiration check, risk assessment, smart contract, financial security

---

unforgiven

high

# function lockCapital() doesn\u0027t filter the expired protections first and code may lock more funds than required and expired defaulted protections may funded

## Summary
when a lending loan defaults, then function \u0060lockCapital()\u0060 get called in the ProtectionPool to lock required funds for the protections bought for that lending pool, but code doesn\u0027t filter the expired protections first and they may be expired protection in the active protection array that are not excluded and this would cause code to lock more fund and pay fund for expired defaulted protections and protection sellers would lose more funds.

## Vulnerability Detail
This \u0060lockCapital()\u0060 code:
\u0060\u0060\u0060solidity
  function lockCapital(address _lendingPoolAddress)
    external
    payable
    override
    onlyDefaultStateManager
    whenNotPaused
    returns (uint256 _lockedAmount, uint256 _snapshotId)
  {
    /// step 1: Capture protection pool\u0027s current investors by creating a snapshot of the token balance by using ERC20Snapshot in SToken
    _snapshotId = _snapshot();

    /// step 2: calculate total capital to be locked
    LendingPoolDetail storage lendingPoolDetail = lendingPoolDetails[
      _lendingPoolAddress
    ];

    /// Get indexes of active protection for a lending pool from the storage
    EnumerableSetUpgradeable.UintSet
      storage activeProtectionIndexes = lendingPoolDetail
        .activeProtectionIndexes;

    /// Iterate all active protections and calculate total locked amount for this lending pool
    /// 1. calculate remaining principal amount for each loan protection in the lending pool.
    /// 2. for each loan protection, lockedAmt = min(protectionAmt, remainingPrincipal)
    /// 3. total locked amount = sum of lockedAmt for all loan protections
    uint256 _length = activeProtectionIndexes.length();
    for (uint256 i; i < _length; ) {
      /// Get protection info from the storage
      uint256 _protectionIndex = activeProtectionIndexes.at(i);
      ProtectionInfo storage protectionInfo = protectionInfos[_protectionIndex];

      /// Calculate remaining principal amount for a loan protection in the lending pool
      uint256 _remainingPrincipal = poolInfo
        .referenceLendingPools
        .calculateRemainingPrincipal(
          _lendingPoolAddress,
          protectionInfo.buyer,
          protectionInfo.purchaseParams.nftLpTokenId
        );

      /// Locked amount is minimum of protection amount and remaining principal
      uint256 _protectionAmount = protectionInfo
        .purchaseParams
        .protectionAmount;
      uint256 _lockedAmountPerProtection = _protectionAmount <
        _remainingPrincipal
        ? _protectionAmount
        : _remainingPrincipal;

      _lockedAmount += _lockedAmountPerProtection;

      unchecked {
        ++i;
      }
    }

    unchecked {
      /// step 3: Update total locked & available capital in storage
      if (totalSTokenUnderlying < _lockedAmount) {
        /// If totalSTokenUnderlying < _lockedAmount, then lock all available capital
        _lockedAmount = totalSTokenUnderlying;
        totalSTokenUnderlying = 0;
      } else {
        /// Reduce the total sToken underlying amount by the locked amount
        totalSTokenUnderlying -= _lockedAmount;
      }
    }
  }
\u0060\u0060\u0060
As you can see code loops through active protection array for that lending pool and calculates required locked amount but it doesn\u0027t call \u0060_accruePremiumAndExpireProtections()\u0060 to make sure active protections doesn\u0027t include any expired protections.
if function \u0060_accruePremiumAndExpireProtections()\u0060 doesn\u0027t get called for a while, then there would be possible that some of the protections are expired and they are still in the active protection array. This would cause code to calculated more locked amount and also pay fund for those expired defaulted protections too from protection sellers.
(also when calculating the required token payment for the protection code doesn\u0027t check the expiration too in the other functions that are get called by the \u0060lockCapital()\u0060, the expire check doesn\u0027t exists in inner function too)

## Impact
see summery

## Code Snippet
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L357-L411

## Tool used
Manual Review

## Recommendation
call \u0060_accruePremiumAndExpireProtections()\u0060 for the defaulted pool to filter out the expired protections.
