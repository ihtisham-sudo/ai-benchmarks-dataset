# dacian - Calls to Oracles don\u0027t check for stale prices

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, oracle calls, stale prices, price feeds, USSD contracts, USSDRebalancer, StableOracleDAI, StableOracleWBGL, StableOracleWBTC, StableOracleWETH, manual review, latestRoundData, updatedAt parameter, incorrect calculations, smart contracts, blockchain, Ethereum, Chainlink, price verification

---

dacian

medium

# Calls to Oracles don\u0027t check for stale prices

## Summary
Calls to Oracles don\u0027t check for stale prices.

## Vulnerability Detail
None of the oracle calls check for stale prices, for example [StableOracleDAI.getPriceUSD()](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L48):
\u0060\u0060\u0060solidity
(, int256 price, , , ) = priceFeedDAIETH.latestRoundData();

return
    (wethPriceUSD * 1e18) /
    ((DAIWethPrice + uint256(price) * 1e10) / 2);
\u0060\u0060\u0060

## Impact
Oracle price feeds can become stale due to a variety of [reasons](https://ethereum.stackexchange.com/questions/133242/how-future-resilient-is-a-chainlink-price-feed/133843#133843). Using a stale price will result in incorrect calculations in most of the key functionality of USSD & USSDRebalancer contracts.

## Code Snippet
[StableOracleDAI.getPriceUSD()](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L48)
[StableOracleWBGL.getPriceUSD()](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleWBGL.sol#L36-L38)
[StableOracleWBTC.getPriceUSD()](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleWBTC.sol#L23-L25)
[StableOracleWETH.getPriceUSD()](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleWETH.sol#L23-L25)

## Tool used
Manual Review

## Recommendation
Read the \u0060\u0060updatedAt\u0060\u0060 parameter from the calls to \u0060\u0060latestRoundData()\u0060\u0060 and verify that it isn\u0027t older than a set amount, eg:

\u0060\u0060\u0060solidity
if (updatedAt < block.timestamp - 60 * 60 /* 1 hour */) {
   revert("stale price feed");
}
\u0060\u0060\u0060
