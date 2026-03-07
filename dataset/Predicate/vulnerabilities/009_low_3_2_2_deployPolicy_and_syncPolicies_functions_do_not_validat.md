# 3.2.2 deployPolicy and syncPolicies functions do not validate non-empty policy

**Severity:** low
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** deployPolicy, syncPolicies, validation, policy, non-empty, require, check, ServiceManager, SimpleServiceManager, Solidity, smart contract, policyID, bytes, length, empty string, content, recommendation, function, error message, PR 21

---

# 3.2.2 deployPolicy and syncPolicies functions do not validate non-empty policy
**Severity:** Low Risk  
**Context:** ServiceManager.sol#L195-L199, SimpleServiceManager.sol#L160  
**Description:** In the ServiceManager.deployPolicy function:  
\u0060\u0060\u0060solidity
require(bytes(idToPolicy[_policyID]).length == 0, "Predicate.deployPolicy: policy exists");
\u0060\u0060\u0060  
checks that the _policyID does not already exist. However, there is no check ensuring the _policy string itself has a nonzero length. This check is also missing in the SimpleServiceManager.syncPolicies function.  
**Recommendation:** Add a check in both functions that ensure that _policy is not empty:  
\u0060\u0060\u0060solidity
require(bytes(_policy).length > 0, "Predicate.deployPolicy: policy string cannot be empty");
\u0060\u0060\u0060  
so that a new policy must contain actual content.  
**Predicate:** Fixed in PR 21.  
**Cantina Managed:** Fix verified.
