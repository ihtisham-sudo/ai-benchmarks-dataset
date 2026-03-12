# Unbound loop enables denial of service

**Severity:** medium
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** Uniswap, V3, loop, denial of service, gas limit, swap function, tick, attacker, positions, Ethereum, mining, liquidity, tick spacing, gas cost, vulnerability, smart contract, security, data validation, risk, exploitation

---

# Unbound loop enables denial of service

**Severity:** Medium  
**Difficulty:** High  
**Type:** Data Validation  
**Finding ID:** TOB-UNI-006  
**Target:** UniswapV3Pool.sol  

The swap function relies on an unbounded loop. An attacker could disrupt swap operations by forcing the loop to go through too many operations, potentially trapping the swap due to a lack of gas.  

UniswapV3Pool.swap iterates over the tick:  

\u0060\u0060\u0060solidity
while (state.amountSpecifiedRemaining != 0 && state.sqrtPriceX96 != sqrtPriceLimitX96) {    
    StepComputations memory step;                    
    step.sqrtPriceStartX96 = state.sqrtPriceX96;                                                                                                                                                                        
    [...]   
    state.tick = zeroForOne ? step.tickNext - 1 : step.tickNext;                                                           
} else if (state.sqrtPriceX96 != step.sqrtPriceStartX96) {    
    // recompute unless we\u0027re on a lower tick boundary (i.e. already transitioned ticks), and haven\u0027t moved   
    state.tick = TickMath.getTickAtSqrtRatio(state.sqrtPriceX96);                                                                                                                                                                                                                                               
}   
\u0060\u0060\u0060  
Figure 6.1: UniswapV3Pool.sol  

On every loop iteration, there is a swap on the current tick’s price, increasing it to the next price limit. The next price limit depends on the next tick:  

\u0060\u0060\u0060solidity
(step.tickNext, step.initialized) = tickBitmap.nextInitializedTickWithinOneWord(                                                                                                                                                          
    state.tick,   
    tickSpacing,   
    zeroForOne   
);   

// ensure that we do not overshoot the min/max tick, as the tick bitmap is not aware of these bounds   
if (step.tickNext < TickMath.MIN_TICK) {    
    step.tickNext = TickMath.MIN_TICK;                                                                                                                                       
} else if (step.tickNext > TickMath.MAX_TICK) {    
    step.tickNext = TickMath.MAX_TICK;                                                                                                                                       
}   

// get the price for the next tick   
\u0060\u0060\u0060  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 29

\u0060\u0060\u0060plaintext
step.sqrtPriceNextX96 = TickMath.getSqrtRatioAtTick(step.tickNext);
\u0060\u0060\u0060

The next tick is the next initialized tick (or an uninitialized tick if no initialized tick is found).

A conservative gas cost analysis of the loop iteration returns the following estimates:  
1. ~50,000 gas per iteration if there is no previous fee on the tick (7 SLOAD, 1 SSTORE from non-zero to non-zero, 2 SSTORE from zero to non-zero).  
2. ~20,000 gas per iteration if there are previous fees on the tick (7 SLOAD, 3 SSTORE from non-zero to non-zero).  

The current block gas limit is 12,500,000. As a result, the swap operation will not be doable if it requires more than 2,500 (scenario 1) or 6,250 (scenario 2) iterations.  

An attacker could create thousands of positions with 1 wei to make the system very costly and potentially prevent swap operations.  

An attacker would have to pay gas to create the position. However, an Ethereum miner could create a position for free, and if the system were deployed on a layer 2 solution (e.g., optimism), the attacker’s gas payment would be significantly lower.  

Eve is a malicious miner involved with a Uniswap competitor. Eve creates thousands of positions in every Uniswap V3 pool to prevent users from using the system.  

Short term, to mitigate the issue, determine a reasonable minimum tick spacing requirement, or consider setting a minimum for liquidity per position.  

Long term, make sure that all parameters that the owner can enable (such as fee level and tick spacing) have bounds that lead to expected behavior, and clearly document those bounds, such as in a markdown file or in the whitepaper.  

© 2021 Trail of Bits
