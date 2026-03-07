# IssueH-1: ClaimRestrictionPreventsUsers fromClaimingMultipleEpochs

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Gamme Brevis Rewarder
**Keywords:** claim, rewards, epochs, user engagement, protocol, restriction, activity, handleProofResult, require, amount, cumulative claim, mapping, block, distribution, eligible, revert, opportunity, satisfaction, check, claiming

---

# IssueH-1: ClaimRestrictionPreventsUsers fromClaimingMultipleEpochs

**Source:**  
https://github.com/sherlock-audit/2024-10-gamma-rewarder-judging/issues/212

**Found by:**  
056Security, 0xAadi, 0xDemon, 0xMosh, 0xNirix, 0xSolus, 0xhuh2005, 0xjarix, 0xlemon, Artur, Atharv, Breeje, Cayde-6, Chonkov, Galturok, Hunter, Japy69, MaslarovK, NoOneWinner, Ollam, PNS, Pro_King, WildSniper, cergyk, dobrevaleri, irresponsible, joshuajee, merlin, ni8mare, rzizah, sammy, silver_eth, spark1, vinica_boy

**Summary**  
After a user makes a claim, they are unable to claim rewards for subsequent epochs due to a check that restricts claims based on prior activity.

**Root Cause**  
The handleProofResult function includes a check that requires the claimed amount to be zero (\u0060require(claim.amount==0,”Already claimed reward.”);\u0060). Once a user successfully claims rewards, this condition prevents them from claiming for any future epochs, as their claim amount is no longer zero.

**Internal pre-conditions**  
No response

**External pre-conditions**  
No response

**Attack Path**  
For simplicity, let’s assume the distribution rewards are set to 100 blocks, with a total of 100 rewards to be distributed and blocks per epoch set to 20, resulting in 5 epochs. In this scenario, the amount per epoch is 20. If Kate is eligible to claim for the entire period and, at block 21, she claims rewards for blocks 0-20, the amount recorded in the CumulativeClaim (in the mapping claimed) for Kate for this token and reward distribution will be 20. If Kate attempts to claim rewards for any other epoch, her request...
would revert due to the check: require(claim.amount==0, "Already claimed reward."); as claim.amount would be 20. Kate should be eligible to claim for other epochs, but she is not. 

Github Link

Users are unable to claim rewards for multiple epochs after their initial claim, resulting in missed opportunities to receive rewards. This restriction diminishes user engagement and overall satisfaction with the protocol.

No response

No response

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/GammaStrategies/GammaRewarder/pull/2](https://github.com/GammaStrategies/GammaRewarder/pull/2)
