# zzykxx - Currently auctioned NFTs can be transferred to a different address in a specific edge case

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** RadicalXChange
**Keywords:** cybersecurity, vulnerability, NFT, auction, transfer, theft, protocol, mintToken, bidder, placeBid, closeAuction, collateral, ETH, withdrawCollateral, malicious, impact, code, recommendation, timestamp, collection

---

zzykxx

high

# Currently auctioned NFTs can be transferred to a different address in a specific edge case

## Summary
Currently auctioned NFTs can be transferred to a different address in a specific edge case, leading to theft of funds.

## Vulnerability Detail
The protocol assumes that an NFT cannot change owner while it\u0027s being auctioned, this is generally the case but there is an exception, an NFT can change owner via [mintToken()](https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/license/StewardLicenseBase.sol#L31) while an auction is ongoing when all the following conditions apply:
1. An NFT is added to the collection without being minted (ie. \u0060to\u0060 set to \u0060address(0)\u0060).
2. The NFT is added to the collection with the parameter \u0060tokenInitialPeriodStartTime[]\u0060 set to a timestamp lower than \u0060l.initialPeriodStartTime\u0060 but bigger than \u00600\u0060(ie. \u00600 < tokenInitialPeriodStartTime[] < l.initialPeriodStartTime\u0060).
3. The current \u0060block.timestamp\u0060 is in-between \u0060tokenInitialPeriodStartTime[]\u0060 and \u0060l.initialPeriodStartTime\u0060.

A malicious \u0060initialBidder\u0060 can take advantage of this by:
1. Bidding on the new added NFT via [placeBid()](https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/auction/EnglishPeriodicAuctionInternal.sol#L286).
2. Calling [mintToken()](https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/license/StewardLicenseBase.sol#L31) to transfer the NFT to a different address he controls.
3. Closing the auction via [closeAuction()](https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/auction/EnglishPeriodicAuctionInternal.sol#L465)

At point \u00603.\u0060, because the NFT owner changed, the winning bidder (ie. \u0060initialBidder\u0060) is not the current NFT owner anymore. This will trigger the [following line of code](https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/auction/EnglishPeriodicAuctionInternal.sol#L499-L506):
\u0060\u0060\u0060solidity
l.availableCollateral[oldBidder] += l.highestBids[tokenId][currentAuctionRound].bidAmount;
\u0060\u0060\u0060

Which increases the \u0060availableCollateral\u0060 of the \u0060oldBidder\u0060 (ie. the address that owns the NFT after point \u00602.\u0060) by \u0060bidAmount\u0060 of the highest bid. But because at the moment the highest bid was placed \u0060initialBidder\u0060 was also the NFT owner, he only needed to transfer the \u0060ETH\u0060 fee to the protocol instead of the whole bid amount. 

The \u0060initialBidder\u0060 is now able to extract ETH from the protocol via the address used in point \u00602.\u0060 by calling [withdrawCollateral()](https://github.com/sherlock-audit/2024-02-radicalxchange/blob/main/pco-art/contracts/auction/EnglishPeriodicAuctionInternal.sol#L439) while also retaining the NFT license.

## Impact
Malicious initial bidder can potentially steal ETH from the protocol in an edge case. If the \u0060ADD_TOKEN_TO_COLLECTION_ROLE\u0060 is also malicious, it\u0027s possible to drain the protocol.

## Code Snippet

## Tool used

Manual Review

## Recommendation
Don\u0027t allow \u0060tokenInitialPeriodStartTime[]\u0060 to be set at a timestamp before\u0060l.initialPeriodStartTime\u0060.

