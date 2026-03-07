# Issue M-21: Reserving a listing checkpoints

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** reserve, compound factor, CollectionToken, supply, protected listing, checkpoint, interest accrual, loan, collateral, burn, mint, transfer, listing, utilization ratio, NFT, borrowers, tax refund, listing fee, liquidation, market impact

---

# Issue M-19: UniswapImplementation::beforeSwap() might revert when swapping native tokens to collection tokens

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/517)  
Found by: 0xAlix2, 0xc0ffEE, ComposableSecurity, JokerStudio, alexzoid, g, h2134, zarkk01, zzykxx

UniswapImplementation::beforeSwap() performs a wrong check which can lead to swaps from native tokens to collection tokens reverting.

UniswapImplementation::beforeSwap() swaps the internally accumulated collection token fees into native tokens when:
1. The hook accumulated at least 1 wei of fees in collection tokens
2. An user is swapping native tokens for collection tokens

When the swap is performed by specifying the exact amount of native tokens to pay (i.e., amountSpecified < 0), the protocol should allow the internal swap only when the amount of native tokens being paid is enough to convert all of the accumulated collection token fees. The protocol however does this incorrectly, as the code checks the amountSpecified against tokenOut instead of ethIn:

\u0060\u0060\u0060solidity
if (params.amountSpecified >= 0) {
    ...
} else {
    (, ethIn, tokenOut, ) = SwapMath.computeSwapStep({
        sqrtPriceCurrentX96: sqrtPriceX96,
        sqrtPriceTargetX96: params.sqrtPriceLimitX96,
        liquidity: poolManager.getLiquidity(poolId),
        amountRemaining: int(pendingPoolFees.amount1),
        feePips: 0
    });
}

if (tokenOut <= uint(-params.amountSpecified)) {
    // Update our hook delta to reduce the upcoming swap amount to show that we have
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// already spent some of the ETH and received some of the underlying ERC20.
// Specified = exact input (ETH)
// Unspecified = token1
beforeSwapDelta_ = toBeforeSwapDelta(ethIn.toInt128(),
               -tokenOut.toInt128());
} else {
    ethIn = tokenOut = 0;
}
\u0060\u0060\u0060

This results in the \u0060UniswapImplementation::beforeSwap()\u0060 reverting in the situations explained in internal pre-conditions below.

1. User is swapping native tokens for collection tokens
2. The hook accumulated at least 1 wei of collection tokens in fees
3. \u0060tokenOut\u0060 is lower than \u0060uint(-params.amountSpecified)\u0060 and \u0060ethIn\u0060 is bigger than \u0060uint(-params.amountSpecified)\u0060

No response

No response

All swaps that follow the internal pre-conditions will revert.

To copy-paste in \u0060UniswapImplementation.t.sol\u0060:
\u0060\u0060\u0060solidity
function test_swapFails() public {
    address alice = makeAddr("alice");
    address bob = makeAddr("bob");
    ERC721Mock erc721 = new ERC721Mock();
    CollectionToken ctoken = CollectionToken(locker.createCollection(address(erc721), \u0027ERC721\u0027, \u0027ERC\u0027, 0));
}
\u0060\u0060\u0060
## APPROVALS

- Alice approvals
\u0060\u0060\u0060solidity
vm.startPrank(alice);
erc721.setApprovalForAll(address(locker), true);
ctoken.approve(address(poolSwap), type(uint256).max);
ctoken.approve(address(uniswapImplementation), type(uint256).max);
vm.stopPrank();
_approveNativeToken(alice, address(locker), type(uint).max);
_approveNativeToken(alice, address(poolManager), type(uint).max);
_approveNativeToken(alice, address(poolSwap), type(uint).max);
\u0060\u0060\u0060

- Bob approvals
\u0060\u0060\u0060solidity
vm.startPrank(bob);
erc721.setApprovalForAll(address(locker), true);
ctoken.approve(address(uniswapImplementation), type(uint256).max);
ctoken.approve(address(poolSwap), type(uint256).max);
vm.stopPrank();
_approveNativeToken(bob, address(locker), type(uint).max);
_approveNativeToken(bob, address(poolManager), type(uint).max);
_approveNativeToken(bob, address(poolSwap), type(uint).max);
\u0060\u0060\u0060
## MINT NFTs

- Mint 10 tokens to Alice
\u0060\u0060\u0060solidity
uint[] memory _tokenIds = new uint[](10);
for (uint i; i < 10; ++i) {
    erc721.mint(alice, i);
    _tokenIds[i] = i;
}
\u0060\u0060\u0060

- Mint an extra token to Alice
\u0060\u0060\u0060solidity
uint[] memory _tokenIdToDepositAlice = new uint[](1);
erc721.mint(alice, 10);
_tokenIdToDepositAlice[0] = 10;
\u0060\u0060\u0060
## [ALICE] COLLECTION INITIALIZATION + LIQUIDITY PROVISION

- alice initializes a collection and adds liquidity: 1e19 NATIVE + 1e19 CTOKEN
\u0060\u0060\u0060solidity
uint256 initialNativeLiquidity = 1e19;
_dealNativeToken(alice, initialNativeLiquidity);
vm.startPrank(alice);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
locker.initializeCollection(address(erc721), initialNativeLiquidity, _tokenIds,
            0, SQRT_PRICE_1_1);
vm.stopPrank();
//### [ALICE] ADDING CTOKEN FEES TO HOOK
//-> alice deposits an NFT to get 1e18 CTOKEN and then deposits 1e18 CTOKENS as
            fees in the UniswapImplementation hook
vm.startPrank(alice);
locker.deposit(address(erc721), _tokenIdToDepositAlice, alice);
uniswapImplementation.depositFees(address(erc721), 0, 1e18);
vm.stopPrank();
//### [BOB] SWAP FAILS
_dealNativeToken(bob, 1e18);
//-> bob swaps \u00601e18\u0060 NATIVE tokens for CTOKENS but the swap fails
vm.startPrank(bob);
poolSwap.swap(
    PoolKey({
        currency0: Currency.wrap(address(ctoken)),
        currency1: Currency.wrap(address(WETH)),
        fee: LPFeeLibrary.DYNAMIC_FEE_FLAG,
        tickSpacing: 60,
        hooks: IHooks(address(uniswapImplementation))
    }),
    IPoolManager.SwapParams({
        zeroForOne: false,
        amountSpecified: -int(1e18),
        sqrtPriceLimitX96: (TickMath.MAX_SQRT_PRICE - 1)
    }),
    PoolSwapTest.TestSettings({
        takeClaims: false,
        settleUsingBurn: false
    }),
    \u0027\u0027
);
\u0060\u0060\u0060
Mitigation
In UniswapImplementation::beforeSwap() check against ethIn instead of tokenOut:
\u0060\u0060\u0060solidity
if (ethIn <= uint(-params.amountSpecified)) {
    // Update our hook delta to reduce the upcoming swap amount to show that we
    // have already spent some of the ETH and received some of the underlying ERC20.
    // Specified = exact input (ETH)
    // Unspecified = token1
    beforeSwapDelta_ = toBeforeSwapDelta(ethIn.toInt128(),
    -tokenOut.toInt128());
} else {
    ethIn = tokenOut = 0;
}
\u0060\u0060\u0060
## Issue M-20: User can cancel or modify Dutch auctions, compromising market integrity and user trust

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/520)  
Found by: 0xNirix  

A lack of listing type preservation during relisting can be exploited by users to modify or cancel Dutch auctions, violating core protocol principles.

In Listings.sol, there\u0027s a critical oversight in the relist function that allows bypassing restrictions on Dutch auctions and Liquidation listings. Here\u0027s a detailed walkthrough:  
The \u0060modifyListings\u0060 and \u0060cancelListings\u0060 functions have checks to prevent modification of Dutch auctions: 

- [modifyListings](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol#L312) 
- [cancelListings](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol#L430)

\u0060\u0060\u0060solidity
function modifyListings(address _collection, ModifyListing[] calldata _modifyListings, bool _payTaxWithEscrow) public nonReentrant lockerNotPaused returns (uint taxRequired_, uint refund_) {
    // ...
    if (getListingType(listing) != Enums.ListingType.LIQUID) revert InvalidListingType();
    // ...
}

function cancelListings(address _collection, uint[] memory _tokenIds, bool _payTaxWithEscrow) public lockerNotPaused {
    // ...
    if (getListingType(listing) != Enums.ListingType.LIQUID) revert CannotCancelListingType();
    // ...
}
\u0060\u0060\u0060

However, the relist function lacks these checks:
\u0060\u0060\u0060solidity
function relist(CreateListing calldata _listing, bool _payTaxWithEscrow) public
    nonReentrant lockerNotPaused {
    // Read the existing listing in a single read
    Listing memory oldListing = _listings[_collection][_tokenId];
    // Ensure the caller is not the owner of the listing
    if (oldListing.owner == msg.sender) revert CallerIsAlreadyOwner();
    // ... price difference payment logic ...
    // We can process a tax refund for the existing listing
    (uint _fees,) = _resolveListingTax(oldListing, _collection, true);
    // Validate our new listing
    _validateCreateListing(_listing);
    // Store our listing into our Listing mappings
    _listings[_collection][_tokenId] = listing;
    // Pay our required taxes
    payTaxWithEscrow(address(collectionToken), getListingTaxRequired(listing, _collection), _payTaxWithEscrow);
    // ... events ...
}
\u0060\u0060\u0060

This function allows any non-owner to relist an item, potentially changing its type from Dutch or liquidation to liquid. The attacker suffers minimal loss due to:
a) Tax refund for the old listing:
\u0060\u0060\u0060solidity
(uint _fees,) = _resolveListingTax(oldListing, _collection, true);
\u0060\u0060\u0060
b) Immediate cancellation after relisting, which refunds most of the new listing\u0027s tax:
\u0060\u0060\u0060solidity
function _resolveListingTax(Listing memory _listing, address _collection, bool _action) private returns (uint fees_, uint refund_) {
    // ...
    if (block.timestamp < _listing.created + _listing.duration) {
        refund_ = (_listing.duration - (block.timestamp - _listing.created)) * taxPaid / _listing.duration;
    }
    // ...
}
\u0060\u0060\u0060

This oversight allows attackers to bypass the intended restrictions on Dutch auctions and liquidation listings, violating the core principle of auction immutability with minimal financial loss.
No response

No response

1. Attacker creates a Dutch auction or liquidation listing from Wallet A.
2. Attacker uses Wallet B to call relist, converting the Dutch auction to a Liquid listing by modifying the duration.
3. Attacker immediately cancels the new liquid listing using cancelListings at minimal cost.

The NFT holders and potential bidders suffer a loss of trust and market efficiency. The attacker gains the ability to manipulate auctions, potentially extracting value by gaming the system. This violates the core principles stated in the whitepaper like around expiry of a liquid auction - the item is immediately locked into a Dutch auction where the price falls from its current floor multiple down to the floor (1x) over a period of 4 days. However, as seen in this issue, the lock can be broken by just relisting and then cancelling. The issue affects not only Dutch auctions but also liquidation listings which can be similarly canceled or modified and is not properly handled. For example, in case a liquidation listing is cancelled, the \u0060_isLiquidation[_collection][_tokenId]\u0060 flag is not cleared causing further issues.

No response

No response
## IssueM-21: Reserving a listing checkpoints

the collection\u0027s compound Factor at an inter- mediary higher compound factor  
Source: https://github.com/sherlock-audit/2024-08-flayer-judging/issues/533  
Found by Sentryx  

When a listing is reserved (Listings#reserve()), there are multiple CollectionToken operations that affect its total Supply that take place in the following order: transfer → transfer → burn → mint → transfer → burn. After the function ends execution the total Supply of the CollectionToken itself remains unchanged compared to before the call to the function, but in the middle of its execution a protected listing is created and its compound factor is checkpointed at an intermediary state of the CollectionToken\u0027s total supply (between the first burn and the mint) that will later affect the rate of interest accrual on the loan itself in harm to all borrowers of NFTs in that collection causing them to actually accrue more interest on the loan.  

To be able to understand the issue, we must inspect what CollectionToken operations are performed throughout the execution of the reserve() function and at which point exactly the protected listing\u0027s compound Factor is checkpointed.  
(Will comment out their relevant parts of the function for brevity) https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol#L690-L759  

\u0060\u0060\u0060solidity
function reserve(address _collection, uint _tokenId, uint _collateral) public
    nonReentrant lockerNotPaused {
        // ...
        if (oldListing.owner != address(0)) {
            // We can process a tax refund for the existing listing if it isn\u0027t a
            // liquidation
            if (!_isLiquidation[_collection][_tokenId]) {
                // 1st transfer
                (uint _fees,) = _resolveListingTax(oldListing, _collection, true);
                if (_fees != 0) {
                    emit ListingFeeCaptured(_collection, _tokenId, _fees);
\u0060\u0060\u0060
\u0060\u0060\u0060
if (listingPrice > listingFloorPrice) {
    unchecked {
        // 2nd transfer
        collectionToken.transferFrom(msg.sender, oldListing.owner,
         listingPrice - listingFloorPrice);
    }
}
// ...
// 1st burn
collectionToken.burnFrom(msg.sender, _collateral * 10 **
 collectionToken.denomination());
// ...
// the protected listing is recorded in storage with the just-checkpointed
compoundFactor
// then: mint + transfer
protectedListings.createListings(createProtectedListing);
// 2nd burn
collectionToken.burn((1 ether - _collateral) * 10 **
 collectionToken.denomination());
// ...
}
Duetotheloan\u0027scompoundFactorbeingcheckpointedbeforethesecondburnof1ether-_
collateralCollectionTokens(andbeforelistingCount[listing.collection]is
incremented),thetotalSupplywillbetemporarilydecreasedwhichwillmakethe
collection\u0027s utilization ratio go up a notch due to the way it\u0027s derived and this will
eventuallybereflectedinthecheckpointedcompoundFactorforthecurrentblockand
respectively for the loan as well.
https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Pr
otectedListings.sol#L117-L156
function createListings(CreateListing[] calldata _createListings) public
 nonReentrant lockerNotPaused {
// ...
for (uint i; i < _createListings.length; ++i) {
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
if (checkpointIndex == 0) {
    // @audit Checkpoint the temporarily altered \u0060compoundFactor\u0060 due
    // to the temporary change in the CollectionToken\u0027s \u0060totalSupply\u0060.
    checkpointIndex = _createCheckpoint(listing.collection);
    assembly { tstore(checkpointKey, checkpointIndex) }
}

// @audit Store the listing with a pointer to the index of the
// inacurate checkpoint above
tokensReceived = _mapListings(listing, tokensIdsLength,
    checkpointIndex) * 10 **
    locker.collectionToken(listing.collection).denomination();

// Register our listing type
unchecked {
    listingCount[listing.collection] += tokensIdsLength;
}
\u0060\u0060\u0060

[Source Code](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L530-L571)

\u0060\u0060\u0060solidity
function _createCheckpoint(address _collection) internal returns (uint index_) {
    Checkpoint memory checkpoint = _currentCheckpoint(_collection);
    // ...
    collectionCheckpoints[_collection].push(checkpoint);
}
\u0060\u0060\u0060

_currentCheckpoint() will fetch the current utilization ratio which is temporarily higher and will calculate the current checkpoint\u0027s compoundedFactor with it (which the newly created loan will reference thereafter).

[Source Code](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L580-L596)

\u0060\u0060\u0060solidity
function _currentCheckpoint(address _collection) internal view returns
    (Checkpoint memory checkpoint_) {
    // ...
    (, uint _utilizationRate) = utilizationRate(_collection);
}
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
checkpoint_ = Checkpoint({
    compoundedFactor: locker.taxCalculator().calculateCompoundedFactor({
        _previousCompoundedFactor: previousCheckpoint.compoundedFactor,
        _utilizationRate: _utilizationRate,
        _timePeriod: block.timestamp - previousCheckpoint.timestamp
    }),
    timestamp: block.timestamp
});
\u0060\u0060\u0060

[Source Code](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L261-L276)

\u0060\u0060\u0060javascript
function utilizationRate(address _collection) public view virtual returns (uint listingsOfType_, uint utilizationRate_) {
    listingsOfType_ = listingCount[_collection];
    // ...
    if (listingsOfType_ != 0) {
        // ...
        uint totalSupply = collectionToken.totalSupply();
        if (totalSupply != 0) {
            utilizationRate_ = (listingsOfType_ * 1e36 * 10 ** collectionToken.denomination()) / totalSupply;
        }
    }
}
\u0060\u0060\u0060

None

None

No attack required.

Knowing how a collection\u0027s utilization rate is calculated we can clearly see the impact it\u0027ll have on the checkpointed compounded factor for a block:

\u0060\u0060\u0060
collection protected listings count ∗ 1e36 ∗ 10denomination
utilizationRate =
                    CTtotalsupply
\u0060\u0060\u0060

The less Collection Token (CT) total supply, the higher the utilization rate for a constant collection\u0027s protected listings count. The higher the utilization rate, the higher the compounded Factor will be for the current checkpoint and for the protected position created (the loan).

\u0060\u0060\u0060
compoundedFactor = previousCompoundFactor ∗ (1e18+(perSecondRate /1000∗_timePeriod))
\u0060\u0060\u0060

Where: 
\u0060\u0060\u0060
perSecondRate = interestRate∗1e18
                365∗24∗60∗60
\u0060\u0060\u0060
\u0060\u0060\u0060
interestRate = 200 + utilizationRate ∗ 600 – When utilizationRate < 0.8e18 (UTILIZATION_KINK) 
OR 
interestRate = ((utilizationRate − 200) ∗ (100 − 8) + 8) ∗ 100 – When utilizationRate > 0.8e18(UTILIZATION_KINK)
\u0060\u0060\u0060

As a result (and with the help of another issue that has a different root cause and a fix which is submitted separately) the loan will end up checkpointing a temporarily higher compounded Factor and thus will compound more interest in the future than it\u0027s correct to. It\u0027s important to know that no matter how many times createCheckpoint() is called after the call to reserve(), the compound Factor for the current block\u0027s checkpoint will remain as. But even without that, there is no guarantee that even if it worked correctly, there\u0027d be any calls that\u0027d record a new checkpoint for that collection.


1. Bob lists an NFT for sale. The duration and the floor Multiple of the listing are irrelevant in this case.
2. John sees the NFT and wants to reserve it, putting up 0.9e18 amount of Collection Tokens as collateral.
3. The collateral is burned.
4. The collection\u0027s compound Factor for the current block is checkpointed.

Let\u0027s say there is only one protected listing prior to John\u0027s call to reserve() and its owner has put up 0.5e18 Collection Tokens as collateral.

\u0060\u0060\u0060
old collection token total supply = 5e18 
collection protected listings count = 1
\u0060\u0060\u0060

We can now calculate the utilization rate the way it\u0027s calculated right now:

\u0060\u0060\u0060
collection protected listings count ∗ 1e36 ∗ 10denomination
utilizationRate =
                     CTtotalsupply
\u0060\u0060\u0060
‘utilizationRate = 5e18 − 0.9e18‘ (assuming denomination is 0)  
utilizationRate = 1e36 = 243902439024390243  
4.1e18  

Wecannowproceedtocalculatethewrongcompoundedfactor:  
‘compoundedFactor = previousCompoundFactor ∗ (1e18+(perSecondRate /1000∗_timePeriod))‘  
Where: previousCompoundFactor = 1e18  
interestRate = 200 + utilizationRate ∗ 600 = 200 + 243902439024390243 ∗ 600 = 382 (3.82 %)  
perSecondRate = interestRate ∗ 1e18 = 382∗1e18 = 12113140537798  
timePeriod = 432000 (5 days) (last checkpoint was made 5 days ago)  
compoundedFactor = 1e18∗(1e18+(12113140537798/1000∗432000))  
compoundedFactor = 1e18∗1005232876711984000 = 1005232876711984000(Thiswillbethe final compoundfactorforthecheckpointforthecurrentblock)  

Thecorrectutilizationratehowever,shouldbecalculatedwithacurrentcollectiontoken total supply of 5e18 at the time when reserve() is called, which will result in:  
‘utilizationRate = collection protected listings count ∗ 1e36 ∗ 10 =1∗1e36 = 200000000000000000‘  
Thedifferencewiththewrongutilizationrateis‘43902439024390243‘or~‘0.439e18‘whichis ~18%smallerthanthewronglycomputedutilizationrate).  
Fromthenontheinterestratewillbelowerandthusthefinalandcorrectcompounded factorcomesoutat1004794520547808000(willnotrepeattheformulasforbrevity)whichis around0.05%smallerthanthewronglyrecordedcompoundedfactor. The%mightnot bebigbutrememberthatthiserrorwillbebiggerwiththelongertimeperiodbetween thetwocheckpointsandwillbecompoundingwitheverycalltoreserve().  

5. AprotectedlistingiscreatedforthereservedNFT,referencingthecurrent checkpoint.  
6. Whenthecollection\u0027scompoundFactorischeckpointedthenexttime,thefinalcompo undFactorproductwillbetimesgreaterduetothenowincrementedcollection\u0027s protectedlistingscountandtheincreased(backtothevaluebeforethereserve wasmade)totalsupplyofCollectionTokens.  

Letssayafteranother5daysthecreateCheckpoint()methodiscalledforthatcollection withoutanychangesintheCollectionTokentotalsupplyorthecollection\u0027sprotected listings count. The math will remain mostly the same with little updates and we will first runthemathwiththewronglycomputedpreviousCompoundedFactorandthenwillcompare it to the correct one.
collection token total supply = 5e18 (because the burned _collateral amount of CollectionTokens has been essentially minted to the ProtectedListings contract hence as we said reserve() does not affect the total supply after the function is executed).  
collection protected listings count = 2 (now 1 more due to the created protected listing)  
previousCompoundedFactor = 1005232876711984000 (the wrong one, as we derived it a bit earlier)  
utilizationRate =  
\u0060\u0060\u0060
CTtotalsupply
0
utilizationRate = 2 ∗ 1e36 ∗ 10 = 2e36 = 0.4e18
          5e18          5e18
\u0060\u0060\u0060  
interestRate = 200 + utilizationRate ∗ 600 = 200 + 0.4e18 ∗ 600 = 500 (5 %)  
\u0060\u0060\u0060
0.8e18
perSecondRate = interestRate ∗ 1e18 = 500∗1e18 = 15854895991882
              365∗24∗60∗60            31 536 000
\u0060\u0060\u0060  
timePeriod = 432000 (5 days) (the previous checkpoint was made 5 days ago)  
compoundedFactor = 1005232876711984000∗(1e18+(15854895991882/1000∗432000)  
\u0060\u0060\u0060
1e18
compoundedFactor = 1005232876711984000∗1006849315068112000 = 1012118033401408964 or
\u0060\u0060\u0060
0.68% accrued interest for that collection for the past 5 days.  
Now let\u0027s run the math but compounding on top of the correct compound factor:  
\u0060\u0060\u0060
compoundedFactor = 1004794520547808000∗1006849315068112000 = 1011676674797752473 or
\u0060\u0060\u0060
0.21% of interest should\u0027ve been accrued for that collection for the past 5 days, instead of 0.68% which in this case is 3 times bigger.  

Just burn the _collateral amount after the protected listing is created. This way the compoundedFactor will be calculated and checkpointed properly.  

\u0060\u0060\u0060
diff --git a/flayer/src/contracts/Listings.sol b/flayer/src/contracts/Listings.sol
index eb39e7a..c8eac4d 100644
--- a/flayer/src/contracts/Listings.sol
+++ b/flayer/src/contracts/Listings.sol
@@ -725,10 +725,6 @@ contract Listings is IListings, Ownable, ReentrancyGuard,
                              unchecked { listingCount[_collection] -= 1; }
                         }
 -          // Burn the tokens that the user provided as collateral, as we will have
 -          // from {ProtectedListings}.
 -          collectionToken.burnFrom(msg.sender, _collateral * 10 **
 -          collectionToken.denomination());
 -
                         // We can now pull in the tokens from the Locker
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
locker.withdrawToken(_collection, _tokenId, address(this));
IERC721(_collection).approve(address(protectedListings), _tokenId);
// Create our listing, receiving the ERC20 into this contract
protectedListings.createListings(createProtectedListing);
// Burn the tokens that the user provided as collateral, as we will have
// it minted from {ProtectedListings}.
collectionToken.burnFrom(msg.sender, _collateral * 10 ** collectionToken.denomination());
// We should now have received the non-collateral assets, which we will
// burn in addition to the amount that the user sent us.
collectionToken.burn((1 ether - _collateral) * 10 ** collectionToken.denomination());
\u0060\u0060\u0060
## Issue M-22: FTokens are burned after quorumVotes are recorded making a portion of the shares unclaimable

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/610)  
Found by: g, zarkk01  


params.quorumVotes is larger than it should because Locker\u0027s collection tokens are burned after quorumVotes is recorded.

\u0060\u0060\u0060solidity
uint newQuorum = params.collectionToken.totalSupply() * SHUTDOWN_QUORUM_PERCENT /
    ONE_HUNDRED_PERCENT;
if (params.quorumVotes != newQuorum) {
    params.quorumVotes = uint88(newQuorum);
}
// Lockdown the collection to prevent any new interaction
// @audit sunsetCollection() burns the Locker\u0027s tokens decreasing the
// \u0060totalSupply\u0060. If this was called before
// \u0060params.quorumVotes\u0060 was set, the totalSupply() would be smaller and each vote
// would get more share of the ETH profits.
locker.sunsetCollection(_collection);
\u0060\u0060\u0060

When a collection is shutdown, its NFTs are sold off via Dutch auction in a SudoSwap pool. This sale\u0027s ETH profits are distributed to the holders of the collection token (fToken). The claim amount is calculated with availableClaim * claimableVotes / params.quorumVotes * 2. The higher params.quorumVotes, the lower the claim amount for each vote.


params.quorumVotes is larger than it should because Locker\u0027s collection tokens are burned after quorumVotes is recorded.


1. At least 50% of Holders have voted for a collection to shut down.
