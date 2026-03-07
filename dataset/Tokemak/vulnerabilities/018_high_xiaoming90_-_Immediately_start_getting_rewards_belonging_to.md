# xiaoming90 - Immediately start getting rewards belonging to others after staking

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, malicious users, reward tokens, staking, accounting error, LMPVault, DV, ERC20, _mint function, _afterTokenTransfer, MainRewarder, _updateReward, snapshot, earned rewards, stakeTracker, userRewardPerTokenPaid, withdraw, impact, manual review, recommendation

---

xiaoming90

high

# Immediately start getting rewards belonging to others after staking
## Summary

Malicious users could abuse the accounting error to immediately start getting rewards belonging to others after staking, leading to a loss of reward tokens.

## Vulnerability Detail

> **Note**
> This issue affects both LMPVault and DV since they use the same underlying reward contract.

Assume a new user called Bob mints 100 LMPVault or DV shares. The ERC20\u0027s \u0060_mint\u0060 function will be called, which will first increase Bob\u0027s balance at Line 267 and then trigger the \u0060_afterTokenTransfer\u0060 hook at Line 271.

https://github.com/OpenZeppelin/openzeppelin-contracts/blob/0457042d93d9dfd760dbaa06a4d2f1216fdbe297/contracts/token/ERC20/ERC20.sol#L259

\u0060\u0060\u0060solidity
File: ERC20.sol
259:     function _mint(address account, uint256 amount) internal virtual {
..SNIP..
262:         _beforeTokenTransfer(address(0), account, amount);
263: 
264:         _totalSupply += amount;
265:         unchecked {
266:             // Overflow not possible: balance + amount is at most totalSupply + amount, which is checked above.
267:             _balances[account] += amount;
268:         }
..SNIP..
271:         _afterTokenTransfer(address(0), account, amount);
272:     }
\u0060\u0060\u0060

The \u0060_afterTokenTransfer\u0060 hook will automatically stake the newly minted shares to the rewarder contracts on behalf of Bob.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L854

\u0060\u0060\u0060solidity
File: LMPVault.sol
854:     function _afterTokenTransfer(address from, address to, uint256 amount) internal virtual override {
..SNIP..
862:         if (to != address(0)) {
863:             rewarder.stake(to, amount);
864:         }
865:     }
\u0060\u0060\u0060

Within the \u0060MainRewarder.stake\u0060 function, it will first call the \u0060_updateReward\u0060 function at Line 87 to take a snapshot of accumulated rewards. Since Bob is a new user, his accumulated rewards should be zero. However, this turned out to be false due to the bug described in this report.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/MainRewarder.sol#L86

\u0060\u0060\u0060solidity
File: MainRewarder.sol
86:     function stake(address account, uint256 amount) public onlyStakeTracker {
87:         _updateReward(account);
88:         _stake(account, amount);
89: 
90:         for (uint256 i = 0; i < extraRewards.length; ++i) {
91:             IExtraRewarder(extraRewards[i]).stake(account, amount);
92:         }
93:     }
\u0060\u0060\u0060

When the \u0060_updateReward\u0060 function is executed, it will compute Bob\u0027s earned rewards.  It is important to note that at this point, Bob\u0027s balance has already been updated to 100 shares in the \u0060stakeTracker\u0060 contract, and \u0060userRewardPerTokenPaid[Bob]\u0060 is zero.

Bob\u0027s earned reward will be as follows, where $r$ is the \u0060rewardPerToken()\u0060:

$$
earned(Bob) = 100\ {shares \times (r - 0)} = 100r
$$

Bob immediately accumulated a reward of $100r$ upon staking into the rewarder contract, which is incorrect. Bob could withdraw $100r$ reward tokens that do not belong to him.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/AbstractRewarder.sol#L128

\u0060\u0060\u0060solidity
File: AbstractRewarder.sol
128:     function _updateReward(address account) internal {
129:         uint256 earnedRewards = 0;
130:         rewardPerTokenStored = rewardPerToken();
131:         lastUpdateBlock = lastBlockRewardApplicable();
132: 
133:         if (account != address(0)) {
134:             earnedRewards = earned(account);
135:             rewards[account] = earnedRewards;
136:             userRewardPerTokenPaid[account] = rewardPerTokenStored;
137:         }
138: 
139:         emit UserRewardUpdated(account, earnedRewards, rewardPerTokenStored, lastUpdateBlock);
140:     }
..SNIP..
155:     function balanceOf(address account) public view returns (uint256) {
156:         return stakeTracker.balanceOf(account);
157:     }
..SNIP..
204:     function earned(address account) public view returns (uint256) {
205:         return (balanceOf(account) * (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18) + rewards[account];
206:     }
\u0060\u0060\u0060

## Impact

Loss of reward tokens for the vault shareholders.

## Code Snippet

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L854

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/MainRewarder.sol#L86

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/rewarders/AbstractRewarder.sol#L128

## Tool used

Manual Review

## Recommendation

Ensure that the balance of the users in the rewarder contract is only incremented after the \u0060_updateReward\u0060 function is executed.

One option is to track the balance of the staker and total supply internally within the rewarder contract and avoid reading the states in the \u0060stakeTracker\u0060 contract, commonly seen in many reward contracts.

\u0060\u0060\u0060diff
File: AbstractRewarder.sol
function balanceOf(address account) public view returns (uint256) {
-   return stakeTracker.balanceOf(account);
+	return _balances[account];
}
\u0060\u0060\u0060

\u0060\u0060\u0060diff
File: AbstractRewarder.sol
function _stake(address account, uint256 amount) internal {
    Errors.verifyNotZero(account, "account");
    Errors.verifyNotZero(amount, "amount");
    
+    _totalSupply += amount
+    _balances[account] += amount

    emit Staked(account, amount);
}
\u0060\u0060\u0060
