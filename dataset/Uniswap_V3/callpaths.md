# Callpaths — Uniswap_V3

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## UniswapV3Factory

_File: contracts/UniswapV3Factory.sol_

### external createPool
-> internal deploy


### public enableFeeAmount
_(no internal calls)_


### external setOwner
_(no internal calls)_


---

## UniswapV3Pool

_File: contracts/UniswapV3Pool.sol_

### external burn
-> private _modifyPosition
  -> private checkTicks
  -> private _updatePosition
    -> internal _blockTimestamp
  -> library SqrtPriceMath.getAmount0Delta
  -> library TickMath.getSqrtRatioAtTick
  -> internal _blockTimestamp
  -> library SqrtPriceMath.getAmount1Delta
  -> library LiquidityMath.addDelta


### external collect
-> library TransferHelper.safeTransfer


### external collectProtocol
-> library TransferHelper.safeTransfer


### external flash
-> library FullMath.mulDivRoundingUp
-> private balance0
-> private balance1
-> library TransferHelper.safeTransfer
-> library FullMath.mulDiv


### external increaseObservationCardinalityNext
_(no internal calls)_


### external initialize
-> library TickMath.getTickAtSqrtRatio
-> internal _blockTimestamp


### external mint
-> private _modifyPosition
  -> private checkTicks
  -> private _updatePosition
    -> internal _blockTimestamp
  -> library SqrtPriceMath.getAmount0Delta
  -> library TickMath.getSqrtRatioAtTick
  -> internal _blockTimestamp
  -> library SqrtPriceMath.getAmount1Delta
  -> library LiquidityMath.addDelta
-> private balance0
-> private balance1


### external observe
-> internal _blockTimestamp


### external setFeeProtocol
_(no internal calls)_


### external snapshotCumulativesInside
-> private checkTicks
-> internal _blockTimestamp


### external swap
-> internal _blockTimestamp
-> library TickMath.getSqrtRatioAtTick
-> library SwapMath.computeSwapStep
-> library FullMath.mulDiv
-> library LiquidityMath.addDelta
-> library TickMath.getTickAtSqrtRatio
-> library TransferHelper.safeTransfer
-> private balance0
-> private balance1

