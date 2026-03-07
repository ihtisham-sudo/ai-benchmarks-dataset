# s1ce - \u0060cancelVesting\u0060 will potentially not give users unclaimed, vested funds, even if giveUnclaimed = true

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Truflation
**Keywords:** cancelVesting, cybersecurity, vulnerability, unclaimed funds, vested funds, giveUnclaimed, bug, staking, locked funds, claimableAmount, claimable function, userVesting, memory vs storage, impact, manual review, recommendation, TrufVesting, unstaked, categoryId, vestingId

---

s1ce

high

# \u0060cancelVesting\u0060 will potentially not give users unclaimed, vested funds, even if giveUnclaimed = true

## Summary

The purpose of \u0060cancelVesting\u0060 is to cancel a vesting grant and potentially give users unclaimed but vested funds in the event that \u0060giveUnclaimed = true\u0060. However, due to a bug, in the event that the user had staked / locked funds, they will potentially not received the unclaimed / vested funds even if \u0060giveUnclaimed = true\u0060. 

## Vulnerability Detail

Here\u0027s the cancelVesting function in TrufVesting:

\u0060\u0060\u0060solidity
function cancelVesting(uint256 categoryId, uint256 vestingId, address user, bool giveUnclaimed)
        external
        onlyOwner
{
        UserVesting memory userVesting = userVestings[categoryId][vestingId][user];

        if (userVesting.amount == 0) {
            revert UserVestingDoesNotExists(categoryId, vestingId, user);
        }

        if (userVesting.startTime + vestingInfos[categoryId][vestingId].period <= block.timestamp) {
            revert AlreadyVested(categoryId, vestingId, user);
        }

        uint256 lockupId = lockupIds[categoryId][vestingId][user];

        if (lockupId != 0) {
            veTRUF.unstakeVesting(user, lockupId - 1, true);
            delete lockupIds[categoryId][vestingId][user];
            userVesting.locked = 0;
        }

        VestingCategory storage category = categories[categoryId];

        uint256 claimableAmount = claimable(categoryId, vestingId, user);
        if (giveUnclaimed && claimableAmount != 0) {
            trufToken.safeTransfer(user, claimableAmount);

            userVesting.claimed += claimableAmount;
            category.totalClaimed += claimableAmount;
            emit Claimed(categoryId, vestingId, user, claimableAmount);
        }

        uint256 unvested = userVesting.amount - userVesting.claimed;

        delete userVestings[categoryId][vestingId][user];

        category.allocated -= unvested;

        emit CancelVesting(categoryId, vestingId, user, giveUnclaimed);
}
\u0060\u0060\u0060

First, consider the following code:

\u0060\u0060\u0060solidity
uint256 lockupId = lockupIds[categoryId][vestingId][user];

if (lockupId != 0) {
            veTRUF.unstakeVesting(user, lockupId - 1, true);
            delete lockupIds[categoryId][vestingId][user];
            userVesting.locked = 0;
}
\u0060\u0060\u0060

First the locked / staked funds will essentially be un-staked. The following line of code: \u0060userVesting.locked = 0;\u0060 exists because there is a call to \u0060uint256 claimableAmount = claimable(categoryId, vestingId, user);\u0060 afterwards, and in the event that there were locked funds that were unstaked, these funds should now potentially be claimable if they are vested (but if locked is not set to 0, then the vested funds will potentially not be deemed claimable by the \u0060claimable\u0060 function). 

However, because \u0060userVesting\u0060 is \u0060memory\u0060 rather than \u0060storage\u0060, this doesn\u0027t end up happening (so \u0060userVesting.locked = 0;\u0060 is actually a bug). This means that if a user is currently staking all their funds (so all their funds are locked), and \u0060cancelVesting\u0060 is called, then they will not receive any funds back even if \u0060giveUnclaimed = true\u0060. This is because the \u0060claimable\u0060 function (which will access the unaltered \u0060userVestings[categoryId][vestingId][user]\u0060) will still think that all the funds are currently locked, even though they are not as they have been forcibly unstaked. 

## Impact

When \u0060cancelVesting\u0060 is called, a user may not receive their unclaimed, vested funds. 

## Code Snippet

https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L348-L388

## Tool used

Manual Review

## Recommendation
Change \u0060userVesting.locked = 0;\u0060 to \u0060userVestings[categoryId][vestingId][user].locked = 0;\u0060

