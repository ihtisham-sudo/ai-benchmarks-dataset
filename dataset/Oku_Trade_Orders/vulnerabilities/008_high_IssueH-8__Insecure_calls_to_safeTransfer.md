# IssueH-8: Insecure calls to safeTransfer

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** insecure, safeTransfer, tokens, attack, transfer, protocol, order, user, approve, residual allowance, profit, abuse, functionality, contract, createOrder, modifyOrder, procureTokens, vulnerabilities, exploit, smart contract

---

# IssueH-8: Insecure calls to safeTransfer

From leads to users tokens steal by attacker  
Source: [GitHub Issue #789](https://github.com/sherlock-audit/2024-11-oku-judging/issues/789)  
Found by  
0x37, 0xaxaxa, 0xc0ffEE, Bigsam, Boy2000, BugPull, ChinmayF, John44, KungFuPanda,  
Laksmana, LonWof-Demon, PoeAudits, Ragnarok, Tri-pathi, Xcrypt, Z3R0, bughuntoor,  
c-n-o-t-e, covey0x07, future2_22, gajiknownnothing, hals, iamandreiski, joshuajee,  
lanrebayode77, nikhil840096, phoenixv110, rahim7x, silver_eth, t.aksoy, tobi0x18,  
vinica_boy, whitehair0330, xiaoming90, y51r, zhoo, zxriptor  

## Summary  
The function safeTransferFrom() is used to transfer tokens from user to the protocol contract. This function is used in modifyOrder and createOrder with the recipient address as the owner from who the tokens will be transferred from. An attacker can abuse this functionality to create unfair orders for a protocol user that approves more tokens than needed to the protocol contract the fill the order immediately and gain instant profit while the victim lost his tokens.  

## Root Cause  
In \u0060OracleLess.sol::procureTokens():280\u0060  
[Link to code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/OracleLess.sol#L280)  
procureTokens() implement tokens transfer from an owner address to the protocol contract  

In \u0060StopLimit.sol::createOrder():171\u0060  
[Link to code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L171)  

In \u0060StopLimit.sol::modifyOrder():226-230\u0060  
[Link to code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L226-L230)  

In \u0060Bracket.sol::modifyOrder():250-254\u0060  
[Link to code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L250-L254)  

## Internal pre-conditions  
No response
## External Pre-conditions
1. A user should have approve more tokens than needed for a trade that would result in some residual allowance to the protocol contract.

## Attack Path
1. The attacker creates/modifies an unfair order with the victim\u0027s recipient with an amount \u0060In <= residual allowance\u0060.
2. The protocol then transfers the tokens from the user to create the order.
3. The attacker fills the order and gains instant profit.

## Impact
No response

## PoC
No response

## Mitigation
It would be better to use \u0060msg.sender\u0060 to ensure that the recipient/owner of the order is the order creator or just use \u0060msg.sender\u0060 as a parameter to the \u0060safeTransferFrom()\u0060 function call instead of order recipient.

## Discussion
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/gfx-labs/oku-custom-order-types/pull/1](https://github.com/gfx-labs/oku-custom-order-types/pull/1)
