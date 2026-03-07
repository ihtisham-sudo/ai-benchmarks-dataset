# Vulnerabilities

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Buffer Finance
**Keywords:** asset, queuedTrade, resolveQueuedTrades, validation, signature, private keeper mode, funds loss, slippage, open trade, cancel trade, timestamp, queued time, price, contract, abuse, function, emit, IBufferBinaryOptions, queuedTrades, user

---

**Source:** [GitHub Issue #85](https://github.com/sherlock-audit/2022-11-buffer-judging/issues/85)  
**Found by:** kaliberpoziomka, KingNFT, hansfriese, adriro, 0x52, bin2chen  

After an order is initiated, it must be filled by calling \u0060resolveQueuedTrades\u0060. This function validates that the asset price has been signed but never validates that the asset being passed in matches the asset of the queuedTrade. When private keeper mode is off, which is the default state of the contract, this can be abused to cause huge loss of funds.

\u0060\u0060\u0060solidity
for (uint32 index = 0; index < params.length; index++) {
    OpenTradeParams memory currentParams = params[index];
    QueuedTrade memory queuedTrade = queuedTrades[
      currentParams.queueId
    ];
    bool isSignerVerifed = _validateSigner(
      currentParams.timestamp,
      currentParams.asset,
      currentParams.price,
      currentParams.signature
    );
    // Silently fail if the signature doesn\u0027t match
    if (!isSignerVerifed) {
      emit FailResolve(
         currentParams.queueId,
         "Router: Signature didn\u0027t match"
      );
      continue;
    }
    if (
      !queuedTrade.isQueued ||
      currentParams.timestamp != queuedTrade.queuedTime
    ) {
      // Trade has already been opened or cancelled or the timestamp is wrong.
      // So ignore this trade.
      continue;
\u0060\u0060\u0060
# Vulnerabilities

\u0060\u0060\u0060solidity
// If the opening time is much greater than the queue time then cancel the
if (block.timestamp - queuedTrade.queuedTime <= MAX_WAIT_TIME) {
    _openQueuedTrade(currentParams.queueId, currentParams.price);
} else {
    _cancelQueuedTrade(currentParams.queueId);
    emit CancelTrade(
        queuedTrade.user,
        currentParams.queueId,
        "Wait time too high"
    );
}
// Track the next queueIndex to be processed for user
userNextQueueIndexToProcess[queuedTrade.user] =
    queuedTrade.userQueueIndex +
    1;
\u0060\u0060\u0060

BufferRouter#resolveQueueTrades never validates that the asset passed in for params is the same asset as the queuedTrade. It only validates that the price is the same, then passes the price and queueId to _openQueuedTrade:

\u0060\u0060\u0060solidity
function _openQueuedTrade(uint256 queueId, uint256 price) internal {
    QueuedTrade storage queuedTrade = queuedTrades[queueId];
    IBufferBinaryOptions optionsContract = IBufferBinaryOptions(
        queuedTrade.targetContract
    );
    bool isSlippageWithinRange = optionsContract.isStrikeValid(
        queuedTrade.slippage,
        price,
        queuedTrade.expectedStrike
    );
    if (!isSlippageWithinRange) {
        _cancelQueuedTrade(queueId);
        emit CancelTrade(
            queuedTrade.user,
            queueId,
            "Slippage limit exceeds"
        );
        return;
    }
}
\u0060\u0060\u0060
Inside \u0060_openQueuedTrade\u0060 it checks that the price is within the slippage bounds of the order, cancelling if it\u0027s not. Otherwise, it uses the price to open an option. According to documentation, the same router will be used across a large number of assets/pools, which means the publisher for every asset is the same, given that the router only has one publisher variable.
