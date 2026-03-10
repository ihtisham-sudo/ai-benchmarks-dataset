# Callpaths — Velocitimeter_V4

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BribeFactory

_File: contracts/factories/BribeFactory.sol_

### external createExternalBribe
_(no internal calls)_


### external createInternalBribe
_(no internal calls)_


---

## ExternalBribe

_File: contracts/ExternalBribe.sol_

### external _deposit
-> internal _writeCheckpoint
-> internal _writeSupplyCheckpoint


### external _withdraw
-> internal _writeCheckpoint
-> internal _writeSupplyCheckpoint


### public earned
-> public getPriorBalanceIndex
-> internal _bribeStart
-> public getPriorSupplyIndex


### public getEpochStart
-> internal _bribeStart


### public getPriorBalanceIndex
_(no internal calls)_


### public getPriorSupplyIndex
_(no internal calls)_


### external getReward
-> public earned
  -> public getPriorBalanceIndex
  -> internal _bribeStart
  -> public getPriorSupplyIndex
-> internal _safeTransfer


### external getRewardForOwner
-> public earned
  -> public getPriorBalanceIndex
  -> internal _bribeStart
  -> public getPriorSupplyIndex
-> internal _safeTransfer


### public lastTimeRewardApplicable
-> library Math.min


### external left
-> public getEpochStart
  -> internal _bribeStart


### external notifyRewardAmount
-> public getEpochStart
  -> internal _bribeStart
-> internal _safeTransferFrom


### external rewardsListLength
_(no internal calls)_


### external swapOutRewardToken
_(no internal calls)_


---

## Flow

_File: contracts/Flow.sol_

### external approve
_(no internal calls)_


### external claim
-> internal _mint


### external initialMint
-> internal _mint


### external mint
-> internal _mint


### external setMerkleClaim
_(no internal calls)_


### external setMinter
_(no internal calls)_


### external setRedemptionReceiver
_(no internal calls)_


### external transfer
-> internal _transfer


### external transferFrom
-> internal _transfer


---

## FlowGovernor

_File: contracts/FlowGovernor.sol_

### public COUNTING_MODE
_(no internal calls)_


### public castVote
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public quorum
        -> public quorumNumerator
        -> public quorumDenominator
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _getVotes
  -> internal _countVote


### public castVoteBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public quorum
        -> public quorumNumerator
        -> public quorumDenominator
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _getVotes
  -> internal _countVote


### public castVoteWithReason
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public quorum
        -> public quorumNumerator
        -> public quorumDenominator
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _getVotes
  -> internal _countVote


### public castVoteWithReasonAndParams
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public quorum
        -> public quorumNumerator
        -> public quorumDenominator
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _getVotes
  -> internal _countVote


### public castVoteWithReasonAndParamsBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public quorum
        -> public quorumNumerator
        -> public quorumDenominator
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _getVotes
  -> internal _countVote


### public execute
-> public hashProposal
-> public state
  -> public proposalSnapshot
  -> public proposalDeadline
  -> internal _quorumReached
    -> public quorum
      -> public quorumNumerator
      -> public quorumDenominator
    -> public proposalSnapshot
  -> internal _voteSucceeded
-> internal _beforeExecute
  -> internal _executor
-> internal _execute
-> internal _afterExecute
  -> internal _executor


### public getVotes
-> internal _getVotes
-> internal _defaultParams


### public getVotesWithParams
-> internal _getVotes


### public hasVoted
_(no internal calls)_


### public hashProposal
_(no internal calls)_


### public name
_(no internal calls)_


### public onERC1155BatchReceived
_(no internal calls)_


### public onERC1155Received
_(no internal calls)_


### public onERC721Received
_(no internal calls)_


### public proposalDeadline
_(no internal calls)_


### public proposalSnapshot
_(no internal calls)_


### public proposalThreshold
_(no internal calls)_


### public proposalVotes
_(no internal calls)_


### public propose
-> public getVotes
  -> internal _getVotes
  -> internal _defaultParams
-> public proposalThreshold
-> public hashProposal
-> public votingDelay
-> public votingPeriod


### public quorum
-> public quorumNumerator
-> public quorumDenominator


### public quorumDenominator
_(no internal calls)_


### public quorumNumerator
_(no internal calls)_


### external relay
_(no internal calls)_


### external setProposalNumerator
_(no internal calls)_


### external setTeam
_(no internal calls)_


### public state
-> public proposalSnapshot
-> public proposalDeadline
-> internal _quorumReached
  -> public quorum
    -> public quorumNumerator
    -> public quorumDenominator
  -> public proposalSnapshot
-> internal _voteSucceeded


### public supportsInterface
_(no internal calls)_


### external updateQuorumNumerator
-> internal _updateQuorumNumerator
  -> public quorumDenominator


### public version
_(no internal calls)_


### public votingDelay
_(no internal calls)_


### public votingPeriod
_(no internal calls)_


---

## Gauge

_File: contracts/Gauge.sol_

### external batchRewardPerToken
-> internal _batchRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint


### external batchUpdateRewardPerToken
-> internal _updateRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.max


### external claimFees
-> internal _claimFees
  -> internal _safeApprove


### public deposit
-> internal _updateRewardForAllTokens
  -> internal _updateRewardPerToken
    -> public getPriorSupplyIndex
    -> library Math.min
    -> internal _calcRewardPerToken
      -> library Math.max
      -> library Math.min
    -> internal _writeRewardPerTokenCheckpoint
    -> public lastTimeRewardApplicable
      -> library Math.min
    -> library Math.max
-> internal _safeTransferFrom
-> public derivedBalance
-> internal _writeCheckpoint
-> internal _writeSupplyCheckpoint


### external depositAll
-> public deposit
  -> internal _updateRewardForAllTokens
    -> internal _updateRewardPerToken
      -> public getPriorSupplyIndex
      -> library Math.min
      -> internal _calcRewardPerToken
        -> library Math.max
        -> library Math.min
      -> internal _writeRewardPerTokenCheckpoint
      -> public lastTimeRewardApplicable
        -> library Math.min
      -> library Math.max
  -> internal _safeTransferFrom
  -> public derivedBalance
  -> internal _writeCheckpoint
  -> internal _writeSupplyCheckpoint


### public derivedBalance
_(no internal calls)_


### public earned
-> library Math.max
-> public getPriorBalanceIndex
-> public getPriorRewardPerToken
-> public rewardPerToken
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.min


### public getPriorBalanceIndex
_(no internal calls)_


### public getPriorRewardPerToken
_(no internal calls)_


### public getPriorSupplyIndex
_(no internal calls)_


### external getReward
-> internal _updateRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.max
-> public earned
  -> library Math.max
  -> public getPriorBalanceIndex
  -> public getPriorRewardPerToken
  -> public rewardPerToken
    -> public lastTimeRewardApplicable
      -> library Math.min
    -> library Math.min
-> internal _safeTransfer
-> public derivedBalance
-> internal _writeCheckpoint
-> internal _writeSupplyCheckpoint


### public lastTimeRewardApplicable
-> library Math.min


### external left
_(no internal calls)_


### external notifyRewardAmount
-> internal _writeRewardPerTokenCheckpoint
-> internal _updateRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.max
-> internal _claimFees
  -> internal _safeApprove
-> internal _safeTransferFrom


### public rewardPerToken
-> public lastTimeRewardApplicable
  -> library Math.min
-> library Math.min


### external rewardsListLength
_(no internal calls)_


### external swapOutRewardToken
_(no internal calls)_


### public withdraw
-> public withdrawToken
  -> internal _updateRewardForAllTokens
    -> internal _updateRewardPerToken
      -> public getPriorSupplyIndex
      -> library Math.min
      -> internal _calcRewardPerToken
        -> library Math.max
        -> library Math.min
      -> internal _writeRewardPerTokenCheckpoint
      -> public lastTimeRewardApplicable
        -> library Math.min
      -> library Math.max
  -> internal _safeTransfer
  -> public derivedBalance
  -> internal _writeCheckpoint
  -> internal _writeSupplyCheckpoint


### external withdrawAll
-> public withdraw
  -> public withdrawToken
    -> internal _updateRewardForAllTokens
      -> internal _updateRewardPerToken
        -> public getPriorSupplyIndex
        -> library Math.min
        -> internal _calcRewardPerToken
          -> library Math.max
          -> library Math.min
        -> internal _writeRewardPerTokenCheckpoint
        -> public lastTimeRewardApplicable
          -> library Math.min
        -> library Math.max
    -> internal _safeTransfer
    -> public derivedBalance
    -> internal _writeCheckpoint
    -> internal _writeSupplyCheckpoint


### public withdrawToken
-> internal _updateRewardForAllTokens
  -> internal _updateRewardPerToken
    -> public getPriorSupplyIndex
    -> library Math.min
    -> internal _calcRewardPerToken
      -> library Math.max
      -> library Math.min
    -> internal _writeRewardPerTokenCheckpoint
    -> public lastTimeRewardApplicable
      -> library Math.min
    -> library Math.max
-> internal _safeTransfer
-> public derivedBalance
-> internal _writeCheckpoint
-> internal _writeSupplyCheckpoint


---

## GaugeFactory

_File: contracts/factories/GaugeFactory.sol_

### external createGauge
_(no internal calls)_


---

## InternalBribe

_File: contracts/InternalBribe.sol_

### external _deposit
-> internal _updateRewardForAllTokens
  -> internal _updateRewardPerToken
    -> public getPriorSupplyIndex
    -> library Math.min
    -> internal _calcRewardPerToken
      -> library Math.max
      -> library Math.min
    -> internal _writeRewardPerTokenCheckpoint
    -> public lastTimeRewardApplicable
      -> library Math.min
    -> library Math.max
-> internal _writeCheckpoint
-> internal _writeSupplyCheckpoint


### external _withdraw
-> internal _updateRewardForAllTokens
  -> internal _updateRewardPerToken
    -> public getPriorSupplyIndex
    -> library Math.min
    -> internal _calcRewardPerToken
      -> library Math.max
      -> library Math.min
    -> internal _writeRewardPerTokenCheckpoint
    -> public lastTimeRewardApplicable
      -> library Math.min
    -> library Math.max
-> internal _writeCheckpoint
-> internal _writeSupplyCheckpoint


### external batchRewardPerToken
-> internal _batchRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint


### external batchUpdateRewardPerToken
-> internal _updateRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.max


### public earned
-> library Math.max
-> public getPriorBalanceIndex
-> public getPriorRewardPerToken
-> public rewardPerToken
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.min


### public getPriorBalanceIndex
_(no internal calls)_


### public getPriorRewardPerToken
_(no internal calls)_


### public getPriorSupplyIndex
_(no internal calls)_


### external getReward
-> internal _updateRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.max
-> public earned
  -> library Math.max
  -> public getPriorBalanceIndex
  -> public getPriorRewardPerToken
  -> public rewardPerToken
    -> public lastTimeRewardApplicable
      -> library Math.min
    -> library Math.min
-> internal _safeTransfer


### external getRewardForOwner
-> internal _updateRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.max
-> public earned
  -> library Math.max
  -> public getPriorBalanceIndex
  -> public getPriorRewardPerToken
  -> public rewardPerToken
    -> public lastTimeRewardApplicable
      -> library Math.min
    -> library Math.min
-> internal _safeTransfer


### public lastTimeRewardApplicable
-> library Math.min


### external left
_(no internal calls)_


### external notifyRewardAmount
-> internal _writeRewardPerTokenCheckpoint
-> internal _updateRewardPerToken
  -> public getPriorSupplyIndex
  -> library Math.min
  -> internal _calcRewardPerToken
    -> library Math.max
    -> library Math.min
  -> internal _writeRewardPerTokenCheckpoint
  -> public lastTimeRewardApplicable
    -> library Math.min
  -> library Math.max
-> internal _safeTransferFrom


### public rewardPerToken
-> public lastTimeRewardApplicable
  -> library Math.min
-> library Math.min


### external rewardsListLength
_(no internal calls)_


### external swapOutRewardToken
_(no internal calls)_


---

## L2Governor

_File: contracts/governance/L2Governor.sol_

### public castVote
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline


### public castVoteBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline


### public castVoteWithReason
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline


### public castVoteWithReasonAndParams
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline


### public castVoteWithReasonAndParamsBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline


### public execute
-> public hashProposal
-> public state
  -> public proposalSnapshot
  -> public proposalDeadline
-> internal _beforeExecute
  -> internal _executor
-> internal _execute
-> internal _afterExecute
  -> internal _executor


### public getVotes
-> internal _defaultParams


### public getVotesWithParams
_(no internal calls)_


### public hashProposal
_(no internal calls)_


### public name
_(no internal calls)_


### public onERC1155BatchReceived
_(no internal calls)_


### public onERC1155Received
_(no internal calls)_


### public onERC721Received
_(no internal calls)_


### public proposalDeadline
_(no internal calls)_


### public proposalSnapshot
_(no internal calls)_


### public proposalThreshold
_(no internal calls)_


### public propose
-> public getVotes
  -> internal _defaultParams
-> public proposalThreshold
-> public hashProposal


### external relay
_(no internal calls)_


### public state
-> public proposalSnapshot
-> public proposalDeadline


### public supportsInterface
_(no internal calls)_


### public version
_(no internal calls)_


---

## L2GovernorCountingSimple

_File: contracts/governance/L2GovernorCountingSimple.sol_

### public COUNTING_MODE
_(no internal calls)_


### public castVote
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _countVote


### public castVoteBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _countVote


### public castVoteWithReason
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _countVote


### public castVoteWithReasonAndParams
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _countVote


### public castVoteWithReasonAndParamsBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
    -> internal _quorumReached
      -> public proposalSnapshot
    -> internal _voteSucceeded
  -> internal _countVote


### public execute
-> public hashProposal
-> public state
  -> public proposalSnapshot
  -> public proposalDeadline
  -> internal _quorumReached
    -> public proposalSnapshot
  -> internal _voteSucceeded
-> internal _beforeExecute
  -> internal _executor
-> internal _execute
-> internal _afterExecute
  -> internal _executor


### public getVotes
-> internal _defaultParams


### public getVotesWithParams
_(no internal calls)_


### public hasVoted
_(no internal calls)_


### public hashProposal
_(no internal calls)_


### public name
_(no internal calls)_


### public onERC1155BatchReceived
_(no internal calls)_


### public onERC1155Received
_(no internal calls)_


### public onERC721Received
_(no internal calls)_


### public proposalDeadline
_(no internal calls)_


### public proposalSnapshot
_(no internal calls)_


### public proposalThreshold
_(no internal calls)_


### public proposalVotes
_(no internal calls)_


### public propose
-> public getVotes
  -> internal _defaultParams
-> public proposalThreshold
-> public hashProposal


### external relay
_(no internal calls)_


### public state
-> public proposalSnapshot
-> public proposalDeadline
-> internal _quorumReached
  -> public proposalSnapshot
-> internal _voteSucceeded


### public supportsInterface
_(no internal calls)_


### public version
_(no internal calls)_


---

## L2GovernorVotes

_File: contracts/governance/L2GovernorVotes.sol_

### public castVote
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
  -> internal _getVotes


### public castVoteBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
  -> internal _getVotes


### public castVoteWithReason
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
  -> internal _getVotes


### public castVoteWithReasonAndParams
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
  -> internal _getVotes


### public castVoteWithReasonAndParamsBySig
-> internal _castVote
  -> public state
    -> public proposalSnapshot
    -> public proposalDeadline
  -> internal _getVotes


### public execute
-> public hashProposal
-> public state
  -> public proposalSnapshot
  -> public proposalDeadline
-> internal _beforeExecute
  -> internal _executor
-> internal _execute
-> internal _afterExecute
  -> internal _executor


### public getVotes
-> internal _getVotes
-> internal _defaultParams


### public getVotesWithParams
-> internal _getVotes


### public hashProposal
_(no internal calls)_


### public name
_(no internal calls)_


### public onERC1155BatchReceived
_(no internal calls)_


### public onERC1155Received
_(no internal calls)_


### public onERC721Received
_(no internal calls)_


### public proposalDeadline
_(no internal calls)_


### public proposalSnapshot
_(no internal calls)_


### public proposalThreshold
_(no internal calls)_


### public propose
-> public getVotes
  -> internal _getVotes
  -> internal _defaultParams
-> public proposalThreshold
-> public hashProposal


### external relay
_(no internal calls)_


### public state
-> public proposalSnapshot
-> public proposalDeadline


### public supportsInterface
_(no internal calls)_


### public version
_(no internal calls)_


---

## L2GovernorVotesQuorumFraction

_File: contracts/governance/L2GovernorVotesQuorumFraction.sol_

### public quorum
-> public quorumNumerator
-> public quorumDenominator


### public quorumDenominator
_(no internal calls)_


### public quorumNumerator
_(no internal calls)_


### external updateQuorumNumerator
-> internal _updateQuorumNumerator
  -> public quorumDenominator


---

## Minter

_File: contracts/Minter.sol_

### external acceptTeam
_(no internal calls)_


### public calculate_emission
_(no internal calls)_


### public calculate_growth
_(no internal calls)_


### public circulating_emission
-> public circulating_supply


### public circulating_supply
_(no internal calls)_


### external initialize
_(no internal calls)_


### external setTeam
_(no internal calls)_


### external setTeamRate
_(no internal calls)_


### external update_period
-> public weekly_emission
  -> library Math.max
  -> public calculate_emission
  -> public circulating_emission
    -> public circulating_supply
-> public calculate_growth
-> public circulating_supply
-> public circulating_emission
  -> public circulating_supply


### public weekly_emission
-> library Math.max
-> public calculate_emission
-> public circulating_emission
  -> public circulating_supply


---

## Pair

_File: contracts/Pair.sol_

### external approve
_(no internal calls)_


### external burn
-> internal _burn
  -> internal _updateFor
-> internal _safeTransfer
-> internal _update
  -> public lastObservation


### external claimFees
-> internal _updateFor


### external current
-> public lastObservation
-> public currentCumulativePrices
  -> public getReserves
-> internal _getAmountOut
  -> internal _k
  -> internal _get_y
    -> internal _f
    -> internal _d


### public currentCumulativePrices
-> public getReserves


### external getAmountOut
-> internal _getAmountOut
  -> internal _k
  -> internal _get_y
    -> internal _f
    -> internal _d


### public getReserves
_(no internal calls)_


### public lastObservation
_(no internal calls)_


### external metadata
_(no internal calls)_


### external mint
-> library Math.sqrt
-> internal _mint
  -> internal _updateFor
-> library Math.min
-> internal _update
  -> public lastObservation


### external observationLength
_(no internal calls)_


### external permit
_(no internal calls)_


### external prices
-> public sample
  -> internal _getAmountOut
    -> internal _k
    -> internal _get_y
      -> internal _f
      -> internal _d


### external quote
-> public sample
  -> internal _getAmountOut
    -> internal _k
    -> internal _get_y
      -> internal _f
      -> internal _d


### public sample
-> internal _getAmountOut
  -> internal _k
  -> internal _get_y
    -> internal _f
    -> internal _d


### external setExternalBribe
-> internal _safeApprove


### external setHasGauge
_(no internal calls)_


### external skim
-> internal _safeTransfer


### external swap
-> internal _safeTransfer
-> internal _update0
  -> internal _safeTransfer
-> internal _update1
  -> internal _safeTransfer
-> internal _k
-> internal _update
  -> public lastObservation


### external sync
-> internal _update
  -> public lastObservation


### external tokens
_(no internal calls)_


### external transfer
-> internal _transferTokens
  -> internal _updateFor


### external transferFrom
-> internal _transferTokens
  -> internal _updateFor


---

## PairFactory

_File: contracts/factories/PairFactory.sol_

### external acceptFeeManager
_(no internal calls)_


### external acceptPauser
_(no internal calls)_


### external acceptTank
_(no internal calls)_


### external allPairsLength
_(no internal calls)_


### external createPair
_(no internal calls)_


### public getFee
_(no internal calls)_


### external getInitializable
_(no internal calls)_


### external getVoter
_(no internal calls)_


### external pairCodeHash
_(no internal calls)_


### external setFee
_(no internal calls)_


### external setFeeManager
_(no internal calls)_


### external setPause
_(no internal calls)_


### external setPauser
_(no internal calls)_


### external setTank
_(no internal calls)_


### external setTeam
_(no internal calls)_


### external setVoter
_(no internal calls)_


---

## PairFees

_File: contracts/PairFees.sol_

### external claimFeesFor
-> internal _safeTransfer


---

## RewardsDistributor

_File: contracts/RewardsDistributor.sol_

### external checkpoint_token
-> internal _checkpoint_token


### external checkpoint_total_supply
-> internal _checkpoint_total_supply
  -> internal _find_timestamp_epoch
  -> library Math.max


### external claim
-> internal _checkpoint_total_supply
  -> internal _find_timestamp_epoch
  -> library Math.max
-> internal _claim
  -> internal _find_timestamp_user_epoch
  -> external_callback IVotingEscrow.Point
  -> library Math.max
  -> library Math.min


### external claim_many
-> internal _checkpoint_total_supply
  -> internal _find_timestamp_epoch
  -> library Math.max
-> internal _claim
  -> internal _find_timestamp_user_epoch
  -> external_callback IVotingEscrow.Point
  -> library Math.max
  -> library Math.min


### external claimable
-> internal _claimable
  -> internal _find_timestamp_user_epoch
  -> external_callback IVotingEscrow.Point
  -> library Math.max


### external setDepositor
_(no internal calls)_


### external timestamp
_(no internal calls)_


### external ve_for_at
-> internal _find_timestamp_user_epoch
-> library Math.max


---

## Router

_File: contracts/Router.sol_

### external UNSAFE_swapExactTokensForTokens
-> internal _safeTransferFrom
-> public pairFor
  -> public sortTokens
-> internal _swap
  -> public sortTokens
  -> public pairFor
    -> public sortTokens


### external addLiquidity
-> internal _addLiquidity
  -> public getReserves
    -> public sortTokens
    -> public pairFor
      -> public sortTokens
  -> internal quoteLiquidity
-> public pairFor
  -> public sortTokens
-> internal _safeTransferFrom


### external addLiquidityETH
-> internal _addLiquidity
  -> public getReserves
    -> public sortTokens
    -> public pairFor
      -> public sortTokens
  -> internal quoteLiquidity
-> public pairFor
  -> public sortTokens
-> internal _safeTransferFrom
-> internal _safeTransferETH


### external getAmountOut
-> public pairFor
  -> public sortTokens


### public getAmountsOut
-> public pairFor
  -> public sortTokens


### public getReserves
-> public sortTokens
-> public pairFor
  -> public sortTokens


### external isPair
_(no internal calls)_


### public pairFor
-> public sortTokens


### external quoteAddLiquidity
-> public getReserves
  -> public sortTokens
  -> public pairFor
    -> public sortTokens
-> library Math.sqrt
-> internal quoteLiquidity
-> library Math.min


### external quoteRemoveLiquidity
-> public getReserves
  -> public sortTokens
  -> public pairFor
    -> public sortTokens


### public removeLiquidity
-> public pairFor
  -> public sortTokens
-> public sortTokens


### public removeLiquidityETH
-> public removeLiquidity
  -> public pairFor
    -> public sortTokens
  -> public sortTokens
-> internal _safeTransfer
-> internal _safeTransferETH


### external removeLiquidityETHWithPermit
-> public pairFor
  -> public sortTokens
-> public removeLiquidityETH
  -> public removeLiquidity
    -> public pairFor
      -> public sortTokens
    -> public sortTokens
  -> internal _safeTransfer
  -> internal _safeTransferETH


### external removeLiquidityWithPermit
-> public pairFor
  -> public sortTokens
-> public removeLiquidity
  -> public pairFor
    -> public sortTokens
  -> public sortTokens


### public sortTokens
_(no internal calls)_


### external swapExactETHForTokens
-> public getAmountsOut
  -> public pairFor
    -> public sortTokens
-> public pairFor
  -> public sortTokens
-> internal _swap
  -> public sortTokens
  -> public pairFor
    -> public sortTokens


### external swapExactTokensForETH
-> public getAmountsOut
  -> public pairFor
    -> public sortTokens
-> internal _safeTransferFrom
-> public pairFor
  -> public sortTokens
-> internal _swap
  -> public sortTokens
  -> public pairFor
    -> public sortTokens
-> internal _safeTransferETH


### external swapExactTokensForTokens
-> public getAmountsOut
  -> public pairFor
    -> public sortTokens
-> internal _safeTransferFrom
-> public pairFor
  -> public sortTokens
-> internal _swap
  -> public sortTokens
  -> public pairFor
    -> public sortTokens


### external swapExactTokensForTokensSimple
-> public getAmountsOut
  -> public pairFor
    -> public sortTokens
-> internal _safeTransferFrom
-> public pairFor
  -> public sortTokens
-> internal _swap
  -> public sortTokens
  -> public pairFor
    -> public sortTokens


---

## VeArtProxy

_File: contracts/VeArtProxy.sol_

### external _tokenURI
-> internal toString


---

## VelocimeterLibrary

_File: contracts/VelocimeterLibrary.sol_

### external getAmountOut
-> internal _getAmountOut
  -> internal _k
  -> internal _get_y
    -> internal _f
    -> internal _d


### external getMinimumValue
_(no internal calls)_


### external getSample
-> internal _getAmountOut
  -> internal _k
  -> internal _get_y
    -> internal _f
    -> internal _d


### external getTradeDiff
-> internal _getAmountOut
  -> internal _k
  -> internal _get_y
    -> internal _f
    -> internal _d


---

## Voter

_File: contracts/Voter.sol_

### external attachTokenToGauge
_(no internal calls)_


### external claimBribes
_(no internal calls)_


### external claimFees
_(no internal calls)_


### external claimRewards
_(no internal calls)_


### external createGauge
-> internal _updateFor


### external detachTokenFromGauge
_(no internal calls)_


### external distribute
-> external distribute


### external distributeFees
_(no internal calls)_


### external distro
-> external distribute
  -> external distribute


### external emitDeposit
_(no internal calls)_


### external emitWithdraw
_(no internal calls)_


### external initialize
-> internal _whitelist


### external killGauge
_(no internal calls)_


### external length
_(no internal calls)_


### external notifyRewardAmount
-> internal _safeTransferFrom


### external poke
-> internal _vote
  -> internal _reset
    -> internal _updateFor
  -> internal _updateFor


### external reset
-> internal _reset
  -> internal _updateFor


### external reviveGauge
_(no internal calls)_


### public setEmergencyCouncil
_(no internal calls)_


### public setGovernor
_(no internal calls)_


### external updateAll
-> public updateForRange
  -> internal _updateFor


### external updateFor
-> internal _updateFor


### public updateForRange
-> internal _updateFor


### external updateGauge
-> internal _updateFor


### external vote
-> internal _vote
  -> internal _reset
    -> internal _updateFor
  -> internal _updateFor


### public whitelist
-> internal _whitelist


---

## VotingEscrow

_File: contracts/VotingEscrow.sol_

### external abstain
_(no internal calls)_


### public approve
_(no internal calls)_


### external attach
_(no internal calls)_


### external balanceOf
-> internal _balance


### external balanceOfAtNFT
-> internal _balanceOfAtNFT
  -> internal _find_block_epoch


### external balanceOfNFT
-> internal _balanceOfNFT


### external balanceOfNFTAt
-> internal _balanceOfNFT


### external block_number
_(no internal calls)_


### external checkpoint
-> internal _checkpoint


### external create_lock
-> internal _create_lock
  -> internal _mint
    -> internal _moveTokenDelegates
      -> internal _findWhatCheckpointToWrite
    -> public delegates
    -> internal _addTokenTo
      -> internal _addTokenToOwnerList
        -> internal _balance
  -> internal _deposit_for
    -> internal _checkpoint


### external create_lock_for
-> internal _create_lock
  -> internal _mint
    -> internal _moveTokenDelegates
      -> internal _findWhatCheckpointToWrite
    -> public delegates
    -> internal _addTokenTo
      -> internal _addTokenToOwnerList
        -> internal _balance
  -> internal _deposit_for
    -> internal _checkpoint


### public delegate
-> internal _delegate
  -> public delegates
  -> internal _moveAllDelegates
    -> internal _findWhatCheckpointToWrite


### public delegateBySig
-> internal _delegate
  -> public delegates
  -> internal _moveAllDelegates
    -> internal _findWhatCheckpointToWrite


### public delegates
_(no internal calls)_


### external deposit_for
-> internal _deposit_for
  -> internal _checkpoint


### external detach
_(no internal calls)_


### external getApproved
_(no internal calls)_


### external getPastTotalSupply
-> public totalSupplyAtT
  -> internal _supply_at


### public getPastVotes
-> public getPastVotesIndex
-> internal _balanceOfNFT


### public getPastVotesIndex
_(no internal calls)_


### external getVotes
-> internal _balanceOfNFT


### external get_last_user_slope
_(no internal calls)_


### external increase_amount
-> internal _isApprovedOrOwner
-> internal _deposit_for
  -> internal _checkpoint


### external increase_unlock_time
-> internal _isApprovedOrOwner
-> internal _deposit_for
  -> internal _checkpoint


### external isApprovedForAll
_(no internal calls)_


### external isApprovedOrOwner
-> internal _isApprovedOrOwner


### external locked__end
_(no internal calls)_


### external merge
-> internal _isApprovedOrOwner
-> internal _checkpoint
-> internal _burn
  -> internal _isApprovedOrOwner
  -> public ownerOf
  -> public approve
  -> internal _moveTokenDelegates
    -> internal _findWhatCheckpointToWrite
  -> public delegates
  -> internal _removeTokenFrom
    -> internal _removeTokenFromOwnerList
      -> internal _balance
-> internal _deposit_for
  -> internal _checkpoint


### public ownerOf
_(no internal calls)_


### public safeTransferFrom
-> internal _transferFrom
  -> internal _isApprovedOrOwner
  -> internal _clearApproval
  -> internal _removeTokenFrom
    -> internal _removeTokenFromOwnerList
      -> internal _balance
  -> internal _moveTokenDelegates
    -> internal _findWhatCheckpointToWrite
  -> public delegates
  -> internal _addTokenTo
    -> internal _addTokenToOwnerList
      -> internal _balance
-> internal _isContract


### external setApprovalForAll
_(no internal calls)_


### external setArtProxy
_(no internal calls)_


### external setTeam
_(no internal calls)_


### external setVoter
_(no internal calls)_


### external supportsInterface
_(no internal calls)_


### external tokenOfOwnerByIndex
_(no internal calls)_


### external tokenURI
-> internal _balanceOfNFT


### external totalSupply
-> public totalSupplyAtT
  -> internal _supply_at


### external totalSupplyAt
-> internal _find_block_epoch
-> internal _supply_at


### public totalSupplyAtT
-> internal _supply_at


### external transferFrom
-> internal _transferFrom
  -> internal _isApprovedOrOwner
  -> internal _clearApproval
  -> internal _removeTokenFrom
    -> internal _removeTokenFromOwnerList
      -> internal _balance
  -> internal _moveTokenDelegates
    -> internal _findWhatCheckpointToWrite
  -> public delegates
  -> internal _addTokenTo
    -> internal _addTokenToOwnerList
      -> internal _balance


### external user_point_history__ts
_(no internal calls)_


### external voting
_(no internal calls)_


### external withdraw
-> internal _isApprovedOrOwner
-> internal _checkpoint
-> internal _burn
  -> internal _isApprovedOrOwner
  -> public ownerOf
  -> public approve
  -> internal _moveTokenDelegates
    -> internal _findWhatCheckpointToWrite
  -> public delegates
  -> internal _removeTokenFrom
    -> internal _removeTokenFromOwnerList
      -> internal _balance


---

## WrappedExternalBribe

_File: contracts/WrappedExternalBribe.sol_

### public earned
-> internal _bribeStart


### public getEpochStart
-> internal _bribeStart


### external getReward
-> public earned
  -> internal _bribeStart
-> internal _safeTransfer


### external getRewardForOwner
-> public earned
  -> internal _bribeStart
-> internal _safeTransfer


### public lastTimeRewardApplicable
-> library Math.min


### external left
-> public getEpochStart
  -> internal _bribeStart


### external notifyRewardAmount
-> public getEpochStart
  -> internal _bribeStart
-> internal _safeTransferFrom


### external rewardsListLength
_(no internal calls)_


### external swapOutRewardToken
_(no internal calls)_


---

## WrappedExternalBribeFactory

_File: contracts/factories/WrappedExternalBribeFactory.sol_

### external createBribe
_(no internal calls)_


### external setVoter
_(no internal calls)_

