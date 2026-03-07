# H-13 - InfernalRiftBelow.claimRoyalties

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** claimRoyalties, msg.sender, authentication, cross-chain, NFT, transfer, ERC721Bridgable, protocol, function, revert, assets, loss, vulnerability, contract, check, xDomainMessageSender, address, INFERNAL_RIFT_ABOVE, ERC721, steal

---

# Issue H-9: _listing mapping not deleted when calling Listings::reserve can lead to a token being sold when it shouldn\u0027t be forsale

Source: https://github.com/sherlock-audit/2024-08-flayer-judging/issues/252

Found by  
0x37, 0xAlix2, 0xHappy, 0xNirix, BugPull, Feder, McToady, Ruhum, alman tare, araj, blockchain555, h2134, jecikpo, kuprum, merlinboii, stuart_the_minion, utsav, valuevalk, zzykxx

Summary  
When the reserve function is called in Listings a protected listing is created for the selected_tokenId, however while doing this the original_listing mapping for this token is not deleted in Listings. While the protected listing is active this is not a problem because getListingPrice will check the protected listing before reaching the old listing. However if the protected listing is removed this old listing will become active again. This becomes especially problematic given the ProtectedListings::unlockProtectedListing function allows the user to not withdraw the token immediately, meaning the token will be in the Locker and can now be sold to a third party calling Listings::fillListings.

Vulnerability Detail  
Consider the following steps:
1. User A lists token via Listings::createListings
2. User B creates a reserve on the token calling Listings::reserve
3. Later when User B is ready to fully pay off the token they call ProtectedListings::unlockProtectedListing however they set _withdraw == false as they will choose to withdraw the token later.
4. Now User C will be able to gain the token via the original (still active) listing by calling Listings::fillListings

Add the following test to Listings.t.sol to highlight this issue:
\u0060\u0060\u0060solidity
function test_Toad_abuseOldListing() public {
   // Get user A token
\u0060\u0060\u0060
address userA = makeAddr("userA");
vm.deal(userA, 1 ether);
uint256 _tokenId = 1199;
erc721a.mint(userA, _tokenId);
vm.startPrank(userA);
erc721a.approve(address(listings), _tokenId);
Listings.Listing memory listing = IListings.Listing({
    owner: payable(userA),
    created: uint40(block.timestamp),
    duration: VALID_LIQUID_DURATION,
    floorMultiple: 120
});
_createListing({
    _listing: IListings.CreateListing({
        collection: address(erc721a),
        tokenIds: _tokenIdToArray(_tokenId),
        listing: listing
    })
});
vm.stopPrank();
// User B calls Listings::reserve
address userB = makeAddr("userB");
uint256 startBalance = 10 ether;
ICollectionToken token = locker.collectionToken(address(erc721a));
deal(address(token), userB, startBalance);
vm.warp(block.timestamp + 10);
vm.startPrank(userB);
token.approve(address(listings), startBalance);
token.approve(address(protectedListings), startBalance);
uint256 listingCountStart = listings.listingCount(address(erc721a));
console.log("Listing count start", listingCountStart);
listings.reserve({
    _collection: address(erc721a),
    _tokenId: _tokenId,
    _collateral: 0.2 ether
});
uint256 listingCountAfterReserve = listings.listingCount(address(erc721a));
console.log("Listing count after reserve", listingCountAfterReserve);
// User B later calls ProtectedListings::unlockProtectedListing with _withdraw
֒→ == false
vm.warp(block.timestamp + 1 days);

This series of actions has the following effects on the users involved:
- User A gets paid the difference between their listing price and floor price twice (during both User B and User C\u0027s purchases).
- User B pays the full price of the token from User A but does not get the NFT.
- User C pays the full price of the token from User A and gets the NFT.

Additionally, during this process \u0060listingCount[_collection]\u0060 gets decremented twice, potentially leading to an underflow as the value is changed in an unchecked block. This incorrect internal accounting can later cause issues if \u0060CollectionShutdown\u0060 attempts to sunset a collection as its \u0060hasListings\u0060 check when sunsetting a collection will be incorrect, potentially sunsetting a collection while listings are still live.

[Link to Code Snippet](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol#L690)

Manual Review

Just as in \u0060_fillListing\u0060 and \u0060cancelListing\u0060 functions, when \u0060reserve\u0060 is called the existing \u0060_listing\u0060 mapping for the specified \u0060tokenId\u0060 should be deleted as so:

\u0060\u0060\u0060solidity
function reserve(address _collection, uint _tokenId, uint _collateral) public
    nonReentrant lockerNotPaused {
        // -- Snip --
        // Check if the listing is a floor item and process additional logic if there
        // was an owner (meaning it was not floor, so liquid or dutch).
        if (oldListing.owner != address(0)) {
            // We can process a tax refund for the existing listing if it isn\u0027t a liquidation
            if (!_isLiquidation[_collection][_tokenId]) {
                (uint _fees,) = _resolveListingTax(oldListing, _collection, true);
                if (_fees != 0) {
                    emit ListingFeeCaptured(_collection, _tokenId, _fees);
                }
            }
            // If the floor multiple of the original listings is different, then this needs
            // to be paid to the original owner of the listing.
            uint listingFloorPrice = 1 ether * 10 ** collectionToken.denomination();
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
if (listingPrice > listingFloorPrice) {
    unchecked {
        collectionToken.transferFrom(msg.sender, oldListing.owner,
        listingPrice - listingFloorPrice);
    }
    delete _listings[_collection][_tokenId]
    // Reduce the amount of listings
    unchecked { listingCount[_collection] -= 1; }
}
// -- Snip --
\u0060\u0060\u0060
This will ensure that even if the token\u0027s new protected listing is removed the stale listing will not be accessible.
## Issue H-10: The Users who voted for collection shutdown will lose their collection tokens by cancelling the shutdown

Source: [GitHub Issue #261](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/261)

Found by
0xAlix2, 0xHappy, 0xc0ffEE, Audinarey, Aymen0909, BADROBINX, BugPull, Hearmen, Limbooo, McToady, Ragnarok, almantare, araj, asui, blockchain555, cawfree, ctf_sec, dany.armstrong90, g, merlinboii, onthehunt, steadyman, stuart_the_minion, utsav, ydlee, zzykxx

When a user votes for collection shutdown, the CollectionShutdown contract gathers the whole balance from the user. However, when cancelling the shutdown process, the contract doesn\u0027t refund the user\u0027s votes.

The function gathers the whole balance of the collection token from a voter.

\u0060\u0060\u0060solidity
function _vote(address _collection, CollectionShutdownParams memory params)
    internal returns (CollectionShutdownParams memory) {
    uint userVotes = params.collectionToken.balanceOf(msg.sender);
    if (userVotes == 0) revert UserHoldsNoTokens();
    // Pull our tokens in from the user
    params.collectionToken.transferFrom(msg.sender, address(this), userVotes);
    ... ...
}
\u0060\u0060\u0060

But in the function, it does not refund the voter\u0027s tokens.

\u0060\u0060\u0060solidity
function cancel(address _collection) public whenNotPaused {
    // Ensure that the vote count has reached quorum
    CollectionShutdownParams memory params = _collectionParams[_collection];
    if (!params.canExecute) revert ShutdownNotReachedQuorum();
    // Check if the total supply has surpassed an amount of the initial required
    // total supply. This would indicate that a collection has grown since the
\u0060\u0060\u0060
// initial shutdown was triggered and could result in an unsuspected liquidation.
if (params.collectionToken.totalSupply() <= MAX_SHUTDOWN_TOKENS * 10 **
    locker.collectionToken(_collection).denomination()) {
    revert InsufficientTotalSupplyToCancel();
}
// Remove our execution flag
delete _collectionParams[_collection];
emit CollectionShutdownCancelled(_collection);
## Proof-Of-Concept
Here is the test case of the POC:
To bypass the total supply vs shutdown votes restriction, added the following line to the test case:
\u0060\u0060\u0060solidity
collectionToken.mint(address(10), _additionalAmount);
\u0060\u0060\u0060
The whole test case is:
\u0060\u0060\u0060solidity
function test_CancelShutdownNotRefund() public withQuorumCollection {
    uint256 _additionalAmount = 1 ether;
    // Confirm that we can execute with our quorum-ed collection
    assertCanExecute(address(erc721b), true);
    vm.prank(address(locker));
    collectionToken.mint(address(10), _additionalAmount);
    // Cancel our shutdown
    collectionShutdown.cancel(address(erc721b));
    // Now that we have cancelled the shutdown process, we should no longer
    // be able to execute the shutdown.
    assertCanExecute(address(erc721b), false);
    console.log("Address 1 balance after:", collectionToken.balanceOf(address(1)));
    console.log("Address 2 balance after:", collectionToken.balanceOf(address(2)));
}
\u0060\u0060\u0060
Here are the logs after running the test:
\u0060\u0060\u0060
$ forge test --match-test test_CancelShutdownNotRefund -vv
[￿] Compiling...
[￿] Compiling 1 files with Solc 0.8.26
[￿] Solc 0.8.26 finished in 8.81s
\u0060\u0060\u0060
## Compiler run successful!

Ran 1 test for test/utils/CollectionShutdown.t.sol:CollectionShutdownTest  
[PASS] test_CancelShutdownNotRefund() (gas: 390566)  
Logs:  
Address 1 balance after: 0  
Address 2 balance after: 0  
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 8.29s (454.80µs CPU time)  
Ran 1 test suite in 8.29s (8.29s CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)  

As can be seen from the logs, the voters (1,2) were not refunded their tokens.  

Shutdown Voters will end up losing their whole collection tokens by cancelling the shutdown.  

utils/CollectionShutdown.sol  

Manual Review  

The problem can be fixed by implementing the following:  
1. Add new state variable to the contract that records all voters  
   \u0060address[] public votersList;\u0060  
2. Update the _vote() function like below:  
   \u0060\u0060\u0060solidity
   function _vote(address _collection, CollectionShutdownParams memory params)
       internal returns (CollectionShutdownParams memory) {
       ... ...
       // Register the amount of votes sent as a whole, and store them against the user
       params.shutdownVotes += uint96(userVotes);
   }
   \u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Register the amount of votes for the collection against the user
if (shutdownVoters[_collection][msg.sender] == 0)
    votersList.push(msg.sender);
unchecked { shutdownVoters[_collection][msg.sender] += userVotes; }
... ...
}
3. Add the new code section to the reclaimVote() function, that removes the sender from the votersList.
4. Update the cancel() function like below:
function cancel(address _collection) public whenNotPaused {
    ... ...
    if (params.collectionToken.totalSupply() <= MAX_SHUTDOWN_TOKENS * 10 **
        locker.collectionToken(_collection).denomination()) {
        revert InsufficientTotalSupplyToCancel();
    }
    uint256 i;
    uint256 votersLength = votersList.length;
    for (; i < votersLength; i ++) {
        params.collectionToken.transfer(
            votersList[i],
            shutdownVoters[_collection][votersList[i]]
        );
    }
    // Remove our execution flag
    delete _collectionParams[_collection];
    delete votersList;
    emit CollectionShutdownCancelled(_collection);
}
After running the testcase on the above update, the user voters are able to get their own votes:
$ forge test --match-test test_CancelShutdownNotRefund -vv
[￿] Compiling...
[￿] Compiling 3 files with Solc 0.8.26
Solc 0.8.26 finished in 8.70s
Compiler run successful!
Ran 1 test for test/utils/CollectionShutdown.t.sol:CollectionShutdownTest
[PASS] test_CancelShutdownNotRefund() (gas: 486318)
Logs:
  Address 1 balance after: 1000000000000000000
  Address 2 balance after: 1000000000000000000
\u0060\u0060\u0060
## Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 3.46s (526.80µs CPU time)

Ran 1 test suite in 3.46s (3.46s CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
## Issue H-11: User can unlock protected listing without paying any fee.

Source: [https://github.com/sherlock-audit/2024-08-flayer-judging/issues/269](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/269)  
Found by: 0x37, OpaBatyo, dany.armstrong90, g, jecikpo, onthehunt, zzykxx

ProtectedListings.adjustPosition() function adjusts listing.tokenTaken without considering compounded factor. Exploiting this vulnerability, user can unlock protected listing without paying any fee.

ProtectedListings.adjustPosition() function is following.

\u0060\u0060\u0060solidity
function adjustPosition(address _collection, uint _tokenId, int _amount) public
    lockerNotPaused {
        // Ensure we don\u0027t have a zero value amount
        if (_amount == 0) revert NoPositionAdjustment();
        // Load our protected listing
        ProtectedListing memory protectedListing = _protectedListings[_collection][_tokenId];
        // Make sure caller is owner
        if (protectedListing.owner != msg.sender) revert CallerIsNotOwner(protectedListing.owner);
        // Get the current debt of the position
        int debt = getProtectedListingHealth(_collection, _tokenId);
        // Calculate the absolute value of our amount
        uint absAmount = uint(_amount < 0 ? -_amount : _amount);
        // cache
        ICollectionToken collectionToken = locker.collectionToken(_collection);
        // Check if we are decreasing debt
        if (_amount < 0) {
            // The user should not be fully repaying the debt in this way. For this
\u0060\u0060\u0060
// the owner would instead use the \u0060unlockProtectedListing\u0060 function.
if (debt + int(absAmount) >= int(MAX_PROTECTED_TOKEN_AMOUNT)) revert IncorrectFunctionUse();
// Take tokens from the caller
collectionToken.transferFrom(
    msg.sender,
    address(this),
    absAmount * 10 ** collectionToken.denomination()
);
// Update the struct to reflect the new tokenTaken, protecting from overflow
_protectedListings[_collection][_tokenId].tokenTaken -= uint96(absAmount);
// Otherwise, the user is increasing their debt to take more token
else {
// Ensure that the user is not claiming more than the remaining collateral
if (_amount > debt) revert InsufficientCollateral();
// Release the token to the caller
collectionToken.transfer(
    msg.sender,
    absAmount * 10 ** collectionToken.denomination()
);
// Update the struct to reflect the new tokenTaken, protecting from overflow
_protectedListings[_collection][_tokenId].tokenTaken += uint96(absAmount);
}
emit ListingDebtAdjusted(_collection, _tokenId, _amount);
As can be seen in L399 and L413, _protectedListings[_collection][_tokenId].tokenTaken is updated without considering compounded factor. Exploiting this vulnerability, user can unlock protected listing without paying any fee.
PoC: Add the following test code into ProtectedListings.t.sol.
function test_adjustPositionError() public {
    erc721a.mint(address(this), 0);
    erc721a.setApprovalForAll(address(protectedListings), true);
    uint[] memory _tokenIds = new uint[](2); _tokenIds[0] = 0; _tokenIds[1] = 1;
}
\u0060\u0060\u0060solidity
IProtectedListings.CreateListing[] memory _listings = new IProtectedListings.CreateListing[](1);
_listings[0] = IProtectedListings.CreateListing({
    collection: address(erc721a),
    tokenIds: _tokenIdToArray(0),
    listing: IProtectedListings.ProtectedListing({
        owner: payable(address(this)),
        tokenTaken: 0.4 ether,
        checkpoint: 0
    })
});
protectedListings.createListings(_listings);
vm.warp(block.timestamp + 7 days);
// unlock protected listing for tokenId = 0
assertEq(protectedListings.unlockPrice(address(erc721a), 0), 402055890410801920);
locker.collectionToken(address(erc721a)).approve(address(protectedListings), 0.4 ether);
protectedListings.adjustPosition(address(erc721a), 0, -0.4 ether);
assertEq(protectedListings.unlockPrice(address(erc721a), 0), 0);
protectedListings.unlockProtectedListing(address(erc721a), 0, true);
\u0060\u0060\u0060

In the above test code, we can see that \u0060unlockPrice(address(erc721a), 0)\u0060 is \u0060402055890410801920\u0060, but after calling \u0060adjustPosition(address(erc721a), 0, -0.4 ether)\u0060, \u0060unlockPrice(address(erc721a), 0)\u0060 decreases to \u00600\u0060. So we unlocked protected listing paying only \u00600.4 ether\u0060 without paying any fee.

User can unlock protected listing without paying any fee. It means loss of funds for the protocol. On the other hand, if user increases \u0060tokenTaken\u0060 in \u0060adjustPosition()\u0060 function, increment of fee will be inflated by compounded factor. It means loss of funds for the user.

[GitHub Link](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L366-L417)

Manual Review

Adjust \u0060tokenTaken\u0060 considering \u0060compoundedFactor\u0060 in \u0060ProtectedListings.adjustPosition()\u0060 function. That is, divide \u0060absAmount\u0060 by \u0060compoundedFactor\u0060 before updating \u0060tokenTaken\u0060.
## IssueH-12: InfernalRiftBelow.thresholdCross

Source: [GitHub](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/405)  
The protocol has acknowledged this issue.  
Found by: Ali9955, Tendency, ZeroTrust, novaman33  

InfernalRiftBelow.thresholdCross verify the wrong msg.sender, thresholdCross will fail to be called, resulting in the loss of user assets.  

thresholdCross determines whether msg.sender is expected AliasedSender:
\u0060\u0060\u0060solidity
address expectedAliasedSender = address(uint160(INFERNAL_RIFT_ABOVE) +
    uint160(0x1111000000000000000000000000000000001111));
// Ensure the msg.sender is the aliased address of {InfernalRiftAbove}
if (msg.sender != expectedAliasedSender) {
    revert CrossChainSenderIsNotRiftAbove();
}
\u0060\u0060\u0060
but in fact the function caller should be RELAYER_ADDRESS, Insudoswap, crossTheThreshold check whether msg.sender is RELAYER_ADDRESS: [GitHub](https://github.com/sudoswap/InfernalRift/blob/7696827b3221929b3fa563692bd4c5d73b20528e/src/InfernalRiftBelow.sol#L56)  

L1 across chain message through the PORTAL.depositTransaction, rather than L1_CROSS_DOMAIN_MESSENGER. To avoid confusion, use in L1 should all L1_CROSS_DOMAIN_MESSENGER.sendMessage to send messages across the chain, avoid the use of low-level PORTAL.depositTransaction function.
\u0060\u0060\u0060solidity
function crossTheThreshold(ThresholdCrossParams memory params) external payable {
    ......
    // Send package off to the portal
    PORTAL.depositTransaction{value: msg.value}(
        INFERNAL_RIFT_BELOW,
        0,
        params.gasLimit,
        false,
    );
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
abi.encodeCall(InfernalRiftBelow.thresholdCross, (package,
             params.recipient))
                    );
                    emit BridgeStarted(address(INFERNAL_RIFT_BELOW), package, params.recipient);
\u0060\u0060\u0060

When transferring nft across chains, thresholdCross cannot be called in L2, resulting in loss of user assets.

[Code Snippet](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf83186835f5ef688c/moongate/src/InfernalRiftBelow.sol#L135-L145)

Manual Review

\u0060\u0060\u0060solidity
// Validate caller is cross-chain
if (msg.sender != RELAYER_ADDRESS) { //or L2_CROSS_DOMAIN_MESSENGER
    revert NotCrossDomainMessenger();
}
// Validate caller comes from {InfernalRiftBelow}
if (ICrossDomainMessenger(msg.sender).xDomainMessageSender() != InfernalRiftAbove) {
    revert CrossChainSenderIsNotRiftBelow();
}
\u0060\u0060\u0060

**zhaojio**  
We asked sponsor:  
InfernalRiftBelow.claimRoyalties function of the msg.sender, is RELAYER_ADDRESS? right??  

**Sponsor reply:**  
good catch, it should be L2_CROSS_DOMAIN_MESSENGER instead
## IssueH-13: InfernalRiftBelow.claimRoyalties

Source: [https://github.com/sherlock-audit/2024-08-flayer-judging/issues/406](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/406)

Found by: Ironsidesec, Thanos, X12, ZeroTrust, cnsdkc007, ctf_sec, gr8tree, rndquu, shaflow01, snapishere, t.aksoy, zzykxx


claimRoyalties used to accept the message on the L1, then execute ERC721Bridgable.claimRoyalties, but not the authentication callers, may result in the loss of the assets in the protocol.


claimRoyalties are used to accept cross-chain calls, but msg.sender is not validated:

\u0060\u0060\u0060solidity
if (ICrossDomainMessenger(msg.sender).xDomainMessageSender() != INFERNAL_RIFT_ABOVE) {
    revert CrossChainSenderIsNotRiftAbove();
}
\u0060\u0060\u0060

If msg.sender is a contract account implementing the ICrossDomainMessenger interface, the xDomainMessageSender function returns an address of INFERNAL_RIFT_ABOVE, which means that the claimRoyalties function can be invoked. So anyone can call this function as long as he deploys a contract.

InfernalRiftBelow.claimRoyalties function will be called ERC721Bridgable.claimRoyalties, transfer NFTs from ERC721Bridgable contract, so any can transfer NFTs from ERC721Bridgable.

L1 Send message to L2:

\u0060\u0060\u0060solidity
function claimRoyalties(address _collectionAddress, address _recipient, address[] calldata _tokens, uint32 _gasLimit) external {
    .....
    ICrossDomainMessenger(L1_CROSS_DOMAIN_MESSENGER).sendMessage(
        INFERNAL_RIFT_BELOW,
        abi.encodeCall(
            IInfernalRiftBelow.claimRoyalties,
            (_collectionAddress, _recipient, _tokens)
        )
    );
}
\u0060\u0060\u0060
\u0060\u0060\u0060
),
                   _gasLimit
               );
               emit RoyaltyClaimStarted(address(INFERNAL_RIFT_BELOW), _collectionAddress,
            ֒→ _recipient, _tokens);
           }
\u0060\u0060\u0060

Anyone can steal NFT from the protocol.

[GitHub Link](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/moongate/src/InfernalRiftBelow.sol#L220-L232)

Manual Review

\u0060\u0060\u0060
if (msg.sender != L2_CROSS_DOMAIN_MESSENGER) {
    revert NotCrossDomainMessenger();
}
\u0060\u0060\u0060
## IssueH-14: ERC1155 cannot claim royalties on L2.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/456)  
Found by: 0xdice91, BugPull, OpaBatyo, Ruhum, Thanos, h2134, heeze, novaman33, zzykxx


[Link to Code](https://github.com/sherlock-audit/2024-08-flayer/blob/main/moongate/src/InfernalRiftBelow.sol#L220-L232)  
The royalty claim function is designed to allow owners of collections deployed on L2 to claim their royalties on L1. However, this function only supports collections using the ERC721 standard. If the collection is an ERC1155, the function reverts due to a check in isDeployedOnL2, preventing the owner from claiming their royalties.


The function claimRoyalties checks if a collection is deployed on L2 using the isDeployedOnL2 function. This check only passes if the collection is an ERC721 standard. When an ERC1155 collection is used as the _collectionAddress, the function reverts because the check fails. As a result, owners of ERC1155 collections are unable to claim their royalties.

**NOTE:** The ERC1155 Bridgable contract implements claimRoyalty function: [Link to Code](https://github.com/sherlock-audit/2024-08-flayer/blob/main/moongate/src/libs/ERC155Bridgable.sol#L104-L135)

## POC:

\u0060\u0060\u0060solidity
// on L1
function claimRoyalties(address _collectionAddress, address _recipient, address[] calldata _tokens, uint32 _gasLimit) external {
    //...
    @>>>   ICrossDomainMessenger(L1_CROSS_DOMAIN_MESSENGER).sendMessage(
                INFERNAL_RIFT_BELOW,
                abi.encodeCall(IInfernalRiftBelow.claimRoyalties, (_collectionAddress, _recipient, _tokens)),
                _gasLimit
            );
    //...
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function claimRoyalties(address _collectionAddress, address _recipient, address[] calldata _tokens) public {
    // Ensure that our message is sent from the L1 domain messenger
    if (ICrossDomainMessenger(msg.sender).xDomainMessageSender() != INFERNAL_RIFT_ABOVE) {
        revert CrossChainSenderIsNotRiftAbove();
    }
    // Get our L2 address from the L1
    // revert will happen here because passing ERC1155 _collectionAddress with false to isDeployedOnL2
    // will check if ERC721Bridgable is deployed not ERC1155Bridgable.
    // so calling claimRoyalties will cause revert.
    if (!isDeployedOnL2(_collectionAddress, false)) revert L1CollectionDoesNotExist();
    // Call our ERC721Bridgable contract as the owner to claim royalties to the recipient
    ERC721Bridgable(l2AddressForL1Collection(_collectionAddress, false)).claimRoyalties(_recipient, _tokens);
    emit RoyaltyClaimFinalized(_collectionAddress, _recipient, _tokens);
}
\u0060\u0060\u0060

The inability of ERC1155 owners to claim royalties results in a loss of expected income for the collection owners.

Add logic to handle ERC1155 collection address.

\u0060\u0060\u0060solidity
function claimRoyalties(address _collectionAddress, address _recipient, address[] calldata _tokens) public {
    // Ensure that our message is sent from the L1 domain messenger
    if (ICrossDomainMessenger(msg.sender).xDomainMessageSender() != INFERNAL_RIFT_ABOVE) {
        revert CrossChainSenderIsNotRiftAbove();
    }
    // Get our L2 address from the L1
    if (isDeployedOnL2(_collectionAddress, false)) {
        // Call our ERC721Bridgable contract as the owner to claim royalties to the recipient
        ERC721Bridgable(l2AddressForL1Collection(_collectionAddress, false)).claimRoyalties(_recipient, _tokens);
    }
}
\u0060\u0060\u0060
emit RoyaltyClaimFinalized(_collectionAddress, _recipient, _tokens);
}
else if (isDeployedOnL2(_collectionAddress, true)) {
// Call our ERC1155Bridgable contract as the owner to claim royalties to
// the recipient
ERC1155Bridgable(l2AddressForL1Collection(_collectionAddress, true)).claimRoyalties(_recipient, _tokens);
emit RoyaltyClaimFinalized(_collectionAddress, _recipient, _tokens);
}
else {
revert L1CollectionDoesNotExist();
}
## Issue H-15: Protected listings checkpoints aren\u0027t always updated when the total supply changes

Source: [GitHub Issue #515](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/515)  
Found by: Ironsidesec, Sentryx, valuevalk, zzykxx  

The protocol doesn\u0027t update protected listings checkpoints every time the total supply of collection tokens changes.

The Protected Listing contract uses a checkpoint system to keep track of the interests to pay. It calculates the current interest rate of a collection based on the utilization rate, which depends, among other factors, on the total supply of collection tokens. For this system to work correctly every time the total supply changes, a new checkpoint for the collection should be created, but this is not the case as both \u0060Locker::deposit()\u0060 and \u0060Locker::redeem()\u0060, which mint and burn collection tokens, don\u0027t create a new checkpoint in the protected listing contract. Another case where this happens is the \u0060UniswapImplementation::afterSwap()\u0060 hook, where collection tokens can be burned.

No response  

No response  

This is a problem by itself, as users will pay a wrong interest rate, but it can also be taken advantage of to force users to pay a huge amount of interest or get their protected.
## Listings Liquidated:
1. Alice creates a new protected listing via \u0060ProtectedListings::createListings()\u0060. This is the first protected listing of the collection and as such she expects a low interest rate.
2. Eve, a liquidity provider, flashloans all of the collection tokens currently in the UniswapV4 pool.
3. Eve calls \u0060Locker::redeem()\u0060 in order to burn all of the flashloaned collection tokens in the exchange for NFTs. This lowers the total supply of collection tokens and increases the utilization rate.
4. Eve calls \u0060Listings::cancelListings()\u0060 by passing as an empty array as token ids. This creates a checkpoint for the collection.
5. Eve calls \u0060Locker::deposit()\u0060 in order to re-deposit the NFT collected during point 3 in exchange for collection tokens.
6. Eve adds the collection tokens back to the UniV4 pool.

This results in Alice having to pay a higher interest rate than expected, which is profitable for Eve, or have her NFT liquidated if the interest rate is so high that the position becomes liquidatable in much less time than she expects.

The worst situation possible is for Alice to create a protected listing by borrowing 1 wei of tokens in a collection that\u0027s just been created and whose whole total supply is locked in the UniswapV4 pool. Eve would be able to create a situation where:
1. The total supply is 1 (Alice\u0027s borrowed token)
2. The amount of listings is 1 (Alice\u0027s listing)

Which would result in a utilization rate of:
\u0060\u0060\u0060
(listingsOfType_ * 1e36 * 10 ** collectionToken.denomination()) / totalSupply
(1 * 1e36 * 10 ** 0) / 1
1e36
\u0060\u0060\u0060

Since the checkpoints are not correctly updated users will pay a wrong interest rate on protected listings no matter what. An attacker can abuse this to artificially inflate the utilization rate, which is profitable when the attacker is also a liquidity provider in the UniV4 pool.

No response.

Correctly update collection checkpoints whenever the total supply of collection token changes.
## Issue H-16: The relist function does not check whether the listing is a liquidation listing causing users to pay taxes and refunds being paid to the listing owner who did not pay taxes

Source: [GitHub Issue #547](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/547)

Found by:  
0x37, 0xAlix2, 0xNirix, BADROBINX, BugPull, Ollam, Sentryx, Tendency, almantare, almurhasan, araj, blockchain555, h2134, kuprum, merlinboii, t.aksoy, utsav, valuevalk, zzykxx


Since liquidated listings are created without the original owner paying taxes, the lack of a check for the liquidation status means the system might incorrectly process a tax refund for a listing that was liquidated, allowing the original owner to receive funds they should not be entitled to.


Liquidated listings are created without the original owner paying taxes. If the system lacks a check for liquidation status, it might process a tax refund incorrectly. The absence of a liquidation status check can lead to the original owner receiving tax refunds for liquidated listings, which they are not entitled to. This creates an opportunity for the owner to receive funds improperly. 

The problem arises because the relist function does not check if the listing being relisted was from a liquidation or not, therefore causing the “relister” to pay taxes and the contract depositing refunds to the “liquidated user” who did not pay taxes.


Without checking liquidation status, the system may wrongly process tax refunds for liquidated listings, allowing the original owner to receive undeserved funds. This error could result in a loss of funds within the protocol.
• https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol

\u0060\u0060\u0060solidity
function relist(CreateListing calldata _listing, bool _payTaxWithEscrow) public
    nonReentrant lockerNotPaused {
    // Load our tokenId
    address _collection = _listing.collection;
    uint _tokenId = _listing.tokenIds[0];
    // Read the existing listing in a single read
    Listing memory oldListing = _listings[_collection][_tokenId];
    // Ensure the caller is not the owner of the listing
    if (oldListing.owner == msg.sender) revert CallerIsAlreadyOwner();
    // Load our new Listing into memory
    Listing memory listing = _listing.listing;
    // Ensure that the existing listing is available
    (bool isAvailable, uint listingPrice) = getListingPrice(_collection, _tokenId);
    if (!isAvailable) revert ListingNotAvailable();
    // We can process a tax refund for the existing listing
    (uint _fees,) = _resolveListingTax(oldListing, _collection, true);
    if (_fees != 0) {
        emit ListingFeeCaptured(_collection, _tokenId, _fees);
    }
    // Find the underlying {CollectionToken} attached to our collection
    ICollectionToken collectionToken = locker.collectionToken(_collection);
    // If the floor multiple of the original listings is different, then this needs
    // to be paid to the original owner of the listing.
    uint listingFloorPrice = 1 ether * 10 ** collectionToken.denomination();
    if (listingPrice > listingFloorPrice) {
        unchecked {
            collectionToken.transferFrom(msg.sender, oldListing.owner, listingPrice - listingFloorPrice);
        }
    }
    // Validate our new listing
    _validateCreateListing(_listing);
    // Store our listing into our Listing mappings
    _listings[_collection][_tokenId] = listing;
    // Pay our required taxes
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
payTaxWithEscrow(address(collectionToken), getListingTaxRequired(listing, _collection), _payTaxWithEscrow);
// Emit events
emit ListingRelisted(_collection, _tokenId, listing);
\u0060\u0060\u0060

**Tool used**  
Manual Review

**Recommendation**  
Add a check inside the relist function to prevent taxes being paid for listings that were liquidated.

\u0060\u0060\u0060solidity
// We can process a tax refund for the existing listing
if (!_isLiquidation[_collection][_tokenId]) {
    (uint _fees,) = _resolveListingTax(oldListing, _collection, true);
    if (_fees != 0) {
        emit ListingFeeCaptured(_collection, _tokenId, _fees);
    }
} else {
    delete _isLiquidation[_collection][_tokenId];
}
\u0060\u0060\u0060
