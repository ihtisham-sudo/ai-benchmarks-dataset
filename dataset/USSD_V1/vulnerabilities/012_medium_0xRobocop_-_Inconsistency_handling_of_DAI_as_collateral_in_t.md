# 0xRobocop - Inconsistency handling of DAI as collateral in the BuyUSSDSellCollateral function

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, DAI, collateral, BuyUSSDSellCollateral, peg-down recovery, rebalancing, Uniswap, sell path, collateral value, amount to buy, impact, manual review, code snippet, if statement, else branch, recommendation, inconsistency handling, smart contract, USSD

---

0xRobocop

high

# Inconsistency handling of DAI as collateral in the BuyUSSDSellCollateral function

## Summary

DAI is the base asset of the \u0060USSD.sol\u0060 contract, when a rebalacing needs to occur during a peg-down recovery, collateral is sold for DAI, which then is used to buy USSD in the DAI / USSD uniswap pool. Hence, when DAI is the collateral, this is not sold because there no existe a path to sell DAI for DAI.

## Vulnerability Detail

The above behavior is handled when collateral is about to be sold for DAI, see the comment \u0060no need to swap DAI\u0060 ([link to the code](https://github.com/sherlock-audit/2023-05-USSD/blob/6d7a9fdfb1f1ed838632c25b6e1b01748d0bafda/ussd-contracts/contracts/USSDRebalancer.sol#L117-L139)):

\u0060\u0060\u0060solidity
if (collateralval > amountToBuyLeftUSD) {
   // sell a portion of collateral and exit
   if (collateral[i].pathsell.length > 0) {
       uint256 amountBefore = IERC20Upgradeable(baseAsset).balanceOf(USSD);
       uint256 amountToSellUnits = IERC20Upgradeable(collateral[i].token).balanceOf(USSD) * ((amountToBuyLeftUSD * 1e18 / collateralval) / 1e18) / 1e18;
       IUSSD(USSD).UniV3SwapInput(collateral[i].pathsell, amountToSellUnits);
       amountToBuyLeftUSD -= (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
       DAItosell += (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
   } 
   else {
       // no need to swap DAI
       DAItosell = IERC20Upgradeable(collateral[i].token).balanceOf(USSD) * amountToBuyLeftUSD / collateralval;
   }
}

else {
   // @audit-issue Not handling the case where this is DAI as is done above.
   // sell all or skip (if collateral is too little, 5% treshold)
   if (collateralval >= amountToBuyLeftUSD / 20) {
      uint256 amountBefore = IERC20Upgradeable(baseAsset).balanceOf(USSD);
      // sell all collateral and move to next one
      IUSSD(USSD).UniV3SwapInput(collateral[i].pathsell, IERC20Upgradeable(collateral[i].token).balanceOf(USSD));
      amountToBuyLeftUSD -= (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
      DAItosell += (IERC20Upgradeable(baseAsset).balanceOf(USSD) - amountBefore);
   }
}
\u0060\u0060\u0060
The problem is in the \u0060else branch\u0060 of the first if statement \u0060collateralval > amountToBuyLeftUSD\u0060, which lacks the check \u0060if (collateral[i].pathsell.length > 0)\u0060

## Impact

A re-balancing on a peg-down recovery will fail if the \u0060collateralval\u0060 of DAI is less than \u0060amountToBuyLeftUSD\u0060 but greater than \u0060amountToBuyLeftUSD / 20\u0060 since the DAI collateral does not have a sell path.

## Code Snippet

https://github.com/sherlock-audit/2023-05-USSD/blob/6d7a9fdfb1f1ed838632c25b6e1b01748d0bafda/ussd-contracts/contracts/USSDRebalancer.sol#L130-L139

## Tool used

Manual Review

## Recommendation

Handle the case as is the done on the if branch of \u0060collateralval > amountToBuyLeftUSD\u0060:

\u0060\u0060\u0060solidity
if (collateral[i].pathsell.length > 0) {
  // Sell collateral for DAI
}
else {
 // No need to swap DAI
}
\u0060\u0060\u0060


