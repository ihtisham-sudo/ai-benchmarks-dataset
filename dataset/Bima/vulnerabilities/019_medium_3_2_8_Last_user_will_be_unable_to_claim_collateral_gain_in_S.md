# 3.2.8 Last user will be unable to claim collateral gain in Stability Pool in some cases

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** StabilityPool, collateral, gain, last user, claim, offset, error, index, sunset, liquidation, reward, deposit, calculation, gains, transfer, contract, test, forge, PoC, issue

---

# 3.2.8 Last user will be unable to claim collateral gain in Stability Pool in some cases
**Submitted by:** T1MOH, also found by pkqs90  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  

**Description:** 
StabilityPool.enableCollateral() will overwrite old collateral index in case that collateral was sunset, this logic is present in _overwriteCollateral() (StabilityPool.sol#L207-L242). The problem is that it doesn\u0027t reset old value of lastCollateralError_Offset in that index. What does this variable mean? It is used to calculate collateral gain per deposit amount, and this specific variable keeps track of the remainder to not always round down calculations. More details are in the comment in StabilityPool.sol#L512-L522.

By the way, a similar issue was previously reported; however, mitigation is insufficient: check 7.3.16 in a Cyfrin report or commit 0915dd49 in Prisma. The problem is that it uses a non-reset value to round up in the future when recalculating collateral gain during offset(). As a result, the total collateral gain distributed will be greater than the actual balance of collateral. This means that the last user to claim reward will be unable to do it.

**Proof of Concept:** Execute with command \u0060forge test --match-test test_custom7_T1MOH -vv\u0060:

\u0060\u0060\u0060diff
192 ~/projects/audit/PoC/bima-v1-core% git diff
diff --git a/contracts/core/StabilityPool.sol b/contracts/core/StabilityPool.sol
index 8f6594e..eea8c8d 100644
--- a/contracts/core/StabilityPool.sol
+++ b/contracts/core/StabilityPool.sol
@@ -10,6 +10,8 @@ import {IStabilityPool, IDebtToken, IBimaVault, IERC20} from "../interfaces/ISta
 import {SafeCast} from "@openzeppelin/contracts/utils/math/SafeCast.sol";
 +import "forge-std/console.sol";
 +
 /**
     @title Bima Stability Pool
     @notice Based on Liquity\u0027s \u0060StabilityPool\u0060
@@ -800,6 +802,8 @@ contract StabilityPool is IStabilityPool, BimaOwnable, SystemStart {
                        collateralGains[collateralIndex] = gains;
                        depositorGains[collateralIndex] = 0;
+                    console.log("gains   %e", gains);
+                    console.log("balance %e", collateralTokens[collateralIndex].balanceOf(address(this)));
                        collateralTokens[collateralIndex].safeTransfer(recipient, gains);
                    }
                    unchecked {
@@ -899,4 +903,8 @@ contract StabilityPool is IStabilityPool, BimaOwnable, SystemStart {
                    storedPendingReward[account] = 0;
                }
\u0060\u0060\u0060
## Code Issue
\u0060\u0060\u0060solidity
function fixOtherIssue(uint256 collIndex) public {
    depositSums[msg.sender][collIndex] = 0;
}
\u0060\u0060\u0060
## Test Case Modification
\u0060\u0060\u0060solidity
contract PoCTest is TestSetup {
    ...
    function test_custom7_T1MOH() public {
        // 1. Deposit into StabilityPool

        address depositorSP = makeAddr("depositorSP");
        deal(address(debtToken), depositorSP, 1e6 * 1e18);

        vm.startPrank(depositorSP);
        stabilityPool.provideToSP(5e5 * 1e18);
        vm.stopPrank();

        // 2. This big block is to make liquidation with SP

        address user11 = makeAddr("user11");
        deal(address(stakedBTC2), user11, 1e6 * 1e18);

        vm.startPrank(user11);
        _openTrove(sbtc2TroveManager, 1e4 * 1e18, 2.25e18);
        vm.stopPrank();

        // skip time. Now \u0060userICR < TCR < CCR\u0060
        skip(365 days * 10);
        _updateOracle(60_000 * 1e8);

        uint256 price = sbtc2TroveManager.fetchPrice();

        // array for liquidations
        address[] memory troveArray = new address[](1);
        troveArray[0] = user11;

        // liquidate
        liquidationMgr.batchLiquidateTroves(sbtc2TroveManager, troveArray);

        // 3. Claim gains
        uint256[] memory collateralIndexes = new uint256[](1);
        collateralIndexes[0] = stabilityPool.indexByCollateral(stakedBTC2) - 1;
        vm.startPrank(depositorSP);
        stabilityPool.claimCollateralGains(depositorSP, collateralIndexes);
        vm.stopPrank();

        console.log("value of error: %e", stabilityPool.lastCollateralError_Offset(collateralIndexes[0]));
    }
}
\u0060\u0060\u0060
## Code Execution Steps

\u0060\u0060\u0060solidity
// 4. Start sunset
vm.startPrank(stabilityPool.owner());
stabilityPool.startCollateralSunset(stakedBTC2);
vm.stopPrank();

// 5. wait sunset expiration
skip(181 days);
_updateOracle(60000 * 1e8);

// 6. Deploy new TroveManager
StakedBTC newCollateral = new StakedBTC();
IFactory.DeploymentParams memory params = IFactory.DeploymentParams({
  minuteDecayFactor: 999037758833783000,
  redemptionFeeFloor: 5e15,
  maxRedemptionFee: 1e18,
  borrowingFeeFloor: 0,
  maxBorrowingFee: 0,
  interestRateInBps: 400,
  maxDebt: 1_000_000e18, // 1M USD
  MCR: 1.3e18 // 200%
});
vm.startPrank(users.owner);
priceFeed.setOracle(
  address(newCollateral),
  address(mockOracle),
  80000, // heartbeat
  bytes4(0x00000000), // Read pure data assume stBTC is 1:1 with BTC
  18, // sharePriceDecimals
  false // _isEthIndexed
);
factory.deployNewInstance(
  address(newCollateral),
  address(priceFeed),
  address(0),
  address(0),
  params
);
vm.stopPrank();
TroveManager newTroveManager = TroveManager(factory.troveManagers(2));

// 7. Open Trove in new TroveManager
// Deposit 2 users because it\u0027s forbidden to liquidate last Trove
address user22 = makeAddr("user22");
deal(address(newCollateral), user22, 1e6 * 1e18);
address user33 = makeAddr("user33");
deal(address(newCollateral), user33, 1e6 * 1e18);

vm.startPrank(user22);
_openTrove(newTroveManager, 1e4 * 1e18, 2.25e18);
vm.stopPrank();
vm.startPrank(user33);
_openTrove(newTroveManager, 1e4 * 1e18, 2.25e18);
vm.stopPrank();

// 8. Wait till it becomes liquidateable
// skip time. Now \u0060userICR < TCR < CCR\u0060
skip(365 days * 8);
_updateOracle(60_000 * 1e8);

// 9. Liquidate it
troveArray[0] = user22;
liquidationMgr.batchLiquidateTroves(newTroveManager, troveArray);

// 10. Claim all collateral gains
// There are 2 depositors: \u0060users.owner\u0060 and \u0060depositorSP\u0060
vm.startPrank(depositorSP);
collateralIndexes[0] = stabilityPool.indexByCollateral(newCollateral) - 1;
//@note it fixes another issue which causes overflow in this case
\u0060\u0060\u0060
