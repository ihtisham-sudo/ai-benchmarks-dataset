# MiloTruck - \u0060drawTimeoutAt()\u0060 causes the prize pool to shutdown one draw earlier

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, MiloTruck, drawTimeoutAt, prize pool, shutdown, draw period, unawarded draws, block.timestamp, awardDraw, PrizePool.sol, timestamp, core functionality, depositors, yield loss, protocol, manual review, code snippet, recommendation, smart contract

---

MiloTruck

high

# \u0060drawTimeoutAt()\u0060 causes the prize pool to shutdown one draw earlier

## Summary

The shutdown timestamp returned by \u0060drawTimeoutAt()\u0060 is one draw period early, causing the protocol to shut down one draw earlier than expected.

## Vulnerability Detail

In \u0060PrizePool.sol\u0060, the prize pool shuts down if the number of unawarded draws in a row is equal to \u0060drawTimeout\u0060:

[PrizePool.sol#L283-L284](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-prize-pool/src/PrizePool.sol#L283-L284)

\u0060\u0060\u0060solidity
  /// @notice The maximum number of draws that can be missed before the prize pool is considered inactive.
  uint24 public immutable drawTimeout;
\u0060\u0060\u0060

\u0060drawTimeout\u0060 is used in \u0060drawTimeoutAt()\u0060, which determines the timestamp at which the pool shuts down:

[PrizePool.sol#L973-L975](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-prize-pool/src/PrizePool.sol#L973-L975)

\u0060\u0060\u0060solidity
  function drawTimeoutAt() public view returns (uint256) { 
    return drawClosesAt(_lastAwardedDrawId + drawTimeout);
  }
\u0060\u0060\u0060

As seen from above, the pool shuts down at the close time of \u0060drawId = _lastAwardedDrawId + drawTimeout\u0060. However, this causes the pool to shut down one draw earlier than expected as draws can only be awarded after their close time in \u0060awardDraw()\u0060:

[PrizePool.sol#L460-L465](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-prize-pool/src/PrizePool.sol#L460-L465)

\u0060\u0060\u0060solidity
    uint24 awardingDrawId = getDrawIdToAward();
    uint48 awardingDrawOpenedAt = drawOpensAt(awardingDrawId);
    uint48 awardingDrawClosedAt = awardingDrawOpenedAt + drawPeriodSeconds;
    if (block.timestamp < awardingDrawClosedAt) {
      revert AwardingDrawNotClosed(awardingDrawClosedAt);
    }
\u0060\u0060\u0060

To illustrate the problem:

- Assume the following:
  - \u0060drawTimeout = 1\u0060, which means the pool should shut down after one draw has been missed.
  - No draws have been awarded yet, so \u0060_lastAwardedDrawId = 0\u0060.
- The first draw to award is always \u0060drawId = 1\u0060.
- When \u0060awardDraw()\u0060 is called before \u0060drawId = 2\u0060, the check in \u0060awardDraw()\u0060 will revert as \u0060block.timestamp\u0060 is less than the close time of \u0060drawId = 1\u0060.
- When \u0060awardDraw()\u0060 is called during or after \u0060drawId = 2\u0060 (ie. \u0060block.timestamp\u0060 is greater than the close time of \u0060drawId = 1\u0060):
  - \u0060_lastAwardedDrawId + drawTimeout = 0 + 1 = 1\u0060
  - \u0060drawTimeoutAt()\u0060 returns the close time of \u0060drawId = 1\u0060, so the pool has already shut down.
  - \u0060awardDraw()\u0060 reverts due to the \u0060notShutdown\u0060 modifier.

As seen from above, \u0060awardDraw()\u0060 can never be called when \u0060drawTimeout = 1\u0060, even though a draw was never missed. This demonstrates how \u0060drawTimeoutAt()\u0060 returns a timestamp one draw period early.
 
## Impact

When \u0060drawTimeout = 1\u0060, the prize pool will never award prizes to any vaults and will immediately shut down, causing a loss of yield for depositors. Furthermore, this breaks core functionality of the protocol as the only incentive for users to deposit into vaults is the chance of winning a huge prize.

When \u0060drawTimeout > 1\u0060, the prize pool will shut down when \u0060drawTimeout - 1\u0060 consecutive draws have been missed, which is one draw early.

## Code Snippet

https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-prize-pool/src/PrizePool.sol#L283-L284

https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-prize-pool/src/PrizePool.sol#L973-L975

https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-prize-pool/src/PrizePool.sol#L460-L465

## Tool used

Manual Review

## Recommendation

Modify \u0060drawTimeoutAt()\u0060 to return the close time of \u0060_lastAwardedDrawId + drawTimeout + 1\u0060:

\u0060\u0060\u0060diff
  function drawTimeoutAt() public view returns (uint256) { 
-   return drawClosesAt(_lastAwardedDrawId + drawTimeout);
+   return drawClosesAt(_lastAwardedDrawId + drawTimeout + 1);
  }
\u0060\u0060\u0060
