# IssueH-3: Calling the transferReserveToAuction will revert due to increase in currentPeriod

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** auction, transferReserveToAuction, currentPeriod, revert, mapping, bondToken, globalPool, address, require, msg.sender, reserveToken, IERC20, safeTransfer, auctionAddress, period, increase, function, tokens, protocol, issue

---

# IssueH-3: Calling the transferReserveToAuction will revert due to increase in currentPeriod

Source: [GitHub Issue #407](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/407)

Found by
056Security, 0x23r0, 0x52, 0xAadi, 0xEkko, 0xPhantom2, 0xadrii, 0xc0ffEE, 0xrex, 4th05, Artur, Aymen0909, BADROBINX, ChainProof, Goran, Hueber, Kenn.eth, Kyosi, Mill, MysteryAuditor, POB, Pablo, Schnilch, Strapontin, Uddercover, Vidus, X0sauce, ZoA, alphacipher, bladeee, bretzel, carlitox477, dobrevaleri, elolpuer, elvin.a.block, evmboi32, farismaulana, i3arba, jimpixjed, jprod15, momentum, mxteem, novaman33, oxelmiguel, pashap9990, phoenixv110, rudhra1749, shiazinho, shui, shushu, silver_eth, sl1, stuart_the_minion, tinnohofficial, tusharr1411, tvdung94, wellbyt3, x0lohaclohell, y4y, zhenyazhd

Summary
The auction contract calls the transferReserveToAuction function to pull the reserve tokens. However, an issue occurs that will prevent the auction contract from calling the function.

Root Cause
During auction creation, the currentPeriod is used to store the auction address in the auctions mapping, however, the currentPeriod is then increased to another value, meaning when we quote the current period again, it will return 2 if it was 1 prior to the increase.

\u0060\u0060\u0060solidity
auctions[currentPeriod] = Utils.deploy(
    address(new Auction()),
    abi.encodeWithSelector(
        Auction.initialize.selector,
        address(couponToken),
        address(reserveToken),
        couponAmountToDistribute,
        block.timestamp + auctionPeriod,
        1000,
        address(this),
        poolSaleLimit
    )
);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Increase the bond token period
bondToken.increaseIndexedAssetPeriod(sharesPerToken);
\u0060\u0060\u0060

Can happen in normal operation.

none

1. User or anyone starts the auction and the auction address is stored in the auctions mapping.
2. After some time, the auction succeed and the transferReserveToAuction is called to transfer the reserve token to the auction contract.
3. Since the currentPeriod has now increased, quoting the bondToken.globalPool() will return the increased value, meaning the mapping will return zero address because there\u0027s no address saved to it, so comparing it with the msg.sender will revert because the caller auction address != address(0).

The call to the transferReserveToAuction will fail and ending the auction will not take place.

No response

This can be mitigated by subtracting 1 from the quoted currentPeriod in the transferReserveToAuction function.

\u0060\u0060\u0060solidity
function transferReserveToAuction(uint256 amount) external virtual {
    (uint256 currentPeriod, ) = bondToken.globalPool();
    uint256 previousCurrentPeriod = currentPeriod - 1;
    address auctionAddress = auctions[previousCurrentPeriod];
    require(msg.sender == auctionAddress, CallerIsNotAuction());
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
IERC20(reserveToken).safeTransfer(msg.sender, amount);
\u0060\u0060\u0060
just like it happened in the distribute function.

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/157](https://github.com/Convexity-Research/plaza-evm/pull/157)
## Issue H-4: BondOracleAdapter will cause massive loss of funds for a large number of bond tokens

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/440)  
Found by: 0x52, ZoA, bladeee


BondOracleAdapter both directly returns the price from the pool and hardcodes the oracle decimals to \u0060bondToken.decimals()\u0060. The combination of these two factors will cause the adapter to return an incorrect value for any bond token that is not alphanumerically greater than USDC. The dex pool always prices token A in terms of token B and because the decimals of the oracle are hardcoded to the decimals of the bond token, the bond token must be token B or else the decimals will be incorrect. This incorrect pricing will cause massive loss of funds to user withdrawing from the pool as the market price will be much too low.

When initializing the BondOracleAdapter, it pulls the pool address from the \u0060getPool\u0060 mapping. While this will pull the relevant pool for those tokens, it does not ensure that the tokens are in the correct order.

\u0060\u0060\u0060solidity
getPool[token0][token1][tickSpacing] = pool;
// populate mapping in the reverse direction, deliberate choice to avoid the cost
getPool[token1][token0][tickSpacing] = pool;
\u0060\u0060\u0060

We see that \u0060getPool\u0060 is populated in both orders even though they are sorted alphanumerically. Therefore when the pool is retrieved for BondOracleAdapter the tokens can be in any order.

\u0060\u0060\u0060solidity
return (uint80(0), int256(getPriceX96FromSqrtPriceX96(getSqrtTwapX96)),
block.timestamp, block.timestamp, uint80(0));
\u0060\u0060\u0060

We see that when price is returned it is always returned directly as returned by the underlying dex pool. The issue is that if the bond token is not token B then the decimal of the return value will be the liquidity token rather than the bond token.

\u0060\u0060\u0060solidity
Pool.sol#L519-L521
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
if (marketRate != 0 && marketRate < redeemRate) {
    redeemRate = marketRate;
}
\u0060\u0060\u0060

As a result when redeeming bond tokens the value will be significantly lower than expected and will result in bondholders losing large amounts of value.

- BondOracleAdapter#L113 always returns price directly
- BondOracleAdapter.sol#L62 always assumes that price is denominated in bond tokens

- address(bondToken) > address(liquidityToken)

- N/A

- N/A

- Loss of funds for redeeming bond token holders

- No response

- BondOracleAdapter#initialize should set decimals to either bondToken or liquidityToken depending on token order in the pool

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/Convexity-Research/plaza-evm/pull/158
