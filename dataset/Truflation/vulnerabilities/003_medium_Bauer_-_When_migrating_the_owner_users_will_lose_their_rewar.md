# Bauer - When migrating the owner users will lose their rewards

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Truflation
**Keywords:** cyber security, vulnerability, migration, private key, user rewards, vesting owner, staking rewards, withdraw, update reward, account, protocol, migrateUser, migrateVestingLock, burning points, reward transfer, manual review, impact, loss of rewards, security flaw, recommendation

---

Bauer

high

# When migrating the owner users will lose their rewards

## Summary
When a user migrates the owner due to a lost private key, the rewards belonging to the previous owner remain recorded in their account and cannot be claimed, resulting in the loss of user rewards.

## Vulnerability Detail
According to the documentation, \u0060migrateUser()\u0060 is used when a user loses their private key to migrate the old vesting owner to a new owner.
\u0060\u0060\u0060solidity
    /**
     * @notice Migrate owner of vesting. Used when user lost his private key
     * @dev Only admin can migrate users vesting
     * @param categoryId Category id
     * @param vestingId Vesting id
     * @param prevUser previous user address
     * @param newUser new user address
     */

\u0060\u0060\u0060

 In this function, the protocol calls \u0060migrateVestingLock()\u0060 to obtain a new ID. 
\u0060\u0060\u0060solidity
    if (lockupId != 0) {
            newLockupId = veTRUF.migrateVestingLock(prevUser, newUser, lockupId - 1) + 1;
            lockupIds[categoryId][vestingId][newUser] = newLockupId;
            delete lockupIds[categoryId][vestingId][prevUser];

            newVesting.locked = prevVesting.locked;
        }

\u0060\u0060\u0060

However, in the \u0060migrateVestingLock()\u0060 function, the protocol calls \u0060stakingRewards.withdraw()\u0060 to withdraw the user\u0027s stake, burning points. In the \u0060withdraw()\u0060 function, the protocol first calls \u0060updateReward()\u0060 to update the user\u0027s rewards and records them in the user\u0027s account. 
\u0060\u0060\u0060solidity
    function withdraw(address user, uint256 amount) public updateReward(user) onlyOperator {
        if (amount == 0) {
            revert ZeroAmount();
        }
        _totalSupply -= amount;
        _balances[user] -= amount;
        emit Withdrawn(user, amount);
    }
\u0060\u0060\u0060

However, \u0060stakingRewards.withdraw()\u0060 is called with the old owner as a parameter, meaning that the rewards will be updated on the old account. 
\u0060\u0060\u0060solidity
  uint256 points = oldLockup.points;
        stakingRewards.withdraw(oldUser, points);
        _burn(oldUser, points);
\u0060\u0060\u0060

As mentioned earlier, the old owner has lost their private key and cannot claim the rewards, resulting in the loss of these rewards.

## Impact
The user\u0027s rewards are lost

## Code Snippet
https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L329

## Tool used

Manual Review

## Recommendation
When migrating the owner, the rewards belonging to the previous owner should be transferred to the new owner.

