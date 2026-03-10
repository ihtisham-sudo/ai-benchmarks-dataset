# Callpaths — UnitasProtocol_V1

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ERC20Token

_File: src/ERC20Token.sol_

### public addBlackList
_(no internal calls)_


### public approve
_(no internal calls)_


### external burn
_(no internal calls)_


### public decreaseAllowance
_(no internal calls)_


### public getBlacklist
_(no internal calls)_


### public increaseAllowance
_(no internal calls)_


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### public removeBlackList
_(no internal calls)_


### external revokeGovernor
_(no internal calls)_


### external revokeGuardian
_(no internal calls)_


### external revokeMinter
_(no internal calls)_


### external setGovernor
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### external setMinter
_(no internal calls)_


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## InsurancePool

_File: src/InsurancePool.sol_

### external depositCollateral
-> internal _checkAmountPositive
-> internal _setBalance
-> internal _getBalance


### public getCollateral
-> internal _getBalance


### public getPortfolio
-> internal _getPortfolio


### external receivePortfolio
-> internal _receivePortfolio
  -> library AddressUtils.checkNotZero
  -> internal _checkAmountPositive
  -> internal _getPortfolio
  -> internal _setPortfolio


### external sendPortfolio
-> internal _sendPortfolio
  -> library AddressUtils.checkNotZero
  -> internal _checkAmountPositive
  -> internal _getPortfolio
  -> internal _getBalance
  -> internal _setPortfolio


### external withdrawCollateral
-> internal _checkAmountPositive
-> internal _getBalance
-> internal _getPortfolio
-> internal _setBalance


---

## TimelockController

_File: src/TimelockController.sol_

### public cancel
-> public isOperationPending
  -> public getTimestamp


### public execute
-> public hashOperation
-> private _beforeCall
  -> public isOperationReady
    -> public getTimestamp
  -> public isOperationDone
    -> public getTimestamp
-> internal _execute
-> private _afterCall
  -> public isOperationReady
    -> public getTimestamp


### public executeBatch
-> public hashOperationBatch
-> private _beforeCall
  -> public isOperationReady
    -> public getTimestamp
  -> public isOperationDone
    -> public getTimestamp
-> internal _execute
-> private _afterCall
  -> public isOperationReady
    -> public getTimestamp


### public getMinDelay
_(no internal calls)_


### public getTimestamp
_(no internal calls)_


### public hashOperation
_(no internal calls)_


### public hashOperationBatch
_(no internal calls)_


### public isOperation
-> public getTimestamp


### public isOperationDone
-> public getTimestamp


### public isOperationPending
-> public getTimestamp


### public isOperationReady
-> public getTimestamp


### public schedule
-> public hashOperation
-> private _schedule
  -> public isOperation
    -> public getTimestamp
  -> public getMinDelay


### public scheduleBatch
-> public hashOperationBatch
-> private _schedule
  -> public isOperation
    -> public getTimestamp
  -> public getMinDelay


### external updateDelay
_(no internal calls)_


---

## TokenManager

_File: src/TokenManager.sol_

### external addTokensAndPairs
-> internal _addTokensAndPairs
  -> internal _addToken
    -> library AddressUtils.checkContract
    -> internal _isTokenTypeValid
  -> internal _setMinMaxPriceTolerance
  -> internal _addPair
    -> internal _checkPairParameters
      -> internal _checkSwapFeeNumerator
      -> internal _checkReserveRatioThreshold
    -> internal _sortTokens
    -> internal _addPairByTokens
      -> internal _getPairHash


### public getPair
-> internal _sortTokens
-> internal _checkPairExists
  -> internal _getPairHash


### public getPairHash
-> internal _sortTokens
-> internal _getPairHash


### public getPriceTolerance
_(no internal calls)_


### public getTokenType
_(no internal calls)_


### public isPairInPool
-> public getPairHash
  -> internal _sortTokens
  -> internal _getPairHash


### public isTokenInPool
-> internal _isTokenTypeValid


### external listPairTokensByIndexAndCount
_(no internal calls)_


### external listPairsByIndexAndCount
_(no internal calls)_


### external listTokensByIndexAndCount
_(no internal calls)_


### public pairByIndex
_(no internal calls)_


### public pairLength
_(no internal calls)_


### public pairTokenByIndex
_(no internal calls)_


### public pairTokenLength
_(no internal calls)_


### external removeTokensAndPairs
-> internal _removePair
  -> internal _sortTokens
  -> internal _removePairByTokens
    -> internal _getPairHash
-> internal _removeToken
  -> public pairTokenLength


### external setMinMaxPriceTolerance
-> internal _setMinMaxPriceTolerance


### external setUSD1
-> internal _setUSD1
  -> internal _removeToken
    -> public pairTokenLength
  -> internal _addToken
    -> library AddressUtils.checkContract
    -> internal _isTokenTypeValid


### public tokenByIndex
_(no internal calls)_


### public tokenLength
_(no internal calls)_


### external updatePairs
-> internal _updatePair
  -> internal _checkPairParameters
    -> internal _checkSwapFeeNumerator
    -> internal _checkReserveRatioThreshold
  -> internal _sortTokens
  -> internal _checkPairExists
    -> internal _getPairHash


---

## TokenPairs

_File: src/TokenPairs.sol_

### public getPairHash
-> internal _sortTokens
-> internal _getPairHash


### public isPairInPool
-> public getPairHash
  -> internal _sortTokens
  -> internal _getPairHash


### external listPairTokensByIndexAndCount
_(no internal calls)_


### public pairLength
_(no internal calls)_


### public pairTokenByIndex
_(no internal calls)_


### public pairTokenLength
_(no internal calls)_


---

## TypeTokens

_File: src/TypeTokens.sol_

### public isTokenInPool
_(no internal calls)_


### external listTokensByIndexAndCount
_(no internal calls)_


### public tokenByIndex
_(no internal calls)_


### public tokenLength
_(no internal calls)_


---

## Unitas

_File: src/Unitas.sol_

### external estimateSwapResult
-> internal _getSwapResult
  -> internal _checkAmountPositive
  -> internal _getPriceQuoteToken
  -> internal _checkPrice
  -> internal _calculateSwapResult
    -> internal _validateFeeFraction
    -> internal _calculateSwapResultByAmountIn
      -> internal _getFeeByAmountWithFee
      -> internal _convert
        -> internal _convertByFromPrice
        -> internal _convertByToPrice
    -> internal _calculateSwapResultByAmountOut
      -> internal _convert
        -> internal _convertByFromPrice
        -> internal _convertByToPrice
      -> internal _getFeeByAmountWithoutFee


### public getPortfolio
-> internal _getPortfolio


### public getReserve
-> internal _getBalance


### public getReserveStatus
-> internal _getTotalReservesAndCollaterals
  -> internal _getBalance
  -> internal _convert
    -> internal _convertByFromPrice
    -> internal _convertByToPrice
-> internal _getTotalLiabilities
  -> internal _convert
    -> internal _convertByFromPrice
    -> internal _convertByToPrice
-> internal _getReserveStatus
  -> library ScalingUtils.scaleByBases


### public initialize
-> internal _setOracle
  -> library AddressUtils.checkContract
-> internal _setSurplusPool
-> internal _setInsurancePool
  -> library AddressUtils.checkContract
-> internal _setTokenManager
  -> library AddressUtils.checkContract


### public pause
_(no internal calls)_


### external receivePortfolio
-> internal _receivePortfolio
  -> library AddressUtils.checkNotZero
  -> internal _checkAmountPositive
  -> internal _getPortfolio
  -> internal _setPortfolio


### external sendPortfolio
-> internal _sendPortfolio
  -> library AddressUtils.checkNotZero
  -> internal _checkAmountPositive
  -> internal _getPortfolio
  -> internal _getBalance
  -> internal _setPortfolio


### external setInsurancePool
-> internal _setInsurancePool
  -> library AddressUtils.checkContract


### external setOracle
-> internal _setOracle
  -> library AddressUtils.checkContract


### external setSurplusPool
-> internal _setSurplusPool


### external setTokenManager
-> internal _setTokenManager
  -> library AddressUtils.checkContract


### external swap
-> internal _getSwapResult
  -> internal _checkAmountPositive
  -> internal _getPriceQuoteToken
  -> internal _checkPrice
  -> internal _calculateSwapResult
    -> internal _validateFeeFraction
    -> internal _calculateSwapResultByAmountIn
      -> internal _getFeeByAmountWithFee
      -> internal _convert
        -> internal _convertByFromPrice
        -> internal _convertByToPrice
    -> internal _calculateSwapResultByAmountOut
      -> internal _convert
        -> internal _convertByFromPrice
        -> internal _convertByToPrice
      -> internal _getFeeByAmountWithoutFee
-> internal _swapIn
  -> internal _setBalance
  -> internal _getBalance
-> internal _swapOut
  -> internal _getBalance
  -> internal _getPortfolio
  -> internal _setBalance
-> internal _checkReserveRatio
  -> internal _getTotalReservesAndCollaterals
    -> internal _getBalance
    -> internal _convert
      -> internal _convertByFromPrice
      -> internal _convertByToPrice
  -> internal _getTotalLiabilities
    -> internal _convert
      -> internal _convertByFromPrice
      -> internal _convertByToPrice
  -> internal _getReserveStatus
    -> library ScalingUtils.scaleByBases


### public unpause
_(no internal calls)_


---

## XOracle

_File: src/XOracle.sol_

### public decimals
_(no internal calls)_


### public getLatestPrice
_(no internal calls)_


### public getPrice
_(no internal calls)_


### public putPrice
-> external_callback IOracle.Price


### external updatePrices
-> public putPrice
  -> external_callback IOracle.Price

