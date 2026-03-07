# ether_sky - Bidders\u0027 funds may become locked due to inconsistent price order checks in MaxPriorityQueue and the _claimBid function.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axis Finance
**Keywords:** cybersecurity, vulnerability, MaxPriorityQueue, bids, marginal price, auction winners, claimBid function, bidder, base tokens, quote tokens, price order checks, inconsistent pricing, bidding process, locking funds, finite supply, manual review, Math.mulDivUp, test modules, auction house, rounding errors

---

ether_sky

high

# Bidders\u0027 funds may become locked due to inconsistent price order checks in MaxPriorityQueue and the _claimBid function.

## Summary
In the \u0060MaxPriorityQueue\u0060, \u0060bids\u0060 are ordered by decreasing \u0060price\u0060.
We calculate the \u0060marginal price\u0060, \u0060marginal bid ID\u0060, and determine the \u0060auction winners\u0060.
When a \u0060bidder\u0060 wants to claim, we verify that the \u0060bid price\u0060 of this \u0060bidder\u0060 exceeds the \u0060marginal price\u0060.
However, there\u0027s minor inconsistency: certain \u0060bids\u0060 may have \u0060marginal price\u0060 and a smaller \u0060bid ID\u0060 than \u0060marginal bid ID\u0060 and they are not actually \u0060winners\u0060.
As a result, the \u0060auction winners\u0060 and these \u0060bidders\u0060 can receive \u0060base\u0060 tokens.
However, there is a finite supply of \u0060base\u0060 tokens for \u0060auction winners\u0060.
Early \u0060bidders\u0060 who claim can receive \u0060base\u0060 tokens, but the last \u0060bidders\u0060 can not.
## Vulnerability Detail
The comparison for the order of \u0060bids\u0060 in the \u0060MaxPriorityQueue\u0060 is as follow:
if \u0060q1 * b2 < q2 * b1\u0060 then \u0060bid (q2, b2)\u0060 takes precedence over \u0060bid (q1, b1)\u0060.
\u0060\u0060\u0060solidity
function _isLess(Queue storage self, uint256 i, uint256 j) private view returns (bool) {
    uint64 iId = self.bidIdList[i];
    uint64 jId = self.bidIdList[j];
    Bid memory bidI = self.idToBidMap[iId];
    Bid memory bidJ = self.idToBidMap[jId];
    uint256 relI = uint256(bidI.amountIn) * uint256(bidJ.minAmountOut);
    uint256 relJ = uint256(bidJ.amountIn) * uint256(bidI.minAmountOut);
    if (relI == relJ) {
        return iId > jId;
    }
    return relI < relJ;
}
\u0060\u0060\u0060
And in the \u0060_calimBid\u0060 function, the \u0060price\u0060 is checked directly as follow:
if \u0060q * 10 ** baseDecimal / b >= marginal price\u0060, then this \u0060bid\u0060 can be claimed.
\u0060\u0060\u0060solidity
function _claimBid(
    uint96 lotId_,
    uint64 bidId_
) internal returns (BidClaim memory bidClaim, bytes memory auctionOutput_) {
    uint96 price = uint96(
        bidData.minAmountOut == 0
            ? 0 // TODO technically minAmountOut == 0 should be an infinite price, but need to check that later. Need to be careful we don\u0027t introduce a way to claim a bid when we set marginalPrice to type(uint96).max when it cannot be settled.
            : Math.mulDivUp(uint256(bidData.amount), baseScale, uint256(bidData.minAmountOut))
    );
    uint96 marginalPrice = auctionData[lotId_].marginalPrice;
    if (
        price > marginalPrice
            || (price == marginalPrice && bidId_ <= auctionData[lotId_].marginalBidId)
    ) { }
}
\u0060\u0060\u0060
The issue is that a \u0060bid\u0060 with the \u0060marginal price\u0060 might being placed after \u0060marginal bid\u0060 in the \u0060MaxPriorityQueue\u0060 due to rounding.
\u0060\u0060\u0060solidity
q1 * b2 < q2 * b1, but mulDivUp(q1, 10 ** baseDecimal, b1) = mulDivUp(q2, 10 ** baseDecimal, b2)
\u0060\u0060\u0060

Let me take an example.
The \u0060capacity\u0060 is \u006010e18\u0060 and there are \u00606 bids\u0060 (\u0060(4e18 + 1, 2e18)\u0060 for first \u0060bidder\u0060, \u0060(4e18 + 2, 2e18)\u0060 for the other \u0060bidders\u0060.
The order in the \u0060MaxPriorityQueue\u0060 is \u0060(2, 3, 4, 5, 6, 1)\u0060.
The \u0060marginal bid ID\u0060 is \u00606\u0060.
The \u0060marginal price\u0060 is \u00602e18 + 1\u0060.
The \u0060auction winners\u0060 are \u0060(2, 3, 4, 5, 6)\u0060.
However, \u0060bidder 1\u0060 can also claim because it\u0027s \u0060price\u0060 matches the \u0060marginal price\u0060 and it has the smallest \u0060bid ID\u0060.
There are only \u006010e18\u0060 \u0060base\u0060 tokens, but all \u00606 bidders\u0060 require \u00602e18\u0060 \u0060base\u0060 tokens.
As a result, at least one \u0060bidder\u0060 won\u0027t be able to claim \u0060base\u0060 tokens, and his \u0060quote\u0060 tokens will remain locked in the \u0060auction house\u0060.

The Log is
\u0060\u0060\u0060solidity
marginal price     ==>   2000000000000000001
marginal bid id    ==>   6

paid to bid  1       ==>   4000000000000000001
payout to bid  1     ==>   1999999999999999999
*****
paid to bid  2       ==>   4000000000000000002
payout to bid  2     ==>   2000000000000000000
*****
paid to bid  3       ==>   4000000000000000002
payout to bid  3     ==>   2000000000000000000
*****
paid to bid  4       ==>   4000000000000000002
payout to bid  4     ==>   2000000000000000000
*****
paid to bid  5       ==>   4000000000000000002
payout to bid  5     ==>   2000000000000000000
*****
paid to bid  6       ==>   4000000000000000002
payout to bid  6     ==>   2000000000000000000
\u0060\u0060\u0060
Please add below test to the \u0060test/modules/auctions/EMPA/claimBids.t.sol\u0060
\u0060\u0060\u0060solidity
function test_claim_nonClaimable_bid()
    external
    givenLotIsCreated
    givenLotHasStarted
    givenBidIsCreated(4e18 + 1, 2e18)           // bidId = 1
    givenBidIsCreated(4e18 + 2, 2e18)           // bidId = 2
    givenBidIsCreated(4e18 + 2, 2e18)           // bidId = 3
    givenBidIsCreated(4e18 + 2, 2e18)           // bidId = 4
    givenBidIsCreated(4e18 + 2, 2e18)           // bidId = 5
    givenBidIsCreated(4e18 + 2, 2e18)           // bidId = 6
    givenLotHasConcluded
    givenPrivateKeyIsSubmitted
    givenLotIsDecrypted
    givenLotIsSettled
{
    EncryptedMarginalPriceAuctionModule.AuctionData memory auctionData = _getAuctionData(_lotId);

    console2.log(\u0027marginal price     ==>  \u0027, auctionData.marginalPrice);
    console2.log(\u0027marginal bid id    ==>  \u0027, auctionData.marginalBidId);
    console2.log(\u0027\u0027);

    for (uint64 i; i < 6; i ++) {
        uint64[] memory bidIds = new uint64[](1);
        bidIds[0] = i + 1;
        vm.prank(address(_auctionHouse));
        (Auction.BidClaim[] memory bidClaims,) = _module.claimBids(_lotId, bidIds);
        Auction.BidClaim memory bidClaim = bidClaims[0];
        if (i > 0) {
            console2.log(\u0027*****\u0027);
        }
        console2.log(\u0027paid to bid \u0027, i + 1, \u0027      ==>  \u0027, bidClaim.paid);
        console2.log(\u0027payout to bid \u0027, i + 1, \u0027    ==>  \u0027, bidClaim.payout);
    }
}
\u0060\u0060\u0060
## Impact

## Code Snippet
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/lib/MaxPriorityQueue.sol#L109-L120
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/auctions/EMPAM.sol#L347-L350
## Tool used

Manual Review

## Recommendation
In the \u0060MaxPriorityQueue\u0060, we should check the \u0060price\u0060: \u0060Math.mulDivUp(q, 10 ** baseDecimal, b)\u0060.
