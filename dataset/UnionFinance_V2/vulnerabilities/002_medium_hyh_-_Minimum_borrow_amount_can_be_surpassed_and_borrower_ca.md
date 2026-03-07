# hyh - Minimum borrow amount can be surpassed and borrower can be treated as being overdue earlier than their actual overdue time

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** cybersecurity, vulnerability, UToken, borrow, minBorrow, assetManager, liquidity, overdue, lastRepay, market conditions, withdrawals, dust amount, material debt, checkIsOverdue, stakerFrozen, frozenCoinAge, staking rewards, manual review, effective amount, loanable amount

---

hyh

Medium

# Minimum borrow amount can be surpassed and borrower can be treated as being overdue earlier than their actual overdue time

## Summary

It is possible to borrow less than \u0060_minBorrow\u0060 and preliminary be marked as overdue when \u0060assetManager\u0060 have temporary fund access limitations.

## Vulnerability Detail

UToken\u0027s \u0060borrow()\u0060 can be effectively run with lesser amount than \u0060_minBorrow\u0060 when it is a liquidity shortage in the asset manager\u0027s underlying markets and they can return only some dust amount or nothing at all. In these cases \u0060borrow()\u0060 call will still be concluded. Particularly, it is possible to run it with zero amount when \u0060assetManager\u0060 cannot access liquidity.

In that case the borrower, if they borrow for the first time after full repay, will not have their \u0060lastRepay\u0060 field reset on a subsequent material borrow operations as it will already be set on zero amount borrow before. As a result such borrowers can be effectively overdue for the system way before the actual overdue time passes for them.

## Impact

\u0060_minBorrow\u0060 threshold can be violated when market conditions restrict \u0060assetManager\u0060 withdrawals. A user can have \u0060lastRepay\u0060 set earlier than time of obtaining the funds, which will mark them overdue before the actual overdue time comes by. This will have a material adverse impact both on such a borrower (for them \u0060checkIsOverdue\u0060 will be true, so they won\u0027t be able to borrow or create vouches) and their lenders (for them \u0060stakerFrozen\u0060 and \u0060frozenCoinAge\u0060 will be increased and staking rewards diminished).

## Code Snippet

If current market conditions don\u0027t allow any material withdrawal then \u0060borrow()\u0060 still can happen and \u0060lastRepay\u0060 be set on any dust or even zero amount being lent out:

[UToken.sol#L611-L634](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L611-L634)

\u0060\u0060\u0060solidity
    function borrow(address to, uint256 amount) external override onlyMember(msg.sender) whenNotPaused nonReentrant {
        IAssetManager assetManagerContract = IAssetManager(assetManager);
        uint256 actualAmount = decimalScaling(amount, underlyingDecimal);
>>      if (actualAmount < _minBorrow) revert AmountLessMinBorrow();

        // Calculate the origination fee
        uint256 fee = calculatingFee(actualAmount);

        if (_borrowBalanceView(msg.sender) + actualAmount + fee > _maxBorrow) revert AmountExceedMaxBorrow();
        if (checkIsOverdue(msg.sender)) revert MemberIsOverdue();
        if (amount > assetManagerContract.getLoanableAmount(underlying)) revert InsufficientFundsLeft();
        if (!accrueInterest()) revert AccrueInterestFailed();

        uint256 borrowedAmount = borrowBalanceStoredInternal(msg.sender);

        // Initialize the last repayment date to the current block timestamp
>>      if (getLastRepay(msg.sender) == 0) {
            accountBorrows[msg.sender].lastRepay = getTimestamp();
        }

        // Withdraw the borrowed amount of tokens from the assetManager and send them to the borrower
>>      uint256 remaining = assetManagerContract.withdraw(underlying, to, amount);
>>      if (remaining > amount) revert WithdrawFailed();
>>      actualAmount -= decimalScaling(remaining, underlyingDecimal);
\u0060\u0060\u0060

If market is such that \u0060assetManagerContract.withdraw\u0060 can only withdraw dust or can\u0027t withdraw anything, a user can request to borrow an amount bigger than minimal, but \u0060borrow()\u0060 will be executed with some dust or even zero amount effectively borrowed. This isn\u0027t fully covered by the \u0060getLoanableAmount()\u0060 check since it measures total funds invested via \u0060getSupplyView()\u0060 calls to the underlying markets.

As \u0060_minBorrow\u0060 is for amount effectively borrowed, and not just for amount requested, it will be in a violation:

[UToken.sol#L141-L144](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L141-L144)

\u0060\u0060\u0060solidity
    /**
>>   *  @dev Min amount that can be borrowed by a single member
     */
    uint256 private _minBorrow;
\u0060\u0060\u0060

Also, it will have a side effect of resetting \u0060lastRepay\u0060 even with zero amount borrowed when the borrower had no debt as of time of the call. This will effectively mark a borrower as an overdue when time since they obtained any material debt is in fact much less than \u0060overdueTime\u0060:

[UToken.sol#L459-L465](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L459-L465)

\u0060\u0060\u0060solidity
    function checkIsOverdue(address account) public view override returns (bool isOverdue) {
        if (_getBorrowed(account) != 0) {
>>          uint256 lastRepay = getLastRepay(account);
>>          uint256 diff = getTimestamp() - lastRepay;
>>          isOverdue = overdueTime < diff;
        }
    }
\u0060\u0060\u0060

[UToken.sol#L450-L452](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L450-L452)

\u0060\u0060\u0060solidity
    function getLastRepay(address account) public view override returns (uint256) {
        return accountBorrows[account].lastRepay;
    }
\u0060\u0060\u0060

This can happen as subsequent \u0060borrow()\u0060 calls will not set \u0060lastRepay\u0060 as the logic is based on having empty \u0060lastRepay\u0060:

[UToken.sol#L627-L629](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L627-L629)

\u0060\u0060\u0060solidity
        if (getLastRepay(msg.sender) == 0) {
            accountBorrows[msg.sender].lastRepay = getTimestamp();
        }
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation

Consider controlling the effective amount being borrowed, e.g.:

[UToken.sol#L611-L634](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L611-L634)

\u0060\u0060\u0060diff
    function borrow(address to, uint256 amount) external override onlyMember(msg.sender) whenNotPaused nonReentrant {
        IAssetManager assetManagerContract = IAssetManager(assetManager);
        uint256 actualAmount = decimalScaling(amount, underlyingDecimal);
-       if (actualAmount < _minBorrow) revert AmountLessMinBorrow();

        // Calculate the origination fee
        uint256 fee = calculatingFee(actualAmount);

        if (_borrowBalanceView(msg.sender) + actualAmount + fee > _maxBorrow) revert AmountExceedMaxBorrow();
        if (checkIsOverdue(msg.sender)) revert MemberIsOverdue();
        if (amount > assetManagerContract.getLoanableAmount(underlying)) revert InsufficientFundsLeft();
        if (!accrueInterest()) revert AccrueInterestFailed();

        uint256 borrowedAmount = borrowBalanceStoredInternal(msg.sender);

        // Initialize the last repayment date to the current block timestamp
        if (getLastRepay(msg.sender) == 0) {
            accountBorrows[msg.sender].lastRepay = getTimestamp();
        }

        // Withdraw the borrowed amount of tokens from the assetManager and send them to the borrower
        uint256 remaining = assetManagerContract.withdraw(underlying, to, amount);
        if (remaining > amount) revert WithdrawFailed();
        actualAmount -= decimalScaling(remaining, underlyingDecimal);
+       if (actualAmount < _minBorrow) revert AmountLessMinBorrow();
\u0060\u0060\u0060
