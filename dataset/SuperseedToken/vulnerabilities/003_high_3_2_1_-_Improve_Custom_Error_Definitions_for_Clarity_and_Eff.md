# 3.2.1 - Improve Custom Error Definitions for Clarity and Efficiency

**Severity:** high
**Auditor:** Cantina
**Protocol:** SuperseedToken
**Keywords:** Gas Optimization, Custom Errors, Bytecode Size, Clarity, Efficiency, Structured Parameters, Revert, Error Handling, Smart Contract, Solidity, TokenClaim, Merkle Root, Zero Balance, Input Validation, Error Messages, Cost-Efficient, Smart Contract Optimization, Code Quality, Best Practices, Development

---

# 3.2 Gas Optimization

### 3.2.1 Improve Custom Error Definitions for Clarity and Efficiency
- **Severity:** Gas Optimization
- **Context:** TokenClaim.sol#L35, TokenClaim.sol#L82, TokenClaim.sol#L92
- **Description:** The InvalidInput error currently includes a string parameter, which increases bytecode size and provides no significant advantage over using a standard revert with a string message.
- **Recommendation:** Instead of using a string parameter, define multiple custom errors with structured and informative parameters. This improves clarity while reducing bytecode size. For example:
    \u0060\u0060\u0060solidity
    error MerkleRootCannotBeEmpty();
    error ZeroBalanceForProvidedToken(address token);
    error InputAmountCannotBeZero();
    \u0060\u0060\u0060
  By using structured parameters, errors become more meaningful and cost-efficient while maintaining clarity.
- **Superseed:** Fixed in commit 69e15ade.
- **CantinaManaged:** Fix verified.

## 3.3 Informational

### 3.3.1 ERC20 import is redundant
- **Severity:** Informational
- **Context:** SuperseedToken.sol#L20
- **Description:** The SuperseedToken contract imports multiple ERC20 extensions: ERC20, ERC20Burnable, AccessControl, ERC20Permit, ERC20Votes which under the hood already use the original ERC20 contract, making it redundant.
- **Recommendation:** Remove the ERC20 import:
    \u0060\u0060\u0060solidity
    - contract SuperseedToken is ERC20, ERC20Burnable, AccessControl, ERC20Permit, ERC20Votes {
    + contract SuperseedToken is ERC20Burnable, AccessControl, ERC20Permit, ERC20Votes {
    \u0060\u0060\u0060
- **Superseed:** Fixed in commit 9cc97c94.
- **CantinaManaged:** Fix verified.

### 3.3.2 Avoid Unnecessary Use of SafeERC20 for SuperseedToken
- **Severity:** Informational
- **Context:** TokenClaim.sol#L14, TokenClaim.sol#L75
- **Description:** Since SuperseedToken strictly follows the ERC20 standard and reverts on failed transfers, the safety checks provided by the SafeERC20 library are unnecessary.
- **Recommendation:** Use direct ERC20 transferFrom call to avoid unnecessary overhead.
- **Superseed:** Fixed in commit 69e15ade.
- **CantinaManaged:** Fix verified.
