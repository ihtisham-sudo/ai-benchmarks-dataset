# Informational

**Severity:** info
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** ServiceManager, validateSignatures, ECDSA, recover, signatures, address, recoveredSigner, function, solidity, messageHash, operator, security, signature verification, smart contract, Ethereum, blockchain, decentralized, audit, best practices, code review

---

# Informational
### Severity: Informational
**Context:** ServiceManager.sol

**Description:** In the validateSignatures function, operator signatures are recovered with:
\u0060\u0060\u0060solidity
address recoveredSigner = ECDSA.recover(messageHash, signatures[i]);
\u0060\u0060\u0060
