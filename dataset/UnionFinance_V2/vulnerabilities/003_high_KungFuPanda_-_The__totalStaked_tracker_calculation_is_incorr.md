# KungFuPanda - The _totalStaked tracker calculation is incorrect and will be inflated due to the improper logic in the writeOffDebt function of the UserManager contract, leading to wrong Comptroller gInflationIndex being calculated and wrong user rewards being issued

**Severity:** high
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** cybersecurity, vulnerability, UserManager, Comptroller, gInflationIndex, debtWriteOff, totalStaked, inflationIndex, user rewards, scaled amount, realAmount, stake, unstake, batchUpdateFrozenInfo, accounting inflation, attack path, impact, mitigation, incorrect calculation, token amount

---

KungFuPanda

High

# The _totalStaked tracker calculation is incorrect and will be inflated due to the improper logic in the writeOffDebt function of the UserManager contract, leading to wrong Comptroller gInflationIndex being calculated and wrong user rewards being issued

### Summary

During \u0060debtWriteOff\u0060 call in the \u0060UserManager\u0060, subtracting the \u0060amount\u0060 instead of \u0060realAmount\u0060 will lead to the whole \u0060gInflationIndex\u0060 being inflated in the \u0060Comptroller\u0060 contract, as well as general accounting inflation.

Due to the \u0060UserManager\u0060\u0027s \u0060_totalStaked\u0060 being coupled with the \u0060Comptroller\u0060\u0027s \u0060gInflationIndex\u0060, the \u0060userInfo\u0060 stake\u0027s \u0060inflationIndex\u0060 will be calculated absolutely incorrectly:
\u0060\u0060\u0060solidity
    /**
     *  @dev Calculate currently unclaimed rewards
     *  @param account Account address
     *  @param token Staking token address
     *  @param totalStaked Effective total staked
     *  @param user User account global state
     *  @return Unclaimed rewards
     */
    function _calculateRewardsInternal(
        address account,
        address token,
        uint256 totalStaked,
        UserManagerAccountState memory user
    ) internal view returns (uint256) {
        Info memory userInfo = users[account][token];
        uint256 startInflationIndex = userInfo.inflationIndex; // @@ <<< this internally depends on the UserManager\u0027s _totalStaked variable
\u0060\u0060\u0060
And due to that, the whole user rewards calculation will be incorrect:
\u0060\u0060\u0060solidity

        uint256 rewardMultiplier = _getRewardsMultiplier(user);

        uint256 curInflationIndex = _getInflationIndexNew(totalStaked, getTimestamp() - gLastUpdated);

        if (curInflationIndex < startInflationIndex) revert InflationIndexTooSmall();

        return
            userInfo.accrued +
            (curInflationIndex - startInflationIndex).wadMul(user.effectiveStaked).wadMul(rewardMultiplier);
    }
\u0060\u0060\u0060
(https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/token/Comptroller.sol#L293)

Furthermore, during the reward accrual, there\u0027s another outcome of the miscalculated \u0060_totalStaked\u0060 and \u0060gInflationIndex\u0060 values:
\u0060\u0060\u0060solidity
    function _accrueRewards(address account, address token) private returns (uint256) {
        IUserManager userManager = _getUserManager(token);

        // Lookup global state from UserManager
        uint256 globalTotalStaked = userManager.globalTotalStaked(); // @@ <<< here a wrong _totalStaked amount is retrieved!!!

        // Lookup account state from UserManager
        UserManagerAccountState memory user = UserManagerAccountState(0, 0, false);
        (user.effectiveStaked, user.effectiveLocked, user.isMember) = userManager.onWithdrawRewards(account);

        uint256 amount = _calculateRewardsInternal(account, token, globalTotalStaked, user); // @@ <<< here a wrong amount is passed down to the calculation!

        // update the global states
        gInflationIndex = _getInflationIndexNew(globalTotalStaked, getTimestamp() - gLastUpdated);
        gLastUpdated = getTimestamp();
        users[account][token].inflationIndex = gInflationIndex;

        return amount;
    }
\u0060\u0060\u0060
Above is a reference from the \u0060Comptroller\u0060 contract: https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/token/Comptroller.sol#L220C1-L238C6.

### References for the main problem:
- https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/token/Comptroller.sol#L276
- https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/token/Comptroller.sol#L287

### The culprit\u0027s details are further explained below.

This is due to using a non-scaled \u0060amount\u0060 instead of the *scaled* \u0060realAmount\u0060 in the \u0060debtWriteOff\u0060 function here, in this line:
https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/user/UserManager.sol#L834

### Root Cause

In this update Union Finance adds distinct definitions for the \u0060actualAmount\u0060 *being the **real** scaled token amount*, and the \u0060amount\u0060 *being an unscaled nominal amount* that is to be scaled by \u0060stakingTokenDecimal\u0060, and is usually accepted as an argument for functions within the \u0060UserManager\u0060 contract.

Both \u0060stake\u0060 and \u0060unstake\u0060 functions track the \u0060totalStaked\u0060 balance as a **scaled** AND **real** token amount, as can be seen here: https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/user/UserManager.sol#L784. The snippet:
\u0060\u0060\u0060solidity
    function unstake(uint96 amount) external whenNotPaused nonReentrant {
        Staker storage staker = _stakers[msg.sender];

        // Stakers can only unstaked stake balance that is unlocked. Stake balance
        // becomes locked when it is used to underwrite a borrow.
        if (staker.stakedAmount - staker.locked < decimalScaling(amount, stakingTokenDecimal))
            revert InsufficientBalance();

        comptroller.withdrawRewards(msg.sender, stakingToken);

        uint256 remaining = IAssetManager(assetManager).withdraw(stakingToken, msg.sender, amount);
        if (remaining > amount) {
            revert AssetManagerWithdrawFailed();
        }
        uint96 actualAmount = decimalScaling(uint256(amount) - remaining, stakingTokenDecimal).toUint96();

        staker.stakedAmount -= actualAmount;
        _totalStaked -= actualAmount; // @@ <<< the actualAmount is subtracted

        emit LogUnstake(msg.sender, amount - remaining.toUint96());
    }
\u0060\u0060\u0060

And for \u0060stake\u0060 it\u0027s \u0060actualAmount\u0060 too (https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/user/UserManager.sol#L748), correspondingly:
\u0060\u0060\u0060solidity
    function stake(uint96 amount) public whenNotPaused nonReentrant {
        IERC20Upgradeable erc20Token = IERC20Upgradeable(stakingToken);
        uint96 actualAmount = decimalScaling(uint256(amount), stakingTokenDecimal).toUint96();
        comptroller.withdrawRewards(msg.sender, stakingToken);

        Staker storage staker = _stakers[msg.sender];

        if (staker.stakedAmount + actualAmount > _maxStakeAmount) revert StakeLimitReached();

        staker.stakedAmount += actualAmount;
        _totalStaked += actualAmount; // @@ <<< here you can see it!

        erc20Token.safeTransferFrom(msg.sender, address(this), amount);
        uint256 currentAllowance = erc20Token.allowance(address(this), assetManager);
        if (currentAllowance < amount) {
            erc20Token.safeIncreaseAllowance(assetManager, amount - currentAllowance);
        }

        if (!IAssetManager(assetManager).deposit(stakingToken, amount)) revert AssetManagerDepositFailed();
        emit LogStake(msg.sender, amount);
    }
\u0060\u0060\u0060

However, the \u0060debtWriteOff\u0060 function doesn\u0027t subtract the \u0060actualAmount\u0060, but decreases the \u0060_totalStaked\u0060 counter by a non-scaled \u0060amount\u0060 value:
\u0060\u0060\u0060solidity
        Staker storage staker = _stakers[stakerAddress];

        staker.stakedAmount -= actualAmount.toUint96();
        staker.locked -= actualAmount.toUint96();
        staker.lastUpdated = currTime.toUint64();

        _totalStaked -= amount;

        // update vouch trust amount
        vouch.trust -= actualAmount.toUint96();
        vouch.locked -= actualAmount.toUint96();
        vouch.lastUpdated = currTime.toUint64();
\u0060\u0060\u0060

Then here later in the \u0060batchUpdateFrozenInfo\u0060 function (that can be called by anyone and is unrestricted!), the \u0060Comptroller\u0060 contract is notified of the new \u0060_totalStaked\u0060 amount (https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/user/UserManager.sol#L1121):
\u0060\u0060\u0060solidity
        comptroller.updateTotalStaked(stakingToken, _totalStaked - _totalFrozen);
    }

    function globalTotalStaked() external view returns (uint256 globalTotal) {
        globalTotal = _totalStaked - _totalFrozen;
    }
\u0060\u0060\u0060

The problem lies in this change here: https://github.com/unioncredit/union-v2-contracts/pull/172/files#diff-e274f419b6384471f87c2b7d6a2c75150b95d37f3174a21d7d675ad20e3e4464R834

The \u0060Comptroller\u0060\u0027s \u0060updateTotalStaked\u0060 function gets called:
\u0060\u0060\u0060solidity
    /**
     *  @dev When total staked change update inflation index
     *  @param totalStaked totalStaked amount
     *  @return Whether succeeded
     */
    function updateTotalStaked(
        address token,
        uint256 totalStaked
    ) external override whenNotPaused onlyUserManager(token) returns (bool) {
        if (totalStaked > 0) {
            gInflationIndex = _getInflationIndexNew(totalStaked, getTimestamp() - gLastUpdated);
            gLastUpdated = getTimestamp();
        }

        return true;
    }
\u0060\u0060\u0060

And finally, the \u0060gInflationIndex\u0060 value will be inflated.

### Internal pre-conditions

1. As far as I can tell, the attack will be unintentional in most cases, happening automatically on each \u0060debtWriteOff\u0060 call, because the culprit is an improper calculation.
2. Or this can be utilized together with calling \u0060batchUpdateFrozenInfo\u0060 to inflate the \u0060gInflationIndex\u0060 value intentionally and cause the \u0060Comptroller\u0060\u0027s \u0060_getInflationIndexNew\u0060 to return incorrect results:
\u0060\u0060\u0060solidity
            gInflationIndex = _getInflationIndexNew(totalStaked, getTimestamp() - gLastUpdated);
\u0060\u0060\u0060

### External pre-conditions

None. The bug is just implicitly there.

### Attack Path

As it\u0027s a mistake in the \u0060_totalStaked\u0060 calculation logic, there\u0027s no particular trigger for this attack, as it will happen if any user \u0060write\u0060\u0027s\u0060OffDebt\u0060.

### Impact

The whole \u0060gInflationIndex\u0060 will be inflated, and will be calculated incorrectly.

Besides that, tracking the wrong amount of the currently active staked tokens will be misleading for the external users that refer to that value.

### PoC

None. Please leave me a comment if you request one from me.

### Mitigation

Instead of subtracting \u0060amount\u0060, you should subtract the \u0060actualAmount\u0060 from the \u0060_totalStaked\u0060 variable here in \u0060writeOffDebt\u0060:
\u0060\u0060\u0060diff

        Staker storage staker = _stakers[stakerAddress];

        staker.stakedAmount -= actualAmount.toUint96();
        staker.locked -= actualAmount.toUint96();
        staker.lastUpdated = currTime.toUint64();

-      _totalStaked -= amount;
+      _totalStaked -= actualAmount;

        // update vouch trust amount
        vouch.trust -= actualAmount.toUint96();
        vouch.locked -= actualAmount.toUint96();
        vouch.lastUpdated = currTime.toUint64();
\u0060\u0060\u0060
