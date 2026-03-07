# 14si2o_Flint - Highest bidder can withdraw his collateral due to a missing check in _cancelAllBids

**Severity:** high
**Auditor:** Sherlock
**Protocol:** RadicalXChange
**Keywords:** cybersecurity, vulnerability, auction, collateral, bidder, highest bidder, cancel bid, cancel all bids, withdraw, eth, smart contract, require check, malicious user, contract balance, locked collateral, bid amount, system exploit, manual review, recommendation, security flaw

---

14si2o_Flint

high

# Highest bidder can withdraw his collateral due to a missing check in _cancelAllBids

## Summary

A bidder with the highest bid cannot cancel his bid since this would break the auction. A check to ensure this was implemented in \u0060_cancelBid\u0060.

However, this check was not implemented in \u0060_cancelAllBids\u0060, allowing the highest bidder to withdraw his collateral and win the auction for free.  

## Vulnerability Detail

The highest bidder should not be able to cancel his bid, since this would break the entire auction mechanism. 

In \u0060_cancelBid\u0060 we can find a require check that ensures this:

\u0060\u0060\u0060solidity
        require(
            bidder != l.highestBids[tokenId][round].bidder,
            \u0027EnglishPeriodicAuction: Cannot cancel bid if highest bidder\u0027
        );

\u0060\u0060\u0060
Yet in \u0060_cancelAllBids\u0060, this check was not implemented. 
\u0060\u0060\u0060solidity
     * @notice Cancel bids for all rounds
     */
    function _cancelAllBids(uint256 tokenId, address bidder) internal {
        EnglishPeriodicAuctionStorage.Layout
            storage l = EnglishPeriodicAuctionStorage.layout();

        uint256 currentAuctionRound = l.currentAuctionRound[tokenId];

        for (uint256 i = 0; i <= currentAuctionRound; i++) {
            Bid storage bid = l.bids[tokenId][i][bidder];

            if (bid.collateralAmount > 0) {
                // Make collateral available to withdraw
                l.availableCollateral[bidder] += bid.collateralAmount;

                // Reset collateral and bid
                bid.collateralAmount = 0;
                bid.bidAmount = 0;
            }
        }
    }

\u0060\u0060\u0060
Example: 
User Bob bids 10 eth and takes the highest bidder spot. 
Bob calls \u0060cancelAllBidsAndWithdrawCollateral\u0060.

The \u0060_cancelAllBids\u0060 function is called and this makes all the collateral from all his bids from every round available to Bob. This includes the current round \u0060<=\u0060 and does not check if Bob is the current highest bidder. Nor is \u0060l.highestBids[tokenId][round].bidder\u0060 reset, so the system still has Bob as the highest bidder. 

Then \u0060_withdrawCollateral\u0060 is automatically called and Bob receives his 10 eth  back. 

The auction ends. If Bob is still the highest bidder, he wins the auction and his bidAmount of 10 eth is added to the availableCollateral of the oldBidder. 

If there currently is more than 10 eth in the contract (ongoing auctions, bids that have not withdrawn), then the oldBidder can withdraw 10 eth. But this means that in the future a withdraw will fail due to this missing 10 eth. 

## Impact

A malicious user can win an auction for free. 

Additionally, either the oldBidder or some other user in the future will suffer the loss.  

If this is repeated multiple times, it will drain the contract balance and all users will lose their locked collateral. 

## Code Snippet
https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/auction/EnglishPeriodicAuctionInternal.sol#L416-L436

https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/auction/EnglishPeriodicAuctionInternal.sol#L380-L413

https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/auction/EnglishPeriodicAuctionInternal.sol#L468-L536

## Tool used

Manual Review

## Recommendation

Implement the require check from _cancelBid to _cancelAllBids.

