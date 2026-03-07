# Kral01 - [M-01] Allocation can start before registration ends. Which can break things in strategies.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, allocation, registration, timestamp, QVBaseStrategy, DonationVotingMerkleDistributionBaseStrategy, recipient, funds, reviewRecipients, status, false distribution, manual review, impact, medium impact, high impact, check, revert, protocol, strategy

---

Kral01

medium

# [M-01] Allocation can start before registration ends. Which can break things in strategies.

Allocation can start before registration ends. Which can break things in strategies. When using \u0060QVBaseStrategy\u0060 and \u0060DonationVotingMerkleDistributionBaseStrategy\u0060 .

## Vulnerability Detail

The way that timestamps are set or specifically, validated right now allows \u0060Allocation\u0060 to start before \u0060Registration\u0060 ends. I havent git a clear answer from the protocol team regarding whether this is intended or not, but even if it is intended, this can potentially break some stuff in \u0060QVBaseStrategy\u0060 and \u0060DonationVotingMerkleDistributionBaseStrategy\u0060. 

If \u0060_registerRecipient\u0060 is called while \u0060Allocation\u0060 is active on both [QVBaseStrategy](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/6430c8004017e96ae2f5aac365bdefd0b6eeea72/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L369C3-L430C6) and [DonationVotingMerkleDistributionBaseStrategy](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/6430c8004017e96ae2f5aac365bdefd0b6eeea72/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L528C4-L601C6) This can completely modify the effects of \u0060reviewRecipients\u0060 and rewrite the status of already \u0027reviewed\u0027 recipients. This can cause rewards being falsely distributed or even stuck as well.

Of course there is a check to see if the caller is a member of the pool. Since the members are \u0027trusted\u0027 then the likelihood is low, thus the impact will be medium, if those roles are not to be trusted, then impact can potentially be high.

## Impact

Recipient statuses can be modified and altered causing funds to sent falsely or get stuck.

## Code Snippet

This is the check to validate timestamps in both strategies. As we can see, it allows \u0060allocationStartTime\u0060 to be less than \u0060registrationEndTime\u0060.

\u0060\u0060\u0060javascript
  if (
            block.timestamp > _registrationStartTime || _registrationStartTime > _registrationEndTime
                || _registrationStartTime > _allocationStartTime || _allocationStartTime > _allocationEndTime
                || _registrationEndTime > _allocationEndTime 
        ) {//@audit I think we can start allocation before registration ends
            revert INVALID();
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation

Consider adding check to revert if allocation can start before registration ends:
\u0060\u0060\u0060javascript
  if (
            block.timestamp > _registrationStartTime || _registrationStartTime > _registrationEndTime
                || _registrationStartTime > _allocationStartTime || _allocationStartTime > _allocationEndTime
                || _registrationEndTime > _allocationEndTime  || _registrationEndTime > _allocationStartTime 
        ) {
            revert INVALID();
\u0060\u0060\u0060
