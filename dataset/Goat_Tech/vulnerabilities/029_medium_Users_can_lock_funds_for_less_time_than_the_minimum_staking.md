# Users can lock funds for less time than the minimum staking duration

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** staking, funds, minimum duration, lock funds, remaining duration, position, system check, expire, new funds, arbitrarily short, minimum staking amount, function check, recommendation, duration check, allow staking, risk, enforcement, user action, contract, validation

---

# Users can lock funds for less time than the minimum staking duration

**Submitted by**: ethan  
**Severity**: Medium Risk  
**Context**: (No context files were provided by the reviewer)  

**Description**: Despite enforcing an explicit minimum staking duration, it is possible for users to lock funds for less time than intended. If a user locks funds in an existing position without adding to its duration, the system checks that the lock has not expired:

\u0060\u0060\u0060
if remainingDuration > 0 {
    // Allow staking to continue
}
\u0060\u0060\u0060

But if the remaining duration is less than the minimum staking duration, the new funds will only be locked for that arbitrarily short period of time. In contrast, the minimum staking amount is enforced in all cases.

**Recommendation**: Rather than requiring that the remaining duration of the position is greater than zero, the function should check that it is greater than the minimum staking duration:

\u0060\u0060\u0060
if remainingDuration > minimumStakingDuration {
    // Allow staking to continue
}
\u0060\u0060\u0060

Goat: confirmed. will fix soon.
PAGE END
