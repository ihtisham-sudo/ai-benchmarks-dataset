# fibonacci - RFPSimpleStrategy milestones can be set multiple times

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, RFPSimpleStrategy, setMilestones, milestones, totalAmountPercentage, contract, upcomingMilestone, pool state, malicious intentions, duplicate milestones, manager, payout amount, manual review, condition fix, reset milestones, distribution, inheritance, smart contract, security risk

---

fibonacci

medium

# RFPSimpleStrategy milestones can be set multiple times

Until the first distribution is completed, it\u0027s possible to call \u0060setMilestones\u0060 function multiple times. New milestones are added to the previous ones. The \u0060totalAmountPercentage\u0060 of all milestones in this case will be greater than 100%. It also affects all the contracts that are inherited from RFPSimpleStrategy.

## Vulnerability Detail

The \u0060setMilestones\u0060 function in \u0060RFPSimpleStrategy\u0060 contract checks if \u0060MILESTONES_ALREADY_SET\u0060 or not by \u0060upcomingMilestone\u0060 index.

\u0060\u0060\u0060solidity
if (upcomingMilestone != 0) revert MILESTONES_ALREADY_SET();
\u0060\u0060\u0060

But \u0060upcomingMilestone\u0060 increases only after distribution, and until this time will always be equal to 0.

## Impact

It can accidentally break the pool state or be used with malicious intentions.

1. Two managers accidentally set the same milestones. Milestones are duplicated and can\u0027t be reset, the pool needs to be recreated.
2. The manager, in cahoots with the recipient, sets milestones one by one, thereby bypassing \u0060totalAmountPercentage\u0060 check and increasing the payout amount.

## Code Snippet

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L224-L247

## Tool used

Manual Review

## Recommendation

Fix condition if milestones should only be set once. 

\u0060\u0060\u0060solidity
if (milestones.length > 0) revert MILESTONES_ALREADY_SET();
\u0060\u0060\u0060

Or allow milestones to be reset while they are not in use.


\u0060\u0060\u0060solidity
if (milestones.length > 0) {
    if (milestones[0].milestoneStatus != Status.None) revert MILESTONES_ALREADY_IN_USE();
    delete milestones;
}
\u0060\u0060\u0060
