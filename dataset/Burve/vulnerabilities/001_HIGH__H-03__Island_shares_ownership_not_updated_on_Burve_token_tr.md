# [H-03] Island shares ownership not updated on Burve token transfer

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---

## Severity

**Impact:** High

**Likelihood:** Medium

## Description

When a Kodiak island contract is set in the `Burve`, on `mint()` a portion of the liquidity will be used to mint island shares, which will then be deposited into the station proxy at the name of the recipient, and the `islandSharesPerOwner` mapping will be updated for the recipient. The recipient will also receive `Burve` tokens (shares) for the liquidity provided to the Uniswap pools.

However, if the recipient transfers the `Burve` tokens to another address, the island shares are still assigned to him, both in `StationProxy` and in the `Burve`'s `islandSharesPerOwner` mapping. This means that after the transfer, the new owner of the `Burve` tokens will not be able to harvest the rewards in `StationProxy`, nor will he be able to burn the island shares in exchange for the underlying liquidity.

## Recommendations

Overwrite the `_update()` function so that on `Burve` transfers:

- The proportional amount of LP tokens are withdrawn from `StationProxy`.
- The LP tokens are deposited again in the name of the new owner.
- `islandSharesPerOwner` is updated by both the old and new owner.
