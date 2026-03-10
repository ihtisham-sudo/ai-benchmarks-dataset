# Callpaths — USSD_V1

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Migrations

_File: contracts/Migrations.sol_

### public setCompleted
_(no internal calls)_


---

## SimOracle

_File: contracts/oracles/SimOracle.sol_

### external getPriceUSD
_(no internal calls)_


### public setPriceUSD
_(no internal calls)_


---

## StableOracleDAI

_File: contracts/oracles/StableOracleDAI.sol_

### external getPriceUSD
_(no internal calls)_


---

## StableOracleUSDT

_File: contracts_BNB/StableOracleUSDT.sol_

### external getPriceUSD
_(no internal calls)_


---

## StableOracleWBGL

_File: contracts/oracles/StableOracleWBGL.sol_

### external getPriceUSD
_(no internal calls)_


---

## StableOracleWBTC

_File: contracts/oracles/StableOracleWBTC.sol_

### external getPriceUSD
_(no internal calls)_


---

## StableOracleWETH

_File: contracts/oracles/StableOracleWETH.sol_

### external getPriceUSD
_(no internal calls)_


---

## StaticOracle

_File: contracts/oracles/UniswapV3StaticOracle.sol_

### external addNewFeeTier
_(no internal calls)_


### public getAllPoolsForPair
-> internal _getPoolsForTiers
  -> internal _resizeArray


### external isPairSupported
_(no internal calls)_


### public prepareAllAvailablePoolsWithCardinality
-> public getAllPoolsForPair
  -> internal _getPoolsForTiers
    -> internal _resizeArray
-> internal _prepare


### external prepareAllAvailablePoolsWithTimePeriod
-> public prepareAllAvailablePoolsWithCardinality
  -> public getAllPoolsForPair
    -> internal _getPoolsForTiers
      -> internal _resizeArray
  -> internal _prepare
-> internal _getCardinalityForTimePeriod


### public prepareSpecificFeeTiersWithCardinality
-> internal _getPoolsForTiers
  -> internal _resizeArray
-> internal _prepare


### external prepareSpecificFeeTiersWithTimePeriod
-> public prepareSpecificFeeTiersWithCardinality
  -> internal _getPoolsForTiers
    -> internal _resizeArray
  -> internal _prepare
-> internal _getCardinalityForTimePeriod


### public prepareSpecificPoolsWithCardinality
-> internal _prepare


### external prepareSpecificPoolsWithTimePeriod
-> public prepareSpecificPoolsWithCardinality
  -> internal _prepare
-> internal _getCardinalityForTimePeriod


### external quoteAllAvailablePoolsWithTimePeriod
-> internal _getQueryablePoolsForTiers
  -> public getAllPoolsForPair
    -> internal _getPoolsForTiers
      -> internal _resizeArray
  -> internal _resizeArray
-> internal _quote


### external quoteSpecificFeeTiersWithTimePeriod
-> internal _getPoolsForTiers
  -> internal _resizeArray
-> internal _quote


### external quoteSpecificPoolsWithTimePeriod
-> internal _quote


### external supportedFeeTiers
_(no internal calls)_


---

## USSD

_File: contracts/USSD.sol_

### public UniV3SwapInput
_(no internal calls)_


### public addCollateral
_(no internal calls)_


### public approveToRouter
_(no internal calls)_


### public burnRebalancer
_(no internal calls)_


### public calculateMint
-> public getCollateralIndex
-> public decimals


### public collateralFactor
_(no internal calls)_


### public collateralList
_(no internal calls)_


### public decimals
_(no internal calls)_


### public getCollateralIndex
_(no internal calls)_


### public initialize
_(no internal calls)_


### public mintForToken
-> public getCollateralIndex
-> public calculateMint
  -> public getCollateralIndex
  -> public decimals


### public mintRebalancer
_(no internal calls)_


### public removeCollateral
_(no internal calls)_


### public setRebalancer
_(no internal calls)_


### public setUniswapRouter
_(no internal calls)_


### public swapCollateralIndexes
_(no internal calls)_


---

## USSDRebalancer

_File: contracts/USSDRebalancer.sol_

### public calculateAmountTillPriceMatch
_(no internal calls)_


### public getOwnValuation
_(no internal calls)_


### public getPool
_(no internal calls)_


### public initialize
_(no internal calls)_


### public rebalance
-> public getOwnValuation
-> public calculateAmountTillPriceMatch
-> internal buyUSSDSellCollateral
-> internal sellUSSDBuyCollateral
  -> public getOwnValuation


### public setBaseAsset
_(no internal calls)_


### public setFlutterRatios
_(no internal calls)_


### public setMinDivisor
_(no internal calls)_


### public setPoolAddress
_(no internal calls)_


### public setTreshold
_(no internal calls)_


### public setUniswapCalculator
_(no internal calls)_


---

## USSDv2

_File: contracts/USSDv2.sol_

### public UniV3SwapInput
_(no internal calls)_


### public addCollateral
_(no internal calls)_


### public approveToRouter
_(no internal calls)_


### public burnRebalancer
_(no internal calls)_


### public collateralFactor
_(no internal calls)_


### public collateralList
_(no internal calls)_


### public decimals
_(no internal calls)_


### public getCollateralIndex
_(no internal calls)_


### public initialize
_(no internal calls)_


### public mintRebalancer
_(no internal calls)_


### public reclaimCollateral
_(no internal calls)_


### public removeCollateral
_(no internal calls)_


### public setRebalancer
_(no internal calls)_


### public setUniswapRouter
_(no internal calls)_


### public swapCollateralIndexes
_(no internal calls)_


---

## UniV3LiqCalculator

_File: contracts/USSDUniV3LiqCalculator.sol_

### public calculateAmountTillPriceMatch
-> internal nextInitializedTickWithinOneWord
  -> private position

