# Callpaths — Aave_V3

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ACLManager

_File: src/contracts/protocol/configuration/ACLManager.sol_

### external addAssetListingAdmin
-> public grantRole
  -> private _grantRole
    -> public hasRole


### external addBridge
-> public grantRole
  -> private _grantRole
    -> public hasRole


### external addEmergencyAdmin
-> public grantRole
  -> private _grantRole
    -> public hasRole


### external addFlashBorrower
-> public grantRole
  -> private _grantRole
    -> public hasRole


### external addPoolAdmin
-> public grantRole
  -> private _grantRole
    -> public hasRole


### external addRiskAdmin
-> public grantRole
  -> private _grantRole
    -> public hasRole


### public getRoleAdmin
_(no internal calls)_


### public grantRole
-> private _grantRole
  -> public hasRole


### public hasRole
_(no internal calls)_


### external isAssetListingAdmin
-> public hasRole


### external isBridge
-> public hasRole


### external isEmergencyAdmin
-> public hasRole


### external isFlashBorrower
-> public hasRole


### external isPoolAdmin
-> public hasRole


### external isRiskAdmin
-> public hasRole


### external removeAssetListingAdmin
-> public revokeRole
  -> private _revokeRole
    -> public hasRole


### external removeBridge
-> public revokeRole
  -> private _revokeRole
    -> public hasRole


### external removeEmergencyAdmin
-> public revokeRole
  -> private _revokeRole
    -> public hasRole


### external removeFlashBorrower
-> public revokeRole
  -> private _revokeRole
    -> public hasRole


### external removePoolAdmin
-> public revokeRole
  -> private _revokeRole
    -> public hasRole


### external removeRiskAdmin
-> public revokeRole
  -> private _revokeRole
    -> public hasRole


### public renounceRole
-> private _revokeRole
  -> public hasRole


### public revokeRole
-> private _revokeRole
  -> public hasRole


### external setRoleAdmin
-> internal _setRoleAdmin
  -> public getRoleAdmin


### public supportsInterface
_(no internal calls)_


---

## AToken

_File: src/contracts/protocol/tokenization/AToken.sol_

### public DOMAIN_SEPARATOR
_(no internal calls)_


### external RESERVE_TREASURY_ADDRESS
_(no internal calls)_


### external UNDERLYING_ASSET_ADDRESS
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external burn
-> internal _burnScaled
  -> library Errors.InvalidBurnAmount


### external getPreviousIndex
_(no internal calls)_


### external getScaledUserBalanceAndSupply
_(no internal calls)_


### external mint
-> internal _mintScaled
  -> library Errors.InvalidMintAmount


### external mintToTreasury
-> internal _mintScaled
  -> library Errors.InvalidMintAmount


### public nonces
_(no internal calls)_


### external permit
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> public DOMAIN_SEPARATOR
-> library Errors.InvalidSignature


### external rescueTokens
-> library Errors.UnderlyingCannotBeRescued


### external scaledBalanceOf
_(no internal calls)_


### public scaledTotalSupply
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### external transferFrom
-> internal _transfer


### external transferOnLiquidation
-> internal _transfer


### external transferUnderlyingTo
_(no internal calls)_


---

## ATokenInstance

_File: src/contracts/instances/ATokenInstance.sol_

### public DOMAIN_SEPARATOR
_(no internal calls)_


### external RESERVE_TREASURY_ADDRESS
_(no internal calls)_


### external UNDERLYING_ASSET_ADDRESS
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external burn
_(no internal calls)_


### public initialize
-> library Errors.PoolAddressesDoNotMatch


### external mint
_(no internal calls)_


### external mintToTreasury
_(no internal calls)_


### public nonces
_(no internal calls)_


### external permit
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> public DOMAIN_SEPARATOR
-> library Errors.InvalidSignature


### external rescueTokens
-> library Errors.UnderlyingCannotBeRescued


### public totalSupply
_(no internal calls)_


### external transferFrom
-> internal _transfer


### external transferOnLiquidation
-> internal _transfer


### external transferUnderlyingTo
_(no internal calls)_


---

## ATokenWithDelegation

_File: src/contracts/protocol/tokenization/ATokenWithDelegation.sol_

### public DOMAIN_SEPARATOR
_(no internal calls)_


### external RESERVE_TREASURY_ADDRESS
_(no internal calls)_


### external UNDERLYING_ASSET_ADDRESS
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external burn
_(no internal calls)_


### external delegate
-> internal _delegateByType
  -> internal _getDelegationState
  -> internal _getDelegateeByType
  -> internal _getBalance
  -> internal _governancePowerTransferByType
    -> library SafeCast.toUint72
    -> internal _getDelegationState
    -> internal _setDelegationState
  -> internal _updateDelegateeByType
  -> internal _setDelegationState
  -> internal _updateDelegationModeByType


### external delegateByType
-> internal _delegateByType
  -> internal _getDelegationState
  -> internal _getDelegateeByType
  -> internal _getBalance
  -> internal _governancePowerTransferByType
    -> library SafeCast.toUint72
    -> internal _getDelegationState
    -> internal _setDelegationState
  -> internal _updateDelegateeByType
  -> internal _setDelegationState
  -> internal _updateDelegationModeByType


### external getDelegateeByType
-> internal _getDelegateeByType
-> internal _getDelegationState


### external getDelegates
-> internal _getDelegationState
-> internal _getDelegateeByType


### public getPowerCurrent
-> internal _getDelegationState
-> internal _getBalance
-> internal _getDelegatedPowerByType


### external getPowersCurrent
-> public getPowerCurrent
  -> internal _getDelegationState
  -> internal _getBalance
  -> internal _getDelegatedPowerByType


### external metaDelegate
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> internal _getDomainSeparator
  -> public DOMAIN_SEPARATOR
-> internal _incrementNonces
-> library Errors.InvalidSignature
-> internal _delegateByType
  -> internal _getDelegationState
  -> internal _getDelegateeByType
  -> internal _getBalance
  -> internal _governancePowerTransferByType
    -> library SafeCast.toUint72
    -> internal _getDelegationState
    -> internal _setDelegationState
  -> internal _updateDelegateeByType
  -> internal _setDelegationState
  -> internal _updateDelegationModeByType


### external metaDelegateByType
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> internal _getDomainSeparator
  -> public DOMAIN_SEPARATOR
-> internal _incrementNonces
-> library Errors.InvalidSignature
-> internal _delegateByType
  -> internal _getDelegationState
  -> internal _getDelegateeByType
  -> internal _getBalance
  -> internal _governancePowerTransferByType
    -> library SafeCast.toUint72
    -> internal _getDelegationState
    -> internal _setDelegationState
  -> internal _updateDelegateeByType
  -> internal _setDelegationState
  -> internal _updateDelegationModeByType


### external mint
_(no internal calls)_


### external mintToTreasury
_(no internal calls)_


### public nonces
_(no internal calls)_


### external permit
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> public DOMAIN_SEPARATOR
-> library Errors.InvalidSignature


### external rescueTokens
-> library Errors.UnderlyingCannotBeRescued


### public totalSupply
_(no internal calls)_


### external transferFrom
-> internal _transfer
  -> internal _delegationChangeOnTransfer
    -> internal _getDelegationState
    -> internal _governancePowerTransferByType
      -> library SafeCast.toUint72
      -> internal _getDelegationState
      -> internal _setDelegationState
    -> internal _getDelegateeByType


### external transferOnLiquidation
-> internal _transfer
  -> internal _delegationChangeOnTransfer
    -> internal _getDelegationState
    -> internal _governancePowerTransferByType
      -> library SafeCast.toUint72
      -> internal _getDelegationState
      -> internal _setDelegationState
    -> internal _getDelegateeByType


### external transferUnderlyingTo
_(no internal calls)_


---

## ATokenWithDelegationInstance

_File: src/contracts/instances/ATokenWithDelegationInstance.sol_

### public initialize
-> library Errors.PoolAddressesDoNotMatch


---

## AaveOracle

_File: src/contracts/misc/AaveOracle.sol_

### public getAssetPrice
_(no internal calls)_


### external getAssetsPrices
-> public getAssetPrice


### external getFallbackOracle
_(no internal calls)_


### external getSourceOfAsset
_(no internal calls)_


### external setAssetSources
-> internal _setAssetsSources
  -> library Errors.InconsistentParamsLength


### external setFallbackOracle
-> internal _setFallbackOracle


---

## AaveProtocolDataProvider

_File: src/contracts/helpers/AaveProtocolDataProvider.sol_

### external getATokenTotalSupply
_(no internal calls)_


### external getAllATokens
_(no internal calls)_


### external getAllReservesTokens
_(no internal calls)_


### external getDebtCeiling
_(no internal calls)_


### external getDebtCeilingDecimals
_(no internal calls)_


### external getFlashLoanEnabled
_(no internal calls)_


### external getInterestRateStrategyAddress
_(no internal calls)_


### external getIsVirtualAccActive
_(no internal calls)_


### external getLiquidationProtocolFee
_(no internal calls)_


### external getPaused
_(no internal calls)_


### external getReserveCaps
_(no internal calls)_


### external getReserveConfigurationData
_(no internal calls)_


### external getReserveData
_(no internal calls)_


### external getReserveDeficit
_(no internal calls)_


### external getReserveTokensAddresses
_(no internal calls)_


### external getSiloedBorrowing
_(no internal calls)_


### external getTotalDebt
_(no internal calls)_


### external getUnbackedMintCap
_(no internal calls)_


### external getUserReserveData
_(no internal calls)_


### external getVirtualUnderlyingBalance
_(no internal calls)_


---

## AaveV3ConfigEngine

_File: src/contracts/extensions/v3-config-engine/AaveV3ConfigEngine.sol_

### external createEModeCategories
-> internal _getEngineConstants


### external listAssets
-> public listAssetsCustom
  -> internal _getEngineConstants
  -> internal _getEngineLibraries


### public listAssetsCustom
-> internal _getEngineConstants
-> internal _getEngineLibraries


### external updateAssetsEMode
-> internal _getEngineConstants


### external updateBorrowSide
-> internal _getEngineConstants


### external updateCaps
-> internal _getEngineConstants


### external updateCollateralSide
-> internal _getEngineConstants


### external updateEModeCategories
-> internal _getEngineConstants


### external updatePriceFeeds
-> internal _getEngineConstants


### external updateRateStrategies
-> internal _getEngineConstants


---

## AaveV3GettersBatchOne

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3GettersBatchOne.sol_

### external getGettersReportOne
_(no internal calls)_


---

## AaveV3GettersBatchTwo

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3GettersBatchTwo.sol_

### external getGettersReportTwo
_(no internal calls)_


---

## AaveV3HelpersBatchOne

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3HelpersBatchOne.sol_

### external getConfigEngineReport
_(no internal calls)_


---

## AaveV3HelpersBatchTwo

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3HelpersBatchTwo.sol_

### external staticATokenReport
_(no internal calls)_


---

## AaveV3L2PoolBatch

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3L2PoolBatch.sol_

### external getPoolReport
_(no internal calls)_


---

## AaveV3LibrariesBatch1

_File: src/deployments/projects/aave-v3-libraries/AaveV3LibrariesBatch1.sol_

### public getLibrariesReport
_(no internal calls)_


---

## AaveV3LibrariesBatch2

_File: src/deployments/projects/aave-v3-libraries/AaveV3LibrariesBatch2.sol_

### public getLibrariesReport
_(no internal calls)_


---

## AaveV3MiscBatch

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3MiscBatch.sol_

### external getMiscReport
_(no internal calls)_


---

## AaveV3Payload

_File: src/contracts/extensions/v3-config-engine/AaveV3Payload.sol_

### public assetsEModeUpdates
_(no internal calls)_


### public borrowsUpdates
_(no internal calls)_


### public capsUpdates
_(no internal calls)_


### public collateralsUpdates
_(no internal calls)_


### public eModeCategoriesUpdates
_(no internal calls)_


### public eModeCategoryCreations
_(no internal calls)_


### external execute
-> internal _preExecute
-> public newListings
-> public newListingsCustom
-> public eModeCategoriesUpdates
-> public assetsEModeUpdates
-> public eModeCategoryCreations
-> public collateralsUpdates
-> public borrowsUpdates
-> public rateStrategiesUpdates
-> public priceFeedsUpdates
-> public capsUpdates
-> internal _postExecute


### public newListings
_(no internal calls)_


### public newListingsCustom
_(no internal calls)_


### public priceFeedsUpdates
_(no internal calls)_


### public rateStrategiesUpdates
_(no internal calls)_


---

## AaveV3PeripheryBatch

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3PeripheryBatch.sol_

### external getPeripheryReport
_(no internal calls)_


---

## AaveV3PoolBatch

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3PoolBatch.sol_

### external getPoolReport
_(no internal calls)_


---

## AaveV3SetupBatch

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3SetupBatch.sol_

### external getInitialReport
_(no internal calls)_


### external getSetupReport
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setMarketReport
_(no internal calls)_


### external setProtocolDataProvider
-> internal _setProtocolDataProvider


### external setupAaveV3Market
-> internal _setupAaveV3Market
  -> internal _validateMarketSetup
  -> internal _setupPoolAddressesProvider
  -> internal _setupACL
    -> internal _configureFlashloanParams


### external transferMarketOwnership
-> internal _transferMarketOwnership


### public transferOwnership
_(no internal calls)_


---

## AaveV3TokensBatch

_File: src/deployments/projects/aave-v3-batched/batches/AaveV3TokensBatch.sol_

### external getTokensReport
_(no internal calls)_


---

## AccessControl

_File: src/contracts/dependencies/openzeppelin/contracts/AccessControl.sol_

### public getRoleAdmin
_(no internal calls)_


### public grantRole
-> private _grantRole
  -> public hasRole
  -> internal _msgSender


### public hasRole
_(no internal calls)_


### public renounceRole
-> internal _msgSender
-> private _revokeRole
  -> public hasRole
  -> internal _msgSender


### public revokeRole
-> private _revokeRole
  -> public hasRole
  -> internal _msgSender


### public supportsInterface
_(no internal calls)_


---

## AdminUpgradeabilityProxy

_File: src/contracts/dependencies/openzeppelin/upgradeability/AdminUpgradeabilityProxy.sol_

### external admin
-> internal _admin


### external changeAdmin
-> internal _admin
-> internal _setAdmin


### external implementation
_(no internal calls)_


### external upgradeTo
_(no internal calls)_


### external upgradeToAndCall
_(no internal calls)_


---

## BaseAdminUpgradeabilityProxy

_File: src/contracts/dependencies/openzeppelin/upgradeability/BaseAdminUpgradeabilityProxy.sol_

### external admin
-> internal _admin


### external changeAdmin
-> internal _admin
-> internal _setAdmin


### external implementation
-> internal _implementation


### external upgradeTo
-> internal _upgradeTo
  -> internal _setImplementation
    -> library Address.isContract


### external upgradeToAndCall
-> internal _upgradeTo
  -> internal _setImplementation
    -> library Address.isContract


---

## BaseDelegation

_File: src/contracts/protocol/tokenization/delegation/BaseDelegation.sol_

### external delegate
-> internal _delegateByType
  -> internal _getDelegateeByType
  -> internal _governancePowerTransferByType
  -> internal _updateDelegateeByType
  -> internal _updateDelegationModeByType


### external delegateByType
-> internal _delegateByType
  -> internal _getDelegateeByType
  -> internal _governancePowerTransferByType
  -> internal _updateDelegateeByType
  -> internal _updateDelegationModeByType


### external getDelegateeByType
-> internal _getDelegateeByType


### external getDelegates
-> internal _getDelegateeByType


### public getPowerCurrent
-> internal _getDelegatedPowerByType


### external getPowersCurrent
-> public getPowerCurrent
  -> internal _getDelegatedPowerByType


### external metaDelegate
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> library Errors.InvalidSignature
-> internal _delegateByType
  -> internal _getDelegateeByType
  -> internal _governancePowerTransferByType
  -> internal _updateDelegateeByType
  -> internal _updateDelegationModeByType


### external metaDelegateByType
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> library Errors.InvalidSignature
-> internal _delegateByType
  -> internal _getDelegateeByType
  -> internal _governancePowerTransferByType
  -> internal _updateDelegateeByType
  -> internal _updateDelegationModeByType


---

## BaseImmutableAdminUpgradeabilityProxy

_File: src/contracts/misc/aave-upgradeability/BaseImmutableAdminUpgradeabilityProxy.sol_

### external admin
_(no internal calls)_


### external implementation
-> internal _implementation


### external upgradeTo
-> internal _upgradeTo
  -> internal _setImplementation
    -> library Address.isContract


### external upgradeToAndCall
-> internal _upgradeTo
  -> internal _setImplementation
    -> library Address.isContract


---

## Collector

_File: src/contracts/treasury/Collector.sol_

### external approve
_(no internal calls)_


### public balanceOf
-> public deltaOf


### external cancelStream
-> public balanceOf
  -> public deltaOf


### external createStream
_(no internal calls)_


### public deltaOf
_(no internal calls)_


### external getNextStreamId
_(no internal calls)_


### external getStream
_(no internal calls)_


### external initialize
_(no internal calls)_


### external isFundsAdmin
_(no internal calls)_


### external transfer
_(no internal calls)_


### external withdrawFromStream
-> public balanceOf
  -> public deltaOf


---

## DebtTokenBase

_File: src/contracts/protocol/tokenization/base/DebtTokenBase.sol_

### public DOMAIN_SEPARATOR
-> internal _calculateDomainSeparator


### external approveDelegation
-> internal _approveDelegation
-> internal _msgSender


### external borrowAllowance
_(no internal calls)_


### external delegationWithSig
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> public DOMAIN_SEPARATOR
  -> internal _calculateDomainSeparator
-> library Errors.InvalidSignature
-> internal _approveDelegation


### public nonces
_(no internal calls)_


### external renounceDelegation
-> internal _approveDelegation
-> internal _msgSender


---

## DefaultReserveInterestRateStrategyV2

_File: src/contracts/misc/DefaultReserveInterestRateStrategyV2.sol_

### external calculateInterestRates
-> internal _rayifyRateData
  -> internal _bpsToRay


### external getBaseVariableBorrowRate
-> internal _bpsToRay


### external getInterestRateData
-> internal _rayifyRateData
  -> internal _bpsToRay


### external getInterestRateDataBps
_(no internal calls)_


### external getMaxVariableBorrowRate
-> internal _bpsToRay


### external getOptimalUsageRatio
-> internal _bpsToRay


### external getVariableRateSlope1
-> internal _bpsToRay


### external getVariableRateSlope2
-> internal _bpsToRay


### external setInterestRateParams
-> internal _setInterestRateParams
  -> library Errors.ZeroAddressNotValid
  -> library Errors.InvalidOptimalUsageRatio
  -> library Errors.Slope2MustBeGteSlope1
  -> library Errors.InvalidMaxRate


---

## DeployUtils

_File: src/deployments/contracts/utilities/DeployUtils.sol_

### public getCreate2Address
_(no internal calls)_


---

## EIP712Base

_File: src/contracts/protocol/tokenization/base/EIP712Base.sol_

### public DOMAIN_SEPARATOR
-> internal _calculateDomainSeparator


### public nonces
_(no internal calls)_


---

## ERC165

_File: src/contracts/dependencies/openzeppelin/contracts/ERC165.sol_

### public supportsInterface
_(no internal calls)_


---

## ERC20AaveLMUpgradeable

_File: src/contracts/extensions/stata-token/ERC20AaveLMUpgradeable.sol_

### external claimRewards
-> internal _claimRewardsOnBehalf
  -> public getCurrentRewardsIndex
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.getAssetIndex
  -> internal _getClaimableRewards
    -> private _getERC20AaveLMStorage
    -> internal _getPendingRewards
  -> public collectAndUpdateRewards
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.claimRewards
  -> private _getERC20AaveLMStorage


### external claimRewardsOnBehalf
-> external_callback INCENTIVES_CONTROLLER.getClaimer
-> internal _claimRewardsOnBehalf
  -> public getCurrentRewardsIndex
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.getAssetIndex
  -> internal _getClaimableRewards
    -> private _getERC20AaveLMStorage
    -> internal _getPendingRewards
  -> public collectAndUpdateRewards
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.claimRewards
      -> internal _claimRewardsOnBehalf
  -> private _getERC20AaveLMStorage


### external claimRewardsToSelf
-> internal _claimRewardsOnBehalf
  -> public getCurrentRewardsIndex
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.getAssetIndex
  -> internal _getClaimableRewards
    -> private _getERC20AaveLMStorage
    -> internal _getPendingRewards
  -> public collectAndUpdateRewards
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.claimRewards
      -> internal _claimRewardsOnBehalf
  -> private _getERC20AaveLMStorage


### public collectAndUpdateRewards
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.claimRewards
  -> internal _claimRewardsOnBehalf
    -> public getCurrentRewardsIndex
      -> private _getERC20AaveLMStorage
      -> external_callback INCENTIVES_CONTROLLER.getAssetIndex
    -> internal _getClaimableRewards
      -> private _getERC20AaveLMStorage
      -> internal _getPendingRewards
    -> public collectAndUpdateRewards
    -> private _getERC20AaveLMStorage


### external getClaimableRewards
-> internal _getClaimableRewards
  -> private _getERC20AaveLMStorage
  -> internal _getPendingRewards
-> public getCurrentRewardsIndex
  -> private _getERC20AaveLMStorage
  -> external_callback INCENTIVES_CONTROLLER.getAssetIndex


### public getCurrentRewardsIndex
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.getAssetIndex


### external getReferenceAsset
-> private _getERC20AaveLMStorage


### external getTotalClaimableRewards
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.getUserRewards


### external getUnclaimedRewards
-> private _getERC20AaveLMStorage


### public isRegisteredRewardToken
-> private _getERC20AaveLMStorage


### public refreshRewardTokens
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.getRewardsByAsset
-> internal _registerRewardToken
  -> public isRegisteredRewardToken
    -> private _getERC20AaveLMStorage
  -> public getCurrentRewardsIndex
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.getAssetIndex
  -> private _getERC20AaveLMStorage


### external rewardTokens
-> private _getERC20AaveLMStorage


---

## ERC4626StataTokenUpgradeable

_File: src/contracts/extensions/stata-token/ERC4626StataTokenUpgradeable.sol_

### public aToken
-> private _getERC4626StataTokenStorage


### external depositATokens
-> public aToken
  -> private _getERC4626StataTokenStorage
-> internal _deposit
  -> internal _deposit


### external depositWithPermit
-> public aToken
  -> private _getERC4626StataTokenStorage
-> internal _deposit
  -> internal _deposit


### external latestAnswer
-> internal _rate


### public maxDeposit
-> library ReserveConfiguration.getActive
-> library ReserveConfiguration.getPaused
-> library ReserveConfiguration.getFrozen
-> library ReserveConfiguration.getSupplyCap
-> library ReserveConfiguration.getDecimals
-> internal _rate


### public maxMint
-> public maxDeposit
  -> library ReserveConfiguration.getActive
  -> library ReserveConfiguration.getPaused
  -> library ReserveConfiguration.getFrozen
  -> library ReserveConfiguration.getSupplyCap
  -> library ReserveConfiguration.getDecimals
  -> internal _rate


### public maxRedeem
-> library ReserveConfiguration.getActive
-> library ReserveConfiguration.getPaused


### public maxWithdraw
-> public maxRedeem
  -> library ReserveConfiguration.getActive
  -> library ReserveConfiguration.getPaused


### external redeemATokens
-> internal _withdraw
  -> internal _withdraw


### public totalAssets
-> internal _convertToAssets
  -> internal _rate


---

## EmissionManager

_File: src/contracts/rewards/EmissionManager.sol_

### external configureAssets
_(no internal calls)_


### external getEmissionAdmin
_(no internal calls)_


### external getRewardsController
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setClaimer
_(no internal calls)_


### external setDistributionEnd
_(no internal calls)_


### external setEmissionAdmin
_(no internal calls)_


### external setEmissionPerSecond
_(no internal calls)_


### external setRewardOracle
_(no internal calls)_


### external setRewardsController
_(no internal calls)_


### external setTransferStrategy
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## IncentivizedERC20

_File: src/contracts/protocol/tokenization/base/IncentivizedERC20.sol_

### external allowance
_(no internal calls)_


### external approve
-> internal _approve
-> internal _msgSender


### public balanceOf
_(no internal calls)_


### external decimals
_(no internal calls)_


### external decreaseAllowance
-> internal _msgSender
-> internal _approve


### external getIncentivesController
_(no internal calls)_


### external increaseAllowance
-> internal _approve
-> internal _msgSender


### public name
_(no internal calls)_


### external renounceAllowance
-> internal _approve
-> internal _msgSender


### external symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### external transfer
-> internal _transfer
-> internal _msgSender


### external transferFrom
-> internal _spendAllowance
  -> internal _approve
-> internal _msgSender
-> internal _transfer


---

## InitializableAdminUpgradeabilityProxy

_File: src/contracts/dependencies/openzeppelin/upgradeability/InitializableAdminUpgradeabilityProxy.sol_

### external admin
-> internal _admin


### external changeAdmin
-> internal _admin
-> internal _setAdmin


### external implementation
_(no internal calls)_


### public initialize
-> external_callback InitializableUpgradeabilityProxy.initialize
-> internal _setAdmin


### external upgradeTo
_(no internal calls)_


### external upgradeToAndCall
_(no internal calls)_


---

## InitializableImmutableAdminUpgradeabilityProxy

_File: src/contracts/misc/aave-upgradeability/InitializableImmutableAdminUpgradeabilityProxy.sol_

### external admin
_(no internal calls)_


### external implementation
_(no internal calls)_


### public initialize
_(no internal calls)_


### external upgradeTo
_(no internal calls)_


### external upgradeToAndCall
_(no internal calls)_


---

## InitializableUpgradeabilityProxy

_File: src/contracts/dependencies/openzeppelin/upgradeability/InitializableUpgradeabilityProxy.sol_

### public initialize
-> internal _implementation
-> internal _setImplementation
  -> library Address.isContract


---

## L2Encoder

_File: src/contracts/helpers/L2Encoder.sol_

### external encodeBorrowParams
_(no internal calls)_


### external encodeLiquidationCall
_(no internal calls)_


### public encodeRepayParams
_(no internal calls)_


### external encodeRepayWithATokensParams
-> public encodeRepayParams


### external encodeRepayWithPermitParams
_(no internal calls)_


### external encodeSetUserUseReserveAsCollateral
_(no internal calls)_


### external encodeSupplyParams
_(no internal calls)_


### external encodeSupplyWithPermitParams
_(no internal calls)_


### external encodeWithdrawParams
_(no internal calls)_


---

## L2Pool

_File: src/contracts/protocol/pool/L2Pool.sol_

### public FLASHLOAN_PREMIUM_TOTAL
_(no internal calls)_


### public FLASHLOAN_PREMIUM_TO_PROTOCOL
_(no internal calls)_


### public MAX_NUMBER_RESERVES
_(no internal calls)_


### external approvePositionManager
_(no internal calls)_


### external borrow
-> external borrow


### external configureEModeCategory
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryBorrowableBitmap
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryCollateralBitmap
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryLtvzeroBitmap
-> library Errors.EModeCategoryReserved


### external deposit
-> library SupplyLogic.executeSupply
-> library DataTypes.ExecuteSupplyParams


### external dropReserve
-> library PoolLogic.executeDropReserve


### external eliminateReserveDeficit
-> library LiquidationLogic.executeEliminateDeficit
-> library DataTypes.ExecuteEliminateDeficitParams


### external finalizeTransfer
-> library Errors.CallerNotAToken
-> library SupplyLogic.executeFinalizeTransfer
-> library DataTypes.FinalizeTransferParams


### public flashLoan
-> library DataTypes.FlashloanParams
-> library FlashLoanLogic.executeFlashLoan


### public flashLoanSimple
-> library DataTypes.FlashloanSimpleParams
-> library FlashLoanLogic.executeFlashLoanSimple


### external getBorrowLogic
_(no internal calls)_


### external getConfiguration
_(no internal calls)_


### external getEModeCategoryBorrowableBitmap
_(no internal calls)_


### external getEModeCategoryCollateralBitmap
_(no internal calls)_


### external getEModeCategoryCollateralConfig
_(no internal calls)_


### external getEModeCategoryData
-> library DataTypes.EModeCategoryLegacy


### external getEModeCategoryLabel
_(no internal calls)_


### external getEModeCategoryLtvzeroBitmap
_(no internal calls)_


### external getFlashLoanLogic
_(no internal calls)_


### external getLiquidationGracePeriod
_(no internal calls)_


### external getLiquidationLogic
_(no internal calls)_


### external getPoolLogic
_(no internal calls)_


### external getReserveAToken
_(no internal calls)_


### external getReserveAddressById
_(no internal calls)_


### external getReserveData
_(no internal calls)_


### external getReserveDeficit
_(no internal calls)_


### external getReserveNormalizedIncome
_(no internal calls)_


### external getReserveNormalizedVariableDebt
_(no internal calls)_


### external getReserveVariableDebtToken
_(no internal calls)_


### external getReservesCount
_(no internal calls)_


### external getReservesList
_(no internal calls)_


### external getSupplyLogic
_(no internal calls)_


### external getUserAccountData
-> library PoolLogic.executeGetUserAccountData
-> library DataTypes.CalculateUserAccountDataParams


### external getUserConfiguration
_(no internal calls)_


### external getUserEMode
_(no internal calls)_


### external getVirtualUnderlyingBalance
_(no internal calls)_


### external initReserve
-> library PoolLogic.executeInitReserve
-> library DataTypes.InitReserveParams
-> public MAX_NUMBER_RESERVES


### external isApprovedPositionManager
_(no internal calls)_


### external liquidationCall
-> library CalldataLogic.decodeLiquidationCallParams
-> external liquidationCall


### external mintToTreasury
-> library PoolLogic.executeMintToTreasury


### external renouncePositionManagerRole
_(no internal calls)_


### external repay
-> library CalldataLogic.decodeRepayParams
-> external repay


### external repayWithATokens
-> library CalldataLogic.decodeRepayParams
-> external repayWithATokens


### external repayWithPermit
-> library CalldataLogic.decodeRepayWithPermitParams
-> external repayWithPermit


### external rescueTokens
-> library PoolLogic.executeRescueTokens


### external resetIsolationModeTotalDebt
-> library PoolLogic.executeResetIsolationModeTotalDebt


### external setConfiguration
-> library Errors.ZeroAddressNotValid
-> library Errors.AssetNotListed


### external setLiquidationGracePeriod
-> library Errors.AssetNotListed
-> library PoolLogic.executeSetLiquidationGracePeriod


### external setUserEMode
-> library SupplyLogic.executeSetUserEMode


### external setUserEModeOnBehalfOf
-> library SupplyLogic.executeSetUserEMode


### external setUserUseReserveAsCollateral
-> library CalldataLogic.decodeSetUserUseReserveAsCollateralParams
-> external setUserUseReserveAsCollateral


### external setUserUseReserveAsCollateralOnBehalfOf
-> library SupplyLogic.executeUseReserveAsCollateral


### external supply
-> library CalldataLogic.decodeSupplyParams
-> external supply


### external supplyWithPermit
-> external supplyWithPermit


### external syncIndexesState
-> library PoolLogic.executeSyncIndexesState


### external syncRatesState
-> library PoolLogic.executeSyncRatesState


### external updateFlashloanPremium
_(no internal calls)_


### external withdraw
-> library CalldataLogic.decodeWithdrawParams
-> external withdraw


---

## L2PoolInstance

_File: src/contracts/instances/L2PoolInstance.sol_

### external borrow
-> external borrow


### external initialize
-> library Errors.InvalidAddressesProvider


### external liquidationCall
-> library CalldataLogic.decodeLiquidationCallParams
-> external liquidationCall


### external repay
-> library CalldataLogic.decodeRepayParams
-> external repay


### external repayWithATokens
-> library CalldataLogic.decodeRepayParams
-> external repayWithATokens


### external repayWithPermit
-> library CalldataLogic.decodeRepayWithPermitParams
-> external repayWithPermit


### external setUserUseReserveAsCollateral
-> library CalldataLogic.decodeSetUserUseReserveAsCollateralParams
-> external setUserUseReserveAsCollateral


### external supply
-> library CalldataLogic.decodeSupplyParams
-> external supply


### external supplyWithPermit
-> external supplyWithPermit


### external withdraw
-> library CalldataLogic.decodeWithdrawParams
-> external withdraw


---

## LibraryReportStorage

_File: src/deployments/contracts/LibraryReportStorage.sol_

### public getLibrariesReport
_(no internal calls)_


---

## LiquidationDataProvider

_File: src/contracts/helpers/LiquidationDataProvider.sol_

### external getCollateralFullInfo
-> private _getCollateralFullInfo


### external getDebtFullInfo
-> private _getDebtFullInfo


### public getLiquidationInfo
-> public getUserPositionFullInfo
-> private _getCollateralFullInfo
-> private _getDebtFullInfo
-> private _canLiquidateThisHealthFactor
-> private _isReserveReadyForLiquidations
-> private _isCollateralEnabledForUser
-> private _getLiquidationBonus
  -> library EModeConfiguration.isReserveEnabledOnBitmap
-> private _getMaxDebtToLiquidate
-> private _getAvailableCollateralAndDebtToLiquidate
-> private _adjustAmountsForGoodLeftovers


### public getUserPositionFullInfo
_(no internal calls)_


---

## MetadataReporter

_File: src/deployments/contracts/utilities/MetadataReporter.sol_

### public getGitModuleVersion
_(no internal calls)_


### public getTimestamp
_(no internal calls)_


### external writeJsonReportLibraryBatch1
-> public getTimestamp
-> public getGitModuleVersion


### external writeJsonReportLibraryBatch2
-> public getTimestamp
-> public getGitModuleVersion


### external writeJsonReportMarket
-> public getTimestamp
-> public getGitModuleVersion


---

## MintableIncentivizedERC20

_File: src/contracts/protocol/tokenization/base/MintableIncentivizedERC20.sol_

### external allowance
_(no internal calls)_


### external approve
-> internal _approve


### public balanceOf
_(no internal calls)_


### external decimals
_(no internal calls)_


### external decreaseAllowance
-> internal _approve


### external getIncentivesController
_(no internal calls)_


### external increaseAllowance
-> internal _approve


### public name
_(no internal calls)_


### external renounceAllowance
-> internal _approve


### external symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### external transfer
-> internal _transfer


### external transferFrom
-> internal _spendAllowance
  -> internal _approve
-> internal _transfer


---

## Ownable

_File: src/contracts/dependencies/openzeppelin/contracts/Ownable.sol_

### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## Pool

_File: src/contracts/protocol/pool/Pool.sol_

### public FLASHLOAN_PREMIUM_TOTAL
_(no internal calls)_


### public FLASHLOAN_PREMIUM_TO_PROTOCOL
_(no internal calls)_


### public MAX_NUMBER_RESERVES
_(no internal calls)_


### external approvePositionManager
_(no internal calls)_


### public borrow
-> library BorrowLogic.executeBorrow
-> library DataTypes.ExecuteBorrowParams
-> library DataTypes.InterestRateMode


### external configureEModeCategory
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryBorrowableBitmap
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryCollateralBitmap
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryLtvzeroBitmap
-> library Errors.EModeCategoryReserved


### external deposit
-> library SupplyLogic.executeSupply
-> library DataTypes.ExecuteSupplyParams


### external dropReserve
-> library PoolLogic.executeDropReserve


### external eliminateReserveDeficit
-> library LiquidationLogic.executeEliminateDeficit
-> library DataTypes.ExecuteEliminateDeficitParams


### external finalizeTransfer
-> library Errors.CallerNotAToken
-> library SupplyLogic.executeFinalizeTransfer
-> library DataTypes.FinalizeTransferParams


### public flashLoan
-> library DataTypes.FlashloanParams
-> library FlashLoanLogic.executeFlashLoan


### public flashLoanSimple
-> library DataTypes.FlashloanSimpleParams
-> library FlashLoanLogic.executeFlashLoanSimple


### external getBorrowLogic
_(no internal calls)_


### external getConfiguration
_(no internal calls)_


### external getEModeCategoryBorrowableBitmap
_(no internal calls)_


### external getEModeCategoryCollateralBitmap
_(no internal calls)_


### external getEModeCategoryCollateralConfig
_(no internal calls)_


### external getEModeCategoryData
-> library DataTypes.EModeCategoryLegacy


### external getEModeCategoryLabel
_(no internal calls)_


### external getEModeCategoryLtvzeroBitmap
_(no internal calls)_


### external getFlashLoanLogic
_(no internal calls)_


### external getLiquidationGracePeriod
_(no internal calls)_


### external getLiquidationLogic
_(no internal calls)_


### external getPoolLogic
_(no internal calls)_


### external getReserveAToken
_(no internal calls)_


### external getReserveAddressById
_(no internal calls)_


### external getReserveData
_(no internal calls)_


### external getReserveDeficit
_(no internal calls)_


### external getReserveNormalizedIncome
_(no internal calls)_


### external getReserveNormalizedVariableDebt
_(no internal calls)_


### external getReserveVariableDebtToken
_(no internal calls)_


### external getReservesCount
_(no internal calls)_


### external getReservesList
_(no internal calls)_


### external getSupplyLogic
_(no internal calls)_


### external getUserAccountData
-> library PoolLogic.executeGetUserAccountData
-> library DataTypes.CalculateUserAccountDataParams


### external getUserConfiguration
_(no internal calls)_


### external getUserEMode
_(no internal calls)_


### external getVirtualUnderlyingBalance
_(no internal calls)_


### external initReserve
-> library PoolLogic.executeInitReserve
-> library DataTypes.InitReserveParams
-> public MAX_NUMBER_RESERVES


### external isApprovedPositionManager
_(no internal calls)_


### public liquidationCall
-> library LiquidationLogic.executeLiquidationCall
-> library DataTypes.ExecuteLiquidationCallParams


### external mintToTreasury
-> library PoolLogic.executeMintToTreasury


### external renouncePositionManagerRole
_(no internal calls)_


### public repay
-> library BorrowLogic.executeRepay
-> library DataTypes.ExecuteRepayParams
-> library DataTypes.InterestRateMode


### public repayWithATokens
-> library BorrowLogic.executeRepay
-> library DataTypes.ExecuteRepayParams
-> library DataTypes.InterestRateMode


### public repayWithPermit
-> library DataTypes.ExecuteRepayParams
-> library DataTypes.InterestRateMode
-> library BorrowLogic.executeRepay


### external rescueTokens
-> library PoolLogic.executeRescueTokens


### external resetIsolationModeTotalDebt
-> library PoolLogic.executeResetIsolationModeTotalDebt


### external setConfiguration
-> library Errors.ZeroAddressNotValid
-> library Errors.AssetNotListed


### external setLiquidationGracePeriod
-> library Errors.AssetNotListed
-> library PoolLogic.executeSetLiquidationGracePeriod


### external setUserEMode
-> library SupplyLogic.executeSetUserEMode


### external setUserEModeOnBehalfOf
-> library SupplyLogic.executeSetUserEMode


### public setUserUseReserveAsCollateral
-> library SupplyLogic.executeUseReserveAsCollateral


### external setUserUseReserveAsCollateralOnBehalfOf
-> library SupplyLogic.executeUseReserveAsCollateral


### public supply
-> library SupplyLogic.executeSupply
-> library DataTypes.ExecuteSupplyParams


### public supplyWithPermit
-> library SupplyLogic.executeSupply
-> library DataTypes.ExecuteSupplyParams


### external syncIndexesState
-> library PoolLogic.executeSyncIndexesState


### external syncRatesState
-> library PoolLogic.executeSyncRatesState


### external updateFlashloanPremium
_(no internal calls)_


### public withdraw
-> library SupplyLogic.executeWithdraw
-> library DataTypes.ExecuteWithdrawParams


---

## PoolAddressesProvider

_File: src/contracts/protocol/configuration/PoolAddressesProvider.sol_

### external getACLAdmin
-> public getAddress


### external getACLManager
-> public getAddress


### public getAddress
_(no internal calls)_


### external getMarketId
_(no internal calls)_


### external getPool
-> public getAddress


### external getPoolConfigurator
-> public getAddress


### external getPoolDataProvider
-> public getAddress


### external getPriceOracle
-> public getAddress


### external getPriceOracleSentinel
-> public getAddress


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external setACLAdmin
_(no internal calls)_


### external setACLManager
_(no internal calls)_


### external setAddress
_(no internal calls)_


### external setAddressAsProxy
-> internal _getProxyImplementation
-> internal _updateImpl


### external setMarketId
-> internal _setMarketId


### external setPoolConfiguratorImpl
-> internal _getProxyImplementation
-> internal _updateImpl


### external setPoolDataProvider
_(no internal calls)_


### external setPoolImpl
-> internal _getProxyImplementation
-> internal _updateImpl


### external setPriceOracle
_(no internal calls)_


### external setPriceOracleSentinel
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## PoolAddressesProviderRegistry

_File: src/contracts/protocol/configuration/PoolAddressesProviderRegistry.sol_

### external getAddressesProviderAddressById
_(no internal calls)_


### external getAddressesProviderIdByAddress
_(no internal calls)_


### external getAddressesProvidersList
_(no internal calls)_


### public owner
_(no internal calls)_


### external registerAddressesProvider
-> library Errors.InvalidAddressesProviderId
-> library Errors.AddressesProviderAlreadyAdded
-> internal _addToAddressesProvidersList


### public renounceOwnership
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### external unregisterAddressesProvider
-> library Errors.AddressesProviderNotRegistered
-> internal _removeFromAddressesProvidersList


---

## PoolConfigurator

_File: src/contracts/protocol/pool/PoolConfigurator.sol_

### external configureReserveAsCollateral
-> library Errors.InvalidReserveParams
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero


### external disableLiquidationGracePeriod
_(no internal calls)_


### external dropReserve
_(no internal calls)_


### external getConfiguratorLogic
_(no internal calls)_


### external getPendingLtv
_(no internal calls)_


### external initReserves
-> library ConfiguratorLogic.executeInitReserve


### external setAssetBorrowableInEMode
-> library Errors.AssetNotListed
-> library EModeConfiguration.setReserveBitmapBit


### external setAssetCollateralInEMode
-> library Errors.AssetNotListed
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero
-> library EModeConfiguration.isReserveEnabledOnBitmap
-> internal _setEmodeLtvZero
  -> library EModeConfiguration.setReserveBitmapBit
-> library Errors.ReserveFrozen
-> library EModeConfiguration.setReserveBitmapBit


### external setAssetLtvzeroInEMode
-> library Errors.AssetNotListed
-> library EModeConfiguration.isReserveEnabledOnBitmap
-> library Errors.MustBeEmodeCollateral
-> library Errors.ReserveFrozen
-> internal _setEmodeLtvZero
  -> library EModeConfiguration.setReserveBitmapBit


### external setBorrowCap
_(no internal calls)_


### external setBorrowableInIsolation
_(no internal calls)_


### external setDebtCeiling
-> internal _checkAssetIsCollateral
  -> library EModeConfiguration.isReserveEnabledOnBitmap
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero


### external setEModeCategory
-> library Errors.InvalidEmodeCategoryParams


### external setLiquidationProtocolFee
-> library Errors.InvalidLiquidationProtocolFee


### external setPoolPause
-> external setPoolPause


### external setReserveActive
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero


### external setReserveBorrowing
_(no internal calls)_


### external setReserveFactor
-> library Errors.InvalidReserveFactor


### external setReserveFlashLoaning
_(no internal calls)_


### external setReserveFreeze
-> library Errors.InvalidFreezeState
-> internal _setReserveLtvzero
  -> library Errors.ReserveFrozen
-> library EModeConfiguration.isReserveEnabledOnBitmap
-> internal _setEmodeLtvZero
  -> library EModeConfiguration.setReserveBitmapBit


### external setReserveInterestRateData
_(no internal calls)_


### external setReserveLtvzero
-> internal _setReserveLtvzero
  -> library Errors.ReserveFrozen
-> library Errors.InvalidLtvzeroState


### external setReservePause
-> external setReservePause


### external setSiloedBorrowing
-> internal _checkNoBorrowers
  -> library Errors.ReserveDebtNotZero


### external setSupplyCap
_(no internal calls)_


### external updateAToken
-> library ConfiguratorLogic.executeUpdateAToken


### external updateFlashloanPremium
-> library Errors.FlashloanPremiumInvalid


### external updateVariableDebtToken
-> library ConfiguratorLogic.executeUpdateVariableDebtToken


---

## PoolConfiguratorInstance

_File: src/contracts/instances/PoolConfiguratorInstance.sol_

### external configureReserveAsCollateral
-> library Errors.InvalidReserveParams
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero


### external disableLiquidationGracePeriod
_(no internal calls)_


### external dropReserve
_(no internal calls)_


### external getConfiguratorLogic
_(no internal calls)_


### external getPendingLtv
_(no internal calls)_


### external initReserves
-> library ConfiguratorLogic.executeInitReserve


### public initialize
_(no internal calls)_


### external setAssetBorrowableInEMode
-> library Errors.AssetNotListed
-> library EModeConfiguration.setReserveBitmapBit


### external setAssetCollateralInEMode
-> library Errors.AssetNotListed
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero
-> library EModeConfiguration.isReserveEnabledOnBitmap
-> internal _setEmodeLtvZero
  -> library EModeConfiguration.setReserveBitmapBit
-> library Errors.ReserveFrozen
-> library EModeConfiguration.setReserveBitmapBit


### external setAssetLtvzeroInEMode
-> library Errors.AssetNotListed
-> library EModeConfiguration.isReserveEnabledOnBitmap
-> library Errors.MustBeEmodeCollateral
-> library Errors.ReserveFrozen
-> internal _setEmodeLtvZero
  -> library EModeConfiguration.setReserveBitmapBit


### external setBorrowCap
_(no internal calls)_


### external setBorrowableInIsolation
_(no internal calls)_


### external setDebtCeiling
-> internal _checkAssetIsCollateral
  -> library EModeConfiguration.isReserveEnabledOnBitmap
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero


### external setEModeCategory
-> library Errors.InvalidEmodeCategoryParams


### external setLiquidationProtocolFee
-> library Errors.InvalidLiquidationProtocolFee


### external setPoolPause
-> external setPoolPause


### external setReserveActive
-> internal _checkNoSuppliers
  -> library Errors.ReserveLiquidityNotZero


### external setReserveBorrowing
_(no internal calls)_


### external setReserveFactor
-> library Errors.InvalidReserveFactor


### external setReserveFlashLoaning
_(no internal calls)_


### external setReserveFreeze
-> library Errors.InvalidFreezeState
-> internal _setReserveLtvzero
  -> library Errors.ReserveFrozen
-> library EModeConfiguration.isReserveEnabledOnBitmap
-> internal _setEmodeLtvZero
  -> library EModeConfiguration.setReserveBitmapBit


### external setReserveInterestRateData
_(no internal calls)_


### external setReserveLtvzero
-> internal _setReserveLtvzero
  -> library Errors.ReserveFrozen
-> library Errors.InvalidLtvzeroState


### external setReservePause
-> external setReservePause


### external setSiloedBorrowing
-> internal _checkNoBorrowers
  -> library Errors.ReserveDebtNotZero


### external setSupplyCap
_(no internal calls)_


### external updateAToken
-> library ConfiguratorLogic.executeUpdateAToken


### external updateFlashloanPremium
-> library Errors.FlashloanPremiumInvalid


### external updateVariableDebtToken
-> library ConfiguratorLogic.executeUpdateVariableDebtToken


---

## PoolInstance

_File: src/contracts/instances/PoolInstance.sol_

### public FLASHLOAN_PREMIUM_TOTAL
_(no internal calls)_


### public FLASHLOAN_PREMIUM_TO_PROTOCOL
_(no internal calls)_


### public MAX_NUMBER_RESERVES
_(no internal calls)_


### external approvePositionManager
_(no internal calls)_


### public borrow
-> library BorrowLogic.executeBorrow
-> library DataTypes.ExecuteBorrowParams
-> library DataTypes.InterestRateMode


### external configureEModeCategory
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryBorrowableBitmap
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryCollateralBitmap
-> library Errors.EModeCategoryReserved


### external configureEModeCategoryLtvzeroBitmap
-> library Errors.EModeCategoryReserved


### external deposit
-> library SupplyLogic.executeSupply
-> library DataTypes.ExecuteSupplyParams


### external dropReserve
-> library PoolLogic.executeDropReserve


### external eliminateReserveDeficit
-> library LiquidationLogic.executeEliminateDeficit
-> library DataTypes.ExecuteEliminateDeficitParams


### external finalizeTransfer
-> library Errors.CallerNotAToken
-> library SupplyLogic.executeFinalizeTransfer
-> library DataTypes.FinalizeTransferParams


### public flashLoan
-> library DataTypes.FlashloanParams
-> library FlashLoanLogic.executeFlashLoan


### public flashLoanSimple
-> library DataTypes.FlashloanSimpleParams
-> library FlashLoanLogic.executeFlashLoanSimple


### external getBorrowLogic
_(no internal calls)_


### external getConfiguration
_(no internal calls)_


### external getEModeCategoryBorrowableBitmap
_(no internal calls)_


### external getEModeCategoryCollateralBitmap
_(no internal calls)_


### external getEModeCategoryCollateralConfig
_(no internal calls)_


### external getEModeCategoryData
-> library DataTypes.EModeCategoryLegacy


### external getEModeCategoryLabel
_(no internal calls)_


### external getEModeCategoryLtvzeroBitmap
_(no internal calls)_


### external getFlashLoanLogic
_(no internal calls)_


### external getLiquidationGracePeriod
_(no internal calls)_


### external getLiquidationLogic
_(no internal calls)_


### external getPoolLogic
_(no internal calls)_


### external getReserveAToken
_(no internal calls)_


### external getReserveAddressById
_(no internal calls)_


### external getReserveData
_(no internal calls)_


### external getReserveDeficit
_(no internal calls)_


### external getReserveNormalizedIncome
_(no internal calls)_


### external getReserveNormalizedVariableDebt
_(no internal calls)_


### external getReserveVariableDebtToken
_(no internal calls)_


### external getReservesCount
_(no internal calls)_


### external getReservesList
_(no internal calls)_


### external getSupplyLogic
_(no internal calls)_


### external getUserAccountData
-> library PoolLogic.executeGetUserAccountData
-> library DataTypes.CalculateUserAccountDataParams


### external getUserConfiguration
_(no internal calls)_


### external getUserEMode
_(no internal calls)_


### external getVirtualUnderlyingBalance
_(no internal calls)_


### external initReserve
-> library PoolLogic.executeInitReserve
-> library DataTypes.InitReserveParams
-> public MAX_NUMBER_RESERVES


### external initialize
-> library Errors.InvalidAddressesProvider


### external isApprovedPositionManager
_(no internal calls)_


### public liquidationCall
-> library LiquidationLogic.executeLiquidationCall
-> library DataTypes.ExecuteLiquidationCallParams


### external mintToTreasury
-> library PoolLogic.executeMintToTreasury


### external renouncePositionManagerRole
_(no internal calls)_


### public repay
-> library BorrowLogic.executeRepay
-> library DataTypes.ExecuteRepayParams
-> library DataTypes.InterestRateMode


### public repayWithATokens
-> library BorrowLogic.executeRepay
-> library DataTypes.ExecuteRepayParams
-> library DataTypes.InterestRateMode


### public repayWithPermit
-> library DataTypes.ExecuteRepayParams
-> library DataTypes.InterestRateMode
-> library BorrowLogic.executeRepay


### external rescueTokens
-> library PoolLogic.executeRescueTokens


### external resetIsolationModeTotalDebt
-> library PoolLogic.executeResetIsolationModeTotalDebt


### external setConfiguration
-> library Errors.ZeroAddressNotValid
-> library Errors.AssetNotListed


### external setLiquidationGracePeriod
-> library Errors.AssetNotListed
-> library PoolLogic.executeSetLiquidationGracePeriod


### external setUserEMode
-> library SupplyLogic.executeSetUserEMode


### external setUserEModeOnBehalfOf
-> library SupplyLogic.executeSetUserEMode


### public setUserUseReserveAsCollateral
-> library SupplyLogic.executeUseReserveAsCollateral


### external setUserUseReserveAsCollateralOnBehalfOf
-> library SupplyLogic.executeUseReserveAsCollateral


### public supply
-> library SupplyLogic.executeSupply
-> library DataTypes.ExecuteSupplyParams


### public supplyWithPermit
-> library SupplyLogic.executeSupply
-> library DataTypes.ExecuteSupplyParams


### external syncIndexesState
-> library PoolLogic.executeSyncIndexesState


### external syncRatesState
-> library PoolLogic.executeSyncRatesState


### external updateFlashloanPremium
_(no internal calls)_


### public withdraw
-> library SupplyLogic.executeWithdraw
-> library DataTypes.ExecuteWithdrawParams


---

## PriceOracleSentinel

_File: src/contracts/misc/PriceOracleSentinel.sol_

### external getGracePeriod
_(no internal calls)_


### external getSequencerOracle
_(no internal calls)_


### external isBorrowAllowed
-> internal _isUpAndGracePeriodPassed


### external isLiquidationAllowed
-> internal _isUpAndGracePeriodPassed


### external setGracePeriod
_(no internal calls)_


### external setSequencerOracle
_(no internal calls)_


---

## PullRewardsTransferStrategy

_File: src/contracts/rewards/transfer-strategies/PullRewardsTransferStrategy.sol_

### external emergencyWithdrawal
_(no internal calls)_


### external getIncentivesController
_(no internal calls)_


### external getRewardsAdmin
_(no internal calls)_


### external getRewardsVault
_(no internal calls)_


### external performTransfer
_(no internal calls)_


---

## RewardsController

_File: src/contracts/rewards/RewardsController.sol_

### external claimAllRewards
-> internal _claimAllRewards
  -> internal _updateDataMultiple
    -> internal _updateData
      -> internal _updateRewardData
        -> internal _getAssetIndex
      -> internal _updateUserData
        -> internal _getRewards
  -> internal _getUserAssetBalances
  -> internal _transferRewards


### external claimAllRewardsOnBehalf
-> internal _claimAllRewards
  -> internal _updateDataMultiple
    -> internal _updateData
      -> internal _updateRewardData
        -> internal _getAssetIndex
      -> internal _updateUserData
        -> internal _getRewards
  -> internal _getUserAssetBalances
  -> internal _transferRewards


### external claimAllRewardsToSelf
-> internal _claimAllRewards
  -> internal _updateDataMultiple
    -> internal _updateData
      -> internal _updateRewardData
        -> internal _getAssetIndex
      -> internal _updateUserData
        -> internal _getRewards
  -> internal _getUserAssetBalances
  -> internal _transferRewards


### external claimRewards
-> internal _claimRewards
  -> internal _updateDataMultiple
    -> internal _updateData
      -> internal _updateRewardData
        -> internal _getAssetIndex
      -> internal _updateUserData
        -> internal _getRewards
  -> internal _getUserAssetBalances
  -> internal _transferRewards


### external claimRewardsOnBehalf
-> internal _claimRewards
  -> internal _updateDataMultiple
    -> internal _updateData
      -> internal _updateRewardData
        -> internal _getAssetIndex
      -> internal _updateUserData
        -> internal _getRewards
  -> internal _getUserAssetBalances
  -> internal _transferRewards


### external claimRewardsToSelf
-> internal _claimRewards
  -> internal _updateDataMultiple
    -> internal _updateData
      -> internal _updateRewardData
        -> internal _getAssetIndex
      -> internal _updateUserData
        -> internal _getRewards
  -> internal _getUserAssetBalances
  -> internal _transferRewards


### external configureAssets
-> internal _installTransferStrategy
  -> internal _isContract
-> internal _setRewardOracle
-> internal _configureAssets
  -> internal _updateRewardData
    -> internal _getAssetIndex


### external getAllUserRewards
-> internal _getUserAssetBalances
-> internal _getPendingRewards
  -> internal _getAssetIndex
  -> internal _getRewards


### external getAssetDecimals
_(no internal calls)_


### external getAssetIndex
-> internal _getAssetIndex


### external getClaimer
_(no internal calls)_


### external getDistributionEnd
_(no internal calls)_


### external getEmissionManager
_(no internal calls)_


### external getRewardOracle
_(no internal calls)_


### external getRewardsByAsset
_(no internal calls)_


### external getRewardsData
_(no internal calls)_


### external getRewardsList
_(no internal calls)_


### external getTransferStrategy
_(no internal calls)_


### external getUserAccruedRewards
_(no internal calls)_


### external getUserAssetIndex
_(no internal calls)_


### external getUserRewards
-> internal _getUserReward
  -> internal _getPendingRewards
    -> internal _getAssetIndex
    -> internal _getRewards
-> internal _getUserAssetBalances


### external handleAction
-> internal _updateData
  -> internal _updateRewardData
    -> internal _getAssetIndex
  -> internal _updateUserData
    -> internal _getRewards


### external initialize
_(no internal calls)_


### external setClaimer
_(no internal calls)_


### external setDistributionEnd
_(no internal calls)_


### external setEmissionPerSecond
-> internal _updateRewardData
  -> internal _getAssetIndex


### external setRewardOracle
-> internal _setRewardOracle


### external setTransferStrategy
-> internal _installTransferStrategy
  -> internal _isContract


---

## RewardsDistributor

_File: src/contracts/rewards/RewardsDistributor.sol_

### external getAllUserRewards
-> internal _getPendingRewards
  -> internal _getAssetIndex
  -> internal _getRewards


### external getAssetDecimals
_(no internal calls)_


### external getAssetIndex
-> internal _getAssetIndex


### external getDistributionEnd
_(no internal calls)_


### external getEmissionManager
_(no internal calls)_


### external getRewardsByAsset
_(no internal calls)_


### external getRewardsData
_(no internal calls)_


### external getRewardsList
_(no internal calls)_


### external getUserAccruedRewards
_(no internal calls)_


### external getUserAssetIndex
_(no internal calls)_


### external getUserRewards
-> internal _getUserReward
  -> internal _getPendingRewards
    -> internal _getAssetIndex
    -> internal _getRewards


### external setDistributionEnd
_(no internal calls)_


### external setEmissionPerSecond
-> internal _updateRewardData
  -> internal _getAssetIndex


---

## ScaledBalanceTokenBase

_File: src/contracts/protocol/tokenization/base/ScaledBalanceTokenBase.sol_

### external getPreviousIndex
_(no internal calls)_


### external getScaledUserBalanceAndSupply
_(no internal calls)_


### external scaledBalanceOf
_(no internal calls)_


### public scaledTotalSupply
_(no internal calls)_


---

## StakedTokenTransferStrategy

_File: src/contracts/rewards/transfer-strategies/StakedTokenTransferStrategy.sol_

### external dropApproval
_(no internal calls)_


### external emergencyWithdrawal
_(no internal calls)_


### external getIncentivesController
_(no internal calls)_


### external getRewardsAdmin
_(no internal calls)_


### external getStakeContract
_(no internal calls)_


### external getUnderlyingToken
_(no internal calls)_


### external performTransfer
_(no internal calls)_


### external renewApproval
_(no internal calls)_


---

## StataTokenFactory

_File: src/contracts/extensions/stata-token/StataTokenFactory.sol_

### external createStataTokens
_(no internal calls)_


### external getStataToken
_(no internal calls)_


### external getStataTokens
_(no internal calls)_


### external initialize
_(no internal calls)_


---

## StataTokenV2

_File: src/contracts/extensions/stata-token/StataTokenV2.sol_

### public aToken
-> private _getERC4626StataTokenStorage


### public canPause
_(no internal calls)_


### external claimRewards
-> internal _claimRewardsOnBehalf


### external claimRewardsOnBehalf
-> external_callback INCENTIVES_CONTROLLER.getClaimer
-> internal _claimRewardsOnBehalf


### external claimRewardsToSelf
-> internal _claimRewardsOnBehalf


### public collectAndUpdateRewards
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.claimRewards
  -> internal _claimRewardsOnBehalf


### public decimals
_(no internal calls)_


### external depositATokens
-> public aToken
  -> private _getERC4626StataTokenStorage
-> internal _deposit
  -> internal _deposit


### external depositWithPermit
-> public aToken
  -> private _getERC4626StataTokenStorage
-> internal _deposit
  -> internal _deposit


### external getClaimableRewards
-> internal _getClaimableRewards
  -> private _getERC20AaveLMStorage
  -> internal _getPendingRewards
    -> public decimals
-> public getCurrentRewardsIndex
  -> private _getERC20AaveLMStorage
  -> external_callback INCENTIVES_CONTROLLER.getAssetIndex


### public getCurrentRewardsIndex
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.getAssetIndex


### external getReferenceAsset
-> private _getERC20AaveLMStorage


### external getTotalClaimableRewards
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.getUserRewards


### external getUnclaimedRewards
-> private _getERC20AaveLMStorage


### external initialize
-> internal __ERC20AaveLM_init
  -> internal __ERC20AaveLM_init_unchained
    -> private _getERC20AaveLMStorage
    -> public refreshRewardTokens
      -> private _getERC20AaveLMStorage
      -> external_callback INCENTIVES_CONTROLLER.getRewardsByAsset
      -> internal _registerRewardToken
        -> public isRegisteredRewardToken
          -> private _getERC20AaveLMStorage
        -> public getCurrentRewardsIndex
          -> private _getERC20AaveLMStorage
          -> external_callback INCENTIVES_CONTROLLER.getAssetIndex
        -> private _getERC20AaveLMStorage
-> internal __ERC4626StataToken_init
  -> internal __ERC4626StataToken_init_unchained
    -> private _getERC4626StataTokenStorage


### public isRegisteredRewardToken
-> private _getERC20AaveLMStorage


### external latestAnswer
-> internal _rate


### public maxDeposit
-> library ReserveConfiguration.getActive
-> library ReserveConfiguration.getPaused
-> library ReserveConfiguration.getFrozen
-> library ReserveConfiguration.getSupplyCap
-> library ReserveConfiguration.getDecimals
-> internal _rate


### public maxMint
-> public maxDeposit
  -> library ReserveConfiguration.getActive
  -> library ReserveConfiguration.getPaused
  -> library ReserveConfiguration.getFrozen
  -> library ReserveConfiguration.getSupplyCap
  -> library ReserveConfiguration.getDecimals
  -> internal _rate


### public maxRedeem
-> library ReserveConfiguration.getActive
-> library ReserveConfiguration.getPaused


### public maxRescue
-> public aToken
  -> private _getERC4626StataTokenStorage
-> internal _convertToAssets
  -> internal _rate


### public maxWithdraw
-> public maxRedeem
  -> library ReserveConfiguration.getActive
  -> library ReserveConfiguration.getPaused


### public nonces
_(no internal calls)_


### external redeemATokens
-> internal _withdraw
  -> internal _withdraw


### public refreshRewardTokens
-> private _getERC20AaveLMStorage
-> external_callback INCENTIVES_CONTROLLER.getRewardsByAsset
-> internal _registerRewardToken
  -> public isRegisteredRewardToken
    -> private _getERC20AaveLMStorage
  -> public getCurrentRewardsIndex
    -> private _getERC20AaveLMStorage
    -> external_callback INCENTIVES_CONTROLLER.getAssetIndex
  -> private _getERC20AaveLMStorage


### external rewardTokens
-> private _getERC20AaveLMStorage


### external setPaused
_(no internal calls)_


### public totalAssets
-> internal _convertToAssets
  -> internal _rate


### public whoCanRescue
_(no internal calls)_


---

## TransferStrategyBase

_File: src/contracts/rewards/transfer-strategies/TransferStrategyBase.sol_

### external emergencyWithdrawal
_(no internal calls)_


### external getIncentivesController
_(no internal calls)_


### external getRewardsAdmin
_(no internal calls)_


---

## UiIncentiveDataProviderV3

_File: src/contracts/helpers/UiIncentiveDataProviderV3.sol_

### external getFullReservesIncentiveData
-> private _getReservesIncentivesData
-> private _getUserReservesIncentivesData


### external getReservesIncentivesData
-> private _getReservesIncentivesData


### external getUserReservesIncentivesData
-> private _getUserReservesIncentivesData


---

## UiPoolDataProviderV3

_File: src/contracts/helpers/UiPoolDataProviderV3.sol_

### public bytes32ToString
_(no internal calls)_


### external getEModes
-> library DataTypes.EModeCategory


### external getReservesData
-> public bytes32ToString


### external getReservesList
_(no internal calls)_


### external getUserReservesData
_(no internal calls)_


---

## VariableDebtToken

_File: src/contracts/protocol/tokenization/VariableDebtToken.sol_

### external UNDERLYING_ASSET_ADDRESS
_(no internal calls)_


### external allowance
-> library Errors.OperationNotSupported


### external approve
-> library Errors.OperationNotSupported


### external approveDelegation
-> internal _approveDelegation


### public balanceOf
_(no internal calls)_


### external borrowAllowance
_(no internal calls)_


### external burn
-> internal _burnScaled
  -> library Errors.InvalidBurnAmount
-> public scaledTotalSupply


### external decreaseAllowance
-> library Errors.OperationNotSupported


### external delegationWithSig
-> library Errors.ZeroAddressNotValid
-> library Errors.InvalidExpiration
-> library Errors.InvalidSignature
-> internal _approveDelegation


### external getPreviousIndex
_(no internal calls)_


### external getScaledUserBalanceAndSupply
_(no internal calls)_


### external increaseAllowance
-> library Errors.OperationNotSupported


### external mint
-> internal _decreaseBorrowAllowance
-> internal _mintScaled
  -> library Errors.InvalidMintAmount
-> public scaledTotalSupply


### external renounceAllowance
-> library Errors.OperationNotSupported


### external renounceDelegation
-> internal _approveDelegation


### external scaledBalanceOf
_(no internal calls)_


### public scaledTotalSupply
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### external transfer
-> library Errors.OperationNotSupported


### external transferFrom
-> library Errors.OperationNotSupported


---

## VariableDebtTokenInstance

_File: src/contracts/instances/VariableDebtTokenInstance.sol_

### external UNDERLYING_ASSET_ADDRESS
_(no internal calls)_


### external allowance
-> library Errors.OperationNotSupported


### external approve
-> library Errors.OperationNotSupported


### public balanceOf
_(no internal calls)_


### external burn
_(no internal calls)_


### external decreaseAllowance
-> library Errors.OperationNotSupported


### external increaseAllowance
-> library Errors.OperationNotSupported


### external initialize
-> library Errors.PoolAddressesDoNotMatch


### external mint
_(no internal calls)_


### external renounceAllowance
-> library Errors.OperationNotSupported


### public totalSupply
_(no internal calls)_


### external transfer
-> library Errors.OperationNotSupported


### external transferFrom
-> library Errors.OperationNotSupported


---

## VariableDebtTokenMainnetInstanceGHO

_File: src/contracts/instances/VariableDebtTokenMainnetInstanceGHO.sol_

### external UNDERLYING_ASSET_ADDRESS
_(no internal calls)_


### external allowance
-> library Errors.OperationNotSupported


### external approve
-> library Errors.OperationNotSupported


### public balanceOf
_(no internal calls)_


### external burn
_(no internal calls)_


### external decreaseAllowance
-> library Errors.OperationNotSupported


### external increaseAllowance
-> library Errors.OperationNotSupported


### external initialize
-> library Errors.PoolAddressesDoNotMatch


### external mint
_(no internal calls)_


### external renounceAllowance
-> library Errors.OperationNotSupported


### public totalSupply
_(no internal calls)_


### external transfer
-> library Errors.OperationNotSupported


### external transferFrom
-> library Errors.OperationNotSupported


### external updateDiscountDistribution
_(no internal calls)_


---

## WETH9

_File: src/contracts/dependencies/weth/WETH9.sol_

### public approve
_(no internal calls)_


### public deposit
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> public transferFrom


### public transferFrom
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## WalletBalanceProvider

_File: src/contracts/helpers/WalletBalanceProvider.sol_

### public balanceOf
_(no internal calls)_


### external batchBalanceOf
-> public balanceOf


### external getUserWalletBalances
-> public balanceOf


---

## WrappedTokenGatewayV3

_File: src/contracts/helpers/WrappedTokenGatewayV3.sol_

### external borrowETH
-> internal _safeTransferETH


### external depositETH
_(no internal calls)_


### external emergencyEtherTransfer
-> internal _safeTransferETH


### external emergencyTokenTransfer
_(no internal calls)_


### external getWETHAddress
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### external repayETH
-> internal _safeTransferETH


### public transferOwnership
_(no internal calls)_


### external withdrawETH
-> internal _safeTransferETH


### external withdrawETHWithPermit
-> internal _safeTransferETH

