# dany.armstrong90 - \u0060ZivoeTranches#rewardZVEJuniorDeposit\u0060 function miscalculates the reward when the ratio traverses lower/upper bound.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cybersecurity, vulnerability, ZivoeTranches, reward calculation, lower bound, upper bound, fund loss, reward miscalculation, junior deposit, senior deposit, ratio incentive, manual review, code snippet, financial protocol, deposit strategy, average rate, incentive BIPS, risk assessment, smart contract, function modification

---

dany.armstrong90

high

# \u0060ZivoeTranches#rewardZVEJuniorDeposit\u0060 function miscalculates the reward when the ratio traverses lower/upper bound.

## Summary
\u0060ZivoeTranches#rewardZVEJuniorDeposit\u0060 function miscalculates the reward when the ratio traverses lower/upper bound.
The same issue also exists in the \u0060ZivoeTranches#rewardZVESeniorDeposit\u0060 function.

## Vulnerability Detail
\u0060ZivoeTranches#rewardZVEJuniorDeposit\u0060 function is the following.
\u0060\u0060\u0060solidity
    function rewardZVEJuniorDeposit(uint256 deposit) public view returns (uint256 reward) {

        (uint256 seniorSupp, uint256 juniorSupp) = IZivoeGlobals_ZivoeTranches(GBL).adjustedSupplies();

        uint256 avgRate;    // The avg ZVE per stablecoin deposit reward, used for reward calculation.

        uint256 diffRate = maxZVEPerJTTMint - minZVEPerJTTMint;

        uint256 startRatio = juniorSupp * BIPS / seniorSupp;
        uint256 finalRatio = (juniorSupp + deposit) * BIPS / seniorSupp;
213:    uint256 avgRatio = (startRatio + finalRatio) / 2;

        if (avgRatio <= lowerRatioIncentiveBIPS) {
216:        avgRate = maxZVEPerJTTMint;
        } else if (avgRatio >= upperRatioIncentiveBIPS) {
218:        avgRate = minZVEPerJTTMint;
        } else {
220:        avgRate = maxZVEPerJTTMint - diffRate * (avgRatio - lowerRatioIncentiveBIPS) / (upperRatioIncentiveBIPS - lowerRatioIncentiveBIPS);
        }

223:    reward = avgRate * deposit / 1 ether;

        // Reduce if ZVE balance < reward.
        if (IERC20(IZivoeGlobals_ZivoeTranches(GBL).ZVE()).balanceOf(address(this)) < reward) {
            reward = IERC20(IZivoeGlobals_ZivoeTranches(GBL).ZVE()).balanceOf(address(this));
        }
    }
\u0060\u0060\u0060
Here, let us assume that \u0060lowerRatioIncentiveBIPS = 1000\u0060, \u0060upperRatioIncentiveBIPS = 2500\u0060, \u0060minZVEPerJTTMint = 0\u0060, \u0060maxZVEPerJTTMint = 0.4 * 10 ** 18\u0060, \u0060seniorSupp = 10000\u0060.

Let us consider the case of \u0060juniorSupp = 0\u0060 where the ratio traverses the lower bound.

Example 1:
Assume that the depositor deposit \u00602000\u0060 at a time.
Then \u0060avgRatio = 1000\u0060 holds in \u0060L213\u0060, thus \u0060avgRate = maxZVEPerJTTMint = 0.4 * 10 ** 18\u0060 holds in \u0060L216\u0060.
Therefore \u0060reward = 0.4 * deposit = 800\u0060 holds in \u0060L223\u0060.

Example 2:
Assume that the depositor deposit \u00601000\u0060 twice.
Then, since \u0060avgRate = 500 < lowerRatioIncentiveBIPS\u0060 holds for the first deposit, \u0060avgRate = 0.4 * 10 ** 18\u0060 holds in \u0060L216\u0060, thus \u0060reward = 400\u0060 holds.
Since \u0060avgRate = 1500 > lowerRatioIncentiveBIPS\u0060 holds for the second deposit, \u0060avgRate = 0.3 * 10 ** 18\u0060 holds in \u0060L220\u0060, thus \u0060reward = 300\u0060 holds.
Finally, the total sum of rewards for two deposits are \u0060400 + 300 = 700\u0060.

This shows that the reward of the case where all assets are deposited at a time is larger than the reward of the case where assets are divided and deposited twice. In this case, the protocol gets loss of funds.

Likewise, in the case where the ratio traverses the upper bound, the reward of one time deposit will be smaller than the reward of two times deposit and thus the depositor gets loss.

The same issue also exists in the \u0060ZivoeTranches#rewardZVESeniorDeposit\u0060 function.

## Impact
When the ratio traverses the lower/upper bound in \u0060ZivoeTranches#rewardZVEJuniorDeposit\u0060 and \u0060ZivoeTranches#rewardZVESeniorDeposit\u0060 functions, the amount of reward will be larger/smaller than it should be. Thus the depositor or the protocol will get loss of funds.

## Code Snippet
https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeTranches.sol#L215-L221

## Tool used
Manual Review

## Recommendation
Modify the functions to calculate the reward dividing into two portion when the ratio traverses the lower/upper bound, which is similar to the case of Example 2.
