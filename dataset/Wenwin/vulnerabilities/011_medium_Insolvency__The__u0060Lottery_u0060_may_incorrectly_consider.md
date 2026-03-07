# Insolvency: The \u0060Lottery\u0060 may incorrectly consider a year old jackpot ticket as unclaimed and increase \u0060currentNetProfit\u0060 by its prize while it was actually claimed

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wenwin
**Keywords:** cybersecurity, vulnerability, smart contract, blockchain, lottery, unclaimed jackpot, prize pot, timestamp, claiming tickets, edge case, insolvency, manual code review, mitigation, claimable amount, draw cooldown period, prize money, transaction, Eve, winning tickets, contract exploit

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/main/src/Lottery.sol#L135-L137
https://github.com/code-423n4/2023-03-wenwin/blob/main/src/Lottery.sol#L164-L166


# Vulnerability details

## Impact
According to the [documentation](https://docs.wenwin.com/wenwin-lottery/the-game):
> "Winning tickets have up to 1 year to claim their prize. If a prize is not claimed before this period, the unclaimed prize money will go back to the Prize Pot."

As part of this mechanism, the \u0060Lottery.executeDraw()\u0060 function (which internally calls \u0060Lottery.returnUnclaimedJackpotToThePot()\u0060) increases \u0060Lottery.currentNetProfit\u0060 by the prize of any 1 year old unclaimed jackpot ticket. At this point, the contract thinks it still hold that prize and it\u0027s going to include it in the prize pot of the next draw. This function can only be called when \u0060block.timestamp >= drawScheduledAt(currentDraw)\u0060.

On the other side, the \u0060Lottery.claimWinningTickets()\u0060 function (which internally calls \u0060Lottery.claimWinningTicket()\u0060 and \u0060Lottery.claimable()\u0060) sends the prize to the owner of a jackpot ticket only if it isn\u0027t 1 year old (if \u0060block.timestamp <= ticketRegistrationDeadline(ticketInfo.drawId + LotteryMath.DRAWS_PER_YEAR)\u0060).

However, if \u0060Lottery.drawCoolDownPeriod\u0060 is zero, both of these condition can pass on the same time - when the \u0060block.timestamp\u0060 is exactly the scheduled draw date of the draw that takes place exactly 1 year after the draw in which the jackpot ticket has won.

In this edge case, the owner of the jackpot ticket can call \u0060Lottery.executeDraw()\u0060, letting the \u0060Lottery\u0060 think the prize wasn\u0027t claimed, followed by \u0060Lottery.claimWinningTickets()\u0060, claiming the prize, all in the same transaction.

## Proof of Concept
Let\u0027s say Eve buys a ticket to draw #1 in a \u0060Lottery\u0060 contract where \u0060Lottery.drawCoolDownPeriod\u0060 equals zero, and win the jackpot. Now, Eve can wait 1 year and then, when \u0060block.timestamp\u0060 equals the scheduled draw date of draw #53 (which is also the registration deadline of draw #53), run a transaction that will do the following:
\u0060\u0060\u0060
lottery.executeDraw()
lottery.claimWinningTickets([eveJackpotTicketId])
\u0060\u0060\u0060
This will send Eve her prize, but will also leave the contract insolvent.

## Tools Used
Manual code review.

## Recommended Mitigation Steps
Fix \u0060Lottery.claimable()\u0060 to set \u0060claimableAmount\u0060 to \u0060winAmount[ticketInfo.drawId][winTier]\u0060 only if \u0060block.timestamp < ticketRegistrationDeadline(ticketInfo.drawId + LotteryMath.DRAWS_PER_YEAR)\u0060 (strictly less than).
