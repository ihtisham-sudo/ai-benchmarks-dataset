# Issue M-2 - FluidLocker::_getUnlockingPercentage() divides before multiplying, suffering a significant precision error

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** SuperFluid Finance 
**Keywords:** FluidLocker, unlockingPercentage, precision error, calculation, BPS, tax pool, loss, divide, multiply, scaling, smart contract, Ethereum, solidity, financial loss, unlock period, function, Math, scaler, user impact, audit

---

# Issue M-2: FluidLocker::_getUnlockingPercentage() divides before multiplying, suffering a significant precision error

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-superfluid-locking-contract-judging/issues/22)  
Found by: 0x73696d616f  


FluidLocker::_getUnlockingPercentage() is calculated as:

\u0060\u0060\u0060solidity
function _getUnlockingPercentage(uint128 unlockPeriod) internal pure returns (uint256 unlockingPercentageBP) {
    unlockingPercentageBP = (
        _PERCENT_TO_BP
            * (
                ((80 * _SCALER) / Math.sqrt(540 * _SCALER)) *
                (Math.sqrt(unlockPeriod * _SCALER) / _SCALER)
                + 20 * _SCALER
            )
    ) / _SCALER;
}
\u0060\u0060\u0060

As can be seen, it divides before multiplying, leading to precision loss. The loss is always \((80*1e18)/Math.sqrt(540*24*3600*1e18)=1712139.4821\), so the 0.4821 component is discarded. This corresponds to \(0.4821*sqrt(540*24*3600*1e18)*100/1e18=0.00032929935BPS\).  
Note: this calculation assumed the other 2 issues are fixed.

As this loss is present in every calculation and it will make a 1 BPS difference in many instances, it is significant. For example, if the maximum duration is picked, instead of 10000 BPS, it will actually be 9999 BPS and 1 BPS goes to the TAX pool. If the user unlocks for example 1e5 USD, this is a 10 USD loss. As it will happen frequently, the loss will accumulate.


In FluidLocker::388, it divides before multiplying.
None.

None.

1. User calls unlock with vesting period, but due to the precision loss it rounds down and 1 BPS more goes to the tax distribution pool.

User suffers a 1 BPS loss of funds. For example, 1e5 USD will yield a 10 USD loss.

Presented in the summary.

Multiply before dividing as it will never overflow.

0xPilou  
Fix for this issue is included in the following PR:  
https://github.com/superfluid-finance/fluid/pull/6  

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/superfluid-finance/fluid/pull/6
## Issue M-3: A malicious user may unlock instantly all the funds from the FluidLocker when no one is staking in the Tax pool

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-superfluid-locking-contract-judging/issues/24)  
Found by: 0x73696d616f

The missing check in \u0060FluidLocker::_instantUnlock()\u0060 for stakers in the tax pool allows users to unlock all their funds without paying any tax instantly. This happens because whenever there are 0 stakers in the tax pool, the flow rate is set to 0 and it does not revert, so the user can loop unlocking until all funds are withdrawn.  
Note: \u0060FluidEPProgramManager::stopFunding()\u0060 also has issues related to 0 stakers in the program or tax pools.  
Note 2: The mentioned assumptions in the readme about assuming there are stakers before calls only refer to \u0060FluidEPProgramManager::startFunding()\u0060 and \u0060Fountaine::initialize()\u0060, not these 2 flows mentioned here.

In \u0060FluidLocker::_instantUnlock()\u0060 there is a missing check for 0 stakers in the tax pool.

### Internal pre-conditions
1. There are 0 stakers in the tax pool.

### External pre-conditions
None.

1. User loops \u0060FluidLocker::unlock()\u0060 with a null unlocking period and instantly withdraws all their funds.
The user is able to unlock all their funds without paying any tax.

Add the following test to \u0060FluidLocker.t.sol\u0060.

\u0060\u0060\u0060solidity
function test_POC_InstantUnlock_WithoutFees() external {
    _helperFundLocker(address(aliceLocker), 10_000e18);
    assertEq(_fluidSuperToken.balanceOf(address(ALICE)), 0, "incorrect Alice bal before op");
    assertEq(_fluidSuperToken.balanceOf(address(aliceLocker)), 10_000e18, "incorrect Locker bal before op");
    _helperUpgradeLocker();
    vm.startPrank(ALICE);
    for (uint i = 0; i < 30; i++) {
        aliceLocker.unlock(0, ALICE);
    }
    assertGt(_fluidSuperToken.balanceOf(address(ALICE)), 9.98e21, "incorrect Alice bal after op");
}
\u0060\u0060\u0060

Check if the pools have 0 units and revert if so.

0xPilou  
Fix for this issue is included in the following PR:  
[https://github.com/superfluid-finance/fluid/pull/7](https://github.com/superfluid-finance/fluid/pull/7)  

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/superfluid-finance/fluid/pull/7](https://github.com/superfluid-finance/fluid/pull/7)
PAGE END
