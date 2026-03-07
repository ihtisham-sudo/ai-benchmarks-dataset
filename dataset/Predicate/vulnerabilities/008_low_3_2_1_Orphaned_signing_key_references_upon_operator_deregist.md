# 3.2.1 Orphaned signing key references upon operator deregistration

**Severity:** low
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** ServiceManager, deregisterOperatorFromAVS, updateOperatorsForQuorum, signing keys, DEREGISTERED, stale mapping, operator, signingKeyToOperator, key references, contract, mapping, stake checks, delete, operator deregistration, valid checks, function, recommendation, context, risk, solidity

---

# 3.2.1 Orphaned signing key references upon operator deregistration
**Severity:** Low Risk  
**Context:** ServiceManager.sol#L177, ServiceManager.sol#L504  
**Description:** In the ServiceManager contract, in the deregisterOperatorFromAVS and updateOperatorsForQuorum functions, operators can be set to DEREGISTERED. However, their signing keys remain mapped in signingKeyToOperator[_operatorSigningKey]. This stale mapping means that the operator’s signing key can still appear valid in certain checks.  
**Recommendation:** Whenever an operator is deregistered (either manually in deregisterOperatorFromAVS or via automatic stake checks in updateOperatorsForQuorum), also clear out their signing key references:  
\u0060\u0060\u0060solidity
delete signingKeyToOperator[oldSigningKey];
\u0060\u0060\u0060  
This ensures that no stale key mappings remain pointing to a deregistered operator.  
**Predicate:** Acknowledged.  
**Cantina Managed:** Acknowledged.
