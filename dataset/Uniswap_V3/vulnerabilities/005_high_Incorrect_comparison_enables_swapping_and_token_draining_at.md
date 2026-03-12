# Incorrect comparison enables swapping and token draining at no cost

**Severity:** high
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** Uniswap, swap function, token draining, data validation, incorrect comparison, amountIn, amountOut, callback, require statement, transfer, pool contract, tokens, unit test, error handling, Echidna, Manticore, smart contract, security, vulnerability, Ethereum

---

# Incorrect comparison enables swapping and token draining at no cost

**Severity:** High  
**Difficulty:** Low  
**Type:** Data Validation  
**Finding ID:** TOB-UNI-005  
**Target:** UniswapV3Pool.sol  

An incorrect comparison in the swap function allows the swap to succeed even if no tokens are paid. This issue could be used to drain any pool of all of its tokens at no cost.  

\u0060\u0060\u0060solidity
// transfer the output   
if (amountOut != 0) TransferHelper.safeTransfer(tokenOut, recipient, uint256(-amountOut));   

// callback for the input   
uint256 balanceBefore = balanceOfToken(tokenIn);                                                                
zeroForOne ? IUniswapV3SwapCallback(msg.sender).uniswapV3SwapCallback(amountIn, amountOut, data)               
: IUniswapV3SwapCallback(msg.sender).uniswapV3SwapCallback(amountOut, amountIn, data);                  
require(balanceBefore.add(uint256(amountIn)) >= balanceOfToken(tokenIn), \u0027IIA\u0027);   
\u0060\u0060\u0060
*Figure 5.1: UniswapV3Pool.sol#L649-L657*  

The swap function calculates how many tokens the initiator (msg.sender) needs to pay (amountIn) to receive the requested amount of tokens (amountOut). It then calls the uniswapV3SwapCallback function on the initiator’s account, passing in the amount of tokens to be paid. The callback function should then transfer at least the requested amount of tokens to the pool contract. Afterward, a require inside the swap function verifies that the correct amount of tokens (amountIn) has been transferred to the pool.  

However, the check inside the require is incorrect. Instead of checking that at least the requested amount of tokens has been transferred to the pool, it checks that no more than the requested amount has been transferred. In other words, if the callback does not transfer any tokens to the pool, the check, and the swap, will succeed without the initiator having paid any tokens.  

Bob deploys a pool for USDT/DAI. The pool holds 1,000,000 DAI. Eve calls a swap for 1,000,000 DAI but transfers 0 USDT, stealing all of the DAI from the pool.  

Short term, replace the \u0060>=\u0060 with \u0060<=\u0060 inside the require in the swap function. Add at least one unit test checking that the IIA error is thrown when too few tokens are transferred from the initiator’s contract to the pool.  

Long term, consider adding at least one unit test for each error that can be thrown by the contracts. With a unit test, an error would be thrown when it should be, at least in a simple manner.  

© 2021 Trail of Bits  
Uniswap V3 Core Assessment | 27

case. Also consider adding more properties and using Echidna or Manticore to verify that initiators are correctly transferring tokens to the pool. 

© 2021 Trail of Bits
