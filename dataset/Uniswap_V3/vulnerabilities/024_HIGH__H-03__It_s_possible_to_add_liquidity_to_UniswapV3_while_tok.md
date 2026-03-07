# [H-03] It's possible to add liquidity to UniswapV3 while token is not migrated

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---


## Severity

**Impact:** High

**Likelihood:** Medium

## Description

Code won't allow to transfer of tokens to the UniswapV3 pool when the token hasn't migrated yet so no one could add liquidity to the pool and manipulate the pool. The issue is that it's possible to bypass these checks and add liquidity to the Uniswap pool. The attacker can use `buy(to)` function to buy tokens for the Uniswap V3 pool address and increase the pool's token balance. When adding liquidity to Uniswap V3, it calls `uniswapV3MintCallback()` and expects that function to transfer the tokens to the pool's address:

```solidity
        if (amount0 > 0) balance0Before = balance0();
        if (amount1 > 0) balance1Before = balance1();
        IUniswapV3MintCallback(msg.sender).uniswapV3MintCallback(amount0, amount1, data);
        if (amount0 > 0) require(balance0Before.add(amount0) <= balance0(), 'M0');
        if (amount1 > 0) require(balance1Before.add(amount1) <= balance1(), 'M1');
```

The attacker's contract can call `mint()` to add liquidity to the pool and during the `uniswapV3MintCallback()` callback it would call `buy(pool)` to increase the pool's balance and as a result, Uniswap V3 pool's liquidity would increase. By performing this attacker can DOS the migration process and also manipulate the token price during the migration.

## Recommendations

Won't allow buying tokens for the pool's address.


