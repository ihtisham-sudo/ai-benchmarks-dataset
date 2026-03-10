# Callpaths — PoolTogetherV4

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ControlledToken

_File: contracts/ControlledToken.sol_

### external controllerBurn
_(no internal calls)_


### external controllerBurnFrom
_(no internal calls)_


### external controllerMint
_(no internal calls)_


### public decimals
_(no internal calls)_


---

## DrawBeacon

_File: contracts/DrawBeacon.sol_

### external beaconPeriodEndAt
-> internal _beaconPeriodEndAt


### external beaconPeriodRemainingSeconds
-> internal _beaconPeriodRemainingSeconds
  -> internal _beaconPeriodEndAt
  -> internal _currentTime


### external calculateNextBeaconPeriodStartTime
-> internal _calculateNextBeaconPeriodStartTime


### external calculateNextBeaconPeriodStartTimeFromCurrentTime
-> internal _calculateNextBeaconPeriodStartTime
-> internal _currentTime


### external canCompleteDraw
-> public isRngRequested
-> public isRngCompleted


### external canStartDraw
-> internal _isBeaconPeriodOver
  -> internal _beaconPeriodEndAt
  -> internal _currentTime
-> public isRngRequested


### external cancelDraw
-> public isRngTimedOut
  -> internal _currentTime


### external completeDraw
-> internal _currentTime
-> external_callback IDrawBeacon.Draw
-> internal _calculateNextBeaconPeriodStartTime


### external getBeaconPeriodSeconds
_(no internal calls)_


### external getBeaconPeriodStartedAt
_(no internal calls)_


### external getDrawBuffer
_(no internal calls)_


### external getLastRngLockBlock
_(no internal calls)_


### external getLastRngRequestId
_(no internal calls)_


### external getNextDrawId
_(no internal calls)_


### external getRngService
_(no internal calls)_


### external getRngTimeout
_(no internal calls)_


### external isBeaconPeriodOver
-> internal _isBeaconPeriodOver
  -> internal _beaconPeriodEndAt
  -> internal _currentTime


### public isRngCompleted
_(no internal calls)_


### public isRngRequested
_(no internal calls)_


### public isRngTimedOut
-> internal _currentTime


### external setBeaconPeriodSeconds
-> internal _setBeaconPeriodSeconds


### external setDrawBuffer
-> internal _setDrawBuffer


### external setRngService
-> internal _setRngService


### external setRngTimeout
-> internal _setRngTimeout


### external startDraw
-> internal _currentTime


---

## DrawBuffer

_File: contracts/DrawBuffer.sol_

### external getBufferCardinality
_(no internal calls)_


### external getDraw
-> internal _drawIdToDrawIndex


### external getDrawCount
_(no internal calls)_


### external getDraws
-> internal _drawIdToDrawIndex


### external getNewestDraw
-> internal _getNewestDraw


### external getOldestDraw
_(no internal calls)_


### external pushDraw
-> internal _pushDraw


### external setDraw
_(no internal calls)_


---

## DrawCalculator

_File: contracts/DrawCalculator.sol_

### external calculate
-> internal _getNormalizedBalancesAt
-> internal _calculatePrizesAwardable
  -> internal _calculateNumberOfUserPicks
  -> internal _calculate
    -> internal _createBitMasks
    -> internal _calculateTierIndex
    -> internal _calculatePrizeTierFractions
      -> internal _calculatePrizeTierFraction
        -> internal _numberOfPrizesForIndex


### external getDrawBuffer
_(no internal calls)_


### external getNormalizedBalancesForDrawIds
-> internal _getNormalizedBalancesAt


### external getPrizeDistributionBuffer
_(no internal calls)_


---

## DrawCalculatorV2

_File: contracts/DrawCalculatorV2.sol_

### external calculate
-> internal _getNormalizedBalancesAt
-> internal _calculatePrizesAwardable
  -> internal _calculateNumberOfUserPicks
  -> internal _calculate
    -> internal _createBitMasks
    -> internal _calculateTierIndex
    -> internal _calculatePrizeTierFractions
      -> internal _calculatePrizeTierFraction
        -> internal _numberOfPrizesForIndex


### external getDrawBuffer
_(no internal calls)_


### external getNormalizedBalancesForDrawIds
-> internal _getNormalizedBalancesAt


### external getPrizeDistributionSource
_(no internal calls)_


---

## EIP2612PermitAndDeposit

_File: contracts/permit/EIP2612PermitAndDeposit.sol_

### external depositToAndDelegate
-> internal _depositToAndDelegate
  -> internal _depositTo


### external permitAndDepositToAndDelegate
-> internal _depositToAndDelegate
  -> internal _depositTo


---

## PrizeDistributionBuffer

_File: contracts/PrizeDistributionBuffer.sol_

### external getBufferCardinality
_(no internal calls)_


### external getNewestPrizeDistribution
_(no internal calls)_


### external getOldestPrizeDistribution
_(no internal calls)_


### external getPrizeDistribution
-> internal _getPrizeDistribution


### external getPrizeDistributionCount
_(no internal calls)_


### external getPrizeDistributions
-> internal _getPrizeDistribution


### external pushPrizeDistribution
-> internal _pushPrizeDistribution


### external setPrizeDistribution
_(no internal calls)_


---

## PrizeDistributor

_File: contracts/PrizeDistributor.sol_

### external claim
-> internal _getDrawPayoutBalanceOf
-> internal _setDrawPayoutBalanceOf
-> internal _awardPayout


### external getDrawCalculator
_(no internal calls)_


### external getDrawPayoutBalanceOf
-> internal _getDrawPayoutBalanceOf


### external getToken
_(no internal calls)_


### external setDrawCalculator
-> internal _setDrawCalculator


### external withdrawERC20
_(no internal calls)_


---

## PrizePool

_File: contracts/prize-pool/PrizePool.sol_

### external award
-> internal _mint


### external awardBalance
_(no internal calls)_


### external awardExternalERC20
-> internal _transferOut


### external awardExternalERC721
_(no internal calls)_


### external balance
_(no internal calls)_


### external canAwardExternal
_(no internal calls)_


### external captureAwardBalance
-> internal _ticketTotalSupply


### external compLikeDelegate
_(no internal calls)_


### external depositTo
-> internal _depositTo
  -> internal _canDeposit
  -> internal _mint


### external depositToAndDelegate
-> internal _depositTo
  -> internal _canDeposit
  -> internal _mint


### external getAccountedBalance
-> internal _ticketTotalSupply


### external getBalanceCap
_(no internal calls)_


### external getLiquidityCap
_(no internal calls)_


### external getPrizeStrategy
_(no internal calls)_


### external getTicket
_(no internal calls)_


### external getToken
_(no internal calls)_


### external isControlled
-> internal _isControlled


### external onERC721Received
_(no internal calls)_


### external setBalanceCap
-> internal _setBalanceCap


### external setLiquidityCap
-> internal _setLiquidityCap


### external setPrizeStrategy
-> internal _setPrizeStrategy


### external setTicket
-> internal _setBalanceCap


### external transferExternalERC20
-> internal _transferOut


### external withdrawFrom
_(no internal calls)_


---

## PrizeSplit

_File: contracts/prize-strategy/PrizeSplit.sol_

### external getPrizeSplit
_(no internal calls)_


### external getPrizeSplits
_(no internal calls)_


### external setPrizeSplit
-> internal _totalPrizeSplitPercentageAmount


### external setPrizeSplits
-> internal _totalPrizeSplitPercentageAmount


---

## PrizeSplitStrategy

_File: contracts/prize-strategy/PrizeSplitStrategy.sol_

### external distribute
-> internal _distributePrizeSplits
  -> internal _awardPrizeSplitAmount


### external getPrizePool
_(no internal calls)_


### external getPrizeSplit
_(no internal calls)_


### external getPrizeSplits
_(no internal calls)_


### external setPrizeSplit
-> internal _totalPrizeSplitPercentageAmount


### external setPrizeSplits
-> internal _totalPrizeSplitPercentageAmount


---

## Reserve

_File: contracts/Reserve.sol_

### external checkpoint
-> internal _checkpoint
  -> internal _getNewestObservation
    -> library RingBufferLib.newestIndex
  -> library ObservationLib.Observation
  -> library RingBufferLib.nextIndex


### external getReserveAccumulatedBetween
-> internal _getNewestObservation
  -> library RingBufferLib.newestIndex
-> internal _getOldestObservation
-> internal _getReserveAccumulatedAt
  -> library ObservationLib.binarySearch


### external getToken
_(no internal calls)_


### external withdrawTo
-> internal _checkpoint
  -> internal _getNewestObservation
    -> library RingBufferLib.newestIndex
  -> library ObservationLib.Observation
  -> library RingBufferLib.nextIndex


---

## StakePrizePool

_File: contracts/prize-pool/StakePrizePool.sol_

### external award
-> internal _mint


### external awardBalance
_(no internal calls)_


### external awardExternalERC20
-> internal _transferOut
  -> internal _canAwardExternal


### external awardExternalERC721
-> internal _canAwardExternal


### external balance
-> internal _balance


### external canAwardExternal
-> internal _canAwardExternal


### external captureAwardBalance
-> internal _ticketTotalSupply
-> internal _balance


### external compLikeDelegate
_(no internal calls)_


### external depositTo
-> internal _depositTo
  -> internal _canDeposit
  -> internal _token
  -> internal _mint
  -> internal _supply


### external depositToAndDelegate
-> internal _depositTo
  -> internal _canDeposit
  -> internal _token
  -> internal _mint
  -> internal _supply


### external getAccountedBalance
-> internal _ticketTotalSupply


### external getBalanceCap
_(no internal calls)_


### external getLiquidityCap
_(no internal calls)_


### external getPrizeStrategy
_(no internal calls)_


### external getTicket
_(no internal calls)_


### external getToken
-> internal _token


### external isControlled
-> internal _isControlled


### external onERC721Received
_(no internal calls)_


### external setBalanceCap
-> internal _setBalanceCap


### external setLiquidityCap
-> internal _setLiquidityCap


### external setPrizeStrategy
-> internal _setPrizeStrategy


### external setTicket
-> internal _setBalanceCap


### external transferExternalERC20
-> internal _transferOut
  -> internal _canAwardExternal


### external withdrawFrom
-> internal _redeem
-> internal _token


---

## Ticket

_File: contracts/Ticket.sol_

### external controllerBurn
_(no internal calls)_


### external controllerBurnFrom
_(no internal calls)_


### external controllerDelegateFor
-> internal _delegate
  -> internal _transferTwab
    -> internal _decreaseUserTwab
      -> library TwabLib.decreaseBalance
    -> internal _decreaseTotalSupplyTwab
      -> library TwabLib.decreaseBalance
    -> internal _increaseUserTwab
      -> library TwabLib.increaseBalance
    -> internal _increaseTotalSupplyTwab
      -> library TwabLib.increaseBalance


### external controllerMint
_(no internal calls)_


### public decimals
_(no internal calls)_


### external delegate
-> internal _delegate
  -> internal _transferTwab
    -> internal _decreaseUserTwab
      -> library TwabLib.decreaseBalance
    -> internal _decreaseTotalSupplyTwab
      -> library TwabLib.decreaseBalance
    -> internal _increaseUserTwab
      -> library TwabLib.increaseBalance
    -> internal _increaseTotalSupplyTwab
      -> library TwabLib.increaseBalance


### external delegateOf
_(no internal calls)_


### external delegateWithSignature
-> internal _delegate
  -> internal _transferTwab
    -> internal _decreaseUserTwab
      -> library TwabLib.decreaseBalance
    -> internal _decreaseTotalSupplyTwab
      -> library TwabLib.decreaseBalance
    -> internal _increaseUserTwab
      -> library TwabLib.increaseBalance
    -> internal _increaseTotalSupplyTwab
      -> library TwabLib.increaseBalance


### external getAccountDetails
_(no internal calls)_


### external getAverageBalanceBetween
-> library TwabLib.getAverageBalanceBetween


### external getAverageBalancesBetween
-> internal _getAverageBalancesBetween
  -> library TwabLib.getAverageBalanceBetween
    -> library TwabLib.getAverageBalanceBetween


### external getAverageTotalSuppliesBetween
-> internal _getAverageBalancesBetween
  -> library TwabLib.getAverageBalanceBetween
    -> library TwabLib.getAverageBalanceBetween


### external getBalanceAt
-> library TwabLib.getBalanceAt


### external getBalancesAt
-> library TwabLib.getBalanceAt
  -> library TwabLib.getBalanceAt


### external getTotalSuppliesAt
-> library TwabLib.getBalanceAt
  -> library TwabLib.getBalanceAt


### external getTotalSupplyAt
-> library TwabLib.getBalanceAt
  -> library TwabLib.getBalanceAt


### external getTwab
_(no internal calls)_


---

## YieldSourcePrizePool

_File: contracts/prize-pool/YieldSourcePrizePool.sol_

### external award
-> internal _mint


### external awardBalance
_(no internal calls)_


### external awardExternalERC20
-> internal _transferOut
  -> internal _canAwardExternal


### external awardExternalERC721
-> internal _canAwardExternal


### external balance
-> internal _balance


### external canAwardExternal
-> internal _canAwardExternal


### external captureAwardBalance
-> internal _ticketTotalSupply
-> internal _balance


### external compLikeDelegate
_(no internal calls)_


### external depositTo
-> internal _depositTo
  -> internal _canDeposit
  -> internal _token
  -> internal _mint
  -> internal _supply
    -> internal _token


### external depositToAndDelegate
-> internal _depositTo
  -> internal _canDeposit
  -> internal _token
  -> internal _mint
  -> internal _supply
    -> internal _token


### external getAccountedBalance
-> internal _ticketTotalSupply


### external getBalanceCap
_(no internal calls)_


### external getLiquidityCap
_(no internal calls)_


### external getPrizeStrategy
_(no internal calls)_


### external getTicket
_(no internal calls)_


### external getToken
-> internal _token


### external isControlled
-> internal _isControlled


### external onERC721Received
_(no internal calls)_


### external setBalanceCap
-> internal _setBalanceCap


### external setLiquidityCap
-> internal _setLiquidityCap


### external setPrizeStrategy
-> internal _setPrizeStrategy


### external setTicket
-> internal _setBalanceCap


### external sweep
-> internal _token
-> internal _supply
  -> internal _token


### external transferExternalERC20
-> internal _transferOut
  -> internal _canAwardExternal


### external withdrawFrom
-> internal _redeem
-> internal _token

