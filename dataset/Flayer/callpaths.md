# Callpaths — Flayer

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AirdropRecipient

_File: src/contracts/utils/AirdropRecipient.sol_

### public claimAirdrop
_(no internal calls)_


### public distributeAirdrop
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public requestAirdrop
_(no internal calls)_


### external setERC1271Signer
_(no internal calls)_


---

## BaseImplementation

_File: src/contracts/implementation/BaseImplementation.sol_

### public claim
_(no internal calls)_


### public depositFees
_(no internal calls)_


### public feeSplit
_(no internal calls)_


### public getCollectionPoolKey
_(no internal calls)_


### public initialize
_(no internal calls)_


### public initializeCollection
_(no internal calls)_


### public poolFees
_(no internal calls)_


### public registerCollection
_(no internal calls)_


### public setBeneficiary
_(no internal calls)_


### public setBeneficiaryRoyalty
_(no internal calls)_


### public setDonateThresholds
_(no internal calls)_


---

## CollectionShutdown

_File: src/contracts/utils/CollectionShutdown.sol_

### public cancel
_(no internal calls)_


### public claim
-> public collectionLiquidationComplete


### public collectionLiquidationComplete
_(no internal calls)_


### public collectionParams
_(no internal calls)_


### public execute
-> internal _hasListings
-> internal _createSudoswapPool


### public pause
_(no internal calls)_


### public preventShutdown
-> external_callback ILocker.CallerIsNotManager


### public reclaimVote
_(no internal calls)_


### public start
-> internal _vote


### public vote
-> internal _vote


### public voteAndClaim
-> public collectionLiquidationComplete


---

## CollectionToken

_File: src/contracts/CollectionToken.sol_

### public burn
-> internal _burn


### public burnFrom
-> internal _burn


### public initialize
_(no internal calls)_


### public maxSupply
_(no internal calls)_


### public mint
-> internal _mint


### public name
_(no internal calls)_


### public setMetadata
_(no internal calls)_


### public symbol
_(no internal calls)_


---

## FlayerTokenMigration

_File: src/contracts/migration/FlayerTokenMigration.sol_

### external pause
_(no internal calls)_


### external swap
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## Listings

_File: src/contracts/Listings.sol_

### public cancelListings
-> public getListingType
-> private _resolveListingTax
  -> public getListingTaxRequired
  -> internal _deposit
-> private payTaxWithEscrow


### public createLiquidationListing
-> private _mapListings


### public createListings
-> private _validateCreateListing
  -> public getListingType
-> private _mapListings
-> public getListingTaxRequired
-> private _depositNftsAndReceiveTokens
-> public getListingType


### public fillListings
-> private _fillListing
  -> public getListingPrice
  -> private _resolveListingTax
    -> public getListingTaxRequired
    -> internal _deposit
-> private _tload
-> internal _deposit


### public getListingPrice
_(no internal calls)_


### public getListingTaxRequired
_(no internal calls)_


### public getListingType
_(no internal calls)_


### public listings
_(no internal calls)_


### public modifyListings
-> public getListingType
-> private _resolveListingTax
  -> public getListingTaxRequired
  -> internal _deposit
-> public getListingTaxRequired
-> private payTaxWithEscrow
-> internal _deposit


### public relist
-> public getListingPrice
-> private _resolveListingTax
  -> public getListingTaxRequired
  -> internal _deposit
-> private _validateCreateListing
  -> public getListingType
-> private payTaxWithEscrow
-> public getListingTaxRequired


### public reserve
-> public getListingPrice
-> private _resolveListingTax
  -> public getListingTaxRequired
  -> internal _deposit
-> external_callback IProtectedListings.CreateListing
-> external_callback IProtectedListings.ProtectedListing


### public setProtectedListings
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## Locker

_File: src/contracts/Locker.sol_

### public claimAirdrop
_(no internal calls)_


### public collectionToken
_(no internal calls)_


### public createCollection
_(no internal calls)_


### public deposit
_(no internal calls)_


### public distributeAirdrop
_(no internal calls)_


### public initializeCollection
-> public deposit


### public isListing
_(no internal calls)_


### external isValidSignature
_(no internal calls)_


### public pause
_(no internal calls)_


### public paused
_(no internal calls)_


### public redeem
-> public isListing


### public requestAirdrop
_(no internal calls)_


### public setCollectionShutdownContract
_(no internal calls)_


### public setCollectionTokenMetadata
_(no internal calls)_


### external setERC1271Signer
_(no internal calls)_


### public setImplementation
_(no internal calls)_


### public setListingsContract
_(no internal calls)_


### public setTaxCalculator
_(no internal calls)_


### public sunsetCollection
_(no internal calls)_


### public swap
-> public isListing


### public swapBatch
-> public isListing


### public unbackedDeposit
_(no internal calls)_


### public withdrawToken
_(no internal calls)_


---

## LockerManager

_File: src/contracts/LockerManager.sol_

### public isManager
_(no internal calls)_


### public setManager
_(no internal calls)_


---

## ProtectedListings

_File: src/contracts/ProtectedListings.sol_

### public adjustPosition
-> public getProtectedListingHealth
  -> public unlockPrice
    -> internal _currentCheckpoint
      -> public utilizationRate


### public createCheckpoint
-> internal _createCheckpoint
  -> public utilizationRate
  -> internal _currentCheckpoint
    -> public utilizationRate


### public createListings
-> internal _validateCreateListing
-> internal _createCheckpoint
  -> public utilizationRate
  -> internal _currentCheckpoint
    -> public utilizationRate
-> internal _mapListings
-> internal _depositNftsAndReceiveTokens


### public getProtectedListingHealth
-> public unlockPrice
  -> internal _currentCheckpoint
    -> public utilizationRate


### public liquidateProtectedListing
-> public getProtectedListingHealth
  -> public unlockPrice
    -> internal _currentCheckpoint
      -> public utilizationRate
-> external_callback IListings.CreateListing
-> external_callback IListings.Listing
-> internal _createCheckpoint
  -> public utilizationRate
  -> internal _currentCheckpoint
    -> public utilizationRate


### public listings
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public unlockPrice
-> internal _currentCheckpoint
  -> public utilizationRate


### public unlockProtectedListing
-> public getProtectedListingHealth
  -> public unlockPrice
    -> internal _currentCheckpoint
      -> public utilizationRate
-> public unlockPrice
  -> internal _currentCheckpoint
    -> public utilizationRate
-> internal _createCheckpoint
  -> public utilizationRate
  -> internal _currentCheckpoint
    -> public utilizationRate


### public utilizationRate
_(no internal calls)_


### public withdrawProtectedListing
_(no internal calls)_


---

## TaxCalculator

_File: src/contracts/TaxCalculator.sol_

### public calculateCompoundedFactor
_(no internal calls)_


### public calculateProtectedInterest
_(no internal calls)_


### public calculateTax
_(no internal calls)_


### public compound
_(no internal calls)_


---

## TokenEscrow

_File: src/contracts/TokenEscrow.sol_

### public withdraw
_(no internal calls)_


---

## UniswapImplementation

_File: src/contracts/implementation/UniswapImplementation.sol_

### public afterAddLiquidity
-> internal _emitPoolStateUpdate


### public afterRemoveLiquidity
-> internal _emitPoolStateUpdate


### public afterSwap
-> internal _distributeFees
  -> public feeSplit
  -> internal _pushTokens
-> internal _emitPoolStateUpdate


### public beforeAddLiquidity
-> internal _distributeFees
  -> public feeSplit
  -> internal _pushTokens


### public beforeInitialize
_(no internal calls)_


### public beforeRemoveLiquidity
-> internal _distributeFees
  -> public feeSplit
  -> internal _pushTokens


### public beforeSwap
-> public getFee
-> internal _pushTokens


### public claim
_(no internal calls)_


### public depositFees
-> internal _pullTokens


### public feeSplit
_(no internal calls)_


### public getCollectionPoolKey
_(no internal calls)_


### public getFee
_(no internal calls)_


### public getHookPermissions
_(no internal calls)_


### public initialize
_(no internal calls)_


### public initializeCollection
-> internal _emitPoolStateUpdate


### public poolFees
_(no internal calls)_


### public registerCollection
_(no internal calls)_


### public removeFeeExemption
_(no internal calls)_


### public setAmmBeneficiary
_(no internal calls)_


### public setAmmFee
_(no internal calls)_


### public setBeneficiary
_(no internal calls)_


### public setBeneficiaryRoyalty
_(no internal calls)_


### public setDefaultFee
_(no internal calls)_


### public setDonateThresholds
_(no internal calls)_


### public setFee
_(no internal calls)_


### public setFeeExemption
_(no internal calls)_

