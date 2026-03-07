# ether_sky - Bidders can not claim their bids if the auction creator claims the proceeds.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axis Finance
**Keywords:** cybersecurity, vulnerability, auction, bidders, auction creator, proceeds, funds, locked, auction house, base tokens, quote tokens, claim bids, auction status, claimed, settled, prefund, manual review, impact, recommendation, test

---

ether_sky

high

# Bidders can not claim their bids if the auction creator claims the proceeds.

## Summary
Before the \u0060batch auction\u0060 begins, the \u0060auction creator\u0060 should \u0060prefund\u0060 \u0060base\u0060 tokens to the \u0060auction house\u0060.
During the \u0060auction\u0060, \u0060bidders\u0060 transfer \u0060quote\u0060 tokens to the \u0060auction house\u0060.
After the \u0060auction\u0060 settles,
- \u0060Bidders\u0060 can claim their \u0060bids\u0060 and either to receive \u0060base\u0060 tokens or \u0060retrieve\u0060 their \u0060quote\u0060 tokens.
- The \u0060auction creator\u0060 can receive the \u0060quote\u0060 tokens and retrieve the remaining \u0060base\u0060 tokens.
- There is no specific order for these two operations.

However, if the \u0060auction creator\u0060 claims the \u0060proceeds\u0060, \u0060bidders\u0060 can not claim their \u0060bids\u0060 anymore.
Consequently, their \u0060funds\u0060 will remain locked in the \u0060auction house\u0060.
## Vulnerability Detail
When the \u0060auction creator\u0060 claims \u0060Proceeds\u0060, the \u0060auction status\u0060 changes to \u0060Claimed\u0060.
\u0060\u0060\u0060solidity
function _claimProceeds(uint96 lotId_)
    internal
    override
    returns (uint96 purchased, uint96 sold, uint96 payoutSent)
{
    auctionData[lotId_].status = Auction.Status.Claimed;
}
\u0060\u0060\u0060
Once the \u0060auction status\u0060 has transitioned to \u0060Claimed\u0060, there is indeed no way to change it back to \u0060Settled\u0060.

However, \u0060bidders\u0060 can only claim their \u0060bids\u0060 when the \u0060auction status\u0060 is \u0060Settled\u0060.
\u0060\u0060\u0060solidity
function claimBids(
    uint96 lotId_,
    uint64[] calldata bidIds_
)
    external
    override
    onlyInternal
    returns (BidClaim[] memory bidClaims, bytes memory auctionOutput)
{
    _revertIfLotInvalid(lotId_);
    _revertIfLotNotSettled(lotId_);   // @audit, here

    return _claimBids(lotId_, bidIds_);
}
\u0060\u0060\u0060

Please add below test to the \u0060test/modules/auctions/claimBids.t.sol\u0060.
\u0060\u0060\u0060solidity
function test_claimProceeds_before_claimBids()
    external
    givenLotIsCreated
    givenLotHasStarted
    givenBidIsCreated(_BID_AMOUNT_UNSUCCESSFUL, _BID_AMOUNT_OUT_UNSUCCESSFUL)
    givenBidIsCreated(_BID_PRICE_TWO_AMOUNT, _BID_PRICE_TWO_AMOUNT_OUT)
    givenBidIsCreated(_BID_PRICE_TWO_AMOUNT, _BID_PRICE_TWO_AMOUNT_OUT)
    givenBidIsCreated(_BID_PRICE_TWO_AMOUNT, _BID_PRICE_TWO_AMOUNT_OUT)
    givenBidIsCreated(_BID_PRICE_TWO_AMOUNT, _BID_PRICE_TWO_AMOUNT_OUT)
    givenBidIsCreated(_BID_PRICE_TWO_AMOUNT, _BID_PRICE_TWO_AMOUNT_OUT)
    givenBidIsCreated(_BID_PRICE_TWO_AMOUNT, _BID_PRICE_TWO_AMOUNT_OUT)
    givenLotHasConcluded
    givenPrivateKeyIsSubmitted
    givenLotIsDecrypted
    givenLotIsSettled
{
    uint64 bidId = 1;

    uint64[] memory bidIds = new uint64[](1);
    bidIds[0] = bidId;

    // Call the function
    vm.prank(address(_auctionHouse));
    _module.claimProceeds(_lotId);


    bytes memory err = abi.encodeWithSelector(EncryptedMarginalPriceAuctionModule.Auction_WrongState.selector, _lotId);
    vm.expectRevert(err);
    vm.prank(address(_auctionHouse));
    _module.claimBids(_lotId, bidIds);
}
\u0060\u0060\u0060
## Impact
Users\u0027 funds could be locked.
## Code Snippet
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/auctions/EMPAM.sol#L846
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/Auction.sol#L556
## Tool used

Manual Review

## Recommendation
Allow \u0060bidders\u0060 to claim their \u0060bids\u0060 even when the \u0060auction status\u0060 is \u0060Claimed\u0060.
