# Unsafe casting from \u0060uint256\u0060 to \u0060uint16\u0060 could cause ticket prizes to become much smaller than intended

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wenwin
**Keywords:** cybersecurity, vulnerability, LotterySetup.sol, packFixedRewards, uint256, uint16, bitwise arithmetic, rewards, winTier, divisor, unsafe cast, upper limit, documentation, non-jackpot, prize amount, tokenDecimals, mapping, OpenZeppelin, SafeCast, smart contract

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/main/src/LotterySetup.sol#L164-L176


# Vulnerability details

## Vulnerability Details

In \u0060LotterySetup.sol\u0060, the \u0060packFixedRewards()\u0060 function packs a \u0060uint256\u0060 array into a \u0060uint256\u0060 through bitwise arithmetic:

[\u0060LotterySetup.sol#L164-L176\u0060](https://github.com/code-423n4/2023-03-wenwin/blob/main/src/LotterySetup.sol#L164-L176):
\u0060\u0060\u0060solidity
function packFixedRewards(uint256[] memory rewards) private view returns (uint256 packed) {
    if (rewards.length != (selectionSize) || rewards[0] != 0) {
        revert InvalidFixedRewardSetup();
    }
    uint256 divisor = 10 ** (IERC20Metadata(address(rewardToken)).decimals() - 1);
    for (uint8 winTier = 1; winTier < selectionSize; ++winTier) {
        uint16 reward = uint16(rewards[winTier] / divisor);
        if ((rewards[winTier] % divisor) != 0) {
            revert InvalidFixedRewardSetup();
        }
        packed |= uint256(reward) << (winTier * 16);
    }
}
\u0060\u0060\u0060

The \u0060rewards[]\u0060 parameter stores the prize amount per each \u0060winTier\u0060, where \u0060winTier\u0060 is the number of matching numbers a ticket has. \u0060packFixedRewards()\u0060 is used when the lottery is first initialized to store the prize for each non-jackpot \u0060winTier\u0060.

The vulnerability lies in the following line:

\u0060\u0060\u0060solidity
uint16 reward = uint16(rewards[winTier] / divisor);
\u0060\u0060\u0060

It casts \u0060rewards[winTier] / divisor\u0060, which is a \u0060uint256\u0060, to a \u0060uint16\u0060. If \u0060rewards[winTier] / divisor\u0060 is larger than \u00602 ** 16 - 1\u0060, the unsafe cast will only keep its rightmost bits, causing the result to be much smaller than defined in \u0060rewards[]\u0060. 

As \u0060divisor\u0060 is defined as \u006010 ** (tokenDecimals - 1)\u0060, the upperbound of \u0060rewards[winTier]\u0060 evaluates to \u00606553.5 * 10 ** tokenDecimals\u0060. This means that the prize of any \u0060winTier\u0060 must not be larger than 6553.5 tokens, otherwise the unsafe cast causes it to become smaller than expected.

## Impact

If a deployer is unaware of this upper limit, he could deploy the lottery with ticket prizes larger than 6553.5 tokens, causing non-jackpot ticket prizes to become significantly smaller. The likelihood of this occuring is increased as:

1. The upper limit is not mentioned anywhere in the documentation.
2. The upper limit is not immediately obvious when looking at the code.
   
This upper limit also restricts the protocol from using low price tokens. For example, if the protocol uses SHIB ($0.00001087 per token), the highest possible prize with 6553.5 tokens is worth only $0.071236545.

## Proof of Concept

If the lottery is initialized with \u0060rewards = [0, 6500, 7000]\u0060, the prize for each \u0060winTier\u0060 would become the following:

| \u0060winTier\u0060 | Token Amount (in tokenDecimals) |
| --------- | ------------------------------- |
| 0         | 0                               |
| 1         | 6500                            |
| 2         | 446                             |


The prize for \u0060winTier = 2\u0060 can be derived as such:

\u0060\u0060\u0060
(tokenAmount * 10) & type(uint16).max = (7000 * 10) & (2 ** 16 - 1) = 4464
4464 / 10 = 446
\u0060\u0060\u0060

The following test demonstrates the above:

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../src/LotterySetup.sol";
import "./TestToken.sol";

contract RewardUnsafeCastTest is Test {
    ERC20 public rewardToken;

    uint8 public constant SELECTION_SIZE = 3;
    uint8 public constant SELECTION_MAX = 10;

    function setUp() public {
        rewardToken = new TestToken();
    }

    function testRewardIsSmallerThanExpected() public {
        // Get 1 token unit
        uint256 tokenUnit = 10 ** rewardToken.decimals();

        // Define fixedRewards as [0, 6500, 7000]
        uint256[] memory fixedRewards = new uint256[](SELECTION_SIZE);
        fixedRewards[1] = 6500 * tokenUnit;
        fixedRewards[2] = 7000 * tokenUnit;

        // Initialize LotterySetup contract
        LotterySetup lotterySetup = new LotterySetup(
            LotterySetupParams(
                rewardToken,
                LotteryDrawSchedule(block.timestamp + 2*100, 100, 60),
                5 ether,
                SELECTION_SIZE,
                SELECTION_MAX,
                38e16,
                fixedRewards
            )
        );

        // Reward for winTier 1 is 6500
        assertEq(lotterySetup.fixedReward(1) / tokenUnit, 6500);

        // Reward for winTier 2 is 446 instead of 7000
        assertEq(lotterySetup.fixedReward(2) / tokenUnit, 446);
    }
}
\u0060\u0060\u0060

## Recommended Mitigation

Consider storing the prize amount of each \u0060winTier\u0060 in a mapping instead of packing them into a \u0060uint256\u0060 using bitwise arithmetic. This approach removes the upper limit (6553.5) and lower limit (0.1) for prizes, which would allow the protocol to use tokens with extremely high or low prices.

Alternatively, check if \u0060rewards[winTier] > type(uint256).max\u0060 and revert if so. This can be done through OpenZeppelin\u0027s [SafeCast](https://docs.openzeppelin.com/contracts/3.x/api/utils#SafeCast-toUint16-uint256-).
