# whitehair0330 - Incorrect implementation of the \u0060PositionMarginProcess.updatePositionFromBalanceMargin()\u0060 function.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, function implementation, PositionMarginProcess, updatePositionFromBalanceMargin, initialMarginInUsd, initialMarginInUsdFromBalance, amount, margin reduction, asset withdrawal, token utilization, code review, manual review, security flaw, risk assessment, financial implications, user assets, position management, bug fix, software security

---

whitehair0330

High

# Incorrect implementation of the \u0060PositionMarginProcess.updatePositionFromBalanceMargin()\u0060 function.

## Summary

The \u0060updatePositionFromBalanceMargin()\u0060 function does nothing when \u0060position.initialMarginInUsd == position.initialMarginInUsdFromBalance && amount < 0\u0060. However, in this case, the function should actually reduce the \u0060initialMarginInUsdFromBalance\u0060 of the position.

## Vulnerability Detail

In the \u0060updatePositionFromBalanceMargin()\u0060 function, when \u0060amount < 0\u0060, it should reduce the value of \u0060initialMarginInUsdFromBalance\u0060 for the position. However, as shown at \u0060L309\u0060, the function does nothing when \u0060position.initialMarginInUsd == position.initialMarginInUsdFromBalance && amount < 0\u0060. Consequently, if users withdraw their assets, the margin amounts of the positions are not reduced accordingly. This results in users being able to utilize more tokens than they have deposited.

\u0060\u0060\u0060solidity
    function updatePositionFromBalanceMargin(
        Position.Props storage position,
        bool needSendEvent,
        uint256 requestId,
        int256 amount
    ) public returns (uint256 changeAmount) {
309     if (position.initialMarginInUsd == position.initialMarginInUsdFromBalance || amount == 0) {
            changeAmount = 0;
            return 0;
        }
        [...]
    }
\u0060\u0060\u0060

## Impact

As a result, users may be able to utilize more tokens than they have deposited.

## Code Snippet

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/PositionMarginProcess.sol#L303-L338

## Tool used

Manual Review

## Recommendation

The \u0060PositionMarginProcess.updatePositionFromBalanceMargin()\u0060 function should be fixed as follows.

\u0060\u0060\u0060diff
-       if (position.initialMarginInUsd == position.initialMarginInUsdFromBalance || amount == 0) {
+       if ((position.initialMarginInUsd == position.initialMarginInUsdFromBalance && amount > 0) || amount == 0) {
            changeAmount = 0;
            return 0;
        }
\u0060\u0060\u0060
