# Gas Optimization

**Severity:** low
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** gas optimization, solidity, smart contract, OpenZeppelin, EOAValidator, function simplification, require statement, redundant code, address, msg.sender, linked lists, error handling, code efficiency, contract security, function return, optimization, code review, commit, verification, best practices

---

# Gas Optimization
### Severity: Gas Optimization
### Context: EOAValidator.sol#L25
### Description: OpenZeppelin\u0027s \u0060tr2\u0060 reads as follows:
\u0060\u0060\u0060
function s() public view returns (address) {
    require(msg.sender == s);
    return s;
}
\u0060\u0060\u0060
The function \u0060s\u0060 checks that the module is appropriately present/absent from the account. This works because the \u0060msg.sender\u0060 updates the linked lists before calling \u0060s\u0060 or \u0060s\u0060.

- Clave: Fixed with commit 328614dc.
- CantinaManaged: Verified.

### 3.4.1 \u0060tr2\u0060 can be simplified
\u0060\u0060\u0060solidity
function s() public view returns (address) {
    require(msg.sender == s);
    return s;
}
\u0060\u0060\u0060
\u0060tr2\u0060 calls \u0060tr2\u0060 and again checks the error to return \u0060s\u0060 if an error is returned:
\u0060\u0060\u0060solidity
require(s == s);
\u0060\u0060\u0060
However, this check is redundant: if \u0060s\u0060 is equal to \u0060s\u0060, \u0060tr2\u0060 always returns \u0060s\u0060 for \u0060s\u0060.

Update \u0060EOAValidator.sol#L21-L25\u0060 as follows:
\u0060\u0060\u0060solidity
function s() public view returns (address) {
    return s;
}
\u0060\u0060\u0060
