# [H-03] Incorrect recipient results in the inability to properly redeem a position

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---

## Severity

**Impact:** Medium

**Likelihood:** High

## Description

Upon minting, we have the following code:

```solidity
if (range.lower == 0 && range.upper == 0) {
            uint256 mintShares = islandLiqToShares(liq);
            island.mint(mintShares, recipient);
        } else {
            // mint the V3 ranges
            pool.mint(address(this), range.lower, range.upper, liq, abi.encode(msg.sender));
        }
```

When minting for the island, we set the recipient as the `recipient` input and when minting Uniswap V3 liquidity, we set the recipient as `address(this)`. The latter is correct while the former is not. This is because when burning, the shares will be burned from the caller of the `burn()` function on the target, which will be the `Burve` contract. As the `Burve` contract does not have the minted shares when minting for the island, we will simply revert.

The user still has 2 options, thus the medium impact:

- batch a transaction by transferring the shares to the `Burve` contract and then burning the liquidity, this will result in the correct result
- simply burn his shares directly on the island, note that this will result in the user still having the minted `Burve` shares

## Recommendations

```diff
-  island.mint(mintShares, recipient);
+  island.mint(mintShares, address(this));
```
