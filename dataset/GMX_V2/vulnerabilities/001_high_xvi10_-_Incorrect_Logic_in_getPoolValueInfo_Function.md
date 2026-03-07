# xvi10 - Incorrect Logic in getPoolValueInfo Function

**Severity:** high
**Auditor:** Sherlock
**Protocol:** GMX V2
**Keywords:** indexTokenPrice, pickPrice, maximize, impactPoolUsd, getPoolValueInfo, withdrawal, overestimation, pool value, logic error, function, MarketUtils, draining, pool, evaluation, parameter, return value, code review, VSCode, manual review, recommendation

---

indexTokenPrice.pickPrice (! maximize) , just like the next itemfor calculating Pnl. 6. longPnl and shortPnl, both use themode ! maximize since both of themwill be subtracted fromthe total value. In summary, just like calculating Pnl, we need to use indexTokenPrice.pickPrice (! maximize) instead of indexTokenPrice.pickPrice (maximize) to calculate impactPoolUsd.Only in thisway, the logic of the input parameter maximize can be implemented properly. Impact CodeSnippet getPoolValueInfo () does not use ! maximizewhen evaluating impactPoolUsd, leading towrong logicofmaximizingorminimizing the poolvalue. As a result,when isMaximize is true, the returned value is actually notmaximized! In the case of withdrawl, a slight overestimation of the output tokensmight occur and lead to possible draining of the pool in the long run! Toolused VSCode ManualReview Recommendation In function MarketUtils.getPoolValueInfo () we need to use indexTokenPrice.pickPrice (! maximize) instead of indexTokenPrice.pickPrice (maximize) to calculate impactPoolUsd. Discussion xvi10 https: //github.com/gmx-io/gmx-synthetics/commit/13913a28e4b07f5a2cc fixed in 0065fdebc34c437864c71 3    
