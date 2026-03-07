# Issue H-1: Boost buyback burns incorrect amount of liquidity

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** liquidity, burn, boost, USD, V3, AMO, contract, reserves, calculation, single sided liquidity, price, peg, overestimate, function, unfarmBuyBurn, tokens, profit, malicious actors, swap, mitigation

---

# Issue H-1: Boost buyback burns incorrect amount of liquidity

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-axion-judging/issues/114)  
Found by: 0x37, carrotsmuggler, pkqs90, s1ce, spark1, vinica_boy

## Summary

The function \u0060unfarmBuyBurn\u0060 in the V3 AMO contract is a public function open to everyone and calculates the amount of liquidity to burn from the pool. This function basically burns LP positions to take out liquidity and uses the USD to buy up boost tokens and burns them to raise the price of boost tokens.

The issue is in the \u0060unfarmBuyBurn\u0060 function when it tries to estimate how much liquidity needs to be taken out.

\u0060\u0060\u0060solidity
https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/SolidlyV3AMO.sol#L320-L326
\u0060\u0060\u0060

As seen above, first the token reserves of the pool are checked. Then, the liquidity to be burnt is calculated from the difference of the reserves.

\u0060\u0060\u0060solidity
liquidity = (totalLiquidity * (boostBalance - usdBalance)) / (boostBalance + usdBalance);
liquidity = (liquidity * LIQUIDITY_COEFF) / FACTOR;
\u0060\u0060\u0060

However, this calculation is not valid for V3/CL pools. This is because in V3 pools, single sided liquidity is allowed which adds to the totalLiquidity count, but increases the reserves of only 1 token. If a user adds liquidity at a tick lower than the current price, they will be adding only USD to the pool.

For example, let\u0027s say the price currently is below peg, at 0.9. Say there are 1000 boost and 900 USD tokens in the pool, similar to a V2 composition. Now, since it\u0027s a V3 pool, a user can come in and add 100 USD to the pool at a price of 0.5. Since this price is lower than the spot price, only USD will be needed to open this position. Now, the total reserves of both boost and USD are 1000 each, so the calculated liquidity amount to be removed will be 0.

Thus the liquidity calculated in the contract has absolutely no meaning since it uses the reserves to calculate it, which is not valid for V3 pools. In the best case scenario, this will cause the function to revert and not work. In the worst case scenario, the liquidity calculated will be overestimated and the price will be pushed up even above the peg price. This is possible if users add single sided boost to the pool, increasing the liquidity.
amount calculated without changing the price. In this case, the contract assets will be used to force the boost token above peg, and malicious actors can buy the boost token before and sell it after for a handy profit.

## Root Cause
The main cause is that liquidity is calculated from the reserves. This is not valid for V3, since it can have single-sided liquidity, and thus the reserves do not serve as an indicator of price or in this case the deviation from the peg.

## Internal Pre-conditions
None

## External Pre-conditions
Any user can add boost-only liquidity to make the contract overestimate the amount of liquidity it needs to burn.

## Attack Path
Users can add boost-only liquidity to make the contract overestimate the amount of liquidity it needs to burn. When extra liquidity is burnt and extra boost is bought back and burnt, the price will be pushed up even above the peg price. Users can buy before triggering this and sell after for profit.

## Impact
Price can be pushed above the peg price.

## PoC
None

## Mitigation
Use the quoteSwap function to calculate how much needs to be swapped until the target price is hit.
## Discussion

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/AXION-MONEY/liquidity-amo/pull/7
