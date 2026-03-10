# Callpaths — Aloe_II

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Borrower

_File: src/Borrower.sol_

### external borrow
_(no internal calls)_


### external clear
-> public getPrices
  -> library BalanceSheet.computeProbePrices
-> private _getAssets
  -> library TickMath.getSqrtRatioAtTick
  -> library LiquidityAmounts.getAmountsForLiquidity
-> public getLiabilities
-> library BalanceSheet.isHealthy


### external getAssets
-> public getPrices
  -> library BalanceSheet.computeProbePrices
-> private _getAssets
  -> library TickMath.getSqrtRatioAtTick
  -> library LiquidityAmounts.getAmountsForLiquidity


### public getLiabilities
_(no internal calls)_


### public getPrices
-> library BalanceSheet.computeProbePrices


### external getUniswapPositions
_(no internal calls)_


### external liquidate
-> private _uniswapWithdraw
-> public getPrices
  -> library BalanceSheet.computeProbePrices
-> public getLiabilities
-> library BalanceSheet.computeAuctionAmounts
-> library BalanceSheet.auctionTime
-> library SafeTransferLib.safeTransferETH
-> library BalanceSheet.isHealthy


### external modify
-> public owner
-> public getLiabilities
-> public getPrices
  -> library BalanceSheet.computeProbePrices
-> private _getAssets
  -> library TickMath.getSqrtRatioAtTick
  -> library LiquidityAmounts.getAmountsForLiquidity
-> library BalanceSheet.isHealthy


### public owner
_(no internal calls)_


### external repay
_(no internal calls)_


### external rescue
_(no internal calls)_


### external transfer
_(no internal calls)_


### external transferEth
-> library SafeTransferLib.safeTransferETH


### external uniswapDeposit
_(no internal calls)_


### external uniswapV3MintCallback
_(no internal calls)_


### external uniswapWithdraw
-> private _uniswapWithdraw


### external warn
-> public getPrices
  -> library BalanceSheet.computeProbePrices
-> private _getAssets
  -> library TickMath.getSqrtRatioAtTick
  -> library LiquidityAmounts.getAmountsForLiquidity
-> public getLiabilities
-> library BalanceSheet.isHealthy
-> library SafeTransferLib.safeTransferETH


---

## BorrowerDeployer

_File: src/Factory.sol_

### external deploy
_(no internal calls)_


---

## Factory

_File: src/Factory.sol_

### external claimRewards
_(no internal calls)_


### external createBorrower
_(no internal calls)_


### external createMarket
-> private _newBorrower
-> private _setMarketConfig


### external enrollCourier
_(no internal calls)_


### external governMarketConfig
-> private _setMarketConfig


### external governRewardsRate
_(no internal calls)_


### external governRewardsToken
_(no internal calls)_


### external pause
_(no internal calls)_


---

## Ledger

_File: src/Ledger.sol_

### public DOMAIN_SEPARATOR
_(no internal calls)_


### public asset
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external borrowBalance
-> internal _previewInterest
-> internal _getCache


### external borrowBalanceStored
_(no internal calls)_


### public convertToAssets
-> internal _previewInterest
-> internal _getCache
-> internal _convertToAssets


### public convertToShares
-> internal _previewInterest
-> internal _getCache
-> internal _convertToShares


### external courierOf
_(no internal calls)_


### external decimals
-> public asset


### external maxDeposit
_(no internal calls)_


### external maxMint
_(no internal calls)_


### public maxRedeem
-> internal _previewInterest
-> internal _getCache
-> private _nominalShares
  -> internal _convertToShares
-> internal _convertToShares


### external maxWithdraw
-> public convertToAssets
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToAssets
-> public maxRedeem
  -> internal _previewInterest
  -> internal _getCache
  -> private _nominalShares
    -> internal _convertToShares
  -> internal _convertToShares


### external name
-> public asset
-> public peer


### public peer
_(no internal calls)_


### public previewDeposit
-> public convertToShares
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToShares


### public previewMint
-> internal _previewInterest
-> internal _getCache
-> internal _convertToAssets


### public previewRedeem
-> public convertToAssets
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToAssets


### public previewWithdraw
-> internal _previewInterest
-> internal _getCache
-> internal _convertToShares


### external principleOf
_(no internal calls)_


### external rewardsOf
-> library Rewards.load
-> library Rewards.previewUserState
-> public balanceOf


### external rewardsRate
-> library Rewards.getRate


### external stats
-> internal _previewInterest
-> internal _getCache


### external supportsInterface
_(no internal calls)_


### external symbol
-> public asset


### external totalAssets
-> internal _previewInterest
-> internal _getCache


### external underlyingBalance
-> internal _previewInterest
-> internal _getCache
-> internal _convertToAssets
-> private _nominalShares
  -> internal _convertToShares


### external underlyingBalanceStored
-> internal _convertToAssets
-> private _nominalShares
  -> internal _convertToShares


---

## Lender

_File: src/Lender.sol_

### public DOMAIN_SEPARATOR
_(no internal calls)_


### public accrueInterest
-> private _load
  -> internal _previewInterest
  -> internal _getCache
  -> private _mint
    -> library Rewards.load
    -> library Rewards.updatePoolState
    -> library Rewards.updateUserState
-> private _save


### external approve
_(no internal calls)_


### public asset
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external borrow
-> private _load
  -> internal _previewInterest
  -> internal _getCache
  -> private _mint
    -> library Rewards.load
    -> library Rewards.updatePoolState
    -> library Rewards.updateUserState
-> private _save
-> public asset


### external borrowBalance
-> internal _previewInterest
-> internal _getCache


### external borrowBalanceStored
_(no internal calls)_


### external claimRewards
-> library Rewards.load
-> library Rewards.claim
-> public balanceOf


### public convertToAssets
-> internal _previewInterest
-> internal _getCache
-> internal _convertToAssets


### public convertToShares
-> internal _previewInterest
-> internal _getCache
-> internal _convertToShares


### external courierOf
_(no internal calls)_


### external decimals
-> public asset


### external deposit
-> external deposit


### external initialize
_(no internal calls)_


### external maxDeposit
_(no internal calls)_


### external maxMint
_(no internal calls)_


### public maxRedeem
-> internal _previewInterest
-> internal _getCache
-> private _nominalShares
  -> internal _convertToShares
-> internal _convertToShares


### external maxWithdraw
-> public convertToAssets
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToAssets
-> public maxRedeem
  -> internal _previewInterest
  -> internal _getCache
  -> private _nominalShares
    -> internal _convertToShares
  -> internal _convertToShares


### external mint
-> public previewMint
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToAssets
-> external deposit
  -> external deposit


### external name
-> public asset
-> public peer


### public peer
_(no internal calls)_


### external permit
-> public DOMAIN_SEPARATOR


### public previewDeposit
-> public convertToShares
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToShares


### public previewMint
-> internal _previewInterest
-> internal _getCache
-> internal _convertToAssets


### public previewRedeem
-> public convertToAssets
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToAssets


### public previewWithdraw
-> internal _previewInterest
-> internal _getCache
-> internal _convertToShares


### external principleOf
_(no internal calls)_


### public redeem
-> public maxRedeem
  -> internal _previewInterest
  -> internal _getCache
  -> private _nominalShares
    -> internal _convertToShares
  -> internal _convertToShares
-> private _load
  -> internal _previewInterest
  -> internal _getCache
  -> private _mint
    -> library Rewards.load
    -> library Rewards.updatePoolState
    -> library Rewards.updateUserState
-> internal _convertToAssets
-> private _burn
  -> library Rewards.load
  -> library Rewards.updatePoolState
  -> library Rewards.updateUserState
-> private _save
-> public asset


### external repay
-> private _load
  -> internal _previewInterest
  -> internal _getCache
  -> private _mint
    -> library Rewards.load
    -> library Rewards.updatePoolState
    -> library Rewards.updateUserState
-> private _save
-> public asset


### external rewardsOf
-> library Rewards.load
-> library Rewards.previewUserState
-> public balanceOf


### external rewardsRate
-> library Rewards.getRate


### external setRateModelAndReserveFactor
-> public accrueInterest
  -> private _load
    -> internal _previewInterest
    -> internal _getCache
    -> private _mint
      -> library Rewards.load
      -> library Rewards.updatePoolState
      -> library Rewards.updateUserState
  -> private _save


### external setRewardsRate
-> library Rewards.load
-> library Rewards.setRate


### external stats
-> internal _previewInterest
-> internal _getCache


### external supportsInterface
_(no internal calls)_


### external symbol
-> public asset


### external totalAssets
-> internal _previewInterest
-> internal _getCache


### external transfer
-> public accrueInterest
  -> private _load
    -> internal _previewInterest
    -> internal _getCache
    -> private _mint
      -> library Rewards.load
      -> library Rewards.updatePoolState
      -> library Rewards.updateUserState
  -> private _save
-> private _transfer
  -> library Rewards.load
  -> library Rewards.updateUserState


### external transferFrom
-> public accrueInterest
  -> private _load
    -> internal _previewInterest
    -> internal _getCache
    -> private _mint
      -> library Rewards.load
      -> library Rewards.updatePoolState
      -> library Rewards.updateUserState
  -> private _save
-> private _transfer
  -> library Rewards.load
  -> library Rewards.updateUserState


### external underlyingBalance
-> internal _previewInterest
-> internal _getCache
-> internal _convertToAssets
-> private _nominalShares
  -> internal _convertToShares


### external underlyingBalanceStored
-> internal _convertToAssets
-> private _nominalShares
  -> internal _convertToShares


### external whitelist
_(no internal calls)_


### external withdraw
-> public previewWithdraw
  -> internal _previewInterest
  -> internal _getCache
  -> internal _convertToShares
-> public redeem
  -> public maxRedeem
    -> internal _previewInterest
    -> internal _getCache
    -> private _nominalShares
      -> internal _convertToShares
    -> internal _convertToShares
  -> private _load
    -> internal _previewInterest
    -> internal _getCache
    -> private _mint
      -> library Rewards.load
      -> library Rewards.updatePoolState
      -> library Rewards.updateUserState
  -> internal _convertToAssets
  -> private _burn
    -> library Rewards.load
    -> library Rewards.updatePoolState
    -> library Rewards.updateUserState
  -> private _save
  -> public asset


---

## RateModel

_File: src/RateModel.sol_

### external getYieldPerSecond
_(no internal calls)_


---

## VolatilityOracle

_File: src/VolatilityOracle.sol_

### external consult
-> library Oracle.consult
-> private _interpolateIV


### external prepare
-> private _getPoolMetadata
  -> library Oracle.getMaxSecondsAgo
-> private _getFeeGrowthGlobalsNow
  -> library Volatility.FeeGrowthGlobals


### external update
-> library Oracle.consult
  -> library Oracle.consult
  -> private _interpolateIV
-> private _interpolateIV
-> private _getFeeGrowthGlobalsOld
  -> private _binarySearch
    -> private _isInInterval
-> private _getFeeGrowthGlobalsNow
  -> library Volatility.FeeGrowthGlobals
-> private _isInInterval
-> private _ema
-> library Volatility.estimate

