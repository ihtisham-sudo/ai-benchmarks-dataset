# Callpaths — HatsSignerGate

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Hats

_File: src/Hats.sol_

### external approveLinkTopHatToTree
-> public getHatLevel
  -> public getLocalHatLevel
  -> public getTopHatDomain
  -> public getHatLevel
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> public buildHatId
-> internal _checkAdminOrWearer
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
  -> public isWearerOfHat
    -> public balanceOf
      -> internal _isActive
        -> internal _getHatStatus
      -> internal _isEligible
-> internal _linkTopHatToTree
  -> public noCircularLinkage
    -> public getTopHatDomain
    -> public noCircularLinkage
  -> public getTippyTopHatDomain
    -> public getTippyTopHatDomain
    -> public getTopHatDomain
  -> public isWearerOfHat
    -> public balanceOf
      -> internal _isActive
        -> internal _getHatStatus
      -> internal _isEligible
  -> public sameTippyTopHatDomain
    -> public getTippyTopHatDomain
      -> public getTippyTopHatDomain
      -> public getTopHatDomain
    -> public getTopHatDomain


### public balanceOf
-> internal _isActive
  -> internal _getHatStatus
-> internal _isEligible


### public balanceOfBatch
-> public balanceOf
  -> internal _isActive
    -> internal _getHatStatus
  -> internal _isEligible


### public batchCreateHats
-> public createHat
  -> public isValidHatId
    -> public isLocalTopHat
    -> public getLocalHatLevel
  -> public getNextId
    -> public buildHatId
  -> internal _checkAdmin
    -> public isAdminOfHat
      -> public isLocalTopHat
      -> public getTopHatDomain
      -> public isWearerOfHat
        -> public balanceOf
          -> internal _isActive
            -> internal _getHatStatus
          -> internal _isEligible
      -> public getLocalHatLevel
      -> public getAdminAtLocalLevel
      -> public isAdminOfHat
  -> internal _createHat


### public batchMintHats
-> public mintHat
  -> public isEligible
    -> internal _isEligible
  -> internal _isActive
    -> internal _getHatStatus
  -> internal _checkAdmin
    -> public isAdminOfHat
      -> public isLocalTopHat
      -> public getTopHatDomain
      -> public isWearerOfHat
        -> public balanceOf
          -> internal _isActive
            -> internal _getHatStatus
          -> internal _isEligible
      -> public getLocalHatLevel
      -> public getAdminAtLocalLevel
      -> public isAdminOfHat
  -> internal _staticBalanceOf
  -> internal _mintHat


### public buildHatId
_(no internal calls)_


### external changeHatDetails
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> public isTopHat
  -> public isLocalTopHat
  -> public getTopHatDomain
-> internal _isMutable


### external changeHatEligibility
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> internal _isMutable


### external changeHatImageURI
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> public isTopHat
  -> public isLocalTopHat
  -> public getTopHatDomain
-> internal _isMutable


### external changeHatMaxSupply
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> internal _isMutable


### external changeHatToggle
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> internal _isMutable
-> internal _pullHatStatus
-> internal _processHatStatus
  -> internal _getHatStatus
  -> internal _setHatStatus


### public checkHatStatus
-> internal _pullHatStatus
-> internal _processHatStatus
  -> internal _getHatStatus
  -> internal _setHatStatus


### public checkHatWearerStatus
-> internal _processHatWearerStatus
  -> internal _staticBalanceOf
  -> internal _burnHat


### public createHat
-> public isValidHatId
  -> public isLocalTopHat
  -> public getLocalHatLevel
-> public getNextId
  -> public buildHatId
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> internal _createHat


### public getAdminAtLevel
-> public getTopHatDomain
-> public getAdminAtLocalLevel
-> public getHatLevel
  -> public getLocalHatLevel
  -> public getTopHatDomain
  -> public getHatLevel
-> public getAdminAtLevel


### public getAdminAtLocalLevel
_(no internal calls)_


### external getHatEligibilityModule
_(no internal calls)_


### public getHatLevel
-> public getLocalHatLevel
-> public getTopHatDomain
-> public getHatLevel


### external getHatMaxSupply
_(no internal calls)_


### external getHatToggleModule
_(no internal calls)_


### public getImageURIForHat
-> public getHatLevel
  -> public getLocalHatLevel
  -> public getTopHatDomain
  -> public getHatLevel
-> public getAdminAtLevel
  -> public getTopHatDomain
  -> public getAdminAtLocalLevel
  -> public getHatLevel
    -> public getLocalHatLevel
    -> public getTopHatDomain
    -> public getHatLevel
  -> public getAdminAtLevel


### public getLocalHatLevel
_(no internal calls)_


### public getNextId
-> public buildHatId


### public getTippyTopHatDomain
-> public getTippyTopHatDomain
-> public getTopHatDomain


### public getTopHatDomain
_(no internal calls)_


### external hatSupply
_(no internal calls)_


### external isActive
-> internal _isActive
  -> internal _getHatStatus


### public isAdminOfHat
-> public isLocalTopHat
-> public getTopHatDomain
-> public isWearerOfHat
  -> public balanceOf
    -> internal _isActive
      -> internal _getHatStatus
    -> internal _isEligible
-> public getLocalHatLevel
-> public getAdminAtLocalLevel
-> public isAdminOfHat


### public isEligible
-> internal _isEligible


### public isInGoodStanding
_(no internal calls)_


### public isLocalTopHat
_(no internal calls)_


### public isTopHat
-> public isLocalTopHat
-> public getTopHatDomain


### public isValidHatId
-> public isLocalTopHat
-> public getLocalHatLevel


### public isWearerOfHat
-> public balanceOf
  -> internal _isActive
    -> internal _getHatStatus
  -> internal _isEligible


### external makeHatImmutable
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> internal _isMutable


### public mintHat
-> public isEligible
  -> internal _isEligible
-> internal _isActive
  -> internal _getHatStatus
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> internal _staticBalanceOf
-> internal _mintHat


### public mintTopHat
-> internal _createHat
-> internal _mintHat


### public noCircularLinkage
-> public getTopHatDomain
-> public noCircularLinkage


### external relinkTopHatWithinTree
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> public getHatLevel
  -> public getLocalHatLevel
  -> public getTopHatDomain
  -> public getHatLevel
-> public buildHatId
-> internal _checkAdminOrWearer
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
  -> public isWearerOfHat
    -> public balanceOf
      -> internal _isActive
        -> internal _getHatStatus
      -> internal _isEligible
-> internal _linkTopHatToTree
  -> public noCircularLinkage
    -> public getTopHatDomain
    -> public noCircularLinkage
  -> public getTippyTopHatDomain
    -> public getTippyTopHatDomain
    -> public getTopHatDomain
  -> public isWearerOfHat
    -> public balanceOf
      -> internal _isActive
        -> internal _getHatStatus
      -> internal _isEligible
  -> public sameTippyTopHatDomain
    -> public getTippyTopHatDomain
      -> public getTippyTopHatDomain
      -> public getTopHatDomain
    -> public getTopHatDomain


### external renounceHat
-> internal _staticBalanceOf
-> internal _burnHat


### external requestLinkTopHatToTree
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat


### public safeBatchTransferFrom
_(no internal calls)_


### public safeTransferFrom
_(no internal calls)_


### public sameTippyTopHatDomain
-> public getTippyTopHatDomain
  -> public getTippyTopHatDomain
  -> public getTopHatDomain
-> public getTopHatDomain


### public setApprovalForAll
_(no internal calls)_


### external setHatStatus
-> internal _processHatStatus
  -> internal _getHatStatus
  -> internal _setHatStatus


### external setHatWearerStatus
-> internal _processHatWearerStatus
  -> internal _staticBalanceOf
  -> internal _burnHat


### public supportsInterface
_(no internal calls)_


### public transferHat
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> public isTopHat
  -> public isLocalTopHat
  -> public getTopHatDomain
-> internal _isMutable
-> internal _staticBalanceOf
-> public isEligible
  -> internal _isEligible
-> internal _isActive
  -> internal _getHatStatus


### external unlinkTopHatFromTree
-> internal _checkAdmin
  -> public isAdminOfHat
    -> public isLocalTopHat
    -> public getTopHatDomain
    -> public isWearerOfHat
      -> public balanceOf
        -> internal _isActive
          -> internal _getHatStatus
        -> internal _isEligible
    -> public getLocalHatLevel
    -> public getAdminAtLocalLevel
    -> public isAdminOfHat
-> public isWearerOfHat
  -> public balanceOf
    -> internal _isActive
      -> internal _getHatStatus
    -> internal _isEligible
-> external_callback HatsErrors.InvalidUnlink


### public uri
-> internal _constructURI
  -> public isTopHat
    -> public isLocalTopHat
    -> public getTopHatDomain
  -> public getAdminAtLevel
    -> public getTopHatDomain
    -> public getAdminAtLocalLevel
    -> public getHatLevel
      -> public getLocalHatLevel
      -> public getTopHatDomain
      -> public getHatLevel
    -> public getAdminAtLevel
  -> public getHatLevel
    -> public getLocalHatLevel
    -> public getTopHatDomain
    -> public getHatLevel


### public viewHat
-> public getImageURIForHat
  -> public getHatLevel
    -> public getLocalHatLevel
    -> public getTopHatDomain
    -> public getHatLevel
  -> public getAdminAtLevel
    -> public getTopHatDomain
    -> public getAdminAtLocalLevel
    -> public getHatLevel
      -> public getLocalHatLevel
      -> public getTopHatDomain
      -> public getHatLevel
    -> public getAdminAtLevel
-> internal _isMutable
-> internal _isActive
  -> internal _getHatStatus


---

## HatsIdUtilities

_File: src/HatsIdUtilities.sol_

### public buildHatId
_(no internal calls)_


### public getAdminAtLevel
-> public getTopHatDomain
-> public getAdminAtLocalLevel
-> public getHatLevel
  -> public getLocalHatLevel
  -> public getTopHatDomain
  -> public getHatLevel
-> public getAdminAtLevel


### public getAdminAtLocalLevel
_(no internal calls)_


### public getHatLevel
-> public getLocalHatLevel
-> public getTopHatDomain
-> public getHatLevel


### public getLocalHatLevel
_(no internal calls)_


### public getTippyTopHatDomain
-> public getTippyTopHatDomain
-> public getTopHatDomain


### public getTopHatDomain
_(no internal calls)_


### public isLocalTopHat
_(no internal calls)_


### public isTopHat
-> public isLocalTopHat
-> public getTopHatDomain


### public isValidHatId
-> public isLocalTopHat
-> public getLocalHatLevel


### public noCircularLinkage
-> public getTopHatDomain
-> public noCircularLinkage


### public sameTippyTopHatDomain
-> public getTippyTopHatDomain
  -> public getTippyTopHatDomain
  -> public getTopHatDomain
-> public getTopHatDomain

