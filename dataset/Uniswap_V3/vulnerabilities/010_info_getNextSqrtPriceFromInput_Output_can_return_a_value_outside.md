# getNextSqrtPriceFromInput|Output can return a value outside of MIN_SQRT_RATIO, MAX_SQRT_RATIO

**Severity:** info
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** getNextSqrtPriceFromInput, getNextSqrtPriceFromOutput, square ratio price, MIN_SQRT_RATIO, MAX_SQRT_RATIO, data validation, liquidity, token0, token1, swapping, require, bounds, Echidna, Manticore, arithmetic functions, refactoring, exploitation, checks, solidity, Uniswap V3

---

# getNextSqrtPriceFromInput|Output can return a value outside of MIN_SQRT_RATIO, MAX_SQRT_RATIO

Severity: Informational  
Difficulty: High  
Type: Data Validation  
Finding ID: TOB-UNI-010  
Target: libraries/SqrtPriceMath.sol, libraries/TickMath.sol  

getNextSqrtPriceFromInput|Output takes a square price and returns the next square ratio price. A square ratio price should be between [MIN_SQRT_RATIO, MAX_SQRT_RATIO]; however, getNextSqrtPriceFromInput|Output does not confirm that is the case.  

The square ratio price’s limit is defined with MIN_SQRT_RATIO/MAX_SQRT_RATIO:  

\u0060\u0060\u0060solidity
/// @dev The minimum value that can be returned from #getSqrtRatioAtTick. Equivalent to 
getSqrtRatioAtTick(MIN_TICK)   
uint160 internal constant MIN_SQRT_RATIO = 4295128739;   

/// @dev The maximum value that can be returned from #getSqrtRatioAtTick. Equivalent to 
getSqrtRatioAtTick(MAX_TICK)   
uint160 internal constant MAX_SQRT_RATIO = 1461446703485210103287273052203988822378723970342;   
\u0060\u0060\u0060
Figure 10.1: libraries/TickMath.sol#L13-L16  

getNextSqrtPriceFromInput/getNextSqrtPriceFromOutput returns a next square price ratio based on the current one:  

\u0060\u0060\u0060solidity
/// @notice Gets the next sqrt price given an input amount of token0 or token1  
/// @dev Throws if price or liquidity are 0, or if the next price is out of bounds  
/// @param sqrtPX96 The starting price, i.e., before accounting for the input amount  
/// @param liquidity The amount of usable liquidity  
/// @param amountIn How much of token0, or token1, is being swapped in  
/// @param zeroForOne Whether the amount in is token0 or token1  
/// @return sqrtQX96 The price after adding the input amount to token0 or token1  
function getNextSqrtPriceFromInput(  
    uint160 sqrtPX96,  
    uint128 liquidity,  
    uint256 amountIn,  
    bool zeroForOne  
) internal pure returns (uint160 sqrtQX96) {  
    require(sqrtPX96 > 0);  
    require(liquidity > 0);  

    // round to make sure that we don\u0027t pass the target price  
    return  
        zeroForOne  
\u0060\u0060\u0060
© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 37
\u0060\u0060\u0060solidity
getNextSqrtPriceFromAmount0RoundingUp(sqrtPX96, liquidity, amountIn, true)
    : getNextSqrtPriceFromAmount1RoundingDown(sqrtPX96, liquidity, amountIn, true);
}

/// @notice Gets the next sqrt price given an output amount of token0 or token1
/// @dev Throws if price or liquidity are 0 or the next price is out of bounds
/// @param sqrtPX96 The starting price before accounting for the output amount
/// @param liquidity The amount of usable liquidity
/// @param amountOut How much of token0, or token1, is being swapped out
/// @param zeroForOne Whether the amount out is token0 or token1
/// @return sqrtQX96 The price after removing the output amount of token0 or token1
function getNextSqrtPriceFromOutput(
    uint160 sqrtPX96,
    uint128 liquidity,
    uint256 amountOut,
    bool zeroForOne
) internal pure returns (uint160 sqrtQX96) {
    require (sqrtPX96 > 0);
    require (liquidity > 0);

    // round to make sure that we pass the target price
    return
        zeroForOne
            ? getNextSqrtPriceFromAmount1RoundingDown(sqrtPX96, liquidity, amountOut, false)
            : getNextSqrtPriceFromAmount0RoundingUp(sqrtPX96, liquidity, amountOut, false);
}
\u0060\u0060\u0060

Figure 10.1: libraries/SqrtPriceMath.sol#L102-L146

Both functions allow the next square ratio to be outside of its expected bounds.

Currently, the issue is not exploitable, as the bound is checked in getTickAtSqrtRatio:

\u0060\u0060\u0060solidity
function getTickAtSqrtRatio(uint160 sqrtPriceX96) internal pure returns (int24 tick) {
    // second inequality must be < because the price can never reach the price at the max tick
    require (sqrtPriceX96 >= MIN_SQRT_RATIO && sqrtPriceX96 < MAX_SQRT_RATIO, \u0027R\u0027);
}
\u0060\u0060\u0060

Figure 10.2: libraries/TickMath.sol#L60-L62

Exploit Scenario  
The code is refactored, and the check in getTickAtSqrtRatio is removed.  
getNextSqrtPriceFromInput is called with the following and returns 1:  
● sqrtPriceX96 = 192527866349542497182378200028923523296830566619  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 38
● liquidity   =   3121856577256316178563069792952001938  
● Amount   =  
    87976224064120683466372192477762052080551804637393713865979671817311  
    849605529  
● Round   up   =   true.  

As   a   result,   the   next   square   ratio   price   is   outside   of   the   expected   bounds.  


Short   term,   check   in    getNextSqrtPriceFromInput/ getNextSqrtPriceFromOutput    that   the   
returned   value   is   within  M   IN_SQRT_RATIO,   M   AX_SQRT_RATIO.  

Long   term,   document   every   bound   for   all   arithmetic   functions   and   test   every   bound   with  
Echidna   and   Manticore.  

©   2021   Trail   of   Bits   Uniswap   V3   Core   Assessment   |   39
PAGE END
