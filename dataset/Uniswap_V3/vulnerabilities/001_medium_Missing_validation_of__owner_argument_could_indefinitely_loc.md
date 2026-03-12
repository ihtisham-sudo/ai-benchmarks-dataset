# Missing validation of _owner argument could indefinitely lock owner role

**Severity:** medium
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** Uniswap, V3, Factory, contract, owner, validation, constructor, setOwner, address, msg.sender, ownership, redeploy, reputational damage, fee amount, tick spacing, input validation, error handling, security, smart contract, Ethereum

---

# Missing validation of _owner argument could indefinitely lock owner role

**Severity:** Medium  
**Difficulty:** High  
**Type:** Data Validation  
**Finding ID:** TOB-UNI-001  
**Target:** UniswapV3Factory.sol  

A lack of input validation of the _owner argument in both the constructor and setOwner functions could permanently lock the owner role, requiring a costly redeploy.  

\u0060\u0060\u0060solidity
constructor(address _owner) {   
    owner = _owner;   
    emit OwnerChanged(address(0), _owner);   

    _enableFeeAmount(600, 12);   
    _enableFeeAmount(3000, 60);   
    _enableFeeAmount(9000, 180);   
}   
\u0060\u0060\u0060
*Figure 1.1: constructor in UniswapV3Factory.sol.*  

\u0060\u0060\u0060solidity
function setOwner(address _owner) external override {     
    require(msg.sender == owner, \u0027OO\u0027);     
    emit OwnerChanged(owner, _owner);     
    owner = _owner;     
}     
\u0060\u0060\u0060
*Figure 1.2: setOwner in UniswapV3Factory.sol.*  

The constructor calls _enableFeeAmount to add three available initial fees and tick spacings. This means that, as far as a regular user is concerned, the contract will work, allowing the creation of pairs and all functionality needed to start trading. In other words, the incorrect owner role may not be noticed before the contract is put into use.  

The following functions are callable only by the owner:  
- UniswapV3Factory.enableFeeAmount  
  - Called to add more fees with specific tick spacing.  
- UniswapV3Pair.setFeeTo  
  - Called to update the fees’ destination address.  
- UniswapV3Pair.recover  
  - Called to withdraw accidentally sent tokens from the pair.  
- UniswapV3Factory.setOwner  
  - Called to change the owner.  

To resolve an incorrect owner issue, Uniswap would need to redeploy the factory contract and re-add pairs and liquidity. Users might not be happy to learn of these actions.  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 21

could lead to reputational damage. Certain users could also decide to continue using the original factory and pair contracts, in which owner functions cannot be called. This could lead to the concurrent use of two versions of Uniswap, one with the original factory contract and no valid owner and another in which the owner was set correctly.

Trail of Bits identified four distinct cases in which an incorrect owner is set:  
- Passing address(0) to the constructor  
- Passing address(0) to the setOwner function  
- Passing an incorrect address to the constructor  
- Passing an incorrect address to the setOwner function.  

Alice deploys the UniswapV3Factory contract but mistakenly passes address(0) as the _owner.  

Several improvements could prevent the four abovementioned cases:  
- Designate msg.sender as the initial owner, and transfer ownership to the chosen owner after deployment.  
- Implement a two-step ownership-change process through which the new owner needs to accept ownership.  
- If it needs to be possible to set the owner to address(0), implement a renounceOwnership function.  

Long term, use Slither, which will catch the missing address(0) check, and consider using two-step processes to change important privileged roles.  

© 2021 Trail of Bits
