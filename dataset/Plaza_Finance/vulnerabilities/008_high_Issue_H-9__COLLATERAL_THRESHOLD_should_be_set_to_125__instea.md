# Issue H-9: COLLATERAL_THRESHOLD should be set to 125% instead of 120%.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** collateral, threshold, Bond Token, redeem Rate, continuity, price curve, Leverage Token, TVL, asset Supply, tvl, multiplier, BOND_TARGET_PRICE, PRECISION, tokenType, significant price increase, substantial losses, current state, price increase, loss, calculation

---

# Issue H-9: COLLATERAL_THRESHOLD should be set to 125% instead of 120%.

Source: [GitHub Issue #895](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/895)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.  
Found by: KupiaSec, makeWeb3safe, werulez99, zraxx  

The price of Bond Token depends on whether the collateral Level is above or below 120%.  
- If collateral Level <= 120%:  
  80% of TVL is allocated for Bond Token, so the price of Bond Token is less than 120 * 80% = 96.  
- If collateral Level > 120%:  
  The price of Bond Token is set to 100.  

As you can see, when the collateral Level moves from below to above 120%, the price of Bond Token changes from <= 96 to 100, indicating that the price curve is not continuous. To ensure continuity, 125% should be used instead of 120%.  

The getRedeemAmount() function calculates the redeem Rate based on whether the collateral Level is above or below 120%.  
- If collateral Level <= 120%:  
  redeemRate = (tvl * multiplier) / assetSupply  
  Here, multiplier is 80%, and asset Supply is the total supply of Bond Token. Since the collateral Level is less than 120%, the redeem Rate will be less than 120 * 80% = 96.  
- If collateral Level > 120%:  
  redeemRate = 100  

As observed, when the collateral Level moves from below to above 120%, the redeem Rate is not continuous, moving from 96 to 100 suddenly.
This means that when the collateral level is around 120%, a minor increase in TVL can lead to a significant price increase of Bond Token, resulting in substantial losses for Leverage Token holders, even as the TVL increases.

\u0060\u0060\u0060solidity
function getRedeemAmount(
    ...
    uint256 redeemRate;
    if (collateralLevel <= COLLATERAL_THRESHOLD) {
        redeemRate = ((tvl * multiplier) / assetSupply);
    } else if (tokenType == TokenType.LEVERAGE) {
        redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) * PRECISION;
    } else {
        redeemRate = BOND_TARGET_PRICE * PRECISION;
    }
    // Calculate and return the final redeem amount
    return ((depositAmount * redeemRate).fromBaseUnit(oracleDecimals) / ethPrice) / PRECISION;
}
\u0060\u0060\u0060




Let\u0027s consider the following scenario:

1. Current State of the Pool:
    - TVL: 1190
    - bondSupply: 10
    - collateralLevel: 119%
    - TVL for Bond Token: 1190 * 0.8 = 952
    - TVL for Leverage Token: 1190 * 0.2 = 238
2. Price of Underlying Rises:
    - TVL: 1210 (due to price increase)
    - bondSupply: 10
    - collateralLevel: 121%
    - TVL for Bond Token: 100 * 10 = 1000
• TVLforLeverageToken: 1210-100=210  
As you can see, Leverage Token holders incur a loss of 238 - 210 = 28, even though the underlying price has increased.  

Even though the price of the underlying increases, Leverage Token holders incur a loss.  


For COLLATERAL_THRESHOLD, use 125% instead of 120%.
