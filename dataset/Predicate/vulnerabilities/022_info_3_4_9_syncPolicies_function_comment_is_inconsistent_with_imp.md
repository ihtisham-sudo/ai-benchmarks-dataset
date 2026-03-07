# 3.4.9 syncPolicies function comment is inconsistent with implementation

**Severity:** info
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** syncPolicies, comment, implementation, policy IDs, register, update, policyIDToThreshold, thresholds, deployedPolicyIDs, emit, PolicySynced, Smart Contract, Solidity, SimpleServiceManager, functionality, documentation, code review, recommendation, fix, verification

---

# 3.4.9 syncPolicies function comment is inconsistent with implementation
**Severity:** Informational  
**Context:** SimpleServiceManager.sol#L156-L180  
**Description:** The syncPolicies\u0027s comment outlines that the function should be able to register or update policy IDs. However, the function can only register new policy IDs. Once a policy ID is registered, the function can not update that policy ID because \u0060policyIDToThreshold[policyIDs[i]]\u0060 is no longer 0.  
\u0060\u0060\u0060solidity
if (policyIDToThreshold[policyIDs[i]] == 0) {
    policyIDToThreshold[policyIDs[i]] = thresholds[i];
    deployedPolicyIDs.push(policyIDs[i]);
    emit PolicySynced(policyIDs[i]);
}
\u0060\u0060\u0060  
**Recommendation:** Consider correcting the syncPolicies\u0027s comment.  
**Predicate:** Fixed in PR 21.  
**Cantina Managed:** Fix verified.
PAGE END
