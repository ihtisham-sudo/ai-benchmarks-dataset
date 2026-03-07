# J4de - \u0060USSDRebalancer.sol#SellUSSDBuyCollateral\u0060 the check of whether collateral is DAI is wrong

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** USSDRebalancer, SellUSSDBuyCollateral, collateral, DAI, vulnerability, revert, UniV3SwapInput, token, pathbuy, impact, cybersecurity, smart contract, manual review, function, logic error, conditional check, stability, Ethereum, decentralized finance, security audit

---

J4de

high

# \u0060USSDRebalancer.sol#SellUSSDBuyCollateral\u0060 the check of whether collateral is DAI is wrong

## Summary

The \u0060SellUSSDBuyCollateral\u0060 function use \u0060||\u0060 instand of \u0060&&\u0060 to check whether the collateral is DAI. It is wrong and may cause \u0060SellUSSDBuyCollateral\u0060 function revert.

## Vulnerability Detail

\u0060\u0060\u0060solidity
196       for (uint256 i = 0; i < collateral.length; i++) {
197         uint256 collateralval = IERC20Upgradeable(collateral[i].token).balanceOf(USSD) * 1e18 / (10**IERC20MetadataUpgradeable(collateral[i].token).decimals()) * collateral[i].oracle.getPriceUSD() / 1e18;
198         if (collateralval * 1e18 / ownval < collateral[i].ratios[flutter]) {
199 >>        if (collateral[i].token != uniPool.token0() || collateral[i].token != uniPool.token1()) {
200             // don\u0027t touch DAI if it\u0027s needed to be bought (it\u0027s already bought)
201             IUSSD(USSD).UniV3SwapInput(collateral[i].pathbuy, daibought/portions);
202           }
203         }
204       }
\u0060\u0060\u0060

Line 199 should use \u0060&&\u0060 instand of \u0060||\u0060 to ensure that the token is not DAI. If the token is DAI, the \u0060UniV3SwapInput\u0060 function will revert because that DAI\u0027s \u0060pathbuy\u0060 is empty.

## Impact

The \u0060SellUSSDBuyCollateral\u0060 will revert and USSD will become unstable.

## Code Snippet

https://github.com/USSDofficial/ussd-contracts/blob/f44c726371f3152634bcf0a3e630802e39dec49c/contracts/USSDRebalancer.sol#L199

## Tool used

Manual Review

## Recommendation

\u0060\u0060\u0060diff
      for (uint256 i = 0; i < collateral.length; i++) {
        uint256 collateralval = IERC20Upgradeable(collateral[i].token).balanceOf(USSD) * 1e18 / (10**IERC20MetadataUpgradeable(collateral[i].token).decimals()) * collateral[i].oracle.getPriceUSD() / 1e18;
        if (collateralval * 1e18 / ownval < collateral[i].ratios[flutter]) {
-         if (collateral[i].token != uniPool.token0() || collateral[i].token != uniPool.token1()) {
+         if (collateral[i].token != uniPool.token0() && collateral[i].token != uniPool.token1()) {
            // don\u0027t touch DAI if it\u0027s needed to be bought (it\u0027s already bought)
            IUSSD(USSD).UniV3SwapInput(collateral[i].pathbuy, daibought/portions);
          }
        }
      }
\u0060\u0060\u0060
