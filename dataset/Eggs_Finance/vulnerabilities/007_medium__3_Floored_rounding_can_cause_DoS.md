# .3 Floored rounding can cause DoS

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Eggs Finance
**Keywords:** floored rounding, DoS, eggs, sonic, computed price, conversion, vulnerability, smart contract, solidity, blockchain, attack vector, price manipulation, integer overflow, security, gas limit, reentrancy, audit, testing, decentralized finance, protocol

---

# .3 Floored rounding can cause DoS
**Severity:** MediumRisk  
**Context:** Eggs.sol#L548-L554  
**Description:** We convert between eggs and sonic based on the current computed price, e.g.:
\u0060\u0060\u0060solidity
// Code snippet not provided
\u0060\u0060\u0060
