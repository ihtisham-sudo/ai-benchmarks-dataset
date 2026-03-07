# 3.2.3 Validate there is no duplicate strategy in strategy array when adding new strategy

**Severity:** low
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** duplicate, strategy, array, validation, operator, stake, share, registerOperatorToAVS, computation, iteration, risk, check, data, input, logic, function, array management, error handling, performance, efficiency

---

# 3.2.3 Validate there is no duplicate strategy in strategy array when adding new strategy
**Severity:** Low Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** When registerOperatorToAVS, a new operator has to have sufficient stake share, the code iterates over all strategies to compute the share.
