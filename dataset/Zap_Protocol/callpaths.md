# Callpaths — Zap_Protocol

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Admin

_File: contracts/Admin.sol_

### external addOperator
_(no internal calls)_


### external addToBlackList
_(no internal calls)_


### external createPoolNew
-> internal _checkingParams
-> internal _addToSales


### external getParams
_(no internal calls)_


### external getTokenSales
_(no internal calls)_


### external getTokenSalesCount
_(no internal calls)_


### public initialize
_(no internal calls)_


### external removeClaimBlock
_(no internal calls)_


### external removeOperator
_(no internal calls)_


### external setClaimBlock
_(no internal calls)_


### external setMasterContractETH
_(no internal calls)_


### external setMasterContractUSDB
_(no internal calls)_


### public setPlatformFee
_(no internal calls)_


### public setPlatformTax
_(no internal calls)_


### public setUserKYC
_(no internal calls)_


### external setWallet
_(no internal calls)_


---

## CalHash

_File: contracts/CalHash.sol_

### public getInitHash
_(no internal calls)_


---

## CallHash

_File: contracts/CallHash.sol_

### public getInitHash
_(no internal calls)_


---

## OwnedUpgradeabilityProxy

_File: contracts/OwnedUpgradeabilityProxy.sol_

### public implementation
_(no internal calls)_


### public maintenance
_(no internal calls)_


### public proxyOwner
_(no internal calls)_


### external setMaintenance
_(no internal calls)_


### public transferProxyOwnership
-> public proxyOwner
-> internal setUpgradeabilityOwner


### public upgradeTo
-> internal _upgradeTo
  -> public implementation
  -> internal setImplementation


### public upgradeToAndCall
-> public upgradeTo
  -> internal _upgradeTo
    -> public implementation
    -> internal setImplementation


---

## ReflectionToken

_File: contracts/ReflectionToken.sol_

### public addPair
_(no internal calls)_


### public allowance
_(no internal calls)_


### public approve
-> private _approveto


### public balanceOf
-> public tokenFromReflection
  -> private _getRate
    -> private _getCurrentSupply


### public decreaseAllowanceto
-> private _approveto


### public excludeFromFee
_(no internal calls)_


### public excludeFromReward
-> public tokenFromReflection
  -> private _getRate
    -> private _getCurrentSupply


### public includeInFee
_(no internal calls)_


### external includeInReward
_(no internal calls)_


### public increaseAllowanceto
-> private _approveto


### public isBot
_(no internal calls)_


### public isExcludedFromFee
_(no internal calls)_


### public isExcludedFromReward
_(no internal calls)_


### public isPair
_(no internal calls)_


### public removePair
_(no internal calls)_


### public rescueAnyERC20Tokens
_(no internal calls)_


### external rescueETH
_(no internal calls)_


### external setAntibot
_(no internal calls)_


### public setTaxes
_(no internal calls)_


### public tokenFromReflection
-> private _getRate
  -> private _getCurrentSupply


### public totalSupply
_(no internal calls)_


### public transfer
-> private _transferto
  -> public balanceOf
    -> public tokenFromReflection
      -> private _getRate
        -> private _getCurrentSupply
  -> private _tokenTransfer
    -> private _getValues
      -> private _getTValues
      -> private _getRValues
      -> private _getRate
        -> private _getCurrentSupply
    -> private _reflectReflection


### public transferFrom
-> private _transferto
  -> public balanceOf
    -> public tokenFromReflection
      -> private _getRate
        -> private _getCurrentSupply
  -> private _tokenTransfer
    -> private _getValues
      -> private _getTValues
      -> private _getRValues
      -> private _getRate
        -> private _getCurrentSupply
    -> private _reflectReflection
-> private _approveto


### external updateCoolDownSettings
_(no internal calls)_


### external updateRouterAndPair
-> public addPair


---

## Token

_File: contracts/Token.sol_

### external changeDecimals
_(no internal calls)_


### public decimals
_(no internal calls)_


### external mint
_(no internal calls)_


---

## TokenA

_File: contracts/TokenA.sol_

### external mint
_(no internal calls)_


---

## TokenSaleETH

_File: contracts/TokenSaleETH.sol_

### external addLiq
_(no internal calls)_


### external canClaim
-> internal _claim


### external claim
-> internal _claim
-> internal ETHTransfer


### external claimLP
_(no internal calls)_


### external deposit
-> internal checkingEpoch
-> internal _processPrivate


### external initialize
_(no internal calls)_


### external setConfig
_(no internal calls)_


### external takeLocked
-> internal _onlyAdmin
-> internal ETHTransfer


### public takeUSDBRaised
-> internal checkingEpoch
-> internal ETHTransfer


### public userWhitelistAllocation
_(no internal calls)_


### external vesting
-> internal _claim


---

## TokenSaleUSDB

_File: contracts/TokenSaleUSDB.sol_

### external addLiq
-> external_callback USDB.approve


### external canClaim
-> internal _claim


### external claim
-> internal _claim
-> external_callback USDB.balanceOf
-> external_callback USDB.safeTransfer


### external claimLP
_(no internal calls)_


### external deposit
-> internal checkingEpoch
-> internal _processPrivate
  -> external_callback USDB.safeTransferFrom


### external initialize
_(no internal calls)_


### external setConfig
_(no internal calls)_


### external setUSDB
_(no internal calls)_


### external takeLocked
-> internal _onlyAdmin
-> external_callback USDB.balanceOf
-> external_callback USDB.safeTransfer


### public takeUSDBRaised
-> internal checkingEpoch
-> external_callback USDB.safeTransfer


### public userWhitelistAllocation
_(no internal calls)_


### external vesting
-> internal _claim
-> external_callback USDB.decimals


---

## USDB

_File: contracts/USDB.sol_

### external mint
_(no internal calls)_


---

## WETH

_File: contracts/WETH9.sol_

### public approve
_(no internal calls)_


### public deposit
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> public transferFrom


### public transferFrom
_(no internal calls)_


### public withdraw
_(no internal calls)_

