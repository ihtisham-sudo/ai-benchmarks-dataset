# Issue H-1: FluidLocker::_getUnlockingPercentage() incorrectly divides one of the components of the formula by S, leading to always having 80% penalty

**Severity:** high
**Auditor:** Sherlock
**Protocol:** SuperFluid Finance 
**Keywords:** FluidLocker, _getUnlockingPercentage, unlocking percentage, penalty, formula, Math.sqrt, _SCALER, unlockPeriod, stakers, contract, solidity, bug, calculation, loss, user, unlock, duration, component, PR, fix

---

# Issue H-1: FluidLocker::_getUnlockingPercentage() incorrectly divides one of the components of the formula by S, leading to always having 80% penalty

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-superfluid-locking-contract-judging/issues/20)

Found by: 056Security, 0x73696d616f, Drynooo, IvanFitro, Kyosi, Z3R0, ke1caM, newspacexyz, redbeans, zhenyazhd

FluidLocker::_getUnlockingPercentage() calculates the percentage to unlock, which is the amount given to the user, while the remaining goes to other stakers. The formula incorrectly divides Math.sqrt(unlockPeriod * _SCALER) by _SCALER:

\u0060\u0060\u0060solidity
function _getUnlockingPercentage(uint128 unlockPeriod) internal pure returns (uint256 unlockingPercentageBP) {
    unlockingPercentageBP = (
        _PERCENT_TO_BP
            * (
                ((80 * _SCALER) / Math.sqrt(540 * _SCALER)) *
                (Math.sqrt(unlockPeriod * _SCALER) / _SCALER //@audit this _SCALER should not be here)
                + 20 * _SCALER
            )
    ) / _SCALER;
}
\u0060\u0060\u0060

In FluidLocker:388, it incorrectly divides the term (Math.sqrt(unlockPeriod * _SCALER) by _SCALER.

None.
## External Pre-conditions
None.

1. User unlocks their Fluid from the locker with a duration bigger than 0, unvesting it through the fountain.

User suffers a big loss; even if they unlock with the maximum period, they will still get 80% penalty.

The component \u0060(Math.sqrt(unlockPeriod*_SCALER)/_SCALER)<=sqrt(540*24*3600*1e18)/1e18=0\u0060 is always null, so only \u006020*_SCALER\u0060 is left, which always yields a 20% unlocking percentage.

Remove the extra \u0060_SCALER\u0060.

\u0060\u0060\u0060solidity
function _getUnlockingPercentage(uint128 unlockPeriod) internal pure returns (uint256 unlockingPercentageBP) {
    unlockingPercentageBP = (
        _PERCENT_TO_BP
            * (
                ((80 * _SCALER) / Math.sqrt(540 * _SCALER)) *
                (Math.sqrt(unlockPeriod * _SCALER))
                + 20 * _SCALER
            )
    ) / _SCALER;
}
\u0060\u0060\u0060

0xPilou  
Fix for this issue is included in the following PR:  
[https://github.com/superfluid-finance/fluid/pull/6](https://github.com/superfluid-finance/fluid/pull/6)  
sherlock-admin2

https://github.com/superfluid-finance/fluid/pull/6
