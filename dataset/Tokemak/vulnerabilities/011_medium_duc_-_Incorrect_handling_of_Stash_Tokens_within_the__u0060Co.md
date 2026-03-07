# duc - Incorrect handling of Stash Tokens within the \u0060ConvexRewardsAdapter._claimRewards()\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, ConvexRewardsAdapter, claimRewards, Stash tokens, Denial-of-Service, DOS, rewardTokens, totalSupply, balanceOf, AURA staking, protocol losses, smart contract, Ethereum, token management, manual review, security flaw, low-level call, token validation, reward pool

---

duc

medium

# Incorrect handling of Stash Tokens within the \u0060ConvexRewardsAdapter._claimRewards()\u0060
## Summary
The \u0060ConvexRewardsAdapter._claimRewards()\u0060 function incorrectly handles Stash tokens, leading to potential vulnerabilities.

## Vulnerability Detail
The primary task of the \u0060ConvexRewardAdapter._claimRewards()\u0060 function revolves around claiming rewards for Convex/Aura staked LP tokens.

\u0060\u0060\u0060solidity=
function _claimRewards(
    address gauge,
    address defaultToken,
    address sendTo
) internal returns (uint256[] memory amounts, address[] memory tokens) {
    ... 

    // Record balances before claiming
    for (uint256 i = 0; i < totalLength; ++i) {
        // The totalSupply check is used to identify stash tokens, which can
        // substitute as rewardToken but lack a "balanceOf()"
        if (IERC20(rewardTokens[i]).totalSupply() > 0) {
            balancesBefore[i] = IERC20(rewardTokens[i]).balanceOf(account);
        }
    }

    // Claim rewards
    bool result = rewardPool.getReward(account, /*_claimExtras*/ true);
    if (!result) {
        revert RewardAdapter.ClaimRewardsFailed();
    }

    // Record balances after claiming and calculate amounts claimed
    for (uint256 i = 0; i < totalLength; ++i) {
        uint256 balance = 0;
        // Same check for "stash tokens"
        if (IERC20(rewardTokens[i]).totalSupply() > 0) {
            balance = IERC20(rewardTokens[i]).balanceOf(account);
        }

        amountsClaimed[i] = balance - balancesBefore[i];

        if (sendTo != address(this) && amountsClaimed[i] > 0) {
            IERC20(rewardTokens[i]).safeTransfer(sendTo, amountsClaimed[i]);
        }
    }

    RewardAdapter.emitRewardsClaimed(rewardTokens, amountsClaimed);

    return (amountsClaimed, rewardTokens);
}
\u0060\u0060\u0060 

An intriguing aspect of this function\u0027s logic lies in its management of "stash tokens" from AURA staking. The check to identify whether \u0060rewardToken[i]\u0060 is a stash token involves attempting to invoke \u0060IERC20(rewardTokens[i]).totalSupply()\u0060. If the returned total supply value is \u00600\u0060, the implementation assumes the token is a stash token and bypasses it. However, this check is flawed since the total supply of stash tokens can indeed be non-zero. For instance, at this [address](https://etherscan.io/address/0x2f5c611420c8ba9e7ec5c63e219e3c08af42a926#readContract), the stash token has \u0060totalSupply = 150467818494283559126567\u0060, which is definitely not zero.

This misstep in checking can potentially lead to a Denial-of-Service (DOS) situation when calling the \u0060claimRewards()\u0060 function. This stems from the erroneous attempt to call the \u0060balanceOf\u0060 function on stash tokens, which lack the \u0060balanceOf()\u0060 method. Consequently, such incorrect calls might incapacitate the destination vault from claiming rewards from AURA, resulting in protocol losses.

## Impact
* The \u0060AuraRewardsAdapter.claimRewards()\u0060 function could suffer from a Denial-of-Service (DOS) scenario.
* The destination vault\u0027s ability to claim rewards from AURA staking might be hampered, leading to protocol losses.

## Code Snippet
https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/destinations/adapters/rewards/ConvexRewardsAdapter.sol#L80-L86

## Tool used
Manual Review

## Recommendation
To accurately determine whether a token is a stash token, it is advised to perform a low-level \u0060balanceOf()\u0060 call to the token and subsequently validate the call\u0027s success.
