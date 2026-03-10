# Callpaths — Telcoin

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ConsensusRegistry

_File: src/consensus/ConsensusRegistry.sol_

### external activate
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> private _checkValidatorStatus
-> internal _beginActivation


### external allocateIssuance
_(no internal calls)_


### public applyIncentives
-> public isRetired
  -> internal _exists
  -> internal _getTokenId
-> public getCurrentEpochInfo
  -> internal _getRecentEpochInfo


### external applySlashes
-> public isRetired
  -> internal _exists
  -> internal _getTokenId
-> internal _consensusBurn
  -> internal _getValidators
    -> internal _getAddress
    -> internal _eligibleForCommitteeNextEpoch
  -> internal _eligibleForCommitteeNextEpoch
  -> internal _ejectFromCommittees
    -> internal _getRecentEpochInfo
    -> internal _eject
    -> internal _checkCommitteeSize
    -> internal _getFutureEpochInfo
  -> public getBalanceBreakdown
    -> internal _getRewards
  -> internal _exit
  -> internal _retire
  -> internal _getRecipient
  -> internal _unstake
    -> internal _getTokenId
    -> public getBalanceBreakdown
      -> internal _getRewards


### public approve
_(no internal calls)_


### external beginExit
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> internal _getValidators
  -> internal _getAddress
  -> internal _eligibleForCommitteeNextEpoch
-> internal _checkCommitteeSize
-> private _checkValidatorStatus
-> internal _beginExit


### external burn
-> public isRetired
  -> internal _exists
  -> internal _getTokenId
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> internal _retire
-> internal _getTokenId
-> internal _consensusBurn
  -> internal _getValidators
    -> internal _getAddress
    -> internal _eligibleForCommitteeNextEpoch
  -> internal _eligibleForCommitteeNextEpoch
  -> internal _ejectFromCommittees
    -> internal _getRecentEpochInfo
    -> internal _eject
    -> internal _checkCommitteeSize
    -> internal _getFutureEpochInfo
  -> public getBalanceBreakdown
    -> internal _getRewards
  -> internal _exit
  -> internal _retire
  -> internal _getRecipient
  -> internal _unstake
    -> internal _getTokenId
    -> public getBalanceBreakdown
      -> internal _getRewards


### external claimStakeRewards
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> internal _getRecipient
-> internal _claimStakeRewards
  -> internal _checkRewards
    -> internal _getRewards


### external concludeEpoch
-> internal _enforceSorting
-> internal _updateEpochInfo
  -> public getCurrentStakeConfig
-> internal _updateValidatorQueue
  -> internal _getValidators
    -> internal _getAddress
    -> internal _eligibleForCommitteeNextEpoch
  -> internal _activate
  -> internal _isCommitteeMember
  -> internal _exit
-> internal _getValidators
  -> internal _getAddress
  -> internal _eligibleForCommitteeNextEpoch
-> internal _checkCommitteeSize


### external delegateStake
-> internal _verifyProofOfPossession
  -> library BlsG1.InvalidBLSPubkey
  -> public proofOfPossessionMessage
    -> library BlsG1.encodeG2PointForEIP2537
    -> library BlsG1.validatePointG2
    -> library BlsG1.InvalidBLSPubkey
  -> library BlsG1.encodeG2PointForEIP2537
  -> library BlsG1.encodeG1PointForEIP2537
  -> library BlsG1.verifyProofOfPossessionG1
  -> private _spendBLSPubkey
-> public getCurrentEpochInfo
  -> internal _getRecentEpochInfo
-> internal _checkStakeValue
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> private _checkValidatorStatus
-> internal _recordStaked


### external delegationDigest
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> public getCurrentEpochInfo
  -> internal _getRecentEpochInfo


### public getBalanceBreakdown
-> internal _getRewards


### public getCommitteeValidators
-> public getEpochInfo
  -> internal _getFutureEpochInfo
  -> internal _getRecentEpochInfo
-> public getValidator
  -> internal _checkConsensusNFTOwner
    -> internal _getTokenId
    -> internal _exists


### public getCurrentEpoch
_(no internal calls)_


### public getCurrentEpochInfo
-> internal _getRecentEpochInfo


### public getCurrentStakeConfig
_(no internal calls)_


### public getCurrentStakeVersion
-> public getCurrentEpochInfo
  -> internal _getRecentEpochInfo


### public getEpochInfo
-> internal _getFutureEpochInfo
-> internal _getRecentEpochInfo


### external getNextCommitteeSize
_(no internal calls)_


### public getRewards
-> internal _getRewards


### public getValidator
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists


### public getValidators
-> internal _getValidators
  -> internal _getAddress
  -> internal _eligibleForCommitteeNextEpoch


### public isRetired
-> internal _exists
-> internal _getTokenId


### public isValidator
-> public isRetired
  -> internal _exists
  -> internal _getTokenId


### external mint
-> public isRetired
  -> internal _exists
  -> internal _getTokenId
-> internal _getTokenId


### external pause
_(no internal calls)_


### public proofOfPossessionMessage
-> library BlsG1.encodeG2PointForEIP2537
-> library BlsG1.validatePointG2
-> library BlsG1.InvalidBLSPubkey


### public setApprovalForAll
_(no internal calls)_


### external setNextCommitteeSize
-> internal _getValidators
  -> internal _getAddress
  -> internal _eligibleForCommitteeNextEpoch


### external stake
-> internal _verifyProofOfPossession
  -> library BlsG1.InvalidBLSPubkey
  -> public proofOfPossessionMessage
    -> library BlsG1.encodeG2PointForEIP2537
    -> library BlsG1.validatePointG2
    -> library BlsG1.InvalidBLSPubkey
  -> library BlsG1.encodeG2PointForEIP2537
  -> library BlsG1.encodeG1PointForEIP2537
  -> library BlsG1.verifyProofOfPossessionG1
  -> private _spendBLSPubkey
-> public getCurrentEpochInfo
  -> internal _getRecentEpochInfo
-> internal _checkStakeValue
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> private _checkValidatorStatus
-> internal _recordStaked


### public stakeConfig
_(no internal calls)_


### public tokenURI
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### external unpause
_(no internal calls)_


### external unstake
-> internal _checkConsensusNFTOwner
  -> internal _getTokenId
  -> internal _exists
-> internal _getRecipient
-> internal _eligibleForUnstake
-> internal _retire
-> internal _unstake
  -> internal _getTokenId
  -> public getBalanceBreakdown
    -> internal _getRewards


### external upgradeStakeVersion
_(no internal calls)_


---

## Create3Utils

_File: deployments/utils/Create3Utils.sol_

### public create3Address
_(no internal calls)_


### public create3Deploy
_(no internal calls)_


---

## GenesisPrecompiler

_File: deployments/genesis/GenesisPrecompiler.sol_

### public copyContractState
_(no internal calls)_


### public saveWrittenSlots
_(no internal calls)_


### public yamlAppendGenesisAccount
_(no internal calls)_


---

## GitAttestationRegistry

_File: src/CI/GitAttestationRegistry.sol_

### external attestGitCommitHash
_(no internal calls)_


### external gitCommitHashAttested
_(no internal calls)_


### external setBufferSize
_(no internal calls)_


---

## ITSConfig

_File: deployments/utils/ITSConfig.sol_

### public eth_registerCustomTokenAndLinkToken
_(no internal calls)_


### public instantiateAxelarAmplifierGateway
_(no internal calls)_


### public instantiateAxelarAmplifierGatewayImpl
_(no internal calls)_


### public instantiateAxelarGasService
_(no internal calls)_


### public instantiateAxelarGasServiceImpl
_(no internal calls)_


### public instantiateGatewayCaller
_(no internal calls)_


### public instantiateITF
_(no internal calls)_


### public instantiateITFImpl
_(no internal calls)_


### public instantiateITS
_(no internal calls)_


### public instantiateITSImpl
_(no internal calls)_


### public instantiateInterchainTEL
_(no internal calls)_


### public instantiateInterchainTELTokenManager
_(no internal calls)_


### public instantiateInterchainTokenDeployer
_(no internal calls)_


### public instantiateInterchainTokenImpl
_(no internal calls)_


### public instantiateTokenHandler
_(no internal calls)_


### public instantiateTokenManagerDeployer
_(no internal calls)_


### public instantiateTokenManagerImpl
_(no internal calls)_


### public instantiateWTEL
_(no internal calls)_


---

## ITSUtils

_File: deployments/utils/ITSUtils.sol_

### public create3Address
_(no internal calls)_


### public create3Deploy
_(no internal calls)_


### public eth_registerCustomTokenAndLinkToken
_(no internal calls)_


### public instantiateAxelarAmplifierGateway
-> public create3Deploy


### public instantiateAxelarAmplifierGatewayImpl
-> public create3Deploy


### public instantiateAxelarGasService
-> public create3Deploy


### public instantiateAxelarGasServiceImpl
-> public create3Deploy


### public instantiateGatewayCaller
-> public create3Deploy


### public instantiateITF
-> public create3Deploy


### public instantiateITFImpl
-> public create3Deploy


### public instantiateITS
-> public create3Deploy


### public instantiateITSImpl
-> public create3Deploy


### public instantiateInterchainTEL
-> public create3Deploy


### public instantiateInterchainTELTokenManager
-> public create3Deploy


### public instantiateInterchainTokenDeployer
-> public create3Deploy


### public instantiateInterchainTokenImpl
-> public create3Deploy


### public instantiateTokenHandler
-> public create3Deploy


### public instantiateTokenManagerDeployer
-> public create3Deploy


### public instantiateTokenManagerImpl
-> public create3Deploy


### public instantiateWTEL
-> public create3Deploy


---

## InterchainTEL

_File: src/InterchainTEL.sol_

### external burn
_(no internal calls)_


### external doubleWrap
_(no internal calls)_


### public interchainTokenId
-> public linkedTokenDeploySalt


### public interchainTokenService
_(no internal calls)_


### external isMinter
_(no internal calls)_


### public linkedTokenDeploySalt
_(no internal calls)_


### external mint
_(no internal calls)_


### public pause
_(no internal calls)_


### external permitWrap
_(no internal calls)_


### public tokenManagerAddress
-> public interchainTokenService
-> public tokenManagerCreate3Salt
  -> public interchainTokenId
    -> public linkedTokenDeploySalt


### public tokenManagerCreate3Salt
-> public interchainTokenId
  -> public linkedTokenDeploySalt


### public unpause
_(no internal calls)_


### external unwrap
_(no internal calls)_


### external unwrapTo
_(no internal calls)_


### external wrap
_(no internal calls)_


---

## Issuance

_File: src/consensus/Issuance.sol_

### external distributeStakeReward
_(no internal calls)_


---

## StablecoinManager

_File: src/faucet/StablecoinManager.sol_

### public UpdateXYZ
-> public isEnabledXYZ
  -> internal _stablecoinManagerStorage
-> internal _recordXYZ
  -> internal _addEnabledXYZ
    -> internal _stablecoinManagerStorage
  -> internal _removeEnabledXYZ
    -> internal _stablecoinManagerStorage


### public drip
_(no internal calls)_


### public getDripAmount
-> internal _faucetStorage


### public getEnabledXYZs
-> internal _stablecoinManagerStorage
-> internal _findNativeTokenIndex


### public getEnabledXYZsWithMetadata
-> public getEnabledXYZs
  -> internal _stablecoinManagerStorage
  -> internal _findNativeTokenIndex


### public getLastFulfilledDripTimestamp
-> internal _faucetStorage


### public getNativeDripAmount
-> internal _faucetStorage


### public initialize
-> internal __Faucet_init
  -> internal _setDripAmount
    -> internal _faucetStorage
  -> internal _setNativeDripAmount
    -> internal _faucetStorage
-> internal _setLowBalanceThreshold
  -> internal _faucetStorage
-> public UpdateXYZ
  -> public isEnabledXYZ
    -> internal _stablecoinManagerStorage
  -> internal _recordXYZ
    -> internal _addEnabledXYZ
      -> internal _stablecoinManagerStorage
    -> internal _removeEnabledXYZ
      -> internal _stablecoinManagerStorage


### public isEnabledXYZ
-> internal _stablecoinManagerStorage


### public rescueCrypto
_(no internal calls)_


### external setDripAmount
-> internal _setDripAmount
  -> internal _faucetStorage


### external setLowBalanceThreshold
-> internal _setLowBalanceThreshold
  -> internal _faucetStorage


### external setNativeDripAmount
-> internal _setNativeDripAmount
  -> internal _faucetStorage


---

## StakeManager

_File: src/consensus/StakeManager.sol_

### public approve
_(no internal calls)_


### public getCurrentStakeConfig
_(no internal calls)_


### public setApprovalForAll
_(no internal calls)_


### public stakeConfig
_(no internal calls)_


### public tokenURI
_(no internal calls)_


### public transferFrom
_(no internal calls)_


---

## TNFaucet

_File: src/faucet/TNFaucet.sol_

### public drip
-> internal _setLastFulfilledDripTimestamp
  -> internal _faucetStorage


### public getDripAmount
-> internal _faucetStorage


### public getLastFulfilledDripTimestamp
-> internal _faucetStorage


### public getNativeDripAmount
-> internal _faucetStorage


---

## TNGenesis

_File: deployments/genesis/TNGenesis.sol_

### public copyContractState
_(no internal calls)_


### public instantiateAxelarAmplifierGateway
-> public saveWrittenSlots
-> public copyContractState


### public instantiateAxelarAmplifierGatewayImpl
-> public copyContractState


### public instantiateAxelarGasService
-> public saveWrittenSlots
-> public copyContractState


### public instantiateAxelarGasServiceImpl
-> public copyContractState


### public instantiateGatewayCaller
-> public copyContractState


### public instantiateGovernanceSafe
-> public saveWrittenSlots
-> public copyContractState


### public instantiateITF
-> public saveWrittenSlots
-> public copyContractState


### public instantiateITFImpl
-> public copyContractState


### public instantiateITS
-> public saveWrittenSlots
-> public copyContractState


### public instantiateITSImpl
-> public copyContractState


### public instantiateInterchainTEL
-> public saveWrittenSlots
-> public copyContractState


### public instantiateInterchainTELTokenManager
-> public saveWrittenSlots
-> public copyContractState


### public instantiateInterchainTokenDeployer
-> public copyContractState


### public instantiateInterchainTokenImpl
-> public copyContractState


### public instantiateSafeImpl
-> public saveWrittenSlots
-> public copyContractState


### public instantiateSafeProxyFactory
-> public copyContractState


### public instantiateTokenHandler
-> public copyContractState


### public instantiateTokenManagerDeployer
-> public copyContractState


### public instantiateTokenManagerImpl
-> public copyContractState


### public instantiateWTEL
-> public copyContractState


### public saveWrittenSlots
_(no internal calls)_


### public yamlAppendGenesisAccount
_(no internal calls)_


---

## WTEL

_File: src/WTEL.sol_

### public name
_(no internal calls)_


### public symbol
_(no internal calls)_

