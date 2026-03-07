# 3 - Permanent Locking of User Funds in the Stability Pool

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** collateral, sunsetted, epochToScaleToSums, depositSums, withdraw, claim rewards, revert, offset, gains, locked funds, user, function, accrueDepositorCollateralGain, epoch, scale, totalActiveDebt, interest, removal, desynchronization, funds, loss

---

# Stale Price Used Due to Buffer
From the logs you can see that even though the oracle\u0027s heartbeat is set to 30 minutes, the contract still accepts and uses a stale price after 85 minutes due to the extra 1-hour buffer, allowing potentially outdated price data to be used for an extended period.

Implement one of the following solutions:
- Reduce the fixed buffer to a more reasonable duration:
    \u0060\u0060\u0060solidity
    uint256 public constant RESPONSE_TIMEOUT_BUFFER = 15 minutes;
    \u0060\u0060\u0060
- Or use dynamic buffers based on heartbeat duration:
    \u0060\u0060\u0060solidity
    function _getTimeoutBuffer(uint256 _heartbeat) internal pure returns (uint256) {
        if (_heartbeat < 1 hours) {
            return 15 minutes;
        }
        if (_heartbeat < 4 hours) {
            return 30 minutes;
        }
        return 1 hours;
    }

    function _isPriceStale(uint256 _priceTimestamp, uint256 _heartbeat) internal view returns (bool) {
        uint256 buffer = _getTimeoutBuffer(_heartbeat);
        return block.timestamp - _priceTimestamp > _heartbeat + buffer;
    }
    \u0060\u0060\u0060

## The calculation of the total weight in the Token Locker is incorrect
Submitted by etherSky, also found by pkqs90, 0xNirix and 0xDjango  
Severity: High Risk  
Context: (No context files were provided by the reviewer)  
Summary: Users lock their tokens to gain voting weights, and the total voting weight should match the sum of all individual users\u0027 voting weights. However, the total weight is miscalculated when users withdraw their tokens with a penalty.

I will explain the issue using an example from the proof of concept. At week 1, User 1 and User 2 each lock 100 tokens for 10 weeks. Initially, the total weight and individual weights of both users are 0.
\u0060\u0060\u0060solidity
// TokenLocker.sol#L608-L611
\u0060\u0060\u0060
## Vulnerability in _lock function

\u0060\u0060\u0060solidity
function _lock(address _account, uint256 _amount, uint256 _weeks) internal {
    uint256 frozen = accountData.frozen;
    if (frozen > 0) {
        accountData.frozen = SafeCast.toUint32(frozen + _amount);
        _weeks = MAX_LOCK_WEEKS;
    }
    else {
        if (_weeks == 1 && block.timestamp % 1 weeks > 4 days) _weeks = 2;
        accountData.locked = SafeCast.toUint32(accountData.locked + _amount);
        totalDecayRate = SafeCast.toUint32(totalDecayRate + _amount);
    }
    accountWeeklyWeights[_account][systemWeek] = SafeCast.toUint40(accountWeight + _amount * _weeks);
    totalWeeklyWeights[systemWeek] = SafeCast.toUint40(totalWeight + _amount * _weeks);
}
\u0060\u0060\u0060

- Line 587: The locked value for both users is updated to 100.
- Line 590: The totalDecayRate is set to 200, which represents the total weight decay per week. This means the total weight would be 2000 at week 1, 1800 at week 2, and so on.
- Line 608: The weights of User 1 and User 2 are each calculated as 1000.
- Line 611: The total weight is updated to 2000, which correctly matches the sum of both users\u0027 weights.

The total weight at week 1 => 2000  
User 1 weight at week 1 => 1000  
User 2 weight at week 1 => 1000  

At week 2, User 1 attempts to withdraw all their tokens with a penalty.
## Vulnerability in withdrawWithPenalty function

\u0060\u0060\u0060solidity
function withdrawWithPenalty(uint256 amountToWithdraw) external notFrozen(msg.sender) returns (uint256 output) {
    accountData.locked -= lockedPlusPenalties;
    totalDecayRate -= lockedPlusPenalties;
    systemWeek = getWeek();
    accountWeeklyWeights[msg.sender][systemWeek] = SafeCast.toUint40(weight - decreasedWeight);
    totalWeeklyWeights[systemWeek] = SafeCast.toUint40(getTotalWeightWrite() - decreasedWeight);
}
\u0060\u0060\u0060

- Line 1184: User 1\u0027s locked value is set to 0.
- Line 1185: The totalDecayRate is reduced by 100, making it 100.
- Line 1189: User 1\u0027s weight becomes 0, as all tokens have been withdrawn.
- Line 1190: The getTotalWeightWrite function is called, but the issue arises because the totalDecayRate had already been updated in line 1185, leading to incorrect calculations.
The function \u0060getTotalWeightWrite\u0060 contains a logic error in the calculation of total weights for users. Specifically, the total weight for week 2 is incorrectly calculated as 1900, because the total decay rate used is 100 instead of the expected 200. This happens because the decay rate for User 1 should have remained at its week 1 value but was prematurely removed before being applied.

As a result, the total weight for week 2 in the \u0060withdrawWithPenalty\u0060 function is computed as 1000 in line 1190 (1900-900). The specific log from the PoC confirms this issue:

\u0060\u0060\u0060
The total weight at week 2 => 1000
User1 weight at week 2     =>  0
User2 weight at week 2     =>  900
*************************
The total weight at week 3 => 900
User1 weight at week 3     =>  0
User2 weight at week 3     =>  800
\u0060\u0060\u0060

It shows that the total voting weight becomes larger than the sum of the individual users\u0027 weights, with the discrepancy growing over time.

In a DAO, accurately calculating the total weights and individual users\u0027 weights is critical. Due to this issue, the discrepancy between the total weight and the sum of individual weights can grow indefinitely, which could ultimately disrupt the proposal system within the DAO.

This issue can occur easily.

Please add the following test file to the test/foundry directory:

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

// test setup
import {TestSetup, IBimaVault, ITokenLocker} from "./TestSetup.sol";
import "forge-std/console2.sol";

contract TokenLockerTest1 is TestSetup {
    function setUp() public virtual override {
        super.setUp();
        // setup the vault to get BimaTokens which are used for voting
        uint128[] memory _fixedInitialAmounts;
        IBimaVault.InitialAllowance[] memory initialAllowances = new IBimaVault.InitialAllowance[](2);
        uint256 tokenAmounts = 100 * INIT_LOCK_TO_TOKEN_RATIO;
        // give user1 allowance
        initialAllowances[0].receiver = users.user1;
        initialAllowances[0].amount = tokenAmounts;
        // give user2 allowance
        initialAllowances[1].receiver = users.user2;
        initialAllowances[1].amount = tokenAmounts;
        vm.prank(users.owner);
        bimaVault.setInitialParameters(
            emissionSchedule,
            boostCalc,
            INIT_BAB_TKN_TOTAL_SUPPLY,
            INIT_VLT_LOCK_WEEKS,
\u0060\u0060\u0060
## Code Snippet

\u0060\u0060\u0060solidity
_fixedInitialAmounts,
initialAllowances
);
// transfer voting tokens to recipients
vm.prank(users.user1);
bimaToken.transferFrom(address(bimaVault), users.user1, tokenAmounts);
vm.prank(users.user2);
bimaToken.transferFrom(address(bimaVault), users.user2, tokenAmounts);
// verify recipients have received voting tokens
assertEq(bimaToken.balanceOf(users.user1), tokenAmounts);
assertEq(bimaToken.balanceOf(users.user2), tokenAmounts);
}
function test_withdrawWithPenalty_totalDecayRate_change() external {
vm.prank(users.owner);
tokenLocker.setAllowPenaltyWithdrawAfter(block.timestamp + 6 weeks);
vm.warp(tokenLocker.allowPenaltyWithdrawAfter() + 1);
vm.prank(users.owner);
tokenLocker.setPenaltyWithdrawalsEnabled(true);
/**
    Penalty withdrawal has been enabled.
*/
assertEq(tokenLocker.penaltyWithdrawalsEnabled(), true);
uint256 tokenAmounts = 100 * INIT_LOCK_TO_TOKEN_RATIO;
uint256 weekLocks = 10;
vm.prank(users.user1);
tokenLocker.lock(users.user1, tokenAmounts / INIT_LOCK_TO_TOKEN_RATIO, weekLocks);
vm.prank(users.user2);
tokenLocker.lock(users.user2, tokenAmounts / INIT_LOCK_TO_TOKEN_RATIO, weekLocks);
/**
    The total weight at week 1: 2000
    User1 weight at week 1: 1000
    User2 weight at week 1: 1000
*/
console2.log(\u0027The total weight at week 1 => \u0027, tokenLocker.getTotalWeight());
console2.log(\u0027User1 weight at week 1     => \u0027, tokenLocker.getAccountWeight(users.user1));
console2.log(\u0027User2 weight at week 1     => \u0027, tokenLocker.getAccountWeight(users.user2));
vm.warp(block.timestamp + 1 weeks);
vm.prank(users.user1);
/**
    User1 withdraws with a penalty at week 2.
*/
tokenLocker.withdrawWithPenalty(type(uint256).max);
/**
    The total weight at week 2: 1000
    User1 weight at week 2: 0
    User2 weight at week 2: 900
*/
console2.log(\u0027*************************\u0027);
console2.log(\u0027The total weight at week 2 => \u0027, tokenLocker.getTotalWeight());
console2.log(\u0027User1 weight at week 2     => \u0027, tokenLocker.getAccountWeight(users.user1));
console2.log(\u0027User2 weight at week 2     => \u0027, tokenLocker.getAccountWeight(users.user2));
vm.warp(block.timestamp + 1 weeks);
/**
    The total weight at week 3: 900
    User1 weight at week 3: 0
    User2 weight at week 3: 800
*/
console2.log(\u0027*************************\u0027);
console2.log(\u0027The total weight at week 3 => \u0027, tokenLocker.getTotalWeight());
console2.log(\u0027User1 weight at week 3     => \u0027, tokenLocker.getAccountWeight(users.user1));
console2.log(\u0027User2 weight at week 3     => \u0027, tokenLocker.getAccountWeight(users.user2));
}
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
9
\u0060\u0060\u0060
## Permanent Locking of User Funds in the Stability Pool
Submitted by etherSky, also found by santipu, T1MOH and pkqs90  
Severity: High Risk  
Context: (No context files were provided by the reviewer)  

If the collateral is sunsetted and 180 days have passed, the sunsetted collateral will be replaced by newly added collateral. At this point, the epochToScaleToSums for the relevant index is reset to zero. This value may increase again if new collateral is added through an offset. If users have a larger depositSums value for this index, actions like depositing or withdrawing underlying tokens, and claiming rewards, gains from the old sunsetted collateral will fail and be reverted.

Assume the sunsetted collateral is assigned index 1. Let the current epoch be E and the current scale be S. Users have already earned gains from this collateral, meaning depositSums[1] is greater than 0 for these users. After 180 days, the sunsetted collateral is replaced with a new one.

- StabilityPool.sol:
    \u0060\u0060\u0060solidity
    function _overwriteCollateral(IERC20 _newCollateral, uint256 idx) internal {
        for (uint128 i; i <= externalLoopEnd; ) {
            for (uint128 j; j <= internalLoopEnd; ) {
                epochToScaleToSums[i][j][idx] = 0;
                unchecked {
                    ++j;
                }
            }
            unchecked {
                ++i;
            }
        }
        collateralTokens[idx] = _newCollateral;
    }
    \u0060\u0060\u0060
In line 223, \u0060epochToScaleToSums[E][S][1]\u0060 is reset to 0. Assume there is a user A with \u0060depositSums[1] = 10,000\u0060. Through an offset, the new collateral generates some gains, causing \u0060epochToScaleToSums[E][S][1]\u0060 to increase to 200 or a similar value (still less than 10,000). At this point, all operations—such as \u0060provideToSP\u0060, \u0060withdrawFromSP\u0060, and \u0060_claimReward\u0060, which invoke the \u0060_accrueDepositorCollateralGain\u0060 function—would fail and revert.
## Function Vulnerability

\u0060\u0060\u0060solidity
function _accrueDepositorCollateralGain(address _depositor) private returns (bool hasGains) {
    uint80[MAX_COLLATERAL_COUNT] storage depositorGains = collateralGainsByDepositor[_depositor];
    uint256 collaterals = collateralTokens.length;
    uint256 initialDeposit = accountDeposits[_depositor].amount;
    if (initialDeposit != 0) {
        uint128 epochSnapshot = depositSnapshots[_depositor].epoch;
        uint128 scaleSnapshot = depositSnapshots[_depositor].scale;
        uint256 P_Snapshot = depositSnapshots[_depositor].P;
        uint256[MAX_COLLATERAL_COUNT] storage sumS = epochToScaleToSums[epochSnapshot][scaleSnapshot];
        uint256[MAX_COLLATERAL_COUNT] storage nextSumS = epochToScaleToSums[epochSnapshot][scaleSnapshot + 1];
        uint256[MAX_COLLATERAL_COUNT] storage depSums = depositSums[_depositor];
        for (uint256 i; i < collaterals; i++) {
            if (sumS[i] == 0) continue; // Collateral was overwritten or not gains
            hasGains = true;
            uint256 firstPortion = sumS[i] - depSums[i];
            uint256 secondPortion = nextSumS[i] / BIMA_SCALE_FACTOR;
            depositorGains[i] += SafeCast.toUint80(
                (initialDeposit * (firstPortion + secondPortion)) / P_Snapshot / BIMA_DECIMAL_PRECISION
            );
        }
    }
}
\u0060\u0060\u0060

An underflow occurs in line 657. As a result, user A\u0027s funds remain locked until \u0060epochToScaleToSums[E][S][1]\u0060 exceeds \u0060depositSums[1]\u0060. This process cannot be manually controlled, as all values are updated automatically through offsets. Moreover, if the scale or epoch increases before this condition is met, user A will lose all their funds.

The impact is that users are unable to deposit or withdraw their underlying tokens when they want. In some cases, they would lose all their funds, including any rewards, as there is no mechanism to increase \u0060epochToScaleToSums\u0060 for those old epochs and scales.

This situation arises as a direct consequence of the system design, where sunsetting collateral is an inherent feature. Such issues can easily occur once collateral is sunsetted.

Please add the following test file to the \u0060test/foundry\u0060 directory.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;
import {TestSetup, IIncentiveVoting, SafeCast} from "./TestSetup.sol";
import {StakedBTC} from "../../contracts/mock/StakedBTC.sol";
import {Factory, IFactory} from "../../contracts/core/Factory.sol";
import {PriceFeed} from "../../contracts/core/PriceFeed.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "forge-std/console2.sol";

contract TestStabilityPoolTest2 is TestSetup {
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

    function test_stabilityPool_sunset_withdraw() external {
        uint256 depositAmount = 20e18;
        vm.prank(address(borrowerOps));
        debtToken.mint(users.user1, depositAmount);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
assertEq(debtToken.balanceOf(users.user1), depositAmount);
vm.prank(users.user1);
/**
    User1 provides debtTokens to the Stability Pool.
*/
stabilityPool.provideToSP(depositAmount);
vm.prank(address(liquidationMgr));
/**
    For testing purposes:
        - A 5e18 debt loss occurs.
        - A 5e18 collateral gain is applied.
*/
stabilityPool.offset(stakedBTC, 5e18, 5e18);
vm.prank(users.user1);
/**
    To update collateralGainsByDepositor, User1 calls the claimReward function.
*/
stabilityPool.claimReward(users.user1);
vm.prank(users.owner);
/**
    The stakedBTC collateral is sunsetted.
*/
stabilityPool.startCollateralSunset(stakedBTC);
/**
    After 200 days, the stakedBTC can be replaced with new collateral.
*/
vm.warp(block.timestamp + 200 days);
console2.log(stabilityPool.depositSums(users.user1, 0), stabilityPool.epochToScaleToSums(0, 0, 0));
vm.prank(users.owner);
StakedBTC newCollateral = new StakedBTC();
vm.prank(address(factory));
/**
    A new collateral token is enabled. (Suppose this new collateral is much more valuable than
    ֒→  stakedBTC.)
*/
stabilityPool.enableCollateral(newCollateral);
vm.prank(address(borrowerOps));
debtToken.mint(users.user2, depositAmount);
vm.prank(users.user2);
/**
    User2 provides debtTokens to the Stability Pool.
*/
stabilityPool.provideToSP(depositAmount);
console2.log(stabilityPool.depositSums(users.user1, 0), stabilityPool.epochToScaleToSums(0, 0, 0));
vm.prank(address(liquidationMgr));
/**
    For testing purposes:
        - A 5e18 debt loss occurs.
        - A 1e18 collateral gain is applied.
*/
stabilityPool.offset(newCollateral, 5e18, 1e18);
console2.log(stabilityPool.depositSums(users.user1, 0), stabilityPool.epochToScaleToSums(0, 0, 0));
/**
    0: normal mode
    1: withdraw test
    2: provide test
    3: claim rewards test
*/
uint256 TEST_MODE = 0;
if (TEST_MODE == 1) {
    vm.prank(users.user1);
\u0060\u0060\u0060
## 1. Withdrawal and Claiming Rewards Reversion
In the test described above, we observed that depositing, withdrawing, and claiming rewards are reverted by changing TEST_MODE to 1, 2, or 3.

Track \u0060epochToScaleToSums\u0060 and deposit sums per token instead of per index.
\u0060\u0060\u0060solidity
- mapping(address depositor => uint256[MAX_COLLATERAL_COUNT] deposits) public depositSums;
+ mapping(address depositor => mapping(IERC20 => uint256)) public depositSums;
- mapping(uint128 epoch => mapping(uint128 scale => uint256[MAX_COLLATERAL_COUNT] sumS)) public epochToScaleToSums;
+ mapping(uint128 epoch => mapping(uint128 scale => mapping(IERC20 => uint256))) public epochToScaleToSums;
\u0060\u0060\u0060

## 2. Interest Accrued Removal
High Risk

TroveManager.sol#L1061

The total active debt in a TroveManager is not correctly updated when a new Trove is opened, resulting in the complete removal of the interest accrued since the last update. When a Trove is opened within a TroveManager, the total active debt is initially updated through \u0060accrueActiveInterests\u0060. This function calculates and adds the accumulated interests since the last update to the total active debt. However, this update is subsequently ignored and overwritten when the total active debt is recalculated as the sum of the previous debt and the new debt from the opening Trove. This final update to the total active debt completely overwrites the earlier interest accrual, effectively removing it from the total active debt calculation.
## Desynchronization of totalActiveDebt in openTrove
\u0060\u0060\u0060solidity
function openTrove(
    address _borrower,
    uint256 _collateralAmount,
    uint256 _compositeDebt,
    uint256 NICR,
    address _upperHint,
    address _lowerHint,
    bool _isRecoveryMode
) external whenNotPaused returns (uint256 stake, uint256 arrayIndex) {
    // ...
    // cache total active debt
    uint256 totalActiveDebtPre = totalActiveDebt; // <<<
    // ...
    t.activeInterestIndex = _accrueActiveInterests(); // <<<
    // ...
    // enforce collateral debt limit
    uint256 _newTotalDebt = totalActiveDebtPre + _compositeDebt; // <<<
    require(_newTotalDebt + defaultedDebt <= maxSystemDebt, "Collateral debt limit reached");
    // update storage new total active debt
    totalActiveDebt = _newTotalDebt; // <<<
}
\u0060\u0060\u0060
This issue causes the totalActiveDebt variable to become desynchronized from the actual total active debt in the TroveManager. While the individual Trove debt balances remain accurate (as activeInterestIndex remains unaffected), the sum of these balances will exceed the value of totalActiveDebt. This discrepancy can lead to the following issues:
- Checks for maxSystemDebt will be inaccurate because they rely on the incorrect totalActiveDebt.
- The reward distribution system will distribute excessive rewards to users, resulting in insufficient funds for later claimants.
- The last Troves to be closed or redeemed from the TroveManager will fail due to an underflow in totalActiveDebt.

Recommendation: To resolve this issue, ensure totalActiveDebt is correctly updated when a Trove is opened:
\u0060\u0060\u0060solidity
uint256 _newTotalDebt = totalActiveDebtPre + _compositeDebt;
uint256 _newTotalDebt = totalActiveDebt + _compositeDebt;
require(_newTotalDebt + defaultedDebt <= maxSystemDebt, "Collateral debt limit reached");
// update storage new total active debt
totalActiveDebt = _newTotalDebt;
\u0060\u0060\u0060
