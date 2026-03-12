# Swapping on zero liquidity allows for control of the pool’s price

**Severity:** medium
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** swapping, zero liquidity, price control, Uniswap, pool initialization, arbitrary price, liquidity providers, amountRemainingLessFee, amountIn, sqrtRatioNextX96, liquidityNet, tick transition, fee growth, price manipulation, token ratio, unfair price, risk awareness, pool state, unit test, liquidity delta

---

# Swapping on zero liquidity allows for control of the pool’s price

**Severity:** Medium  
**Difficulty:** Medium  
**Type:** Data Validation  
**Finding ID:** TOB-UNI-008  
**Target:** UniswapV3Pool.sol, libraries/SwapMath.sol  

Swapping on a tick with zero liquidity enables a user to adjust the price of 1 wei of tokens in any direction. As a result, an attacker could set an arbitrary price at the pool’s initialization or if the liquidity providers withdraw all of the liquidity for a short time.  

Swapping 1 wei in exactIn with a liquidity of zero and a fee enabled will cause amountRemainingLessFee and amountIn to be zero:  

\u0060\u0060\u0060solidity
uint256 amountRemainingLessFee = FullMath.mulDiv(
    uint256(amountRemaining), 
    1e6 - feePips, 
    1e6
);   
amountIn = zeroForOne 
    ? SqrtPriceMath.getAmount0Delta(sqrtRatioTargetX96, sqrtRatioCurrentX96, liquidity, true) 
    : SqrtPriceMath.getAmount1Delta(sqrtRatioCurrentX96, sqrtRatioTargetX96, liquidity, true);   
\u0060\u0060\u0060
*Figure 8.1: libraries/SwapMath.sol*

As amountRemainingLessFee == amountIn, the next square root ratio will be the square root target ratio:  

\u0060\u0060\u0060solidity
if (amountRemainingLessFee >= amountIn) 
    sqrtRatioNextX96 = sqrtRatioTargetX96;  
\u0060\u0060\u0060
*Figure 8.2: libraries/SwapMath.sol*  

The next square root ratio assignment results in updates to the pool’s price and tick:  

\u0060\u0060\u0060solidity
// shift tick if we reached the next price 
if (state.sqrtPriceX96 == step.sqrtPriceNextX96) {    
    // if the tick is initialized, run the tick transition   
    if (step.initialized) {    
        int128 liquidityNet = ticks.cross(
            step.tickNext,   
            (zeroForOne ? state.feeGrowthGlobalX128 : feeGrowthGlobal0X128),    
            (zeroForOne ? feeGrowthGlobal1X128 : state.feeGrowthGlobalX128)                
        );   
        // if we\u0027re moving leftward, we interpret liquidityNet as the opposite sign   
        // safe because liquidityNet cannot be type(int128).min   
        if (zeroForOne) 
            liquidityNet = -liquidityNet;                                             

        secondsOutside.cross(step.tickNext, tickSpacing, cache.blockTimestamp);  
    }  
}
\u0060\u0060\u0060
© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 33

\u0060\u0060\u0060plaintext
state.liquidity = LiquidityMath.addDelta(state.liquidity, liquidityNet);
\u0060\u0060\u0060

On a tick without liquidity, anyone could move the price and the tick in any direction. A user could abuse this option to move the initial pool’s price (e.g., between its initialization and minting) or to move the pool’s price if all the liquidity is temporarily withdrawn.

- Bob initializes the pool’s price to have a ratio such that 1 token0 == 10 token1.
- Eve changes the pool’s price such that 1 token0 == 1 token1.
- Bob adds liquidity to the pool.
- Eve executes a swap and profits off of the unfair price.

Appendix I contains a unit test for this issue.

Short term, there does not appear to be a straightforward way to prevent the issue. We recommend investigating the limits associated with pools without liquidity in some ticks and ensuring that users are aware of the risks.

Long term, ensure that pools can never end up in an unexpected state.

© 2021 Trail of Bits
