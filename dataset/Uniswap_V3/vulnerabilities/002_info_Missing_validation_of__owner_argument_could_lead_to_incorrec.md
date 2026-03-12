# Missing validation of _owner argument could lead to incorrect event emission

**Severity:** info
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** Uniswap, event emission, input validation, setOwner, owner, contract state, monitoring, OwnerChanged, address, configuration functions, user confusion, audit, logging, smart contract, Ethereum, security, functionality, state change, contract behavior, code inspection

---

# Missing validation of _owner argument could lead to incorrect event emission

**Severity:** Informational  
**Difficulty:** High  
**Type:** Auditing and Logging  
**Finding ID:** TOB-UNI-002  
**Target:** UniswapV3Factory.sol  

Because the \u0060setOwner\u0060 lacks input validation, the owner can be updated to the existing owner. Although such an update wouldn’t change the contract state, it would emit an event falsely indicating the owner had been changed.  

\u0060\u0060\u0060solidity
function setOwner(address _owner) external override {     
    require(msg.sender == owner, \u0027OO\u0027);     
    emit OwnerChanged(owner, _owner);     
    owner = _owner;     
}
\u0060\u0060\u0060
*Figure 2.1: setOwner in UniswapV3Factory.sol.*  

Alice has set up monitoring of the \u0060OwnerChanged\u0060 event to track transfers of the owner role. Bob, the current owner, calls \u0060setOwner\u0060 to update the owner to his address (not actually making a change). Alice is notified that the owner was changed but upon closer inspection discovers it was not.  

Short term, add a check ensuring that the \u0060_owner\u0060 argument does not equal the existing owner.  

Long term, carefully inspect the code to ensure that configuration functions do not allow a value to be updated as the existing value. Such updates are not inherently problematic but could cause confusion among users monitoring the events.  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 23
