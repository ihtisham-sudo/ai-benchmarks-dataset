# MiloTruck - \u0060TpdaLiquidationPair.swapExactAmountOut()\u0060 can be DOSed by a vault\u0027s mint limit

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, DOS attack, liquidation bot, vault, mint limit, swapExactAmountOut, liquidatable balance, tokenOut, front-running, back-running, available balance, liquidYield, yieldFeePercentage, smoothingFactor, type(uint96).max, attack vector, profit, manual review, recommendation

---

MiloTruck

medium

# \u0060TpdaLiquidationPair.swapExactAmountOut()\u0060 can be DOSed by a vault\u0027s mint limit

## Summary

By repeatedly DOSing \u0060TpdaLiquidationPair.swapExactAmountOut()\u0060 for a period of time, an attacker can swap the liquidatable balancce in a vault for profit.

## Vulnerability Detail

When liquidation bots call \u0060TpdaLiquidationPair.swapExactAmountOut()\u0060, they specify the amount of tokens they wish to receive in \u0060_amountOut\u0060. \u0060_amountOut\u0060 is then checked against the available balance to swap from the vault:

[TpdaLiquidationPair.sol#L141-L144](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-tpda-liquidator/src/TpdaLiquidationPair.sol#L141-L144)

\u0060\u0060\u0060solidity
        uint256 availableOut = _availableBalance();
        if (_amountOut > availableOut) {
            revert InsufficientBalance(_amountOut, availableOut);
        }
\u0060\u0060\u0060

The available balance to swap is determined by the liquidatable balance of the vault:
 
[TpdaLiquidationPair.sol#L184-L186](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-tpda-liquidator/src/TpdaLiquidationPair.sol#L184-L186)

\u0060\u0060\u0060solidity
    function _availableBalance() internal returns (uint256) {
        return ((1e18 - smoothingFactor) * source.liquidatableBalanceOf(address(_tokenOut))) / 1e18;
    }
\u0060\u0060\u0060

However, when the output token from the swap (ie. \u0060tokenOut\u0060) is vault shares, \u0060PrizeVault.liquidatableBalanceOf()\u0060 is restricted by the mint limit:

[PrizeVault.sol#L687-L709](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-vault/src/PrizeVault.sol#L687-L709)

\u0060\u0060\u0060solidity
    function liquidatableBalanceOf(address _tokenOut) external view returns (uint256) {
        uint256 _totalDebt = totalDebt();
        uint256 _maxAmountOut;
        if (_tokenOut == address(this)) {
            // Liquidation of vault shares is capped to the mint limit.
            _maxAmountOut = _mintLimit(_totalDebt);
        } else if (_tokenOut == address(_asset)) {
            // Liquidation of yield assets is capped at the max yield vault withdraw plus any latent balance.
            _maxAmountOut = _maxYieldVaultWithdraw() + _asset.balanceOf(address(this));
        } else {
            return 0;
        }

        // The liquid yield is limited by the max that can be minted or withdrawn, depending on
        // \u0060_tokenOut\u0060.
        uint256 _availableYield = _availableYieldBalance(totalPreciseAssets(), _totalDebt);
        uint256 _liquidYield = _availableYield >= _maxAmountOut ? _maxAmountOut : _availableYield;

        // The final balance is computed by taking the liquid yield and multiplying it by
        // (1 - yieldFeePercentage), rounding down, to ensure that enough yield is left for
        // the yield fee.
        return _liquidYield.mulDiv(FEE_PRECISION - yieldFeePercentage, FEE_PRECISION);
    }
\u0060\u0060\u0060

This means that if the amount of shares minted is close to \u0060type(uint96).max\u0060, the available balance in the vault (ie. \u0060_liquidYield\u0060) will be restricted by the remaining number of shares that can be minted.

However, an attacker can take advantage of this to force all calls to \u0060TpdaLiquidationPair.swapExactAmountOut()\u0060 to revert:

- Assume a vault has the following state:
  - The amount of \u0060_availableYield\u0060 in the vault is \u00601000e18\u0060.
  - The amount of shares currently minted is \u0060type(uint96).max - 2000e18\u0060, so \u0060_liquidYield\u0060 is not restricted by the mint limit.
  - \u0060yieldFeePercentage = 0\u0060 and \u0060smoothingFactor = 0\u0060.
- A liquidation bot calls \u0060swapExactAmountOut()\u0060 with \u0060_amountOut = 1000e18\u0060.
- An attacker front-runs the liquidation bot\u0027s transaction and deposits \u00601000e18 + 1\u0060 tokens, which mints the same amount of shares:
  - The amount of shares minted is now \u0060type(uint96).max - 1000e18 + 1\u0060, which means the mint limit is \u00601000e18 - 1\u0060.
  - As such, the available balance in the vault is reduced to \u00601000e18 - 1\u0060.
- The liquidation bot\u0027s transaction is now executed:
  - In \u0060swapExactAmountOut()\u0060, \u0060_amountOut > availableOut\u0060 so the call reverts.

Note that the \u0060type(uint96).max\u0060 mint limit is reachable for tokens with low value. For example, PEPE has 18 decimals and a current price of $0.00001468, so \u0060type(uint96).max\u0060 is equal to $1,163,070 worth of PEPE. For tokens with a higher value, the attacker can borrow funds in the front-run transaction, and back-run the victim\u0027s transaction to return the funds.

This is an issue as the price paid by liquidation bots for the liquidatable balance decreases linearly over time:

[TpdaLiquidationPair.sol#L191-L195](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-tpda-liquidator/src/TpdaLiquidationPair.sol#L191-L195)

\u0060\u0060\u0060solidity
        uint256 elapsedTime = block.timestamp - lastAuctionAt;
        if (elapsedTime == 0) {
            return type(uint192).max;
        }
        uint192 price = uint192((targetAuctionPeriod * lastAuctionPrice) / elapsedTime);
\u0060\u0060\u0060

As such, an attacker can repeatedly perform this attack (or deposit sufficient funds until the mint limit is 0) to prevent any liquidation bot from swapping the liquidatable balance. After the price has decreased sufficiently, the attacker can then swap the liquidatable balance for himself at a profit.

## Impact

By depositing funds into a vault to reach the mint limit, an attacker can DOS all calls to \u0060TpdaLiquidationPair.swapExactAmountOut()\u0060 and prevent liquidation bots from swapping the vault\u0027s liquidatable balance. This allows the attacker to purchase the liquidatable balance at a discount, which causes a loss of funds for users in the vault.

## Code Snippet

https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-tpda-liquidator/src/TpdaLiquidationPair.sol#L141-L144

https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-tpda-liquidator/src/TpdaLiquidationPair.sol#L184-L186

https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-vault/src/PrizeVault.sol#L687-L709

https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-tpda-liquidator/src/TpdaLiquidationPair.sol#L191-L195

## Tool used

Manual Review

## Recommendation

Consider implementing \u0060liquidatableBalanceOf()\u0060 and/or \u0060_availableBalance()\u0060 such that it is not restricted by the vault\u0027s mint limit. 

For example, consider adding a \u0060_tokenOut\u0060 parameter to \u0060TpdaLiquidationPair.swapExactAmountOut()\u0060 for callers to specify the output token. This would allow liquidation bots to swap for the vault\u0027s asset token, which is not restricted by the mint limit, when the mint limit is reached.

