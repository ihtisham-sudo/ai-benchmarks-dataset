# jkoppel - Protection too expensive when some capital is locked

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, leverage ratio, locked capital, protection positions, capitalization, financial risk, pool deposits, protection costs, late payments, unallocated deposits, capital lock, protection market, risk assessment, manual review, financial modeling, protection strategy, investment risk, capital management, regulatory compliance, risk mitigation

---

jkoppel

medium

# Protection too expensive when some capital is locked

## Summary

The leverage ratio is computed as a ratio of unlocked capital to total protections. This means that each protection position which has locked capital is effectively counted twice: once to lock up capital, and once again to decrease the leverage ratio. This can lead to situations where a pool is very well capitalized to sell more protection, but cannot do so.

## Vulnerability Detail

Consider: Pool has $1.1 million in deposits, and $1 million in protection positions. All pools have late payments, and so $1 million is locked. Pool now has $100k in unallocated deposits, but its leverage ratio is $100k/$1.1M ~ 0.09. Depending on the leverage floor, protection will either be really expensive or cannot be bought at all, even though the pool is well-capitalized.

Compare: If all pools defaulted and the $1M was lost, then the pool would have $100k in deposits and $0 in protection positions, and protection would be very cheap.  The situation with locked capital should be treated similarly.

## Impact

Protection is very expensive or impossible in some situations where it should be cheap.

## Code Snippet

Note that lockCapital() decreases totalSTokenUnderlying but does not modify totalProtections. These are the two variables used to compute the leverage ratio. See https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L357

## Tool used

Manual Review

## Recommendation

Do not count protections which are locking up capital when computing the leverage ratio.
