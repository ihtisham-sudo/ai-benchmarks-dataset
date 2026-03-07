# Scenario in ReferralSystem.referralDrawFinalize() where reward (for both referrer and player) < totalTicketsForReferrersPerCurrentDraw can result in loss of rewards

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Kwenta Staking Contracts
**Keywords:** cybersecurity, vulnerability, referrer reward, player rewards, lottery draw, tickets sold, reward loss, referral system, claimPerDraw, precision loss, manual review, mitigation steps, reward components, totalReward, totalTicketCount, struct, division, multiplication, unclaimed tickets, drawFinalized

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/ReferralSystem.sol#L99-L100
https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/ReferralSystem.sol#L105


# Vulnerability details

## Impact
If there is a sufficiently small referrer reward and correspondingly large amount of eligible referred tickets sold for a given draw, there is potential for the reward for one ticket to = 0, leading to loss of rewards.

## Proof of Concept
Example context for player rewards (same situation applies for referrer rewards):

- Assume all tickets are bought by 1 user
- \u0060playerRewardForDraw = 99\u0060
- \u0060ticketsSoldDuringDraw = 100\u0060

\u0060ReferralSystem.referralDrawFinalize()\u0060 is called when finalizing a lottery draw, and in this case, the user should receive the full 99 from \u0060playerRewardForDraw\u0060.

However, since in \u0060referralDrawFinalize()\u0060
\u0060playerRewardsPerDrawForOneTicket[drawFinalized] = playerRewardForDraw / ticketsSoldDuringDraw\u0060 rounds down to 0,
and later in \u0060claimPerDraw()\u0060
\u0060claimedReward += playerRewardsPerDrawForOneTicket[drawId] * _unclaimedTickets.playerTicketCount;\u0060,
although the user should receive the full allocated amount of the reward (99), they receive 0.


## Tools Used
Manual review

## Recommended Mitigation Steps
Some suggestions:
- Ensure rewards are stored according to the # decimals in the underlying token (ie: 1 LOT is stored as 1e18), so that it is very unlikely to have \u0060# tickets sold > reward\u0060
- In \u0060referralDrawFinalize()\u0060, store the draw\u0027s reward components (ie: \u0060totalReward\u0060 & \u0060totalTicketCount\u0060) as a struct and perform the division after the multiplication in \u0060claimPerDraw\u0060 in order to minimize the precision loss.
(ie: this would become \u0060userReward = userTicketCount * totalReward / totalTicketCount\u0060)
