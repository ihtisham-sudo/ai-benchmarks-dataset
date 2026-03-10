# Callpaths — Kwenta_Staking_Contracts

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BatchClaimer

_File: contracts/misc/BatchClaimer.sol_

### external claimMultiple
_(no internal calls)_


---

## ERC20

_File: contracts/utils/ERC20.sol_

### public allowance
_(no internal calls)_


### public approve
-> internal _approve
-> internal _msgSender


### public balanceOf
_(no internal calls)_


### public decimals
_(no internal calls)_


### public decreaseAllowance
-> internal _msgSender
-> internal _approve


### public increaseAllowance
-> internal _approve
-> internal _msgSender


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
-> internal _msgSender


### public transferFrom
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer
-> internal _msgSender
-> internal _approve


---

## EscrowDistributor

_File: contracts/EscrowDistributor.sol_

### external distributeEscrowed
_(no internal calls)_


---

## EscrowMigrator

_File: contracts/EscrowMigrator.sol_

### external getRegisteredVestingEntry
_(no internal calls)_


### external getRegisteredVestingEntryIDs
-> public numberOfRegisteredEntries


### external getRegisteredVestingSchedules
-> public numberOfRegisteredEntries


### external initialize
_(no internal calls)_


### external migrateEntries
-> internal _migrateEntries
  -> internal _checkIfMigrationAllowed
    -> internal _deadlinePassed
  -> internal _payForMigration
    -> public toPay
  -> external_callback IRewardEscrowV2.VestingEntry


### external migrateIntegratorEntries
-> internal _migrateEntries
  -> internal _checkIfMigrationAllowed
    -> internal _deadlinePassed
  -> internal _payForMigration
    -> public toPay
  -> external_callback IRewardEscrowV2.VestingEntry


### external numberOfMigratedEntries
_(no internal calls)_


### public numberOfRegisteredEntries
_(no internal calls)_


### external pauseEscrowMigrator
_(no internal calls)_


### external recoverExcessFunds
_(no internal calls)_


### external registerEntries
-> internal _registerEntries
  -> internal _deadlinePassed


### external registerIntegratorEntries
-> internal _registerEntries
  -> internal _deadlinePassed


### external setTreasuryDAO
_(no internal calls)_


### public toPay
_(no internal calls)_


### public totalEscrowMigrated
_(no internal calls)_


### public totalEscrowRegistered
_(no internal calls)_


### public totalEscrowUnmigrated
_(no internal calls)_


### external unpauseEscrowMigrator
_(no internal calls)_


### public updateTotalLocked
-> internal _deadlinePassed
-> public totalEscrowUnmigrated


---

## EscrowedMultipleMerkleDistributor

_File: contracts/EscrowedMultipleMerkleDistributor.sol_

### external acceptOwnership
_(no internal calls)_


### public claim
-> public isClaimed
-> private _setClaimed


### external claimMultiple
-> public claim
  -> public isClaimed
  -> private _setClaimed


### public isClaimed
_(no internal calls)_


### external nominateNewOwner
_(no internal calls)_


### external setMerkleRootForEpoch
_(no internal calls)_


---

## Kwenta

_File: contracts/Kwenta.sol_

### external acceptOwnership
_(no internal calls)_


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
-> internal _approve


### public increaseAllowance
-> internal _approve


### external mint
-> internal _mint
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer


### public name
_(no internal calls)_


### external nominateNewOwner
_(no internal calls)_


### external setSupplySchedule
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
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer
-> internal _approve


---

## LPRewards

_File: contracts/misc/LPRewards.sol_

### external balanceOf
_(no internal calls)_


### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable


### external escrowedBalanceOf
_(no internal calls)_


### external exit
-> public unstake
  -> public nonEscrowedBalanceOf
-> public nonEscrowedBalanceOf
-> public getReward


### public getReward
_(no internal calls)_


### external getRewardForDuration
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### public nonEscrowedBalanceOf
_(no internal calls)_


### external notifyRewardAmount
_(no internal calls)_


### external pauseStakingRewards
_(no internal calls)_


### external recoverERC20
_(no internal calls)_


### public rewardPerToken
-> public lastTimeRewardApplicable


### external setRewardsDuration
_(no internal calls)_


### external stake
_(no internal calls)_


### external stakeEscrow
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### external unpauseStakingRewards
_(no internal calls)_


### public unstake
-> public nonEscrowedBalanceOf


### external unstakeEscrow
_(no internal calls)_


---

## MultipleMerkleDistributor

_File: contracts/MultipleMerkleDistributor.sol_

### external acceptOwnership
_(no internal calls)_


### public claim
-> public isClaimed
-> private _setClaimed


### external claimMultiple
-> public claim
  -> public isClaimed
  -> private _setClaimed


### public isClaimed
_(no internal calls)_


### external nominateNewOwner
_(no internal calls)_


### external setMerkleRootForEpoch
_(no internal calls)_


---

## Owned

_File: contracts/utils/Owned.sol_

### external acceptOwnership
_(no internal calls)_


### external nominateNewOwner
_(no internal calls)_


---

## RewardEscrow

_File: contracts/RewardEscrow.sol_

### external acceptOwnership
_(no internal calls)_


### external appendVestingEntry
-> internal _appendVestingEntry
  -> library VestingEntries.VestingEntry


### public balanceOf
_(no internal calls)_


### external createEscrowEntry
-> internal _appendVestingEntry
  -> library VestingEntries.VestingEntry


### external getAccountVestingEntryIDs
_(no internal calls)_


### external getKwentaAddress
_(no internal calls)_


### external getVestingEntry
_(no internal calls)_


### external getVestingEntryClaimable
-> internal _claimableAmount
  -> internal _earlyVestFee


### external getVestingQuantity
-> internal _claimableAmount
  -> internal _earlyVestFee


### external getVestingSchedules
-> library VestingEntries.VestingEntryWithID


### external nominateNewOwner
_(no internal calls)_


### external numVestingEntries
_(no internal calls)_


### public setStakingRewards
_(no internal calls)_


### external setTreasuryDAO
_(no internal calls)_


### external stakeEscrow
_(no internal calls)_


### public unstakeEscrow
_(no internal calls)_


### external vest
-> internal _claimableAmount
  -> internal _earlyVestFee
-> internal _isEscrowStaked
-> public unstakeEscrow
-> internal _reduceAccountEscrowBalances
-> internal _transferVestedTokens
  -> internal _reduceAccountEscrowBalances


---

## RewardEscrowV2

_File: contracts/RewardEscrowV2.sol_

### external appendVestingEntry
-> internal _mint


### external bulkTransferFrom
-> internal _checkApproved
-> internal _applyTransferBalanceUpdates
  -> public unstakedEscrowedBalanceOf


### external createEscrowEntry
-> internal _mint


### external escrowedBalanceOf
_(no internal calls)_


### external getAccountVestingEntryIDs
_(no internal calls)_


### external getKwentaAddress
_(no internal calls)_


### external getVestingEntry
_(no internal calls)_


### external getVestingEntryClaimable
-> internal _unpackVestingEntryStruct
-> internal _claimableAmount
  -> internal _earlyVestFee


### external getVestingQuantity
-> internal _unpackVestingEntryStruct
-> internal _claimableAmount
  -> internal _earlyVestFee


### external getVestingSchedules
_(no internal calls)_


### external importEscrowEntry
-> internal _mint


### external initialize
_(no internal calls)_


### external pauseRewardEscrow
_(no internal calls)_


### external setEscrowMigrator
_(no internal calls)_


### external setStakingRewards
_(no internal calls)_


### external setTreasuryDAO
_(no internal calls)_


### external unpauseRewardEscrow
_(no internal calls)_


### public unstakedEscrowedBalanceOf
_(no internal calls)_


### external vest
-> internal _claimableAmount
  -> internal _earlyVestFee
-> internal _unpackVestingEntryStruct
-> public unstakedEscrowedBalanceOf


---

## StakingRewards

_File: contracts/StakingRewards.sol_

### external acceptOwnership
_(no internal calls)_


### external balanceOf
_(no internal calls)_


### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable


### external escrowedBalanceOf
_(no internal calls)_


### external exit
-> public unstake
  -> public nonEscrowedBalanceOf
-> public nonEscrowedBalanceOf
-> public getReward


### public getReward
_(no internal calls)_


### external getRewardForDuration
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### external nominateNewOwner
_(no internal calls)_


### public nonEscrowedBalanceOf
_(no internal calls)_


### external notifyRewardAmount
_(no internal calls)_


### external pauseStakingRewards
_(no internal calls)_


### external recoverERC20
_(no internal calls)_


### public rewardPerToken
-> public lastTimeRewardApplicable


### external setRewardsDuration
_(no internal calls)_


### external stake
_(no internal calls)_


### external stakeEscrow
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### external unpauseStakingRewards
_(no internal calls)_


### public unstake
-> public nonEscrowedBalanceOf


### external unstakeEscrow
_(no internal calls)_


---

## StakingRewardsNotifier

_File: contracts/StakingRewardsNotifier.sol_

### external notifyRewardAmount
_(no internal calls)_


### external setStakingRewardsV2
_(no internal calls)_


---

## StakingRewardsV2

_File: contracts/StakingRewardsV2.sol_

### external approveOperator
_(no internal calls)_


### external balanceAtTime
-> internal _checkpointBinarySearch


### public balanceOf
_(no internal calls)_


### external balancesCheckpointsLength
_(no internal calls)_


### external compound
-> internal _compound
  -> internal _getReward
  -> internal _stakeEscrow
    -> public unstakedEscrowedBalanceOf
      -> public escrowedBalanceOf
    -> internal _addBalancesCheckpoint
      -> internal _addCheckpoint
    -> public balanceOf
    -> internal _addEscrowedBalancesCheckpoint
      -> internal _addCheckpoint
    -> public escrowedBalanceOf
    -> internal _addTotalSupplyCheckpoint
      -> internal _addCheckpoint
    -> public totalSupply
  -> public unstakedEscrowedBalanceOf
    -> public escrowedBalanceOf


### external compoundOnBehalf
-> internal _compound
  -> internal _getReward
  -> internal _stakeEscrow
    -> public unstakedEscrowedBalanceOf
      -> public escrowedBalanceOf
    -> internal _addBalancesCheckpoint
      -> internal _addCheckpoint
    -> public balanceOf
    -> internal _addEscrowedBalancesCheckpoint
      -> internal _addCheckpoint
    -> public escrowedBalanceOf
    -> internal _addTotalSupplyCheckpoint
      -> internal _addCheckpoint
    -> public totalSupply
  -> public unstakedEscrowedBalanceOf
    -> public escrowedBalanceOf


### public earned
-> public balanceOf
-> public rewardPerToken
  -> public totalSupply
  -> public lastTimeRewardApplicable


### public earnedUSDC
-> public balanceOf
-> public rewardPerTokenUSDC
  -> public totalSupply
  -> public lastTimeRewardApplicable


### external escrowedBalanceAtTime
-> internal _checkpointBinarySearch


### public escrowedBalanceOf
_(no internal calls)_


### external escrowedBalancesCheckpointsLength
_(no internal calls)_


### external exit
-> public unstake
  -> public nonEscrowedBalanceOf
    -> public balanceOf
    -> public escrowedBalanceOf
  -> internal _addTotalSupplyCheckpoint
    -> internal _addCheckpoint
  -> public totalSupply
  -> internal _addBalancesCheckpoint
    -> internal _addCheckpoint
  -> public balanceOf
-> public nonEscrowedBalanceOf
  -> public balanceOf
  -> public escrowedBalanceOf
-> internal _getReward


### external getReward
-> internal _getReward


### external getRewardForDuration
_(no internal calls)_


### external getRewardForDurationUSDC
_(no internal calls)_


### external getRewardOnBehalf
-> internal _getReward


### external initialize
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### public nonEscrowedBalanceOf
-> public balanceOf
-> public escrowedBalanceOf


### external notifyRewardAmount
_(no internal calls)_


### external pauseStakingRewards
_(no internal calls)_


### external recoverERC20
_(no internal calls)_


### public rewardPerToken
-> public totalSupply
-> public lastTimeRewardApplicable


### public rewardPerTokenUSDC
-> public totalSupply
-> public lastTimeRewardApplicable


### external setCooldownPeriod
_(no internal calls)_


### external setRewardsDuration
_(no internal calls)_


### external stake
-> internal _addTotalSupplyCheckpoint
  -> internal _addCheckpoint
-> public totalSupply
-> internal _addBalancesCheckpoint
  -> internal _addCheckpoint
-> public balanceOf


### external stakeEscrow
-> internal _stakeEscrow
  -> public unstakedEscrowedBalanceOf
    -> public escrowedBalanceOf
  -> internal _addBalancesCheckpoint
    -> internal _addCheckpoint
  -> public balanceOf
  -> internal _addEscrowedBalancesCheckpoint
    -> internal _addCheckpoint
  -> public escrowedBalanceOf
  -> internal _addTotalSupplyCheckpoint
    -> internal _addCheckpoint
  -> public totalSupply


### external stakeEscrowOnBehalf
-> internal _stakeEscrow
  -> public unstakedEscrowedBalanceOf
    -> public escrowedBalanceOf
  -> internal _addBalancesCheckpoint
    -> internal _addCheckpoint
  -> public balanceOf
  -> internal _addEscrowedBalancesCheckpoint
    -> internal _addCheckpoint
  -> public escrowedBalanceOf
  -> internal _addTotalSupplyCheckpoint
    -> internal _addCheckpoint
  -> public totalSupply


### public totalSupply
_(no internal calls)_


### external totalSupplyAtTime
-> internal _checkpointBinarySearch


### external totalSupplyCheckpointsLength
_(no internal calls)_


### external unpauseStakingRewards
_(no internal calls)_


### public unstake
-> public nonEscrowedBalanceOf
  -> public balanceOf
  -> public escrowedBalanceOf
-> internal _addTotalSupplyCheckpoint
  -> internal _addCheckpoint
-> public totalSupply
-> internal _addBalancesCheckpoint
  -> internal _addCheckpoint
-> public balanceOf


### external unstakeEscrow
-> internal _unstakeEscrow
  -> public escrowedBalanceOf
  -> internal _addBalancesCheckpoint
    -> internal _addCheckpoint
  -> public balanceOf
  -> internal _addEscrowedBalancesCheckpoint
    -> internal _addCheckpoint
  -> internal _addTotalSupplyCheckpoint
    -> internal _addCheckpoint
  -> public totalSupply


### external unstakeEscrowSkipCooldown
-> internal _unstakeEscrow
  -> public escrowedBalanceOf
  -> internal _addBalancesCheckpoint
    -> internal _addCheckpoint
  -> public balanceOf
  -> internal _addEscrowedBalancesCheckpoint
    -> internal _addCheckpoint
  -> internal _addTotalSupplyCheckpoint
    -> internal _addCheckpoint
  -> public totalSupply


### public unstakedEscrowedBalanceOf
-> public escrowedBalanceOf


---

## SupplySchedule

_File: contracts/SupplySchedule.sol_

### external acceptOwnership
_(no internal calls)_


### public isMintable
_(no internal calls)_


### external mint
-> public mintableSupply
  -> public isMintable
  -> public weeksSinceLastIssuance
  -> public tokenDecaySupplyForWeek
    -> library SafeDecimalMath.unit
    -> external_callback INITIAL_WEEKLY_SUPPLY.multiplyDecimal
  -> public terminalInflationSupply
    -> library SafeDecimalMath.unit
-> internal recordMintEvent
  -> public weeksSinceLastIssuance


### public mintableSupply
-> public isMintable
-> public weeksSinceLastIssuance
-> public tokenDecaySupplyForWeek
  -> library SafeDecimalMath.unit
  -> external_callback INITIAL_WEEKLY_SUPPLY.multiplyDecimal
-> public terminalInflationSupply
  -> library SafeDecimalMath.unit


### external nominateNewOwner
_(no internal calls)_


### external setKwenta
_(no internal calls)_


### external setMinterReward
_(no internal calls)_


### external setStakingRewards
_(no internal calls)_


### external setTradingRewards
_(no internal calls)_


### external setTradingRewardsDiversion
_(no internal calls)_


### external setTreasuryDAO
_(no internal calls)_


### external setTreasuryDiversion
_(no internal calls)_


### public terminalInflationSupply
-> library SafeDecimalMath.unit


### public tokenDecaySupplyForWeek
-> library SafeDecimalMath.unit
-> external_callback INITIAL_WEEKLY_SUPPLY.multiplyDecimal


### public weeksSinceLastIssuance
_(no internal calls)_


---

## TokenDistributor

_File: contracts/TokenDistributor.sol_

### public calculateEpochFees
-> internal _startOfEpoch


### public checkpointToken
-> internal _startOfWeek
-> internal _epochFromTimestamp
  -> internal _startOfWeek


### public claimEpoch
-> internal _checkpointWhenReady
  -> internal _startOfWeek
  -> public checkpointToken
    -> internal _startOfWeek
    -> internal _epochFromTimestamp
      -> internal _startOfWeek
-> internal _claimEpoch
  -> internal _isEpochReady
    -> internal _startOfEpoch
  -> public claimedEpoch
  -> public calculateEpochFees
    -> internal _startOfEpoch


### public claimMany
-> internal _checkpointWhenReady
  -> internal _startOfWeek
  -> public checkpointToken
    -> internal _startOfWeek
    -> internal _epochFromTimestamp
      -> internal _startOfWeek
-> internal _claimEpoch
  -> internal _isEpochReady
    -> internal _startOfEpoch
  -> public claimedEpoch
  -> public calculateEpochFees
    -> internal _startOfEpoch


### public claimedEpoch
_(no internal calls)_


---

## vKwenta

_File: contracts/vKwenta.sol_

### public allowance
_(no internal calls)_


### public approve
-> internal _approve


### public balanceOf
_(no internal calls)_


### public decimals
_(no internal calls)_


### public decreaseAllowance
-> internal _approve


### public increaseAllowance
-> internal _approve


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
-> internal _transfer
  -> internal _beforeTokenTransfer
  -> internal _afterTokenTransfer
-> internal _approve


---

## vKwentaRedeemer

_File: contracts/vKwentaRedeemer.sol_

### external redeem
_(no internal calls)_

