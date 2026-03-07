# bughuntoor - Rewards supplied to a gauge, prior to its first depositor will be permanently lost.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cyber security, vulnerability, rewards, gauge, depositor, permanently lost, pool weight, Voter contract, automatic rewards, loss of funds, impact, manual review, recommendation, revert, current supply, funds management, smart contracts, blockchain, financial security, risk assessment

---

bughuntoor

Medium

# Rewards supplied to a gauge, prior to its first depositor will be permanently lost.

## Summary
Rewards supplied to a gauge, prior to its first depositor will be permanently lost.

## Vulnerability Detail
Every week, gauges receive rewards based on their pool weight, within the Voter contract.

\u0060\u0060\u0060solidity
    function distribute(address _gauge) public lock {
        IMinter(minter).update_period();
        _updateFor(_gauge); // should set claimable to 0 if killed
        uint _claimable = claimable[_gauge];
        if (_claimable > IGauge(_gauge).left(base) && _claimable / DURATION > 0) {
            claimable[_gauge] = 0;
            if((_claimable * 1e18) / currentEpochRewardAmount > minShareForActiveGauge) {
                activeGaugeNumber += 1;
            }

            IGauge(_gauge).notifyRewardAmount(base, _claimable);
            emit DistributeReward(msg.sender, _gauge, _claimable);
        }
    }
\u0060\u0060\u0060

The problem is that any rewards sent to the gauge prior to its first depositor will remain permanently stuck. Given that rewards are sent automatically, the likelihood of such occurrence is significantly higher

## Impact
Loss of funds

## Code Snippet
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/GaugeV4.sol#L563

## Tool used

Manual Review

## Recommendation
Revert in case current supply is 0.
