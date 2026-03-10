# Callpaths — Aegis

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AegisChainlinkOracleV2

_File: AegisChainlinkOracleV2.sol_

### public decimals
_(no internal calls)_


### public lastUpdateTimestamp
_(no internal calls)_


### external price
_(no internal calls)_


### external setOperator
-> internal _setOperator


### external updateYUSDPrice
_(no internal calls)_


### public yusdUSDPrice
_(no internal calls)_


---

## AegisChainlinkOracleV3

_File: AegisChainlinkOracleV3.sol_

### public decimals
_(no internal calls)_


### external description
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### public lastUpdateTimestamp
_(no internal calls)_


### external latestRoundData
_(no internal calls)_


### external setOperator
-> internal _setOperator


### external updateYUSDPrice
_(no internal calls)_


### external version
_(no internal calls)_


### public yusdUSDPrice
_(no internal calls)_


---

## AegisConfig

_File: AegisConfig.sol_

### external disableWhitelist
_(no internal calls)_


### external enableWhitelist
_(no internal calls)_


### public isWhitelisted
_(no internal calls)_


### external setOperator
-> internal _setOperator


### external setTrustedSigner
-> internal _setTrustedSigner


### public supportsInterface
_(no internal calls)_


### external whitelistAddress
_(no internal calls)_


---

## AegisMinting

_File: AegisMinting.sol_

### public addCustodianAddress
-> internal _addCustodianAddress


### public addSupportedAsset
-> internal _addSupportedAsset


### external approveRedeemRequest
-> internal _calculateInsuranceFundFeeFromAmount
-> internal _calculateRedeemMinCollateralAmount
  -> internal _getAssetUSDPriceChainlink
  -> internal _getAssetYUSDPriceOracle
    -> internal _getAssetUSDPriceChainlink
-> internal _rejectRedeemRequest
-> internal _untrackedAvailableAssetBalance


### public assetAegisOracleYUSDPrice
-> internal _getAssetYUSDPriceOracle
  -> internal _getAssetUSDPriceChainlink


### public assetChainlinkUSDPrice
-> internal _getAssetUSDPriceChainlink


### external burnForCrossChain
_(no internal calls)_


### public custodyAvailableAssetBalance
-> internal _custodyAvailableAssetBalance


### external depositIncome
-> public getDomainSeparator
  -> internal _computeDomainSeparator
-> private _deduplicateOrder
  -> public verifyNonce
-> internal _untrackedAvailableAssetBalance
-> internal _calculateMinYUSDAmount
  -> internal _getAssetUSDPriceChainlink
-> internal _calculateInsuranceFundFeeFromAmount


### external forceTransferToCustody
-> internal _custodyAvailableAssetBalance


### external freezeFunds
_(no internal calls)_


### public getDomainSeparator
-> internal _computeDomainSeparator


### public getRedeemRequest
_(no internal calls)_


### public isSupportedAsset
_(no internal calls)_


### external mint
-> internal _checkMintRedeemLimit
-> public getDomainSeparator
  -> internal _computeDomainSeparator
-> private _deduplicateOrder
  -> public verifyNonce
-> internal _calculateMinYUSDAmount
  -> internal _getAssetUSDPriceChainlink
-> internal _calculateInsuranceFundFeeFromAmount


### external mintForCrossChain
_(no internal calls)_


### external rejectRedeemRequest
-> internal _rejectRedeemRequest


### external removeCustodianAddress
_(no internal calls)_


### external removeSupportedAsset
_(no internal calls)_


### external requestRedeem
-> internal _checkMintRedeemLimit
-> public getDomainSeparator
  -> internal _computeDomainSeparator
-> internal _calculateRedeemMinCollateralAmount
  -> internal _getAssetUSDPriceChainlink
  -> internal _getAssetYUSDPriceOracle
    -> internal _getAssetUSDPriceChainlink


### external setAegisConfigAddress
-> internal _setAegisConfigAddress


### external setAegisOracleAddress
-> internal _setAegisOracleAddress


### external setAegisRewardsAddress
-> internal _setAegisRewardsAddress


### external setChainlinkAssetHeartbeat
_(no internal calls)_


### external setCrossChainOperator
-> internal _setCrossChainOperator


### external setCrossChainPaused
_(no internal calls)_


### external setFeedRegistryAddress
-> internal _setFeedRegistryAddress


### external setIncomeFeeBP
_(no internal calls)_


### external setInsuranceFundAddress
-> internal _setInsuranceFundAddress


### external setMintFeeBP
_(no internal calls)_


### external setMintLimits
_(no internal calls)_


### external setMintPaused
_(no internal calls)_


### external setRedeemFeeBP
_(no internal calls)_


### external setRedeemLimits
_(no internal calls)_


### external setRedeemPaused
_(no internal calls)_


### external transferToCustody
-> internal _custodyAvailableAssetBalance


### external unfreezeFunds
_(no internal calls)_


### public untrackedAvailableAssetBalance
-> internal _untrackedAvailableAssetBalance


### public verifyNonce
_(no internal calls)_


### public withdrawRedeemRequest
_(no internal calls)_


---

## AegisMintingJUSD

_File: AegisMintingJUSD.sol_

### public addCustodianAddress
-> internal _addCustodianAddress


### public addSupportedAsset
-> internal _addSupportedAsset


### external approveRedeemRequest
-> internal _calculateInsuranceFundFeeFromAmount
-> internal _calculateRedeemMinCollateralAmount
  -> internal _getAssetUSDPriceChainlink
  -> internal _getAssetJUSDPriceOracle
    -> internal _getAssetUSDPriceChainlink
-> internal _rejectRedeemRequest
-> internal _untrackedAvailableAssetBalance


### public assetAegisOracleJUSDPrice
-> internal _getAssetJUSDPriceOracle
  -> internal _getAssetUSDPriceChainlink


### public assetChainlinkUSDPrice
-> internal _getAssetUSDPriceChainlink


### external burnForCrossChain
_(no internal calls)_


### public custodyAvailableAssetBalance
-> internal _custodyAvailableAssetBalance


### external depositIncome
-> public getDomainSeparator
  -> internal _computeDomainSeparator
-> private _deduplicateOrder
  -> public verifyNonce
-> internal _untrackedAvailableAssetBalance
-> internal _calculateMinJUSDAmount
  -> internal _getAssetUSDPriceChainlink
-> internal _calculateInsuranceFundFeeFromAmount


### external forceTransferToCustody
-> internal _custodyAvailableAssetBalance


### external freezeFunds
_(no internal calls)_


### public getDomainSeparator
-> internal _computeDomainSeparator


### public getRedeemRequest
_(no internal calls)_


### public isSupportedAsset
_(no internal calls)_


### external mint
-> internal _checkMintRedeemLimit
-> public getDomainSeparator
  -> internal _computeDomainSeparator
-> private _deduplicateOrder
  -> public verifyNonce
-> internal _calculateMinJUSDAmount
  -> internal _getAssetUSDPriceChainlink
-> internal _calculateInsuranceFundFeeFromAmount


### external mintForCrossChain
_(no internal calls)_


### external mintPreCollateralized
-> internal _checkPreCollateralizedMintLimit


### external rejectRedeemRequest
-> internal _rejectRedeemRequest


### external removeCustodianAddress
_(no internal calls)_


### external removeSupportedAsset
_(no internal calls)_


### external requestRedeem
-> internal _checkMintRedeemLimit
-> public getDomainSeparator
  -> internal _computeDomainSeparator
-> internal _calculateRedeemMinCollateralAmount
  -> internal _getAssetUSDPriceChainlink
  -> internal _getAssetJUSDPriceOracle
    -> internal _getAssetUSDPriceChainlink


### external setAegisConfigAddress
-> internal _setAegisConfigAddress


### external setAegisOracleAddress
-> internal _setAegisOracleAddress


### external setAegisRewardsAddress
-> internal _setAegisRewardsAddress


### external setChainlinkAssetHeartbeat
_(no internal calls)_


### external setCrossChainOperator
-> internal _setCrossChainOperator


### external setCrossChainPaused
_(no internal calls)_


### external setFeedRegistryAddress
-> internal _setFeedRegistryAddress


### external setIncomeFeeBP
_(no internal calls)_


### external setInsuranceFundAddress
-> internal _setInsuranceFundAddress


### external setMintFeeBP
_(no internal calls)_


### external setMintLimits
_(no internal calls)_


### external setMintPaused
_(no internal calls)_


### external setPreCollateralizedMintLimits
_(no internal calls)_


### external setPreCollateralizedMinter
_(no internal calls)_


### external setRedeemFeeBP
_(no internal calls)_


### external setRedeemLimits
_(no internal calls)_


### external setRedeemPaused
_(no internal calls)_


### external transferToCustody
-> internal _custodyAvailableAssetBalance


### external unfreezeFunds
_(no internal calls)_


### public untrackedAvailableAssetBalance
-> internal _untrackedAvailableAssetBalance


### public verifyNonce
_(no internal calls)_


### public withdrawRedeemRequest
_(no internal calls)_


---

## AegisOracle

_File: AegisOracle.sol_

### public decimals
_(no internal calls)_


### public lastUpdateTimestamp
_(no internal calls)_


### external setOperator
-> internal _setOperator


### external updateYUSDPrice
_(no internal calls)_


### public yusdUSDPrice
_(no internal calls)_


---

## AegisOracleJUSD

_File: AegisOracleJUSD.sol_

### public decimals
_(no internal calls)_


### public jusdUSDPrice
_(no internal calls)_


### public lastUpdateTimestamp
_(no internal calls)_


### external setOperator
-> internal _setOperator


### external updateJUSDPrice
_(no internal calls)_


---

## AegisRewards

_File: AegisRewards.sol_

### external claimRewards
-> public getDomainSeparator
  -> internal _computeDomainSeparator


### external depositRewards
-> private _stringToBytes32


### external finalizeRewards
_(no internal calls)_


### public getDomainSeparator
-> internal _computeDomainSeparator


### public rewardById
-> private _stringToBytes32


### external setAegisConfigAddress
-> internal _setAegisConfigAddress


### external setAegisMintingAddress
_(no internal calls)_


### external withdrawExpiredRewards
_(no internal calls)_


---

## AegisRewardsManual

_File: AegisRewardsManual.sol_

### public availableBalanceForDeposits
_(no internal calls)_


### external claimRewards
-> public getDomainSeparator
  -> internal _computeDomainSeparator


### external depositRewards
-> private _stringToBytes32


### external finalizeRewards
_(no internal calls)_


### public getDomainSeparator
-> internal _computeDomainSeparator


### external rescueAssets
-> library SafeERC20.safeTransfer


### public rewardById
-> private _stringToBytes32


### external setAegisConfigAddress
-> internal _setAegisConfigAddress


### public totalReservedRewards
_(no internal calls)_


### external withdrawExpiredRewards
_(no internal calls)_


---

## JUSD

_File: JUSD.sol_

### public addBlackList
_(no internal calls)_


### external getBlackListStatus
_(no internal calls)_


### external mint
_(no internal calls)_


### public removeBlackList
_(no internal calls)_


### external setMinter
_(no internal calls)_


---

## JUSDMintBurnOFTAdapter

_File: JUSDMintBurnOFTAdapter.sol_

### external claimEscrow
_(no internal calls)_


### public decimals
_(no internal calls)_


### public getAegisMinting
_(no internal calls)_


### public jusdToken
_(no internal calls)_


### public localDecimals
_(no internal calls)_


---

## JUSDOFT

_File: JUSDOFT.sol_

### public addBlackList
_(no internal calls)_


### external getBlackListStatus
_(no internal calls)_


### public removeBlackList
_(no internal calls)_


---

## YUSD

_File: YUSD.sol_

### public addBlackList
_(no internal calls)_


### external getBlackListStatus
_(no internal calls)_


### external mint
_(no internal calls)_


### public removeBlackList
_(no internal calls)_


### external setMinter
_(no internal calls)_


---

## YUSDMintBurnOFTAdapter

_File: YUSDMintBurnOFTAdapter.sol_

### public decimals
_(no internal calls)_


### public getAegisMinting
_(no internal calls)_


### public localDecimals
_(no internal calls)_


### public yusdToken
_(no internal calls)_


---

## YUSDOFT

_File: YUSDOFT.sol_

### public addBlackList
_(no internal calls)_


### external getBlackListStatus
_(no internal calls)_


### public removeBlackList
_(no internal calls)_


---

## sJUSD

_File: sJUSD.sol_

### external cooldownAssets
_(no internal calls)_


### external cooldownShares
_(no internal calls)_


### public decimals
_(no internal calls)_


### external getUserCooldownStatus
_(no internal calls)_


### public initialize
_(no internal calls)_


### external initializeV2
_(no internal calls)_


### public redeem
-> internal _instantUnstakeShares


### external rescueTokens
_(no internal calls)_


### external setCooldownDuration
-> internal _setCooldownDuration


### external setInstantUnstakingFee
_(no internal calls)_


### external setInsuranceFund
_(no internal calls)_


### external unstake
_(no internal calls)_


### public withdraw
-> internal _instantUnstakeAssets


---

## sJUSDSilo

_File: sJUSDSilo.sol_

### external getJUSD
_(no internal calls)_


### external getStakingVault
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## sYUSD

_File: sYUSD.sol_

### external cooldownAssets
_(no internal calls)_


### external cooldownShares
_(no internal calls)_


### public decimals
_(no internal calls)_


### external getUserCooldownStatus
_(no internal calls)_


### public initialize
_(no internal calls)_


### external initializeV2
_(no internal calls)_


### public redeem
-> internal _instantUnstakeShares


### external rescueTokens
_(no internal calls)_


### external setCooldownDuration
-> internal _setCooldownDuration


### external setInstantUnstakingFee
_(no internal calls)_


### external setInsuranceFund
_(no internal calls)_


### external unstake
_(no internal calls)_


### public withdraw
-> internal _instantUnstakeAssets


---

## sYUSDSilo

_File: sYUSDSilo.sol_

### external getStakingVault
_(no internal calls)_


### external getYUSD
_(no internal calls)_


### external withdraw
_(no internal calls)_

