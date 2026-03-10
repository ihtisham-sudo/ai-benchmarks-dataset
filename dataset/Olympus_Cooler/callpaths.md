# Callpaths — Olympus_Cooler

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Clearinghouse

_File: src/Clearinghouse.sol_

### external claimDefaulted
-> public interestFromDebt


### external configureDependencies
_(no internal calls)_


### public debtForCollateral
_(no internal calls)_


### public defund
_(no internal calls)_


### external emergencyShutdown
-> public defund


### public interestFromDebt
_(no internal calls)_


### external isCoolerCallback
_(no internal calls)_


### external lendToCooler
-> public rebalance
  -> internal _sweepIntoDSR
-> public debtForCollateral


### external onDefault
-> internal _onDefault


### external onRepay
-> internal _onRepay
  -> internal _sweepIntoDSR


### external onRoll
-> internal _onRoll


### external reactivate
_(no internal calls)_


### public rebalance
-> internal _sweepIntoDSR


### external requestPermissions
_(no internal calls)_


### external rollLoan
_(no internal calls)_


### public sweepIntoDSR
-> internal _sweepIntoDSR


---

## Cooler

_File: src/Cooler.sol_

### external approveTransfer
_(no internal calls)_


### external claimDefaulted
-> public collateral
-> public factory


### external claimRepaid
-> public debt


### external clearRequest
-> public interestFor
-> public collateralFor
  -> public collateral
-> public debt
-> public owner
-> public factory


### public collateral
_(no internal calls)_


### public collateralFor
-> public collateral


### public debt
_(no internal calls)_


### external delegateVoting
-> public owner
-> public collateral


### public factory
_(no internal calls)_


### external getLoan
_(no internal calls)_


### external getRequest
_(no internal calls)_


### public interestFor
_(no internal calls)_


### external isActive
_(no internal calls)_


### external isDefaulted
_(no internal calls)_


### public newCollateralFor
-> public collateralFor
  -> public collateral


### public owner
_(no internal calls)_


### external provideNewTermsForRoll
_(no internal calls)_


### external repayLoan
-> public debt
-> public collateral
-> public owner
-> public factory


### external requestLoan
-> public collateral
-> public collateralFor
  -> public collateral
-> public factory


### external rescindRequest
-> public owner
-> public collateral
-> public collateralFor
  -> public collateral
-> public factory


### external rollLoan
-> public newCollateralFor
  -> public collateralFor
    -> public collateral
-> public interestFor
-> public collateral


### external setDirectRepay
_(no internal calls)_


### external transferOwnership
_(no internal calls)_


---

## CoolerCallback

_File: src/CoolerCallback.sol_

### external isCoolerCallback
_(no internal calls)_


### external onDefault
_(no internal calls)_


### external onRepay
_(no internal calls)_


### external onRoll
_(no internal calls)_


---

## CoolerFactory

_File: src/CoolerFactory.sol_

### external generateCooler
_(no internal calls)_


### external newEvent
_(no internal calls)_

