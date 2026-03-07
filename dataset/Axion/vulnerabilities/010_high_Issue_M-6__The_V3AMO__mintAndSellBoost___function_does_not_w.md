# Issue M-6: The V3AMO._mintAndSellBoost() function does not work with Velodrome, Aerodrome, Fenix, Thena and Ramses

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** V3AMO, mintAndSellBoost, Velodrome, Aerodrome, Fenix, Thena, Ramses, function parameters, BOOST tokens, USD, swap function, Solidly V3 DEXes, protocol team, DoS, mint, sell, USDC, price peg, attack path, mitigation

---

# Issue M-6: The V3AMO._mintAndSellBoost() function does not work with Velodrome, Aerodrome, Fenix, Thena and Ramses

Source: [GitHub Issue #268](https://github.com/sherlock-audit/2024-10-axion-judging/issues/268)  
Found by: ABA, Kirkeelee, KupiaSec, carrotsmuggler, pkqs90

## Summary
The protocol mints BOOST tokens and sells them for USD using the _mintAndSellBoost() function for Solidly V3 DEXes. Since Velodrome, Aerodrome, Fenix, Thena and Ramses are parts of the Solidly V3 DEXes, they should be compatible. However, the _mintAndSellBoost() function does not work with the DEXes due to incorrect function parameters.

## Root Cause
In the _mintAndSellBoost() function, it mints BOOST tokens and swaps them for USD tokens. 

\u0060\u0060\u0060solidity
https://github.com/sherlock-audit/2024-10-axion/blob/c65e662999d0c79439703fc6713814b4ad023e01/liquidity-amo/contracts/SolidlyV3AMO.sol#L144-L151
File: liquidity-amo\contracts\SolidlyV3AMO.sol
144: @>      (int256 amount0, int256 amount1) = ISolidlyV3Pool(pool).swap(
145:             address(this),
146:             boost < usd,
147:             int256(boostAmount), // Amount of BOOST tokens being swapped
148:             targetSqrtPriceX96, // The target square root price
149:             minUsdAmountOut, // Minimum acceptable amount of USD to receive from the swap
150:             deadline
151:         );
\u0060\u0060\u0060

However, the swap() function of Velodrome, Aerodrome, Fenix, Thena and Ramses has different parameters. The swap() functions of the DEXes are as follows:

- Velodrome: [CLPool.sol](https://optimistic.etherscan.io/address/0xCc0bDDB707055e04e497aB22a59c2aF4391cd12F#code::text=File%208%20of%2037%20%3A%20CLPool.solL613-L619)
- Aerodrome: [CLPool.sol](https://basescan.org/address/0x5e7BB104d84c7CB9B682AaC2F3d509f5406809A#code::text=File%208%20of%2037%20%3A%20CLPool.solL679-L685)
Fenix: [https://blastscan.io/address/0x5aCCAc55f692Ae2F065CEdDF5924C8f6B53cDa](https://blastscan.io/address/0x5aCCAc55f692Ae2F065CEdDF5924C8f6B53cDa)  
\u0060\u0060\u0060solidity
File 2 of 44 : AlgebraPool.sol L212-L218
\u0060\u0060\u0060

Thena: [https://bscscan.com/address/0xc89F69Baa3ff17a842AB2DE89E5Fc8a8e2cc735](https://bscscan.com/address/0xc89F69Baa3ff17a842AB2DE89E5Fc8a8e2cc735)  
\u0060\u0060\u0060solidity
File 2 of 31 : AlgebraPool.sol L591-L597
\u0060\u0060\u0060

Ramses: [https://arbiscan.io/address/0xf896d16fa56a625802b6013f9f9202790ec69908](https://arbiscan.io/address/0xf896d16fa56a625802b6013f9f9202790ec69908)  
\u0060\u0060\u0060solidity
File 44 of 45 : RamsesV2Pool.sol L944-L950
function swap(
 address recipient,
 bool zeroToOne,
 int256 amountRequired,
 uint160 limitSqrtPrice,
 bytes calldata data
) external override returns (int256 amount0, int256 amount1) {
\u0060\u0060\u0060

As a result, the \u0060mintAndSellBoost()\u0060 function does not work with Velodrome, Aerodrome, Fenix, Thena, and Ramses due to incorrect function parameters.

## Internal pre-conditions
For convenience, let\u0027s assume that the USD token is USDC from this point forward.
- Protocol team is going to mint additional BOOST and sell them for USDC to bring the price back down to peg.

## External pre-conditions
- The BOOST-USDC price diverges from peg and BOOST is trading above $1 in Velodrome.

## Attack Path
- Alice (protocol team) calls the \u0060mintAndSellBoost()\u0060 function.  
It reverts.

## Impact
The \u0060mintAndSellBoost()\u0060, \u0060mintSellFarm()\u0060 functions will be permanently DoSed for Velodrome, Aerodrome, Fenix, Thena, and Ramses. Protocol team can\u0027t mint additional BOOST and sell them for USDC to bring the price back down to peg. 

## PoC
\u0060\u0060\u0060plaintext
34
\u0060\u0060\u0060
## Mitigation

Use the correct function parameters for Velodrome, Aerodrome, Fenix, Thena and Ramses.

## Discussion

sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:  
https://github.com/AXION-MONEY/liquidity-amo/pull/13
PAGE END
