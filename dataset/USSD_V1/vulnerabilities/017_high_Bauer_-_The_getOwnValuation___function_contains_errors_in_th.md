# Bauer - The getOwnValuation() function contains errors in the price calculation

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, getOwnValuation, price calculation, USSD, token0, token1, UniSwap V3, sqrtPriceX96, uniPool, valuation, asset valuation, trading decisions, liquidity provision, financial calculations, error, impact, manual review, recommendation, code snippet

---

Bauer

high

# The getOwnValuation() function contains errors in the price calculation

## Summary
The getOwnValuation() function in the provided code has incorrect price calculation logic when token0() or token1() is equal to USSD. The error leads to inaccurate price calculations.

## Vulnerability Detail
The \u0060USSDRebalancer.getOwnValuation()\u0060 function calculates the price based on the sqrtPriceX96 value obtained from the uniPool.slot0() function. The calculation depends on whether token0() is equal to USSD or not.
If token0() is equal to USSD, the price calculation is performed as follows:
\u0060\u0060\u0060solidity
  price = uint(sqrtPriceX96)*(uint(sqrtPriceX96))/(1e6) >> (96 * 2);
\u0060\u0060\u0060
However,there is an error in the price calculation logic. The calculation should be:
\u0060\u0060\u0060solidity
price = uint(sqrtPriceX96) * uint(sqrtPriceX96) * 1e6 >> (96 * 2);

\u0060\u0060\u0060
If token0() is not equal to USSD, the price calculation is slightly different:
\u0060\u0060\u0060solidity
 price = uint(sqrtPriceX96)*(uint(sqrtPriceX96))*(1e18 /* 1e12 + 1e6 decimal representation */) >> (96 * 2);
        // flip the fraction
        price = (1e24 / price) / 1e12;
\u0060\u0060\u0060
The calculation should be:
\u0060\u0060\u0060solidity
 price = uint(sqrtPriceX96)*(uint(sqrtPriceX96))*(1e6 /* 1e12 + 1e6 decimal representation */) >> (96 * 2);
        // flip the fraction
        price = (1e24 / price) / 1e12;
\u0060\u0060\u0060
Reference link:
https://blog.uniswap.org/uniswap-v3-math-primer

## Impact
The incorrect price calculation in the getOwnValuation() function can lead to significant impact on the valuation of assets in the UniSwap V3 pool. The inaccurate prices can result in incorrect asset valuations, which may affect trading decisions, liquidity provision, and overall financial calculations based on the UniSwap V3 pool.

## Code Snippet
https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L74
https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L76
## Tool used

Manual Review

## Recommendation
When token0() is USSD, the correct calculation should be uint(sqrtPriceX96) * uint(sqrtPriceX96) * 1e6 >> (96 * 2).
When token1() is USSD, the correct calculation should be 
\u0060\u0060\u0060solidity 
price = uint(sqrtPriceX96)*(uint(sqrtPriceX96))*(1e6 /* 1e12 + 1e6 decimal representation */) >> (96 * 2);
        // flip the fraction
        price = (1e24 / price) / 1e12;
\u0060\u0060\u0060

