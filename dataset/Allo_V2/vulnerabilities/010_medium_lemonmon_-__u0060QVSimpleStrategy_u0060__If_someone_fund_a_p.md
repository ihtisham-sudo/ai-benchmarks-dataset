# lemonmon - \u0060QVSimpleStrategy\u0060: If someone fund a pool when the fund is partially/fully distributed, part of the fund may be locked

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, fundPool, BaseStrategy, poolAmount, increasePoolAmount, payout, recipientId, paidOut, distribution, locked funds, recoverFund, manual review, QVBaseStrategy, fund distribution, smart contracts, security risk, fund management, contract vulnerability, decentralized finance

---

lemonmon

medium

# \u0060QVSimpleStrategy\u0060: If someone fund a pool when the fund is partially/fully distributed, part of the fund may be locked

When \u0060Allo::fundPool\u0060 is called when the funds are partially or fully distributed, the added funds may be locked.

## Vulnerability Detail

\u0060Allo::fundPool\u0060 can be called by anyone at anytime, and it will increase the \u0060BaseStrategy.poolAmount\u0060 via \u0060BaseStrategy::increasePoolAmount()\u0060.

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/core/Allo.sol#L339-L345

The \u0060BaseStrategy.poolAmount\u0060 storage variable is used to determine the payout of each recipient by \u0060QVBaseStrategy::_getPayout\u0060:

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L559-L574


When the fund is distributed by the pool manager via \u0060QVBaseStrategy::_distribute\u0060, the \u0060paidOut\u0060 flag for the recipientId whose share was distributed will be set to be true.

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L458

The problem occurs when some funds are  added when some funds are distributed.
In the case, the funds will be partially or fully locked.

## Impact

If some funds are added after the distribution is started, the added funds may be locked.

## Code Snippet

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/core/Allo.sol#L339-L345

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L559-L574


https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L458

## Tool used

Manual Review

## Recommendation

Consider adding recoverFund function like other strategies.
Alternatively, allow the \u0060fundPool\u0060 function only before the distribution starts.

