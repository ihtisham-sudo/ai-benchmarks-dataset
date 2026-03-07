# M-1 - An attacker may DoS user Fluid

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** SuperFluid Finance 
**Keywords:** DoS, FluidLocker, claim, EP_PROGRAM_MANAGER, batchUpdateUserUnits, frontrunning, signature, nonce, user balance, stake, tax distribution, smart contract, Ethereum, attack vector, user experience, contract vulnerability, fluid balance, program points, tax, funds

---

# Issue H-2: FluidLocker::_getUnlockingPercentage() uses 540 instead of 540 days leading to stuck funds as the unlocking percentage will be bigger than 100% and underflow

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-superfluid-locking-contract-judging/issues/21)  
Found by: 0x73696d616f, Drynooo, merlinboii, zxriptor

FluidLocker::_getUnlockingPercentage() calculates the amount to unlock when unvesting via the FluidLocker. It incorrectly uses 540 instead of 540 days, yielding a massive error such that the unlocking percentage will be much bigger than 10,000 and underflow.

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

Note: due to other bugs in the calculation it will not revert.

In FluidLocker:388 it uses 540 instead of 540 days.
None.

None.

1. User unlocks their Fluid from the FluidLocker, but it reverts because of the mentioned underflow. The funds within the locker will be stuck unless the user instantly unlocks and takes an 80% penalty.

User is forced to take an 80% penalty or have the funds stuck.

The calculation is presented in the summary. Essentially, as 540 is used in the denominator, much smaller than the correct 540 days (which is the maximum unlock period, when the percentage becomes 100%), the value will be much bigger than 10,000. As the unlocking percentage is bigger than 10,000, the unlock flow rate 

\u0060\u0060\u0060solidity
unlockFlowRate = (globalFlowRate *
  int256(_getUnlockingPercentage(unlockPeriod))).toInt96()
  / int256(_BP_DENOMINATOR).toInt96();
\u0060\u0060\u0060

will be bigger than the global flow rate, so it reverts when calculating the tax flow rate 

\u0060\u0060\u0060solidity
taxFlowRate = globalFlowRate - unlockFlowRate;
\u0060\u0060\u0060

Use 540 days instead of 540.

0xPilou  
Fix for this issue is included in the following PR:  
https://github.com/superfluid-finance/fluid/pull/6  
sherlock-admin2

https://github.com/superfluid-finance/fluid/pull/6
## Issue H-3: Fontaine never stops the flows

tothetaxandrecipient,sothebuffercom-
ponentoftheflowswillbelost  
Source: https://github.com/sherlock-audit/2024-11-superfluid-locking-contract-judging/issues/36  
Foundby  
0x73696d616f  

Superfluid flows reserve 4 hours of the stream flow rate as a buffer for liquidations, and returns this when the flow is closed. However, Fontaine::initialize() never actually stops the flows, which means the deposit buffer will never be reclaimed, taking the recipient and the tax pool the loss.  

In Fontaine::initialize(), the flows are never stopped, which means the buffer will not be returned.  

None.  

None.  

1. User unlocks their Fluid from the Locker by calling FluidLocker::unlock() with a nonnull unlocking period.
## Impact
The recipient and the tax distribution pool take the loss as they do not receive all their funds (the deposit buffer is never sent to them).
## PoC
Add the following logs to \u0060Fontaine.sol\u0060 and run for getest -- mttestVestUnlock - vvvv. Alice sends \u006010_000e18\u0060 to the fontaine, but only \u00609996.8e18\u0060 are left in the fontaine as a part of the mare reserved for the buffer which will never be collected back.

\u0060\u0060\u0060solidity
function initialize(address unlockRecipient, int96 unlockFlowRate, int96 taxFlowRate) external initializer {
    // Ensure recipient is not a SuperApp
    if (ISuperfluid(FLUID.getHost()).isApp(ISuperApp(unlockRecipient))) revert CANNOT_UNLOCK_TO_SUPERAPP();
    console2.log("fontaine balance pre distributeFlow", FLUID.balanceOf(address(this)));
    // Distribute Tax flow to Staker GDA Pool
    FLUID.distributeFlow(address(this), TAX_DISTRIBUTION_POOL, taxFlowRate);
    console2.log("fontaine balance pre createFlow", FLUID.balanceOf(address(this)));
    // Create the unlocking flow from the Fontaine to the locker owner
    FLUID.createFlow(unlockRecipient, unlockFlowRate);
    console2.log("fontaine balance after createFlow", FLUID.balanceOf(address(this)));
}
\u0060\u0060\u0060
## Mitigation
Add a way to stop the flow and receive the deposit back.
## Discussion
0xPilou  
Fix for this issue is included in the following PR:  
[https://github.com/superfluid-finance/fluid/pull/8](https://github.com/superfluid-finance/fluid/pull/8)  

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/superfluid-finance/fluid/pull/8](https://github.com/superfluid-finance/fluid/pull/8)
## Issue M-1: An attacker may DoS user Fluid

An attacker may DoS user Fluid balance increases by frontrunning Fluid Locker::claim() calls and calling EP_PROGRAM_MANAGER::batchUpdateUserUnits() directly.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-superfluid-locking-contract-judging/issues/19)

Found by: 0x73696d616f


FluidLocker::claim() connects to the fluid pool and then calls EPProgramManager::batchUpdateUserUnits() to verify the signature and update user points. However, any attacker may frontrun this call and call directly EPProgramManager::batchUpdateUserUnits(), spending the signature (nonce) and making the claim transaction revert.

As the Fluid balances only increase whenever the user connects to the pool, the user balance will be 0. An attacker will profit from this because a large tax amount may be coming from a user instantly unlocking or a program being stopped, which transfers immediately funds to the stakers by calling \u0060FLUID.distributeToPool(address(this), TAX_DISTRIBUTION_POOL, amount);\u0060.

As the user wanted to stake, they needed Fluid balance to do so, but as the attacker DoSed their claim transaction, they will not have balance to stake and will completely miss these large instant funds. Even if users had already staked before, this claim transaction could be increasing their points (by increasing their program points, they could get more Fluid and stake more Fluid to get more staker points), so an attacker profits from not allowing the user to do so just before the tax is distributed.

Note 1: The tax is distributed pro-rata to the units of each user, so if the attacker denies a user increasing their funds, the attacker will receive a larger share of the funds.
EP_PROGRAM_MANAGER::updateUserUnits() may be called directly allowing attackers to DoS FluidLocker::claim().

None.

None.

1. Attacker spots that a user is unlocking or a program is coming to an end and a large sum of tax is coming.
2. Attacker frontruns users that are going to increase their Fluid balance in the Locker by calling FluidLocker::claim() so that the Locker connects to the program pool and receives the corresponding Fluid tokens.
3. Due to the FluidLocker::claim() call reverting, users will have less Fluid in the Locker and will stake less funds, getting less points, which means the attacker will get a bigger share of the incoming TAX distribution.

Attacker profits from having a bigger share of the TAX distributions and users lose this share.

The only way to collect the Locker to the program pool is by calling FluidLocker::claim() which may be DoSed by calling EP_PROGRAM_MANAGER.updateUserUnits() directly using the same signature.

\u0060\u0060\u0060solidity
function claim(uint256 programId, uint256 totalProgramUnits, uint256 nonce, bytes memory stackSignature)
    external
    nonReentrant
{
    // Get the corresponding program pool
    ISuperfluidPool programPool = EP_PROGRAM_MANAGER.getProgramPool(programId);
}
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
if (!FLUID.isMemberConnected(address(programPool), address(this))) {
    // Connect this locker to the Program Pool
    FLUID.connectPool(programPool);
}
// Request program manager to update this locker\u0027s units
EP_PROGRAM_MANAGER.updateUserUnits(lockerOwner, programId, totalProgramUnits,
    nonce, stackSignature);
emit IFluidLocker.FluidStreamClaimed(programId, totalProgramUnits);
\u0060\u0060\u0060

The locker should have a separate method to connect to the pool.

0xPilou  
Fix for this issue is included in the following PR:  
https://github.com/superfluid-finance/fluid/pull/9  

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/superfluid-finance/fluid/pull/9
