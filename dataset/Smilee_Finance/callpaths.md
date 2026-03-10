# Callpaths — Smilee_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## GBera

_File: src/GBera.sol_

### public approveShares
-> internal _sharesToAssets
  -> internal _totalAssets


### public balanceOf
-> internal _sharesToAssets
  -> internal _totalAssets


### public balanceOfShares
_(no internal calls)_


### public burnShares
_(no internal calls)_


### external completeWithdrawal
_(no internal calls)_


### public deposit
-> public totalSupply
  -> internal _sharesToAssets
    -> internal _totalAssets
-> internal _assetsToShares
  -> internal _totalAssets


### external getRebasedAmount
-> internal _sharesToAssets
  -> internal _totalAssets


### external getUnrebasedAmount
-> internal _assetsToShares
  -> internal _totalAssets


### public initialize
_(no internal calls)_


### external requestWithdrawal
-> internal _assetsToShares
  -> internal _totalAssets
-> public totalShares
-> public balanceOfShares
-> public transferShares
  -> internal _transferShares


### external setAssetManager
_(no internal calls)_


### external setWithdrawalEnabled
_(no internal calls)_


### external setWithdrawalQueue
_(no internal calls)_


### external sharePrice
-> internal _totalAssets


### public totalShares
_(no internal calls)_


### public totalSupply
-> internal _sharesToAssets
  -> internal _totalAssets


### public transferShares
-> internal _transferShares


### public transferSharesFrom
-> internal _sharesToAssets
  -> internal _totalAssets
-> internal _transferShares


---

## GBeraAssetManager

_File: src/GBeraAssetManager.sol_

### external activateBoost
_(no internal calls)_


### external cancelBoost
_(no internal calls)_


### external cancelDropBoost
_(no internal calls)_


### external cancelOperatorChange
_(no internal calls)_


### public collectNodeFeeRewards
-> internal _accrueProtocolFees


### public collectStakerRewards
-> internal _accrueProtocolFees


### external deposit
-> internal _deposit


### external dropBoost
_(no internal calls)_


### public initialize
_(no internal calls)_


### external processWithdrawalQueue
_(no internal calls)_


### external protocolFees
_(no internal calls)_


### external queueBoost
_(no internal calls)_


### external queueDropBoost
_(no internal calls)_


### external queueNewRewardAllocation
_(no internal calls)_


### external redeemBGT
-> public updateBgtFees
  -> internal _accrueProtocolFees


### external requestOperatorChange
_(no internal calls)_


### external setFeePercentage
-> public updateBgtFees
  -> internal _accrueProtocolFees
-> public collectStakerRewards
  -> internal _accrueProtocolFees
-> public collectNodeFeeRewards
  -> internal _accrueProtocolFees


### external setNodeFeeReceiver
_(no internal calls)_


### external setNodeFeeUnlockTime
_(no internal calls)_


### external totalAssets
_(no internal calls)_


### public updateBgtFees
-> internal _accrueProtocolFees


### external withdrawProtocolFees
_(no internal calls)_


### external withdrawWithdrawals
_(no internal calls)_


---

## NodeFeeReceiver

_File: src/NodeFeeReceiver.sol_

### external collectRewards
_(no internal calls)_


### external earned
_(no internal calls)_


### external setUnlockTime
_(no internal calls)_


### external updateReward
_(no internal calls)_


---

## NodeRegistry

_File: src/NodeRegistry.sol_

### external createNode
-> internal _withdrawalAddressToCredentials


### external deallocateNode
-> internal _decreaseNodeStake


### external getAllNodes
_(no internal calls)_


### external getLastNodePK
_(no internal calls)_


### external getNodeData
_(no internal calls)_


### external increaseNodeStake
_(no internal calls)_


### public initialize
_(no internal calls)_


### external registerWithdrawal
-> internal _decreaseNodeStake


### external setMaxAllocation
_(no internal calls)_


### external setNodeActivationStatus
_(no internal calls)_


---

## NodeWithdrawalVault

_File: src/NodeWithdrawalVault.sol_

### external withdrawWithdrawals
_(no internal calls)_


---

## WithdrawalQueue

_File: src/WithdrawalQueue.sol_

### external claimBera
_(no internal calls)_


### public initialize
_(no internal calls)_


### external processQueue
_(no internal calls)_


### external submitRequest
_(no internal calls)_

