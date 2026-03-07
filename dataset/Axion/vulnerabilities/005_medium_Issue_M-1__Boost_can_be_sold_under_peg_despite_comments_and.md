# Issue M-1: Boost can be sold under peg despite comments and code attempting to prevent it

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** Boost, peg, sell, admin, mintAndSellBoost, usdAmountOut, usdBalanceAfter, usdBalanceBefore, liquidity, AMO, protocol, funds, loss, invariant, preconditions, check, code, comments, readme, attack

---

# Issue M-1: Boost can be sold under peg despite comments and code attempting to prevent it

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-axion-judging/issues/36)  
Found by: spark1, vinica_boy  

## Summary  
Boost can be sold under peg despite comments and code attempting to prevent it. This is defined in the comments [here](https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/MasterAMO.sol#L148-L150) and in the readme. “There are, however, some hard-coded limitations — mainly to ensure that even admins can only buy back BOOST below peg and sell it above peg. These are doxtringed.”  

## Root Cause  
The only apparent check to prevent boost from being sold below peg is a simple if statement:  
\u0060\u0060\u0060solidity
if (minUsdAmountOut < toUsdAmount(boostAmount)) 
    minUsdAmountOut = toUsdAmount(boostAmount);
\u0060\u0060\u0060
However, this does not prevent boost from being sold below peg. Consider a pool with 90 boost and 110 usdc (ignore fees for now). 1 boost > 1 usdc. If \u0060mintAndSellBoost\u0060 is called with 20 boost, we will get an end result of 110 boost and 90 usdc. 20 boost were sold for 20 usdc. However, some of the boost were sold below the peg. Consider the first boost we sold. It was above the peg. At about 99.498 boost and 99.498 usdc the pool will be balanced. However, once we continue selling boost we will be selling below the peg.  

The admin can call \u0060mintAndSellBoost\u0060 directly. [Link to code](https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/MasterAMO.sol#L155-L168)  

The following affiliated check does nothing as without fee on transfer it will always pass.  
\u0060\u0060\u0060solidity
// Code snippet
\u0060\u0060\u0060  
[Link to code](https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/SolidlyV2AMO.sol#L186-L188)
// we check that selling BOOST yields proportionally more USD
if (usdAmountOut != usdBalanceAfter - usdBalanceBefore)
   revert UsdAmountOutMismatch(usdAmountOut, usdBalanceAfter - usdBalanceBefore);
This also applies to mintSellFarm as it does the same call with toUsdAmount(boostAmount) https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/SolidlyV2AMO.sol#L349.
This may not apply to V3AMO depending on if target SqrtPriceX96 is set correctly: https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/SolidlyV3AMO.sol#L141-L160
This contradicts the comments and readme stating that boost cannot be sold below peg by the AMO.

## Internal pre-conditions
no preconditions

## External pre-conditions
no preconditions

## Attack Path
Not an attack

## Impact
The protocol loses funds equivalent to the area under the curve of boost sold below peg. In large depeg this could be a huge amount of money. In the 90-110 example the total loss is 10.502 - 9.498 = 1.004. The protocol has lost 5% of the funds used in _mintAndSellBoost. High severity as it has large loss and violates important invariant specified explicitly in readme.

## PoC
Not required according to the terms

## Mitigation
Check that you can only sell to the sqrtK 1:1 balanced price.
## Discussion

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/AXION-MONEY/liquidity-amo/pull/4
