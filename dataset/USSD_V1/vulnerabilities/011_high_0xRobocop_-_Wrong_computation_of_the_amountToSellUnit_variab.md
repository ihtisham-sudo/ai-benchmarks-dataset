# 0xRobocop - Wrong computation of the amountToSellUnit variable

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, collateral, amountToSellUnits, BuyUSSDSellCollateral, peg-down recovery, incorrect computation, USD ratio, collateral value, decimals, contract, manual review, impact, recommendation, 1e18 factor, code review, smart contract, blockchain, financial security, risk assessment

---

0xRobocop

high

# Wrong computation of the amountToSellUnit variable

## Summary

The variable \u0060amountToSellUnits\u0060 is computed wrongly in the code which will lead to an incorrect amount of collateral to be sold.

## Vulnerability Detail

The \u0060BuyUSSDSellCollateral()\u0060 function is used to sell collateral during a peg-down recovery event. The computation of the amount to sell is computed using the following formula:

\u0060\u0060\u0060solidity
// @audit-issue Wrong computation
uint256 amountToSellUnits = IERC20Upgradeable(collateral[i].token).balanceOf(USSD) * ((amountToBuyLeftUSD * 1e18 / collateralval) / 1e18) / 1e18;
\u0060\u0060\u0060

The idea is to sell an amount which is equivalent (in USD) to the ratio of \u0060amountToBuyLeftUSD / collateralval\u0060. Flattening the equation it ends up as:

\u0060\u0060\u0060solidity
uint256 amountToSellUnits = (collateralBalance * amountToBuyLeftUSD * 1e18) / (collateralval * 1e18 * 1e18);

// Reducing the equation
uint256 amountToSellUnits = (collateralBalance * amountToBuyLeftUSD) / (collateralval * 1e18);
\u0060\u0060\u0060

\u0060amountToBuyLeftUSD\u0060 and \u0060collateralval\u0060 already have 18 decimals so their decimals get cancelled together which will lead the last 1e18 factor as not necessary.

## Impact

The contract will sell an incorrect amount of collateral during a peg-down recovery event.

## Code Snippet

https://github.com/sherlock-audit/2023-05-USSD/blob/6d7a9fdfb1f1ed838632c25b6e1b01748d0bafda/ussd-contracts/contracts/USSDRebalancer.sol#L121

## Tool used

Manual Review

## Recommendation

Delete the last 1e18 factor
