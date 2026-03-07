# Issue M-2: Incorrect Freshness Logic Validation in PythOracle breaking the entire mechanism for triggering orders

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** PythOracle, freshness, price data, stale, order execution, validation, publishTime, block.timestamp, noOlderThan, stop-limit order, oracle, financial losses, smart contract, Ethereum, logic error, require condition, test case, audit, protocol reputation, user trust

---

# Issue M-2: Incorrect Freshness Logic Validation in PythOracle breaking the entire mechanism for triggering orders

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-oku-judging/issues/115)

Found by: 
0x486776, 0xCNX, 0xMitev, 0xNirix, 0xRiO, 0xShoonya, 0xaxaxa, 0xc0ffEE, 0xgremlincat, 0xmujahid002, 10ap17, 4gontuk, BijanF, Boy2000, BugPull, ChaosSR, Contest-Squad, DharkArtz, ExtraCaterpillar, Icon0x, John44, LonWof-Demon, LordAdhaar, MoonShadow, NickAuditor2, PoeAudits, Pro_King, Smacaud, Sparrow_Jac, TxGuard, Uddercover, Waydou, Weed0607, X0sauce, Xcrypt, ZanyBonzy, curly, durov, jovemjeune, lukris02, mladenov, mxteem, nikhilx0111, oxwhite, pkabhi01, s0x0mtee, safdie, sakibcy, silver_eth, skid0016, t0x1c, tmotfl, tnevler, udo, vinica_boy, xiaoming90, yovchev_yoan, zhenyazhd, zhoo

## Summary
The PythOracle contract incorrectly validates the freshness of price data using the \u0060getPriceUnsafe()\u0060 function. The current logic ensures that prices are always considered stale, which results in valid orders failing to execute.

## Root Cause
In \u0060PythOracle.sol:29\u0060, the logic: [link](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/oracle/External/PythOracle.sol#L28-L31) is incorrect. The condition ensures that the price is always considered stale, regardless of whether the price is recent or valid. The comparison fails to verify if the \u0060price.publishTime\u0060 is newer than the defined threshold.

## Internal pre-conditions
1. The \u0060noOlderThan\u0060 parameter is set during the function call, defining the allowed freshness window for price data.
2. A valid \u0060price.publishTime\u0060 is provided by the oracle, but due to incorrect logic, it fails validation.
## External Pre-conditions
1. The price feed from the Pyth Oracle contains a valid and fresh publishTime that is newer than block.timestamp - noOlderThan.
2. No tampering or delays in oracle updates occur externally.

## Attack Path
1. Alice places a stop-limit order for a token pair using the Pyth Oracle as the price feed.
2. The oracle updates its price feed, providing a fresh price with a publishTime newer than block.timestamp - noOlderThan.
3. When \u0060checkInRange()\u0060 is called, the require condition in \u0060PythOracle.sol:29\u0060 evaluates the price as stale, despite it being valid.
4. The order fails to execute as the system misinterprets the freshness of the price data.

## Impact
The protocol and its users face the following consequences:

### User Losses:
- Orders fail to execute at the right price, leading to missed opportunities for profit or failure to exit losing positions.
- This affects users placing stop-loss or take-profit orders reliant on timely price updates.

### Protocol Reputation:
- Continuous failures in executing valid orders due to perceived stale data undermine user trust in the system.

## PoC

### Example Scenario
1. Alice places a stop-limit order to sell Token A for Token B if the price of Token A falls below 50.
2. The oracle updates its price feed with a publishTime of \u0060block.timestamp - 5 seconds\u0060.
3. The noOlderThan parameter is set to 30 seconds.

**Execution:** The condition in \u0060PythOracle.sol:29\u0060 evaluates:
\u0060\u0060\u0060solidity
require(price.publishTime < block.timestamp - 30, "Stale Price");
\u0060\u0060\u0060
- With \u0060price.publishTime = block.timestamp - 5\u0060, the condition becomes:
\u0060\u0060\u0060
block.timestamp - 5 < block.timestamp - 30
\u0060\u0060\u0060
- This condition is always false, causing the price to be deemed stale.

Result:
- Alice\u0027s stop-limit order does not execute, resulting in financial losses as she misses the opportunity to sell her tokens before the price drops further.

## Mitigation
Correct the logic to ensure the freshness validation verifies that the publishTime is newer than the threshold:
\u0060\u0060\u0060solidity
require(price.publishTime >= block.timestamp - noOlderThan, "Stale Price");
\u0060\u0060\u0060

The following test demonstrates the issue and verifies the fix:
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "forge-std/Test.sol";

contract PythOracleTest is Test {
    uint256 public noOlderThan = 30;

    function testIncorrectFreshnessCheck() public {
        uint256 currentTime = block.timestamp;
        uint256 validPublishTime = currentTime - 5;

        // Incorrect logic
        bool stale = (validPublishTime < currentTime - noOlderThan);
        assertTrue(stale); // This fails even though the price is valid.

        // Correct logic
        bool fresh = (validPublishTime >= currentTime - noOlderThan);
        assertTrue(fresh); // This passes as the price is valid.
    }
}
\u0060\u0060\u0060

## Discussion
sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:
[https://github.com/gfx-labs/oku-custom-order-types/pull/1](https://github.com/gfx-labs/oku-custom-order-types/pull/1)
