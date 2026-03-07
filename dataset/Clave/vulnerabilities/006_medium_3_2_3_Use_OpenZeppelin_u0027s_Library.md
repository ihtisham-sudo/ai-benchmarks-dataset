# 3.2.3 Use OpenZeppelin\u0027s Library

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** ERC20, OpenZeppelin, library, transfer, transferFrom, USDT, tokens, specification, failure, return, revert, function, recommendation, code, verification, PR 716, context, managed, security, best practices

---

# 3.2.3 Use OpenZeppelin\u0027s Library
**Severity:** Medium Risk  
**Context:** ERC20Paymaster.sol#L113, ERC20Paymaster.sol#L200  
**Description:** Some ERC20 tokens may not follow the entire ERC20 specification. For example, transfer and transferFrom are expected to return true and revert on any failure, but USDT doesn\u0027t return any value. OpenZeppelin\u0027s library handles these cases.  
**Recommendation:** Consider using OpenZeppelin\u0027s library\u0027s transfer and transferFrom functions instead of calling transfer and transferFrom on the token directly.  
**Clave:** Fixed with PR 716.  
**Cantina Managed:** Verified.
