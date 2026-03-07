# MalfurionWhitehat - Protection seller will lose unlocked capital if it fails to claim during more than one period

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, protection seller, unlocked capital, claimable amount, DefaultStateManager, calculateAndClaimUnlockedCapital, ProtectionPool, lockedCapitals, snapshot, claiming, capital loss, snapshotId, active state, locked state, code review, manual review, increment, capital instances, proof of concept

---

MalfurionWhitehat

high

# Protection seller will lose unlocked capital if it fails to claim during more than one period

## Summary

The protection seller will lose unlocked capital if it fails to claim during more than one period.

## Vulnerability Detail

The function \u0060DefaultStateManager._calculateClaimableAmount\u0060, used by \u0060DefaultStateManager.calculateAndClaimUnlockedCapital\u0060, which in turn is used by \u0060ProtectionPool.claimUnlockedCapital\u0060, [overrides the claimable unlocked capital](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L500-L505) on every loop iteration on the [\u0060lockedCapitals\u0060 array](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L476-L478). 

As a result, [only the last snapshot is returned](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L479) by this function, regardless if the protection seller has claimed the unlocked capital or not. The purpose of this code was to prevent sellers from [claiming the same snapshot twice](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L487), but since the \u0060_claimableUnlockedCapital\u0060 variable is being overwritten instead of incremented, on each loop iteration, it will also make sellers lose unlocked capital if they fail to claim at each snapshot.

Proof of concept:

1. Pool goes to locked state with snapshotId 1
2. Pool goes to active state
3. Pool goes to locked state with snapshotId 2
4. Pool goes to active state
5. Protection seller calls \u0060ProtectionPool.claimUnlockedCapital\u0060, but they will only receive what\u0027s due from snapshotId 2, not from snapshotId 1

## Impact

The protection seller will lose unlocked capital if it fails to claim during more than one period.

## Code Snippet

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L500-L505

## Tool used

Manual Review

## Recommendation

Increment \u0060_claimableUnlockedCapital\u0060 [for all](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L502-L505) locked capital instances.

