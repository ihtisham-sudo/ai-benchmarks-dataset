# Callpaths — Midas

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AcreAdapter

_File: contracts/misc/acre/AcreAdapter.sol_

### public asset
_(no internal calls)_


### external convertToAssets
-> private _mTokenToAsset
  -> private _getTokenRate
  -> private _getTokenConfig
  -> public asset


### external convertToShares
-> private _assetToMToken
  -> private _getTokenConfig
  -> public asset
  -> private _getTokenRate


### external deposit
-> public asset
-> private _assetToMToken
  -> private _getTokenConfig
  -> public asset
  -> private _getTokenRate


### external requestRedeem
-> public share
-> public asset


### public share
_(no internal calls)_


---

## AcreMBtc1CustomAggregatorFeed

_File: contracts/products/acremBTC1/AcreMBtc1CustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## AcreMBtc1DataFeed

_File: contracts/products/acremBTC1/AcreMBtc1DataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## AcreMBtc1DepositVault

_File: contracts/products/acremBTC1/AcreMBtc1DepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## AcreMBtc1RedemptionVaultWithSwapper

_File: contracts/products/acremBTC1/AcreMBtc1RedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## BandStdChailinkAdapter

_File: contracts/misc/adapters/BandStdChailinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
-> private _getBandReferenceData


### public latestRound
-> public latestTimestamp
  -> private _getBandReferenceData


### external latestRoundData
-> private _getBandReferenceData


### public latestTimestamp
-> private _getBandReferenceData


### external version
_(no internal calls)_


---

## BeHypeChainlinkAdapter

_File: contracts/misc/adapters/BeHypeChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp
-> public latestAnswer


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## BlacklistableTester

_File: contracts/testers/BlacklistableTester.sol_

### external initialize
-> internal __Blacklistable_init
  -> internal __Blacklistable_init_unchained


### external initializeUnchainedWithoutInitializer
-> internal __Blacklistable_init_unchained


### external initializeWithoutInitializer
-> internal __Blacklistable_init
  -> internal __Blacklistable_init_unchained


### external onlyNotBlacklistedTester
_(no internal calls)_


---

## CUsdoCustomAggregatorFeed

_File: contracts/products/cUSDO/CUsdoCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## CUsdoDataFeed

_File: contracts/products/cUSDO/CUsdoDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## CUsdoDepositVault

_File: contracts/products/cUSDO/CUsdoDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## CUsdoRedemptionVaultWithSwapper

_File: contracts/products/cUSDO/CUsdoRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ChainlinkAdapterBase

_File: contracts/misc/adapters/ChainlinkAdapterBase.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## CompositeDataFeed

_File: contracts/feeds/CompositeDataFeed.sol_

### external changeDenominatorFeed
_(no internal calls)_


### external changeNumeratorFeed
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> internal _computeCompositePrice


### external initialize
-> internal __WithMidasAccessControl_init


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## CompositeDataFeedMultiply

_File: contracts/feeds/CompositeDataFeedMultiply.sol_

### external changeDenominatorFeed
_(no internal calls)_


### external changeNumeratorFeed
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> internal _computeCompositePrice


### external initialize
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## CompositeDataFeedTest

_File: contracts/testers/CompositeDataFeedTest.sol_

### external changeDenominatorFeed
_(no internal calls)_


### external changeNumeratorFeed
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> internal _computeCompositePrice


### external initialize
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## CompositeDataFeedToBandStdAdapter

_File: contracts/misc/adapters/CompositeDataFeedToBandStdAdapter.sol_

### external getReferenceData
-> private _validatePair
-> private _fetchReferenceData
  -> internal _getTimestamp
    -> internal _getAggregatorTimestamp


### external getReferenceDataBulk
-> private _validatePair
-> private _fetchReferenceData
  -> internal _getTimestamp
    -> internal _getAggregatorTimestamp


---

## CustomAggregatorV3CompatibleFeed

_File: contracts/feeds/CustomAggregatorV3CompatibleFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> internal __WithMidasAccessControl_init
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## CustomAggregatorV3CompatibleFeedDiscounted

_File: contracts/feeds/CustomAggregatorV3CompatibleFeedDiscounted.sol_

### public decimals
_(no internal calls)_


### public description
_(no internal calls)_


### public getRoundData
-> internal _calculateDiscountedAnswer
  -> public decimals


### external latestRoundData
-> internal _calculateDiscountedAnswer
  -> public decimals


### external version
_(no internal calls)_


---

## CustomAggregatorV3CompatibleFeedDiscountedTester

_File: contracts/testers/CustomAggregatorV3CompatibleFeedDiscountedTester.sol_

### public decimals
_(no internal calls)_


### public description
_(no internal calls)_


### public getDiscountedAnswer
-> internal _calculateDiscountedAnswer
  -> public decimals


### public getRoundData
-> internal _calculateDiscountedAnswer
  -> public decimals


### external latestRoundData
-> internal _calculateDiscountedAnswer
  -> public decimals


### external version
_(no internal calls)_


---

## CustomAggregatorV3CompatibleFeedGrowth

_File: contracts/feeds/CustomAggregatorV3CompatibleFeedGrowth.sol_

### public applyGrowth
_(no internal calls)_


### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
-> public applyGrowth


### public getRoundDataRaw
_(no internal calls)_


### external initialize
-> internal __WithMidasAccessControl_init


### public lastAnswer
-> public applyGrowth
-> public lastGrowthApr
-> public lastStartedAt


### public lastGrowthApr
_(no internal calls)_


### public lastStartedAt
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData
  -> public applyGrowth


### external latestRoundDataRaw
-> public getRoundDataRaw


### external setMaxGrowthApr
_(no internal calls)_


### external setMinGrowthApr
_(no internal calls)_


### external setOnlyUp
_(no internal calls)_


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
-> public lastAnswer
  -> public applyGrowth
  -> public lastGrowthApr
  -> public lastStartedAt
-> public applyGrowth
-> public lastStartedAt
-> public setRoundData


### external version
_(no internal calls)_


---

## CustomAggregatorV3CompatibleFeedGrowthTester

_File: contracts/testers/CustomAggregatorV3CompatibleFeedGrowthTester.sol_

### public applyGrowth
_(no internal calls)_


### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getDeviation
-> internal _getDeviation


### public getRoundData
-> public applyGrowth


### public getRoundDataRaw
_(no internal calls)_


### external initialize
_(no internal calls)_


### public lastAnswer
-> public applyGrowth
-> public lastGrowthApr
-> public lastStartedAt


### public lastGrowthApr
_(no internal calls)_


### public lastStartedAt
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData
  -> public applyGrowth


### external latestRoundDataRaw
-> public getRoundDataRaw


### public setMaxAnswerDeviation
_(no internal calls)_


### external setMaxGrowthApr
_(no internal calls)_


### external setMinGrowthApr
_(no internal calls)_


### external setOnlyUp
_(no internal calls)_


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
-> public lastAnswer
  -> public applyGrowth
  -> public lastGrowthApr
  -> public lastStartedAt
-> public applyGrowth
-> public lastStartedAt
-> public setRoundData


### external version
_(no internal calls)_


---

## CustomAggregatorV3CompatibleFeedTester

_File: contracts/testers/CustomAggregatorV3CompatibleFeedTester.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getDeviation
-> internal _getDeviation
  -> public decimals


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## DataFeed

_File: contracts/feeds/DataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
-> internal __WithMidasAccessControl_init


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## DataFeedTest

_File: contracts/testers/DataFeedTest.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## DataFeedToBandStdAdapter

_File: contracts/misc/adapters/DataFeedToBandStdAdapter.sol_

### external getReferenceData
-> private _validatePair
-> private _fetchReferenceData
  -> internal _getTimestamp
    -> internal _getAggregatorTimestamp


### external getReferenceDataBulk
-> private _validatePair
-> private _fetchReferenceData
  -> internal _getTimestamp
    -> internal _getAggregatorTimestamp


---

## DecimalsCorrectionTester

_File: contracts/testers/DecimalsCorrectionTester.sol_

### public convertAmountFromBase18Public
_(no internal calls)_


### public convertAmountToBase18Public
_(no internal calls)_


---

## DepositVault

_File: contracts/DepositVault.sol_

### external addPaymentToken
-> internal _validateAddress
-> internal _validateFee


### external addWaivedFeeAccount
_(no internal calls)_


### external approveRequest
-> private _approveRequest
  -> internal _requireVariationTolerance
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external changeTokenAllowance
-> internal _requireTokenExists


### external changeTokenFee
-> internal _requireTokenExists
-> internal _validateFee


### external depositInstant
-> internal _validateUserAccess
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _tokenDecimals
    -> internal _requireTokenExists
    -> internal _convertTokenToUsd
      -> internal _getTokenRate
    -> internal _requireAndUpdateAllowance
    -> internal _truncate
    -> internal _getFeeAmount
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
        -> internal _getTokenRate
    -> internal _validateMinAmount
  -> internal _requireAndUpdateLimit
  -> internal _instantTransferTokensToTokensReceiver
    -> internal _tokenTransferFromUser
  -> internal _tokenTransferFromUser
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> internal _validateUserAccess
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _tokenDecimals
    -> internal _requireTokenExists
    -> internal _convertTokenToUsd
      -> internal _getTokenRate
    -> internal _requireAndUpdateAllowance
    -> internal _truncate
    -> internal _getFeeAmount
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
        -> internal _getTokenRate
    -> internal _validateMinAmount
  -> internal _tokenTransferFromUser


### external freeFromMinAmount
_(no internal calls)_


### external getPaymentTokens
_(no internal calls)_


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
  -> internal __ManageableVault_init
    -> internal _validateAddress
    -> internal _validateFee
-> public initializeV2


### public initializeV1
-> internal __ManageableVault_init
  -> internal _validateAddress
  -> internal _validateFee


### public initializeV2
_(no internal calls)_


### public pauseAdminRole
-> public vaultRole


### external rejectRequest
_(no internal calls)_


### external removePaymentToken
_(no internal calls)_


### external removeWaivedFeeAccount
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _requireVariationTolerance
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _requireVariationTolerance
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _requireVariationTolerance
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public sanctionsListAdminRole
-> public vaultRole


### external setFeeReceiver
-> internal _validateAddress


### external setInstantDailyLimit
_(no internal calls)_


### external setInstantFee
-> internal _validateFee


### external setMaxSupplyCap
_(no internal calls)_


### external setMinAmount
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### external setTokensReceiver
-> internal _validateAddress


### external setVariationTolerance
-> internal _validateFee


### public vaultRole
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## DepositVaultTest

_File: contracts/testers/DepositVaultTest.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external calcAndValidateDeposit
-> internal _calcAndValidateDeposit
  -> internal _convertTokenToUsd
    -> internal _getTokenRate
  -> internal _convertUsdToMToken
    -> private _getMTokenRate
      -> internal _getTokenRate
  -> internal _validateMinAmount


### external convertTokenToUsdTest
-> internal _convertTokenToUsd
  -> internal _getTokenRate


### external convertUsdToMTokenTest
-> internal _convertUsdToMToken
  -> private _getMTokenRate
    -> internal _getTokenRate


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
      -> internal _getTokenRate
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
        -> internal _getTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
      -> internal _getTokenRate
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
        -> internal _getTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setGetTokenRateValue
_(no internal calls)_


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### external setOverrideGetTokenRate
_(no internal calls)_


### external tokenTransferFromToTester
_(no internal calls)_


### external tokenTransferToUserTester
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DepositVaultWithUSTB

_File: contracts/DepositVaultWithUSTB.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> external initialize


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### external setUstbDepositsEnabled
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DepositVaultWithUSTBTest

_File: contracts/testers/DepositVaultWithUSTBTest.sol_

### external calcAndValidateDeposit
_(no internal calls)_


### external convertTokenToUsdTest
_(no internal calls)_


### external convertUsdToMTokenTest
_(no internal calls)_


### external initialize
-> external initialize


### external setGetTokenRateValue
_(no internal calls)_


### external setOverrideGetTokenRate
_(no internal calls)_


### external setUstbDepositsEnabled
_(no internal calls)_


### external tokenTransferFromToTester
_(no internal calls)_


### external tokenTransferToUserTester
_(no internal calls)_


---

## DnEthCustomAggregatorFeed

_File: contracts/products/dnETH/DnEthCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## DnEthDataFeed

_File: contracts/products/dnETH/DnEthDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## DnEthDepositVault

_File: contracts/products/dnETH/DnEthDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnEthRedemptionVaultWithSwapper

_File: contracts/products/dnETH/DnEthRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnFartCustomAggregatorFeed

_File: contracts/products/dnFART/DnFartCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## DnFartDataFeed

_File: contracts/products/dnFART/DnFartDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## DnFartDepositVault

_File: contracts/products/dnFART/DnFartDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnFartRedemptionVaultWithSwapper

_File: contracts/products/dnFART/DnFartRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnHypeCustomAggregatorFeed

_File: contracts/products/dnHYPE/DnHypeCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## DnHypeDataFeed

_File: contracts/products/dnHYPE/DnHypeDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## DnHypeDepositVault

_File: contracts/products/dnHYPE/DnHypeDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnHypeRedemptionVaultWithSwapper

_File: contracts/products/dnHYPE/DnHypeRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnPumpCustomAggregatorFeed

_File: contracts/products/dnPUMP/DnPumpCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## DnPumpDataFeed

_File: contracts/products/dnPUMP/DnPumpDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## DnPumpDepositVault

_File: contracts/products/dnPUMP/DnPumpDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnPumpRedemptionVaultWithSwapper

_File: contracts/products/dnPUMP/DnPumpRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnTestCustomAggregatorFeedGrowth

_File: contracts/products/dnTEST/DnTestCustomAggregatorFeedGrowth.sol_

### public applyGrowth
_(no internal calls)_


### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
-> public applyGrowth


### public getRoundDataRaw
_(no internal calls)_


### external initialize
_(no internal calls)_


### public lastAnswer
-> public applyGrowth
-> public lastGrowthApr
-> public lastStartedAt


### public lastGrowthApr
_(no internal calls)_


### public lastStartedAt
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData
  -> public applyGrowth


### external latestRoundDataRaw
-> public getRoundDataRaw


### external setMaxGrowthApr
_(no internal calls)_


### external setMinGrowthApr
_(no internal calls)_


### external setOnlyUp
_(no internal calls)_


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
-> public lastAnswer
  -> public applyGrowth
  -> public lastGrowthApr
  -> public lastStartedAt
-> public applyGrowth
-> public lastStartedAt
-> public setRoundData


### external version
_(no internal calls)_


---

## DnTestDataFeed

_File: contracts/products/dnTEST/DnTestDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## DnTestDepositVault

_File: contracts/products/dnTEST/DnTestDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## DnTestRedemptionVaultWithSwapper

_File: contracts/products/dnTEST/DnTestRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ERC4626ChainlinkAdapter

_File: contracts/misc/adapters/ERC4626ChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
-> public vaultDecimals


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp
-> public latestAnswer
  -> public vaultDecimals


### public latestTimestamp
_(no internal calls)_


### public vaultDecimals
_(no internal calls)_


### external version
_(no internal calls)_


---

## EUsdDepositVault

_File: contracts/products/eUSD/EUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public greenlistedRole
_(no internal calls)_


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## EUsdRedemptionVault

_File: contracts/products/eUSD/EUsdRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### public greenlistedRole
_(no internal calls)_


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## EUsdRedemptionVaultWithBUIDL

_File: contracts/products/eUSD/EUsdRedemptionVaultWithBUIDL.sol_

### public greenlistedRole
_(no internal calls)_


### external initialize
_(no internal calls)_


### external setMinBuidlBalance
_(no internal calls)_


### external setMinBuidlToRedeem
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## Greenlistable

_File: contracts/access/Greenlistable.sol_

### public greenlistedRole
_(no internal calls)_


### external setGreenlistEnable
-> internal _onlyGreenlistToggler


---

## GreenlistableTester

_File: contracts/testers/GreenlistableTester.sol_

### public greenlistTogglerRole
_(no internal calls)_


### public greenlistedRole
_(no internal calls)_


### external initialize
-> internal __Greenlistable_init
  -> internal __Greenlistable_init_unchained


### external initializeUnchainedWithoutInitializer
-> internal __Greenlistable_init_unchained


### external initializeWithoutInitializer
-> internal __Greenlistable_init
  -> internal __Greenlistable_init_unchained


### external onlyGreenlistTogglerTester
-> internal _onlyGreenlistToggler


### external onlyGreenlistedTester
_(no internal calls)_


### external setGreenlistEnable
-> internal _onlyGreenlistToggler


---

## HBUsdcCustomAggregatorFeed

_File: contracts/products/hbUSDC/HBUsdcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## HBUsdcDataFeed

_File: contracts/products/hbUSDC/HBUsdcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## HBUsdcDepositVault

_File: contracts/products/hbUSDC/HBUsdcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HBUsdcRedemptionVaultWithSwapper

_File: contracts/products/hbUSDC/HBUsdcRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HBUsdtCustomAggregatorFeed

_File: contracts/products/hbUSDT/HBUsdtCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## HBUsdtDataFeed

_File: contracts/products/hbUSDT/HBUsdtDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## HBUsdtDepositVault

_File: contracts/products/hbUSDT/HBUsdtDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HBUsdtRedemptionVaultWithSwapper

_File: contracts/products/hbUSDT/HBUsdtRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HBXautCustomAggregatorFeed

_File: contracts/products/hbXAUt/HBXautCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## HBXautDataFeed

_File: contracts/products/hbXAUt/HBXautDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## HBXautDepositVault

_File: contracts/products/hbXAUt/HBXautDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HBXautRedemptionVaultWithSwapper

_File: contracts/products/hbXAUt/HBXautRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HypeBtcCustomAggregatorFeed

_File: contracts/products/hypeBTC/HypeBtcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## HypeBtcDataFeed

_File: contracts/products/hypeBTC/HypeBtcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## HypeBtcDepositVault

_File: contracts/products/hypeBTC/HypeBtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HypeBtcRedemptionVaultWithSwapper

_File: contracts/products/hypeBTC/HypeBtcRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HypeEthCustomAggregatorFeed

_File: contracts/products/hypeETH/HypeEthCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## HypeEthDataFeed

_File: contracts/products/hypeETH/HypeEthDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## HypeEthDepositVault

_File: contracts/products/hypeETH/HypeEthDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HypeEthRedemptionVaultWithSwapper

_File: contracts/products/hypeETH/HypeEthRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HypeUsdCustomAggregatorFeed

_File: contracts/products/hypeUSD/HypeUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## HypeUsdDataFeed

_File: contracts/products/hypeUSD/HypeUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## HypeUsdDepositVault

_File: contracts/products/hypeUSD/HypeUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## HypeUsdRedemptionVaultWithSwapper

_File: contracts/products/hypeUSD/HypeUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## JIV

_File: contracts/products/JIV/JIV.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## JivCustomAggregatorFeed

_File: contracts/products/JIV/JivCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## JivDataFeed

_File: contracts/products/JIV/JivDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## JivDepositVault

_File: contracts/products/JIV/JivDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## JivRedemptionVaultWithSwapper

_File: contracts/products/JIV/JivRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KitBtcCustomAggregatorFeed

_File: contracts/products/kitBTC/KitBtcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## KitBtcDataFeed

_File: contracts/products/kitBTC/KitBtcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## KitBtcDepositVault

_File: contracts/products/kitBTC/KitBtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KitBtcRedemptionVaultWithSwapper

_File: contracts/products/kitBTC/KitBtcRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KitHypeCustomAggregatorFeed

_File: contracts/products/kitHYPE/KitHypeCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## KitHypeDataFeed

_File: contracts/products/kitHYPE/KitHypeDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## KitHypeDepositVault

_File: contracts/products/kitHYPE/KitHypeDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KitHypeRedemptionVaultWithSwapper

_File: contracts/products/kitHYPE/KitHypeRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KitUsdCustomAggregatorFeed

_File: contracts/products/kitUSD/KitUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## KitUsdDataFeed

_File: contracts/products/kitUSD/KitUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## KitUsdDepositVault

_File: contracts/products/kitUSD/KitUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KitUsdRedemptionVaultWithSwapper

_File: contracts/products/kitUSD/KitUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KmiUsdCustomAggregatorFeed

_File: contracts/products/kmiUSD/KmiUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## KmiUsdDataFeed

_File: contracts/products/kmiUSD/KmiUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## KmiUsdDepositVault

_File: contracts/products/kmiUSD/KmiUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## KmiUsdRedemptionVaultWithSwapper

_File: contracts/products/kmiUSD/KmiUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## LiquidHypeCustomAggregatorFeed

_File: contracts/products/liquidHYPE/LiquidHypeCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## LiquidHypeDataFeed

_File: contracts/products/liquidHYPE/LiquidHypeDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## LiquidHypeDepositVault

_File: contracts/products/liquidHYPE/LiquidHypeDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## LiquidHypeRedemptionVaultWithSwapper

_File: contracts/products/liquidHYPE/LiquidHypeRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## LiquidReserveCustomAggregatorFeed

_File: contracts/products/liquidRESERVE/LiquidReserveCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## LiquidReserveDataFeed

_File: contracts/products/liquidRESERVE/LiquidReserveDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## LiquidReserveDepositVault

_File: contracts/products/liquidRESERVE/LiquidReserveDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## LiquidReserveRedemptionVaultWithSwapper

_File: contracts/products/liquidRESERVE/LiquidReserveRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## LstHypeCustomAggregatorFeed

_File: contracts/products/lstHYPE/LstHypeCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## LstHypeDataFeed

_File: contracts/products/lstHYPE/LstHypeDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## LstHypeDepositVault

_File: contracts/products/lstHYPE/LstHypeDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## LstHypeRedemptionVaultWithSwapper

_File: contracts/products/lstHYPE/LstHypeRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MApolloCustomAggregatorFeed

_File: contracts/products/mAPOLLO/MApolloCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MApolloDataFeed

_File: contracts/products/mAPOLLO/MApolloDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MApolloDepositVault

_File: contracts/products/mAPOLLO/MApolloDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MApolloRedemptionVaultWithSwapper

_File: contracts/products/mAPOLLO/MApolloRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MBasisCustomAggregatorFeed

_File: contracts/products/mBASIS/MBasisCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MBasisDataFeed

_File: contracts/products/mBASIS/MBasisDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MBasisDepositVault

_File: contracts/products/mBASIS/MBasisDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MBasisRedemptionVault

_File: contracts/products/mBASIS/MBasisRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MBasisRedemptionVaultWithBUIDL

_File: contracts/products/mBASIS/MBasisRedemptionVaultWithBUIDL.sol_

### external initialize
_(no internal calls)_


### external setMinBuidlBalance
_(no internal calls)_


### external setMinBuidlToRedeem
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MBasisRedemptionVaultWithSwapper

_File: contracts/products/mBASIS/MBasisRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MBtcCustomAggregatorFeed

_File: contracts/products/mBTC/MBtcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MBtcDataFeed

_File: contracts/products/mBTC/MBtcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MBtcDepositVault

_File: contracts/products/mBTC/MBtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MBtcRedemptionVault

_File: contracts/products/mBTC/MBtcRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MEdgeCustomAggregatorFeed

_File: contracts/products/mEDGE/MEdgeCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MEdgeDataFeed

_File: contracts/products/mEDGE/MEdgeDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MEdgeDepositVault

_File: contracts/products/mEDGE/MEdgeDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MEdgeRedemptionVaultWithSwapper

_File: contracts/products/mEDGE/MEdgeRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MEvUsdCustomAggregatorFeed

_File: contracts/products/mEVUSD/MEvUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MEvUsdDataFeed

_File: contracts/products/mEVUSD/MEvUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MEvUsdDepositVault

_File: contracts/products/mEVUSD/MEvUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MEvUsdRedemptionVaultWithSwapper

_File: contracts/products/mEVUSD/MEvUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MFOneCustomAggregatorFeed

_File: contracts/products/mFONE/MFOneCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MFOneDataFeed

_File: contracts/products/mFONE/MFOneDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MFOneDepositVault

_File: contracts/products/mFONE/MFOneDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MFOneRedemptionVaultWithSwapper

_File: contracts/products/mFONE/MFOneRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MFarmCustomAggregatorFeed

_File: contracts/products/mFARM/MFarmCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MFarmDataFeed

_File: contracts/products/mFARM/MFarmDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MFarmDepositVault

_File: contracts/products/mFARM/MFarmDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MFarmRedemptionVaultWithSwapper

_File: contracts/products/mFARM/MFarmRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MHyperBtcCustomAggregatorFeed

_File: contracts/products/mHyperBTC/MHyperBtcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MHyperBtcDataFeed

_File: contracts/products/mHyperBTC/MHyperBtcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MHyperBtcDepositVault

_File: contracts/products/mHyperBTC/MHyperBtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MHyperBtcRedemptionVaultWithSwapper

_File: contracts/products/mHyperBTC/MHyperBtcRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MHyperCustomAggregatorFeed

_File: contracts/products/mHYPER/MHyperCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MHyperDataFeed

_File: contracts/products/mHYPER/MHyperDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MHyperDepositVault

_File: contracts/products/mHYPER/MHyperDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MHyperEthCustomAggregatorFeed

_File: contracts/products/mHyperETH/MHyperEthCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MHyperEthDataFeed

_File: contracts/products/mHyperETH/MHyperEthDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MHyperEthDepositVault

_File: contracts/products/mHyperETH/MHyperEthDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MHyperEthRedemptionVaultWithSwapper

_File: contracts/products/mHyperETH/MHyperEthRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MHyperRedemptionVaultWithSwapper

_File: contracts/products/mHYPER/MHyperRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MKRalphaCustomAggregatorFeed

_File: contracts/products/mKRalpha/MKRalphaCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public initializeV2
  -> public decimals


### public initializeV2
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MKRalphaDataFeed

_File: contracts/products/mKRalpha/MKRalphaDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MKRalphaDepositVault

_File: contracts/products/mKRalpha/MKRalphaDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MKRalphaRedemptionVaultWithSwapper

_File: contracts/products/mKRalpha/MKRalphaRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MLiquidityCustomAggregatorFeed

_File: contracts/products/mLIQUIDITY/MLiquidityCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MLiquidityDataFeed

_File: contracts/products/mLIQUIDITY/MLiquidityDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MLiquidityDepositVault

_File: contracts/products/mLIQUIDITY/MLiquidityDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MLiquidityRedemptionVault

_File: contracts/products/mLIQUIDITY/MLiquidityRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MM1UsdCustomAggregatorFeed

_File: contracts/products/mM1USD/MM1UsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MM1UsdDataFeed

_File: contracts/products/mM1USD/MM1UsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MM1UsdDepositVault

_File: contracts/products/mM1USD/MM1UsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MM1UsdRedemptionVaultWithSwapper

_File: contracts/products/mM1USD/MM1UsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MMevCustomAggregatorFeed

_File: contracts/products/mMEV/MMevCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MMevDataFeed

_File: contracts/products/mMEV/MMevDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MMevDepositVault

_File: contracts/products/mMEV/MMevDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MMevRedemptionVaultWithSwapper

_File: contracts/products/mMEV/MMevRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MPortofinoCustomAggregatorFeed

_File: contracts/products/mPortofino/MPortofinoCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MPortofinoDataFeed

_File: contracts/products/mPortofino/MPortofinoDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MPortofinoDepositVault

_File: contracts/products/mPortofino/MPortofinoDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MPortofinoRedemptionVaultWithSwapper

_File: contracts/products/mPortofino/MPortofinoRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRe7BtcCustomAggregatorFeed

_File: contracts/products/mRE7BTC/MRe7BtcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MRe7BtcDataFeed

_File: contracts/products/mRE7BTC/MRe7BtcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MRe7BtcDepositVault

_File: contracts/products/mRE7BTC/MRe7BtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRe7BtcRedemptionVaultWithSwapper

_File: contracts/products/mRE7BTC/MRe7BtcRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRe7CustomAggregatorFeed

_File: contracts/products/mRE7/MRe7CustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public initializeV3
  -> public decimals


### public initializeV3
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MRe7DataFeed

_File: contracts/products/mRE7/MRe7DataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MRe7DepositVault

_File: contracts/products/mRE7/MRe7DepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRe7RedemptionVaultWithSwapper

_File: contracts/products/mRE7/MRe7RedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRe7SolCustomAggregatorFeed

_File: contracts/products/mRE7SOL/MRe7SolCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MRe7SolDataFeed

_File: contracts/products/mRE7SOL/MRe7SolDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MRe7SolDepositVault

_File: contracts/products/mRE7SOL/MRe7SolDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRe7SolRedemptionVault

_File: contracts/products/mRE7SOL/MRe7SolRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRoxCustomAggregatorFeed

_File: contracts/products/mROX/MRoxCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MRoxDataFeed

_File: contracts/products/mROX/MRoxDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MRoxDepositVault

_File: contracts/products/mROX/MRoxDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MRoxRedemptionVaultWithSwapper

_File: contracts/products/mROX/MRoxRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MSlCustomAggregatorFeed

_File: contracts/products/mSL/MSLCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MSlDataFeed

_File: contracts/products/mSL/MSlDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MSlDepositVault

_File: contracts/products/mSL/MSlDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MSlRedemptionVaultWithSwapper

_File: contracts/products/mSL/MSlRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MSyrupUsdCustomAggregatorFeed

_File: contracts/products/msyrupUSD/MSyrupUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MSyrupUsdDataFeed

_File: contracts/products/msyrupUSD/MSyrupUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MSyrupUsdDepositVault

_File: contracts/products/msyrupUSD/MSyrupUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MSyrupUsdRedemptionVaultWithSwapper

_File: contracts/products/msyrupUSD/MSyrupUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MSyrupUsdpCustomAggregatorFeed

_File: contracts/products/msyrupUSDp/MSyrupUsdpCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MSyrupUsdpDataFeed

_File: contracts/products/msyrupUSDp/MSyrupUsdpDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MSyrupUsdpDepositVault

_File: contracts/products/msyrupUSDp/MSyrupUsdpDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MSyrupUsdpRedemptionVaultWithSwapper

_File: contracts/products/msyrupUSDp/MSyrupUsdpRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MTBillCustomAggregatorFeed

_File: contracts/products/mTBILL/MTBillCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MTBillCustomAggregatorFeedGrowth

_File: contracts/products/mTBILL/MTBillCustomAggregatorFeedGrowth.sol_

### public applyGrowth
_(no internal calls)_


### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
-> public applyGrowth


### public getRoundDataRaw
_(no internal calls)_


### external initialize
_(no internal calls)_


### public lastAnswer
-> public applyGrowth
-> public lastGrowthApr
-> public lastStartedAt


### public lastGrowthApr
_(no internal calls)_


### public lastStartedAt
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData
  -> public applyGrowth


### external latestRoundDataRaw
-> public getRoundDataRaw


### external setMaxGrowthApr
_(no internal calls)_


### external setMinGrowthApr
_(no internal calls)_


### external setOnlyUp
_(no internal calls)_


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
-> public lastAnswer
  -> public applyGrowth
  -> public lastGrowthApr
  -> public lastStartedAt
-> public applyGrowth
-> public lastStartedAt
-> public setRoundData


### external version
_(no internal calls)_


---

## MTBillDataFeed

_File: contracts/products/mTBILL/MTBillDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MTuCustomAggregatorFeed

_File: contracts/products/mTU/MTuCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MTuDataFeed

_File: contracts/products/mTU/MTuDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MTuDepositVault

_File: contracts/products/mTU/MTuDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MTuRedemptionVaultWithSwapper

_File: contracts/products/mTU/MTuRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MWildUsdCustomAggregatorFeed

_File: contracts/products/mWildUSD/MWildUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MWildUsdDataFeed

_File: contracts/products/mWildUSD/MWildUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MWildUsdDepositVault

_File: contracts/products/mWildUSD/MWildUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MWildUsdRedemptionVaultWithSwapper

_File: contracts/products/mWildUSD/MWildUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MXrpCustomAggregatorFeed

_File: contracts/products/mXRP/MXrpCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MXrpDataFeed

_File: contracts/products/mXRP/MXrpDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MXrpDepositVault

_File: contracts/products/mXRP/MXrpDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MXrpRedemptionVaultWithSwapper

_File: contracts/products/mXRP/MXrpRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ManageableVault

_File: contracts/abstract/ManageableVault.sol_

### external addPaymentToken
-> internal _validateAddress
-> internal _validateFee


### external addWaivedFeeAccount
_(no internal calls)_


### external changeTokenAllowance
-> internal _requireTokenExists


### external changeTokenFee
-> internal _requireTokenExists
-> internal _validateFee


### external freeFromMinAmount
_(no internal calls)_


### external getPaymentTokens
_(no internal calls)_


### public greenlistedRole
_(no internal calls)_


### external pause
_(no internal calls)_


### public pauseAdminRole
_(no internal calls)_


### external pauseFn
_(no internal calls)_


### external removePaymentToken
_(no internal calls)_


### external removeWaivedFeeAccount
_(no internal calls)_


### public sanctionsListAdminRole
_(no internal calls)_


### external setFeeReceiver
-> internal _validateAddress


### external setGreenlistEnable
-> internal _onlyGreenlistToggler


### external setInstantDailyLimit
_(no internal calls)_


### external setInstantFee
-> internal _validateFee


### external setMinAmount
_(no internal calls)_


### external setSanctionsList
-> public sanctionsListAdminRole


### external setTokensReceiver
-> internal _validateAddress


### external setVariationTolerance
-> internal _validateFee


### external unpause
_(no internal calls)_


### external unpauseFn
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## ManageableVaultTester

_File: contracts/testers/ManageableVaultTester.sol_

### external addPaymentToken
-> internal _validateAddress
-> internal _validateFee


### external addWaivedFeeAccount
_(no internal calls)_


### external changeTokenAllowance
-> internal _requireTokenExists


### external changeTokenFee
-> internal _requireTokenExists
-> internal _validateFee


### external freeFromMinAmount
_(no internal calls)_


### external getPaymentTokens
_(no internal calls)_


### public greenlistTogglerRole
_(no internal calls)_


### external initialize
-> internal __ManageableVault_init
  -> internal _validateAddress
  -> internal _validateFee


### external initializeWithoutInitializer
-> internal __ManageableVault_init
  -> internal _validateAddress
  -> internal _validateFee


### public pauseAdminRole
-> public vaultRole


### external removePaymentToken
_(no internal calls)_


### external removeWaivedFeeAccount
_(no internal calls)_


### public sanctionsListAdminRole
-> public vaultRole


### external setFeeReceiver
-> internal _validateAddress


### external setInstantDailyLimit
_(no internal calls)_


### external setInstantFee
-> internal _validateFee


### external setMinAmount
_(no internal calls)_


### external setTokensReceiver
-> internal _validateAddress


### external setVariationTolerance
-> internal _validateFee


### public vaultRole
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## MantleLspStakingChainlinkAdapter

_File: contracts/misc/adapters/MantleLspStakingChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp
-> public latestAnswer


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## MevBtcCustomAggregatorFeed

_File: contracts/products/mevBTC/MevBtcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## MevBtcDataFeed

_File: contracts/products/mevBTC/MevBtcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## MevBtcDepositVault

_File: contracts/products/mevBTC/MevBtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MevBtcRedemptionVaultWithSwapper

_File: contracts/products/mevBTC/MevBtcRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## MidasAccessControl

_File: contracts/access/MidasAccessControl.sol_

### external grantRoleMult
_(no internal calls)_


### external initialize
-> private _setupRoles


### public renounceRole
_(no internal calls)_


### external revokeRoleMult
_(no internal calls)_


---

## MidasAccessControlTest

_File: contracts/testers/MidasAccessControlTest.sol_

### external grantRoleMult
_(no internal calls)_


### external initialize
-> private _setupRoles


### public renounceRole
_(no internal calls)_


### external revokeRoleMult
_(no internal calls)_


---

## MidasAxelarVaultExecutable

_File: contracts/misc/axelar/MidasAxelarVaultExecutable.sol_

### external depositAndSend
-> internal _depositAndSend
  -> private _getChainNameHash
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _bytesToAddress
  -> internal _itsTransfer


### external handleExecuteWithInterchainToken
-> internal _depositAndSend
  -> private _getChainNameHash
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _bytesToAddress
  -> internal _itsTransfer
-> internal _redeemAndSend
  -> private _getChainNameHash
  -> internal _redeem
    -> internal _balanceOf
  -> internal _bytesToAddress
  -> internal _itsTransfer


### external initialize
_(no internal calls)_


### external redeemAndSend
-> internal _redeemAndSend
  -> private _getChainNameHash
  -> internal _redeem
    -> internal _balanceOf
  -> internal _bytesToAddress
  -> internal _itsTransfer


---

## MidasAxelarVaultExecutableTester

_File: contracts/testers/MidasAxelarVaultExecutableTester.sol_

### external balanceOfPublic
-> internal _balanceOf


### external bytesToAddressPublic
-> internal _bytesToAddress


### external depositAndSend
-> internal _depositAndSend
  -> private _getChainNameHash
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _bytesToAddress
  -> internal _itsTransfer


### external depositAndSendPublic
-> internal _depositAndSend
  -> private _getChainNameHash
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _bytesToAddress
  -> internal _itsTransfer


### external depositPublic
-> internal _deposit
  -> internal _balanceOf
  -> internal _tokenAmountToBase18


### external handleExecuteWithInterchainToken
-> internal _depositAndSend
  -> private _getChainNameHash
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _bytesToAddress
  -> internal _itsTransfer
-> internal _redeemAndSend
  -> private _getChainNameHash
  -> internal _redeem
    -> internal _balanceOf
  -> internal _bytesToAddress
  -> internal _itsTransfer


### external initialize
_(no internal calls)_


### external itsTransferPublic
-> internal _itsTransfer


### external redeemAndSend
-> internal _redeemAndSend
  -> private _getChainNameHash
  -> internal _redeem
    -> internal _balanceOf
  -> internal _bytesToAddress
  -> internal _itsTransfer


### external redeemAndSendPublic
-> internal _redeemAndSend
  -> private _getChainNameHash
  -> internal _redeem
    -> internal _balanceOf
  -> internal _bytesToAddress
  -> internal _itsTransfer


### external redeemPublic
-> internal _redeem
  -> internal _balanceOf


---

## MidasLzMintBurnOFTAdapter

_File: contracts/misc/layerzero/MidasLzMintBurnOFTAdapter.sol_

### external burn
_(no internal calls)_


### external getRateLimit
_(no internal calls)_


### external mint
_(no internal calls)_


### external setRateLimits
_(no internal calls)_


### public sharedDecimals
_(no internal calls)_


---

## MidasLzOFT

_File: contracts/misc/layerzero/MidasLzOFT.sol_

### public sharedDecimals
_(no internal calls)_


---

## MidasLzOFTAdapter

_File: contracts/misc/layerzero/MidasLzOFTAdapter.sol_

### public sharedDecimals
_(no internal calls)_


---

## MidasLzVaultComposerSync

_File: contracts/misc/layerzero/MidasLzVaultComposerSync.sol_

### external depositAndSend
-> internal _depositAndSend
  -> internal _parseDepositExtraOptions
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _sendOft
  -> internal _requireNoValue
-> library OFTComposeMsgCodec.addressToBytes32


### public handleCompose
-> internal _depositAndSend
  -> internal _parseDepositExtraOptions
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _sendOft
  -> internal _requireNoValue
-> internal _redeemAndSend
  -> internal _redeem
    -> internal _balanceOf
  -> internal _sendOft
  -> internal _requireNoValue


### external initialize
_(no internal calls)_


### external lzCompose
-> internal _refund
  -> library OFTComposeMsgCodec.srcEid
  -> library OFTComposeMsgCodec.composeFrom
  -> internal _sendOft


### external redeemAndSend
-> internal _redeemAndSend
  -> internal _redeem
    -> internal _balanceOf
  -> internal _sendOft
  -> internal _requireNoValue
-> library OFTComposeMsgCodec.addressToBytes32


---

## MidasLzVaultComposerSyncTester

_File: contracts/testers/MidasLzVaultComposerSyncTester.sol_

### external balanceOfPublic
-> internal _balanceOf


### external depositAndSend
-> internal _depositAndSend
  -> internal _parseDepositExtraOptions
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _sendOft
  -> internal _requireNoValue
-> library OFTComposeMsgCodec.addressToBytes32


### external depositAndSendPublic
-> internal _depositAndSend
  -> internal _parseDepositExtraOptions
  -> internal _deposit
    -> internal _balanceOf
    -> internal _tokenAmountToBase18
  -> internal _sendOft
  -> internal _requireNoValue


### external depositPublic
-> internal _deposit
  -> internal _balanceOf
  -> internal _tokenAmountToBase18


### public handleCompose
_(no internal calls)_


### external initialize
_(no internal calls)_


### external lzCompose
-> internal _refund
  -> library OFTComposeMsgCodec.srcEid
  -> library OFTComposeMsgCodec.composeFrom
  -> internal _sendOft


### external parseExtraOptionsPublic
-> internal _parseDepositExtraOptions


### external redeemAndSend
-> internal _redeemAndSend
  -> internal _redeem
    -> internal _balanceOf
  -> internal _sendOft
  -> internal _requireNoValue
-> library OFTComposeMsgCodec.addressToBytes32


### external redeemAndSendPublic
-> internal _redeemAndSend
  -> internal _redeem
    -> internal _balanceOf
  -> internal _sendOft
  -> internal _requireNoValue


### external redeemPublic
-> internal _redeem
  -> internal _balanceOf


### external sendOftPublic
-> internal _sendOft


### external setHandleComposeType
_(no internal calls)_


---

## MidasTimelockController

_File: contracts/access/MidasTimelockController.sol_

### external getInitialExecutors
_(no internal calls)_


### external getInitialProposers
_(no internal calls)_


---

## ObeatUsdCustomAggregatorFeed

_File: contracts/products/obeatUSD/ObeatUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## ObeatUsdDataFeed

_File: contracts/products/obeatUSD/ObeatUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## ObeatUsdDepositVault

_File: contracts/products/obeatUSD/ObeatUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ObeatUsdRedemptionVaultWithSwapper

_File: contracts/products/obeatUSD/ObeatUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## Pausable

_File: contracts/access/Pausable.sol_

### external pause
_(no internal calls)_


### external pauseFn
_(no internal calls)_


### external unpause
_(no internal calls)_


### external unpauseFn
_(no internal calls)_


---

## PausableTester

_File: contracts/testers/PausableTester.sol_

### external initialize
-> internal __Pausable_init


### external initializeWithoutInitializer
-> internal __Pausable_init


### external pause
_(no internal calls)_


### public pauseAdminRole
_(no internal calls)_


### external pauseFn
_(no internal calls)_


### external unpause
_(no internal calls)_


### external unpauseFn
_(no internal calls)_


---

## PlUsdCustomAggregatorFeed

_File: contracts/products/plUSD/PlUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## PlUsdDataFeed

_File: contracts/products/plUSD/PlUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## PlUsdDepositVault

_File: contracts/products/plUSD/PlUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## PlUsdRedemptionVaultWithSwapper

_File: contracts/products/plUSD/PlUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## PythChainlinkAdapter

_File: contracts/misc/adapters/PythChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
_(no internal calls)_


### public latestTimestamp
_(no internal calls)_


### public updateFeeds
_(no internal calls)_


### external version
_(no internal calls)_


---

## RedemptionVault

_File: contracts/RedemptionVault.sol_

### external addPaymentToken
-> internal _validateAddress
-> internal _validateFee


### external addWaivedFeeAccount
_(no internal calls)_


### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _requireVariationTolerance
  -> internal _tokenDecimals
  -> internal _truncate
  -> internal _validateLiquidity
  -> internal _tokenTransferFromTo
  -> internal _requireAndUpdateAllowance
  -> external_callback mToken.burn


### external changeTokenAllowance
-> internal _requireTokenExists


### external changeTokenFee
-> internal _requireTokenExists
-> internal _validateFee


### external freeFromMinAmount
_(no internal calls)_


### external getPaymentTokens
_(no internal calls)_


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init
  -> internal __ManageableVault_init
    -> internal _validateAddress
    -> internal _validateFee
  -> internal _validateFee
  -> internal _validateAddress


### public pauseAdminRole
-> public vaultRole


### external redeemFiatRequest
-> internal _validateUserAccess
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem
    -> internal _getFeeAmount
    -> internal _requireTokenExists
  -> internal _getTokenRate
  -> internal _tokenTransferFromUser


### external redeemInstant
-> internal _validateUserAccess
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
    -> internal _getFeeAmount
    -> internal _requireTokenExists
  -> internal _requireAndUpdateLimit
  -> internal _tokenDecimals
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
      -> internal _getTokenRate
  -> internal _convertUsdToToken
    -> internal _getTokenRate
  -> internal _truncate
  -> internal _requireAndUpdateAllowance
  -> external_callback mToken.burn
  -> internal _tokenTransferFromUser
  -> internal _tokenTransferToUser


### external redeemRequest
-> internal _validateUserAccess
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem
    -> internal _getFeeAmount
    -> internal _requireTokenExists
  -> internal _getTokenRate
  -> internal _tokenTransferFromUser


### external rejectRequest
-> internal _validateRequest


### external removePaymentToken
_(no internal calls)_


### external removeWaivedFeeAccount
_(no internal calls)_


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _requireVariationTolerance
  -> internal _tokenDecimals
  -> internal _truncate
  -> internal _validateLiquidity
  -> internal _tokenTransferFromTo
  -> internal _requireAndUpdateAllowance
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _requireVariationTolerance
  -> internal _tokenDecimals
  -> internal _truncate
  -> internal _validateLiquidity
  -> internal _tokenTransferFromTo
  -> internal _requireAndUpdateAllowance
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _requireVariationTolerance
  -> internal _tokenDecimals
  -> internal _truncate
  -> internal _validateLiquidity
  -> internal _tokenTransferFromTo
  -> internal _requireAndUpdateAllowance
  -> external_callback mToken.burn


### public sanctionsListAdminRole
-> public vaultRole


### external setFeeReceiver
-> internal _validateAddress


### external setFiatAdditionalFee
-> internal _validateFee


### external setFiatFlatFee
_(no internal calls)_


### external setInstantDailyLimit
_(no internal calls)_


### external setInstantFee
-> internal _validateFee


### external setMinAmount
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
-> internal _validateAddress


### external setTokensReceiver
-> internal _validateAddress


### external setVariationTolerance
-> internal _validateFee


### public vaultRole
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## RedemptionVaultTest

_File: contracts/testers/RedemptionVaultTest.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external calcAndValidateRedeemTest
-> internal _calcAndValidateRedeem


### external convertMTokenToUsdTest
-> internal _convertMTokenToUsd
  -> private _getMTokenRate
    -> internal _getTokenRate


### external convertUsdToTokenTest
-> internal _convertUsdToToken
  -> internal _getTokenRate


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external initializeWithoutInitializer
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem
  -> internal _getTokenRate


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
      -> internal _getTokenRate
  -> internal _convertUsdToToken
    -> internal _getTokenRate
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem
  -> internal _getTokenRate


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setGetTokenRateValue
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setOverrideGetTokenRate
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## RedemptionVaultWIthBUIDL

_File: contracts/RedemptionVaultWithBUIDL.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn
  -> internal _checkAndRedeemBUIDL


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinBuidlBalance
_(no internal calls)_


### external setMinBuidlToRedeem
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## RedemptionVaultWithBUIDLTest

_File: contracts/testers/RedemptionVaultWithBUIDLTest.sol_

### external initialize
_(no internal calls)_


### external setMinBuidlBalance
_(no internal calls)_


### external setMinBuidlToRedeem
_(no internal calls)_


---

## RedemptionVaultWithSwapper

_File: contracts/RedemptionVaultWithSwapper.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn
  -> internal _swapMToken1ToMToken2


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## RedemptionVaultWithSwapperTest

_File: contracts/testers/RedemptionVaultWithSwapperTest.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


---

## RedemptionVaultWithUSTB

_File: contracts/RedemptionVaultWithUSTB.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn
  -> internal _checkAndRedeemUSTB


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## RedemptionVaultWithUSTBTest

_File: contracts/testers/RedemptionVaultWithUSTBTest.sol_

### external checkAndRedeemUSTB
-> internal _checkAndRedeemUSTB


### external initialize
_(no internal calls)_


---

## RsEthChainlinkAdapter

_File: contracts/misc/adapters/RsEthChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp
-> public latestAnswer


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## SLInjCustomAggregatorFeed

_File: contracts/products/sLINJ/SLInjCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## SLInjDataFeed

_File: contracts/products/sLINJ/SLInjDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## SLInjDepositVault

_File: contracts/products/sLINJ/SLInjDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## SLInjRedemptionVaultWithSwapper

_File: contracts/products/sLINJ/SLInjRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## SplUsdCustomAggregatorFeed

_File: contracts/products/splUSD/SplUsdCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## SplUsdDataFeed

_File: contracts/products/splUSD/SplUsdDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## SplUsdDepositVault

_File: contracts/products/splUSD/SplUsdDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## SplUsdRedemptionVaultWithSwapper

_File: contracts/products/splUSD/SplUsdRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## StorkChainlinkAdapter

_File: contracts/misc/adapters/StorkChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
_(no internal calls)_


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## SyrupChainlinkAdapter

_File: contracts/misc/adapters/SyrupChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public latestAnswer
-> public vaultDecimals


### public vaultDecimals
_(no internal calls)_


---

## TACmBTC

_File: contracts/products/mBTC/tac/TACmBTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## TACmBtcDepositVault

_File: contracts/products/mBTC/tac/TACmBtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TACmBtcRedemptionVault

_File: contracts/products/mBTC/tac/TACmBtcRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TACmEDGE

_File: contracts/products/mEDGE/tac/TACmEDGE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## TACmEdgeDepositVault

_File: contracts/products/mEDGE/tac/TACmEdgeDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TACmEdgeRedemptionVault

_File: contracts/products/mEDGE/tac/TACmEdgeRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TACmMEV

_File: contracts/products/mMEV/tac/TACmMEV.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## TACmMevDepositVault

_File: contracts/products/mMEV/tac/TACmMevDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TACmMevRedemptionVault

_File: contracts/products/mMEV/tac/TACmMevRedemptionVault.sol_

### external approveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public greenlistTogglerRole
-> public vaultRole


### external initialize
-> internal __RedemptionVault_init


### external redeemFiatRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external redeemInstant
-> internal _redeemInstant
  -> internal _calcAndValidateRedeem
  -> internal _convertMTokenToUsd
    -> private _getMTokenRate
  -> internal _convertUsdToToken
  -> external_callback mToken.burn


### external redeemRequest
-> internal _redeemRequest
  -> internal _calcAndValidateRedeem


### external rejectRequest
-> internal _validateRequest


### external safeApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### public safeBulkApproveRequest
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external safeBulkApproveRequestAtSavedRate
-> internal _approveRequest
  -> internal _validateRequest
  -> internal _validateLiquidity
  -> external_callback mToken.burn


### external setFiatAdditionalFee
_(no internal calls)_


### external setFiatFlatFee
_(no internal calls)_


### external setMinFiatRedeemAmount
_(no internal calls)_


### external setRequestRedeemer
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TBtcCustomAggregatorFeed

_File: contracts/products/tBTC/TBtcCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## TBtcDataFeed

_File: contracts/products/tBTC/TBtcDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## TBtcDepositVault

_File: contracts/products/tBTC/TBtcDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TBtcRedemptionVaultWithSwapper

_File: contracts/products/tBTC/TBtcRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TEthCustomAggregatorFeed

_File: contracts/products/tETH/TEthCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## TEthDataFeed

_File: contracts/products/tETH/TEthDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## TEthDepositVault

_File: contracts/products/tETH/TEthDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TEthRedemptionVaultWithSwapper

_File: contracts/products/tETH/TEthRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TUsdeCustomAggregatorFeed

_File: contracts/products/tUSDe/TUsdeCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## TUsdeDataFeed

_File: contracts/products/tUSDe/TUsdeDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## TUsdeDepositVault

_File: contracts/products/tUSDe/TUsdeDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TUsdeRedemptionVaultWithSwapper

_File: contracts/products/tUSDe/TUsdeRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TacTonCustomAggregatorFeed

_File: contracts/products/tacTON/TacTonCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## TacTonDataFeed

_File: contracts/products/tacTON/TacTonDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## TacTonDepositVault

_File: contracts/products/tacTON/TacTonDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## TacTonRedemptionVaultWithSwapper

_File: contracts/products/tacTON/TacTonRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## WNlpCustomAggregatorFeed

_File: contracts/products/wNLP/WNlpCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## WNlpDataFeed

_File: contracts/products/wNLP/WNlpDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## WNlpDepositVault

_File: contracts/products/wNLP/WNlpDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## WNlpRedemptionVaultWithSwapper

_File: contracts/products/wNLP/WNlpRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## WVLPCustomAggregatorFeed

_File: contracts/products/wVLP/WVLPCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## WVLPDataFeed

_File: contracts/products/wVLP/WVLPDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## WVLPDepositVault

_File: contracts/products/wVLP/WVLPDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## WVLPRedemptionVaultWithSwapper

_File: contracts/products/wVLP/WVLPRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## WeEurCustomAggregatorFeed

_File: contracts/products/weEUR/WeEurCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## WeEurDataFeed

_File: contracts/products/weEUR/WeEurDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## WeEurDepositVault

_File: contracts/products/weEUR/WeEurDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## WeEurRedemptionVaultWithSwapper

_File: contracts/products/weEUR/WeEurRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## WithMidasAccessControlTester

_File: contracts/testers/WithMidasAccessControlTester.sol_

### external grantRoleTester
_(no internal calls)_


### external initialize
-> internal __WithMidasAccessControl_init


### external initializeWithoutInitializer
-> internal __WithMidasAccessControl_init


### external revokeRoleTester
_(no internal calls)_


### external withOnlyNotRole
_(no internal calls)_


### external withOnlyRole
_(no internal calls)_


---

## WithSanctionsList

_File: contracts/abstract/WithSanctionsList.sol_

### external setSanctionsList
-> internal _onlyRole


---

## WithSanctionsListTester

_File: contracts/testers/WithSanctionsListTester.sol_

### external initialize
-> internal __WithSanctionsList_init
  -> internal __WithSanctionsList_init_unchained


### external initializeUnchainedWithoutInitializer
-> internal __WithSanctionsList_init_unchained


### external initializeWithoutInitializer
-> internal __WithSanctionsList_init
  -> internal __WithSanctionsList_init_unchained


### public onlyNotSanctionedTester
_(no internal calls)_


### public sanctionsListAdminRole
_(no internal calls)_


### external setSanctionsList
-> public sanctionsListAdminRole


---

## WrappedEEthChainlinkAdapter

_File: contracts/misc/adapters/WrappedEEthChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp
-> public latestAnswer


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## WstEthChainlinkAdapter

_File: contracts/misc/adapters/WstEthChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp
-> public latestAnswer


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## YInjChainlinkAdapter

_File: contracts/misc/adapters/YInjChainlinkAdapter.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getAnswer
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external getTimestamp
_(no internal calls)_


### public latestAnswer
_(no internal calls)_


### public latestRound
-> public latestTimestamp


### external latestRoundData
-> public latestTimestamp
-> public latestAnswer


### public latestTimestamp
_(no internal calls)_


### external version
_(no internal calls)_


---

## ZeroGBtcvCustomAggregatorFeed

_File: contracts/products/zeroGBTCV/ZeroGBtcvCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## ZeroGBtcvDataFeed

_File: contracts/products/zeroGBTCV/ZeroGBtcvDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## ZeroGBtcvDepositVault

_File: contracts/products/zeroGBTCV/ZeroGBtcvDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ZeroGBtcvRedemptionVaultWithSwapper

_File: contracts/products/zeroGBTCV/ZeroGBtcvRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ZeroGEthvCustomAggregatorFeed

_File: contracts/products/zeroGETHV/ZeroGEthvCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## ZeroGEthvDataFeed

_File: contracts/products/zeroGETHV/ZeroGEthvDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## ZeroGEthvDepositVault

_File: contracts/products/zeroGETHV/ZeroGEthvDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ZeroGEthvRedemptionVaultWithSwapper

_File: contracts/products/zeroGETHV/ZeroGEthvRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ZeroGUsdvCustomAggregatorFeed

_File: contracts/products/zeroGUSDV/ZeroGUsdvCustomAggregatorFeed.sol_

### public decimals
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public initialize
-> public decimals


### public lastAnswer
_(no internal calls)_


### public lastTimestamp
_(no internal calls)_


### external latestRoundData
-> public getRoundData


### public setRoundData
_(no internal calls)_


### external setRoundDataSafe
-> public lastTimestamp
-> internal _getDeviation
  -> public decimals
-> public lastAnswer
-> public setRoundData


### external version
_(no internal calls)_


---

## ZeroGUsdvDataFeed

_File: contracts/products/zeroGUSDV/ZeroGUsdvDataFeed.sol_

### external changeAggregator
_(no internal calls)_


### public feedAdminRole
_(no internal calls)_


### external getDataInBase18
-> private _getDataInBase18


### external initialize
_(no internal calls)_


### external setHealthyDiff
_(no internal calls)_


### external setMaxExpectedAnswer
_(no internal calls)_


### external setMinExpectedAnswer
_(no internal calls)_


---

## ZeroGUsdvDepositVault

_File: contracts/products/zeroGUSDV/ZeroGUsdvDepositVault.sol_

### external approveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external depositInstant
-> internal _depositInstant
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount
  -> internal _instantTransferTokensToTokensReceiver
  -> external_callback mToken.mint
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply


### external depositRequest
-> private _depositRequest
  -> internal _calcAndValidateDeposit
    -> internal _convertTokenToUsd
    -> internal _convertUsdToMToken
      -> private _getMTokenRate
    -> internal _validateMinAmount


### public greenlistTogglerRole
-> public vaultRole


### public initialize
-> public initializeV1
-> public initializeV2


### public initializeV1
_(no internal calls)_


### public initializeV2
_(no internal calls)_


### external rejectRequest
_(no internal calls)_


### external safeApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### public safeBulkApproveRequest
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external safeBulkApproveRequestAtSavedRate
-> private _approveRequest
  -> internal _validateMaxSupplyCap
    -> external_callback mToken.totalSupply
  -> external_callback mToken.mint


### external setMaxSupplyCap
_(no internal calls)_


### external setMinMTokenAmountForFirstDeposit
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## ZeroGUsdvRedemptionVaultWithSwapper

_File: contracts/products/zeroGUSDV/ZeroGUsdvRedemptionVaultWithSwapper.sol_

### external initialize
_(no internal calls)_


### external setLiquidityProvider
_(no internal calls)_


### external setSwapperVault
_(no internal calls)_


### public vaultRole
_(no internal calls)_


---

## acremBTC1

_File: contracts/products/acremBTC1/acremBTC1.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### public name
-> internal _getNameSymbol


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### public symbol
-> internal _getNameSymbol


### external unpause
_(no internal calls)_


---

## cUSDO

_File: contracts/products/cUSDO/cUSDO.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## dnETH

_File: contracts/products/dnETH/dnETH.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## dnFART

_File: contracts/products/dnFART/dnFART.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## dnHYPE

_File: contracts/products/dnHYPE/dnHYPE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## dnPUMP

_File: contracts/products/dnPUMP/dnPUMP.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## dnTEST

_File: contracts/products/dnTEST/dnTEST.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## eUSD

_File: contracts/products/eUSD/eUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## hbUSDC

_File: contracts/products/hbUSDC/hbUSDC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## hbUSDT

_File: contracts/products/hbUSDT/hbUSDT.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## hbXAUt

_File: contracts/products/hbXAUt/hbXAUt.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## hypeBTC

_File: contracts/products/hypeBTC/hypeBTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## hypeETH

_File: contracts/products/hypeETH/hypeETH.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## hypeUSD

_File: contracts/products/hypeUSD/hypeUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## kitBTC

_File: contracts/products/kitBTC/kitBTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## kitHYPE

_File: contracts/products/kitHYPE/kitHYPE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## kitUSD

_File: contracts/products/kitUSD/kitUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## kmiUSD

_File: contracts/products/kmiUSD/kmiUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## liquidHYPE

_File: contracts/products/liquidHYPE/liquidHYPE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## liquidRESERVE

_File: contracts/products/liquidRESERVE/liquidRESERVE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## lstHYPE

_File: contracts/products/lstHYPE/lstHYPE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mAPOLLO

_File: contracts/products/mAPOLLO/mAPOLLO.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mBASIS

_File: contracts/products/mBASIS/mBASIS.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mBTC

_File: contracts/products/mBTC/mBTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mEDGE

_File: contracts/products/mEDGE/mEDGE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mEVUSD

_File: contracts/products/mEVUSD/mEVUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mFARM

_File: contracts/products/mFARM/mFARM.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mFONE

_File: contracts/products/mFONE/mFONE.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mHYPER

_File: contracts/products/mHYPER/mHYPER.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mHyperBTC

_File: contracts/products/mHyperBTC/mHyperBTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mHyperETH

_File: contracts/products/mHyperETH/mHyperETH.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mKRalpha

_File: contracts/products/mKRalpha/mKRalpha.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mLIQUIDITY

_File: contracts/products/mLIQUIDITY/mLIQUIDITY.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mM1USD

_File: contracts/products/mM1USD/mM1USD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mMEV

_File: contracts/products/mMEV/mMEV.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mPortofino

_File: contracts/products/mPortofino/mPortofino.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mRE7

_File: contracts/products/mRE7/mRE7.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mRE7BTC

_File: contracts/products/mRE7BTC/mRE7BTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mRE7SOL

_File: contracts/products/mRE7SOL/mRE7SOL.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mROX

_File: contracts/products/mROX/mROX.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mSL

_File: contracts/products/mSL/mSL.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mTBILL

_File: contracts/products/mTBILL/mTBILL.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mTU

_File: contracts/products/mTU/mTU.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mToken

_File: contracts/mToken.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal __Blacklistable_init
  -> internal __Blacklistable_init_unchained


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mWildUSD

_File: contracts/products/mWildUSD/mWildUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mXRP

_File: contracts/products/mXRP/mXRP.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## mevBTC

_File: contracts/products/mevBTC/mevBTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## msyrupUSD

_File: contracts/products/msyrupUSD/msyrupUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## msyrupUSDp

_File: contracts/products/msyrupUSDp/msyrupUSDp.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## obeatUSD

_File: contracts/products/obeatUSD/obeatUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## plUSD

_File: contracts/products/plUSD/plUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## sLINJ

_File: contracts/products/sLINJ/sLINJ.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## splUSD

_File: contracts/products/splUSD/splUSD.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## tBTC

_File: contracts/products/tBTC/tBTC.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## tETH

_File: contracts/products/tETH/tETH.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## tUSDe

_File: contracts/products/tUSDe/tUSDe.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## tacTON

_File: contracts/products/tacTON/tacTON.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## wNLP

_File: contracts/products/wNLP/wNLP.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## wVLP

_File: contracts/products/wVLP/wVLP.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## weEUR

_File: contracts/products/weEUR/weEUR.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## zeroGBTCV

_File: contracts/products/zeroGBTCV/zeroGBTCV.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## zeroGETHV

_File: contracts/products/zeroGETHV/zeroGETHV.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## zeroGUSDV

_File: contracts/products/zeroGUSDV/zeroGUSDV.sol_

### external burn
_(no internal calls)_


### external initialize
-> internal _getNameSymbol


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external setMetadata
_(no internal calls)_


### external unpause
_(no internal calls)_

