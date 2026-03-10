# Callpaths — RadicalXChange

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AccessControlFacet

_File: contracts/access_control/facets/AccessControlFacet.sol_

### external initializeAccessControl
_(no internal calls)_


---

## AllowlistFacet

_File: contracts/allowlist/facets/AllowlistFacet.sol_

### external addToAllowlist
-> internal _addToAllowlist
  -> library AllowlistStorage.layout
-> internal _setAllowAny
  -> library AllowlistStorage.layout


### external batchAddToAllowlist
-> internal _batchAddToAllowlist
  -> library AllowlistStorage.layout
-> internal _setAllowAny
  -> library AllowlistStorage.layout


### external batchRemoveFromAllowlist
-> internal _batchRemoveFromAllowlist
  -> library AllowlistStorage.layout
-> internal _setAllowAny
  -> library AllowlistStorage.layout


### external batchUpdateAllowlist
-> internal _batchRemoveFromAllowlist
  -> library AllowlistStorage.layout
-> internal _batchAddToAllowlist
  -> library AllowlistStorage.layout
-> internal _setAllowAny
  -> library AllowlistStorage.layout


### external getAllowAny
-> internal _getAllowAny
  -> library AllowlistStorage.layout


### external getAllowlist
-> internal _getAllowlist
  -> library AllowlistStorage.layout


### external initializeAllowlist
-> internal _isInitialized
  -> library AllowlistStorage.layout
-> internal _initializeAllowlist
  -> library AllowlistStorage.layout
  -> internal _setAllowAny
    -> library AllowlistStorage.layout


### external isAllowed
-> internal _isAllowed
  -> library AllowlistStorage.layout


### external removeFromAllowlist
-> internal _removeFromAllowlist
  -> library AllowlistStorage.layout
-> internal _setAllowAny
  -> library AllowlistStorage.layout


### external setAllowAny
-> internal _setAllowAny
  -> library AllowlistStorage.layout


---

## AllowlistMock

_File: contracts/allowlist/facets/AllowlistMock.sol_

### external isAllowed
-> internal layout


### external setIsAllowed
-> internal layout


---

## BeneficiaryMock

_File: contracts/beneficiary/facets/BeneficiaryMock.sol_

### external distribute
_(no internal calls)_


### external initializeMockBeneficiary
_(no internal calls)_


---

## EnglishPeriodicAuctionFacet

_File: contracts/auction/facets/EnglishPeriodicAuctionFacet.sol_

### external auctionEndTime
-> internal _auctionEndTime
  -> library EnglishPeriodicAuctionStorage.layout
  -> internal _auctionLengthSeconds
    -> library EnglishPeriodicAuctionStorage.layout
  -> internal _auctionStartTime
    -> library EnglishPeriodicAuctionStorage.layout


### external auctionLengthSeconds
-> internal _auctionLengthSeconds
  -> library EnglishPeriodicAuctionStorage.layout


### external auctionStartTime
-> internal _auctionStartTime
  -> library EnglishPeriodicAuctionStorage.layout


### external availableCollateral
-> internal _availableCollateral
  -> library EnglishPeriodicAuctionStorage.layout


### external bidExtensionSeconds
-> internal _bidExtensionSeconds
  -> library EnglishPeriodicAuctionStorage.layout


### external bidExtensionWindowLengthSeconds
-> internal _bidExtensionWindowLengthSeconds


### external bidOf
-> internal _bidOf
  -> library EnglishPeriodicAuctionStorage.layout


### external calculateFeeFromBid
-> internal _calculateFeeFromBid


### external cancelAllBidsAndWithdrawCollateral
-> internal _cancelAllBids
  -> library EnglishPeriodicAuctionStorage.layout
-> internal _withdrawCollateral
  -> library EnglishPeriodicAuctionStorage.layout


### external cancelBid
-> internal _cancelBid
  -> library EnglishPeriodicAuctionStorage.layout


### external cancelBidAndWithdrawCollateral
-> internal _cancelBid
  -> library EnglishPeriodicAuctionStorage.layout
-> internal _withdrawCollateral
  -> library EnglishPeriodicAuctionStorage.layout


### external closeAuction
-> internal _isReadyForTransfer
  -> internal _auctionEndTime
    -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionLengthSeconds
      -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionStartTime
      -> library EnglishPeriodicAuctionStorage.layout
-> internal _closeAuction
  -> library EnglishPeriodicAuctionStorage.layout


### external currentAuctionRound
-> internal _currentAuctionRound
  -> library EnglishPeriodicAuctionStorage.layout


### external highestBid
-> internal _highestBid
  -> library EnglishPeriodicAuctionStorage.layout


### external initialBidder
-> internal _initialBidder
  -> library EnglishPeriodicAuctionStorage.layout


### external initialPeriodStartTime
-> internal _initialPeriodStartTime
  -> library EnglishPeriodicAuctionStorage.layout


### external initializeAuction
-> internal _isInitialized
  -> library EnglishPeriodicAuctionStorage.layout
-> internal _initializeAuction
  -> library EnglishPeriodicAuctionStorage.layout
  -> internal _setStartingBid
    -> library EnglishPeriodicAuctionStorage.layout
  -> internal _setRepossessor
    -> library EnglishPeriodicAuctionStorage.layout
  -> internal _setAuctionLengthSeconds
  -> internal _setMinBidIncrement
  -> internal _setBidExtensionWindowLengthSeconds
  -> internal _setBidExtensionSeconds


### external isAuctionPeriod
-> internal _isAuctionPeriod
  -> internal _auctionStartTime
    -> library EnglishPeriodicAuctionStorage.layout


### external isReadyForTransfer
-> internal _isReadyForTransfer
  -> internal _auctionEndTime
    -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionLengthSeconds
      -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionStartTime
      -> library EnglishPeriodicAuctionStorage.layout


### external lockedCollateral
-> internal _lockedCollateral
  -> library EnglishPeriodicAuctionStorage.layout


### external minBidIncrement
-> internal _minBidIncrement
  -> library EnglishPeriodicAuctionStorage.layout


### external placeBid
-> internal _isAuctionPeriod
  -> internal _auctionStartTime
    -> library EnglishPeriodicAuctionStorage.layout
-> internal _isReadyForTransfer
  -> internal _auctionEndTime
    -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionLengthSeconds
      -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionStartTime
      -> library EnglishPeriodicAuctionStorage.layout
-> internal _placeBid
  -> library EnglishPeriodicAuctionStorage.layout
  -> internal _checkBidAmount
    -> internal _calculateFeeFromBid
  -> internal _auctionEndTime
    -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionLengthSeconds
      -> library EnglishPeriodicAuctionStorage.layout
    -> internal _auctionStartTime
      -> library EnglishPeriodicAuctionStorage.layout
  -> internal _bidExtensionWindowLengthSeconds
  -> internal _auctionLengthSeconds
    -> library EnglishPeriodicAuctionStorage.layout
  -> internal _bidExtensionSeconds
    -> library EnglishPeriodicAuctionStorage.layout


### external repossessor
-> internal _repossessor
  -> library EnglishPeriodicAuctionStorage.layout


### external setAuctionLengthSeconds
-> internal _setAuctionLengthSeconds


### external setAuctionParameters
-> internal _setAuctionParameters
  -> internal _setRepossessor
    -> library EnglishPeriodicAuctionStorage.layout
  -> internal _setAuctionLengthSeconds
  -> internal _setMinBidIncrement
  -> internal _setBidExtensionWindowLengthSeconds
  -> internal _setBidExtensionSeconds
  -> internal _setStartingBid
    -> library EnglishPeriodicAuctionStorage.layout


### external setBidExtensionSeconds
-> internal _setBidExtensionSeconds


### external setBidExtensionWindowLengthSeconds
-> internal _setBidExtensionWindowLengthSeconds


### external setMinBidIncrement
-> internal _setMinBidIncrement


### external setRepossessor
-> internal _setRepossessor
  -> library EnglishPeriodicAuctionStorage.layout


### external setStartingBid
-> internal _setStartingBid
  -> library EnglishPeriodicAuctionStorage.layout


### external startingBid
-> internal _startingBid
  -> library EnglishPeriodicAuctionStorage.layout


### external withdrawCollateral
-> internal _withdrawCollateral
  -> library EnglishPeriodicAuctionStorage.layout


---

## IDABeneficiaryFacet

_File: contracts/beneficiary/facets/IDABeneficiaryFacet.sol_

### external distribute
-> internal _distribute
  -> library IDABeneficiaryStorage.layout


### external initializeIDABeneficiary
-> internal _isInitialized
  -> library IDABeneficiaryStorage.layout
-> internal _initializeIDABeneficiary
  -> library IDABeneficiaryStorage.layout
  -> internal _setToken
    -> library IDABeneficiaryStorage.layout
  -> internal _updateBeneficiaryUnits
    -> library IDABeneficiaryStorage.layout


### external updateBeneficiaryUnits
-> internal _updateBeneficiaryUnits
  -> library IDABeneficiaryStorage.layout


---

## NativeStewardLicenseFacet

_File: contracts/license/facets/NativeStewardLicenseFacet.sol_

### external addTokenToCollection
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensToCollection
-> internal _initialSteward
  -> library StewardLicenseStorage.layout
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensWithBaseURIToCollection
-> internal _addTokenWithBaseURIToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external exists
_(no internal calls)_


### external initializeStewardLicense
-> internal _isInitialized
  -> library StewardLicenseStorage.layout
-> internal _initializeStewardLicense
  -> library StewardLicenseStorage.layout


### external maxTokenCount
-> internal _maxTokenCount
  -> library StewardLicenseStorage.layout


### external mintToken
-> internal _triggerTransfer


### external minter
-> internal _minter
  -> library StewardLicenseStorage.layout


### external triggerTransfer
-> internal _triggerTransfer


---

## NativeStewardLicenseMock

_File: contracts/license/facets/NativeStewardLicenseMock.sol_

### external burn
_(no internal calls)_


### external initializeStewardLicense
_(no internal calls)_


### external mint
_(no internal calls)_


### external minter
_(no internal calls)_


### external testTriggerTransfer
_(no internal calls)_


---

## OwnableDiamondFactory

_File: contracts/proxies/OwnableDiamondFactory.sol_

### external createDiamond
_(no internal calls)_


---

## PeriodicAuctionMock

_File: contracts/auction/facets/PeriodicAuctionMock.sol_

### external initialBidder
-> internal layout


### external initialPeriodStartTime
-> internal layout


### external isAuctionPeriod
-> internal layout


### external setInitialBidder
-> internal layout


### external setInitialPeriodStartTime
-> internal layout


### external setIsAuctionPeriod
-> internal layout


### external setShouldFail
-> internal layout


---

## PeriodicPCOParamsFacet

_File: contracts/pco/facets/PeriodicPCOParamsFacet.sol_

### external feeDenominator
-> internal _feeDenominator
  -> library PeriodicPCOParamsStorage.layout


### external feeNumerator
-> internal _feeNumerator
  -> library PeriodicPCOParamsStorage.layout


### external initializePCOParams
-> internal _isInitialized
  -> library PeriodicPCOParamsStorage.layout
-> internal _initializeParams
  -> internal _setLicensePeriod
  -> internal _setFeeNumerator
  -> internal _setFeeDenominator


### external licensePeriod
-> internal _licensePeriod
  -> library PeriodicPCOParamsStorage.layout


### external setFeeDenominator
-> internal _setFeeDenominator


### external setFeeNumerator
-> internal _setFeeNumerator


### external setLicensePeriod
-> internal _setLicensePeriod


### external setPCOParameters
-> internal _setPCOParameters
  -> internal _setLicensePeriod
  -> internal _setFeeNumerator
  -> internal _setFeeDenominator


---

## SingleCutDiamondFactory

_File: contracts/proxies/SingleCutDiamondFactory.sol_

### external createDiamond
_(no internal calls)_


---

## SolidStateERC1155Mock

_File: contracts/license/facets/SolidStateERC1155Mock.sol_

### external __mint
_(no internal calls)_


---

## SolidStateERC721Mock

_File: contracts/license/facets/SolidStateERC721Mock.sol_

### external mint
_(no internal calls)_


---

## StewardLicenseBase

_File: contracts/license/StewardLicenseBase.sol_

### external addTokenToCollection
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensToCollection
-> internal _initialSteward
  -> library StewardLicenseStorage.layout
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensWithBaseURIToCollection
-> internal _addTokenWithBaseURIToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external exists
_(no internal calls)_


### external maxTokenCount
-> internal _maxTokenCount
  -> library StewardLicenseStorage.layout


### external mintToken
-> internal _triggerTransfer


### external triggerTransfer
-> internal _triggerTransfer


---

## WrappedERC1155StewardLicenseFacet

_File: contracts/license/facets/WrappedERC1155StewardLicenseFacet.sol_

### external addTokenToCollection
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensToCollection
-> internal _initialSteward
  -> library StewardLicenseStorage.layout
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensWithBaseURIToCollection
-> internal _addTokenWithBaseURIToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external exists
_(no internal calls)_


### external initializeWrappedStewardLicense
-> internal _isInitialized
  -> library StewardLicenseStorage.layout
-> internal _initializeWrappedLicense
  -> library WrappedStewardLicenseStorage.layout
-> internal _initializeStewardLicense
  -> library StewardLicenseStorage.layout


### external maxTokenCount
-> internal _maxTokenCount
  -> library StewardLicenseStorage.layout


### external mintToken
-> internal _triggerTransfer


### external minter
-> internal _minter
  -> library StewardLicenseStorage.layout


### external onERC1155BatchReceived
-> internal _isInitialized
  -> library StewardLicenseStorage.layout
-> internal _wrappedTokenAddress
  -> library WrappedStewardLicenseStorage.layout
-> internal _wrappedTokenId
  -> library WrappedStewardLicenseStorage.layout


### external onERC1155Received
-> internal _isInitialized
  -> library StewardLicenseStorage.layout
-> internal _wrappedTokenAddress
  -> library WrappedStewardLicenseStorage.layout
-> internal _wrappedTokenId
  -> library WrappedStewardLicenseStorage.layout


### external triggerTransfer
-> internal _triggerTransfer


---

## WrappedERC1155StewardLicenseMock

_File: contracts/license/facets/WrappedERC1155StewardLicenseMock.sol_

### external initializeWrappedStewardLicense
_(no internal calls)_


### external mint
_(no internal calls)_


### external minter
_(no internal calls)_


### external onERC1155BatchReceived
_(no internal calls)_


### external onERC1155Received
_(no internal calls)_


---

## WrappedERC721StewardLicenseFacet

_File: contracts/license/facets/WrappedERC721StewardLicenseFacet.sol_

### external addTokenToCollection
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensToCollection
-> internal _initialSteward
  -> library StewardLicenseStorage.layout
-> internal _addTokenToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external addTokensWithBaseURIToCollection
-> internal _addTokenWithBaseURIToCollection
  -> library StewardLicenseStorage.layout
  -> library EnglishPeriodicAuctionStorage.layout


### external exists
_(no internal calls)_


### external initializeWrappedStewardLicense
-> internal _isInitialized
  -> library StewardLicenseStorage.layout
-> internal _initializeWrappedLicense
  -> library WrappedStewardLicenseStorage.layout
-> internal _initializeStewardLicense
  -> library StewardLicenseStorage.layout


### external maxTokenCount
-> internal _maxTokenCount
  -> library StewardLicenseStorage.layout


### external mintToken
-> internal _triggerTransfer


### external minter
-> internal _minter
  -> library StewardLicenseStorage.layout


### external onERC721Received
-> internal _isInitialized
  -> library StewardLicenseStorage.layout
-> internal _wrappedTokenAddress
  -> library WrappedStewardLicenseStorage.layout
-> internal _wrappedTokenId
  -> library WrappedStewardLicenseStorage.layout


### external triggerTransfer
-> internal _triggerTransfer


---

## WrappedERC721StewardLicenseMock

_File: contracts/license/facets/WrappedERC721StewardLicenseMock.sol_

### external initializeWrappedStewardLicense
_(no internal calls)_


### external mint
_(no internal calls)_


### external minter
_(no internal calls)_


### external onERC721Received
_(no internal calls)_

