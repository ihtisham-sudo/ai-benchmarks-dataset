# Aymen0909 - Incorrect amount given as input to \u0060_handleRebalanceIn\u0060 when \u0060flashRebalance\u0060 is called

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, flashRebalance, rebalance operation, DOS, insufficient amount error, tokenInBalanceAfter, tokenInBalanceBefore, flashloan, deposit amount, input amount, destination vault, LMPVault, manual review, code review, smart contract, error handling, funds transfer, rebalancing error, security recommendation

---

Aymen0909

high

# Incorrect amount given as input to \u0060_handleRebalanceIn\u0060 when \u0060flashRebalance\u0060 is called
## Summary

When \u0060flashRebalance\u0060 is called, the wrong deposit amount is given to the \u0060_handleRebalanceIn\u0060 function as the whole \u0060tokenInBalanceAfter\u0060 amount is given as input instead of the delta value \u0060tokenInBalanceAfter - tokenInBalanceBefore\u0060, this will result in an incorrect rebalance operation and can potentialy lead to a DOS due to the insufficient amount error.

## Vulnerability Detail

The issue occurs in the \u0060flashRebalance\u0060 function below :

\u0060\u0060\u0060solidity
function flashRebalance(
    DestinationInfo storage destInfoOut,
    DestinationInfo storage destInfoIn,
    IERC3156FlashBorrower receiver,
    IStrategy.RebalanceParams memory params,
    FlashRebalanceParams memory flashParams,
    bytes calldata data
) external returns (uint256 idle, uint256 debt) {
    ...

    // Handle increase (shares coming "In", getting underlying from the swapper and trading for new shares)
    if (params.amountIn > 0) {
        IDestinationVault dvIn = IDestinationVault(params.destinationIn);

        // get "before" counts
        uint256 tokenInBalanceBefore = IERC20(params.tokenIn).balanceOf(address(this));

        // Give control back to the solver so they can make use of the "out" assets
        // and get our "in" asset
        bytes32 flashResult = receiver.onFlashLoan(msg.sender, params.tokenIn, params.amountIn, 0, data);

        // We assume the solver will send us the assets
        uint256 tokenInBalanceAfter = IERC20(params.tokenIn).balanceOf(address(this));

        // Make sure the call was successful and verify we have at least the assets we think
        // we were getting
        if (
            flashResult != keccak256("ERC3156FlashBorrower.onFlashLoan")
                || tokenInBalanceAfter < tokenInBalanceBefore + params.amountIn
        ) {
            revert Errors.FlashLoanFailed(params.tokenIn, params.amountIn);
        }

        if (params.tokenIn != address(flashParams.baseAsset)) {
            // @audit should be \u0060tokenInBalanceAfter - tokenInBalanceBefore\u0060 given to \u0060_handleRebalanceIn\u0060
            (uint256 debtDecreaseIn, uint256 debtIncreaseIn) =
                _handleRebalanceIn(destInfoIn, dvIn, params.tokenIn, tokenInBalanceAfter);
            idleDebtChange.debtDecrease += debtDecreaseIn;
            idleDebtChange.debtIncrease += debtIncreaseIn;
        } else {
            idleDebtChange.idleIncrease += tokenInBalanceAfter - tokenInBalanceBefore;
        }
    }
    ...
}
\u0060\u0060\u0060

As we can see from the code above, the function executes a flashloan in order to receive th tokenIn amount which should be the difference between \u0060tokenInBalanceAfter\u0060 (balance of the contract after the flashloan) and \u0060tokenInBalanceBefore\u0060 (balance of the contract before the flashloan) : \u0060tokenInBalanceAfter - tokenInBalanceBefore\u0060.

But when calling the \u0060_handleRebalanceIn\u0060 function the wrong deposit amount is given as input, as the total balance \u0060tokenInBalanceAfter\u0060 is used instead of the received amount \u0060tokenInBalanceAfter - tokenInBalanceBefore\u0060.

Because the \u0060_handleRebalanceIn\u0060 function is supposed to deposit the input amount to the destination vault, this error can result in sending a larger amount of funds to DV then what was intended or this error can cause a DOS of the \u0060flashRebalance\u0060 function (due to the insufficient amount error when performing the transfer to DV), all of this will make the rebalance operation fail (or not done correctely) which can have a negative impact on the LMPVault.

## Impact

See summary

## Code Snippet

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/libs/LMPDebt.sol#L185-L215

## Tool used

Manual Review

## Recommendation

Use the correct received tokenIn amount \u0060tokenInBalanceAfter - tokenInBalanceBefore\u0060 as input to the \u0060_handleRebalanceIn\u0060 function :

\u0060\u0060\u0060solidity
function flashRebalance(
    DestinationInfo storage destInfoOut,
    DestinationInfo storage destInfoIn,
    IERC3156FlashBorrower receiver,
    IStrategy.RebalanceParams memory params,
    FlashRebalanceParams memory flashParams,
    bytes calldata data
) external returns (uint256 idle, uint256 debt) {
    ...

    // Handle increase (shares coming "In", getting underlying from the swapper and trading for new shares)
    if (params.amountIn > 0) {
        IDestinationVault dvIn = IDestinationVault(params.destinationIn);

        // get "before" counts
        uint256 tokenInBalanceBefore = IERC20(params.tokenIn).balanceOf(address(this));

        // Give control back to the solver so they can make use of the "out" assets
        // and get our "in" asset
        bytes32 flashResult = receiver.onFlashLoan(msg.sender, params.tokenIn, params.amountIn, 0, data);

        // We assume the solver will send us the assets
        uint256 tokenInBalanceAfter = IERC20(params.tokenIn).balanceOf(address(this));

        // Make sure the call was successful and verify we have at least the assets we think
        // we were getting
        if (
            flashResult != keccak256("ERC3156FlashBorrower.onFlashLoan")
                || tokenInBalanceAfter < tokenInBalanceBefore + params.amountIn
        ) {
            revert Errors.FlashLoanFailed(params.tokenIn, params.amountIn);
        }

        if (params.tokenIn != address(flashParams.baseAsset)) {
            // @audit Use \u0060tokenInBalanceAfter - tokenInBalanceBefore\u0060 as input
            (uint256 debtDecreaseIn, uint256 debtIncreaseIn) =
                _handleRebalanceIn(destInfoIn, dvIn, params.tokenIn, tokenInBalanceAfter - tokenInBalanceBefore);
            idleDebtChange.debtDecrease += debtDecreaseIn;
            idleDebtChange.debtIncrease += debtIncreaseIn;
        } else {
            idleDebtChange.idleIncrease += tokenInBalanceAfter - tokenInBalanceBefore;
        }
    }
    ...
}
\u0060\u0060\u0060
