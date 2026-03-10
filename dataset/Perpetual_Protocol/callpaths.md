# Callpaths — Perpetual_Protocol

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Amm

_File: src/legacy/AmmV1.sol_

### public calcBaseAssetAfterLiquidityMigration
-> public getOutputPriceWithReserves
  -> library Decimal.zero
  -> library MixedDecimal.fromDecimal
  -> library Decimal.decimal
-> library MixedDecimal.fromDecimal
-> public getInputPrice
  -> public getInputPriceWithReserves
    -> library Decimal.zero
    -> library MixedDecimal.fromDecimal
    -> library Decimal.decimal


### external calcFee
-> library Decimal.zero


### public candidate
_(no internal calls)_


### external getBaseAssetDeltaThisFundingPeriod
_(no internal calls)_


### external getCumulativeNotional
_(no internal calls)_


### public getInputPrice
-> public getInputPriceWithReserves
  -> library Decimal.zero
  -> library MixedDecimal.fromDecimal
  -> library Decimal.decimal


### public getInputPriceWithReserves
-> library Decimal.zero
-> library MixedDecimal.fromDecimal
-> library Decimal.decimal


### public getInputTwap
-> internal implGetInputAssetTwapPrice
  -> internal calcTwap
    -> internal getPriceWithSpecificSnapshot
      -> library Decimal.zero
      -> public getInputPriceWithReserves
        -> library Decimal.zero
        -> library MixedDecimal.fromDecimal
        -> library Decimal.decimal
      -> public getOutputPriceWithReserves
        -> library Decimal.zero
        -> library MixedDecimal.fromDecimal
        -> library Decimal.decimal
    -> internal _blockTimestamp


### public getLatestLiquidityChangedSnapshots
_(no internal calls)_


### external getLiquidityChangedSnapshots
_(no internal calls)_


### external getLiquidityHistoryLength
_(no internal calls)_


### external getMaxHoldingBaseAsset
_(no internal calls)_


### external getOpenInterestNotionalCap
_(no internal calls)_


### public getOutputPrice
-> public getOutputPriceWithReserves
  -> library Decimal.zero
  -> library MixedDecimal.fromDecimal
  -> library Decimal.decimal


### public getOutputPriceWithReserves
-> library Decimal.zero
-> library MixedDecimal.fromDecimal
-> library Decimal.decimal


### public getOutputTwap
-> internal implGetInputAssetTwapPrice
  -> internal calcTwap
    -> internal getPriceWithSpecificSnapshot
      -> library Decimal.zero
      -> public getInputPriceWithReserves
        -> library Decimal.zero
        -> library MixedDecimal.fromDecimal
        -> library Decimal.decimal
      -> public getOutputPriceWithReserves
        -> library Decimal.zero
        -> library MixedDecimal.fromDecimal
        -> library Decimal.decimal
    -> internal _blockTimestamp


### external getReserve
_(no internal calls)_


### external getSettlementPrice
_(no internal calls)_


### external getSnapshotLen
_(no internal calls)_


### public getSpotPrice
_(no internal calls)_


### public getTwapPrice
-> internal implGetReserveTwapPrice
  -> internal calcTwap
    -> internal getPriceWithSpecificSnapshot
      -> library Decimal.zero
      -> public getInputPriceWithReserves
        -> library Decimal.zero
        -> library MixedDecimal.fromDecimal
        -> library Decimal.decimal
      -> public getOutputPriceWithReserves
        -> library Decimal.zero
        -> library MixedDecimal.fromDecimal
        -> library Decimal.decimal
    -> internal _blockTimestamp


### public getUnderlyingPrice
-> library Decimal.decimal


### public getUnderlyingTwapPrice
-> library Decimal.decimal


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
-> library Decimal.decimal
-> library Decimal.one
-> library SignedDecimal.zero
-> internal _blockTimestamp
-> internal _blockNumber


### external migrateLiquidity
-> library Decimal.one
-> internal checkLiquidityMultiplierLimit
  -> library Decimal.decimal
-> internal checkFluctuationLimit
  -> internal _blockNumber
  -> internal isOverFluctuationLimit
    -> library Decimal.one
-> public calcBaseAssetAfterLiquidityMigration
  -> public getOutputPriceWithReserves
    -> library Decimal.zero
    -> library MixedDecimal.fromDecimal
    -> library Decimal.decimal
  -> library MixedDecimal.fromDecimal
  -> public getInputPrice
    -> public getInputPriceWithReserves
      -> library Decimal.zero
      -> library MixedDecimal.fromDecimal
      -> library Decimal.decimal


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setCap
_(no internal calls)_


### external setCounterParty
_(no internal calls)_


### public setFluctuationLimitRatio
_(no internal calls)_


### external setGlobalShutdown
_(no internal calls)_


### external setOpen
-> internal _blockTimestamp


### public setOwner
_(no internal calls)_


### external setSpotPriceTwapInterval
_(no internal calls)_


### public setSpreadRatio
_(no internal calls)_


### public setTollRatio
_(no internal calls)_


### external settleFunding
-> internal _blockTimestamp
-> public getUnderlyingTwapPrice
  -> library Decimal.decimal
-> library MixedDecimal.fromDecimal
-> public getTwapPrice
  -> internal implGetReserveTwapPrice
    -> internal calcTwap
      -> internal getPriceWithSpecificSnapshot
        -> library Decimal.zero
        -> public getInputPriceWithReserves
          -> library Decimal.zero
          -> library MixedDecimal.fromDecimal
          -> library Decimal.decimal
        -> public getOutputPriceWithReserves
          -> library Decimal.zero
          -> library MixedDecimal.fromDecimal
          -> library Decimal.decimal
      -> internal _blockTimestamp
-> private updateFundingRate
-> library SignedDecimal.zero


### external shutdown
-> public owner
-> internal implShutdown
  -> public getLatestLiquidityChangedSnapshots
  -> library MixedDecimal.fromDecimal


### external swapInput
-> library Decimal.zero
-> public getInputPrice
  -> public getInputPriceWithReserves
    -> library Decimal.zero
    -> library MixedDecimal.fromDecimal
    -> library Decimal.decimal
-> internal updateReserve
  -> internal checkFluctuationLimit
    -> internal _blockNumber
    -> internal isOverFluctuationLimit
      -> library Decimal.one
  -> internal addReserveSnapshot
    -> internal _blockNumber
    -> internal _blockTimestamp


### external swapOutput
-> internal implSwapOutput
  -> library Decimal.zero
  -> public getOutputPrice
    -> public getOutputPriceWithReserves
      -> library Decimal.zero
      -> library MixedDecimal.fromDecimal
      -> library Decimal.decimal
  -> internal isSingleTxOverFluctuation
    -> internal isOverFluctuationLimit
      -> library Decimal.one
  -> internal updateReserve
    -> internal checkFluctuationLimit
      -> internal _blockNumber
      -> internal isOverFluctuationLimit
        -> library Decimal.one
    -> internal addReserveSnapshot
      -> internal _blockNumber
      -> internal _blockTimestamp


### public updateOwner
_(no internal calls)_


---

## AmmReader

_File: src/AmmReader.sol_

### external getAmmStates
-> private bytes32ToString


---

## BaseBridge

_File: src/bridge/BaseBridge.sol_

### public candidate
_(no internal calls)_


### external erc20Transfer
-> internal multiTokenTransfer
  -> internal _transferFrom
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> private approveToMediator
    -> internal _allowance
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _approve
      -> private _updateDecimal
        -> internal _getTokenDecimals
      -> private __approve
        -> internal _toUint
          -> internal _getTokenDecimals
      -> library Decimal.zero
    -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setAMBBridge
_(no internal calls)_


### public setMultiTokenMediator
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## ChainlinkL1

_File: src/ChainlinkL1.sol_

### external addAggregator
-> internal requireNonEmptyAddress


### public candidate
_(no internal calls)_


### public getAggregator
_(no internal calls)_


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
-> public setRootBridge
  -> internal requireNonEmptyAddress
-> public setPriceFeedL2
  -> internal requireNonEmptyAddress


### public owner
_(no internal calls)_


### external removeAggregator
-> internal requireNonEmptyAddress
-> public getAggregator


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public setPriceFeedL2
-> internal requireNonEmptyAddress


### public setRootBridge
-> internal requireNonEmptyAddress


### external updateLatestRoundData
-> public getAggregator
-> internal requireNonEmptyAddress
-> library Decimal.decimal
-> internal formatDecimals


### public updateOwner
_(no internal calls)_


---

## ChainlinkPriceFeed

_File: src/ChainlinkPriceFeed.sol_

### external addAggregator
-> internal requireNonEmptyAddress


### public candidate
_(no internal calls)_


### public getAggregator
_(no internal calls)_


### external getLatestTimestamp
-> public getAggregator
-> internal requireNonEmptyAddress
-> internal getLatestRoundData
  -> internal requireEnoughHistory
  -> internal getRoundData
    -> internal requireEnoughHistory


### external getPreviousPrice
-> public getAggregator
-> internal requireNonEmptyAddress
-> internal requirePositivePrice
-> internal formatDecimals


### external getPreviousTimestamp
-> public getAggregator
-> internal requireNonEmptyAddress
-> internal requirePositivePrice


### external getPrice
-> public getAggregator
-> internal requireNonEmptyAddress
-> internal getLatestRoundData
  -> internal requireEnoughHistory
  -> internal getRoundData
    -> internal requireEnoughHistory
-> internal formatDecimals


### external getTwapPrice
-> public getAggregator
-> internal requireNonEmptyAddress
-> internal getLatestRoundData
  -> internal requireEnoughHistory
  -> internal getRoundData
    -> internal requireEnoughHistory
-> internal _blockTimestamp
-> internal formatDecimals
-> internal getRoundData
  -> internal requireEnoughHistory


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public owner
_(no internal calls)_


### external removeAggregator
-> internal requireNonEmptyAddress
-> public getAggregator


### public renounceOwnership
_(no internal calls)_


### external setLatestData
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## ClearingHouse

_File: src/legacy/ClearingHouseV1.sol_

### external addMargin
-> private requireAmm
-> private requireNonZeroInput
-> internal _msgSender
-> internal adjustPositionForLiquidityChanged
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
  -> internal setPosition
-> internal setPosition
-> internal _transferFrom
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


### external adjustPosition
-> internal adjustPositionForLiquidityChanged
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
  -> internal setPosition
-> internal _msgSender


### external closePosition
-> private requireAmm
-> private requireNotRestrictionMode
  -> internal _blockNumber
  -> public getUnadjustedPosition
  -> internal _msgSender
-> internal _msgSender
-> internal adjustPositionForLiquidityChanged
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
  -> internal setPosition
-> private internalClosePosition
  -> public getUnadjustedPosition
  -> private requirePositionSize
  -> public getPositionNotionalAndUnrealizedPnl
    -> public getPosition
      -> public getUnadjustedPosition
      -> internal calcPositionAfterLiquidityMigration
    -> library MixedDecimal.fromDecimal
  -> private calcRemainMarginWithFundingPayment
    -> public getLatestCumulativePremiumFraction
  -> library MixedDecimal.fromDecimal
  -> internal updateOpenInterestNotional
    -> library SignedDecimal.zero
    -> internal _msgSender
  -> internal clearPosition
    -> library SignedDecimal.zero
    -> library Decimal.zero
    -> internal _blockNumber
-> internal enterRestrictionMode
  -> internal _blockNumber
-> internal realizeBadDebt
  -> library Decimal.zero
-> internal withdraw
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
-> internal transferFee
  -> internal _transferFrom
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### public getLatestCumulativePremiumFraction
_(no internal calls)_


### public getMarginRatio
-> public getPosition
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
-> private requirePositionSize
-> private requireNonZeroInput
-> public getPositionNotionalAndUnrealizedPnl
  -> public getPosition
    -> public getUnadjustedPosition
    -> internal calcPositionAfterLiquidityMigration
  -> library MixedDecimal.fromDecimal
-> private calcRemainMarginWithFundingPayment
  -> public getLatestCumulativePremiumFraction
-> library MixedDecimal.fromDecimal


### public getPosition
-> public getUnadjustedPosition
-> internal calcPositionAfterLiquidityMigration


### public getPositionNotionalAndUnrealizedPnl
-> public getPosition
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
-> library MixedDecimal.fromDecimal


### public getUnadjustedPosition
_(no internal calls)_


### public initialize
-> internal __OwnerPausable_init
-> library Decimal.decimal
-> public setMaintenanceMarginRatio
-> public setLiquidationFeeRatio


### external liquidate
-> private requireAmm
-> private requireMoreMarginRatio
-> public getMarginRatio
  -> public getPosition
    -> public getUnadjustedPosition
    -> internal calcPositionAfterLiquidityMigration
  -> private requirePositionSize
  -> private requireNonZeroInput
  -> public getPositionNotionalAndUnrealizedPnl
    -> public getPosition
      -> public getUnadjustedPosition
      -> internal calcPositionAfterLiquidityMigration
    -> library MixedDecimal.fromDecimal
  -> private calcRemainMarginWithFundingPayment
    -> public getLatestCumulativePremiumFraction
  -> library MixedDecimal.fromDecimal
-> internal adjustPositionForLiquidityChanged
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
  -> internal setPosition
-> private internalClosePosition
  -> public getUnadjustedPosition
  -> private requirePositionSize
  -> public getPositionNotionalAndUnrealizedPnl
    -> public getPosition
      -> public getUnadjustedPosition
      -> internal calcPositionAfterLiquidityMigration
    -> library MixedDecimal.fromDecimal
  -> private calcRemainMarginWithFundingPayment
    -> public getLatestCumulativePremiumFraction
  -> library MixedDecimal.fromDecimal
  -> internal updateOpenInterestNotional
    -> library SignedDecimal.zero
    -> internal _msgSender
  -> internal clearPosition
    -> library SignedDecimal.zero
    -> library Decimal.zero
    -> internal _blockNumber
-> library Decimal.zero
-> internal enterRestrictionMode
  -> internal _blockNumber
-> internal realizeBadDebt
  -> library Decimal.zero
-> internal transferToInsuranceFund
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
-> internal withdraw
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
-> internal _msgSender


### external openPosition
-> private requireAmm
-> private requireNonZeroInput
-> private requireMoreMarginRatio
-> library MixedDecimal.fromDecimal
-> library Decimal.one
-> private requireNotRestrictionMode
  -> internal _blockNumber
  -> public getUnadjustedPosition
  -> internal _msgSender
-> internal _msgSender
-> internal adjustPositionForLiquidityChanged
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
  -> internal setPosition
-> public getMarginRatio
  -> public getPosition
    -> public getUnadjustedPosition
    -> internal calcPositionAfterLiquidityMigration
  -> private requirePositionSize
  -> private requireNonZeroInput
  -> public getPositionNotionalAndUnrealizedPnl
    -> public getPosition
      -> public getUnadjustedPosition
      -> internal calcPositionAfterLiquidityMigration
    -> library MixedDecimal.fromDecimal
  -> private calcRemainMarginWithFundingPayment
    -> public getLatestCumulativePremiumFraction
  -> library MixedDecimal.fromDecimal
-> internal internalIncreasePosition
  -> internal _msgSender
  -> public getUnadjustedPosition
  -> internal swapInput
    -> library MixedDecimal.fromDecimal
  -> internal updateOpenInterestNotional
    -> library SignedDecimal.zero
    -> internal _msgSender
  -> library MixedDecimal.fromDecimal
  -> private calcRemainMarginWithFundingPayment
    -> public getLatestCumulativePremiumFraction
  -> public getPositionNotionalAndUnrealizedPnl
    -> public getPosition
      -> public getUnadjustedPosition
      -> internal calcPositionAfterLiquidityMigration
    -> library MixedDecimal.fromDecimal
  -> internal _blockNumber
-> internal openReversePosition
  -> public getPositionNotionalAndUnrealizedPnl
    -> public getPosition
      -> public getUnadjustedPosition
      -> internal calcPositionAfterLiquidityMigration
    -> library MixedDecimal.fromDecimal
  -> internal _msgSender
  -> internal updateOpenInterestNotional
    -> library SignedDecimal.zero
    -> internal _msgSender
  -> library MixedDecimal.fromDecimal
  -> public getUnadjustedPosition
  -> internal swapInput
    -> library MixedDecimal.fromDecimal
  -> private calcRemainMarginWithFundingPayment
    -> public getLatestCumulativePremiumFraction
  -> internal _blockNumber
  -> internal closeAndOpenReversePosition
    -> private internalClosePosition
      -> public getUnadjustedPosition
      -> private requirePositionSize
      -> public getPositionNotionalAndUnrealizedPnl
        -> public getPosition
          -> public getUnadjustedPosition
          -> internal calcPositionAfterLiquidityMigration
        -> library MixedDecimal.fromDecimal
      -> private calcRemainMarginWithFundingPayment
        -> public getLatestCumulativePremiumFraction
      -> library MixedDecimal.fromDecimal
      -> internal updateOpenInterestNotional
        -> library SignedDecimal.zero
        -> internal _msgSender
      -> internal clearPosition
        -> library SignedDecimal.zero
        -> library Decimal.zero
        -> internal _blockNumber
    -> internal _msgSender
    -> library Decimal.zero
    -> internal internalIncreasePosition
      -> internal _msgSender
      -> public getUnadjustedPosition
      -> internal swapInput
        -> library MixedDecimal.fromDecimal
      -> internal updateOpenInterestNotional
        -> library SignedDecimal.zero
        -> internal _msgSender
      -> library MixedDecimal.fromDecimal
      -> private calcRemainMarginWithFundingPayment
        -> public getLatestCumulativePremiumFraction
      -> public getPositionNotionalAndUnrealizedPnl
        -> public getPosition
          -> public getUnadjustedPosition
          -> internal calcPositionAfterLiquidityMigration
        -> library MixedDecimal.fromDecimal
      -> internal _blockNumber
    -> library SignedDecimal.zero
-> internal setPosition
-> internal enterRestrictionMode
  -> internal _blockNumber
-> internal _transferFrom
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
-> internal withdraw
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
-> internal transferFee
  -> internal _transferFrom
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### public pause
_(no internal calls)_


### external payFunding
-> private requireAmm
-> public getLatestCumulativePremiumFraction
-> internal transferToInsuranceFund
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### external removeMargin
-> private requireAmm
-> private requireNonZeroInput
-> internal _msgSender
-> internal adjustPositionForLiquidityChanged
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
  -> internal setPosition
-> library MixedDecimal.fromDecimal
-> private calcRemainMarginWithFundingPayment
  -> public getLatestCumulativePremiumFraction
-> internal setPosition
-> private requireMoreMarginRatio
-> public getMarginRatio
  -> public getPosition
    -> public getUnadjustedPosition
    -> internal calcPositionAfterLiquidityMigration
  -> private requirePositionSize
  -> private requireNonZeroInput
  -> public getPositionNotionalAndUnrealizedPnl
    -> public getPosition
      -> public getUnadjustedPosition
      -> internal calcPositionAfterLiquidityMigration
    -> library MixedDecimal.fromDecimal
  -> private calcRemainMarginWithFundingPayment
    -> public getLatestCumulativePremiumFraction
  -> library MixedDecimal.fromDecimal
-> internal withdraw
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### external setFeePool
_(no internal calls)_


### public setLiquidationFeeRatio
_(no internal calls)_


### public setMaintenanceMarginRatio
_(no internal calls)_


### external setWhitelist
_(no internal calls)_


### external settlePosition
-> private requireAmm
-> internal _msgSender
-> public getPosition
  -> public getUnadjustedPosition
  -> internal calcPositionAfterLiquidityMigration
-> private requirePositionSize
-> internal clearPosition
  -> library SignedDecimal.zero
  -> library Decimal.zero
  -> internal _blockNumber
-> library MixedDecimal.fromDecimal
-> internal _transfer
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


### public unpause
_(no internal calls)_


---

## ClearingHouseViewer

_File: src/ClearingHouseViewer.sol_

### external getFreeCollateral
-> public getPersonalPositionWithFundingPayment
  -> library MixedDecimal.fromDecimal
  -> private getFundingPayment
    -> library SignedDecimal.zero
  -> library Decimal.zero
-> library MixedDecimal.fromDecimal
-> library Decimal.decimal


### external getMarginRatio
_(no internal calls)_


### external getPersonalBalanceWithFundingPayment
-> public getPersonalPositionWithFundingPayment
  -> library MixedDecimal.fromDecimal
  -> private getFundingPayment
    -> library SignedDecimal.zero
  -> library Decimal.zero


### public getPersonalPositionWithFundingPayment
-> library MixedDecimal.fromDecimal
-> private getFundingPayment
  -> library SignedDecimal.zero
-> library Decimal.zero


### external getUnrealizedPnl
_(no internal calls)_


### external isPositionNeedToBeMigrated
_(no internal calls)_


---

## ClientBridge

_File: src/bridge/xDai/ClientBridge.sol_

### external erc20Transfer
-> internal multiTokenTransfer


### public initialize
-> internal __BaseBridge_init
  -> public setAMBBridge
  -> public setMultiTokenMediator


### public setAMBBridge
_(no internal calls)_


### external setMinWithdrawalAmount
_(no internal calls)_


### public setMultiTokenMediator
_(no internal calls)_


---

## ERC20ViewOnly

_File: src/utils/ERC20ViewOnly.sol_

### public allowance
_(no internal calls)_


### public approve
_(no internal calls)_


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


---

## ExchangeWrapper

_File: src/exchangeWrapper/ExchangeWrapper.sol_

### public approve
-> internal _approve
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> private __approve
    -> internal _toUint
      -> internal _getTokenDecimals
  -> library Decimal.zero


### public candidate
_(no internal calls)_


### external getInputPrice
-> internal implGetSpotPrice
  -> library Decimal.one
  -> internal balancerAcceptableToken
    -> internal isUSDT
  -> library Decimal.decimal
  -> internal _getTokenDecimals
  -> internal _toDecimal
    -> internal _getTokenDecimals
    -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> internal isUSDT
  -> internal compoundUnderlyingAmount
    -> internal _toUint
      -> internal _getTokenDecimals
    -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


### external getOutputPrice
-> internal implGetSpotPrice
  -> library Decimal.one
  -> internal balancerAcceptableToken
    -> internal isUSDT
  -> library Decimal.decimal
  -> internal _getTokenDecimals
  -> internal _toDecimal
    -> internal _getTokenDecimals
    -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> internal isUSDT
  -> internal compoundUnderlyingAmount
    -> internal _toUint
      -> internal _getTokenDecimals
    -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


### external getSpotPrice
-> internal implGetSpotPrice
  -> library Decimal.one
  -> internal balancerAcceptableToken
    -> internal isUSDT
  -> library Decimal.decimal
  -> internal _getTokenDecimals
  -> internal _toDecimal
    -> internal _getTokenDecimals
    -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> internal isUSDT
  -> internal compoundUnderlyingAmount
    -> internal _toUint
      -> internal _getTokenDecimals
    -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
-> public setBalancerPool
-> public setCompoundCUsdt
  -> public approve
    -> internal _approve
      -> private _updateDecimal
        -> internal _getTokenDecimals
      -> private __approve
        -> internal _toUint
          -> internal _getTokenDecimals
      -> library Decimal.zero
  -> library Decimal.decimal


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setBalancerPool
_(no internal calls)_


### public setCompoundCUsdt
-> public approve
  -> internal _approve
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> private __approve
      -> internal _toUint
        -> internal _getTokenDecimals
    -> library Decimal.zero
-> library Decimal.decimal


### public setOwner
_(no internal calls)_


### external swapInput
-> internal implSwapInput
  -> internal _transferFrom
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> internal isUSDT
  -> internal compoundMint
    -> internal _toUint
      -> internal _getTokenDecimals
    -> internal compoundCTokenAmount
      -> internal _toUint
        -> internal _getTokenDecimals
      -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> internal balancerAcceptableToken
    -> internal isUSDT
  -> internal balancerSwapIn
    -> library Decimal.decimal
    -> internal _approve
      -> private _updateDecimal
        -> internal _getTokenDecimals
      -> private __approve
        -> internal _toUint
          -> internal _getTokenDecimals
      -> library Decimal.zero
    -> internal _toUint
      -> internal _getTokenDecimals
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal compoundRedeem
    -> internal _toUint
      -> internal _getTokenDecimals
    -> internal compoundUnderlyingAmount
      -> internal _toUint
        -> internal _getTokenDecimals
      -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### external swapOutput
-> internal implSwapOutput
  -> internal isUSDT
  -> internal compoundCTokenAmount
    -> internal _toUint
      -> internal _getTokenDecimals
    -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal balancerAcceptableToken
    -> internal isUSDT
  -> internal calcBalancerInGivenOut
    -> internal _toUint
      -> internal _getTokenDecimals
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal compoundUnderlyingAmount
    -> internal _toUint
      -> internal _getTokenDecimals
    -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transferFrom
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> internal compoundMint
    -> internal _toUint
      -> internal _getTokenDecimals
    -> internal compoundCTokenAmount
      -> internal _toUint
        -> internal _getTokenDecimals
      -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> internal balancerSwapOut
    -> library Decimal.decimal
    -> internal _approve
      -> private _updateDecimal
        -> internal _getTokenDecimals
      -> private __approve
        -> internal _toUint
          -> internal _getTokenDecimals
      -> library Decimal.zero
    -> internal _toUint
      -> internal _getTokenDecimals
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal compoundRedeemUnderlying
    -> internal _toUint
      -> internal _getTokenDecimals
    -> internal compoundCTokenAmount
      -> internal _toUint
        -> internal _getTokenDecimals
      -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### public updateOwner
_(no internal calls)_


---

## FeeRewardPoolL1

_File: src/staking/FeeRewardPoolL1.sol_

### public candidate
_(no internal calls)_


### public earned
-> internal balanceOf
  -> library Decimal.decimal
-> public rewardPerToken
  -> internal totalSupply
    -> library Decimal.decimal
  -> public lastTimeRewardApplicable
    -> internal _blockTimestamp


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public lastTimeRewardApplicable
-> internal _blockTimestamp


### external notifyRewardAmount
-> internal updateReward
  -> public rewardPerToken
    -> internal totalSupply
      -> library Decimal.decimal
    -> public lastTimeRewardApplicable
      -> internal _blockTimestamp
  -> public lastTimeRewardApplicable
    -> internal _blockTimestamp
  -> public earned
    -> internal balanceOf
      -> library Decimal.decimal
    -> public rewardPerToken
      -> internal totalSupply
        -> library Decimal.decimal
      -> public lastTimeRewardApplicable
        -> internal _blockTimestamp
-> internal _blockTimestamp


### external notifyStakeChanged
-> internal updateReward
  -> public rewardPerToken
    -> internal totalSupply
      -> library Decimal.decimal
    -> public lastTimeRewardApplicable
      -> internal _blockTimestamp
  -> public lastTimeRewardApplicable
    -> internal _blockTimestamp
  -> public earned
    -> internal balanceOf
      -> library Decimal.decimal
    -> public rewardPerToken
      -> internal totalSupply
        -> library Decimal.decimal
      -> public lastTimeRewardApplicable
        -> internal _blockTimestamp


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public rewardPerToken
-> internal totalSupply
  -> library Decimal.decimal
-> public lastTimeRewardApplicable
  -> internal _blockTimestamp


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


### external withdrawReward
-> internal updateReward
  -> public rewardPerToken
    -> internal totalSupply
      -> library Decimal.decimal
    -> public lastTimeRewardApplicable
      -> internal _blockTimestamp
  -> public lastTimeRewardApplicable
    -> internal _blockTimestamp
  -> public earned
    -> internal balanceOf
      -> library Decimal.decimal
    -> public rewardPerToken
      -> internal totalSupply
        -> library Decimal.decimal
      -> public lastTimeRewardApplicable
        -> internal _blockTimestamp
-> library Decimal.zero
-> internal _transfer
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


---

## FeeTokenPoolDispatcherL1

_File: src/staking/FeeTokenPoolDispatcherL1.sol_

### external addFeeRewardPool
_(no internal calls)_


### public candidate
_(no internal calls)_


### external getFeeTokenLength
_(no internal calls)_


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public isFeeTokenExisted
_(no internal calls)_


### public owner
_(no internal calls)_


### external removeFeeRewardPool
-> private transferToPool
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public transferToFeeRewardPool
-> private transferToPool
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _transfer
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal


### public updateOwner
_(no internal calls)_


---

## InflationMonitor

_File: src/InflationMonitor.sol_

### external appendMintedTokenHistory
-> internal _blockTimestamp


### public candidate
_(no internal calls)_


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
-> library Decimal.one


### external isOverMintThreshold
-> internal _totalSupply
  -> internal _toDecimal
    -> internal _getTokenDecimals
    -> library Decimal.decimal
-> public mintedAmountDuringMintThresholdPeriod
  -> library Decimal.zero
  -> internal _blockTimestamp


### public mintedAmountDuringMintThresholdPeriod
-> library Decimal.zero
-> internal _blockTimestamp


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public setShutdownThreshold
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## InsuranceFund

_File: src/InsuranceFund.sol_

### public addAmm
-> public isExistedAmm
-> internal isQuoteTokenExisted


### public candidate
_(no internal calls)_


### external getAllAmms
_(no internal calls)_


### public getQuoteTokenLength
_(no internal calls)_


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public isExistedAmm
_(no internal calls)_


### public owner
_(no internal calls)_


### external removeAmm
-> public isExistedAmm


### external removeToken
-> internal isQuoteTokenExisted
-> public getQuoteTokenLength
-> internal balanceOf
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
-> internal getTokenWithMaxValue
  -> internal balanceOf
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
-> internal swapInput
  -> library Decimal.zero
  -> internal _approve
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> private __approve
      -> internal _toUint
        -> internal _getTokenDecimals
    -> library Decimal.zero
-> library Decimal.zero


### public renounceOwnership
_(no internal calls)_


### external setBeneficiary
_(no internal calls)_


### external setExchange
_(no internal calls)_


### external setInflationMonitor
_(no internal calls)_


### public setMinter
_(no internal calls)_


### public setOwner
_(no internal calls)_


### external shutdownAllAmm
_(no internal calls)_


### public updateOwner
_(no internal calls)_


### external withdraw
-> internal isQuoteTokenExisted
-> internal balanceOf
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
-> internal swapEnoughQuoteAmount
  -> internal getOrderedQuoteTokens
    -> public getQuoteTokenLength
    -> internal balanceOf
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
  -> internal balanceOf
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
  -> internal swapInput
    -> library Decimal.zero
    -> internal _approve
      -> private _updateDecimal
        -> internal _getTokenDecimals
      -> private __approve
        -> internal _toUint
          -> internal _getTokenDecimals
      -> library Decimal.zero
  -> library Decimal.zero
-> internal _transfer
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


---

## KeeperRewardBase

_File: src/keeper/KeeperRewardBase.sol_

### public candidate
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setKeeperFunctions
-> library Decimal.decimal


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## KeeperRewardL1

_File: src/keeper/KeeperRewardL1.sol_

### external initialize
-> internal __BaseKeeperReward_init


### external setKeeperFunctions
-> library Decimal.decimal


### external updatePriceFeed
-> internal getTaskInfo
  -> internal requireNonEmptyAddress
-> internal postTaskAction
  -> internal getTaskInfo
    -> internal requireNonEmptyAddress


---

## KeeperRewardL2

_File: src/keeper/KeeperRewardL2.sol_

### external initialize
-> internal __BaseKeeperReward_init


### external payFunding
-> internal getTaskInfo
  -> internal requireNonEmptyAddress
-> internal postTaskAction
  -> internal getTaskInfo
    -> internal requireNonEmptyAddress


### external setKeeperFunctions
-> library Decimal.decimal


---

## L2PriceFeed

_File: src/L2PriceFeed.sol_

### external addAggregator
-> private requireKeyExisted
  -> private isExistedKey


### public candidate
_(no internal calls)_


### public getLatestTimestamp
-> private isExistedKey
-> public getPriceFeedLength


### public getPreviousPrice
-> private isExistedKey
-> public getPriceFeedLength


### public getPreviousTimestamp
-> private isExistedKey
-> public getPriceFeedLength


### external getPrice
-> private isExistedKey
-> public getPriceFeedLength


### public getPriceFeedLength
_(no internal calls)_


### external getTwapPrice
-> private isExistedKey
-> public getPriceFeedLength
-> internal _blockTimestamp


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public owner
_(no internal calls)_


### external removeAggregator
-> private requireKeyExisted
  -> private isExistedKey


### public renounceOwnership
_(no internal calls)_


### external setLatestData
-> private requireKeyExisted
  -> private isExistedKey
-> public getLatestTimestamp
  -> private isExistedKey
  -> public getPriceFeedLength


### public setOwner
_(no internal calls)_


### external setRootBridge
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## MerkleRedeemUpgradeSafe

_File: src/staking/Balancer/MerkleRedeemUpgradeSafe.sol_

### public candidate
_(no internal calls)_


### external claimStatus
_(no internal calls)_


### public claimWeek
-> public verifyClaim
-> private disburse


### public claimWeeks
-> public verifyClaim
-> private disburse


### external merkleRoots
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public seedAllocations
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


### public verifyClaim
_(no internal calls)_


---

## MetaTxGateway

_File: src/MetaTxGateway.sol_

### external addToWhitelists
_(no internal calls)_


### public candidate
_(no internal calls)_


### external executeMetaTransaction
-> public isInWhitelists
-> internal verify
  -> internal toTypedMessageHash
  -> internal hashMetaTransaction
-> internal _getRevertMessage


### external getNonce
_(no internal calls)_


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
-> internal getChainID


### public isInWhitelists
_(no internal calls)_


### public owner
_(no internal calls)_


### external removeFromWhitelists
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## Minter

_File: src/Minter.sol_

### public candidate
_(no internal calls)_


### external getPerpToken
_(no internal calls)_


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public mintForLoss
_(no internal calls)_


### external mintReward
-> library Decimal.decimal


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setInflationMonitor
_(no internal calls)_


### external setInsuranceFund
_(no internal calls)_


### public setOwner
_(no internal calls)_


### external setRewardsDistribution
_(no internal calls)_


### external setSupplySchedule
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## OwnerPausableUpgradeSafe

_File: src/OwnerPausable.sol_

### public candidate
_(no internal calls)_


### public owner
_(no internal calls)_


### public pause
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public unpause
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## PerpFiOwnableUpgrade

_File: src/utils/PerpFiOwnableUpgrade.sol_

### public candidate
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## PerpRewardVesting

_File: src/staking/PerpRewardVesting.sol_

### external claimStatus
_(no internal calls)_


### public claimWeek
-> internal _blockTimestamp


### public claimWeeks
-> public claimWeek
  -> internal _blockTimestamp


### external getLengthOfMerkleRoots
_(no internal calls)_


### external initialize
-> internal __MerkleRedeem_init
  -> internal __MerkleRedeem_init_unchained


### external merkleRoots
_(no internal calls)_


### public seedAllocations
-> internal _blockTimestamp


### public verifyClaim
_(no internal calls)_


---

## RewardsDistribution

_File: src/RewardsDistribution.sol_

### public addRewardsDistribution
_(no internal calls)_


### public candidate
_(no internal calls)_


### public distributeRewards
-> internal _balanceOf
  -> internal _toDecimal
    -> internal _getTokenDecimals
    -> library Decimal.decimal
-> internal _transfer
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
-> internal _blockTimestamp


### public editRewardsDistribution
_(no internal calls)_


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public owner
_(no internal calls)_


### external removeRewardsDistribution
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## RewardsDistributionRecipient

_File: src/RewardsDistributionRecipient.sol_

### public candidate
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public setOwner
_(no internal calls)_


### external setRewardsDistribution
_(no internal calls)_


### public updateOwner
_(no internal calls)_


---

## RootBridge

_File: src/bridge/ethereum/RootBridge.sol_

### external erc20Transfer
-> internal multiTokenTransfer
  -> private approveToMediator
    -> library Decimal.decimal


### public initialize
-> internal __BaseBridge_init
  -> public setAMBBridge
  -> public setMultiTokenMediator


### public setAMBBridge
_(no internal calls)_


### public setMultiTokenMediator
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


### external updatePriceFeed
-> internal callBridge


---

## RootBridgeV2

_File: src/bridge/ethereum/RootBridgeV2.sol_

### public initialize
_(no internal calls)_


### external setMinDepositAmount
_(no internal calls)_


### external setMinWithdrawalAmount
_(no internal calls)_


---

## StakedPerpToken

_File: src/staking/StakedPerpToken.sol_

### external addStakeModule
_(no internal calls)_


### public allowance
_(no internal calls)_


### public approve
_(no internal calls)_


### public balanceOf
-> internal _balanceOfAt
  -> library Decimal.decimal
-> internal _blockNumber


### external balanceOfAt
-> internal _balanceOfAt
  -> library Decimal.decimal


### public candidate
_(no internal calls)_


### external getStakeModuleLength
_(no internal calls)_


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public isStakeModuleExisted
_(no internal calls)_


### public owner
_(no internal calls)_


### external removeStakeModule
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setCooldownPeriod
_(no internal calls)_


### public setOwner
_(no internal calls)_


### external stake
-> private requireNonZeroAmount
-> internal requireStakeModuleExisted
-> internal _transferFrom
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
-> internal _mint
  -> library Decimal.decimal
  -> public balanceOf
    -> internal _balanceOfAt
      -> library Decimal.decimal
    -> internal _blockNumber
  -> public totalSupply
    -> internal _totalSupplyAt
      -> library Decimal.decimal
    -> internal _blockNumber
  -> internal _blockNumber
  -> internal addPersonalBalanceCheckPoint
  -> internal addTotalSupplyCheckPoint


### public totalSupply
-> internal _totalSupplyAt
  -> library Decimal.decimal
-> internal _blockNumber


### external totalSupplyAt
-> internal _totalSupplyAt
  -> library Decimal.decimal


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external unstake
-> internal requireStakeModuleExisted
-> library Decimal.decimal
-> private requireNonZeroAmount
-> internal _burn
  -> library Decimal.decimal
  -> public balanceOf
    -> internal _balanceOfAt
      -> library Decimal.decimal
    -> internal _blockNumber
  -> public totalSupply
    -> internal _totalSupplyAt
      -> library Decimal.decimal
    -> internal _blockNumber
  -> internal _blockNumber
  -> internal addPersonalBalanceCheckPoint
  -> internal addTotalSupplyCheckPoint
-> internal _blockTimestamp


### public updateOwner
_(no internal calls)_


### external withdraw
-> private requireNonZeroAmount
-> internal _blockTimestamp
-> internal _transfer
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


---

## StakingReserve

_File: src/StakingReserve.sol_

### external claimFeesAndVestedReward
-> public getVestedReward
  -> public nextEpochIndex
  -> library Decimal.zero
-> public getFeeRevenue
  -> public nextEpochIndex
  -> public getFeeOfEpoch
-> internal _transfer
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


### external depositAndStake
-> private deposit
  -> public nextEpochIndex
  -> internal _transferFrom
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toUint
      -> internal _getTokenDecimals
    -> private _validateBalance
      -> internal _balanceOf
        -> internal _toDecimal
          -> internal _getTokenDecimals
          -> library Decimal.decimal
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
-> public stake
  -> public getUnlockedBalance
    -> public getLockedBalance
      -> library Decimal.zero
    -> public nextEpochIndex
  -> public nextEpochIndex
  -> internal _blockTimestamp
  -> private increaseStake
    -> public getLockedBalance
      -> library Decimal.zero


### external getEpochRewardHistoryLength
_(no internal calls)_


### public getFeeEpochCursor
_(no internal calls)_


### public getFeeOfEpoch
_(no internal calls)_


### public getFeeRevenue
-> public nextEpochIndex
-> public getFeeOfEpoch


### public getLockedBalance
-> library Decimal.zero


### public getRewardEpochCursor
_(no internal calls)_


### public getTotalBalance
-> public nextEpochIndex


### public getTotalEffectiveStake
_(no internal calls)_


### public getUnlockedBalance
-> public getLockedBalance
  -> library Decimal.zero
-> public nextEpochIndex


### public getUnstakableBalance
-> public getLockedBalance
  -> library Decimal.zero
-> public nextEpochIndex


### public getVestedReward
-> public nextEpochIndex
-> library Decimal.zero


### public initialize
_(no internal calls)_


### public isExistedFeeToken
_(no internal calls)_


### public nextEpochIndex
_(no internal calls)_


### external notifyRewardAmount
-> public getTotalBalance
  -> public nextEpochIndex
-> public nextEpochIndex
-> library Decimal.zero
-> library SignedDecimal.zero


### external notifyTokenAmount
-> public isExistedFeeToken


### external setFeeNotifier
_(no internal calls)_


### external setRewardsDistribution
_(no internal calls)_


### external setVestingPeriod
_(no internal calls)_


### public stake
-> public getUnlockedBalance
  -> public getLockedBalance
    -> library Decimal.zero
  -> public nextEpochIndex
-> public nextEpochIndex
-> internal _blockTimestamp
-> private increaseStake
  -> public getLockedBalance
    -> library Decimal.zero


### external unstake
-> public getUnstakableBalance
  -> public getLockedBalance
    -> library Decimal.zero
  -> public nextEpochIndex
-> public nextEpochIndex
-> public getLockedBalance
  -> library Decimal.zero


### external withdraw
-> public getUnlockedBalance
  -> public getLockedBalance
    -> library Decimal.zero
  -> public nextEpochIndex
-> internal _transfer
  -> private _updateDecimal
    -> internal _getTokenDecimals
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _toUint
    -> internal _getTokenDecimals
  -> private _validateBalance
    -> internal _balanceOf
      -> internal _toDecimal
        -> internal _getTokenDecimals
        -> library Decimal.decimal
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal


---

## SupplySchedule

_File: src/SupplySchedule.sol_

### public candidate
_(no internal calls)_


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
-> library Decimal.decimal


### public isMintable
-> internal _blockTimestamp


### external isStarted
_(no internal calls)_


### external mintableSupply
-> public isMintable
  -> internal _blockTimestamp
-> library Decimal.zero
-> internal _blockTimestamp
-> library Decimal.decimal


### public owner
_(no internal calls)_


### external recordMintEvent
-> library Decimal.one


### public renounceOwnership
_(no internal calls)_


### public setDecayRate
_(no internal calls)_


### public setOwner
_(no internal calls)_


### external startSchedule
-> internal _blockTimestamp


### public updateOwner
_(no internal calls)_


---

## TollPool

_File: src/TollPool.sol_

### external addFeeToken
_(no internal calls)_


### public candidate
_(no internal calls)_


### external getFeeTokenLength
_(no internal calls)_


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained


### public isFeeTokenExisted
_(no internal calls)_


### public owner
_(no internal calls)_


### external removeFeeToken
-> private transferToDispatcher
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _approve
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> private __approve
      -> internal _toUint
        -> internal _getTokenDecimals
    -> library Decimal.zero


### public renounceOwnership
_(no internal calls)_


### external setFeeTokenPoolDispatcher
_(no internal calls)_


### public setOwner
_(no internal calls)_


### external transferToFeeTokenPoolDispatcher
-> private transferToDispatcher
  -> internal _balanceOf
    -> internal _toDecimal
      -> internal _getTokenDecimals
      -> library Decimal.decimal
  -> internal _approve
    -> private _updateDecimal
      -> internal _getTokenDecimals
    -> private __approve
      -> internal _toUint
        -> internal _getTokenDecimals
    -> library Decimal.zero


### public updateOwner
_(no internal calls)_

