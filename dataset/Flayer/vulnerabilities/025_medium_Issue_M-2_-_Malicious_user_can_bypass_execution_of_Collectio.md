# Issue M-2 - Malicious user can bypass execution of CollectionShutdown function

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** CollectionShutdown, preventShutdown, malicious user, bypass, shutdownVotes, reclaimVote, locker manager, attack path, quorumVotes, shutdown process, smart contract, voting, security, vulnerability, revert, function call, checks, contract logic, exploitation, Ethereum

---

# Issue M-2: Malicious user can bypass execution of CollectionShutdown function

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/113)  
**Found by:** BugPull  

Malicious user bypasses \u0060CollectionShutdown::preventShutdown\u0060 by calling \u0060CollectionShutdown::start\u0060 then \u0060CollectionShutdown::reclaimVote\u0060 making the use of checks in \u0060preventShutdown\u0060 useless.

In \u0060preventShutdown\u0060 function there a check to make sure there isn\u0027t currently a shutdown in progress.

\u0060\u0060\u0060solidity
File: CollectionShutdown.sol
415:      function preventShutdown(address _collection, bool _prevent) public {
416:           // Make sure our user is a locker manager
417:           if (!locker.lockerManager().isManager(msg.sender)) revert ILocker.CallerIsNotManager();
418:
419:           // Make sure that there isn\u0027t currently a shutdown in progress
420:         if (_collectionParams[_collection].shutdownVotes != 0) revert ShutdownProcessAlreadyStarted();
421:
422:           // Update the shutdown to be prevented
423:           shutdownPrevented[_collection] = _prevent;
424:           emit CollectionShutdownPrevention(_collection, _prevent);
425:      }
\u0060\u0060\u0060

This check doesn\u0027t confirm that the shutdown is in progress or not; user can call \u0060CollectionShutdown::start\u0060 to start a shutdown. Then \u0060CollectionShutdown::reclaimVote\u0060 to set \u0060shutdownVotes\u0060 back to 0.

Calling start function indeed increases the votes by calling \u0060_vote\u0060.

\u0060\u0060\u0060solidity
CollectionShutdown.sol#L156-L157
\u0060\u0060\u0060
File: CollectionShutdown.sol

\u0060\u0060\u0060solidity
function start(address _collection) public whenNotPaused {
    //code
\u0060\u0060\u0060

In \u0060_votes\u0060 the count of \u0060shutdownVotes\u0060 increases which is normal  
CollectionShutdown.sol#L200-L201

File: CollectionShutdown.sol

\u0060\u0060\u0060solidity
function _vote(address _collection, CollectionShutdownParams memory params) internal returns (CollectionShutdownParams memory) {
    //code
\u0060\u0060\u0060

There is no prevention for the use initiated the shutdown from calling \u0060reclaimVote\u0060.  
CollectionShutdown.sol#L369-L370

File: CollectionShutdown.sol

\u0060\u0060\u0060solidity
function reclaimVote(address _collection) public whenNotPaused {
    //code
\u0060\u0060\u0060

This line resets back the \u0060shutdownVotes\u0060 to 0  
Making \u0060CollectionShutdown::preventShutdown\u0060 checks useless.  

**Internal pre-conditions**
- \u0060lockerManager\u0060 calling \u0060CollectionShutdown::preventShutdown\u0060.

**Attack Path 1**
1. \u0060lockerManager\u0060 calling \u0060CollectionShutdown::preventShutdown\u0060.
2. Malicious user front runs the \u0060CollectionShutdown::preventShutdown\u0060 by calling \u0060CollectionShutdown::start\u0060 and \u0060CollectionShutdown::reclaimVote\u0060.
3. \u0060lockerManager\u0060 believes this collection is prevented from shutdown but it\u0027s not.

**Attack Path 2**
1. Malicious user calling \u0060CollectionShutdown::start\u0060 and \u0060CollectionShutdown::reclaimVote\u0060.
## lockerManager calling Collection Shutdown

Bypass preventShutdown function making it useless.

- When doing a shutdown check for quorumVotes or check during vote() that the collection is prevented from shutdown.
  
Change the check in preventShutdown.
- if (_collectionParams[_collection].shutdownVotes != 0) revert
  → ShutdownProcessAlreadyStarted();
- if (_collectionParams[_collection].quorumVotes != 0) revert
  → ShutdownProcessAlreadyStarted();
## Issue M-3: ERC721 Airdrop item can be redeemed/swapped out by user who is not an authorised claimant

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/124)  
**Found by:** h2134  

ERC721 airdrop item can be redeemed/swapped out by user who is not an authorised claimant.

Locker contract owner calls \u0060requestAirdrop()\u0060 to claim airdrop from external contracts. The airdropped items can be ERC20, ERC721, ERC1155 or Native ETH, and these items are only supposed to be claimed by authorised claimants. Unfortunately, if the airdropped item is ERC721, a malicious user can bypass the restriction and claim the item by calling \u0060redeem()\u0060 / \u0060swap()\u0060, despite they are not the authorised claimant.

Consider the following scenario:
1. A highly valuable ERC721 collection item is claimed by Locker contract in an airdrop;
2. Bob creates a collection in Locker contract against this ERC721 collection;
3. Bob swaps the airdropped item by using a floor collection item;
4. By doing that, Bob is able to claim the airdropped item even if he is not the authorised claimant.

Please run the PoC in \u0060Locker.t.sol\u0060 to verify:

\u0060\u0060\u0060solidity
function testAudit_RedeemAirdroppedItem() public {
    // Airdrop ERC721
    ERC721WithAirdrop erc721d = new ERC721WithAirdrop();
    // Owner requests to claim a highly valuable airdropped item
    locker.requestAirdrop(address(erc721d),
        abi.encodeWithSignature("claimAirdrop()"));
    assertEq(erc721d.ownerOf(888), address(locker));
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
address bob = makeAddr("Bob");
erc721d.mint(bob, 1);
// Bob creates a Locker collection against the airdrop collection
vm.prank(bob);
address collectionToken = locker.createCollection(address(erc721d), "erc721d", "erc721d", 0);
// Bob swaps out the airdropped item
vm.startPrank(bob);
erc721d.approve(address(locker), 1);
locker.swap(address(erc721d), 1, 888);
vm.stopPrank();
// Bob owns the airdropped item despite he is not the authorised claimant
assertEq(erc721d.ownerOf(888), address(bob));
\u0060\u0060\u0060

An airdropped ERC721 item can be stolen by a malicious user; the authorised claimant won\u0027t be able to make a claim.

[Locker.sol#L198](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Locker.sol#L198)  
[Locker.sol#L241](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Locker.sol#L241)

Manual Review

Should not allow arbitrary user to redeem/swap the airdropped item.
## Issue M-4: Admin can not set the pool fee since it is only set in memory

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/188)  
Found by: Ironsidesec, ZeroTrust, alexzoid, g, h2134, tvdung94, zarkk01

The pool fee is only set in memory and not in storage so specific pool fees will not apply.

The pool fee is only stored in memory.  
ref: UniswapImplementation:setFee()
\u0060\u0060\u0060solidity
// @audit poolParams is only stored in memory so the new fee is not set in
// permanent storage
PoolParams memory poolParams = _poolParams[_poolId];
poolParams.poolFee = _fee;
\u0060\u0060\u0060

1. Admin calls with any fee value.

None

None

Specific pool fees will not apply. Only the default fee will apply to swaps.  
ref: UniswapImplementation::getFee()
\u0060\u0060\u0060solidity
// @audit poolFee will always be 0
uint24 poolFee = _poolParams[_poolId].poolFee;
if (poolFee != 0) {
  fee_ = poolFee;
}
\u0060\u0060\u0060

**PoC**  
No response

**Mitigation**  
Use storage instead of memory for poolParams.
## IssueM-5: ERC1155Bridgable is not EIP-1155 compliant

Source: [https://github.com/sherlock-audit/2024-08-flayer-judging/issues/202](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/202)  
The protocol has acknowledged this issue.  
Found by Composable Security, Spearmint, kuprum  


According to the README:  
The Bridged1155 should be strictly compliant with EIP-1155 and EIP-2981.  
EIP-1155 states the following about ERC1155Metadata_URI extension:  
The optional ERC1155Metadata_URI extension can be identified with the ERC-165 Standard Interface Detection.  
If the optional ERC1155Metadata_URI extension is included:  
- The ERC-165 supportsInterface function MUST return the constant value true if 0x0e89341c is passed through the interfaceID argument.  
- Changes to the URI MUST emit the URI event if the change can be expressed with an event (i.e. it isn’t dynamic/programmatic).  

But we see that:  
- ERC1155Bridgable does support the extension, and returns the required constant via supportsInterface.  
- It does not emit the URI event as required, when it\u0027s changed via function setTokenURIAndMintFromRiftAbove:

\u0060\u0060\u0060solidity
function setTokenURIAndMintFromRiftAbove(uint _id, uint _amount, string memory _uri, address _recipient) external {
    if (msg.sender != INFERNAL_RIFT_BELOW) {
        revert NotRiftBelow();
    }
    // Set our tokenURI
    uriForToken[_id] = _uri;
    // Mint the token to the specified recipient
}
\u0060\u0060\u0060
_mint(_recipient, _id, _amount, \u0027\u0027);
}
Notice that when bridging the ERC-1155 tokens, URIs are retrieved from the corresponding token contract by Internal Rift Above, and encoded into the package as follows:

\u0060\u0060\u0060solidity
// Go through each NFT, set its URI and escrow it
uris = new string[](numIds);
for (uint j; j < numIds; ++j) {
    // Ensure we have a valid amount passed (TODO: Is this needed?)
    tokenAmount = params.amountsToCross[i][j];
    if (tokenAmount == 0) {
        revert InvalidERC1155Amount();
    }
    uris[j] = erc1155.uri(params.idsToCross[i][j]);
    erc1155.safeTransferFrom(msg.sender, address(this), params.idsToCross[i][j],
        params.amountsToCross[i][j], \u0027\u0027);
}
// Set up payload
package[i] = Package({
    chainId: block.chainid,
    collectionAddress: collectionAddress,
    ids: params.idsToCross[i],
    amounts: params.amountsToCross[i],
    uris: uris,
    royaltyBps: _getCollectionRoyalty(collectionAddress, params.idsToCross[i][0]),
    name: \u0027\u0027,
    symbol: \u0027\u0027
});
\u0060\u0060\u0060

I.e. the information is properly retrieved, transferred, and is available; but the URI event is not emitted as required; this breaks the specification.

Protocols integrating with ERC1155 Bridgable may work incorrectly.

Compare the URIs supplied for an NFT in function setTokenURIAndMintFromRiftAbove, and if it has changed -- emit the URI event as required per the specification.
## Issue M-6: The unused tokens from the user’s initialization of UniswapV4‘s pool will be locked in the UniswapImplementation contract.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/208)

Found by: 0x37, 0xHappy, 0xNilesh, 0xc0ffEE, 0xlucky, BADROBINX, BugPull, ComposableSecurity, Ironsidesec, KingNFT, Ollam, ZeroTrust, blockchain555, h2134, merlinboii, novaman33, shaflow01, wickie, zarkk01, zzykxx

The unused tokens from the user’s initialization of UniswapV4‘s pool will be locked in the UniswapImplementation contract.

\u0060\u0060\u0060solidity
function initializeCollection(address _collection, uint _amount0, uint _amount1,
    uint _amount1Slippage, uint160 _sqrtPriceX96) public override {
    // Ensure that only our {Locker} can call initialize
    if (msg.sender != address(locker)) revert CallerIsNotLocker();
    // Ensure that the PoolKey is not empty
    PoolKey memory poolKey = _poolKeys[_collection];
    if (poolKey.tickSpacing == 0) revert UnknownCollection();
    // Initialise our pool
    poolManager.initialize(poolKey, _sqrtPriceX96, \u0027\u0027);
    // After our contract is initialized, we mark our pool as initialized and emit
    // our first state update to notify the UX of current prices, etc.
    PoolId id = poolKey.toId();
    _emitPoolStateUpdate(id);
    // Load our pool parameters and update the initialized flag
    PoolParams storage poolParams = _poolParams[id];
    poolParams.initialized = true;
}
\u0060\u0060\u0060
// Obtain the UV4 lock for the pool to pull in liquidity
poolManager.unlock(
    abi.encode(CallbackData({
        poolKey: poolKey,
        liquidityDelta: LiquidityAmounts.getLiquidityForAmounts({
            sqrtPriceX96: _sqrtPriceX96,
            sqrtPriceAX96: TICK_SQRT_PRICEAX96,
            sqrtPriceBX96: TICK_SQRT_PRICEBX96,
            amount0: poolParams.currencyFlipped ? _amount1 : _amount0,
            amount1: poolParams.currencyFlipped ? _amount0 : _amount1
        }),
        liquidityTokens: _amount1,
        liquidityTokenSlippage: _amount1Slippage
    })
));

This function calls UniswapV4’s poolManager.unlock().
function unlock(bytes calldata data) external override returns (bytes memory result) {
    if (Lock.isUnlocked()) AlreadyUnlocked.selector.revertWith();
    Lock.unlock();
    // the caller does everything in this callback, including paying what they
    owe via calls to settle
    result = IUnlockCallback(msg.sender).unlockCallback(data);
    if (NonzeroDeltaCount.read() != 0) CurrencyNotSettled.selector.revertWith();
    Lock.lock();
}

And in poolManager.unlock(), the unlockCallback() function of Uniswap Implementation is called.
function _unlockCallback(bytes calldata _data) internal override returns (bytes memory) {
    // Unpack our passed data
    CallbackData memory params = abi.decode(_data, (CallbackData));
    // As this call should only come in when we are initializing our pool, we
    // don\u0027t need to worry about \u0060take\u0060 calls, but only \u0060settle\u0060 calls.
    (BalanceDelta delta,) = poolManager.modifyLiquidity({
        key: params.poolKey,
        params: IPoolManager.ModifyLiquidityParams({
            tickLower: MIN_USABLE_TICK,
            tickUpper: MAX_USABLE_TICK,
            liquidityDelta: int(uint(params.liquidityDelta)),
\u0060\u0060\u0060solidity
salt: \u0027\u0027
}),
hookData: \u0027\u0027
});
// Check the native delta amounts that we need to transfer from the contract
if (delta.amount0() < 0) {
    _pushTokens(params.poolKey.currency0, uint128(-delta.amount0()));
}
// Check our ERC20 donation
if (delta.amount1() < 0) {
    _pushTokens(params.poolKey.currency1, uint128(-delta.amount1()));
}
// If we have an expected amount of tokens being provided as liquidity,
// need to ensure that this exact amount is sent. There may be some dust
// lost during rounding and for this reason we need to set a small slippage
// tolerance on the checked amount.
if (params.liquidityTokens != 0) {
    uint128 deltaAbs = _poolParams[params.poolKey.toId()].currencyFlipped ?
        uint128(-delta.amount0()) : uint128(-delta.amount1());
    if (params.liquidityTokenSlippage < params.liquidityTokens - deltaAbs) {
        revert IncorrectTokenLiquidity(
            deltaAbs,
            params.liquidityTokenSlippage,
            params.liquidityTokens
        );
    }
}
// We return our \u0060BalanceDelta\u0060 response from the donate call
return abi.encode(delta);
}
\u0060\u0060\u0060

In the above code, \u0060_pushTokens()\u0060 transfers the required amounts of currency0 and currency1 (i.e., nativeToken and collectionToken) from the UniswapImplementation contract to the poolManager contract in UniswapV4.

\u0060\u0060\u0060solidity
function getLiquidityForAmounts(
    uint160 sqrtPriceX96,
    uint160 sqrtPriceAX96,
    uint160 sqrtPriceBX96,
    uint256 amount0,
    uint256 amount1
) internal pure returns (uint128 liquidity) {
    if (sqrtPriceAX96 > sqrtPriceBX96) (sqrtPriceAX96, sqrtPriceBX96) =
        (sqrtPriceBX96, sqrtPriceAX96);
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
if (sqrtPriceX96 <= sqrtPriceAX96) {
    liquidity = getLiquidityForAmount0(sqrtPriceAX96, sqrtPriceBX96, amount0);
} else if (sqrtPriceX96 < sqrtPriceBX96) {
    uint128 liquidity0 = getLiquidityForAmount0(sqrtPriceX96, sqrtPriceBX96, amount0);
    uint128 liquidity1 = getLiquidityForAmount1(sqrtPriceAX96, sqrtPriceX96, amount1);
    liquidity = liquidity0 < liquidity1 ? liquidity0 : liquidity1;
} else {
    liquidity = getLiquidityForAmount1(sqrtPriceAX96, sqrtPriceBX96, amount1);
}
\u0060\u0060\u0060

From \u0060LiquidityAmounts.getLiquidityForAmounts()\u0060 in Uniswap V4, we can see that the amounts of currency0 and currency1 might not be fully utilized, and one of the tokens will always have a leftover amount. In the \u0060UniswapImplementation::_unlockCallback()\u0060 function, there is no operation to return the leftover tokens to the \u0060msg.sender\u0060 (i.e., the Locker). It only compares the leftover \u0060collectionToken\u0060 with the \u0060liquidityTokenSlippage\u0060, and if the leftover \u0060collectionToken\u0060 exceeds the \u0060liquidityTokenSlippage\u0060, the entire operation will revert.

This only ensures that the remaining amount of \u0060collectionToken\u0060 is within the user’s control. However, the leftover tokens (either \u0060nativeToken\u0060 or \u0060collectionToken\u0060) will remain permanently locked in the \u0060UniswapImplementation\u0060 contract.

The user loses the leftover tokens.

- [UniswapImplementation.sol#L205](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/implementation/UniswapImplementation.sol#L205)
- [UniswapImplementation.sol#L376](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/implementation/UniswapImplementation.sol#L376)

Manual Review

Add handling for refunding the leftover tokens.
## Issue M-7: ERC721Bridgable and ERC1155Bridgable are not EIP-2981 compliant, and fail to correctly collect or attribute royalties to artists

Source: [https://github.com/sherlock-audit/2024-08-flayer-judging/issues/214](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/214)  
The protocol has acknowledged this issue.  
Found by Ruhum, h2134, kuprum, novaman33, rndquu, zzykxx  


According to the README:

The Bridged721 should be strictly compliant with EIP-721 and EIP-2981.  
The Bridged1155 should be strictly compliant with EIP-1155 and EIP-2981.  

EIP-2981 states the following:

Marketplaces that support this standard MUST pay royalties no matter where the sale occurred or in what currency, including on-chain sales, over-the-counter (OTC) sales and off-chain sales such as at auction houses.  
As royalty payments are voluntary, entities that respect this EIP must pay no matter where the sale occurred - a sale conducted outside of the blockchain is still a sale.  

The crux of the standard is that if a contract is EIP-2981 compliant, the royalty should be paid to the artist who created the NFT no matter where the sale occurred. For that it first needs to be correctly reported to marketplaces, and attributed to the artist. It\u0027s worth noting that as returned by the EIP-2981 function royaltyInfo, both the royalty recipient and the royalty amount are specific to each NFT:

\u0060\u0060\u0060solidity
function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view returns (address receiver, uint256 royaltyAmount);
\u0060\u0060\u0060

The problem is that both ERC721Bridgable and ERC1155Bridgable completely violate this crucial property via both setting a uniform royalty amount across all NFTs, and designating themselves as the royalty recipient, thus reporting wrong amounts, and mixing them together in a single bucket. This makes it impossible to either correctly collect the appropriate royalty amounts, or to attribute the collected royalties to artists.

Both ERC721Bridgable and ERC1155Bridgable perform the following in their initialize function:

\u0060\u0060\u0060solidity
// Set this contract to receive marketplace royalty
_setDefaultRoyalty(address(this), _royaltyBps);
\u0060\u0060\u0060

As per NFT royalties are not set, this makes the contract a single recipient of the same royalty Bps across all NFTs, as implemented by OZ\u0027s ERC2981 contract. No matter what happens next, it\u0027s impossible to either correctly collect the appropriate royalty amounts at marketplaces, or to correctly attribute the royalties to different artists.


Definite loss of funds (NFT creators won\u0027t receive the appropriate royalties):
- Marketplaces who sell NFTs on L2s are not able to pay correct amounts of royalties
- Artists who created the NFTs in collections on L1, which are bridged to L2, are not able to track the amounts of royalties they have the right to receive (which effectively deprives them of said royalties)


Both for ERC721Bridgable and ERC1155Bridgable have to implement a system which:
- correctly reports per-NFT royalty amounts on L2 via royaltyInfo
- correctly collects the appropriate royalty amounts, and tracks the per-NFT recipients of said amounts on L1.

Notice: this finding concerns only with the absence of the correct tracking and reporting system as per EIP-2981. Royalty distribution system from L2 to L1 is out of scope of this finding.
## Issue M-8: There is a logical error in the removeFeeExemption() function.

Source: [GitHub Issue #219](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/219)

Found by: 0xc0ffEE, BugPull, Ironsidesec, NoOne, Tendency, ZeroTrust, alexzoid, cawfree, g, h2134, kuprum, stuart_the_minion, valuevalk, xKeywordx, zzykxx


There is a logical error in the removeFeeExemption() function, causing \u0060feeOverrides[_beneficiary]\u0060 to never be removed.


\u0060\u0060\u0060solidity
function removeFeeExemption(address _beneficiary) public onlyOwner {
    // Check that a beneficiary is currently enabled
    uint24 hasExemption = uint24(feeOverrides[_beneficiary] & 0xFFFFFF);
    if (hasExemption != 1) {
        revert NoBeneficiaryExemption(_beneficiary);
    }
    delete feeOverrides[_beneficiary];
    emit BeneficiaryFeeRemoved(_beneficiary);
}
\u0060\u0060\u0060

Through \u0060setFeeExemption()\u0060, we know that the lower 24 bits of \u0060feeOverrides[_beneficiary]\u0060 are set to \u00600xFFFFFF\u0060. Therefore, the expression \u0060uint24 hasExemption = uint24(feeOverrides[_beneficiary] & 0xFFFFFF)\u0060 results in \u00600xFFFFFF & 0xFFFFFF = 0xFFFFFF\u0060. As a result, \u0060hasExemption\u0060 will never be \u00601\u0060, causing \u0060removeFeeExemption()\u0060 to always revert. Consequently, \u0060feeOverrides[_beneficiary]\u0060 will never be removed.

\u0060\u0060\u0060solidity
function setFeeExemption(address _beneficiary, uint24 _flatFee) public onlyOwner {
    // Ensure that our custom fee conforms to Uniswap V4 requirements
    if (!_flatFee.isValid()) {
        revert FeeExemptionInvalid(_flatFee, LPFeeLibrary.MAX_LP_FEE);
    }
    // We need to be able to detect if the zero value is a flat fee being
    // applied to the user, or it just hasn\u0027t been set. By packing the \u00601\u0060 in the latter
    \u0060uint24\u0060
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// we essentially get a boolean flag to show this.
feeOverrides[_beneficiary] = uint48(_flatFee) << 24 | 0xFFFFFF;
emit BeneficiaryFeeSet(_beneficiary, _flatFee);
\u0060\u0060\u0060

Since \u0060feeOverrides[_beneficiary]\u0060 cannot be removed, the user continues to receive reduced fee benefits, leading to partial fee losses for LPs and the protocol.

[UniswapImplementation.sol#L749](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/implementation/UniswapImplementation.sol#L749)  
[UniswapImplementation.sol#L729](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/implementation/UniswapImplementation.sol#L729)

Manual Review

\u0060\u0060\u0060solidity
function removeFeeExemption(address _beneficiary) public onlyOwner {
    // Check that a beneficiary is currently enabled
    uint24 hasExemption = uint24(feeOverrides[_beneficiary] & 0xFFFFFF);
    if (hasExemption != 0xFFFFFF) {
        revert NoBeneficiaryExemption(_beneficiary);
    }
    delete feeOverrides[_beneficiary];
    emit BeneficiaryFeeRemoved(_beneficiary);
}
\u0060\u0060\u0060
