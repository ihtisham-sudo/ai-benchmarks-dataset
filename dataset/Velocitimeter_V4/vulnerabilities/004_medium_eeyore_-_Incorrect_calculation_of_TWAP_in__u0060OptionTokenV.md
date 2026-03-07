# eeyore - Incorrect calculation of TWAP in \u0060OptionTokenV4.getTimeWeightedAveragePrice()\u0060 function.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cybersecurity, vulnerability, TWAP, OptionTokenV4, getTimeWeightedAveragePrice, price calculation, Token price, outdated data, Pair contract, price observations, protocol fees, current price, manual review, impact assessment, financial losses, risk management, smart contract, decentralized finance, blockchain security, price manipulation

---

eeyore

Medium

# Incorrect calculation of TWAP in \u0060OptionTokenV4.getTimeWeightedAveragePrice()\u0060 function.

## Summary

The average price returned by \u0060OptionTokenV4.getTimeWeightedAveragePrice()\u0060 can be up to 30 minutes outdated and does not reflect the current Token price.

## Vulnerability Detail

In the \u0060getTimeWeightedAveragePrice()\u0060 function, the average price is calculated using the last \u0060X\u0060 known price observations from the \u0060Pair\u0060 contract. However, this approach has a flaw because it does not consider the current price, which could be as much as 30 minutes old.

Consider a scenario where the price of the Token significantly increases during this 30-minute window. The resulting maximum discount might not adequately cover the percentage increase in price. This could lead to the protocol failing to collect proper fees when exercising the Tokens.

## Impact

The use of an outdated TWAP price could result in losses for the protocol or users.

## Code Snippet

https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/OptionTokenV4.sol#L372-L388
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/Pair.sol#L222-L246

## Tool used

Manual Review

## Recommendation

To address this issue, incorporating also the current price retrieved from \u0060Pair.current()\u0060 function:

\u0060\u0060\u0060diff
function getTimeWeightedAveragePrice(uint256 _amount) public view returns (uint256) {
    uint256[] memory amtsOut = IPair(pair).prices(
        underlyingToken,
        _amount,
        twapPoints
    );
    uint256 len = amtsOut.length;
    uint256 summedAmount;

    for (uint256 i = 0; i < len; i++) {
        summedAmount += amtsOut[i];
    }

+    summedAmount += IPair(pair).current(underlyingToken, _amount);

-    return summedAmount / twapPoints;
+    return (summedAmount / twapPoints) + 1;
}
\u0060\u0060\u0060
