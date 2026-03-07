# cergyk - ZivoeYDL::distributeYield yield distribution is flash-loan manipulatable

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cybersecurity, vulnerability, flash loan, manipulation, ZivoeYDL, distributeYield, yield distribution, totalSupply, stZVE, attacker, staking, protocol earnings, residual earnings, gaming the system, distributed yields, withdrawal, undeserved yields, time locking, claim rewards, manual review

---

cergyk

high

# ZivoeYDL::distributeYield yield distribution is flash-loan manipulatable

## Summary

\u0060ZivoeYDL::distributeYield\u0060 is used to "distributes available yield within this contract to appropriate entities" but it relies on the tokens \u0060totalSupply()\u0060 which can be manipulable through a flashloan.

## Vulnerability Detail

\u0060ZivoeYDL::distributeYield\u0060 relies on \u0060stZVE().totalSupply()\u0060 to distribute protocol earnings and residual earnings:

[ZivoeYDL.sol#L241-L310](https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeYDL.sol#L241-L310)
\u0060\u0060\u0060solidity
        // Distribute protocol earnings.
...
            else if (_recipient == IZivoeGlobals_YDL(GBL).stZVE()) {
                uint256 splitBIPS = (
>>                  IERC20(IZivoeGlobals_YDL(GBL).stZVE()).totalSupply() * BIPS
                ) / (
                    IERC20(IZivoeGlobals_YDL(GBL).stZVE()).totalSupply() + 
                    IERC20(IZivoeGlobals_YDL(GBL).vestZVE()).totalSupply()
                );
...
        // Distribute residual earnings.
...
                else if (_recipient == IZivoeGlobals_YDL(GBL).stZVE()) {
                    uint256 splitBIPS = (
>>                      IERC20(IZivoeGlobals_YDL(GBL).stZVE()).totalSupply() * BIPS
                    ) / (
                        IERC20(IZivoeGlobals_YDL(GBL).stZVE()).totalSupply() + 
                        IERC20(IZivoeGlobals_YDL(GBL).vestZVE()).totalSupply()
                    );
...
\u0060\u0060\u0060

This can be abused by an attacker by buying then staking a very large amount of \u0060ZVE\u0060 right before calling \u0060ZivoeYDL::distributeYield\u0060 (a flashloan can be used) in order to game the system and collect a lot more distributed yields than he should be entitled to.

### Scenario

1. Attacker buys and stakes a very large amount of \u0060ZVE\u0060 through a flashloan
2. Attacker calls \u0060ZivoeYDL::distributeYield\u0060
3. Attacker collects a very large amount of distributed yields
4. Attacker withdraws and sells back his \u0060ZVE\u0060 tokens effectively stealing undeserved yields

## Impact

A user can systematically claim a big chunk of the rewards reserved to \u0060stZVE\u0060 and \u0060vestZVE\u0060 in \u0060ZivoeYDL\u0060 by using a flash loan

## Code Snippet

- https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeYDL.sol#L241-L310

## Tool used

Manual Review

## Recommendation

Use a minimal time locking for stZVE such as it would not be possible to stake and unstake all in one block, or use past (1 block in the past) total supply to claim rewards
