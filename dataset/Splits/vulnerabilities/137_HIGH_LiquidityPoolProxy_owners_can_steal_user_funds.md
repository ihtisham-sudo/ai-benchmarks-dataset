# LiquidityPoolProxy owners can steal user funds

**Severity:** HIGH
**Auditor:** TrailOfBits

---

## Timing

## Difficulty: Medium

### Description
The LiquidityPoolProxy contract implements the IOceanPrimitive interface and can integrate with the Ocean contract as a primitive. The proxy contract calls into an implementation contract to perform deposit, swap, and withdrawal operations (Figure 2.1).

```solidity
function swapOutput(uint256 inputToken, uint256 inputAmount)
public
view
override
returns (uint256 outputAmount)
{
    (uint256 xBalance, uint256 yBalance) = _getBalances();
    outputAmount = implementation.swapOutput(
        xBalance,
        yBalance,
        inputToken == xToken ? 0 : 1,
        inputAmount
    );
}
```
Figure 2.1: The swapOutput() function in LiquidityPoolProxy.sol#L39–47

However, the owner of a LiquidityPoolProxy contract can perform the privileged operation of changing the underlying implementation contract via a call to `setImplementation` (Figure 2.2). The owner could thus replace the underlying implementation with a malicious contract to steal user funds.

```solidity
function setImplementation(address _implementation)
external
onlyOwner
{
}
implementation = ILiquidityPoolImplementation(_implementation);
```
Figure 2.2: The setImplementation() function in LiquidityPoolProxy.sol#L28–33

This level of privilege creates a single point of failure in the system. It increases the likelihood that a contract’s owner will be targeted by an attacker and incentivizes the owner to act maliciously.

### Exploit Scenario
Alice deploys a LiquidityPoolProxy contract as an Ocean primitive. Eve gains access to Alice’s machine and upgrades the implementation to a malicious contract that she controls. Bob attempts to swap USD 1 million worth of shDAI for shUSDC by calling `computeOutputAmount`. Eve’s contract returns 0 for `outputAmount`. As a result, the malicious primitive’s balance of shDAI increases by USD 1 million, but Bob does not receive any tokens in exchange for his shDAI.

### Recommendations
- **Short term**: Document the functions and implementations that LiquidityPoolProxy contract owners can change. Additionally, split the privileges provided to the owner role across multiple roles to ensure that no one address has excessive control over the system.
- **Long term**: Develop user documentation on all risks associated with the system, including those associated with privileged users and the existence of a single point of failure.
