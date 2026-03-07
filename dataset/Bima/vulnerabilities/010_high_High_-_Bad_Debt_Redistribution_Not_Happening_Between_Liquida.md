# High - Bad Debt Redistribution Not Happening Between Liquidations in Batch Mode

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** liquidation, debt, redistribution, batch mode, LiquidationManager, ICR, MCR, collateral, surplus, system impact, bad debt, liquidateNormalMode, liquidateWithoutSP, finalizeLiquidation, totals, singleLiquidation, debtInStabPool, collToOffset, collateral value, incorrect values

---

# Bad Debt Redistribution Not Happening Between Liquidations in Batch Mode
**Submitted by:** 0xNirix, also found by 0xBeastBoy, santipu and 0xghOst  
**Severity:** High Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** The issue lies in how liquidations handle debt redistribution in LiquidationManager.sol. Here\u0027s the problematic flow:
\u0060\u0060\u0060solidity
function batchLiquidateTroves(ITroveManager troveManager, address[] memory _troveArray) public {
    LiquidationValues memory singleLiquidation;
    LiquidationTotals memory totals;
    // First iteration round
    while (troveIter < length && troveCount > 1) {
        address account = _troveArray[troveIter];
        uint256 ICR = troveManager.getCurrentICR(account, troveManagerValues.price);
        if (ICR <= _100pct) {
            singleLiquidation = _liquidateWithoutSP(troveManager, account);
        } else if (ICR < troveManagerValues.MCR) {
            singleLiquidation = _liquidateNormalMode(troveManager, account, debtInStabPool, sunsetting);
        }
        // Problem: Redistribution happens at the end of batch, not after each liquidation
        _applyLiquidationValuesToTotals(totals, singleLiquidation);
    }
    // Redistribution only happens here, after all liquidations
    troveManager.finalizeLiquidation(
        msg.sender,
        totals.totalDebtToRedistribute,
        totals.totalCollToRedistribute,
        totals.totalCollSurplus,
        totals.totalDebtGasCompensation,
        totals.totalCollGasCompensation
    );
}
\u0060\u0060\u0060
## Sequence of Events
1. When a CDP creates bad debt after liquidation, that debt should be redistributed immediately to update the system\u0027s state.
2. However, the redistribution is only updated at the end of the batch through finalizeLiquidation, not after each individual liquidation.
3. This means subsequent liquidations in the same batch are working with incorrect debt values because they don\u0027t account for the redistributed debt from previous liquidations in the batch.

## Issue
The issue is present in \u0060batchLiquidateTroves\u0060 and \u0060liquidateTroves\u0060. The consequences are:

1. **Underestimated Debt:**
   \u0060\u0060\u0060solidity
   // The subsequent liquidations use incorrect debt values because redistribution hasn\u0027t been applied
   uint256 ICR = troveManager.getCurrentICR(account, troveManagerValues.price);
   // This ICR calculation uses outdated debt values
   \u0060\u0060\u0060

2. **Incorrect Collateral Distribution:**
   \u0060\u0060\u0060solidity
   // Because debt is underestimated, more collateral than should be is marked as surplus
   uint256 collSurplus = entireTroveColl - collToOffset;
   if (collSurplus > 0) {
       singleLiquidation.collSurplus = collSurplus;
       troveManager.addCollateralSurplus(_borrower, collSurplus);
   }
   \u0060\u0060\u0060

3. **System-Wide Impact:** Other users in the system have to cover the unaccounted debt.

Add in \u0060LiquidtionManagerTest.t.sol\u0060
\u0060\u0060\u0060solidity
function test_batchVsSequential_liquidation_comparison() external {
    uint256 collateral1 = 1e18;    // 1 BTC
    uint256 collateral2 = 2e18;    // 2 BTC
    uint256 debt1 = _getMaxDebtAmount(collateral1);
    uint256 debt2 = _getMaxDebtAmount(collateral2);
    console.log("Debt of user 1:", debt1);
    console.log("Debt of user 2:", debt2);
    uint256 snapId = vm.snapshot();
    // First case - Sequential Liquidations
    _openTrove(users.user1, collateral1, debt1);
    _openTrove(users.user2, collateral2, debt2);
    mockOracle.setResponse(
        mockOracle.roundId() + 1,
        int256(30000 * 10 ** 8),
        block.timestamp + 1,
        block.timestamp + 1,
        mockOracle.answeredInRound() + 1
    );
    vm.warp(block.timestamp + 1);
    LiquidationState memory user2PreSeq = _getLiquidationState(users.user2);
    // Capture events from sequential liquidations
    vm.recordLogs();
    liquidationMgr.liquidate(stakedBTCTroveMgr, users.user1);
    Vm.Log[] memory logs1 = vm.getRecordedLogs();
    LiquidationState memory user2PostFirstLiq = _getLiquidationState(users.user2);
    vm.recordLogs();
    liquidationMgr.liquidate(stakedBTCTroveMgr, users.user2);
    Vm.Log[] memory logs2 = vm.getRecordedLogs();
    // Parse sequential liquidation events
    uint256 seqLiqDebt1;
    uint256 seqLiqColl1;
    uint256 seqLiqDebt2;
    uint256 seqLiqColl2;
    for (uint i = 0; i < logs1.length; i++) {
        if (logs1[i].topics[0] == keccak256("Liquidation(uint256,uint256,uint256,uint256)")) {
\u0060\u0060\u0060
## 3.2 MediumRisk

### 3.2.1 PriceFeed use BTC/USD chainlink oracle to price WBTC which can be problematic if WBTC depegs

Submitted by 0xTheBlackPanther, also found by GeneralKay  
Severity: MediumRisk
## Context
PriceFeed.sol#L131

## Summary
The protocol relies on oracles, specifically the BTC/USD feed, for pricing bridged assets such as WBTC. However, the system remains vulnerable to depeg attacks where WBTC, or other bridged assets, could become mispriced, allowing users to inflate the value of their collateral. This results in an ability to mint excessive amounts of USBD based on incorrect asset valuations. Despite some safeguards like staleness and price deviation checks, these are insufficient to prevent depeg exploits.

## Vulnerability Details
The protocol uses a BTC/USD price feed as a fallback when a specific oracle is not available for bridged assets like WBTC. If the price of WBTC depegs from BTC but the system continues to use the BTC/USD price, this results in a mispricing of WBTC.

## Impact
In the event of a depeg, users can mint more USBD by exploiting the inflated collateral value of WBTC, based on the incorrect BTC/USD price feed. This can lead to the accumulation of bad debt in the protocol, as the overvalued collateral allows users to borrow more than the true market value of their assets. This mispricing could destabilize the protocol, causing a loss of funds and erosion of trust.

Run the test below, add it in BorrowOperationsTest.t.sol:
\u0060\u0060\u0060solidity
function test_DepegAttack() external {
  // Setup initial owner trove
  vm.startPrank(users.owner);
  borrowerOps.closeTrove(stakedBTCTroveMgr, users.owner);
  vm.stopPrank();
  
  // Setup WBTC oracle
  MockOracle wbtcOracle = new MockOracle();
  address WBTC = address(0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599);
  
  // Set initial WBTC price equal to BTC price ($60,000)
  wbtcOracle.setResponse(
    1, // roundId
    int256(60000e8), // $60,000
    block.timestamp - 1,
    block.timestamp - 1,
    1
  );
  wbtcOracle.setResponse(
    2,
    int256(60000e8),
    block.timestamp,
    block.timestamp,
    2
  );
  
  // Register WBTC oracle
  vm.startPrank(users.owner);
  priceFeed.setOracle(
    WBTC,
    address(wbtcOracle),
    3600,
    bytes4(0),
    8,
    false
  );
  vm.stopPrank();
  
  // Verify initial prices match
  uint256 btcPrice = priceFeed.fetchPrice(address(0));
  uint256 wbtcPrice = priceFeed.fetchPrice(WBTC);
  assertEq(btcPrice, wbtcPrice, "Initial prices should match");
  console.log("Pre-depeg BTC Price:", btcPrice / 1e18);
  console.log("Pre-depeg WBTC Price:", wbtcPrice / 1e18);
  
  // User deposits collateral at initial price match
  uint256 depositAmount = 10e18; // 10 WBTC - smaller amount
  _sendStakedBtc(users.user1, depositAmount);
  vm.startPrank(users.user1);
  stakedBTC.approve(address(borrowerOps), depositAmount);
  
  // Calculate max debt based on initial BTC price, staying within system limits
  uint256 maxDebt = ((depositAmount * btcPrice) / borrowerOps.CCR()) - borrowerOps.DEBT_GAS_COMPENSATION();
}
\u0060\u0060\u0060
## System Debt Limit Exceeded

\u0060\u0060\u0060solidity
// Make sure we don\u0027t exceed system debt limit
uint256 debtLimit = 1_000_000e18; // 1M maximum
maxDebt = maxDebt > debtLimit ? debtLimit : maxDebt;
// Open trove using BTC price as collateral value
borrowerOps.openTrove(
    stakedBTCTroveMgr,
    users.user1,
    0,
    depositAmount,
    maxDebt,
    address(0),
    address(0)
);
// Simulate WBTC depeg by 25% ($45,000)
wbtcOracle.setResponse(
    3,
    int256(45000e8),
    block.timestamp + 1,
    block.timestamp + 1,
    3
);
vm.warp(block.timestamp + 1);
// Get new prices after depeg
uint256 newBtcPrice = priceFeed.fetchPrice(address(0));
uint256 newWbtcPrice = priceFeed.fetchPrice(WBTC);
console.log("Post-depeg BTC Price:", newBtcPrice / 1e18);
console.log("Post-depeg WBTC Price:", newWbtcPrice / 1e18);
// Calculate collateral values
uint256 reportedCollateralValue = depositAmount * newBtcPrice / 1e18;
uint256 actualCollateralValue = depositAmount * newWbtcPrice / 1e18;
uint256 excess = reportedCollateralValue - actualCollateralValue;
console.log("\nCollateral Value Analysis:");
console.log("Reported Collateral Value:", reportedCollateralValue / 1e18);
console.log("Actual Collateral Value:", actualCollateralValue / 1e18);
console.log("Excess Value:", excess / 1e18);
// Show borrowed amounts
uint256 borrowedAmount = debtToken.balanceOf(users.user1);
uint256 properMaxDebt = ((depositAmount * newWbtcPrice) / borrowerOps.CCR()) -
    borrowerOps.DEBT_GAS_COMPENSATION();
console.log("\nBorrowed Amount Analysis:");
console.log("Actual Borrowed Amount:", borrowedAmount / 1e18);
console.log("Proper Max Debt:", properMaxDebt / 1e18);
console.log("Excess USBD Borrowed:", (borrowedAmount - properMaxDebt) / 1e18);
// Verify over-borrowing occurred
assertGt(borrowedAmount, properMaxDebt, "Should be able to borrow more than proper max debt");
vm.stopPrank();
// Verify system risk
uint256 ICR = stakedBTCTroveMgr.getCurrentICR(users.user1, newWbtcPrice);
uint256 MCR = stakedBTCTroveMgr.MCR();
console.log("\nSystem Risk Analysis:");
console.log("Current ICR:", ICR / 1e16, "%");
console.log("Required MCR:", MCR / 1e16, "%");
console.log("System is undercollateralized:", ICR < MCR);
\u0060\u0060\u0060
## Test Results
Ran 1 test for \u0060test/foundry/core/LiquidationManagerTest.t.sol:LiquidationManagerTest\u0060
- [PASS] \u0060test_DepegAttack()\u0060 (gas: 942215)

### Logs:
- Pre-depeg BTC Price: 60000
- Pre-depeg WBTC Price: 60000
- Post-depeg BTC Price: 60000
- Post-depeg WBTC Price: 45000

### Collateral Value Analysis:
- Reported Collateral Value: 600000
- Actual Collateral Value: 450000
- Excess Value: 150000

### Borrowed Amount Analysis:
- Actual Borrowed Amount: 266665
- Proper Max Debt: 199999
- Excess USBD Borrowed: 66666

### System Risk Analysis:
- Current ICR: 168 %
- Required MCR: 200 %
- System is undercollateralized: true

### Recommendation:
To mitigate the vulnerability, it is recommended to implement a double oracle setup for WBTC pricing by integrating both the BTC/USD Chainlink oracle and an on-chain liquidity-based oracle (e.g., UniV3 TWAP), which ensures accurate pricing & safeguards against depegging by halting borrowing activities if the price deviation exceeds a set threshold.
