# \u0060LotteryMath.calculateNewProfit\u0060 returns wrong profit when there is no jackpot winner

**Severity:** high
**Auditor:** Code4rena
**Protocol:** Wenwin
**Keywords:** cybersecurity, vulnerability, LotteryMath, calculateNewProfit, jackpot winner, currentNetProfit, reward calculation, protocol functionality, expectedRewardsOut, payout calculation, multiplier, calculateMultiplier, calculateExcessPot, ticketsSold, expectedPayout, PercentageMath, mitigation, foundry, console log, smart contract

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/main/src/LotteryMath.sol#L50-L53
https://github.com/code-423n4/2023-03-wenwin/blob/main/src/Lottery.sol#L216-L223
https://github.com/code-423n4/2023-03-wenwin/blob/main/src/Lottery.sol#L238-L247


# Vulnerability details

## Impact
\u0060LotteryMath.calculateNewProfit\u0060 returns the wrong profit when there is no jackpot winner, and the library function is used when we update \u0060currentNetProfit\u0060 of \u0060Lottery\u0060 contract. 

\u0060\u0060\u0060solidity
        currentNetProfit = LotteryMath.calculateNewProfit(
            currentNetProfit,
            ticketsSold[drawFinalized],
            ticketPrice,
            jackpotWinners > 0,
            fixedReward(selectionSize),
            expectedPayout
        );
\u0060\u0060\u0060
\u0060Lottery.currentNetProfit\u0060 is used during reward calculation, so it can ruin the main functionality of this protocol.

\u0060\u0060\u0060solidity
    function drawRewardSize(uint128 drawId, uint8 winTier) private view returns (uint256 rewardSize) {
        return LotteryMath.calculateReward(
            currentNetProfit,
            fixedReward(winTier), 
            fixedReward(selectionSize),
            ticketsSold[drawId],
            winTier == selectionSize,
            expectedPayout
        );
    }
\u0060\u0060\u0060

## Proof of Concept

In \u0060LotteryMath.calculateNewProfit\u0060, \u0060expectedRewardsOut\u0060 is calculated as follows:

\u0060\u0060\u0060solidity
        uint256 expectedRewardsOut = jackpotWon
            ? calculateReward(oldProfit, fixedJackpotSize, fixedJackpotSize, ticketsSold, true, expectedPayout)
            : calculateMultiplier(calculateExcessPot(oldProfit, fixedJackpotSize), ticketsSold, expectedPayout)
                * ticketsSold * expectedPayout;
\u0060\u0060\u0060
The calculation is not correct when there is no jackpot winner. When \u0060jackpotWon\u0060 is false, \u0060ticketsSold * expectedPayout\u0060 is the total payout in reward token, and then we need to apply a multiplier to the total payout, and the multiplier is \u0060calculateMultiplier(calculateExcessPot(oldProfit, fixedJackpotSize), ticketsSold, expectedPayout)\u0060.

The calculation result is \u0060expectedRewardsOut\u0060, and it is also in reward token, so we should use \u0060PercentageMath\u0060 instead of multiplying directly.

For coded PoC, I added this function in \u0060LotteryMath.sol\u0060 and imported \u0060forge-std/console.sol\u0060 for console log.
\u0060\u0060\u0060solidity
    function testCalculateNewProfit() public {
        int256 oldProfit = 0;
        uint256 ticketsSold = 1;
        uint256 ticketPrice = 5 ether;
        uint256 fixedJackpotSize = 1_000_000e18; // don\u0027t affect the profit when oldProfit is 0, use arbitrary value
        uint256 expectedPayout = 38e16;
        int256 newProfit = LotteryMath.calculateNewProfit(oldProfit, ticketsSold, ticketPrice, false, fixedJackpotSize, expectedPayout );

        uint256 TICKET_PRICE_TO_POT = 70_000;
        uint256 ticketsSalesToPot = PercentageMath.getPercentage(ticketsSold * ticketPrice, TICKET_PRICE_TO_POT);
        int256 expectedProfit = oldProfit + int256(ticketsSalesToPot);
        uint256 expectedRewardsOut = ticketsSold * expectedPayout; // full percent because oldProfit is 0
        expectedProfit -= int256(expectedRewardsOut);
        
        console.log("Calculated value (Decimal 15):");
        console.logInt(newProfit / 1e15); // use decimal 15 for output purpose

        console.log("Expected value (Decimal 15):");
        console.logInt(expectedProfit / 1e15);
    }
\u0060\u0060\u0060

The result is as follows:
\u0060\u0060\u0060
  Calculated value (Decimal 15):
  -37996500
  Expected value (Decimal 15):
  3120
\u0060\u0060\u0060

## Tools Used
Foundry

## Recommended Mitigation Steps

Use \u0060PercentageMath\u0060 instead of multiplying directly.

\u0060\u0060\u0060solidity
        uint256 expectedRewardsOut = jackpotWon
            ? calculateReward(oldProfit, fixedJackpotSize, fixedJackpotSize, ticketsSold, true, expectedPayout)
            : (ticketsSold * expectedPayout).getPercentage(
                calculateMultiplier(calculateExcessPot(oldProfit, fixedJackpotSize), ticketsSold, expectedPayout)
            )
\u0060\u0060\u0060          


