# M-11 - There is a logical error in the _distributeFees() function, resulting in an unfair distribution of fees.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** logical error, distributeFees, unfair distribution, fees, pool, beneficiary, LP Holders, NFT, collectionToken, poolParams, donateAmount, feeSplit, beneficiaryFee, poolFee, PoolId, poolManager, donation, emit, revert, contract

---

# Issue M-11: There is a logical error in the _distributeFees() function, resulting in an unfair distribution of fees.

Source: [GitHub Issue #328](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/328)  
Found by: ZeroTrust  

There is a logical error in the _distributeFees() function, resulting in an unfair distribution of fees.  

\u0060\u0060\u0060solidity
function _distributeFees(PoolKey memory _poolKey) internal {
    // If the pool is not initialized, we prevent this from raising an
    // exception and bricking hooks
    PoolId poolId = _poolKey.toId();
    PoolParams memory poolParams = _poolParams[poolId];
    if (!poolParams.initialized) {
        return;
    }
    // Get the amount of the native token available to donate
    uint donateAmount = _poolFees[poolId].amount0;
    // Ensure that the collection has sufficient fees available
    if (donateAmount < donateThresholdMin) {
        return;
    }
    // Reduce our available fees
    _poolFees[poolId].amount0 = 0;
    // Split the donation amount between beneficiary and LP
    (uint poolFee, uint beneficiaryFee) = feeSplit(donateAmount);
    // Make our donation to the pool, with the beneficiary amount remaining in
}
\u0060\u0060\u0060
// contract ready to be claimed.
if (poolFee > 0) {
    // Determine whether the currency is flipped to determine which is the
    // donation side
    (uint amount0, uint amount1) = poolParams.currencyFlipped ? (uint(0), poolFee) : (poolFee, uint(0));
    BalanceDelta delta = poolManager.donate(_poolKey, amount0, amount1, \u0027\u0027);
    // Check the native delta amounts that we need to transfer from the
    // contract
    if (delta.amount0() < 0) {
        _pushTokens(_poolKey.currency0, uint128(-delta.amount0()));
    }
    if (delta.amount1() < 0) {
        _pushTokens(_poolKey.currency1, uint128(-delta.amount1()));
    }
    emit PoolFeesDistributed(poolParams.collection, poolFee, 0);
}
// Check if we have beneficiary fees to distribute
if (beneficiaryFee != 0) {
    // If our beneficiary is a Flayer pool, then we make a direct call
    if (beneficiaryIsPool) {
        // As we don\u0027t want to make a transfer call, we just extrapolate
        // the required logic from the \u0060depositFees\u0060 function.
        _poolFees[_poolKeys[beneficiary].toId()].amount0 += beneficiaryFee;
        emit PoolFeesReceived(beneficiary, beneficiaryFee, 0);
    }
    // Otherwise, we can just update the escrow allocation
    else {
        beneficiaryFees[beneficiary] += beneficiaryFee;
        emit BeneficiaryFeesReceived(beneficiary, beneficiaryFee);
    }
}
If beneficiaryIsPool = true, then BaseImplementation::beneficiary is the Flayer protocol’s NFTCollection. We can also confirm this from the setBeneficiary() function.
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
emit BeneficiaryUpdated(_beneficiary, _isPool;
}

The function checks that the NFT collection must have the corresponding collectionToken.

function feeSplit(uint _amount) public view returns (uint poolFee_, uint beneficiaryFee_) {
    // If our beneficiary royalty is zero, then we can exit early and avoid reverts
    if (beneficiary == address(0) || beneficiaryRoyalty == 0) {
        return (_amount, 0);
    }
    // Calculate the split of fees, prioritising benefit to the pool
    beneficiaryFee_ = _amount * beneficiaryRoyalty / ONE_HUNDRED_PERCENT;
    poolFee_ = _amount - beneficiaryFee_;
}

In the feeSplit() function, the fees are divided into two parts: poolFee (95%) and beneficiaryFee (5%). The poolFee goes to the LP Holders of the collectionToken for some NFT, while the beneficiaryFee goes to the LP Holders of the collectionToken for the Flayer protocol’s NFT.

The root cause of the issue is that when distributeFees() is called for the collectionToken of the Flayer protocol’s NFT Collection (which we will refer to as the collectionToken of Flayer), _poolKeys[beneficiary].toId() and PoolId poolId = _poolKey.toId(); result in the same poolId. This leaves 5% of the fees undistributed, which is clearly wrong. It should distribute 100% of the fees to the current LP Holders.

According to the current logic in the code, when distributeFees() is called for the collectionToken of the Flayer protocol’s NFT, it always leaves 5% of the fees unallocated. If a user provides liquidity to the pool, 95% of the fees will be distributed to the original LP Holders. However, the new LP Holder, upon joining, will immediately gain a share of the remaining 5% of the fees. That\u0027s wrong.


The newly joined LP Holders receive an unfair portion of the fees, leading to a loss for the original LP Holders.
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/implementation/UniswapImplementation.sol#L308
\u0060\u0060\u0060

ManualReview

\u0060\u0060\u0060solidity
// Split the donation amount between beneficiary and LP
(uint poolFee, uint beneficiaryFee) = feeSplit(donateAmount);
if(poolId==_poolKeys[beneficiary].toId()){
    poolFee = donateAmount;
    beneficiaryFee = 0;
}
\u0060\u0060\u0060
## IssueM-12: A user loses funds when he modifies only price of listings.

Source: [GitHub Issue #340](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/340)

Found by: 0xHappy, Ironsidesec, Ruhum, ZeroTrust, blockchain555, dany.armstrong90, dimulski, super_jack, t.aksoy, ydlee, zarkk01

When a user modifies only the price of listings, the protocol applies more taxes than normal.

Listings.sol \u0060modifyListings()\u0060 function is as follows:

\u0060\u0060\u0060solidity
function modifyListings(address _collection, ModifyListing[] calldata _modifyListings, bool _payTaxWithEscrow) public nonReentrant lockerNotPaused returns (uint taxRequired_, uint refund_) {
    uint fees;
    for (uint i; i < _modifyListings.length; ++i) {
        // Store the listing
        ModifyListing memory params = _modifyListings[i];
        Listing storage listing = _listings[_collection][params.tokenId];
        // We can only modify liquid listings
        if (getListingType(listing) != Enums.ListingType.LIQUID) revert InvalidListingType();
        // Ensure the caller is the owner of the listing
        if (listing.owner != msg.sender) revert CallerIsNotOwner(listing.owner);
        // Check if we have no changes, as we can continue our loop early
        if (params.duration == 0 && params.floorMultiple == listing.floorMultiple) {
            continue;
        }
        // Collect tax on the existing listing
        (uint _fees, uint _refund) = _resolveListingTax(listing, _collection, false);
        emit ListingFeeCaptured(_collection, params.tokenId, _fees);
    }
}
\u0060\u0060\u0060
fees += _fees;
refund_ += _refund;
// Check if we are altering the duration of the listing
if (params.duration != 0) {
    // Ensure that the requested duration falls within our listing range
    if (params.duration < MIN_LIQUID_DURATION) revert ListingDurationBelowMin(params.duration, MIN_LIQUID_DURATION);
    if (params.duration > MAX_LIQUID_DURATION) revert ListingDurationExceedsMax(params.duration, MAX_LIQUID_DURATION);
    emit ListingExtended(_collection, params.tokenId, listing.duration, params.duration);
    listing.created = uint40(block.timestamp);
    listing.duration = params.duration;
}
// Check if the floor multiple price has been updated
if (params.floorMultiple != listing.floorMultiple) {
    // If we are creating a listing, and not performing an instant liquidation (which
    // would be done via \u0060deposit\u0060), then we need to ensure that the \u0060floorMultiple\u0060 is
    // greater than 1.
    if (params.floorMultiple <= MIN_FLOOR_MULTIPLE) revert FloorMultipleMustBeAbove100(params.floorMultiple);
    if (params.floorMultiple > MAX_FLOOR_MULTIPLE) revert FloorMultipleExceedsMax(params.floorMultiple, MAX_FLOOR_MULTIPLE);
    emit ListingFloorMultipleUpdated(_collection, params.tokenId, listing.floorMultiple, params.floorMultiple);
    listing.floorMultiple = params.floorMultiple;
}
// Get the amount of tax required for the newly extended listing
taxRequired_ += getListingTaxRequired(listing, _collection);
// cache
ICollectionToken collectionToken = locker.collectionToken(_collection);
// If our tax refund does not cover the full amount of tax required, then we will need to make an
// additional tax payment.
if (taxRequired_ > refund_) {
    unchecked {
\u0060\u0060\u0060solidity
payTaxWithEscrow(address(collectionToken), taxRequired_ - refund_,
              _payTaxWithEscrow);
}
refund_ = 0;
} else {
    unchecked {
        refund_ -= taxRequired_;
    }
}
// Check if we have fees to be paid from the listings
if (fees != 0) {
    collectionToken.approve(address(locker.implementation()), fees);
    locker.implementation().depositFees(_collection, 0, fees);
}
// If there is tax to refund after paying the new tax, then allocate it to
// the user via escrow
if (refund_ != 0) {
    _deposit(msg.sender, address(collectionToken), refund_);
}
}
It calculates refund amount on L323 through _resolveListingTax().
function _resolveListingTax(Listing memory _listing, address _collection, bool
_action) private returns (uint fees_, uint refund_) {
// If we have been passed a Floor item as the listing, then no tax should
// be handled
if (_listing.owner == address(0)) {
    return (fees_, refund_);
}
// Get the amount of tax in total that will have been paid for this listing
uint taxPaid = getListingTaxRequired(_listing, _collection);
if (taxPaid == 0) {
    return (fees_, refund_);
}
// Get the amount of tax to be refunded. If the listing has already ended
// then no refund will be offered.
if (block.timestamp < _listing.created + _listing.duration) {
    refund_ = (_listing.duration - (block.timestamp - _listing.created)) *
    taxPaid / _listing.duration;
}
...
\u0060\u0060\u0060
As we can see on L933, refund amount is calculated according to remained time. If a user modifies with \u0060params.duration == 0\u0060, \u0060listing.created\u0060 is not updated. But on L355, the protocol applies full tax for whole duration. This is wrong.


The protocol applies more tax than normal.


[Code Snippet](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol#L303-L384)


Manual Review


\u0060Listings.sol#modifyListings()\u0060 function has to be modified as follows:

\u0060\u0060\u0060solidity
function modifyListings(address _collection, ModifyListing[] calldata _modifyListings, bool _payTaxWithEscrow) public nonReentrant lockerNotPaused returns (uint taxRequired_, uint refund_) {
    uint fees;
    for (uint i; i < _modifyListings.length; ++i) {
        // Store the listing
        ModifyListing memory params = _modifyListings[i];
        Listing storage listing = _listings[_collection][params.tokenId];
        ...
        // Check if we are altering the duration of the listing
        if (params.duration != 0) {
            // Ensure that the requested duration falls within our listing range
            if (params.duration < MIN_LIQUID_DURATION) revert ListingDurationBelowMin(params.duration, MIN_LIQUID_DURATION);
            if (params.duration > MAX_LIQUID_DURATION) revert ListingDurationExceedsMax(params.duration, MAX_LIQUID_DURATION);
            emit ListingExtended(_collection, params.tokenId, listing.duration, params.duration);
            listing.created = uint40(block.timestamp);
        }
    }
}
\u0060\u0060\u0060
listing.duration = params.duration;
listing.created = uint40(block.timestamp);
// Check if the floor multiple price has been updated
if (params.floorMultiple != listing.floorMultiple) {
    // If we are creating a listing, and not performing an instant
    // liquidation (which
    // would be done via \u0060deposit\u0060), then we need to ensure that the
    // \u0060floorMultiple\u0060 is
    // greater than 1.
    if (params.floorMultiple <= MIN_FLOOR_MULTIPLE) revert FloorMultipleMustBeAbove100(params.floorMultiple);
    if (params.floorMultiple > MAX_FLOOR_MULTIPLE) revert FloorMultipleExceedsMax(params.floorMultiple, MAX_FLOOR_MULTIPLE);
    emit ListingFloorMultipleUpdated(_collection, params.tokenId, listing.floorMultiple, params.floorMultiple);
    listing.floorMultiple = params.floorMultiple;
}
// Get the amount of tax required for the newly extended listing
taxRequired_ += getListingTaxRequired(listing, _collection);
