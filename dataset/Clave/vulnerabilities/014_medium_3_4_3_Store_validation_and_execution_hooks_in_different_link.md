# 3.4.3 Store validation and execution hooks in different linked lists

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** gas optimization, hook, validation hook, execution hook, linked list, iteration, performance, smart contract, efficiency, storage, recommendation, implementation, case handling, code optimization, solidity, contract design, data structure, hook management, resource management, best practices

---

# 3.4.3 Store validation and execution hooks in different linked lists
- **Severity:** Gas Optimization
- **Context:** HookManager.sol#L108-L109
- **Description:** A hook can be a validation hook, an execution hook or both. r✉♥❱❛❧✐❞❛t✐♦♥❍♦♦❦s✭✮ and r✉♥❊①❡❝✉t✐♦♥❍♦♦❦s✭✮ iterate through a linked list storing hooks to find validation and execution hooks respectively. Storing validation and execution hooks in different lists will save gas for r✉♥❱❛❧✐❞❛t✐♦♥❍♦♦❦s✭✮ and r✉♥❊①❡❝✉t✐♦♥❍♦♦❦s✭✮.
- **Recommendation:** Consider storing validation and execution hooks in different lists. If you decide to implement this change, be careful of the case where a hook is both a validation and execution hook. In this case, that hook has to be added to both lists.
- **Clave:** Fixed in PR 787.
- **CantinaManaged:** Verified.
