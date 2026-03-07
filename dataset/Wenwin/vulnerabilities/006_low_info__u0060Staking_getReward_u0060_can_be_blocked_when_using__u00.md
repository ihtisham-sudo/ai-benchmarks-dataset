# \u0060Staking#getReward\u0060 can be blocked when using \u0060rewardsToken\u0060 that reverts on zero transfer

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wenwin
**Keywords:** cybersecurity, vulnerability, staking, reward token, zero value transfer, claimRewards, Lottery contract, accumulated rewards, dueTicketsSoldAndReset, claimedAmount, transfer failure, user claims, smart contract, manual review, mitigation steps, blockchain, tokenomics, reward distribution, contract interaction, security audit

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/staking/Staking.sol#L91
https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/staking/Staking.sol#L97


# Vulnerability details

## Impact

Getting rewards from staking Lottery token can be blocked if used in conjunction with a reward token that does not support zero value transfer. Such token is https://github.com/d-xo/weird-erc20#revert-on-zero-value-transfers


## Proof of Concept

Lets examine the following scenario:

For the current draw we have accumulated some non zero rewards.

1. User A calls for the first time \u0060getReward\u0060 

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/staking/Staking.sol#L91

This user has earned some reward by staking so the call proceeds internally by calling \u0060Lottery#claimRewards(LotteryRewardType.STAKING)\u0060 which will transfer **all accumulated rewards to the staking contract at once** so on next user claim this transferred value can be distributed from the staking contract to the claiming users.

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/staking/Staking.sol#L97

\u0060claimRewards\u0060 internally calls \u0060dueTicketsSoldAndReset\u0060 which will for the first time return \u0060claimedAmount\u0060 value that is in our scenario greater than zero and will succeed to transfer this value to the staking (which is the current \u0060beneficiary\u0060) contract with:

\u0060\u0060\u0060solidity
rewardToken.safeTransfer(beneficiary, claimedAmount);
\u0060\u0060\u0060
From the staking contract will go directly to the user A that claimed its reward

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/staking/Staking.sol#L98

2. When a second user B comes around and tries to call \u0060getReward\u0060 it will revert because 

\u0060dueTicketsSoldAndReset\u0060 has already reset the \u0060claimedAmount\u0060 to zero the first time and now will fail when trying to transfer zero amount from the reward token to the staking contract.

## Tools Used
Manual review

## Recommended Mitigation Steps

\u0060\u0060\u0060diff
 function claimRewards(LotteryRewardType rewardType) external override returns (uint256 claimedAmount) {
        // audit-ok : someone (staking contract) need/is to call/ing this to get staking reward
        // audit-ok : is recipent correct => it is
        address beneficiary = (rewardType == LotteryRewardType.FRONTEND) ? msg.sender : stakingRewardRecipient;
        claimedAmount = LotteryMath.calculateRewards(ticketPrice, dueTicketsSoldAndReset(beneficiary), rewardType);

        emit ClaimedRewards(beneficiary, claimedAmount, rewardType);
+
+       if (claimedAmount > 0)
+           rewardToken.safeTransfer(beneficiary, claimedAmount);

-        rewardToken.safeTransfer(beneficiary, claimedAmount);
    }
\u0060\u0060\u0060
