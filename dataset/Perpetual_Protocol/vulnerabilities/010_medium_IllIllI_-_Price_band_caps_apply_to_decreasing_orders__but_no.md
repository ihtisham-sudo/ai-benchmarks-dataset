# IllIllI - Price band caps apply to decreasing orders, but not to liquidations

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Perpetual Protocol
**Keywords:** cybersecurity, vulnerability, price band caps, liquidation, trading, market price, OracleMaker, liquidity, trading halts, extreme price movement, borrowing fees, funding fees, liquidation penalties, notional value, market-determined price, stale oracle price, high volatility, order gateways, relayers, manual review

---

IllIllI

medium

# Price band caps apply to decreasing orders, but not to liquidations

## Summary

Price band caps limit the price at which an order can be settled (e.g. someone trying to reduce their exposure in order to avoid liquidation), but liquidations have no such limitation.


## Vulnerability Detail

Price bands are [used](https://github.com/sherlock-audit/2024-02-perpetual/blob/02f17e70a23da5d71364268ccf7ed9ee7cedf428/perp-contract-v3/test/orderGatewayV2/OrderGatewayV2.settleOrder.int.t.sol#L1269-L1273) in order to ensure that users can\u0027t trade a extreme prices, which would result in lower-than usual fees, and liquidations to be less likely, because borrowing fees, funding fees, and liquidation penalties are all based on the opening notional value, rather than the current position size\u0027s value, and the reduced fee wouldn\u0027t be enough incentive to liquidate the position.

Having price caps means that even if there are two willing parties willing to settle a trade at a market-determined price, they will be prevented from doing so. In traditional financial markets, there are also trading halts when there is extreme price movement. The difference here is that while no trades are allowed during market halts in traditional finance, in the Perpetual system, liquidations are allowed to take place even if users can\u0027t close their positions.


## Impact

The whole purpose of the OracleMaker is to be able to provide liquidity at _all_ times, though this liquidity may be available at a disadvantageous price. If there\u0027s a price band, anyone who tries to exit their position before they\u0027re liquidated (incurring a fee charged on top of losing the position), will have their orders rejected, even at the disadvantageous price. Note that orders interacting with the OracleMaker, and with other non-whitelisted makers (other traders) are executed by Relayers, who are expected to settle orders after a delay, so definitionally, they\u0027ll either be using a stale oracle price or will be executing after other traders have had a change to withdraw their liquidity. In either case, during periods of high volatility and liquidations, the price being used will no longer match the market\u0027s clearing price.


## Code Snippet

Orders modifying/creating positions have price band checks:
\u0060\u0060\u0060solidity
// File: src/clearingHouse/ClearingHouse.sol : ClearingHouse._openPosition()   #1

321                if (params.isBaseToQuote) {
322                    // base to exactOutput(quote), B2Q base- quote+
323                    result.base = -oppositeAmount.toInt256();
324                    result.quote = params.amount.toInt256();
325                } else {
326                    // quote to exactOutput(base), Q2B base+ quote-
327                    result.base = params.amount.toInt256();
328                    result.quote = -oppositeAmount.toInt256();
329                }
330            }
331:@>         _checkPriceBand(params.marketId, result.quote.abs().divWad(result.base.abs()));
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/clearingHouse/ClearingHouse.sol#L321-L331

but liquidations don\u0027t have any price caps, and dont have any authorization checks, which means it can be executed without going through the order gateways and their [relayers](https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/orderGatewayV2/OrderGatewayV2.sol#L161):
\u0060\u0060\u0060solidity
// File: src/clearingHouse/ClearingHouse.sol : ClearingHouse.params   #2

160        /// @inheritdoc IClearingHouse
161        function liquidate(
162            LiquidatePositionParams calldata params
163:       ) external nonZero(params.positionSize) returns (int256, int256) {
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/clearingHouse/ClearingHouse.sol#L160-L163


## Tool used

Manual Review


## Recommendation

Don\u0027t use the price bands for trades against the OracleMaker. As is shown by some of my other submissions, removing the price bands altogether is not safe.

