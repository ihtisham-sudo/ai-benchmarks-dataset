# neumo - If collateral factor is high enough, flutter ends up being out of bounds

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, USSDRebalancer, SellUSSDBuyCollateral, collateral factor, flutterRatios, index out of bounds, revert, rebalance, function, collateral ratios, manual review, impact, recommendation, code snippet, loop, flutter, array, error handling, smart contract

---

neumo

high

# If collateral factor is high enough, flutter ends up being out of bounds

## Summary
In \u0060USSDRebalancer\u0060 contract, function \u0060SellUSSDBuyCollateral\u0060 will revert everytime a rebalance calls it, provided the collateral factor is greater than all the elements of the \u0060flutterRatios\u0060 array.

## Vulnerability Detail
Function \u0060SellUSSDBuyCollateral\u0060 calculates \u0060flutter\u0060 as the lowest index of the \u0060flutterRatios\u0060 array for which the collateral factor is smaller than the flutter ratio.
\u0060\u0060\u0060solidity
uint256 cf = IUSSD(USSD).collateralFactor();
uint256 flutter = 0;
for (flutter = 0; flutter < flutterRatios.length; flutter++) {
	if (cf < flutterRatios[flutter]) {
	  break;
	}
}
\u0060\u0060\u0060
The problem arises when, if collateral factor is greater than all flutter values, after the loop \u0060flutter = flutterRatios.length\u0060.

This \u0060flutter\u0060 value is used afterwards here:
\u0060\u0060\u0060solidity
...
if (collateralval * 1e18 / ownval < collateral[i].ratios[flutter]) {
  portions++;
}
...
\u0060\u0060\u0060
 And here:
 \u0060\u0060\u0060solidity
...
if (collateralval * 1e18 / ownval < collateral[i].ratios[flutter]) {
  if (collateral[i].token != uniPool.token0() || collateral[i].token != uniPool.token1()) {
	// don\u0027t touch DAI if it\u0027s needed to be bought (it\u0027s already bought)
	IUSSD(USSD).UniV3SwapInput(collateral[i].pathbuy, daibought/portions);
  }
}
...
\u0060\u0060\u0060

As we can see in the tests of the project, the flutterRatios array and the collateral ratios array are set to be of the same length, so if flutter = flutterRatios.length, any call to that index in the \u0060ratios\u0060 array will revert with an index out of bounds.

## Impact
High, when the collateral factor reaches certain level, a rebalance that calls \u0060SellUSSDBuyCollateral\u0060 will always revert.

## Code Snippet
https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L178-L184

## Tool used
Manual review.


## Recommendation
When checking \u0060collateral[i].ratios[flutter]\u0060 always check first that flutter is \u0060< flutterRatios.length\u0060.



