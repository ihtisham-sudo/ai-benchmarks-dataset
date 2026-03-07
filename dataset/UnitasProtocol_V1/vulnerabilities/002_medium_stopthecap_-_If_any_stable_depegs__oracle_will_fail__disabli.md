# stopthecap - If any stable depegs, oracle will fail, disabling swaps

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnitasProtocol V1
**Keywords:** cyber security, vulnerability, oracle, depeg, swaps, price fetching, OracleX, price deviation, require statement, minPrice, maxPrice, PRICE_INVALID, transaction failure, core functionality, token, manual review, secondary oracle, try catch, last fetched price, protocol failure

---

stopthecap

high

# If any stable depegs, oracle will fail, disabling swaps

## Summary
If any stable depegs, oracle will fail, disabling swaps

## Vulnerability Detail

When swapping, the price of the asset/stable is fetched from OracleX. After fetching the price, the deviation is checked in the \u0060_checkPrice\u0060 function. 

https://github.com/sherlock-audit/2023-04-unitasprotocol/blob/d5328421bea80e3b0fd4595e4eb6b732a40e421e/Unitas-Protocol/src/Unitas.sol#L595-L600

If the price of an asset/stable depegs, the following require will fail:

\u0060\u0060\u0060@solidity
 _require(minPrice <= price && price <= maxPrice, Errors.PRICE_INVALID);
\u0060\u0060\u0060 
Due to the fail in the deviation, any swapping activity will be disabled by default and transactions will not go through

## Impact
Core functionality of the protocol will fail to work if any token they fetch depegs and its price goes outside the bounds.


## Code Snippet

https://github.com/sherlock-audit/2023-04-unitasprotocol/blob/d5328421bea80e3b0fd4595e4eb6b732a40e421e/Unitas-Protocol/src/Unitas.sol#L440

https://github.com/sherlock-audit/2023-04-unitasprotocol/blob/d5328421bea80e3b0fd4595e4eb6b732a40e421e/Unitas-Protocol/src/Unitas.sol#L595-L600

## Tool used

Manual Review

## Recommendation

Use a secondary oracle when the first one fails and wrap the code in a try catch and store the last fetched price in a variable

