# 3.5.3 Invalid signature reverts instead of returning value

**Severity:** info
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** zkSync, account abstraction, validation function, boolean return, secp256k1, signature validation, EOAValidator, invalid signature, revert, error handling, linked list library, return value, validation behavior, exit early, smart contract, Ethereum, blockchain, security, functionality, implementation

---

# 3.5.3 Invalid signature reverts instead of returning value
**Severity:** Informational  
**Context:** ValidationHandler.sol#L36-L43  
**Description:** In native zkSync account abstraction, it is intended that the validation function returns a value if validation fails. As part of this, the Clave account\u0027s validation function returns a boolean to indicate if validation succeeds or not. For secp256k1 signature validation specifically, this code is used:
\u0060\u0060\u0060
    revert signature validation
    return value
\u0060\u0060\u0060
In the current EOAValidator implementation, an invalid signature length will lead to the revert being returned as an error. On the other hand, the validation function reverts if the argument is not a valid address in the linked list library. So, invalid signatures will incorrectly revert the validation call instead of causing a return value. Since this deviates from the intended zkSync behavior, the error might not be correctly handled off-chain.  
**Recommendation:** Remove this revert by either changing the validation behavior or by exiting early as follows:
\u0060\u0060\u0060
    exit early
\u0060\u0060\u0060
