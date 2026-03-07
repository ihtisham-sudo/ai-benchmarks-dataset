# panprog - Bad debt liquidation doesn\u0027t allow liquidator to receive its ETH bonus (ante)

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Aloe II
**Keywords:** bad debt, liquidation, ETH bonus, liquidator, borrower, assets, repay, swap, revert, liabilities, incentive, strain, WETH, DAI, smart contract, compensation, test, manual review, proof of concept, financial loss

---

panprog

medium

# Bad debt liquidation doesn\u0027t allow liquidator to receive its ETH bonus (ante)
## Summary

When bad debt liquidation happens, user account will still have borrows, but no assets to repay them. In such case, and when borrow is only in 1 token, \u0060Borrower.liquidate\u0060 code will still try to swap the other asset (which account doesn\u0027t have) and will revert trying to transfer that asset to callee.

The following code will repay all assets, but since it\u0027s bad debt, one of the liabilities will remain non-0:
\u0060\u0060\u0060solidity
uint256 repayable0 = Math.min(liabilities0, TOKEN0.balanceOf(address(this)));
uint256 repayable1 = Math.min(liabilities1, TOKEN1.balanceOf(address(this)));

// See what remains (similar to "shortfall" in BalanceSheet)
liabilities0 -= repayable0;
liabilities1 -= repayable1;
\u0060\u0060\u0060

\u0060shouldSwap\u0060 will then be set to \u0060true\u0060, because exactly one of liabilities is non-0:
\u0060\u0060\u0060solidity
bool shouldSwap;
assembly ("memory-safe") {
    // If both are zero or neither is zero, there\u0027s nothing more to do
    shouldSwap := xor(gt(liabilities0, 0), gt(liabilities1, 0))
    // Divide by \u0060strain\u0060 and check again. This second check can generate false positives in cases
    // where one division (not both) floors to 0, which is why we \u0060and()\u0060 with the check above.
    liabilities0 := div(liabilities0, strain)
    liabilities1 := div(liabilities1, strain)
    shouldSwap := and(shouldSwap, xor(gt(liabilities0, 0), gt(liabilities1, 0)))
    // If not swapping, set \u0060incentive1 = 0\u0060
    incentive1 := mul(shouldSwap, incentive1)
}
\u0060\u0060\u0060
\u0060incentive1\u0060 will also have some value (5% from the bad debt amount)

When trying to swap, the execution will revert in TOKEN0 or TOKEN1 \u0060safeTransfer\u0060, because account has 0 of this token:
\u0060\u0060\u0060solidity
if (liabilities0 > 0) {
    // NOTE: This value is not constrained to \u0060TOKEN1.balanceOf(address(this))\u0060, so liquidators
    // are responsible for setting \u0060strain\u0060 such that the transfer doesn\u0027t revert. This shouldn\u0027t
    // be an issue unless the borrower has already started accruing bad debt.
    uint256 available1 = mulDiv128(liabilities0, priceX128) + incentive1;

    TOKEN1.safeTransfer(address(callee), available1);
    callee.swap1For0(data, available1, liabilities0);

    repayable0 += liabilities0;
} else {
    // NOTE: This value is not constrained to \u0060TOKEN0.balanceOf(address(this))\u0060, so liquidators
    // are responsible for setting \u0060strain\u0060 such that the transfer doesn\u0027t revert. This shouldn\u0027t
    // be an issue unless the borrower has already started accruing bad debt.
    uint256 available0 = Math.mulDiv(liabilities1 + incentive1, Q128, priceX128);

    TOKEN0.safeTransfer(address(callee), available0);
    callee.swap0For1(data, available0, liabilities1);

    repayable1 += liabilities1;
}
\u0060\u0060\u0060

There are only 2 possible ways to work around this problem:
1. Use very high value of \u0060strain\u0060. This will divide remaining liabilities by large value, making them 0 and will at least repay the remaining assets account has. However, in such case liquidator will get almost no bonus ETH (ante), because it will be divided by \u0060strain\u0060:
\u0060\u0060\u0060solidity
payable(callee).transfer(address(this).balance / strain);
\u0060\u0060\u0060

2. Transfer enough assets to bad debt account to cover its bad debt and finish the liquidation successfully, getting the bonus ETH. However, this will still be a loss of funds for the liquidator, because it will have to cover bad debt from its own assets, which is a loss for liquidator.

So the issue described here leads to liquidator not receiving compensation from bad debt liquidations of accounts which have remaining bad debt in only 1 asset. Ante (bonus ETH for liquidator) will be stuck in the liquidated account and nobody will be able to retrieve it without repaying bad debt for the account.

## Vulnerability Detail

More detailed scenario
1. Alice account goes into bad debt for whatever reason. For example, the account has 150 DAI borrowed, but only 100 DAI assets.
2. Bob tries to liquidate Alice account, but his transaction reverts, because remaining DAI liability after repaying 100 DAI assets Alice has, will be 50 DAI bad debt. \u0060liquidate\u0060 code will try to call Bob\u0027s callee contract to swap 0.03 WETH to 50 DAI sending it 0.03 WETH. However, since Alice account has 0 WETH, the transfer will revert.
3. Bob tries to work around the liquidation problem:
3.1. Bob calls \u0060liquidate\u0060 with \u0060strain\u0060 set to \u0060type(uint256).max\u0060. Liquidation succeeds, but Bob doesn\u0027t receive anything for his liquidation (he receives 0 ETH bonus). Alice\u0027s ante is stuck in the contract until Alice bad debt is fully repaid.
3.2. Bob sends 0.03 WETH directly to Alice account and calls \u0060liquidate\u0060 normally. It succeeds and Bob gets his bonus for liquidation (0.01 ETH). He has 0.02 ETH net loss from liquidaiton (in addition to gas fees).

In both cases there is no incentive for Bob to liquidate Alice. So it\u0027s likely Alice account won\u0027t be liquidated and a borrow of 150 will be stuck in Alice account for a long time. Some lender depositors who can\u0027t withdraw might still have incentive to liquidate Alice to be able to withdraw from lender, but Alice\u0027s ante will still be stuck in the contract.

## Impact

Liquidators are not compensated for bad debt liquidations in some cases. Ante (liquidator bonus) is stuck in the borrower smart contract until bad debt is repaid. There is not enough incentive to liquidate such bad debt accounts, which can lead for these accounts to accumulate even bigger bad debt and lender depositors being unable to withdraw their funds from lender.

## Proof of concept

The scenario above is demonstrated in the test, add it to test/Liquidator.t.sol:
\u0060\u0060\u0060ts
    function test_badDebtLiquidationAnte() public {

        // malicious user borrows at max leverage + some safety margin
        uint256 margin0 = 1e18;
        uint256 borrows0 = 100e18;

        deal(address(asset0), address(account), margin0);

        bytes memory data = abi.encode(Action.BORROW, borrows0, 0);
        account.modify(this, data, (1 << 32));

        // borrow increased by 50%
        _setInterest(lender0, 15000);

        emit log_named_uint("User borrow:", lender0.borrowBalance(address(account)));
        emit log_named_uint("User assets:", asset0.balanceOf(address(account)));

        // warn account
        account.warn((1 << 32));

        // skip warning time
        skip(LIQUIDATION_GRACE_PERIOD);
        lender0.accrueInterest();

        // liquidation reverts because it requires asset the account doesn\u0027t have to swap
        vm.expectRevert();
        account.liquidate(this, bytes(""), 1, (1 << 32));

        // liquidate with max strain to avoid revert when trying to swap assets account doesn\u0027t have
        account.liquidate(this, bytes(""), type(uint256).max, (1 << 32));

        emit log_named_uint("Liquidated User borrow:", lender0.borrowBalance(address(account)));
        emit log_named_uint("Liquidated User assets:", asset0.balanceOf(address(account)));
        emit log_named_uint("Liquidated User ante:", address(account).balance);
    }
\u0060\u0060\u0060

Execution console log:
\u0060\u0060\u0060solidity
  User borrow:: 150000000000000000000
  User assets:: 101000000000000000000
  Liquidated User borrow:: 49000000162000000001
  Liquidated User assets:: 0
  Liquidated User ante:: 10000000000000001
\u0060\u0060\u0060

## Code Snippet

\u0060Borrower.liquidate\u0060 calculates remaining liabilities after assets are used to repay borrows:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L231-L236

Notice, that if both assets are 0, \u0060liabilities0\u0060 or \u0060liabilities1\u0060 will still be non-0 if bad debt has happened.

Since either \u0060liabilities0\u0060 or \u0060liabilities\u0060 are non-0, \u0060shouldSwap\u0060 is set to true:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L239-L250

When trying to swap, revert will happen either here:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L263

or here:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L273

## Tool used

Manual Review

## Recommendation

Consider verifying the bad debt situation and not forcing swap which will fail, so that liquidation can repay whatever assets account still has and give liquidator its full bonus.

