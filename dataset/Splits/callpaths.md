# Callpaths — Splits

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## SplitMain

_File: contracts/SplitMain.sol_

### external acceptControl
_(no internal calls)_


### external cancelControlTransfer
_(no internal calls)_


### external createSplit
-> internal _hashSplit
-> library Clones.cloneDeterministic
-> library Clones.clone


### external distributeERC20
-> internal _validSplitHash
  -> internal _hashSplit
-> internal _distributeERC20
  -> internal _scaleAmountByPercentage


### external distributeETH
-> internal _validSplitHash
  -> internal _hashSplit
-> internal _distributeETH
  -> internal _scaleAmountByPercentage


### external getController
_(no internal calls)_


### external getERC20Balance
_(no internal calls)_


### external getETHBalance
_(no internal calls)_


### external getHash
_(no internal calls)_


### external getNewPotentialController
_(no internal calls)_


### external makeSplitImmutable
_(no internal calls)_


### external predictImmutableSplitAddress
-> internal _hashSplit
-> library Clones.predictDeterministicAddress


### external transferControl
_(no internal calls)_


### external updateAndDistributeERC20
-> internal _updateSplit
  -> internal _hashSplit
-> internal _distributeERC20
  -> internal _scaleAmountByPercentage


### external updateAndDistributeETH
-> internal _updateSplit
  -> internal _hashSplit
-> internal _distributeETH
  -> internal _scaleAmountByPercentage


### external updateSplit
-> internal _updateSplit
  -> internal _hashSplit


### external withdraw
-> internal _withdraw
-> internal _withdrawERC20


---

## SplitWallet

_File: contracts/SplitWallet.sol_

### external sendERC20ToMain
_(no internal calls)_


### external sendETHToMain
_(no internal calls)_

