# IssueM-11: Malicious users can create Order with 0 amount and make DOS for all

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** malicious users, create order, zero amount, DOS, block users, fill order, cancel order, block gas limit, ArrayMutation, pending orders, gas limit, procure tokens, emit OrderCreated, require check, mitigation, security, smart contract, vulnerability, exploit, protocol

---

# IssueM-11: Malicious users can create Order with 0 amount and make DOS for all

Source: [GitHub Issue #731](https://github.com/sherlock-audit/2024-11-oku-judging/issues/731)  
Found by: sakibcy  

## Summary  
Malicious users can create Order with 0 amount and can cause DOS / block users to fill Order, cancel Order.  

## Impact  
Malicious users will create huge numbers of orders with 0 amount In. Now if anyone wants to fill Order or cancel Order they cannot do it because:  
- Due to the block gas limit, there is a clear limitation in the amount of operation that can be handled in an Array.  
- ArrayMutation::removeFromArray is called on fillOrder, cancelOrder functions.  
- Now because the malicious users have created a huge amount of orders with 0 amount,  
- When normal users go to fill Order or cancel Order they simply run out of gas while iterating a huge array of pending Order Ids.  
- This makes them and everyone impossible to do any further action on fill Order, cancel Order.  

## PoC  
\u0060\u0060\u0060solidity
OracleLess::createOrder
function createOrder(
    IERC20 tokenIn,
    IERC20 tokenOut,
    uint256 amountIn,
    uint256 minAmountOut,
    address recipient,
    uint16 feeBips,
    bool permit,
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
bytes calldata permitPayload
) external override returns (uint96 orderId) {
   //procure tokens
   procureTokens(tokenIn, amountIn, recipient, permit, permitPayload);
   //construct and store order
   orderId = MASTER.generateOrderId(recipient);
   orders[orderId] = Order({
     orderId: orderId,
     tokenIn: tokenIn,
     tokenOut: tokenOut,
     amountIn: amountIn,
     minAmountOut: minAmountOut,
     recipient: recipient,
     feeBips: feeBips
   });
   //store pending order
   pendingOrderIds.push(orderId);
   emit OrderCreated(orderId);
}
\u0060\u0060\u0060

## Mitigation
We can add checks for the createOrder function something like this:
\u0060\u0060\u0060solidity
require(amountIn > 0, "amount should be greater than 0")
\u0060\u0060\u0060
Or can add code like the other Contracts:
\u0060\u0060\u0060solidity
MASTER.checkMinOrderSize(tokenIn, amountIn);
\u0060\u0060\u0060

## Discussion
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/gfx-labs/oku-custom-order-types/pull/1](https://github.com/gfx-labs/oku-custom-order-types/pull/1)
PAGE END
