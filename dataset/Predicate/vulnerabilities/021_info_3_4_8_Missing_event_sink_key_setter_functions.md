# 3.4.8 Missing event sink key setter functions

**Severity:** info
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** event sink, setter functions, state-modifying, addPermissionedOperators, removePermissionedOperators, rotatePredicateSigningKey, emit events, state changes, recommendation, commit, fix verified, informational, code quality, best practices, event emission, functionality, state management, contract, audit, review

---

# 3.4.8 Missing event sink key setter functions
**Severity:** Informational  
**Context:** (No context files were provided by the reviewer)  
**Description:** The following state-modifying functions do not emit events.  
- addPermissionedOperators.  
- removePermissionedOperators.  
- rotatePredicateSigningKey.  
**Recommendation:** Consider emitting events that reflect the state changes in the functions listed above.  
**Predicate:** Fixed in commit 279b9fcb.  
**Cantina Managed:** Fix verified.
