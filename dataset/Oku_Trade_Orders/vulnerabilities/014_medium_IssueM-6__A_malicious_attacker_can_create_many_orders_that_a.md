# IssueM-6: A malicious attacker can create many orders that are not cancelable.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** malicious, orders, cancelable, token, contract, revert, IERC20, OracleLess, admin, grift, protocol, gas, whitelist, transfer, refund, recipient, amountIn, attack, pre-conditions, impact

---

# IssueM-6: A malicious attacker can create many orders that are not cancelable.

Source: [GitHub Issue #331](https://github.com/sherlock-audit/2024-11-oku-judging/issues/331)  
Found by: covey0x07, vinica_boy  

## Summary  
When a user creates an order in the OracleLess contract, he can add a malicious token contract that reverts when tokens are transferred from the OracleLess contract. This order can\u0027t be canceled by admin. A malicious attacker can create this kind of order as many as he can to grift the protocol.

## Root Cause  
At OracleLess.sol#L38, there are no restrictions for tokenIn. Any contract that implements IERC20 can be tokenIn.

## Internal pre-conditions  
N/A  

## External pre-conditions  
N/A  

## Attack Path  
- Alice creates a malicious token contract that reverts if token is transferred from the OracleLess contract.  
- Alice creates orders by using this fake token contract.  
- This order can\u0027t be cancelable as it reverts at L160.  
\u0060\u0060\u0060solidity
function _cancelOrder(Order memory order) internal returns (bool) {
    // refund tokenIn amountIn to recipient
    order.tokenIn.safeTransfer(order.recipient, order.amountIn);
}
\u0060\u0060\u0060
## Impact
- Amalicousattackercangrieftheprotocolbymakingalotofuncancelableorders.
- All users of the protocol wastes significant gas in whenevertheyfill or cancel orders.
## Mitigation
It is recommendedtoaddmechanismtowhitelisttokens.
## Discussion
sherlock-admin2  
TheprotocolteamfixedthisissueinthefollowingPRs/commits:  
https://github.com/gfx-labs/oku-custom-order-types/pull/1
