# panprog - In some situations the liquidation can become unprofitable for liquidators, keeping unhealthy positions

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Aloe II
**Keywords:** liquidation, liquidator, unhealthy positions, swap price, LIQUIDATION_INCENTIVE, UNISWAP_AVG_WINDOW, average price, collateral, market price, ETH, USDT, debt, liquidation incentive, profitability, bad debt, protocol mechanism, asset composition, manual review, attack vectors, recommendations

---

panprog

medium

# In some situations the liquidation can become unprofitable for liquidators, keeping unhealthy positions
## Summary

When liquidators liquidate unhealthy accounts and the swap is required, they receive \u0060LIQUIDATION_INCENTIVE\u0060 to compensate for the potentially unprofitable swap price required (as the swap price is the pool average price over the \u0060UNISWAP_AVG_WINDOW\u0060, which lags the current price). However, this only happens when swap is required **at the average price**. The assets composition can be different depending on price if the user has uniswap position as a collateral. Such uniswap position can happen (intentionally or not) to be composed in such way, that it has 100% of one asset at the current average price, but 100% of the other asset at the current market price, thus liquidator\u0027s incentive will be 0.

In particular, it can happen in the following situation:
1. Current price is different from the average price by a reasonable amount (like 1%+)
2. Uniswap position is such, that it\u0027s fully in one asset at the average price and fully in the other asset at the current price

In this case, there is no swap required at the average price (thus liquidation incentive = 0), however at the current price a swap of all user assets is required from liquidator at the unfavorable average price (which is worse than current price). Since liquidator doesn\u0027t receive its bonus in such case, the liquidation will be unprofitable and liquidator won\u0027t liquidate user. 


## Vulnerability Detail

Example scenario of the situation when liquidation is not profitable for the liquidator:
1. Current ETH price = 1000 USDT. Average price over the last 30 minutes = 1010 USDT
2. Alice position is 1 ETH in the range [1000, 1006]. Alice debt is 9990 USDT. Alice account in not healthy.
3. Bob wants to liquidate Alice account. Since at the average price of 1010 USDT Alice position composition is 0 ETH + 1003 USDT, this fully covers Alice debt and liquidation incentive = 0. However, as the liquidation proceeds, at the current price of 1000 USDT Alice\u0027s position will be converted into 1 ETH + 0 USDT and Bob will have to exchange 1 ETH into 1010 USDT without any additional bonus.
3.1. If Bob decides to liquidate Alice account, Alice will have her 1 ETH converted into 1010 USDT, which she can immediately exchange into 1.01 ETH, creating a profit for Alice (and Bob will lose 10 USDT based on the current ETH price)
3.2. If Bob is being rational and doesn\u0027t luiquidate unprofitably, Alice unhealthy position will remain active without being liquidated.

## Impact

In some cases, liquidation will require swap of assets at unfavorable (lagging average) price without any bonus for the liquidator. Due to this, liquidation will not happen and user account will stay unhealthy, this can continue for extended time, breaking important protocol mechanism (timely liquidation) and possibly causing bad debt for unhealthy account.

## Code Snippet

\u0060BalanceSheet.computeLiquidationIncentive\u0060 sets incentive only when \u0060liabilities0 > assets0\u0060 or \u0060liabilities1 > assets1\u0060 at the average prices:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/libraries/BalanceSheet.sol#L125-L149

In \u0060liquidation\u0060 it is called with compositions of uniswap position assets at the average price (C):
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L213-L219

However, \u0060_getAssets\u0060 withdraws uniswap position at current price, which can be different:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L209

## Tool used

Manual Review

## Recommendation

Quite hard to come up with good recommendations here, because allowing liquidation incentive at current price opens up different attack vectors to abuse it. Possibly choose max amount required to swap at average price, average price-5% and average price+5% (or some other %) and pay out based on this max (still not on current price to be fair and not force liquidators manipulate pool for max profit) or something like that.

