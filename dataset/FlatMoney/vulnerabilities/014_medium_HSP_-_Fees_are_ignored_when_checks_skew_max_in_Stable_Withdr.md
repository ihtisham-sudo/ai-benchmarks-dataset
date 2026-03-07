# HSP - Fees are ignored when checks skew max in Stable Withdrawal /  Leverage Open / Leverage Adjust

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** FlatMoney
**Keywords:** cybersecurity, vulnerability, stable withdrawal, leverage open, leverage adjust, withdrawal fee, skew max, collateral, vault, skew fraction, protocol, trade fee, manual review, impact, risk assessment, financial security, smart contracts, decentralized finance, fee calculation, system integrity

---

HSP

medium

# Fees are ignored when checks skew max in Stable Withdrawal /  Leverage Open / Leverage Adjust

## Summary
Fees are ignored when checks skew max in Stable Withdrawal / Leverage Open / Leverage Adjust.

## Vulnerability Detail
When user [withdrawal from the stable LP](https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/StableModule.sol#L96-L100), vault **total stable collateral** is updated:
\u0060\u0060\u0060solidity
        vault.updateStableCollateralTotal(-int256(_amountOut));
\u0060\u0060\u0060
Then **_withdrawFee** is calculated and [checkSkewMax(...)](https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/FlatcoinVault.sol#L296) function is called to ensure that the system will not be too skewed towards longs:
\u0060\u0060\u0060solidity
            // Apply the withdraw fee if it\u0027s not the final withdrawal.
            _withdrawFee = (stableWithdrawFee * _amountOut) / 1e18;

            // additionalSkew = 0 because withdrawal was already processed above.
            vault.checkSkewMax({additionalSkew: 0});
\u0060\u0060\u0060
At the end of the execution, vault collateral is settled again with **withdrawFee**, keeper receives **keeperFee** and \u0060(amountOut - totalFee)\u0060 amount of collaterals are transferred to the user:
\u0060\u0060\u0060solidity
        // include the fees here to check for slippage
        amountOut -= totalFee;

        if (amountOut < stableWithdraw.minAmountOut)
            revert FlatcoinErrors.HighSlippage(amountOut, stableWithdraw.minAmountOut);

        // Settle the collateral
        vault.updateStableCollateralTotal(int256(withdrawFee)); // pay the withdrawal fee to stable LPs
        vault.sendCollateral({to: msg.sender, amount: order.keeperFee}); // pay the keeper their fee
        vault.sendCollateral({to: account, amount: amountOut}); // transfer remaining amount to the trader
\u0060\u0060\u0060
The \u0060totalFee\u0060 is composed of keeper fee and withdrawal fee:
\u0060\u0060\u0060solidity
        uint256 totalFee = order.keeperFee + withdrawFee;
\u0060\u0060\u0060
This means withdrawal fee is still in the vault, however this fee is ignored when checks skew max and protocol may revert on a safe withdrawal. Consider the following scenario:
1. **skewFractionMax** is \u0060120%\u0060 and **stableWithdrawFee** is \u00601%\u0060;
2. Alice deposits \u0060100\u0060 collateral and Bob opens a leverage position with size \u0060100\u0060;
3. At the moment, there is \u0060100\u0060 collaterals in the Vault, **skew** is \u00600\u0060 and **skew fraction** is \u0060100%\u0060;
4. Alice tries to withdraw \u006016.8\u0060 collaterals,  **withdrawFee** is \u00600.168\u0060, after withdrawal, it is expected that there is \u006083.368\u0060 stable collaterals in the Vault, so **skewFraction** should be \u0060119.5%\u0060, which is less than **skewFractionMax**;
5. However, the withdrawal will actually fail because when protocol checks skew max, **withdrawFee** is ignored and the **skewFraction** turns out to be \u0060120.19%\u0060, which is higher than **skewFractionMax**.

The same issue may occur when protocol executes a [leverage open](https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/LeverageModule.sol#L80-L84) and [leverage adjust](https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/LeverageModule.sol#L147-L151), in both executions, **tradeFee**  is ignored when checks skew max.

Please see the test codes:
\u0060\u0060\u0060solidity
    function test_audit_withdraw_fee_ignored_when_checks_skew_max() public {
        // skewFractionMax is 120%
        uint256 skewFractionMax = vaultProxy.skewFractionMax();
        assertEq(skewFractionMax, 120e16);

        // withdraw fee is 1%
        vm.prank(vaultProxy.owner());
        stableModProxy.setStableWithdrawFee(1e16);

        uint256 collateralPrice = 1000e8;

        uint256 depositAmount = 100e18;
        announceAndExecuteDeposit({
            traderAccount: alice,
            keeperAccount: keeper,
            depositAmount: depositAmount,
            oraclePrice: collateralPrice,
            keeperFeeAmount: 0
        });

        uint256 additionalSize = 100e18;
        announceAndExecuteLeverageOpen({
            traderAccount: bob,
            keeperAccount: keeper,
            margin: 50e18,
            additionalSize: 100e18,
            oraclePrice: collateralPrice,
            keeperFeeAmount: 0
        });

        // After leverage Open, skew is 0
        int256 skewAfterLeverageOpen = vaultProxy.getCurrentSkew();
        assertEq(skewAfterLeverageOpen, 0);
        // skew fraction is 100%
        uint256 skewFractionAfterLeverageOpen = getLongSkewFraction();
        assertEq(skewFractionAfterLeverageOpen, 1e18);

        // Note: comment out \u0060vault.checkSkewMax({additionalSkew: 0})\u0060 and below lines to see the actual skew fraction
        // Alice withdraws 16.8 collateral
        // uint256 aliceLpBalance = stableModProxy.balanceOf(alice);
        // announceAndExecuteWithdraw({
        //     traderAccount: alice, 
        //     keeperAccount: keeper, 
        //     withdrawAmount: 168e17, 
        //     oraclePrice: collateralPrice, 
        //     keeperFeeAmount: 0
        // });

        // // After withdrawal, the actual skew fraction is 119.9%, less than skewFractionMax
        // uint256 skewFactionAfterWithdrawal = getLongSkewFraction();
        // assertEq(skewFactionAfterWithdrawal, 1199501007580846367);

        // console2.log(WETH.balanceOf(address(vaultProxy)));
    }
\u0060\u0060\u0060

## Impact
Protocol may wrongly prevent a Stable Withdrawal / Leverage Open / Leverage Adjust even if the execution is essentially safe.

## Code Snippet
https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/StableModule.sol#L130
https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/LeverageModule.sol#L101
https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/LeverageModule.sol#L166

## Tool used
Manual Review

## Recommendation
Include withdrawal fee / trade fee when check skew max.

