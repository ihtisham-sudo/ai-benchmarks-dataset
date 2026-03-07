# Sentinel Pointing to Itself

**Severity:** high
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** linked list, sentinel, empty, remove, head, tail, isEmpty, removeValidator, removeOwner, accounts, validators, owners, bricking, functions, update, solidity, bytes, elements, incorrect, case

---

# Sentinel Pointing to Itself
### Severity: High Risk
### Context: LinkedList.sol#L152, LinkedList.sol#L323
Description: An empty linked list can have the sentinel element pointing to itself if all elements are removed using \u0060remove\u0060. In this case, the \u0060head\u0060 for bytes linked list, and \u0060tail\u0060 for bytes linked list. However, \u0060isEmpty\u0060 doesn\u0027t account for this case, and will incorrectly consider the list as non-empty.

As a consequence, the \u0060removeValidator\u0060 and \u0060removeOwner\u0060 functions will not correctly prevent users from bricking their accounts by removing all validators/owners.

- Update \u0060isEmpty\u0060 as follows:
\u0060\u0060\u0060solidity
return head == tail;
\u0060\u0060\u0060
- Update \u0060remove\u0060 as follows:
\u0060\u0060\u0060solidity
return head == tail;
\u0060\u0060\u0060

Clave: Fixed with commit 2bba7a5e.  
CantinaManaged: Verified.
