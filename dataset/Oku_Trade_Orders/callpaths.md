# Callpaths — Oku_Trade_Orders

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AutomationMaster

_File: contracts/automatedTrigger/AutomationMaster.sol_

### external checkMinOrderSize
_(no internal calls)_


### external checkUpkeep
_(no internal calls)_


### external generateOrderId
_(no internal calls)_


### external getExchangeRate
-> internal _getExchangeRate
  -> internal _getOraclePrices


### external getMinAmountReceived
-> internal _getOraclePrices


### external getRegisteredTokens
_(no internal calls)_


### public owner
_(no internal calls)_


### external pauseAll
-> internal _pause
-> internal _unpause


### public paused
_(no internal calls)_


### external performUpkeep
_(no internal calls)_


### external registerOracle
_(no internal calls)_


### external registerSubKeepers
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### external setMaxPendingOrders
_(no internal calls)_


### external setMinOrderSize
_(no internal calls)_


### external setOrderFee
_(no internal calls)_


### external sweep
_(no internal calls)_


### external sweepEther
_(no internal calls)_


### public transferOwnership
-> internal _transferOwnership


### external validateTarget
_(no internal calls)_


### external whitelistTargetSetter
_(no internal calls)_


### external whitelistTargets
_(no internal calls)_


---

## Bracket

_File: contracts/automatedTrigger/Bracket.sol_

### external adminCancelOrder
-> internal _cancelOrder


### external cancelOrder
-> internal _cancelOrder


### external checkUpkeep
-> internal checkInRange


### external createOrder
-> internal _initializeOrder
  -> internal procureTokens
  -> internal _createOrderWithSwap
    -> internal verifyTokenBalances
    -> internal execute
      -> internal getMinAmountReceivedAfterFee
    -> internal _createOrder
  -> internal _createOrder


### external fillStopLimitOrder
-> internal _initializeOrder
  -> internal procureTokens
  -> internal _createOrderWithSwap
    -> internal verifyTokenBalances
    -> internal execute
      -> internal getMinAmountReceivedAfterFee
    -> internal _createOrder
  -> internal _createOrder


### external getPendingOrders
_(no internal calls)_


### external getSpecificPendingOrders
_(no internal calls)_


### external modifyOrder
-> internal procureTokens


### public owner
_(no internal calls)_


### external pause
-> public owner
-> internal _pause
-> internal _unpause


### public paused
_(no internal calls)_


### external performUpkeep
-> internal checkInRange
-> internal verifyTokenBalances
-> internal execute
  -> internal getMinAmountReceivedAfterFee
-> internal applyFee


### public renounceOwnership
-> internal _transferOwnership


### external sweepDust
_(no internal calls)_


### public transferOwnership
-> internal _transferOwnership


---

## ERC20

_File: contracts/interfaces/openzeppelin/ERC20.sol_

### public DOMAIN_SEPARATOR
-> internal computeDomainSeparator


### public approve
_(no internal calls)_


### public permit
-> public DOMAIN_SEPARATOR
  -> internal computeDomainSeparator


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


---

## OracleLess

_File: contracts/automatedTrigger/OracleLess.sol_

### external adminCancelOrder
-> internal _cancelOrder


### external cancelOrder
-> internal _cancelOrder


### external createOrder
-> internal procureTokens


### external fillOrder
-> internal execute
  -> internal verifyTokenBalances
    -> internal getWhitelistedTokens
  -> internal getMinAmountReceivedAfterFee
-> internal applyFee


### external getPendingOrders
_(no internal calls)_


### external getSpecificPendingOrders
_(no internal calls)_


### external modifyOrder
-> internal _modifyOrder
  -> internal procureTokens


### public owner
_(no internal calls)_


### external pause
-> public owner
-> internal _pause
-> internal _unpause


### public paused
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


### external whitelistTokens
_(no internal calls)_


---

## OracleRelay

_File: contracts/oracle/External/OracleRelay.sol_

### external currentValue
_(no internal calls)_


---

## Ownable

_File: contracts/interfaces/openzeppelin/Ownable.sol_

### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


---

## Pausable

_File: contracts/interfaces/openzeppelin/Pausable.sol_

### public paused
_(no internal calls)_


---

## PlaceholderOracle

_File: contracts/oracle/Logic/PlaceholderOracle.sol_

### external currentValue
_(no internal calls)_


### external setPrice
_(no internal calls)_


---

## PythOracle

_File: contracts/oracle/External/PythOracle.sol_

### external currentValue
_(no internal calls)_


### external getUpdateFee
_(no internal calls)_


### external updatePrice
_(no internal calls)_


---

## StopLimit

_File: contracts/automatedTrigger/StopLimit.sol_

### external adminCancelOrder
-> internal _cancelOrder


### external cancelOrder
-> internal _cancelOrder


### external checkUpkeep
-> internal checkInRange


### external createOrder
-> internal _createOrder


### external getPendingOrders
_(no internal calls)_


### external getSpecificPendingOrders
_(no internal calls)_


### external modifyOrder
_(no internal calls)_


### public owner
_(no internal calls)_


### external pause
-> public owner
-> internal _pause
-> internal _unpause


### public paused
_(no internal calls)_


### external performUpkeep
-> internal checkInRange


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


---

## TokenEthRelay

_File: contracts/oracle/External/TokenEthRelay.sol_

### external currentValue
_(no internal calls)_


---

## UniV3TickTwapOracle

_File: contracts/oracle/External/UniV3TickTwapOracle.sol_

### external currentValue
-> private getLastSeconds

