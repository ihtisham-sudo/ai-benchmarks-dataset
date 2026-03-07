# dany.armstrong90 - Attacker can inflate stake rewards as he wants.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, stake rewards, flash loan, FeeRewardsProcess, updateAccountFeeRewards, stake tokens, account balance, inflation, attacker, ETH, reward claiming, transfer, account1, account2, stakeAmount, manual review, security recommendation, smart contract, DeFi

---

dany.armstrong90

High

# Attacker can inflate stake rewards as he wants.

## Summary
\u0060FeeRewardsProcess.sol#updateAccountFeeRewards\u0060 function uses balance of account as amount of stake tokens.
Since it is possible to transfer stake tokens to any accounts, attacker can flash loan other\u0027s stake tokens to inflate stake rewards.

## Vulnerability Detail
\u0060FeeRewardsProcess.sol#updateAccountFeeRewards\u0060 function is the following.
\u0060\u0060\u0060solidity
    function updateAccountFeeRewards(address account, address stakeToken) public {
        StakingAccount.Props storage stakingAccount = StakingAccount.load(account);
        StakingAccount.FeeRewards storage accountFeeRewards = stakingAccount.getFeeRewards(stakeToken);
        FeeRewards.MarketRewards storage feeProps = FeeRewards.loadPoolRewards(stakeToken);
        if (accountFeeRewards.openRewardsPerStakeToken == feeProps.getCumulativeRewardsPerStakeToken()) {
            return;
        }
63:     uint256 stakeTokens = IERC20(stakeToken).balanceOf(account);
        if (
            stakeTokens > 0 &&
            feeProps.getCumulativeRewardsPerStakeToken() - accountFeeRewards.openRewardsPerStakeToken >
            feeProps.getPoolRewardsPerStakeTokenDeltaLimit()
        ) {
            accountFeeRewards.realisedRewardsTokenAmount += (
                stakeToken == CommonData.getStakeUsdToken()
                    ? CalUtils.mul(
                        feeProps.getCumulativeRewardsPerStakeToken() - accountFeeRewards.openRewardsPerStakeToken,
                        stakeTokens
                    )
                    : CalUtils.mulSmallRate(
                        feeProps.getCumulativeRewardsPerStakeToken() - accountFeeRewards.openRewardsPerStakeToken,
                        stakeTokens
                    )
            );
        }
        accountFeeRewards.openRewardsPerStakeToken = feeProps.getCumulativeRewardsPerStakeToken();
        stakingAccount.emitFeeRewardsUpdateEvent(stakeToken);
    }
\u0060\u0060\u0060
Balance of account is used as amount of stake tokens in \u0060L63\u0060.
But since the stake tokens can be transferred to any other account, attacker can inflate stake token rewards by flash loan.

Example:
1. User has two account: \u0060account1\u0060, \u0060account2\u0060.
2. User has staked 1000 ETH in \u0060account1\u0060 and 1000 ETH in \u0060account2\u0060.
3. After a period of time, user transfer 1000 xETH from \u0060account2\u0060 to \u0060account1\u0060 and claim rewards for \u0060account1\u0060.
4. Now, attacker can claim rewards twice for \u0060account1\u0060.
5. In the same way, attacker can claim rewards twice for \u0060account2\u0060 too.

## Impact
Attacker can inflate stake rewards as he wants using this vulnerability.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/FeeRewardsProcess.sol#L63

## Tool used

Manual Review

## Recommendation
Use \u0060stakingAccount.stakeTokenBalances[stakeToken].stakeAmount\u0060 instead of stake token balance as follows.
\u0060\u0060\u0060solidity
    function updateAccountFeeRewards(address account, address stakeToken) public {
        StakingAccount.Props storage stakingAccount = StakingAccount.load(account);
        StakingAccount.FeeRewards storage accountFeeRewards = stakingAccount.getFeeRewards(stakeToken);
        FeeRewards.MarketRewards storage feeProps = FeeRewards.loadPoolRewards(stakeToken);
        if (accountFeeRewards.openRewardsPerStakeToken == feeProps.getCumulativeRewardsPerStakeToken()) {
            return;
        }
--      uint256 stakeTokens = IERC20(stakeToken).balanceOf(account);
++      uint256 stakeTokens = stakingAccount.stakeTokenBalances[stakeToken].stakeAmount;
        if (
            stakeTokens > 0 &&
            feeProps.getCumulativeRewardsPerStakeToken() - accountFeeRewards.openRewardsPerStakeToken >
            feeProps.getPoolRewardsPerStakeTokenDeltaLimit()
        ) {
            accountFeeRewards.realisedRewardsTokenAmount += (
                stakeToken == CommonData.getStakeUsdToken()
                    ? CalUtils.mul(
                        feeProps.getCumulativeRewardsPerStakeToken() - accountFeeRewards.openRewardsPerStakeToken,
                        stakeTokens
                    )
                    : CalUtils.mulSmallRate(
                        feeProps.getCumulativeRewardsPerStakeToken() - accountFeeRewards.openRewardsPerStakeToken,
                        stakeTokens
                    )
            );
        }
        accountFeeRewards.openRewardsPerStakeToken = feeProps.getCumulativeRewardsPerStakeToken();
        stakingAccount.emitFeeRewardsUpdateEvent(stakeToken);
    }
\u0060\u0060\u0060
