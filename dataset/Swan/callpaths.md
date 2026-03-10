# Callpaths — Swan

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Swan

_File: Swan.sol_

### external addOperator
_(no internal calls)_


### external createAgent
_(no internal calls)_


### public getCurrentMarketParameters
_(no internal calls)_


### external getListedArtifacts
_(no internal calls)_


### external getListing
_(no internal calls)_


### external getListingPrice
_(no internal calls)_


### external getMarketParameters
_(no internal calls)_


### external getOracleFee
_(no internal calls)_


### external getOracleParameters
_(no internal calls)_


### public initialize
_(no internal calls)_


### external list
-> external_callback SwanAgent.InvalidPhase
-> public getCurrentMarketParameters
-> internal transferListingFees
  -> library Math.mulDiv
  -> public getCurrentMarketParameters


### external purchase
_(no internal calls)_


### external relist
-> public getCurrentMarketParameters
-> external_callback SwanAgent.InvalidPhase
-> internal transferListingFees
  -> library Math.mulDiv
  -> public getCurrentMarketParameters


### external removeOperator
_(no internal calls)_


### external setFactories
_(no internal calls)_


### external setMarketParameters
_(no internal calls)_


### external setOracleParameters
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## SwanAgent

_File: SwanAgent.sol_

### public getInventory
_(no internal calls)_


### public getRoundPhase
-> internal _computePhase
  -> internal _computeCycleTime


### public minFundAmount
_(no internal calls)_


### external oraclePurchaseRequest
-> internal _checkRoundPhase
  -> public getRoundPhase
    -> internal _computePhase
      -> internal _computeCycleTime


### public oracleResult
_(no internal calls)_


### external oracleStateRequest
-> internal _checkRoundPhase
  -> public getRoundPhase
    -> internal _computePhase
      -> internal _computeCycleTime


### external purchase
-> internal _checkRoundPhase
  -> public getRoundPhase
    -> internal _computePhase
      -> internal _computeCycleTime
-> public oracleResult


### external setAmountPerRound
-> internal _checkRoundPhase
  -> public getRoundPhase
    -> internal _computePhase
      -> internal _computeCycleTime


### public setListingFee
-> internal _checkRoundPhase
  -> public getRoundPhase
    -> internal _computePhase
      -> internal _computeCycleTime


### public treasury
_(no internal calls)_


### external updateState
-> internal _checkRoundPhase
  -> public getRoundPhase
    -> internal _computePhase
      -> internal _computeCycleTime
-> public oracleResult


### public withdraw
-> public getRoundPhase
  -> internal _computePhase
    -> internal _computeCycleTime
-> public treasury
-> public minFundAmount


### external withdrawAll
-> public getRoundPhase
  -> internal _computePhase
    -> internal _computeCycleTime
-> public treasury
-> public minFundAmount


---

## SwanAgentFactory

_File: SwanAgent.sol_

### external deploy
_(no internal calls)_


---

## SwanArtifactFactory

_File: SwanArtifact.sol_

### external deploy
_(no internal calls)_


---

## SwanDebate

_File: SwanDebate.sol_

### external approveFeeToken
_(no internal calls)_


### external getAgent
_(no internal calls)_


### external getAgentDebates
_(no internal calls)_


### external getDebateInfo
_(no internal calls)_


### external getLatestRoundForDebate
_(no internal calls)_


### external getRoundForDebate
_(no internal calls)_


### external initializeDebate
_(no internal calls)_


### external pause
_(no internal calls)_


### external recordOracleOutput
_(no internal calls)_


### external registerAgent
_(no internal calls)_


### external requestOracleOutput
_(no internal calls)_


### external terminateDebate
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## SwanLottery

_File: SwanLottery.sol_

### external claimRewards
-> public selectMultiplier
-> internal _computeRandomness


### external computeMultiplier
-> public selectMultiplier
-> internal _computeRandomness


### public getRewards
_(no internal calls)_


### public selectMultiplier
_(no internal calls)_


### external setAuthorization
_(no internal calls)_


### external setClaimWindow
_(no internal calls)_


---

## SwanManager

_File: SwanManager.sol_

### external addOperator
_(no internal calls)_


### public getCurrentMarketParameters
_(no internal calls)_


### external getMarketParameters
_(no internal calls)_


### external getOracleFee
_(no internal calls)_


### external getOracleParameters
_(no internal calls)_


### external removeOperator
_(no internal calls)_


### external setMarketParameters
_(no internal calls)_


### external setOracleParameters
_(no internal calls)_

