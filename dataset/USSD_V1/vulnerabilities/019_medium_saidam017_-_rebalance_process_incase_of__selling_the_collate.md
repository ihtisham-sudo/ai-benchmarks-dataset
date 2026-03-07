# saidam017 - rebalance process incase of  selling the collateral, could revert because of underflow calculation

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, rebalance process, collateral, underflow, BuyUSSDSellCollateral, baseAsset, amountToSellUnits, Uniswap, amountToBuyLeftUSD, IERC20Upgradeable, balanceOf, oracle price, swap, collateralval, manual review, impact, recommendation, calculation error, smart contract

---

saidam017

high

# rebalance process incase of  selling the collateral, could revert because of underflow calculation

## Summary

rebalance process, will try to sell the collateral in case of peg-down. However, the process can revert because the calculation can underflow.

## Vulnerability Detail

Inside \u0060rebalance()\u0060 call, if \u0060BuyUSSDSellCollateral()\u0060 is triggered, it will try to sell the current collateral to \u0060baseAsset\u0060. The asset that will be sold (\u0060amountToSellUnits\u0060) first calculated. Then swap it to \u0060baseAsset\u0060 via uniswap. However, when subtracting \u0060amountToBuyLeftUSD\u0060, it with result of \u0060(IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore)\u0060. There is no guarantee \u0060amountToBuyLeftUSD\u0060 always bigger than \u0060(IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore)\u0060.

This causing the call could revert in case \u0060(IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore)\u0060 > \u0060amountToBuyLeftUSD\u0060.

There are two branch where \u0060amountToBuyLeftUSD -= (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore)\u0060 is performed : 

1. Incase \u0060collateralval > amountToBuyLeftUSD\u0060

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L116-L125

\u0060collateralval\u0060 is calculated using oracle price, thus the result of swap not guaranteed to reflect the proportion of \u0060amountToBuyLefUSD\u0060 against \u0060collateralval\u0060 ratio, and could result in returning \u0060baseAsset\u0060 larger than expected. And potentially  \u0060(IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore)\u0060 > \u0060amountToBuyLeftUSD\u0060

\u0060\u0060\u0060solidity
        uint256 collateralval = IERC20Upgradeable(collateral[i].token).balanceOf(USSD) * 1e18 / (10**IERC20MetadataUpgradeable(collateral[i].token).decimals()) * collateral[i].oracle.getPriceUSD() / 1e18;
        if (collateralval > amountToBuyLeftUSD) {
          // sell a portion of collateral and exit
          if (collateral[i].pathsell.length > 0) {
            uint256 amountBefore = IERC20Upgradeable(baseAsset).balanceOf(USSD);
            uint256 amountToSellUnits = IERC20Upgradeable(collateral[i].token).balanceOf(USSD) * ((amountToBuyLeftUSD * 1e18 / collateralval) / 1e18) / 1e18;
            IUSSD(USSD).UniV3SwapInput(collateral[i].pathsell, amountToSellUnits);
            amountToBuyLeftUSD -= (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
            DAItosell += (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
          } else {
\u0060\u0060\u0060

2. Incase \u0060collateralval < amountToBuyLeftUSD\u0060

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L132-L138

This also can\u0027t guarantee \u0060(IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore)\u0060 < \u0060amountToBuyLeftUSD\u0060.

\u0060\u0060\u0060solidity
          if (collateralval >= amountToBuyLeftUSD / 20) {
            uint256 amountBefore = IERC20Upgradeable(baseAsset).balanceOf(USSD);
            // sell all collateral and move to next one
            IUSSD(USSD).UniV3SwapInput(collateral[i].pathsell, IERC20Upgradeable(collateral[i].token).balanceOf(USSD));
            amountToBuyLeftUSD -= (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
            DAItosell += (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
          }
\u0060\u0060\u0060

## Impact

Rebalance process can revert caused by underflow calculation.

## Code Snippet

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L116-L125
https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L132-L138

## Tool used

Manual Review

## Recommendation

Check if \u0060(IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore)\u0060 > \u0060amountToBuyLeftUSD\u0060, in that case, just set \u0060amountToBuyLeftUSD\u0060 to 0.

\u0060\u0060\u0060solidity
          ...
            uint baseAssetChange = IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
            if (baseAssetChange > amountToBuyLeftUSD) {
                amountToBuyLeftUSD = 0;
            } else {
                amountToBuyLeftUSD -= baseAssetChange;
           }
            DAItosell += baseAssetChange;
          ...
\u0060\u0060\u0060


