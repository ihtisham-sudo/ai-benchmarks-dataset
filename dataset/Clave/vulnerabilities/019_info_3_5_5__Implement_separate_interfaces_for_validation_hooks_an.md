# 3.5.5  Implement separate interfaces for validation hooks and execution hooks

**Severity:** info
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** validation hooks, execution hooks, IHook.sol, interfaces, function implementation, dummy functions, hook development, Clave accounts, simplification, recommendation, pure validation hooks, pure execution hooks, code structure, software design, interface segregation, hook compatibility, development efficiency, PR 787, verification, code quality

---

# 3.5.5  Implement separate interfaces for validation hooks and execution hooks
**Severity:** Informational  
**Context:** IHook.sol  
**Description:** Clave accounts are compatible with two types of hooks: validation hooks and execution hooks. Both of these hooks use the same ■❍♦♦❦ interface, which means both hooks must implement functions that they may not actually use. Pure validation hooks will need to implement dummy ♣r❡❊①❡❝✉✲ t✐♦♥❍♦♦❦✭✮/♣♦st❊①❡❝✉t✐♦♥❍♦♦❦✭✮ functions, while pure execution hooks will need to implement a dummy ✈❛❧✐❞❛t✐♦♥❍♦♦❦✭✮ function.  
**Recommendation:** Consider simplifying hook development by splitting these functions into two separate interfaces: ■❱❛❧✐❞❛t✐♦♥❍♦♦❦✳s♦❧ and ■❊①❡❝✉t✐♦♥❍♦♦❦✳s♦❧.  
**Clave:** Fixed with PR 787.  
**CantinaManaged:** Verified.
