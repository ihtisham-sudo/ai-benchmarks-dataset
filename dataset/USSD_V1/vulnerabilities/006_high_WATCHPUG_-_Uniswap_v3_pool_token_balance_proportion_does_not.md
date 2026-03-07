# WATCHPUG - Uniswap v3 pool token balance proportion does not necessarily correspond to the price, and it is easy to manipulate.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** Uniswap v3, pool token balance, price manipulation, getSupplyProportion, USSDamount, DAIamount, underflow, accumulative fees, liquidity manipulation, collateral asset, rebalance, limit-order, JIT liquidity, high price range, price peg, manual review, vulnerability, protocol impact, complex formula, liquidity range

---

WATCHPUG

high

# Uniswap v3 pool token balance proportion does not necessarily correspond to the price, and it is easy to manipulate.

## Summary

\u0060getSupplyProportion()\u0060 retrieves Uniswap v3 pool balances, but the proportion of pool tokens doesn\u0027t always correspond to the price. If \u0060ownval\u0060 is less than \u00601e6 - threshold\u0060, \u0060USSDamount\u0060 may be lower than \u0060DAIamount\u0060, causing L97 \u0060USSDamount - DAIamount\u0060 to revert due to underflow. Proportion can be easily manipulated, which can be exploited by attackers.

## Vulnerability Detail

\u0060getSupplyProportion()\u0060 retrieves the balances of the Uniswap v3 pool. However, due to the different designs of Uniswap v3 and Uniswap v2, the proportion of pool tokens does not necessarily correspond to the price.

As a result, if \u0060ownval\u0060 is less than \u00601e6 - threshold\u0060 (e.g. 0.95), \u0060USSDamount\u0060 may be lower than \u0060DAIamount\u0060, causing L97 \u0060USSDamount - DAIamount\u0060 to revert due to underflow.

Additionally, the pool contract holds accumulative fees on its balances, which are not impacted by price changes.

---

Furthermore, the proportion can be easily manipulated with minimal cost, which can be exploited by attackers.

If the price of USSD goes over-peg (which can happen naturally), an attacker can take advantage by following these steps:

1. Add single leg liquidity of DAI to the DAI/USSD pool at an exorbitantly high price range, such as 1 DAI == 1000-2000 USSD.
2. Manipulate the price of the collateral asset, such as WETH, to a higher price.
3. Place a limit-order like JIT liquidity at a higher price in the WETH/DAI pool.
4. Trigger \u0060rebalance() -> SellUSSDBuyCollateral()\u0060, but it will mint and sell much more than expected (the amount needed to bring the peg back) as the \u0060DAIamount\u0060 is significantly higher than \u0060USSDamount\u0060 at a manipulated high price. This will buy the limit order from step 3.
5. Reverse the price of WETH/DAI and remove the liquidity placed at step 1.

## Impact

1. \u0060rebalance()\u0060 may malfunction if the proportion is not as expected.
2. Manipulating the proportion can result in the protocol selling a significantly larger amount of collateral assets than intended. If the collateral asset is also manipulated, it would be sold at a manipulated price, causing even larger damage to the protocol.

## Code Snippet

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L13-L16

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L83-L107

## Tool used

Manual Review

## Recommendation

Instead of using the pool balances to calculate the delta amount required to restore the peg, a more complex formula that considers the liquidity range should be used.
