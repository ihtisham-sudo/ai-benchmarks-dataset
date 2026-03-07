# bin2chen - stake() missing set lastEpochClaimed when userBalance equal 0

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** BondProtocol
**Keywords:** cybersecurity, vulnerability, stake, lastEpochClaimed, userBalance, claimRewards, GAS, GAS_OUT, rewardsPerTokenClaimed, staker, epoch, manual review, smart contract, Ethereum, gas optimization, loop inefficiency, blockchain, decentralized finance, contract execution, performance issue

---

bin2chen

medium

# stake() missing set lastEpochClaimed when userBalance equal 0

## Summary
because \u0060stake()\u0060 don\u0027t  set \u0060 lastEpochClaimed[user] = last epoch\u0060 if \u0060userBalance\u0060 equal 0
So all new stake user must loop from 0 to \u0060last epoch\u0060 for \u0060_claimRewards()\u0060
As the epoch gets bigger and bigger it will waste a lot of GAS, which may eventually lead to \u0060GAS_OUT\u0060

## Vulnerability Detail
in \u0060stake()\u0060,  when the first-time stake() only \u0060rewardsPerTokenClaimed[msg.sender]\u0060
but don\u0027t set \u0060lastEpochClaimed[msg.sender]\u0060

\u0060\u0060\u0060solidity
    function stake(
        uint256 amount_,
        bytes calldata proof_
    ) external nonReentrant requireInitialized updateRewards tryNewEpoch {
...
        uint256 userBalance = stakeBalance[msg.sender];
        if (userBalance > 0) {
            // Claim outstanding rewards, this will update the rewards per token claimed
            _claimRewards();
        } else {
            // Initialize the rewards per token claimed for the user to the stored rewards per token
@>          rewardsPerTokenClaimed[msg.sender] = rewardsPerTokenStored;
        }

        // Increase the user\u0027s stake balance and the total balance
        stakeBalance[msg.sender] = userBalance + amount_;
        totalBalance += amount_;

        // Transfer the staked tokens from the user to this contract
        stakedToken.safeTransferFrom(msg.sender, address(this), amount_);
    }
\u0060\u0060\u0060

so every new staker , needs claims from 0 
\u0060\u0060\u0060solidity
    function _claimRewards() internal returns (uint256) {
        // Claims all outstanding rewards for the user across epochs
        // If there are unclaimed rewards from epochs where the option token has expired, the rewards are lost

        // Get the last epoch claimed by the user
@>      uint48 userLastEpoch = lastEpochClaimed[msg.sender];

        // If the last epoch claimed is equal to the current epoch, then only try to claim for the current epoch
        if (userLastEpoch == epoch) return _claimEpochRewards(epoch);

        // If not, then the user has not claimed all rewards
        // Start at the last claimed epoch because they may not have completely claimed that epoch
        uint256 totalRewardsClaimed;
@>     for (uint48 i = userLastEpoch; i <= epoch; i++) {
            // For each epoch that the user has not claimed rewards for, claim the rewards
            totalRewardsClaimed += _claimEpochRewards(i);
        }

        return totalRewardsClaimed;
    }
\u0060\u0060\u0060
With each new addition of epoch, the new stake must consumes a lot of useless loops, from loop 0 to \u0060last epoch\u0060
When \u0060epoch\u0060 reaches a large size, it will result in GAS_OUT and the method cannot be executed

## Impact
When the \u0060epoch\u0060 gradually increases, the new take will waste a lot of GAS
When it is very large, it will cause GAS_OUT

## Code Snippet
https://github.com/sherlock-audit/2023-06-bond/blob/main/options/src/fixed-strike/liquidity-mining/OTLM.sol#L324-L327

## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060solidity
    function stake(
        uint256 amount_,
        bytes calldata proof_
    ) external nonReentrant requireInitialized updateRewards tryNewEpoch {
...
        if (userBalance > 0) {
            // Claim outstanding rewards, this will update the rewards per token claimed
            _claimRewards();
        } else {
            // Initialize the rewards per token claimed for the user to the stored rewards per token
            rewardsPerTokenClaimed[msg.sender] = rewardsPerTokenStored;
+           lastEpochClaimed[msg.sender] = epoch;
        }
\u0060\u0060\u0060

