# Callpaths — Yieldoor

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## LendingPool

_File: yieldoor/src/LendingPool.sol_

### external borrow
-> internal getReserve


### public borrowingRateOfReserve
_(no internal calls)_


### public deposit
-> internal _deposit
  -> internal getReserve


### public disableBorrowing
_(no internal calls)_


### external emergencyPauseAll
_(no internal calls)_


### public enableBorrowing
_(no internal calls)_


### public exchangeRateOfReserve
_(no internal calls)_


### public freezeReserve
_(no internal calls)_


### public getCurrentBorrowingIndex
_(no internal calls)_


### public getLeverageParams
-> internal getReserve


### public getYTokenAddress
_(no internal calls)_


### external pullFunds
-> internal getReserve


### external pushFunds
-> internal getReserve


### public redeem
-> internal getReserve
-> internal _redeem
  -> internal getReserve


### external repay
-> internal getReserve


### public setBorrowingRateConfig
-> public setBorrowingRateConfig


### external setLeverageParams
_(no internal calls)_


### external setLeverager
_(no internal calls)_


### public setReserveCapacity
_(no internal calls)_


### public totalBorrowsOfReserve
_(no internal calls)_


### public totalLiquidityOfReserve
_(no internal calls)_


### public unFreezeReserve
_(no internal calls)_


### external unPauseAll
_(no internal calls)_


### public utilizationRateOfReserve
_(no internal calls)_


---

## Leverager

_File: yieldoor/src/Leverager.sol_

### external changeVaultMaxBorrow
_(no internal calls)_


### external changeVaultMaxLeverage
_(no internal calls)_


### external changeVaultMinCollateralPct
_(no internal calls)_


### external enableTokenAsBorrowed
_(no internal calls)_


### external getPosition
_(no internal calls)_


### external initVault
_(no internal calls)_


### public isLiquidateable
-> internal _calculateTokenValues


### external liquidatePosition
-> public isLiquidateable
  -> internal _calculateTokenValues
-> internal _calculateTokenValues


### external openLeveragedPosition
-> internal _calculateTokenValues
-> internal _getTokenIn
-> internal _checkWithinlimits
-> public isLiquidateable
  -> internal _calculateTokenValues
-> internal _sweepTokens


### external setLiquidationFee
_(no internal calls)_


### external setMinBorrow
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


### external setSwapRouter
_(no internal calls)_


### external toggleVaultLeverage
_(no internal calls)_


### external withdraw
-> internal _isApprovedOrOwner


---

## PriceFeed

_File: yieldoor/src/PriceFeed.sol_

### public getPrice
-> internal _getChainlinkPrice


### public hasPriceFeed
_(no internal calls)_


### external setChainlinkPriceFeed
_(no internal calls)_


---

## Strategy

_File: yieldoor/src/Strategy.sol_

### external addVestingPosition
-> public collectFees
  -> public idleBalances
  -> internal collectPositionFees
  -> internal _withdrawPartOfVestingPosition
    -> internal _removeFromPosition
-> private _requirePriceWithinRange
  -> internal _priceWithinRange
    -> public twapTick
    -> public checkPoolActivity
-> library LiquidityAmounts.getLiquidityForAmounts
-> library TickMath.getSqrtRatioAtTick


### public balances
-> public idleBalances
-> library LiquidityAmounts.getAmountsForLiquidity
-> library TickMath.getSqrtRatioAtTick


### external changeFeeRecipient
_(no internal calls)_


### external changePositionWidth
-> public rebalance
  -> private _requirePriceWithinRange
    -> internal _priceWithinRange
      -> public twapTick
      -> public checkPoolActivity
  -> public collectFees
    -> public idleBalances
    -> internal collectPositionFees
    -> internal _withdrawPartOfVestingPosition
      -> internal _removeFromPosition
  -> internal _removeLiquidity
    -> internal _removeFromPosition
  -> public idleBalances
  -> internal _setMainTicks
  -> internal _addLiquidityToMainPosition
    -> library LiquidityAmounts.getLiquidityForAmounts
    -> library TickMath.getSqrtRatioAtTick
  -> internal _setSecondaryPositionsTicks
    -> public price
      -> library FullMath.mulDiv
  -> internal _addLiquidityToSecondaryPosition
    -> library LiquidityAmounts.getLiquidityForAmounts
    -> library TickMath.getSqrtRatioAtTick


### external changeRebalancer
_(no internal calls)_


### public checkPoolActivity
_(no internal calls)_


### public collectFees
-> public idleBalances
-> internal collectPositionFees
-> internal _withdrawPartOfVestingPosition
  -> internal _removeFromPosition


### public compound
-> private _requirePriceWithinRange
  -> internal _priceWithinRange
    -> public twapTick
    -> public checkPoolActivity
-> public collectFees
  -> public idleBalances
  -> internal collectPositionFees
  -> internal _withdrawPartOfVestingPosition
    -> internal _removeFromPosition
-> public idleBalances
-> internal _addLiquidityToMainPosition
  -> library LiquidityAmounts.getLiquidityForAmounts
  -> library TickMath.getSqrtRatioAtTick
-> internal _addLiquidityToSecondaryPosition
  -> library LiquidityAmounts.getLiquidityForAmounts
  -> library TickMath.getSqrtRatioAtTick


### external getMainPosition
_(no internal calls)_


### external getSecondaryPosition
_(no internal calls)_


### external getVestingPosition
_(no internal calls)_


### public idleBalances
_(no internal calls)_


### public price
-> library FullMath.mulDiv


### public rebalance
-> private _requirePriceWithinRange
  -> internal _priceWithinRange
    -> public twapTick
    -> public checkPoolActivity
-> public collectFees
  -> public idleBalances
  -> internal collectPositionFees
  -> internal _withdrawPartOfVestingPosition
    -> internal _removeFromPosition
-> internal _removeLiquidity
  -> internal _removeFromPosition
-> public idleBalances
-> internal _setMainTicks
-> internal _addLiquidityToMainPosition
  -> library LiquidityAmounts.getLiquidityForAmounts
  -> library TickMath.getSqrtRatioAtTick
-> internal _setSecondaryPositionsTicks
  -> public price
    -> library FullMath.mulDiv
-> internal _addLiquidityToSecondaryPosition
  -> library LiquidityAmounts.getLiquidityForAmounts
  -> library TickMath.getSqrtRatioAtTick


### external setMaxObservationDeviation
_(no internal calls)_


### external setProtocolFee
-> public collectFees
  -> public idleBalances
  -> internal collectPositionFees
  -> internal _withdrawPartOfVestingPosition
    -> internal _removeFromPosition


### external setRebalanceInterval
_(no internal calls)_


### external setTickTwapDeviation
_(no internal calls)_


### external setTwap
_(no internal calls)_


### public twapPrice
-> public twapTick
-> library TickMath.getSqrtRatioAtTick
-> library FullMath.mulDiv


### public twapTick
_(no internal calls)_


### external uniswapV3MintCallback
_(no internal calls)_


### external withdrawPartial
-> public idleBalances
-> internal _removeFromPosition


---

## Vault

_File: yieldoor/src/Vault.sol_

### external addVestingPosition
_(no internal calls)_


### external balances
_(no internal calls)_


### public checkPoolActivity
_(no internal calls)_


### external deposit
-> internal _calcDeposit


### public price
_(no internal calls)_


### external setDepositFee
_(no internal calls)_


### external setStrategy
_(no internal calls)_


### public twapPrice
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## yToken

_File: yieldoor/src/yToken.sol_

### external burn
_(no internal calls)_


### public decimals
_(no internal calls)_


### external mint
_(no internal calls)_


### external transferUnderlyingTo
_(no internal calls)_

