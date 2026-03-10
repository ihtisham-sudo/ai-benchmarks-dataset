# Callpaths — Footium

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## FootiumAcademy

_File: contracts/FootiumAcademy.sol_

### external activateContract
_(no internal calls)_


### external changeCurrentSeasonId
_(no internal calls)_


### public changeMaxGenerationId
_(no internal calls)_


### external initialize
-> public setDivisionFees
-> public changeMaxGenerationId


### external mintPlayers
-> private _validateMintingParams


### external pauseContract
_(no internal calls)_


### external setClubDivsMerkleRoot
_(no internal calls)_


### public setDivisionFees
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## FootiumClub

_File: contracts/FootiumClub.sol_

### external activateContract
_(no internal calls)_


### external initialize
_(no internal calls)_


### external pauseContract
_(no internal calls)_


### external safeMint
_(no internal calls)_


### public setBaseURI
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## FootiumClubMinter

_File: contracts/FootiumClubMinter.sol_

### external initialize
_(no internal calls)_


### external mint
_(no internal calls)_


### external setClubAddress
_(no internal calls)_


### external setPlayerAddress
_(no internal calls)_


---

## FootiumEscrow

_File: contracts/FootiumEscrow.sol_

### external isValidSignature
_(no internal calls)_


### external setApprovalForERC20
_(no internal calls)_


### external setApprovalForERC721
_(no internal calls)_


### external transferERC20
_(no internal calls)_


### external transferERC721
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## FootiumGeneralPaymentContract

_File: contracts/FootiumGeneralPaymentContract.sol_

### external activateContract
_(no internal calls)_


### external initialize
_(no internal calls)_


### external makePayment
_(no internal calls)_


### external pauseContract
_(no internal calls)_


### external setPaymentReceiverAddress
_(no internal calls)_


---

## FootiumPlayer

_File: contracts/FootiumPlayer.sol_

### external activateContract
_(no internal calls)_


### external initialize
_(no internal calls)_


### external pauseContract
_(no internal calls)_


### external safeMint
_(no internal calls)_


### external setBaseURI
_(no internal calls)_


### external setRoyaltyInfo
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## FootiumPrizeDistributor

_File: contracts/FootiumPrizeDistributor.sol_

### external activateContract
_(no internal calls)_


### external claimERC20Prize
_(no internal calls)_


### external claimETHPrize
_(no internal calls)_


### external initialize
_(no internal calls)_


### external pauseContract
_(no internal calls)_


### external setERC20MerkleRoot
_(no internal calls)_


### external setETHMerkleRoot
_(no internal calls)_


---

## FootiumToken

_File: contracts/FootiumToken.sol_

### external initialize
_(no internal calls)_


### public mint
_(no internal calls)_

