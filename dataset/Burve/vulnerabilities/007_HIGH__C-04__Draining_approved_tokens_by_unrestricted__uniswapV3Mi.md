# [C-04] Draining approved tokens by unrestricted `uniswapV3MintCallback()`

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---

## Severity

**Impact:** High

**Likelihood:** High

## Description

`Burve::uniswapV3MintCallback` is an external function with no access control. This function takes three parameters: `amount0Owed`, `amount1Owed`, and `data`. It then decodes `data` to get an address and transfers tokens from that address to the liquidity pool (lp). An attacker could see which addresses have approved to `Burve.sol` and transfer tokens from those addresses to the pool.

```solidity
  function uniswapV3MintCallback(uint256 amount0Owed, uint256 amount1Owed, bytes calldata data) external {
        address source = abi.decode(data, (address));
        TransferHelper.safeTransferFrom(token0, source, address(pool), amount0Owed);
        TransferHelper.safeTransferFrom(token1, source, address(pool), amount1Owed);
    }
```

1. Provide `data` which decodes to a user address with a hanging approval to `Burve` and amounts equal to the approved amounts
2. As the function has no access control, the funds will be transferred into the pool
3. This causes a direct loss of funds for the users

## Recommendations

Restrict this function so that only the pool can call it.
