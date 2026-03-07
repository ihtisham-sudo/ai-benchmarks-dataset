# IssueM-5: InOracleLess.createOrder() fee-Bips value validation is missing

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** fee Bips, validation, createOrder, execute, malicious user, blacklist, cancelOrder, transfer, DoS, pending Order Ids, queue size, gas usage, input validation, OracleLess, USDC, 1 wei orders, protocol team, commit, PR, sherlock-audit

---

# IssueM-5: InOracleLess.createOrder() fee-Bips value validation is missing

Source: [GitHub Issue #277](https://github.com/sherlock-audit/2024-11-oku-judging/issues/277)  
Found by: phoenixv110  

## Summary  
The max value of fee Bips should be <= 10000. But this validation is missing in createOrder(). All such orders where fee Bips is > 10000 will revert in execute() method. A malicious user can create 100s of such orders which never execute even if the price conditions are met. It can use USDC as token In and blacklist itself so that _cancelOrder() also reverts. As _cancelOrder() tries to transfer token Into the user. If the receiver is a blacklisted user then transfer will fail. This way the malicious user can create 1 wei orders which can neither execute nor be cancellable.  
[OracleLess.sol](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/OracleLess.sol#L38C5-L67C6)  

## Root Cause  
Missing fee Bips input validation in createOrder()  

## Internal pre-conditions  
No response  

## External pre-conditions  
No response  

## Attack Path  
No response
## Impact
Such orders will exist in the pending Order Ids which cannot be deleted from the queue. These orders can increase the queue size until the max gas usage limit is reached. Which will DoS all other orders.
## PoC
No response
## Mitigation
Add the check fee Bips <= 10000 in createOrder() of OracleLess.sol.
## Discussion
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/gfx-labs/oku-custom-order-types/pull/1](https://github.com/gfx-labs/oku-custom-order-types/pull/1)
