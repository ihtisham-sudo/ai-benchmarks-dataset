# Front-running pool’s initialization can lead to draining of liquidity provider’s initial deposits

**Severity:** medium
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** front-running, liquidity provider, initial deposits, UniswapV3Pool, initialize, unfair price, attack, access controls, profit, deployment, market price, transaction, mint, assets, swaps, constructor, documentation, risks, testing, TickMath

---

# Front-running pool’s initialization can lead to draining of liquidity provider’s initial deposits

**Severity:** Medium  
**Difficulty:** High  
**Type:** Data Validation  
**Finding ID:** TOB-UNI-007  
**Target:** UniswapV3Pool.sol  

A front-run on UniswapV3Pool.initialize allows an attacker to set an unfair price and to drain assets from the first deposits.  

UniswapV3Pool.initialize initiates the pool’s price:  

\u0060\u0060\u0060solidity
function initialize(uint160 sqrtPriceX96) external override {
    require(slot0.sqrtPriceX96 == 0, \u0027AI\u0027);

    int24 tick = TickMath.getTickAtSqrtRatio(sqrtPriceX96);

    (uint16 cardinality, uint16 cardinalityNext) = observations.initialize(_blockTimestamp());

    slot0 = Slot0({
        sqrtPriceX96: sqrtPriceX96,
        tick: tick,
        observationIndex: 0,
        observationCardinality: cardinality,
        observationCardinalityNext: cardinalityNext,
        feeProtocol: 0,
        unlocked: true
    });

    emit Initialize(sqrtPriceX96, tick);
}
\u0060\u0060\u0060

There are no access controls on the function, so anyone could call it on a deployed pool.  

Initializing a pool with an incorrect price allows an attacker to generate profits from the initial liquidity provider’s deposits.  

- Bob deploys a pool for assets A and B through a deployment script. The current market price is 1 A == 1 B.  
- Eve front-runs Bob’s transaction to the initialize function and sets a price such that 1 A ~= 10 B.  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 31

● Bob calls mint and deposits assets A and B worth $100,000, sending ~10 times more of asset B than asset A.  
● Eve swaps A tokens for B tokens at an unfair price, profiting off of Bob’s deployment.  

Two tests that demonstrate such an attack are included in Appendix G.   

Short term, consider  
● moving the price operations from initialize to the constructor,  
● adding access controls to initialize, or  
● ensuring that the documentation clearly warns users about incorrect initialization.    

Long term, avoid initialization outside of the constructor. If that is not possible, ensure that the underlying risks of initialization are documented and properly tested.
