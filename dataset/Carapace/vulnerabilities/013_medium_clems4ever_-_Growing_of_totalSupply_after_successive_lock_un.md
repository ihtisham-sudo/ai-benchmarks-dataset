# clems4ever - Growing of totalSupply after successive lock/unlockCapital can freeze protection pools by uint overflow

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cyber security, vulnerability, totalSupply, lock/unlockCapital, overflow, protection pools, uint256, convertToSToken, exchange rate, funds locking, new depositors, shares, oversized share, capital, exponential growth, type(uint).max, protocol halt, manual review, rebasing, token design

---

clems4ever

medium

# Growing of totalSupply after successive lock/unlockCapital can freeze protection pools by uint overflow

## Summary
In a protection pool, after enough cycles of locking capital/depositing, totalSupply can grow to overflow uint256. 

## Vulnerability Detail
In \u0060convertToSToken\u0060:
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L589-L606

\u0060_getExchangeRate()\u0060 can become arbitrarily small after a funds locking, since locked funds are substracted from \u0060totalSTokenUnderlying\u0060;
This means that new depositors can get a lot more shares than depositors from before funds locking. 
This behavior is correct, because otherwise previous depositors would have an oversized share of the new capital. However this has the negative effect of growing \u0060totalSupply\u0060 exponentially, eventually reaching \u0060type(uint).max\u0060 and overflowing (reverting every new deposit).

## Impact
Protocol can come to a halt if totalSupply reaches \u0060type(uint).max\u0060.

## Code Snippet

## Tool used
Manual Review

## Recommendation
Design the token in a way that it can be rebased regularly.
