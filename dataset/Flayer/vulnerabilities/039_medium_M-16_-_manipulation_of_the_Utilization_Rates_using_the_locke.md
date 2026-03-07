# M-16 - manipulation of the Utilization Rates using the locker.sol function deposit and redeem to Force Liquidations

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** utilization rate, manipulation, liquidation, NFT, ERC20, deposit, redeem, interest rate, keeper reward, total supply, smart contract, audit, bug, exploitation, collateral, liquidation process, losses, malicious user, auction, discount price

---

# Issue M-13: Price limit is used as the price range in internal swaps, causing swap TXs to revert

Source: [GitHub Issue #402](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/402)  
Found by: 0xAlix2  


When initializing a swap on Uniswap V4, the user inputs a price limit that represents the sqrt price at which, if reached, the swap will stop executing, from Uni V4 code.

\u0060\u0060\u0060solidity
struct SwapParams {
    /// Whether to swap token0 for token1 or vice versa
    bool zeroForOne;
    /// The desired input amount if negative (exactIn), or the desired output amount if positive (exactOut)
    int256 amountSpecified;
    /// The sqrt price at which, if reached, the swap will stop executing
    uint160 sqrtPriceLimitX96;
}
\u0060\u0060\u0060

When a swap happens in a Uniswap pool, the swap calculation happens by calling \u0060SwapMath.computeSwapStep\u0060, where the input price limit is translated to a price target using \u0060SwapMath.getSqrtPriceTarget\u0060. Knowing that the price target represents "The price target for the next swap step" [SwapMath.sol](https://github.com/Uniswap/v4-core/blob/main/src/libraries/SwapMath.sol#L19).

On the other hand, when the internal swap is done in the Uniswap implementation, \u0060SwapMath.computeSwapStep\u0060 is called while passing the price limit as the price target.

\u0060\u0060\u0060solidity
(, ethIn, tokenOut, ) = SwapMath.computeSwapStep({
    sqrtPriceCurrentX96: sqrtPriceX96,
    sqrtPriceTargetX96: params.sqrtPriceLimitX96,
    liquidity: poolManager.getLiquidity(poolId),
    amountRemaining: int(amountSpecified),
    feePips: 0
});
\u0060\u0060\u0060

This affects the in/out token calculation, as it will calculate those values based on a wrong target, forcing swap TXs to unexpectedly revert.
When calculating internal swaps, the input price limit is used as the price range for the swap calculation, here and here.

Swap transactions will revert in most cases; DOSing swaps.

Add the following test in layer/test/UniswapImplementation.t.sol:
\u0060\u0060\u0060solidity
function test_WrongPriceTargetUsed() public withLiquidity withTokens {
    bool flipped = false;
    PoolKey memory poolKey = _poolKey(flipped);
    CollectionToken token = flipped ? flippedToken : unflippedToken;
    ERC721Mock nft = flipped ? flippedErc : unflippedErc;
    uint256 fees = 10 ether;
    deal(address(token), address(this), fees);
    token.approve(address(uniswapImplementation), type(uint).max);
    uniswapImplementation.depositFees(address(nft), 0, fees);
    // token0 = WETH, token1 = token
    assertEq(address(Currency.unwrap(poolKey.currency0)), address(WETH));
    assertEq(address(Currency.unwrap(poolKey.currency1)), address(token));
    // amount of token out to receive
    uint amountSpecified = 15 ether;
    // Uniswap implementation + pool manager have enough tokens to fulfill the swap
    assertGt(
        token.balanceOf(address(uniswapImplementation)) +
        token.balanceOf(address(uniswapImplementation.poolManager())),
        amountSpecified
    );
    // This contract has more than enough WETH to fulfill the swap
    assertEq(WETH.balanceOf(address(this)), 1000 ether);
    // Swap WETH -> TOKEN
    vm.expectRevert();
    poolSwap.swap(
        poolKey,
        IPoolManager.SwapParams({
            zeroForOne: true,
            amountSpecified: int(amountSpecified),
            sqrtPriceLimitX96: TickMath.MIN_SQRT_PRICE + 1
        });
}
\u0060\u0060\u0060

In UniswapImplementation::beforeSwap, whenever the internal swap is being computed, i.e. by calling SwapMath.computeSwapStep, translate the passed price limit to price range, using SwapMath.getSqrtPriceTarget, by doing something similar to:

\u0060\u0060\u0060
(, ethIn, tokenOut, ) = SwapMath.computeSwapStep({
    sqrtPriceCurrentX96: sqrtPriceX96,
    sqrtPriceTargetX96: SwapMath.getSqrtPriceTarget(zeroForOne,
    step.sqrtPriceNextX96, params.sqrtPriceLimitX96),
    liquidity: poolManager.getLiquidity(poolId),
    amountRemaining: int(amountSpecified),
    feePips: 0
});
\u0060\u0060\u0060
## Issue M-14: In the unlockProtectedListing() function, the interest that was supposed to be distributed to LP holders was instead burned.

Source: [GitHub Issue #431](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/431)  
Found by: 0x73696d616f, Audinarey, Ironsidesec, Ollam, ZeroTrust

In the unlockProtectedListing() function, the interest that was supposed to be distributed to LP holders was instead burned.

\u0060\u0060\u0060solidity
function unlockProtectedListing(address _collection, uint _tokenId, bool _withdraw) 
    public lockerNotPaused {
        // Ensure this is a protected listing
        ProtectedListing memory listing = _protectedListings[_collection][_tokenId];
        // Ensure the caller owns the listing
        if (listing.owner != msg.sender) revert CallerIsNotOwner(listing.owner);
        // Ensure that the protected listing has run out of collateral
        int collateral = getProtectedListingHealth(_collection, _tokenId);
        if (collateral < 0) revert InsufficientCollateral();
        // cache
        ICollectionToken collectionToken = locker.collectionToken(_collection);
        uint denomination = collectionToken.denomination();
        uint96 tokenTaken = _protectedListings[_collection][_tokenId].tokenTaken;
        // Repay the loaned amount, plus a fee from lock duration
        uint fee = unlockPrice(_collection, _tokenId) * 10 ** denomination;
        collectionToken.burnFrom(msg.sender, fee);
        // We need to burn the amount that was paid into the Listings contract
        collectionToken.burn((1 ether - tokenTaken) * 10 ** denomination);
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Remove our listing type
unchecked { --listingCount[_collection]; }
// Delete the listing objects
delete _protectedListings[_collection][_tokenId];
// Transfer the listing ERC721 back to the user
if (_withdraw) {
    locker.withdrawToken(_collection, _tokenId, msg.sender);
    emit ListingAssetWithdraw(_collection, _tokenId);
} else {
    canWithdrawAsset[_collection][_tokenId] = msg.sender;
}
// Update our checkpoint to reflect that listings have been removed
_createCheckpoint(_collection);
// Emit an event
emit ListingUnlocked(_collection, _tokenId, fee);
}

function unlockPrice(address _collection, uint _tokenId) public view returns (uint unlockPrice_) {
    // Get the information relating to the protected listing
    ProtectedListing memory listing = _protectedListings[_collection][_tokenId];
    // Calculate the final amount using the compounded factors and principle
    unlockPrice_ = locker.taxCalculator().compound({
        _principle: listing.tokenTaken,
        _initialCheckpoint: collectionCheckpoints[_collection][listing.checkpoint],
        _currentCheckpoint: _currentCheckpoint(_collection)
    });
}

Therefore, after burning the fee, the interest paid by the user was also burned. This portion of the interest should have been distributed to the LP holders. Evidence for this can be found in the liquidateProtectedListing() function, where the interest generated by the Protected Listing NFT is distributed to the LP holders.

function liquidateProtectedListing(address _collection, uint _tokenId) public lockerNotPaused listingExists(_collection, _tokenId) {
    //-------skip-----------
    // Send the remaining tokens to {Locker} implementation as fees
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint remainingCollateral = (1 ether - listing.tokenTaken - KEEPER_REWARD) *
            10 ** denomination;
if (remainingCollateral > 0) {
    IBaseImplementation implementation = locker.implementation();
    collectionToken.approve(address(implementation), remainingCollateral);
    implementation.depositFees(_collection, 0, remainingCollateral);
}
//-------skip-----------
}
After the interest is burned, it causes deflation in the total amount of collectionToken,
which leads to serious problems:
1. The total number of collectionTokens no longer matches the number of NFTs (it
   becomes less than the number of NFTs in the Locker contract), making it
   impossible to redeem some NFTs.
2. The utilizationRate() calculation results in a utilization rate greater than
   100%, leading to an excessively high interestRate_, which in turn makes it
   impossible for users to create listings on ProtectedListings.
/**
 * Determines the usage rate of a listing type.
 *
 * @param _collection The collection to calculate the utilization rate of
 *
 * @return listingsOfType_ The number of listings that match the type passed
 * @return utilizationRate_ The utilization rate percentage of the listing type
 * (80% = 0.8 ether)
 */
function utilizationRate(address _collection) public view virtual returns (uint
   listingsOfType_, uint utilizationRate_) {
   // Get the count of active listings of the specified listing type
   listingsOfType_ = listingCount[_collection];
   // If we have listings of this type then we need to calculate the percentage,
   // otherwise
   // we will just return a zero percent value.
   if (listingsOfType_ != 0) {
       ICollectionToken collectionToken = locker.collectionToken(_collection);
       // If we have no totalSupply, then we have a zero percent utilization
       uint totalSupply = collectionToken.totalSupply();
       if (totalSupply != 0) {
           utilizationRate_ = (listingsOfType_ * 1e36 * 10 **
           collectionToken.denomination()) / totalSupply;
       }
   }
}
\u0060\u0060\u0060
LPholders suffer losses, and users may be unable to use Protected Listings normally.

- [ProtectedListings.sol#L287](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L287)
- [ProtectedListings.sol#L607](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L607)
- [ProtectedListings.sol#L429](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L429)
- [ProtectedListings.sol#L261](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L261)

Manual Review

Distribute the interest to the LP holders.
## IssueM-15: Users can dodge create Listing fees

Source: [GitHub Issue #440](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/440)  
Found by: Ollam, OpaBatyo, ZeroTrust, valuevalk, zzykxx  

Users can abuse a loophole to create a listing for 5% less tax than intended, hijack others\u0027 tokens at floor value and perpetually relist for free.

For the sake of simplicity, we assume that collection token denomination = 4 and floor price = 1e22.  
Users who intend to create a dutch listing for any duration <= 4 days can do the following:

1. Create a normal listing at min floor multiple = 101 and MIN_DUTCH_DURATION = 1 day, tax = 0.1457% (tokens Received = 0.99855e22)
2. Reserve their own listing from a different account for token Taken 0.95e18, collateral 0.05e18, collateral is burnt, protected listing is at 0 health and will be liquidatable in a few moments (remaining Tokens = 0.94855e22)
3. Liquidate their own listing through liquidateProtectedListing, receive KEEPER_REWARD = 0.05e22 (remaining Tokens = 0.99855e22)
4. createLiquidationListing is invoked with us as owner and hardcoded values floor Multiple = 400 and duration = 4 days

User has paid 0.14% in tax for a listing that would\u0027ve normally cost them 5.14% in tax.  
This process can be repeated any number of times even after the liquidation Listing expires to constantly reserve-liquidate it instead of calling relist and paying further tax.  

There are numerous other ways in which this loophole of reserve-liquidate can be abused:

1. Users can create listings for free out of any expired listing at floor value, they only burn 0.05e18 collateral which is then received back as KEEPER_REWARD.
2. Users can constantly cycle NFTs at floor value (since it is free) and make liquidation Listings, either making profit if the token sells or making the token unpurchasable at floor since it is in the loop.
3) Any user-owned expired listing can be relisted for free through this method instead of paying tax by invoking relist

Tax evasion

\u0060\u0060\u0060solidity
_listings.createLiquidationListing(
    IListings.CreateListing({
        collection: _collection,
        tokenIds: tokenIds,
        listing: IListings.Listing({
            owner: listing.owner,
            created: uint40(block.timestamp),
            duration: 4 days,
            floorMultiple: 400
        })
    })
);
\u0060\u0060\u0060

Manual Review

Impose higher minimum collateral and lower token Taken (e.g. 0.2e18 and 0.8e18) so the KEE PER_REWARD would not cover the cost of burning collateral during reservation, making this exploit unprofitable.
## IssueM-16: manipulation of the Utilization Rates using the locker.sol function deposit and redeem to Force Liquidations

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/476)  
Found by: BugPull, ComposableSecurity, OpaBatyo, jo13  

A user with a significant number of NFTs can manipulate the total supply of ERC20 tokens to indirectly push protected listings towards liquidation by influencing the utilization rate and associated.

The vulnerability arises from the ability of a user to deposit and redeem any quantities of NFTs, without fees. As shown in the locker.sol contract: 

- The deposit function increases the total supply by mint function.

\u0060\u0060\u0060solidity
function deposit(address _collection, uint[] calldata _tokenIds, address _recipient) public
{
    //.....
    ICollectionToken token = _collectionToken[_collection];
    token.mint(_recipient, tokenIdsLength * 1 ether * 10 ** token.denomination());
    //.....
}
\u0060\u0060\u0060

- And decreases the total supply using the redeem function.

\u0060\u0060\u0060solidity
function redeem(address _collection, uint[] calldata _tokenIds, address _recipient) public
{
    //...
    collectionToken_.burnFrom(msg.sender, tokenIdsLength * 1 ether * 10 ** collectionToken_.denomination());
    //..
}
\u0060\u0060\u0060
The manipulation affects the utilization rate, [source](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L261-L276) which in turn influences interest rates that are used directly to calculate the \u0060calculateCompoundedFactor\u0060 function:

\u0060\u0060\u0060solidity
function calculateCompoundedFactor(uint _previousCompoundedFactor, uint _utilizationRate, uint _timePeriod) public view returns (uint compoundedFactor_) {
    uint interestRate = this.calculateProtectedInterest(_utilizationRate);
    uint perSecondRate = (interestRate * 1e18) / (365 * 24 * 60 * 60);
    compoundedFactor_ = _previousCompoundedFactor * (1e18 + (perSecondRate / 1000 * _timePeriod)) / 1e18;
}
\u0060\u0060\u0060

We use this to calculate the amount of tax that would need to be paid against protected listings. In the function \u0060unlockPrice\u0060, [source](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L607-L617) this function is used to check the protected listing health in \u0060getProtectedListingHealth\u0060 that is used in \u0060liquidateProtectedListing\u0060. An exploitation of the direct relation between the total supply and the liquidation is possible by a malicious user who owns half of the NFTs. The user can perform an action that causes the liquidation of the positions of the other participants and receives the \u0060KEEPER_REWARD\u0060 for being a keeper for initiating the liquidation process. In addition, the user can buy up the one that had its NFT liquidated at an auction at a discount price which increases their gain.


The impact of this vulnerability is that it allows a user to exploit the system to force protected listings into liquidation. This can lead to losses for other users whose listings are liquidated. It undermines the stability and fairness of the protocol by enabling manipulative tactics.


- [calculateCompoundedFactor](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L261-L276)
- [unlockPrice](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L607-L617)


Manual Review

\u0060\u0060\u0060
usefeesindepositandredeem
\u0060\u0060\u0060
## Issue M-17: CollectionShutdown::execute() doesn\u0027t ensure that all locked NFTs are sold

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/502)  
Found by: IMAFVCKINSTARRRRRR, McToady, zzykxx

No response

CollectionShutdown::execute() doesn\u0027t ensure that all tokens of the collection being shutdown are added to the sudoswap pool in order to be sold. This function takes as input an array of the token IDs to be sold via sudoswap pool. In case an NFT ID that\u0027s locked in the protocol is not in this array, the NFT will stay locked and not sold. Even if the function is only callable by admins, the admins have no control on the order and the moment transactions are executed and such scenarios should be handled at the moment of execution.

No response

No response

1. The protocol currently holds NFTs 55 and 56, admin calls CollectionShutdown::execute() by passing as a parameter [55, 56].
2. While the CollectionShutdown::execute() transaction is in the mempool, a deposit of NFT 60 is done via Locker::deposit().
3. TheCollectionShutdown::execute() transaction goes through and a sudoswap pool selling 55 and 56 is created  
4. NFT 60 is locked in the protocol  

NFTs that should be sold are locked in the protocol, which leads to an indirect loss of funds to collection token holders.  

No response  

In CollectionShutdown::execute(), make sure all tokens currently locked in the protocol are added to the sudoswap pool.
## Issue M-18: If the royalties receiver it\u0027s a smart contract it might be impossible to collect L2 royalties

Source: [GitHub Issue #509](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/509)  
Found by: zzykxx  

No response  

The function \u0060InfernalRiftAbove::claimRoyalties()\u0060 can only be called by the receiver of the royalties:
\u0060\u0060\u0060solidity
(address receiver,) = IERC2981(_collectionAddress).royaltyInfo(0, 0);
// Check that the receiver of royalties is making this call
if (receiver != msg.sender) revert CallerIsNotRoyaltiesReceiver(msg.sender, receiver);
\u0060\u0060\u0060
This is fine for EOAs but is problematic if the receiver is a contract that doesn\u0027t have a way to call \u0060InfernalRiftAbove::claimRoyalties()\u0060, as this would result in the receiver not being able to claim the royalties collected by NFTs bridged to L2.

No response  

No response  

No response
If the royalties receiver is a smart contract that doesn\u0027t have a way to call InfernalRiftAbove::claimRoyalties() it\u0027s impossible to claim the royalties, which will be stuck.

No response

Allow royalties to be claimed to the receiver address by anybody when the receiver is a smart contract.
