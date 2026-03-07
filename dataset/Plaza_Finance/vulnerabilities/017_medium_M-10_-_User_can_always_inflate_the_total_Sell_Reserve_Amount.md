# M-10 - User can always inflate the total Sell Reserve Amount variable to block the auction from being ended

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** Sell Reserve Amount, auction, bid function, buyReserveAmount, FAILED_POOL_SALE_LIMIT, totalSellReserveAmount, money flow, attack, valid bid, poolSaleLimit, IERC20, claimRefund, unprofitable investments, bond ETH, inflation, checks, pool, endAuction, user, cost

---

# Issue M-9: Market rate never used due to decimal discrepancy

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/561)  
Found by: 0x52, 0xadrii, 0xc0ffEE, Hueber, Ryonen, X0sauce, ZoA, bretzel, farman1094, future, fuzzysquirrel, shui, stuart_the_minion, tinnohofficial

A decimal precision mismatch between \u0060marketRate\u0060 (18 decimal precision) and \u0060redeemRate\u0060 (6 decimal precision) in \u0060Pool.sol\u0060 will cause the market rate to never be used.

In \u0060Pool.sol#L512-L516\u0060, the \u0060redeemRate\u0060 is calculated and implicitly uses a precision of 6 decimal precision:
- Pool#512
- Pool#516
- Pool#516: The constant \u0060BOND_TARGET_PRICE = 100\u0060 multiplied by \u0060PRECISION = 1e6 = 100e6\u0060.

However, the \u0060marketRate\u0060 will be normalized to 18dp: The BPT token itself has 18 decimals (\u0060BalancerPoolToken.sol\u0060) so \u0060totalSupply()\u0060 is 18dp. When calculating the price of a BPT, it will formalize each price of the asset of the BPT pool to 18dp: "balancer math works with 18 dec" \u0060BalancerOracleAdapter.sol#L109\u0060. It implies that the decimals of \u0060BalancerOracleAdapter\u0060 is set to 18. Then the final value will have a precision of 18dp. The comparison \u0060marketRate < redeemRate\u0060 will always be false due to this difference in decimal precision.

1. A Chainlink price feed for the bond token must exist and be registered in \u0060OracleFeeds\u0060.
2. The market rate from the Balancer oracle is lower than the calculated redeem rate when both are expressed with the same decimal precision.
3. \u0060getOracleDecimals(reserveToken, USD)\u0060 returns 18.
N/A

1. A user initiates a redeem transaction.
2. The \u0060simulateRedeem\u0060 and \u0060getRedeemAmount\u0060 functions are called.
3. The condition \u0060marketRate < redeemRate\u0060 evaluates to false due to the decimal mismatch.
4. The \u0060redeemRate\u0060, which might be higher than the actual market rate, is used to calculate the amount of reserve tokens the user receives.

The intended functionality of considering the market rate for redemptions is completely bypassed. Users redeeming tokens might receive more reserve tokens than expected if the true market rate (with correct decimals) is lower than the calculated \u0060redeemRate\u0060.

N/A

Change the normalization in \u0060simulateRedeem\u0060 to use the \u0060bondToken.SHARES_DECIMALS()\u0060 instead of \u0060oracleDecimals\u0060.

\u0060\u0060\u0060solidity
uint256 marketRate;
address feed = OracleFeeds(oracleFeeds).priceFeeds(address(bondToken), USD);
uint8 sharesDecimals = bondToken.SHARES_DECIMALS(); // Get the decimals of the shares
if (feed != address(0)) {
    marketRate = getOraclePrice(address(bondToken), USD).normalizeAmount(
        getOracleDecimals(address(bondToken), USD),
        sharesDecimals // Normalize to sharesDecimals
    );
}
\u0060\u0060\u0060

Modify the normalization of \u0060marketRate\u0060 in \u0060Pool.sol\u0060\u0027s \u0060simulateRedeem\u0060 function to use the same decimal precision as \u0060redeemRate\u0060 (6 decimals). Specifically, change the normalization to use \u0060bondToken.SHARES_DECIMALS()\u0060 instead of \u0060oracleDecimals\u0060.

if (feed != address(0)) {
    uint8 sharesDecimals = bondToken.SHARES_DECIMALS(); // Use sharesDecimals for consistent precision
    marketRate = getOraclePrice(address(bondToken), USD)
        .normalizeAmount(
            getOracleDecimals(address(bondToken), USD),
            sharesDecimals
        );
}
return getRedeemAmount(tokenType, depositAmount, bondSupply, levSupply,
    poolReserves, getOraclePrice(reserveToken, USD), oracleDecimals, marketRate)
    .normalizeAmount(COMMON_DECIMALS, IERC20(reserveToken).safeDecimals());

The protocol team fixed this issue in the following PRs/commits:
https://github.com/Convexity-Research/plaza-evm/pull/156
## Issue M-10: User can always inflate the total Sell Reserve Amount variable to block the auction from being ended

Source: [GitHub Issue #723](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/723)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.

Found by:  
0x23r0, 0xDazai, 0xRaz, 0xc0ffEE, 0xmystery, AuditorPraise, Aymen0909, Benterkii, Boy2000, Chain-sentry, ChainProof, DenTonylifer, Hurley, KiroBrejka, Nave765, Ryonen, Saurabh_Singh, Waydou, ZoA, aswinraj94, copperscrewer, elolpuer, evmboi32, farismaulana, gegul, krishnambstu, moray5554, novaman33, pashap9990, queen, rudhra1749, sl1, solidityenj0yer, t0x1c, zxriptor

User can always inflate the total Sell Reserve Amount variable to block the auction from being ended. This is an extremely and cheap attack to perform because the user practically loses nothing. He can call the Auction::bid function right before the end of the auction with some enormous buyReserveAmount as input. This will brick the money flow because he can do it over and over again for every auction, resulting in unprofitable investments for the people who hold bond ETH.

totalSellReserveAmount being easily inflatable without any checks to prevent it.

User making a valid bid with enormous buyReserveAmount as input, right before the end of the auction.

None.

1. User waits until for example 1 second before the end of the auction.
2. Then he calls the bid function, making a valid bid with big buyReserveAmount input.
With this the attack is already performed. After this happens and someone calls the Auction::endAuction function, the auction will be in FAILED_POOL_SALE_LIMIT state because of this check:

\u0060\u0060\u0060solidity
} else if (
  totalSellReserveAmount >=
  (IERC20(sellReserveToken).balanceOf(pool) * poolSaleLimit) / 100
)
\u0060\u0060\u0060


The money flow can be bricked and a user can purposefully bring every auction to FAILED_POOL_SALE_LIMIT for no cost at all, since he can just call the Auction::claimRefund function afterwards.


None


No response
