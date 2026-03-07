# 0x73696d616f - Lost rewards when the supply is \u00600\u0060, which always happens if the rewards are queued before anyone has \u0060StakeTracker\u0060 tokens

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, StakeTracker, rewards, totalSupply, rewardPerToken, MasterChef, smart contract, accrued rewards, snapshot, MainRewarder, ExtraRewarder, block numbers, queued rewards, DestinationVault, LMPVault, lost rewards, impact, recommendation, manual review

---

0x73696d616f

medium

# Lost rewards when the supply is \u00600\u0060, which always happens if the rewards are queued before anyone has \u0060StakeTracker\u0060 tokens
## Summary
If the supply of \u0060StakeTracker\u0060 tokens is \u00600\u0060, the \u0060rewardPerTokenStored\u0060 won\u0027t increase, but the \u0060lastUpdateBlock\u0060 will, leading to lost rewards. 

## Vulnerability Detail
The rewards are destributed in a [\u0060MasterChef\u0060](https://medium.com/coinmonks/analysis-of-the-billion-dollar-algorithm-sushiswaps-masterchef-smart-contract-81bb4e479eb6) style, which takes snapshots of the total accrued rewards over time and whenever someone wants to get the rewards, it subtracts the snapshot of the user from the most updated, global snapshot. 

The [\u0060rewardsPerToken()\u0060](https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/AbstractRewarder.sol#L180) calculation factors the blocks passed times the reward rate by the \u0060totalSupply()\u0060, to get the reward per token in a specific interval (and then accrues to the previous intervals, as stated in the last paragraph). When the \u0060totalSupply()\u0060 is \u00600\u0060, there is 0 \u0060rewardPerToken()\u0060 increment as there is no supply to factor the rewards by.

The current solution is to [maintain](https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/AbstractRewarder.sol#L176-L178) the same \u0060rewardsPerToken()\u0060 if the \u0060totalSupply()\u0060 is \u00600\u0060, but the \u0060lastUpdateBlock\u0060 is still updated. This means that, during the interval in which the \u0060totalSupply()\u0060 is \u00600\u0060, no rewards are destributed but the block numbers still move forward, leaving the tokens stuck in the \u0060MainRewarder\u0060 and \u0060ExtraRewarder\u0060 smart contracts.

This will always happen if the rewards are quewed before the \u0060totalSupply()\u0060 is bigger than \u00600\u0060 (before an initial deposit to either \u0060DestinationVault\u0060 or \u0060LMPVault\u0060). It might also happen if users withdraw all their tokens from the vaults, leading to a \u0060totalSupply()\u0060 of \u00600\u0060, but this is very unlikely.

## Impact
Lost reward tokens. The amount depends on the time during which the \u0060totalSupply()\u0060 is \u00600\u0060, but could be significant.

## Code Snippet
The \u0060rewardPerToken()\u0060 calculation:
\u0060\u0060\u0060solidity
function rewardPerToken() public view returns (uint256) {
    uint256 total = totalSupply();
    if (total == 0) {
        return rewardPerTokenStored;
    }

    return rewardPerTokenStored + ((lastBlockRewardApplicable() - lastUpdateBlock) * rewardRate * 1e18 / total);
}
\u0060\u0060\u0060
The \u0060rewardPerTokenStored\u0060 does not increment when the \u0060totalSupply()\u0060 is \u00600\u0060.

## Tool used
Vscode
Foundry
Manual Review

## Recommendation
The \u0060totalSupply()\u0060 should not realistically be \u00600\u0060 after the initial setup period (unless for some reason everyone decides to withdraw from the vaults, but this should be handled separately). It should be enough to only allow queueing rewards if the \u0060totalSupply()\u0060 is bigger than \u00600\u0060. For this, only a new check needs to be added:
\u0060\u0060\u0060solidity
function queueNewRewards(uint256 newRewards) external onlyWhitelisted {
    if (totalSupply() == 0) revert ZeroTotalSupply();
    ...
}
\u0060\u0060\u0060
