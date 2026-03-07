# Issue M-19: Low TVL and high Leverage Supply will DoS the redeem of Leverage tokens

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** Low TVL, high Leverage Supply, DoS, redeem, Leverage tokens, underflow, getRedeemAmount, multiplication, division, asset Supply, TVL, PRECISION, Bond supply, collateral level, redemption, tokens, governance, user, mint, approve

---

# Issue M-19: Low TVL and high Leverage Supply will DoS the redeem of Leverage tokens

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/1039)  
Found by: 0xc0ffEE, 0xe4669da, CL001, Goran, KupiaSec, dobrevaleri, elvin.a.block, future, zxriptor

Low TVL and high Leverage Supply might lead to DoS of the Leverage tokens redemption, due to underflow.

In \u0060getRedeemAmount\u0060, there is multiplication after division, which might lead to underflow. (ref). This can happen when the asset Supply is higher than the TVL * PRECISION.

1. There should be high Leverage Supply
2. The Bond supply and the TVL should be just enough, so that the collateral level is above 1.2.

No response

1. User redeems any number of Leverage Tokens.

User will be unable to redeem his Leverage tokens.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.26;
import {Test, console} from "forge-std/Test.sol";
import {Pool} from "src/Pool.sol";
import {Token} from "test/mocks/Token.sol";
import {Utils} from "src/lib/Utils.sol";
import {Auction} from "src/Auction.sol";
import {BondToken} from "src/BondToken.sol";
import {PoolFactory} from "src/PoolFactory.sol";
import {Distributor} from "src/Distributor.sol";
import {OracleFeeds} from "src/OracleFeeds.sol";
import {LeverageToken} from "src/LeverageToken.sol";
import {Deployer} from "src/utils/Deployer.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {UpgradeableBeacon} from "@openzeppelin/contracts/proxy/beacon/UpgradeableBeacon.sol";
import {PausableUpgradeable} from "@openzeppelin/contracts-upgradeable/utils/PausableUpgradeable.sol";
import {MockPriceFeed} from "test/mocks/MockPriceFeed.sol";

contract PoolPoC is Test {
    error ZeroLeverageSupply();
    Pool pool;
    Token reserve;
    BondToken bond;
    LeverageToken lev;
    address governance = address(0x1);
    address user = address(0x2);
    uint256 constant RESERVE_AMOUNT = 13 ether;
    uint256 private constant CHAINLINK_DECIMAL_PRECISION = 10 ** 8;
    uint8 private constant CHAINLINK_DECIMAL = 8;

    function setUp() public {
        vm.startPrank(governance);
        address deployer = address(new Deployer());
        address oracleFeeds = address(new OracleFeeds());
        address poolBeacon = address(new UpgradeableBeacon(address(new Pool()), governance));
        address bondBeacon = address(new UpgradeableBeacon(address(new BondToken()), governance));
    }
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
address levBeacon = address(new UpgradeableBeacon(address(new LeverageToken()), governance));
address distributorBeacon = address(new UpgradeableBeacon(address(new Distributor()), governance));
reserve = new Token("Balancer Pool Token", "balancerPoolToken", false);
Token coupon = new Token("Coupon Token", "couponToken", false);
// Deploy a mock price feed for the reserve token
MockPriceFeed mockPriceFeed = new MockPriceFeed();
mockPriceFeed.setMockPrice(100 * int256(CHAINLINK_DECIMAL_PRECISION), uint8(CHAINLINK_DECIMAL));
// Set the price feed for the reserve token
OracleFeeds(oracleFeeds).setPriceFeed(address(reserve), address(0), address(mockPriceFeed), 1 days);
// Deploy the pool factory
PoolFactory poolFactory = PoolFactory(
    Utils.deploy(
        address(new PoolFactory()),
        abi.encodeCall(
            PoolFactory.initialize,
            (governance, deployer, oracleFeeds, poolBeacon, bondBeacon, levBeacon, distributorBeacon)
        )
    )
);
// Prepare the pool parameters
PoolFactory.PoolParams memory params;
params.fee = 0;
params.reserveToken = address(reserve);
params.sharesPerToken = 2500000;
params.distributionPeriod = 90 days;
params.couponToken = address(coupon);
poolFactory.grantRole(poolFactory.GOV_ROLE(), governance);
poolFactory.grantRole(poolFactory.POOL_ROLE(), governance);
// Mint enough tokens for the pool deployment
reserve.mint(governance, RESERVE_AMOUNT);
reserve.approve(address(poolFactory), RESERVE_AMOUNT);
pool = Pool(
    poolFactory.createPool(
        params,
        RESERVE_AMOUNT,
        10 * 10 ** 18,
        1000 * 10 ** 18,
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
                        bond = pool.bondToken();
                        lev = pool.lToken();
                        vm.stopPrank();
                   }
                   function testLowTvlAndLowBondTokenSupplyWillBlockLevTokenRedemption() public {
                        // The Bond and Leverage tokens are minted to the governance, because the
                        // pool is deployed by this address
                        // Using governance we bypass the need to have PreDeposit contract, which
                        // deploys the pool
                        // The tokens from governance are sent to the user, simulating the
                        // PreDeposit claim functionality
                        console.log("Governance lev balance: ", lev.balanceOf(governance));
                        vm.startPrank(governance);
                        lev.transfer(user, lev.balanceOf(governance));
                        vm.stopPrank();
                        console.log("User lev balance: ", lev.balanceOf(user));
                        console.log("Governance lev balance: ", lev.balanceOf(governance));
                        vm.startPrank(user);
                        uint256 amountLev = lev.balanceOf(user);
                        vm.expectRevert(Pool.ZeroAmount.selector);
                        pool.redeem(Pool.TokenType.LEVERAGE, amountLev, 0);
                        console.log("User lev balance after redeem: ", lev.balanceOf(user));
                        console.log("Pool reserve tokens: ", reserve.balanceOf(address(pool)));
                        vm.stopPrank();
                   }
              }
             Logs:
             Mitigation
              if (collateralLevel <= COLLATERAL_THRESHOLD) {
                     redeemRate = ((tvl * multiplier) / assetSupply);
                   } else if (tokenType == TokenType.LEVERAGE) {
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) * PRECISION;
redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) * PRECISION / assetSupply);
} else {
  redeemRate = BOND_TARGET_PRICE * PRECISION;
}
if (marketRate != 0 && marketRate < redeemRate) {
  redeemRate = marketRate;
}
\u0060\u0060\u0060

The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/159](https://github.com/Convexity-Research/plaza-evm/pull/159)
PAGE END
