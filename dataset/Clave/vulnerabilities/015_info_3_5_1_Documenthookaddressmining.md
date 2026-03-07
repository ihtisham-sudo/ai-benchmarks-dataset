# 3.5.1 Documenthookaddressmining

**Severity:** info
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** hook, address, mining, validation, execution, bitmask, contract, documentation, deployment, comments, classification, source code, requirement, lists, PR, verification, behavior, management, removal, process

---

# 3.5.1 Documenthookaddressmining
**Severity:** Informational  
**Context:** HookManager.sol#L241-L244  
**Description:** The contract classifies hooks as validation hooks, execution hooks or both. This classification is based on two bitmasks applied to the hook\u0027s address, which implies that hook addresses must be mined before deployment to find appropriate values for these bits. However, this process isn\u0027t documented in the code.  
**Recommendation:** Document this behavior in the comments of the contract.  
**Clave:** Fixed with PR 787.  
**CantinaManaged:** Requirement on hook address is removed with this fix as it now stores validation and execution hooks in different lists. Verified.
