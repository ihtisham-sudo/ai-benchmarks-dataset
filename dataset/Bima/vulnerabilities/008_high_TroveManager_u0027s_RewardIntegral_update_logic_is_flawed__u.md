# TroveManager\u0027s RewardIntegral update logic is flawed, users may be receiving less rewards than expected

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** TroveManager, RewardIntegral, Bima token, debt, interest, reward rate, global, user, accrued, pending rewards, totalActiveDebt, activeInterestIndex, debt calculation, supply, integral, update logic, reward loss, smart contract, Sushiswap, audit

---

# TroveManager\u0027s RewardIntegral update logic is flawed, users may be receiving less rewards than expected
- **Submitted by:** pkqs90, also found by santipu and 0xBeastBoy
- **Severity:** High Risk
- **Context:** (No context files were provided by the reviewer)
- **Description:** TroveManager rewards users with Bima token by the amount of debt they have. Rewards are updated by the \u0060_updateIntegrals\u0060 function. The updating mechanism is similar to Sushiswap Masterchef, maintaining the amount of reward token per debt token in \u0060rewardIntegral\u0060 (global) and \u0060rewardIntegralFor[account]\u0060 (per account). The difference between here and Sushiswap is that debt is always accruing interest.

The issue is that the global reward rate \u0060rewardIntegral\u0060 always uses the total debt as the denominator, which is frequently updated to include latest interest, but user\u0027s \u0060rewardIntegralFor[account]\u0060 may not be updated in sync. This will lead to user\u0027s amount of debt to be less than what global \u0060rewardIntegral\u0060 expects, leading to a loss of rewards for users.

**Example:**
1. Initial status: Global debt = 100, User debt = 50. Current \u0060rewardIntegral\u0060 = 0, \u0060rewardIntegralFor[user]\u0060 = 0.
2. Sometime pass, 10% debt interest is accrued. Another user comes and performs some actions (e.g. claims rewards), which triggers \u0060_applyPendingRewards()\u0060, which increases \u0060totalActiveDebt\u0060 to 100 * (1 + 10%) = 110.
3. Sometime pass, and we have 100 pending Bima rewards. Original user tries to claim rewards. We first update global variable \u0060rewardIntegral\u0060 = 100 / 110 = 0.909, then update for user \u0060storedPendingReward\u0060 += 50 * (0.909 - 0) = 45.45.

User should have received 50 rewards, but only received 45.45. The bug is that in step 2, we already updated \u0060totalActiveDebt\u0060 with 10% interest to 110, but user debt remains unchanged. Then in step 3, when we try to calculate user rewards, we use the before-debt-accrued amount (50) to calculate for users. This results in loss of rewards for the user.

**Code References:**
\u0060\u0060\u0060solidity
function _applyPendingRewards(address _borrower) internal returns (uint256 coll, uint256 debt) {
    Trove storage t = Troves[_borrower];
    if (t.status == Status.active) {
        uint256 troveInterestIndex = t.activeInterestIndex;
        uint256 supply = totalActiveDebt; // <<<
        uint256 currentInterestIndex = _accrueActiveInterests();
        debt = t.debt;
        uint256 prevDebt = debt; // <<<
        // ...
        // @audit-bug: Use previous debt instead of updated one.
        _updateIntegrals(_borrower, prevDebt, supply); // <<<
    }
}

function _updateIntegrals(address account, uint256 balance, uint256 supply) internal {
    // @audit-note: Global reward update.
    uint256 integral = _updateRewardIntegral(supply);
}
\u0060\u0060\u0060
