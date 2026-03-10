# Callpaths — Brevis

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AccessControl

_File: contracts/safeguard/AccessControl.sol_

### public getRoleAccounts
_(no internal calls)_


### public grantRole
-> internal _grantRole
  -> public hasRole


### public grantRoles
-> internal _grantRole
  -> public hasRole


### public hasRole
_(no internal calls)_


### public numRoleAccounts
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceRole
-> internal _revokeRole
  -> public hasRole


### public revokeRole
-> internal _revokeRole
  -> public hasRole


### public revokeRoles
-> internal _revokeRole
  -> public hasRole


### public transferOwnership
-> private _setOwner


---

## AggregationVerifier

_File: contracts/sdk/core/verifiers/AggregationVerifier.sol_

### public verifyProof
-> internal publicInputMSM


### external verifyRaw
-> public verifyProof
  -> internal publicInputMSM


---

## AnchorBlocks

_File: contracts/light-client-eth/AnchorBlocks.sol_

### public addProvers
-> private _addProver


### public isActiveProver
_(no internal calls)_


### public numProvers
_(no internal calls)_


### public pause
_(no internal calls)_


### external processUpdate
-> private verifyHeadBlock
  -> private hasSupermajority
  -> private verifyExecutionPayload
    -> library Helpers.isValidMerkleBranch
    -> private verifyMerkleProof
      -> library Helpers.isValidMerkleBranch
  -> library Helpers.revertEndian
-> private doUpdate


### external processUpdateWithChainProof
-> private verifyHeadBlock
  -> private hasSupermajority
  -> private verifyExecutionPayload
    -> library Helpers.isValidMerkleBranch
    -> private verifyMerkleProof
      -> library Helpers.isValidMerkleBranch
  -> library Helpers.revertEndian
-> private verifyChainProof
-> private doUpdate


### public removeProvers
-> private _removeProver


### external setLightClient
_(no internal calls)_


### public unpause
_(no internal calls)_


---

## BSCValidatorSet

_File: contracts/light-client-others/bsc-tendermint/BSCValidatorSet.sol_

### external handleAckPackage
_(no internal calls)_


### external handleFailAckPackage
_(no internal calls)_


### external handleSynPackage
-> internal decodeValidatorSetSynPackage
  -> internal decodeValidator
-> internal updateValidatorSet
  -> private checkValidatorSet
  -> private doUpdateState
    -> private isSameValidator


### external init
-> internal decodeValidatorSetSynPackage
  -> internal decodeValidator


### external isCurrentValidator
_(no internal calls)_


---

## BVN

_File: contracts/bvn/BVN.sol_

### external deregisterBrevisValidator
_(no internal calls)_


### public getBondedTokens
_(no internal calls)_


### public getBondedValidatorNum
_(no internal calls)_


### public getBondedValidators
-> public getBondedValidatorNum


### public getRegisteredValidatorNum
_(no internal calls)_


### public getRegisteredValidators
_(no internal calls)_


### public isBondedValidator
-> public isRegisteredValidator


### public isRegisteredValidator
_(no internal calls)_


### external registerBrevisValidator
_(no internal calls)_


### external slash
-> public verifySignatures
  -> public getBondedTokens
  -> public isBondedValidator
    -> public isRegisteredValidator


### external updateValidatorSigner
_(no internal calls)_


### public verifySignatures
-> public getBondedTokens
-> public isBondedValidator
  -> public isRegisteredValidator


---

## BaseFactory

_File: contracts/apps/uniswap-v4/uniswap-v4-hook/BaseFactory.sol_

### public mineDeploy
-> public mineSalt
  -> internal _computeHookAddress
  -> internal _isPrefix


### public mineSalt
-> internal _computeHookAddress
-> internal _isPrefix


---

## BaseHook

_File: contracts/apps/uniswap-v4/uniswap-v4-hook/BaseHook.sol_

### external afterDonate
_(no internal calls)_


### external afterInitialize
_(no internal calls)_


### external afterModifyPosition
_(no internal calls)_


### external afterSwap
_(no internal calls)_


### external beforeDonate
_(no internal calls)_


### external beforeInitialize
_(no internal calls)_


### external beforeModifyPosition
_(no internal calls)_


### external beforeSwap
_(no internal calls)_


### external lockAcquired
_(no internal calls)_


### public owner
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## BeaconVerifier

_File: contracts/verifiers/BeaconVerifier.sol_

### public verifyBlsSigProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> library Common.accumulate
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


### public verifyCommitteeRootMappingProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> private verifyingKey1
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> library Common.accumulate
-> library Pairing.pairing
-> library Pairing.negate


### public verifySignatureProof
-> public verifyBlsSigProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> internal verifyingKey
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> library Common.accumulate
  -> library Pairing.plus
  -> library Pairing.pairing
  -> library Pairing.negate


### public verifySyncCommitteeRootMappingProof
-> public verifyCommitteeRootMappingProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> private verifyingKey1
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> library Common.accumulate
  -> library Pairing.pairing
  -> library Pairing.negate


---

## BlockChunks

_File: contracts/chunk-sync/BlockChunks.sol_

### public addProvers
-> private _addProver


### public historicalRoots
_(no internal calls)_


### public isActiveProver
_(no internal calls)_


### public isBlockHashValid
-> public historicalRoots


### public numProvers
_(no internal calls)_


### public pause
_(no internal calls)_


### public removeProvers
-> private _removeProver


### public unpause
_(no internal calls)_


### external updateAnchorBlockProvider
_(no internal calls)_


### external updateOld
-> internal getBoundaryBlockData
-> public historicalRoots
-> private verifyRaw


### external updateRecent
-> internal getBoundaryBlockData
-> private verifyRaw


### external updateVerifierAddress
_(no internal calls)_


---

## BlsSigVerifier

_File: contracts/verifiers/zk-verifiers/BlsSigVerifier.sol_

### public verifyBlsSigProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> library Common.accumulate
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


---

## Bn254Agg16Bn254Verifier

_File: contracts/sdk/core/verifiers/Bn254Agg16Bn254Verifier.sol_

### public verifyProof
-> internal publicInputMSM


### external verifyRaw
_(no internal calls)_


---

## BrevisAccess

_File: contracts/safeguard/BrevisAccess.sol_

### public addPauser
-> private _addPauser
  -> public isPauser


### public addPausers
-> private _addPauser
  -> public isPauser


### public addProvers
-> private _addProver


### public isActiveProver
_(no internal calls)_


### public isPauser
_(no internal calls)_


### public numPausers
_(no internal calls)_


### public numProvers
_(no internal calls)_


### public pause
_(no internal calls)_


### public removePauser
-> private _removePauser
  -> public isPauser


### public removePausers
-> private _removePauser
  -> public isPauser


### public removeProvers
-> private _removeProver


### public renouncePauser
-> private _removePauser
  -> public isPauser


### public unpause
_(no internal calls)_


---

## BrevisAggProof

_File: contracts/sdk/core/BrevisAggProof.sol_

### public addProvers
-> private _addProver


### public isActiveProver
_(no internal calls)_


### public numProvers
_(no internal calls)_


### public pause
_(no internal calls)_


### public removeProvers
-> private _removeProver


### public setAggVkHash
_(no internal calls)_


### public setDummyInputCommitments
_(no internal calls)_


### external submitAggProof
-> internal unpack


### public unpause
_(no internal calls)_


### public updateAggProofVerifierAddresses
_(no internal calls)_


### public updateSmtContract
_(no internal calls)_


### external validateAggProofData
_(no internal calls)_


---

## BrevisApp

_File: contracts/sdk/apps/framework/BrevisApp.sol_

### public applyBrevisOpResult
-> private _getBrevisConfig
-> internal handleOpProofResult


### external applyBrevisOpResults
-> private _getBrevisConfig
-> internal handleOpProofResult


### external brevisBatchCallback
-> internal handleProofResult


### external brevisCallback
-> internal handleProofResult


---

## BrevisAppZkOnly

_File: contracts/sdk/apps/framework/BrevisAppZkOnly.sol_

### external brevisBatchCallback
-> internal handleProofResult


### external brevisCallback
-> internal handleProofResult


---

## BrevisBn254Verifier

_File: contracts/verifiers/zk-verifiers/BrevisBn254Verifier.sol_

### public verifyProof
-> internal publicInputMSM


---

## BrevisDispute

_File: contracts/sdk/core/BrevisDispute.sol_

### external askForDataAvailabilityProof
_(no internal calls)_


### external askForDataValidityProof
_(no internal calls)_


### external askForRequestData
_(no internal calls)_


### external getChallengeWindow
_(no internal calls)_


### external getDisputeStatus
_(no internal calls)_


### external getResponseDeadline
_(no internal calls)_


### external postDataAvailabilityProof
_(no internal calls)_


### external postDataValidityProof
_(no internal calls)_


### external postRequestData
_(no internal calls)_


### external setChallengeWindow
_(no internal calls)_


### external setDisputeDeposits
_(no internal calls)_


### external setResponseTimeout
_(no internal calls)_


---

## BrevisPlonky2SmtVerifier

_File: contracts/verifiers/zk-verifiers/BrevisPlonky2SmtVerifier.sol_

### public verifyProof
-> internal publicInputMSM


---

## BrevisProof

_File: contracts/sdk/core/BrevisProof.sol_

### external init
_(no internal calls)_


### public setAggVkHash
_(no internal calls)_


### public setDummyInputCommitments
_(no internal calls)_


### external submitAggProof
-> internal unpack


### external submitProof
-> internal unpackProofData
-> private verifyRaw


### public updateAggProofVerifierAddresses
_(no internal calls)_


### public updateSmtContract
_(no internal calls)_


### public updateVerifierAddress
_(no internal calls)_


### external validateAggProofData
_(no internal calls)_


### external validateProofAppData
_(no internal calls)_


---

## BrevisProofOwnerProxy

_File: contracts/safeguard/governed-owner/proxies/BrevisProofOwnerProxy.sol_

### public initGov
_(no internal calls)_


### external proposeSetAggVkHashProposal
_(no internal calls)_


### external proposeSetDummyInputCommitments
_(no internal calls)_


### external proposeUpdateAggProofVerifierAddresses
_(no internal calls)_


### external proposeUpdateSmtContract
_(no internal calls)_


### external proposeUpdateVerifierAddress
_(no internal calls)_


---

## BrevisRequest

_File: contracts/sdk/core/BrevisRequest.sol_

### public addProvers
-> private _addProver


### external applyBrevisAggProof
_(no internal calls)_


### external applyBrevisProof
_(no internal calls)_


### external collectFee
_(no internal calls)_


### external dataURL
_(no internal calls)_


### external fulfillOpRequests
-> private _bitSet
-> private _submitOpStates


### external fulfillRequest
-> private _brevisCallback


### external fulfillRequests
-> private _brevisCallback


### external increaseGasFee
_(no internal calls)_


### external init
_(no internal calls)_


### public isActiveProver
_(no internal calls)_


### public numProvers
_(no internal calls)_


### public pause
_(no internal calls)_


### external queryRequestStatus
-> private _queryRequestStatus


### external refund
_(no internal calls)_


### public removeProvers
-> private _removeProver


### external sendRequest
_(no internal calls)_


### external setAvsSigsVerifier
_(no internal calls)_


### external setBaseDataURL
_(no internal calls)_


### external setBrevisDispute
_(no internal calls)_


### external setBrevisProof
_(no internal calls)_


### external setBvnSigsVerifier
_(no internal calls)_


### external setFeeCollector
_(no internal calls)_


### external setRequestStatus
_(no internal calls)_


### external setRequestTimeout
_(no internal calls)_


### public unpause
_(no internal calls)_


### external validateOpAppData
-> private _validateOpAppData
  -> private _queryRequestStatus


---

## BrevisRequestOwnerProxy

_File: contracts/safeguard/governed-owner/proxies/BrevisRequestOwnerProxy.sol_

### public initGov
_(no internal calls)_


### external proposeSetAvsSigsVerifier
_(no internal calls)_


### external proposeSetBaseDataURL
_(no internal calls)_


### external proposeSetBrevisDispute
_(no internal calls)_


### external proposeSetBrevisProof
_(no internal calls)_


### external proposeSetBvnSigsVerifier
_(no internal calls)_


### external proposeSetChallengeWindow
_(no internal calls)_


### external proposeSetDisputeDeposits
_(no internal calls)_


### external proposeSetFeeCollector
_(no internal calls)_


### external proposeSetRequestTimeout
_(no internal calls)_


### external proposeSetResponseTimeout
_(no internal calls)_


---

## BrevisUniNFT

_File: contracts/apps/demo-tx-uniswap-amount/BrevisUniNFT.sol_

### external mint
_(no internal calls)_


### public owner
_(no internal calls)_


### external setBaseURI
_(no internal calls)_


### external setMinter
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## CommitteeRootMappingVerifier

_File: contracts/verifiers/zk-verifiers/CommitteeRootMappingVerifier.sol_

### public verifyCommitteeRootMappingProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> private verifyingKey1
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> library Common.accumulate
-> library Pairing.pairing
-> library Pairing.negate


---

## CommonOwnerProxy

_File: contracts/safeguard/governed-owner/proxies/CommonOwnerProxy.sol_

### public initGov
_(no internal calls)_


### external proposeTransferOwnership
_(no internal calls)_


### external proposeUpdateGovernor
_(no internal calls)_


### external proposeUpdateGovernors
_(no internal calls)_


### external proposeUpdatePauser
_(no internal calls)_


### external proposeUpdatePausers
_(no internal calls)_


### external proposeUpdateProvers
_(no internal calls)_


---

## CrossChain

_File: contracts/light-client-others/bsc-tendermint/CrossChain.sol_

### public encodePayload
-> library Memory.fromBytes
-> library Memory.copy


### external handlePackage
-> internal decodePayloadHeader
  -> library Memory.fromBytes
  -> library Memory.copy
-> internal sendPackage
-> public encodePayload
  -> library Memory.fromBytes
  -> library Memory.copy


### external init
_(no internal calls)_


### external sendSynPackage
-> internal sendPackage
-> public encodePayload
  -> library Memory.fromBytes
  -> library Memory.copy


---

## Ed25519Verifier

_File: contracts/light-client-others/bsc-tendermint/Ed25519Verifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


---

## EthChunkOf128Verifier

_File: contracts/verifiers/zk-verifiers/EthChunkOf128Verifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> library Common.accumulate
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


### external verifyRaw
-> public verifyProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> internal verifyingKey
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> library Common.accumulate
  -> library Pairing.plus
  -> library Pairing.pairing
  -> library Pairing.negate


---

## EthChunkOf4Verifier

_File: contracts/verifiers/zk-verifiers/EthChunkOf4Verifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


### external verifyRaw
-> public verifyProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> internal verifyingKey
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> internal accumulate
    -> library Pairing.scalar_mul_raw
    -> library Pairing.plus_raw
  -> library Pairing.plus
  -> library Pairing.pairing
  -> library Pairing.negate


---

## EthStorageVerifier

_File: contracts/verifiers/zk-verifiers/EthStorageVerifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


### external verifyRaw
-> public verifyProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> internal verifyingKey
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> internal accumulate
    -> library Pairing.scalar_mul_raw
    -> library Pairing.plus_raw
  -> library Pairing.plus
  -> library Pairing.pairing
  -> library Pairing.negate


---

## EthereumLightClient

_File: contracts/light-client-eth/EthereumLightClient.sol_

### public addProvers
-> private _addProver


### public computeDomain
_(no internal calls)_


### public computeSigningRoot
-> library Helpers.hashTreeRoot


### external finalizedExecutionStateRootAndSlot
_(no internal calls)_


### public isActiveProver
_(no internal calls)_


### external latestFinalizedSlotAndCommitteeRoots
_(no internal calls)_


### public numProvers
_(no internal calls)_


### external optimisticExecutionStateRootAndSlot
_(no internal calls)_


### public pause
_(no internal calls)_


### external processLightClientForceUpdate
-> private currentSlot
-> private applyFinalityUpdate
  -> private computeSyncCommitteePeriodAtSlot
    -> private computeSyncCommitteePeriod
    -> private computeEpochAtSlot


### public processLightClientUpdate
-> private hasSupermajority
-> private isBetterUpdate
  -> private hasSupermajority
  -> private hasRelavantSyncCommittee
    -> private hasNextSyncCommitteeProof
    -> private computeSyncCommitteePeriodAtSlot
      -> private computeSyncCommitteePeriod
      -> private computeEpochAtSlot
  -> private hasFinalityProof
  -> private computeSyncCommitteePeriodAtSlot
    -> private computeSyncCommitteePeriod
    -> private computeEpochAtSlot
-> private validateLightClientUpdate
  -> private currentSlot
  -> private computeSyncCommitteePeriodAtSlot
    -> private computeSyncCommitteePeriod
    -> private computeEpochAtSlot
  -> private hasNextSyncCommitteeProof
  -> private hasFinalityProof
  -> library Helpers.isValidMerkleBranch
  -> library Helpers.hashTreeRoot
  -> private verifyExecutionPayload
    -> library Helpers.isValidMerkleBranch
  -> public verifyCommitteeSignature
    -> private computeSyncCommitteePeriodAtSlot
      -> private computeSyncCommitteePeriod
      -> private computeEpochAtSlot
    -> private computeForkVersion
    -> private computeEpochAtSlot
    -> public computeDomain
    -> public computeSigningRoot
      -> library Helpers.hashTreeRoot
-> private applyOptimisticUpdate
-> private hasNextSyncCommittee
  -> private hasNextSyncCommitteeProof
  -> private hasFinalityProof
  -> private computeSyncCommitteePeriodAtSlot
    -> private computeSyncCommitteePeriod
    -> private computeEpochAtSlot
-> private applyFinalityUpdate
  -> private computeSyncCommitteePeriodAtSlot
    -> private computeSyncCommitteePeriod
    -> private computeEpochAtSlot


### public removeProvers
-> private _removeProver


### public unpause
_(no internal calls)_


### external updateForkVersion
_(no internal calls)_


### public verifyCommitteeSignature
-> private computeSyncCommitteePeriodAtSlot
  -> private computeSyncCommitteePeriod
  -> private computeEpochAtSlot
-> private computeForkVersion
-> private computeEpochAtSlot
-> public computeDomain
-> public computeSigningRoot
  -> library Helpers.hashTreeRoot


---

## FeeVault

_File: contracts/sdk/core/FeeVault.sol_

### external collectFee
_(no internal calls)_


### public owner
_(no internal calls)_


### external setFeeCollector
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## Friendship

_File: contracts/apps/demo-tx-friendship/Friendship.sol_

### public owner
_(no internal calls)_


### external setTxVerifier
_(no internal calls)_


### external submitFriendshipProof
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## Govern

_File: contracts/bvn/Govern.sol_

### external collectForfeiture
_(no internal calls)_


### external confirmParamProposal
-> public getParamProposalVote


### external createParamProposal
_(no internal calls)_


### public getParamProposalVote
_(no internal calls)_


### external voteParam
_(no internal calls)_


---

## GovernedOwnerProxy

_File: contracts/safeguard/governed-owner/GovernedOwnerProxy.sol_

### external proposeChangeProxyAdmin
_(no internal calls)_


### external proposeProcessLightClientForceUpdate
_(no internal calls)_


### external proposeSetAggVkHashProposal
_(no internal calls)_


### external proposeSetAnchorProvider
_(no internal calls)_


### external proposeSetAvsSigsVerifier
_(no internal calls)_


### external proposeSetBaseDataURL
_(no internal calls)_


### external proposeSetBrevisDispute
_(no internal calls)_


### external proposeSetBrevisProof
_(no internal calls)_


### external proposeSetBvnSigsVerifier
_(no internal calls)_


### external proposeSetChallengeWindow
_(no internal calls)_


### external proposeSetCircuitDigest
_(no internal calls)_


### external proposeSetDisputeDeposits
_(no internal calls)_


### external proposeSetDummyInputCommitments
_(no internal calls)_


### external proposeSetFeeCollector
_(no internal calls)_


### external proposeSetLightClient
_(no internal calls)_


### external proposeSetRequestTimeout
_(no internal calls)_


### external proposeSetResponseTimeout
_(no internal calls)_


### external proposeSetRootUpdater
_(no internal calls)_


### external proposeSetVerifier
_(no internal calls)_


### external proposeTransferOwnership
_(no internal calls)_


### external proposeUpdateAggProofVerifierAddresses
_(no internal calls)_


### external proposeUpdateForkVersion
_(no internal calls)_


### external proposeUpdateGovernor
_(no internal calls)_


### external proposeUpdateGovernors
_(no internal calls)_


### external proposeUpdatePauser
_(no internal calls)_


### external proposeUpdatePausers
_(no internal calls)_


### external proposeUpdateProvers
_(no internal calls)_


### external proposeUpdateSmtContract
_(no internal calls)_


### external proposeUpdateVerifierAddress
_(no internal calls)_


### external proposeUpgrade
_(no internal calls)_


### external proposeUpgradeAndCall
_(no internal calls)_


### external proposeUpgradeTo
_(no internal calls)_


### external proposeUpgradeToAndCall
_(no internal calls)_


---

## Governor

_File: contracts/safeguard/Governor.sol_

### public addGovernor
-> private _addGovernor
  -> public isGovernor


### public addGovernors
-> private _addGovernor
  -> public isGovernor


### public isGovernor
_(no internal calls)_


### public owner
_(no internal calls)_


### public removeGovernor
-> private _removeGovernor
  -> public isGovernor


### public removeGovernors
-> private _removeGovernor
  -> public isGovernor


### public renounceGovernor
-> private _removeGovernor
  -> public isGovernor


### public transferOwnership
-> private _setOwner


---

## LightClientOwnerProxy

_File: contracts/safeguard/governed-owner/proxies/LightClientOwnerProxy.sol_

### public initGov
_(no internal calls)_


### external proposeProcessLightClientForceUpdate
_(no internal calls)_


### external proposeSetLightClient
_(no internal calls)_


### external proposeUpdateForkVersion
_(no internal calls)_


---

## MessageApp

_File: contracts/apps/message-bridge/framework/MessageApp.sol_

### external executeMessage
_(no internal calls)_


---

## MessageBridge

_File: contracts/apps/message-bridge/MessageBridge.sol_

### external executeMessage
-> private _getSlotAndMessageId
  -> library MsgLib.computeMessageId
-> private _verifyAccountAndStorageProof
  -> private _retrieveStorageRoot
    -> public getExecutionStateRootAndSlot
    -> library MerkleProofTree.read
  -> library MerkleProofTree.read
-> private _executeMessage
  -> private _handleExecutionRevert
    -> library MsgLib.checkRevertMsg


### external executeMessageWithZkProof
-> private _getSlotAndMessageId
  -> library MsgLib.computeMessageId
-> private _verifyZkSlotValueProof
-> private _executeMessage
  -> private _handleExecutionRevert
    -> library MsgLib.checkRevertMsg


### public getExecutionStateRootAndSlot
_(no internal calls)_


### public owner
_(no internal calls)_


### external sendMessage
-> library MsgLib.computeMessageId


### external setLightClient
_(no internal calls)_


### public setPreExecuteMessageGasUsage
_(no internal calls)_


### external setRemoteMessageBridge
_(no internal calls)_


### external setSlotValueVerifier
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## MessageReceiverApp

_File: contracts/apps/message-bridge/framework/MessageReceiverApp.sol_

### external executeMessage
_(no internal calls)_


---

## MintableERC20

_File: contracts/apps/message-bridge/apps/token-bridge/MintableERC20.sol_

### public decimals
_(no internal calls)_


### public mint
_(no internal calls)_


### public minter
_(no internal calls)_


### public owner
_(no internal calls)_


### external setMinter
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## MsgInOrder

_File: contracts/apps/message-bridge/apps/examples/MsgInOrder.sol_

### external sendMessage
_(no internal calls)_


---

## MsgReceiver

_File: contracts/apps/demo-slot-value/MsgProof.sol_

### external recvMsg
_(no internal calls)_


---

## MsgSender

_File: contracts/apps/demo-slot-value/MsgProof.sol_

### external sendMsg
_(no internal calls)_


---

## MsgTest

_File: contracts/apps/message-bridge/apps/examples/MsgTest.sol_

### external sendMessage
_(no internal calls)_


---

## MyBrevisApp

_File: contracts/sdk/apps/examples/dummy/MyBrevisApp.sol_

### public applyBrevisOpResult
-> private _getBrevisConfig
-> internal handleOpProofResult


### external applyBrevisOpResults
-> private _getBrevisConfig
-> internal handleOpProofResult


### external brevisBatchCallback
-> internal handleProofResult


### external brevisCallback
-> internal handleProofResult


### public owner
_(no internal calls)_


### external setBrevisOpConfig
_(no internal calls)_


### external setBrevisRequest
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## Ownable

_File: contracts/safeguard/Ownable.sol_

### public owner
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## OwnerProxyBase

_File: contracts/safeguard/governed-owner/proxies/OwnerProxyBase.sol_

### public initGov
_(no internal calls)_


---

## Pauser

_File: contracts/safeguard/Pauser.sol_

### public addPauser
-> private _addPauser
  -> public isPauser


### public addPausers
-> private _addPauser
  -> public isPauser


### public isPauser
_(no internal calls)_


### public numPausers
_(no internal calls)_


### public owner
_(no internal calls)_


### public pause
_(no internal calls)_


### public removePauser
-> private _removePauser
  -> public isPauser


### public removePausers
-> private _removePauser
  -> public isPauser


### public renouncePauser
-> private _removePauser
  -> public isPauser


### public transferOwnership
-> private _setOwner


### public unpause
_(no internal calls)_


---

## PegBridge

_File: contracts/apps/message-bridge/apps/token-bridge/PegBridge.sol_

### external burn
-> private _burn


### external deletePegTokens
_(no internal calls)_


### external deleteVaultTokens
_(no internal calls)_


### public owner
_(no internal calls)_


### external setBridgeTokens
_(no internal calls)_


### external setMinBurn
_(no internal calls)_


### external setTokenVault
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## Plonky2AggProofVerifier

_File: contracts/sdk/core/verifiers/Plonky2AggProofVerifier.sol_

### public verifyProof
-> internal publicInputMSM


### external verifyRaw
_(no internal calls)_


---

## Plonky2ProofVerifier

_File: contracts/sdk/core/verifiers/Plonky2ProofVerifier.sol_

### public verifyProof
-> internal publicInputMSM


### external verifyRaw
_(no internal calls)_


---

## Plonky2ProofVerifierForxLayer

_File: contracts/sdk/core/verifiers/Plonky2ProofVerifierForxLayer.sol_

### public verifyProof
-> internal publicInputMSM


### external verifyRaw
_(no internal calls)_


---

## PoALightClient

_File: contracts/light-client-others/poa/PoALightClient.sol_

### external finalizedExecutionStateRootAndSlot
_(no internal calls)_


### external optimisticExecutionStateRootAndSlot
_(no internal calls)_


### external updateHeader
-> internal _retrieveSignerInfo
  -> library Memory.range
  -> internal _hashHeaderWithChainId
    -> library RLPWriter.writeUint
    -> library RLPWriter.writeBytes
    -> library RLPWriter.writeAddress
    -> library RLPWriter.writeList
  -> library ECDSA.recover


---

## PostNumber

_File: contracts/apps/demo-receipt-tx/PostNumber.sol_

### external sendNumber
_(no internal calls)_


---

## ReceiptCircuitProofVerifier

_File: contracts/verifiers/zk-verifiers/ReceiptCircuitProofVerifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


### external verifyRaw
-> public verifyProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> internal verifyingKey
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> internal accumulate
    -> library Pairing.scalar_mul_raw
    -> library Pairing.plus_raw
  -> library Pairing.plus
  -> library Pairing.pairing
  -> library Pairing.negate


---

## ReceiptVerifier

_File: contracts/verifiers/ReceiptVerifier.sol_

### public decodeReceipt
_(no internal calls)_


### public owner
_(no internal calls)_


### public transferOwnership
-> private _setOwner


### external updateBlockChunks
_(no internal calls)_


### external updateVerifierAddress
_(no internal calls)_


### public verifyReceipt
-> internal getProofData
-> private verifyRaw
-> internal getFromAuxiBlkVerifyInfo
-> external_callback IBlockChunks.BlockHashWitness
-> public decodeReceipt


### external verifyReceiptAndLog
-> public verifyReceipt
  -> internal getProofData
  -> private verifyRaw
  -> internal getFromAuxiBlkVerifyInfo
  -> external_callback IBlockChunks.BlockHashWitness
  -> public decodeReceipt


---

## SMT

_File: contracts/smt/SMT.sol_

### public addProvers
-> private _addProver


### public getLatestRoot
_(no internal calls)_


### public isActiveProver
_(no internal calls)_


### public isSmtRootValid
_(no internal calls)_


### public numProvers
_(no internal calls)_


### public pause
_(no internal calls)_


### external postRoot
_(no internal calls)_


### public removeProvers
-> private _removeProver


### external setAnchorProvider
_(no internal calls)_


### external setCircuitDigest
_(no internal calls)_


### external setRootUpdater
_(no internal calls)_


### external setVerifier
_(no internal calls)_


### public unpause
_(no internal calls)_


### external updateRoot
-> private verifyProof


---

## SMTUpdateCircuitProofOnOpVerifier

_File: contracts/verifiers/zk-verifiers/SMTUpdateSD18CD7ForOpVerifier.sol_

### public verifyProof
-> internal publicInputMSM


---

## SMTUpdateCircuitProofVerifier

_File: contracts/verifiers/zk-verifiers/SMTUpdateCircuitProofSD18CD7Verifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


---

## SameChainAnchorBlocks

_File: contracts/light-client-eth/SameChainAnchorBlock.sol_

### external blocks
_(no internal calls)_


---

## SigsVerifier

_File: contracts/bvn/SigsVerifier.sol_

### external increaseNoticePeriod
_(no internal calls)_


### external notifyResetSigners
_(no internal calls)_


### public owner
_(no internal calls)_


### external resetSigners
-> private _updateSigners


### public transferOwnership
-> private _setOwner


### external updateSigners
-> public verifySigs
  -> private _verifySignedPowers
-> private _updateSigners


### public verifySigs
-> private _verifySignedPowers


---

## SimpleGovernance

_File: contracts/safeguard/governed-owner/SimpleGovernance.sol_

### public countVotes
-> public getVote


### external createParamChangeProposal
-> private _createProposal


### external createProposal
-> private _createProposal


### external createProxyUpdateProposal
-> private _createProposal


### external createTransferTokenProposal
-> private _createProposal


### external createVoterUpdateProposal
-> private _createProposal


### external executeProposal
-> public countVotes
  -> public getVote
-> private _setVoter
-> private _removeVoter
-> private _transfer


### public getVote
_(no internal calls)_


### public getVoters
_(no internal calls)_


### external setNativeTokenTransferGas
_(no internal calls)_


### public voteProposal
_(no internal calls)_


### external voteProposals
-> public voteProposal


---

## SlotValue

_File: contracts/apps/demo-slot-value/SlotValue.sol_

### external submitSlotValuePoof
_(no internal calls)_


---

## SlotValueExample

_File: contracts/sdk/apps/examples/slot/SlotValueExample.sol_

### public applyBrevisOpResult
-> private _getBrevisConfig
-> internal handleOpProofResult


### external applyBrevisOpResults
-> private _getBrevisConfig
-> internal handleOpProofResult


### external brevisBatchCallback
-> internal handleProofResult
  -> internal decodeOutput


### external brevisCallback
-> internal handleProofResult
  -> internal decodeOutput


### public owner
_(no internal calls)_


### external setVkHash
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## SlotValueVerifier

_File: contracts/verifiers/SlotValueVerifier.sol_

### public owner
_(no internal calls)_


### public transferOwnership
-> private _setOwner


### external updateBlockChunks
_(no internal calls)_


### external updateVerifierAddress
_(no internal calls)_


### external verifySlotValue
-> private verifyRaw
-> internal getFromBlkVerifyInfo
-> internal getProofData
-> external_callback IBlockChunks.BlockHashWitness


---

## SmtOwnerProxy

_File: contracts/safeguard/governed-owner/proxies/SmtOwnerProxy.sol_

### public initGov
_(no internal calls)_


### external proposeSetAnchorProvider
_(no internal calls)_


### external proposeSetCircuitDigest
_(no internal calls)_


### external proposeSetRootUpdater
_(no internal calls)_


### external proposeSetVerifier
_(no internal calls)_


---

## Staking

_File: contracts/bvn/Staking.sol_

### public addPauser
-> private _addPauser
  -> public isPauser


### public addPausers
-> private _addPauser
  -> public isPauser


### public addWhitelistedAccount
-> public isWhitelisted


### public addWhitelistedAccounts
-> public addWhitelistedAccount
  -> public isWhitelisted


### external bondValidator
-> public hasMinRequiredTokens
  -> private _shareToToken
-> private _bondValidator
  -> private _setBondedValidator
-> private _decentralizationCheck
  -> public getQuorumTokens
-> private _replaceBondedValidator
  -> private _setUnbondingValidator
  -> private _setBondedValidator


### external collectForfeiture
_(no internal calls)_


### external completeUndelegate
-> private _shareToToken


### external confirmUnbondedValidator
_(no internal calls)_


### public delegate
-> private _tokenToShare
-> private _decentralizationCheck
  -> public getQuorumTokens


### external drainToken
_(no internal calls)_


### public getBondedValidatorNum
_(no internal calls)_


### public getBondedValidatorsTokens
_(no internal calls)_


### public getDelegatorInfo
-> private _shareToToken


### public getParamValue
_(no internal calls)_


### public getQuorumTokens
_(no internal calls)_


### public getValidatorNum
_(no internal calls)_


### public getValidatorStatus
_(no internal calls)_


### public getValidatorTokens
_(no internal calls)_


### public hasMinRequiredTokens
-> private _shareToToken


### external initializeValidator
-> public delegate
  -> private _tokenToShare
  -> private _decentralizationCheck
    -> public getQuorumTokens


### public isBondedValidator
_(no internal calls)_


### public isPauser
_(no internal calls)_


### public isWhitelisted
_(no internal calls)_


### public numPausers
_(no internal calls)_


### public pause
_(no internal calls)_


### public removePauser
-> private _removePauser
  -> public isPauser


### public removePausers
-> private _removePauser
  -> public isPauser


### public removeWhitelistedAccount
-> public isWhitelisted


### public removeWhitelistedAccounts
-> public removeWhitelistedAccount
  -> public isWhitelisted


### public renouncePauser
-> private _removePauser
  -> public isPauser


### external setGovContract
_(no internal calls)_


### external setMaxSlashFactor
_(no internal calls)_


### external setParamValue
_(no internal calls)_


### external setRewardContract
_(no internal calls)_


### public setWhitelistEnabled
_(no internal calls)_


### external slash
-> public verifySignatures
  -> public getQuorumTokens
-> library PbStaking.decSlash
-> public hasMinRequiredTokens
  -> private _shareToToken
-> private _unbondValidator
  -> private _setUnbondingValidator


### external undelegateShares
-> private _shareToToken
-> private _undelegate
  -> public hasMinRequiredTokens
    -> private _shareToToken
  -> private _unbondValidator
    -> private _setUnbondingValidator
  -> private _tokenToShare


### external undelegateTokens
-> private _tokenToShare
-> private _undelegate
  -> public hasMinRequiredTokens
    -> private _shareToToken
  -> private _unbondValidator
    -> private _setUnbondingValidator
  -> private _tokenToShare


### public unpause
_(no internal calls)_


### external updateCommissionRate
_(no internal calls)_


### external updateMinSelfDelegation
_(no internal calls)_


### external updateValidatorSigner
_(no internal calls)_


### external validatorNotice
_(no internal calls)_


### public verifySignatures
-> public getQuorumTokens


### public verifySigs
-> public verifySignatures
  -> public getQuorumTokens


---

## StakingReward

_File: contracts/bvn/StakingReward.sol_

### public addPauser
-> private _addPauser
  -> public isPauser


### public addPausers
-> private _addPauser
  -> public isPauser


### external claimReward
-> library PbStaking.decStakingReward


### external contributeToRewardPool
_(no internal calls)_


### external drainToken
_(no internal calls)_


### public isPauser
_(no internal calls)_


### public numPausers
_(no internal calls)_


### public pause
_(no internal calls)_


### public removePauser
-> private _removePauser
  -> public isPauser


### public removePausers
-> private _removePauser
  -> public isPauser


### public renouncePauser
-> private _removePauser
  -> public isPauser


### public unpause
_(no internal calls)_


---

## System

_File: contracts/light-client-others/bsc-tendermint/System.sol_

### external init
_(no internal calls)_


### public owner
_(no internal calls)_


### external setRelayer
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## TendermintLightClient

_File: contracts/light-client-others/bsc-tendermint/TendermintLightClient.sol_

### external getAppHash
_(no internal calls)_


### external init
-> internal unmarshalTmHeader


### external isHeaderSynced
_(no internal calls)_


### external syncTendermintHeader
-> internal unmarshalTmHeader
-> private checkValidity


---

## TestSmtVerifier

_File: contracts/verifiers/zk-verifiers/TestSmtVerifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


---

## TierFactory

_File: contracts/apps/uniswap-v4/uniswap-v4-hook/TierHook.sol_

### public deploy
_(no internal calls)_


### public mineDeploy
-> public mineSalt
  -> internal _computeHookAddress
    -> internal _hashBytecode
  -> internal _isPrefix
-> public deploy


### public mineSalt
-> internal _computeHookAddress
  -> internal _hashBytecode
-> internal _isPrefix


### public owner
_(no internal calls)_


### public transferOwnership
-> private _setOwner


### public updateHookSumVolumeAddress
_(no internal calls)_


---

## TierHook

_File: contracts/apps/uniswap-v4/uniswap-v4-hook/TierHook.sol_

### external afterDonate
_(no internal calls)_


### external afterInitialize
_(no internal calls)_


### external afterModifyPosition
_(no internal calls)_


### external afterSwap
_(no internal calls)_


### external beforeDonate
_(no internal calls)_


### external beforeInitialize
_(no internal calls)_


### external beforeModifyPosition
_(no internal calls)_


### external beforeSwap
_(no internal calls)_


### external getFee
-> internal calcFee
  -> internal senderTier


### external getFeeBySwapper
-> internal calcFee
  -> internal senderTier


### external getHookFees
_(no internal calls)_


### external getHookWithdrawFee
_(no internal calls)_


### public getHooksCalls
_(no internal calls)_


### external lockAcquired
_(no internal calls)_


### external updateSumVolumeAddress
_(no internal calls)_


---

## TokenVault

_File: contracts/apps/message-bridge/apps/token-bridge/TokenVault.sol_

### external deposit
-> private _deposit


### public owner
_(no internal calls)_


### external setMinDeposit
_(no internal calls)_


### external setRemotePegBridge
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## TransactionProofVerifier

_File: contracts/verifiers/zk-verifiers/TransactionProofVerifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


### external verifyRaw
-> public verifyProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> internal verifyingKey
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> internal accumulate
    -> library Pairing.scalar_mul_raw
    -> library Pairing.plus_raw
  -> library Pairing.plus
  -> library Pairing.pairing
  -> library Pairing.negate


---

## TxVerifier

_File: contracts/verifiers/TxVerifier.sol_

### public decodeTx
-> internal recover


### public owner
_(no internal calls)_


### public transferOwnership
-> private _setOwner


### external updateBlockChunks
_(no internal calls)_


### external updateVerifierAddress
_(no internal calls)_


### public verifyTx
-> public decodeTx
  -> internal recover
-> private verifyRaw
-> internal getProofData
-> internal getFromAuxiBlkVerifyInfo
-> external_callback IBlockChunks.BlockHashWitness


### external verifyTxAndLog
-> public verifyTx
  -> public decodeTx
    -> internal recover
  -> private verifyRaw
  -> internal getProofData
  -> internal getFromAuxiBlkVerifyInfo
  -> external_callback IBlockChunks.BlockHashWitness


---

## UniswapAmount

_File: contracts/apps/demo-tx-uniswap-amount/UniswapAmount.sol_

### public owner
_(no internal calls)_


### external setTierNFTs
_(no internal calls)_


### external setTxVerifier
_(no internal calls)_


### external setUSDC
_(no internal calls)_


### external setUniversalRouter
_(no internal calls)_


### external setWETH
_(no internal calls)_


### external submitUniswapTxProof
-> public usdcSwapAmount
  -> library Path.decodeFirstPool
  -> private getAmountTier


### public transferOwnership
-> private _setOwner


### public usdcSwapAmount
-> library Path.decodeFirstPool
-> private getAmountTier


---

## UniswapSumVolume

_File: contracts/apps/uniswap-v4/uniswap-sum/UniswapSumVolume.sol_

### external getAttestedSwapSumVolume
_(no internal calls)_


### public owner
_(no internal calls)_


### external setBatchTierVkHashes
_(no internal calls)_


### external submitUniswapSumVolumeProof
-> private verifyRaw
-> internal getProofData
-> internal isIn


### public transferOwnership
-> private _setOwner


### external updateSmtContract
_(no internal calls)_


### external updateVerifierAddress
_(no internal calls)_


---

## UniswapSumVolumeVerifier

_File: contracts/verifiers/zk-verifiers/UniVolumeSumBatchProofVerifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> internal accumulate
  -> library Pairing.scalar_mul_raw
  -> library Pairing.plus_raw
-> library Pairing.plus
-> library Pairing.pairing
-> library Pairing.negate


### external verifyRaw
-> public verifyProof
  -> library Pairing.G1Point
  -> library Pairing.G2Point
  -> internal verifyingKey
    -> library Pairing.G1Point
    -> library Pairing.G2Point
  -> internal accumulate
    -> library Pairing.scalar_mul_raw
    -> library Pairing.plus_raw
  -> library Pairing.plus
  -> library Pairing.pairing
  -> library Pairing.negate


---

## UniswapVolume

_File: contracts/sdk/apps/examples/uniswap-volume/UniswapVolume.sol_

### public applyBrevisOpResult
-> private _getBrevisConfig
-> internal handleOpProofResult


### external applyBrevisOpResults
-> private _getBrevisConfig
-> internal handleOpProofResult


### external brevisBatchCallback
-> internal handleProofResult
  -> internal decodeOutput


### external brevisCallback
-> internal handleProofResult
  -> internal decodeOutput


### public owner
_(no internal calls)_


### external setVkHash
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## UpgradeableOwnerProxy

_File: contracts/safeguard/governed-owner/proxies/UpgradeableOwnerProxy.sol_

### public initGov
_(no internal calls)_


### external proposeChangeProxyAdmin
_(no internal calls)_


### external proposeUpgrade
_(no internal calls)_


### external proposeUpgradeAndCall
_(no internal calls)_


### external proposeUpgradeTo
_(no internal calls)_


### external proposeUpgradeToAndCall
_(no internal calls)_


---

## VerifierGasReport

_File: contracts/test-helper/VerifierGasReport.sol_

### external ethChunkOf128VerifyProof
-> private verifyProof


### external ethChunkOf4VerifyProof
-> private verifyProof


### external ethStorageVerifyProof
-> private verifyProof


### external receiptVerifyProof
-> private verifyProof


### external setVerifier
_(no internal calls)_


### external transaction13VerifyProof
-> private verifyProof


### external transaction37VerifyProof
-> private verifyProof


### external transactionVerifyProof
-> private verifyProof


### external verifyRaw
_(no internal calls)_


### external verifyReceipt
_(no internal calls)_


### external verifySlotValue
_(no internal calls)_


### external verifyTx
_(no internal calls)_


---

## VerifyNumberEvent

_File: contracts/apps/demo-receipt-tx/VerifyNumberEvent.sol_

### public owner
_(no internal calls)_


### external setReceiptVerifier
_(no internal calls)_


### external setSrcContract
_(no internal calls)_


### external submitNumberReceiptProof
_(no internal calls)_


### public transferOwnership
-> private _setOwner


---

## VerifyNumberTx

_File: contracts/apps/demo-receipt-tx/VerifyNumberTx.sol_

### public owner
_(no internal calls)_


### external setReceiptVerifier
_(no internal calls)_


### external setSrcContract
_(no internal calls)_


### external submitNumberTxProof
-> private decodeCalldata


### public transferOwnership
-> private _setOwner


---

## Viewer

_File: contracts/bvn/Viewer.sol_

### public getBondedValidatorInfos
-> public getValidatorInfo


### public getDelegatorInfos
_(no internal calls)_


### public getDelegatorTokens
-> public getDelegatorInfos


### public getMinValidatorTokens
_(no internal calls)_


### public getValidatorInfo
_(no internal calls)_


### public getValidatorInfos
-> public getValidatorInfo


### public shouldBondValidator
-> public getMinValidatorTokens


---

## Whitelist

_File: contracts/safeguard/Whitelist.sol_

### public addWhitelistedAccount
-> public isWhitelisted


### public addWhitelistedAccounts
-> public addWhitelistedAccount
  -> public isWhitelisted


### public isWhitelisted
_(no internal calls)_


### public owner
_(no internal calls)_


### public removeWhitelistedAccount
-> public isWhitelisted


### public removeWhitelistedAccounts
-> public removeWhitelistedAccount
  -> public isWhitelisted


### public setWhitelistEnabled
_(no internal calls)_


### public transferOwnership
-> private _setOwner

