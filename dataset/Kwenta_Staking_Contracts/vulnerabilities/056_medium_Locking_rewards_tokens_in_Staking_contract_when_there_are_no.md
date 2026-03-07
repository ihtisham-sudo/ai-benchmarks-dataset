# Locking rewards tokens in Staking contract when there are no stakes

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Kwenta Staking Contracts
**Keywords:** cybersecurity, vulnerability, staking contract, lottery tickets, blocked rewards, staked tokens, total supply, locked tokens, claimRewards, rewardPerToken, lastUpdateTicketId, manual review, mitigation steps, withdrawal method, funds flow, contract security, token distribution, proof of concept, reward blocking, smart contract

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/Lottery.sol#L151
https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/staking/Staking.sol#L48


# Vulnerability details

## Impact
Blocking rewards assigned to stakes from the sale of lottery tickets when stakes are absent in the \u0060Staking\u0060 contract

*So, the situation is unlikely, but it can happen* 

## Proof of Concept
In order to confirm the problem, we need to prove 2 things: 
1. That there may be no staked tokens -> #Total supply == 0
2. That the reward that will be transferred to the contract will be blocked -> #Locked tokens

### Total supply == 0:
Flow 1:
   1. Deploy protocol
   2. Anyone buy tickets
   3. Anyone call [claimRewards()](https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/Lottery.sol#L151) for \u0060LotteryRewardType.STAKING\u0060
   4. Since no one has managed to stake the tokens yet, the reward for the first sold tickets will be transferred to the staking contract and blocked
   5. First user stake tokens and we can see then Staking contract have rewards but for first user \u0060rewardPerToken\u0060 will start from \u00600\u0060 and  \u0060lastUpdateTicketId\u0060 will update to actually
\u0060\u0060\u0060solidity
src/staking/Staking.sol

50: if (_totalSupply == 0) { // totalSupply == 0
51:     return rewardPerTokenStored;

120: rewardPerTokenStored = currentRewardPerToken; // will set 0
121: lastUpdateTicketId = lottery.nextTicketId(); // set actually
\u0060\u0060\u0060
   6. Tokens before the first stake will be blocked forever

Flow 2:
1. Everything is going well. The first bets are made before the sale of the first tokens
2. But there will moments when all the stakers withdraw their bets
3. get time periods when \u0060totalSupply == 0\u0060
4. During these periods, all the reward that will come will be blocked on the contract by analogy with the first flow

### Locked tokens
* Tokens are blocked because \u0060rewardPerTokenStored\u0060 is not updated when \u0060totalSupply == 0\u0060 

Let\u0027s just write a test
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "./LotteryTestBase.sol";
import "../src/Lottery.sol";
import "./TestToken.sol";
import "forge-std/console2.sol";
import "../src/interfaces/ILottery.sol";

contract StakingTest is LotteryTestBase {
    IStaking public staking;
    address public constant STAKER = address(69);

    ILotteryToken public stakingToken;

    function setUp() public override {
        super.setUp();
        staking = IStaking(lottery.stakingRewardRecipient());
        stakingToken = ILotteryToken(address(lottery.nativeToken()));
    }

    function testDelayFirstStake() public {
        console.log(
            "Init state totalSupply: %d, rewards: %d, rewardPerTokenStored: %d",
            staking.totalSupply(),
            rewardToken.balanceOf(address(staking)),
            staking.rewardPerTokenStored()
        );
        buySameTickets(lottery.currentDraw(), uint120(0x0F), address(0), 4);
        lottery.claimRewards(LotteryRewardType.STAKING);
        console.log(
            "After buy tickets totalSupply: %d, rewards: %d, rewardPerTokenStored: %d",
            staking.totalSupply(),
            rewardToken.balanceOf(address(staking)),
            staking.rewardPerTokenStored()
        );
        vm.prank(address(lottery));
        stakingToken.mint(STAKER, 1e18);
        vm.startPrank(STAKER);
        stakingToken.approve(address(staking), 1e18);
        staking.stake(1e18);
        console.log(
            "After user stake, totalSupply: %d, rewards: %d, rewardPerTokenStored: %d",
            staking.totalSupply(),
            rewardToken.balanceOf(address(staking)),
            staking.rewardPerTokenStored()
        );
        // buy one ticket and get rewards
        buySameTickets(lottery.currentDraw(), uint120(0x0F), address(0), 1);
        lottery.claimRewards(LotteryRewardType.STAKING);
        console.log(
            "After buy tickets, totalSupply: %d, rewards: %d, rewardPerTokenStored: %d",
            staking.totalSupply(),
            rewardToken.balanceOf(address(staking)),
            staking.rewardPerTokenStored()
        );
        staking.exit();
        console.log(
            "After user exit, totalSupply: %d, rewards: %d, rewardPerTokenStored: %d",
            staking.totalSupply(),
            rewardToken.balanceOf(address(staking)),
            staking.rewardPerTokenStored()
        );
        buySameTickets(lottery.currentDraw(), uint120(0x0F), address(0), 1);
        lottery.claimRewards(LotteryRewardType.STAKING);
        console.log(
            "After buy ticket again, totalSupply: %d, rewards: %d, rewardPerTokenStored: %d",
            staking.totalSupply(),
            rewardToken.balanceOf(address(staking)),
            staking.rewardPerTokenStored()
        );
    }
}

\u0060\u0060\u0060
Result:
\u0060\u0060\u0060text
Logs:
  Init state totalSupply: 0, rewards: 0, rewardPerTokenStored: 0
  After buy tickets totalSupply: 0, rewards: 4000000000000000000, rewardPerTokenStored: 0
  After user stake, totalSupply: 1000000000000000000, rewards: 4000000000000000000, rewardPerTokenStored: 0
  After buy tickets, totalSupply: 1000000000000000000, rewards: 5000000000000000000, rewardPerTokenStored: 0
  After user exit, totalSupply: 0, rewards: 4000000000000000000, rewardPerTokenStored: 1000000000000000000
  After buy ticket again, totalSupply: 0, rewards: 5000000000000000000, rewardPerTokenStored: 1000000000000000000
\u0060\u0060\u0060
## Tools Used
* Manual review

## Recommended Mitigation Steps
One of:
1. Develop a flow where funds should go in case of lack of stakers
2. Develop a method of withdrawing blocked coins (which will not be distributed among stakers)
