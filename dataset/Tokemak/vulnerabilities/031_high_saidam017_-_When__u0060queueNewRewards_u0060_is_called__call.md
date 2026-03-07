# saidam017 - When \u0060queueNewRewards\u0060 is called, caller could transfer tokens more than it should be

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cyber security, vulnerability, queueNewRewards, tokens, stakers, accrued rewards, queuedRatio, newRewardRatio, queuedRewards, safeTransferFrom, funds, logic error, approval, impact, transfer, startingQueuedRewards, startingNewRewards, manual review, recommendation, smart contract

---

saidam017

medium

# When \u0060queueNewRewards\u0060 is called, caller could transfer tokens more than it should be
## Summary

\u0060queueNewRewards\u0060 is used for Queues the specified amount of new rewards for distribution to stakers. However, it used wrong calculated value when pulling token funds from the caller, could make caller transfer tokens more that it should be.

## Vulnerability Detail

Inside \u0060queueNewRewards\u0060, irrespective of whether we\u0027re near the start or the end of a reward period, if the accrued rewards are too large relative to the new rewards (\u0060queuedRatio\u0060 is greater than \u0060newRewardRatio\u0060), the new rewards will be added to the queue (\u0060queuedRewards\u0060) rather than being immediately distributed.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/AbstractRewarder.sol#L235-L261

\u0060\u0060\u0060solidity
    function queueNewRewards(uint256 newRewards) external onlyWhitelisted {
        uint256 startingQueuedRewards = queuedRewards;
        uint256 startingNewRewards = newRewards;

        newRewards += startingQueuedRewards;

        if (block.number >= periodInBlockFinish) {
            notifyRewardAmount(newRewards);
            queuedRewards = 0;
        } else {
            uint256 elapsedBlock = block.number - (periodInBlockFinish - durationInBlock);
            uint256 currentAtNow = rewardRate * elapsedBlock;
            uint256 queuedRatio = currentAtNow * 1000 / newRewards;

            if (queuedRatio < newRewardRatio) {
                notifyRewardAmount(newRewards);
                queuedRewards = 0;
            } else {
                queuedRewards = newRewards;
            }
        }

        emit QueuedRewardsUpdated(startingQueuedRewards, startingNewRewards, queuedRewards);

        // Transfer the new rewards from the caller to this contract.
        IERC20(rewardToken).safeTransferFrom(msg.sender, address(this), newRewards);
    }
\u0060\u0060\u0060

However, when this function tried to pull funds from sender via \u0060safeTransferFrom\u0060, it used \u0060newRewards\u0060 amount, which already added  by \u0060startingQueuedRewards\u0060. If previously \u0060queuedRewards\u0060 already have value, the processed amount will be wrong.


## Impact

There are two possible issue here : 

1. If previously \u0060queuedRewards\u0060 is not 0, and the caller don\u0027t have enough funds or approval, the call will revert due to this logic error.
2. If previously \u0060queuedRewards\u0060 is not 0,  and the caller have enough funds and approval, the caller funds will be pulled more than it should (reward param + \u0060queuedRewards\u0060 )

## Code Snippet

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/AbstractRewarder.sol#L236-L239
https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/AbstractRewarder.sol#L260

## Tool used

Manual Review

## Recommendation

Update the transfer to use \u0060startingNewRewards\u0060 instead of \u0060newRewards\u0060  : 

\u0060\u0060\u0060diff
    function queueNewRewards(uint256 newRewards) external onlyWhitelisted {
        uint256 startingQueuedRewards = queuedRewards;
        uint256 startingNewRewards = newRewards;

        newRewards += startingQueuedRewards;

        if (block.number >= periodInBlockFinish) {
            notifyRewardAmount(newRewards);
            queuedRewards = 0;
        } else {
            uint256 elapsedBlock = block.number - (periodInBlockFinish - durationInBlock);
            uint256 currentAtNow = rewardRate * elapsedBlock;
            uint256 queuedRatio = currentAtNow * 1000 / newRewards;

            if (queuedRatio < newRewardRatio) {
                notifyRewardAmount(newRewards);
                queuedRewards = 0;
            } else {
                queuedRewards = newRewards;
            }
        }

        emit QueuedRewardsUpdated(startingQueuedRewards, startingNewRewards, queuedRewards);

        // Transfer the new rewards from the caller to this contract.
-        IERC20(rewardToken).safeTransferFrom(msg.sender, address(this), newRewards);
+        IERC20(rewardToken).safeTransferFrom(msg.sender, address(this), startingNewRewards);
    }
\u0060\u0060\u0060

