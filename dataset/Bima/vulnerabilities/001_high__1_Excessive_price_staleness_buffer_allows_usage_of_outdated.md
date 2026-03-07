# .1 Excessive price staleness buffer allows usage of outdated oracle prices

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** price staleness, oracle prices, PriceFeed, RESPONSE_TIMEOUT_BUFFER, heartbeat, block.timestamp, financial loss, market volatility, crypto markets, exploitation, collateral valuations, attack scenario, smart contract, Ethereum, protocol functionality, price feeds, test, foundry, console2, mockOracle

---

# .1 Excessive price staleness buffer allows usage of outdated oracle prices
Submitted by 0xTheBlackPanther, also found by kelvinsmart, santipu, zanderbyte, 0xNirix and pkqs90  
Severity: High Risk  
Context: PriceFeed.sol  
Summary: The PriceFeed contract adds a fixed 1-hour buffer to all oracle heartbeats when checking for price staleness, which can allow prices to be used up to 3x longer than their intended maximum age for oracles with short heartbeat periods.  

**Finding Description:** In the PriceFeed contract, the \u0060_isPriceStale()\u0060 function adds a constant \u0060RESPONSE_TIMEOUT_BUFFER\u0060 of 1 hour to each oracle\u0027s heartbeat when determining if a price is stale:
\u0060\u0060\u0060solidity
uint256 public constant RESPONSE_TIMEOUT_BUFFER = 1 hours; // @audit-poc
function _isPriceStale(uint256 _priceTimestamp, uint256 _heartbeat) internal view returns (bool isPriceStale) {
    isPriceStale = block.timestamp - _priceTimestamp > _heartbeat + RESPONSE_TIMEOUT_BUFFER;
}
\u0060\u0060\u0060
This means that for any oracle feed, the actual maximum allowed age of a price is the heartbeat period plus an additional hour. The impact is particularly severe for oracles with short heartbeat periods. Let\u0027s take an example:
- An oracle with a 30-minute heartbeat will actually allow prices up to 90 minutes old.
- An oracle with a 15-minute heartbeat will allow prices up to 75 minutes old.

The root cause is the design decision to use a fixed 1-hour buffer regardless of the oracle\u0027s heartbeat period. This appears to be inherited from the Prisma codebase but creates a significant discrepancy between intended & actual price freshness guarantees.

**Impact Explanation:** High -- This issue can lead to the protocol operating on significantly stale price data, which could be exploited during periods of high volatility:
1. For fast-moving assets like ETH/USD where prices can move >5% in under an hour:
   - If ETH is $2000 and drops 10% to $1800 in 45 minutes.
   - A 30-minute heartbeat feed would intend to reject the $2000 price after 30 minutes.
   - But due to the buffer, the $2000 price could still be used for up to 90 minutes.
   - This allows users to interact with the protocol at incorrect prices.
2. Specific attack scenario:
   - Attacker monitors for rapid price movements in underlying asset.
   - When price drops significantly but oracle\u0027s old price is still accepted due to buffer.
   - Attacker can mint loans using inflated collateral valuations.
   - Once oracle updates, these positions become undercollateralized.

The severity is high because:
- It affects core protocol functionality (price feeds).
- Can lead to direct financial loss.
- Requires no special permissions to exploit.
- Most dangerous during market volatility when accurate pricing is most critical.

**Likelihood Explanation:** Medium -- While the conditions required (significant price movement + stale oracle price within buffer period) don\u0027t occur frequently, they are natural market events that happen periodically:
- Crypto markets regularly see >5% moves within hour timeframes.
- Oracle network issues or high gas prices can delay updates.
- The longer buffer makes exploitation more practical compared to normal heartbeat periods.

Add the test below in \u0060test/foundry/core/PriceFeedTest.t.sol\u0060 and run it. Make sure to add console2 import:

\u0060\u0060\u0060solidity
import {console2} from "forge-std/console2.sol";

function test_StalePriceUsedDueToBuffer() external {
    vm.startPrank(users.owner);
    console2.log("\n=== Initial Setup ===");
    uint256 initialTimestamp = block.timestamp;
    console2.log("Current block timestamp:", initialTimestamp);
    
    // First set previous round data (round 1)
    mockOracle2.setResponse(
        1, // roundId
        2000e8, // $2000 price
        block.timestamp - 2 minutes, // startedAt
        block.timestamp - 2 minutes, // updatedAt
        1 // answeredInRound
    );

    // Set current round data (round 2) - this price will be stored
    mockOracle2.setResponse(
        2, // roundId
        2000e8, // $2000 price
        block.timestamp, // startedAt
        block.timestamp, // updatedAt
        2 // answeredInRound
    );

    // Set oracle with 30 minute heartbeat
    priceFeed.setOracle(
        address(stakedBTC),
        address(mockOracle2),
        30 minutes, // heartbeat
        bytes4(0), // no share price signature
        18, // decimals
        false // not ETH indexed
    );

    uint256 initialPrice = priceFeed.fetchPrice(address(stakedBTC));
    assertEq(initialPrice, 2000e18, "Initial price should be $2000");
    console2.log("Initial price:", initialPrice / 1e18);

    // Advance time by 85 minutes (> heartbeat but < heartbeat + buffer)
    vm.warp(block.timestamp + 85 minutes);
    console2.log("\nTime advanced by 85 minutes");
    console2.log("New timestamp:", block.timestamp);
    console2.log("Time elapsed:", (block.timestamp - initialTimestamp) / 60, "minutes");

    // Keep the oracle returning the same timestamp for round 2
    mockOracle2.setResponse(
        2, // Same roundId
        2000e8, // Same price
        block.timestamp - 85 minutes, // Old timestamp
        block.timestamp - 85 minutes, // Old timestamp
        2 // Same answeredInRound
    );

    // Get price - should still be valid despite being stale
    uint256 stalePrice = priceFeed.fetchPrice(address(stakedBTC));
    assertEq(stalePrice, 2000e18, "Old price still used due to buffer");
    console2.log("\nStale price still being used:", stalePrice / 1e18);
    console2.log("Price age:", 85, "minutes (> 30min heartbeat but < 90min total timeout)");

    // Now advance just past the buffer
    vm.warp(block.timestamp + 6 minutes);
    console2.log("\nTime advanced by additional 6 minutes");
    console2.log("Total time elapsed:", (block.timestamp - initialTimestamp) / 60, "minutes");

    // Should revert due to truly stale price
    vm.expectRevert(abi.encodeWithSelector(PriceFeed__FeedFrozenError.selector, address(stakedBTC)));
    priceFeed.fetchPrice(address(stakedBTC));
    console2.log("Price finally considered stale and fetchPrice() reverted");
}
\u0060\u0060\u0060
