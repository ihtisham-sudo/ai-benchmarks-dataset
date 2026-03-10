# Callpaths — FrankenDAO

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Admin

_File: src/utils/Admin.sol_

### external acceptFounders
_(no internal calls)_


### external revokeFounders
_(no internal calls)_


### external setCouncil
_(no internal calls)_


### external setPauser
_(no internal calls)_


### external setPendingFounders
_(no internal calls)_


### external setVerifier
_(no internal calls)_


---

## Executor

_File: src/Executor.sol_

### public cancelTransaction
_(no internal calls)_


### public executeTransaction
_(no internal calls)_


### public queueTransaction
_(no internal calls)_


---

## Governance

_File: src/Governance.sol_

### external acceptFounders
_(no internal calls)_


### external banProposer
_(no internal calls)_


### external cancel
-> internal _removeTransactionWithQueuedOrExpiredCheck
  -> public state
  -> private _removeFromActiveProposals


### external castVote
-> internal _castVote
  -> public state
-> internal _refundGas
  -> internal _min


### external clear
-> public state
-> internal _removeTransactionWithQueuedOrExpiredCheck
  -> public state
  -> private _removeFromActiveProposals


### external execute
-> public state


### external getActions
_(no internal calls)_


### public getActiveProposals
_(no internal calls)_


### public getProposalData
_(no internal calls)_


### public getProposalStatus
_(no internal calls)_


### public getProposalVotes
_(no internal calls)_


### external getReceipt
_(no internal calls)_


### public initialize
_(no internal calls)_


### public proposalThreshold
-> internal bps2Uint


### public propose
-> internal _propose
  -> public proposalThreshold
    -> internal bps2Uint
  -> public state
  -> public quorumVotes
    -> internal bps2Uint
-> internal _refundGas
  -> internal _min


### external queue
-> public state
-> private _removeFromActiveProposals


### public quorumVotes
-> internal bps2Uint


### external revokeFounders
_(no internal calls)_


### external setCouncil
_(no internal calls)_


### external setPauser
_(no internal calls)_


### external setPendingFounders
_(no internal calls)_


### external setProposalThresholdBPS
_(no internal calls)_


### external setQuorumVotesBPS
_(no internal calls)_


### external setRefunds
_(no internal calls)_


### external setStakingAddress
_(no internal calls)_


### external setVerifier
_(no internal calls)_


### external setVotingDelay
_(no internal calls)_


### external setVotingPeriod
_(no internal calls)_


### public state
_(no internal calls)_


### external updateTotalCommunityScoreData
_(no internal calls)_


### external verifyProposal
-> public state


### external veto
-> internal _removeTransactionWithQueuedOrExpiredCheck
  -> public state
  -> private _removeFromActiveProposals
-> public state


---

## GovernanceProxy

_File: src/proxy/GovernanceProxy.sol_

### external admin
_(no internal calls)_


### external changeAdmin
_(no internal calls)_


### external implementation
_(no internal calls)_


### external upgradeTo
_(no internal calls)_


### external upgradeToAndCall
_(no internal calls)_


---

## Staking

_File: src/Staking.sol_

### external acceptFounders
_(no internal calls)_


### external changeStakeAmount
_(no internal calls)_


### external changeStakeTime
_(no internal calls)_


### public delegate
-> internal _delegate
  -> public getDelegate
  -> internal _updateTotalCommunityVotingPower
-> internal _refundGas
  -> internal _min


### public evilBonus
_(no internal calls)_


### public getCommunityVotingPower
_(no internal calls)_


### public getDelegate
_(no internal calls)_


### public getStakedTokenSupplies
_(no internal calls)_


### public getTokenVotingPower
-> public evilBonus


### public getTotalVotingPower
-> public getCommunityVotingPower


### public getVotes
-> public getCommunityVotingPower


### external isFrankenPunksStakingContract
_(no internal calls)_


### external revokeFounders
_(no internal calls)_


### external setBaseURI
_(no internal calls)_


### external setContractURI
_(no internal calls)_


### external setCouncil
_(no internal calls)_


### external setPause
_(no internal calls)_


### external setPauser
_(no internal calls)_


### external setPendingFounders
_(no internal calls)_


### external setProposalsCreatedMultiplier
_(no internal calls)_


### external setProposalsPassedMultiplier
_(no internal calls)_


### external setRefunds
_(no internal calls)_


### external setVerifier
_(no internal calls)_


### external setVotesMultiplier
_(no internal calls)_


### public stake
-> internal _stake
  -> internal _stakeToken
    -> public getTokenVotingPower
      -> public evilBonus
  -> public getDelegate
  -> internal _updateTotalCommunityVotingPower
-> internal _refundGas
  -> internal _min


### public tokenURI
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### public unstake
-> internal _unstake
  -> internal _unstakeToken
    -> public getTokenVotingPower
      -> public evilBonus
  -> public getDelegate
  -> internal _updateTotalCommunityVotingPower

