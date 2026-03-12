# Whitepaper contains incorrect equation

**Severity:** info
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** whitepaper, equation, liquidity pool, price, assets, formula, Uniswap, users, misunderstanding, system, correct formula, N, 1 - 1 /√, financial loss, documentation, clarity, correction, communication, integrated products, assessment

---

# Whitepaper contains incorrect equation

**Severity:** Informational  
**Difficulty:** High  
**Type:** Undefined Behavior  
**Finding ID:** TOB-UNI-004  
**Target:** Whitepaper  

The whitepaper contains the following statement:  

\u0060\u0060\u0060
For example, at any given time, 25% of the assets in a liquidity pool will only be touched 
if the relative price moves by a factor of 16. (In general, 1 /√ N of the pool’s liquidity 
is only touched if the price moves by a factor of N in one direction.)
\u0060\u0060\u0060
Figure 4.1: Whitepaper, page 1.  

This formula does not make sense, even for a trivial case. When the price is constant (i.e., N = 1), the function indicates that 1/1 (i.e., 100%) of the pool’s liquidity is touched.  

The correct formula is 1 - 1 /√ N.  

Alice is a Uniswap user or a developer of integrated products. She reads the whitepaper and misunderstands the system, causing her users to lose money.  

Short term, correct the following sentence:  

\u0060\u0060\u0060
For example, at any given time, 75% of the assets in a liquidity pool will only be touched 
if the relative price moves by a factor of 16. (In general, 1 - 1 /√ N of the pool’s 
liquidity is only touched if the price moves by a factor of N in one direction.)
\u0060\u0060\u0060
Figure 4.2: Corrected version.  

Long term, finalize the whitepaper, ensuring that it is clear.  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 26
