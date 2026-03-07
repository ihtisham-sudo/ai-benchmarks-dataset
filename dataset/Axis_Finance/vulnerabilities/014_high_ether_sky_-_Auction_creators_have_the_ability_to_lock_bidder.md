# ether_sky - Auction creators have the ability to lock bidders\u0027 funds.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axis Finance
**Keywords:** cyber security, vulnerability, auction creators, bidders, funds locking, auction cancellation, quote tokens, base tokens, auction house, batch auction, risk assessment, block.timestamp, auction status, claimed, refund, claimBids, settled, private key, decrypt, manual review

---

ether_sky

high

# Auction creators have the ability to lock bidders\u0027 funds.

## Summary
\u0060Auction creators\u0060 have the ability to cancel an \u0060auction\u0060 before it starts.
However, once the \u0060auction\u0060 begins, they should not be allowed to cancel it.
During the \u0060auction\u0060, \u0060bidders\u0060 can place \u0060bids\u0060 and send \u0060quote\u0060 tokens to the \u0060auction house\u0060.
After the \u0060auction\u0060 concludes, \u0060bidders\u0060 can either receive \u0060base\u0060 tokens or retrieve their \u0060quote\u0060 tokens.
Unfortunately, \u0060batch auction creators\u0060 can cancel an \u0060auction\u0060 when it ends.
This means that \u0060auction creators\u0060 can cancel their \u0060auctions\u0060 if they anticipate \u0060losses\u0060.
This should not be allowed.
The significant risk is that \u0060bidders\u0027 funds\u0060 could become locked in the \u0060auction house\u0060.
## Vulnerability Detail
\u0060Auction creators\u0060 can not cancel an \u0060auction\u0060 once it concludes.
\u0060\u0060\u0060solidity
function cancelAuction(uint96 lotId_) external override onlyInternal {
    _revertIfLotConcluded(lotId_);
}
\u0060\u0060\u0060
They also can not cancel it while it is active.
\u0060\u0060\u0060solidity
function _cancelAuction(uint96 lotId_) internal override {
    _revertIfLotActive(lotId_);

    auctionData[lotId_].status = Auction.Status.Claimed;
}
\u0060\u0060\u0060
When the \u0060block.timestamp\u0060 aligns with the \u0060conclusion\u0060 time of the \u0060auction\u0060, we can bypass these checks.
\u0060\u0060\u0060solidity
function _revertIfLotConcluded(uint96 lotId_) internal view virtual {
    if (lotData[lotId_].conclusion < uint48(block.timestamp)) {
        revert Auction_MarketNotActive(lotId_);
    }

    if (lotData[lotId_].capacity == 0) revert Auction_MarketNotActive(lotId_);
}
function _revertIfLotActive(uint96 lotId_) internal view override {
    if (
        auctionData[lotId_].status == Auction.Status.Created
            && lotData[lotId_].start <= block.timestamp
            && lotData[lotId_].conclusion > block.timestamp
    ) revert Auction_WrongState(lotId_);
}
\u0060\u0060\u0060
So \u0060Auction creators\u0060 can cancel an \u0060auction\u0060 when it concludes.
Then the \u0060capacity\u0060 becomes \u00600\u0060 and the \u0060auction status\u0060 transitions to \u0060Claimed\u0060.

\u0060Bidders\u0060 can not \u0060refund\u0060 their \u0060bids\u0060.
\u0060\u0060\u0060solidity
function refundBid(
    uint96 lotId_,
    uint64 bidId_,
    address caller_
) external override onlyInternal returns (uint96 refund) {
    _revertIfLotConcluded(lotId_);
}
 function _revertIfLotConcluded(uint96 lotId_) internal view virtual {
    if (lotData[lotId_].capacity == 0) revert Auction_MarketNotActive(lotId_);
}
\u0060\u0060\u0060
The only way for \u0060bidders\u0060 to reclaim their tokens is by calling the \u0060claimBids\u0060 function.
However, \u0060bidders\u0060 can only claim \u0060bids\u0060 when the \u0060auction status\u0060 is \u0060Settled\u0060.
\u0060\u0060\u0060solidity
function claimBids(
    uint96 lotId_,
    uint64[] calldata bidIds_
) {
    _revertIfLotNotSettled(lotId_);
}
\u0060\u0060\u0060
To \u0060settle\u0060 the \u0060auction\u0060, the \u0060auction status\u0060 should be \u0060Decrypted\u0060.
This requires submitting the \u0060private key\u0060.
The \u0060auction creator\u0060 can not submit the \u0060private key\u0060 or submit it without decrypting any \u0060bids\u0060 by calling \u0060submitPrivateKey(lotId, privateKey, 0)\u0060.
Then nobody can decrypt the \u0060bids\u0060 using the \u0060decryptAndSortBids\u0060 function which always reverts.
\u0060\u0060\u0060solidity
function decryptAndSortBids(uint96 lotId_, uint64 num_) external {
    if (
        auctionData[lotId_].status != Auction.Status.Created     // @audit, here
            || auctionData[lotId_].privateKey == 0
    ) {
        revert Auction_WrongState(lotId_);
    }

    _decryptAndSortBids(lotId_, num_);
}
\u0060\u0060\u0060
As a result, the \u0060auction status\u0060 remains unchanged, preventing it from transitioning to \u0060Settled\u0060.
This leaves the \u0060bidders\u0027\u0060 \u0060quote\u0060 tokens locked in the \u0060auction house\u0060.

Please add below test to the \u0060test/modules/Auction/cancel.t.sol\u0060.
\u0060\u0060\u0060solidity
function test_cancel() external whenLotIsCreated {
    Auction.Lot memory lot = _mockAuctionModule.getLot(_lotId);

    console2.log("lot.conclusion before   ==> ", lot.conclusion);
    console2.log("block.timestamp before  ==> ", block.timestamp);
    console2.log("isLive                  ==> ", _mockAuctionModule.isLive(_lotId));

    vm.warp(lot.conclusion - block.timestamp + 1);
    console2.log("lot.conclusion after    ==> ", lot.conclusion);
    console2.log("block.timestamp after   ==> ", block.timestamp);
    console2.log("isLive                  ==> ", _mockAuctionModule.isLive(_lotId));

    vm.prank(address(_auctionHouse));
    _mockAuctionModule.cancelAuction(_lotId);
}
\u0060\u0060\u0060
The log is
\u0060\u0060\u0060solidity
lot.conclusion before   ==>  86401
block.timestamp before  ==>  1
isLive                  ==>  true
lot.conclusion after    ==>  86401
block.timestamp after   ==>  86401
isLive                  ==>  false
\u0060\u0060\u0060
## Impact
Users\u0027 funds can be locked.
## Code Snippet
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/Auction.sol#L354
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/auctions/EMPAM.sol#L204
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/Auction.sol#L512
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/Auction.sol#L556
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/auctions/EMPAM.sol#L449
## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060solidity
function _revertIfLotConcluded(uint96 lotId_) internal view virtual {
-     if (lotData[lotId_].conclusion < uint48(block.timestamp)) {
+     if (lotData[lotId_].conclusion <= uint48(block.timestamp)) {
        revert Auction_MarketNotActive(lotId_);
    }

    // Capacity is sold-out, or cancelled
    if (lotData[lotId_].capacity == 0) revert Auction_MarketNotActive(lotId_);
}
\u0060\u0060\u0060
