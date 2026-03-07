# berndartmueller - \u0060DrawManager.canStartDraw\u0060 does not consider retried RNG requests when determining if a new draw auction can be started

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, DrawManager, canStartDraw, RNG requests, auction, draw auction, expired draw, timestamp, retry mechanism, off-chain actors, startDraw, drawReward, manual review, auction duration, failed requests, security impact, code consistency, timestamp validation, function checks

---

berndartmueller

medium

# \u0060DrawManager.canStartDraw\u0060 does not consider retried RNG requests when determining if a new draw auction can be started

## Summary

Inconsistent checks in the \u0060DrawManager.canStartDraw\u0060 function, neglecting to consider retried RNG requests, might lead to wrongly assuming that a new draw auction cannot be started.

## Vulnerability Detail

The \u0060DrawManager.canStartDraw\u0060 function checks if the \u0060startDraw\u0060 function can be called. However, the checks are not consistent with the \u0060startDraw\u0060 function. Specifically, the check in line \u0060289\u0060 to determine if the draw has expired is different than the auction duration check in the \u0060startDraw\u0060 function in lines [\u0060250-251\u0060](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-draw-manager/src/DrawManager.sol#L250-L251). The latter uses the last RNG request\u0027s \u0060closedAt\u0060 timestamp to determine the elapsed **auction** time, to consider any retried failed RNG requests, while the former checks if the **draw** has expired, not considering retried RNG requests.

As a result, if for a given draw a RNG request has been retried, and thus the total elapsed time from the draw close until now (\u0060block.timestamp\u0060) might exceed the auction duration, off-chain actors calling the \u0060canStartDraw\u0060 function might wrongly assume that the draw auction can not be started, even though such a call would succeed.

## Impact

As \u0060canStartDraw\u0060 is also [called internally by the \u0060startDrawReward\u0060 function](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-draw-manager/src/DrawManager.sol#L296-L298) and both functions are likely to be used by off-chain actors to determine if a new draw auction an be started, this might lead to wrongly assuming that a new draw auction cannot be started, even though it should be possible. As a result, the current draw might not get awarded.

## Code Snippet

[DrawManager.canStartDraw()](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-draw-manager/src/DrawManager.sol#L289)

\u0060\u0060\u0060solidity
275: /// @notice Checks if the start draw can be called.
276: /// @return True if start draw can be called, false otherwise
277: function canStartDraw() public view returns (bool) {
278:   uint24 drawId = prizePool.getDrawIdToAward();
279:   uint48 drawClosesAt = prizePool.drawClosesAt(drawId);
280:   StartDrawAuction memory lastStartDrawAuction = getLastStartDrawAuction();
281:   return (
282:     (
283:       // if we\u0027re on a new draw
284:       drawId != lastStartDrawAuction.drawId ||
285:       // OR we\u0027re on the same draw, but the request has failed and we haven\u0027t retried too many times
286:       (rng.isRequestFailed(lastStartDrawAuction.rngRequestId) && _startDrawAuctions.length <= maxRetries)
287:     ) && // we haven\u0027t started it, or we have and the request has failed
288:     block.timestamp >= drawClosesAt && // the draw has closed
289: ❌  _computeElapsedTime(drawClosesAt, block.timestamp) <= auctionDuration // the draw hasn\u0027t expired
290:   );
291: }
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation

Consider using the last request\u0027s \u0060closedAt\u0060 timestamp instead of \u0060drawClosesAt\u0060 to determine if the auction has expired to consider failed RNG requests that have been retried by calling \u0060startDraw\u0060 again.

