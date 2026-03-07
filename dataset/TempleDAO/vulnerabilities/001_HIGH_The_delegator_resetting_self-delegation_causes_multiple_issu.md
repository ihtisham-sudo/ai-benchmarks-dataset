# The delegator resetting self-delegation causes multiple issues in the protocol

**Severity:** HIGH
**Auditor:** Cyfrin

---

**Description:** Whenever the vote power of delegators are changed, the validity of self-delegation of the delegator is not checked, which results in issues in multiple parts of the protocol.

- `unsetUserVoteDelegate`: It does not allow stakers to unset delegation through the function because it tries to subtract delegated balance from zero.
- `_withdrawFor`: It does not allow stakers to withdraw their assets because it tries to subtract delegated balance from zero.
- `_stakeFor`: It allows malicious stakers to get infinite voting power by repeating staking & modifying delegator & withdrawal process.

**Impact:** It allows attackers to repeat issues in `_stakeFor` to accumulate voting power, also it causes reverts in withdrawals.

**Proof of Concept:** Here's a scenario where a malicious attacker can get infinite voting power by repeating the following process:

1. Staker delegates to Bob.
2. Bob resets self-delegation.
3. The staker stakes the token.
4. The staker changes the delegation to another party.

**Recommended Mitigation:** In 3 functions above, it should validate if the delegator has self-delegation enabled at the time of function call.

**TempleDAO:** Fixed in [PR 1034](https://github.com/TempleDAO/temple/pull/1034)

**Cyfrin:** Verified

\clearpage
