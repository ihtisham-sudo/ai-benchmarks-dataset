# Callpaths — Truflation

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ERC677Token

_File: src/token/ERC677Token.sol_

### public transferAndCall
-> private _contractFallback


---

## StakingRewards

_File: src/staking/StakingRewards.sol_

### external balanceOf
_(no internal calls)_


### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable


### external exit
-> public withdraw
-> public getReward


### public getReward
_(no internal calls)_


### external getRewardForDuration
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### external notifyRewardAmount
_(no internal calls)_


### external recoverERC20
_(no internal calls)_


### public rewardPerToken
-> public lastTimeRewardApplicable


### external setRewardsDistribution
_(no internal calls)_


### external setRewardsDuration
_(no internal calls)_


### external stake
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## TfiBurn

_File: src/token/TfiBurn.sol_

### external burnOldTfi
_(no internal calls)_


---

## TrufMigrator

_File: src/token/TrufMigrator.sol_

### external migrate
_(no internal calls)_


### external setMerkleRoot
_(no internal calls)_


### external withdrawTruf
_(no internal calls)_


---

## TrufPartner

_File: src/TrufPartner.sol_

### external cancel
-> internal _updateRewardDebt


### external end
-> internal _updateRewardDebt


### external initiate
_(no internal calls)_


### external pay
-> internal _updateRewardDebt


---

## TrufVesting

_File: src/token/TrufVesting.sol_

### external cancelVesting
-> public claimable
  -> public getEmission


### public claim
-> public claimable
  -> public getEmission


### public claimable
-> public getEmission


### external extendStaking
_(no internal calls)_


### public getEmission
_(no internal calls)_


### external getEmissionSchedule
_(no internal calls)_


### external migrateUser
_(no internal calls)_


### external multicall
_(no internal calls)_


### public setEmissionSchedule
_(no internal calls)_


### public setUserVesting
_(no internal calls)_


### external setVeTruf
_(no internal calls)_


### public setVestingCategory
_(no internal calls)_


### public setVestingInfo
_(no internal calls)_


### external stake
_(no internal calls)_


### external unstake
_(no internal calls)_


---

## TruflationToken

_File: src/token/TruflationToken.sol_

### public transferAndCall
-> private _contractFallback


---

## TruflationTokenCCIP

_File: src/token/TruflationTokenCCIP.sol_

### external burn
_(no internal calls)_


### external mint
_(no internal calls)_


### external setCcipPool
_(no internal calls)_


### public transferAndCall
-> private _contractFallback


---

## VirtualStakingRewards

_File: src/staking/VirtualStakingRewards.sol_

### external balanceOf
_(no internal calls)_


### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable


### external exit
-> public withdraw
-> public getReward


### public getReward
_(no internal calls)_


### external getRewardForDuration
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### external notifyRewardAmount
_(no internal calls)_


### public rewardPerToken
-> public lastTimeRewardApplicable


### external setOperator
_(no internal calls)_


### external setRewardsDistribution
_(no internal calls)_


### external setRewardsDuration
_(no internal calls)_


### external stake
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## VotingEscrowTruf

_File: src/token/VotingEscrowTruf.sol_

### external claimReward
_(no internal calls)_


### external extendLock
-> internal _extendLock
  -> public previewPoints


### external extendVestingLock
-> internal _extendLock
  -> public previewPoints


### external migrateVestingLock
_(no internal calls)_


### public previewPoints
_(no internal calls)_


### external stake
-> internal _stake
  -> public previewPoints


### external stakeVesting
-> internal _stake
  -> public previewPoints


### external unstake
-> internal _unstake


### external unstakeVesting
-> internal _unstake

