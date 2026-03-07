# stopthecap - No slippage or deadline control for swapping while stability burning

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnitasProtocol V1
**Keywords:** cybersecurity, vulnerability, slippage, deadline control, swapping, stability burn, reserve ratio, totalSupply, usd1, one sided burn, mempool, transaction, unilateral, user impact, funds, minOutAmount, execution, manual review, edge-case, recommendation

---

stopthecap

high

# No slippage or deadline control for swapping while stability burning

## Summary
No slippage or deadline control for swapping while stability burning

## Vulnerability Detail

Even though Unitas claims there will not be slippage because if it is burned from one side, it is minted in the other one, there is an edge-case where it does create a slight slippage depending on the burn amount.  Unitas intends to make stability burns when the reserve ratio is below 130% to try and get it back to normal levels. This burn, is a one sided burn of \u0060usd1\u0060, which reduces the \u0060totalSupply\u0060 of \u0060usd1\u0060 unilaterally.
https://github.com/sherlock-audit/2023-04-unitasprotocol/blob/main/Unitas-Protocol/src/Unitas.sol#L208

If any user is trying to swap \u0060usd1\u0060 while there is a stability burn being conducted, they will be affected by that slippage.

The other recommendation is the usage of a deadline param. Without a deadline parameter, the transaction may sit in the mempool and be executed at a much later time potentially resulting in a swap after/before a stability burn.

## Impact
User will be affected by unintended and unhandled slippage, potentially affecting the funds they get back from the swap

## Code Snippet
https://github.com/sherlock-audit/2023-04-unitasprotocol/blob/main/Unitas-Protocol/src/Unitas.sol#L208

## Tool used

Manual Review

## Recommendation
Allow a user to specify to key parameters, a \u0060deadline\u0060 and a \u0060minOutAmount\u0060. And make a check for both at start and end of the execution in the swap function.

