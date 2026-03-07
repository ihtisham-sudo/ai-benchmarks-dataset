# 3.5.2 Always use reset when resetting values in linked lists

**Severity:** info
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** linked list, reset, default value, consistency, codebase, library, function, value erasure, implementation, best practices, refactoring, software design, maintenance, clean code, performance, efficiency, bug prevention, code quality, standards, development

---

# 3.5.2 Always use reset when resetting values in linked lists
**Severity:** Informational  
**Context:** LinkedList.sol#L59, LinkedList.sol#L230  
**Description:** In the two linked list libraries, the reset function must erase an existing value from the linked list. For the first list, this is done by setting the value to its default, and for the second list, this is done by setting the value to its default as well. In both cases, the same logic can be accomplished by instead calling reset, which is more consistent with the rest of the codebase.  
**Recommendation:** Instead of manually setting values to their defaults, use the reset keyword.  
**Clave:** Fixed with 2bba7a5e.  
**CantinaManaged:** Verified.
