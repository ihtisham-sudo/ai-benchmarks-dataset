# 74 - Incorrect decimal handling in liquidation logic will prevent liquidation fee recipient from receiving liquidation fees.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Yieldoor
**Keywords:** liquidation, fee, USD, borrowedValue, inflation, protocol, feeRecipient, liquidator, position, value, denomination, WETH, WBTC, USDC, Uniswap, liquidationFee, test, assert, error, calculation

---

**Source:** [GitHub Issue #74](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/74)  
**Found by:** JasonBPMIASN, montecristo, redtrama, stuart_the_minion, v_2110, xKeywordx, zraxx

Incorrect decimal handling in liquidation logic will prevent liquidation fee recipient from receiving liquidation fees.

In Yieldoor protocol, liquidation fee is claimed in the following case:
- Position\u0027s current USD value is greater than borrowed token\u0027s current USD value.

However, borrowed token\u0027s current USD value is inflated in \u0060Leverager.sol\u0060:

\u0060\u0060\u0060solidity
uint256 borrowedValue = owedAmount * bPrice / ERC20(up.denomination).decimals();
\u0060\u0060\u0060

Instead of dividing by 10^decimals, it divides by decimals. Thus, \u0060borrowedValue\u0060 is greatly inflated. 

And the following if branch will never get reached:

\u0060\u0060\u0060solidity
if (totalValueUSD > borrowedValue) {
    // What % of the amountsOut are profit is calculated by \u0060(totalValueUSD - borrowedUSD) / totalValueUSD\u0060
    // Then, on top of that, we calculate the protocol fee and scale it in 1e18.
    uint256 protocolFeePct = 1e18 * liquidationFee * (totalValueUSD - borrowedValue) / (totalValueUSD * 10_000);
    uint256 pf0 = protocolFeePct * amount0 / 1e18;
    uint256 pf1 = protocolFeePct * amount1 / 1e18;
    if (pf0 > 0) IERC20(up.token0).safeTransfer(feeRecipient, pf0);
    if (pf1 > 0) IERC20(up.token1).safeTransfer(feeRecipient, pf1);
    amount0 -= pf0;
    amount1 -= pf1;
}
\u0060\u0060\u0060
1. Liquidator liquidates a position
2. Position\u0027s total value in USD is greater than borrowed value in USD

N/A

N/A

Liquidation fee is not collected.
# Scenario
- Liquidation fee is set to 900 BPS
- A leverager (depositor) creates the following leveraged position:
  - token0 = WBTC
  - token1 = USDC
  - amount0In = 0
  - amount1In = 100000 USDC
  - denomination = WETH
  - vault0In = 1 WBTC = 100000 USD
  - vault1In = 100000 USDC = 100000 USD
  - maxBorrowAmount = 41 WETH
  - Total position value is 200k USD
  - Total borrowed amount is 88800 USD (or 35.52 WETH)
    Here, debt is lower than WBTC price because Uniswap V3 is using current
    WBTC price (88800 USD) instead of test price (100000 USD)
- Later WBTC price drops to 40000 USD and USDC price drops to 0.5 USD
- Position total value is 90000 USD and liquidatable
## Liquidator liquidates the position
## Liquidation fee recipient receives nothing although position value is greater than borrowed value

## How to run POC
In order to check how much borrowedValue is inflated, you can optionally apply the following patch:

\u0060\u0060\u0060diff
diff --git a/yieldoor/src/Leverager.sol b/yieldoor/src/Leverager.sol
index b59c56c..bcad781 100644
--- a/yieldoor/src/Leverager.sol
+++ b/yieldoor/src/Leverager.sol
@@ -292,6 +292,7 @@ contract Leverager is ReentrancyGuard, Ownable, ERC721,
         ILeverager {
                }
            }
+    event log_named_decimal_uint(string key, uint256 value, uint256 decimal);
    /// @notice Liquidates a certain leveraged position.
    /// @dev Check the ILeverager contract for comments on all LiquidateParams
    /// @dev Does not support partial liquidations
@@ -317,6 +318,8 @@ contract Leverager is ReentrancyGuard, Ownable, ERC721,
        ILeverager {
            uint256 bPrice = IPriceFeed(pricefeed).getPrice(up.denomination);
            uint256 borrowedValue = owedAmount * bPrice /
            ERC20(up.denomination).decimals();
+        emit log_named_decimal_uint("totalValueUSD", totalValueUSD, 18);
+        emit log_named_decimal_uint("borrowedValue", borrowedValue, 18);
            if (totalValueUSD > borrowedValue) {
                // What % of the amountsOut are profit is calculated by
                \u0060(totalValueUSD - borrowedUSD) / totalValueUSD\u0060
                // Then, on top of that, we calculate the protocol fee and scale it in
                1e18.
\u0060\u0060\u0060

Add the following content to Leverager.t.sol:

\u0060\u0060\u0060solidity
function test_cantClaimLiquidationFee() external {
    vm.startPrank(owner);
    ILeverager(leverager).enableTokenAsBorrowed(address(weth));
    ILeverager(leverager).setLiquidationFee(900);
    vm.stopPrank();
    // depositor initial fund 100000 USDC = 100000 USD
    vm.startPrank(depositor);
    deal(address(wbtc), depositor, 0e8);
    deal(address(usdc), depositor, 100_000e6);
}
\u0060\u0060\u0060
## Leveraged Position Management

\u0060\u0060\u0060solidity
// position will have 1WBTC and 100000 USDC
// total position value would be 200000 USD
// denom token is weth, will borrow some weth and swap them into wbtc
ILeverager.LeverageParams memory lp;
lp.amount0In = 0e8;
lp.amount1In = 100_000e6;
lp.vault0In = 1e8;
lp.vault1In = 100_000e6;
lp.vault = vault;
lp.maxBorrowAmount = 41e18;
lp.denomination = address(weth);
IMainnetRouter.ExactOutputParams memory ep1;
ep1.path = abi.encodePacked(address(wbtc), uint24(3000), address(weth));
ep1.deadline = block.timestamp + 300;
ep1.amountInMaximum = 41e18;
ep1.recipient = leverager;
lp.swapParams1 = abi.encode(ep1);
wbtc.approve(leverager, type(uint256).max);
usdc.approve(leverager, type(uint256).max);
ILeverager(leverager).openLeveragedPosition(lp);
vm.stopPrank();
ILeverager.Position memory position = ILeverager(leverager).getPosition(1);
// debt is 88800 USD
assertEq(position.initBorrowedUsd / 10 ** 18, 88800);
// price changes will drop position value to 90000 USD
// position is liquidatable but still position value is greater than debt
// so liquidation fee is expected to be claimed
MockOracle(wbtcOracle).setPrice(40000e18); // position has 1 WBTC = 40000 USD
MockOracle(usdcOracle).setPrice(0.5e18); // position has 100000 USDC = 50000 USD
// liquidator liquidate the position with denom token - weth
vm.startPrank(liquidator);
uint256 debtWethAmount = position.borrowedAmount
    * ILendingPool(lendingPool).getCurrentBorrowingIndex(position.denomination)
    / position.borrowedIndex;
deal(address(weth), liquidator, debtWethAmount);
weth.approve(address(leverager), debtWethAmount);
ILeverager.LiquidateParams memory lip;
lip.id = 1;
ILeverager(leverager).liquidatePosition(lip);
vm.stopPrank();
// fee recipient received nothing
assertEq(wbtc.balanceOf(ILeverager(leverager).feeRecipient()), 0);
\u0060\u0060\u0060
## Test Results
\u0060\u0060\u0060plaintext
assertEq(usdc.balanceOf(ILeverager(leverager).feeRecipient()), 0);
\u0060\u0060\u0060
Run the following command:
\u0060\u0060\u0060plaintext
forge test --rpc-url $MAINNET_FORK_URL --match-test test_cantClaimLiquidationFee --fork-block-number 21926708 -vvv
\u0060\u0060\u0060

### Console Output:
\u0060\u0060\u0060plaintext
[PASS] test_cantClaimLiquidationFee() (gas: 1862589)
Logs:
  totalValueUSD: 89999.999199500000000000
  borrowedValue: 4933386117326049569027.777777777777777777
\u0060\u0060\u0060

The following can fix the calculation:
\u0060\u0060\u0060plaintext
- uint256 borrowedValue = owedAmount * bPrice / ERC20(up.denomination).decimals();
+ uint256 borrowedValue = owedAmount * bPrice / 10 ** ERC20(up.denomination).decimals();
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [GitHub Commit](https://github.com/spaceliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858)
**Source:** [GitHub Issue #93](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/93)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.  
**Found by:** 0x73696d616f  

Main position ticks are set according to the tick in slot 0, which is not accurate if the price is near a border. The most obvious case is when the tick just crosses a left boundary, in which the tick is set to the current price tick - 1. In this case, the actual price of the pool is in the current tick in slot 0 + 1, but the code will use the tick in slot 0. Thus, to be more precise, the sqrtPrice should be used and converted to a tick, which always represents the final swap price of the pool.

In Strategy:207, the tick in slot 0 is used to set the main position ticks.

None.

Pool is at the boundary.

1. Uniswap swap causes the tick to be exactly at the boundary.

Loss of fees as the position will not accumulate as many fees.
Forked the base chain at block 26874136 with the addresses below and add 1e18 liquidity of each token in the constructor. The swap will place the price exactly at the boundary, which means a second swap of just 1 wei is enough to push the pool to the next tick. The price is currently tick -1769, but tick -1770 is used as reference, so liquidity is allocated to ticks -1772 to -1768. A 1 wei swap moves the tick to -1769, so only 1 tick spacing has to be crossed to the right to reach the upper -1768 boundary, whereas 3 tick spacing must be crossed to the left. Thus, the position is not symmetrical and will lead to loss of fees. The reason this happens is that the next tick to the left includes the current tick, so for example while it is at tick -1770, the next tick in the code to the left will also be -1770, having to cross 3 tick spacings to the left to reach the lower boundary, but 1 to the right only.

\u0060\u0060\u0060solidity
IUniswapV3Pool pool =
    IUniswapV3Pool(0x20E068D76f9E90b90604500B84c7e19dCB923e7e);
IERC20 wbtc = IERC20(0x4200000000000000000000000000000000000006); // token0
IERC20 usdc = IERC20(0xc1CBa3fCea344f92D9239c08C0568f6F2F0ee452); // token1
address uniRouter = address(0x2626664c2603336E57B271c5C0b26F421741e481);

function test_POC_WrongTicks_DueToNotUsingSqrtPriceX96() public {
    (uint160 sqrtPriceX96, int24 tick,,,,,) = pool.slot0();
    assertEq(tick, -1769);
    //@audit swap to clear current tick token0 liquidity
    uint256 amountToSwap = 100e18;
    deal(address(wbtc), depositor, amountToSwap);
    vm.startPrank(depositor);
    IMainnetRouter.ExactInputSingleParamsV2 memory swapParams;
    swapParams.tokenIn = address(wbtc);
    swapParams.tokenOut = address(usdc);
    swapParams.recipient = depositor;
    swapParams.fee = 100;
    swapParams.amountIn = amountToSwap;
    swapParams.sqrtPriceLimitX96 = TickMath.getSqrtRatioAtTick(-1769);
    wbtc.approve(uniRouter, amountToSwap);
    IMainnetRouter(uniRouter).exactInputSingle(swapParams);
    vm.startPrank(rebalancer);
    skip(10 minutes);
    IStrategy(strategy).rebalance();
    IStrategy.Position memory mainPos = IStrategy(strategy).getMainPosition();
    (sqrtPriceX96, tick,,,,,) = pool.slot0();
    assertEq(sqrtPriceX96, TickMath.getSqrtRatioAtTick(tick + 1)); //@audit price
    // is in tick -1769 actually
    assertEq(tick, -1770); //@audit but current tick is 1 more
    assertEq(mainPos.tickLower, -1772);
    assertEq(mainPos.tickUpper, -1768);
\u0060\u0060\u0060
## Swaps Just 1 Wei

\u0060\u0060\u0060solidity
//@audit swaps just 1 wei, which is enough to cross to next tick.
//@audit thus, the position is not 50/50 symmetric.
amountToSwap = 1;
deal(address(usdc), depositor, amountToSwap);
vm.startPrank(depositor);
swapParams.tokenIn = address(usdc);
swapParams.tokenOut = address(wbtc);
swapParams.recipient = depositor;
swapParams.fee = 100;
swapParams.amountIn = amountToSwap;
swapParams.sqrtPriceLimitX96 = 0;
usdc.approve(uniRouter, amountToSwap);
IMainnetRouter(uniRouter).exactInputSingle(swapParams);
mainPos = IStrategy(strategy).getMainPosition();
(, tick,,,,,) = pool.slot0();
assertEq(tick, -1769); //@audit proves price moves outside range in just 1 wei
\u0060\u0060\u0060

Get the tick from the sqrt price and set the position ticks according to it.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/103)  
**Found by:** iamnmt

When \u0060observationCardinality\u0060 and \u0060currentIndex\u0060 are large enough, the index calculation in \u0060Strategy#checkPoolActivity\u0060 will revert due to integer overflow, causing a denial of service for critical protocol functions.

\u0060checkPoolActivity\u0060 is called by:
- \u0060Strategy#_requirePriceWithinRange\u0060
- \u0060Strategy#rebalance\u0060
- \u0060Strategy#compound\u0060
- \u0060Strategy#addVestingPosition\u0060
- \u0060Leverager#openLeveragedPosition\u0060

These functions are essential for protocol operation.

In \u0060Strategy#checkPoolActivity\u0060, the observation index calculation:

\u0060\u0060\u0060solidity
uint256 index = (observationCardinality + currentIndex - i) % observationCardinality;
\u0060\u0060\u0060

will revert when \u0060observationCardinality + currentIndex >= 2**16\u0060 due to integer overflow in the addition operation, as both variables are \u0060uint16\u0060.
1. An attacker increases \u0060observationCardinalityNext\u0060 to 60000 via \u0060UniswapV3Pool#increaseObservationCardinalityNext\u0060 (See the Appendix for calculation of gas cost).
2. \u0060currentIndex\u0060 increases so that \u0060observationCardinality + currentIndex >= 2**16\u0060.
3. The \u0060checkPoolActivity\u0060 function will revert until \u0060currentIndex\u0060 wraps around to 0.

High. The integer overflow causes all critical functions that rely on \u0060checkPoolActivity\u0060 to revert, making the contract completely unusable. This includes:
1. \u0060rebalance()\u0060 - Cannot adjust positions when market conditions change.
2. \u0060compound()\u0060 - Cannot reinvest earned fees.
3. \u0060addVestingPosition()\u0060 - Cannot add new vesting positions.

Most critically, when positions become out-of-range, the protocol cannot rebalance them back into profitable ranges. This leads to:
- Loss of yield since out-of-range positions earn no fees.
- Locked funds that cannot be rebalanced back into range.

The issue persists until \u0060currentIndex\u0060 wraps around to 0, which could take a significant amount of time depending on pool activity.
## Proof of Concept
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import "forge-std/Test.sol";

contract PoC is Test {
    function test_PoC() public {
        uint16 observationCardinality = 2**15 + 1;
        uint16 currentIndex = 2**15;
        uint16 i = 1;
        uint256 index = (observationCardinality + currentIndex - i) %
            observationCardinality;
    }
}
\u0060\u0060\u0060

\u0060\u0060\u0060
13
\u0060\u0060\u0060
## Vulnerabilities
## Arithmetic Underflow or Overflow
**FAIL:** panic: arithmetic underflow or overflow (0x11) in \u0060test_PoC()\u0060
- Traces:
  - [433] PoC::test_PoC()
    - ← [Revert] panic: arithmetic underflow or overflow (0x11)
- Suite result: FAILED. 0 passed; 1 failed; 0 skipped; finished in 332.96µs (74.17µs CPU time)

### Recommendation
Cast \u0060observationCardinality\u0060 to \u0060uint32\u0060
\u0060\u0060\u0060solidity
- uint256 index = (observationCardinality + currentIndex - i) %
→  observationCardinality;
+ uint256 index = (uint32(observationCardinality) + currentIndex - i) %
→  observationCardinality;
\u0060\u0060\u0060

### Appendix
At block 26923358 on Base tx, on ETH/USDC pool:
- observationCardinality = 5000
- observationCardinalityNext = 5000
- Gas Price: 0.002855 Gwei
- 2230192 gas to increase observationCardinalityNext by 100. Assuming that 1 ETH = 2500 USD. This means it costs 2230192 * 0.002855 / 1e9 = 6.36719816e-06 ETH = 0.0159179954 USD
- It costs ((60000 - 5000) / 100) * 0.0159179954 USD = 8.75489747 USD to increase observationCardinalityNext to 60000.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import "forge-std/Test.sol";
import {IUniswapV3Pool} from "../src/interfaces/IUniswapV3Pool.sol";
import {IUniswapV3Factory} from "../src/interfaces/IUniswapV3Factory.sol";

contract PoC is Test {
    address WETH = 0x4200000000000000000000000000000000000006;
    address USDT = 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913;
    IUniswapV3Factory factory = IUniswapV3Factory(0x33128a8fC17869897dcE68Ed026d694621f6FDfD);
}
\u0060\u0060\u0060
## Code
\u0060\u0060\u0060solidity
function test_PoC() public {
    IUniswapV3Pool pool = IUniswapV3Pool(factory.getPool(WETH, USDT, 500));
    (uint160 sqrtPriceX96, int24 tick,, uint16 observationCardinality, uint16 observationCardinalityNext,,) = pool.slot0();
    console.log("observationCardinality", observationCardinality);
    console.log("observationCardinalityNext", observationCardinalityNext);
    uint256 gasStart = gasleft();
    pool.increaseObservationCardinalityNext(observationCardinality + 100);
    uint256 gasEnd = gasleft();
    console.log("Gas cost of increaseObservationCardinalityNext", gasStart - gasEnd);
}
\u0060\u0060\u0060

\u0060\u0060\u0060
observationCardinality 5000
observationCardinalityNext 5000
Gas cost of increaseObservationCardinalityNext 2230192
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [commit link](https://github.com/spaceliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858)
