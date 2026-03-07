# CL001 - User cannot withdraw stakingToken due to incorrect calculation of _totalSupply

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cybersecurity, vulnerability, stakingToken, withdrawal, totalSupply, VestingSchedule, amountToVest, daysToCliff, daysToVest, amountWithdrawable, revoke, manual review, impact, code snippet, smart contract, blockchain, decentralized finance, userA, userB, revert

---

CL001

high

# User cannot withdraw stakingToken due to incorrect calculation of _totalSupply

## Summary
User cannot withdraw \u0060stakingToken\u0060 due to incorrect calculation of \u0060_totalSupply\u0060

## Vulnerability Detail
Given:

1.userA VestingSchedule\u0060 amountToVest\u0060= 20 ether ,\u0060daysToCliff\u0060=30 , \u0060daysToVest\u0060=120

2.userB VestingSchedule \u0060amountToVest\u0060= 30 ether , \u0060daysToCliff\u0060=30, \u0060daysToVest\u0060=120
_totalSupply =20 +30= 50

3.skip 60 days  userB withdraw (\u0060amountWithdrawable =15\u0060)
_totalSupply = 50-15=35

4.\u0060revoke\u0060 userB \u0060VestingSchedule\u0060 
_totalSupply = 35-30=5
https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeRewardsVesting.sol#L451

5.skip 60 days (120 days later)
userA withdraw \u0060(amountWithdrawable =20\u0060)
_totalSupply = 5-20 lead to revert
https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeRewardsVesting.sol#L508


POC:
src/TESTS_Core/Test_ZivoeRewardsVesting.sol
\u0060\u0060\u0060solidity

    function testpoc() public{
        assert(zvl.try_createVestingSchedule(
            address(vestZVE), 
            address(qcp), 
            30, 
            120,
            20 ether, 
            true
        ));
        assert(zvl.try_createVestingSchedule(
            address(vestZVE), 
            address(pam), 
            30, 
            120,
            30 ether, 
            true
        ));


        hevm.warp(block.timestamp + 60 days);

        vestZVE.amountWithdrawable(address(pam));
        //pam withdraw
         hevm.startPrank(address(pam));
        vestZVE.withdraw();
        hevm.stopPrank();
        vestZVE.totalSupply();

        //revokeVesting
        hevm.startPrank(address(zvl));
        vestZVE.revokeVestingSchedule(address(pam));
        hevm.stopPrank();
        vestZVE.totalSupply();

        //qcp withdraw
        hevm.warp(block.timestamp + 60 days);
        vestZVE.amountWithdrawable(address(qcp));
         hevm.startPrank(address(qcp));
        vestZVE.withdraw();
        hevm.stopPrank(); 
    }
[FAIL. Reason: panic: arithmetic underflow or overflow (0x11)] testpoc() (gas: 795816)
\u0060\u0060\u0060

## Impact
User cannot withdraw stakingToken

## Code Snippet
https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeRewardsVesting.sol#L451
## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060solidity
   function revokeVestingSchedule(address account) external updateReward(account) onlyZVLOrITO nonReentrant {
        require(
            vestingScheduleSet[account], 
            "ZivoeRewardsVesting::revokeVestingSchedule() !vestingScheduleSet[account]"
        );
        require(
            vestingScheduleOf[account].revokable, 
            "ZivoeRewardsVesting::revokeVestingSchedule() !vestingScheduleOf[account].revokable"
        );
        
        uint256 amount = amountWithdrawable(account);
        uint256 vestingAmount = vestingScheduleOf[account].totalVesting;

        vestingTokenAllocated -= amount;

        vestingScheduleOf[account].totalWithdrawn += amount;
        vestingScheduleOf[account].totalVesting = vestingScheduleOf[account].totalWithdrawn;
        vestingScheduleOf[account].cliff = block.timestamp - 1;
        vestingScheduleOf[account].end = block.timestamp;

        vestingTokenAllocated -= (vestingAmount - vestingScheduleOf[account].totalWithdrawn);

     -  _totalSupply = _totalSupply.sub(vestingAmount);
     + _totalSupply = _totalSupply.sub(amount);
\u0060\u0060\u0060

