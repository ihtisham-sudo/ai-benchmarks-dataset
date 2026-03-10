# Callpaths — Wildcat_V2

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AccessControlHooks

_File: src/access/AccessControlHooks.sol_

### external addRoleProvider
_(no internal calls)_


### external blockFromDeposits
_(no internal calls)_


### external getHookedMarket
_(no internal calls)_


### external getHookedMarkets
_(no internal calls)_


### external getLenderStatus
-> internal _tryGetCredential
-> internal _loopTryGetCredential
  -> internal _tryGetCredential


### external getParameterConstraints
_(no internal calls)_


### external getPreviousLenderStatus
_(no internal calls)_


### external getPullProviders
_(no internal calls)_


### external getRoleProvider
_(no internal calls)_


### external grantRole
-> internal _grantRole
  -> internal _setCredentialAndEmitAccessGranted


### external grantRoles
-> internal _grantRole
  -> internal _setCredentialAndEmitAccessGranted


### external onBorrow
_(no internal calls)_


### external onCloseMarket
_(no internal calls)_


### external onDeposit
-> internal _tryValidateAccessInner
  -> internal _handleHooksData
    -> internal _readAddress
    -> internal _tryGetCredential
    -> internal _tryValidateCredential
      -> internal _readAddress
  -> internal _tryGetCredential
  -> internal _loopTryGetCredential
    -> internal _tryGetCredential
-> internal _writeLenderStatus


### external onExecuteWithdrawal
_(no internal calls)_


### external onNukeFromOrbit
_(no internal calls)_


### external onQueueWithdrawal
-> internal _tryValidateAccess
  -> internal _tryValidateAccessInner
    -> internal _handleHooksData
      -> internal _readAddress
      -> internal _tryGetCredential
      -> internal _tryValidateCredential
        -> internal _readAddress
    -> internal _tryGetCredential
    -> internal _loopTryGetCredential
      -> internal _tryGetCredential
  -> internal _writeLenderStatus


### external onRepay
_(no internal calls)_


### public onSetAnnualInterestAndReserveRatioBips
_(no internal calls)_


### external onSetMaxTotalSupply
_(no internal calls)_


### external onSetProtocolFeeBips
_(no internal calls)_


### external onTransfer
-> internal _tryValidateAccessInner
  -> internal _handleHooksData
    -> internal _readAddress
    -> internal _tryGetCredential
    -> internal _tryValidateCredential
      -> internal _readAddress
  -> internal _tryGetCredential
  -> internal _loopTryGetCredential
    -> internal _tryGetCredential
-> internal _writeLenderStatus


### external removeRoleProvider
-> internal _removePullProvider


### external revokeRole
_(no internal calls)_


### external setMinimumDeposit
_(no internal calls)_


### external unblockFromDeposits
_(no internal calls)_


### external version
_(no internal calls)_


---

## FixedTermLoanHooks

_File: src/access/FixedTermLoanHooks.sol_

### external addRoleProvider
_(no internal calls)_


### external blockFromDeposits
_(no internal calls)_


### external getHookedMarket
_(no internal calls)_


### external getHookedMarkets
_(no internal calls)_


### external getLenderStatus
-> internal _tryGetCredential
-> internal _loopTryGetCredential
  -> internal _tryGetCredential


### external getParameterConstraints
_(no internal calls)_


### external getPreviousLenderStatus
_(no internal calls)_


### external getPullProviders
_(no internal calls)_


### external getRoleProvider
_(no internal calls)_


### external grantRole
-> internal _grantRole
  -> internal _setCredentialAndEmitAccessGranted


### external grantRoles
-> internal _grantRole
  -> internal _setCredentialAndEmitAccessGranted


### external onBorrow
_(no internal calls)_


### external onCloseMarket
_(no internal calls)_


### external onDeposit
-> internal _tryValidateAccessInner
  -> internal _handleHooksData
    -> internal _readAddress
    -> internal _tryGetCredential
    -> internal _tryValidateCredential
      -> internal _readAddress
  -> internal _tryGetCredential
  -> internal _loopTryGetCredential
    -> internal _tryGetCredential
-> internal _writeLenderStatus


### external onExecuteWithdrawal
_(no internal calls)_


### external onNukeFromOrbit
_(no internal calls)_


### external onQueueWithdrawal
-> internal _tryValidateAccess
  -> internal _tryValidateAccessInner
    -> internal _handleHooksData
      -> internal _readAddress
      -> internal _tryGetCredential
      -> internal _tryValidateCredential
        -> internal _readAddress
    -> internal _tryGetCredential
    -> internal _loopTryGetCredential
      -> internal _tryGetCredential
  -> internal _writeLenderStatus


### external onRepay
_(no internal calls)_


### public onSetAnnualInterestAndReserveRatioBips
_(no internal calls)_


### external onSetMaxTotalSupply
_(no internal calls)_


### external onSetProtocolFeeBips
_(no internal calls)_


### external onTransfer
-> internal _tryValidateAccessInner
  -> internal _handleHooksData
    -> internal _readAddress
    -> internal _tryGetCredential
    -> internal _tryValidateCredential
      -> internal _readAddress
  -> internal _tryGetCredential
  -> internal _loopTryGetCredential
    -> internal _tryGetCredential
-> internal _writeLenderStatus


### external removeRoleProvider
-> internal _removePullProvider


### external revokeRole
_(no internal calls)_


### external setFixedTermEndTime
_(no internal calls)_


### external setMinimumDeposit
_(no internal calls)_


### external unblockFromDeposits
_(no internal calls)_


### external version
_(no internal calls)_


---

## HooksFactory

_File: src/HooksFactory.sol_

### external addHooksTemplate
-> internal _validateFees


### external archController
_(no internal calls)_


### external changeSphereXEngine
-> internal _getAddress
-> internal _setAddress


### external computeMarketAddress
-> library LibStoredInitCode.calculateCreate2Address


### external deployHooksInstance
-> internal _deployHooksInstance


### external deployMarket
-> internal _deployMarket
  -> library LibStoredInitCode.calculateCreate2Address
  -> internal _packString
  -> internal _setTmpMarketParameters
  -> library LibStoredInitCode.create2WithStoredInitCode


### external deployMarketAndHooks
-> internal _deployHooksInstance
-> internal _deployMarket
  -> library LibStoredInitCode.calculateCreate2Address
  -> internal _packString
  -> internal _setTmpMarketParameters
  -> library LibStoredInitCode.create2WithStoredInitCode


### external disableHooksTemplate
_(no internal calls)_


### external getHooksInstancesCountForBorrower
_(no internal calls)_


### external getHooksInstancesForBorrower
_(no internal calls)_


### external getHooksTemplateDetails
_(no internal calls)_


### external getHooksTemplates
-> library MathUtils.min


### external getHooksTemplatesCount
_(no internal calls)_


### external getMarketParameters
-> internal _getTmpMarketParameters
-> public sphereXEngine
  -> internal _getAddress


### external getMarketsForHooksInstance
-> library MathUtils.min


### external getMarketsForHooksInstanceCount
_(no internal calls)_


### external getMarketsForHooksTemplate
-> library MathUtils.min


### external getMarketsForHooksTemplateCount
_(no internal calls)_


### external isHooksInstance
_(no internal calls)_


### external isHooksTemplate
_(no internal calls)_


### external name
_(no internal calls)_


### external pushProtocolFeeBipsUpdates
-> external pushProtocolFeeBipsUpdates


### external registerWithArchController
_(no internal calls)_


### public sphereXEngine
-> internal _getAddress


### public sphereXOperator
_(no internal calls)_


### external updateHooksTemplateFees
-> internal _validateFees


---

## IHooks

_File: src/access/IHooks.sol_

### external onCreateMarket
_(no internal calls)_


---

## MarketConstraintHooks

_File: src/access/MarketConstraintHooks.sol_

### external getParameterConstraints
_(no internal calls)_


### external onCreateMarket
-> internal _onCreateMarket
  -> internal enforceParameterConstraints
    -> internal assertValueInRange


### public onSetAnnualInterestAndReserveRatioBips
-> internal assertValueInRange
-> internal _calculateTemporaryReserveRatioBips
  -> library MathUtils.mulDiv
  -> library MathUtils.min
  -> library MathUtils.max


---

## MarketLens

_File: src/lens/MarketLens.sol_

### public getAllHooksTemplatesForBorrower
-> public getHooksTemplatesForBorrower


### external getAllMarketsDataForHooksTemplate
-> public getMarketsData


### public getHooksDataForBorrower
_(no internal calls)_


### public getHooksInstancesForBorrower
_(no internal calls)_


### public getHooksTemplateForBorrower
_(no internal calls)_


### public getHooksTemplatesForBorrower
_(no internal calls)_


### external getLenderAccountData
_(no internal calls)_


### public getMarketData
_(no internal calls)_


### public getMarketDataWithLenderStatus
_(no internal calls)_


### public getMarketsData
_(no internal calls)_


### public getMarketsDataWithLenderStatus
_(no internal calls)_


### external getMarketsForHooksTemplateCount
_(no internal calls)_


### public getPaginatedMarketsDataForHooksTemplate
-> public getMarketsData


### public getTokenInfo
_(no internal calls)_


### public getTokensInfo
_(no internal calls)_


### public getWithdrawalBatchData
_(no internal calls)_


### external getWithdrawalBatchDataWithLenderStatus
_(no internal calls)_


### external getWithdrawalBatchDataWithLendersStatus
_(no internal calls)_


### public getWithdrawalBatchesData
_(no internal calls)_


### external getWithdrawalBatchesDataWithLenderStatus
_(no internal calls)_


### external queryLenderAccount
_(no internal calls)_


### external queryLenderAccounts
_(no internal calls)_


---

## SphereXConfig

_File: src/spherex/SphereXConfig.sol_

### public acceptSphereXAdminRole
-> public pendingSphereXAdmin
  -> internal _getAddress
-> public sphereXAdmin
  -> internal _getAddress
-> internal _setAddress


### external changeSphereXEngine
-> internal _getAddress
-> internal _setSphereXEngine
  -> internal _setAddress


### external changeSphereXOperator
-> internal _getAddress
-> internal _setAddress


### public pendingSphereXAdmin
-> internal _getAddress


### public sphereXAdmin
-> internal _getAddress


### public sphereXEngine
-> internal _getAddress


### public sphereXOperator
-> internal _getAddress


### public transferSphereXAdminRole
-> internal _setAddress
-> public sphereXAdmin
  -> internal _getAddress


---

## SphereXProtectedRegisteredBase

_File: src/spherex/SphereXProtectedRegisteredBase.sol_

### external changeSphereXEngine
-> internal _getAddress
-> internal _setAddress


### public sphereXEngine
-> internal _getAddress


### public sphereXOperator
_(no internal calls)_


---

## WildcatArchController

_File: src/WildcatArchController.sol_

### public acceptSphereXAdminRole
-> public pendingSphereXAdmin
  -> internal _getAddress
-> public sphereXAdmin
  -> internal _getAddress
-> internal _setAddress


### external addBlacklist
_(no internal calls)_


### external changeSphereXEngine
-> internal _getAddress
-> internal _setSphereXEngine
  -> internal _setAddress


### external changeSphereXOperator
-> internal _getAddress
-> internal _setAddress


### external getBlacklistedAssets
-> library MathUtils.min


### external getBlacklistedAssetsCount
_(no internal calls)_


### external getRegisteredBorrowers
-> library MathUtils.min


### external getRegisteredBorrowersCount
_(no internal calls)_


### external getRegisteredControllerFactories
-> library MathUtils.min


### external getRegisteredControllerFactoriesCount
_(no internal calls)_


### external getRegisteredControllers
-> library MathUtils.min


### external getRegisteredControllersCount
_(no internal calls)_


### external getRegisteredMarkets
-> library MathUtils.min


### external getRegisteredMarketsCount
_(no internal calls)_


### external isBlacklistedAsset
_(no internal calls)_


### external isRegisteredBorrower
_(no internal calls)_


### external isRegisteredController
_(no internal calls)_


### external isRegisteredControllerFactory
_(no internal calls)_


### external isRegisteredMarket
_(no internal calls)_


### public pendingSphereXAdmin
-> internal _getAddress


### external registerBorrower
_(no internal calls)_


### external registerController
-> internal _addAllowedSenderOnChain
  -> public sphereXEngine
    -> internal _getAddress


### external registerControllerFactory
-> internal _addAllowedSenderOnChain
  -> public sphereXEngine
    -> internal _getAddress


### external registerMarket
-> internal _addAllowedSenderOnChain
  -> public sphereXEngine
    -> internal _getAddress


### external removeBlacklist
_(no internal calls)_


### external removeBorrower
_(no internal calls)_


### external removeController
_(no internal calls)_


### external removeControllerFactory
_(no internal calls)_


### external removeMarket
_(no internal calls)_


### public sphereXAdmin
-> internal _getAddress


### public sphereXEngine
-> internal _getAddress


### public sphereXOperator
-> internal _getAddress


### public transferSphereXAdminRole
-> internal _setAddress
-> public sphereXAdmin
  -> internal _getAddress


### external updateSphereXEngineOnRegisteredContracts
-> public sphereXEngine
  -> internal _getAddress
-> internal _updateSphereXEngineOnRegisteredContractsInSet
  -> internal _callWith


---

## WildcatMarket

_File: src/market/WildcatMarket.sol_

### external accruedProtocolFees
_(no internal calls)_


### external annualInterestBips
_(no internal calls)_


### external approve
-> internal _approve


### external archController
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external borrow
-> internal _isFlaggedByChainalysis
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> public totalAssets
-> internal _writeState
  -> public totalAssets


### external borrowableAssets
-> public totalAssets


### external closeMarket
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> public totalAssets
-> internal _repay
-> internal _applyWithdrawalBatchPayment
  -> library MathUtils.min
  -> library MathUtils.mulDiv
  -> internal _runtimeConstant
-> internal _processUnpaidWithdrawalBatch
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external collectFees
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> public totalAssets
-> internal _writeState
  -> public totalAssets


### external coverageLiquidity
_(no internal calls)_


### external currentState
_(no internal calls)_


### external deposit
-> internal _depositUpTo
  -> internal _getUpdatedState
    -> internal _processExpiredWithdrawalBatch
      -> public totalAssets
      -> internal _applyWithdrawalBatchPayment
        -> library MathUtils.min
        -> library MathUtils.mulDiv
        -> internal _runtimeConstant
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> library MathUtils.min
  -> internal _getAccount
    -> internal _isSanctioned
  -> internal _runtimeConstant
  -> internal _writeState
    -> public totalAssets


### external depositUpTo
-> internal _depositUpTo
  -> internal _getUpdatedState
    -> internal _processExpiredWithdrawalBatch
      -> public totalAssets
      -> internal _applyWithdrawalBatchPayment
        -> library MathUtils.min
        -> library MathUtils.mulDiv
        -> internal _runtimeConstant
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> library MathUtils.min
  -> internal _getAccount
    -> internal _isSanctioned
  -> internal _runtimeConstant
  -> internal _writeState
    -> public totalAssets


### public executeWithdrawal
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _executeWithdrawal
  -> library MathUtils.mulDiv
  -> internal _isSanctioned
  -> internal _createEscrowForUnderlyingAsset
-> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external executeWithdrawals
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _executeWithdrawal
  -> library MathUtils.mulDiv
  -> internal _isSanctioned
  -> internal _createEscrowForUnderlyingAsset
-> internal _writeState
  -> public totalAssets


### external getAccountWithdrawalStatus
_(no internal calls)_


### external getAvailableWithdrawalAmount
-> internal _calculateCurrentState
  -> public totalAssets
  -> internal _applyWithdrawalBatchPaymentView


### external getUnpaidBatchExpiries
_(no internal calls)_


### external getWithdrawalBatch
-> internal _calculateCurrentState
  -> public totalAssets
  -> internal _applyWithdrawalBatchPaymentView


### external isClosed
_(no internal calls)_


### external maxTotalSupply
_(no internal calls)_


### external maximumDeposit
_(no internal calls)_


### external name
_(no internal calls)_


### external nukeFromOrbit
-> internal _isSanctioned
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _blockAccount
  -> internal _queueWithdrawal
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
    -> internal _writeState
      -> public totalAssets
-> internal _writeState
  -> public totalAssets


### external previousState
_(no internal calls)_


### external queueFullWithdrawal
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _getAccount
  -> internal _isSanctioned
-> internal _queueWithdrawal
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
  -> internal _writeState
    -> public totalAssets
-> internal _runtimeConstant


### external queueWithdrawal
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _getAccount
  -> internal _isSanctioned
-> internal _queueWithdrawal
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
  -> internal _writeState
    -> public totalAssets
-> internal _runtimeConstant


### external repay
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### public repayAndProcessUnpaidWithdrawalBatches
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _runtimeConstant
-> public totalAssets
-> library MathUtils.min
-> internal _processUnpaidWithdrawalBatch
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external rescueTokens
_(no internal calls)_


### external reserveRatioBips
_(no internal calls)_


### external scaleFactor
_(no internal calls)_


### external scaledBalanceOf
_(no internal calls)_


### external scaledTotalSupply
_(no internal calls)_


### external setAnnualInterestAndReserveRatioBips
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> public totalAssets
-> internal _writeState
  -> public totalAssets


### external setMaxTotalSupply
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external setProtocolFeeBips
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external symbol
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### external totalDebts
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### external transfer
-> internal _transfer
  -> internal _getUpdatedState
    -> internal _processExpiredWithdrawalBatch
      -> public totalAssets
      -> internal _applyWithdrawalBatchPayment
        -> library MathUtils.min
        -> library MathUtils.mulDiv
        -> internal _runtimeConstant
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> internal _getAccount
    -> internal _isSanctioned
  -> internal _writeState
    -> public totalAssets


### external transferFrom
-> internal _approve
-> internal _transfer
  -> internal _getUpdatedState
    -> internal _processExpiredWithdrawalBatch
      -> public totalAssets
      -> internal _applyWithdrawalBatchPayment
        -> library MathUtils.min
        -> library MathUtils.mulDiv
        -> internal _runtimeConstant
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> internal _getAccount
    -> internal _isSanctioned
  -> internal _writeState
    -> public totalAssets


### external updateState
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external version
_(no internal calls)_


### external withdrawableProtocolFees
-> public totalAssets


---

## WildcatMarketBase

_File: src/market/WildcatMarketBase.sol_

### external accruedProtocolFees
_(no internal calls)_


### external archController
_(no internal calls)_


### external borrowableAssets
-> public totalAssets


### external changeSphereXEngine
-> internal _getAddress
-> internal _setAddress


### external coverageLiquidity
_(no internal calls)_


### external currentState
_(no internal calls)_


### external name
_(no internal calls)_


### external previousState
_(no internal calls)_


### external scaleFactor
_(no internal calls)_


### external scaledBalanceOf
_(no internal calls)_


### external scaledTotalSupply
_(no internal calls)_


### public sphereXEngine
-> internal _getAddress


### public sphereXOperator
_(no internal calls)_


### external symbol
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### external totalDebts
_(no internal calls)_


### external version
_(no internal calls)_


### external withdrawableProtocolFees
-> public totalAssets


---

## WildcatMarketConfig

_File: src/market/WildcatMarketConfig.sol_

### external accruedProtocolFees
_(no internal calls)_


### external annualInterestBips
_(no internal calls)_


### external archController
_(no internal calls)_


### external borrowableAssets
-> public totalAssets


### external coverageLiquidity
_(no internal calls)_


### external currentState
_(no internal calls)_


### external isClosed
_(no internal calls)_


### external maxTotalSupply
_(no internal calls)_


### external maximumDeposit
_(no internal calls)_


### external name
_(no internal calls)_


### external nukeFromOrbit
-> internal _isSanctioned
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _blockAccount
-> internal _writeState
  -> public totalAssets


### external previousState
_(no internal calls)_


### external reserveRatioBips
_(no internal calls)_


### external scaleFactor
_(no internal calls)_


### external scaledBalanceOf
_(no internal calls)_


### external scaledTotalSupply
_(no internal calls)_


### external setAnnualInterestAndReserveRatioBips
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> public totalAssets
-> internal _writeState
  -> public totalAssets


### external setMaxTotalSupply
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external setProtocolFeeBips
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external symbol
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### external totalDebts
_(no internal calls)_


### external version
_(no internal calls)_


### external withdrawableProtocolFees
-> public totalAssets


---

## WildcatMarketToken

_File: src/market/WildcatMarketToken.sol_

### external accruedProtocolFees
_(no internal calls)_


### external approve
-> internal _approve


### external archController
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external borrowableAssets
-> public totalAssets


### external coverageLiquidity
_(no internal calls)_


### external currentState
_(no internal calls)_


### external name
_(no internal calls)_


### external previousState
_(no internal calls)_


### external scaleFactor
_(no internal calls)_


### external scaledBalanceOf
_(no internal calls)_


### external scaledTotalSupply
_(no internal calls)_


### external symbol
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### external totalDebts
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### external transfer
-> internal _transfer
  -> internal _getUpdatedState
    -> internal _processExpiredWithdrawalBatch
      -> public totalAssets
      -> internal _applyWithdrawalBatchPayment
        -> library MathUtils.min
        -> library MathUtils.mulDiv
        -> internal _runtimeConstant
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> internal _getAccount
    -> internal _isSanctioned
  -> internal _writeState
    -> public totalAssets


### external transferFrom
-> internal _approve
-> internal _transfer
  -> internal _getUpdatedState
    -> internal _processExpiredWithdrawalBatch
      -> public totalAssets
      -> internal _applyWithdrawalBatchPayment
        -> library MathUtils.min
        -> library MathUtils.mulDiv
        -> internal _runtimeConstant
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> internal _getAccount
    -> internal _isSanctioned
  -> internal _writeState
    -> public totalAssets


### external version
_(no internal calls)_


### external withdrawableProtocolFees
-> public totalAssets


---

## WildcatMarketWithdrawals

_File: src/market/WildcatMarketWithdrawals.sol_

### external accruedProtocolFees
_(no internal calls)_


### external archController
_(no internal calls)_


### external borrowableAssets
-> public totalAssets


### external coverageLiquidity
_(no internal calls)_


### external currentState
_(no internal calls)_


### public executeWithdrawal
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _executeWithdrawal
  -> library MathUtils.mulDiv
  -> internal _isSanctioned
  -> internal _createEscrowForUnderlyingAsset
-> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external executeWithdrawals
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _executeWithdrawal
  -> library MathUtils.mulDiv
  -> internal _isSanctioned
  -> internal _createEscrowForUnderlyingAsset
-> internal _writeState
  -> public totalAssets


### external getAccountWithdrawalStatus
_(no internal calls)_


### external getAvailableWithdrawalAmount
-> internal _calculateCurrentState
  -> public totalAssets
  -> internal _applyWithdrawalBatchPaymentView


### external getUnpaidBatchExpiries
_(no internal calls)_


### external getWithdrawalBatch
-> internal _calculateCurrentState
  -> public totalAssets
  -> internal _applyWithdrawalBatchPaymentView


### external name
_(no internal calls)_


### external previousState
_(no internal calls)_


### external queueFullWithdrawal
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _getAccount
  -> internal _isSanctioned
-> internal _queueWithdrawal
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
  -> internal _writeState
    -> public totalAssets
-> internal _runtimeConstant


### external queueWithdrawal
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _getAccount
  -> internal _isSanctioned
-> internal _queueWithdrawal
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
  -> internal _writeState
    -> public totalAssets
-> internal _runtimeConstant


### public repayAndProcessUnpaidWithdrawalBatches
-> internal _getUpdatedState
  -> internal _processExpiredWithdrawalBatch
    -> public totalAssets
    -> internal _applyWithdrawalBatchPayment
      -> library MathUtils.min
      -> library MathUtils.mulDiv
      -> internal _runtimeConstant
  -> public totalAssets
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _runtimeConstant
-> public totalAssets
-> library MathUtils.min
-> internal _processUnpaidWithdrawalBatch
  -> internal _applyWithdrawalBatchPayment
    -> library MathUtils.min
    -> library MathUtils.mulDiv
    -> internal _runtimeConstant
-> internal _writeState
  -> public totalAssets


### external scaleFactor
_(no internal calls)_


### external scaledBalanceOf
_(no internal calls)_


### external scaledTotalSupply
_(no internal calls)_


### external symbol
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### external totalDebts
_(no internal calls)_


### external version
_(no internal calls)_


### external withdrawableProtocolFees
-> public totalAssets


---

## WildcatSanctionsEscrow

_File: src/WildcatSanctionsEscrow.sol_

### public balance
_(no internal calls)_


### public canReleaseEscrow
_(no internal calls)_


### public escrowedAsset
_(no internal calls)_


### public releaseEscrow
-> public canReleaseEscrow


---

## WildcatSanctionsSentinel

_File: src/WildcatSanctionsSentinel.sol_

### public createEscrow
-> public getEscrowAddress
  -> internal _deriveSalt
-> internal _deriveSalt
-> internal _resetTmpEscrowParams


### public getEscrowAddress
-> internal _deriveSalt


### public isFlaggedByChainalysis
_(no internal calls)_


### public isSanctioned
-> public isFlaggedByChainalysis


### public overrideSanction
_(no internal calls)_


### public removeSanctionOverride
_(no internal calls)_

