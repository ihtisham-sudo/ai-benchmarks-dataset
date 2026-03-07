# Koolex - Missing validation of snapshotId makes it possible for the investor to claim unlocked capitals from the same snapshot multiple times

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, snapshotId, claimUnlockedCapital, ProtectionPool, calculateAndClaimUnlockedCapital, lastClaimedSnapshotId, lending pools, locked capitals, unlocked capitals, claimable amount, manual review, security flaw, code snippet, investor, seller, funds drainage, state transition, zero validation, unfair claims

---

Koolex

high

# Missing validation of snapshotId makes it possible for the investor to claim unlocked capitals from the same snapshot multiple times

## Summary
Missing validation of snapshotId makes it possible for the investor/seller to claim unlocked capitals from the same snapshot multiple times

## Vulnerability Detail
### Description
The seller can call \u0060ProtectionPool.claimUnlockedCapital\u0060 function to claim unlocked capitals. It then calls \u0060defaultStateManager.calculateAndClaimUnlockedCapital\u0060 to calculate the claimable amount, then it transfers the amount to the seller if it is greater than zero. 
\u0060defaultStateManager.calculateAndClaimUnlockedCapital\u0060 function works as follows:
1. Iterates over all lending pools.
2. For each lending pool calculates the claimable amount for the seller.
3. Updates the last claimed snapshot id for the seller for the given lending pool so it becomes uncalimable next time.

However, before updating the last claimed snapshot id, it doesn\u0027t check if the returned snapshot Id (from \u0060_calculateClaimableAmount\u0060 function) is zero. This means if it happens that the returned value is zero, the last claimed snapshot id will be reset to its initial value (zero) and the seller can claim again as if s/he never did.

### PoC

Given:
A pool protection with one lending pool for simplicity 
Seller\u0027s lastClaimedSnapshotId = 0

Imagine the following sequence of events:

- **Event**: Lending pool transition from **Active to Late**
	- A snapshot taken
	- LockedCapitals[0].snapshotId = 1
	- LockedCapitals[0].locked = true
- **Event**: Lending pool transition from **Late to Active**
	- LockedCapitals[0].snapshotId = 1
	- LockedCapitals[0].locked = false
- **Event**: **Seller claims** => receives his/her share of the unlocked capital
	- LastClaimedSnapshotId = 1
- **Event**: **Seller claims** => doesn\u0027t receive anything
	- LastClaimedSnapshotId = 0 (this is the issue as it is reset to zero)
- **Now the seller can claim again from the same snapshot**
- **Event**: **Seller claims** => receives his/her share of the unlocked capital
	- LastClaimedSnapshotId = 1

This can be repeated till all funds/capitals are drained.

This happens when all snapshots were claimed before, then the function \u0060_calculateClaimableAmount\u0060 will return_latestClaimedSnapshotId as zero.


## Impact
- An investor/seller could possibly claim unlocked capitals from the same snapshot multiple times which is unfair.
- An attacker could join the pool as seller, later drains the funds from the protection pool whenever any lending pool goes into Late then Active state again.

## Code Snippet
- ProtectionPool.claimUnlockedCapital
\u0060\u0060\u0060sh
    /// Investors can claim their total share of released/unlocked capital across all lending pools
    uint256 _claimableAmount = defaultStateManager
      .calculateAndClaimUnlockedCapital(msg.sender);

    if (_claimableAmount > 0) {
      console.log(
        "Total sToken underlying: %s, claimableAmount: %s",
        totalSTokenUnderlying,
        _claimableAmount
      );
      /// transfer the share of unlocked capital to the receiver
      poolInfo.underlyingToken.safeTransfer(_receiver, _claimableAmount);
    }
\u0060\u0060\u0060
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L427-L445

- defaultStateManager.calculateAndClaimUnlockedCapital

\u0060\u0060\u0060sh
 /// Calculate the claimable amount across all the locked capital instances for a given protection pool
      (
        uint256 _unlockedCapitalPerLendingPool,
        uint256 _snapshotId
      ) = _calculateClaimableAmount(poolState, _lendingPool, _seller);
      _claimedUnlockedCapital += _unlockedCapitalPerLendingPool;

      /// update the last claimed snapshot id for the seller for the given lending pool,
      /// so that the next time the seller claims, the calculation starts from the last claimed snapshot id
      poolState.lastClaimedSnapshotIds[_lendingPool][_seller] = _snapshotId;

\u0060\u0060\u0060
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L186-L195

- defaultStateManager._calculateClaimableAmount
\u0060\u0060\u0060sh
      /// Verify that the seller does not claim the same snapshot twice
      if (!lockedCapital.locked && _snapshotId > _lastClaimedSnapshotId) {
        ERC20SnapshotUpgradeable _poolSToken = ERC20SnapshotUpgradeable(
          address(poolState.protectionPool)
        );

        console.log(
          "balance of seller: %s, total supply: %s at snapshot: %s",
          _poolSToken.balanceOfAt(_seller, _snapshotId),
          _poolSToken.totalSupplyAt(_snapshotId),
          _snapshotId
        );

        /// The claimable amount for the given seller is proportional to the seller\u0027s share of the total supply at the snapshot
        /// claimable amount = (seller\u0027s snapshot balance / total supply at snapshot) * locked capital amount
        _claimableUnlockedCapital =
          (_poolSToken.balanceOfAt(_seller, _snapshotId) *
            lockedCapital.amount) /
          _poolSToken.totalSupplyAt(_snapshotId);

        /// Update the last claimed snapshot id for the seller
        _latestClaimedSnapshotId = _snapshotId;

        console.log(
          "Claimable amount for seller %s is %s",
          _seller,
          _claimableUnlockedCapital
        );
      }

\u0060\u0060\u0060
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L487-L515


## Tool used

Manual Review

## Recommendation
Only update the last snapshot id of the seller if it is greater than zero.
 
 Example:
\u0060\u0060\u0060sh
if(_snapshotId > 0){
      poolState.lastClaimedSnapshotIds[_lendingPool][_seller] = _snapshotId;
	 }

\u0060\u0060\u0060
  
