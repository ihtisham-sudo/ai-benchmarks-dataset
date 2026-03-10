# Callpaths — MagicSea_Staking

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BaseRewarder

_File: src/rewarders/BaseRewarder.sol_

### public getCaller
_(no internal calls)_


### public getPendingReward
-> internal _token
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public getPid
-> internal _pid
  -> internal _getArgUint256
    -> internal _getImmutableArgsOffset


### public getRemainingReward
-> internal _balanceOfThis
-> internal _token
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public getRewarderParameter
-> internal _token
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public getToken
-> internal _token
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public initialize
_(no internal calls)_


### public isStopped
_(no internal calls)_


### public onModify
-> internal _pid
  -> internal _getArgUint256
    -> internal _getImmutableArgsOffset
-> internal _update


### public renounceOwnership
_(no internal calls)_


### public setRewardPerSecond
-> internal _setRewardParameters
  -> internal _balanceOfThis
  -> internal _token
    -> internal _getArgAddress
      -> internal _getImmutableArgsOffset


### public setRewarderParameters
-> internal _setRewardParameters
  -> internal _balanceOfThis
  -> internal _token
    -> internal _getArgAddress
      -> internal _getImmutableArgsOffset


### public stop
-> internal _setRewardParameters
  -> internal _balanceOfThis
  -> internal _token
    -> internal _getArgAddress
      -> internal _getImmutableArgsOffset


### public sweep
-> internal _balanceOfThis
-> internal _token
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset
-> internal _safeTransferTo


---

## Booster

_File: src/booster/Booster.sol_

### external addRewards
_(no internal calls)_


### external allowAccount
_(no internal calls)_


### external allowAccounts
_(no internal calls)_


### external burn
-> internal _updatePool
  -> public getMonthlyReward
  -> internal _rewardForSlices
-> private _burnTokens


### external deposit
-> internal _updatePool
  -> public getMonthlyReward
  -> internal _rewardForSlices
-> internal _computeSnapshotRewards
-> public timeToUnlock
-> internal lastBurnRound


### external disallowAccount
_(no internal calls)_


### external disallowAccounts
_(no internal calls)_


### external emergencyUnlock
-> public timeToUnlock
-> internal _computeSnapshotRewards
-> internal lastBurnRound
-> internal safeGoldenPearlTransfer
-> private _burnTokens


### external enableAllowlist
_(no internal calls)_


### public getMonthlyReward
_(no internal calls)_


### external getRewardSlice
_(no internal calls)_


### external getSnapshot
_(no internal calls)_


### external getUserInfo
-> internal _computeSnapshotRewards


### external harvest
-> internal _updatePool
  -> public getMonthlyReward
  -> internal _rewardForSlices
-> internal _computeSnapshotRewards
-> internal lastBurnRound
-> internal safeGoldenPearlTransfer


### external initialize
-> private _createMonthlyRewardSlices


### external nextClaimableBurn
_(no internal calls)_


### external pendingBurnReward
_(no internal calls)_


### external pendingReward
-> public getMonthlyReward
-> internal _rewardForSlices
-> internal _computeSnapshotRewards


### external rewardSlicesLength
_(no internal calls)_


### external snapshotsLength
_(no internal calls)_


### public timeToUnlock
_(no internal calls)_


### external updateBurnAfterTime
_(no internal calls)_


### external updateBurnPause
_(no internal calls)_


### external updateRewardFee
_(no internal calls)_


### external updateTimeLocked
_(no internal calls)_


### external updateWithdrawFee
_(no internal calls)_


### external usersLength
_(no internal calls)_


### external withdrawAndHarvest
-> public timeToUnlock
-> internal _computeSnapshotRewards
-> internal _updatePool
  -> public getMonthlyReward
  -> internal _rewardForSlices
-> internal lastBurnRound
-> internal safeGoldenPearlTransfer


---

## BribeRewarder

_File: src/rewarders/BribeRewarder.sol_

### public bribe
-> internal _bribe
  -> internal _checkAlreadyInitialized
  -> internal _calcTotalAmount
    -> internal _calcPeriods
  -> internal _balanceOfThis
  -> internal _token
    -> internal _getArgAddress
      -> internal _getImmutableArgsOffset
  -> internal _calcPeriods


### external claim
-> private _modify
  -> internal _indexByPeriodId
  -> internal _calculateRewards
  -> internal _token
    -> internal _getArgAddress
      -> internal _getImmutableArgsOffset
  -> internal _safeTransferTo
-> internal _pool
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public deposit
-> private _modify
  -> internal _indexByPeriodId
  -> internal _calculateRewards
  -> internal _token
    -> internal _getArgAddress
      -> internal _getImmutableArgsOffset
  -> internal _safeTransferTo
-> internal _pool
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### external fundAndBribe
-> internal _token
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset
-> internal _calcTotalAmount
  -> internal _calcPeriods
-> internal _bribe
  -> internal _checkAlreadyInitialized
  -> internal _calcTotalAmount
    -> internal _calcPeriods
  -> internal _balanceOfThis
  -> internal _token
    -> internal _getArgAddress
      -> internal _getImmutableArgsOffset
  -> internal _calcPeriods


### external getAmountPerPeriod
_(no internal calls)_


### external getBribePeriods
-> internal _pool
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public getCaller
_(no internal calls)_


### public getLastVotingPeriodId
_(no internal calls)_


### external getPendingReward
-> internal _indexByPeriodId
-> internal _calculateRewards


### public getPool
-> internal _pool
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public getStartVotingPeriodId
_(no internal calls)_


### public getToken
-> internal _token
  -> internal _getArgAddress
    -> internal _getImmutableArgsOffset


### public initialize
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


---

## FarmLens

_File: src/FarmLens.sol_

### external getBribe
_(no internal calls)_


### external getBribesForPool
_(no internal calls)_


### external getFarmData
_(no internal calls)_


### external getFarmInfo
-> public getMasterChefPendingRewardsAt
-> private _getRemainingReward


### public getMasterChefPendingRewardsAt
_(no internal calls)_


### external getPoolInfo
_(no internal calls)_


### external getRewardToken
_(no internal calls)_


### external getUserBribeRewardFor
_(no internal calls)_


### external getUserBribeRewards
-> internal _numberOfAllUserBribeRewards


### external getVoteData
_(no internal calls)_


### external getVoteInfoAt
_(no internal calls)_


---

## FarmZapper

_File: src/FarmZapper.sol_

### public checkWETH
_(no internal calls)_


### public estimateSwap
-> public checkWETH
-> private _getMasterChefPair
-> private _getSwapAmount


### external getMasterChef
_(no internal calls)_


### external getMinimumAmount
_(no internal calls)_


### external getRouter
_(no internal calls)_


### external getWNative
_(no internal calls)_


### external releaseStuckToken
_(no internal calls)_


### external zapIn
-> private _swapAndStake
  -> private _getMasterChefPair
  -> private _getSwapAmount
  -> private _approveTokenIfNeeded
  -> private _returnAssets


### external zapInWNative
-> private _swapAndStake
  -> private _getMasterChefPair
  -> private _getSwapAmount
  -> private _approveTokenIfNeeded
  -> private _returnAssets


### external zapOut
-> private _getPair
-> private _removeLiquidity
-> private _returnAssets


### external zapOutAndSwap
-> private _getPair
-> private _removeLiquidity
-> private _approveTokenIfNeeded
-> private _returnAssets


---

## MasterChef

_File: src/MasterchefV2.sol_

### external add
-> private _checkOwnerOrOperator
-> private _setExtraRewarder


### external claim
-> private _modify
  -> private _getRewardForPid
  -> private _mintLum
    -> private _calculateAmounts


### external deposit
-> private _modify
  -> private _getRewardForPid
  -> private _mintLum
    -> private _calculateAmounts


### external depositOnBehalf
-> private _modify
  -> private _getRewardForPid
  -> private _mintLum
    -> private _calculateAmounts


### external emergencyWithdraw
_(no internal calls)_


### external getDeposit
_(no internal calls)_


### external getExtraRewarder
_(no internal calls)_


### external getLBHooksManager
_(no internal calls)_


### external getLastUpdateTimestamp
_(no internal calls)_


### external getLum
_(no internal calls)_


### external getLumPerSecond
_(no internal calls)_


### external getLumPerSecondForPid
-> private _getRewardForPid


### external getMintLumFlag
_(no internal calls)_


### external getNumberOfFarms
_(no internal calls)_


### external getPendingRewards
-> private _calculateAmounts
-> private _getRewardForPid


### external getRewarderFactory
_(no internal calls)_


### external getToken
_(no internal calls)_


### external getTotalDeposit
_(no internal calls)_


### external getTreasury
_(no internal calls)_


### external getTreasuryShare
_(no internal calls)_


### external getVoter
_(no internal calls)_


### external initialize
-> private _setTreasury


### public renounceOwnership
_(no internal calls)_


### external setExtraRewarder
-> private _setExtraRewarder


### external setLumPerSecond
_(no internal calls)_


### external setMintLum
_(no internal calls)_


### external setTreasury
-> private _setTreasury


### external setTrustee
_(no internal calls)_


### external setVoter
_(no internal calls)_


### external updateAll
-> private _updateAll
  -> private _getRewardForPid
  -> private _mintLum
    -> private _calculateAmounts


### external updateOperator
_(no internal calls)_


### external withdraw
-> private _modify
  -> private _getRewardForPid
  -> private _mintLum
    -> private _calculateAmounts


---

## MasterChefRewarder

_File: src/rewarders/MasterChefRewarder.sol_

### public getCaller
_(no internal calls)_


### public getPendingReward
-> internal _token


### public getPid
-> internal _pid


### public getRemainingReward
-> internal _getTotalSupply
  -> internal _pid
-> internal _balanceOfThis
-> internal _token


### public getRewarderParameter
-> internal _token


### public getToken
-> internal _token


### public initialize
_(no internal calls)_


### public isStopped
_(no internal calls)_


### public link
-> internal _pid


### public onModify
-> external_callback BaseRewarder.onModify
-> internal _claim
  -> internal _token
  -> internal _safeTransferTo


### public renounceOwnership
_(no internal calls)_


### public setRewardPerSecond
-> internal _setRewardParameters
  -> internal _getTotalSupply
    -> internal _pid
  -> internal _balanceOfThis
  -> internal _token


### public setRewarderParameters
-> internal _setRewardParameters
  -> internal _getTotalSupply
    -> internal _pid
  -> internal _balanceOfThis
  -> internal _token


### public stop
_(no internal calls)_


### public sweep
-> internal _balanceOfThis
-> internal _token
-> internal _getTotalSupply
  -> internal _pid
-> internal _safeTransferTo


### public unlink
-> internal _pid


---

## MlumStaking

_File: src/MlumStaking.sol_

### external addToPosition
-> internal _requireOnlyOperatorOrOwnerOf
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _harvestPosition
  -> internal _safeRewardTransfer
-> internal _remainingLockTime
  -> internal _currentBlockTimestamp
-> internal _currentBlockTimestamp
-> public getMultiplierByLockDuration
  -> public isUnlocked
-> internal _transferSupportingFeeOnTransfer
-> internal _updateBoostMultiplierInfoAndRewardDebt


### external createPosition
-> public isUnlocked
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _transferSupportingFeeOnTransfer
-> internal _mintNextTokenId
-> public getMultiplierByLockDuration
  -> public isUnlocked
-> internal _currentBlockTimestamp


### external emergencyWithdraw
-> internal _requireOnlyOwnerOf
  -> internal _isOwnerOf
-> internal _currentBlockTimestamp
-> public isUnlocked
-> internal _destroyPosition


### external exists
_(no internal calls)_


### external extendLockPosition
-> internal _requireOnlyApprovedOrOwnerOf
  -> internal _isOwnerOf
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _lockPosition
  -> public isUnlocked
  -> internal _currentBlockTimestamp
  -> internal _harvestPosition
    -> internal _safeRewardTransfer
  -> public getMultiplierByLockDuration
    -> public isUnlocked
  -> internal _updateBoostMultiplierInfoAndRewardDebt


### public getMultiplierByLockDuration
-> public isUnlocked


### external getStakingPosition
_(no internal calls)_


### external harvestPosition
-> internal _requireOnlyApprovedOrOwnerOf
  -> internal _isOwnerOf
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _harvestPosition
  -> internal _safeRewardTransfer
-> internal _updateBoostMultiplierInfoAndRewardDebt


### external harvestPositionTo
-> internal _requireOnlyApprovedOrOwnerOf
  -> internal _isOwnerOf
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _harvestPosition
  -> internal _safeRewardTransfer
-> internal _updateBoostMultiplierInfoAndRewardDebt


### external harvestPositionsTo
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _requireOnlyApprovedOrOwnerOf
  -> internal _isOwnerOf
-> internal _harvestPosition
  -> internal _safeRewardTransfer
-> internal _updateBoostMultiplierInfoAndRewardDebt


### external hasDeposits
_(no internal calls)_


### external initialize
_(no internal calls)_


### external isUnlockOperator
_(no internal calls)_


### public isUnlocked
_(no internal calls)_


### external lastTokenId
_(no internal calls)_


### external pendingRewards
_(no internal calls)_


### external renewLockPosition
-> internal _requireOnlyApprovedOrOwnerOf
  -> internal _isOwnerOf
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _lockPosition
  -> public isUnlocked
  -> internal _currentBlockTimestamp
  -> internal _harvestPosition
    -> internal _safeRewardTransfer
  -> public getMultiplierByLockDuration
    -> public isUnlocked
  -> internal _updateBoostMultiplierInfoAndRewardDebt


### public safeTransferFrom
_(no internal calls)_


### external setEmergencyUnlock
-> internal _requireOnlyOwner


### external setLockMultiplierSettings
_(no internal calls)_


### external setOperator
-> internal _requireOnlyOwner


### external setUnlockOperator
-> internal _requireOnlyOwner


### public supportsInterface
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external unlockOperator
_(no internal calls)_


### external unlockOperatorsLength
_(no internal calls)_


### external updatePool
-> internal _updatePool
  -> internal _currentBlockTimestamp


### external withdrawFromPosition
-> internal _requireOnlyApprovedOrOwnerOf
  -> internal _isOwnerOf
-> internal _updatePool
  -> internal _currentBlockTimestamp
-> internal _withdrawFromPosition
  -> internal _currentBlockTimestamp
  -> public isUnlocked
  -> internal _harvestPosition
    -> internal _safeRewardTransfer
  -> internal _destroyPosition
  -> internal _updateBoostMultiplierInfoAndRewardDebt


---

## ProxyAdmin2Step

_File: src/transparent/ProxyAdmin2Step.sol_

### public renounceOwnership
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## RewarderFactory

_File: src/rewarders/RewarderFactory.sol_

### external createBribeRewarder
-> private _cloneBribe
  -> library ImmutableClone.cloneDeterministic


### external createRewarder
-> private _clone
  -> library ImmutableClone.cloneDeterministic


### external getRewarderAt
_(no internal calls)_


### external getRewarderCount
_(no internal calls)_


### external getRewarderImplementation
_(no internal calls)_


### external getRewarderType
_(no internal calls)_


### external initialize
-> private _setRewarderImplementation


### external setRewarderImplementation
-> private _setRewarderImplementation


---

## Voter

_File: src/Voter.sol_

### external createFarms
-> internal hasFarm


### external getBribeRewarderAt
_(no internal calls)_


### external getBribeRewarderLength
_(no internal calls)_


### external getCurrentVotingPeriod
_(no internal calls)_


### external getLatestFinishedPeriod
-> internal _votingEnded
  -> internal _votingStarted


### external getMasterChef
_(no internal calls)_


### external getMinimumLockTime
_(no internal calls)_


### external getMinimumVotesPerPool
_(no internal calls)_


### external getMlumStaking
_(no internal calls)_


### external getPeriodDuration
_(no internal calls)_


### external getPeriodStartEndtime
_(no internal calls)_


### external getPeriodStartTime
_(no internal calls)_


### external getPoolVotes
_(no internal calls)_


### external getPoolVotesPerPeriod
_(no internal calls)_


### external getTopPoolIds
_(no internal calls)_


### external getTotalVotes
_(no internal calls)_


### external getTotalWeight
_(no internal calls)_


### external getUserBribeRewaderAt
_(no internal calls)_


### external getUserBribeRewarderLength
_(no internal calls)_


### external getUserVotes
_(no internal calls)_


### external getVotedPools
_(no internal calls)_


### external getVotedPoolsAtIndex
_(no internal calls)_


### external getVotedPoolsLength
_(no internal calls)_


### external getVotesPerPeriod
_(no internal calls)_


### external getWeight
_(no internal calls)_


### external hasVoted
_(no internal calls)_


### external initialize
_(no internal calls)_


### external onRegister
-> internal _checkRegisterCaller


### external ownerOf
_(no internal calls)_


### external setTopPoolIdsWithWeights
_(no internal calls)_


### public startNewVotingPeriod
_(no internal calls)_


### external updateMinimumLockTime
_(no internal calls)_


### external updateMinimumVotesPerPool
_(no internal calls)_


### external updateOperator
_(no internal calls)_


### external updatePeriodDuration
_(no internal calls)_


### external updatePoolValidator
_(no internal calls)_


### external vote
-> internal _votingStarted
-> internal _votingEnded
  -> internal _votingStarted
-> private _notifyBribes

