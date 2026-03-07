# bin2chen - claimRewards() If a rewards is too small, it may block other epochs

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** BondProtocol
**Keywords:** cybersecurity, vulnerability, claimRewards, rewards, payoutToken, transferring 0, block epochs, rewards calculation, stake balance, userRewardsClaimed, rewardsPerTokenEnd, round down, transfer amount, revert, manual review, impact, stuck claim, epoch rewards, token support, smart contract

---

bin2chen

medium

# claimRewards() If a rewards is too small, it may block other epochs

## Summary
When \u0060claimRewards()\u0060, if some \u0060rewards\u0060 is too small after being round down to 0
If \u0060payoutToken\u0060 does not support transferring 0, it will block the subsequent epochs
## Vulnerability Detail
The current formula for calculating rewards per cycle is as follows.

\u0060\u0060\u0060solidity
    function _claimEpochRewards(uint48 epoch_) internal returns (uint256) {
...
@>      uint256 rewards = ((rewardsPerTokenEnd - userRewardsClaimed) * stakeBalance[msg.sender]) /
            10 ** stakedTokenDecimals;
        // Mint the option token on the teller
        // This transfers the reward amount of payout tokens to the option teller in exchange for the amount of option tokens
        payoutToken.approve(address(optionTeller), rewards);
        optionTeller.create(optionToken, rewards);
\u0060\u0060\u0060

Calculate \u0060rewards\u0060 formula : \u0060uint256 rewards = ((rewardsPerTokenEnd - userRewardsClaimed) * stakeBalance[msg.sender]) /10 ** stakedTokenDecimals;\u0060

When \u0060rewardsPerTokenEnd\u0060 is very close to \u0060userRewardsClaimed\u0060, \u0060rewards\u0060 is likely to be round downs to 0
Some tokens do not support transfer(amount=0)
This will revert and lead to can\u0027t claims

## Impact
Stuck \u0060claimRewards()\u0060 when the rewards of an epoch is 0
## Code Snippet
https://github.com/sherlock-audit/2023-06-bond/blob/main/options/src/fixed-strike/liquidity-mining/OTLM.sol#L499
## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060solidity
    function _claimEpochRewards(uint48 epoch_) internal returns (uint256) {
.....

        uint256 rewards = ((rewardsPerTokenEnd - userRewardsClaimed) * stakeBalance[msg.sender]) /
            10 ** stakedTokenDecimals;
+      if (rewards == 0 ) return 0;
        // Mint the option token on the teller
        // This transfers the reward amount of payout tokens to the option teller in exchange for the amount of option tokens
        payoutToken.approve(address(optionTeller), rewards);
        optionTeller.create(optionToken, rewards);
\u0060\u0060\u0060
