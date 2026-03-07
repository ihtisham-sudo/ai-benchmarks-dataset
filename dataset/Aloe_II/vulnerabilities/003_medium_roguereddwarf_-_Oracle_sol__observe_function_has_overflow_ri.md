# roguereddwarf - Oracle.sol: observe function has overflow risk and should cast to uint256 like Uniswap V3 does

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Aloe II
**Keywords:** Oracle.observe, overflow risk, uint256 cast, Uniswap V3, secondsPerLiquidityCumulativeX128, intermediate overflow, liquidity, unchecked block, liquidity accumulators, corrupted return value, Volatility library, IV calculation, LTV ratios, bad debt, capital efficiency, seed calculation, off-chain computation, targetDelta, time difference, vulnerability detail

---

roguereddwarf

medium

# Oracle.sol: observe function has overflow risk and should cast to uint256 like Uniswap V3 does
## Summary
The \u0060Oracle.observe\u0060 function basically uses the same math from the Uniswap V3 code to search for observations.  

In comparison to Uniswap V3, the \u0060Oracle.observe\u0060 function takes a \u0060seed\u0060 such that the runtime of the function can be decreased by calculating the \u0060seed\u0060 off-chain to act as a hint for finding the observation.  

In the process of copying the Uniswap V3 code, a \u0060uint256\u0060 cast has been forgotten which introduces a risk of intermediate overflow in the \u0060Oracle.observe\u0060 function.  

Thereby the \u0060secondsPerLiquidityCumulativeX128\u0060 return value can be wrong which can corrupt the implied volatility (ÌV) calculation.  

## Vulnerability Detail
Looking at the \u0060Oracle.observe\u0060 function, the \u0060secondsPerLiquidityCumulativeX128\u0060 return value is calculated as follows:

https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/libraries/Oracle.sol#L196
\u0060\u0060\u0060solidity
liqCumL + uint160(((liqCumR - liqCumL) * delta) / denom)
\u0060\u0060\u0060

The calculation is done in an \u0060unchecked\u0060 block. \u0060liqCumR\u0060 and \u0060liqCumL\u0060 have type \u0060uint160\u0060.  
\u0060delta\u0060 and \u0060denom\u0060 have type \u0060uint56\u0060.  

Let\u0027s compare this to the Uniswap V3 code.

https://github.com/Uniswap/v3-core/blob/d8b1c635c275d2a9450bd6a78f3fa2484fef73eb/contracts/libraries/Oracle.sol#L279-L284
\u0060\u0060\u0060solidity
beforeOrAt.secondsPerLiquidityCumulativeX128 +
    uint160(
        (uint256(
            atOrAfter.secondsPerLiquidityCumulativeX128 - beforeOrAt.secondsPerLiquidityCumulativeX128
        ) * targetDelta) / observationTimeDelta
    )
\u0060\u0060\u0060

The result of \u0060atOrAfter.secondsPerLiquidityCumulativeX128 - beforeOrAt.secondsPerLiquidityCumulativeX128\u0060 is cast to \u0060uint256\u0060.  

That\u0027s because multiplying the result by \u0060targetDelta\u0060 can overflow the \u0060uint160\u0060 type.  

The maximum value of \u0060uint160\u0060 is roughly \u00601.5e48\u0060.  

\u0060delta\u0060 is simply the time difference between \u0060timeL\u0060 and \u0060target\u0060 in seconds.  

The \u0060secondsPerLiquidityCumulative\u0060 values are accumulators that are calculated as follows:
https://github.com/Uniswap/v3-core/blob/d8b1c635c275d2a9450bd6a78f3fa2484fef73eb/contracts/libraries/Oracle.sol#L41-L42
\u0060\u0060\u0060solidity
secondsPerLiquidityCumulativeX128: last.secondsPerLiquidityCumulativeX128 +
    ((uint160(delta) << 128) / (liquidity > 0 ? liquidity : 1)),
\u0060\u0060\u0060

If \u0060liquidity\u0060 is very low and the time difference between observations is very big (hours to days), this can lead to the intermediate overflow in the \u0060Oracle\u0060 library, such that the \u0060secondsPerLiquidityCumulative\u0060 is much smaller than it should be.  

The lowest value for the above division is \u00601\u0060. In that case the accumulator grows by \u00602^128\u0060 (\u0060~3.4e38\u0060) every second.

If observations are apart 24 hours (\u006086400 seconds\u0060), this can lead to an overflow:
Assume for simplicity \u0060target - timeL = timeR - timeL\u0060
\u0060\u0060\u0060text
(liqCumR - liqCumL) * delta = 3.4e38 * 86400 * 86400 > 1.5e48\u0060
\u0060\u0060\u0060

## Impact
The corrupted return value affects the [\u0060Volatility\u0060 library](https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/libraries/Volatility.sol#L121). Specifically, the IV calculation.    

This can lead to wrong IV updates and LTV ratios that do not reflect the true IV, making the application more prone to bad debt or reducing capital efficiency.  

## Code Snippet
https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/libraries/Oracle.sol#L196

https://github.com/Uniswap/v3-core/blob/d8b1c635c275d2a9450bd6a78f3fa2484fef73eb/contracts/libraries/Oracle.sol#L279-L284

## Tool used
Manual Review

## Recommendation
Perform the same cast to \u0060uint256\u0060 that Uniswap V3 performs:  
\u0060\u0060\u0060solidity
liqCumL + uint160((uint256(liqCumR - liqCumL) * delta) / denom)
\u0060\u0060\u0060
