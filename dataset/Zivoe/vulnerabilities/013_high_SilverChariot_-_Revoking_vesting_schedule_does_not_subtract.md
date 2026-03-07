# SilverChariot - Revoking vesting schedule does not subtract user votes correctly

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cybersecurity, vulnerability, SilverChariot, ZivoeVestingRewards, revokeVestingSchedule, voting power, withdrawable amount, checkpoint value, governance proposals, amountWithdrawable, frontrun, transaction, vesting schedule, impact, code snippet, proof of concept, Foundry, recommendation, token withdrawal, smart contract

---

SilverChariot

medium

# Revoking vesting schedule does not subtract user votes correctly

## Summary
[ZivoeVestingRewards.revokeVestingSchedule()](https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeRewardsVesting.sol#L429-L467) should reduce the voting power of the user with the withdrawable amount plus the revoked amount. However, it reduces it only by the withdrawable amount.

## Vulnerability Detail
When called, \u0060revokeVestingSchedule()\u0060 fetches the withdrawable amount by the user at that moment.
\u0060\u0060\u0060solidity
        uint256 amount = amountWithdrawable(account);
\u0060\u0060\u0060

The revoke logic is executed and the user\u0027s checkpoint value is decreased by \u0060amount\u0060.
\u0060\u0060\u0060solidity
        _writeCheckpoint(_checkpoints[account], _subtract, amount);
\u0060\u0060\u0060

The code ignores the amount that\u0027s being revoked and the user keeps more voting power than he has to.
Imagine the following:
\u0060totalVested = 1000\u0060
\u0060withdrawable = 0\u0060

If the schedule gets revoked, the user\u0027s checkpoint value will not be decreased at all because there is nothing to be withdrawn. The user can later use their voting power to vote on governance proposals.

In fact, \u0060amountWithdrawable(account)\u0060 being close to 0 has a very high likelihood because:
   - the user can frontrun the transaction and withdraw the tokens they are entitled to
   -  it\u0027s highly likely that a vesting schedule will be removed shortly after creating it.

However, even if \u0060amountWithdrawable()\u0060 is not equal to 0, the user would still be left with more voting power.
## Impact
Users keep voting power that must have been taken away.

## Code Snippet
POC to be run in [Test_ZivoeRewardsVesting.sol](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-testing/src/TESTS_Core/Test_ZivoeRewardsVesting.sol)
\u0060\u0060\u0060solidity
    function test_revoking_leaves_votes() public {
       assert(zvl.try_createVestingSchedule(
            address(vestZVE), 
            address(moe), 
            0, 
            360,
            6000 ether, 
            true
        ));
        // Vesting succeeded
        assertEq(vestZVE.balanceOf(address(moe)), 6000 ether);

        hevm.roll(block.number + 1);
     
        // User votes have increased
        assertEq(vestZVE.getPastVotes(address(moe), block.number - 1), 6000 ether);

        assert(zvl.try_revokeVestingSchedule(address(vestZVE), address(moe)));
        // Revoking succeeded
        assertEq(vestZVE.balanceOf(address(moe)), 0);

        hevm.roll(block.number + 1);
        // User votes have not been decreased at all
        assertEq(vestZVE.getPastVotes(address(moe), block.number - 1), 6000 ether);
    }
\u0060\u0060\u0060

## Tool used

Foundry

## Recommendation
Subtract the correct amount from the checkpoint\u0027s value
\u0060\u0060\u0060diff
-        _writeCheckpoint(_checkpoints[account], _subtract, amount);
+       _writeCheckpoint(_checkpoints[account], _subtract, vestingAmount - vestingScheduleOf[account].totalWithdrawn + amount)
\u0060\u0060\u0060


