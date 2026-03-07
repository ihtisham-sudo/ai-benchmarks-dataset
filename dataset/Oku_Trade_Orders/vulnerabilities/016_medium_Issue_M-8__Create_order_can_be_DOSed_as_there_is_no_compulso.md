# Issue M-8: Create order can be DOSed as there is no compulsory fee collected during the creation/cancellation of orders

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** DOS, order creation, cancellation, pending orders, maxPendingOrders, refund, gas fee, malicious user, attack path, protocol admin, order limit, economic infeasibility, vulnerability, smart contract, Optimism, Brackets, StopLimit, require statement, function call, asset management

---

# Issue M-8: Create order can be DOSed as there is no compulsory fee collected during the creation/cancellation of orders

Source: [https://github.com/sherlock-audit/2024-11-oku-judging/issues/429](https://github.com/sherlock-audit/2024-11-oku-judging/issues/429)  
Found by: BugPull, krot-0025, xiaoming90, zxriptor  

## Summary
No response  

## Root Cause
No response  

## Internal pre-conditions
No response  

## External pre-conditions
No response  

## Attack Path
Assume that:
- maxPendingOrders is set to 25, which is similar to the value configured in the test script
- minOrderSize is set to 10 USD, which is similar to the value configured in the test script

Bob (malicious user) can spend 250 USD to create 25 orders, which will cause the number of pending orders to reach the maxPendingOrders (25) limit. For each of the orders Bob created, he intentionally configured the order in a way that it will always never be in range. For instance, setting the takeProfit, stopPrice, and/or stopLimitPrice to uint256.max - 1. In this case, no one can fill his orders.
The protocol admin can attempt to delete Bob\u0027s order by calling the \u0060adminCancelOrder\u0060 function to remove Bob\u0027s order from the pending Order Ids to reduce the size. When Bob\u0027s order is canceled, the 10 USD worth of assets will be refunded back to Bob. The issue is that this protocol is intended to be deployed on Optimism as per the Contest’s README where the gas fee is extremely cheap. Thus, Bob can simply use the refunded 10 USD worth of assets and create a new order again. 

Thus, whenever the admin cancels Bob\u0027s order, he can always re-create a new one again. As a result, whenever innocent users attempt to create an order, it will always revert with a “Max Order Count Reached” error.

\u0060\u0060\u0060solidity
https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L444
File: Bracket.sol
444:     function _createOrder(
..SNIP..
462:         require(
463:             pendingOrderIds.length < MASTER.maxPendingOrders(),
464:             "Max Order Count Reached"
465:         );
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L300
File: StopLimit.sol
300:     function _createOrder(
..SNIP..
320:         require(
321:             pendingOrderIds.length < MASTER.maxPendingOrders(),
322:             "Max Order Count Reached"
323:         );
\u0060\u0060\u0060

## Impact

Medium. DOS and broken functionality. This DOS can be repeated infinitely, and the cost of attack is low.

## PoC

No response.

## Mitigation

Consider collecting fees upon creating new orders or canceling existing orders so that attackers will not be incentivized to do so, as it would be economically infeasible.
## Discussion

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/gfx-labs/oku-custom-order-types/pull/1
