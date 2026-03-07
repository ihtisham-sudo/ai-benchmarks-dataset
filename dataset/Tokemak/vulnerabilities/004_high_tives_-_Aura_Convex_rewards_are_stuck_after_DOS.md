# tives - Aura/Convex rewards are stuck after DOS

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, Convex rewards, DOS attack, LiquidationRow contract, reward tokens, Tokemak, claimRewards, balanceBefore, balanceAfter, ConvexRewardsAdapter, getReward, amountsClaimed, MainRewarder, accounting hook, manual review, security recommendation, token transfer, reward accounting, smart contract

---

tives

medium

# Aura/Convex rewards are stuck after DOS
## Summary

Since \u0060_claimRewards\u0060 accounts for rewards with balanceBefore/After, and anyone can claim Convex rewards, then attacker can DOS the rewards and make them stuck in the LiquidationRow contract.

## Vulnerability Detail

Anyone can claim Convex rewards for any account.

https://etherscan.io/address/0x0A760466E1B4621579a82a39CB56Dda2F4E70f03#code

\u0060\u0060\u0060solidity
function getReward(address _account, bool _claimExtras) public updateReward(_account) returns(bool){
    uint256 reward = earned(_account);
    if (reward > 0) {
        rewards[_account] = 0;
        rewardToken.safeTransfer(_account, reward);
        IDeposit(operator).rewardClaimed(pid, _account, reward);
        emit RewardPaid(_account, reward);
    }

    //also get rewards from linked rewards
    if(_claimExtras){
        for(uint i=0; i < extraRewards.length; i++){
            IRewards(extraRewards[i]).getReward(_account);
        }
    }
    return true;
}
\u0060\u0060\u0060

In ConvexRewardsAdapter, the rewards are accounted for by using balanceBefore/after.

\u0060\u0060\u0060solidity
function _claimRewards(
    address gauge,
    address defaultToken,
    address sendTo
) internal returns (uint256[] memory amounts, address[] memory tokens) {

		uint256[] memory balancesBefore = new uint256[](totalLength);
    uint256[] memory amountsClaimed = new uint256[](totalLength);
...

		for (uint256 i = 0; i < totalLength; ++i) {
        uint256 balance = 0;
        // Same check for "stash tokens"
        if (IERC20(rewardTokens[i]).totalSupply() > 0) {
            balance = IERC20(rewardTokens[i]).balanceOf(account);
        }

        amountsClaimed[i] = balance - balancesBefore[i];

	return (amountsClaimed, rewardTokens);
\u0060\u0060\u0060

Adversary can call the external convex contract’s  \u0060getReward(tokemakContract)\u0060. After this, the reward tokens are transferred to Tokemak without an accounting hook.

Now, when Tokemak calls claimRewards, then no new rewards are transferred, because the attacker already transferred them. \u0060amountsClaimed\u0060 will be 0.

## Impact

Rewards are stuck in the LiquidationRow contract and not queued to the MainRewarder.

## Code Snippet

\u0060\u0060\u0060solidity
// get balances after and calculate amounts claimed
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
\u0060\u0060\u0060

https://github.com/sherlock-audit/2023-06-tokemak/blob/5d8e902ce33981a6506b1b5fb979a084602c6c9a/v2-core-audit-2023-07-14/src/destinations/adapters/rewards/ConvexRewardsAdapter.sol/#L102

## Tool used

Manual Review

## Recommendation

Don’t use balanceBefore/After. You could consider using \u0060balanceOf(address(this))\u0060 after claiming to see the full amount of tokens in the contract. This assumes that only the specific rewards balance is in the contract.
