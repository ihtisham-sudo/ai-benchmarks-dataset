# 3.2.12 - An attacker can consistently steal the majority of the daily mint rewards by opening and closing a trove atomically

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** TroveManager, daily mint rewards, USBD, BIMA rewards, minted amount, reward system, open trove, close trove, atomic transaction, flash loans, Morph, Balancer, borrowing fee, Recovery Mode, profitability, test, BorrowerOperationsTest.t.sol, integral, storedPendingReward, rewardIntegralFor

---

# 3.2.11 Different accumulation of debt will break the sorting of Troves
**Submitted by:** santipu, also found by pkqs90  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** When a Trove is opened within a TroveManager, it is inserted into SortedTroves, a contract designed to keep Troves sorted by NICR (Nominal Individual Collateral Ratio). This sorting invariant is crucial for key operations such as ordered liquidations and redemptions.

However, a flaw in the protocol’s design causes Troves to accumulate debt at different rates over time, leading to the NICRs of individual Troves evolving differently. This discrepancy can ultimately break the sorting within the SortedTroves contract.
The root of the issue lies in how debt accumulation is influenced by whether a Trove claims pending collateral and debt from redistributions. The accrued debt for each Trove is calculated as:

\u0060\u0060\u0060
prevDebt * interest + pendingRewards
\u0060\u0060\u0060

When a Trove invokes \u0060claimReward\u0060, the pending debt from redistributions is added to its active debt, which then starts accruing interest. Over time, this leads to faster debt growth for Troves which claims rewards because the interest is applied to a larger base amount. 

As a result, the NICRs of Troves diverge based on their reward-claiming behavior, which disrupts the sorting within SortedTroves. Over time, this divergence can cause newly inserted Troves to be positioned incorrectly, compounding the problem. If enough Troves are affected, the sorting mechanism in SortedTroves could fail entirely, undermining the reliability of redemptions and ordered liquidations, which depend on perfectly ordered Troves.

The following test demonstrates how two Troves which are the exact same at the start end up having different debt (therefore different NICR) due to this issue. Paste this test in \u0060poc.t.sol\u0060:

\u0060\u0060\u0060solidity
function test_different_interest() external {
  address user1 = makeAddr("user1");
  address user2 = makeAddr("user2");
  vm.startPrank(users.owner);
  // We set the interest rate to 4% per year (rest of the parameters are default)
  sbtcTroveManager.setParameters({
    _minuteDecayFactor: 999037758833783000,
    _redemptionFeeFloor: INIT_REDEMPTION_FEE_FLOOR,
    _maxRedemptionFee: INIT_MAX_REDEMPTION_FEE,
    _borrowingFeeFloor: INIT_BORROWING_FEE_FLOOR,
    _maxBorrowingFee: INIT_MAX_BORROWING_FEE,
    _interestRateInBPS: 400,
    _maxSystemDebt: INIT_MAX_DEBT,
    _MCR: INIT_MCR
  });
  deal(address(stakedBTC), user1, 1e6 * 1e18);
  deal(address(stakedBTC), user2, 1e6 * 1e18);
  // Both users open same Troves
  vm.startPrank(user1);
  _openTrove(sbtcTroveManager, 2_000e18, 2e18);
  vm.startPrank(user2);
  _openTrove(sbtcTroveManager, 2_000e18, 2e18);
  // Rewards are activated
  vm.startPrank(users.owner);
  bimaVault.registerReceiver(address(sbtcTroveManager), 2); // internally calls notifyRegisteredId
  vm.stopPrank();
  (uint256 debt1, uint256 coll1,,) = sbtcTroveManager.getEntireDebtAndColl(user1);
  (uint256 debt2, uint256 coll2,,) = sbtcTroveManager.getEntireDebtAndColl(user2);
  // User1 and user2 have the same debt and coll
  assertEq(debt1, debt2);
  assertEq(coll1, coll2);
  // A liquidation happens, distributing some debt and coll
  vm.prank(address(liquidationMgr));
  sbtcTroveManager.finalizeLiquidation({
    _liquidator: users.user3,
    _debt: 1e18,
    _coll: 0.8e18,
    _collSurplus: 0,
    _debtGasComp: 0,
    _collGasComp: 0
  });
  (debt1, coll1,,) = sbtcTroveManager.getEntireDebtAndColl(user1);
  (debt2, coll2,,) = sbtcTroveManager.getEntireDebtAndColl(user2);
  // Both users still have the same debt and coll
  assertEq(debt1, debt2);
  assertEq(coll1, coll2);
}
\u0060\u0060\u0060
## User1 claims some rewards
\u0060\u0060\u0060solidity
vm.prank(user1);
sbtcTroveManager.claimReward(user1);
// Some time passes, interest accrues
vm.warp(block.timestamp + 30 days);
(debt1, coll1,,) = sbtcTroveManager.getEntireDebtAndColl(user1);
(debt2, coll2,,) = sbtcTroveManager.getEntireDebtAndColl(user2);
// Both users still have the same collateral
assertEq(coll1, coll2);
// User1 has more debt than user2
assertGt(debt1, debt2);
\u0060\u0060\u0060
Recommendation: This issue stems from a fundamental aspect of the protocol’s design, making it challenging to resolve without significant changes. The easiest fix would be to always set the interest rate to 0%.
## An attacker can consistently steal the majority of the daily mint rewards by opening and closing a trove atomically
Submitted by Spearmint, also found by alix40 and pkqs90  
Severity: Medium Risk  
Context: (No context files were provided by the reviewer)  

The TroveManager implements a daily mint reward system where users who mint USBD (protocol\u0027s debt token) receive BIMA rewards proportional to their minted amount compared to the total mints for that day. These rewards are designed to incentivize users to borrow from the protocol and maintain their positions.

When a user opens a trove, their minted amount is registered in the reward system through the \u0060_updateIntegrals\u0060 function, but the system doesn\u0027t properly handle scenarios where the trove is closed in the same block. Even if a user opens and immediately closes their position, they will still be credited for their proportion of that day\u0027s mint rewards.

\u0060\u0060\u0060solidity
function _updateIntegrals(address account, uint256 balance, uint256 supply) internal {
    uint256 integral = _updateRewardIntegral(supply);
    _updateIntegralForAccount(account, balance, integral);
}

function _updateIntegralForAccount(address account, uint256 balance, uint256 currentIntegral) internal {
    uint256 integralFor = rewardIntegralFor[account];
    if (currentIntegral > integralFor) {
        storedPendingReward[account] += (balance * (currentIntegral - integralFor)) / 1e18;
        rewardIntegralFor[account] = currentIntegral;
    }
}
\u0060\u0060\u0060

An attacker can open a trove and mint debt, then instantly close the trove in the same transaction, to steal the majority of the daily mint rewards from other users. Since the attack is atomic, the attacker can use flash loans from Morph or Balancer (0 flash loan fees from these protocols) to create and close large positions without requiring much capital, thus maximizing their share of the daily rewards.

The attack is profitable when the value of stolen rewards exceeds the borrowing fee paid to open the position. The attack becomes significantly more profitable during Recovery Mode since the protocol removes all borrowing fees during this period, leaving only gas costs as an expense.

Here is a simple proof of concept to show the issue. Add the following test to \u0060BorrowerOperationsTest.t.sol\u0060:

\u0060\u0060\u0060solidity
function test_DailyMintAttack() public {
    // Setup vault and allocate emissions
    _vaultSetupAndLockTokens(INIT_BAB_TKN_TOTAL_SUPPLY / 2, true);
    vm.prank(users.owner);
    bimaVault.registerReceiver(address(stakedBTCTroveMgr), 2);
}
\u0060\u0060\u0060
## Voting for Minting Rewards Vulnerability

Bima\u0027s CurveProxy is copied from Prisma Finance. However, Prisma Finance only supports...

Medium Risk

There are multiple solutions:
1. Add minimum holding period requirements before positions are eligible for rewards.
2. Calculate rewards based on time-weighted positions rather than point-in-time balances.

### Console Output
\u0060\u0060\u0060
Ran 1 test for test/foundry/core/BorrowerOperationsTest.t.sol:BorrowerOperationsTest
[PASS] test_DailyMintAttack() (gas: 1760908)
Logs:
  Week: 1
  Day: 4
  Daily mint reward: 7.6695844553571428571428571e25
  Week: 1
  Day: 5
  User 1 reward: 7.5936479756011315417256e23
  User 2 reward: 7.593647975601131541725601e25
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 15.31ms (3.48ms CPU time)
\u0060\u0060\u0060

(No context files were provided by the reviewer)
