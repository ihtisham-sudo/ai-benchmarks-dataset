# cergyk - OCL_ZVE.sol::forwardYield relies on manipulable Uniswap V2 pool reserves leading to theft of funds

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cybersecurity, vulnerability, OCL_ZVE.sol, forwardYield, Uniswap V2, pool reserves, theft of funds, fetchBasis, pairAsset, USDC, LP tokens, negative yield, flashloan, manipulation, attack, basis, yield distribution, protocol loss, backrunning, manual review

---

cergyk

high

# OCL_ZVE.sol::forwardYield relies on manipulable Uniswap V2 pool reserves leading to theft of funds

## Summary

\u0060OCL_ZVE.sol::forwardYield\u0060 is used to forward yield in excess of the basis but it relies on Uniswap V2 pools that can be manipulable by an attacker to set \u0060basis\u0060 to a very small amount and steal funds.

## Vulnerability Detail

\u0060fetchBasis\u0060 is a function which returns the amount of pairAsset (USDC) which is claimable by burning the balance of LP tokens of OCL_ZVE

\u0060fetchBasis\u0060 is called first in \u0060forwardYield\u0060 in order to determine the yield to distribute:

[OCL_ZVE.sol#L301-L303](https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L301-L303)
\u0060\u0060\u0060solidity
>>    (uint256 amount, uint256 lp) = fetchBasis();
        if (amount > basis) { _forwardYield(amount, lp); }
        (basis,) = fetchBasis();
\u0060\u0060\u0060

If the returned \u0060amount\u0060 is \u0060<= basis\u0060 (negative yield) no yield is forwarded and basis is updated to the low \u0060amount\u0060 value 

By manipulating the Uniswap V2 pool with a flashloan, an attacker can get the \u0060uint256 amount\u0060 value to be returned by \u0060OCL_ZVE.sol::fetchBasis\u0060 to be very small and set \u0060basis\u0060 to this very small value:

[OCL_ZVE.sol#L301-L303](https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L301-L303)
\u0060\u0060\u0060solidity
        if (amount > basis) { _forwardYield(amount, lp); }
>>      (basis,) = fetchBasis();
\u0060\u0060\u0060

The next call (30 days later) to \u0060OCL_ZVE.sol::forwardYield\u0060 will forward much more yield (in excess of \u0060basis\u0060) than it should, leading to a loss of funds for the protocol.

### Scenario

1. Attacker buys a very large amount of USDC in the Uniswap V2 pool \u0060ZVE/pairAsset\u0060 (can use a flash-loan if needed)
2. Attacker calls \u0060OCL_ZVE.sol::forwardYield\u0060
  - \u0060OCL_ZVE.sol::fetchBasis\u0060 returns an incorrect and very small value for \u0060amount\u0060:
  -  No yield is forwarded since \u0060amount < basis\u0060
  - \u0060OCL_ZVE.sol::forwardYield\u0060 sets \u0060basis\u0060 to \u0060amount\u0060
3. Attacker backruns the calls to \u0060OCL_ZVE.sol::forwardYield\u0060 with the sell of his large buy in the Uniswap V2 pool
4. 30 days later, Attacker calls \u0060OCL_ZVE.sol::forwardYield\u0060 and steal funds in excess of \u0060basis\u0060

## Impact

Loss of funds for the protocol.

## Code Snippet

- https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L302-L303
- https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L311-L330

## Tool used

Manual Review

## Recommendation
Consider reverting during a call to \u0060forwardYield\u0060 if \u0060amount <= basis\u0060
