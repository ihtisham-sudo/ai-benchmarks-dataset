# Callpaths — GMX_V2

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AdlHandler

_File: contracts/exchange/AdlHandler.sol_

### external executeAdl
-> library AdlUtils.validateAdl
-> library MarketUtils.isPnlFactorExceeded
-> library Errors.AdlNotRequired
-> library AdlUtils.createAdlOrder
-> library AdlUtils.CreateAdlOrderParams
-> library OrderStoreUtils.get
-> internal _getExecuteOrderParams
  -> library MarketUtils.getSwapPathMarkets
  -> library MarketUtils.getEnabledMarket
-> library FeatureUtils.validateFeature
-> library Keys.executeAdlFeatureDisabledKey
-> library ExecuteOrderUtils.executeOrder
-> library MarketUtils.getPnlToPoolFactor
-> library Errors.InvalidAdl
-> library MarketUtils.getMinPnlFactorAfterAdl
-> library Errors.PnlOvercorrected


### external updateAdlState
-> library AdlUtils.updateAdlState


---

## AutoCancelSyncer

_File: contracts/config/AutoCancelSyncer.sol_

### external multicall
-> library ErrorUtils.revertWithParsedMessage


### external syncAutoCancelOrderListForAccount
-> library PositionStoreUtils.getAccountPositionKeys
-> internal _syncAutoCancelOrderListForPosition
  -> library AutoCancelUtils.getAutoCancelOrderKeys
  -> library OrderStoreUtils.get
  -> library AutoCancelUtils.removeAutoCancelOrderKey
  -> library Cast.toBytes32


### external syncAutoCancelOrderListForPosition
-> internal _syncAutoCancelOrderListForPosition
  -> library AutoCancelUtils.getAutoCancelOrderKeys
  -> library OrderStoreUtils.get
  -> library AutoCancelUtils.removeAutoCancelOrderKey
  -> library Cast.toBytes32


---

## Bank

_File: contracts/bank/Bank.sol_

### external transferOut
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut
-> internal _transferOut
  -> library Errors.SelfTransferNotSupported
  -> internal _afterTransferOut


### external transferOutNativeToken
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut


---

## BaseGelatoRelayRouter

_File: contracts/router/relay/BaseGelatoRelayRouter.sol_

### external sendNativeToken
-> library AccountUtils.validateReceiver
-> library TokenUtils.sendNativeToken


### external sendTokens
-> library AccountUtils.validateReceiver


### external sendWnt
-> library AccountUtils.validateReceiver
-> library TokenUtils.depositAndSendWrappedNativeToken


---

## BaseRouter

_File: contracts/router/BaseRouter.sol_

### external multicall
-> library ErrorUtils.revertWithParsedMessage


### external sendNativeToken
-> library AccountUtils.validateReceiver
-> library TokenUtils.sendNativeToken


### external sendTokens
-> library AccountUtils.validateReceiver


### external sendWnt
-> library AccountUtils.validateReceiver
-> library TokenUtils.depositAndSendWrappedNativeToken


---

## BasicMulticall

_File: contracts/utils/BasicMulticall.sol_

### external multicall
-> library ErrorUtils.revertWithParsedMessage


---

## ChainReader

_File: contracts/chain/ChainReader.sol_

### public getBlockHash
_(no internal calls)_


### external getBlockHashAndLatestBlockNumber
-> public getBlockHash
-> public getBlockNumber


### external getBlockHashWithDelayAndLatestBlockNumber
-> public getBlockNumber


### public getBlockNumber
_(no internal calls)_


### public updateLatestBlockHash
-> public getBlockHash
-> public getBlockNumber


### public updateLatestBlockHashWithDelay
-> public updateLatestBlockHash
  -> public getBlockHash
  -> public getBlockNumber
-> public getBlockNumber


---

## ChainlinkDataStreamProvider

_File: contracts/oracle/ChainlinkDataStreamProvider.sol_

### external getOraclePrice
-> library Keys.dataStreamIdKey
-> library Errors.EmptyDataStreamFeedId
-> internal _getPayloadParameter
-> library Errors.InvalidDataStreamFeedId
-> library Errors.InvalidDataStreamPrices
-> library Errors.InvalidDataStreamBidAsk
-> internal _getDataStreamMultiplier
  -> library Keys.dataStreamMultiplierKey
  -> library Errors.EmptyDataStreamMultiplier
-> library Precision.mulDiv
-> internal _getDataStreamSpreadReductionFactor
  -> library Keys.dataStreamSpreadReductionFactorKey
  -> library Errors.InvalidDataStreamSpreadReductionFactor
-> library Precision.applyFactor
-> library OracleUtils.ValidatedPrice


### external isChainlinkOnChainProvider
_(no internal calls)_


### external shouldAdjustTimestamp
_(no internal calls)_


---

## ChainlinkPriceFeedProvider

_File: contracts/oracle/ChainlinkPriceFeedProvider.sol_

### external getOraclePrice
-> library ChainlinkPriceFeedUtils.getPriceFeedPrice
-> library Errors.EmptyChainlinkPriceFeed
-> library Keys.stablePriceKey
-> library Price.Props
-> library OracleUtils.ValidatedPrice
-> library Chain.currentTimestamp


### external isChainlinkOnChainProvider
_(no internal calls)_


### external shouldAdjustTimestamp
_(no internal calls)_


---

## ClaimHandler

_File: contracts/claim/ClaimHandler.sol_

### external acceptTermsAndClaim
-> library Errors.InvalidParams
-> internal _validateNonEmptyReceiver
  -> library Errors.EmptyReceiver
-> library FeatureUtils.validateFeature
-> library Keys.generalClaimFeatureDisabled
-> library ClaimUtils._validateNonEmptyToken
-> library ClaimUtils._validateNonZeroDistributionId
-> internal _validateTermsSignature
  -> library Keys.claimTermsKey
  -> library StringUtils.compareStrings
  -> library Errors.InvalidClaimTermsSignature
  -> library SafeUtils.getMessageHash
  -> library Errors.InvalidClaimTermsSignatureForContract
-> library Keys.claimableFundsAmountKey
-> library Errors.EmptyClaimableAmount
-> library Keys.totalClaimableFundsAmountKey
-> library ClaimEventUtils.emitClaimFundsClaimed
-> library ClaimUtils._validateTotalClaimableFundsAmount


### external depositFunds
-> library ClaimUtils.incrementClaims
-> library Keys.totalClaimableFundsAmountKey
-> library ClaimUtils._validateTotalClaimableFundsAmount


### external getClaimableAmount
-> library Keys.claimableFundsAmountKey


### external getTotalClaimableAmount
-> library Keys.totalClaimableFundsAmountKey


### external removeTerms
-> library Keys.claimTermsKey
-> library Errors.InvalidParams
-> library Keys.claimTermsBackrefKey
-> library ClaimEventUtils.emitClaimTermsRemoved


### external setTerms
-> library ClaimUtils._validateNonZeroDistributionId
-> library Errors.InvalidParams
-> library Keys.claimTermsBackrefKey
-> library Errors.DuplicateClaimTerms
-> library Keys.claimTermsKey
-> library ClaimEventUtils.emitClaimTermsSet


### external transferClaim
-> library Errors.InvalidParams
-> library ClaimUtils._validateNonEmptyToken
-> library ClaimUtils._validateNonEmptyAccount
-> internal _validateNonEmptyReceiver
  -> library Errors.EmptyReceiver
-> library ClaimUtils._validateNonZeroDistributionId
-> library Keys.claimableFundsAmountKey
-> library ClaimEventUtils.emitClaimFundsTransferred
-> library ClaimUtils._validateTotalClaimableFundsAmount


### external withdrawFunds
-> library ClaimUtils._validateNonEmptyToken
-> internal _validateNonEmptyReceiver
  -> library Errors.EmptyReceiver
-> library Errors.InvalidParams
-> library ClaimUtils._validateNonEmptyAccount
-> library ClaimUtils._validateNonZeroDistributionId
-> library Keys.claimableFundsAmountKey
-> library ClaimEventUtils.emitClaimFundsWithdrawn
-> library Keys.totalClaimableFundsAmountKey
-> library ClaimUtils._validateTotalClaimableFundsAmount


---

## ClaimVault

_File: contracts/claim/ClaimVault.sol_

### external transferOut
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut
-> internal _transferOut
  -> library Errors.SelfTransferNotSupported
  -> internal _afterTransferOut


### external transferOutNativeToken
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut


---

## Config

_File: contracts/config/Config.sol_

### external initOracleConfig
-> library ConfigUtils.initOracleConfig


### external initOracleProviderForToken
-> library Errors.EmptyToken
-> library Keys.oracleProviderForTokenKey
-> library Errors.OracleProviderAlreadyExistsForToken
-> library Keys.isOracleProviderEnabledKey
-> library Errors.InvalidOracleProvider


### external multicall
-> library ErrorUtils.revertWithParsedMessage


### external setAddress
-> internal _validateKey
  -> library Errors.InvalidBaseKey
-> library Keys.getFullKey


### external setBool
-> internal _validateKey
  -> library Errors.InvalidBaseKey
-> library Keys.getFullKey


### external setBytes32
-> internal _validateKey
  -> library Errors.InvalidBaseKey
-> library Keys.getFullKey


### external setClaimableCollateralFactorForAccount
-> library ConfigUtils.setClaimableCollateralFactorForAccount


### external setClaimableCollateralFactorForTime
-> library ConfigUtils.setClaimableCollateralFactorForTime


### external setClaimableCollateralReductionFactorForAccount
-> library ConfigUtils.setClaimableCollateralReductionFactorForAccount


### external setInt
-> internal _validateKey
  -> library Errors.InvalidBaseKey
-> library Keys.getFullKey


### external setOracleProviderForFeeHandlerToken
-> library Errors.EmptyToken
-> library Keys.isOracleProviderEnabledKey
-> library Errors.InvalidOracleProvider
-> library Chain.currentTimestamp
-> library Keys.oracleProviderUpdatedAt
-> library Errors.OracleProviderMinChangeDelayNotYetPassed
-> library Keys.oracleProviderForTokenKey


### external setOracleProviderForToken
-> library Errors.EmptyToken
-> library Keys.isOracleProviderEnabledKey
-> library Errors.InvalidOracleProvider
-> library Chain.currentTimestamp
-> library Keys.oracleProviderUpdatedAt
-> library Errors.OracleProviderMinChangeDelayNotYetPassed
-> library Keys.oracleProviderForTokenKey


### external setPositionImpactDistributionRate
-> library ConfigUtils.setPositionImpactDistributionRate


### external setUint
-> internal _validateKey
  -> library Errors.InvalidBaseKey
-> library Keys.getFullKey
-> library ConfigUtils.validateRange


---

## ConfigSyncer

_File: contracts/config/ConfigSyncer.sol_

### external sync
-> library FeatureUtils.validateFeature
-> library Keys.syncConfigFeatureDisabledKey
-> library Errors.SyncConfigInvalidInputLengths
-> library Keys.syncConfigLatestUpdateIdKey
-> library Keys.syncConfigMarketDisabledKey
-> library Errors.SyncConfigUpdatesDisabledForMarket
-> library Keys.syncConfigParameterDisabledKey
-> library Errors.SyncConfigUpdatesDisabledForParameter
-> library Keys.syncConfigMarketParameterDisabledKey
-> library Errors.SyncConfigUpdatesDisabledForMarketParameter
-> internal _validateMarketInData
  -> library Errors.SyncConfigInvalidMarketFromData
-> internal _validateKey
  -> library Errors.InvalidBaseKey
-> library Keys.getFullKey
-> library Cast.bytesToUint256
-> library Keys.syncConfigUpdateCompletedKey


---

## ConfigTimelockController

_File: contracts/config/ConfigTimelockController.sol_

### external executeWithOraclePrices
_(no internal calls)_


### external reduceLentImpactAmount
-> library PositionImpactPoolUtils.reduceLentAmount


### external withdrawFromPositionImpactPool
-> library PositionImpactPoolUtils.withdrawFromPositionImpactPool


---

## ContributorHandler

_File: contracts/contributor/ContributorHandler.sol_

### external addContributorAccount
_(no internal calls)_


### external addContributorToken
_(no internal calls)_


### external multicall
-> library ErrorUtils.revertWithParsedMessage


### external removeContributorAccount
_(no internal calls)_


### external removeContributorToken
_(no internal calls)_


### external sendPayments
-> library Chain.currentTimestamp
-> library Errors.MinContributorPaymentIntervalNotYetPassed
-> library Keys.contributorFundingAccountKey
-> library Keys.customContributorFundingAccountKey
-> library Keys.contributorTokenAmountKey
-> library Cast.toBytes32


### external setContributorAmount
-> library Errors.InvalidSetContributorPaymentInput
-> library Errors.InvalidContributorToken
-> library Keys.contributorTokenAmountKey
-> library Cast.toBytes32
-> internal _validateMaxContributorTokenAmounts
  -> library Keys.contributorTokenAmountKey
  -> library Keys.maxTotalContributorTokenAmountKey
  -> library Errors.MaxTotalContributorTokenAmountExceeded


### external setContributorFundingAccount
-> library Keys.contributorFundingAccountKey


### external setCustomContributorFundingAccount
-> library Keys.customContributorFundingAccountKey


### external setMaxTotalContributorTokenAmount
-> library Errors.InvalidSetMaxTotalContributorTokenAmountInput
-> library Errors.InvalidContributorToken
-> library Keys.maxTotalContributorTokenAmountKey
-> internal _validateMaxContributorTokenAmounts
  -> library Keys.contributorTokenAmountKey
  -> library Keys.maxTotalContributorTokenAmountKey
  -> library Errors.MaxTotalContributorTokenAmountExceeded


### external setMinContributorPaymentInterval
-> library Errors.MinContributorPaymentIntervalBelowAllowedRange


---

## DataStore

_File: contracts/data/DataStore.sol_

### external addAddress
_(no internal calls)_


### external addBytes32
_(no internal calls)_


### external addUint
_(no internal calls)_


### external applyBoundedDeltaToUint
-> library Calc.sumReturnUint256


### external applyDeltaToInt
_(no internal calls)_


### external applyDeltaToUint
_(no internal calls)_


### external containsAddress
_(no internal calls)_


### external containsBytes32
_(no internal calls)_


### external containsUint
_(no internal calls)_


### external decrementInt
_(no internal calls)_


### external decrementUint
_(no internal calls)_


### external getAddress
_(no internal calls)_


### external getAddressArray
_(no internal calls)_


### external getAddressCount
_(no internal calls)_


### external getAddressValuesAt
_(no internal calls)_


### external getBool
_(no internal calls)_


### external getBoolArray
_(no internal calls)_


### external getBytes32
_(no internal calls)_


### external getBytes32Array
_(no internal calls)_


### external getBytes32Count
_(no internal calls)_


### external getBytes32ValuesAt
_(no internal calls)_


### external getInt
_(no internal calls)_


### external getIntArray
_(no internal calls)_


### external getString
_(no internal calls)_


### external getStringArray
_(no internal calls)_


### external getUint
_(no internal calls)_


### external getUintArray
_(no internal calls)_


### external getUintCount
_(no internal calls)_


### external getUintValuesAt
_(no internal calls)_


### external incrementInt
_(no internal calls)_


### external incrementUint
_(no internal calls)_


### external removeAddress
_(no internal calls)_


### external removeAddressArray
_(no internal calls)_


### external removeBool
_(no internal calls)_


### external removeBoolArray
_(no internal calls)_


### external removeBytes32
_(no internal calls)_


### external removeBytes32Array
_(no internal calls)_


### external removeInt
_(no internal calls)_


### external removeIntArray
_(no internal calls)_


### external removeString
_(no internal calls)_


### external removeStringArray
_(no internal calls)_


### external removeUint
_(no internal calls)_


### external removeUintArray
_(no internal calls)_


### external setAddress
_(no internal calls)_


### external setAddressArray
_(no internal calls)_


### external setBool
_(no internal calls)_


### external setBoolArray
_(no internal calls)_


### external setBytes32
_(no internal calls)_


### external setBytes32Array
_(no internal calls)_


### external setInt
_(no internal calls)_


### external setIntArray
_(no internal calls)_


### external setString
_(no internal calls)_


### external setStringArray
_(no internal calls)_


### external setUint
_(no internal calls)_


### external setUintArray
_(no internal calls)_


---

## DecreaseOrderExecutor

_File: contracts/order/DecreaseOrderExecutor.sol_

### external processOrder
-> library DecreaseOrderUtils.processOrder


---

## DepositHandler

_File: contracts/exchange/DepositHandler.sol_

### external _executeDeposit
-> library FeatureUtils.validateFeature
-> library Keys.executeDepositFeatureDisabledKey
-> external_callback IExecuteDepositUtils.ExecuteDepositParams
-> library ExecuteDepositUtils.executeDeposit
  -> library DepositStoreUtils.get
  -> library GasUtils.estimateExecuteDepositGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleDepositError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library DepositUtils.cancelDeposit
      -> library DepositStoreUtils.get
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelDepositFeatureDisabledKey
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library DepositUtils.cancelDeposit


### external cancelDeposit
-> library DepositStoreUtils.get
-> library FeatureUtils.validateFeature
-> library Keys.cancelDepositFeatureDisabledKey
-> internal validateRequestCancellation
  -> library Chain.currentTimestamp
  -> library Errors.RequestNotYetCancellable
-> library DepositUtils.cancelDeposit


### external createDeposit
-> library FeatureUtils.validateFeature
-> library Keys.createDepositFeatureDisabledKey
-> internal validateDataListLength
  -> library Errors.MaxDataListLengthExceeded
-> library DepositUtils.createDeposit


### external executeDeposit
-> library DepositStoreUtils.get
-> library GasUtils.estimateExecuteDepositGasLimit
-> library GasUtils.validateExecutionGas
-> library GasUtils.getExecutionGas
-> internal _handleDepositError
  -> library GasUtils.validateExecutionErrorGas
  -> library ErrorUtils.getErrorSelectorFromData
  -> internal validateNonKeeperError
    -> library OracleUtils.isOracleError
    -> library ErrorUtils.revertWithCustomError
  -> library ErrorUtils.getRevertMessage
  -> library DepositUtils.cancelDeposit
    -> library DepositStoreUtils.get
    -> library FeatureUtils.validateFeature
    -> library Keys.cancelDepositFeatureDisabledKey
    -> internal validateRequestCancellation
      -> library Chain.currentTimestamp
      -> library Errors.RequestNotYetCancellable
    -> library DepositUtils.cancelDeposit


### external executeDepositFromController
-> library FeatureUtils.validateFeature
-> library Keys.executeDepositFeatureDisabledKey
-> library ExecuteDepositUtils.executeDeposit
  -> library DepositStoreUtils.get
  -> library GasUtils.estimateExecuteDepositGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleDepositError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library DepositUtils.cancelDeposit
      -> library DepositStoreUtils.get
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelDepositFeatureDisabledKey
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library DepositUtils.cancelDeposit


### external simulateExecuteDeposit
-> library DepositStoreUtils.get


---

## DepositVault

_File: contracts/deposit/DepositVault.sol_

### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_


---

## EdgeDataStreamProvider

_File: contracts/oracle/EdgeDataStreamProvider.sol_

### external getOraclePrice
-> library Keys.edgeDataStreamIdKey
-> library Errors.EmptyDataStreamFeedId
-> library Errors.InvalidDataStreamFeedId
-> library Errors.InvalidEdgeDataStreamBidAsk
-> library Errors.InvalidEdgeDataStreamPrices
-> library Keys.edgeDataStreamTokenDecimalsKey
-> library Errors.InvalidEdgeDataStreamExpo
-> library OracleUtils.ValidatedPrice


### external isChainlinkOnChainProvider
_(no internal calls)_


### external shouldAdjustTimestamp
_(no internal calls)_


---

## EdgeDataStreamVerifier

_File: contracts/oracle/EdgeDataStreamVerifier.sol_

### public extractSigner
-> private getMessageHash
-> library Cast.uint192ToBytes
-> library Cast.uint32ToBytes
-> library Cast.uint256ToBytes
-> library Cast.int32ToBytes
-> library Errors.InvalidEdgeSignature


### public verifyData
-> public verifySignature
  -> public extractSigner
    -> private getMessageHash
    -> library Cast.uint192ToBytes
    -> library Cast.uint32ToBytes
    -> library Cast.uint256ToBytes
    -> library Cast.int32ToBytes
    -> library Errors.InvalidEdgeSignature
-> library Errors.InvalidEdgeSigner


### public verifySignature
-> public extractSigner
  -> private getMessageHash
  -> library Cast.uint192ToBytes
  -> library Cast.uint32ToBytes
  -> library Cast.uint256ToBytes
  -> library Cast.int32ToBytes
  -> library Errors.InvalidEdgeSignature


---

## EventEmitter

_File: contracts/event/EventEmitter.sol_

### external emitDataLog1
_(no internal calls)_


### external emitDataLog2
_(no internal calls)_


### external emitDataLog3
_(no internal calls)_


### external emitDataLog4
_(no internal calls)_


### external emitEventLog
_(no internal calls)_


### external emitEventLog1
_(no internal calls)_


### external emitEventLog2
_(no internal calls)_


---

## ExchangeRouter

_File: contracts/router/ExchangeRouter.sol_

### external cancelDeposit
-> library DepositStoreUtils.get
-> library Errors.EmptyDeposit
-> library Errors.Unauthorized


### external cancelOrder
-> library OrderStoreUtils.get
-> library Errors.EmptyOrder
-> library Errors.Unauthorized


### external cancelShift
-> library ShiftStoreUtils.get
-> library Errors.Unauthorized


### external cancelWithdrawal
-> library WithdrawalStoreUtils.get
-> library Errors.Unauthorized


### external claimAffiliateRewards
-> library ReferralUtils.batchClaimAffiliateRewards


### external claimCollateral
-> library MarketUtils.batchClaimCollateral


### external claimFundingFees
-> library FeeUtils.batchClaimFundingFees


### external claimUiFees
-> library FeeUtils.batchClaimUiFees


### external createDeposit
_(no internal calls)_


### external createOrder
_(no internal calls)_


### external createShift
_(no internal calls)_


### external createWithdrawal
_(no internal calls)_


### external executeAtomicWithdrawal
_(no internal calls)_


### external makeExternalCalls
_(no internal calls)_


### external sendNativeToken
-> library AccountUtils.validateReceiver
-> library TokenUtils.sendNativeToken


### external sendTokens
-> library AccountUtils.validateReceiver


### external sendWnt
-> library AccountUtils.validateReceiver
-> library TokenUtils.depositAndSendWrappedNativeToken


### external setSavedCallbackContract
-> library CallbackUtils.setSavedCallbackContract


### external setUiFeeFactor
-> library MarketUtils.setUiFeeFactor


### external simulateExecuteLatestDeposit
-> library NonceUtils.getCurrentKey


### external simulateExecuteLatestJitOrder
-> library NonceUtils.getCurrentKey


### external simulateExecuteLatestOrder
-> library NonceUtils.getCurrentKey


### external simulateExecuteLatestShift
-> library NonceUtils.getCurrentKey


### external simulateExecuteLatestWithdrawal
-> library NonceUtils.getCurrentKey


### external updateOrder
-> library OrderStoreUtils.get
-> library Errors.Unauthorized


---

## ExternalHandler

_File: contracts/external/ExternalHandler.sol_

### external makeExternalCalls
-> library Errors.InvalidExternalCallInput
-> library Errors.InvalidExternalReceiversInput
-> internal _makeExternalCall
  -> library Errors.InvalidExternalCallTarget
  -> library Errors.ExternalCallFailed


---

## FeeDistributor

_File: contracts/fee/FeeDistributor.sol_

### external bridgedGmxReceived
-> internal _validateDistributionState
  -> internal _getUint
  -> library Errors.InvalidDistributionState
-> internal _validateReadResponseTimestamp
  -> internal _getUint
  -> library Errors.OutdatedReadResponse
-> internal _getUint
-> internal _validateDistributionNotCompleted
  -> internal _getUint
  -> library Errors.FeeDistributionAlreadyCompleted
-> library Keys2.feeDistributorStakedGmxKey
-> library Precision.mulDiv
-> library Keys2.feeDistributorFeeAmountGmxKey
-> library Keys2.feeDistributorBridgeSlippageFactorKey
-> library Precision.applyFactor
-> internal _getFeeDistributorVaultBalance
-> library Errors.BridgedAmountNotSufficient
-> internal _setUint
-> internal _setDistributionState
  -> internal _setUint
-> internal _setUintItem
-> internal _emitFeeDistributionEvent


### external depositReferralRewards
-> internal _validateDistributionState
  -> internal _getUint
  -> library Errors.InvalidDistributionState
-> internal _getUint
-> library Keys2.feeDistributorReferralRewardsAmountKey
-> library Keys2.feeDistributorReferralRewardsDepositedKey
-> library Errors.MaxEsGmxReferralRewardsAmountExceeded
-> internal _getFeeDistributorVaultBalance
-> internal _getAddressInfo
  -> internal _getAddress
  -> library Keys2.feeDistributorAddressInfoKey
-> internal _setUintItem
-> library Cast.toBytes32
-> library Errors.InvalidReferralRewardToken
-> library ClaimUtils.incrementClaims
-> internal _transferOut
-> library Keys.totalClaimableFundsAmountKey
-> library ClaimUtils._validateTotalClaimableFundsAmount
-> library Errors.MaxReferralRewardsExceeded
-> internal _setUint


### external distribute
-> internal _getAddressInfo
  -> internal _getAddress
  -> library Keys2.feeDistributorAddressInfoKey
-> library Errors.ZeroTreasuryAddress
-> internal _validateDistributionState
  -> internal _getUint
  -> library Errors.InvalidDistributionState
-> internal _validateReadResponseTimestamp
  -> internal _getUint
  -> library Errors.OutdatedReadResponse
-> internal _getUint
-> internal _validateDistributionNotCompleted
  -> internal _getUint
  -> library Errors.FeeDistributionAlreadyCompleted
-> internal _calculateAndTransferWntCosts
  -> internal _getFeeDistributorVaultBalance
  -> library FeeDistributorUtils.calculateKeeperCosts
  -> internal _calculateChainlinkAndTreasuryAmounts
    -> library Precision.applyFactor
    -> internal _getUint
    -> library Precision.mulDiv
  -> internal _calculateWntForReferralRewards
    -> internal _getUint
    -> library Errors.MaxWntReferralRewardsInUsdAmountExceeded
    -> library Precision.applyFactor
    -> library Errors.MaxWntReferralRewardsInUsdExceeded
    -> library Precision.toFactor
  -> internal _finalizeWntForTreasury
    -> internal _getUint
    -> library Errors.MaxWntFromTreasuryExceeded
    -> internal _getAddressInfo
      -> internal _getAddress
      -> library Keys2.feeDistributorAddressInfoKey
  -> internal _transferWntCosts
    -> library Errors.KeeperAmountMismatch
    -> internal _transferOut
    -> internal _getAddressInfo
      -> internal _getAddress
      -> library Keys2.feeDistributorAddressInfoKey
    -> internal _getAddressInfoForChain
      -> internal _getAddress
      -> library Keys2.feeDistributorAddressInfoForChainKey
    -> internal _getUint
    -> library Keys2.feeDistributorFeeAmountGmxKey
-> internal _setUint
-> library Keys2.feeDistributorFeeAmountUsdKey
-> library Keys2.feeDistributorReferralRewardsAmountKey
-> internal _setDistributionState
  -> internal _setUint
-> internal _setUintItem
-> internal _emitFeeDistributionEvent


### external initiateDistribute
-> internal _getAddress
-> library Errors.InvalidFeeReceiver
-> internal _validateDistributionState
  -> internal _getUint
  -> library Errors.InvalidDistributionState
-> internal _validateDistributionNotCompleted
  -> internal _getUint
  -> library Errors.FeeDistributionAlreadyCompleted
-> internal _setUint
-> library Keys2.feeDistributorReferralRewardsDepositedKey
-> library FeeDistributorUtils.retrieveChainIds
-> internal _getAddressInfoForChain
  -> internal _getAddress
  -> library Keys2.feeDistributorAddressInfoForChainKey
-> internal _getUint
-> library Keys.withdrawableBuybackTokenAmountKey
-> internal _getFeeDistributorVaultBalance
-> library Keys2.feeDistributorFeeAmountGmxKey
-> library Keys2.feeDistributorStakedGmxKey
-> library Keys2.feeDistributorLayerZeroChainIdKey
-> internal _setReadRequestInput
  -> library MultichainReaderUtils.ReadRequestInputs
-> internal _setDistributionState
  -> internal _setUint
-> internal _setUintItem
-> internal _emitFeeDistributionEvent


### external processLzReceive
-> internal _validateDistributionState
  -> internal _getUint
  -> library Errors.InvalidDistributionState
-> internal _validateReadResponseTimestamp
  -> internal _getUint
  -> library Errors.OutdatedReadResponse
-> library FeeDistributorUtils.retrieveChainIds
-> internal _createUintArray
-> internal _getUint
-> library Keys2.feeDistributorFeeAmountGmxKey
-> library Keys2.feeDistributorStakedGmxKey
-> internal _decodeReadData
-> internal _setUint
-> internal _setTokenPrices
  -> internal _setUint
  -> internal _getOraclePrice
    -> library ChainlinkPriceFeedUtils.getPriceFeedPrice
    -> library Errors.EmptyChainlinkPriceFeed
-> library Precision.mulDiv
-> internal _calculateAndBridgeGmx
  -> library Precision.mulDiv
  -> library FeeDistributorUtils.computeTransfers
  -> internal _createUintArray
  -> internal _bridgeGmx
    -> internal _getAddressInfo
      -> internal _getAddress
      -> library Keys2.feeDistributorAddressInfoKey
    -> internal _removeDust
    -> internal _transferOut
    -> internal _getUint
    -> library Keys2.feeDistributorLayerZeroChainIdKey
    -> library Cast.toBytes32
    -> internal _getAddressInfoForChain
      -> internal _getAddress
      -> library Keys2.feeDistributorAddressInfoForChainKey
    -> library Precision.applyFactor
    -> library Keys2.feeDistributorBridgeSlippageFactorKey
-> library Errors.AttemptedBridgeAmountTooHigh
-> internal _setDistributionState
  -> internal _setUint
-> internal _setUintItem
-> internal _emitFeeDistributionEvent


### external withdrawNativeToken
-> library FeeDistributorUtils.withdrawNativeToken


### external withdrawToken
-> library FeeDistributorUtils.withdrawToken


---

## FeeDistributorVault

_File: contracts/fee/FeeDistributorVault.sol_

### external transferOut
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut
-> internal _transferOut
  -> library Errors.SelfTransferNotSupported
  -> internal _afterTransferOut


### external transferOutNativeToken
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut


### external withdrawNativeToken
-> library TokenUtils.sendNativeToken


### external withdrawToken
-> internal _transferOut
  -> library Errors.SelfTransferNotSupported
  -> internal _afterTransferOut


---

## FeeHandler

_File: contracts/fee/FeeHandler.sol_

### external buyback
-> library Errors.BuybackAndFeeTokenAreEqual
-> internal _getBatchSize
  -> internal _getUint
  -> library Keys.buybackBatchAmountKey
-> internal _validateBuybackToken
  -> library Errors.InvalidBuybackToken
-> internal _getAvailableFeeAmount
  -> internal _getUint
  -> library Keys.buybackAvailableFeeAmountKey
-> library Errors.AvailableFeeAmountIsZero
-> internal _getMaxFeeTokenAmount
  -> library Precision.mulDiv
  -> internal _getUint
  -> library Keys.buybackMaxPriceImpactFactorKey
  -> library Precision.applyFactor
-> library Errors.InsufficientBuybackOutputAmount
-> internal _buybackFees
  -> internal _incrementWithdrawableBuybackTokenAmount
    -> library Keys.withdrawableBuybackTokenAmountKey
  -> internal _setAvailableFeeAmount
    -> library Keys.buybackAvailableFeeAmountKey


### external claimFees
-> internal _validateMarket
  -> library Errors.EmptyClaimFeesMarket
-> library FeeUtils.claimFees
-> library Errors.InvalidVersion
-> internal _incrementAvailableFeeAmounts
  -> internal _getFeeAmounts
    -> internal _getUint
    -> library Keys.buybackGmxFactorKey
    -> library Precision.applyFactor
  -> internal _incrementAvailableFeeAmount
    -> internal _incrementWithdrawableBuybackTokenAmount
      -> library Keys.withdrawableBuybackTokenAmountKey
    -> internal _getAvailableFeeAmount
      -> internal _getUint
      -> library Keys.buybackAvailableFeeAmountKey
    -> internal _setAvailableFeeAmount
      -> library Keys.buybackAvailableFeeAmountKey


### external getOutputAmount
-> internal _getBatchSize
  -> internal _getUint
  -> library Keys.buybackBatchAmountKey
-> internal _validateBuybackToken
  -> library Errors.InvalidBuybackToken
-> internal _getAvailableFeeAmount
  -> internal _getUint
  -> library Keys.buybackAvailableFeeAmountKey
-> internal _validateMarket
  -> library Errors.EmptyClaimFeesMarket
-> internal _getUint
-> library Keys.claimableFeeAmountKey
-> library Errors.InvalidVersion
-> internal _getFeeAmounts
  -> internal _getUint
  -> library Keys.buybackGmxFactorKey
  -> library Precision.applyFactor
-> internal _getMaxFeeTokenAmount
  -> library Precision.mulDiv
  -> internal _getUint
  -> library Keys.buybackMaxPriceImpactFactorKey
  -> library Precision.applyFactor


### external multicall
-> library ErrorUtils.revertWithParsedMessage


### external withdrawFees
-> internal _validateBuybackToken
  -> library Errors.InvalidBuybackToken
-> internal _getBatchSize
  -> internal _getUint
  -> library Keys.buybackBatchAmountKey
-> library Keys.withdrawableBuybackTokenAmountKey


---

## GelatoRelayRouter

_File: contracts/router/relay/GelatoRelayRouter.sol_

### external batch
-> library RelayUtils.getBatchStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> internal _batch
  -> library Errors.RelayEmptyBatch
  -> internal _createOrder
    -> internal _getContracts
      -> library TokenUtils.wnt
    -> library Order.isSwapOrder
    -> library Order.isIncreaseOrder
    -> internal _sendTokens
      -> library AccountUtils.validateReceiver
  -> internal _updateOrder
    -> internal _getContracts
      -> library TokenUtils.wnt
    -> library OrderStoreUtils.get
    -> library Errors.EmptyOrder
    -> library Errors.Unauthorized
  -> internal _cancelOrder
    -> internal _getContracts
      -> library TokenUtils.wnt
    -> library OrderStoreUtils.get
    -> library Errors.EmptyOrder
    -> library Errors.Unauthorized


### external cancelOrder
-> library RelayUtils.getCancelOrderStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> internal _cancelOrder
  -> internal _getContracts
    -> library TokenUtils.wnt
  -> library OrderStoreUtils.get
  -> library Errors.EmptyOrder
  -> library Errors.Unauthorized


### external createOrder
-> library RelayUtils.getCreateOrderStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> internal _createOrder
  -> internal _getContracts
    -> library TokenUtils.wnt
  -> library Order.isSwapOrder
  -> library Order.isIncreaseOrder
  -> internal _sendTokens
    -> library AccountUtils.validateReceiver


### external updateOrder
-> library RelayUtils.getUpdateOrderStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> internal _updateOrder
  -> internal _getContracts
    -> library TokenUtils.wnt
  -> library OrderStoreUtils.get
  -> library Errors.EmptyOrder
  -> library Errors.Unauthorized


---

## GlpMigrator

_File: contracts/migration/GlpMigrator.sol_

### external migrate
-> library Errors.InvalidGlpAmount
-> library Errors.InvalidExecutionFeeForMigration
-> library MarketUtils.getEnabledMarket
-> internal _redeemGlp
-> library TokenUtils.depositAndSendWrappedNativeToken
-> external_callback IDepositUtils.CreateDepositParams
-> external_callback IDepositUtils.CreateDepositParamsAddresses
-> library Cast.toBytes32


### external setReducedMintBurnFeeBasisPoints
_(no internal calls)_


---

## GlvDepositHandler

_File: contracts/exchange/GlvDepositHandler.sol_

### external _executeGlvDeposit
-> library FeatureUtils.validateFeature
-> library Keys.executeGlvDepositFeatureDisabledKey
-> library ExecuteGlvDepositUtils.ExecuteGlvDepositParams
-> library ExecuteGlvDepositUtils.executeGlvDeposit
  -> library GlvDepositStoreUtils.get
  -> library GlvUtils.getGlvMarketCount
  -> library GasUtils.estimateExecuteGlvDepositGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleGlvDepositError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library GlvDepositUtils.CancelGlvDepositParams
    -> library GlvDepositUtils.cancelGlvDeposit
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelGlvDepositFeatureDisabledKey
      -> library GlvDepositStoreUtils.get
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library GlvDepositUtils.CancelGlvDepositParams
      -> library GlvDepositUtils.cancelGlvDeposit


### external cancelGlvDeposit
-> library FeatureUtils.validateFeature
-> library Keys.cancelGlvDepositFeatureDisabledKey
-> library GlvDepositStoreUtils.get
-> internal validateRequestCancellation
  -> library Chain.currentTimestamp
  -> library Errors.RequestNotYetCancellable
-> library GlvDepositUtils.CancelGlvDepositParams
-> library GlvDepositUtils.cancelGlvDeposit


### external createGlvDeposit
-> library FeatureUtils.validateFeature
-> library Keys.createGlvDepositFeatureDisabledKey
-> internal validateDataListLength
  -> library Errors.MaxDataListLengthExceeded
-> library GlvDepositUtils.createGlvDeposit


### external executeGlvDeposit
-> library GlvDepositStoreUtils.get
-> library GlvUtils.getGlvMarketCount
-> library GasUtils.estimateExecuteGlvDepositGasLimit
-> library GasUtils.validateExecutionGas
-> library GasUtils.getExecutionGas
-> internal _handleGlvDepositError
  -> library GasUtils.validateExecutionErrorGas
  -> library ErrorUtils.getErrorSelectorFromData
  -> internal validateNonKeeperError
    -> library OracleUtils.isOracleError
    -> library ErrorUtils.revertWithCustomError
  -> library ErrorUtils.getRevertMessage
  -> library GlvDepositUtils.CancelGlvDepositParams
  -> library GlvDepositUtils.cancelGlvDeposit
    -> library FeatureUtils.validateFeature
    -> library Keys.cancelGlvDepositFeatureDisabledKey
    -> library GlvDepositStoreUtils.get
    -> internal validateRequestCancellation
      -> library Chain.currentTimestamp
      -> library Errors.RequestNotYetCancellable
    -> library GlvDepositUtils.CancelGlvDepositParams
    -> library GlvDepositUtils.cancelGlvDeposit


### external simulateExecuteGlvDeposit
-> library GlvDepositStoreUtils.get


---

## GlvFactory

_File: contracts/glv/GlvFactory.sol_

### external createGlv
-> library Errors.GlvSymbolTooLong
-> library Errors.GlvNameTooLong
-> library GlvStoreUtils.getGlvSaltHash
-> library Errors.GlvAlreadyExists
-> library Glv.Props
-> library GlvStoreUtils.set
-> internal emitGlvCreated
  -> library Cast.toBytes32


---

## GlvReader

_File: contracts/reader/GlvReader.sol_

### external getAccountGlvDeposits
-> library GlvDepositStoreUtils.getAccountGlvDepositKeys
-> library GlvDepositStoreUtils.get


### external getAccountGlvWithdrawals
-> library GlvWithdrawalStoreUtils.getAccountGlvWithdrawalKeys
-> library GlvWithdrawalStoreUtils.get


### external getGlv
-> library GlvStoreUtils.get


### external getGlvBySalt
-> library GlvStoreUtils.getBySalt


### external getGlvDeposit
-> library GlvDepositStoreUtils.get


### external getGlvDeposits
-> library GlvDepositStoreUtils.getGlvDepositKeys
-> library GlvDepositStoreUtils.get


### public getGlvInfo
-> library Keys.glvSupportedMarketListKey
-> library GlvStoreUtils.get


### external getGlvInfoList
-> library GlvStoreUtils.getGlvCount
-> library GlvStoreUtils.getGlvKeys
-> public getGlvInfo
  -> library Keys.glvSupportedMarketListKey
  -> library GlvStoreUtils.get


### external getGlvShift
-> library GlvShiftStoreUtils.get


### external getGlvShifts
-> library GlvShiftStoreUtils.getGlvShiftKeys
-> library GlvShiftStoreUtils.get


### external getGlvTokenPrice
-> library GlvUtils.getGlvTokenPrice


### external getGlvValue
-> library GlvUtils.getGlvValue


### external getGlvWithdrawal
-> library GlvWithdrawalStoreUtils.get


### external getGlvWithdrawals
-> library GlvWithdrawalStoreUtils.getGlvWithdrawalKeys
-> library GlvWithdrawalStoreUtils.get


### external getGlvs
-> library GlvStoreUtils.getGlvCount
-> library GlvStoreUtils.getGlvKeys
-> library GlvStoreUtils.get


---

## GlvRouter

_File: contracts/router/GlvRouter.sol_

### external cancelGlvDeposit
-> library GlvDepositStoreUtils.get
-> library Errors.EmptyGlvDeposit
-> library Errors.Unauthorized


### external cancelGlvWithdrawal
-> library GlvWithdrawalStoreUtils.get
-> library Errors.EmptyGlvWithdrawal
-> library Errors.Unauthorized


### external createGlvDeposit
_(no internal calls)_


### external createGlvWithdrawal
_(no internal calls)_


### external makeExternalCalls
_(no internal calls)_


### external sendNativeToken
-> library AccountUtils.validateReceiver
-> library TokenUtils.sendNativeToken


### external sendTokens
-> library AccountUtils.validateReceiver


### external sendWnt
-> library AccountUtils.validateReceiver
-> library TokenUtils.depositAndSendWrappedNativeToken


### external simulateExecuteGlvDeposit
_(no internal calls)_


### external simulateExecuteGlvWithdrawal
_(no internal calls)_


### external simulateExecuteLatestGlvDeposit
-> library NonceUtils.getCurrentKey


### external simulateExecuteLatestGlvWithdrawal
-> library NonceUtils.getCurrentKey


---

## GlvShiftHandler

_File: contracts/exchange/GlvShiftHandler.sol_

### external addMarketToGlv
-> library GlvUtils.addMarketToGlv


### external createGlvShift
-> library FeatureUtils.validateFeature
-> library Keys.createGlvShiftFeatureDisabledKey
-> library GlvShiftUtils.createGlvShift


### external doExecuteGlvShift
-> library FeatureUtils.validateFeature
-> library Keys.executeGlvShiftFeatureDisabledKey
-> library GlvShiftUtils.ExecuteGlvShiftParams
-> library GlvShiftUtils.executeGlvShift
  -> library GlvShiftStoreUtils.get
  -> library GasUtils.estimateExecuteGlvShiftGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleGlvShiftError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library GlvShiftUtils.cancelGlvShift


### external executeGlvShift
-> library GlvShiftStoreUtils.get
-> library GasUtils.estimateExecuteGlvShiftGasLimit
-> library GasUtils.validateExecutionGas
-> library GasUtils.getExecutionGas
-> internal _handleGlvShiftError
  -> library GasUtils.validateExecutionErrorGas
  -> library ErrorUtils.getErrorSelectorFromData
  -> internal validateNonKeeperError
    -> library OracleUtils.isOracleError
    -> library ErrorUtils.revertWithCustomError
  -> library ErrorUtils.getRevertMessage
  -> library GlvShiftUtils.cancelGlvShift


### external removeMarketFromGlv
-> library GlvUtils.removeMarketFromGlv


---

## GlvToken

_File: contracts/glv/GlvToken.sol_

### external burn
_(no internal calls)_


### external mint
_(no internal calls)_


### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_


---

## GlvVault

_File: contracts/glv/GlvVault.sol_

### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_


---

## GlvWithdrawalHandler

_File: contracts/exchange/GlvWithdrawalHandler.sol_

### external _executeGlvWithdrawal
-> library FeatureUtils.validateFeature
-> library Keys.executeGlvWithdrawalFeatureDisabledKey
-> library GlvWithdrawalUtils.ExecuteGlvWithdrawalParams
-> library GlvWithdrawalUtils.executeGlvWithdrawal
  -> library GlvWithdrawalStoreUtils.get
  -> library GlvUtils.getGlvMarketCount
  -> library GasUtils.estimateExecuteGlvWithdrawalGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleGlvWithdrawalError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library GlvWithdrawalUtils.CancelGlvWithdrawalParams
    -> library GlvWithdrawalUtils.cancelGlvWithdrawal
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelGlvWithdrawalFeatureDisabledKey
      -> library GlvWithdrawalStoreUtils.get
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library GlvWithdrawalUtils.CancelGlvWithdrawalParams
      -> library GlvWithdrawalUtils.cancelGlvWithdrawal


### external cancelGlvWithdrawal
-> library FeatureUtils.validateFeature
-> library Keys.cancelGlvWithdrawalFeatureDisabledKey
-> library GlvWithdrawalStoreUtils.get
-> internal validateRequestCancellation
  -> library Chain.currentTimestamp
  -> library Errors.RequestNotYetCancellable
-> library GlvWithdrawalUtils.CancelGlvWithdrawalParams
-> library GlvWithdrawalUtils.cancelGlvWithdrawal


### external createGlvWithdrawal
-> library FeatureUtils.validateFeature
-> library Keys.createGlvWithdrawalFeatureDisabledKey
-> internal validateDataListLength
  -> library Errors.MaxDataListLengthExceeded
-> library GlvWithdrawalUtils.createGlvWithdrawal


### external executeGlvWithdrawal
-> library GlvWithdrawalStoreUtils.get
-> library GlvUtils.getGlvMarketCount
-> library GasUtils.estimateExecuteGlvWithdrawalGasLimit
-> library GasUtils.validateExecutionGas
-> library GasUtils.getExecutionGas
-> internal _handleGlvWithdrawalError
  -> library GasUtils.validateExecutionErrorGas
  -> library ErrorUtils.getErrorSelectorFromData
  -> internal validateNonKeeperError
    -> library OracleUtils.isOracleError
    -> library ErrorUtils.revertWithCustomError
  -> library ErrorUtils.getRevertMessage
  -> library GlvWithdrawalUtils.CancelGlvWithdrawalParams
  -> library GlvWithdrawalUtils.cancelGlvWithdrawal
    -> library FeatureUtils.validateFeature
    -> library Keys.cancelGlvWithdrawalFeatureDisabledKey
    -> library GlvWithdrawalStoreUtils.get
    -> internal validateRequestCancellation
      -> library Chain.currentTimestamp
      -> library Errors.RequestNotYetCancellable
    -> library GlvWithdrawalUtils.CancelGlvWithdrawalParams
    -> library GlvWithdrawalUtils.cancelGlvWithdrawal


### external simulateExecuteGlvWithdrawal
-> library GlvWithdrawalStoreUtils.get


---

## GmOracleProvider

_File: contracts/oracle/GmOracleProvider.sol_

### external getOraclePrice
-> internal _getSigners
  -> library Errors.GmMinOracleSigners
  -> library Errors.GmMaxOracleSigners
  -> library Errors.GmMaxSignerIndex
  -> library Errors.GmEmptySigner
-> library Errors.GmInvalidMinMaxBlockNumber
-> library Chain.currentBlockNumber
-> library Errors.GmInvalidBlockNumber
-> library Keys.oracleTypeKey
-> library Errors.GmMinPricesNotSorted
-> library Errors.GmMaxPricesNotSorted
-> internal _getSalt
-> library Errors.InvalidGmSignerMinMaxPrice
-> library GmOracleUtils.validateSigner
-> library Array.getMedian
-> library Errors.InvalidGmOraclePrice
-> library Errors.InvalidGmMedianMinMaxPrice
-> library OracleUtils.ValidatedPrice


### external isChainlinkOnChainProvider
_(no internal calls)_


### external shouldAdjustTimestamp
_(no internal calls)_


---

## GovTimelockController

_File: contracts/gov/GovTimelockController.sol_

### public name
_(no internal calls)_


---

## GovToken

_File: contracts/gov/GovToken.sol_

### public CLOCK_MODE
-> public clock
  -> library Chain.currentTimestamp
-> library Chain.currentTimestamp


### external burn
-> internal _burn


### public clock
-> library Chain.currentTimestamp


### public decimals
_(no internal calls)_


### external mint
-> internal _mint


---

## IncreaseOrderExecutor

_File: contracts/order/IncreaseOrderExecutor.sol_

### external processOrder
-> library IncreaseOrderUtils.processOrder


---

## JitOrderHandler

_File: contracts/exchange/JitOrderHandler.sol_

### external executeJitOrder
-> internal _executeJitOrder
  -> library FeatureUtils.validateFeature
  -> library Keys.jitFeatureDisabledKey
  -> library OrderStoreUtils.get
  -> internal _validateOrder
    -> library Order.isIncreaseOrder
    -> library Errors.JitUnsupportedOrderType
  -> internal _processShifts
    -> library Errors.JitEmptyShiftParams
    -> library Errors.JitInvalidToMarket
    -> internal _createGlvShift
      -> library GlvShiftUtils.validateGlvShift
      -> library GlvShift.Props
      -> library GlvShift.Addresses
      -> library GlvShift.Numbers
      -> library GlvShiftEventUtils.emitGlvShiftCreated
  -> library GasUtils.estimateExecuteOrderGasLimit
  -> library GasUtils.validateExecutionGas


### external simulateExecuteJitOrder
-> internal _executeJitOrder
  -> library FeatureUtils.validateFeature
  -> library Keys.jitFeatureDisabledKey
  -> library OrderStoreUtils.get
  -> internal _validateOrder
    -> library Order.isIncreaseOrder
    -> library Errors.JitUnsupportedOrderType
  -> internal _processShifts
    -> library Errors.JitEmptyShiftParams
    -> library Errors.JitInvalidToMarket
    -> internal _createGlvShift
      -> library GlvShiftUtils.validateGlvShift
      -> library GlvShift.Props
      -> library GlvShift.Addresses
      -> library GlvShift.Numbers
      -> library GlvShiftEventUtils.emitGlvShiftCreated
  -> library GasUtils.estimateExecuteOrderGasLimit
  -> library GasUtils.validateExecutionGas


---

## KeeperReader

_File: contracts/reader/KeeperReader.sol_

### external getOrders
-> library OrderStoreUtils.getOrderKeys
-> library OrderStoreUtils.get


---

## LayerZeroProvider

_File: contracts/multichain/LayerZeroProvider.sol_

### external bridgeOut
-> library Errors.InvalidBridgeOutToken
-> library Keys.eidToSrcChainId
-> library Errors.InvalidEid
-> private prepareSend
  -> library Cast.toBytes32
-> library MultichainUtils.transferOut
-> library TokenUtils.depositAndSendWrappedNativeToken
-> library MultichainUtils.recordTransferIn


### external lzCompose
-> library MultichainUtils.validateMultichainProvider
-> library MultichainUtils.validateMultichainEndpoint
-> private _decodeLzComposeMsg
  -> library Keys.eidToSrcChainId
-> library TokenUtils.depositAndSendWrappedNativeToken
-> library TokenUtils.wnt
-> library MultichainUtils.recordBridgeIn
-> private _handleNativeTopUp
  -> library Errors.InsufficientNativeTokenAmount
  -> library TokenUtils.depositAndSendWrappedNativeToken
  -> library MultichainUtils.recordBridgeIn
  -> library TokenUtils.wnt
-> library MultichainEventUtils.emitMultichainBridgeAction
-> private _handleDeposit
  -> private _areValidTransferRequests
  -> library GasUtils.estimateCreateDepositGasLimit
  -> internal _validateGasLeft
    -> library Errors.InsufficientGasLeft
  -> library MultichainEventUtils.emitMultichainBridgeActionFailed
  -> library ErrorUtils.getRevertMessage
-> private _handleGlvDeposit
  -> private _areValidTransferRequests
  -> library GasUtils.estimateCreateGlvDepositGasLimit
  -> internal _validateGasLeft
    -> library Errors.InsufficientGasLeft
  -> library MultichainEventUtils.emitMultichainBridgeActionFailed
  -> library ErrorUtils.getRevertMessage
-> private _handleSetTraderReferralCode
  -> library GasUtils.estimateSetTraderReferralCodeGasLimit
  -> internal _validateGasLeft
    -> library Errors.InsufficientGasLeft
  -> library MultichainEventUtils.emitMultichainBridgeActionFailed
  -> library ErrorUtils.getRevertMessage
-> private _handleRegisterCode
  -> library GasUtils.estimateRegisterCodeGasLimit
  -> internal _validateGasLeft
    -> library Errors.InsufficientGasLeft
  -> library MultichainEventUtils.emitMultichainBridgeActionFailed
  -> library ErrorUtils.getRevertMessage
-> private _handleWithdrawal
  -> private _areValidTransferRequests
  -> library GasUtils.estimateCreateWithdrawalGasLimit
  -> internal _validateGasLeft
    -> library Errors.InsufficientGasLeft
  -> library MultichainEventUtils.emitMultichainBridgeActionFailed
  -> library ErrorUtils.getRevertMessage
-> private _handleGlvWithdrawal
  -> private _areValidTransferRequests
  -> library GasUtils.estimateCreateGlvWithdrawalGasLimit
  -> internal _validateGasLeft
    -> library Errors.InsufficientGasLeft
  -> library MultichainEventUtils.emitMultichainBridgeActionFailed
  -> library ErrorUtils.getRevertMessage


### external withdrawTokens
-> library Errors.EmptyWithdrawalAmount
-> library TokenUtils.sendNativeToken


---

## LiquidationHandler

_File: contracts/exchange/LiquidationHandler.sol_

### external executeLiquidation
-> library LiquidationUtils.createLiquidationOrder
-> library OrderStoreUtils.get
-> internal _getExecuteOrderParams
  -> library MarketUtils.getSwapPathMarkets
  -> library MarketUtils.getEnabledMarket
-> library FeatureUtils.validateFeature
-> library Keys.executeOrderFeatureDisabledKey
-> library ExecuteOrderUtils.executeOrder


---

## MarketFactory

_File: contracts/market/MarketFactory.sol_

### external createMarket
-> library MarketStoreUtils.getMarketSaltHash
-> library Errors.MarketAlreadyExists
-> library Market.Props
-> library MarketStoreUtils.set
-> internal emitMarketCreated
  -> library Cast.toBytes32


---

## MarketToken

_File: contracts/market/MarketToken.sol_

### external burn
_(no internal calls)_


### external mint
_(no internal calls)_


### external transferOut
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut
-> internal _transferOut
  -> library Errors.SelfTransferNotSupported
  -> internal _afterTransferOut


### external transferOutNativeToken
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut


---

## MultichainClaimsRouter

_File: contracts/multichain/MultichainClaimsRouter.sol_

### external claimAffiliateRewards
-> library RelayUtils.getClaimAffiliateRewardsStructHash
-> private _claimAffiliateRewards
  -> library ReferralUtils.batchClaimAffiliateRewards
  -> library MultichainUtils.recordTransferIn


### external claimCollateral
-> private _claimCollateral
  -> library RelayUtils.getClaimCollateralStructHash
  -> library MarketUtils.batchClaimCollateral
  -> library MultichainUtils.recordTransferIn


### external claimFundingFees
-> library RelayUtils.getClaimFundingFeesStructHash
-> private _claimFundingFees
  -> library FeeUtils.batchClaimFundingFees
  -> library MultichainUtils.recordTransferIn


---

## MultichainGlvRouter

_File: contracts/multichain/MultichainGlvRouter.sol_

### external createGlvDeposit
-> library RelayUtils.getCreateGlvDepositStructHash
-> private _createGlvDeposit
  -> internal _processTransferRequests
    -> library Errors.InvalidTransferRequestsLength
    -> internal _sendTokens
      -> library AccountUtils.validateReceiver
      -> library MultichainUtils.transferOut
  -> library TokenUtils.wnt


### external createGlvWithdrawal
-> library RelayUtils.getCreateGlvWithdrawalStructHash
-> internal _processTransferRequests
  -> library Errors.InvalidTransferRequestsLength
  -> internal _sendTokens
    -> library AccountUtils.validateReceiver
    -> library MultichainUtils.transferOut
-> library TokenUtils.wnt


---

## MultichainGmRouter

_File: contracts/multichain/MultichainGmRouter.sol_

### external createDeposit
-> library RelayUtils.getCreateDepositStructHash
-> private _createDeposit
  -> internal _processTransferRequests
    -> library Errors.InvalidTransferRequestsLength
    -> internal _sendTokens
      -> library AccountUtils.validateReceiver
      -> library MultichainUtils.transferOut
  -> library TokenUtils.wnt


### external createShift
-> library RelayUtils.getCreateShiftStructHash
-> internal _processTransferRequests
  -> library Errors.InvalidTransferRequestsLength
  -> internal _sendTokens
    -> library AccountUtils.validateReceiver
    -> library MultichainUtils.transferOut
-> library TokenUtils.wnt


### external createWithdrawal
-> library RelayUtils.getCreateWithdrawalStructHash
-> internal _processTransferRequests
  -> library Errors.InvalidTransferRequestsLength
  -> internal _sendTokens
    -> library AccountUtils.validateReceiver
    -> library MultichainUtils.transferOut
-> library TokenUtils.wnt


---

## MultichainOrderRouter

_File: contracts/multichain/MultichainOrderRouter.sol_

### external batch
-> library RelayUtils.getBatchStructHash


### external cancelOrder
-> library RelayUtils.getCancelOrderStructHash


### external createOrder
-> library RelayUtils.getCreateOrderStructHash


### external registerCode
-> library RelayUtils.getRegisterCodeStructHash
-> library Errors.ReferralCodeAlreadyExists


### external setTraderReferralCode
-> library RelayUtils.getTraderReferralCodeStructHash


### external updateOrder
-> library RelayUtils.getUpdateOrderStructHash


---

## MultichainReader

_File: contracts/multichain/MultichainReader.sol_

### external allowInitializePath
-> library Keys2.multichainPeersKey


### external isComposeMsgSender
_(no internal calls)_


### external lzReceive
-> library Errors.Unauthorized
-> internal _getPeerOrRevert
  -> library Keys2.multichainPeersKey
  -> library Errors.EmptyPeer
-> internal _lzReceive
  -> library Keys2.multichainGuidToOriginatorKey
  -> library MultichainReaderUtils.ReceivedData


### external lzReduce
_(no internal calls)_


### external nextNonce
_(no internal calls)_


### external oAppVersion
_(no internal calls)_


### external peers
-> library Keys2.multichainPeersKey


### external quoteReadFee
-> internal _quote
  -> internal _getPeerOrRevert
    -> library Keys2.multichainPeersKey
    -> library Errors.EmptyPeer
-> internal _getCmd
  -> library Keys2.multichainConfirmationsKey
-> internal _extraOptions


### external sendReadRequests
-> library Keys2.multichainAuthorizedOriginatorsKey
-> library Errors.Unauthorized
-> library Keys2.multichainGuidToOriginatorKey
-> internal _getCmd
  -> library Keys2.multichainConfirmationsKey
-> internal _lzSend
  -> internal _payNative
    -> library Errors.InsufficientMultichainNativeFee
  -> internal _getPeerOrRevert
    -> library Keys2.multichainPeersKey
    -> library Errors.EmptyPeer
-> internal _extraOptions


### external setDelegate
_(no internal calls)_


---

## MultichainSubaccountRouter

_File: contracts/multichain/MultichainSubaccountRouter.sol_

### external batch
-> private _handleBatch
  -> library RelayUtils.getBatchStructHash
  -> library SubaccountUtils.validateCreateOrderParams
  -> private _handleSubaccountOrderAction
    -> library SubaccountRouterUtils.handleSubaccountAction


### external cancelOrder
-> private _handleCancelOrder
  -> library RelayUtils.getCancelOrderStructHash
  -> private _handleSubaccountOrderAction
    -> library SubaccountRouterUtils.handleSubaccountAction


### external createOrder
-> private _handleCreateOrder
  -> library RelayUtils.getCreateOrderStructHash
  -> library SubaccountUtils.validateCreateOrderParams
  -> private _handleSubaccountOrderAction
    -> library SubaccountRouterUtils.handleSubaccountAction


### external removeSubaccount
-> library RelayUtils.getRemoveSubaccountStructHash
-> library SubaccountUtils.removeSubaccount


### external updateOrder
-> private _handleUpdateOrder
  -> library RelayUtils.getUpdateOrderStructHash
  -> private _handleSubaccountOrderAction
    -> library SubaccountRouterUtils.handleSubaccountAction


---

## MultichainTransferRouter

_File: contracts/multichain/MultichainTransferRouter.sol_

### external bridgeIn
-> library MultichainUtils.recordTransferIn
-> library MultichainEventUtils.emitMultichainBridgeIn


### external bridgeOut
-> library RelayUtils.getBridgeOutStructHash
-> internal _bridgeOut
  -> library MultichainUtils.transferOut
    -> internal _bridgeOut
  -> library MultichainEventUtils.emitMultichainBridgeOut
  -> library MultichainUtils.validateMultichainProvider
  -> external_callback IRelayUtils.BridgeOutParams


### external bridgeOutFromController
-> internal _bridgeOut
  -> library MultichainUtils.transferOut
    -> internal _bridgeOut
  -> library MultichainEventUtils.emitMultichainBridgeOut
  -> library MultichainUtils.validateMultichainProvider
  -> external_callback IRelayUtils.BridgeOutParams


### external initialize
-> library Errors.InvalidInitializer
-> library Errors.InvalidMultichainProvider


### external transferOut
-> internal _bridgeOut
  -> library MultichainUtils.transferOut
  -> library MultichainEventUtils.emitMultichainBridgeOut
  -> library MultichainUtils.validateMultichainProvider
  -> external_callback IRelayUtils.BridgeOutParams


---

## MultichainVault

_File: contracts/multichain/MultichainVault.sol_

### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_


---

## Oracle

_File: contracts/oracle/Oracle.sol_

### external clearAllPrices
-> internal _removePrimaryPrice


### external getPrimaryPrice
-> library Price.Props
-> library Errors.EmptyPrimaryPrice


### external getTokensWithPrices
_(no internal calls)_


### external getTokensWithPricesCount
_(no internal calls)_


### external setPrices
-> internal _validatePrices
  -> library Errors.InvalidOracleSetPricesProvidersParam
  -> library Errors.InvalidOracleSetPricesDataParam
  -> library Keys.isOracleProviderEnabledKey
  -> library Errors.InvalidOracleProvider
  -> library Keys.isAtomicOracleProviderKey
  -> library Errors.NonAtomicOracleProvider
  -> library Keys.oracleProviderForTokenKey
  -> library Errors.InvalidOracleProviderForToken
  -> library Keys.oracleTimestampAdjustmentKey
  -> library Chain.currentTimestamp
  -> library Errors.MaxPriceAgeExceeded
  -> library ChainlinkPriceFeedUtils.getPriceFeedPrice
  -> internal _validateRefPrice
    -> library Calc.diff
    -> library Precision.toFactor
    -> library Errors.MaxRefPriceDeviationExceeded
-> internal _setPrices
  -> library Errors.NonEmptyTokensWithPrices
  -> internal _setPrimaryPrice
    -> library Errors.InvalidMinMaxForPrice
    -> library Errors.PriceAlreadySet
  -> library Price.Props
  -> internal _emitOraclePriceUpdated
    -> library Cast.toBytes32
  -> library Errors.MaxOracleTimestampRangeExceeded


### external setPricesForAtomicAction
-> public validateSequencerUp
  -> library Errors.SequencerDown
  -> library Errors.SequencerGraceDurationNotYetPassed
-> internal _validatePrices
  -> library Errors.InvalidOracleSetPricesProvidersParam
  -> library Errors.InvalidOracleSetPricesDataParam
  -> library Keys.isOracleProviderEnabledKey
  -> library Errors.InvalidOracleProvider
  -> library Keys.isAtomicOracleProviderKey
  -> library Errors.NonAtomicOracleProvider
  -> library Keys.oracleProviderForTokenKey
  -> library Errors.InvalidOracleProviderForToken
  -> library Keys.oracleTimestampAdjustmentKey
  -> library Chain.currentTimestamp
  -> library Errors.MaxPriceAgeExceeded
  -> library ChainlinkPriceFeedUtils.getPriceFeedPrice
  -> internal _validateRefPrice
    -> library Calc.diff
    -> library Precision.toFactor
    -> library Errors.MaxRefPriceDeviationExceeded
-> internal _setPrices
  -> library Errors.NonEmptyTokensWithPrices
  -> internal _setPrimaryPrice
    -> library Errors.InvalidMinMaxForPrice
    -> library Errors.PriceAlreadySet
  -> library Price.Props
  -> internal _emitOraclePriceUpdated
    -> library Cast.toBytes32
  -> library Errors.MaxOracleTimestampRangeExceeded


### external setPrimaryPrice
-> internal _setPrimaryPrice
  -> library Errors.InvalidMinMaxForPrice
  -> library Errors.PriceAlreadySet


### external setTimestamps
_(no internal calls)_


### external validatePrices
-> internal _validatePrices
  -> library Errors.InvalidOracleSetPricesProvidersParam
  -> library Errors.InvalidOracleSetPricesDataParam
  -> library Keys.isOracleProviderEnabledKey
  -> library Errors.InvalidOracleProvider
  -> library Keys.isAtomicOracleProviderKey
  -> library Errors.NonAtomicOracleProvider
  -> library Keys.oracleProviderForTokenKey
  -> library Errors.InvalidOracleProviderForToken
  -> library Keys.oracleTimestampAdjustmentKey
  -> library Chain.currentTimestamp
  -> library Errors.MaxPriceAgeExceeded
  -> library ChainlinkPriceFeedUtils.getPriceFeedPrice
  -> internal _validateRefPrice
    -> library Calc.diff
    -> library Precision.toFactor
    -> library Errors.MaxRefPriceDeviationExceeded


### public validateSequencerUp
-> library Errors.SequencerDown
-> library Errors.SequencerGraceDurationNotYetPassed


---

## OracleStore

_File: contracts/oracle/OracleStore.sol_

### external addSigner
-> library Cast.toBytes32


### external getSigner
_(no internal calls)_


### external getSignerCount
_(no internal calls)_


### external getSigners
_(no internal calls)_


### external removeSigner
-> library Cast.toBytes32


---

## OrderHandler

_File: contracts/exchange/OrderHandler.sol_

### external cancelOrder
-> library OrderStoreUtils.get
-> library FeatureUtils.validateFeature
-> library Keys.cancelOrderFeatureDisabledKey
-> library Order.isMarketOrder
-> library OrderUtils.cancelOrder
-> library OrderUtils.CancelOrderParams


### external createOrder
-> library FeatureUtils.validateFeature
-> library Keys.createOrderFeatureDisabledKey
-> library OrderUtils.createOrder


### external doExecuteOrder
-> internal _getExecuteOrderParams
  -> library MarketUtils.getSwapPathMarkets
  -> library MarketUtils.getEnabledMarket
-> internal _validateFrozenOrderKeeper
  -> library Errors.InvalidKeeperForFrozenOrder
-> library FeatureUtils.validateFeature
-> library Keys.executeOrderFeatureDisabledKey
-> library ExecuteOrderUtils.executeOrder
  -> library OrderStoreUtils.get
  -> library GasUtils.estimateExecuteOrderGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleOrderError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> library OrderStoreUtils.get
    -> library Order.isMarketOrder
    -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library OrderUtils.cancelOrder
      -> library OrderStoreUtils.get
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelOrderFeatureDisabledKey
      -> library Order.isMarketOrder
      -> library OrderUtils.cancelOrder
      -> library OrderUtils.CancelOrderParams
    -> library OrderUtils.CancelOrderParams
    -> library OrderUtils.freezeOrder
-> internal getOrderExecutor
  -> library Order.isIncreaseOrder
  -> library Order.isDecreaseOrder
  -> library Order.isSwapOrder
  -> library Errors.UnsupportedOrderType


### external executeOrder
-> library OrderStoreUtils.get
-> library GasUtils.estimateExecuteOrderGasLimit
-> library GasUtils.validateExecutionGas
-> library GasUtils.getExecutionGas
-> internal _handleOrderError
  -> library GasUtils.validateExecutionErrorGas
  -> library ErrorUtils.getErrorSelectorFromData
  -> library OrderStoreUtils.get
  -> library Order.isMarketOrder
  -> library ErrorUtils.revertWithCustomError
  -> library ErrorUtils.getRevertMessage
  -> library OrderUtils.cancelOrder
    -> library OrderStoreUtils.get
    -> library FeatureUtils.validateFeature
    -> library Keys.cancelOrderFeatureDisabledKey
    -> library Order.isMarketOrder
    -> library OrderUtils.cancelOrder
    -> library OrderUtils.CancelOrderParams
  -> library OrderUtils.CancelOrderParams
  -> library OrderUtils.freezeOrder


### external simulateExecuteOrder
-> library OrderStoreUtils.get


### external updateOrder
-> library FeatureUtils.validateFeature
-> library Keys.updateOrderFeatureDisabledKey
-> library Order.isMarketOrder
-> library Errors.OrderNotUpdatable
-> library Order.isSupportedOrder
-> library Errors.UnsupportedOrderType
-> library OrderUtils.updateAutoCancelList
-> library OrderUtils.validateTotalCallbackGasLimitForAutoCancelOrders
-> library TokenUtils.wnt
-> library GasUtils.estimateExecuteOrderGasLimit
-> library GasUtils.estimateOrderOraclePriceCount
-> library GasUtils.validateAndCapExecutionFee
-> library GasUtils.transferExcessiveExecutionFee
-> library BaseOrderUtils.validateNonEmptyOrder
-> library OrderStoreUtils.set
-> library OrderEventUtils.emitOrderUpdated


---

## OrderVault

_File: contracts/order/OrderVault.sol_

### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_


---

## PayableMulticall

_File: contracts/utils/PayableMulticall.sol_

### external multicall
-> library ErrorUtils.revertWithParsedMessage


---

## ProtocolGovernor

_File: contracts/gov/ProtocolGovernor.sol_

### public CLOCK_MODE
-> public clock
  -> library Chain.currentTimestamp
-> library Chain.currentTimestamp


### public cancel
_(no internal calls)_


### public clock
-> library Chain.currentTimestamp


### public proposalThreshold
_(no internal calls)_


### public propose
_(no internal calls)_


### public state
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public version
_(no internal calls)_


---

## Reader

_File: contracts/reader/Reader.sol_

### external getAccountOrders
-> library ReaderUtils.getAccountOrders


### external getAccountPositionInfoList
-> library ReaderPositionUtils.getAccountPositionInfoList


### external getAccountPositions
-> library ReaderPositionUtils.getAccountPositions


### external getAdlState
-> library ReaderUtils.getAdlState


### external getDeposit
-> library DepositStoreUtils.get


### external getDepositAmountOut
-> library ReaderDepositUtils.getDepositAmountOut


### external getExecutionPrice
-> library MarketStoreUtils.get
-> library ReaderPricingUtils.getExecutionPrice


### external getMarket
-> library MarketStoreUtils.get


### external getMarketBySalt
-> library MarketStoreUtils.getBySalt


### public getMarketInfo
-> library ReaderUtils.getMarketInfo


### external getMarketInfoList
-> library ReaderUtils.getMarketInfoList


### external getMarketTokenPrice
-> library MarketUtils.getMarketTokenPrice


### external getMarkets
-> library ReaderUtils.getMarkets


### external getNetPnl
-> library MarketUtils.getNetPnl


### external getOpenInterestWithPnl
-> library MarketUtils.getOpenInterestWithPnl


### external getOrder
-> library ReaderUtils.getOrder


### external getPendingPositionImpactPoolDistributionAmount
-> library MarketUtils.getPendingPositionImpactPoolDistributionAmount


### external getPnl
-> library MarketUtils.getPnl


### external getPnlToPoolFactor
-> library MarketStoreUtils.get
-> library MarketUtils.getPnlToPoolFactor


### external getPosition
-> library PositionStoreUtils.get


### public getPositionInfo
-> library ReaderPositionUtils.getPositionInfo


### external getPositionInfoList
-> library ReaderPositionUtils.getPositionInfoList


### external getPositionPnlUsd
-> library PositionStoreUtils.get
-> library PositionUtils.getPositionPnlUsd


### external getShift
-> library ShiftStoreUtils.get


### external getSwapAmountOut
-> library ReaderPricingUtils.getSwapAmountOut


### external getSwapPriceImpact
-> library MarketStoreUtils.get
-> library ReaderPricingUtils.getSwapPriceImpact


### external getWithdrawal
-> library WithdrawalStoreUtils.get


### external getWithdrawalAmountOut
-> library ReaderWithdrawalUtils.getWithdrawalAmountOut


### public isPositionLiquidatable
-> library PositionStoreUtils.get
-> library PositionUtils.isPositionLiquidatable


---

## RoleStore

_File: contracts/role/RoleStore.sol_

### external getRoleCount
_(no internal calls)_


### external getRoleMemberCount
_(no internal calls)_


### external getRoleMembers
_(no internal calls)_


### external getRoles
_(no internal calls)_


### external grantRole
-> internal _grantRole


### public hasRole
_(no internal calls)_


### external revokeRole
-> internal _revokeRole
  -> library Errors.ThereMustBeAtLeastOneRoleAdmin
  -> library Errors.ThereMustBeAtLeastOneTimelockMultiSig


---

## Router

_File: contracts/router/Router.sol_

### external pluginTransfer
_(no internal calls)_


---

## ShiftHandler

_File: contracts/exchange/ShiftHandler.sol_

### external _executeShift
-> library FeatureUtils.validateFeature
-> library Keys.executeShiftFeatureDisabledKey
-> library ShiftUtils.ExecuteShiftParams
-> library ShiftUtils.executeShift
  -> library ShiftStoreUtils.get
  -> library GasUtils.estimateExecuteShiftGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleShiftError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library ShiftUtils.cancelShift
      -> library ShiftStoreUtils.get
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelShiftFeatureDisabledKey
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library ShiftUtils.cancelShift


### external cancelShift
-> library ShiftStoreUtils.get
-> library FeatureUtils.validateFeature
-> library Keys.cancelShiftFeatureDisabledKey
-> internal validateRequestCancellation
  -> library Chain.currentTimestamp
  -> library Errors.RequestNotYetCancellable
-> library ShiftUtils.cancelShift


### external createShift
-> library FeatureUtils.validateFeature
-> library Keys.createShiftFeatureDisabledKey
-> internal validateDataListLength
  -> library Errors.MaxDataListLengthExceeded
-> library ShiftUtils.createShift


### external executeShift
-> library ShiftStoreUtils.get
-> library GasUtils.estimateExecuteShiftGasLimit
-> library GasUtils.validateExecutionGas
-> library GasUtils.getExecutionGas
-> internal _handleShiftError
  -> library GasUtils.validateExecutionErrorGas
  -> library ErrorUtils.getErrorSelectorFromData
  -> internal validateNonKeeperError
    -> library OracleUtils.isOracleError
    -> library ErrorUtils.revertWithCustomError
  -> library ErrorUtils.getRevertMessage
  -> library ShiftUtils.cancelShift
    -> library ShiftStoreUtils.get
    -> library FeatureUtils.validateFeature
    -> library Keys.cancelShiftFeatureDisabledKey
    -> internal validateRequestCancellation
      -> library Chain.currentTimestamp
      -> library Errors.RequestNotYetCancellable
    -> library ShiftUtils.cancelShift


### external executeShiftFromController
-> library FeatureUtils.validateFeature
-> library Keys.executeShiftFeatureDisabledKey
-> library ShiftUtils.executeShift
  -> library ShiftStoreUtils.get
  -> library GasUtils.estimateExecuteShiftGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleShiftError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library ShiftUtils.cancelShift
      -> library ShiftStoreUtils.get
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelShiftFeatureDisabledKey
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library ShiftUtils.cancelShift


### external simulateExecuteShift
-> library ShiftStoreUtils.get


---

## ShiftVault

_File: contracts/shift/ShiftVault.sol_

### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_


---

## StrictBank

_File: contracts/bank/StrictBank.sol_

### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_


### external transferOut
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut
-> internal _transferOut
  -> library Errors.SelfTransferNotSupported
  -> internal _afterTransferOut


### external transferOutNativeToken
-> library TokenUtils.wnt
-> internal _transferOutNativeToken
  -> library Errors.SelfTransferNotSupported
  -> library TokenUtils.withdrawAndSendNativeToken
  -> internal _afterTransferOut


---

## SubaccountGelatoRelayRouter

_File: contracts/router/relay/SubaccountGelatoRelayRouter.sol_

### external batch
-> library RelayUtils.getBatchStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> library SubaccountUtils.validateCreateOrderParams
-> private _handleSubaccountOrderAction
  -> library SubaccountRouterUtils.handleSubaccountAction
-> internal _batch
  -> library Errors.RelayEmptyBatch
  -> internal _createOrder
    -> internal _getContracts
      -> library TokenUtils.wnt
    -> library Order.isSwapOrder
    -> library Order.isIncreaseOrder
    -> internal _sendTokens
      -> library AccountUtils.validateReceiver
  -> internal _updateOrder
    -> internal _getContracts
      -> library TokenUtils.wnt
    -> library OrderStoreUtils.get
    -> library Errors.EmptyOrder
    -> library Errors.Unauthorized
  -> internal _cancelOrder
    -> internal _getContracts
      -> library TokenUtils.wnt
    -> library OrderStoreUtils.get
    -> library Errors.EmptyOrder
    -> library Errors.Unauthorized


### external cancelOrder
-> library RelayUtils.getCancelOrderStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> private _handleSubaccountOrderAction
  -> library SubaccountRouterUtils.handleSubaccountAction
-> internal _cancelOrder
  -> internal _getContracts
    -> library TokenUtils.wnt
  -> library OrderStoreUtils.get
  -> library Errors.EmptyOrder
  -> library Errors.Unauthorized


### external createOrder
-> library RelayUtils.getCreateOrderStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> library SubaccountUtils.validateCreateOrderParams
-> private _handleSubaccountOrderAction
  -> library SubaccountRouterUtils.handleSubaccountAction
-> internal _createOrder
  -> internal _getContracts
    -> library TokenUtils.wnt
  -> library Order.isSwapOrder
  -> library Order.isIncreaseOrder
  -> internal _sendTokens
    -> library AccountUtils.validateReceiver


### external removeSubaccount
-> library RelayUtils.getRemoveSubaccountStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> library SubaccountUtils.removeSubaccount


### external updateOrder
-> library RelayUtils.getUpdateOrderStructHash
-> internal _validateCall
  -> internal _validateCallWithoutSignature
    -> library Errors.InvalidDestinationChainId
    -> internal _isMultichain
    -> library Errors.TokenPermitsNotAllowedForMultichain
    -> library Keys.isSrcChainIdEnabledKey
    -> library Errors.InvalidSrcChainId
    -> internal _validateDeadline
      -> library Errors.DeadlinePassed
  -> library RelayUtils.getDomainSeparator
  -> internal _validateDigest
    -> library Errors.InvalidUserDigest
  -> library RelayUtils.validateSignature
-> private _handleSubaccountOrderAction
  -> library SubaccountRouterUtils.handleSubaccountAction
-> internal _updateOrder
  -> internal _getContracts
    -> library TokenUtils.wnt
  -> library OrderStoreUtils.get
  -> library Errors.EmptyOrder
  -> library Errors.Unauthorized


---

## SubaccountRouter

_File: contracts/router/SubaccountRouter.sol_

### external addSubaccount
-> library SubaccountUtils.addSubaccount


### external cancelOrder
-> library OrderStoreUtils.get
-> library Errors.EmptyOrder
-> internal _handleSubaccountAction
  -> library FeatureUtils.validateFeature
  -> library Keys.subaccountFeatureDisabledKey
  -> library SubaccountUtils.validateIntegrationId
  -> library SubaccountUtils.handleSubaccountAction
-> internal _autoTopUpSubaccount
  -> library SubaccountUtils.getSubaccountAutoTopUpAmount
  -> library TokenUtils.withdrawAndSendNativeToken
  -> library Cast.toBytes32


### external createOrder
-> internal _handleSubaccountAction
  -> library FeatureUtils.validateFeature
  -> library Keys.subaccountFeatureDisabledKey
  -> library SubaccountUtils.validateIntegrationId
  -> library SubaccountUtils.handleSubaccountAction
-> library SubaccountUtils.validateCreateOrderParams
-> internal _autoTopUpSubaccount
  -> library SubaccountUtils.getSubaccountAutoTopUpAmount
  -> library TokenUtils.withdrawAndSendNativeToken
  -> library Cast.toBytes32


### external removeSubaccount
-> library SubaccountUtils.removeSubaccount


### external sendNativeToken
-> library AccountUtils.validateReceiver
-> library TokenUtils.sendNativeToken


### external sendTokens
-> library AccountUtils.validateReceiver


### external sendWnt
-> library AccountUtils.validateReceiver
-> library TokenUtils.depositAndSendWrappedNativeToken


### external setIntegrationId
-> library SubaccountUtils.setSubaccountIntegrationId


### external setMaxAllowedSubaccountActionCount
-> library SubaccountUtils.setMaxAllowedSubaccountActionCount


### external setSubaccountAutoTopUpAmount
-> library SubaccountUtils.setSubaccountAutoTopUpAmount


### external setSubaccountExpiresAt
-> library SubaccountUtils.setSubaccountExpiresAt


### external updateOrder
-> library OrderStoreUtils.get
-> library Errors.EmptyOrder
-> internal _handleSubaccountAction
  -> library FeatureUtils.validateFeature
  -> library Keys.subaccountFeatureDisabledKey
  -> library SubaccountUtils.validateIntegrationId
  -> library SubaccountUtils.handleSubaccountAction
-> internal _autoTopUpSubaccount
  -> library SubaccountUtils.getSubaccountAutoTopUpAmount
  -> library TokenUtils.withdrawAndSendNativeToken
  -> library Cast.toBytes32


---

## SwapHandler

_File: contracts/swap/SwapHandler.sol_

### external swap
-> library SwapUtils.swap


---

## SwapOrderExecutor

_File: contracts/order/SwapOrderExecutor.sol_

### external processOrder
-> library SwapOrderUtils.processOrder


---

## TimelockConfig

_File: contracts/config/TimelockConfig.sol_

### external cancelAction
_(no internal calls)_


### external execute
_(no internal calls)_


### external executeBatch
_(no internal calls)_


### external executeWithOraclePrice
_(no internal calls)_


### external getHash
_(no internal calls)_


### external getHashBatch
_(no internal calls)_


### external increaseTimelockDelay
-> library Errors.InvalidTimelockDelay
-> library Errors.MaxTimelockDelayExceeded
-> internal _schedule
-> internal _signalPendingAction


### external multicall
-> library ErrorUtils.revertWithParsedMessage


### external revokeRole
-> internal _signalPendingAction


### external signalAddOracleSigner
-> library Errors.InvalidOracleSigner
-> internal _schedule
-> internal _signalPendingAction


### external signalGrantRole
-> internal _schedule
-> internal _signalPendingAction


### external signalReduceLentAmount
-> library Errors.EmptyMarket
-> library Errors.EmptyFundingAccount
-> library Errors.EmptyReduceLentAmount
-> internal _schedule
-> internal _signalPendingAction


### external signalRemoveOracleSigner
-> library Errors.InvalidOracleSigner
-> internal _schedule
-> internal _signalPendingAction


### external signalRevokeRole
-> internal _schedule
-> internal _signalPendingAction


### external signalSetAtomicOracleProvider
-> library Keys.isAtomicOracleProviderKey
-> internal _schedule
-> internal _signalPendingAction


### external signalSetDataStream
-> library Errors.ConfigValueExceedsAllowedRange
-> library Keys.dataStreamIdKey
-> library Keys.dataStreamMultiplierKey
-> library Keys.dataStreamSpreadReductionFactorKey
-> internal _scheduleBatch
-> internal _signalPendingAction


### external signalSetEdgeDataStream
-> library Errors.EmptyDataStreamFeedId
-> library Keys.edgeDataStreamIdKey
-> library Keys.edgeDataStreamTokenDecimalsKey
-> internal _scheduleBatch
-> internal _signalPendingAction


### external signalSetFeeReceiver
-> library Errors.InvalidFeeReceiver
-> internal _schedule
-> internal _signalPendingAction


### external signalSetHoldingAddress
-> library Errors.InvalidHoldingAddress
-> internal _schedule
-> internal _signalPendingAction


### external signalSetMaxTotalContributorTokenAmount
-> library Errors.EmptyTarget
-> library Errors.InvalidSetMaxTotalContributorTokenAmountInput
-> library Errors.InvalidContributorToken
-> internal _schedule
-> internal _signalPendingAction


### external signalSetMinContributorPaymentInterval
-> library Errors.EmptyTarget
-> library Errors.MinContributorPaymentIntervalBelowAllowedRange
-> internal _schedule
-> internal _signalPendingAction


### external signalSetOracleProviderEnabled
-> library Keys.isOracleProviderEnabledKey
-> internal _schedule
-> internal _signalPendingAction


### external signalSetPriceFeed
-> library Keys.priceFeedKey
-> library Keys.priceFeedMultiplierKey
-> library Keys.priceFeedHeartbeatDurationKey
-> library Keys.stablePriceKey
-> internal _scheduleBatch
-> internal _signalPendingAction


### external signalWithdrawFromPositionImpactPool
-> library Errors.EmptyMarket
-> library Errors.EmptyReceiver
-> library Errors.EmptyPositionImpactWithdrawalAmount
-> internal _schedule
-> internal _signalPendingAction


### external signalWithdrawTokens
-> library Errors.EmptyTarget
-> library Errors.EmptyToken
-> library Errors.EmptyReceiver
-> library Errors.EmptyWithdrawalAmount
-> internal _schedule
-> internal _signalPendingAction


---

## TimestampInitializer

_File: contracts/migration/TimestampInitializer.sol_

### external initializeOrderTimestamps
-> library Chain.currentTimestamp


### external initializePositionTimestamps
-> library Chain.currentTimestamp


---

## WithdrawalHandler

_File: contracts/exchange/WithdrawalHandler.sol_

### external _executeWithdrawal
-> library FeatureUtils.validateFeature
-> library Keys.executeWithdrawalFeatureDisabledKey
-> external_callback IExecuteWithdrawalUtils.ExecuteWithdrawalParams
-> library ExecuteWithdrawalUtils.executeWithdrawal
  -> library WithdrawalStoreUtils.get
  -> library GasUtils.estimateExecuteWithdrawalGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleWithdrawalError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library WithdrawalUtils.cancelWithdrawal
      -> library WithdrawalStoreUtils.get
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelWithdrawalFeatureDisabledKey
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library WithdrawalUtils.cancelWithdrawal


### external cancelWithdrawal
-> library WithdrawalStoreUtils.get
-> library FeatureUtils.validateFeature
-> library Keys.cancelWithdrawalFeatureDisabledKey
-> internal validateRequestCancellation
  -> library Chain.currentTimestamp
  -> library Errors.RequestNotYetCancellable
-> library WithdrawalUtils.cancelWithdrawal


### external createWithdrawal
-> library FeatureUtils.validateFeature
-> library Keys.createWithdrawalFeatureDisabledKey
-> internal validateDataListLength
  -> library Errors.MaxDataListLengthExceeded
-> library WithdrawalUtils.createWithdrawal


### external executeAtomicWithdrawal
-> library FeatureUtils.validateFeature
-> library Keys.executeAtomicWithdrawalFeatureDisabledKey
-> internal validateDataListLength
  -> library Errors.MaxDataListLengthExceeded
-> library Errors.SwapsNotAllowedForAtomicWithdrawal
-> library WithdrawalUtils.createWithdrawal
  -> library FeatureUtils.validateFeature
  -> library Keys.createWithdrawalFeatureDisabledKey
  -> internal validateDataListLength
    -> library Errors.MaxDataListLengthExceeded
  -> library WithdrawalUtils.createWithdrawal
-> library WithdrawalStoreUtils.get


### external executeWithdrawal
-> library WithdrawalStoreUtils.get
-> library GasUtils.estimateExecuteWithdrawalGasLimit
-> library GasUtils.validateExecutionGas
-> library GasUtils.getExecutionGas
-> internal _handleWithdrawalError
  -> library GasUtils.validateExecutionErrorGas
  -> library ErrorUtils.getErrorSelectorFromData
  -> internal validateNonKeeperError
    -> library OracleUtils.isOracleError
    -> library ErrorUtils.revertWithCustomError
  -> library ErrorUtils.getRevertMessage
  -> library WithdrawalUtils.cancelWithdrawal
    -> library WithdrawalStoreUtils.get
    -> library FeatureUtils.validateFeature
    -> library Keys.cancelWithdrawalFeatureDisabledKey
    -> internal validateRequestCancellation
      -> library Chain.currentTimestamp
      -> library Errors.RequestNotYetCancellable
    -> library WithdrawalUtils.cancelWithdrawal


### external executeWithdrawalFromController
-> library FeatureUtils.validateFeature
-> library Keys.executeWithdrawalFeatureDisabledKey
-> library ExecuteWithdrawalUtils.executeWithdrawal
  -> library WithdrawalStoreUtils.get
  -> library GasUtils.estimateExecuteWithdrawalGasLimit
  -> library GasUtils.validateExecutionGas
  -> library GasUtils.getExecutionGas
  -> internal _handleWithdrawalError
    -> library GasUtils.validateExecutionErrorGas
    -> library ErrorUtils.getErrorSelectorFromData
    -> internal validateNonKeeperError
      -> library OracleUtils.isOracleError
      -> library ErrorUtils.revertWithCustomError
    -> library ErrorUtils.getRevertMessage
    -> library WithdrawalUtils.cancelWithdrawal
      -> library WithdrawalStoreUtils.get
      -> library FeatureUtils.validateFeature
      -> library Keys.cancelWithdrawalFeatureDisabledKey
      -> internal validateRequestCancellation
        -> library Chain.currentTimestamp
        -> library Errors.RequestNotYetCancellable
      -> library WithdrawalUtils.cancelWithdrawal


### external simulateExecuteWithdrawal
-> library WithdrawalStoreUtils.get


---

## WithdrawalVault

_File: contracts/withdrawal/WithdrawalVault.sol_

### external recordTransferIn
-> internal _recordTransferIn


### external syncTokenBalance
_(no internal calls)_

