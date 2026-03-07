# sammy - Auction fails if the \u0027Honorarium Rate\u0027 is 0%

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** RadicalXChange
**Keywords:** cybersecurity, vulnerability, auction, Honorarium Rate, Denial of Service, collateral, placeBid, bidAmount, feeAmount, Stewardship License, totalCollateralAmount, bidder, protocol, functionality, bidding process, smart contract, Ethereum, manual review, hardhat, test case

---

sammy

medium

# Auction fails if the \u0027Honorarium Rate\u0027 is 0%

## Summary
The Honorarium Rate is the required percentage of a winning Auction Pitch bid that the Steward makes to the Creator Circle at the beginning of each Stewardship Cycle. 

\u0060$$ Winning Bid * Honorarium Rate = Periodic Honorarium $$\u0060

To mimic the dynamics of private ownership, the _Creator Circle_ may choose a 0% _Honorarium Rate_. However, doing so breaks the functionality of the protocol.
## Vulnerability Detail
To place a bid, a user must call the [\u0060placeBid\u0060](https://github.com/RadicalxChange/pco-art/blob/4acd6b06840028ba616b6200439ce0d6aa1e6276/contracts/auction/facets/EnglishPeriodicAuctionFacet.sol#L153) function in \u0060EnglishPeriodicAuctionFacet.sol\u0060 and deposit collateral(\u0060collateralAmount\u0060) equal to \u0060bidAmount + feeAmount\u0060. The \u0060feeAmount\u0060 here represents the _Honorarium Rate_ mentioned above. 
The \u0060placeBid\u0060 function calls the [\u0060_placeBid\u0060](https://github.com/RadicalxChange/pco-art/blob/4acd6b06840028ba616b6200439ce0d6aa1e6276/contracts/auction/EnglishPeriodicAuctionInternal.sol#L286) internal function in \u0060EnglishPeriodicAuctionInternal.sol\u0060 which calculates the  \u0060totalCollateralAmount\u0060 as follows : 
\u0060\u0060\u0060solidity
uint256 totalCollateralAmount = bid.collateralAmount + collateralAmount;
\u0060\u0060\u0060
Here, \u0060bid.collateralAmount\u0060 is the cumulative collateral deposited by the bidder in previous bids during the current auction round(i.e, zero if no bids were placed), and \u0060collateralAmount\u0060 is the collateral to be deposited to place the bid. However the \u0060_placeBid\u0060 function requires that \u0060totalCollateralAmount\u0060 is strictly greater than \u0060bidAmount\u0060 if the bidder is not the current owner of the _Stewardship License_. This check fails when the \u0060feeAmount\u0060 is zero and this causes a _Denial of Service_ to users trying to place a bid. Even if the users try to bypass this by depositing a value slightly larger than \u0060bidAmount\u0060, the [\u0060_checkBidAmount\u0060](https://github.com/RadicalxChange/pco-art/blob/4acd6b06840028ba616b6200439ce0d6aa1e6276/contracts/auction/EnglishPeriodicAuctionInternal.sol#L338) function would still revert with \u0060\u0027Incorrect bid amount\u0027\u0060

## POC
The following test demonstrates the above-mentioned scenario :

\u0060\u0060\u0060solidity
 describe(\u0027exploit\u0027, function () {
    it(\u0027POC\u0027, async function () {
      // Auction start: Now + 100
      // Auction end: Now + 400
      const instance = await getInstance({
        auctionLengthSeconds: 300,
        initialPeriodStartTime: (await time.latest()) + 100,
        licensePeriod: 1000,
      });
      const licenseMock = await ethers.getContractAt(
        \u0027NativeStewardLicenseMock\u0027,
        instance.address,
      );

      // Mint token manually
      const steward = bidder2.address;
      await licenseMock.mintToken(steward, 0);

      // Start auction
      await time.increase(300);
        
      const bidAmount = ethers.utils.parseEther(\u00271.0\u0027);
      const feeAmount = await instance.calculateFeeFromBid(bidAmount);
      const collateralAmount = feeAmount.add(bidAmount);

      // Reverts when a user tries to place a bid
      await expect( instance
        .connect(bidder1)
        .placeBid(0, bidAmount, { value: collateralAmount })).to.be.revertedWith(\u0027EnglishPeriodicAuction: Collateral must be greater than current bid\u0027);

      
    
      const extraAmt = ethers.utils.parseEther(\u00270.1\u0027);
      const collateralAmount1 = feeAmount.add(bidAmount).add(extraAmt);
      
      // Also reverts when the user tries to deposit collateral slighty greater than bid amount
      await expect( instance
        .connect(bidder1)
        .placeBid(0, bidAmount, { value: collateralAmount1 })).to.be.revertedWith(\u0027EnglishPeriodicAuction: Incorrect bid amount\u0027);  
      
      // Only accepts a bid from the current steward
      
      await expect( instance
        .connect(bidder2)
        .placeBid(0, bidAmount, { value: 0 })).to.not.be.reverted;

    });
  });
\u0060\u0060\u0060
To run the test, copy the code above to \u0060EnglishPeriodicAuction.ts\u0060 and alter [L#68](https://github.com/RadicalxChange/pco-art/blob/4acd6b06840028ba616b6200439ce0d6aa1e6276/test/auction/EnglishPeriodicAuction.ts#L68) as follows : 
\u0060\u0060\u0060diff
-          [await owner.getAddress(), licensePeriod, 1, 10],
+          [await owner.getAddress(), licensePeriod, 0, 10],
\u0060\u0060\u0060
Run \u0060yarn run hardhat test --grep \u0027POC\u0027\u0060
## Impact
The protocol becomes dysfunctional in such a scenario as users as DOS\u0027d from placing a bid.
## Code Snippet

## Tool used

Manual Review
Hardhat

## Recommendation
Alter [EnglishPeriodicAuctionInternal.sol::L#330](https://github.com/RadicalxChange/pco-art/blob/4acd6b06840028ba616b6200439ce0d6aa1e6276/contracts/auction/EnglishPeriodicAuctionInternal.sol#L330) as follows :
\u0060\u0060\u0060diff
- totalCollateralAmount > bidAmount,
+ totalCollateralAmount >= bidAmount, 
\u0060\u0060\u0060


