# Callpaths — FlatMoney

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ArbKeeperFee

_File: src/flattened-contracts/42161/ArbKeeperFee.42161.flattened.sol_

### external getConfig
_(no internal calls)_


### public getKeeperFee
-> external_callback ICommonErrors.PriceInvalid
-> external_callback ICommonErrors.PriceStale


### external setGasPriceOracle
-> external_callback ICommonErrors.ZeroAddress


### external setParameters
-> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.ZeroValue


### external setStalenessPeriod
-> external_callback ICommonErrors.ZeroValue


---

## ControllerBase

_File: src/flattened-contracts/42161/OptionsControllerModule.42161.flattened.sol_

### public accruedFunding
-> private _netFundingPerUnit
  -> public nextFundingEntry
    -> internal _unrecordedFunding
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
    -> public currentFundingRate
      -> internal _currentFundingRate
      -> internal _fundingChangeSinceRecomputed
        -> public currentFundingVelocity
          -> public getProportionalSkew
        -> private _proportionalElapsedTime


### public accruedFundingTotalByLongs
-> internal _accruedFundingTotalByLongs
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public currentFundingRate
-> internal _currentFundingRate
-> internal _fundingChangeSinceRecomputed
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime


### public currentFundingVelocity
-> public getProportionalSkew


### public fundingAdjustedLongPnLTotal
-> public profitLossTotal
-> public accruedFundingTotalByLongs
  -> internal _accruedFundingTotalByLongs
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime


### external getCurrentSkew
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public getProportionalSkew
_(no internal calls)_


### public nextFundingEntry
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public profitLoss
_(no internal calls)_


### public profitLossTotal
_(no internal calls)_


### external setMaxFundingVelocity
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs


### external setMaxVelocitySkew
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> private _setMaxVelocitySkew


### public setMinFundingRate
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### external setTargetSizeCollateralRatio
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> private _setTargetSizeCollateralRatio
  -> external_callback ICommonErrors.ZeroValue


### external setVault
-> external_callback ICommonErrors.ZeroAddress


### public settleFundingFees
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> internal _accruedFundingTotalByLongs


---

## DelayedOrder

_File: src/flattened-contracts/12345/DelayedOrder.12345.flattened.sol_

### external announceLeverageAdjust
-> internal _prepareAnnouncementOrder
  -> library FlatcoinErrors.InvalidFee
  -> public cancelExistingOrder
    -> library FlatcoinErrors.OrderHasNotExpired
    -> library FlatcoinEvents.OrderCancelled
-> library FlatcoinErrors.ZeroValue
-> library FlatcoinErrors.NotTokenOwner
-> library FlatcoinErrors.MaxFillPriceTooLow
-> library FlatcoinErrors.MinFillPriceTooHigh
-> library FlatcoinErrors.ValueNotPositive
-> library FlatcoinErrors.PositionCreatesBadDebt
-> library FlatcoinStructs.Order
-> library FlatcoinStructs.AnnouncedLeverageAdjust
-> library FlatcoinEvents.OrderAnnounced


### external announceLeverageClose
-> internal _prepareAnnouncementOrder
  -> library FlatcoinErrors.InvalidFee
  -> public cancelExistingOrder
    -> library FlatcoinErrors.OrderHasNotExpired
    -> library FlatcoinEvents.OrderCancelled
-> library FlatcoinErrors.NotTokenOwner
-> library FlatcoinErrors.NotEnoughMarginForFees
-> library FlatcoinErrors.MinFillPriceTooHigh
-> library FlatcoinStructs.Order
-> library FlatcoinStructs.AnnouncedLeverageClose
-> library FlatcoinEvents.OrderAnnounced


### external announceLeverageOpen
-> public announceLeverageOpenFor
  -> internal _prepareAnnouncementOrder
    -> library FlatcoinErrors.InvalidFee
    -> public cancelExistingOrder
      -> library FlatcoinErrors.OrderHasNotExpired
      -> library FlatcoinEvents.OrderCancelled
  -> library FlatcoinErrors.MaxFillPriceTooLow
  -> library FlatcoinErrors.PositionCreatesBadDebt
  -> library FlatcoinStructs.Order
  -> library FlatcoinStructs.AnnouncedLeverageOpen
  -> library FlatcoinEvents.OrderAnnounced


### public announceLeverageOpenFor
-> internal _prepareAnnouncementOrder
  -> library FlatcoinErrors.InvalidFee
  -> public cancelExistingOrder
    -> library FlatcoinErrors.OrderHasNotExpired
    -> library FlatcoinEvents.OrderCancelled
-> library FlatcoinErrors.MaxFillPriceTooLow
-> library FlatcoinErrors.PositionCreatesBadDebt
-> library FlatcoinStructs.Order
-> library FlatcoinStructs.AnnouncedLeverageOpen
-> library FlatcoinEvents.OrderAnnounced


### external announceStableDeposit
-> public announceStableDepositFor
  -> internal _prepareAnnouncementOrder
    -> library FlatcoinErrors.InvalidFee
    -> public cancelExistingOrder
      -> library FlatcoinErrors.OrderHasNotExpired
      -> library FlatcoinEvents.OrderCancelled
  -> library FlatcoinErrors.AmountTooSmall
  -> library FlatcoinErrors.HighSlippage
  -> library FlatcoinStructs.Order
  -> library FlatcoinStructs.AnnouncedStableDeposit
  -> library FlatcoinEvents.OrderAnnounced


### public announceStableDepositFor
-> internal _prepareAnnouncementOrder
  -> library FlatcoinErrors.InvalidFee
  -> public cancelExistingOrder
    -> library FlatcoinErrors.OrderHasNotExpired
    -> library FlatcoinEvents.OrderCancelled
-> library FlatcoinErrors.AmountTooSmall
-> library FlatcoinErrors.HighSlippage
-> library FlatcoinStructs.Order
-> library FlatcoinStructs.AnnouncedStableDeposit
-> library FlatcoinEvents.OrderAnnounced


### external announceStableWithdraw
-> internal _prepareAnnouncementOrder
  -> library FlatcoinErrors.InvalidFee
  -> public cancelExistingOrder
    -> library FlatcoinErrors.OrderHasNotExpired
    -> library FlatcoinEvents.OrderCancelled
-> library FlatcoinErrors.NotEnoughBalanceForWithdraw
-> library FlatcoinErrors.WithdrawalTooSmall
-> library FlatcoinErrors.HighSlippage
-> library FlatcoinStructs.Order
-> library FlatcoinStructs.AnnouncedStableWithdraw
-> library FlatcoinEvents.OrderAnnounced


### public cancelExistingOrder
-> library FlatcoinErrors.OrderHasNotExpired
-> library FlatcoinEvents.OrderCancelled


### external executeOrder
-> library FlatcoinErrors.DelayedOrderInvalid
-> internal _executeStableDeposit
  -> internal _prepareExecutionOrder
    -> library FlatcoinErrors.OrderHasExpired
    -> library FlatcoinErrors.ExecutableTimeNotReached
  -> library FlatcoinEvents.OrderExecuted
-> internal _executeStableWithdraw
  -> internal _prepareExecutionOrder
    -> library FlatcoinErrors.OrderHasExpired
    -> library FlatcoinErrors.ExecutableTimeNotReached
  -> library FlatcoinErrors.NotEnoughMarginForFees
  -> library FlatcoinErrors.HighSlippage
  -> library FlatcoinEvents.OrderExecuted
-> internal _executeLeverageOpen
  -> internal _prepareExecutionOrder
    -> library FlatcoinErrors.OrderHasExpired
    -> library FlatcoinErrors.ExecutableTimeNotReached
  -> library FlatcoinEvents.OrderExecuted
-> internal _executeLeverageClose
  -> internal _prepareExecutionOrder
    -> library FlatcoinErrors.OrderHasExpired
    -> library FlatcoinErrors.ExecutableTimeNotReached
  -> library FlatcoinEvents.OrderExecuted
-> internal _executeLeverageAdjust
  -> internal _prepareExecutionOrder
    -> library FlatcoinErrors.OrderHasExpired
    -> library FlatcoinErrors.ExecutableTimeNotReached
  -> library FlatcoinEvents.OrderExecuted


### external getAnnouncedOrder
_(no internal calls)_


### public hasOrderExpired
-> library FlatcoinErrors.ZeroValue


### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress
-> internal __ReentrancyGuard_init
  -> internal __ReentrancyGuard_init_unchained
    -> private _getReentrancyGuardStorage


### external setVault
-> external_callback ICommonErrors.ZeroAddress


---

## ERC165Upgradeable

_File: src/flattened-contracts/42161/LeverageModule.42161.flattened.sol_

### public supportsInterface
_(no internal calls)_


---

## ERC20LockableUpgradeable

_File: src/flattened-contracts/42161/StableModule.42161.flattened.sol_

### public allowance
-> private _getERC20Storage


### public approve
-> internal _approve
  -> private _getERC20Storage


### public balanceOf
-> private _getERC20Storage


### public decimals
_(no internal calls)_


### public name
-> private _getERC20Storage


### public symbol
-> private _getERC20Storage


### public totalSupply
-> private _getERC20Storage


### public transfer
-> internal _transfer
  -> internal _update
    -> public balanceOf
      -> private _getERC20Storage


### public transferFrom
-> internal _spendAllowance
  -> public allowance
    -> private _getERC20Storage
  -> internal _approve
    -> private _getERC20Storage
-> internal _transfer
  -> internal _update
    -> public balanceOf
      -> private _getERC20Storage


---

## ERC20Upgradeable

_File: src/flattened-contracts/42161/StableModule.42161.flattened.sol_

### public allowance
-> private _getERC20Storage


### public approve
-> internal _msgSender
-> internal _approve
  -> private _getERC20Storage


### public balanceOf
-> private _getERC20Storage


### public decimals
_(no internal calls)_


### public name
-> private _getERC20Storage


### public symbol
-> private _getERC20Storage


### public totalSupply
-> private _getERC20Storage


### public transfer
-> internal _msgSender
-> internal _transfer
  -> internal _update
    -> private _getERC20Storage


### public transferFrom
-> internal _msgSender
-> internal _spendAllowance
  -> public allowance
    -> private _getERC20Storage
  -> internal _approve
    -> private _getERC20Storage
-> internal _transfer
  -> internal _update
    -> private _getERC20Storage


---

## ERC721EnumerableUpgradeable

_File: src/flattened-contracts/42161/LeverageModule.42161.flattened.sol_

### public approve
-> internal _approve
  -> private _getERC721Storage
  -> internal _requireOwned
    -> internal _ownerOf
      -> private _getERC721Storage
  -> public isApprovedForAll
    -> private _getERC721Storage


### public balanceOf
-> private _getERC721Storage


### public getApproved
-> internal _requireOwned
  -> internal _ownerOf
    -> private _getERC721Storage
-> internal _getApproved
  -> private _getERC721Storage


### public isApprovedForAll
-> private _getERC721Storage


### public name
-> private _getERC721Storage


### public ownerOf
-> internal _requireOwned
  -> internal _ownerOf
    -> private _getERC721Storage


### public safeTransferFrom
-> public transferFrom
  -> internal _update
    -> private _addTokenToAllTokensEnumeration
      -> private _getERC721EnumerableStorage
    -> private _removeTokenFromOwnerEnumeration
      -> private _getERC721EnumerableStorage
      -> public balanceOf
        -> private _getERC721Storage
    -> private _removeTokenFromAllTokensEnumeration
      -> private _getERC721EnumerableStorage
    -> private _addTokenToOwnerEnumeration
      -> private _getERC721EnumerableStorage
      -> public balanceOf
        -> private _getERC721Storage
-> private _checkOnERC721Received


### public setApprovalForAll
-> internal _setApprovalForAll
  -> private _getERC721Storage


### public supportsInterface
_(no internal calls)_


### public symbol
-> private _getERC721Storage


### public tokenByIndex
-> private _getERC721EnumerableStorage
-> public totalSupply
  -> private _getERC721EnumerableStorage


### public tokenOfOwnerByIndex
-> private _getERC721EnumerableStorage
-> public balanceOf
  -> private _getERC721Storage


### public tokenURI
-> internal _requireOwned
  -> internal _ownerOf
    -> private _getERC721Storage
-> internal _baseURI


### public totalSupply
-> private _getERC721EnumerableStorage


### public transferFrom
-> internal _update
  -> private _addTokenToAllTokensEnumeration
    -> private _getERC721EnumerableStorage
  -> private _removeTokenFromOwnerEnumeration
    -> private _getERC721EnumerableStorage
    -> public balanceOf
      -> private _getERC721Storage
  -> private _removeTokenFromAllTokensEnumeration
    -> private _getERC721EnumerableStorage
  -> private _addTokenToOwnerEnumeration
    -> private _getERC721EnumerableStorage
    -> public balanceOf
      -> private _getERC721Storage


---

## ERC721LockableEnumerableUpgradeable

_File: src/flattened-contracts/12345/LeverageModule.12345.flattened.sol_

### public supportsInterface
_(no internal calls)_


### public tokenByIndex
-> private _getERC721EnumerableStorage
-> public totalSupply
  -> private _getERC721EnumerableStorage


### public tokenOfOwnerByIndex
-> private _getERC721EnumerableStorage


### public totalSupply
-> private _getERC721EnumerableStorage


---

## ERC721Upgradeable

_File: src/flattened-contracts/42161/LeverageModule.42161.flattened.sol_

### public approve
-> internal _approve
  -> private _getERC721Storage
  -> internal _requireOwned
    -> internal _ownerOf
      -> private _getERC721Storage
  -> public isApprovedForAll
    -> private _getERC721Storage
-> internal _msgSender


### public balanceOf
-> private _getERC721Storage


### public getApproved
-> internal _requireOwned
  -> internal _ownerOf
    -> private _getERC721Storage
-> internal _getApproved
  -> private _getERC721Storage


### public isApprovedForAll
-> private _getERC721Storage


### public name
-> private _getERC721Storage


### public ownerOf
-> internal _requireOwned
  -> internal _ownerOf
    -> private _getERC721Storage


### public safeTransferFrom
-> public transferFrom
  -> internal _update
    -> private _getERC721Storage
    -> internal _ownerOf
      -> private _getERC721Storage
    -> internal _checkAuthorized
      -> internal _isAuthorized
        -> public isApprovedForAll
          -> private _getERC721Storage
        -> internal _getApproved
          -> private _getERC721Storage
    -> internal _approve
      -> private _getERC721Storage
      -> internal _requireOwned
        -> internal _ownerOf
          -> private _getERC721Storage
      -> public isApprovedForAll
        -> private _getERC721Storage
  -> internal _msgSender
-> private _checkOnERC721Received
  -> internal _msgSender


### public setApprovalForAll
-> internal _setApprovalForAll
  -> private _getERC721Storage
-> internal _msgSender


### public supportsInterface
_(no internal calls)_


### public symbol
-> private _getERC721Storage


### public tokenURI
-> internal _requireOwned
  -> internal _ownerOf
    -> private _getERC721Storage
-> internal _baseURI


### public transferFrom
-> internal _update
  -> private _getERC721Storage
  -> internal _ownerOf
    -> private _getERC721Storage
  -> internal _checkAuthorized
    -> internal _isAuthorized
      -> public isApprovedForAll
        -> private _getERC721Storage
      -> internal _getApproved
        -> private _getERC721Storage
  -> internal _approve
    -> private _getERC721Storage
    -> internal _requireOwned
      -> internal _ownerOf
        -> private _getERC721Storage
    -> public isApprovedForAll
      -> private _getERC721Storage
-> internal _msgSender


---

## ETHCrossAggregator

_File: src/flattened-contracts/8453/ETHCrossAggregator.8453.flattened.sol_

### external decimals
_(no internal calls)_


### external latestRoundData
_(no internal calls)_


---

## FeeManager

_File: src/flattened-contracts/42161/OrderExecutionModule.42161.flattened.sol_

### external getProtocolFee
_(no internal calls)_


### external getTradeFee
_(no internal calls)_


### external getWithdrawalFee
_(no internal calls)_


### public owner
-> private _getOwnableStorage


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external setLeverageTradingFee
-> private _setLeverageTradingFee
  -> external_callback ICommonErrors.InvalidPercentageValue


### external setProtocolFeePercentage
-> private _setProtocolFeePercentage
  -> external_callback ICommonErrors.InvalidPercentageValue


### external setProtocolFeeRecipient
-> private _setProtocolFeeRecipient
  -> external_callback ICommonErrors.ZeroAddress


### external setStableWithdrawFee
-> private _setStableWithdrawFee
  -> external_callback ICommonErrors.InvalidPercentageValue


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


---

## FlatZapper

_File: src/flattened-contracts/42161/FlatZapper.42161.flattened.sol_

### public getCollateral
-> private _getFlatZapperStorage


### public getSwapper
-> private _getFlatZapperStorage


### public getVault
-> private _getFlatZapperStorage


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
    -> internal _transferOwnership
      -> private _getOwnableStorage
-> internal __FlatZapperStorage_init
  -> private _getFlatZapperStorage
-> internal __TokenTransferMethods_init
-> private _unlimitedApprove


### public owner
-> private _getOwnableStorage


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external rescueFunds
_(no internal calls)_


### external setCollateral
-> internal _setCollateral
  -> private _getFlatZapperStorage
-> private _unlimitedApprove
-> public getVault
  -> private _getFlatZapperStorage


### external setSwapper
-> internal _setSwapper
  -> private _getFlatZapperStorage


### external setVault
-> internal _setVault
  -> private _getFlatZapperStorage


### external setWrappedNativeToken
_(no internal calls)_


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external unlimitedApproveOrderAnnouncementModule
-> public getVault
  -> private _getFlatZapperStorage
-> private _unlimitedApprove
-> public getCollateral
  -> private _getFlatZapperStorage


### external zap
-> public getCollateral
  -> private _getFlatZapperStorage
-> internal _transferFromCaller
  -> internal _transferUsingSimpleAllowance
  -> internal _transferUsingPermit2
  -> internal _wrapNativeToken
-> internal _swap
  -> public getSwapper
    -> private _getFlatZapperStorage
  -> private _unlimitedApprove
-> internal _createOrder
  -> public getVault
    -> private _getFlatZapperStorage


---

## FlatZapperStorage

_File: src/flattened-contracts/42161/FlatZapper.42161.flattened.sol_

### public getCollateral
-> private _getFlatZapperStorage


### public getSwapper
-> private _getFlatZapperStorage


### public getVault
-> private _getFlatZapperStorage


---

## FlatcoinVault

_File: src/flattened-contracts/42161/FlatcoinVault.42161.flattened.sol_

### public addAuthorizedModule
-> external_callback ICommonErrors.ZeroAddress
-> external_callback ICommonErrors.ZeroValue


### external addAuthorizedModules
-> public addAuthorizedModule
  -> external_callback ICommonErrors.ZeroAddress
  -> external_callback ICommonErrors.ZeroValue


### public checkCollateralCap
_(no internal calls)_


### public checkGlobalMarginPositive
_(no internal calls)_


### public checkSkewMax
-> external_callback ICommonErrors.ZeroValue
-> external_callback ICommonErrors.MaxSkewReached


### external deletePosition
_(no internal calls)_


### external getGlobalPositions
_(no internal calls)_


### external getMaxPositionIds
_(no internal calls)_


### external getPosition
_(no internal calls)_


### external getProtocolFee
_(no internal calls)_


### external getTradeFee
_(no internal calls)_


### external getWithdrawalFee
_(no internal calls)_


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
    -> internal _transferOwnership
      -> private _getOwnableStorage
-> internal __FeeManager_init


### public isMaxPositionsReached
_(no internal calls)_


### public isPositionOpenWhitelisted
_(no internal calls)_


### public owner
-> private _getOwnableStorage


### external pauseModule
_(no internal calls)_


### external removeAuthorizedModule
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external sendCollateral
_(no internal calls)_


### external setLeverageTradingFee
-> private _setLeverageTradingFee
  -> external_callback ICommonErrors.InvalidPercentageValue


### external setMaxDeltaError
_(no internal calls)_


### external setMaxPositions
-> external_callback ICommonErrors.ZeroValue
-> external_callback ICommonErrors.MaxPositionsReached


### external setMaxPositionsWhitelist
_(no internal calls)_


### external setPosition
-> external_callback ICommonErrors.MaxPositionsReached


### external setProtocolFeePercentage
-> private _setProtocolFeePercentage
  -> external_callback ICommonErrors.InvalidPercentageValue


### external setProtocolFeeRecipient
-> private _setProtocolFeeRecipient
  -> external_callback ICommonErrors.ZeroAddress


### external setSkewFractionMax
_(no internal calls)_


### external setStableCollateralCap
_(no internal calls)_


### external setStableWithdrawFee
-> private _setStableWithdrawFee
  -> external_callback ICommonErrors.InvalidPercentageValue


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external unpauseModule
_(no internal calls)_


### external updateGlobalMargin
_(no internal calls)_


### external updateGlobalPositionData
_(no internal calls)_


### external updateStableCollateralTotal
-> private _updateStableCollateralTotal
  -> external_callback ICommonErrors.ValueNotPositive


---

## KeeperFee

_File: src/flattened-contracts/8453/KeeperFee.8453.flattened.sol_

### external getConfig
_(no internal calls)_


### public getKeeperFee
-> library FlatcoinErrors.ETHPriceStale
-> library FlatcoinErrors.ETHPriceInvalid
-> library FlatcoinErrors.PriceInvalid
-> library FlatcoinErrors.PriceStale


### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### external setGasPriceOracle
-> library FlatcoinErrors.ZeroAddress


### external setParameters
-> library FlatcoinErrors.InvalidFee
-> library FlatcoinErrors.ZeroValue


### external setStalenessPeriod
-> library FlatcoinErrors.ZeroValue


### public transferOwnership
-> internal _transferOwnership


---

## KeeperFeeBase

_File: src/flattened-contracts/42161/ArbKeeperFee.42161.flattened.sol_

### external getConfig
_(no internal calls)_


### public getKeeperFee
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### external setGasPriceOracle
-> external_callback ICommonErrors.ZeroAddress


### external setParameters
-> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.ZeroValue


### external setStalenessPeriod
-> external_callback ICommonErrors.ZeroValue


### public transferOwnership
-> internal _transferOwnership


---

## LeverageModule

_File: src/flattened-contracts/42161/LeverageModule.42161.flattened.sol_

### public burn
_(no internal calls)_


### public checkLeverageCriteria
_(no internal calls)_


### external executeAdjust
-> internal _getMaxAge
-> public getPositionSummary
-> external_callback ICommonErrors.ValueNotPositive
-> external_callback ICommonErrors.HighSlippage
-> public checkLeverageCriteria
-> external_callback ICommonErrors.PositionCreatesBadDebt


### external executeClose
-> internal _getMaxAge
-> external_callback ICommonErrors.HighSlippage
-> public getPositionSummary
-> external_callback ICommonErrors.ValueNotPositive
-> external_callback ICommonErrors.NotEnoughMarginForFees
-> public burn


### external executeOpen
-> internal _getMaxAge
-> external_callback ICommonErrors.HighSlippage
-> internal _mint
-> external_callback ICommonErrors.PositionCreatesBadDebt


### public getPositionSummary
_(no internal calls)_


### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress
-> private _setLeverageCriteria


### public mint
-> internal _mint


### external setLeverageCriteria
-> private _setLeverageCriteria


### external setVault
-> external_callback ICommonErrors.ZeroAddress


### public supportsInterface
_(no internal calls)_


### public tokenByIndex
-> private _getERC721EnumerableStorage
-> public totalSupply
  -> private _getERC721EnumerableStorage


### public tokenOfOwnerByIndex
-> private _getERC721EnumerableStorage


### public totalSupply
-> private _getERC721EnumerableStorage


---

## LimitOrder

_File: src/flattened-contracts/12345/LimitOrder.12345.flattened.sol_

### external announceLimitOrder
-> internal _prepareAnnouncementOrder
-> internal _checkPositionOwner
  -> library FlatcoinErrors.NotTokenOwner
-> internal _checkThresholds
  -> library FlatcoinErrors.InvalidThresholds
-> library FlatcoinStructs.Order
-> library FlatcoinStructs.LimitClose
-> library FlatcoinEvents.LimitOrderAnnounced


### external cancelExistingLimitOrder
-> library FlatcoinEvents.LimitOrderCancelled


### external cancelLimitOrder
-> internal _checkPositionOwner
  -> library FlatcoinErrors.NotTokenOwner
-> internal _checkLimitCloseOrder
  -> library FlatcoinErrors.LimitOrderInvalid
-> library FlatcoinEvents.LimitOrderCancelled


### external executeLimitOrder
-> internal _checkLimitCloseOrder
  -> library FlatcoinErrors.LimitOrderInvalid
-> internal _closePosition
  -> library FlatcoinErrors.ExecutableTimeNotReached
  -> library FlatcoinErrors.LimitOrderPriceNotInRange
  -> library FlatcoinStructs.AnnouncedLeverageClose
  -> library FlatcoinEvents.LimitOrderExecuted


### external getLimitOrder
_(no internal calls)_


### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress
-> internal __ReentrancyGuard_init
  -> internal __ReentrancyGuard_init_unchained
    -> private _getReentrancyGuardStorage


### external resetExecutionTime
_(no internal calls)_


### external setVault
-> external_callback ICommonErrors.ZeroAddress


---

## LiquidationModule

_File: src/flattened-contracts/42161/LiquidationModule.42161.flattened.sol_

### public canLiquidate
-> public getLiquidationMargin
  -> public getLiquidationFee


### public getLiquidationFee
_(no internal calls)_


### public getLiquidationMargin
-> public getLiquidationFee


### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress
-> internal __ReentrancyGuard_init
  -> internal __ReentrancyGuard_init_unchained
    -> private _getReentrancyGuardStorage
-> private _setLiquidationFeeRatio
  -> external_callback ICommonErrors.ZeroValue
-> private _setLiquidationBufferRatio
  -> external_callback ICommonErrors.ZeroValue
-> private _setLiquidationFeeBounds
  -> external_callback ICommonErrors.ZeroValue


### public liquidate
-> public canLiquidate
  -> public getLiquidationMargin
    -> public getLiquidationFee
-> private _processLiquidation
  -> public getLiquidationFee


### external setLiquidationBufferRatio
-> private _setLiquidationBufferRatio
  -> external_callback ICommonErrors.ZeroValue


### external setLiquidationFeeBounds
-> private _setLiquidationFeeBounds
  -> external_callback ICommonErrors.ZeroValue


### external setLiquidationFeeRatio
-> private _setLiquidationFeeRatio
  -> external_callback ICommonErrors.ZeroValue


### external setVault
-> external_callback ICommonErrors.ZeroAddress


---

## ModuleUpgradeable

_File: src/flattened-contracts/42161/OrderExecutionModule.42161.flattened.sol_

### external setVault
-> external_callback ICommonErrors.ZeroAddress


---

## OPKeeperFee

_File: src/flattened-contracts/10/OPKeeperFee.10.flattened.sol_

### external getConfig
_(no internal calls)_


### public getKeeperFee
-> external_callback ICommonErrors.PriceInvalid
-> external_callback ICommonErrors.PriceStale


### external setGasPriceOracle
-> external_callback ICommonErrors.ZeroAddress


### external setParameters
-> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.ZeroValue


### external setStalenessPeriod
-> external_callback ICommonErrors.ZeroValue


---

## OptionViewer

_File: src/flattened-contracts/42161/OptionViewer.42161.flattened.sol_

### external getAccountLeveragePositionData
-> public getPositionData
  -> public liquidationPrice


### external getFlatcoinPriceInUSD
_(no internal calls)_


### external getFlatcoinTVL
_(no internal calls)_


### external getMarketSkewPercentage
_(no internal calls)_


### public getMarketSummary
_(no internal calls)_


### public getPositionData
-> public liquidationPrice


### external getVaultSummary
_(no internal calls)_


### public liquidationPrice
_(no internal calls)_


---

## OptionsControllerModule

_File: src/flattened-contracts/42161/OptionsControllerModule.42161.flattened.sol_

### public accruedFunding
-> private _netFundingPerUnit
  -> public nextFundingEntry
    -> internal _unrecordedFunding
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
    -> public currentFundingRate
      -> internal _currentFundingRate
      -> internal _fundingChangeSinceRecomputed
        -> public currentFundingVelocity
          -> public getProportionalSkew
        -> private _proportionalElapsedTime


### public accruedFundingTotalByLongs
-> internal _accruedFundingTotalByLongs
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public currentFundingRate
-> internal _currentFundingRate
-> internal _fundingChangeSinceRecomputed
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime


### public currentFundingVelocity
-> public getProportionalSkew


### public fundingAdjustedLongPnLTotal
-> public profitLossTotal
  -> public profitLoss
-> public accruedFundingTotalByLongs
  -> internal _accruedFundingTotalByLongs
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime


### external getCurrentSkew
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public getProportionalSkew
_(no internal calls)_


### external initialize
-> internal __ControllerBase_init
  -> private _setMaxVelocitySkew
  -> private _setTargetSizeCollateralRatio
    -> external_callback ICommonErrors.ZeroValue


### public nextFundingEntry
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public profitLoss
_(no internal calls)_


### public profitLossTotal
-> public profitLoss


### external setMaxFundingVelocity
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs


### external setMaxVelocitySkew
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> private _setMaxVelocitySkew


### public setMinFundingRate
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### external setTargetSizeCollateralRatio
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> private _setTargetSizeCollateralRatio
  -> external_callback ICommonErrors.ZeroValue


### public settleFundingFees
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> internal _accruedFundingTotalByLongs


---

## OracleModule

_File: src/flattened-contracts/42161/OracleModule.42161.flattened.sol_

### external getOracleData
_(no internal calls)_


### public getPrice
-> internal _getPrice
  -> internal _getOnchainPrice
    -> external_callback ICommonErrors.ZeroAddress
    -> external_callback ICommonErrors.PriceStale
    -> external_callback ICommonErrors.PriceInvalid
  -> internal _getOffchainPrice
    -> external_callback ICommonErrors.ZeroAddress
  -> external_callback ICommonErrors.PriceStale


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
    -> internal _transferOwnership
      -> private _getOwnableStorage
-> internal __ReentrancyGuard_init
  -> internal __ReentrancyGuard_init_unchained
    -> private _getReentrancyGuardStorage


### public owner
-> private _getOwnableStorage


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external setMaxDiffPercent
-> private _setMaxDiffPercent


### external setOracles
-> internal _setOnchainOracle
-> internal _setOffchainOracle


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external updatePythPrice
_(no internal calls)_


---

## OrderAnnouncementModule

_File: src/flattened-contracts/42161/OrderAnnouncementModule.42161.flattened.sol_

### external addAuthorizedCaller
_(no internal calls)_


### external announceLeverageAdjust
-> internal _prepareAnnouncementOrder
  -> internal _preAnnouncementChores
  -> external_callback ICommonErrors.ZeroAddress
  -> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.ZeroValue
-> external_callback ICommonErrors.NotTokenOwner
-> external_callback ICommonErrors.ValueNotPositive
-> external_callback ICommonErrors.PositionCreatesBadDebt


### external announceLeverageClose
-> internal _prepareAnnouncementOrder
  -> internal _preAnnouncementChores
  -> external_callback ICommonErrors.ZeroAddress
  -> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.NotTokenOwner
-> external_callback ICommonErrors.NotEnoughMarginForFees


### external announceLeverageOpen
-> public announceLeverageOpenFor
  -> external_callback ICommonErrors.MaxPositionsReached
  -> internal _prepareAnnouncementOrder
    -> internal _preAnnouncementChores
    -> external_callback ICommonErrors.ZeroAddress
    -> external_callback ICommonErrors.InvalidFee
  -> external_callback ICommonErrors.PositionCreatesBadDebt


### public announceLeverageOpenFor
-> external_callback ICommonErrors.MaxPositionsReached
-> internal _prepareAnnouncementOrder
  -> internal _preAnnouncementChores
  -> external_callback ICommonErrors.ZeroAddress
  -> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.PositionCreatesBadDebt


### external announceLeverageOpenWithLimits
-> public announceLeverageOpenFor
  -> external_callback ICommonErrors.MaxPositionsReached
  -> internal _prepareAnnouncementOrder
    -> internal _preAnnouncementChores
    -> external_callback ICommonErrors.ZeroAddress
    -> external_callback ICommonErrors.InvalidFee
  -> external_callback ICommonErrors.PositionCreatesBadDebt


### external announceLimitOrder
-> external_callback ICommonErrors.NotTokenOwner
-> private _createLimitOrder
  -> internal _preAnnouncementChores


### external announceStableDeposit
-> public announceStableDepositFor
  -> internal _prepareAnnouncementOrder
    -> internal _preAnnouncementChores
    -> external_callback ICommonErrors.ZeroAddress
    -> external_callback ICommonErrors.InvalidFee
  -> external_callback ICommonErrors.AmountTooSmall
  -> external_callback ICommonErrors.HighSlippage


### public announceStableDepositFor
-> internal _prepareAnnouncementOrder
  -> internal _preAnnouncementChores
  -> external_callback ICommonErrors.ZeroAddress
  -> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.AmountTooSmall
-> external_callback ICommonErrors.HighSlippage


### external announceStableWithdraw
-> internal _prepareAnnouncementOrder
  -> internal _preAnnouncementChores
  -> external_callback ICommonErrors.ZeroAddress
  -> external_callback ICommonErrors.InvalidFee
-> external_callback ICommonErrors.HighSlippage


### external cancelLimitOrder
-> external_callback ICommonErrors.NotTokenOwner
-> private _deleteLimitOrder


### external createLimitOrder
-> private _createLimitOrder
  -> internal _preAnnouncementChores


### external deleteLimitOrder
-> private _deleteLimitOrder


### external deleteOrder
_(no internal calls)_


### external getAnnouncedOrder
_(no internal calls)_


### external getLimitOrder
_(no internal calls)_


### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress
-> private _setMinExecutabilityAge
  -> external_callback ICommonErrors.ZeroValue


### external removeAuthorizedCaller
_(no internal calls)_


### external resetExecutionTime
_(no internal calls)_


### external setMinExecutabilityAge
-> private _setMinExecutabilityAge
  -> external_callback ICommonErrors.ZeroValue


### external setVault
-> external_callback ICommonErrors.ZeroAddress


### external setminDepositAmountUSD
_(no internal calls)_


---

## OrderExecutionModule

_File: src/flattened-contracts/42161/OrderExecutionModule.42161.flattened.sol_

### external cancelExistingOrder
-> private _getAnnouncedOrder
-> internal _cancelOrder


### external cancelOrderByModule
-> internal _cancelOrder
-> private _getAnnouncedOrder


### external executeLimitOrder
-> internal _validateAndModifyLimitCloseOrder
  -> external_callback ICommonErrors.ExecutableTimeNotReached
-> internal _executeLeverageClose


### external executeOrder
-> private _getAnnouncedOrder
-> internal _prepareExecutionOrder
  -> external_callback ICommonErrors.ExecutableTimeNotReached
-> internal _executeStableDeposit
-> internal _executeStableWithdraw
  -> external_callback ICommonErrors.NotEnoughMarginForFees
  -> external_callback ICommonErrors.HighSlippage
-> internal _executeLeverageOpen
-> internal _executeLeverageClose
-> internal _executeLeverageAdjust


### public hasOrderExpired
-> private _getAnnouncedOrder
-> external_callback ICommonErrors.ZeroValue


### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress
-> internal __ReentrancyGuard_init
  -> internal __ReentrancyGuard_init_unchained
    -> private _getReentrancyGuardStorage
-> private _setMaxExecutabilityAge
  -> external_callback ICommonErrors.ZeroValue


### external setMaxExecutabilityAge
-> private _setMaxExecutabilityAge
  -> external_callback ICommonErrors.ZeroValue


### external setVault
-> external_callback ICommonErrors.ZeroAddress


---

## Ownable

_File: src/flattened-contracts/42161/ArbKeeperFee.42161.flattened.sol_

### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


---

## OwnableUpgradeable

_File: src/flattened-contracts/42161/OracleModule.42161.flattened.sol_

### public owner
-> private _getOwnableStorage


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


---

## PerpControllerModule

_File: src/flattened-contracts/10/PerpControllerModule.10.flattened.sol_

### public accruedFunding
-> private _netFundingPerUnit
  -> public nextFundingEntry
    -> internal _unrecordedFunding
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
    -> public currentFundingRate
      -> internal _currentFundingRate
      -> internal _fundingChangeSinceRecomputed
        -> public currentFundingVelocity
          -> public getProportionalSkew
        -> private _proportionalElapsedTime


### public accruedFundingTotalByLongs
-> internal _accruedFundingTotalByLongs
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public currentFundingRate
-> internal _currentFundingRate
-> internal _fundingChangeSinceRecomputed
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime


### public currentFundingVelocity
-> public getProportionalSkew


### public fundingAdjustedLongPnLTotal
-> public profitLossTotal
-> public accruedFundingTotalByLongs
  -> internal _accruedFundingTotalByLongs
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime


### external getCurrentSkew
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public getProportionalSkew
_(no internal calls)_


### external initialize
-> internal __ControllerBase_init
  -> private _setMaxVelocitySkew
  -> private _setTargetSizeCollateralRatio
    -> external_callback ICommonErrors.ZeroValue


### public nextFundingEntry
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### public profitLoss
_(no internal calls)_


### public profitLossTotal
_(no internal calls)_


### external setMaxFundingVelocity
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs


### external setMaxVelocitySkew
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> private _setMaxVelocitySkew


### public setMinFundingRate
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime


### external setTargetSizeCollateralRatio
-> public settleFundingFees
  -> public currentFundingRate
    -> internal _currentFundingRate
    -> internal _fundingChangeSinceRecomputed
      -> public currentFundingVelocity
        -> public getProportionalSkew
      -> private _proportionalElapsedTime
  -> internal _unrecordedFunding
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
  -> internal _accruedFundingTotalByLongs
-> private _setTargetSizeCollateralRatio
  -> external_callback ICommonErrors.ZeroValue


### public settleFundingFees
-> public currentFundingRate
  -> internal _currentFundingRate
  -> internal _fundingChangeSinceRecomputed
    -> public currentFundingVelocity
      -> public getProportionalSkew
    -> private _proportionalElapsedTime
-> internal _unrecordedFunding
  -> public currentFundingVelocity
    -> public getProportionalSkew
  -> private _proportionalElapsedTime
-> internal _accruedFundingTotalByLongs


---

## PerpViewer

_File: src/flattened-contracts/10/PerpViewer.10.flattened.sol_

### external getAccountLeveragePositionData
-> public getPositionData
  -> public liquidationPrice
    -> internal _calcLiquidationPrice


### external getFlatcoinPriceInUSD
_(no internal calls)_


### external getFlatcoinTVL
_(no internal calls)_


### external getMarketSkewPercentage
_(no internal calls)_


### public getMarketSummary
_(no internal calls)_


### public getPositionData
-> public liquidationPrice
  -> internal _calcLiquidationPrice


### external getVaultSummary
_(no internal calls)_


### public liquidationPrice
-> internal _calcLiquidationPrice


---

## PointsModule

_File: src/flattened-contracts/12345/PointsModule.12345.flattened.sol_

### public getAccumulatedMint
_(no internal calls)_


### public getAvailableMint
-> public getAccumulatedMint


### public getUnlockTax
_(no internal calls)_


### external initialize
-> library FlatcoinErrors.ZeroAddress
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress
-> public setTreasury
  -> library FlatcoinErrors.ZeroAddress
-> public setPointsVest
  -> library FlatcoinErrors.MaxVarianceExceeded
  -> library FlatcoinErrors.ZeroValue
-> public setPointsMint
-> public setMintRate


### public lockedBalance
_(no internal calls)_


### external mintDeposit
-> internal _updateAccumulatedMint
  -> public getAccumulatedMint
  -> public getAvailableMint
    -> public getAccumulatedMint
-> internal _mintTo
  -> internal _unlock
    -> public getUnlockTax
    -> internal _unlock
  -> internal _lock
  -> internal _setMintUnlockTime


### external mintLeverageOpen
-> internal _updateAccumulatedMint
  -> public getAccumulatedMint
  -> public getAvailableMint
    -> public getAccumulatedMint
-> internal _mintTo
  -> internal _unlock
    -> public getUnlockTax
    -> internal _unlock
  -> internal _lock
  -> internal _setMintUnlockTime


### external mintTo
-> internal _mintTo
  -> internal _unlock
    -> public getUnlockTax
    -> internal _unlock
  -> internal _lock
  -> internal _setMintUnlockTime


### external mintToMultiple
-> internal _mintTo
  -> internal _unlock
    -> public getUnlockTax
    -> internal _unlock
  -> internal _lock
  -> internal _setMintUnlockTime


### public setMintRate
_(no internal calls)_


### public setPointsMint
_(no internal calls)_


### public setPointsVest
-> library FlatcoinErrors.MaxVarianceExceeded
-> library FlatcoinErrors.ZeroValue


### public setTreasury
-> library FlatcoinErrors.ZeroAddress


### external setVault
-> external_callback ICommonErrors.ZeroAddress


### public unlock
-> internal _unlock
  -> public getUnlockTax
  -> internal _unlock


### public unlockAll
-> internal _unlock
  -> public getUnlockTax
  -> internal _unlock


---

## PositionSplitterModule

_File: src/PositionSplitterModule.sol_

### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress


### external setVault
-> external_callback ICommonErrors.ZeroAddress


### external split
-> external_callback ICommonErrors.OrderExists


---

## RouterProcessor

_File: src/flattened-contracts/42161/Swapper.42161.flattened.sol_

### public getRouter
-> private _getRouterProcessorStorage


---

## RouterProcessorStorage

_File: src/flattened-contracts/42161/Swapper.42161.flattened.sol_

### public getRouter
-> private _getRouterProcessorStorage


---

## StableModule

_File: src/flattened-contracts/42161/StableModule.42161.flattened.sol_

### external executeDeposit
-> internal _getMaxAge
-> public stableCollateralPerShare
  -> public stableCollateralTotalAfterSettlement
-> external_callback ICommonErrors.HighSlippage
-> external_callback ICommonErrors.AmountTooSmall


### external executeWithdraw
-> internal _getMaxAge
-> public stableCollateralPerShare
  -> public stableCollateralTotalAfterSettlement
-> internal _unlock
-> external_callback ICommonErrors.MaxSkewReached


### public getLockedAmount
_(no internal calls)_


### external initialize
-> internal __Module_init
  -> external_callback ICommonErrors.ZeroAddress


### external lock
-> internal _lock


### external setVault
-> external_callback ICommonErrors.ZeroAddress


### public stableCollateralPerShare
-> public stableCollateralTotalAfterSettlement


### public stableCollateralTotalAfterSettlement
_(no internal calls)_


### public stableDepositQuote
-> public stableCollateralPerShare
  -> public stableCollateralTotalAfterSettlement


### public stableWithdrawQuote
-> public stableCollateralPerShare
  -> public stableCollateralTotalAfterSettlement


### external unlock
-> internal _unlock


---

## Swapper

_File: src/flattened-contracts/42161/Swapper.42161.flattened.sol_

### external addRouter
_(no internal calls)_


### external initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
    -> internal _transferOwnership
      -> private _getOwnableStorage
-> internal __TokenTransferMethods_init


### public owner
-> private _getOwnableStorage


### external removeRouter
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### external rescueFunds
_(no internal calls)_


### external setWrappedNativeToken
_(no internal calls)_


### external swap
-> internal _transferFromCaller
  -> internal _transferUsingSimpleAllowance
  -> internal _transferUsingPermit2
  -> internal _wrapNativeToken
-> internal _processSwap
  -> private _preParaswap
  -> private _approveAndCallRouter


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


---

## TokenTransferMethods

_File: src/flattened-contracts/42161/Swapper.42161.flattened.sol_

### public getPermit2Address
-> private _getTokenTransferMethodsStorage


### public getWrappedNativeToken
-> private _getTokenTransferMethodsStorage


---

## TokenTransferMethodsStorage

_File: src/flattened-contracts/42161/Swapper.42161.flattened.sol_

### public getPermit2Address
-> private _getTokenTransferMethodsStorage


### public getWrappedNativeToken
-> private _getTokenTransferMethodsStorage


---

## Viewer

_File: src/flattened-contracts/84532/Viewer.84532.flattened.sol_

### external getAccountLeveragePositionData
-> public getPositionData
  -> library FlatcoinStructs.LeveragePositionData


### external getFlatcoinPriceInUSD
_(no internal calls)_


### external getFlatcoinTVL
_(no internal calls)_


### external getMarketSkewPercentage
_(no internal calls)_


### public getPositionData
-> library FlatcoinStructs.LeveragePositionData


---

## ViewerBase

_File: src/flattened-contracts/42161/OptionViewer.42161.flattened.sol_

### external getAccountLeveragePositionData
-> public getPositionData
  -> public liquidationPrice
    -> internal _calcLiquidationPrice


### external getFlatcoinPriceInUSD
_(no internal calls)_


### external getFlatcoinTVL
_(no internal calls)_


### external getMarketSkewPercentage
_(no internal calls)_


### public getMarketSummary
_(no internal calls)_


### public getPositionData
-> public liquidationPrice
  -> internal _calcLiquidationPrice


### external getVaultSummary
_(no internal calls)_


### public liquidationPrice
-> internal _calcLiquidationPrice

