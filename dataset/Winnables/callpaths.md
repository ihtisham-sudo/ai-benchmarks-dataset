# Callpaths — Winnables

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BaseCCIPContract

_File: contracts/BaseCCIPContract.sol_

### external getCCIPRouter
_(no internal calls)_


---

## BaseCCIPReceiver

_File: contracts/BaseCCIPReceiver.sol_

### external ccipReceive
_(no internal calls)_


### external getCCIPRouter
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## BaseCCIPSender

_File: contracts/BaseCCIPSender.sol_

### external getCCIPRouter
_(no internal calls)_


### external getLinkToken
_(no internal calls)_


---

## BaseLinkConsumer

_File: contracts/BaseLinkConsumer.sol_

### external getLinkToken
_(no internal calls)_


---

## Roles

_File: contracts/Roles.sol_

### external getRoles
_(no internal calls)_


### external setRole
-> internal _setRole


---

## WinnablesPrizeManager

_File: contracts/WinnablesPrizeManager.sol_

### external ccipReceive
-> internal _ccipReceive
  -> internal _decodeRaffleCanceledMessage
  -> internal _cancelRaffle
  -> internal _decodeWinnerDrawnMessage


### external claimPrize
-> internal _sendNFTPrize
-> internal _sendTokenPrize
-> internal _sendETHPrize


### external getETHRaffle
_(no internal calls)_


### external getNFTRaffle
_(no internal calls)_


### external getRaffle
_(no internal calls)_


### external getRoles
_(no internal calls)_


### external getTokenRaffle
_(no internal calls)_


### external getWinner
_(no internal calls)_


### external lockETH
-> internal _checkValidRaffle
-> internal _sendCCIPMessage


### external lockNFT
-> internal _checkValidRaffle
-> internal _sendCCIPMessage


### external lockTokens
-> internal _checkValidRaffle
-> internal _sendCCIPMessage


### external onERC721Received
_(no internal calls)_


### external setCCIPExtraArgs
-> internal _setCCIPExtraArgs


### external setRole
-> internal _setRole


### public supportsInterface
_(no internal calls)_


### external withdrawETH
_(no internal calls)_


### external withdrawNFT
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## WinnablesTicket

_File: contracts/WinnablesTicket.sol_

### external balanceOf
_(no internal calls)_


### external balanceOfBatch
_(no internal calls)_


### external batchMint
_(no internal calls)_


### external initializeManager
_(no internal calls)_


### external isApprovedForAll
_(no internal calls)_


### external mint
_(no internal calls)_


### public ownerOf
_(no internal calls)_


### external refreshMetadata
-> public uri


### external safeBatchTransferFrom
_(no internal calls)_


### external safeTransferFrom
_(no internal calls)_


### external setApprovalForAll
_(no internal calls)_


### external setURI
_(no internal calls)_


### external supplyOf
_(no internal calls)_


### external supportsInterface
_(no internal calls)_


### external transferOwnership
_(no internal calls)_


### public uri
_(no internal calls)_


---

## WinnablesTicketManager

_File: contracts/WinnablesTicketManager.sol_

### external buyTickets
-> internal _checkTicketPurchaseable
-> internal _checkPurchaseSig
  -> internal _getSigner
  -> internal _hasRole


### external cancelRaffle
-> internal _checkVRFTimeout
  -> internal _checkRole
    -> internal _hasRole
-> internal _checkShouldCancel
  -> internal _checkRole
    -> internal _hasRole
-> internal _sendCCIPMessage


### external ccipReceive
-> internal _ccipReceive
  -> internal _sendCCIPMessage


### external createRaffle
-> internal _checkRaffleTimings


### external drawWinner
-> internal _checkVRFTimeout
  -> internal _checkRole
    -> internal _hasRole
-> internal _checkShouldDraw


### external getNonce
_(no internal calls)_


### external getParticipation
_(no internal calls)_


### external getRaffle
_(no internal calls)_


### external getRequestStatus
_(no internal calls)_


### external getRoles
_(no internal calls)_


### external getWinner
-> internal _getWinnerByRequestId


### external propagateRaffleWinner
-> internal _getWinnerByRequestId
-> internal _sendCCIPMessage


### external refundPlayers
-> internal _sendETH


### external setCCIPCounterpart
_(no internal calls)_


### external setCCIPExtraArgs
-> internal _setCCIPExtraArgs


### external setRequestConfirmations
_(no internal calls)_


### external setRole
-> internal _setRole


### external shouldCancelRaffle
-> internal _checkShouldCancel
  -> internal _checkRole
    -> internal _hasRole


### external shouldDrawRaffle
-> internal _checkShouldDraw


### public supportsInterface
_(no internal calls)_


### external withdrawETH
-> internal _sendETH


### external withdrawTokens
_(no internal calls)_

