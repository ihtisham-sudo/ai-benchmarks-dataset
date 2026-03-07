# 174 - User deposit may remain stuck in deposit queue

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Y2K Finance
**Keywords:** depositQueue, user deposit, relayer, FILO, gas, queue, manual review, DDoS, withdraw, economic damage, attack vector, Carousel, Y2K, commit, epoch, function, recommendation, fix, pull request, duplicate, issue

---

# Discussion
3xHarry will use one location for the treasury address which will be on the factory.

3xHarry fixed in [this pull request](https://github.com/Y2K-Finance/Earthquake/pull/137).

IAm0x52 Needs additional changes. Controller still sends to its immutable address and not the treasury address on the factory.

IAm0x52 Fix looks good. Controller has been updated to use the treasury address from the factory.

jacksanford1 Note: 0x52 is referring to this specific commit in the last message: [commit link](https://github.com/Y2K-Finance/Earthquake/pull/137/commits/272199687465252d1da8cb1af624e90c12315953).
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/122)  
**Found by:** 0x52, Ch_301, bin2chen, carrot, cccz, hickuphh3, immeas, kenzo, libratus, ltyu, roguereddwarf, sinarette  

If either the premium and/or collateral vault has 0 TVL for an epoch with emissions, those emissions will not be withdrawable by anyone.

The final TVL set for a vault with 0 TVL (epoch will be nullified) will be 0. As a result, emissions that were allocated to that vault are not withdrawable by anyone. It\u0027s admittedly unlikely to happen since the emissions token is expected to be Y2K which has value and is tradeable.

Emissions cannot be recovered.

- [Carousel.sol#L157](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L157)
- [Carousel.sol#L630-L636](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L630-L636)

Manual Review

Create a function to send emissions back to the treasury if an epoch is marked as nullified. A related issue is that if both the premium and collateral vaults have 0 TVL, only the collateral vault gets marked as nullified. Consider handling this edge case.
3xHarry  
great catch  
3xHarry  
fix PR: https://github.com/Y2K-Finance/Earthquake/pull/139  
IAm0x52  
Fix looks good. setEpochNull is overridden in Carousel to transfer emissions back  
to treasury
**Source:** [GitHub](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/172)  
**Found by:** Ace-30, ElKu, Respx, ShadowForce, TrungOre, bin2chen, ck, evan, hickuphh3, immeas, minhtrng, nobody2018, twicek  

rolloverQueue is shared by all epochs. For each round of epoch, mintRollovers will process rolloverQueue from the beginning. A normal user calls enlistInRollover to enter the rolloverQueue, and in the next round of epoch, he will call delistInRollover to exit the rolloverQueue. In this case, rolloverQueue.length is acceptable. However, a malicious user can make the rolloverQueue.length huge, causing the relayer to consume a huge amount of gas for every round of epoch. Carousel will send relayerFee to relayer in order to encourage external relayer to call mintRollovers. Malicious user can make external relayer unwilling to call mintRollovers. Ultimately, rolloverQueue will never be processed.

Let\u0027s assume the following scenario: relayerFee is 1e18. The current epochId is E1, and the next epochId is E2. At present, rolloverQueue has 10 normal user QueueItem. Bob has deposited 1000e18 assets before the start of E1, so balanceOf(bob, E1) = 1000e18.
1. Bob creates 1000 addresses, each address has setApprovalForAll to bob. He calls two functions for each address:
   - Carousel.safeTransferFrom(bob, eachAddress, E1, 1e18)
   - Carousel.enlistInRollover(E1, 1e18, eachAddress), 1e18 equal to minRequiredDeposit.
2. rolloverQueue.length equals to 1010 (1000 + 10).

These 1000 addresses will never call delistInRollover to exit the rolloverQueue, so no matter whether these addresses win or lose, their QueueItem will always be in the rolloverQueue. In each round of epoch, the relayer has to process at least 1000 QueueItems, and these QueueItems are useless. Malicious users only need to do it once to cause permanent effects.

When a normal user loses in a certain round of epoch, he may not call delistInRollover to exit the rolloverQueue. For example, he left the platform and...
## Rollover Queue Growth
The rolloverQueue.length will become larger and larger as time goes by. The Carousel contract will not send any relayer Fee to the relayer, because these useless Queue Items will not increase the value of [executions](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L447). Obviously, calling mintRollovers has no benefit for the relayer. Therefore, no relayer is willing to do this.

### Impact
The relayer consumes a huge amount of gas for calling mintRollovers for each round of epoch. In other words, as long as the rolloverQueue is unacceptably long, it is a permanent DOS.

### Code Snippet
- [Carousel.sol L361-L459](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L361-L459)
- [Carousel.sol L238-L271](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L238-L271)

### Tool Used
Manual Review

### Recommendation
We should change the single queue to queue mapping. In this way, the relayer only needs to process the queue corresponding to the epochId.

\u0060\u0060\u0060diff
--- a/Earthquake/src/v2/Carousel/Carousel.sol
+++ b/Earthquake/src/v2/Carousel/Carousel.sol
@@ -23,7 +23,7 @@ contract Carousel is VaultV2 {
     IERC20 public immutable emissionsToken;
     mapping(address => uint256) public ownerToRollOverQueueIndex;
-    QueueItem[] public rolloverQueue;
+    mapping(uint256 => QueueItem[]) public rolloverQueues;
     QueueItem[] public depositQueue;
     mapping(uint256 => uint256) public rolloverAccounting;
     mapping(uint256 => mapping(address => uint256)) public _emissionsBalances;
\u0060\u0060\u0060
I would disagree with the feasibility of this attack.
1. there is a non neglectable minDeposit which makes this attack much more expensive
2. the queue can be processed in multiple transactions and the relayerFee is supposed to be configured so much so that each processed item gas consumption is reimbursed with a profit
## IAm0x52
Issue has been acknowledged by sponsor
**Source:** [GitHub Issue #174](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/174)  
**Found by:** 0Kage, 0xmuxyz, Ruhum, TrungOre, ck, csanuragjain, hickuphh3, jprod15, twicek  

Due to FILO (first in last out) stack structure, while dequeuing, the first few entries may never be retrieved. This means User deposit may never be entertained from deposit queue if there are too many deposits.

1. Assume User A made a deposit which becomes 1st entry in depositQueue.
2. Post this, X more deposits were made, so depositQueue.length = X + 1.
3. Relayer calls \u0060mintDepositInQueue\u0060 and processes X - 9 deposits.
   \u0060\u0060\u0060solidity
   while ((length - _operations) <= i) {
       // this loop implements FILO (first in last out) stack to reduce gas
       // cost and improve code readability
       // changing it to FIFO (first in first out) would require more code
       // changes and would be more expensive
       _mintShares(
           queue[i].receiver,
           _epochId,
           queue[i].assets - relayerFee
       );
       emit Deposit(
           msg.sender,
           queue[i].receiver,
           _epochId,
           queue[i].assets - relayerFee
       );
       depositQueue.pop();
       if (i == 0) break;
       unchecked {
           i--;
       }
   }
   \u0060\u0060\u0060
4. This reduces deposit queue to only 10.
Before relayer could process these, Y more deposits were made which increases deposit queue to y+10. This means Relayer might not be able to again process User A deposit as this deposit is lying after processing Y+9 deposits.

User deposit may remain stuck in deposit queue if a large number of deposits are present in queue and relayer is interested in dequeuing all entries.

[Carousel.sol](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L310)

Manual Review

Allow User to dequeue deposit queue based on index, so that if such condition arises, user would be able to dequeue his deposit (independent of relayer).

**3xHarry**: Depositing into queue should count as committing to an epoch. By giving the user the ability to delist his queue he could take advantage of market movements. However, we will raise min deposit for the queue to make DDoS very expensive.  
**twicek**: Escalate for 10 USDC.  

My issues #62 and #63 are both marked as duplicate of this issue when only #63 is actually a duplicate. #63 is a duplicate of #174 who both relate to how queued deposits can get stuck in the deposit queue for various reasons. #62 however, does not describe anything related to both the deposit queue and the separate fact that there is a DoS attack vector. Instead, it relates to how relayers can get griefed because unrollable rollover items in the rollover queue can aggregate and lead them to not get paid for their work. In the duplicates, that I will cite below, this issue is achieved in various different ways but they all lead to the same impact. Therefore, to reiterate, the #62 and #63 are different because they don\u0027t involve the same states, attack vector and users. #63 involve the deposit queue and a DoS.
## #62
Involves the rollover queue and a griefing attack that lead to economic damage for relayers.
