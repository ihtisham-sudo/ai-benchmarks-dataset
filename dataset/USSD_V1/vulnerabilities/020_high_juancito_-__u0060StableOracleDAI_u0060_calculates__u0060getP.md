# juancito - \u0060StableOracleDAI\u0060 calculates \u0060getPriceUSD\u0060 with inverted base/rate tokens for Chainlink price

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** StableOracleDAI, getPriceUSD, Chainlink price feed, Uniswap pool price, WETH/DAI, DAI/ETH, price difference, USSD tokens, minting, vulnerability, price calculation, average price, priceFeedDAIETH, Etherscan, Chainlink Feeds, DAIWethPrice, token addresses, incorrect result, USSDRebalancer, rebalance

---

juancito

high

# \u0060StableOracleDAI\u0060 calculates \u0060getPriceUSD\u0060 with inverted base/rate tokens for Chainlink price

## Summary

\u0060StableOracleDAI::getPriceUSD()\u0060 calculates the average price between the Uniswap pool price for a pair and the Chainlink feed as part of its result.

The problem is that it uses \u0060WETH/DAI\u0060 as the base/rate tokens for the pool, and \u0060DAI/ETH\u0060 for the Chainlink feed, which is the opposite.

This will incur in a huge price difference that will impact on the amount of USSD tokens being minted, while requesting the price from this oracle.

## Vulnerability Detail

In \u0060StableOracleDAI::getPrice()\u0060 the \u0060price\u0060 from the Chainlink feed \u0060priceFeedDAIETH\u0060 returns the price as DAI/ETH.

This can be checked on [Etherscan](https://etherscan.io/address/0x773616E4d11A78F511299002da57A0a94577F1f4#readContract#F10) and the [Chainlink Feeds Page](https://docs.chain.link/data-feeds/price-feeds/addresses/).

Also note the comment on the code is misleading, as it is refering to another pair:

> chainlink price data is 8 decimals for WETH/USD

\u0060\u0060\u0060solidity
/// constructor
24:    priceFeedDAIETH = AggregatorV3Interface(
25:        0x773616E4d11A78F511299002da57A0a94577F1f4
26:    );

/// getPrice()
46:    // chainlink price data is 8 decimals for WETH/USD, so multiply by 10 decimals to get 18 decimal fractional
47:    //(uint80 roundID, int256 price, uint256 startedAt, uint256 timeStamp, uint80 answeredInRound) = priceFeedDAIETH.latestRoundData();
48:    (, int256 price, , , ) = priceFeedDAIETH.latestRoundData();
\u0060\u0060\u0060

[Link to code](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L46-L48)

On the other hand, the price coming from the Uniswap pool \u0060DAIWethPrice\u0060 returns the price as \u0060WETH/DAI\u0060.

Note that the relation WETH/DAI is given by the orders of the token addresses passed as arguments, being the first the base token, and the second the quote token.

Also note that the variable name \u0060DAIWethPrice\u0060 is misleading as well as the base/rate are the opposite (although this doesn\u0027t affect the code).

\u0060\u0060\u0060solidity
    uint256 DAIWethPrice = DAIEthOracle.quoteSpecificPoolsWithTimePeriod(
        1000000000000000000, // 1 Eth
        0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2, // WETH (base token) // @audit
        0x6B175474E89094C44Da98b954EedeAC495271d0F, // DAI (quote token) // @audit
        pools, // DAI/WETH pool uni v3
        600 // period
    );
\u0060\u0060\u0060

[Link to code](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L36-L42)

Finally, both values are used to calculate an average price of in \u0060((DAIWethPrice + uint256(price) * 1e10) / 2)\u0060.

But as seen, one has price in \u0060DAI/ETH\u0060 and the other one in \u0060WETH/DAI\u0060, which leads to an incorrect result.

\u0060\u0060\u0060solidity
    return
        (wethPriceUSD * 1e18) /
        ((DAIWethPrice + uint256(price) * 1e10) / 2);
\u0060\u0060\u0060

[Link to code](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L50C15-L52)

The average will be lower in this case, and the resulting price higher. 

This will be used by \u0060USSD::mintForToken()\u0060 for calculating the amount of tokens to mint for the user, and thus giving them much more than they should.

Also worth mentioning that \u0060USSDRebalancer::rebalance()\u0060 also relies on the result of this price calculation and will make it perform trades with incorrect values.

## Impact

Users will receive far more USSD tokens than they should when they call \u0060mintForToken()\u0060, ruining the token value.

When performed the \u0060USSDRebalancer::rebalance()\u0060, all the calculations will be broken for the DAI oracle, leading to incorrect pool trades due to the error in \u0060getPrice()\u0060

## Code Snippet

- https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L46C28-L48
- https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L36-L42
- https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/oracles/StableOracleDAI.sol#L50C15-L52

## Tool used

Manual Review

## Recommendation

Calculate the inverse of the \u0060price\u0060 returned by the Chainlink feed so that it can be averaged with the pool price, making sure that both use the correct \u0060WETH/DAI\u0060 and \u0060ETH/DAI\u0060 base/rate tokens.



