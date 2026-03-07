# n33k - Stale inflationMultiplier in L1ECOBridge

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Eco Op Bridge 
**Keywords:** L1ECOBridge, inflationMultiplier, rebase, Ethereum, ERC20, deposit, withdrawal, token amounts, stale value, inconsistent results, transferFrom, L2ECOBridge, synchronous update, impact, attacker, steal tokens, L1 bridge, larger value, getPastLinearInflation, manual review

---

n33k

high

# Stale inflationMultiplier in L1ECOBridge

## Summary 

\u0060L1ECOBridge::inflationMultiplier\u0060 is updated through \u0060L1ECOBridge::rebase\u0060 on Ethereum, and it is used in \u0060_initiateERC20Deposit\u0060 and \u0060finalizeERC20Withdrawal\u0060 to convert between token amount and \u0060_gonsAmount\u0060. However, if \u0060rebase\u0060 is not called in a timely manner, the \u0060inflationMultiplier\u0060 value can be stale and inconsistent with the value of L1 ECO token during transfer, leading to incorrect token amounts in deposit and withdraw.

## Vulnerability Detail

The \u0060inflationMultiplier\u0060 value is updated in \u0060rebase\u0060 with an independent transaction on L1 as shown below:

\u0060\u0060\u0060solidity
    function rebase(uint32 _l2Gas) external {
        inflationMultiplier = IECO(l1Eco).getPastLinearInflation(block.number);
\u0060\u0060\u0060

However, in both \u0060_initiateERC20Deposit\u0060, \u0060transferFrom\u0060 is called before the \u0060inflationMultiplier\u0060 is used, which can lead to inconsistent results if \u0060rebase\u0060 is not called on time for the \u0060inflationMultiplier\u0060 to be updated. The code snippet for \u0060_initiateERC20Deposit\u0060 is as follows:

\u0060\u0060\u0060solidity
        IECO(_l1Token).transferFrom(_from, address(this), _amount);
        _amount = _amount * inflationMultiplier;
\u0060\u0060\u0060
\u0060finalizeERC20Withdrawal\u0060 has the same problem.

\u0060\u0060\u0060solidity
        uint256 _amount = _gonsAmount / inflationMultiplier;
        bytes memory _ecoTransferMessage = abi.encodeWithSelector(IERC20.transfer.selector,_to,_amount);
\u0060\u0060\u0060

The same problem does not exist in L2ECOBridge. Because the L2 rebase function updates inflationMultiplier and rebase l2Eco token synchronously.

\u0060\u0060\u0060solidity
    function rebase(uint256 _inflationMultiplier)
        external
        virtual
        onlyFromCrossDomainAccount(l1TokenBridge)
        validRebaseMultiplier(_inflationMultiplier)
    {
        inflationMultiplier = _inflationMultiplier;
        l2Eco.rebase(_inflationMultiplier);
        emit RebaseInitiated(_inflationMultiplier);
    }
\u0060\u0060\u0060

## Impact

The attacker can steal tokens with this.

He can deposit to L1 bridge when he observes a stale larger value and he will receive more tokens on L2.

## Code Snippet

https://github.com/sherlock-audit/2023-05-ecoprotocol/blob/main/op-eco/contracts/bridge/L1ECOBridge.sol#L244-L251

https://github.com/sherlock-audit/2023-05-ecoprotocol/blob/main/op-eco/contracts/bridge/L1ECOBridge.sol#L333-L335

## Tool used

Manual Review

## Recommendation

Calling \u0060IECO(l1Eco).getPastLinearInflation(block.number)\u0060 instead of using \u0060inflationMultiplier\u0060.


