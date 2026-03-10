# Callpaths — Eco_Op_Bridge

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ConfigureNotifierL2Rebase

_File: contracts/temp_proposals/configureNotifierL2Rebase.propo.sol_

### public description
_(no internal calls)_


### public enacted
_(no internal calls)_


### public name
_(no internal calls)_


### public url
_(no internal calls)_


---

## CrossDomainEnabledUpgradeable

_File: contracts/bridge/CrossDomainEnabledUpgradeable.sol_

### public __CrossDomainEnabledUpgradeable_init
_(no internal calls)_


---

## ERC20PermitUpgradeable

_File: contracts/token/ERC20PermitUpgradeable.sol_

### external DOMAIN_SEPARATOR
_(no internal calls)_


### public allowance
_(no internal calls)_


### public approve
-> internal _approve


### public balanceOf
_(no internal calls)_


### public decimals
_(no internal calls)_


### public decreaseAllowance
-> public allowance
-> internal _approve


### public increaseAllowance
-> internal _approve
-> public allowance


### public name
_(no internal calls)_


### public nonces
_(no internal calls)_


### public permit
-> internal _useNonce
-> internal _approve


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


### public transferFrom
-> internal _spendAllowance
  -> public allowance
  -> internal _approve
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


---

## ERC20Upgradeable

_File: contracts/token/ERC20Upgradeable.sol_

### public allowance
_(no internal calls)_


### public approve
-> internal _approve


### public balanceOf
_(no internal calls)_


### public decimals
_(no internal calls)_


### public decreaseAllowance
-> public allowance
-> internal _approve


### public increaseAllowance
-> internal _approve
-> public allowance


### public name
_(no internal calls)_


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


### public transferFrom
-> internal _spendAllowance
  -> public allowance
  -> internal _approve
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


---

## Faucet

_File: contracts/token/Faucet.sol_

### external batchDrip
_(no internal calls)_


### external drain
_(no internal calls)_


### external drip
_(no internal calls)_


### external updateApprovedOperator
_(no internal calls)_


### external updateDripAmount
_(no internal calls)_


### external updateSuperOperator
_(no internal calls)_


---

## FaucetStaging

_File: contracts/token/FaucetStaging.sol_

### external batchDrip
_(no internal calls)_


### external drain
_(no internal calls)_


### external drip
_(no internal calls)_


### external updateApprovedOperator
_(no internal calls)_


### external updateDripAmount
_(no internal calls)_


### external updateMultiDrip
_(no internal calls)_


### external updateSuperOperator
_(no internal calls)_


---

## InitialImplementation

_File: contracts/bridge/InitialImplementation.sol_

### public initialize
_(no internal calls)_


---

## L1ECOBridge

_File: contracts/bridge/L1ECOBridge.sol_

### public __CrossDomainEnabledUpgradeable_init
_(no internal calls)_


### external depositERC20
-> internal _initiateERC20Deposit
  -> internal sendCrossDomainMessage
    -> internal getCrossDomainMessenger


### external depositERC20To
-> internal _initiateERC20Deposit
  -> internal sendCrossDomainMessage
    -> internal getCrossDomainMessenger


### external finalizeERC20Withdrawal
-> internal sendCrossDomainMessage
  -> internal getCrossDomainMessenger


### public initialize
-> external_callback CrossDomainEnabledUpgradeable.__CrossDomainEnabledUpgradeable_init


### external rebase
-> internal sendCrossDomainMessage
  -> internal getCrossDomainMessenger


### external upgradeECO
-> internal sendCrossDomainMessage
  -> internal getCrossDomainMessenger


### external upgradeECOx
-> internal sendCrossDomainMessage
  -> internal getCrossDomainMessenger


### external upgradeL2Bridge
-> internal sendCrossDomainMessage
  -> internal getCrossDomainMessenger


### external upgradeSelf
_(no internal calls)_


---

## L2ECO

_File: contracts/token/L2ECO.sol_

### external DOMAIN_SEPARATOR
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external burn
_(no internal calls)_


### public initialize
-> external_callback ERC20Upgradeable.__ERC20_init
-> external_callback ERC20PermitUpgradeable.__ERC20Permit_init


### external mint
_(no internal calls)_


### public nonces
_(no internal calls)_


### public permit
-> internal _useNonce


### external rebase
-> internal _rebase


### external supportsInterface
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public updateBurners
_(no internal calls)_


### public updateMinters
_(no internal calls)_


### public updateRebasers
_(no internal calls)_


### public updateTokenRoleAdmin
_(no internal calls)_


---

## L2ECOBridge

_File: contracts/bridge/L2ECOBridge.sol_

### public __CrossDomainEnabledUpgradeable_init
_(no internal calls)_


### external finalizeDeposit
_(no internal calls)_


### public initialize
-> external_callback CrossDomainEnabledUpgradeable.__CrossDomainEnabledUpgradeable_init


### external rebase
_(no internal calls)_


### external upgradeECO
_(no internal calls)_


### external upgradeECOx
_(no internal calls)_


### external upgradeSelf
_(no internal calls)_


### external withdraw
-> internal _initiateWithdrawal
  -> internal sendCrossDomainMessage
    -> internal getCrossDomainMessenger


### external withdrawTo
-> internal _initiateWithdrawal
  -> internal sendCrossDomainMessage
    -> internal getCrossDomainMessenger


---

## L2ECOx

_File: contracts/token/L2ECOx.sol_

### public allowance
_(no internal calls)_


### public approve
-> internal _approve


### public balanceOf
_(no internal calls)_


### external burn
-> internal _burn
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


### public decimals
_(no internal calls)_


### public decreaseAllowance
-> public allowance
-> internal _approve


### public increaseAllowance
-> internal _approve
-> public allowance


### public initialize
-> external_callback ERC20Upgradeable.__ERC20_init
  -> internal __ERC20_init_unchained


### external mint
-> internal _mint
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


### public name
_(no internal calls)_


### external supportsInterface
_(no internal calls)_


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


### public transferFrom
-> internal _spendAllowance
  -> public allowance
  -> internal _approve
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


### public updateBurners
_(no internal calls)_


### public updateMinters
_(no internal calls)_


### public updateTokenRoleAdmin
_(no internal calls)_


---

## TokenInitial

_File: contracts/token/TokenInitial.sol_

### public initialize
_(no internal calls)_


---

## TriggerL2Upgrade

_File: contracts/temp_proposals/triggerL2Upgrade.propo.sol_

### public description
_(no internal calls)_


### public enacted
_(no internal calls)_


### public name
_(no internal calls)_


### public url
_(no internal calls)_

