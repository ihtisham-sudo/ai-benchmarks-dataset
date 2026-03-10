# Callpaths — Wenwin

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## API3DaoRNSource

_File: src/rnsources/API3DaoRNSource.sol_

### external fulfillUint256
-> internal fulfill


### external requestRandomNumber
-> internal requestRandomnessFromUnderlyingSource


---

## GelatoRNSource

_File: src/rnsources/GelatoRNSource.sol_

### external fulfillRandomness
-> internal _operator
-> internal _fulfillRandomness
  -> internal fulfill


### external requestRandomNumber
-> internal requestRandomnessFromUnderlyingSource
  -> internal _requestRandomness
    -> private _round


---

## GelatoVRFConsumerBase

_File: src/rnsources/external/GelatoVRFConsumerBase.sol_

### external fulfillRandomness
_(no internal calls)_


---

## Lottery

_File: src/Lottery.sol_

### public buyTickets
-> internal buyTicketsAsDelegate
  -> private registerTicket
    -> internal mint


### external changeFeeRecipient
-> public claimFees
  -> library LotteryMath.calculateFees
  -> private dueTicketsSoldAndReset


### public claimFees
-> library LotteryMath.calculateFees
-> private dueTicketsSoldAndReset


### public claimFrontendFees
-> library LotteryMath.calculateFees
-> private dueTicketsSoldAndReset


### public claimWinningTickets
-> internal claimWinningTicketsAsDelegate
  -> private claimWinningTicket


### external claimable
-> library TicketUtils.ticketWinTier
-> public ticketRegistrationDeadline
  -> public drawScheduledAt
    -> private unpackDrawPeriod


### public currentRewardSize
-> private drawRewardSize
  -> library LotteryMath.calculateReward
  -> public fixedReward
    -> internal _baseJackpot


### public drawScheduledAt
-> private unpackDrawPeriod


### external executeDraw
-> public drawScheduledAt
  -> private unpackDrawPeriod
-> private returnUnclaimedJackpotToThePot
-> internal requestRandomNumber
  -> private requestRandomNumberFromSource


### external feeToken
_(no internal calls)_


### public fixedReward
-> internal _baseJackpot


### external initSource
_(no internal calls)_


### external onRandomNumberFulfilled
-> internal receiveRandomNumber
  -> library TicketUtils.reconstructTicket
  -> private drawRewardSize
    -> library LotteryMath.calculateReward
    -> public fixedReward
      -> internal _baseJackpot
  -> library LotteryMath.calculateNewProfit
  -> public fixedReward
    -> internal _baseJackpot


### external rescueTokens
_(no internal calls)_


### external retry
-> private requestRandomNumberFromSource


### external setBaseURI
_(no internal calls)_


### external swapSource
-> private requestRandomNumberFromSource


### public ticketRegistrationDeadline
-> public drawScheduledAt
  -> private unpackDrawPeriod


### external unclaimedFees
-> library LotteryMath.calculateFees


### external unclaimedFrontendFees
-> library LotteryMath.calculateFees


---

## LotteryNativeToken

_File: src/LotteryNativeToken.sol_

### public buyTickets
-> internal buyTicketsAsDelegate
  -> private registerTicket


### external buyTicketsWithNativeToken
-> internal buyTicketsAsDelegate
  -> private registerTicket


### external changeFeeRecipient
-> public claimFees
  -> library LotteryMath.calculateFees
  -> private dueTicketsSoldAndReset


### public claimFees
-> library LotteryMath.calculateFees
-> private dueTicketsSoldAndReset


### public claimFrontendFees
-> library LotteryMath.calculateFees
-> private dueTicketsSoldAndReset


### public claimWinningTickets
-> internal claimWinningTicketsAsDelegate
  -> private claimWinningTicket


### external claimWinningTicketsInNativeToken
-> internal claimWinningTicketsAsDelegate
  -> private claimWinningTicket


### external claimable
-> library TicketUtils.ticketWinTier


### public currentRewardSize
-> private drawRewardSize
  -> library LotteryMath.calculateReward


### external executeDraw
-> private returnUnclaimedJackpotToThePot


### external feeToken
_(no internal calls)_


### external rescueTokens
_(no internal calls)_


### external unclaimedFees
-> library LotteryMath.calculateFees


### external unclaimedFrontendFees
-> library LotteryMath.calculateFees


---

## LotterySetup

_File: src/LotterySetup.sol_

### public drawScheduledAt
-> private unpackDrawPeriod


### public fixedReward
-> internal _baseJackpot


### public ticketRegistrationDeadline
-> public drawScheduledAt
  -> private unpackDrawPeriod


---

## LotteryToken

_File: src/LotteryToken.sol_

### external burn
_(no internal calls)_


### external mint
_(no internal calls)_


---

## RNSourceBase

_File: src/rnsources/RNSourceBase.sol_

### external requestRandomNumber
_(no internal calls)_


---

## RNSourceController

_File: src/RNSourceController.sol_

### external initSource
_(no internal calls)_


### external onRandomNumberFulfilled
_(no internal calls)_


### external retry
-> private requestRandomNumberFromSource


### external swapSource
-> private requestRandomNumberFromSource


---

## StakedTokenLock

_File: src/staking/StakedTokenLock.sol_

### external deposit
_(no internal calls)_


### external getReward
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## Staking

_File: src/staking/Staking.sol_

### public earned
-> public rewardPerToken
  -> library LotteryMath.calculateFees


### external exit
-> public withdraw
-> public getReward
  -> internal _updateReward
    -> public rewardPerToken
      -> library LotteryMath.calculateFees
    -> public earned
      -> public rewardPerToken
        -> library LotteryMath.calculateFees


### public getReward
-> internal _updateReward
  -> public rewardPerToken
    -> library LotteryMath.calculateFees
  -> public earned
    -> public rewardPerToken
      -> library LotteryMath.calculateFees


### public rewardPerToken
-> library LotteryMath.calculateFees


### external stake
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## SupraRNSource

_File: src/rnsources/SupraRNSource.sol_

### external fulfill
-> external fulfill


### external requestRandomNumber
-> internal requestRandomnessFromUnderlyingSource


---

## Ticket

_File: src/Ticket.sol_

### external setBaseURI
_(no internal calls)_


---

## VRFv2RNSource

_File: src/rnsources/VRFv2RNSource.sol_

### external requestRandomNumber
-> internal requestRandomnessFromUnderlyingSource

