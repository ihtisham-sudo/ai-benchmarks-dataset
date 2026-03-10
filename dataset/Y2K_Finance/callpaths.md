# Callpaths — Y2K_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AdminPriceProvider

_File: oracles/individual/AdminPriceProvider.sol_

### public conditionMet
-> public getLatestPrice
  -> public latestRoundData


### public getLatestPrice
-> public latestRoundData


### public latestRoundData
_(no internal calls)_


### external setPrice
_(no internal calls)_


---

## CVIPriceProvider

_File: oracles/individual/CVIPriceProvider.sol_

### public conditionMet
-> public getLatestPrice


### public getLatestPrice
_(no internal calls)_


### public latestRoundData
_(no internal calls)_


---

## Carousel

_File: Carousel/Carousel.sol_

### public calculateFeePercent
_(no internal calls)_


### public changeController
_(no internal calls)_


### external changeDepositFee
_(no internal calls)_


### external changeRelayerFee
_(no internal calls)_


### external cleanUpRolloverQueue
_(no internal calls)_


### public delistInRollover
-> public isEnlistedInRolloverQueue
  -> public getRolloverIndex
-> public getRolloverIndex


### public deposit
-> internal _asset
-> internal _deposit
  -> public getEpochDepositFee
    -> public getEpochConfig
    -> public calculateFeePercent
  -> internal _asset
  -> public treasury
  -> internal _mintShares


### external depositETH
-> internal _deposit
  -> public getEpochDepositFee
    -> public getEpochConfig
    -> public calculateFeePercent
  -> internal _asset
  -> public treasury
  -> internal _mintShares


### public enlistInRollover
-> public previewWithdraw
-> public getRolloverIndex


### public getAllEpochs
_(no internal calls)_


### public getDepositQueueLength
_(no internal calls)_


### public getDepositQueueTVL
_(no internal calls)_


### public getEpochConfig
_(no internal calls)_


### public getEpochDepositFee
-> public getEpochConfig
-> public calculateFeePercent


### public getEpochsLength
_(no internal calls)_


### public getRolloverIndex
_(no internal calls)_


### public getRolloverPosition
-> public isEnlistedInRolloverQueue
  -> public getRolloverIndex
-> public getRolloverIndex


### public getRolloverQueueItem
_(no internal calls)_


### public getRolloverQueueLength
_(no internal calls)_


### public getRolloverTVL
-> public previewWithdraw


### public getRolloverTVLByEpochId
-> public previewWithdraw


### public isEnlistedInRolloverQueue
-> public getRolloverIndex


### external mintDepositInQueue
-> public getEpochDepositFee
  -> public getEpochConfig
  -> public calculateFeePercent
-> internal _asset
-> public treasury
-> internal _mintShares


### external mintRollovers
-> public previewWithdraw
-> public previewAmountInShares
-> public previewEmissionsWithdraw
-> internal _mintShares


### public previewAmountInShares
_(no internal calls)_


### public previewEmissionsWithdraw
_(no internal calls)_


### public previewWithdraw
_(no internal calls)_


### external resolveEpoch
-> public totalAssets


### public safeBatchTransferFrom
_(no internal calls)_


### public safeTransferFrom
_(no internal calls)_


### external sendTokens
-> public treasury


### external setClaimTVL
_(no internal calls)_


### external setCounterPartyVault
_(no internal calls)_


### external setEmissions
_(no internal calls)_


### external setEpoch
_(no internal calls)_


### public setEpochNull
-> public treasury


### public totalAssets
_(no internal calls)_


### public treasury
_(no internal calls)_


### public whiteListAddress
_(no internal calls)_


### external withdraw
-> public previewEmissionsWithdraw
-> public previewWithdraw


---

## CarouselFactory

_File: Carousel/CarouselFactory.sol_

### public changeController
_(no internal calls)_


### public changeDepositFee
_(no internal calls)_


### public changeOracle
_(no internal calls)_


### public changeRelayerFee
_(no internal calls)_


### public changeTimelocker
_(no internal calls)_


### public cleanupRolloverQueue
_(no internal calls)_


### public createEpoch
_(no internal calls)_


### external createEpochWithEmissions
-> internal _createEpoch
  -> public getEpochId
  -> internal _setEpoch


### external createNewCarouselMarket
-> public getMarketId
-> library CarouselCreator.createCarousel
-> library CarouselCreator.CarouselMarketConfiguration


### external createNewMarket
_(no internal calls)_


### public getEpochFee
_(no internal calls)_


### public getEpochId
_(no internal calls)_


### public getEpochsByMarketId
_(no internal calls)_


### public getMarketId
_(no internal calls)_


### public getMarketInfo
_(no internal calls)_


### public getVaults
_(no internal calls)_


### public setTreasury
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public whitelistAddressOnMarket
_(no internal calls)_


### public whitelistController
_(no internal calls)_


---

## CarouselFactoryPausable

_File: Carousel/CarouselFactoryPausable.sol_

### public changeController
_(no internal calls)_


### public changeDepositFee
_(no internal calls)_


### public changeOracle
_(no internal calls)_


### public changeRelayerFee
_(no internal calls)_


### public changeTimelocker
_(no internal calls)_


### public cleanupRolloverQueue
_(no internal calls)_


### public createEpoch
_(no internal calls)_


### external createEpochWithEmissions
-> internal _createEpoch
  -> public getEpochId
  -> internal _setEpoch


### external createNewCarouselMarket
-> public getMarketId
-> library CarouselCreatorPausable.createCarousel
-> library CarouselCreatorPausable.CarouselMarketConfiguration


### external createNewMarket
_(no internal calls)_


### public getEpochFee
_(no internal calls)_


### public getEpochId
_(no internal calls)_


### public getEpochsByMarketId
_(no internal calls)_


### public getMarketId
_(no internal calls)_


### public getMarketInfo
_(no internal calls)_


### public getVaults
_(no internal calls)_


### external pauseMarket
_(no internal calls)_


### public setTreasury
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public whitelistAddressOnMarket
_(no internal calls)_


### public whitelistController
_(no internal calls)_


---

## CarouselPausable

_File: Carousel/CarouselPausable.sol_

### public calculateFeePercent
_(no internal calls)_


### public changeController
_(no internal calls)_


### external changeDepositFee
_(no internal calls)_


### external changeRelayerFee
_(no internal calls)_


### external cleanUpRolloverQueue
_(no internal calls)_


### public delistInRollover
-> public isEnlistedInRolloverQueue
  -> public getRolloverIndex
-> public getRolloverIndex


### public deposit
-> internal _asset
-> internal _deposit
  -> public getEpochDepositFee
    -> public getEpochConfig
    -> public calculateFeePercent
  -> internal _asset
  -> public treasury
  -> internal _mintShares


### external depositETH
-> internal _deposit
  -> public getEpochDepositFee
    -> public getEpochConfig
    -> public calculateFeePercent
  -> internal _asset
  -> public treasury
  -> internal _mintShares


### public enlistInRollover
-> public previewWithdraw
-> public getRolloverIndex


### public getAllEpochs
_(no internal calls)_


### public getDepositQueueLength
_(no internal calls)_


### public getDepositQueueTVL
_(no internal calls)_


### public getEpochConfig
_(no internal calls)_


### public getEpochDepositFee
-> public getEpochConfig
-> public calculateFeePercent


### public getEpochsLength
_(no internal calls)_


### public getRolloverIndex
_(no internal calls)_


### public getRolloverPosition
-> public isEnlistedInRolloverQueue
  -> public getRolloverIndex
-> public getRolloverIndex


### public getRolloverQueueItem
_(no internal calls)_


### public getRolloverQueueLength
_(no internal calls)_


### public getRolloverTVL
-> public previewWithdraw


### public getRolloverTVLByEpochId
-> public previewWithdraw


### public isEnlistedInRolloverQueue
-> public getRolloverIndex


### external mintDepositInQueue
-> public getEpochDepositFee
  -> public getEpochConfig
  -> public calculateFeePercent
-> internal _asset
-> public treasury
-> internal _mintShares


### external mintRollovers
-> public previewWithdraw
-> public previewAmountInShares
-> public previewEmissionsWithdraw
-> internal _mintShares


### external pauseMarket
_(no internal calls)_


### public previewAmountInShares
_(no internal calls)_


### public previewEmissionsWithdraw
_(no internal calls)_


### public previewWithdraw
_(no internal calls)_


### external resolveEpoch
-> public totalAssets


### public safeBatchTransferFrom
_(no internal calls)_


### public safeTransferFrom
_(no internal calls)_


### external sendTokens
-> public treasury


### external setClaimTVL
_(no internal calls)_


### external setCounterPartyVault
_(no internal calls)_


### external setEmissions
_(no internal calls)_


### external setEpoch
_(no internal calls)_


### public setEpochNull
-> public treasury


### public totalAssets
_(no internal calls)_


### public treasury
_(no internal calls)_


### public whiteListAddress
_(no internal calls)_


### external withdraw
-> public previewEmissionsWithdraw
-> public previewWithdraw


---

## ChainlinkPriceProvider

_File: oracles/individual/ChainlinkPriceProvider.sol_

### public conditionMet
-> public getLatestPrice
  -> public latestRoundData


### public getLatestPrice
-> public latestRoundData


### public latestRoundData
_(no internal calls)_


---

## ChainlinkUniversalProvider

_File: oracles/universal/ChainlinkUniversalProvider.sol_

### public conditionMet
-> public getLatestPrice
  -> public latestRoundData
  -> public decimals


### public decimals
_(no internal calls)_


### public description
_(no internal calls)_


### public getLatestPrice
-> public latestRoundData
-> public decimals


### public latestRoundData
_(no internal calls)_


### external setConditionType
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


---

## ControllerGeneric

_File: Controllers/ControllerGeneric.sol_

### public calculateWithdrawalFeeValue
_(no internal calls)_


### public canExecEnd
_(no internal calls)_


### public canExecLiquidation
_(no internal calls)_


### public canExecNullEpoch
_(no internal calls)_


### external getVaultFactory
_(no internal calls)_


### public triggerEndEpoch
-> private _checkGenericConditions
-> internal _checkEndEpochConditions
-> public calculateWithdrawalFeeValue


### public triggerLiquidation
-> private _checkGenericConditions
-> internal _checkLiquidationConditions
-> public calculateWithdrawalFeeValue


### public triggerNullEpoch
-> private _checkGenericConditions
-> internal _checkNullEpochConditions


---

## ControllerPeggedAssetV2

_File: Controllers/ControllerPeggedAssetV2.sol_

### public calculateWithdrawalFeeValue
_(no internal calls)_


### public canExecDepeg
-> public getLatestPrice


### public canExecEnd
_(no internal calls)_


### public canExecNullEpoch
_(no internal calls)_


### public getLatestPrice
_(no internal calls)_


### external getVaultFactory
_(no internal calls)_


### public triggerDepeg
-> public getLatestPrice
-> public calculateWithdrawalFeeValue


### public triggerEndEpoch
-> public calculateWithdrawalFeeValue


### public triggerNullEpoch
_(no internal calls)_


---

## DIAPriceProvider

_File: oracles/individual/DIAPriceProvider.sol_

### public conditionMet
-> private _getLatestPrice


### public getLatestPrice
-> private _getLatestPrice


### public latestRoundData
-> private _getLatestPrice


---

## DIAUniversalProvider

_File: oracles/universal/DIAUniversalProvider.sol_

### public conditionMet
-> private _getLatestPrice
  -> public decimals


### public decimals
_(no internal calls)_


### public description
_(no internal calls)_


### public getLatestPrice
-> private _getLatestPrice
  -> public decimals


### public latestRoundData
-> private _getLatestPrice
  -> public decimals


### external setConditionType
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


---

## ERC1155

_File: CustomERC1155/ERC1155.sol_

### public balanceOf
_(no internal calls)_


### public balanceOfBatch
-> public balanceOf


### public isApprovedForAll
_(no internal calls)_


### public safeBatchTransferFrom
-> public isApprovedForAll
-> internal _safeBatchTransferFrom
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer
  -> private _doSafeBatchTransferAcceptanceCheck


### public safeTransferFrom
-> public isApprovedForAll
-> internal _safeTransferFrom
  -> private _asSingletonArray
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer
  -> private _doSafeTransferAcceptanceCheck


### public setApprovalForAll
-> internal _setApprovalForAll


### public supportsInterface
_(no internal calls)_


### public uri
_(no internal calls)_


---

## ERC1155Supply

_File: CustomERC1155/ERC1155Supply.sol_

### public balanceOf
_(no internal calls)_


### public balanceOfBatch
-> public balanceOf


### public exists
-> external_callback ERC1155Supply.totalSupply


### public isApprovedForAll
_(no internal calls)_


### public safeBatchTransferFrom
-> public isApprovedForAll
-> internal _safeBatchTransferFrom
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer
  -> private _doSafeBatchTransferAcceptanceCheck


### public safeTransferFrom
-> public isApprovedForAll
-> internal _safeTransferFrom
  -> private _asSingletonArray
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer
  -> private _doSafeTransferAcceptanceCheck


### public setApprovalForAll
-> internal _setApprovalForAll


### public supportsInterface
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public uri
_(no internal calls)_


---

## GdaiPriceProvider

_File: oracles/individual/GdaiPriceProvider.sol_

### public conditionMet
-> public getLatestPrice


### public getLatestPrice
_(no internal calls)_


### public latestRoundData
_(no internal calls)_


---

## Owned

_File: Farms/Owned.sol_

### external acceptOwnership
_(no internal calls)_


### external nominateNewOwner
_(no internal calls)_


---

## PythPriceProvider

_File: oracles/individual/PythPriceProvider.sol_

### public conditionMet
-> public getLatestPrice


### public getLatestPrice
_(no internal calls)_


### public latestRoundData
_(no internal calls)_


---

## RedstoneCoreUniversalProvider

_File: oracles/universal/RedstoneCoreUniversalProvider.sol_

### public conditionMet
-> public getLatestPrice
  -> public latestRoundData
  -> public decimals


### public decimals
_(no internal calls)_


### public description
_(no internal calls)_


### public extractPrice
-> public getDataFeeds


### public getCurrentPrices
_(no internal calls)_


### public getDataFeeds
_(no internal calls)_


### public getLatestPrice
-> public latestRoundData
-> public decimals


### public latestRoundData
_(no internal calls)_


### external setConditionType
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


### external updatePrices
-> public extractPrice
  -> public getDataFeeds


---

## RedstonePriceProvider

_File: oracles/individual/RedstonePriceProvider.sol_

### public conditionMet
-> public getLatestPrice
  -> public latestRoundData


### public getLatestPrice
-> public latestRoundData


### public latestRoundData
_(no internal calls)_


### public stringToBytes32
_(no internal calls)_


---

## RedstoneUniversalProvider

_File: oracles/universal/RedstoneUniversalProvider.sol_

### public conditionMet
-> public getLatestPrice
  -> public latestRoundData
  -> public decimals


### public decimals
_(no internal calls)_


### public description
_(no internal calls)_


### public getLatestPrice
-> public latestRoundData
-> public decimals


### public latestRoundData
_(no internal calls)_


### external setConditionType
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


---

## RewardBalances

_File: Farms/RewardBalances.sol_

### public appendStakingContractAddress
_(no internal calls)_


### external appendStakingContractAddressesLoop
-> public appendStakingContractAddress


### external balanceOf
_(no internal calls)_


### external removeStakingContractAddress
_(no internal calls)_


---

## RewardsDistributionRecipient

_File: Farms/RewardsDistributionRecipient.sol_

### external acceptOwnership
_(no internal calls)_


### external nominateNewOwner
_(no internal calls)_


### external setRewardsDistribution
_(no internal calls)_


---

## SemiFungibleVault

_File: SemiFungibleVault.sol_

### public deposit
_(no internal calls)_


### public exists
-> external_callback ERC1155Supply.totalSupply


### public previewWithdraw
_(no internal calls)_


### public totalAssets
-> public totalSupply


### public totalSupply
_(no internal calls)_


### external withdraw
-> public previewWithdraw


---

## StakingRewards

_File: Farms/StakingRewards.sol_

### external balanceOf
_(no internal calls)_


### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable


### external exit
-> public withdraw
-> public getReward


### public getReward
_(no internal calls)_


### external getRewardForDuration
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### external notifyRewardAmount
_(no internal calls)_


### external pause
_(no internal calls)_


### external recoverERC20
_(no internal calls)_


### public rewardPerToken
-> public lastTimeRewardApplicable


### external setRewardsDistribution
_(no internal calls)_


### external setRewardsDuration
_(no internal calls)_


### external stake
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### external unpause
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## TimeLock

_File: TimeLock.sol_

### external cancel
-> public getTxId


### external changeOwner
_(no internal calls)_


### external changeOwnerOnFactory
_(no internal calls)_


### external changeTimelockerOnFactory
_(no internal calls)_


### external execute
-> public getTxId


### public getTxId
_(no internal calls)_


### external queue
-> public getTxId


---

## UmaV2AssertionProvider

_File: oracles/individual/UmaV2AssertionProvider.sol_

### public checkAssertion
_(no internal calls)_


### public conditionMet
-> public checkAssertion


### external priceSettled
_(no internal calls)_


### external requestLatestAssertion
-> internal _toUtf8BytesUint


### external updateCoverageStart
_(no internal calls)_


### external updateReward
_(no internal calls)_


### external withdrawBond
_(no internal calls)_


---

## UmaV2PriceProvider

_File: oracles/individual/UmaV2PriceProvider.sol_

### public conditionMet
-> public getLatestPrice
  -> public latestRoundData


### public getLatestPrice
-> public latestRoundData


### public latestRoundData
_(no internal calls)_


### external priceSettled
_(no internal calls)_


### external requestLatestPrice
_(no internal calls)_


### external updateReward
_(no internal calls)_


### external withdrawBond
_(no internal calls)_


---

## UmaV3AssertionProvider

_File: oracles/individual/UmaV3AssertionProvider.sol_

### external assertionResolvedCallback
_(no internal calls)_


### public checkAssertion
_(no internal calls)_


### public conditionMet
-> public checkAssertion


### external fetchAssertion
-> private _fetchAssertion
  -> internal _composeClaim
    -> internal _toUtf8BytesUint


### external resetAnswerAfterTimeout
_(no internal calls)_


### external setAssertionDescription
_(no internal calls)_


### external updateRelayer
_(no internal calls)_


### external updateRequiredBond
_(no internal calls)_


### external withdrawBond
_(no internal calls)_


---

## UmaV3PriceProvider

_File: oracles/individual/UmaV3PriceProvider.sol_

### external assertionResolvedCallback
_(no internal calls)_


### public conditionMet
-> public getLatestPrice


### public getLatestPrice
_(no internal calls)_


### external updateAssertionDataAndFetch
-> internal _updateAssertionData
-> internal _fetchAssertion
  -> internal _composeClaim
    -> internal _toUtf8BytesUint


### external updateRelayer
_(no internal calls)_


### external updateRequiredBond
_(no internal calls)_


### external withdrawBond
_(no internal calls)_


---

## UmaV3PriceProviderRound

_File: oracles/individual/UmaV3PriceProviderRound.sol_

### external assertionResolvedCallback
_(no internal calls)_


### public conditionMet
-> public getLatestPrice


### public getLatestPrice
_(no internal calls)_


### external updateAssertionDataAndFetch
-> internal _updateAssertionData
-> internal _fetchAssertion
  -> internal _composeClaim
    -> internal _toUtf8BytesUint


### external updateRelayer
_(no internal calls)_


### external updateRequiredBond
_(no internal calls)_


### external withdrawBond
_(no internal calls)_


---

## UmaV3PriceProviderVol

_File: oracles/individual/UmaV3PriceProviderVol.sol_

### external assertionResolvedCallback
_(no internal calls)_


### public conditionMet
-> public getLatestPrice


### public getLatestPrice
_(no internal calls)_


### public latestRoundData
_(no internal calls)_


### external updateAssertionDataAndFetch
-> internal _updateAssertionData
-> internal _fetchAssertion
  -> internal _composeClaim
    -> internal _toUtf8BytesUint


### external updateRelayer
_(no internal calls)_


### external updateRequiredBond
_(no internal calls)_


### external withdrawBond
_(no internal calls)_


---

## VaultFactoryV2

_File: VaultFactoryV2.sol_

### public changeController
_(no internal calls)_


### public changeOracle
_(no internal calls)_


### public changeTimelocker
_(no internal calls)_


### public createEpoch
-> internal _createEpoch
  -> public getEpochId
  -> internal _setEpoch


### external createNewMarket
-> internal _createNewMarket
  -> public getMarketId
  -> library VaultV2Creator.createVaultV2
  -> library VaultV2Creator.MarketConfiguration


### public getEpochFee
_(no internal calls)_


### public getEpochId
_(no internal calls)_


### public getEpochsByMarketId
_(no internal calls)_


### public getMarketId
_(no internal calls)_


### public getMarketInfo
_(no internal calls)_


### public getVaults
_(no internal calls)_


### public setTreasury
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public whitelistAddressOnMarket
_(no internal calls)_


### public whitelistController
_(no internal calls)_


---

## VaultFactoryV2Pausable

_File: VaultFactoryV2Pausable.sol_

### public changeController
_(no internal calls)_


### public changeOracle
_(no internal calls)_


### public changeTimelocker
_(no internal calls)_


### public createEpoch
-> internal _createEpoch
  -> public getEpochId
  -> internal _setEpoch


### external createNewMarket
-> internal _createNewMarket
  -> public getMarketId
  -> library VaultV2CreatorPausable.createPausableVaultV2
  -> library VaultV2CreatorPausable.MarketConfiguration


### public getEpochFee
_(no internal calls)_


### public getEpochId
_(no internal calls)_


### public getEpochsByMarketId
_(no internal calls)_


### public getMarketId
_(no internal calls)_


### public getMarketInfo
_(no internal calls)_


### public getVaults
_(no internal calls)_


### external pauseMarket
_(no internal calls)_


### public setTreasury
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public whitelistAddressOnMarket
_(no internal calls)_


### public whitelistController
_(no internal calls)_


---

## VaultV2

_File: VaultV2.sol_

### public changeController
_(no internal calls)_


### public deposit
_(no internal calls)_


### external depositETH
_(no internal calls)_


### public getAllEpochs
_(no internal calls)_


### public getEpochConfig
_(no internal calls)_


### public getEpochsLength
_(no internal calls)_


### public previewWithdraw
_(no internal calls)_


### external resolveEpoch
-> public totalAssets


### external sendTokens
-> public treasury


### external setClaimTVL
_(no internal calls)_


### external setCounterPartyVault
_(no internal calls)_


### external setEpoch
_(no internal calls)_


### public setEpochNull
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### public treasury
_(no internal calls)_


### public whiteListAddress
_(no internal calls)_


### external withdraw
-> public previewWithdraw


---

## VaultV2Pausable

_File: VaultV2Pausable.sol_

### public changeController
_(no internal calls)_


### public deposit
_(no internal calls)_


### external depositETH
_(no internal calls)_


### public getAllEpochs
_(no internal calls)_


### public getEpochConfig
_(no internal calls)_


### public getEpochsLength
_(no internal calls)_


### external pauseMarket
_(no internal calls)_


### public previewWithdraw
_(no internal calls)_


### external resolveEpoch
-> public totalAssets


### external sendTokens
-> public treasury


### external setClaimTVL
_(no internal calls)_


### external setCounterPartyVault
_(no internal calls)_


### external setEpoch
_(no internal calls)_


### public setEpochNull
_(no internal calls)_


### public totalAssets
_(no internal calls)_


### public treasury
_(no internal calls)_


### public whiteListAddress
_(no internal calls)_


### external withdraw
-> public previewWithdraw

