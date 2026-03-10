# Callpaths — Rage_Trade

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BatchingManagerBypass

_File: contracts/periphery/BatchingManagerBypass.sol_

### external deposit
_(no internal calls)_


### external setJuniorVault
_(no internal calls)_


### external setSglp
_(no internal calls)_


---

## DepositPeriphery

_File: contracts/periphery/DepositPeriphery.sol_

### external depositToken
-> internal _convertToSglp


### external setAddresses
_(no internal calls)_


### external setSlippageThreshold
_(no internal calls)_


---

## DnGmxBatchingManager

_File: contracts/vaults/DnGmxBatchingManager.sol_

### external claim
-> internal _claim


### external claimAndRedeem
-> internal _claim
-> public unclaimedShares


### external currentRound
_(no internal calls)_


### external depositUsdc
-> private _usdcToGlp


### external executeBatch
-> internal _executeVaultUserBatchStake
  -> internal _stakeGlp
-> internal _executeVaultUserBatchDeposit


### external grantAllowances
_(no internal calls)_


### external initialize
-> internal __GMXBatchingManager_init


### external pauseDeposit
_(no internal calls)_


### external rescueFees
-> internal _stakeGlp


### external roundDeposits
_(no internal calls)_


### external roundGlpDepositPending
_(no internal calls)_


### external roundGlpStaked
_(no internal calls)_


### external roundSharesMinted
_(no internal calls)_


### external roundUsdcBalance
_(no internal calls)_


### external setDepositCap
_(no internal calls)_


### external setGlp
_(no internal calls)_


### external setGlpBatchingManager
_(no internal calls)_


### external setKeeper
_(no internal calls)_


### external setParamsV1
_(no internal calls)_


### external setTargetAssetCap
_(no internal calls)_


### external setThresholds
_(no internal calls)_


### public unclaimedShares
_(no internal calls)_


### external unpauseDeposit
_(no internal calls)_


### public usdcBalance
_(no internal calls)_


### external userDeposits
_(no internal calls)_


---

## DnGmxBatchingManagerGlp

_File: contracts/vaults/DnGmxBatchingManagerGlp.sol_

### public assetBalance
_(no internal calls)_


### external claim
-> internal _claim


### external claimAndRedeem
-> internal _claim
-> public unclaimedShares


### external currentRound
_(no internal calls)_


### external deposit
-> private _usdcToGlp


### external executeBatch
-> internal _executeVaultUserBatchDeposit


### external grantAllowances
_(no internal calls)_


### external initialize
-> internal __GMXBatchingManager_init


### external pauseDeposit
_(no internal calls)_


### external roundAssetBalance
_(no internal calls)_


### external roundDeposits
_(no internal calls)_


### external roundGlpDeposited
_(no internal calls)_


### external roundSharesMinted
_(no internal calls)_


### external setDepositCap
_(no internal calls)_


### external setKeeper
_(no internal calls)_


### external setTargetAssetCap
_(no internal calls)_


### external setThresholds
_(no internal calls)_


### external setUsdcBatchingManager
_(no internal calls)_


### public unclaimedShares
_(no internal calls)_


### external unpauseDeposit
_(no internal calls)_


### external userDeposits
_(no internal calls)_


---

## DnGmxJuniorVault

_File: contracts/vaults/DnGmxJuniorVault.sol_

### external claimVestedGmx
_(no internal calls)_


### public convertToAssets
_(no internal calls)_


### public convertToShares
_(no internal calls)_


### public deposit
-> internal _rebalanceBeforeShareAllocation
  -> internal _emitVaultState
-> internal _previewDeposit
  -> public convertToShares
-> internal _emitVaultState


### external depositCap
_(no internal calls)_


### external dnUsdcDeposited
_(no internal calls)_


### external getAdminParams
_(no internal calls)_


### external getCurrentBorrows
_(no internal calls)_


### external getHedgeParams
_(no internal calls)_


### public getMarketValue
_(no internal calls)_


### external getOptimalBorrows
_(no internal calls)_


### public getPrice
_(no internal calls)_


### public getPriceX128
_(no internal calls)_


### external getRebalanceParams
_(no internal calls)_


### external getThresholds
_(no internal calls)_


### public getUsdcBorrowed
_(no internal calls)_


### public getVaultMarketValue
-> public getMarketValue


### external grantAllowances
_(no internal calls)_


### external harvestFees
_(no internal calls)_


### external initialize
-> internal __ERC4626Upgradeable_init


### public isValidRebalance
_(no internal calls)_


### public maxDeposit
_(no internal calls)_


### public maxMint
-> public convertToShares
-> public maxDeposit


### public maxRedeem
_(no internal calls)_


### public maxWithdraw
-> public convertToAssets


### public mint
-> internal _rebalanceBeforeShareAllocation
  -> internal _emitVaultState
-> internal _previewMint
  -> public convertToAssets
-> internal _emitVaultState


### external pause
_(no internal calls)_


### public previewDeposit
-> internal _previewDeposit
  -> public convertToShares


### public previewMint
-> internal _previewMint
  -> public convertToAssets


### public previewRedeem
-> internal _previewRedeem
  -> public convertToAssets


### public previewWithdraw
-> internal _previewWithdraw


### external rebalance
-> public isValidRebalance
-> internal _emitVaultState


### external rebalanceProfit
_(no internal calls)_


### external receiveFlashLoan
_(no internal calls)_


### public redeem
-> internal _rebalanceBeforeShareAllocation
  -> internal _emitVaultState
-> internal _previewRedeem
  -> public convertToAssets
-> internal _emitVaultState


### external setAdminParams
_(no internal calls)_


### external setDirectConversion
_(no internal calls)_


### external setFeeParams
_(no internal calls)_


### external setGmxParams
_(no internal calls)_


### external setHedgeParams
_(no internal calls)_


### external setParamsV1
_(no internal calls)_


### external setRebalanceParams
_(no internal calls)_


### external setThresholds
_(no internal calls)_


### external stopVestAndStakeEsGmx
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### external unpause
_(no internal calls)_


### external unstakeAndVestEsGmx
_(no internal calls)_


### public withdraw
-> internal _rebalanceBeforeShareAllocation
  -> internal _emitVaultState
-> internal _previewWithdraw
-> internal _emitVaultState


### external withdrawFees
_(no internal calls)_


---

## DnGmxSeniorVault

_File: contracts/vaults/DnGmxSeniorVault.sol_

### public availableBorrow
_(no internal calls)_


### external borrow
-> public availableBorrow


### public convertToAssets
-> public totalAssets
  -> public totalUsdcBorrowed


### public convertToShares
-> public totalAssets
  -> public totalUsdcBorrowed


### public decimals
_(no internal calls)_


### public deposit
-> internal _emitVaultState


### public getEthRewardsSplitRate
-> public totalUsdcBorrowed


### public getPriceX128
_(no internal calls)_


### public getVaultMarketValue
-> public totalAssets
  -> public totalUsdcBorrowed


### external grantAllowances
_(no internal calls)_


### external initialize
-> internal __ERC4626Upgradeable_init


### public maxDeposit
-> public totalAssets
  -> public totalUsdcBorrowed


### public maxMint
-> public convertToShares
  -> public totalAssets
    -> public totalUsdcBorrowed
-> public maxDeposit
  -> public totalAssets
    -> public totalUsdcBorrowed


### public maxRedeem
-> public convertToShares
  -> public totalAssets
    -> public totalUsdcBorrowed
-> public maxWithdraw
  -> public totalAssets
    -> public totalUsdcBorrowed
  -> public totalUsdcBorrowed
  -> public convertToAssets
    -> public totalAssets
      -> public totalUsdcBorrowed


### public maxWithdraw
-> public totalAssets
  -> public totalUsdcBorrowed
-> public totalUsdcBorrowed
-> public convertToAssets
  -> public totalAssets
    -> public totalUsdcBorrowed


### public mint
-> internal _emitVaultState


### external pause
_(no internal calls)_


### public previewDeposit
-> public convertToShares
  -> public totalAssets
    -> public totalUsdcBorrowed


### public previewMint
-> public totalAssets
  -> public totalUsdcBorrowed


### public previewRedeem
-> public convertToAssets
  -> public totalAssets
    -> public totalUsdcBorrowed


### public previewWithdraw
-> public totalAssets
  -> public totalUsdcBorrowed


### public redeem
-> internal _emitVaultState


### external repay
_(no internal calls)_


### external setDepositCap
_(no internal calls)_


### external setDnGmxJuniorVault
_(no internal calls)_


### external setLeveragePool
_(no internal calls)_


### external setMaxUtilizationBps
_(no internal calls)_


### public totalAssets
-> public totalUsdcBorrowed


### public totalUsdcBorrowed
_(no internal calls)_


### external unpause
_(no internal calls)_


### external updateBorrowCap
_(no internal calls)_


### external updateFeeStrategyParams
_(no internal calls)_


### public withdraw
-> internal _emitVaultState


---

## DnGmxTraderHedgeStrategy

_File: contracts/vaults/DnGmxTraderHedgeStrategy.sol_

### external initialize
-> internal __DnGmxTraderHedgeStrategy_init


### external overrideTraderOIHedges
-> internal _checkHedgeAmounts
  -> internal _getMaxTokenHedgeAmount
  -> internal _checkTokenHedgeAmount


### external setKeeper
_(no internal calls)_


### external setTraderOIHedgeBps
_(no internal calls)_


### external setTraderOIHedges
-> internal _getTokenHedgeAmount


---

## ERC4626Upgradeable

_File: contracts/ERC4626/ERC4626Upgradeable.sol_

### public convertToAssets
_(no internal calls)_


### public convertToShares
_(no internal calls)_


### public deposit
-> public previewDeposit
  -> public convertToShares
-> internal afterDeposit


### public maxDeposit
_(no internal calls)_


### public maxMint
_(no internal calls)_


### public maxRedeem
_(no internal calls)_


### public maxWithdraw
-> public convertToAssets


### public mint
-> public previewMint
-> internal afterDeposit


### public previewDeposit
-> public convertToShares


### public previewMint
_(no internal calls)_


### public previewRedeem
-> public convertToAssets


### public previewWithdraw
_(no internal calls)_


### public redeem
-> public previewRedeem
  -> public convertToAssets
-> internal beforeWithdraw


### public withdraw
-> public previewWithdraw
-> internal beforeWithdraw


---

## WithdrawPeriphery

_File: contracts/periphery/WithdrawPeriphery.sol_

### external redeemToken
-> internal _convertToToken
  -> private _getGlpPrice


### external setAddresses
_(no internal calls)_


### external setSlippageThreshold
_(no internal calls)_


### external withdrawToken
-> internal _convertToToken
  -> private _getGlpPrice

