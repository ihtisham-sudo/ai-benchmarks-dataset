# Functions

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** liquidation, Trove, ICR, MCR, Stability Pool, bad debt, collateral, gas compensation, liquidator, debt, collateral distribution, protocol health, liquidation functions, emissionId, fetchRewards, claimRewards, MockCurveDepositToken, bimaVault, claimableRewards, reward allocation

---

# Functions

### notifyRegisteredId
\u0060\u0060\u0060solidity
function notifyRegisteredId(uint256[] calldata assignedIds) external returns (bool success) {
    require(msg.sender == address(vault));
    require(emissionId == 0, "Already registered");
    require(assignedIds.length == 1, "Incorrect ID count");
    emissionId = assignedIds[0];
    success = true;
}
\u0060\u0060\u0060

### fetchRewards
\u0060\u0060\u0060solidity
function fetchRewards() external {
    uint256 bimaAmount = vault.allocateNewEmissions(emissionId);
    claimableRewards += bimaAmount;
}
\u0060\u0060\u0060

### claimRewards
\u0060\u0060\u0060solidity
function claimRewards() external {
    vault.transferAllocatedTokens(msg.sender, msg.sender, claimableRewards);
    claimableRewards = 0;
}
\u0060\u0060\u0060

## Contracts

### TestCurveDepositTokenTest1
\u0060\u0060\u0060solidity
contract TestCurveDepositTokenTest1 is TestSetup {
    function setUp() public virtual override {
        super.setUp();
    }
    function test_curveDepositToken_claimReward() external {
        MockCurveDepositToken curveDepositToken = new MockCurveDepositToken(bimaVault);
        /**
            User 1 locks tokens to gain weight.
        */
        uint256 initialUnallocated = _vaultSetupAndLockTokens(INIT_BAB_TKN_TOTAL_SUPPLY / 2, true);
        /**
            Register curveDepositToken as the receiver
        */
        vm.prank(users.owner);
        bimaVault.registerReceiver(address(curveDepositToken), 1);
        uint256 emissionId = curveDepositToken.emissionId();
        assertEq(emissionId, 1);
        IIncentiveVoting.Vote[] memory votes = new IIncentiveVoting.Vote[](1);
        votes[0].id = emissionId;
        votes[0].points = incentiveVoting.MAX_POINTS();
        /**
            User 1 votes for curveDepositToken, enabling it to receive BIMA rewards.
        */
        vm.prank(users.user1);
        incentiveVoting.registerAccountWeightAndVote(users.user1, 1, votes);
        /**
            Assume that 5 weeks have passed, which is the initial grace period in the boost calculator.
            INIT_BS_GRACE_WEEKS = 5
        */
        vm.warp(block.timestamp + 5 weeks);
        uint256 balanceBefore = bimaToken.balanceOf(users.user1);
        /**
            Fetch rewards in curveDepositToken to update weeklyEmissions in the vault up to the current week.
        */
        curveDepositToken.fetchRewards();
        console2.log(\u0027The claimable rewards in curveDepositToken are => \u0027, curveDepositToken.claimableRewards());
        /**
            Advance to the next week.
        */
        vm.warp(block.timestamp + 1 weeks);
    }
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 TEST_MODE = 1;
if (TEST_MODE == 0) {
    vm.prank(users.user1);
    curveDepositToken.claimRewards();
    uint256 balanceAfter = bimaToken.balanceOf(users.user1);
    console2.log(\u0027The claimed rewards without updating the weeklyEmissions for the current week => \u0027,
    balanceAfter - balanceBefore);
} else {
    vm.prank(address(curveDepositToken));
    bimaVault.allocateNewEmissions(emissionId);
    vm.prank(users.user1);
    curveDepositToken.claimRewards();
    uint256 balanceAfter = bimaToken.balanceOf(users.user1);
    console2.log(\u0027The claimed rewards after updating the weeklyEmissions for the current week   => \u0027,
    balanceAfter - balanceBefore);
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function _claimReward(address claimant, address receiver) internal returns (uint128[2] memory amounts) {
    _updateIntegrals(claimant, balanceOf[claimant], totalSupply);
    _fetchRewards();
    amounts = storedPendingReward[claimant];
    delete storedPendingReward[claimant];
    CRV.transfer(receiver, amounts[1]);
}
\u0060\u0060\u0060
Apply this fix to both of ConvexDepositToken and CurveDepositToken.

**Submitted by:** santipu  
**Severity:** Medium Risk  
**Context:** LiquidationManager.sol#L183, LiquidationManager.sol#L314, LiquidationManager.sol#L349  
**Description:** When a Trove is liquidated with an ICR slightly above 100% but still below 100.5%, it will cause a loss of funds for the users in Stability Pool due to the collateral gas compensation. A Trove can be liquidated in two ways:
- If a Trove has an ICR lower than MCR but still higher than 100%, it should be liquidated using the Stability Pool.
- If the Trove has an ICR lower than 100% it should be liquidated without the Stability Pool, instead the debt and collateral are distributed within the same TroveManager.

This distinction is made so that liquidations that carry bad debt, i.e. debt without backing collateral, do not negatively impact the Stability Pool and only that TroveManager. However, there is an edge case where a Trove has an ICR higher than 100% but it still generates some bad debt due to the gas compensation. The collateral gas compensation is a percentage of the total collateral of a Trove (0.5%) that is discounted from a Trove\u0027s collateral on liquidation and sent to the liquidator. This gas compensation can cause a Trove that is slightly healthy, meaning it has an ICR slightly above 100%, to be suddenly unhealthy without that 0.5% of collateral.

This issue will happen whenever a Trove is liquidated with an ICR that is above 100% but is below 100.5%. In these scenarios, the liquidation will offset the Trove\u0027s debt and collateral using the Stability Pool, causing losses to its depositors.
## Significant Loss in StabilityPool
If the Trove is big enough, it can cause a significant loss to users in StabilityPool, leading to some withdrawals from there and hurting the overall protocol health.  
**Recommendation:** To mitigate this issue, the liquidation functions should liquidate without using the StabilityPool when the Den\u0027s ICR is below 100.5% and not 100%.
