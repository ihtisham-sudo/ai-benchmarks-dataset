# Single user reward update

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** reward, integral, account, balance, pendingReward, rewardIntegralFor, supply, duration, lastUpdate, fetchRewards, interest, calculation, loss, users, expected, impact, medium, high, update, function

---

# Single user reward update
\u0060\u0060\u0060solidity
_updateIntegralForAccount(account, balance, integral);
}
function _updateIntegralForAccount(address account, uint256 balance, uint256 currentIntegral) internal {
    uint256 integralFor = rewardIntegralFor[account];
    if (currentIntegral > integralFor) {
        storedPendingReward[account] += (balance * (currentIntegral - integralFor)) / 1e18;
        rewardIntegralFor[account] = currentIntegral;
    }
}
function _updateRewardIntegral(uint256 supply) internal returns (uint256 integral) {
    uint256 _periodFinish = periodFinish;
    uint256 updated = _periodFinish;
    if (updated > block.timestamp) updated = block.timestamp;
    uint256 duration = updated - lastUpdate;
    integral = rewardIntegral;
    if (duration > 0) {
        lastUpdate = uint32(updated);
        if (supply > 0) {
            integral += (duration * rewardRate * 1e18) / supply;
            rewardIntegral = integral;
        }
    }
    _fetchRewards(_periodFinish);
}
\u0060\u0060\u0060
**Impact:** Users would receive less rewards than expected. The likelihood of this issue is high (would almost always happen), impact is medium (loss of rewards), hence reported as high severity.  
**Recommendation:** Always accrue interest before calculating rewards.
