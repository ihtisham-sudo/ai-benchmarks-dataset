# Use Named Constants for Improved Readability

**Severity:** info
**Auditor:** Cantina
**Protocol:** SuperseedToken
**Keywords:** named constants, code clarity, maintainability, hardcoded values, meaningful identifiers, constant definition, readability, prevent errors, improvement, best practices, solidity, smart contracts, token management, code quality, software development, programming, refactoring, code review, commit, verification

---

# Use Named Constants for Improved Readability
**Severity:** Informational  
**Context:** SuperseedToken.sol  
**Description:** Named constants enhance code clarity and maintainability by replacing hardcoded values with meaningful identifiers.  
**Recommendation:** Define \u0060TEN_BILLION_TOKENS\u0060 as a constant:  
\u0060\u0060\u0060solidity
uint256 internal constant TEN_BILLION_TOKENS = 10_000_000_000e18;
\u0060\u0060\u0060
Use this constant instead of directly writing the value to improve readability and prevent errors.  
**Superseed:** Fixed in commit 9cc97c94.  
**Cantina Managed:** Fix verified.
PAGE END
