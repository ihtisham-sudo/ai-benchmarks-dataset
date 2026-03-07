# ether_sky - There may be excess funds in the PnL pool or bad debt due to the funding fee.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Perpetual Protocol
**Keywords:** cybersecurity, vulnerability, PnL pool, bad debt, OracleMaker, SpotHedgeBaseMaker, LPs, Traders, orders, borrowing fee, funding fee, positions, funding rate, openNotionals, long position, short position, protocol, yields, funding sources, manual review

---

ether_sky

medium

# There may be excess funds in the PnL pool or bad debt due to the funding fee.

## Summary
There are two types of \u0060makers\u0060: \u0060OracleMaker\u0060 and \u0060SpotHedgeBaseMaker\u0060, where \u0060LPs\u0060 can deposit funds.
\u0060Traders\u0060 can then execute their \u0060orders\u0060 against these \u0060makers\u0060.
To incentivize \u0060LPs\u0060, several mechanisms exist for these \u0060makers\u0060 to profit.
One is the \u0060borrowing fee\u0060, which both \u0060makers\u0060 can benefit from.
Another is the \u0060funding fee\u0060, which specifically benefits \u0060OracleMaker\u0060.
The \u0060funding fee\u0060 incentivizes users to maintain \u0060positions\u0060 with the same direction of \u0060OracleMaker\u0060.
However, due to the \u0060funding fee\u0060, there may be excess funds in the \u0060PnL pool\u0060 or occurrences of \u0060bad debt\u0060.
## Vulnerability Detail
Typically, in most \u0060protocols\u0060, the generated \u0060yields\u0060 are totally distributed to users and the \u0060protocol\u0060 itself.
In the \u0060Perpetual\u0060 protocol, all \u0060borrowing fees\u0060 from \u0060payers\u0060 are solely distributed to \u0060receivers\u0060, which are whitelisted by the \u0060protocol\u0060.
However, not all \u0060funding fees\u0060 are distributed, or there may be a lack of \u0060funding fees\u0060 available for distribution.
The current \u0060funding rate\u0060 is determined based on the current \u0060position\u0060 of the \u0060base pool\u0060(\u0060OracleMaker\u0060).
\u0060\u0060\u0060solidity
function getCurrentFundingRate(uint256 marketId) public view returns (int256) {
    uint256 fundingRateAbs = FixedPointMathLib.fullMulDiv(
        fundingConfig.fundingFactor,
        FixedPointMathLib
            .powWad(openNotionalAbs.toInt256(), fundingConfig.fundingExponentFactor.toInt256())
            .toUint256(),
        maxCapacity
    );
}
\u0060\u0060\u0060
Holders of \u0060positions\u0060 with the same direction of the \u0060position\u0060 of the \u0060OracleMaker\u0060 receive \u0060funding fees\u0060, while those with \u0060positions\u0060 in the opposite direction are required to pay \u0060funding fees\u0060.
The amount of \u0060funding fees\u0060 generated per second is calculated as the product of the \u0060funding rate\u0060 and the sum of \u0060openNotionals\u0060 of \u0060positions\u0060 with the opposite direction.
Conversely, the amount of \u0060funding fees\u0060 distributed per second is calculated as the product of the \u0060funding rate\u0060 and the sum of \u0060openNotionls\u0060 of \u0060positions\u0060 with the same direction of the \u0060position\u0060 of the \u0060OracleMaker\u0060.
\u0060\u0060\u0060solidity
function getPendingFee(uint256 marketId, address trader) public view returns (int256) {
    int256 fundingRate = getCurrentFundingRate(marketId);
    int256 fundingGrowthLongIndex = _getFundingFeeStorage().fundingGrowthLongIndexMap[marketId] +
        (fundingRate * int256(block.timestamp - _getFundingFeeStorage().lastUpdatedTimestampMap[marketId]));
    int256 openNotional = _getVault().getOpenNotional(marketId, trader);
    int256 fundingFee = 0;
    if (openNotional != 0) {
        fundingFee = _calcFundingFee(
            openNotional,
            fundingGrowthLongIndex - _getFundingFeeStorage().lastFundingGrowthLongIndexMap[marketId][trader]
        );   // @audit, here
    }
    return fundingFee;
}
\u0060\u0060\u0060
All \u0060orders\u0060 are settled against \u0060makers\u0060, meaning for every \u0060long position\u0060, there should be an equivalent \u0060short position\u0060.
While we might expect the sum of \u0060openNotionals\u0060 of \u0060long positions\u0060 to be equal to the \u0060openNotionals\u0060 of \u0060short positions\u0060, in reality, they may differ.

Suppose there are two \u0060long positions\u0060 with \u0060openNotional\u0060 values of \u0060S\u0060 and \u0060S/2\u0060.
Then there should be two \u0060short positions\u0060 with \u0060openNotianal\u0060 values of \u0060-S\u0060 and \u0060-S/2\u0060.
If the holder of the first \u0060long position\u0060 cancels his \u0060order\u0060 against the second \u0060short position\u0060 with \u0060-S/2\u0060, the \u0060openNotional\u0060 of the \u0060long position\u0060 becomes \u00600\u0060, and the second \u0060short position\u0060 becomes a \u0060long position\u0060.
However, we can not be certain that the \u0060openNotional\u0060 of the new \u0060long position\u0060 is exactly \u0060S/2\u0060.
\u0060\u0060\u0060solidity
function add(Position storage self, int256 positionSizeDelta, int256 openNotionalDelta) internal returns (int256) {
    int256 openNotional = self.openNotional;
    int256 positionSize = self.positionSize;

    bool isLong = positionSizeDelta > 0;
    int256 realizedPnl = 0;

    // new or increase position
    if (positionSize == 0 || (positionSize > 0 && isLong) || (positionSize < 0 && !isLong)) {
        // no old pos size = new position
        // direction is same as old pos = increase position
    } else {
        // openNotionalDelta and oldOpenNotional have different signs = reduce, close or reverse position
        // check if it\u0027s reduce or close by comparing absolute position size
        // if reduce
        // realizedPnl = oldOpenNotional * closedRatio + openNotionalDelta
        // closedRatio = positionSizeDeltaAbs / positionSizeAbs
        // if close and increase reverse position
        // realizedPnl = oldOpenNotional + openNotionalDelta * closedPositionSize / positionSizeDelta
        uint256 positionSizeDeltaAbs = positionSizeDelta.abs();
        uint256 positionSizeAbs = positionSize.abs();

        if (positionSizeAbs >= positionSizeDeltaAbs) {
            // reduce or close position
            int256 reducedOpenNotional = (openNotional * positionSizeDeltaAbs.toInt256()) /
                positionSizeAbs.toInt256();
            realizedPnl = reducedOpenNotional + openNotionalDelta;
        } else {
            // open reverse position
            realizedPnl =
                openNotional +
                (openNotionalDelta * positionSizeAbs.toInt256()) /
                positionSizeDeltaAbs.toInt256();
        }
    }

    self.positionSize += positionSizeDelta;
    self.openNotional += openNotionalDelta - realizedPnl;

    return realizedPnl;
}
\u0060\u0060\u0060
Indeed, the \u0060openNotional\u0060 of the new \u0060long position\u0060 is determined by the current \u0060price\u0060.
Consequently, while the \u0060position size\u0060 of this new \u0060long position\u0060 will be the same with the old second \u0060long position\u0060 with an \u0060openNotional\u0060 value of \u0060S/2\u0060, the \u0060openNotional\u0060 of the new \u0060long position\u0060 can indeed vary from \u0060S/2\u0060.
As a result, the sum of \u0060openNotionals\u0060 of \u0060short positions\u0060 can differ from the sum of \u0060long positions\u0060.
There are numerous other scenarios where the sums of \u0060openNotionals\u0060 may vary.

I believe that the developers also thought that the \u0060funding fees\u0060 are totally used between it\u0027s \u0060payers\u0060 and \u0060receivers\u0060 from the below code.
\u0060\u0060\u0060solidity
/// @notice positive -> pay funding fee -> fundingFee should round up
/// negative -> receive funding fee -> -fundingFee should round down
function _calcFundingFee(int256 openNotional, int256 deltaGrowthIndex) internal pure returns (int256) {
    if (openNotional * deltaGrowthIndex > 0) {
        return int256(FixedPointMathLib.fullMulDivUp(openNotional.abs(), deltaGrowthIndex.abs(), WAD));
    } else {
        return (openNotional * deltaGrowthIndex) / WAD.toInt256();
    }
}
\u0060\u0060\u0060
They even took \u0060rounding\u0060 into serious consideration to prevent any shortfall of \u0060funding fees\u0060 for distribution.
## Impact
Excess \u0060funding fees\u0060 in the \u0060PnL pool\u0060 can arise when the sum of \u0060openNotionals\u0060 of the \u0060payers\u0060 exceeds that of the \u0060receivers\u0060.
Conversely, \u0060bad debt\u0060 may occur in other cases, leading to a situation where users are unable to receive their \u0060funding fees\u0060 due to an insufficient \u0060PnL pool\u0060.
It is worth to note that other \u0060yields\u0060, such as the \u0060borrowing fee\u0060, are entirely utilized between it\u0027s \u0060payers\u0060 and \u0060receivers\u0060.
Therefore, there are no additional \u0060funding sources\u0060 available to address any shortages of \u0060funding fees\u0060.
## Code Snippet
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/fundingFee/FundingFee.sol#L133-L139
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/fundingFee/FundingFee.sol#L89-L102
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/vault/LibPosition.sol#L45-L48
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/fundingFee/FundingFee.sol#L183-L191
## Tool used

Manual Review

## Recommendation
We can calculate \u0060funding fees\u0060 based on the \u0060position size\u0060 because the sum of the \u0060position sizes\u0060 of \u0060long positions\u0060 will always be equal to the sum of \u0060short positions\u0060 in all cases.
