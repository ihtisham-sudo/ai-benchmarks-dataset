# Unbalanced or single-sided liquidity leaves tokens locked in MarginalV1LBLiquidityReceiver 

**Severity:** HIGH
**Auditor:** Cantina

---

## MarginalV1LBLiquidityReceiver Vulnerability Report

## Context
`MarginalV1LBLiquidityReceiver.sol#L448`

## Description
After invoking `MarginalV1LBLiquidityReceiver.mintUniswapV3()`, some amount of tokens can remain locked in the contract, with no ability to withdraw or deposit them back to Marginal. The `mintUniswapV3()` function is utilized to deposit funds to Uniswap V3 after a pool has been finalized. This deposit is made as pool liquidity at the current price of the pool, which necessitates that the deposited amounts are balanced relative to the price.

There can be a delay between the finalization of the LB pool and the deposit to Uniswap V3, resulting in the current price in the Uniswap pool differing from the final price of the LB pool. Consequently, the amounts deposited to Uniswap will be balanced differently, leading to a leftover of one of the amounts (Uniswap takes the smaller liquidity when minting, hence not requesting more tokens). It is not possible to deposit this leftover to Marginal via `MarginalV1LBLiquidityReceiver.mintMarginalV1()`, as this function also requires balanced liquidity.

However, the receiver contract does not allow the refunding of tokens that remain after providing liquidity to Uniswap, resulting in the tokens being left in the contract.

In a rare alternative scenario, if an LB pool is finalized with the full initial liquidity (i.e., no swaps were made), the entire liquidity in the receiver contract becomes single-sided. Since Uniswap does not permit adding single-sided liquidity at the current price, the call to `MarginalV1LBLiquidityReceiver.mintUniswapV3()` will fail, locking the entire liquidity in the contract. Additionally, `mintMarginalV1()` will fail as it requires that liquidity was previously added to Uniswap.

## Impact
There is a risk of locking all or a portion of liquidity in the receiver contract.

## Likelihood
The vulnerability affects the normal flow of events in the protocol, but not all scenarios; for instance, when there is no price difference between the LB and Uniswap pools, there will be no leftover token amounts.

## Recommendation
Consider implementing a refunding functionality to allow users to withdraw tokens after providing liquidity to Uniswap V3. It may also be beneficial to enable withdrawals even before liquidity is provided to Uniswap and Marginal.

## Marginal
Fixed in commit `10e31504`. A `freeReserves()` function has been added that can be called after `params.lockDuration` seconds have elapsed since `receiver.notifyRewardAmounts` was called. This function zeroes the reserve state and transfers `(token0, token1)` balances to the `params.refundAddress`.

## Cantina Managed
Fixed.
