# bughuntoor - If user merges their \u0060veNFT\u0060, they\u0027ll lose part of their rewards

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cyber security, vulnerability, veNFT, rewards, claim rewards, last_token_time, RewardsDistributor, merge, token burn, msg.sender, approved, owner, loss of funds, manual review, impact, recommendation, user merge, funds loss, token approval, reward lag

---

bughuntoor

High

# If user merges their \u0060veNFT\u0060, they\u0027ll lose part of their rewards

## Summary
If user merges their \u0060veNFT\u0060, they\u0027ll lose part of their rewards

## Vulnerability Detail
When users claim rewards, they can at most claim up to the week before \u0060last_token_time\u0060.
\u0060\u0060\u0060solidity
        for (uint i = 0; i < 50; i++) {
            if (week_cursor >= _last_token_time) break;
\u0060\u0060\u0060
And given that \u0060last_token_time\u0060 can at most be this week, this means that rewards in the \u0060RewardsDistributor\u0060 are lagging at least a week at a time.

Then, if we look at the code of \u0060merge\u0060 we\u0027ll see that the \u0060from\u0060 token is actually burned.

\u0060\u0060\u0060solidity
    function merge(uint _from, uint _to) external {
        require(attachments[_from] == 0 && !voted[_from], "attached");
        require(_from != _to);
        require(_isApprovedOrOwner(msg.sender, _from));
        require(_isApprovedOrOwner(msg.sender, _to));

        LockedBalance memory _locked0 = locked[_from];
        LockedBalance memory _locked1 = locked[_to];
        uint value0 = uint(int256(_locked0.amount));
        uint end = _locked0.end >= _locked1.end ? _locked0.end : _locked1.end;

        locked[_from] = LockedBalance(0, 0);
        _checkpoint(_from, _locked0, LockedBalance(0, 0));
        _burn(_from);
        _deposit_for(_to, value0, end, _locked1, DepositType.MERGE_TYPE);
    }
\u0060\u0060\u0060

Since \u0060claim\u0060 requires \u0060msg.sender\u0060 to be approved or owner, because the token is burned, they won\u0027t be able to claim the rewards.
Any time a user merges their \u0060veNFT\u0060, they\u0027ll lose at least 1 week of rewards.

## Impact
Loss of funds

## Code Snippet
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L1208

## Tool used

Manual Review

## Recommendation
Do not burn the token
