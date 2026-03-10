# Callpaths — Tokemak

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AbstractRewarder

_File: src/rewarders/AbstractRewarder.sol_

### external addToWhitelist
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### public earned
-> public rewardPerToken
  -> public lastBlockRewardApplicable


### external isWhitelisted
_(no internal calls)_


### public lastBlockRewardApplicable
_(no internal calls)_


### external queueNewRewards
-> internal notifyRewardAmount
  -> internal _updateReward
    -> public rewardPerToken
      -> public lastBlockRewardApplicable
    -> public lastBlockRewardApplicable
    -> public earned
      -> public rewardPerToken
        -> public lastBlockRewardApplicable
  -> library Errors.ZeroAmount


### external recover
-> library Errors.verifyNotZero
-> library Errors.InvalidAddress
-> library Errors.AssetNotAllowed


### external removeFromWhitelist
-> library Errors.ItemNotFound


### public rewardPerToken
-> public lastBlockRewardApplicable


### external setTokeLockDuration
-> library Errors.verifyNotZero
-> external_callback IAccToke.StakingDurationTooShort


---

## AccToke

_File: src/staking/AccToke.sol_

### external addWETHRewards
-> internal _addWETHRewards
  -> library Errors.verifyNotZero


### external collectRewards
-> internal _collectRewards


### external extend
-> internal _collectRewards
-> library Errors.verifyNotZero
-> public previewPoints


### external getLockups
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### public isStakeableAmount
_(no internal calls)_


### external pause
_(no internal calls)_


### public paused
_(no internal calls)_


### public previewPoints
_(no internal calls)_


### public previewRewards
_(no internal calls)_


### external setMaxStakeDuration
_(no internal calls)_


### external stake
-> internal _stake
  -> public isStakeableAmount
  -> public previewPoints
  -> internal _collectRewards


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external unpause
_(no internal calls)_


### external unstake
-> internal _collectRewards


---

## AccessController

_File: src/security/AccessController.sol_

### external getSystemRegistry
_(no internal calls)_


### external setupRole
_(no internal calls)_


### public verifyOwner
_(no internal calls)_


---

## AerodromeDestinationVault

_File: src/vault/AerodromeDestinationVault.sol_

### public balanceOfUnderlyingDebt
-> public internalDebtBalance
-> public externalDebtBalance


### external baseAsset
_(no internal calls)_


### external collectRewards
-> internal _collectRewards
  -> library AerodromeRewardsAdapter.claimRewards


### external debtValue
-> private _debtValue
  -> public getPool


### public decimals
_(no internal calls)_


### external depositUnderlying
-> library Errors.verifyNotZero
-> internal _onDeposit
  -> library AerodromeStakingAdapter.stakeLPs


### external exchangeName
_(no internal calls)_


### external executeExtension
-> library Errors.verifyNotZero
-> public externalDebtBalance
-> public internalDebtBalance
-> public externalQueriedBalance
-> public internalQueriedBalance


### public externalDebtBalance
_(no internal calls)_


### public externalQueriedBalance
_(no internal calls)_


### external getMarketplaceRewards
_(no internal calls)_


### public getPool
_(no internal calls)_


### external getRangePricesLP
-> public getPool


### external getStats
_(no internal calls)_


### external getUnderlyerCeilingPrice
-> public getPool


### external getUnderlyerFloorPrice
-> public getPool


### external getValidatedSafePrice
-> public getPool


### external getValidatedSpotPrice
-> public getPool


### public initialize
-> library Errors.verifyNotZero
-> library Errors.InvalidParam
-> external_callback IVoter.GaugeNotAlive
-> library Errors.InvalidConfiguration
-> internal _addTrackedToken


### public internalDebtBalance
_(no internal calls)_


### public internalQueriedBalance
_(no internal calls)_


### external isShutdown
_(no internal calls)_


### public isTrackedToken
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public name
_(no internal calls)_


### public poolDealInEth
_(no internal calls)_


### external poolType
_(no internal calls)_


### external recover
-> public isTrackedToken


### external recoverUnderlying
-> library Errors.verifyNotZero
-> public externalQueriedBalance
-> public externalDebtBalance
-> public internalQueriedBalance
-> public internalDebtBalance
-> internal _ensureLocalUnderlyingBalance
  -> library AerodromeStakingAdapter.unstakeLPs


### external rewarder
_(no internal calls)_


### external setExtension
_(no internal calls)_


### external setIncentiveCalculator
-> internal _validateCalculator


### external setMessage
_(no internal calls)_


### external setRecoupMaxCredit
-> private _setRecoupMaxCredit
  -> library Errors.InvalidParam


### external shutdown
_(no internal calls)_


### external shutdownStatus
_(no internal calls)_


### public symbol
_(no internal calls)_


### public trackedTokens
_(no internal calls)_


### external underlying
_(no internal calls)_


### external underlyingReserves
_(no internal calls)_


### external underlyingTokens
_(no internal calls)_


### external underlyingTotalSupply
_(no internal calls)_


### external withdrawBaseAsset
-> internal _withdrawBaseAsset
  -> library Errors.verifyNotZero
  -> internal _ensureLocalUnderlyingBalance
    -> library AerodromeStakingAdapter.unstakeLPs
  -> internal _burnUnderlyer
    -> library AerodromeAdapter.AerodromeRemoveLiquidityParams
    -> library AerodromeAdapter.removeLiquidity
  -> library Errors.verifyArrayLengths
  -> library LibAdapter._approve


### external withdrawUnderlying
-> library Errors.verifyNotZero
-> internal _ensureLocalUnderlyingBalance
  -> library AerodromeStakingAdapter.unstakeLPs


---

## AerodromeOracle

_File: src/oracles/providers/base/AerodromeOracle.sol_

### external getDescription
_(no internal calls)_


### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor


### external getSpotPrice
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor


### external getSystemRegistry
_(no internal calls)_


---

## AerodromeStakingDexCalculator

_File: src/stats/calculators/AerodromeStakingDexCalculator.sol_

### external current
_(no internal calls)_


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.CalculatorAssetMismatch


### public shouldSnapshot
_(no internal calls)_


### external snapshot
-> public shouldSnapshot
-> internal _snapshot


---

## AerodromeStakingIncentiveCalculator

_File: src/stats/calculators/AerodromeStakingIncentiveCalculator.sol_

### external current
-> internal _computeTotalAPR
  -> internal _snapshotRewarder
    -> internal _getSnapshotStatus
  -> internal _getLpTokenPriceInEth
    -> library Errors.UnsafePrice
  -> internal _computeAPR
    -> internal _getIncentivePrice
-> library Stats.decayCredits


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _getSnapshotStatus
-> library Stats.differsByMoreThanFivePercent


### external snapshot
-> public shouldSnapshot
  -> internal _getSnapshotStatus
  -> library Stats.differsByMoreThanFivePercent
-> internal _snapshot
  -> internal _computeTotalAPR
    -> internal _snapshotRewarder
      -> internal _getSnapshotStatus
    -> internal _getLpTokenPriceInEth
      -> library Errors.UnsafePrice
    -> internal _computeAPR
      -> internal _getIncentivePrice
  -> library Stats.decayCredits


---

## AerodromeSwap

_File: src/swapper/adapters/AerodromeSwap.sol_

### external swap
-> library LibAdapter._approve
-> library Errors.SlippageExceeded


### external validate
-> library Errors.ItemNotFound


---

## AsyncSwapperRegistry

_File: src/liquidation/AsyncSwapperRegistry.sol_

### external getSystemRegistry
_(no internal calls)_


### external isRegistered
_(no internal calls)_


### external list
_(no internal calls)_


### external register
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external unregister
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external verifyIsRegistered
-> library Errors.NotRegistered


---

## AuraCalculator

_File: src/stats/calculators/AuraCalculator.sol_

### external current
-> internal _computeTotalAPR
  -> internal _getRewardPoolMetrics
  -> internal _shouldSnapshot
    -> internal _snapshotStatus
    -> library Stats.differsByMoreThanFivePercent
  -> internal _snapshotRewarder
    -> internal _snapshotStatus
  -> internal _getLpTokenPriceInEth
    -> library Errors.UnsafePrice
  -> internal _computeAPR
    -> internal _getIncentivePrice
  -> public getPlatformTokenMintAmount
    -> library AuraRewards.getAURAMintAmount
  -> public resolveRewardToken
-> library Stats.decayCredits
-> internal _getStakingIncentiveStats
  -> public resolveRewardToken
-> public getPlatformTokenMintAmount
  -> library AuraRewards.getAURAMintAmount


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public getPlatformTokenMintAmount
-> library AuraRewards.getAURAMintAmount


### public initialize
-> library Errors.InvalidParam


### public resolveRewardToken
_(no internal calls)_


### public shouldSnapshot
-> internal _getRewardPoolMetrics
-> internal _shouldSnapshot
  -> internal _snapshotStatus
  -> library Stats.differsByMoreThanFivePercent


---

## AuraL2Calculator

_File: src/stats/calculators/AuraL2Calculator.sol_

### public getPlatformTokenMintAmount
_(no internal calls)_


### public initialize
-> library Errors.InvalidParam


### public resolveRewardToken
_(no internal calls)_


---

## AutopilotRouter

_File: src/vault/AutopilotRouter.sol_

### external claimAutopoolRewards
-> internal _checkVault
  -> library Errors.ItemNotFound
-> internal _checkRewarder
  -> library Errors.ItemNotFound


### public claimRewards
-> library Errors.AccessDenied


### public deposit
_(no internal calls)_


### public depositBalance
-> public deposit


### public depositMax
-> public deposit


### external expiration
_(no internal calls)_


### public mint
_(no internal calls)_


### public redeem
_(no internal calls)_


### public redeemMax
-> public redeem


### external redeemToDeposit
-> public redeem
-> public deposit


### external stakeVaultToken
-> internal _checkVault
  -> library Errors.ItemNotFound


### external swapToken
_(no internal calls)_


### external swapTokenBalance
_(no internal calls)_


### public withdraw
_(no internal calls)_


### external withdrawToDeposit
-> public withdraw
-> public deposit


### external withdrawVaultToken
-> internal _checkVault
  -> library Errors.ItemNotFound
-> internal _checkRewarder
  -> library Errors.ItemNotFound


---

## AutopilotRouterBase

_File: src/vault/AutopilotRouterBase.sol_

### public approve
-> library LibAdapter._approve


### external claimAutopoolRewards
-> internal _checkVault
  -> library Errors.ItemNotFound
-> internal _checkRewarder
  -> library Errors.ItemNotFound


### public deposit
_(no internal calls)_


### external expiration
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### public mint
_(no internal calls)_


### public multicall
_(no internal calls)_


### public pullToken
_(no internal calls)_


### public redeem
_(no internal calls)_


### external refundETH
_(no internal calls)_


### public selfPermit
_(no internal calls)_


### external stakeVaultToken
-> internal _checkVault
  -> library Errors.ItemNotFound


### public sweepToken
_(no internal calls)_


### public unwrapWETH9
_(no internal calls)_


### public withdraw
_(no internal calls)_


### external withdrawVaultToken
-> internal _checkVault
  -> library Errors.ItemNotFound
-> internal _checkRewarder
  -> library Errors.ItemNotFound


### public wrapWETH9
_(no internal calls)_


---

## AutopoolETH

_File: src/vault/AutopoolETH.sol_

### public DOMAIN_SEPARATOR
_(no internal calls)_


### public addDestinations
-> library AutopoolDestinations.addDestinations


### public allowance
_(no internal calls)_


### public approve
_(no internal calls)_


### public asset
_(no internal calls)_


### public balanceOf
-> library Autopool4626.balanceOf


### public balanceOfActual
_(no internal calls)_


### public convertToAssets
_(no internal calls)_


### public convertToShares
_(no internal calls)_


### public decimals
_(no internal calls)_


### public deposit
-> library Errors.verifyNotZero
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> private _maxDeposit
  -> public convertToAssets
  -> public maxMint
    -> library Autopool4626.maxMint
    -> public paused
  -> public totalSupply
    -> library Autopool4626.totalSupply
-> public convertToShares
-> public totalSupply
  -> library Autopool4626.totalSupply
-> internal _transferAndMint
  -> library Autopool4626.transferAndMint


### public flashRebalance
-> internal _processRebalance
  -> library Errors.InvalidParams
  -> library AutopoolDebt.flashRebalance
  -> library AutopoolDebt.FlashRebalanceParams
-> internal _feeAndProfitHandling
  -> library AutopoolFees.burnUnlockedShares
  -> public totalSupply
    -> library Autopool4626.totalSupply
  -> internal _collectFees
    -> library AutopoolFees.collectFees
  -> library AutopoolFees.calculateProfitLocking
  -> public balanceOfActual
-> library AutopoolDestinations._manageQueuesForDestination
-> internal _updateStrategyNav


### public getAssetBreakdown
_(no internal calls)_


### public getDebtReportingQueue
_(no internal calls)_


### external getDestinationInfo
_(no internal calls)_


### public getDestinations
_(no internal calls)_


### external getFeeSettings
_(no internal calls)_


### external getPastRewarders
_(no internal calls)_


### external getProfitUnlockSettings
_(no internal calls)_


### public getRemovalQueue
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### public getWithdrawalQueue
_(no internal calls)_


### external initialize
-> library Errors.verifyNotEmpty
-> library Errors.verifyNotZero
-> library AutopoolFees.initializeFeeSettings
-> public deposit
  -> library Errors.verifyNotZero
  -> private _totalAssetsTimeChecked
    -> library AutopoolDebt.totalAssetsTimeChecked
  -> private _maxDeposit
    -> public convertToAssets
    -> public maxMint
      -> library Autopool4626.maxMint
      -> public paused
    -> public totalSupply
      -> library Autopool4626.totalSupply
  -> public convertToShares
  -> public totalSupply
    -> library Autopool4626.totalSupply
  -> internal _transferAndMint
    -> library Autopool4626.transferAndMint
-> library AutopoolFees.setProfitUnlockPeriod
  -> library AutopoolFees.setProfitUnlockPeriod


### external isDestinationQueuedForRemoval
_(no internal calls)_


### external isDestinationRegistered
_(no internal calls)_


### external isPastRewarder
_(no internal calls)_


### external isShutdown
_(no internal calls)_


### public maxDeposit
-> private _maxDeposit
  -> public convertToAssets
  -> public maxMint
    -> library Autopool4626.maxMint
    -> public paused
  -> public totalSupply
    -> library Autopool4626.totalSupply
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked


### public maxMint
-> library Autopool4626.maxMint
-> public paused


### public maxRedeem
-> private _maxRedeem
  -> public paused
  -> public balanceOf
    -> library Autopool4626.balanceOf
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked


### public maxWithdraw
-> public balanceOf
  -> library Autopool4626.balanceOf
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> public paused
-> public convertToAssets
-> public totalSupply
  -> library Autopool4626.totalSupply
-> library AutopoolDebt.preview


### public mint
-> public maxMint
  -> library Autopool4626.maxMint
  -> public paused
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> public convertToAssets
-> public totalSupply
  -> library Autopool4626.totalSupply
-> internal _transferAndMint
  -> library Autopool4626.transferAndMint


### public name
_(no internal calls)_


### public nonces
_(no internal calls)_


### public oldestDebtReporting
_(no internal calls)_


### external pause
_(no internal calls)_


### public paused
_(no internal calls)_


### public permit
_(no internal calls)_


### public previewDeposit
-> public convertToShares
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> public totalSupply
  -> library Autopool4626.totalSupply


### public previewMint
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> public convertToAssets
-> public totalSupply
  -> library Autopool4626.totalSupply
-> library Errors.verifyNotZero


### public previewRedeem
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> public convertToAssets
-> public totalSupply
  -> library Autopool4626.totalSupply
-> library AutopoolDebt.preview


### public previewWithdraw
-> library AutopoolDebt.preview
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked


### external recover
-> library Autopool4626.recover


### public redeem
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> private _maxRedeem
  -> public paused
  -> public balanceOf
    -> library Autopool4626.balanceOf
-> public convertToAssets
-> public totalSupply
  -> library Autopool4626.totalSupply
-> library Errors.verifyNotZero
-> library AutopoolDebt.redeem
-> internal _completeWithdrawal
  -> library AutopoolDebt.completeWithdrawal


### public removeDestinations
-> library AutopoolDestinations.removeDestinations


### external setFeeSink
-> library AutopoolFees.setFeeSink


### external setPeriodicFeeBps
-> library AutopoolFees.setPeriodicFeeBps
-> public oldestDebtReporting


### external setPeriodicFeeSink
-> library AutopoolFees.setPeriodicFeeSink


### external setProfitUnlockPeriod
-> library AutopoolFees.setProfitUnlockPeriod


### external setRebalanceFeeHighWaterMarkEnabled
-> library AutopoolFees.setRebalanceFeeHighWaterMarkEnabled


### external setRewarder
-> internal _hasRole
-> library Errors.AccessDenied
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external setStreamingFeeBps
-> library AutopoolFees.setStreamingFeeBps
-> public oldestDebtReporting


### external setSymbolAndDescAfterShutdown
-> library Errors.verifyNotEmpty


### external shutdown
_(no internal calls)_


### external shutdownStatus
_(no internal calls)_


### public symbol
_(no internal calls)_


### public totalAssets
-> library Autopool4626.totalAssets


### public totalSupply
-> library Autopool4626.totalSupply


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external unlockedShares
-> library AutopoolFees.unlockedShares


### external unpause
_(no internal calls)_


### external updateDebtReporting
-> library AutopoolDebt._updateDebtReporting
-> internal _feeAndProfitHandling
  -> library AutopoolFees.burnUnlockedShares
  -> public totalSupply
    -> library Autopool4626.totalSupply
  -> internal _collectFees
    -> library AutopoolFees.collectFees
  -> library AutopoolFees.calculateProfitLocking
  -> public balanceOfActual
-> internal _updateStrategyNav


### public withdraw
-> library Errors.verifyNotZero
-> library AutopoolDebt.withdraw
-> private _totalAssetsTimeChecked
  -> library AutopoolDebt.totalAssetsTimeChecked
-> internal _completeWithdrawal
  -> library AutopoolDebt.completeWithdrawal


---

## AutopoolETHStrategy

_File: src/strategy/AutopoolETHStrategy.sol_

### external expiredRewardTolerance
_(no internal calls)_


### external getDestinationSummaryStats
-> private _getInOutTokenPriceInEth
-> library SummaryStats.getDestinationSummaryStats


### public getHooks
_(no internal calls)_


### external getRebalanceOutSummaryStats
-> internal validateRebalanceParams
  -> library Errors.verifyNotZero
  -> private ensureDestinationRegistered
-> library SummaryStats.verifyLSTPriceGap
-> internal _getRebalanceOutSummaryStats
  -> private _getInOutTokenPriceInEth
  -> library SummaryStats.getDestinationSummaryStats
    -> private _getInOutTokenPriceInEth
    -> library SummaryStats.getDestinationSummaryStats


### external getSystemRegistry
_(no internal calls)_


### external initialize
-> internal _initialize
  -> library Errors.verifyNotZero


### external navUpdate
-> internal clearExpiredPause
  -> internal expiredPauseState
    -> public paused
-> public paused


### public paused
_(no internal calls)_


### external rebalanceSuccessfullyExecuted
-> internal clearExpiredPause
  -> internal expiredPauseState
    -> public paused
-> public swapCostOffsetPeriodInDays
  -> internal expiredPauseState
    -> public paused
-> internal tightenSwapCostOffset
  -> public swapCostOffsetPeriodInDays
    -> internal expiredPauseState
      -> public paused


### external setDustPositionPortions
_(no internal calls)_


### external setIdleThresholds
_(no internal calls)_


### external setLstPriceGapTolerance
_(no internal calls)_


### public swapCostOffsetPeriodInDays
-> internal expiredPauseState
  -> public paused


### external verifyRebalance
-> library SummaryStats.getRebalanceValueStats
-> internal verifyRebalanceToIdle
  -> internal verifyIdleUpOperation
    -> internal ensureNotStaleData
  -> internal verifyCleanUpOperation
    -> internal ensureNotStaleData
  -> internal getDestinationTrimAmount
    -> internal getDiscountAboveThreshold
  -> internal verifyTrimOperation
    -> internal ensureNotStaleData
-> internal ensureNotPaused
  -> public paused
-> internal getRebalanceInSummaryStats
  -> private _getInOutTokenPriceInEth
  -> library SummaryStats.getDestinationSummaryStats
    -> private _getInOutTokenPriceInEth
    -> library SummaryStats.getDestinationSummaryStats
-> public swapCostOffsetPeriodInDays
  -> internal expiredPauseState
    -> public paused
-> library StrategyUtils.convertUintToInt


---

## AutopoolFactory

_File: src/vault/AutopoolFactory.sol_

### external addStrategyTemplate
-> library Errors.verifySystemsMatch
-> library Errors.ItemExists


### external createVault
-> library Errors.verifyNotZero
-> library LibAdapter._approve


### public getStrategyTemplates
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### public isStrategyTemplate
_(no internal calls)_


### external removeStrategyTemplate
-> library Errors.ItemNotFound


### external setDefaultRewardBlockDuration
-> private _setDefaultRewardBlockDuration


### external setDefaultRewardRatio
-> private _setDefaultRewardRatio


---

## AutopoolMainRewarder

_File: src/rewarders/AutopoolMainRewarder.sol_

### external addExtraReward
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### public balanceOf
_(no internal calls)_


### public canTokenBeRecovered
_(no internal calls)_


### external extraRewards
_(no internal calls)_


### external extraRewardsLength
_(no internal calls)_


### external getExtraRewarder
_(no internal calls)_


### public getReward
-> library Errors.AccessDenied
-> internal _getReward
  -> internal _processRewards
    -> internal _getReward


### public stake
-> internal _stake


### public totalSupply
_(no internal calls)_


### public withdraw
-> library Errors.AccessDenied
-> internal _withdraw
  -> internal _processRewards
    -> internal _getReward
      -> internal _processRewards


---

## AutopoolRegistry

_File: src/vault/AutopoolRegistry.sol_

### external addVault
-> library Errors.verifyNotZero


### external getSystemRegistry
_(no internal calls)_


### external isVault
_(no internal calls)_


### external listVaults
_(no internal calls)_


### external listVaultsForAsset
_(no internal calls)_


### external listVaultsForType
_(no internal calls)_


### external removeVault
-> library Errors.verifyNotZero


---

## BalancerAuraDestinationVault

_File: src/vault/BalancerAuraDestinationVault.sol_

### public balanceOfUnderlyingDebt
-> public internalDebtBalance
-> public externalDebtBalance


### external baseAsset
_(no internal calls)_


### external collectRewards
-> internal _collectRewards
  -> library AuraRewards.claimRewards


### external debtValue
-> private _debtValue
  -> public getPool


### public decimals
_(no internal calls)_


### external depositUnderlying
-> library Errors.verifyNotZero
-> internal _onDeposit
  -> library BalancerUtilities._getPoolTokens
  -> library AuraStaking.depositAndStake


### external exchangeName
_(no internal calls)_


### external executeExtension
-> library Errors.verifyNotZero
-> public externalDebtBalance
-> public internalDebtBalance
-> public externalQueriedBalance
-> public internalQueriedBalance


### public externalDebtBalance
_(no internal calls)_


### public externalQueriedBalance
_(no internal calls)_


### external getMarketplaceRewards
_(no internal calls)_


### public getPool
_(no internal calls)_


### external getRangePricesLP
-> public getPool


### external getStats
_(no internal calls)_


### external getUnderlyerCeilingPrice
-> public getPool


### external getUnderlyerFloorPrice
-> public getPool


### external getValidatedSafePrice
-> public getPool


### external getValidatedSpotPrice
-> public getPool


### public initialize
-> library Errors.verifyNotZero
-> library BalancerUtilities.isComposablePool
-> library BalancerUtilities._getPoolTokens
-> internal _addTrackedToken


### public internalDebtBalance
_(no internal calls)_


### public internalQueriedBalance
_(no internal calls)_


### external isShutdown
_(no internal calls)_


### public isTrackedToken
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public name
_(no internal calls)_


### external poolDealInEth
_(no internal calls)_


### external poolType
_(no internal calls)_


### external recover
-> public isTrackedToken


### external recoverUnderlying
-> library Errors.verifyNotZero
-> public externalQueriedBalance
-> public externalDebtBalance
-> public internalQueriedBalance
-> public internalDebtBalance
-> internal _ensureLocalUnderlyingBalance
  -> library AuraStaking.withdrawStake


### external rewarder
_(no internal calls)_


### external setExtension
_(no internal calls)_


### external setIncentiveCalculator
-> internal _validateCalculator


### external setMessage
_(no internal calls)_


### external setRecoupMaxCredit
-> private _setRecoupMaxCredit
  -> library Errors.InvalidParam


### external shutdown
_(no internal calls)_


### external shutdownStatus
_(no internal calls)_


### public symbol
_(no internal calls)_


### public trackedTokens
_(no internal calls)_


### external underlying
_(no internal calls)_


### external underlyingReserves
-> library BalancerUtilities._getPoolTokens
-> library BalancerUtilities._convertERC20sToAddresses


### external underlyingTokens
-> library BalancerUtilities._convertERC20sToAddresses


### external underlyingTotalSupply
_(no internal calls)_


### external withdrawBaseAsset
-> internal _withdrawBaseAsset
  -> library Errors.verifyNotZero
  -> internal _ensureLocalUnderlyingBalance
    -> library AuraStaking.withdrawStake
  -> internal _burnUnderlyer
    -> library BalancerUtilities._convertERC20sToAddresses
    -> library BalancerBeethovenAdapter.removeLiquidity
  -> library Errors.verifyArrayLengths
  -> library LibAdapter._approve


### external withdrawUnderlying
-> library Errors.verifyNotZero
-> internal _ensureLocalUnderlyingBalance
  -> library AuraStaking.withdrawStake


---

## BalancerBaseOracle

_File: src/oracles/providers/base/BalancerBaseOracle.sol_

### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor
  -> external_callback IVault.BatchSwapStep
  -> external_callback IVault.FundManagement


### public getSpotPrice
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor
  -> external_callback IVault.BatchSwapStep
  -> external_callback IVault.FundManagement


### external getSystemRegistry
_(no internal calls)_


---

## BalancerComposableStablePoolCalculator

_File: src/stats/calculators/BalancerComposableStablePoolCalculator.sol_

### external current
-> internal getPoolTokens
  -> library BalancerUtilities._getComposablePoolTokensSkipBpt
-> internal calculateReserveInEthByIndex
-> internal adjustBaseAprForBalancerYieldProtocolFee


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> internal getPoolTokens
  -> library BalancerUtilities._getComposablePoolTokensSkipBpt
-> library Stats.generateBalancerPoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> internal getVirtualPrice
-> internal _isExemptFromYieldProtocolFee


### public shouldSnapshot
_(no internal calls)_


---

## BalancerDestinationVault

_File: src/vault/BalancerDestinationVault.sol_

### public balanceOfUnderlyingDebt
-> public internalDebtBalance
-> public externalDebtBalance


### external baseAsset
_(no internal calls)_


### external collectRewards
-> internal _collectRewards


### external debtValue
-> private _debtValue
  -> public getPool


### public decimals
_(no internal calls)_


### external depositUnderlying
-> library Errors.verifyNotZero
-> internal _onDeposit


### external exchangeName
_(no internal calls)_


### external executeExtension
-> library Errors.verifyNotZero
-> public externalDebtBalance
-> public internalDebtBalance
-> public externalQueriedBalance
-> public internalQueriedBalance


### public externalDebtBalance
_(no internal calls)_


### public externalQueriedBalance
_(no internal calls)_


### external getMarketplaceRewards
_(no internal calls)_


### public getPool
_(no internal calls)_


### external getRangePricesLP
-> public getPool


### external getStats
_(no internal calls)_


### external getUnderlyerCeilingPrice
-> public getPool


### external getUnderlyerFloorPrice
-> public getPool


### external getValidatedSafePrice
-> public getPool


### external getValidatedSpotPrice
-> public getPool


### public initialize
-> library Errors.verifyNotZero
-> library BalancerUtilities.isComposablePool
-> library BalancerUtilities._getPoolTokens
-> library BalancerUtilities._convertERC20sToAddresses
-> internal _addTrackedToken


### public internalDebtBalance
_(no internal calls)_


### public internalQueriedBalance
_(no internal calls)_


### external isShutdown
_(no internal calls)_


### public isTrackedToken
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public name
_(no internal calls)_


### external poolDealInEth
_(no internal calls)_


### external poolType
_(no internal calls)_


### external recover
-> public isTrackedToken


### external recoverUnderlying
-> library Errors.verifyNotZero
-> public externalQueriedBalance
-> public externalDebtBalance
-> public internalQueriedBalance
-> public internalDebtBalance
-> internal _ensureLocalUnderlyingBalance


### external rewarder
_(no internal calls)_


### external setExtension
_(no internal calls)_


### external setIncentiveCalculator
-> internal _validateCalculator


### external setMessage
_(no internal calls)_


### external setRecoupMaxCredit
-> private _setRecoupMaxCredit
  -> library Errors.InvalidParam


### external shutdown
_(no internal calls)_


### external shutdownStatus
_(no internal calls)_


### public symbol
_(no internal calls)_


### public trackedTokens
_(no internal calls)_


### external underlying
_(no internal calls)_


### external underlyingReserves
-> library BalancerUtilities._getPoolTokens
-> library BalancerUtilities._convertERC20sToAddresses


### external underlyingTokens
-> library BalancerUtilities._getComposablePoolTokensSkipBpt
-> library BalancerUtilities._convertERC20sToAddresses


### external underlyingTotalSupply
_(no internal calls)_


### external withdrawBaseAsset
-> internal _withdrawBaseAsset
  -> library Errors.verifyNotZero
  -> internal _ensureLocalUnderlyingBalance
  -> internal _burnUnderlyer
    -> library BalancerBeethovenAdapter.removeLiquidity
  -> library Errors.verifyArrayLengths
  -> library LibAdapter._approve


### external withdrawUnderlying
-> library Errors.verifyNotZero
-> internal _ensureLocalUnderlyingBalance


---

## BalancerGyroPoolCalculator

_File: src/stats/calculators/BalancerGyroPoolCalculator.sol_

### external current
-> internal getPoolTokens
  -> library BalancerUtilities._getPoolTokens
-> internal calculateReserveInEthByIndex
  -> library Stats.getFilteredValue
-> internal adjustBaseAprForBalancerYieldProtocolFee


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> internal getPoolTokens
  -> library BalancerUtilities._getPoolTokens
-> library Stats.generateBalancerPoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> internal getVirtualPrice
-> internal _isExemptFromYieldProtocolFee


### public shouldSnapshot
_(no internal calls)_


---

## BalancerGyroscopeDestinationVault

_File: src/vault/BalancerGyroscopeDestinationVault.sol_

### external exchangeName
_(no internal calls)_


### public externalDebtBalance
_(no internal calls)_


### public externalQueriedBalance
_(no internal calls)_


### public getPool
_(no internal calls)_


### public initialize
-> library Errors.verifyNotZero
-> library BalancerUtilities.isComposablePool
-> library BalancerUtilities._getPoolTokens


### public internalDebtBalance
_(no internal calls)_


### external poolDealInEth
_(no internal calls)_


### external poolType
_(no internal calls)_


### external underlyingReserves
-> library BalancerUtilities._getPoolTokens
-> library BalancerUtilities._convertERC20sToAddresses


### external underlyingTokens
-> library BalancerUtilities._convertERC20sToAddresses


### external underlyingTotalSupply
_(no internal calls)_


---

## BalancerGyroscopeEthOracle

_File: src/oracles/providers/BalancerGyroscopeEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> internal getTotalSupply_
-> internal getPoolTokens_
  -> library BalancerUtilities._getPoolTokens
-> internal _getSpotPrice
  -> library Errors.verifyArrayLengths


### public getSpotPrice
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Errors.verifyArrayLengths


---

## BalancerLPComposableStableEthOracle

_File: src/oracles/providers/BalancerLPComposableStableEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> internal getTotalSupply_
-> internal getPoolTokens_
  -> library BalancerUtilities._getComposablePoolTokensSkipBpt
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor
  -> external_callback IVault.BatchSwapStep
  -> external_callback IVault.FundManagement


### public getSpotPrice
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor
  -> external_callback IVault.BatchSwapStep
  -> external_callback IVault.FundManagement


---

## BalancerLPMetaStableEthOracle

_File: src/oracles/providers/BalancerLPMetaStableEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> internal getTotalSupply_
-> internal getPoolTokens_
  -> library BalancerUtilities._getPoolTokens
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor
  -> external_callback IVault.BatchSwapStep
  -> external_callback IVault.FundManagement


### public getSpotPrice
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor
  -> external_callback IVault.BatchSwapStep
  -> external_callback IVault.FundManagement


---

## BalancerMetaStablePoolCalculator

_File: src/stats/calculators/BalancerMetaStablePoolCalculator.sol_

### external current
-> internal getPoolTokens
  -> library BalancerUtilities._getPoolTokens
-> internal calculateReserveInEthByIndex
-> internal adjustBaseAprForBalancerYieldProtocolFee


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> internal getPoolTokens
  -> library BalancerUtilities._getPoolTokens
-> library Stats.generateBalancerPoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> internal getVirtualPrice
  -> library BalancerUtilities._getMetaStableVirtualPrice
-> internal _isExemptFromYieldProtocolFee


### public shouldSnapshot
_(no internal calls)_


---

## BalancerStablePoolCalculatorBase

_File: src/stats/calculators/base/BalancerStablePoolCalculatorBase.sol_

### external current
-> internal calculateReserveInEthByIndex
-> internal adjustBaseAprForBalancerYieldProtocolFee


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.generateBalancerPoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> internal _isExemptFromYieldProtocolFee


### public shouldSnapshot
_(no internal calls)_


### external snapshot
-> public shouldSnapshot
-> internal _snapshot
  -> internal calculateReserveInEthByIndex
  -> library Stats.calculateAnnualizedChangeMinZero
  -> internal adjustBaseAprForBalancerYieldProtocolFee
  -> library Stats.getFilteredValue


---

## BalancerV2Swap

_File: src/swapper/adapters/BalancerV2Swap.sol_

### external swap
-> external_callback IVault.SingleSwap
-> external_callback IVault.FundManagement
-> library LibAdapter._approve


### external validate
_(no internal calls)_


---

## BaseAggregatorV3OracleInformation

_File: src/oracles/providers/base/BaseAggregatorV3OracleInformation.sol_

### external getOracleInfo
_(no internal calls)_


### public registerOracle
-> library Errors.verifyNotZero
-> library Errors.AlreadyRegistered


### public removeOracleRegistration
-> library Errors.verifyNotZero
-> library Errors.MustBeSet


---

## BaseAsyncSwapper

_File: src/liquidation/BaseAsyncSwapper.sol_

### public swap
-> library LibAdapter._approve


---

## BaseOracleDenominations

_File: src/oracles/providers/base/BaseOracleDenominations.sol_

### external getSystemRegistry
_(no internal calls)_


---

## BaseStatsCalculator

_File: src/stats/calculators/base/BaseStatsCalculator.sol_

### external getSystemRegistry
_(no internal calls)_


### external snapshot
_(no internal calls)_


---

## BridgedLSTCalculator

_File: src/stats/calculators/bridged/BridgedLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Errors.verifyNotZero
-> library Stats.generateRawTokenIdentifier
-> internal _setEthPerTokenStore
  -> library Errors.verifyNotZero


### external onMessageReceive
-> internal _onMessageReceive
  -> internal _snapshotOnMessageReceive
    -> internal _snapshot
      -> public calculateEthPerToken
      -> internal _timeForAprSnapshot
      -> library Stats.calculateAnnualizedChangeMinZero
      -> library Stats.getFilteredValue
      -> library MessageTypes.LSTDestinationInfo
      -> internal _timeForDiscountSnapshot
      -> internal updateDiscountHistory
        -> private calculateDiscount
          -> public usePriceAsDiscount
      -> internal updateDiscountTimestampByPercent
    -> internal updateDiscountHistory
      -> private calculateDiscount
        -> public usePriceAsDiscount
    -> internal updateDiscountTimestampByPercent
  -> library Errors.UnsupportedMessage


### external setDestinationMessageSend
-> library Errors.NotSupported


### external setEthPerTokenStore
-> internal _setEthPerTokenStore
  -> library Errors.verifyNotZero


### public shouldSnapshot
_(no internal calls)_


### public usePriceAsDiscount
_(no internal calls)_


---

## CCIPReceiver

_File: src/external/chainlink/ccip/CCIPReceiver.sol_

### external ccipReceive
_(no internal calls)_


### public getRouter
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## CbethLSTCalculator

_File: src/stats/calculators/CbethLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## ChainlinkEthPerTokenSenderUpkeep

_File: src/stats/calculators/bridged/ChainlinkEthPerTokenSenderUpkeep.sol_

### external checkUpkeep
_(no internal calls)_


### external performUpkeep
_(no internal calls)_


---

## ChainlinkIncentivePricesUpkeepV3

_File: src/stats/ChainlinkIncentivePricesUpkeepV3.sol_

### external checkUpkeep
_(no internal calls)_


### external performUpkeep
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setMaxPerCheck
-> library Errors.verifyNotZero


---

## ChainlinkOracle

_File: src/oracles/providers/ChainlinkOracle.sol_

### external getDescription
_(no internal calls)_


### external getOracleInfo
_(no internal calls)_


### external getPriceInEth
-> internal _getOracleInfo
  -> library Errors.verifyNotZero
-> internal _validateOffchainAggregator
  -> library Errors.InvalidDataReturned
-> external_callback BaseAggregatorV3OracleInformation._getPriceInEth
  -> library Errors.InvalidDataReturned


### public registerOracle
-> library Errors.verifyNotZero
-> library Errors.AlreadyRegistered


### public removeOracleRegistration
-> library Errors.verifyNotZero
-> library Errors.MustBeSet


---

## ChainlinkStatsUpkeepV4

_File: src/stats/ChainlinkStatsUpkeepV4.sol_

### external checkUpkeep
_(no internal calls)_


### external performUpkeep
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setMaxPerCheck
-> library Errors.verifyNotZero


---

## ConvexCalculator

_File: src/stats/calculators/ConvexCalculator.sol_

### external current
-> internal _computeTotalAPR
  -> internal _getRewardPoolMetrics
  -> internal _shouldSnapshot
    -> internal _snapshotStatus
    -> library Stats.differsByMoreThanFivePercent
  -> internal _snapshotRewarder
    -> internal _snapshotStatus
  -> internal _getLpTokenPriceInEth
    -> library Errors.UnsafePrice
  -> internal _computeAPR
    -> internal _getIncentivePrice
  -> public getPlatformTokenMintAmount
    -> library ConvexRewards.getCVXMintAmount
  -> public resolveRewardToken
-> library Stats.decayCredits
-> internal _getStakingIncentiveStats
  -> public resolveRewardToken
-> public getPlatformTokenMintAmount
  -> library ConvexRewards.getCVXMintAmount


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public getPlatformTokenMintAmount
-> library ConvexRewards.getCVXMintAmount


### public initialize
-> library Errors.InvalidParam


### public resolveRewardToken
_(no internal calls)_


### public shouldSnapshot
-> internal _getRewardPoolMetrics
-> internal _shouldSnapshot
  -> internal _snapshotStatus
  -> library Stats.differsByMoreThanFivePercent


---

## CurveConvexDestinationVault

_File: src/vault/CurveConvexDestinationVault.sol_

### public balanceOfUnderlyingDebt
-> public internalDebtBalance
-> public externalDebtBalance


### external baseAsset
_(no internal calls)_


### external collectRewards
-> internal _collectRewards
  -> library ConvexRewards.claimRewards


### external debtValue
-> private _debtValue
  -> public getPool


### public decimals
_(no internal calls)_


### external depositUnderlying
-> library Errors.verifyNotZero
-> internal _onDeposit
  -> library ConvexStaking.depositAndStake


### external exchangeName
_(no internal calls)_


### external executeExtension
-> library Errors.verifyNotZero
-> public externalDebtBalance
-> public internalDebtBalance
-> public externalQueriedBalance
-> public internalQueriedBalance


### public externalDebtBalance
_(no internal calls)_


### public externalQueriedBalance
_(no internal calls)_


### external getMarketplaceRewards
_(no internal calls)_


### public getPool
_(no internal calls)_


### external getRangePricesLP
-> public getPool


### external getStats
_(no internal calls)_


### external getUnderlyerCeilingPrice
-> public getPool


### external getUnderlyerFloorPrice
-> public getPool


### external getValidatedSafePrice
-> public getPool


### external getValidatedSpotPrice
-> public getPool


### public initialize
-> library Errors.verifyNotZero
-> library Errors.InvalidParam
-> internal _addTrackedToken


### public internalDebtBalance
_(no internal calls)_


### public internalQueriedBalance
_(no internal calls)_


### external isShutdown
_(no internal calls)_


### public isTrackedToken
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public name
_(no internal calls)_


### external poolDealInEth
_(no internal calls)_


### external poolType
_(no internal calls)_


### external recover
-> public isTrackedToken


### external recoverUnderlying
-> library Errors.verifyNotZero
-> public externalQueriedBalance
-> public externalDebtBalance
-> public internalQueriedBalance
-> public internalDebtBalance
-> internal _ensureLocalUnderlyingBalance
  -> library ConvexStaking.withdrawStake


### external rewarder
_(no internal calls)_


### external setExtension
_(no internal calls)_


### external setIncentiveCalculator
-> internal _validateCalculator


### external setMessage
_(no internal calls)_


### external setRecoupMaxCredit
-> private _setRecoupMaxCredit
  -> library Errors.InvalidParam


### external shutdown
_(no internal calls)_


### external shutdownStatus
_(no internal calls)_


### public symbol
_(no internal calls)_


### public trackedTokens
_(no internal calls)_


### external underlying
_(no internal calls)_


### external underlyingReserves
_(no internal calls)_


### external underlyingTokens
_(no internal calls)_


### external underlyingTotalSupply
_(no internal calls)_


### external withdrawBaseAsset
-> internal _withdrawBaseAsset
  -> library Errors.verifyNotZero
  -> internal _ensureLocalUnderlyingBalance
    -> library ConvexStaking.withdrawStake
  -> internal _burnUnderlyer
    -> library CurveV2FactoryCryptoAdapter.removeLiquidity
  -> library Errors.verifyArrayLengths
  -> library LibAdapter._approve


### external withdrawUnderlying
-> library Errors.verifyNotZero
-> internal _ensureLocalUnderlyingBalance
  -> library ConvexStaking.withdrawStake


---

## CurveNGConvexDestinationVault

_File: src/vault/CurveNGConvexDestinationVault.sol_

### external exchangeName
_(no internal calls)_


### public externalDebtBalance
_(no internal calls)_


### public externalQueriedBalance
_(no internal calls)_


### public getPool
_(no internal calls)_


### public initialize
-> library Errors.verifyNotZero
-> library Errors.InvalidParam


### public internalDebtBalance
_(no internal calls)_


### external poolDealInEth
_(no internal calls)_


### external poolType
_(no internal calls)_


### external underlyingReserves
_(no internal calls)_


### external underlyingTokens
_(no internal calls)_


### external underlyingTotalSupply
_(no internal calls)_


---

## CurvePoolNoRebasingCalculatorBase

_File: src/stats/calculators/base/CurvePoolNoRebasingCalculatorBase.sol_

### external current
-> library CurveUtils.getDecimals


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.generateCurvePoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> library CurveUtils.getDecimals


### public shouldSnapshot
_(no internal calls)_


### external snapshot
-> public shouldSnapshot
-> internal _snapshot
  -> library Stats.calculateAnnualizedChangeMinZero
  -> library Stats.getFilteredValue


---

## CurvePoolRebasingCalculatorBase

_File: src/stats/calculators/base/CurvePoolRebasingCalculatorBase.sol_

### external current
-> internal calculateReserveInEthByIndex
  -> library CurveUtils.getDecimals


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.generateCurvePoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> library CurveUtils.getDecimals


### public shouldSnapshot
_(no internal calls)_


### external snapshot
-> public shouldSnapshot
-> internal _snapshot
  -> internal calculateReserveInEthByIndex
    -> library CurveUtils.getDecimals
  -> library Stats.calculateAnnualizedChangeMinZero
  -> library Stats.getFilteredValue


---

## CurveResolverMainnet

_File: src/utils/CurveResolverMainnet.sol_

### public getLpToken
_(no internal calls)_


### external getReservesInfo
-> library Errors.verifyNotZero


### public resolve
-> library Errors.verifyNotZero
-> private _isStableSwap


### external resolveWithLpToken
-> public resolve
  -> library Errors.verifyNotZero
  -> private _isStableSwap
-> public getLpToken


---

## CurveV1PoolNoRebasingStatsCalculator

_File: src/stats/calculators/CurveV1PoolNoRebasingStatsCalculator.sol_

### external current
-> library CurveUtils.getDecimals


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.generateCurvePoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> library CurveUtils.getDecimals
-> internal getVirtualPrice


### public shouldSnapshot
_(no internal calls)_


---

## CurveV1PoolRebasingLockedStatsCalculator

_File: src/stats/calculators/CurveV1PoolRebasingLockedStatsCalculator.sol_

### external current
-> internal calculateReserveInEthByIndex
  -> library CurveUtils.getDecimals


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.generateCurvePoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> library CurveUtils.getDecimals
-> internal getVirtualPrice


### public shouldSnapshot
_(no internal calls)_


---

## CurveV1PoolRebasingStatsCalculator

_File: src/stats/calculators/CurveV1PoolRebasingStatsCalculator.sol_

### external current
-> internal calculateReserveInEthByIndex
  -> library CurveUtils.getDecimals


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.generateCurvePoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> library CurveUtils.getDecimals
-> internal getVirtualPrice


### public shouldSnapshot
_(no internal calls)_


---

## CurveV1StableEthOracle

_File: src/oracles/providers/CurveV1StableEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getLpTokenToUnderlying
_(no internal calls)_


### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> private _checkEth
-> internal _getSpotPrice
  -> private _checkEth
  -> library Utilities.getScaleDownFactor


### public getSpotPrice
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> private _checkEth
  -> library Utilities.getScaleDownFactor


### external getSystemRegistry
_(no internal calls)_


### external registerPool
-> library Errors.verifyNotZero
-> library Errors.AlreadyRegistered


### external unregister
-> library Errors.verifyNotZero


---

## CurveV1StableSwap

_File: src/swapper/adapters/CurveV1StableSwap.sol_

### external swap
-> library LibAdapter._approve


### external validate
-> internal _int128ToUint256
-> internal isTokenMatch


---

## CurveV2CryptoEthOracle

_File: src/oracles/providers/CurveV2CryptoEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor


### public getSpotPrice
-> library Errors.verifyNotZero
-> internal _getSpotPrice
  -> library Utilities.getScaleDownFactor


### external getSystemRegistry
_(no internal calls)_


### external registerPool
-> library Errors.verifyNotZero
-> library Errors.AlreadyRegistered


### external unregister
-> library Errors.verifyNotZero


---

## CurveV2PoolNoRebasingStatsCalculator

_File: src/stats/calculators/CurveV2PoolNoRebasingStatsCalculator.sol_

### external current
-> library CurveUtils.getDecimals


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.generateCurvePoolIdentifier
-> library Stats.CalculatorAssetMismatch
-> library CurveUtils.getDecimals
-> internal getVirtualPrice


### public shouldSnapshot
_(no internal calls)_


---

## CurveV2Swap

_File: src/swapper/adapters/CurveV2Swap.sol_

### external swap
-> library LibAdapter._approve


### external validate
_(no internal calls)_


---

## CustomSetOracle

_File: src/oracles/providers/CustomSetOracle.sol_

### external getDescription
_(no internal calls)_


### external getPriceInEth
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external isRegistered
_(no internal calls)_


### external registerTokens
-> private _registerTokens
  -> library Errors.verifyNotZero
  -> library Errors.verifyArrayLengths


### external setMaxAge
-> private _setMaxAge
  -> library Errors.verifyNotZero


### external setPrices
-> library Errors.verifyNotZero
-> library Errors.verifyArrayLengths


### external unregisterTokens
-> library Errors.verifyNotZero


### external updateTokenMaxAges
-> private _registerTokens
  -> library Errors.verifyNotZero
  -> library Errors.verifyArrayLengths


---

## DestinationRegistry

_File: src/destinations/DestinationRegistry.sol_

### external addToWhitelist
_(no internal calls)_


### public getAdapter
-> library Errors.verifyNotZero


### external getSystemRegistry
_(no internal calls)_


### public isWhitelistedDestination
_(no internal calls)_


### public register
-> library Errors.verifyArrayLengths
-> public isWhitelistedDestination
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### external removeFromWhitelist
-> library Errors.ItemNotFound


### public replace
-> library Errors.verifyArrayLengths
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### public unregister
-> library Errors.verifyNotZero


---

## DestinationVault

_File: src/vault/DestinationVault.sol_

### public balanceOfUnderlyingDebt
_(no internal calls)_


### external baseAsset
_(no internal calls)_


### external collectRewards
_(no internal calls)_


### external debtValue
-> private _debtValue


### public decimals
_(no internal calls)_


### external depositUnderlying
-> library Errors.verifyNotZero


### external executeExtension
-> library Errors.verifyNotZero
-> public internalQueriedBalance


### external getMarketplaceRewards
_(no internal calls)_


### external getRangePricesLP
_(no internal calls)_


### external getStats
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external getUnderlyerCeilingPrice
_(no internal calls)_


### external getUnderlyerFloorPrice
_(no internal calls)_


### external getValidatedSafePrice
_(no internal calls)_


### external getValidatedSpotPrice
_(no internal calls)_


### public initialize
-> library Errors.verifyNotZero
-> internal _addTrackedToken
-> private _setRecoupMaxCredit
  -> library Errors.InvalidParam


### public internalQueriedBalance
_(no internal calls)_


### external isShutdown
_(no internal calls)_


### public isTrackedToken
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public name
_(no internal calls)_


### external recover
-> public isTrackedToken


### external recoverUnderlying
-> library Errors.verifyNotZero
-> public internalQueriedBalance


### external rewarder
_(no internal calls)_


### external setExtension
_(no internal calls)_


### external setIncentiveCalculator
_(no internal calls)_


### external setMessage
_(no internal calls)_


### external setRecoupMaxCredit
-> private _setRecoupMaxCredit
  -> library Errors.InvalidParam


### external shutdown
_(no internal calls)_


### external shutdownStatus
_(no internal calls)_


### public symbol
_(no internal calls)_


### public trackedTokens
_(no internal calls)_


### external underlying
_(no internal calls)_


### external withdrawBaseAsset
-> internal _withdrawBaseAsset
  -> library Errors.verifyNotZero
  -> library Errors.verifyArrayLengths
  -> library LibAdapter._approve


### external withdrawUnderlying
-> library Errors.verifyNotZero


---

## DestinationVaultFactory

_File: src/vault/DestinationVaultFactory.sol_

### external create
-> library Errors.verifyNotZero


### external getSystemRegistry
_(no internal calls)_


### public setDefaultRewardBlockDuration
-> private _setDefaultRewardBlockDuration


### public setDefaultRewardRatio
-> private _setDefaultRewardRatio


---

## DestinationVaultMainRewarder

_File: src/rewarders/DestinationVaultMainRewarder.sol_

### external addExtraReward
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### public balanceOf
_(no internal calls)_


### public canTokenBeRecovered
_(no internal calls)_


### external extraRewards
_(no internal calls)_


### external extraRewardsLength
_(no internal calls)_


### external getExtraRewarder
_(no internal calls)_


### public getReward
-> library Errors.AccessDenied
-> internal _getReward
  -> internal _processRewards
    -> internal _getReward


### public stake
-> internal _stake


### public totalSupply
_(no internal calls)_


### public withdraw
-> internal _withdraw
  -> internal _processRewards
    -> internal _getReward
      -> internal _processRewards


---

## DestinationVaultRegistry

_File: src/vault/DestinationVaultRegistry.sol_

### external getSystemRegistry
_(no internal calls)_


### external isRegistered
_(no internal calls)_


### external listVaults
_(no internal calls)_


### external register
-> library Errors.verifyNotZero


### external setVaultFactory
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### external verifyIsRegistered
-> library Errors.NotRegistered


---

## ERC4626RateProvider

_File: src/external/balancer/ERC4626RateProvider.sol_

### external getRate
_(no internal calls)_


---

## ETHxLSTCalculator

_File: src/stats/calculators/ETHxLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## EethLSTCalculator

_File: src/stats/calculators/EethLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## EethOracle

_File: src/oracles/providers/EethOracle.sol_

### external getDescription
_(no internal calls)_


### external getPriceInEth
-> library Errors.InvalidToken


### external getSystemRegistry
_(no internal calls)_


---

## EthPeggedOracle

_File: src/oracles/providers/EthPeggedOracle.sol_

### external getDescription
_(no internal calls)_


### external getPriceInEth
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


---

## EthPerTokenSender

_File: src/stats/calculators/bridged/EthPerTokenSender.sol_

### public encodeMessage
-> library MessageTypes.LstBackingMessage


### external execute
-> library Errors.verifyNotZero
-> internal _shouldSend
-> public encodeMessage
  -> library MessageTypes.LstBackingMessage


### external getCalculators
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external registerCalculators
-> library Errors.verifyNotZero
-> library Errors.AlreadyRegistered


### external setHeartbeat
-> internal _setHeartbeat
  -> library Errors.verifyNotZero
  -> library Errors.InvalidParam


### external shouldSend
-> internal _validateSkipTake
  -> library Errors.InvalidParam
-> internal _shouldSend


### external unregisterCalculators
-> library Errors.verifyNotZero
-> library Errors.NotRegistered


---

## EthPerTokenStore

_File: src/stats/calculators/bridged/EthPerTokenStore.sol_

### external getEthPerToken
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external onMessageReceive
-> internal _onMessageReceive
  -> internal _trackPerTokenOnMessageReceive
  -> library Errors.UnsupportedMessage


### external registerToken
-> library Errors.verifyNotZero
-> library Errors.AlreadyRegistered


### external setMaxAgeSeconds
-> library Errors.verifyNotZero
-> library Errors.InvalidParam


### external unregisterToken
-> library Errors.NotRegistered


---

## ExtraRewarder

_File: src/rewarders/ExtraRewarder.sol_

### external addToWhitelist
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### public balanceOf
_(no internal calls)_


### public canTokenBeRecovered
_(no internal calls)_


### public earned
-> public balanceOf
-> public rewardPerToken
  -> public totalSupply
  -> public lastBlockRewardApplicable


### external getReward
-> external getReward


### external isWhitelisted
_(no internal calls)_


### public lastBlockRewardApplicable
_(no internal calls)_


### external queueNewRewards
-> internal notifyRewardAmount
  -> public totalSupply
  -> internal _updateReward
    -> public rewardPerToken
      -> public totalSupply
      -> public lastBlockRewardApplicable
    -> public lastBlockRewardApplicable
    -> public earned
      -> public balanceOf
      -> public rewardPerToken
        -> public totalSupply
        -> public lastBlockRewardApplicable
  -> library Errors.ZeroAmount


### external recover
-> library Errors.verifyNotZero
-> library Errors.InvalidAddress
-> public canTokenBeRecovered
-> library Errors.AssetNotAllowed


### external removeFromWhitelist
-> library Errors.ItemNotFound


### public rewardPerToken
-> public totalSupply
-> public lastBlockRewardApplicable


### external setTokeLockDuration
-> library Errors.verifyNotZero
-> external_callback IAccToke.StakingDurationTooShort


### external stake
-> internal _updateReward
  -> public rewardPerToken
    -> public totalSupply
    -> public lastBlockRewardApplicable
  -> public lastBlockRewardApplicable
  -> public earned
    -> public balanceOf
    -> public rewardPerToken
      -> public totalSupply
      -> public lastBlockRewardApplicable
-> internal _stakeAbstractRewarder
  -> library Errors.verifyNotZero


### public totalSupply
_(no internal calls)_


### external withdraw
-> internal _updateReward
  -> public rewardPerToken
    -> public totalSupply
    -> public lastBlockRewardApplicable
  -> public lastBlockRewardApplicable
  -> public earned
    -> public balanceOf
    -> public rewardPerToken
      -> public totalSupply
      -> public lastBlockRewardApplicable
-> internal _withdrawAbstractRewarder
  -> library Errors.verifyNotZero


---

## EzethLRTCalculator

_File: src/stats/calculators/EzethLRTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> private _setRenzoRestakeManager
  -> library Errors.verifyNotZero


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### external setRenzoRestakeManager
-> private _setRenzoRestakeManager
  -> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## FrxEthLSTCalculator

_File: src/stats/calculators/FrxEthLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## IncentiveCalculatorBase

_File: src/stats/calculators/base/IncentiveCalculatorBase.sol_

### external current
-> internal _computeTotalAPR
  -> internal _getRewardPoolMetrics
  -> internal _shouldSnapshot
    -> internal _snapshotStatus
    -> library Stats.differsByMoreThanFivePercent
  -> internal _snapshotRewarder
    -> internal _snapshotStatus
  -> internal _getLpTokenPriceInEth
    -> library Errors.UnsafePrice
  -> internal _computeAPR
    -> internal _getIncentivePrice
-> library Stats.decayCredits
-> internal _getStakingIncentiveStats


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _getRewardPoolMetrics
-> internal _shouldSnapshot
  -> internal _snapshotStatus
  -> library Stats.differsByMoreThanFivePercent


### external snapshot
-> public shouldSnapshot
  -> internal _getRewardPoolMetrics
  -> internal _shouldSnapshot
    -> internal _snapshotStatus
    -> library Stats.differsByMoreThanFivePercent
-> internal _snapshot
  -> internal _computeTotalAPR
    -> internal _getRewardPoolMetrics
    -> internal _shouldSnapshot
      -> internal _snapshotStatus
      -> library Stats.differsByMoreThanFivePercent
    -> internal _snapshotRewarder
      -> internal _snapshotStatus
    -> internal _getLpTokenPriceInEth
      -> library Errors.UnsafePrice
    -> internal _computeAPR
      -> internal _getIncentivePrice
  -> library Stats.decayCredits


---

## IncentivePricingStats

_File: src/stats/calculators/IncentivePricingStats.sol_

### public getPrice
_(no internal calls)_


### external getPriceOrZero
-> public getPrice


### external getRegisteredTokens
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external getTokenPricingInfo
_(no internal calls)_


### external removeRegisteredToken
_(no internal calls)_


### external setRegisteredToken
-> internal updatePricingInfo
  -> library Stats.getFilteredValue
  -> internal emitSnapshotTaken


### external snapshot
-> library Errors.InvalidParam
-> library Errors.verifyNotZero
-> internal updatePricingInfo
  -> library Stats.getFilteredValue
  -> internal emitSnapshotTaken


---

## LSTCalculatorBase

_File: src/stats/calculators/base/LSTCalculatorBase.sol_

### external current
-> private calculateDiscount


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> internal updateDiscountHistory
  -> private calculateDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### external snapshot
-> public shouldSnapshot
  -> internal _timeForAprSnapshot
  -> internal _timeForDiscountSnapshot
-> internal _snapshot
  -> internal _timeForAprSnapshot
  -> library Stats.calculateAnnualizedChangeMinZero
  -> library Stats.getFilteredValue
  -> library MessageTypes.LSTDestinationInfo
  -> internal _timeForDiscountSnapshot
  -> internal updateDiscountHistory
    -> private calculateDiscount
  -> internal updateDiscountTimestampByPercent


---

## Lens

_File: src/lens/Lens.sol_

### external getPools
-> private _getPools
  -> private _fillInFeeSettings


### external getPoolsAndDestinations
-> private _getPools
  -> private _fillInFeeSettings
-> private _getDestinations
  -> private _safeDestinationGetStats
  -> private _safeGetDestinationUnderlying
  -> private _safeGetSummaryStats


### external getSystemRegistry
_(no internal calls)_


### external getUserRewardInfo
-> private _getPools
  -> private _fillInFeeSettings


### public proxyGetDestinationSummaryStats
_(no internal calls)_


### public proxyGetFeeSettings
_(no internal calls)_


### public proxyGetStats
_(no internal calls)_


---

## LiquidationExecutor

_File: src/liquidation/LiquidationExecutor.sol_

### external execute
_(no internal calls)_


---

## LiquidationRow

_File: src/liquidation/LiquidationRow.sol_

### external addToWhitelist
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external balanceOf
_(no internal calls)_


### public calculateFee
_(no internal calls)_


### external claimsVaultRewards
-> library Errors.InvalidParam
-> internal _increaseBalance
  -> library Errors.verifyNotZero
  -> library Errors.InsufficientBalance
  -> library Errors.ItemExists


### external getSystemRegistry
_(no internal calls)_


### external getTokens
_(no internal calls)_


### external getVaultsForToken
_(no internal calls)_


### external isWhitelisted
_(no internal calls)_


### external liquidateVaultsForToken
-> private _liquidateVaultsForToken
  -> private _prepareForLiquidation
    -> library Errors.ItemNotFound
  -> private _performLiquidation
    -> public calculateFee
    -> library LibAdapter._approve


### external liquidateVaultsForTokens
-> library Errors.verifyNotZero
-> private _liquidateVaultsForToken
  -> private _prepareForLiquidation
    -> library Errors.ItemNotFound
  -> private _performLiquidation
    -> public calculateFee
    -> library LibAdapter._approve


### external removeFromWhitelist
-> library Errors.ItemNotFound


### external setFeeAndReceiver
_(no internal calls)_


### external setPriceMarginBps
-> private _setPriceMarginBps
  -> library Errors.InvalidParam


### external totalBalanceOf
_(no internal calls)_


---

## MainRewarder

_File: src/rewarders/MainRewarder.sol_

### external addExtraReward
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external addToWhitelist
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### public balanceOf
_(no internal calls)_


### public earned
-> public balanceOf
-> public rewardPerToken
  -> public totalSupply
  -> public lastBlockRewardApplicable


### external extraRewards
_(no internal calls)_


### external extraRewardsLength
_(no internal calls)_


### external getExtraRewarder
_(no internal calls)_


### external getReward
-> internal _updateReward
  -> public rewardPerToken
    -> public totalSupply
    -> public lastBlockRewardApplicable
  -> public lastBlockRewardApplicable
  -> public earned
    -> public balanceOf
    -> public rewardPerToken
      -> public totalSupply
      -> public lastBlockRewardApplicable
-> internal _processRewards
  -> internal _getReward
    -> internal _updateReward
      -> public rewardPerToken
        -> public totalSupply
        -> public lastBlockRewardApplicable
      -> public lastBlockRewardApplicable
      -> public earned
        -> public balanceOf
        -> public rewardPerToken
          -> public totalSupply
          -> public lastBlockRewardApplicable
    -> internal _processRewards


### external isWhitelisted
_(no internal calls)_


### public lastBlockRewardApplicable
_(no internal calls)_


### external queueNewRewards
-> internal notifyRewardAmount
  -> public totalSupply
  -> internal _updateReward
    -> public rewardPerToken
      -> public totalSupply
      -> public lastBlockRewardApplicable
    -> public lastBlockRewardApplicable
    -> public earned
      -> public balanceOf
      -> public rewardPerToken
        -> public totalSupply
        -> public lastBlockRewardApplicable
  -> library Errors.ZeroAmount


### external recover
-> library Errors.verifyNotZero
-> library Errors.InvalidAddress
-> library Errors.AssetNotAllowed


### external removeFromWhitelist
-> library Errors.ItemNotFound


### public rewardPerToken
-> public totalSupply
-> public lastBlockRewardApplicable


### external setTokeLockDuration
-> library Errors.verifyNotZero
-> external_callback IAccToke.StakingDurationTooShort


### public totalSupply
_(no internal calls)_


---

## MavEthOracle

_File: src/oracles/providers/MavEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getSafeSpotPriceInfo
-> library Errors.verifyNotZero
-> internal _scaleDecimalsToOriginal
-> external_callback ISpotPriceOracle.ReserveItemInfo
-> private _getSpotPrice
  -> library Utilities.getScaleDownFactor


### public getSpotPrice
-> library Errors.verifyNotZero
-> private _getSpotPrice
  -> library Utilities.getScaleDownFactor


### external getSystemRegistry
_(no internal calls)_


### external setPoolInformation
-> library Errors.verifyNotZero


---

## MaverickCalculator

_File: src/stats/calculators/MaverickCalculator.sol_

### public _shouldSnapshot
-> public _snapshotRewarderStatus
-> library Stats.differsByMoreThanFivePercent


### public _snapshotRewarderStatus
_(no internal calls)_


### external current
-> internal _computeTotalAPR
  -> public _shouldSnapshot
    -> public _snapshotRewarderStatus
    -> library Stats.differsByMoreThanFivePercent
  -> internal _snapshotRewarder
    -> public _snapshotRewarderStatus
  -> internal _computeAPR
    -> internal _getIncentivePrice
-> library Stats.decayCredits


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Errors.verifyNotZero


### public lpToken
_(no internal calls)_


### public shouldSnapshot
-> public _shouldSnapshot
  -> public _snapshotRewarderStatus
  -> library Stats.differsByMoreThanFivePercent


### external snapshot
-> public shouldSnapshot
  -> public _shouldSnapshot
    -> public _snapshotRewarderStatus
    -> library Stats.differsByMoreThanFivePercent
-> internal _snapshot
  -> internal _computeTotalAPR
    -> public _shouldSnapshot
      -> public _snapshotRewarderStatus
      -> library Stats.differsByMoreThanFivePercent
    -> internal _snapshotRewarder
      -> public _snapshotRewarderStatus
    -> internal _computeAPR
      -> internal _getIncentivePrice
  -> library Stats.decayCredits


---

## MaverickDestinationVault

_File: src/vault/MaverickDestinationVault.sol_

### public balanceOfUnderlyingDebt
-> public internalDebtBalance
-> public externalDebtBalance


### external baseAsset
_(no internal calls)_


### external collectRewards
-> internal _collectRewards
  -> library MaverickRewardsAdapter.claimRewards


### external debtValue
-> private _debtValue
  -> public getPool


### public decimals
_(no internal calls)_


### external depositUnderlying
-> library Errors.verifyNotZero
-> internal _onDeposit
  -> library MaverickStakingAdapter.stakeLPs


### external exchangeName
_(no internal calls)_


### external executeExtension
-> library Errors.verifyNotZero
-> public externalDebtBalance
-> public internalDebtBalance
-> public externalQueriedBalance
-> public internalQueriedBalance


### public externalDebtBalance
_(no internal calls)_


### public externalQueriedBalance
_(no internal calls)_


### external getMarketplaceRewards
_(no internal calls)_


### public getPool
_(no internal calls)_


### external getRangePricesLP
-> public getPool


### external getStats
_(no internal calls)_


### external getUnderlyerCeilingPrice
-> public getPool


### external getUnderlyerFloorPrice
-> public getPool


### external getValidatedSafePrice
-> public getPool


### external getValidatedSpotPrice
-> public getPool


### public initialize
-> library Errors.verifyNotZero
-> library Errors.InvalidConfiguration
-> internal _addTrackedToken


### public internalDebtBalance
_(no internal calls)_


### public internalQueriedBalance
_(no internal calls)_


### external isShutdown
_(no internal calls)_


### public isTrackedToken
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public name
_(no internal calls)_


### external poolDealInEth
_(no internal calls)_


### external poolType
_(no internal calls)_


### external recover
-> public isTrackedToken


### external recoverUnderlying
-> library Errors.verifyNotZero
-> public externalQueriedBalance
-> public externalDebtBalance
-> public internalQueriedBalance
-> public internalDebtBalance
-> internal _ensureLocalUnderlyingBalance
  -> library MaverickStakingAdapter.unstakeLPs


### external rewarder
_(no internal calls)_


### external setExtension
_(no internal calls)_


### external setIncentiveCalculator
-> internal _validateCalculator


### external setMessage
_(no internal calls)_


### external setRecoupMaxCredit
-> private _setRecoupMaxCredit
  -> library Errors.InvalidParam


### external shutdown
_(no internal calls)_


### external shutdownStatus
_(no internal calls)_


### public symbol
_(no internal calls)_


### public trackedTokens
_(no internal calls)_


### external underlying
_(no internal calls)_


### external underlyingReserves
_(no internal calls)_


### external underlyingTokens
_(no internal calls)_


### external underlyingTotalSupply
_(no internal calls)_


### external withdrawBaseAsset
-> internal _withdrawBaseAsset
  -> library Errors.verifyNotZero
  -> internal _ensureLocalUnderlyingBalance
    -> library MaverickStakingAdapter.unstakeLPs
  -> internal _burnUnderlyer
  -> library Errors.verifyArrayLengths
  -> library LibAdapter._approve


### external withdrawUnderlying
-> library Errors.verifyNotZero
-> internal _ensureLocalUnderlyingBalance
  -> library MaverickStakingAdapter.unstakeLPs


---

## MaverickDexCalculator

_File: src/stats/calculators/MaverickDexCalculator.sol_

### external current
-> internal _getCurrentReservesInEth
  -> internal calculateReserveInEthByIndex
-> library Stats.getFilteredValue


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
-> library Errors.verifyNotZero
-> library Stats.CalculatorAssetMismatch


### public shouldSnapshot
_(no internal calls)_


### external snapshot
-> public shouldSnapshot
-> internal _snapshot
  -> internal _getCurrentReservesInEth
    -> internal calculateReserveInEthByIndex
  -> library Stats.getFilteredValue


---

## MaverickFeeAprOracle

_File: src/oracles/providers/MaverickFeeAprOracle.sol_

### external getFeeApr
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external setFeeApr
_(no internal calls)_


### external setMaxFeeAprLatency
-> private _setMaxFeeAprLatency
  -> library Errors.verifyNotZero


---

## MessageProxy

_File: src/messageProxy/MessageProxy.sol_

### external addMessageRoutes
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external getFee
-> library Errors.verifyNotZero
-> internal _ccipBuild
  -> library Client.EVM2AnyMessage
  -> library Client._argsToBytes
  -> library Client.EVMExtraArgsV1


### external getMessageRoutes
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external removeMessageRoutes
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external resendLastMessage
-> library Errors.verifyNotZero
-> internal _ccipBuild
  -> library Client.EVM2AnyMessage
  -> library Client._argsToBytes
  -> library Client.EVMExtraArgsV1


### external sendMessage
-> internal _ccipBuild
  -> library Client.EVM2AnyMessage
  -> library Client._argsToBytes
  -> library Client.EVMExtraArgsV1


### external setDestinationChainReceiver
_(no internal calls)_


### external setGasForRoute
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


---

## MessageReceiverBase

_File: src/receivingRouter/MessageReceiverBase.sol_

### external onMessageReceive
_(no internal calls)_


---

## Multicall

_File: src/utils/Multicall.sol_

### public multicall
_(no internal calls)_


---

## OethLSTCalculator

_File: src/stats/calculators/OethLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## OsethLSTCalculator

_File: src/stats/calculators/OsethLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> private _setOsEthPriceOracle
  -> library Errors.verifyNotZero


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### external setOsEthPriceOracle
-> private _setOsEthPriceOracle
  -> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## Ownable2Step

_File: src/access/Ownable2Step.sol_

### public renounceOwnership
_(no internal calls)_


---

## Pausable

_File: src/security/Pausable.sol_

### external pause
_(no internal calls)_


### public paused
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## PctFeeSplitter

_File: src/vault/fees/PctFeeSplitter.sol_

### external claimFees
-> library Errors.verifyNotZero
-> library Errors.InvalidSigner


### external getSystemRegistry
_(no internal calls)_


### external setFeeRecipients
-> library Errors.verifyNotZero
-> library Errors.InvalidParams


---

## PeripheryPayments

_File: src/utils/PeripheryPayments.sol_

### public approve
-> library LibAdapter._approve


### public pullToken
_(no internal calls)_


### external refundETH
_(no internal calls)_


### public sweepToken
_(no internal calls)_


### public unwrapWETH9
_(no internal calls)_


### public wrapWETH9
_(no internal calls)_


---

## PointsHook

_File: src/strategy/hooks/PointsHook.sol_

### external execute
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external setBoosts
-> library Errors.verifyNotZero
-> library Errors.verifyArrayLengths


---

## ProxyLSTCalculator

_File: src/stats/calculators/ProxyLSTCalculator.sol_

### external calculateEthPerToken
_(no internal calls)_


### external current
_(no internal calls)_


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### external initialize
_(no internal calls)_


### public shouldSnapshot
_(no internal calls)_


### external snapshot
-> public shouldSnapshot
-> internal _snapshot


### external usePriceAsDiscount
_(no internal calls)_


---

## PufEthLRTCalculator

_File: src/stats/calculators/PufEthLRTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> private _setPufEthVault
  -> library Errors.verifyNotZero


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### external setPufEthVault
-> private _setPufEthVault
  -> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## PxETHEthOracle

_File: src/oracles/providers/PxETHEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getPriceInEth
-> library Errors.InvalidToken


### external getSystemRegistry
_(no internal calls)_


---

## PxEthLSTCalculator

_File: src/stats/calculators/PxEthLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## ReceivingRouter

_File: src/receivingRouter/ReceivingRouter.sol_

### external ccipReceive
-> internal _ccipReceive
  -> private decodeMessage
  -> private _getMessageReceiversKey


### external getMessageReceivers
-> private _getMessageReceiversKey


### public getRouter
_(no internal calls)_


### external getSourceChainSenders
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external removeMessageReceivers
-> library Errors.verifyNotZero
-> private _getMessageReceiversKey
-> library Errors.ItemNotFound


### external setMessageReceivers
-> library Errors.verifyNotZero
-> private _getMessageReceiversKey
-> library Errors.ItemExists


### external setSourceChainSenders
-> library Errors.InvalidParam
-> library Errors.ItemExists


### public supportsInterface
_(no internal calls)_


---

## RedstoneOracle

_File: src/oracles/providers/RedstoneOracle.sol_

### external getDescription
_(no internal calls)_


### external getOracleInfo
_(no internal calls)_


### external getPriceInEth
-> external_callback BaseAggregatorV3OracleInformation._getOracleInfo
  -> library Errors.verifyNotZero
-> external_callback BaseAggregatorV3OracleInformation._getPriceInEth
  -> library Errors.InvalidDataReturned


### public registerOracle
-> library Errors.verifyNotZero
-> library Errors.AlreadyRegistered


### public removeOracleRegistration
-> library Errors.verifyNotZero
-> library Errors.MustBeSet


---

## RethLSTCalculator

_File: src/stats/calculators/RethLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## Rewards

_File: src/rewarders/Rewards.sol_

### external claim
-> library Errors.SenderMismatch
-> internal _claim
  -> public genHash
    -> private _hashRecipient
  -> library Errors.InvalidSigner
  -> private _getChainID
  -> library Errors.InvalidChainId
  -> library Errors.ZeroAmount
  -> library Errors.InsufficientBalance


### external claimFor
-> library Errors.AccessDenied
-> internal _claim
  -> public genHash
    -> private _hashRecipient
  -> library Errors.InvalidSigner
  -> private _getChainID
  -> library Errors.InvalidChainId
  -> library Errors.ZeroAmount
  -> library Errors.InsufficientBalance


### public genHash
-> private _hashRecipient


### external getClaimableAmount
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external setSigner
-> library Errors.verifyNotZero


---

## RootPriceOracle

_File: src/oracles/RootPriceOracle.sol_

### external getCeilingPrice
-> public getFloorCeilingPrice
  -> internal _calculateReservesAndPrice
    -> private _checkSpotOracleRegistration
    -> internal _scaleValue
    -> public getPriceInQuote
      -> private _checkTokenOracleRegistration
    -> internal _enforceQuoteToken
      -> public getPriceInQuote
        -> private _checkTokenOracleRegistration


### public getFloorCeilingPrice
-> internal _calculateReservesAndPrice
  -> private _checkSpotOracleRegistration
  -> internal _scaleValue
  -> public getPriceInQuote
    -> private _checkTokenOracleRegistration
  -> internal _enforceQuoteToken
    -> public getPriceInQuote
      -> private _checkTokenOracleRegistration


### external getFloorPrice
-> public getFloorCeilingPrice
  -> internal _calculateReservesAndPrice
    -> private _checkSpotOracleRegistration
    -> internal _scaleValue
    -> public getPriceInQuote
      -> private _checkTokenOracleRegistration
    -> internal _enforceQuoteToken
      -> public getPriceInQuote
        -> private _checkTokenOracleRegistration


### external getPriceInEth
-> private _checkTokenOracleRegistration


### public getPriceInQuote
-> private _checkTokenOracleRegistration


### external getRangePricesLP
-> private _checkSpotOracleRegistration
-> library Errors.InvalidParam
-> public getPriceInQuote
  -> private _checkTokenOracleRegistration
-> internal _enforceQuoteToken
  -> public getPriceInQuote
    -> private _checkTokenOracleRegistration


### external getSpotPriceInEth
-> library Errors.verifyNotZero
-> private _checkSpotOracleRegistration
-> internal _getSpotPriceInQuote
  -> internal _enforceQuoteToken
    -> public getPriceInQuote
      -> private _checkTokenOracleRegistration


### external getSystemRegistry
_(no internal calls)_


### external registerMapping
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### external registerPoolMapping
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### external removeMapping
-> library Errors.verifyNotZero


### external removePoolMapping
-> library Errors.verifyNotZero


### external replaceMapping
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### external replacePoolMapping
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### external setSafeSpotPriceThreshold
-> library Errors.verifyNotZero
-> library Errors.InvalidParam


---

## RsethLRTCalculator

_File: src/stats/calculators/RsethLRTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## RswethLRTCalculator

_File: src/stats/calculators/RswethLRTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## SelfPermit

_File: src/utils/SelfPermit.sol_

### public selfPermit
_(no internal calls)_


---

## SequencerChecker

_File: src/security/SequencerChecker.sol_

### external checkSequencerUptimeFeed
-> library Errors.InvalidDataReturned


### external getSystemRegistry
_(no internal calls)_


---

## StatsCalculatorFactory

_File: src/stats/StatsCalculatorFactory.sol_

### external create
-> library Errors.verifyNotZero


### external getSystemRegistry
_(no internal calls)_


### external registerTemplate
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


### external removeTemplate
-> library Errors.verifyNotZero


### external replaceTemplate
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


---

## StatsCalculatorRegistry

_File: src/stats/StatsCalculatorRegistry.sol_

### external getCalculator
-> library Errors.verifyNotZero


### external getSystemRegistry
_(no internal calls)_


### external listCalculators
_(no internal calls)_


### external register
-> library Errors.verifyNotZero


### external removeCalculator
-> library Errors.NotRegistered


### external setCalculatorFactory
-> library Errors.verifyNotZero
-> library Errors.verifySystemsMatch


---

## StethLSTCalculator

_File: src/stats/calculators/StethLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## SwapRouter

_File: src/swapper/SwapRouter.sol_

### external getSystemRegistry
_(no internal calls)_


### external setSwapRoute
-> library Errors.verifyNotZero
-> library Errors.InvalidParams


### external swapForQuote
-> library Errors.ZeroAmount
-> library Errors.InvalidParams
-> library Errors.verifyNotZero


---

## SwethLSTCalculator

_File: src/stats/calculators/SwethLSTCalculator.sol_

### public calculateEthPerToken
_(no internal calls)_


### external current
-> private calculateDiscount
  -> public usePriceAsDiscount
-> public calculateEthPerToken


### external getAddressId
_(no internal calls)_


### external getAprId
_(no internal calls)_


### public initialize
-> library Stats.generateRawTokenIdentifier
-> public calculateEthPerToken
-> internal updateDiscountHistory
  -> private calculateDiscount
    -> public usePriceAsDiscount
-> internal updateDiscountTimestampByPercent


### external setDestinationMessageSend
-> library Errors.verifyNotZero


### public shouldSnapshot
-> internal _timeForAprSnapshot
-> internal _timeForDiscountSnapshot


### public usePriceAsDiscount
_(no internal calls)_


---

## SystemComponent

_File: src/SystemComponent.sol_

### external getSystemRegistry
_(no internal calls)_


---

## SystemRegistry

_File: src/SystemRegistry.sol_

### external accToke
_(no internal calls)_


### external accessController
_(no internal calls)_


### external addRewardToken
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external asyncSwapperRegistry
_(no internal calls)_


### external autoPoolRegistry
_(no internal calls)_


### external autoPoolRouter
_(no internal calls)_


### external curveResolver
_(no internal calls)_


### external destinationTemplateRegistry
_(no internal calls)_


### external destinationVaultRegistry
_(no internal calls)_


### external getAutopoolFactoryByType
-> library Errors.ItemNotFound


### external getUniqueContract
-> library Errors.verifyNotZero


### external incentivePricing
_(no internal calls)_


### external isRewardToken
_(no internal calls)_


### external isValidContract
_(no internal calls)_


### external listAdditionalContractTypes
_(no internal calls)_


### external listAdditionalContracts
_(no internal calls)_


### external listUniqueContracts
_(no internal calls)_


### external messageProxy
_(no internal calls)_


### external receivingRouter
_(no internal calls)_


### external removeAutopoolFactory
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external removeRewardToken
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external rootPriceOracle
_(no internal calls)_


### external setAccToke
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAccessController
-> library Errors.verifyNotZero
-> library Errors.AlreadySet
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAsyncSwapperRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopilotRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopoolFactory
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopoolRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setContract
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setCurveResolver
-> library Errors.verifyNotZero


### external setDestinationTemplateRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setDestinationVaultRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setIncentivePricingStats
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setMessageProxy
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setReceivingRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setRootPriceOracle
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setStatsCalculatorRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setSwapRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setSystemSecurity
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setUniqueContract
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external statsCalculatorRegistry
_(no internal calls)_


### external swapRouter
_(no internal calls)_


### external systemSecurity
_(no internal calls)_


### external unsetContract
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external unsetUniqueContract
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


---

## SystemRegistryBase

_File: src/SystemRegistryBase.sol_

### external accToke
_(no internal calls)_


### external accessController
_(no internal calls)_


### external addRewardToken
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external asyncSwapperRegistry
_(no internal calls)_


### external autoPoolRegistry
_(no internal calls)_


### external autoPoolRouter
_(no internal calls)_


### external curveResolver
_(no internal calls)_


### external destinationTemplateRegistry
_(no internal calls)_


### external destinationVaultRegistry
_(no internal calls)_


### external getAutopoolFactoryByType
-> library Errors.ItemNotFound


### external getUniqueContract
-> library Errors.verifyNotZero


### external incentivePricing
_(no internal calls)_


### external isRewardToken
_(no internal calls)_


### external isValidContract
_(no internal calls)_


### external listAdditionalContractTypes
_(no internal calls)_


### external listAdditionalContracts
_(no internal calls)_


### external listUniqueContracts
_(no internal calls)_


### external messageProxy
_(no internal calls)_


### external receivingRouter
_(no internal calls)_


### external removeAutopoolFactory
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external removeRewardToken
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### public renounceOwnership
_(no internal calls)_


### external rootPriceOracle
_(no internal calls)_


### external setAccToke
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAccessController
-> library Errors.verifyNotZero
-> library Errors.AlreadySet
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAsyncSwapperRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopilotRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopoolFactory
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopoolRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setContract
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setCurveResolver
-> library Errors.verifyNotZero


### external setDestinationTemplateRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setDestinationVaultRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setIncentivePricingStats
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setMessageProxy
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setReceivingRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setRootPriceOracle
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setStatsCalculatorRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setSwapRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setSystemSecurity
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setUniqueContract
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external statsCalculatorRegistry
_(no internal calls)_


### external swapRouter
_(no internal calls)_


### external systemSecurity
_(no internal calls)_


### external unsetContract
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external unsetUniqueContract
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


---

## SystemRegistryL2

_File: src/SystemRegistryL2.sol_

### external accToke
_(no internal calls)_


### external accessController
_(no internal calls)_


### external addRewardToken
-> library Errors.verifyNotZero
-> library Errors.ItemExists


### external asyncSwapperRegistry
_(no internal calls)_


### external autoPoolRegistry
_(no internal calls)_


### external autoPoolRouter
_(no internal calls)_


### external curveResolver
_(no internal calls)_


### external destinationTemplateRegistry
_(no internal calls)_


### external destinationVaultRegistry
_(no internal calls)_


### external getAutopoolFactoryByType
-> library Errors.ItemNotFound


### external getUniqueContract
-> library Errors.verifyNotZero


### external incentivePricing
_(no internal calls)_


### external isRewardToken
_(no internal calls)_


### external isValidContract
_(no internal calls)_


### external listAdditionalContractTypes
_(no internal calls)_


### external listAdditionalContracts
_(no internal calls)_


### external listUniqueContracts
_(no internal calls)_


### external messageProxy
_(no internal calls)_


### external receivingRouter
_(no internal calls)_


### external removeAutopoolFactory
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external removeRewardToken
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external rootPriceOracle
_(no internal calls)_


### external sequencerChecker
_(no internal calls)_


### external setAccToke
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAccessController
-> library Errors.verifyNotZero
-> library Errors.AlreadySet
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAsyncSwapperRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopilotRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopoolFactory
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setAutopoolRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setContract
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setCurveResolver
-> library Errors.verifyNotZero


### external setDestinationTemplateRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setDestinationVaultRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setIncentivePricingStats
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setMessageProxy
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setReceivingRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setRootPriceOracle
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setSequencerChecker
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setStatsCalculatorRegistry
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setSwapRouter
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setSystemSecurity
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setToke
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external setUniqueContract
-> library Errors.verifyNotZero
-> internal _verifySystemsAgree
  -> library Errors.SystemMismatch


### external statsCalculatorRegistry
_(no internal calls)_


### external swapRouter
_(no internal calls)_


### external systemSecurity
_(no internal calls)_


### external unsetContract
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


### external unsetUniqueContract
-> library Errors.verifyNotZero
-> library Errors.ItemNotFound


---

## SystemSecurity

_File: src/security/SystemSecurity.sol_

### external enterNavOperation
_(no internal calls)_


### external exitNavOperation
_(no internal calls)_


### external getSystemRegistry
_(no internal calls)_


### external pauseSystem
_(no internal calls)_


### external unpauseSystem
_(no internal calls)_


---

## SystemSecurityL1

_File: src/security/SystemSecurityL1.sol_

### external enterNavOperation
_(no internal calls)_


### external exitNavOperation
_(no internal calls)_


### external isSystemPaused
_(no internal calls)_


### external pauseSystem
_(no internal calls)_


### external unpauseSystem
_(no internal calls)_


---

## SystemSecurityL2

_File: src/security/SystemSecurityL2.sol_

### external enterNavOperation
_(no internal calls)_


### external exitNavOperation
_(no internal calls)_


### external isSystemPaused
-> library Errors.verifyNotZero


### external pauseSystem
_(no internal calls)_


### external setOverrideSequencerUptime
_(no internal calls)_


### external unpauseSystem
_(no internal calls)_


---

## TellorOracle

_File: src/oracles/providers/TellorOracle.sol_

### external addTellorRegistration
-> library Errors.verifyNotZero
-> library Errors.MustBeZero


### external getDescription
_(no internal calls)_


### external getPriceInEth
-> private _getQueryInfo
  -> library Errors.verifyNotZero
-> library Errors.InvalidDataReturned
-> internal _denominationPricing
  -> private _getPriceDenominationUSD


### external getQueryInfo
_(no internal calls)_


### external removeTellorRegistration
-> library Errors.verifyNotZero


### external setTellorPricingFreshness
-> library Errors.verifyNotZero


---

## UniV3Swap

_File: src/swapper/adapters/UniV3Swap.sol_

### external swap
-> library LibAdapter._approve
-> external_callback IUniswapV3SwapRouter.ExactInputParams


### external validate
-> private _decodePath


---

## WstETHEthOracle

_File: src/oracles/providers/WstETHEthOracle.sol_

### external getDescription
_(no internal calls)_


### external getPriceInEth
-> library Errors.InvalidToken


### external getSystemRegistry
_(no internal calls)_


---

## ZeroCalculator

_File: src/stats/calculators/ZeroCalculator.sol_

### external current
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setLpTokenPool
_(no internal calls)_

