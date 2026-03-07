# Strategies Array Can Be Optimized - Issue 2

**Severity:** info
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** dynamic array, strategies, duplicates, check, manual search, inconsistent data, OpenZeppelin, EnumerableSet, AddressSet, remove, enumerate, supported strategies, contract, solidity, recommendation, optimization, data structure, efficiency, implementation, future version

---

# Unused Code in ServiceManager

**Context:** ServiceManager.sol#L75-L80, ServiceManager.sol#L97-L121, ServiceManager.sol#L478  
**Description:** Several pieces of code in ServiceManager are unused or do not serve a functional purpose:

\u0060\u0060\u0060solidity
modifier onlyPermissionedOperator() {
    if (!permissionedOperators[msg.sender]) {
        revert ServiceManager__Unauthorized();
    }
    _;
}

function addPermissionedOperators(address[] calldata _operators) external onlyOwner { ... }
function removePermissionedOperators(address[] calldata _operators) external onlyOwner { ... }
\u0060\u0060\u0060

Similarly, in the function \u0060updateOperatorsForQuorum\u0060, the function never references the \u0060quorumNumbers[i]\u0060, only \u0060quorumNumbers.length\u0060.

In short:
- \u0060onlyPermissionedOperator\u0060 is never called, and \u0060addPermissionedOperators\u0060 / \u0060removePermissionedOperators\u0060 are similarly unused.
- \u0060quorumNumbers\u0060 is read only for its length; the actual bytes inside are never parsed.

**Recommendation:** Remove all these unused features to maintain clarity and minimize maintenance. Specifically:
- Remove \u0060onlyPermissionedOperator\u0060, \u0060addPermissionedOperators\u0060, and \u0060removePermissionedOperators\u0060 if permissioned-operator functionality is no longer intended.
- Eliminate the \u0060quorumNumbers\u0060 parameter if it is never used for anything but length checks. If you truly require multiple quorums, parse and apply those bytes meaningfully; otherwise, drop the parameter altogether.

**Predicate:** Acknowledged. Some of this code will be re-used and the other will be removed in a future version.  
**CantinaManaged:** Acknowledged.

## Strategies Array Can Be Optimized

**Severity:** Informational  
**Context:** ServiceManager.sol#L42  
**Description:** Currently, the ServiceManager contract uses a simple dynamic array:

\u0060\u0060\u0060solidity
address[] public strategies;
\u0060\u0060\u0060

to track recognized strategies. This approach allows duplicates, provides no straightforward way to check if a strategy is already stored, and forces a manual search to remove items. It can lead to inconsistent or duplicated data if a strategy is pushed twice.

**Recommendation:** Use OpenZeppelin\u0027s \u0060EnumerableSet\u0060 library instead of an array:

\u0060\u0060\u0060solidity
EnumerableSet.AddressSet public supportedStrategies;
\u0060\u0060\u0060

This ensures:
- You can add a strategy only if it’s not already in the set.
- You can remove a strategy cleanly without searching the array.
- You avoid duplicates and can still enumerate all supported strategies when needed.

**Predicate:** Acknowledged. This will be implemented in a future version.  
**CantinaManaged:** Acknowledged.
