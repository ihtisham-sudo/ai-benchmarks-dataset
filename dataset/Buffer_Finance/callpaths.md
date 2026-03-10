# Callpaths — Buffer_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BufferBNBOptions

_File: contracts/Options/BufferBNBOptions.sol_

### external create
-> public fees
  -> internal getSettlementFee
  -> internal getPeriodFee
    -> internal sqrt
  -> internal getStrikeFee
-> internal createOptionFor
-> internal distributeSettlementFee


### external exercise
-> internal canExercise
-> internal payProfit


### public fees
-> internal getSettlementFee
-> internal getPeriodFee
  -> internal sqrt
-> internal getStrikeFee


### public setAutoExerciseStatus
_(no internal calls)_


### external setImpliedVolRate
_(no internal calls)_


### external setOptionCollaterizationRatio
_(no internal calls)_


### external setReferralRewardPercentage
_(no internal calls)_


### external setSettlementFeePercentage
_(no internal calls)_


### external setSettlementFeeRecipient
_(no internal calls)_


### external setStakingFeePercentage
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public unlock
_(no internal calls)_


### external unlockAll
-> public unlock


---

## BufferGenericBNBOptions

_File: contracts/Options/BufferGenericBNBOptions.sol_

### external create
-> public fees
  -> internal getSettlementFee
  -> internal getPeriodFee
    -> internal sqrt
  -> internal getStrikeFee
-> internal createOptionFor
-> internal distributeSettlementFee


### external exercise
-> internal canExercise
-> internal payProfit


### public fees
-> internal getSettlementFee
-> internal getPeriodFee
  -> internal sqrt
-> internal getStrikeFee


### public setAutoExerciseStatus
_(no internal calls)_


### external setImpliedVolRate
_(no internal calls)_


### external setOptionCollaterizationRatio
_(no internal calls)_


### external setReferralRewardPercentage
_(no internal calls)_


### external setSettlementFeePercentage
_(no internal calls)_


### external setSettlementFeeRecipient
_(no internal calls)_


### external setStakingFeePercentage
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public unlock
_(no internal calls)_


### external unlockAll
-> public unlock


---

## BufferStaking

_File: contracts/Staking/BufferStaking.sol_

### external buy
-> public maxSupply
-> public lotPrice


### external claimProfit
-> internal saveProfit
  -> internal getUnsaved


### public lotPrice
_(no internal calls)_


### public maxSupply
_(no internal calls)_


### external profitOf
-> internal getUnsaved


### external revertTransfersInLockUpPeriod
_(no internal calls)_


### external sell
-> public lotPrice


---

## BufferStakingBNB

_File: contracts/Staking/BufferStakingBNB.sol_

### external buy
-> public maxSupply
-> public lotPrice


### external claimProfit
-> internal saveProfit
  -> internal getUnsaved
-> internal _transferProfit


### public lotPrice
_(no internal calls)_


### public maxSupply
_(no internal calls)_


### external profitOf
-> internal getUnsaved


### external revertTransfersInLockUpPeriod
_(no internal calls)_


### external sell
-> public lotPrice


### external sendProfit
_(no internal calls)_


---

## BufferStakingIBFR

_File: contracts/Staking/BufferStakingIBFR.sol_

### external buy
-> public maxSupply
-> public lotPrice


### external claimProfit
-> internal saveProfit
  -> internal getUnsaved
-> internal _transferProfit


### public lotPrice
_(no internal calls)_


### public maxSupply
_(no internal calls)_


### external profitOf
-> internal getUnsaved


### external revertTransfersInLockUpPeriod
_(no internal calls)_


### external sell
-> public lotPrice


### external sendProfit
_(no internal calls)_


---

## FakeBTCPriceProvider

_File: contracts/TestImplementations.sol_

### external getRoundData
_(no internal calls)_


### external latestAnswer
-> public latestRoundData


### public latestRoundData
_(no internal calls)_


### external setPrice
_(no internal calls)_


---

## FakePriceProvider

_File: contracts/TestImplementations.sol_

### external getRoundData
_(no internal calls)_


### external latestAnswer
-> public latestRoundData


### public latestRoundData
_(no internal calls)_


### external setPrice
_(no internal calls)_


---

## Migrations

_File: contracts/Migrations.sol_

### public setCompleted
_(no internal calls)_


### public upgrade
_(no internal calls)_

