# lemonmon - Missing access modifier for \u0060RFPSimpleStrategy.setPoolActive()\u0060 may lead to multiple issues

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, access modifier, RFPSimpleStrategy, setPoolActive, onlyPoolManager, malicious actor, funds theft, smart contract, Ethereum, proposalBid, pool manager, token distribution, frontrunning, recipient registration, malicious behavior, security audit, code review, contract exploit, risk mitigation

---

lemonmon

high

# Missing access modifier for \u0060RFPSimpleStrategy.setPoolActive()\u0060 may lead to multiple issues

\u0060RFPSimpleStrategy.setPoolActive()\u0060 can be called by anybody since it\u0027s missing the \u0060onlyPoolManager(msg.sender)\u0060 modifier, which can be abused by a malicious actor to steal funds.

## Vulnerability Detail

The comment on line 217 in RFPSimpleStrategy.sol says that \u0060\u0027msg.sender\u0027 must be a pool manager\u0060 in order to be able to call \u0060RFPSimpleStrategy.setPoolActive()\u0060. However, the necessary \u0060onlyPoolManager(msg.sender)\u0060 modifier is missing.

## Impact

Multiple functions inside \u0060RFPSimpleStrategy.sol\u0060 are either using the \u0060onlyActivePool\u0060 or the \u0060onlyInactivePool\u0060 modifiers:

* \u0060RFPSimpleStrategy._distribute()\u0060
* \u0060RFPSimpleStrategy.withdraw()\u0060
* \u0060RFPSimpleStrategy._registerRecipient()\u0060
* \u0060RFPSimpleStrategy._allocate()\u0060

A malicious actor (Alice) might do the following for example:

1. Alice registers themself as recipient for a \u0060RFPSimpleStrategy\u0060, specifying a \u0060proposalBid\u0060 which is \u006015e18\u0060.
1. Alice is being declared as the accepted recipient by the pool manager.
1. Now if the tokens were distributed to Alice, the amount of tokens Alice would receive would be \u0060(15e18 * milestone.amountPercentage) / 1e18\u0060 (line 435 RFPSimpleStrategy.sol).
1. However, Alice calls \u0060RFPSimpleStrategy.setPoolActive()\u0060 to make the pool active again, before the tokens are distributed. Alice might do this by either frontrunning or by executing the tx earlier.
1. Now Alice can call \u0060RFPSimpleStrategy._registerRecipient()\u0060, since the pool is active again, and Alice re-registers themself but with a higher \u0060proposalBid\u0060 than was accepted before (line 378 RFPSimpleStrategy.sol), for example they re-register with a \u0060proposalBid\u0060 of \u006060e18\u0060.
1. Then Alice calls \u0060RFPSimpleStrategy.setPoolActive()\u0060 to set the pool inactive, so that the tokens can be distributed.
1. Now when the tokens are distributed to Alice for the first milestone (and later also for subsequent milestones), they receive a much higher amount of tokens, since Alice maliciously increased their accepted \u0060proposalBid\u0060 from \u006015e18\u0060 to \u006060e18\u0060, so they would now receive \u0060(60e18 * milestone.amountPercentage) / 1e18\u0060 (line 435 RFPSimpleStrategy.sol) which is more than was accepted.

The above example illustrates how Alice can abuse setting the pool to active and inactive to change their accepted \u0060proposalBid\u0060 to receive more tokens.

Also, Alice could potentially steal funds from the strategy, if they get accepted with a smaller \u0060proposalBid\u0060 and then maliciously increase the \u0060proposalBid\u0060 as described in the above example, so that Alice would receive a much higher amount of tokens that they are not eligible to receive and that are effectively being stolen from the funds of the strategy.

## Code Snippet

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L217-L221

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L417-L450

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L314-L380

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L386-L393

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L295


## Tool used

Manual Review

## Recommendation

Consider adding the missing access modifier \u0060onlyPoolManager(msg.sender)\u0060 to \u0060RFPSimpleStrategy.setPoolActive()\u0060.
