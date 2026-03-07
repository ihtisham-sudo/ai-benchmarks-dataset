# 23 - Quorum Manipulation Risk

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** FrankenDAO
**Keywords:** quorum, manipulation, delegation, voting, proposals, malicious, delegate, unstake, locked, token, governance, active proposals, emergency eject, blacklist, cooldown, veto, bonus, community score, proposer, abuse

---

# sherlock-admin

Escalation accepted. Assigning medium severity as the impact is not that significant + it requires a lot of effort to execute.

The quorum can be manipulated which can lead to unexpected behavior as illustrated.

This issue\u0027s escalations have been accepted! Contestants\u0027 payouts and scores will be updated according to the changes made on this issue.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/23)  
**Found by:** rvierdiiev, curiousapple, 0x52  

Users are allowed to delegate their votes to other users. Since staking does not implement checkpoints, users are not allowed to delegate or unstake during an active proposal if their delegate has already voted. A malicious delegate can abuse this by creating proposals so that there is always an active proposal and their delegatees are always locked to them.

\u0060\u0060\u0060solidity
modifier lockedWhileVotesCast() {
    uint[] memory activeProposals = governance.getActiveProposals();
    for (uint i = 0; i < activeProposals.length; i++) {
        if (governance.getReceipt(activeProposals[i], getDelegate(msg.sender)).hasVoted) revert TokenLocked();
        (, address proposer,) = governance.getProposalData(activeProposals[i]);
        if (proposer == getDelegate(msg.sender)) revert TokenLocked();
    }
    _;
}
\u0060\u0060\u0060
The above modifier is applied when unstaking or delegating. This reverts if the delegate of msg.sender either has voted or currently has an open proposal. The result is that under those conditions, the delegatee cannot unstake or delegate. A malicious delegate can abuse these conditions to keep their delegatees forever delegated to them. They would keep opening proposals so that delegatees could never unstake or delegate. A single user can only have one proposal opened at the same time, so they would use a secondary account to alternate and always keep an active proposal.

Delegatees can never unstake or delegate to anyone else.
[Staking.sol](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L166-L174)

Manual Review

There should be a function to emergency eject the token from staking. To prevent abuse, a token that has been emergency ejected should be blacklisted from staking again for a certain cooldown period, such as the length of the current voting period.

zobront  
In the case that a user did this, Admins would create a contract that all "stuck" users approve, and they would veto and unstake all tokens in one transaction. It would be inconvenient, but no long-term harm would be caused.  
I still think it\u0027s valid as a Medium, as this is obviously a situation we\u0027d like to avoid being possible.  
zobront  
Fixed: [PR #18](https://github.com/Solidity-Guild/FrankenDAO/pull/18)  
This fix addresses the risk laid out in the issue, that a delegate may repeatedly propose to keep votes locked.  
We chose to not address the similar risk with voting because admins need to explicitly verify proposals before they can be voted on, so in the event this happens, admins would just hold off on verifying to give them a chance to undelegate.  
We decided to go this direction because the cooldown period would add extra complexity and slightly increase gas fees on transactions that we plan to refund a lot of.  
jack-the-pug  
Fix confirmed
**Source:** [GitHub Issue #9](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/9)  
**Found by:** neumo, Trumpero  

When a proposal that has passed is vetoed, the proposer still has the bonus of proposals Created and proposals Passed related to the proposal. Both should be decremented because veto is intended to be used for malicious proposals.

The function \u0060getCommunityVotingPower\u0060 returns a bonus to users for voting, creating proposals, and having them passed. [Link to code](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L520-L541). The veto function is supposed to be used against malicious proposals (see comment in line 522): [Link to code](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Governance.sol#L520-L534). So the malicious proposer should not keep a bonus based on this proposal\u0027s creation and/or passing, and the function should decrease both the values of proposals Created and proposals Passed.

Malicious proposer keeps bonus after his proposal is vetoed.

N/A

Manual Review

Put a check in the veto function that decreases the values of both proposals Created and proposals Passed.
\u0060\u0060\u0060javascript
if(proposal.verified){
  --userCommunityScoreData[proposal.proposer].proposalsCreated;
  --totalCommunityScoreData.proposalsCreated;
}
if (state(_proposalId) == ProposalState.Queued){
  --userCommunityScoreData[proposal.proposer].proposalsPassed;
  --totalCommunityScoreData.proposalsPassed;
}
\u0060\u0060\u0060

**ZakkMan**  
Fixed: [https://github.com/Solidity-Guild/FrankenDAO/pull/22](https://github.com/Solidity-Guild/FrankenDAO/pull/22)  
**jack-the-pug**  
Fix confirmed
PAGE END
