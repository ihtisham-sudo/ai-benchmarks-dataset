# clems4ever - Freezing of the protocol when totalSTokenUnderlying is zero but totalSupply is non-zero

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, protocol freezing, totalSTokenUnderlying, totalSupply, STokens, deposits, protection buys, lockCapital, exchange rate, convertToSToken, leverage ratio, leverageRatioFloor, impact, withdraw, manual review, recommendation, capital lock, zero funds, contract management

---

clems4ever

medium

# Freezing of the protocol when totalSTokenUnderlying is zero but totalSupply is non-zero

## Summary
In some cases the protocol can contain zero funds while having a non zero totalSupply of STokens. In that case the protocol will not be able to accept any new deposits and any new protection buys, thus coming to a halt, unless all STokens are burned by their respective holders.

## Vulnerability Detail
In the case \u0060lockCapital\u0060 has to lock all available capital:
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L415-L419

\u0060totalSTokenUnderlying\u0060 becomes zero, but \u0060totalSupply\u0060 is still non-zero since no SToken have been burned. 
Which means that new deposits will revert because \u0060_getExchangeRate()\u0060 is zero:
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L602-L605

And \u0060convertToSToken\u0060 tries to divide by \u0060_getExchangeRate()\u0060;
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L602-L605 

Also all new protection buying attempts will revert because \u0060_leverageRatio\u0060 is zero, and thus under \u0060leverageRatioFloor\u0060.

## Impact
The protocol comes to a halt, unless every SToken holder burn their shares by calling \u0060withdraw\u0060 after enough cycles have passed, returning to the case \u0060totalSupply == 0\u0060.

## Code Snippet

## Tool used

Manual Review

## Recommendation
Keep a minimum amount of totalSTokenUnderlying in the contract in any case (can be 1e6).
