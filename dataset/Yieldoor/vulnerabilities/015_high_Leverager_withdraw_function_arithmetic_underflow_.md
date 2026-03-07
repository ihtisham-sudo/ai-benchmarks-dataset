# Leverager withdraw function arithmetic underflow.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Yieldoor
**Keywords:** withdraw, arithmetic, underflow, token1, token0, balance, error, audit, contract, denial of service, withdrawal, funds locked, repay, amount, condition, error handling

---

# Attack Path
1. Protocol rebalances but main ticks are not symmetric and will miss out on fees when the price moves to the side that has less liquidity allocated.

Loss of fees.

\u0060\u0060\u0060solidity
// in setup
IUniswapV3Pool pool =
    IUniswapV3Pool(0x20E068D76f9E90b90604500B84c7e19dCB923e7e);
IERC20 wbtc = IERC20(0x4200000000000000000000000000000000000006); // token0
IERC20 usdc = IERC20(0xc1CBa3fCea344f92D9239c08C0568f6F2F0ee452); // token1
address uniRouter = address(0x2626664c2603336E57B271c5C0b26F421741e481);
vm.createSelectFork(vm.envString("RPC_URL_BASE"), 26874136);

function test_POC_WrongTicks_DueToIsLowerSide() public {
    skip(10 minutes);
    vm.startPrank(rebalancer);
    IStrategy(strategy).rebalance();
    IStrategy.Position memory mainPos = IStrategy(strategy).getMainPosition();
    (, int24 tick,,,,,) = pool.slot0();
    //@audit position is not symmetric, harming long term fees
    assertEq(tick, -1769);
    assertEq(mainPos.tickLower, -1770);
    assertEq(mainPos.tickUpper, -1766);
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
bool isLowerSided = modulo <= (tickSpacing / 2);
\u0060\u0060\u0060
**Source:** [GitHub Issue #96](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/96)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.  
**Found by:** 0x73696d616f  

Strategy::checkPoolActivity() reverts if the timestamp is 0. However, this will never happen. What actually happens is the timestamp being 1, when the cardinality has been increased and the tick timestamp was set to 1 for gas saving purposes. When this tick is hit in the loop, it means there were not enough observations to reach the lookAgo timestamp and it should revert because the price could not be validated. However, if the timestamp is 1, it may not revert depending on the value of the tick delta calculated, and as the timestamp is 1, it will return true with an invalid price observation.

In Strategy:322, the timestamp check is incorrect.

None.

None.

1. Twap would not have enough credibility and rebalancing would be impossible.
2. Attacker or user adds cardinality to the uniswap pool, which sets the next tick\u0027s timestamp to 1.
3. Rebalance goes through with an invalid price with not enough validation, leading to depositing liquidity at a bad price and causing losses for users.
Lossoffundsduetodepositingliquidityatanunfavourableprice.

Thefollowingfunctionisusedwhencardinalityisincreasedinthepool.
\u0060\u0060\u0060solidity
function grow(
  Observation[65535] storage self,
  uint16 current,
  uint16 next
) internal returns (uint16) {
  require(current > 0, \u0027I\u0027);
  // no-op if the passed next value isn\u0027t greater than the current next value
  if (next <= current) return current;
  // store in each slot to prevent fresh SSTOREs in swaps
  // this data will not be used because the initialized boolean is still false
  for (uint16 i = current; i < next; i++) self[i].blockTimestamp = 1;
  return next;
}
\u0060\u0060\u0060

if (timestamp == 1) {
  revert("timestamp 1");
}
**Source:** [GitHub Issue #97](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/97)  
**Found by:** 0x73696d616f  

Strategy::checkPoolActivity() is supposed to check tick delta until the tick more in the past than lookAgo. From the security doc:  
\u0060checkPoolActivity\u0060 does intentionally check 1 extra observation before lookAgo. “1 extra observation” and “before” indicate that it is intended that 1 more observation in the past is looked at, with a timestamp before lookAgo.  
However, the opposite actually happens, due to the way observations are being calculated.

In Strategy:335, it will return 1 observation too early.

None.

None.

1. Protocol rebalances but the twap price validation is incomplete and may lead to losses when depositing in the pool at a bad price.
Lossoffundsthatwillbearbitraged.

Thewaytheobservationsworkis:
1. The current tick of the pool is taken.
2. Thetickcumulativeofthemostrecentobservationistaken.
3. Thetickcumulativeofthesecondmostrecentobservationistaken.
4. Thesecumulativeticksaresubtractedanddividedbythedeltatimestamp,leading
   tothetickatthemostrecentobservation.
5. Thecurrenttickofthepooliscomparedwiththetickofthemostrecent
   observationinthefirstiteration. Inthesecond,it\u0027sthemostrecenttickwiththe
   secondmostrecent,soonandsoforth.

However,whencheckinglookAgovstimestamp,itisusingthetimestampofthesecond
mostrecentobservation,butitevaluatedthetickofthemostrecentobservation. Thus,
it will return 1 tick too early.  
Note: recentandsecondmostrecentcanbeshiftedintimeto3rdand4thandsoon.

ThetimestampcheckshouldbemadeonthenextTimestamp,beforeitisupdatedtotime
stampintheloop.
**Source:** [GitHub Issue #126](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/126)  
**Found by:** 000000, 0x73696d616f, 0xaxaxa, 0xc0ffEE, JohnTPark24, RampageAudit, TessKimy, armoking32, future2_22, iamnmt, montecristo, mstpr-brainbot, newspacexyz, patitonar, super_jack

The \u0060Strategy#_setSecondaryPositionsTicks\u0060 function incorrectly handles negative ticks when calculating modulo, causing the secondary position to be active when it should be out-of-range and potentially leading to division by zero in \u0060LiquidityAmounts#getLiquidityForAmounts\u0060.

The strategy maintains two Uniswap V3 positions:
1. A main position that should be balanced (50:50)
2. A secondary position that should always be out-of-range and filled with only one token

The secondary position\u0027s ticks are set based on the current tick and token balances to ensure it remains out-of-range. The main position\u0027s ticks are calculated with proper handling of negative modulos, but this correction is missing in the secondary position calculation.
## _setMainTicks
\u0060\u0060\u0060solidity
/// @notice Calculates and sets the ticks of the main position
/// @dev Checks if the nearest initializable tick is lower or higher than the current tick
function _setMainTicks(int24 tick) internal {
    int24 halfWidth = int24(positionWidth / 2);
    int24 modulo = tick % tickSpacing;
    if (modulo < 0) modulo += tickSpacing; // if tick is negative, modulo is also negative
    bool isLowerSided = modulo < (tickSpacing / 2);
    int24 tickBorder = tick - modulo;
}
\u0060\u0060\u0060
## Incorrect Modulo Calculation for Negative Ticks

In \u0060Strategy#_setSecondaryPositionsTicks\u0060, the modulo calculation for negative ticks is incorrect:

\u0060\u0060\u0060solidity
int24 modulo = tick % tickSpacing;
\u0060\u0060\u0060

Unlike \u0060Strategy#_setMainTicks\u0060 which handles negative modulos correctly:

\u0060\u0060\u0060solidity
if (modulo < 0) modulo += tickSpacing;
\u0060\u0060\u0060
This leads to two issues:
1. When bal0 in 1 < bal1, the secondary position becomes active because tick < tickUpper = tick - modulo
2. When bal0 in 1 >= bal1, the secondary position range is shorter than intended because tick - (tickSpacing + modulo) + tickSpacing < tick - modulo + tickSpacing

Additionally, when positionWidth = 4 * tickSpacing and isLowerSide is true, tickLower equals tickUpper, causing a division by zero in LiquidityAmounts#getLiquidityForAmounts.

1. Initial conditions:
   - positionWidth = 4 * tickSpacing
   - Current tick is negative
   - bal0 in 1 >= bal1
   - Current tick results in isLowerSide = true in main position
2. When rebalance() is called:
   - _setSecondaryPositionsTicks calculates incorrect modulo
   - Set tickLower = tick - modulo + tickSpacing
   - Set tickUpper = mainPosition.tickUpper
   - Due to incorrect modulo, tickLower = tickUpper
3. _addLiquidityToSecondaryPosition attempts to add liquidity:
   - Calls LiquidityAmounts#getLiquidityForAmounts
   - Division by zero occurs due to equal ticks
   - Transaction reverts

High. The vulnerability has two severe impacts:
1. Secondary position becomes active when it should be out-of-range, breaking a core invariant of the strategy
2. Strategy becomes unusable when specific conditions are met due to division by zero
## ProofofConcept

### Case1: bal0in1 < bal1
Consider:
1. tickSpacing = 60
2. Currenttick = -121
3. modulo = -121 % 60 = -1 (incorrect)
4. bal0in1 < bal1

Calculations:
- secondaryPosition.tickLower = mainPosition.tickLower
- secondaryPosition.tickUpper = -121 - (-1) = -120
- Currenttick (-121) is less than tickUpper (-120)
- Result: Secondary position becomes active when it should be out-of-range

With correct modulo handling:
- modulo = -1 + 60 = 59
- secondaryPosition.tickUpper = -121 - 59 = -180
- Currenttick (-121) would be greater than tickUpper (-180)
- Result: Secondary position remains out-of-range as intended

### Case2: bal0in1 >= bal1 (with isLowerSided = true)
Consider:
1. tickSpacing = 60
2. Currenttick = -91
3. positionWidth = 240 (4 * tickSpacing)
4. modulo = -91 % 60 = -31 (incorrect)
5. bal0in1 >= bal1

Main position calculations:
- modulo = -31 + 60 = 29 (corrected in setMainTicks)
- isLowerSided = 29 < (60/2) = true
- tickBorder = -91 - 29 = -120
- mainPosition.tickUpper = -120 + 120 = 0
- tickLower = -91 - (-31) + 60 = 0
- tickUpper = mainPosition.tickUpper = 0
- Result: tickLower = tickUpper = 0, causing division by zero
## With correct modulo handling:
- modulo = -31 + 60 = 29
- tickLower = -91 - 29 + 60 = -60
- tickUpper = mainPosition.tickUpper = 0
- Result: Valid position range (-60, 0)

## Recommendation
Add the same modulo correction as in \u0060setMainTicks\u0060:
\u0060\u0060\u0060solidity
function _setSecondaryPositionsTicks(int24 tick) internal {
    int24 modulo = tick % tickSpacing;
    if (modulo < 0) modulo += tickSpacing;
    uint256 bal0 = IERC20(token0).balanceOf(address(this));
    uint256 bal1 = IERC20(token1).balanceOf(address(this));
    uint256 _price = price();
    uint256 bal0in1 = bal0 * _price / PRECISION;
    if (bal0in1 < bal1) {
        secondaryPosition.tickLower = mainPosition.tickLower;
        secondaryPosition.tickUpper = tick - modulo;
    } else {
        secondaryPosition.tickLower = tick - modulo + tickSpacing;
        secondaryPosition.tickUpper = mainPosition.tickUpper;
    }
    emit NewSecondaryTicks(secondaryPosition.tickLower, secondaryPosition.tickUpper);
}
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [Commit Link](https://github.com/spa/cegliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858)
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/159)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.

**Found by**  
0x73696d616f

Vault::withdraw() withdraws from the help position whenever the idle capital is not enough. However, it withdraws too much as it does not take into account that some of the idle capital is already available.

In Vault:98, it withdraws too many shares.

None.

None.

1. User withdraws 1000 shares, worth 1000 tokens. There already are 500 tokens idle, but the code will still withdraw all 1000 tokens, keeping 500 tokens idle.

Loss of fees as the liquidity stays idle.
\u0060\u0060\u0060solidity
function withdraw(uint256 shares, uint256 minAmount0, uint256 minAmount1)
    public
    returns (uint256 withdrawAmount0, uint256 withdrawAmount1)
{
    IStrategy(strategy).collectFees();
    (uint256 totalBalance0, uint256 totalBalance1) = IStrategy(strategy).balances();
    uint256 totalSupply = totalSupply();
    _burn(msg.sender, shares);
    withdrawAmount0 = totalBalance0 * shares / totalSupply;
    withdrawAmount1 = totalBalance1 * shares / totalSupply;
    (uint256 idle0, uint256 idle1) = IStrategy(strategy).idleBalances();
    if (idle0 < withdrawAmount0 || idle1 < withdrawAmount1) {
        // When withdrawing partial, there might be a few wei difference.
        (withdrawAmount0, withdrawAmount1) =
            IStrategy(strategy).withdrawPartial(shares, totalSupply);
    }
}
\u0060\u0060\u0060

Reduce the shares to withdraw from the strategy by the liquidity already available (idle).
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/190)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.  
**Found by:** future2_22  

The decimal precision of the collateral is insufficient for calculating the interest, especially for wbtc.

In \u0060ReserveLogic::_updateIndexes::L156\u0060, the totalBorrows may not update or may experience precision loss. [Link to Code](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/libraries/ReserveLogic.sol#L156)

\u0060\u0060\u0060solidity
156:         newTotalBorrows = newBorrowingIndex * (reserve.totalBorrows) /
             (reserve.borrowingIndex);
\u0060\u0060\u0060

To change the totalBorrows, the unaccounted interest must be equal to or greater than 1 wei. To avoid precision loss, the interest must exceed 10,000 wei. If the collateral is wbtc, this value is not small. The \u0060_updateIndexes\u0060 function could be executed every block (period=15s), and the unaccounted interest may be less than the above value.
## Internal pre-conditions
N/A

## External pre-conditions
N/A

An attacker can repeatedly deposit 1001 wei of wbtc and redeem the maximum amount of wbtc (type(uint256).max). Alternatively, users can interact with the LendingPool frequently.
Let\u0027s consider the following scenario. LendingPool\u0027s asset = wbtc, BorrowingRateConfig:  
(0%,0%)->(80%,20%)->(90%,50%)->(100%,150%) totalLiquidityAndBorrows=0.25 wbtc, totalBorrows=0.126144 wbtc currentUtilizationRate=50.4576%,  
[InterestRateUtils.sol#L28](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/libraries/InterestRateUtils.sol#L28) currentBorrowingRate=50.4576%*20%/80%=12.6144%  
[InterestRateUtils.sol#L73](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/libraries/InterestRateUtils.sol#L73) rate = 12.6144% = 0.126144e27, currentTimestamp = lastUpdateTimestamp+15. ratePerSecond=rate/SECONDS_PER_YEAR=4e18  
basePowerTwo=ratePerSecond*ratePerSecond/PRECISION=16e9 basePowerThree=64 secondTerm=exp*expMinusOne*basePowerTwo/2=15*14*16e9=3360e9  
thirdTerm=exp*expMinusOne*expMinusTwo*basePowerThree/6=15*14*13*64/6=29120 CompoundedInterest=(PRECISION)+(ratePerSecond*exp)+(secondTerm)+(thirdTerm) = 1e27 + 4e18 * 15 + 3360e9 + 29120 = 1e27 + 60e18 + 3360e9 + 29120 < 1e27 + 60.1e18  
[ReserveLogic.sol#L115](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/libraries/ReserveLogic.sol#L115) latestBorrowingIndex=reserve.borrowingIndex*calculateCompoundedInterest/1e27<reserve.borrowingIndex*(1e27+60.1e18)/1e27  
[ReserveLogic.sol#L156](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/libraries/ReserveLogic.sol#L156) newTotalBorrows=latestBorrowingIndex*(reserve.totalBorrows)/(reserve.borrowingIndex)<<(reserve.borrowingIndex*(1e27+60.1e18)/1e27)*(reserve.totalBorrows)/(reserve.borrowingIndex) = (1e27 + 60.1e18) / 1e27 *(reserve.totalBorrows) = reserve.totalBorrows + 60.1e-9 * 0.126144e8 << reserve.totalBorrows+1; Therefore, newTotalBorrows=reserve.totalBorrows

The depositor of the LendingPool may not be able to take any profits at all or may receive reduced profits.  
When BorrowingRateConfig := (0%, 0%) -> (80%, 20%) -> (90%, 50%) -> (100%, 150%),

1. LendingPool\u0027s asset = wbtc, totalLiquidityAndBorrows = 0.25 wbtc, totalBorrows = 0.126144 wbtc If the _updateIndexes function is executed every block, the interest is not collected. If it is executed every 100 blocks (25 mins), the calculation of interest experiences 1% precision loss.
2. LendingPool\u0027s asset = wbtc, totalLiquidityAndBorrows = 25 wbtc, totalBorrows = 12.6144 wbtc If the _updateIndexes function is executed every 100 block (25 mins), the calculation of interest experiences 0.01% precision loss.
3. LendingPool\u0027s asset = usdc, totalLiquidityAndBorrows = 250,000 usdc, totalBorrows = 126,144 usdc If the _updateIndexes function is executed every block, the calculation of interest experiences 0.01% precision loss.
Consider increasing the decimal precision of the collateral.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/407)  
**Found by:** 000000, 0xJi, 0x15, 0x73696d616f, 0xaxaxa, 0xnegan, CL001, Chain-sentry, DSbeX, Drynooo, Elawdie, Harsh, JasonBPMIASN, Jumcee, KiteWeb3, MaslarovK, Mrmatrixxx, Ryonen, Spomaria, Uddercover, Victor_TheOracle, Z-Bra, bigbear1229, bladeee, brakeless, destiny_rs, devAnas, elolpuer, elvin.a.block, eta, fspah, godwinudo, gogolevds, hackcat, iamephraim, ilyadruzh, ivanalexandur, kazan, m3dython, oct0pwn, princekay, stuart_the_minion, surenyan-oks, v_2110, verbotenviking, whitehair0330, xKeywordx, yuza101, zraxx

In the withdraw function of the Leverager contract, when the borrowed asset is token1, the code uses the wrong variable in its conditional subtraction. Instead of using the available amount of token1 (amountOut1), it mistakenly uses amountOut0 (the token0 balance) to determine how much to subtract from the owed amount. This error causes an arithmetic underflow if amountOut1 (the correct balance) is less than the owed amount, because the ternary operator selects amountOut0 even though it might be much larger. In Solidity 0.8.x, arithmetic underflow reverts the transaction, blocking the withdrawal.

The bug is a simple copy-paste error. In the branch where borrowed == up.token1, the code should reference amountOut1 in the ternary operator. Instead, it mistakenly uses amountOut0, leading to an underflow when token1’s balance is insufficient.

None.

None.

[GitHub Code Reference](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/Leverage%20r.sol#L209)
## Vulnerability Details

In the withdraw function, after obtaining withdrawal amounts from the vault:

\u0060\u0060\u0060solidity
uint256 bIndex = ILendingPool(lendingPool).getCurrentBorrowingIndex(borrowed);
uint256 totalOwedAmount = up.borrowedAmount * bIndex / up.borrowedIndex;
uint256 owedAmount = totalOwedAmount * wp.pctWithdraw / 1e18;
// ...
if (borrowed == up.token0) {
    uint256 repayFromWithdraw = amountOut0 < owedAmount ? amountOut0 : owedAmount;
    owedAmount -= repayFromWithdraw;
    amountOut0 -= repayFromWithdraw;
} else if (borrowed == up.token1) {
    // BUG: Should use amountOut1 below instead of amountOut0.
    uint256 repayFromWithdraw = amountOut1 < owedAmount ? amountOut0 : owedAmount;
    owedAmount -= repayFromWithdraw;
    amountOut1 -= repayFromWithdraw;
}
\u0060\u0060\u0060

### Issue Trigger

When borrowed equals \u0060up.token1\u0060, the condition \u0060if(amountOut1 < owedAmount)\u0060 is met. Instead of using \u0060amountOut1\u0060 (the correct available balance of token1), the code mistakenly uses \u0060amountOut0\u0060 to compute \u0060repayFromWithdraw\u0060. For example, assume:

- \u0060owedAmount = 150\u0060
- \u0060amountOut1 = 100\u0060 (available token1 is less than owed)
- \u0060amountOut0 = 300\u0060 (available token0 is much higher)

The ternary operator incorrectly selects \u0060amountOut0\u0060 (300) because \u0060amountOut1 < owedAmount\u0060 is true. Then, the code performs:

\u0060\u0060\u0060solidity
owedAmount -= repayFromWithdraw; // 150 - 300, which underflows.
\u0060\u0060\u0060

Solidity 0.8 enforces checked arithmetic, so this underflow causes a revert.

### Consequences

- **Denial of Withdrawal**: Users with positions borrowing token1 cannot withdraw if the token1 liquidity is insufficient compared to token0’s balance.
- **Funds Locked**: Repeated failures due to underflow may lock user funds, preventing any withdrawal until the bug is fixed.
- **Attack Vector**: Although likely unintentional, an attacker could manipulate the withdrawal scenario (e.g., by altering input amounts) to trigger the bug repeatedly, effectively causing a denial-of-service on withdrawals for token1 borrowers.
- **Denial of Withdrawal**: Users with positions borrowing token1 cannot withdraw if the token1 liquidity is insufficient compared to token0’s balance.
- **Funds Locked**: Repeated failures due to underflow may lock user funds, preventing any withdrawal until the bug is fixed.

Foundry test demonstrating that the withdrawal call reverts due to the arithmetic underflow when the borrowed asset is token1:

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import "forge-std/Test.sol";

// Minimal interfaces and contract fragments required for the test.
interface IVault {
    function withdraw(uint256 shares, uint256 min0, uint256 min1) external returns (uint256, uint256);
}
interface ILendingPool {
    function getCurrentBorrowingIndex(address asset) external view returns (uint256);
    function repay(address asset, uint256 amount) external;
}
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
contract Leverager {
    // Simplified Position struct used in the withdraw function.
    struct Position {
        address token0;
        address token1;
        address vault;
        uint256 borrowedAmount;
        uint256 borrowedIndex;
        address denomination; // borrowed token
        uint256 shares;
    }
    mapping(uint256 => Position) public positions;
    address public lendingPool;
}
\u0060\u0060\u0060
## Vulnerable withdraw function fragment
\u0060\u0060\u0060solidity
function withdraw(uint256 wp_pctWithdraw, uint256 shares, uint256 totalSupply,
        address msgSender) external {
    Position memory up = positions[1]; // using position ID 1 for testing
    // For testing, assume borrowed token equals up.token1.
    address borrowed = up.denomination;
    uint256 bIndex =
        ILendingPool(lendingPool).getCurrentBorrowingIndex(borrowed);
    uint256 totalOwedAmount = up.borrowedAmount * bIndex / up.borrowedIndex;
    uint256 owedAmount = totalOwedAmount * wp_pctWithdraw / 1e18;
    // Simulated values from vault.withdraw.
    // In our test, we set:
    // amountOut0 (token0 balance from vault) = 300
    // amountOut1 (token1 balance from vault) = 100, which is less than
    // owedAmount = 150.
    uint256 amountOut0 = 300;
    uint256 amountOut1 = 100;
    if (borrowed == up.token0) {
        uint256 repayFromWithdraw = amountOut0 < owedAmount ? amountOut0 :
            owedAmount;
        owedAmount -= repayFromWithdraw;
        amountOut0 -= repayFromWithdraw;
    } else if (borrowed == up.token1) {
        // BUG: incorrectly uses amountOut0 instead of amountOut1.
        uint256 repayFromWithdraw = amountOut1 < owedAmount ? amountOut0 :
            owedAmount;
        // This line causes underflow: 150 - 300 underflows.
        owedAmount -= repayFromWithdraw;
        amountOut1 -= repayFromWithdraw;
    }
    // For testing, we simply require that owedAmount must be zero at end.
    require(owedAmount == 0, "Underflow detected: insufficient token1 funds");
}

// For testing: allow setting a position directly.
function testSetPosition(Position calldata pos) external {
    positions[1] = pos;
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
contract LeveragerWithdrawTest is Test {
    Leverager leverager;
    // Dummy lending pool to return a fixed borrowing index.
    contract DummyLendingPool {
        function getCurrentBorrowingIndex(address) external pure returns (uint256) {
\u0060\u0060\u0060
