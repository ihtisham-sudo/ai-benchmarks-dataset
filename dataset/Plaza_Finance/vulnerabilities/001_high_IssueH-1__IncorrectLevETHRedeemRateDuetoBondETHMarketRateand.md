# IssueH-1: IncorrectLevETHRedeemRateDuetoBondETHMarketRateandLevETHRateComparison,LeadingtoTraderLosses

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** LevETH, BondETH, marketRate, redeemRate, traderLosses, withdrawal, Pool, getRedeemAmount, collateralLevel, TokenType, smart contract, Ethereum, financial loss, liquidity, oracle, price feed, trading, decentralized finance, audit, bug

---

# IssueH-1: IncorrectLevETHRedeemRateDuetoBondETHMarketRateandLevETHRateComparison,LeadingtoTraderLosses

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/190)

Found by: 0x23r0, 0xDLG, KupiaSec, OrangeSantra, Ryonen, Waydou, ZoA, alphacipher, bladeee, bretzel, eta, farman1094, momentum, phn210, sl1, tinnohofficial, wickie, zxriptor

Withdrawal of BondETH is dependent on two rates.
1. redeemRate calculated in contract based on real time values.
2. marketRate created through taking the price from Bond Oracle Adapter. Then we compare the both rate and take the lower one to use for withdrawing.

However the market rate is only for BondETH not for LevETH, still we comparing with the LevETH as well which always result in using the BondETH market rate, because it always be lower.
- General Lev redeem rate (625000000) [as per POC]
- Market rate always be up to (100000000)

It\u0027s always result in loss for traders. They are always withdraw the wrong amount.

Link: [GitHub Code](https://github.com/sherlock-audit/2024-12-plaza-finance/blob/main/plaza-evm/src/Pool.sol#L477C2-L525C4)

Issue lies in \u0060Pool::getRedeemAmount\u0060
\u0060\u0060\u0060solidity
if (marketRate != 0 && marketRate < redeemRate) {
    redeemRate = marketRate;
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function getRedeemAmount(
    TokenType tokenType,
    uint256 depositAmount,
    uint256 bondSupply,
    uint256 levSupply,
    uint256 poolReserves,
    uint256 ethPrice,
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint8 oracleDecimals,
uint256 marketRate
) public pure returns(uint256) {
    if (bondSupply == 0) {
        revert ZeroDebtSupply();
    }
    uint256 tvl = (ethPrice * poolReserves).toBaseUnit(oracleDecimals);
    uint256 assetSupply = bondSupply;
    uint256 multiplier = POINT_EIGHT;
    // Calculate the collateral level based on the token type
    uint256 collateralLevel;
    if (tokenType == TokenType.BOND) {
        collateralLevel = ((tvl - (depositAmount * BOND_TARGET_PRICE)) * PRECISION) /
        ((bondSupply - depositAmount) * BOND_TARGET_PRICE);
    } else {
        multiplier = POINT_TWO;
        assetSupply = levSupply;
        collateralLevel = (tvl * PRECISION) / (bondSupply * BOND_TARGET_PRICE);
        if (assetSupply == 0) {
            revert ZeroLeverageSupply();
        }
    }
    // Calculate the redeem rate based on the collateral level and token type
    uint256 redeemRate;
    if (collateralLevel <= COLLATERAL_THRESHOLD) {
        redeemRate = ((tvl * multiplier) / assetSupply);
    } else if (tokenType == TokenType.LEVERAGE) {
        redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) *
        PRECISION;
    } else {
        redeemRate = BOND_TARGET_PRICE * PRECISION;
    }
    if (marketRate != 0 && marketRate < redeemRate) {
        redeemRate = marketRate;
    }
    // Calculate and return the final redeem amount
    return ((depositAmount * redeemRate).fromBaseUnit(oracleDecimals) / ethPrice) /
    PRECISION;
}
\u0060\u0060\u0060
There always be issue as long we are taking market Price.

No pre-conditions required

This issue in core function, issue is exist in all withdrawal order of LevETH as long we are getting Market Rate.

Below is the situation if we mint 1 eth for LevETH and then redeem.
1. When market rate is not working (Redeemed 1 ETH)
2. When market rate is returning value (Redeemed 0.16 ETH)

The trader loss is around 84%.

Make sure to make the market Rate return value. and then not returning value. For initial pool value Healthy rate is considered which used in script/TestnetScript.s.sol

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;
import "forge-std/Test.sol";
import {Pool} from "../src/Pool.sol";
import {Token} from "./mocks/Token.sol";
import {Auction} from "../src/Auction.sol";
import {Utils} from "../src/lib/Utils.sol";
import {MockPool} from "./mocks/MockPool.sol";
import {BondToken} from "../src/BondToken.sol";
import {TestCases} from "./data/TestCases.sol";
import {Decimals} from "../src/lib/Decimals.sol";
import {PoolFactory} from "../src/PoolFactory.sol";
import {Distributor} from "../src/Distributor.sol";
import {OracleFeeds} from "../src/OracleFeeds.sol";
import {Validator} from "../src/utils/Validator.sol";
import {OracleReader} from "../src/OracleReader.sol};
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
import {LeverageToken} from "../src/LeverageToken.sol";
import {MockPriceFeed} from "./mocks/MockPriceFeed.sol";
import {Deployer} from "../src/utils/Deployer.sol";
import {Strings} from "@openzeppelin/contracts/utils/Strings.sol";
import {UpgradeableBeacon} from "@openzeppelin/contracts/proxy/beacon/UpgradeableBeacon.sol";
import {console} from "forge-std/console.sol";

contract PersTest is Test, TestCases {
    using Decimals for uint256;
    using Strings for uint256;

    PoolFactory private poolFactory;
    PoolFactory.PoolParams private params;
    MockPriceFeed private mockPriceFeed;
    address private oracleFeedsContract;
    address private deployer = address(0x1);
    address private minter = address(0x2);
    address private governance = address(0x3);
    address private securityCouncil = address(0x4);
    address private user = address(0x5);
    address private user2 = address(0x6);
    address private user3 = address(0x7);
    address private user4 = address(0x8);
    address private user5 = address(0x9);
    
    BondToken bond;
    Pool pool;
    LeverageToken lev;
    Token rToken;
    
    address public constant ethPriceFeed = address(0x71041dddad3595F9CEd3DcCFBe3D1F4b0a16Bb70);
    uint256 private constant CHAINLINK_DECIMAL_PRECISION = 10**8;
    uint8 private constant CHAINLINK_DECIMAL = 8;

    /**
     * @dev Sets up the testing environment.
     * Deploys the BondToken contract and a proxy, then initializes them.
     * Grants the minter and governance roles and mints initial tokens.
     */
    function setUp() public {
        vm.startPrank(deployer);
        address contractDeployer = address(new Deployer());
        oracleFeedsContract = address(new OracleFeeds());
    }
}
\u0060\u0060\u0060
address poolBeacon = address(new UpgradeableBeacon(address(new Pool()),
            governance));
address bondBeacon = address(new UpgradeableBeacon(address(new BondToken()),
            governance));
address levBeacon = address(new UpgradeableBeacon(address(new LeverageToken()),
            governance));
address distributorBeacon = address(new UpgradeableBeacon(address(new
            Distributor()), governance));
poolFactory = PoolFactory(Utils.deploy(address(new PoolFactory()),
            abi.encodeCall(
                 PoolFactory.initialize,
                 (governance, contractDeployer, oracleFeedsContract, poolBeacon, bondBeacon,
            levBeacon, distributorBeacon)
               )));
params.fee = 0;
params.feeBeneficiary = governance;
params.reserveToken = address(new Token("Wrapped ETH", "WETH", false));
params.sharesPerToken = 2_500_000;
params.distributionPeriod = 7776000;
params.couponToken = address(new Token("USDC", "USDC", false));
OracleFeeds(oracleFeedsContract).setPriceFeed(params.reserveToken, address(0),
            ethPriceFeed, 1 days);
// Deploy the mock price feed
mockPriceFeed = new MockPriceFeed();
// Use vm.etch to deploy the mock contract at the specific address
bytes memory bytecode = address(mockPriceFeed).code;
vm.etch(ethPriceFeed, bytecode);
// Set oracle price
mockPriceFeed = MockPriceFeed(ethPriceFeed);
mockPriceFeed.setMockPrice(3125 * int256(CHAINLINK_DECIMAL_PRECISION),
            uint8(CHAINLINK_DECIMAL));
vm.stopPrank();
vm.startPrank(governance);
poolFactory.grantRole(poolFactory.POOL_ROLE(), governance);
poolFactory.grantRole(poolFactory.SECURITY_COUNCIL_ROLE(), securityCouncil);
vm.stopPrank();
}
function testMarketRateImbalance() public {
vm.startPrank(governance);
rToken = Token(params.reserveToken);
\u0060\u0060\u0060solidity
// Mint reserve tokens
rToken.mint(governance, 100 ether);
rToken.approve(address(poolFactory), 100 ether);
// Create pool and approve deposit amount
pool = Pool(poolFactory.createPool(params, 100 ether, 2500 ether, 100 ether,
    "", "", "", "", false));
bond = pool.bondToken();
lev = pool.lToken();
assertEq(2500 ether, BondToken(pool.bondToken()).totalSupply());
assertEq(100 ether, LeverageToken(pool.lToken()).totalSupply());
console.log("1st Iteration");
createToken(user, 1 ether, Pool.TokenType.LEVERAGE);
console.log("                 ");
// NOTE Make sure to mock MarketRate to return value.
vm.startPrank(user);
console.log("3rd Iteration LEv Redeem");
uint amount = pool.redeem(Pool.TokenType.LEVERAGE, lev.balanceOf(user), 1);
console.log("Amount Redeemed", amount);
console.log("                 ");
assertEq(amount, rToken.balanceOf(user));
vm.stopPrank();
}
function createToken(address inBehalfOf,uint dealAmount, Pool.TokenType tokenType
) internal {
    vm.startPrank(inBehalfOf);
    deal(address(rToken), inBehalfOf, dealAmount );
    rToken.approve(address(pool), dealAmount);
    uint amount = pool.create(tokenType, dealAmount, 1);
    console.log("Amount Minted", amount);
    if(tokenType == Pool.TokenType.BOND){
        assertEq(amount, bond.balanceOf(inBehalfOf));
    } else {
        assertEq(amount, lev.balanceOf(inBehalfOf));
    }
    vm.stopPrank();
}
\u0060\u0060\u0060

Mitigation
There is 2 possible solution
1. To change the code in \u0060Pool::simulateRedeem\u0060 only fetching marketRate if redeem TokenType is Bond.
2. Made changes in \u0060Pool::getRedeemAmount\u0060 comparing marketRate with redeemRate if TokenType is Bond only.

\u0060\u0060\u0060cpp
if (tokenType == TokenType.BOND) {
    if (marketRate != 0 && marketRate < redeemRate) {
        redeemRate = marketRate;
    }
}
\u0060\u0060\u0060

sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/147](https://github.com/Convexity-Research/plaza-evm/pull/147)
