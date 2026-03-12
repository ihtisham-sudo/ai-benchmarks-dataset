# Anyone could steal pool tokens’ earned interest

**Severity:** low
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** Uniswap, ERC20, tokens, interest, mint, flash, callback, liquidity, balance, attacker, pool, function, increase, require, check, payment, contract, user, payout, passive

---

# Anyone could steal pool tokens’ earned interest

**Severity:** Low  
**Difficulty:** Medium  
**Type:** Timing  
**Finding ID:** TOB-UNI-003  
**Target:** UniswapV3Pool.sol  


Unexpected ERC20 token interest behavior might allow token interest to count toward the amount of tokens required for the \u0060UniswapV3Pool.mint\u0060 and \u0060flash\u0060 functions, enabling the user to avoid paying in full.  

The mint function allows an account to increase its liquidity in a position. To verify that the pool has received at least the minimum amount of tokens necessary, the following code is used:  

\u0060\u0060\u0060solidity
uint256 balance0Before;   
uint256 balance1Before;   
if (amount0 > 0) balance0Before = balance0();                  
if (amount1 > 0) balance1Before = balance1();                  
IUniswapV3MintCallback(msg.sender).uniswapV3MintCallback(amount0, amount1, data);          
if (amount0 > 0) require(balance0Before.add(amount0) <= balance0(), \u0027M0\u0027);   
if (amount1 > 0) require(balance1Before.add(amount1) <= balance1(), \u0027M1\u0027);   
\u0060\u0060\u0060
*Figure 3.1: UniswapV3Pool.sol*

Assume that both \u0060amount0\u0060 and \u0060amount1\u0060 are positive. First, the current balances of the tokens are fetched. This step is followed by a call to the \u0060uniswapV3MintCallback\u0060 function of the caller, which should transfer the required amount of each token to the pool contract. Finally, the code verifies that each token’s balance has increased by at least the required amount.  

A token could allow token holders to earn interest simply because they are token holders. It is possible that to retrieve this interest, any token holder could call a function to calculate the interest earned and increase the token holder’s balance.  

An attacker could call the function to pay out interest to the pool contract from within the \u0060uniswapV3MintCallback\u0060 function. This would increase the pool’s token balance, decreasing the number of tokens that the user needs to transfer to the pool contract in order to pass the balance check (i.e., the check confirming that the balance has sufficiently increased). In effect, the user’s token payment obligation is reduced because the interest accounts for part of the required balance increase.  

To date, we have not identified a token contract that contains such a functionality; however, it is possible that one could exist or be created.  

Similarly, the \u0060flash\u0060 function allows any user to secure a flash loan from the pool.  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 24
Bob deploys a pool with token1 and token2. Token1 allows all of its holders to earn passive interest. Anyone can call \u0060get_interest(address)\u0060 to make a specific token holder’s interest be claimed and added to the token holder’s balance. Over time, the pool can claim 1,000 tokens. Eve calls \u0060mint\u0060 on the pool, such that the pool requires Eve to send 1,000 tokens. Eve calls \u0060get_interest(address)\u0060 instead of sending the tokens, adding liquidity to the pool without paying.  

Short term, add documentation explaining to users that the use of interest-earning tokens can reduce the standard payments for minting and flash loans.  

Long term, using the token integration checklist (Appendix E), generate a document detailing the shortcomings of tokens with certain features and the impacts of their use in the Uniswap V3 protocol. That way, users will not be alarmed if the use of a token with non-standard features leads to unexpected results.  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 25
