# BoRonGod - DAO unable to withdraw their funds due to Convex admin action

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cyber security, vulnerability, DAO, Convex, admin action, Zivoe protocol, funds stuck, pull/pull assets, restricted access, BaseRewardPool.sol, extraRewards, malicious token, claimRewards, pullFromLocker, asset management, protocol risks, contingency plan, manual review, user impact, withdrawal issues

---

BoRonGod

medium

# DAO unable to withdraw their funds due to Convex admin action

## Summary

Convex admin action can lead to the fund of Zivoe protocol and its users being stuck, resulting in DAO being unable to push/pull assets from convex_lockers.

## Vulnerability Detail

Per the contest page, the admins of the protocols that Zivoe integrates with are considered "RESTRICTED". This means that any issue related to Convex‘s admin action that could negatively affect Zivoe protocol/users will be considered valid in this audit contest.

> Q: Are the admins of the protocols your contracts integrate with (if any) TRUSTED or RESTRICTED?
> 
> RESTRICTED

In current \u0060BaseRewardPool.sol\u0060 used by convex, admin can add infinite \u0060extraRewards\u0060:

    function extraRewardsLength() external view returns (uint256) {
        return extraRewards.length;
    }

    function addExtraReward(address _reward) external returns(bool){
        require(msg.sender == rewardManager, "!authorized");
        require(_reward != address(0),"!reward setting");

        extraRewards.push(_reward);
        return true;
    }

By setting a malicious token or add a lot of tokens, it is easy to completely forbid Zivoe DAO to \u0060pullFromLocker\u0060, since claimRewards() is forced to call:

    function pullFromLocker(address asset, bytes calldata data) external override onlyOwner {
        require(asset == convexPoolToken, "OCY_Convex_C::pullFromLocker() asset != convexPoolToken");
        
        claimRewards(false);
        ...

## Impact

The fund of Zivoe protocol and its users will be stuck, resulting in users being unable to withdraw their assets.

## Code Snippet

https://github.com/convex-eth/platform/blob/main/contracts/contracts/BaseRewardPool.sol#L109

## Tool used

Manual Review

## Recommendation

Ensure that the protocol team and its users are aware of the risks of such an event and develop a contingency plan to manage it.

