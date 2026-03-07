# 0x73696d616f - DoSed liquidations as \u0060PrizeVault::liquidatableBalanceOf()\u0060 does not take into account the \u0060mintLimit\u0060 when the token out is the asset

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, DoS attack, liquidations, PrizeVault, liquidatableBalanceOf, mintLimit, minted yield fee, TpdaLiquidationPair, swapExactAmountOut, maxAmountOut, yield fee, liquidation pair, smart contracts, liquidity, revert, impact, manual review, code snippet, recommendation

---

0x73696d616f

medium

# DoSed liquidations as \u0060PrizeVault::liquidatableBalanceOf()\u0060 does not take into account the \u0060mintLimit\u0060 when the token out is the asset

## Summary

\u0060PrizeVault::liquidatableBalanceOf()\u0060 is called in \u0060TpdaLiquidationPair::_availableBalance()\u0060 to get the maximum amount to liquidate, which will be incorrect when \u0060_tokenOut\u0060 is the \u0060asset\u0060 of the \u0060PrizeVault\u0060, due to not taking the minted yield fee into account. Thus, it will overestimate the amount to liquidate and revert.

## Vulnerability Detail

\u0060TpdaLiquidationPair::_availableBalance()\u0060 is called in \u0060TpdaLiquidationPair::swapExactAmountOut()\u0060 to revert if the amount to liquidate exceeds the maximum and in \u0060TpdaLiquidationPair::maxAmountOut()\u0060 to get the maximum liquidatable amount. Thus, users or smart contracts will [call](https://dev.pooltogether.com/protocol/guides/bots/liquidating-yield/#2-compute-the-available-liquidity) \u0060TpdaLiquidationPair::maxAmountOut()\u0060 to get the maximum amount out and then \u0060TpdaLiquidationPair::swapExactAmountOut()\u0060 with this amount to liquidate.
> Compute how much yield is available using the [maxAmountOut](https://dev.pooltogether.com/protocol/reference/liquidator/TpdaLiquidationPair#maxamountout) function on the Liquidation Pair. This function returns the maximum number of tokens you can swap out.

However, this is going to revert whenever the minted yield fee exceeds the mint limit, as \u0060PrizeVault::liquidatableBalanceOf()\u0060 does not consider it when the asset to liquidate is the asset of the \u0060PrizeVault\u0060. Consider \u0060PrizeVault::liquidatableBalanceOf()\u0060:
\u0060\u0060\u0060solidity
function liquidatableBalanceOf(address _tokenOut) external view returns (uint256) {
    ...
    } else if (_tokenOut == address(_asset)) { //@audit missing yield percentage for mintLimit
        // Liquidation of yield assets is capped at the max yield vault withdraw plus any latent balance.
        _maxAmountOut = _maxYieldVaultWithdraw() + _asset.balanceOf(address(this));
    }
    ...
}
\u0060\u0060\u0060
As can be seen from the code snipped above, the minted yield fee is not taken into account and the mint limit is not calculated. On \u0060PrizeVault::transferTokensOut()\u0060, a mint fee given by \u0060_yieldFee = (_amountOut * FEE_PRECISION) / (FEE_PRECISION - _yieldFeePercentage) - _amountOut;\u0060 is always minted and the limit is enforced at the end of the function \u0060_enforceMintLimit(_totalDebtBefore, _yieldFee);\u0060. Thus, without limiting the liquidatable assets to the amount that would trigger a yield fee that reaches the mint limit, liquidations will be DoSed.

## Impact

DoSed liquidations when the asset out is the asset of the \u0060PrizeVault\u0060.

## Code Snippet

https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-vault/src/PrizeVault.sol#L693-L696

## Tool used

Manual Review

Vscode

## Recommendation

The correct formula can be obtained by inverting \u0060_yieldFee = (_amountOut * FEE_PRECISION) / (FEE_PRECISION - _yieldFeePercentage) - _amountOut;\u0060, leading to:
\u0060\u0060\u0060solidity
function liquidatableBalanceOf(address _tokenOut) external view returns (uint256) {
    ...
    } else if (_tokenOut == address(_asset)) {
        // Liquidation of yield assets is capped at the max yield vault withdraw plus any latent balance.
        _maxAmountOut = _maxYieldVaultWithdraw() + _asset.balanceOf(address(this));
        // Limit to the fee amount
        uint256  mintLimitDueToFee = (FEE_PRECISION - yieldFeePercentage) * _mintLimit(_totalDebt) / yieldFeePercentage;
       _maxAmountOut = _maxAmountOut >= mintLimitDueToFee ? mintLimitDueToFee : _maxAmountOut;
    }
    ...
}
\u0060\u0060\u0060

