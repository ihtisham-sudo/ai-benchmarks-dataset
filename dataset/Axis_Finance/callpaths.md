# Callpaths — Axis_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AtomicAuctionHouse

_File: src/AtomicAuctionHouse.sol_

### external auction
-> library Callbacks.isValidCallbacksAddress
-> internal _auction
-> internal _onCreateCallback
  -> library Callbacks.onCreate


### external cancel
-> internal _isLotValid
-> internal _getAuctionModuleForId
-> internal _cancel
-> library Callbacks.onCancel


### external curate
-> internal _isLotValid
-> internal _getAuctionModuleForId
-> internal _curate
-> library Callbacks.onCurate


### external getAuctionModuleForId
-> internal _isLotValid
-> internal _getAuctionModuleForId


### external getDerivativeModuleForId
-> internal _isLotValid
-> internal _getDerivativeModuleForId


### external multiPurchase
-> internal _purchase
  -> internal _isLotValid
  -> internal _allocateQuoteFees
  -> internal _getAuctionModuleForId
  -> internal _collectPayment
  -> internal _sendPayment
  -> library Callbacks.hasPermission
  -> library Callbacks.onPurchase
  -> internal _sendPayout


### external purchase
-> internal _purchase
  -> internal _isLotValid
  -> internal _allocateQuoteFees
  -> internal _getAuctionModuleForId
  -> internal _collectPayment
  -> internal _sendPayment
  -> library Callbacks.hasPermission
  -> library Callbacks.onPurchase
  -> internal _sendPayout


### external setCondenser
_(no internal calls)_


### external setFee
_(no internal calls)_


### external setProtocol
_(no internal calls)_


---

## AtomicAuctionModule

_File: src/modules/auctions/AtomicAuctionModule.sol_

### public TYPE
_(no internal calls)_


### external auction
_(no internal calls)_


### external auctionType
_(no internal calls)_


### external cancelAuction
-> internal _revertIfLotInvalid
-> internal _revertIfLotConcluded


### external capacityInQuote
_(no internal calls)_


### external getLot
_(no internal calls)_


### public hasEnded
_(no internal calls)_


### public isLive
_(no internal calls)_


### public isUpcoming
_(no internal calls)_


### external purchase
-> internal _revertIfLotInvalid
-> internal _revertIfLotInactive
  -> public isLive


### external remainingCapacity
_(no internal calls)_


### external setMinAuctionDuration
_(no internal calls)_


---

## AtomicCatalogue

_File: src/AtomicCatalogue.sol_

### external getAuctionsByBaseToken
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByCurator
-> internal _validateRange
  -> public getMaxLotId
-> public getFeeData
  -> external_callback IAuctionHouse.FeeData


### external getAuctionsByDerivative
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByFormat
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByModule
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByQuoteToken
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByRequestedCurator
-> internal _validateRange
  -> public getMaxLotId
-> public getFeeData
  -> external_callback IAuctionHouse.FeeData


### external getAuctionsBySeller
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### public getFeeData
-> external_callback IAuctionHouse.FeeData


### external getLiveAuctions
-> internal _validateRange
  -> public getMaxLotId
-> public isLive


### public getMaxLotId
_(no internal calls)_


### public getRouting
-> external_callback IAuctionHouse.Routing


### external getUpcomingAuctions
-> internal _validateRange
  -> public getMaxLotId
-> public isUpcoming


### external hasEnded
_(no internal calls)_


### public isLive
_(no internal calls)_


### public isUpcoming
_(no internal calls)_


### external maxAmountAccepted
-> internal _withFee


### external maxPayout
_(no internal calls)_


### external payoutFor
_(no internal calls)_


### external priceFor
-> internal _withFee


### external remainingCapacity
_(no internal calls)_


---

## AuctionHouse

_File: src/bases/AuctionHouse.sol_

### external auction
-> internal _getLatestModuleIfActive
-> internal _getModuleIfInstalled
-> library Callbacks.isValidCallbacksAddress
-> internal _onCreateCallback
  -> library Callbacks.onCreate


### public calculateQuoteFees
_(no internal calls)_


### external cancel
-> internal _isLotValid
-> internal _getAuctionModuleForId
  -> internal _getModuleIfInstalled
-> library Callbacks.onCancel


### external claimRewards
_(no internal calls)_


### external curate
-> internal _isLotValid
-> internal _getAuctionModuleForId
  -> internal _getModuleIfInstalled
-> internal _calculatePayoutFees
-> library Callbacks.onCurate


### external execOnModule
-> internal _getModuleIfInstalled


### external getAuctionModuleForId
-> internal _isLotValid
-> internal _getAuctionModuleForId
  -> internal _getModuleIfInstalled


### external getCuratorFee
_(no internal calls)_


### external getDerivativeModuleForId
-> internal _isLotValid
-> internal _getDerivativeModuleForId
  -> internal _getModuleIfInstalled


### external getFees
_(no internal calls)_


### public getProtocol
_(no internal calls)_


### external getRewards
_(no internal calls)_


### external installModule
-> internal _ensureContract


### external setCondenser
-> internal _getModuleIfInstalled


### external setCuratorFee
_(no internal calls)_


### external setFee
_(no internal calls)_


### external setProtocol
_(no internal calls)_


### external sunsetModule
-> internal _moduleIsInstalled


---

## AuctionModule

_File: src/modules/Auction.sol_

### external INIT
_(no internal calls)_


### public TYPE
_(no internal calls)_


### public VEECODE
_(no internal calls)_


### external auction
_(no internal calls)_


### external cancelAuction
-> internal _revertIfLotInvalid
-> internal _revertIfLotConcluded


### external capacityInQuote
_(no internal calls)_


### external getLot
_(no internal calls)_


### public hasEnded
_(no internal calls)_


### public isLive
_(no internal calls)_


### public isUpcoming
_(no internal calls)_


### external remainingCapacity
_(no internal calls)_


### external setMinAuctionDuration
_(no internal calls)_


---

## BaseCallback

_File: src/bases/BaseCallback.sol_

### external onBid
_(no internal calls)_


### external onCancel
_(no internal calls)_


### external onCreate
_(no internal calls)_


### external onCurate
_(no internal calls)_


### external onPurchase
_(no internal calls)_


### external onSettle
_(no internal calls)_


---

## BatchAuctionHouse

_File: src/BatchAuctionHouse.sol_

### external abort
-> internal _isLotValid
-> public getBatchModuleForId
  -> internal _getAuctionModuleForId
-> internal _getAddressGivenCallbackBaseTokenFlag


### external auction
-> library Callbacks.isValidCallbacksAddress
-> internal _auction
  -> internal _onCreateCallback
    -> library Callbacks.onCreate
-> internal _onCreateCallback
  -> library Callbacks.onCreate


### external bid
-> internal _isLotValid
-> public getBatchModuleForId
  -> internal _getAuctionModuleForId
-> internal _collectPayment
-> library Callbacks.onBid


### external cancel
-> internal _isLotValid
-> internal _getAuctionModuleForId
-> internal _cancel
  -> internal _getAddressGivenCallbackBaseTokenFlag
  -> library Callbacks.onCancel
-> library Callbacks.onCancel


### external claimBids
-> internal _isLotValid
-> public getBatchModuleForId
  -> internal _getAuctionModuleForId
-> internal _allocateQuoteFees
-> internal _sendPayout


### external curate
-> internal _isLotValid
-> internal _getAuctionModuleForId
-> internal _curate
  -> library Callbacks.hasPermission
  -> library Callbacks.onCurate
-> library Callbacks.onCurate


### external getAuctionModuleForId
-> internal _isLotValid
-> internal _getAuctionModuleForId


### public getBatchModuleForId
-> internal _getAuctionModuleForId


### external getDerivativeModuleForId
-> internal _isLotValid
-> internal _getDerivativeModuleForId


### external refundBid
-> internal _isLotValid
-> public getBatchModuleForId
  -> internal _getAuctionModuleForId


### external setCondenser
_(no internal calls)_


### external setFee
_(no internal calls)_


### external setProtocol
_(no internal calls)_


### external settle
-> internal _isLotValid
-> public getBatchModuleForId
  -> internal _getAuctionModuleForId
-> internal _sendPayment
-> internal _sendPayout
-> internal _getAddressGivenCallbackBaseTokenFlag
-> library Callbacks.onSettle


---

## BatchAuctionModule

_File: src/modules/auctions/BatchAuctionModule.sol_

### public TYPE
_(no internal calls)_


### external abort
-> internal _revertIfLotInvalid
-> internal _revertIfBeforeLotConcluded
-> internal _revertIfDedicatedSettlePeriod


### external auction
_(no internal calls)_


### external auctionType
_(no internal calls)_


### external bid
-> internal _revertIfLotInvalid
-> internal _revertIfBeforeLotStart
-> internal _revertIfLotConcluded


### external cancelAuction
-> internal _revertIfLotInvalid
-> internal _revertIfLotConcluded


### external capacityInQuote
_(no internal calls)_


### external claimBids
-> internal _revertIfLotInvalid


### external getLot
_(no internal calls)_


### public hasEnded
_(no internal calls)_


### public isLive
_(no internal calls)_


### public isUpcoming
_(no internal calls)_


### external refundBid
-> internal _revertIfLotInvalid
-> internal _revertIfBeforeLotStart
-> internal _revertIfLotConcluded


### external remainingCapacity
_(no internal calls)_


### external setDedicatedSettlePeriod
_(no internal calls)_


### external setMinAuctionDuration
_(no internal calls)_


### external settle
-> internal _revertIfLotInvalid
-> internal _revertIfBeforeLotStart
-> internal _revertIfLotActive
  -> public isLive


---

## BatchCatalogue

_File: src/BatchCatalogue.sol_

### external getAuctionsByBaseToken
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByCurator
-> internal _validateRange
  -> public getMaxLotId
-> public getFeeData
  -> external_callback IAuctionHouse.FeeData


### external getAuctionsByDerivative
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByFormat
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByModule
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByQuoteToken
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByRequestedCurator
-> internal _validateRange
  -> public getMaxLotId
-> public getFeeData
  -> external_callback IAuctionHouse.FeeData


### external getAuctionsBySeller
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getBidClaim
_(no internal calls)_


### external getBidIdAtIndex
_(no internal calls)_


### external getBidIds
_(no internal calls)_


### public getFeeData
-> external_callback IAuctionHouse.FeeData


### external getLiveAuctions
-> internal _validateRange
  -> public getMaxLotId
-> public isLive


### public getMaxLotId
_(no internal calls)_


### external getNumBids
_(no internal calls)_


### public getRouting
-> external_callback IAuctionHouse.Routing


### external getUpcomingAuctions
-> internal _validateRange
  -> public getMaxLotId
-> public isUpcoming


### external hasEnded
_(no internal calls)_


### public isLive
_(no internal calls)_


### public isUpcoming
_(no internal calls)_


### external remainingCapacity
_(no internal calls)_


---

## BlastAtomicAuctionHouse

_File: src/blast/BlastAtomicAuctionHouse.sol_

### external claimModuleGas
_(no internal calls)_


### external claimYieldAndGas
_(no internal calls)_


### external multiPurchase
-> internal _purchase
  -> library Callbacks.hasPermission
  -> library Callbacks.onPurchase


### external purchase
-> internal _purchase
  -> library Callbacks.hasPermission
  -> library Callbacks.onPurchase


---

## BlastAuctionHouse

_File: src/blast/BlastAuctionHouse.sol_

### external auction
-> library Callbacks.isValidCallbacksAddress
-> internal _onCreateCallback
  -> library Callbacks.onCreate


### external cancel
-> internal _isLotValid
-> internal _getAuctionModuleForId
-> library Callbacks.onCancel


### external claimModuleGas
_(no internal calls)_


### external claimYieldAndGas
_(no internal calls)_


### external curate
-> internal _isLotValid
-> internal _getAuctionModuleForId
-> library Callbacks.onCurate


### external getAuctionModuleForId
-> internal _isLotValid
-> internal _getAuctionModuleForId


### external getDerivativeModuleForId
-> internal _isLotValid
-> internal _getDerivativeModuleForId


### external setCondenser
_(no internal calls)_


### external setFee
_(no internal calls)_


### external setProtocol
_(no internal calls)_


---

## BlastBatchAuctionHouse

_File: src/blast/BlastBatchAuctionHouse.sol_

### external abort
-> public getBatchModuleForId


### external bid
-> public getBatchModuleForId
-> library Callbacks.onBid


### external claimBids
-> public getBatchModuleForId


### external claimModuleGas
_(no internal calls)_


### external claimYieldAndGas
_(no internal calls)_


### public getBatchModuleForId
_(no internal calls)_


### external refundBid
-> public getBatchModuleForId


### external settle
-> public getBatchModuleForId
-> library Callbacks.onSettle


---

## BlastEMP

_File: src/blast/modules/auctions/batch/BlastEMP.sol_

### public VEECODE
_(no internal calls)_


### external decryptAndSortBids
-> internal _revertIfLotActive
-> internal _decryptAndSortBids
  -> internal _decrypt
    -> public decryptBid


### public decryptBid
_(no internal calls)_


### external getAuctionData
_(no internal calls)_


### external getBid
-> internal _revertIfBidInvalid


### external getBidClaim
-> internal _revertIfLotNotSettled
-> internal _revertIfBidInvalid
-> internal _getBidClaim


### external getBidIdAtIndex
_(no internal calls)_


### external getBidIds
_(no internal calls)_


### external getNextInQueue
_(no internal calls)_


### external getNumBids
_(no internal calls)_


### external getNumBidsInQueue
_(no internal calls)_


### external getPartialFill
-> internal _revertIfLotNotSettled


### external refundBid
-> internal _revertIfBidInvalid
-> internal _revertIfNotBidOwner
-> internal _revertIfBidClaimed
-> internal _revertIfKeySubmitted
-> internal _revertIfLotSettled
-> internal _refundBid


### external submitPrivateKey
-> internal _revertIfLotActive
-> internal _revertIfLotSettled
-> internal _decryptAndSortBids
  -> internal _decrypt
    -> public decryptBid


---

## BlastFPB

_File: src/blast/modules/auctions/batch/BlastFPB.sol_

### public VEECODE
_(no internal calls)_


### external getAuctionData
_(no internal calls)_


### external getBid
-> internal _revertIfBidInvalid


### external getBidClaim
-> internal _revertIfLotNotSettled
-> internal _revertIfBidInvalid
-> internal _getBidClaim


### external getBidIdAtIndex
_(no internal calls)_


### external getBidIds
_(no internal calls)_


### external getNumBids
_(no internal calls)_


### external getPartialFill
-> internal _revertIfLotNotSettled


---

## BlastFPS

_File: src/blast/modules/auctions/atomic/BlastFPS.sol_

### public VEECODE
_(no internal calls)_


### public maxAmountAccepted
_(no internal calls)_


### public maxPayout
_(no internal calls)_


### public payoutFor
_(no internal calls)_


### public priceFor
_(no internal calls)_


---

## BlastLinearVesting

_File: src/blast/modules/derivatives/BlastLinearVesting.sol_

### public TYPE
_(no internal calls)_


### public VEECODE
_(no internal calls)_


### public approve
_(no internal calls)_


### external computeId
-> internal _decodeVestingParams
-> internal _computeId
  -> public VEECODE


### public decimals
-> internal _getTokenMetadata


### external deploy
-> internal _decodeVestingParams
-> internal _validate
-> internal _deployIfNeeded
  -> internal _computeId
    -> public VEECODE
  -> internal _deployWrapIfNeeded
    -> internal _computeNameAndSymbol


### external exercise
-> external_callback IDerivative.Derivative_NotImplemented


### external exerciseCost
_(no internal calls)_


### external getTokenVestingParams
_(no internal calls)_


### external mint
-> internal _mintDeployed
  -> internal _deployWrapIfNeeded
    -> internal _computeNameAndSymbol


### public name
-> internal _getTokenMetadata
-> internal _computeNameAndSymbol


### external reclaim
-> external_callback IDerivative.Derivative_NotImplemented


### external redeem
-> public redeemable
-> internal _redeem


### external redeemMax
-> public redeemable
-> internal _redeem


### public redeemable
_(no internal calls)_


### public symbol
-> internal _getTokenMetadata
-> internal _computeNameAndSymbol


### public tokenURI
-> internal _getTokenMetadata


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external transform
-> external_callback IDerivative.Derivative_NotImplemented


### external unwrap
_(no internal calls)_


### public validate
-> internal _decodeVestingParams
-> internal _validate


### external wrap
-> internal _deployWrapIfNeeded
  -> internal _computeNameAndSymbol


---

## Catalogue

_File: src/bases/Catalogue.sol_

### external getAuctionsByBaseToken
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByCurator
-> internal _validateRange
  -> public getMaxLotId
-> public getFeeData
  -> external_callback IAuctionHouse.FeeData


### external getAuctionsByDerivative
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByFormat
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByModule
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByQuoteToken
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### external getAuctionsByRequestedCurator
-> internal _validateRange
  -> public getMaxLotId
-> public getFeeData
  -> external_callback IAuctionHouse.FeeData


### external getAuctionsBySeller
-> internal _validateRange
  -> public getMaxLotId
-> public getRouting
  -> external_callback IAuctionHouse.Routing


### public getFeeData
-> external_callback IAuctionHouse.FeeData


### external getLiveAuctions
-> internal _validateRange
  -> public getMaxLotId
-> public isLive


### public getMaxLotId
_(no internal calls)_


### public getRouting
-> external_callback IAuctionHouse.Routing


### external getUpcomingAuctions
-> internal _validateRange
  -> public getMaxLotId
-> public isUpcoming


### external hasEnded
_(no internal calls)_


### public isLive
_(no internal calls)_


### public isUpcoming
_(no internal calls)_


### external remainingCapacity
_(no internal calls)_


---

## CondenserModule

_File: src/modules/Condenser.sol_

### external INIT
_(no internal calls)_


### public TYPE
_(no internal calls)_


### public VEECODE
_(no internal calls)_


---

## DerivativeModule

_File: src/modules/Derivative.sol_

### external INIT
_(no internal calls)_


### public TYPE
_(no internal calls)_


### public VEECODE
_(no internal calls)_


### external getTokenMetadata
_(no internal calls)_


### public totalSupply
_(no internal calls)_


---

## EncryptedMarginalPrice

_File: src/modules/auctions/batch/EMP.sol_

### public VEECODE
_(no internal calls)_


### external abort
-> internal _revertIfDedicatedSettlePeriod
-> internal _revertIfLotSettled
-> internal _abort


### external auctionType
_(no internal calls)_


### external bid
-> internal _revertIfLotSettled
-> internal _bid


### external claimBids
-> internal _revertIfLotNotSettled
-> internal _claimBids
  -> internal _revertIfBidInvalid
  -> internal _revertIfBidClaimed
  -> internal _claimBid
    -> internal _getBidClaim


### external decryptAndSortBids
-> internal _revertIfLotActive
-> internal _decryptAndSortBids
  -> internal _decrypt
    -> public decryptBid


### public decryptBid
_(no internal calls)_


### external getAuctionData
_(no internal calls)_


### external getBid
-> internal _revertIfBidInvalid


### external getBidClaim
-> internal _revertIfLotNotSettled
-> internal _revertIfBidInvalid
-> internal _getBidClaim


### external getBidIdAtIndex
_(no internal calls)_


### external getBidIds
_(no internal calls)_


### external getNextInQueue
_(no internal calls)_


### external getNumBids
_(no internal calls)_


### external getNumBidsInQueue
_(no internal calls)_


### external getPartialFill
-> internal _revertIfLotNotSettled


### external refundBid
-> internal _revertIfBidInvalid
-> internal _revertIfNotBidOwner
-> internal _revertIfBidClaimed
-> internal _revertIfDedicatedSettlePeriod
-> internal _revertIfKeySubmitted
-> internal _revertIfLotSettled
-> internal _refundBid


### external setDedicatedSettlePeriod
_(no internal calls)_


### external settle
-> internal _revertIfLotActive
-> internal _revertIfLotSettled
-> internal _settle
  -> internal _getLotMarginalPrice
    -> internal _getNextBid


### external submitPrivateKey
-> internal _revertIfLotActive
-> internal _revertIfLotSettled
-> internal _decryptAndSortBids
  -> internal _decrypt
    -> public decryptBid


---

## FeeManager

_File: src/bases/FeeManager.sol_

### public calculateQuoteFees
_(no internal calls)_


### external claimRewards
_(no internal calls)_


### external getCuratorFee
_(no internal calls)_


### external getFees
_(no internal calls)_


### public getProtocol
_(no internal calls)_


### external getRewards
_(no internal calls)_


### external setCuratorFee
_(no internal calls)_


---

## FixedPriceBatch

_File: src/modules/auctions/batch/FPB.sol_

### public VEECODE
_(no internal calls)_


### external abort
-> internal _revertIfDedicatedSettlePeriod
-> internal _revertIfLotSettled
-> internal _abort


### external auctionType
_(no internal calls)_


### external bid
-> internal _revertIfLotSettled
-> internal _bid
  -> internal _calculatePartialFill


### external claimBids
-> internal _revertIfLotNotSettled
-> internal _claimBids
  -> internal _revertIfBidInvalid
  -> internal _revertIfBidClaimed
  -> internal _getBidClaim


### external getAuctionData
_(no internal calls)_


### external getBid
-> internal _revertIfBidInvalid


### external getBidClaim
-> internal _revertIfLotNotSettled
-> internal _revertIfBidInvalid
-> internal _getBidClaim


### external getBidIdAtIndex
_(no internal calls)_


### external getBidIds
_(no internal calls)_


### external getNumBids
_(no internal calls)_


### external getPartialFill
-> internal _revertIfLotNotSettled


### external refundBid
-> internal _revertIfBidInvalid
-> internal _revertIfNotBidOwner
-> internal _revertIfBidClaimed
-> internal _refundBid


### external setDedicatedSettlePeriod
_(no internal calls)_


### external settle
-> internal _revertIfLotActive
-> internal _revertIfLotSettled
-> internal _settle


---

## FixedPriceSale

_File: src/modules/auctions/atomic/FPS.sol_

### public VEECODE
_(no internal calls)_


### external auctionType
_(no internal calls)_


### public maxAmountAccepted
_(no internal calls)_


### public maxPayout
_(no internal calls)_


### public payoutFor
_(no internal calls)_


### public priceFor
_(no internal calls)_


### external purchase
-> internal _purchase


---

## LinearVesting

_File: src/modules/derivatives/LinearVesting.sol_

### public TYPE
_(no internal calls)_


### public VEECODE
_(no internal calls)_


### public approve
_(no internal calls)_


### external computeId
-> internal _decodeVestingParams
-> internal _computeId
  -> public VEECODE


### public decimals
-> internal _getTokenMetadata


### external deploy
-> internal _decodeVestingParams
-> internal _validate
-> internal _deployIfNeeded
  -> internal _computeId
    -> public VEECODE
  -> internal _deployWrapIfNeeded
    -> internal _computeNameAndSymbol


### external exercise
-> external_callback IDerivative.Derivative_NotImplemented


### external exerciseCost
_(no internal calls)_


### external getTokenMetadata
_(no internal calls)_


### external getTokenVestingParams
_(no internal calls)_


### external mint
-> internal _mintDeployed
  -> internal _deployWrapIfNeeded
    -> internal _computeNameAndSymbol


### public name
-> internal _getTokenMetadata
-> internal _computeNameAndSymbol


### external reclaim
-> external_callback IDerivative.Derivative_NotImplemented


### external redeem
-> public redeemable
-> internal _redeem


### external redeemMax
-> public redeemable
-> internal _redeem


### public redeemable
_(no internal calls)_


### public symbol
-> internal _getTokenMetadata
-> internal _computeNameAndSymbol


### public tokenURI
-> internal _getTokenMetadata
-> public totalSupply
-> internal _attributes


### public totalSupply
_(no internal calls)_


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external transform
-> external_callback IDerivative.Derivative_NotImplemented


### external unwrap
_(no internal calls)_


### public validate
-> internal _decodeVestingParams
-> internal _validate


### external wrap
-> internal _deployWrapIfNeeded
  -> internal _computeNameAndSymbol


---

## Module

_File: src/modules/Modules.sol_

### external INIT
_(no internal calls)_


### public TYPE
_(no internal calls)_


### public VEECODE
_(no internal calls)_


---

## SoulboundCloneERC20

_File: src/modules/derivatives/SoulboundCloneERC20.sol_

### public approve
_(no internal calls)_


### external burn
_(no internal calls)_


### external expiry
_(no internal calls)_


### external mint
_(no internal calls)_


### public owner
_(no internal calls)_


### public transfer
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external underlying
_(no internal calls)_


---

## WithModules

_File: src/modules/Modules.sol_

### external execOnModule
-> internal _getModuleIfInstalled


### external installModule
-> internal _ensureContract


### external sunsetModule
-> internal _moduleIsInstalled

