# Allarious - If a \u0060lendingPool\u0060 is added to the network while in \u0060late\u0060 state, can be defaulted instantly

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, lending pool, defaultStateManager, currentState, late state, late timestamp, _assessState, protocol, exploitation, ReferenceLendingPool, Active state, attack vector, pool default, unusable pool, manual review, security recommendation, state management, risk assessment, smart contract

---

Allarious

high

# If a \u0060lendingPool\u0060 is added to the network while in \u0060late\u0060 state, can be defaulted instantly

## Summary
If a lending pool is added to a protection pool, the \u0060defaultStateManager\u0060 sets the \u0060currentState\u0060 to late without setting the late timestamp. This can enable anyone in the network to be able to call the \u0060_assessState\u0060 once more and mark the pool as default.

## Vulnerability Detail
\u0060defaultStateManager\u0060 user \u0060_assessState\u0060 function to transfer between states. However, in case an underlying pool is called by \u0060_assessState\u0060 for the first time when it is added to the protocol. The \u0060_assessState\u0060 function sets the \u0060currentState\u0060 to \u0060late\u0060 without updating the \u0060lateTimestamp\u0060 which will remain zero. The attacker can exploit this to move the pool to the default state where it locks the lending pool and renders it unusable.

While it is checked that when pools are added to the \u0060ReferenceLendingPool\u0060 inside \u0060_addReferenceLendingPool\u0060 that the pools should be in \u0060Active\u0060 state, if in the time between the addition of a pool and the first time call of \u0060_assessState\u0060 the pool goes from \u0060Active\u0060 to \u0060Late\u0060, this attack can be performed by the attacker.

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L370-L375

## Impact
An attacker can render an underlying lending pool unusable.

## Code Snippet

## Tool used

Manual Review

## Recommendation
The \u0060_assessState\u0060 should handle the initial setting of the state seperately.
