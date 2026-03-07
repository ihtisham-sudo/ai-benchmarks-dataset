# 3.3.2 - ❈▲❆❱❊❴❙❚❖❘❆●❊❴❙▲❖❚ should be subtracted by one

**Severity:** low
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** storage slot, EIP-1967, offset, collision, preimage, contract, ClaveStorage, calculation, verification, bug fix, commit, CantinaManaged, smart contract, data integrity, safety, recommendation, audit, code review, best practices, development

---

# 3.3 Low Risk

### 3.3.1 Unbounded linked list traversals
**Severity:** Low Risk  
**Context:** LinkedList.sol, HookManager.sol, ValidationHandler.sol  
**Description:** The Clave account implementation uses linked lists in various locations, and in some places, these lists are fully traversed. Since there is no maximum size, these traversals can become arbitrarily expensive in terms of gas. In an extreme scenario, a full list traversal will cost more than the block gas limit, and will make some functions impossible to call.  
**Recommendation:** Consider enforcing a maximum size on the account\u0027s linked lists. Alternatively, since out-of-gas issues are very unlikely to happen in normal circumstances, consider simply documenting this behavior as a warning in the front end/comments.  
**Clave:** Acknowledged.  
**CantinaManaged:** Acknowledged.  

### 3.3.2 ❈▲❆❱❊❴❙❚❖❘❆●❊❴❙▲❖❚ should be subtracted by one
**Severity:** Low Risk  
**Context:** ClaveStorage.sol#L5  
**Description:** The ❈❧❛✈❡❙t♦r❛❣❡ library maintains the contract\u0027s ▲❛②♦✉t struct in the storage slot equal to ❦❡❝❝❛❦✷✺✻✭✬❝❧❛✈❡✳❝♦♥tr❛❝ts✳❈❧❛✈❡❙t♦r❛❣❡✬✮. This is similar to how EIP-1967 storage slots are maintained, except that there is an offset of ✲✶ missing in the calculation. The offset is recommended because the resulting value wouldn\u0027t have a known preimage, which decreases the chance of a collision with a compiler storage slot.  
**Recommendation:** Subtract one from the ❈▲❆❱❊❴❙❚❖❘❆●❊❴❙▲❖❚:  
- ✲ ❜②t❡s✸✷ ♣r✐✈❛t❡ ❝♦♥st❛♥t ❈▲❆❱❊❴❙❚❖❘❆●❊❴❙▲❖❚ ❂ ❦❡❝❝❛❦✷✺✻✭✬❝❧❛✈❡✳❝♦♥tr❛❝ts✳❈❧❛✈❡❙t♦r❛❣❡✬✮❀  
- ✰ ❜②t❡s✸✷ ♣r✐✈❛t❡ ❝♦♥st❛♥t ❈▲❆❱❊❴❙❚❖❘❆●❊❴❙▲❖❚ ❂ ❜②t❡s✸✷✭✉✐♥t✷✺✻✭❦❡❝❝❛❦✷✺✻✭✬❝❧❛✈❡✳❝♦♥tr❛❝ts✳❈❧❛✈❡❙t♦r❛❣❡✬✮✮ ✲ ✶✮❀  
**Clave:** Fixed with commit da6b75a3.  
**CantinaManaged:** Verified.  

### 3.3.3 Unsafe ❛❞❞r❡ss casting
**Severity:** Low Risk  
**Context:** ClaveImplementation.sol#L218  
**Description:** In the zkSync ❚r❛♥s❛❝t✐♦♥ struct, the ❢r♦♠, t♦, and ♣❛②♠❛st❡r fields are defined as ✉✐♥t✷✺✻ values, even though they each represent an ❛❞❞r❡ss value (which is equivalent to ✉✐♥t✶✻✵ under-the-hood). As a result, it is possible for these values to overflow if the conversion is not carefully handled. For zkSync\u0027s native transactions, this is not a concern, since the bootloader enforces that no overflow happens. However, an alternative usage of the zkSync ❚r❛♥s❛❝t✐♦♥ struct exists in the ❡①❡❝✉t❡❚r❛♥s❛❝t✐♦♥❋r♦✲ ♠❖✉ts✐❞❡✭✮ function. This function will be called in a transaction originating by another address, so the bootloader will not have inspected any of the values for overflow. So, when this code eventually runs:
## Vulnerability 1
the ❛❞❞r❡ss✭✉✐♥t✶✻✵✭tr❛♥s❛❝t✐♦♥✳t♦✮✮ casting can silently overﬂow. Fortunately, since the full t♦ value
wouldhavebeensignedbytheuser,thereisn\u0027tanydirectwaytoexploitthis. However,itdoesallowodd
behavior and would makemoresensetobedisallowed.
Recommendation: When casting any of the ❚r❛♥s❛❝t✐♦♥ struct values to an address, ensure that no
overﬂowhappens:
- ❢✉♥❝t✐♦♥ ❴s❛❢❡❈❛st❚♦❆❞❞r❡ss✭✉✐♥t✷✺✻ ✈❛❧✉❡✮ ✐♥t❡r♥❛❧ r❡t✉r♥s ✭❛❞❞r❡ss✮ ④
- ✐❢ ✭✈❛❧✉❡ ❃ t②♣❡✭✉✐♥t✶✻✵✮✳♠❛①✮ r❡✈❡rt✭✮❀
- r❡t✉r♥ ❛❞❞r❡ss✭✉✐♥t✶✻✵✭✈❛❧✉❡✮✮❀
