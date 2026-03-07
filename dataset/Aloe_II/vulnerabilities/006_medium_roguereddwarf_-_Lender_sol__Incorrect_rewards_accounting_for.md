# roguereddwarf - Lender.sol: Incorrect rewards accounting for RESERVE address in _transfer function

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Aloe II
**Keywords:** cybersecurity, vulnerability, Lender.sol, RESERVE address, rewards accounting, _transfer function, interest accrual, share balance, Rewards.updateUserState, incorrect balance, manual review, impact assessment, special-casing, gas optimization, transfer execution, Rewards.updatePoolState, accrued balance, audit, smart contract, security flaw

---

roguereddwarf

medium

# Lender.sol: Incorrect rewards accounting for RESERVE address in _transfer function
## Summary
The \u0060RESERVE\u0060 address is a special address in the \u0060Lender\u0060 since it earns some of the interest that the \u0060Lender\u0060 accrues.  

According to the contest README, which links to the [auditor quick start guide](https://docs.aloe.capital/aloe-ii/auditor-quick-start), the \u0060RESERVE\u0060 address should behave normally, i.e. all accounting should be done correctly for it:  

\u0060\u0060\u0060text
Special-cases related to the RESERVE address and couriers

We believe the RESERVE address can operate without restriction, i.e. it can call any function in the protocol without causing accounting errors. Where it needs to be limited, we believe it is. For example, Lender.deposit prevents it from having a courier. But are we missing anything? Many of our invariants in LenderHarness have special logic to account for the RESERVE address, and while we think everything is correct, we\u0027d like to have more eyes on it.
\u0060\u0060\u0060

The issue is that the [\u0060Lender._transfer\u0060](https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/Lender.sol#L399-L425) function, which contains the logic for share transfers, does not accrue interest.  

Thereby the \u0060RESERVE\u0060\u0027s share balance is not up-to-date and it loses out on any rewards that should be earned for the accrued balance.  

For all other addresses the reward accounting is performed correctly in the \u0060Lender._transfer\u0060 function and according to the auditor quick start guide it is required that the same is true for the \u0060RESERVE\u0060 address.  


## Vulnerability Detail
When interest is accrued, the \u0060RESERVE\u0060 address [gets minted shares](https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/Lender.sol#L536-L547).  

However the \u0060Lender._transfer\u0060 function does not accrue interest and so \u0060RESERVE\u0060\u0027s balance is not up to date which means the \u0060Rewards.updateUserState\u0060 call operates on an [incorrect balance](https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/Lender.sol#L411-L421).  

The balance of \u0060RESERVE\u0060 is too low which results in a loss of rewards.  

## Impact
As described above, the \u0060RESERVE\u0060 address should have its reward accounting done correctly just like all other addresses.  

Failing to do so means that the \u0060RESERVE\u0060 misses out on some rewards because \u0060Lender._transfer\u0060 does not update the share balance correctly and so the rewards will be accrued on a balance that is too low.

## Code Snippet
https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/Lender.sol#L399-L425

## Tool used
Manual Review

## Recommendation
The \u0060RESERVE\u0060 address should be special-cased in the \u0060Lender._transfer\u0060 function. Thereby gas is saved when transfers are executed that do not involve the \u0060RESERVE\u0060 address and the reward accounting is done correctly for when the \u0060RESERVE\u0060 address is involved.  

When the \u0060RESERVE\u0060 address is involved, \u0060(Cache memory cache, ) = _load();\u0060 and \u0060_save(cache, /* didChangeBorrowBase: */ false);\u0060 must be called. Also the Rewards state must be updated with this call: \u0060Rewards.updatePoolState(s, a, newTotalSupply);\u0060.  

