# jkoppel - The 1-second overlap between the during- and after-allocation periods may cause funds to become stuck, permanently.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, funds, allocation, QV strategy, DonationVotingMerkle, pool manager, voting rights, distribute transaction, block timestamp, onlyActiveAllocation, onlyAfterAllocation, collusion, permanent loss, EVM-compatible chain, manual review, withdraw function, QVSimplStrategy, Bob' vote, Carol

---

jkoppel

medium

# The 1-second overlap between the during- and after-allocation periods may cause funds to become stuck, permanently.

There is a 1-second overlap between the  during- and after-allocation periods of both the QV strategy and the DonationVotingMerkle strategies. In the QV strategy, this can lead to funds permanently becoming stuck.

## Vulnerability Detail

1. A QVSimpleStrategy pool is created. Alice is the Pool manager. 10 people are given voting rights. The pool is funded for 100k USDC.
2. Everyone except Bob votes, giving Carol and Dan each 50% of the votes.
3. Carol tells Alice she really needs the money, and asks her to distribute ASAP. Alice schedules a distribute() transaction to occur the moment allocation ends.
4. At the last minute, the Bob votes, casting all his votes for Carol.
5. It so happens that Alice and Bob\u0027s transaction occur in the same block. Further, it so happens that this block is scheduled with block.timestamp exactly equal to \u0060allocationEndTime\u0060. (Note that, other some comments talk about the registration and allocation period times being in milliseconds, they are actually in seconds.)
6. For this second, both \u0060onlyActiveAllocation\u0060 and \u0060onlyAfterAllocation\u0060 pass
7.  Bob\u0027s vote gets scheduled within the block after the call to distribute()
8. The call to distribute gives 50% of the funds to Carol, or 50k USDC. Bob\u0027s vote changes  the total so that 55% of votes are for Carol, and 45% for Dan.
9. Dan can now be given his $45k. But the remaining $5k is stuck in the pool forever.

If there is one block every 40 seconds, then there is a 2.5% chance that a block will run on the exact second of overlap. However, the contest page says it should run on any EVM-compatible chain. If there is a rollup that has blocks every second, then the conditions for this bug to occur has a 100% chance

If there is collusion from the miner, then there is also a significantly higher chance.

## Impact

A chance of permanent loss of funds

## Code Snippet

When \u0060block.timestamp == allocationEndTime\u0060, then both _checkOnlyAfterRegistration and _checkOnlyActiveAllocation pass.

I am guessing that the protocol authors thought \u0060block.timestamp\u0060 was in milliseconds, when it is actually in seconds. That makes this problem 1000x more likely to occur  without miner collusion.

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L317C1-L328C6

\u0060\u0060\u0060solidity
   function _checkOnlyActiveAllocation() internal view virtual {
        if (allocationStartTime > block.timestamp || block.timestamp > allocationEndTime) {
            revert ALLOCATION_NOT_ACTIVE();
        }
    }

    /// @notice Check if the allocation has ended
    /// @dev Reverts if the allocation has not ended
    function _checkOnlyAfterAllocation() internal view virtual {
        if (block.timestamp < allocationEndTime) revert ALLOCATION_NOT_ENDED();
    }
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation

1. Don\u0027t have this 1-second overlap
2. Add a withdraw function to QVBaseStrategy

