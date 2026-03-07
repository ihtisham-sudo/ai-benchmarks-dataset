# carrotsmuggler - Price calculation susceptible to flashloan exploits

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, flash loan, price manipulation, Uniswap, TWAP, slot0, DAI-USSD pool, instantaneous price, asset ratio, rebalance, arbitrage, collateral, just-in-time liquidity, contract exploit, price calculation, pool manipulation, attack vector, manual review, recommendation

---

carrotsmuggler

high

# Price calculation susceptible to flashloan exploits

## Summary

Contract uses uniswap \u0060slot0\u0060 price instead of TWAP price. \u0060slot0\u0060 price can be manipulated with flash loans.

## Vulnerability Detail

The contract uses the uniswap DAI-USSD pool to get the price of USSD. It however uses the instantaneous price from \u0060slot0\u0060 instead of the TWAP price. The \u0060slot0\u0060 price is calculated from the ratios of the assets. This ratio can however be manipulated by buying/selling assets in the pool.

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L71-L80

Thus any user can take a flashloan, use those funds to manipulate the price of USSD, and then trigger a rebalance. The attacks can be made profitable by providing just-in-time liquidity to the various pools that \u0060reabalance\u0060 interacts with, draining the contract of collateral through arbitrage.

## Impact

Price can be manipulated and \u0060rebalance\u0060 can be called any time. Susceptible to flash loan exploits.

## Code Snippet

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L71-L80

## Tool used

Manual Review

## Recommendation

Use TWAP price instead of \u0060slot0\u0060 price. [Here](https://github.com/charmfinance/alpha-vaults-contracts/blob/07db2b213315eea8182427be4ea51219003b8c1a/contracts/AlphaStrategy.sol#L136-L144) is an example implementation of TWAP.

