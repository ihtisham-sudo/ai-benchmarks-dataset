# 3.2.15 Possible DoS of the AllocationVesting.transferPoints() by front-running

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** DoS, front-running, transferPoints, vesting period, allocation, points, revert, self-transfer, insufficient points, incompatible vesting period, malicious users, investors, address, legal transfer, proof of concept, allocation state, zero points, callerOrDelegated, allocationVesting, Ethereum

---

# 3.2.15 Possible DoS of the AllocationVesting.transferPoints() by front-running
**Submitted by:** KupiaSec  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Summary:** The transferPoints() can be DoSed if a recipient address has a different vesting period by front-running.  

The transferPoints() (AllocationVesting.sol) checks if the sender and recipient have the same vesting periods.

\u0060\u0060\u0060solidity
function transferPoints(address from, address to, uint24 points) external callerOrDelegated(from) {
    // revert on self-transfer to prevent infinite points exploit
    if (from == to) revert SelfTransfer();
    // revert on zero points input
    if (points == 0) revert ZeroAllocation();
    // cache allocation state of \u0060from\u0060 and \u0060to\u0060 addresses
    AllocationState memory fromAllocation = allocations[from];
    AllocationState memory toAllocation = allocations[to];
    // revert if \u0060from\u0060 has less points allocation than they are
    // trying to transfer
    if (fromAllocation.points < points) revert InsufficientPoints();
    // enforce identical vesting periods if \u0060to\u0060 has an active vesting period
    if (toAllocation.numberOfWeeks != 0 && toAllocation.numberOfWeeks != fromAllocation.numberOfWeeks) //@audit
        revert IncompatibleVestingPeriod(fromAllocation.numberOfWeeks, toAllocation.numberOfWeeks);
}
\u0060\u0060\u0060

Malicious users might use this validation to make it revert during a legal transfer. Here is a simple example:
- There are 2 investors - Alice and Bob who have 4 weeks and 8 weeks vesting periods.
- 4 weeks later, Bob is going to transfer the points to his another address.
- Alice transfers her points to Bob\u0027s address before Bob\u0027s transfer.
- Alice gets all of the vesting funds because her vesting period has ended already.
- But Bob\u0027s transfer reverts because his address has a different vesting period already.

Users wouldn\u0027t be able to transfer points to their addresses forever.

Medium because there is no loss for a front-runner if he does after his vesting period.

Here is a detailed proof of concept:
\u0060\u0060\u0060  
\u0060\u0060\u0060
