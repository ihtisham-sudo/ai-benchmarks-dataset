# Callpaths — Predicate

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AdvancedVault

_File: examples/inheritance/AdvancedVault.sol_

### external deposit
_(no internal calls)_


### external depositAndLock
-> internal _authorizeTransaction
  -> private _getPredicateClientStorage


### external getPolicyID
-> internal _getPolicyID
  -> private _getPredicateClientStorage


### external getRegistry
-> internal _getRegistry
  -> private _getPredicateClientStorage


### external setPolicyID
-> internal _setPolicyID
  -> private _getPredicateClientStorage


### external setRegistry
-> internal _setRegistry
  -> private _getPredicateClientStorage


### external transfer
-> internal _authorizeTransaction
  -> private _getPredicateClientStorage
-> internal _executeTransfer


### external withdraw
-> internal _authorizeTransaction
  -> private _getPredicateClientStorage
-> internal _executeWithdraw


### external withdrawTo
-> internal _authorizeTransaction
  -> private _getPredicateClientStorage
-> internal _executeWithdraw


---

## BasicPredicateClient

_File: mixins/BasicPredicateClient.sol_

### external getPolicyID
-> internal _getPolicyID
  -> private _getPredicateClientStorage


### external getRegistry
-> internal _getRegistry
  -> private _getPredicateClientStorage


---

## BasicVault

_File: examples/inheritance/BasicVault.sol_

### external deposit
_(no internal calls)_


### external getPolicyID
-> internal _getPolicyID
  -> private _getPredicateClientStorage


### external getRegistry
-> internal _getRegistry
  -> private _getPredicateClientStorage


### external setPolicyID
-> internal _setPolicyID
  -> private _getPredicateClientStorage


### external setRegistry
-> internal _setRegistry
  -> private _getPredicateClientStorage


### external withdraw
-> internal _authorizeTransaction
  -> private _getPredicateClientStorage


---

## MetaCoin

_File: examples/proxy/MetaCoin.sol_

### external disablePredicateProxy
-> internal _disablePredicateProxy
  -> private _getPredicateProtectedStorage


### external enablePredicateProxy
-> internal _enablePredicateProxy
  -> private _getPredicateProtectedStorage


### public getBalance
_(no internal calls)_


### external getPredicateProxy
-> private _getPredicateProtectedStorage


### external sendCoin
-> internal _sendCoin


### external setPredicateProxy
-> internal _setPredicateProxy
  -> private _getPredicateProtectedStorage


---

## PredicateClient

_File: mixins/PredicateClient.sol_

### external getPolicyID
-> internal _getPolicyID
  -> private _getPredicateClientStorage


### external getRegistry
-> internal _getRegistry
  -> private _getPredicateClientStorage


---

## PredicateClientProxy

_File: examples/proxy/PredicateClientProxy.sol_

### external getPolicyID
-> internal _getPolicyID
  -> private _getPredicateClientStorage


### external getRegistry
-> internal _getRegistry
  -> private _getPredicateClientStorage


### external proxySendCoin
-> internal _authorizeTransaction
  -> private _getPredicateClientStorage


### external setPolicyID
-> internal _setPolicyID
  -> private _getPredicateClientStorage


### public setRegistry
-> internal _setRegistry
  -> private _getPredicateClientStorage


---

## PredicateHolding

_File: examples/inheritance/PredicateHolding.sol_

### external getPolicyID
-> internal _getPolicyID
  -> private _getPredicateClientStorage


### external getRegistry
-> internal _getRegistry
  -> private _getPredicateClientStorage


### external setPolicyID
-> internal _setPolicyID
  -> private _getPredicateClientStorage


### public setRegistry
-> internal _setRegistry
  -> private _getPredicateClientStorage


---

## PredicateProtected

_File: examples/proxy/PredicateProtected.sol_

### external getPredicateProxy
-> private _getPredicateProtectedStorage


---

## PredicateRegistry

_File: PredicateRegistry.sol_

### external deregisterAttester
_(no internal calls)_


### external getPolicyID
_(no internal calls)_


### external getRegisteredAttesters
_(no internal calls)_


### public hashStatementSafe
_(no internal calls)_


### public hashStatementWithExpiry
_(no internal calls)_


### external initialize
_(no internal calls)_


### external migrateAttesterIndices
_(no internal calls)_


### external registerAttester
_(no internal calls)_


### external setPolicyID
_(no internal calls)_


### external validateAttestation
-> public hashStatementSafe

