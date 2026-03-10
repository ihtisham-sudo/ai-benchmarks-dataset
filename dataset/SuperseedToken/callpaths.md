# Callpaths — SuperseedToken

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AccessControl

_File: src/supersale/dependencies/openzeppelin/access/AccessControl.sol_

### public getRoleAdmin
_(no internal calls)_


### public grantRole
-> internal _grantRole
  -> public hasRole


### public hasRole
_(no internal calls)_


### public renounceRole
-> internal _revokeRole
  -> public hasRole


### public revokeRole
-> internal _revokeRole
  -> public hasRole


### public supportsInterface
_(no internal calls)_


---

## ERC165

_File: src/supersale/dependencies/openzeppelin/utils/introspection/ERC165.sol_

### public supportsInterface
_(no internal calls)_


---

## ERC20

_File: src/supersale/dependencies/openzeppelin/token/ERC20/ERC20.sol_

### public allowance
_(no internal calls)_


### public approve
-> internal _msgSender
-> internal _approve


### public balanceOf
_(no internal calls)_


### public decimals
_(no internal calls)_


### public name
_(no internal calls)_


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> internal _msgSender
-> internal _transfer
  -> internal _update


### public transferFrom
-> internal _msgSender
-> internal _spendAllowance
  -> public allowance
  -> internal _approve
-> internal _transfer
  -> internal _update


---

## MintManager

_File: src/token/MintManager.sol_

### external mint
_(no internal calls)_


---

## Pausable

_File: src/supersale/dependencies/openzeppelin/utils/Pausable.sol_

### public paused
_(no internal calls)_


---

## SuperSaleDeposit

_File: src/supersale/SuperSaleDeposit.sol_

### external depositUSDC
-> private _verifyDepositConditions
  -> private _verifyUser
    -> library MerkleProof.verify
-> private _purchase
  -> private _calculateTokensToTransfer
    -> private _computeTokens
  -> private _getRemainingCap
  -> internal _pause


### external depositUSDT
-> private _verifyDepositConditions
  -> private _verifyUser
    -> library MerkleProof.verify
-> private _purchase
  -> private _calculateTokensToTransfer
    -> private _computeTokens
  -> private _getRemainingCap
  -> internal _pause


### external getCurrentStage
-> private _getCurrentStage


### external getRemainingCap
-> private _getRemainingCap


### external getRemainingDepositAmount
_(no internal calls)_


### public getRoleAdmin
_(no internal calls)_


### public grantRole
-> internal _grantRole
  -> public hasRole


### public hasRole
_(no internal calls)_


### external pause
-> internal _pause


### public paused
_(no internal calls)_


### public renounceRole
-> internal _revokeRole
  -> public hasRole


### public revokeRole
-> internal _revokeRole
  -> public hasRole


### external setMerkleRoot
-> private _setMerkleRoot


### external setSaleParameters
_(no internal calls)_


### external setSaleSchedule
_(no internal calls)_


### public setTiers
-> private _setTiers


### public supportsInterface
_(no internal calls)_


### external unpause
-> internal _unpause


### external verifyUser
-> private _verifyUser
  -> library MerkleProof.verify


### external withdrawAssets
_(no internal calls)_


---

## SuperseedToken

_File: src/token/SuperseedToken.sol_

### public getRoleAdmin
_(no internal calls)_


### public grantRole
-> internal _grantRole
  -> public hasRole


### public hasRole
_(no internal calls)_


### external mint
_(no internal calls)_


### public nonces
_(no internal calls)_


### public renounceRole
-> internal _revokeRole
  -> public hasRole


### public revokeRole
-> internal _revokeRole
  -> public hasRole


### public supportsInterface
_(no internal calls)_


---

## TokenClaim

_File: src/claim/TokenClaim.sol_

### external claim
-> library MerkleProof.verify


### external setMerkleRoot
-> private _setMerkleRoot


### external withdraw
_(no internal calls)_

