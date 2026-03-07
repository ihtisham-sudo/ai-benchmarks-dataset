# Issue M-1: Bracket and Stop Limit contracts are vulnerable to DoS attacks.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** DoS, vulnerability, Bracket contracts, Stop Limit contracts, uncancellable orders, pending orders, Automation Master, gas limit, admin cancellation, inexecutable order, USDT, recipient address, address(0), transfer, ERC20, maxPendingOrders, attack path, impact, mitigation, protocol team

---

# Issue M-1: Bracket and Stop Limit contracts are vulnerable to DoS attacks.

Source: [https://github.com/sherlock-audit/2024-11-oku-judging/issues/72](https://github.com/sherlock-audit/2024-11-oku-judging/issues/72)  
Found by Contest-Squad, vinica_boy  

## Summary  
Users can create uncancellable orders and brick the Bracket and Stop Limit contracts. Both contracts have an upper limit for their pending orders defined in the Automation Master contract. This will ensure that the length of the pendingOrderIds array won\u0027t grow indefinitely and it can be traversed with the current gas block limit. Also, the admin can cancel orders if users create an inexecutable order which only takes space in the array. But there is a case where orders won\u0027t be possible to be cancelled by admin when the tokenIn is USDT which will allow users to fulfill the supported amount of orders with an order that will never be in range to be executed. For example, a bracket order for WETH with stopPrice=0 and takeProfit=100000 USD.

## Root Cause  
In \u0060_cancelOrder()\u0060, the tokenIn amount is sent back to the recipient:  
\u0060\u0060\u0060solidity
order.tokenIn.safeTransfer(order.recipient, order.amountIn)
\u0060\u0060\u0060  
But this call will always revert for \u0060order.recipient=address(0)\u0060. Here is the \u0060_transfer()\u0060 function of USDT:  
\u0060\u0060\u0060solidity
function _transfer(address sender, address recipient, uint256 amount) internal virtual {
    require(sender != address(0), "ERC20: transfer from the zero address");
    require(recipient != address(0), "ERC20: transfer to the zero address");
    _beforeTokenTransfer(sender, recipient, amount);
    _balances[sender] = _balances[sender].sub(amount, "ERC20: transfer amount exceeds balance");
    _balances[recipient] = _balances[recipient].add(amount);
    emit Transfer(sender, recipient, amount);
}
\u0060\u0060\u0060  
And when an order is created, the recipient can be set to \u0060address(0)\u0060 since there are no constraints.
_cancelOrder(): https://github.com/sherlock-audit/2024-11-oku/blob/ee3f781a73d65e3fb452c9a44eb1337c5cfdbd6/oku-custom-order-types/contracts/automatedTrigger/B racket.sol#L501C1-L520C6

**Internal pre-conditions**  
N/A

**External pre-conditions**  
N/A

**Attack Path**  
User create enough orders with recipient set to address(0) to make the length of pendingOrderIds reach AutomationMaster.maxPendingOrders. We assume that this does not lead to DoS and array elements can be traversed within the block gas limit. Admin cannot cancel such orders and can only increase the maxPendingOrders. This process can happen again and again until the size of pendingOrderIds and maxPendingOrders reach numbers for which gas cost to traverse the whole array would be more than the current gas block limit.

**Impact**  
Complete DoS for Bracket and Stop Limit contracts.

**PoC**  
N/A

**Mitigation**  
Ensure order recipient to be different than address(0).

**Discussion**  
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/gfx-labs/oku-custom-order-types/pull/1
