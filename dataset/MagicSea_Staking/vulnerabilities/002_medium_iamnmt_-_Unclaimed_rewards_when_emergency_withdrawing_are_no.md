# iamnmt - Unclaimed rewards when emergency withdrawing are not redistributed in \u0060MasterChef\u0060 and \u0060MlumStaking\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** MagicSea Staking
**Keywords:** cyber security, vulnerability, unclaimed rewards, emergency withdraw, MasterChef, MlumStaking, token withdrawal, reward redistribution, smart contracts, protocol, manual review, code snippet, impact assessment, security risk, decentralized finance, DeFi, contract exploitation, user impact, recommendation, contract audit

---

iamnmt

Medium

# Unclaimed rewards when emergency withdrawing are not redistributed in \u0060MasterChef\u0060 and \u0060MlumStaking\u0060

## Summary

Unclaimed rewards when emergency withdrawing are not redistributed in \u0060MasterChef\u0060 and \u0060MlumStaking\u0060.

## Vulnerability Detail

Users can call \u0060MasterChef#emergencyWithdraw\u0060, \u0060MlumStaking#emergencyWithdraw\u0060 to withdraw tokens without claiming the rewards.

But the unclaimed rewards are not redistributed in \u0060emergencyWithdraw\u0060 call, which will left the rewards stuck in the contracts and lost forever. Other users can not claim the rewards and the protocol can not redistribute the rewards.

## Impact

Unclaimed rewards when emergency withdrawing  in \u0060MasterChef\u0060 and \u0060MlumStaking\u0060 will stuck in the contracts and lost forever.

## Code Snippet

https://github.com/sherlock-audit/2024-06-magicsea/blob/42e799446595c542eff9519353d3becc50cdba63/magicsea-staking/src/MasterchefV2.sol#L326

https://github.com/sherlock-audit/2024-06-magicsea/blob/42e799446595c542eff9519353d3becc50cdba63/magicsea-staking/src/MlumStaking.sol#L536

## Tool used

Manual Review

## Recommendation

Redistribute the unclaimed rewards in \u0060emergencyWithdraw\u0060

\u0060MasterchefV2.sol\u0060

\u0060\u0060\u0060diff
    function emergencyWithdraw(uint256 pid) external override {
        Farm storage farm = _farms[pid];

        uint256 balance = farm.amounts.getAmountOf(msg.sender);
        int256 deltaAmount = -balance.toInt256();

-       farm.amounts.update(msg.sender, deltaAmount);

+       (uint256 oldBalance, uint256 newBalance, uint256 oldTotalSupply,) = farm.amounts.update(msg.sender, deltaAmount);

+       uint256 totalLumRewardForPid = _getRewardForPid(farm.rewarder, pid, oldTotalSupply);
+       uint256 lumRewardForPid = _mintLum(totalLumRewardForPid);

+       uint256 lumReward = farm.rewarder.update(msg.sender, oldBalance, newBalance, oldTotalSupply, lumRewardForPid);
+       lumReward = lumReward + unclaimedRewards[pid][msg.sender];
+       unclaimedRewards[pid][msg.sender] = 0;

+       farm.rewarder.updateAccDebtPerShare(oldTotalSupply, lumReward);

        farm.token.safeTransfer(msg.sender, balance);

        emit PositionModified(pid, msg.sender, deltaAmount, 0);
    }
\u0060\u0060\u0060

\u0060MlumStaking.sol\u0060

\u0060\u0060\u0060diff
function emergencyWithdraw(uint256 tokenId) external override nonReentrant {
        _requireOnlyOwnerOf(tokenId);

        StakingPosition storage position = _stakingPositions[tokenId];

        // position should be unlocked
        require(
            _unlockOperators.contains(msg.sender)
                || (position.startLockTime + position.lockDuration) <= _currentBlockTimestamp() || isUnlocked(),
            "locked"
        );
        // emergencyWithdraw: locked

+       _updatePool();

+       uint256 pending = position.amountWithMultiplier * _accRewardsPerShare / PRECISION_FACTOR - position.rewardDebt;

+       _lastRewardBalance = _lastRewardBalance - pending;

        uint256 amount = position.amount;

        // update total lp supply
        _stakedSupply = _stakedSupply - amount;
        _stakedSupplyWithMultiplier = _stakedSupplyWithMultiplier - position.amountWithMultiplier;

        // destroy position (ignore boost points)
        _destroyPosition(tokenId);

        emit EmergencyWithdraw(tokenId, amount);
        stakedToken.safeTransfer(msg.sender, amount);
    }

\u0060\u0060\u0060






