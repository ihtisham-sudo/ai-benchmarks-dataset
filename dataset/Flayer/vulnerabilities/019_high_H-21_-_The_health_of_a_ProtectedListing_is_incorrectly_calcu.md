# H-21 - The health of a ProtectedListing is incorrectly calculated if the token Taken has been changed through ProtectedListings::adjustPosition()

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** ProtectedListing, adjustPosition, getProtectedListingHealth, debt, compound factor, liquidation, tokenTaken, interest, unfair liquidation, user debt, compounding, interest calculation, position adjustment, liquidation risk, user funds, debt inflation, financial loss, smart contract, vulnerability, audit

---

# Issue flow:

1. Figure out the tick where the donated fee will go in according to the @notice comment above on IPoolManager.donate.
2. And provide the in-range liquidity so heavy (like 100x than available in the whole range of that pool).
3. Then do the liquidate ProtectedListing, cancelListing, modifyListings, fillListings, Reserve and Relist actions that donate fees worth doing this sandwich.
4. Then trigger a fee donation happening on before swap hook and then remove the provided liquidity in the first step.

You don\u0027t need to front run other user\u0027s actions, just do this sandwiching whenever a liquidation of someone\u0027s listing happens. And you can also recover the paid tax/fees of your listings by this MEV. Or even better if chain allows to have public mempool, then every user\u0027s action is sandwichable.

[UniswapImplementation.sol](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/flayer/src/contracts/implementation/UniswapImplementation.sol#L335-L345)

[BaseImplementation.sol](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/flayer/src/contracts/implementation/BaseImplementation.sol#L58-L62)

\u0060\u0060\u0060solidity
/// Prevents fee distribution to Uniswap V4 pools below a certain threshold:
/// - Saves wasted calls that would distribute less ETH than gas spent
/// - Prevents targeted distribution to sandwich rewards
uint public donateThresholdMin = 0.001 ether;
>> uint public donateThresholdMax = 0.1 ether;
function _distributeFees(PoolKey memory _poolKey) internal {
    ---- SNIP ----
    if (poolFee > 0) {
        // Determine whether the currency is flipped to determine which is the donation side
        (uint amount0, uint amount1) = poolParams.currencyFlipped ?
            (uint(0), poolFee) : (poolFee, uint(0));
\u0060\u0060\u0060

LossoffundstotheLPs. ThefeestheyabouttogetduetoLP,canbesandwichedand extracted. Sohighseverity,andabovemediumlikelihoodeveninthechansthatdoesn\u0027t havemempool. So,highseverity.


- [UniswapImplementation.sol](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/flayer/src/contracts/implementation/UniswapImplementation.sol#L335-L345)
- [IPoolManager.sol](https://github.com/Uniswap/v4-core/blob/18b223cab19dc778d9d287a82d29fee3e99162b0/src/interfaces/IPoolManager.sol#L167-L172)
- [BaseImplementation.sol](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/flayer/src/contracts/implementation/BaseImplementation.sol#L58-L62)


ManualReview

Introduce a new way to track how much is donated on this block and limit it on every \u0060donate\u0060 call. Example, allow only 0.1 ether per block.
## Issue H-21: The health of a ProtectedListing is incorrectly calculated if the token Taken has been changed through ProtectedListings::adjustPosition().
Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/689)  
Found by: 0x73696d616f, 0xNirix, ZeroTrust, dimulski, t.aksoy, zarkk01  

ProtectedListings::adjustPosition() will change the token Taken but after this, ProtectedListings::getProtectedListingHealth() will assume that the token Taken has been the same as the starting ones and will incorrectly compound them.

A user can create a Protected Listing by calling ProtectedListings::createPosition(), deposit his token and take back an amount token Take as debt. This amount is supposed to be compounded throughout the time depending on the newest compound factor and the compound factor when the position was created. However, when the user calls ProtectedListings::adjustPosition() and takes some more debt, this new debt will be assumed to be there from the start and it will be compounded as such in ProtectedListings::getProtectedListingHealth() while this is not the case and it will be compounded from the moment it got taken. 

Let\u0027s have a look on ProtectedListings::adjustPosition():
\u0060\u0060\u0060solidity
function adjustPosition(address _collection, uint _tokenId, int _amount) public lockerNotPaused {
    // ...
    // Get the current debt of the position
    int debt = getProtectedListingHealth(_collection, _tokenId);
    // ...
    // Check if we are decreasing debt
    if (_amount < 0) {
        // ...
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Update the struct to reflect the new tokenTaken, protecting from
_protectedListings[_collection][_tokenId].tokenTaken -=
    uint96(absAmount);
}

// Otherwise, the user is increasing their debt to take more token
else {
    // ...
    // Update the struct to reflect the new tokenTaken, protecting from
    _protectedListings[_collection][_tokenId].tokenTaken +=
        uint96(absAmount);
}
// ...
}
\u0060\u0060\u0060

Link to code

As we can see, this function just increases or decreases the tokenTaken of this Protected Listings meaning the debt that the owner should repay. Now, if we see the Protected Listings::getProtectedListingHealth(), we will understand that function just takes the tokenTaken and compounds it without caring when this tokenTaken increased or decreased:

\u0060\u0060\u0060solidity
function getProtectedListingHealth(address _collection, uint _tokenId) public
    view listingExists(_collection, _tokenId) returns (int) {
    // So we start at a whole token, minus: the keeper fee, the amount of
    // tokens borrowed
    // and the amount of collateral based on the protected tax.
    return int(MAX_PROTECTED_TOKEN_AMOUNT) - int(unlockPrice(_collection,
        _tokenId));
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function unlockPrice(address _collection, uint _tokenId) public view returns
    (uint unlockPrice_) {
    // Get the information relating to the protected listing
    ProtectedListing memory listing = _protectedListings[_collection][_tokenId];
    // Calculate the final amount using the compounded factors and principle
    unlockPrice_ = locker.taxCalculator().compound({
        _principle: listing.tokenTaken,
        _initialCheckpoint:
            collectionCheckpoints[_collection][listing.checkpoint],
        _currentCheckpoint: _currentCheckpoint(_collection)
    });
}
\u0060\u0060\u0060
Link to code

So, it will take this tokenTaken and it will compound it from the start of the ProtectedListing until now, while it shouldn\u0027t be the case since some debt may have been added later (through ProtectedListings::adjustPosition()) and in this way this amount must be compounded from the moment it got taken until now, not from the start.

1. User creates a ProtectedListing through ProtectedListings::createListings().

1. User wants to take some debt on his ProtectedListing.

1. Firstly, user calls ProtectedListings::createListings() and creates a ProtectedListing with tokenTaken and expecting them to compound.
2. After some time and the initial tokenTaken have been compounded a bit, user decides to take some more debt and increase tokenTaken and calls ProtectedListings::adjustListing() to take x more debt.
3. Now, ProtectedListings::getProtectedListingHealth() shows that the x more debt is compounded like it was taken from the very start of the ProtectedListing creation and in this way his debt is unfairly more inflated.

The impact of this serious vulnerability is that the user is being in more debt than what he should have been, since he accrues interest for a period that he had not actually taken that debt. In this way, while he expects his tokenTaken to be increased by x amount (as it would be fairly happen), he sees his debt to be inflated by x compounded. This can cause instant and unfair liquidations and loss of funds for users unfairly taken into more debt.

No PoC needed.

To mitigate this vulnerability successfully, consider updating the checkpoints of the ProtectedListing whenever an adjustment is happening in the position, so the debt to be compounded correctly.
## Issue H-22: reserve() doesn\u0027t delete the _isLiquidation mapping, causing tax loss for owner in future

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/698)  
Found by: 0x37, BADROBINX, BugPull, Ollam, araj, cawfree, h2134, kuprum, utsav, zzykxx

\u0060reserve()\u0060 doesn\u0027t delete the \u0060_isLiquidation\u0060 mapping, causing tax loss for owner in future.

When a user reserves a tokenId, it doesn\u0027t delete the \u0060_isLiquidation\u0060 mapping.

\u0060\u0060\u0060solidity
function reserve(address _collection, uint _tokenId, uint _collateral) public
    nonReentrant lockerNotPaused {
    //
    // Check if the listing is a floor item and process additional logic if
    // there was an owner (meaning it was not floor, so liquid or dutch).
    if (oldListing.owner != address(0)) {
        // We can process a tax refund for the existing listing if it isn\u0027t a
        // liquidation
        if (!_isLiquidation[_collection][_tokenId]) {
            (uint _fees,) = _resolveListingTax(oldListing, _collection, true);
            if (_fees != 0) {
                emit ListingFeeCaptured(_collection, _tokenId, _fees);
            }
        }
        // If the floor multiple of the original listings is different, then
        // this needs to be paid to the original owner of the listing.
        uint listingFloorPrice = 1 ether * 10 ** collectionToken.denomination();
        if (listingPrice > listingFloorPrice) {
            unchecked {
                collectionToken.transferFrom(msg.sender, oldListing.owner,
                listingPrice - listingFloorPrice);
            }
        }
    }
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
                            // Reduce the amount of listings
                            unchecked { listingCount[_collection] -= 1; }
                       }
              //
                   }
            Let\u0027s go step by step to see how this will create problem for the owner:
                1. Suppose a token is liquidated, which set the _isLiquidation = true for that tokenId in
                   listing.sol
               2. A user reserved that tokenId (_isLiquidation is not deleted) & withdrew that token
                   from protectedListing.sol
               3. He listed that tokenId in listing.sol paying tax amount.
               4. Now, if that tokenId is filled then owner should get tax refund amount (if any) but
                   will not receive due to _isLiquidation = true for that tokenId.
               function _fillListing(address _collection, address _collectionToken, uint
               →
              ֒    _tokenId) private {
              //
                       if (_listings[_collection][_tokenId].owner != address(0)) {
                            // Check if there is collateral on the listing, as this we bypass fees
              ֒→   and refunds
                            if (!_isLiquidation[_collection][_tokenId]) {
                                 // Find the amount of prepaid tax from current timestamp to prepaid
              ֒→   timestamp
                                 // and refund unused gas to the user.
              >                   (uint fee, uint refund) =
              ֒→   _resolveListingTax(_listings[_collection][_tokenId], _collection, false);
                                 emit ListingFeeCaptured(_collection, _tokenId, fee);
              //
                   }
            Impact
            Lose of tax amount for the user
            CodeSnippet
            https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Lis
            tings.sol#L501C12-L510C18
            https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol#L690C4-L759C6
\u0060\u0060\u0060
Manual Review

Delete the \u0060isLiquidation\u0060 mapping in \u0060reserve()\u0060
## Issue H-23: Lister is overpaying during the cancel of his listing on Listings::cancelListings()

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/705)  
Found by: 0x73696d616f, almurhasan, zarkk01  

Lister unfairly double pays the tax used while he is cancelling his listing through Listings::cancelListings().

When a user is creating his listing through Listings::createListings(), he is paying upfront the tax that is expected to be used for the whole duration of the listing. However, if he decides to cancel the listing after some time calling Listings::cancelListings(), he will find himself paying again the portion of the tax that has been used until this point. Let\u0027s see the Listings::cancelListings():

\u0060\u0060\u0060solidity
function cancelListings(address _collection, uint[] memory _tokenIds, bool _payTaxWithEscrow) public lockerNotPaused {
    uint fees;
    uint refund;
    for (uint i; i < _tokenIds.length; ++i) {
        uint _tokenId = _tokenIds[i];
        // Read the listing in a single read
        Listing memory listing = _listings[_collection][_tokenId];
        // Ensure the caller is the owner of the listing
        if (listing.owner != msg.sender) revert CallerIsNotOwner(listing.owner);
        // We cannot allow a dutch listing to be cancelled. This will also
        // check that a liquid listing has not expired, as it will instantly change to a dutch listing type.
        Enums.ListingType listingType = getListingType(listing);
        if (listingType != Enums.ListingType.LIQUID) revert CannotCancelListingType();
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Find the amount of prepaid tax from current timestamp to prepaid
// and refund unused gas to the user.
(uint _fees, uint _refund) = _resolveListingTax(listing, _collection, false);
emit ListingFeeCaptured(_collection, _tokenId, _fees);
fees += _fees;
refund += _refund;
// Delete the listing objects
delete _listings[_collection][_tokenId];
// Transfer the listing ERC721 back to the user
locker.withdrawToken(_collection, _tokenId, msg.sender);
// cache
ICollectionToken collectionToken = locker.collectionToken(_collection);
// Burn the ERC20 token that would have been given to the user when it was
uint requiredAmount = ((1 ether * _tokenIds.length) * 10 ** collectionToken.denomination()) - refund;
payTaxWithEscrow(address(collectionToken), requiredAmount, _payTaxWithEscrow);
collectionToken.burn(requiredAmount + refund);
// ...
\u0060\u0060\u0060

Link to code

As we can see, user is expected to return back the whole 1e18 - refund. It helps to remember that when he created the listing he “took” 1e18 - TAX where, now, TAX = refund + fees. So the user is expected to give back to the protocol 1e18 - refund while he got 1e18 - refund - fees. The difference of what he got at the start and what he is expected to return now:

whatHeGot - whatHeMustReturn = (1e18 - refund - fees) - (1e18 - refund) = -fees

So, now the user has to get out of his pocket and pay again for the fees while, technically, he has paid for them in the start by never taking them. Furthermore, in this way, as we can see from this line, the protocol burns the whole 1e18 without considering the tax that got actually used and shouldn\u0027t be burned as it will be deposited to the Uniswap V4 Implementation.
collectionToken.burn(requiredAmount + refund);

1. User creates a listing from Listings::createListings().

1. User wants to cancel his listing by Listings::cancelListings().

1. User creates a listing from Listings::createListings() and takes back as collectionTokens -> 1e18-prepaidTax.
2. Some time passes by.
3. User wants to cancel the listing by calling Listings::cancelListings() and he has to give back 1e18-unusedTax. This means that he has to give also the usedTax amount.

The impact of this serious vulnerability is that the user is forced to double pay the tax that has been used for the duration that his listing was up. He, firstly, paid for it by not taking it and now, when he cancels the listing, he has to pay it again out of his own pocket. This results in unfair loss of funds for whoever tries to cancel his listing.

No PoC needed.

To mitigate this vulnerability successfully, consider not requiring user to return the fee variable as well:
\u0060\u0060\u0060solidity
function cancelListings(address _collection, uint[] memory _tokenIds, bool _payTaxWithEscrow) public lockerNotPaused {
    uint fees;
    uint refund;
    for (uint i; i < _tokenIds.length; ++i) {
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// ...
}
                     // cache
                     ICollectionToken collectionToken = locker.collectionToken(_collection);
                     // Burn the ERC20 token that would have been given to the user when it was
                     // initially created
                     uint requiredAmount = ((1 ether * _tokenIds.length) * 10 **
                     collectionToken.denomination()) - refund - fees;
                     payTaxWithEscrow(address(collectionToken), requiredAmount,
                     _payTaxWithEscrow);
                     collectionToken.burn(requiredAmount + refund);
                     // ...
\u0060\u0060\u0060
## Issue H-24: Incorrect index handling in checkpoint creation leads to incorrect initial checkpoint retrieval and potential DoS

Source: [https://github.com/sherlock-audit/2024-08-flayer-judging/issues/732](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/732)  
Found by: 0x37, ComposableSecurity, Ironsidesec, KungFuPanda, McToady, Ollam, Tendency, blockchain555, dany.armstrong90, g, h2134, heeze, merlinboii, stuart_the_minion, zzykxx

In the current implementation, when multiple listings are created for the same collection at the same timestamp, the existing checkpoint is updated, and no new checkpoint is pushed. However, the function incorrectly returns the wrong index for this case, leading to incorrect index referencing during subsequent listing creations.

When a checkpoint is created at the same timestamp, the existing checkpoint is updated, and no new checkpoint is pushed.

\u0060\u0060\u0060solidity
ProtectedListings::_createCheckpoint()
 File: ProtectedListings.sol
 530:     function _createCheckpoint(address _collection) internal returns (uint index_) {
 531:         // Determine the index that will be created
 532:         index_ = collectionCheckpoints[_collection].length;
 ---
 559:         // Get our new (current) checkpoint
 560:         Checkpoint memory checkpoint = _currentCheckpoint(_collection);
 561:
 562:         // If no time has passed in our new checkpoint, then we just need to
 563:         // utilization rate of the existing checkpoint.
 564:         if (checkpoint.timestamp == collectionCheckpoints[_collection][index_ - 1].timestamp) {
 565:             collectionCheckpoints[_collection][index_ - 1].compoundedFactor = checkpoint.compoundedFactor;
 566:             return index_;
\u0060\u0060\u0060
However, the current implementation returns the wrong index for this case, causing incorrect checkpoint handling for new listing creations, especially when creating multiple listings for the same collection with different variations.

File: ProtectedListings.sol

\u0060\u0060\u0060solidity
/**
 * 
 */
function createListings(CreateListing[] calldata _createListings) public
    nonReentrant lockerNotPaused {
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
    checkpointKey = keccak256(abi.encodePacked(\u0027checkpointIndex\u0027,
    listing.collection));
    assembly { checkpointIndex := tload(checkpointKey) }
    if (checkpointIndex == 0) {
        checkpointIndex = _createCheckpoint(listing.collection);
        assembly { tstore(checkpointKey, checkpointIndex) }
    }
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
    tokensReceived = _mapListings(listing, tokensIdsLength,
    checkpointIndex) * 10 **
    locker.collectionToken(listing.collection).denomination();
\u0060\u0060\u0060

An edge case arises when a new listing is created for a collection that has no checkpoints (collectionCheckpoints[_collection].length == 0). Assuming erc721b has no existing checkpoints (length = 0):
- Creating 2 CreateListings for the same collection (erc721b) with different variants should result in only one checkpoint being created.
- In the first iteration, it returns 0 as the index, stores it in checkpointIndex, and updates the transient storage at the checkpointKey slot. The listing is then stored with the current checkpoint.

File: ProtectedListings.sol

\u0060\u0060\u0060solidity
/**
 * 
 */
function createListings(CreateListing[] calldata _createListings) public
    nonReentrant lockerNotPaused {
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
    checkpointKey = keccak256(abi.encodePacked(\u0027checkpointIndex\u0027,
    listing.collection));
    assembly { checkpointIndex := tload(checkpointKey) }
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
if (checkpointIndex == 0) {
    checkpointIndex = _createCheckpoint(listing.collection);
    assembly { tstore(checkpointKey, checkpointIndex) }
}

tokensReceived = _mapListings(listing, tokensIdsLength,
 checkpointIndex) * 10 **
 locker.collectionToken(listing.collection).denomination();
\u0060\u0060\u0060

• In the second iteration, since checkpointKey stores 0, it is triggered again and returns 1 (the length of checkpoints) even though no new checkpoint was pushed. As a result, the second iteration incorrectly references index 1, even though the checkpoint only exists at index 0 (with a length of 1). This causes incorrect indexing for the listings.

Incorrect index returns lead to the wrong initial checkpoint index for new listings, causing incorrect checkpoint retrieval and utilization. This can result in inaccurate data and potential out-of-bound array access, leading to a Denial of Service (DoS) in

\u0060\u0060\u0060solidity
function _createCheckpoint(address _collection) internal returns (uint index_) {
    // Determine the index that will be created
    index_ = collectionCheckpoints[_collection].length;

    // Get our new (current) checkpoint
    Checkpoint memory checkpoint = _currentCheckpoint(_collection);

    // If no time has passed in our new checkpoint, then we just need to
    // update the utilization rate of the existing checkpoint.
    if (checkpoint.timestamp ==
        collectionCheckpoints[_collection][index_ - 1].timestamp) {
        collectionCheckpoints[_collection][index_ - 1].compoundedFactor
            = checkpoint.compoundedFactor;
        return index_;
    }
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
}
ProtectedListings::createListings()
File: ProtectedListings.sol
116:      */
function createListings(CreateListing[] calldata _createListings) public
    nonReentrant lockerNotPaused {
---
134:              checkpointKey = keccak256(abi.encodePacked(\u0027checkpointIndex\u0027,
    listing.collection));
135:              assembly { checkpointIndex := tload(checkpointKey) }
136:@>            if (checkpointIndex == 0) {
137:@>                checkpointIndex = _createCheckpoint(listing.collection);
138:@>                assembly { tstore(checkpointKey, checkpointIndex) }
139:              }
---
143:              tokensReceived = _mapListings(listing, tokensIdsLength,
    checkpointIndex) * 10 **
    locker.collectionToken(listing.collection).denomination();
---
156:     }
ProtectedListings::unlockPrice()
File: ProtectedListings.sol
607:     function unlockPrice(address _collection, uint _tokenId) public view
    returns (uint unlockPrice_) {
608:          // Get the information relating to the protected listing
609:          ProtectedListing memory listing =
    _protectedListings[_collection][_tokenId];
610:
611:          // Calculate the final amount using the compounded factors and
    principle amount
612:          unlockPrice_ = locker.taxCalculator().compound({
613:              _principle: listing.tokenTaken,
614:              _initialCheckpoint:
    collectionCheckpoints[_collection][listing.checkpoint],
615:              _currentCheckpoint: _currentCheckpoint(_collection)
616:          });
617:     }
\u0060\u0060\u0060
Toolused
ManualReview

Update the return value of the \u0060ProtectedListings::_createCheckpoint()\u0060 to return \u0060index_ - 1\u0060 when the checkpoint is updated at the same timestamp to ensure that subsequent listings reference the correct index.

\u0060\u0060\u0060solidity
function _createCheckpoint(address _collection) internal returns (uint index_) {
    // Determine the index that will be created
    index_ = collectionCheckpoints[_collection].length;
    // If no time has passed in our new checkpoint, then we just need to update the
    // utilization rate of the existing checkpoint.
    if (checkpoint.timestamp == collectionCheckpoints[_collection][index_ - 1].timestamp) {
        collectionCheckpoints[_collection][index_ - 1].compoundedFactor = checkpoint.compoundedFactor;
        return (index_ - 1);
    }
}
\u0060\u0060\u0060
## Issue H-25: The attacker will prevent eligible users from claiming the liquidated balance

Source: https://github.com/sherlock-audit/2024-08-flayer-judging/issues/742  
Found by: 0x37, 0xc0ffEE, BADROBINX, OpaBatyo, Ruhum, ZeroTrust, alman tare, araj, asui, dany.armstrong90, merlinboii, utsav, zzykxx

The Collection Shutdown contract has vulnerabilities allowing a malicious actor to prevent eligible users from claiming the liquidated balance after liquidation by SudoSwap.

- The contract does not prevent voting after the collection shutdown is executed and/or during the claim state, allowing malicious actors to trigger canExecute to TRUE after execution.
- The contract does not use params.collectionToken to retrieve the denomination() for validating the total supply during cancellation, which opens the door to manipulations that can bypass the checks.

1. The collection token total supply must be within a valid limit for the shutdown condition (e.g., less than or equal to MAX_SHUTDOWN_TOKENS).
2. The denomination of the collection token for the shutdown collection is greater than 0.

1. The attacker holds some portion of the collection token supply for the shutdown collection.
## Pre-condition:
1. Assume the collection token (CT) total supply is 4 CTs (4 * 1e18 * 10**denom).
2. There are 2 holders of this supply: Lewis (2 CTs) and Max (2 CTs).

## Attack:
1. Lewis notices that the collection can be shutdown and calls \u0060CollectionShutdown::start()\u0060.
   - totalSupply meets the condition <= MAX_SHUTDOWN_TOKENS.
   - params.quorumVotes = 50% of total Supply = 2 * 1e18 * 1eDenom (2 CTs).
   - Vote for Lewis is recorded.
   - The contract transfers 2 CTs of Lewis balances, and params.shutdownVotes += 2 CTs.
   - Now params.canExecute is flagged to be TRUE since params.shutdownVotes (2 CTs) >= params.quorumVotes (2 CTs).
2. Time passes, no cancellation occurs, and the owner executes the pending shutdown.
   - The NFTs are liquidated on SudoSwap.
   - params.quorumVotes remains the same as there is no change in supply.
   - The collection is sunset in the Locker, deleting \u0060collectionToken[_collection]\u0060 and \u0060collectionInitialized[_collection]\u0060.
   - params.canExecute is flagged back to FALSE.

## After some or all NFTs are sold on SudoSwap:
3. Max monitors the NFT sales and prepares for the attack.
4. Max splits their balance of CTs to his another wallet and remains holding a small amount to perform the attack.
5. Max, who never voted, calls \u0060CollectionShutdown::vote()\u0060 to flag params.canExecute back to TRUE.
   - The contract transfers small amount of CTs of Max balances.
   - Since params.shutdownVotes >= params.quorumVotes (due to Lewis\u0027s shutdown), params.canExecute is set back to TRUE.
6. Max registers the target collection again, manipulating the token\u0027s denomination via the \u0060Locker::createCollection()\u0060.
   - Max specifies a denomination lower than the previous one (e.g., previously 4, now 0).
## MaxinvokesCollectionShutdown::cancel() to remove all properties of collection

Params[_collection], including collectionParams[].availableClaim.

- The following check passes:
  
  \u0060\u0060\u0060solidity
  File: CollectionShutdown.sol
  398:          if (params.collectionToken.totalSupply() <= MAX_SHUTDOWN_TOKENS *
  ֒→ 10 ** locker.collectionToken(_collection).denomination()) {
  399:              revert InsufficientTotalSupplyToCancel();
  400:          }
  \u0060\u0060\u0060

- Since the new denomination is 0, the check becomes:

  \u0060\u0060\u0060solidity
  (4 * 1e18 * 10 ** 4) <= (4 * 1e18 * 10 ** 0): FALSE
  \u0060\u0060\u0060

Result: This check passes, allowing Max to cancel and prevent Lewis from claiming their eligible ETH from SudoSwap.


The attack allows a malicious actor to prevent legitimate token holders from claiming their eligible NFT sale proceeds from SudoSwap. This could lead to significant financial losses for affected users.


### Setup

- Update the to mint CTs token with denomination more than 0
  
  \u0060\u0060\u0060solidity
  File: CollectionShutdown.t.sol
  29:      constructor () forkBlock(19_425_694) {
  30:          // Deploy our platform contracts
  31:          _deployPlatform();
  ---
  -35:          locker.createCollection(address(erc721b), \u0027Test Collection\u0027, \u0027TEST\u0027,
  ֒→  0);
  +35:          locker.createCollection(address(erc721b), \u0027Test Collection\u0027, \u0027TEST\u0027,
  ֒→  4);
  36:
  \u0060\u0060\u0060

- Put the snippet below into the protocol test suite: flayer/test/utils/CollectionShutdown.t.sol
- Run test:

  \u0060\u0060\u0060bash
  forge test --mt test_CanBlockEligibleUsersToClaim -vvv
  \u0060\u0060\u0060
## CodedPoC

\u0060\u0060\u0060solidity
function test_CanBlockEligibleUsersToClaim() public {
    address Lewis = makeAddr("Lewis");
    address Max = makeAddr("Max");
    address MaxRecovery = makeAddr("MaxRecovery");
    // -- Before Attack --
    // Mint some tokens to our test users -> totalSupply: 4 ethers (can shutdown)
    vm.startPrank(address(locker));
    collectionToken.mint(Lewis, 2 ether * 10 ** collectionToken.denomination());
    collectionToken.mint(Max, 2 ether * 10 ** collectionToken.denomination());
    vm.stopPrank();
    // Start shutdown with their vore that has passed the threshold quorum
    vm.startPrank(Lewis);
    uint256 lewisVoteBalance = 2 ether * 10 ** collectionToken.denomination();
    collectionToken.approve(address(collectionShutdown), type(uint256).max);
    collectionShutdown.start(address(erc721b));
    assertEq(collectionShutdown.shutdownVoters(address(erc721b), address(Lewis)),
        lewisVoteBalance);
    vm.stopPrank();
    // Confirm that we can now execute
    assertCanExecute(address(erc721b), true);
    // Mint NFTs into our collection {Locker} and process the execution
    uint[] memory tokenIds = _mintTokensIntoCollection(erc721b, 3);
    collectionShutdown.execute(address(erc721b), tokenIds);
    // Confirm that the {CollectionToken} has been sunset from our {Locker}
    assertEq(address(locker.collectionToken(address(erc721b))), address(0));
    // After we have executed, we should no longer have an execute flag
    assertCanExecute(address(erc721b), false);
    // Mock the process of the Sudoswap pool liquidating the NFTs for ETH. This will
    // provide 0.5 ETH <-> 1 {CollectionToken}.
    _mockSudoswapLiquidation(SUDOSWAP_POOL, tokenIds, 2 ether);
    // Ensure that all state are SET
    ICollectionShutdown.CollectionShutdownParams memory shutdownParamsBefore =
        collectionShutdown.collectionParams(address(erc721b));
    assertEq(shutdownParamsBefore.shutdownVotes, lewisVoteBalance);
    assertEq(shutdownParamsBefore.sweeperPool, SUDOSWAP_POOL);
    assertEq(shutdownParamsBefore.quorumVotes, lewisVoteBalance);
    assertEq(shutdownParamsBefore.canExecute, false);
    assertEq(address(shutdownParamsBefore.collectionToken),
        address(collectionToken));
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
assertEq(shutdownParamsBefore.availableClaim, 2 ether);
// -- Attack --
uint256 balanceOfMaxBefore = collectionToken.balanceOf(address(Max));
uint256 amountSpendForAttack = 1;
// Transfer almost full funds to their second account and perform with small amount
vm.prank(Max);
collectionToken.transfer(address(MaxRecovery), balanceOfMaxBefore - amountSpendForAttack);
uint256 balanceOfMaxAfter = collectionToken.balanceOf(address(Max));
assertEq(balanceOfMaxAfter, amountSpendForAttack);
// Max votes even it is in the claim state to flag the \u0060canExecute\u0060 back to Trrue
vm.startPrank(Max);
collectionToken.approve(address(collectionShutdown), type(uint256).max);
collectionShutdown.vote(address(erc721b));
assertEq(collectionShutdown.shutdownVoters(address(erc721b), address(Max)), amountSpendForAttack);
vm.stopPrank();
// Confirm that Max can now flag \u0060canExecute\u0060 back to \u0060TRUE\u0060
assertCanExecute(address(erc721b), true);
// Attack to delete all varaibles track, resulting others cannot claim thier eligible ethers
vm.startPrank(Max);
locker.createCollection(address(erc721b), \u0027Test Collection\u0027, \u0027TEST\u0027, 0);
collectionShutdown.cancel(address(erc721b));
vm.stopPrank();
// Ensure that all state are DELETE
ICollectionShutdown.CollectionShutdownParams memory shutdownParamsAfter = collectionShutdown.collectionParams(address(erc721b));
assertEq(shutdownParamsAfter.shutdownVotes, 0);
assertEq(shutdownParamsAfter.sweeperPool, address(0));
assertEq(shutdownParamsAfter.quorumVotes, 0);
assertEq(shutdownParamsAfter.canExecute, false);
assertEq(address(shutdownParamsAfter.collectionToken), address(0));
assertEq(shutdownParamsAfter.availableClaim, 0);
// -- After Attack --
vm.expectRevert();
vm.prank(Lewis);
collectionShutdown.claim(address(erc721b), payable(Lewis));
\u0060\u0060\u0060
## Result

Results of running the test:

Ran 1 test for test/utils/CollectionShutdown.t.sol:CollectionShutdownTest  
[PASS] test_CanBlockEligibleUsersToClaim() (gas: 1491640)  
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 10.96s (3.48ms CPU time)  
Ran 1 test suite in 11.17s (10.96s CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)


- Add validation to prevent manipulation of the CT denomination, and restrict voting during the claim state to prevent re-triggering of params.canExecute.

\u0060\u0060\u0060solidity
function vote(address _collection) public nonReentrant whenNotPaused {
    // Ensure that we are within the shutdown window
    CollectionShutdownParams memory params = _collectionParams[_collection];
    if (params.quorumVotes == 0) revert ShutdownProccessNotStarted();
    if (params.sweeperPool != address(0)) revert ShutdownExecuted();
    _collectionParams[_collection] = _vote(_collection, params);
}
\u0060\u0060\u0060

- Update the usage of token denomination to use the token dependent on the tracked token in consistent value.

\u0060\u0060\u0060solidity
function cancel(address _collection) public whenNotPaused {
    // Ensure that the vote count has reached quorum
    CollectionShutdownParams memory params = _collectionParams[_collection];
    if (!params.canExecute) revert ShutdownNotReachedQuorum();
    // Check if the total supply has surpassed an amount of the initial required
    // total supply. This would indicate that a collection has grown since the
    // initial shutdown was triggered and could result in an unsuspected liquidation.
    if (params.collectionToken.totalSupply() <= MAX_SHUTDOWN_TOKENS * 10 ** params.collectionToken.denomination()) {
        revert InsufficientTotalSupplyToCancel();
    }
    // Remove our execution flag
    delete _collectionParams[_collection];
    emit CollectionShutdownCancelled(_collection);
}
\u0060\u0060\u0060
## Issue M-1: Previous beneficiary will not be able to claim beneficiaryFees if current beneficiary is a pool

Source: [GitHub Issue #101](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/101)  
Found by: Ragnarok, araj, cawfree, dany.armstrong90, g, h2134, utsav

Previous beneficiary will not be able to claim beneficiaryFees if current beneficiary is a pool.

Beneficiary can claim their fees using \u0060claim()\u0060, which checks if the beneficiaryIsPool and if it\u0027s true, it reverts.

\u0060\u0060\u0060solidity
function claim(address _beneficiary) public nonReentrant {
    // Ensure that the beneficiary has an amount available to claim. We don\u0027t
    // revert at this point as it could open an external protocol to DoS.
    uint amount = beneficiaryFees[_beneficiary];
    if (amount == 0) return;
    // We cannot make a direct claim if the beneficiary is a pool
    if (beneficiaryIsPool) revert BeneficiaryPoolCannotClaim();
    ...
}
\u0060\u0060\u0060

Above pointed check is a problem because it checks beneficiaryIsPool regardless of beneficiary is current beneficiary or previous beneficiary. As a result, if current beneficiary is a pool but previous beneficiary was not, then previous beneficiary will not be able to withdraw the fees as above check will revert because beneficiaryIsPool represents the status of current beneficiary.

## How this works
1. Suppose the current beneficiary A is not a pool i.e. beneficiaryIsPool=false & receives a fees of 100 e18.
Owner changed the beneficiary using \u0060setBeneficiary()\u0060 to beneficiary B, which is a pool i.e. \u0060beneficiaryIsPool=true\u0060.

Natspec of the \u0060setBeneficiary()\u0060 clearly says previous beneficiary should claim their fees, but they will not be able to claim because now \u0060beneficiaryIsPool = true\u0060, which will revert the transaction.

\u0060\u0060\u0060solidity
/**
 * Allows our beneficiary address to be updated, changing the address that will
 * be allocated fees moving forward. The old beneficiary will still have access
 * to \u0060claim\u0060 any fees that were generated whilst they were set.
 *
 * @param _beneficiary The new fee beneficiary
 * @param _isPool If the beneficiary is a Flayer pool
 */
function setBeneficiary(address _beneficiary, bool _isPool) public onlyOwner {
    beneficiary = _beneficiary;
    beneficiaryIsPool = _isPool;
    // If we are setting the beneficiary to be a Flayer pool, then we want to
    // run some additional logic to confirm that this is a valid pool by
    // checking
    // if we can match it to a corresponding {CollectionToken}.
    if (_isPool && address(locker.collectionToken(_beneficiary)) == address(0)) {
        revert BeneficiaryIsNotPool();
    }
    emit BeneficiaryUpdated(_beneficiary, _isPool);
}
\u0060\u0060\u0060

This issue is arising because \u0060beneficiaryIsPool\u0060 is the status of the current beneficiary, but \u0060claim()\u0060 can be used to claim fee by previous beneficiary also.

Previous beneficiary will not be able to claim their fees.

[BaseImplementation.sol#L171](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/implementation/BaseImplementation.sol#L171)  
[BaseImplementation.sol#L203C4-L223C6](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/implementation/BaseImplementation.sol#L203C4-L223C6)
Manual Review

Remove the above check because if the beneficiary is a pool then their fees are stored in a different mapping _poolFee not beneficiaryFees, which means any beneficiary which is a pool, will try to claim then it will revert as their beneficiaryFee will be 0 (zero)
