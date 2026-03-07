# BlockBusters - Rewards might get stuck when approved actor renews a position

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** MagicSea Staking
**Keywords:** cybersecurity, vulnerability, smart contract, NFT, approved actor, harvest function, renewLockPosition, rewards, tokenId, msg.sender, MlumStaking, Chainlink keeper, funds, internal function, bug, extendLockPosition, manual review, foundry, position owner, loss of rewards

---

BlockBusters

Medium

# Rewards might get stuck when approved actor renews a position

## Summary

When an approved actor calls the harvest function, the rewards get sent to the user (staker). However, when the approved actor renews the user’s position, they receive the rewards instead.

If the approved actor is a smart contract (e.g., a keeper), the funds might get stuck forever or go to the wrong user, such as a Chainlink keeper.

## Vulnerability Detail

Suppose Alice mints an NFT by creating a position and approves Bob to use it.

- When Bob calls \u0060harvestPosition\u0060 with Alice’s \u0060tokenId\u0060, Alice will receive the rewards (as intended)
- When Bob calls \u0060renewLockPosition\u0060 with Alice’s \u0060tokenId\u0060, Bob will receive the rewards. The internal function \u0060_lockPosition\u0060, which is called by \u0060renewLockPosition\u0060, also harvests the position before updating the lock duration. Unlike the harvest function, \u0060_lockPosition\u0060 [sends the rewards to \u0060msg.sender\u0060](https://github.com/sherlock-audit/2024-06-magicsea/blob/main/magicsea-staking/src/MlumStaking.sol#L710) instead of the token owner.

This bug exists in both \u0060renewLockPosition\u0060 and \u0060extendLockPosition\u0060, as they both call \u0060_lockPosition\u0060, which includes the wrong receiver.

### PoC

To run this test, add it into \u0060MlumStaking.t.sol\u0060.

\u0060\u0060\u0060solidity
function testVuln_ApprovedActorReceivesRewardsWhenRenewingPosition() public {
    // setup pool
    uint256 _amount = 100e18;
    uint256 lockTime = 1 days;

    _rewardToken.mint(address(_pool), 100_000e6);
    _stakingToken.mint(ALICE, _amount);

    // alice creates new position
    vm.startPrank(ALICE);
    _stakingToken.approve(address(_pool), _amount);
    _pool.createPosition(_amount, lockTime);
    vm.stopPrank();

    // alice approves bob
    vm.prank(ALICE);
    _pool.approve(BOB, 1);

    skip(1 hours);

    // for simplicity of the PoC we use a static call
    // IMlumStaking doesn\u0027t include \u0060renewLockPosition(uint256)\u0060
    uint256 bobBefore = _rewardToken.balanceOf(BOB);
    vm.prank(BOB);
    address(_pool).call(abi.encodeWithSignature("renewLockPosition(uint256)", 1));

    // Bob receivew the rewards, instead of alice
    assertGt(_rewardToken.balanceOf(BOB), bobBefore);
}
\u0060\u0060\u0060

## Impact

Possible loss of reward tokens

## Code Snippet

https://github.com/sherlock-audit/2024-06-magicsea/blob/main/magicsea-staking/src/MlumStaking.sol#L710

## Tool used

Manual Review, Foundry

## Recommendation

Change \u0060_lockPosition()\u0060 in \u0060MlumStaking.sol\u0060  to use the owner of the position instead of \u0060msg.sender\u0060.

\u0060\u0060\u0060solidity
function _lockPosition(uint256 tokenId, uint256 lockDuration, bool resetInitial) internal {
    ...
-   _harvestPosition(tokenId, msg.sender);
+   _harvestPosition(tokenId, _ownerOf(tokenId));
    ...
}
\u0060\u0060\u0060

