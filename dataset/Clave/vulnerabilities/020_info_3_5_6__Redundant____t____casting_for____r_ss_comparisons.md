# 3.5.6  Redundant ✉✐♥t✶✻✵ casting for ❛❞❞r❡ss comparisons

**Severity:** info
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** redundant, casting, address, comparisons, Solidity, LinkedList, HookManager, SocialRecoveryModule, codebase, simplification, value comparison, type casting, optimization, best practices, smart contracts, development, code quality, clean code, refactoring, issues

---

# 3.5.6  Redundant ✉✐♥t✶✻✵ casting for ❛❞❞r❡ss comparisons
**Severity:** Informational  
**Context:** LinkedList.sol, HookManager.sol, SocialRecoveryModule.sol  
**Description:** Throughout the codebase, there are a few instances of two ❛❞❞r❡ss values being cast to ✉✐♥t✶✻✵ for the purpose of comparing their values. Since it is possible to compare ❛❞❞r❡ss values directly in Solidity, these castings are technically redundant.  
**Recommendation:** Consider simplifying the codebase by removing these redundant ✉✐♥t✶✻✵ casts.  
**Clave:** Fixed with commits 83c114a5 and 2bba7a5e.  
**CantinaManaged:** Verified.
