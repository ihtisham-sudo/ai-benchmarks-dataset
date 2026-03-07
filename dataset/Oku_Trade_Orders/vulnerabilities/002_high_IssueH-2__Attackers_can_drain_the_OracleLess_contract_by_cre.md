# IssueH-2: Attackers can drain the OracleLess contract by creating an order with a malicious token In and executing it with a malicious target.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** OracleLess, ERC20, malicious token, createOrder, fillOrder, target, txData, attack, exploit, vulnerability, drain, contract, approve, transfer, WETH, USDT, whitelist, mitigation, function, attack path

---

# IssueH-2: Attackers can drain the OracleLess contract by creating an order with a malicious token In and executing it with a malicious target.

Source: [GitHub Issue #357](https://github.com/sherlock-audit/2024-11-oku-judging/issues/357)  
Found by: 0xaxaxa, BugPull, Ragnarok, whitehair0330

## Summary
In the OracleLess contract, the createOrder() function does not verify whether the tokenIn is a legitimate ERC20 token, allowing attackers to create an order with a malicious token. Additionally, the fillOrder() function does not check if the target and txData are valid, enabling attackers to execute their order with a malicious target and txData.

## Root Cause
The OracleLess.createOrder() function does not verify whether tokenIn is a legitimate ERC20 token. Additionally, the OracleLess.fillOrder() function does not check if target and txData are valid.

## Internal pre-conditions

## External pre-conditions

## Attack Path
Let\u0027s consider the following scenario:
1. Alice, the attacker, creates a malicious token.
2. Alice creates an order with her malicious token:
   - tokenIn: Alice\u0027s malicious token
   - tokenOut: WETH
• minAmountOut: 0  
3. Alice calls the fillOrder() function to execute her malicious order, setting parameters as follows:  
   • target: addressofUSDT  
   • txData: transfer all USDT in the OracleLess contract to Alice.  
   \u0060\u0060\u0060solidity
   function fillOrder(
       ...
       (uint256 amountOut, uint256 tokenInRefund) = execute(
           target,
           txData,
           order
       );
       ...
   }
   \u0060\u0060\u0060  
   • At line 118 of the fillOrder() function, execute() is invoked:  
   \u0060\u0060\u0060solidity
   function execute(
       address target,
       bytes calldata txData,
       Order memory order
   ) internal returns (uint256 amountOut, uint256 tokenInRefund) {
       // update accounting
       uint256 initialTokenIn = order.tokenIn.balanceOf(address(this));
       uint256 initialTokenOut = order.tokenOut.balanceOf(address(this));
       // approve
       order.tokenIn.safeApprove(target, order.amountIn);
       // perform the call
       (bool success, bytes memory reason) = target.call(txData);
       if (!success) {
           revert TransactionFailed(reason);
       }
       uint256 finalTokenIn = order.tokenIn.balanceOf(address(this));
       require(finalTokenIn >= initialTokenIn - order.amountIn, "over spend");
       uint256 finalTokenOut = order.tokenOut.balanceOf(address(this));
       require(
           finalTokenOut - initialTokenOut > order.minAmountOut,
           "Too Little Received"
       );
   }
   \u0060\u0060\u0060
amountOut = finalTokenOut - initialTokenOut;  
tokenInRefund = order.amountIn - (initialTokenIn - finalTokenIn);  
}  
– At line 237 of the execute() function, tokenIn.safeApprove() is called.  
Alice made her malicious tokenIn as follows:  
function approve(address spender, uint256 amount) public virtual  
→ override returns (bool) {  
    WETH.transfer(msg.sender, 1);  
    return true;  
}  
This transfers 1 wei of WETH to the OracleLess contract.  
– At line 240, all USDT are transferred to Alice, as target is USDT and txData is  
set to transfer to Alice.  
– At line 251, finalTokenOut - initialTokenOut will be 1, as the contract has  
already received 1 wei. Thus, the require statement will pass since  
order.minAmountOut was set 0.  
As a result, Alice can drain all USDT from the OracleLess contract.  

## Impact  
Attackers can drain the OracleLess contract by using malicious token, target, and txData.  

## PoC  

## Mitigation  
It is recommended to implement a whitelist mechanism for token, target, and txData.  

## Discussion  
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/gfx-labs/oku-custom-order-types/pull/1
