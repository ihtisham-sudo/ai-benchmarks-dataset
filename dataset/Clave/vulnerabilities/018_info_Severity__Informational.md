# Severity: Informational

**Severity:** info
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** social recovery, helper functions, optimization, smart contract, Solidity, view function, code reuse, functionality, logic, main function, efficiency, contract design, best practices, refactoring, modularity, readability, maintenance, performance, development, audit

---

# Severity: Informational
### Context: SocialRecoveryModule.sol#L94-L104
### Description: The contract contains the following function:
\u0060\u0060\u0060solidity
function socialRecovery(uint256 _id) public view returns (uint256) {
    // some logic here
}
\u0060\u0060\u0060
Also, this contract has two helper functions with the following logic:
\u0060\u0060\u0060solidity
function someHelperFunction() public view returns (uint256) {
    // some logic here
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function anotherHelperFunction() public view returns (uint256) {
    // some logic here
}
\u0060\u0060\u0060
### Recommendation: Since these helper functions contain similar logic to the main function, consider utilizing them there:
\u0060\u0060\u0060solidity
function mainFunction() public view returns (uint256) {
    // some logic here
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function anotherMainFunction() public view returns (uint256) {
    // some logic here
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function someOtherFunction() public view returns (uint256) {
    // some logic here
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function finalFunction() public view returns (uint256) {
    // some logic here
}
\u0060\u0060\u0060

### Clave: Fixed with commit bcd0a6d9.
### CantinaManaged: Verified.
