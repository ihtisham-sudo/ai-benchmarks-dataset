# .3.2.7 Pool owner can sandwich deposits into his pool to keep their fs at 1 while being able to withdraw ETH earnings

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** pool owner, sandwich attack, deposits, ETH earnings, financial stability, trust score, withdrawal, mempool, transaction, staking, owner fees, incentives, exploit, penalty, ratio, ETH, Bob, Alice, frontrunning, max ETH earning

---

# .3.2.7 Pool owner can sandwich deposits into his pool to keep their fs at 1 while being able to withdraw ETH earnings
- **Submitted by**: Aslanbek Aibimov, also found by cccz
- **Severity**: Medium Risk
- **Context**: (No context files were provided by the reviewer)
- **Description**: The trust Score depends on three factors: total ETH staked in the pool, Booster, and financial stability. Financial stability is the ratio of current ETH earnings to max ETH earning, so the reason why pool owners would not claim their ETH earnings is to not decrease their financial stability. The purpose of FS formula is to impose a temporary penalty on pool owners for withdrawing ETH earnings; however, this penalty can be bypassed: a pool owner would monitor the mempool for incoming transactions into their pool, and withdraw as much ETH as they are going to receive in owner fees from the upcoming transaction.
- **Likelihood**: Many of the pool owners could be interested in this exploit, as it would allow them to withdraw liquid ETH for any purpose without affecting their financial stability.
- **Proof of concept**:
  1. Bob signs a transaction that is going to stake 50 ETH into Alice\u0027s pool.
  2. Alice frontruns Bob and withdraws 1 ETH from her EthEarnings, decreasing her financial stability.
  3. Bob\u0027s transaction makes Alice 1 ETH in owner fees, so Alice\u0027s FS is instantly back to 1.
- **Recommendation**: Perhaps, more incentives for keeping financial stability as high as possible should be introduced.

---
