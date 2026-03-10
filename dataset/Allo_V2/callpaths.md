# Callpaths — Allo_V2

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Allo

_File: contracts/core/Allo.sol_

### external addPoolManager
_(no internal calls)_


### external addToCloneableStrategies
_(no internal calls)_


### external allocate
-> internal _allocate


### external batchAllocate
-> internal _allocate


### external batchRegisterRecipient
_(no internal calls)_


### external createPool
-> internal _isCloneableStrategy
-> internal _createPool
  -> internal _transferAmount
  -> internal _fundPool
    -> public getFeeDenominator
    -> internal _transferAmountFrom
    -> internal _getBalance
-> library Clone.createClone


### external createPoolWithCustomStrategy
-> internal _isCloneableStrategy
-> internal _createPool
  -> internal _transferAmount
  -> internal _fundPool
    -> public getFeeDenominator
    -> internal _transferAmountFrom
    -> internal _getBalance


### external distribute
_(no internal calls)_


### external fundPool
-> internal _fundPool
  -> public getFeeDenominator
  -> internal _transferAmountFrom
  -> internal _getBalance


### external getBaseFee
_(no internal calls)_


### public getFeeDenominator
_(no internal calls)_


### external getPercentFee
_(no internal calls)_


### external getPool
_(no internal calls)_


### external getRegistry
_(no internal calls)_


### external getStrategy
_(no internal calls)_


### external getTreasury
_(no internal calls)_


### external initialize
-> internal _updateRegistry
-> internal _updateTreasury
-> internal _updatePercentFee
-> internal _updateBaseFee


### external isCloneableStrategy
-> internal _isCloneableStrategy


### external isPoolAdmin
-> internal _isPoolAdmin


### external isPoolManager
-> internal _isPoolManager
  -> internal _isPoolAdmin


### external recoverFunds
-> internal _transferAmount


### external registerRecipient
_(no internal calls)_


### external removeFromCloneableStrategies
_(no internal calls)_


### external removePoolManager
_(no internal calls)_


### external updateBaseFee
-> internal _updateBaseFee


### external updatePercentFee
-> internal _updatePercentFee


### external updatePoolMetadata
_(no internal calls)_


### external updateRegistry
-> internal _updateRegistry


### external updateTreasury
-> internal _updateTreasury


---

## AlloV1ToV2ProfileMigration

_File: contracts/migration/AlloV1ToV2ProfileMigration.sol_

### external createProfiles
_(no internal calls)_


---

## Anchor

_File: contracts/core/Anchor.sol_

### external execute
_(no internal calls)_


---

## BaseStrategy

_File: contracts/strategies/BaseStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
_(no internal calls)_


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipientStatus
_(no internal calls)_


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
_(no internal calls)_


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _afterRegisterRecipient


---

## BulkProfileMigration

_File: contracts/migration/BulkProfileMigration.sol_

### external createProfiles
_(no internal calls)_


---

## ContractFactory

_File: contracts/factories/ContractFactory.sol_

### external deploy
_(no internal calls)_


### external setDeployer
_(no internal calls)_


---

## DGLFactory

_File: contracts/factories/DGLFactory.sol_

### external createCustomStrategy
_(no internal calls)_


### external createStrategy
_(no internal calls)_


### external updateAllo
_(no internal calls)_


### external updateName
_(no internal calls)_


---

## DVMDTFactory

_File: contracts/factories/DVMDTFactory.sol_

### external createStrategy
_(no internal calls)_


### external createStrategyCustom
_(no internal calls)_


### external updateAllo
_(no internal calls)_


### external updateName
_(no internal calls)_


### external updatePermit2
_(no internal calls)_


---

## DirectAllocationStrategy

_File: contracts/strategies/direct-allocation/DirectAllocation.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipientStatus
-> internal _getRecipientStatus


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __BaseStrategy_init


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
-> internal _afterRegisterRecipient


### external withdraw
_(no internal calls)_


---

## DirectGrantsLiteStrategy

_File: contracts/strategies/direct-grants-lite/DirectGrantsLite.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
  -> internal _getRecipient
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __DirectGrantsLiteStrategy_init
  -> internal __BaseStrategy_init
  -> internal _isPoolTimestampValid


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
  -> internal _setRecipientStatus
    -> internal _getStatusRowColumn
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn
-> internal _afterRegisterRecipient


### external reviewRecipients
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## DirectGrantsSimpleStrategy

_File: contracts/strategies/_poc/direct-grants-simple/DirectGrantsSimpleStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> private _distributeUpcomingMilestone
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getMilestoneStatus
_(no internal calls)_


### external getMilestones
_(no internal calls)_


### external getPayouts
-> internal _getPayout
  -> internal _getRecipient


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __DirectGrantsSimpleStrategy_init
  -> internal __BaseStrategy_init
  -> internal _setPoolActive


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external rejectMilestone
_(no internal calls)_


### external reviewSetMilestones
_(no internal calls)_


### external setMilestones
-> internal _isProfileMember
-> internal _setMilestones


### external setPoolActive
-> internal _setPoolActive


### external setRecipientStatusToInReview
_(no internal calls)_


### external submitMilestone
-> internal _isProfileMember


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## DonationVotingCustomRegistryStrategy

_File: contracts/strategies/_poc/donation-voting-custom-registry/DonationVotingCustomRegistryStrategy.sol_

### external claim
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external initialize
-> internal __DonationVotingStrategy_init
  -> internal _isPoolTimestampValid


### external reviewRecipients
_(no internal calls)_


### external setPayout
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## DonationVotingMerkleDistributionBaseStrategy

_File: contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> private _distributeSingle
    -> internal _validateDistribution
      -> internal _hasBeenDistributed
    -> private _setDistributed
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout
  -> internal _getRecipient
  -> internal _validateDistribution
    -> internal _hasBeenDistributed


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn


### external getStrategyId
_(no internal calls)_


### external hasBeenDistributed
-> internal _hasBeenDistributed


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __DonationVotingStrategy_init
  -> internal __BaseStrategy_init
  -> internal _isPoolTimestampValid


### external isDistributionSet
_(no internal calls)_


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
  -> internal _setRecipientStatus
    -> internal _getStatusRowColumn
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn
-> internal _afterRegisterRecipient


### external reviewRecipients
_(no internal calls)_


### external updateDistribution
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## DonationVotingMerkleDistributionDirectTransferStrategy

_File: contracts/strategies/donation-voting-merkle-distribution-direct-transfer/DonationVotingMerkleDistributionDirectTransferStrategy.sol_

### external getRecipient
-> internal _getRecipient


### external hasBeenDistributed
-> internal _hasBeenDistributed


### external initialize
-> internal __DonationVotingStrategy_init
  -> internal _isPoolTimestampValid


### external isDistributionSet
_(no internal calls)_


### external reviewRecipients
_(no internal calls)_


### public splitSignature
_(no internal calls)_


### external updateDistribution
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
-> internal _tokenAmountInVault


---

## DonationVotingMerkleDistributionVaultStrategy

_File: contracts/strategies/donation-voting-merkle-distribution-vault/DonationVotingMerkleDistributionVaultStrategy.sol_

### external claim
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external hasBeenDistributed
-> internal _hasBeenDistributed


### external initialize
-> internal __DonationVotingStrategy_init
  -> internal _isPoolTimestampValid


### external isDistributionSet
_(no internal calls)_


### external reviewRecipients
_(no internal calls)_


### external updateDistribution
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
-> internal _tokenAmountInVault


---

## DonationVotingStrategy

_File: contracts/strategies/_poc/donation-voting/DonationVotingStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external claim
_(no internal calls)_


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __DonationVotingStrategy_init
  -> internal __BaseStrategy_init
  -> internal _isPoolTimestampValid


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external reviewRecipients
_(no internal calls)_


### external setPayout
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## EasyRPGFStrategy

_File: contracts/strategies/easy-rpgf/EasyRPGFStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipientStatus
-> internal _getRecipientStatus


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __BaseStrategy_init


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
-> internal _afterRegisterRecipient


### external withdraw
_(no internal calls)_


---

## EasyRetroFundingStrategy

_File: contracts/strategies/_poc/easy-rf/EasyRetroFundingStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> private _distributeSingle
    -> internal _hasBeenDistributed
    -> private _setDistributed
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout
  -> internal _getRecipient


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn


### external getStrategyId
_(no internal calls)_


### external hasBeenDistributed
-> internal _hasBeenDistributed


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __EasyRFStrategy_init
  -> internal __BaseStrategy_init
  -> internal _isPoolTimestampValid


### external isDistributionSet
_(no internal calls)_


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
  -> internal _setRecipientStatus
    -> internal _getStatusRowColumn
  -> internal _getUintRecipientStatus
    -> internal _getStatusRowColumn
-> internal _afterRegisterRecipient


### external reviewRecipients
_(no internal calls)_


### external updateDistribution
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## HackathonQVStrategy

_File: contracts/strategies/_poc/qv-hackathon/HackathonQVStrategy.sol_

### external attest
-> internal onAttest


### external getAttestation
_(no internal calls)_


### public getPayouts
-> internal _getPayout


### external getRecipient
-> internal _getRecipient


### external getSchema
_(no internal calls)_


### external initialize
-> internal __HackathonQVStrategy_init
  -> internal __QVBaseStrategy_init
    -> internal _updatePoolTimestamps
  -> internal __SchemaResolver_init


### external isAttestationExpired
_(no internal calls)_


### public isPayable
_(no internal calls)_


### external multiAttest
-> internal onAttest


### external multiRevoke
-> internal onRevoke


### external reviewRecipients
_(no internal calls)_


### external revoke
-> internal onRevoke


### external setAllowedRecipientIds
-> internal _grantEASAttestation


### external setPayoutPercentages
_(no internal calls)_


### external updatePoolTimestamps
-> internal _updatePoolTimestamps


### external withdraw
_(no internal calls)_


---

## HedgeyRFPCommitteeStrategy

_File: contracts/strategies/_poc/hedgey/HedgeyRFPCommitteeStrategy.sol_

### external getRecipientLockupTerm
_(no internal calls)_


### external initialize
-> internal __HedgeyRPFCommiteeStrategy_init
  -> internal __RPFCommiteeStrategy_init


### external setAdminAddress
_(no internal calls)_


### external setAdminTransferOBO
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## LTIPHedgeyGovernorStrategy

_File: contracts/strategies/ltip-hedgey-governor/LTIPHedgeyGovernorStrategy.sol_

### external initialize
-> internal __LTIPHedgeyGovernorStrategy_init
  -> internal __LTIPHedgeyStrategy_init


### external revokeVotes
_(no internal calls)_


### external setAdminTransferOBO
_(no internal calls)_


### external setTimepoint
_(no internal calls)_


### external setVestingAdmin
_(no internal calls)_


---

## LTIPHedgeyStrategy

_File: contracts/strategies/ltip-hedgey/LTIPHedgeyStrategy.sol_

### external cancelRecipients
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getRecipient
_(no internal calls)_


### external getVestingPlan
_(no internal calls)_


### external initialize
-> internal __LTIPHedgeyStrategy_init
  -> internal __LTIPSimpleStrategy_init
    -> internal _isPoolTimestampValid


### external reviewRecipients
_(no internal calls)_


### external setAdminTransferOBO
_(no internal calls)_


### external setVestingAdmin
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## LTIPSimpleStrategy

_File: contracts/strategies/ltip-simple/LTIPSimpleStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
  -> internal _isValidAllocator
-> internal _afterAllocate


### external cancelRecipients
_(no internal calls)_


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> internal _vestAmount
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
_(no internal calls)_


### external getRecipientStatus
-> internal _getRecipientStatus


### external getStrategyId
_(no internal calls)_


### external getVestingPlan
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __LTIPSimpleStrategy_init
  -> internal __BaseStrategy_init
  -> internal _isPoolTimestampValid


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external reviewRecipients
_(no internal calls)_


### external updatePoolTimestamps
-> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## LockupDynamicStrategy

_File: contracts/strategies/_poc/sablier-v2/LockupDynamicStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external cancelStream
_(no internal calls)_


### external changeRecipientSegments
_(no internal calls)_


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> private _distributeToLockupDynamic
-> internal _afterDistribute


### external getAllRecipientStreamIds
_(no internal calls)_


### external getAllo
_(no internal calls)_


### external getBroker
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getRecipientStreamId
_(no internal calls)_


### external getStatus
-> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### public initialize
-> internal __LockupDynamicStrategy_init
  -> internal __BaseStrategy_init
  -> internal _setPoolActive


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external setBroker
_(no internal calls)_


### external setRecipientStatusToInReview
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## LockupLinearStrategy

_File: contracts/strategies/_poc/sablier-v2/LockupLinearStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external cancelStream
_(no internal calls)_


### external changeRecipientDurations
_(no internal calls)_


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> private _distributeToLockupLinear
-> internal _afterDistribute


### external getAllRecipientStreamIds
_(no internal calls)_


### external getAllo
_(no internal calls)_


### external getBroker
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getRecipientStreamId
_(no internal calls)_


### external getStatus
-> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### public initialize
-> internal __LockupLinearStrategy_init
  -> internal __BaseStrategy_init
  -> internal _setPoolActive


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external setBroker
_(no internal calls)_


### external setRecipientStatusToInReview
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## MicroGrantsBaseStrategy

_File: contracts/strategies/_poc/micro-grants/MicroGrantsBaseStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout
  -> internal _getRecipient


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increaseMaxRequestedAmount
-> internal _increaseMaxRequestedAmount


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __MicroGrants_init
  -> internal __BaseStrategy_init
  -> internal _updatePoolTimestamps
    -> internal _isPoolTimestampValid
  -> internal _increaseMaxRequestedAmount
  -> internal _setApprovalThreshold


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
_(no internal calls)_


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external setApprovalThreshold
-> internal _setApprovalThreshold


### external updatePoolTimestamps
-> internal _updatePoolTimestamps
  -> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## MicroGrantsGovStrategy

_File: contracts/strategies/_poc/micro-grants/MicroGrantsGovStrategy.sol_

### external getRecipient
-> internal _getRecipient


### external increaseMaxRequestedAmount
-> internal _increaseMaxRequestedAmount


### external initialize
-> internal __MicroGrants_init
  -> internal _updatePoolTimestamps
    -> internal _isPoolTimestampValid
  -> internal _increaseMaxRequestedAmount
  -> internal _setApprovalThreshold


### external setApprovalThreshold
-> internal _setApprovalThreshold


### external updatePoolTimestamps
-> internal _updatePoolTimestamps
  -> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## MicroGrantsHatsStrategy

_File: contracts/strategies/_poc/micro-grants/MicroGrantsHatsStrategy.sol_

### external getRecipient
-> internal _getRecipient


### external increaseMaxRequestedAmount
-> internal _increaseMaxRequestedAmount


### external initialize
-> internal __MicroGrants_init
  -> internal _updatePoolTimestamps
    -> internal _isPoolTimestampValid
  -> internal _increaseMaxRequestedAmount
  -> internal _setApprovalThreshold


### external setApprovalThreshold
-> internal _setApprovalThreshold


### external updatePoolTimestamps
-> internal _updatePoolTimestamps
  -> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## MicroGrantsStrategy

_File: contracts/strategies/_poc/micro-grants/MicroGrantsStrategy.sol_

### external batchSetAllocator
-> internal _setAllocator


### external getRecipient
-> internal _getRecipient


### external increaseMaxRequestedAmount
-> internal _increaseMaxRequestedAmount


### external initialize
-> internal __MicroGrants_init
  -> internal _updatePoolTimestamps
    -> internal _isPoolTimestampValid
  -> internal _increaseMaxRequestedAmount
  -> internal _setApprovalThreshold


### external setAllocator
-> internal _setAllocator


### external setApprovalThreshold
-> internal _setApprovalThreshold


### external updatePoolTimestamps
-> internal _updatePoolTimestamps
  -> internal _isPoolTimestampValid


### external withdraw
_(no internal calls)_


---

## NFT

_File: contracts/strategies/_poc/wrapped-voting-nftmint/NFT.sol_

### external mintTo
_(no internal calls)_


### public name
_(no internal calls)_


### public symbol
_(no internal calls)_


### public tokenURI
_(no internal calls)_


### external withdrawPayments
_(no internal calls)_


---

## NFTFactory

_File: contracts/strategies/_poc/wrapped-voting-nftmint/NFTFactory.sol_

### external createNFTContract
_(no internal calls)_


---

## ProportionalPayoutStrategy

_File: contracts/strategies/_poc/proportional-payout/ProportionalPayoutStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> internal _getPayout
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __ProtportionalPayoutStrategy_init
  -> internal __BaseStrategy_init
  -> internal _setAllocationTime
  -> internal _setPoolActive


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
-> internal _afterRegisterRecipient


### external setAllocationTime
-> internal _setAllocationTime


---

## QVBaseStrategy

_File: contracts/strategies/qv-base/QVBaseStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> internal _getPayout
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
_(no internal calls)_


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external reviewRecipients
_(no internal calls)_


### external updatePoolTimestamps
-> internal _updatePoolTimestamps


### external withdraw
_(no internal calls)_


---

## QVGovernanceERC20Votes

_File: contracts/strategies/_poc/qv-governance/QVGovernanceERC20Votes.sol_

### external getRecipient
-> internal _getRecipient


### external initialize
-> internal __QVGovernanceERC20Votes_init
  -> internal __QVBaseStrategy_init
    -> internal _updatePoolTimestamps


### external reviewRecipients
_(no internal calls)_


### external updatePoolTimestamps
-> internal _updatePoolTimestamps


### external withdraw
_(no internal calls)_


---

## QVImpactStreamStrategy

_File: contracts/strategies/_poc/qv-impact-stream/QVImpactStreamStrategy.sol_

### external addAllocator
-> internal _addAllocator


### external allocate
-> internal _beforeAllocate
-> internal _allocate
  -> internal _isValidAllocator
  -> internal _isAcceptedRecipient
  -> internal _hasVoiceCreditsLeft
  -> internal _sqrt
-> internal _afterAllocate


### external batchAddAllocator
-> internal _addAllocator


### external batchRemoveAllocator
-> internal _removeAllocator


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external getTotalVotesForRecipient
_(no internal calls)_


### external getVoiceCreditsCastByAllocator
_(no internal calls)_


### external getVoiceCreditsCastByAllocatorToRecipient
_(no internal calls)_


### external getVotesCastByAllocatorToRecipient
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __BaseStrategy_init
-> internal _updatePoolTimestamps


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external recoverFunds
_(no internal calls)_


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
-> internal _afterRegisterRecipient


### external removeAllocator
-> internal _removeAllocator


### external setPayouts
-> internal _getRecipientStatus
  -> internal _getRecipient


### external updatePoolTimestamps
-> internal _updatePoolTimestamps


---

## QVNftTieredStrategy

_File: contracts/strategies/_poc/qv-nft-tiered/QVNftTieredStrategy.sol_

### external getRecipient
-> internal _getRecipient


### external initialize
-> internal __QV_NFT_TieredStrategy_init
  -> internal __QVBaseStrategy_init
    -> internal _updatePoolTimestamps


### external reviewRecipients
_(no internal calls)_


### external updatePoolTimestamps
-> internal _updatePoolTimestamps


### external withdraw
_(no internal calls)_


---

## QVSimpleStrategy

_File: contracts/strategies/qv-simple/QVSimpleStrategy.sol_

### external addAllocator
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external initialize
-> internal __QVBaseStrategy_init
  -> internal _updatePoolTimestamps


### external removeAllocator
_(no internal calls)_


### external reviewRecipients
_(no internal calls)_


### external updatePoolTimestamps
-> internal _updatePoolTimestamps


### external withdraw
_(no internal calls)_


---

## RFPCommitteeStrategy

_File: contracts/strategies/rfp-committee/RFPCommitteeStrategy.sol_

### external getMilestone
_(no internal calls)_


### external getMilestoneStatus
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getRecipient
-> internal _getRecipient


### external increaseMaxBid
-> internal _increaseMaxBid


### external initialize
-> internal __RPFCommiteeStrategy_init
  -> internal __RFPSimpleStrategy_init
    -> internal _increaseMaxBid


### external rejectMilestone
_(no internal calls)_


### external setMilestones
_(no internal calls)_


### external setPoolActive
_(no internal calls)_


### external submitUpcomingMilestone
-> internal _isProfileMember


### external withdraw
_(no internal calls)_


---

## RFPSimpleStrategy

_File: contracts/strategies/rfp-simple/RFPSimpleStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
  -> internal _setPoolActive
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getMilestone
_(no internal calls)_


### external getMilestoneStatus
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external increaseMaxBid
-> internal _increaseMaxBid


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __RFPSimpleStrategy_init
  -> internal __BaseStrategy_init
  -> internal _increaseMaxBid
  -> internal _setPoolActive


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external rejectMilestone
_(no internal calls)_


### external setMilestones
_(no internal calls)_


### external setPoolActive
-> internal _setPoolActive


### external submitUpcomingMilestone
-> internal _isProfileMember


### external withdraw
_(no internal calls)_


---

## RecipientSuperApp

_File: contracts/strategies/_poc/sqf-superfluid/RecipientSuperApp.sol_

### external afterAgreementCreated
-> internal _checkHookParam
  -> public isAcceptedSuperToken
-> internal isAcceptedAgreement
-> internal onFlowCreated
  -> internal onFlowUpdated
    -> private _updateOutflow


### external afterAgreementTerminated
-> internal isAcceptedAgreement
-> public isAcceptedSuperToken
-> internal onFlowUpdated
  -> private _updateOutflow


### external afterAgreementUpdated
-> internal _checkHookParam
  -> public isAcceptedSuperToken
-> internal isAcceptedAgreement
-> internal onFlowUpdated
  -> private _updateOutflow


### external beforeAgreementCreated
_(no internal calls)_


### external beforeAgreementTerminated
-> internal isAcceptedAgreement
-> public isAcceptedSuperToken
-> internal _createCbData


### external beforeAgreementUpdated
-> internal _checkHookParam
  -> public isAcceptedSuperToken
-> internal isAcceptedAgreement
-> internal _createCbData


### external closeIncomingStream
_(no internal calls)_


### external emergencyWithdraw
_(no internal calls)_


### public isAcceptedSuperToken
_(no internal calls)_


---

## RecipientSuperAppFactory

_File: contracts/strategies/_poc/sqf-superfluid/RecipientSuperAppFactory.sol_

### public createRecipientSuperApp
_(no internal calls)_


---

## Registry

_File: contracts/core/Registry.sol_

### external acceptProfileOwnership
_(no internal calls)_


### external addMembers
_(no internal calls)_


### external createProfile
-> internal _generateProfileId
-> internal _generateAnchor


### external getProfileByAnchor
_(no internal calls)_


### external getProfileById
_(no internal calls)_


### external initialize
_(no internal calls)_


### external isMemberOfProfile
-> internal _isMemberOfProfile


### external isOwnerOfProfile
-> internal _isOwnerOfProfile


### external isOwnerOrMemberOfProfile
-> internal _isOwnerOfProfile
-> internal _isMemberOfProfile


### external recoverFunds
-> internal _transferAmount


### external removeMembers
_(no internal calls)_


### external updateProfileMetadata
_(no internal calls)_


### external updateProfileName
-> internal _generateAnchor


### external updateProfilePendingOwner
_(no internal calls)_


---

## SQFSuperFluidStrategy

_File: contracts/strategies/_poc/sqf-superfluid/SQFSuperFluidStrategy.sol_

### external adjustWeightings
-> internal _updateMemberUnits


### external allocate
-> internal _beforeAllocate
-> internal _allocate
  -> internal _isValidAllocator
-> internal _afterAllocate


### external cancelRecipients
-> internal _updateMemberUnits


### external closeStream
_(no internal calls)_


### external distribute
-> internal _beforeDistribute
-> internal _distribute
  -> internal _checkOnlyAfterRegistration
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipient
-> internal _getRecipient


### external getRecipientId
_(no internal calls)_


### external getRecipientStatus
-> internal _getRecipientStatus
  -> internal _getRecipient


### external getStrategyId
_(no internal calls)_


### external getSuperApp
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __BaseStrategy_init
-> library SuperTokenV1Library.createPool
-> internal _updatePoolTimestamps


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
  -> internal _isProfileMember
-> internal _afterRegisterRecipient


### external reviewRecipients
-> internal _updateMemberUnits


### external updateMinPassportScore
_(no internal calls)_


### external updatePoolTimestamps
-> internal _updatePoolTimestamps


### external withdraw
_(no internal calls)_


---

## SchemaResolver

_File: contracts/strategies/_poc/qv-hackathon/SchemaResolver.sol_

### external attest
_(no internal calls)_


### public isPayable
_(no internal calls)_


### external multiAttest
_(no internal calls)_


### external multiRevoke
_(no internal calls)_


### external revoke
_(no internal calls)_


---

## SimpleProjectRegistry

_File: contracts/strategies/_poc/donation-voting-custom-registry/SimpleProjectRegistry.sol_

### external addProject
-> internal _addProject


### external addProjects
-> internal _addProject


### external removeProject
-> internal _removeProject


### external removeProjects
-> internal _removeProject


---

## WrappedVotingNftMintStrategy

_File: contracts/strategies/_poc/wrapped-voting-nftmint/WrappedVotingNftMintStrategy.sol_

### external allocate
-> internal _beforeAllocate
-> internal _allocate
-> internal _afterAllocate


### external distribute
-> internal _beforeDistribute
-> internal _distribute
-> internal _afterDistribute


### external getAllo
_(no internal calls)_


### external getPayouts
-> internal _getPayout


### external getPoolAmount
_(no internal calls)_


### external getPoolId
_(no internal calls)_


### external getRecipientStatus
-> internal _getRecipientStatus


### external getStrategyId
_(no internal calls)_


### external increasePoolAmount
-> internal _beforeIncreasePoolAmount
-> internal _afterIncreasePoolAmount


### external initialize
-> internal __WrappedVotingStrategy_init
  -> internal __BaseStrategy_init
  -> internal _isPoolTimestampValid


### external isPoolActive
-> internal _isPoolActive


### external isValidAllocator
-> internal _isValidAllocator


### external registerRecipient
-> internal _beforeRegisterRecipient
-> internal _registerRecipient
-> internal _afterRegisterRecipient


### external setAllocationTimes
-> internal _setAllocationTimes
  -> internal _isPoolTimestampValid

