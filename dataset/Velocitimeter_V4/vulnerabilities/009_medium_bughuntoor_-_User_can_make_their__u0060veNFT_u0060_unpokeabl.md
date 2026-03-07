# bughuntoor - User can make their \u0060veNFT\u0060 unpokeable by voting for a to-be-killed gauge

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cybersecurity, vulnerability, veNFT, poke, gauge, voting, balance, unlock_time, decaying, outdated votes, emissions, bribes, manual review, impact, protocol, admin intervention, unpokeable, recommendation, code snippet, user exploitation

---

bughuntoor

High

# User can make their \u0060veNFT\u0060 unpokeable by voting for a to-be-killed gauge

## Summary

## Vulnerability Detail
In order to understand the impact of the issue, we need to first understand why poke is critical to the system. When users vote for a pool of their choice, they contribute with the current balance of their veNFT. As the veNFT balance is linearly decaying, this results in possible outdated votes. For example: if a user has voted with a veNFT which has 10 weeks until unlock_time and 9 weeks have passed without anyone poking or revoting the veNFT, it will still be contributing with the balance from 9 weeks ago, despite the current balance being 10x less.

For this reason poking is introduced, so if a NFT has not been updated in a long time, admins can do it (usually in other protocols like Velodrome, poking is unrestricted and anyone can do it to make it fair for all users)

A user can make their \u0060veNFT\u0060 unpokeable in the following way:
1. Gauge is known that it will soon be killed
2. User votes most of their weight to the pool they\u0027d like and a dust amount to the to-be-killed gauge.
3. As soon as the gauge is killed, user\u0027s \u0060veNFT\u0060 becomes unpokeable due to the following check in \u0060_vote\u0060: 
\u0060\u0060\u0060solidity
            if (isGauge[_gauge]) {
                require(isAlive[_gauge], "gauge already dead");
\u0060\u0060\u0060

## Impact
User\u0027s gauge of choice will receive more emissions than supposed to. User will receive more bribes than supposed to.

## Code Snippet
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/Voter.sol#L266

## Tool used

Manual Review

## Recommendation
If gauge is killed, instead of reverting, \u0060continue\u0060
