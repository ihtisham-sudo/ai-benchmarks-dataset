# Callpaths — Clave

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AccountFactory

_File: AccountFactory.sol_

### external changeDeployer
_(no internal calls)_


### external changeImplementation
_(no internal calls)_


### external changeRegistry
_(no internal calls)_


### external claveAccountCreated
-> library Errors.NOT_FROM_DEPLOYER


### external deployAccount
-> library Errors.NOT_FROM_DEPLOYER
-> library Errors.DEPLOYMENT_FAILED
-> library Errors.INITIALIZATION_FAILED


### external getAddressForSalt
_(no internal calls)_


### external getAddressForSaltAndImplementation
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


---

## BaseRecovery

_File: modules/recovery/base/BaseRecovery.sol_

### public eip712Domain
-> internal _EIP712Name
-> internal _EIP712Version


### external executeRecovery
-> library Errors.RECOVERY_NOT_STARTED
-> library Errors.RECOVERY_TIMELOCK


### external getEip712Hash
-> internal _hashTypedDataV4
  -> library MessageHashUtils.toTypedDataHash
  -> internal _domainSeparatorV4
    -> private _buildDomainSeparator
-> internal _recoveryDataHash


### public isRecovering
_(no internal calls)_


### external recoveryDataTypeHash
_(no internal calls)_


### external stopRecovery
-> public isRecovering
-> library Errors.RECOVERY_NOT_STARTED
-> internal _stopRecovery
  -> public isRecovering


### external supportsInterface
_(no internal calls)_


---

## BatchCaller

_File: batch/BatchCaller.sol_

### external batchCall
-> library Errors.ONLY_DELEGATECALL
-> library Errors.CALL_FAILED


---

## ClaveEarnRouter

_File: earn/ClaveEarnRouter.sol_

### external stakePositions
_(no internal calls)_


---

## ClaveImplementation

_File: ClaveImplementation.sol_

### external addHook
-> internal _addHook
  -> library Errors.EMPTY_HOOK_ADDRESS
  -> internal _supportsHook
  -> library Errors.HOOK_ERC165_FAIL
  -> private _validationHooksLinkedList
    -> library ClaveStorage.layout
  -> private _executionHooksLinkedList
    -> library ClaveStorage.layout


### external addModule
-> internal _addModule
  -> library Errors.EMPTY_MODULE_ADDRESS
  -> internal _supportsModule
  -> library Errors.MODULE_ERC165_FAIL
  -> private _modulesLinkedList
    -> library ClaveStorage.layout


### external executeFromModule
-> library Errors.RECUSIVE_MODULE_CALL


### external executeTransaction
-> internal _executeTransaction
  -> internal _safeCastToAddress
  -> internal _executeCall


### external executeTransactionFromOutside
-> library Errors.UNAUTHORIZED_OUTSIDE_TRANSACTION
-> library SignatureDecoder.decodeSignatureOnlyHookData
-> internal runValidationHooks
  -> private _validationHooksLinkedList
    -> library ClaveStorage.layout
  -> private _call
-> library Errors.VALIDATION_HOOK_FAILED
-> internal _executeTransaction
  -> internal _safeCastToAddress
  -> internal _executeCall


### external getHookData
-> private _hookDataStore
  -> library ClaveStorage.layout


### external implementation
_(no internal calls)_


### external initialize
-> internal _addModule
  -> library Errors.EMPTY_MODULE_ADDRESS
  -> internal _supportsModule
  -> library Errors.MODULE_ERC165_FAIL
  -> private _modulesLinkedList
    -> library ClaveStorage.layout
-> internal _executeCall


### external isHook
-> internal _isHook
  -> private _validationHooksLinkedList
    -> library ClaveStorage.layout
  -> private _executionHooksLinkedList
    -> library ClaveStorage.layout


### external isModule
-> internal _isModule
  -> private _modulesLinkedList
    -> library ClaveStorage.layout


### external listHooks
-> private _validationHooksLinkedList
  -> library ClaveStorage.layout
-> private _executionHooksLinkedList
  -> library ClaveStorage.layout


### external listModules
-> private _modulesLinkedList
  -> library ClaveStorage.layout


### external onERC1155BatchReceived
_(no internal calls)_


### external onERC1155Received
_(no internal calls)_


### external onERC721Received
_(no internal calls)_


### external payForTransaction
-> library Errors.FEE_PAYMENT_FAILED


### external prepareForPaymaster
_(no internal calls)_


### external removeHook
-> internal _removeHook
  -> private _validationHooksLinkedList
    -> library ClaveStorage.layout
  -> private _executionHooksLinkedList
    -> library ClaveStorage.layout


### external removeModule
-> internal _removeModule
  -> private _modulesLinkedList
    -> library ClaveStorage.layout


### external setHookData
-> library Errors.INVALID_KEY
-> private _hookDataStore
  -> library ClaveStorage.layout


### public supportsInterface
_(no internal calls)_


### external upgradeTo
-> library Errors.SAME_IMPLEMENTATION


### external validateTransaction
-> internal _incrementNonce
-> library Errors.INSUFFICIENT_FUNDS
-> internal _validateTransaction
  -> internal runValidationHooks
    -> private _validationHooksLinkedList
      -> library ClaveStorage.layout
    -> private _call


---

## ClaveNameService

_File: cns/ClaveNameService.sol_

### public burn
_(no internal calls)_


### external expireName
-> private toLower


### external flipRenewals
_(no internal calls)_


### public registerName
-> private toLower
-> private isAlphanumeric
-> internal _safeMint


### external registerNameMultiple
-> public registerName
  -> private toLower
  -> private isAlphanumeric
  -> internal _safeMint


### external renewName
-> private toLower


### external resolve
-> private toLower


### external setBaseTokenURI
_(no internal calls)_


### external setExpirationTime
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public tokenURI
_(no internal calls)_


### external totalSupply
_(no internal calls)_


---

## ClaveRegistry

_File: ClaveRegistry.sol_

### public owner
_(no internal calls)_


### external register
-> public owner
-> library Errors.NOT_FROM_FACTORY


### external registerMultiple
-> public owner
-> library Errors.NOT_FROM_FACTORY


### public renounceOwnership
-> internal _transferOwnership


### external setFactory
_(no internal calls)_


### public transferOwnership
-> internal _transferOwnership


### external unregister
-> public owner
-> library Errors.NOT_FROM_FACTORY


### external unregisterMultiple
-> public owner
-> library Errors.NOT_FROM_FACTORY


### external unsetFactory
_(no internal calls)_


---

## CloudRecoveryModule

_File: modules/recovery/CloudRecoveryModule.sol_

### external disable
-> public isInited
-> library Errors.RECOVERY_NOT_INITED
-> library Errors.MODULE_NOT_REMOVED_CORRECTLY
-> internal _stopRecovery
  -> public isRecovering


### external executeRecovery
-> library Errors.RECOVERY_NOT_STARTED
-> library Errors.RECOVERY_TIMELOCK


### external getEip712Hash
-> internal _recoveryDataHash


### external getGuardian
_(no internal calls)_


### external init
-> public isInited
-> library Errors.ALREADY_INITED
-> library Errors.MODULE_NOT_ADDED_CORRECTLY
-> internal _updateGuardian
  -> library Errors.ZERO_ADDRESS_GUARDIAN


### public isInited
_(no internal calls)_


### public isRecovering
_(no internal calls)_


### external recoveryDataTypeHash
_(no internal calls)_


### external startRecovery
-> library Errors.INVALID_RECOVERY_NONCE
-> public isRecovering
-> library Errors.RECOVERY_IN_PROGRESS
-> public isInited
-> library Errors.RECOVERY_NOT_INITED
-> internal _recoveryDataHash
-> library Errors.INVALID_GUARDIAN_SIGNATURE


### external stopRecovery
-> public isRecovering
-> library Errors.RECOVERY_NOT_STARTED
-> internal _stopRecovery
  -> public isRecovering


### external supportsInterface
_(no internal calls)_


### external updateGuardian
-> public isInited
-> library Errors.RECOVERY_NOT_INITED
-> public isRecovering
-> library Errors.RECOVERY_IN_PROGRESS
-> internal _updateGuardian
  -> library Errors.ZERO_ADDRESS_GUARDIAN


---

## DKIMRegistry

_File: EmailRecoveryManager.sol_

### public isDKIMPublicKeyHashValid
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public revokeDKIMPublicKeyHash
_(no internal calls)_


### public setDKIMPublicKeyHash
_(no internal calls)_


### public setDKIMPublicKeyHashes
-> public setDKIMPublicKeyHash


### public transferOwnership
-> internal _transferOwnership


---

## EIP712

_File: helpers/EIP712.sol_

### public eip712Domain
-> internal _EIP712Name
-> internal _EIP712Version


---

## EOAValidator

_File: validators/EOAValidator.sol_

### external supportsInterface
_(no internal calls)_


### external validateSignature
_(no internal calls)_


---

## ERC20

_File: EmailRecoveryManager.sol_

### public allowance
_(no internal calls)_


### public approve
-> internal _msgSender
-> internal _approve


### public balanceOf
_(no internal calls)_


### public decimals
_(no internal calls)_


### public name
_(no internal calls)_


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> internal _msgSender
-> internal _transfer
  -> internal _update


### public transferFrom
-> internal _msgSender
-> internal _spendAllowance
  -> public allowance
  -> internal _approve
-> internal _transfer
  -> internal _update


---

## ERC20Paymaster

_File: paymasters/ERC20Paymaster.sol_

### external allowToken
-> library Errors.INVALID_TOKEN
-> library Errors.INVALID_MARKUP


### external callOracle
_(no internal calls)_


### public owner
_(no internal calls)_


### external postTransaction
_(no internal calls)_


### external removeToken
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


### external validateAndPayForPaymasterTransaction
-> library Errors.SHORT_PAYMASTER_INPUT
-> library Errors.UNSUPPORTED_FLOW
-> library Errors.UNSUPPORTED_TOKEN
-> private getPairPrice
-> library Errors.LESS_ALLOWANCE_FOR_PAYMASTER
-> library Errors.FAILED_FEE_TRANSFER


### external withdraw
-> library Errors.UNAUTHORIZED_WITHDRAW


### external withdrawToken
_(no internal calls)_


---

## EmailAccountRecovery

_File: EmailRecoveryManager.sol_

### public computeAcceptanceTemplateId
_(no internal calls)_


### public computeEmailAuthAddress
-> public emailAuthImplementation
-> library Create2.computeAddress


### public computeRecoveryTemplateId
_(no internal calls)_


### public dkim
_(no internal calls)_


### public emailAuthImplementation
_(no internal calls)_


### external handleAcceptance
-> public computeEmailAuthAddress
  -> public emailAuthImplementation
  -> library Create2.computeAddress
-> public computeAcceptanceTemplateId
-> public emailAuthImplementation
-> public dkim
-> public verifier
-> public computeRecoveryTemplateId


### external handleRecovery
-> public computeEmailAuthAddress
  -> public emailAuthImplementation
  -> library Create2.computeAddress


### public verifier
_(no internal calls)_


---

## EmailAuth

_File: EmailRecoveryManager.sol_

### public authEmail
-> library SubjectUtils.computeExpectedSubject
-> private removePrefix
-> library Strings.equal


### public deleteSubjectTemplate
_(no internal calls)_


### public dkimRegistryAddr
_(no internal calls)_


### public getSubjectTemplate
_(no internal calls)_


### public initDKIMRegistry
_(no internal calls)_


### public initVerifier
_(no internal calls)_


### public initialize
-> internal __Ownable_init
  -> internal __Ownable_init_unchained
    -> internal _transferOwnership
      -> private _getOwnableStorage


### public insertSubjectTemplate
_(no internal calls)_


### public owner
-> private _getOwnableStorage


### external proxiableUUID
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### public setTimestampCheckEnabled
_(no internal calls)_


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### public updateDKIMRegistry
_(no internal calls)_


### public updateSubjectTemplate
_(no internal calls)_


### public updateVerifier
_(no internal calls)_


### public upgradeToAndCall
-> internal _authorizeUpgrade
-> private _upgradeToAndCallUUPS
  -> library ERC1967Utils.upgradeToAndCall
  -> library ERC1967Utils.ERC1967InvalidImplementation


### public verifierAddr
_(no internal calls)_


---

## EmailRecoveryManager

_File: EmailRecoveryManager.sol_

### public acceptanceSubjectTemplates
_(no internal calls)_


### public addGuardian
-> internal _addGuardian


### external cancelRecovery
_(no internal calls)_


### external changeThreshold
_(no internal calls)_


### external completeRecovery
_(no internal calls)_


### public computeAcceptanceTemplateId
_(no internal calls)_


### public computeEmailAuthAddress
-> public emailAuthImplementation
-> library Create2.computeAddress


### public computeRecoveryTemplateId
_(no internal calls)_


### public dkim
_(no internal calls)_


### public emailAuthImplementation
_(no internal calls)_


### public extractRecoveredAccountFromAcceptanceSubject
_(no internal calls)_


### public extractRecoveredAccountFromRecoverySubject
_(no internal calls)_


### public getGuardian
_(no internal calls)_


### public getGuardianConfig
_(no internal calls)_


### external getRecoveryConfig
_(no internal calls)_


### external getRecoveryRequest
_(no internal calls)_


### external handleAcceptance
-> public extractRecoveredAccountFromAcceptanceSubject
-> public computeEmailAuthAddress
  -> public emailAuthImplementation
  -> library Create2.computeAddress
-> public computeAcceptanceTemplateId
-> public emailAuthImplementation
-> public dkim
-> public verifier
-> public acceptanceSubjectTemplates
-> public recoverySubjectTemplates
-> public computeRecoveryTemplateId
-> internal acceptGuardian
  -> public getGuardian
  -> internal updateGuardianStatus


### external handleRecovery
-> public extractRecoveredAccountFromRecoverySubject
-> public computeEmailAuthAddress
  -> public emailAuthImplementation
  -> library Create2.computeAddress
-> internal processRecovery
  -> public getGuardian


### public recoverySubjectTemplates
_(no internal calls)_


### external removeGuardian
_(no internal calls)_


### public updateRecoveryConfig
_(no internal calls)_


### public verifier
_(no internal calls)_


---

## EmailRecoveryModule

_File: modules/recovery/EmailRecoveryModule.sol_

### public acceptanceSubjectTemplates
_(no internal calls)_


### external canStartRecoveryRequest
_(no internal calls)_


### external cancelRecovery
_(no internal calls)_


### external completeRecovery
-> internal recover


### external disable
-> internal deInitRecoveryModule


### public extractRecoveredAccountFromAcceptanceSubject
_(no internal calls)_


### public extractRecoveredAccountFromRecoverySubject
_(no internal calls)_


### external getRecoveryConfig
_(no internal calls)_


### external getRecoveryRequest
_(no internal calls)_


### external init
-> public isInited
-> library Errors.ALREADY_INITED
-> library Errors.MODULE_NOT_ADDED_CORRECTLY
-> internal configureRecovery
  -> public updateRecoveryConfig


### public isInited
_(no internal calls)_


### public recoverySubjectTemplates
_(no internal calls)_


### external supportsInterface
_(no internal calls)_


### public updateRecoveryConfig
_(no internal calls)_


---

## EmailRecoverySubjectHandler

_File: modules/recovery/EmailRecoverySubjectHandler.sol_

### public acceptanceSubjectTemplates
_(no internal calls)_


### public extractRecoveredAccountFromAcceptanceSubject
_(no internal calls)_


### public extractRecoveredAccountFromRecoverySubject
_(no internal calls)_


### public recoverySubjectTemplates
_(no internal calls)_


### external validateAcceptanceSubject
_(no internal calls)_


### public validateRecoverySubject
-> library StringUtils.hexToBytes32


---

## GaslessPaymaster

_File: paymasters/GaslessPaymaster.sol_

### external addLimitlessAddresses
_(no internal calls)_


### external changeClaveRegistry
_(no internal calls)_


### external changeClaveRegistry2
_(no internal calls)_


### external getRemainingUserLimit
_(no internal calls)_


### public owner
_(no internal calls)_


### external postTransaction
_(no internal calls)_


### external removeLimitlessAddresses
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


### external updateMaxSponsoredEth
_(no internal calls)_


### external updateUserLimit
_(no internal calls)_


### external validateAndPayForPaymasterTransaction
-> library Errors.SHORT_PAYMASTER_INPUT
-> library Errors.UNSUPPORTED_FLOW
-> library Errors.USER_LIMIT_REACHED
-> library Errors.NOT_CLAVE_ACCOUNT
-> library Errors.EXCEEDS_MAX_SPONSORED_ETH
-> library Errors.FAILED_FEE_TRANSFER


### external withdraw
-> library Errors.UNAUTHORIZED_WITHDRAW


---

## Groth16Verifier

_File: EmailRecoveryManager.sol_

### public checkField
_(no internal calls)_


### public checkPairing
-> public g1_mulAccC


### public g1_mulAccC
_(no internal calls)_


### public verifyProof
-> public checkField
-> public g1_mulAccC
-> public checkPairing
  -> public g1_mulAccC


---

## GuardianManager

_File: EmailRecoveryManager.sol_

### public addGuardian
-> internal _addGuardian


### external changeThreshold
_(no internal calls)_


### public getGuardian
_(no internal calls)_


### public getGuardianConfig
_(no internal calls)_


### external removeGuardian
_(no internal calls)_


---

## HookManager

_File: managers/HookManager.sol_

### external addHook
-> internal _addHook
  -> library Errors.EMPTY_HOOK_ADDRESS
  -> internal _supportsHook
  -> library Errors.HOOK_ERC165_FAIL
  -> private _validationHooksLinkedList
    -> library ClaveStorage.layout
  -> private _executionHooksLinkedList
    -> library ClaveStorage.layout


### external getHookData
-> private _hookDataStore
  -> library ClaveStorage.layout


### external isHook
-> internal _isHook
  -> private _validationHooksLinkedList
    -> library ClaveStorage.layout
  -> private _executionHooksLinkedList
    -> library ClaveStorage.layout


### external listHooks
-> private _validationHooksLinkedList
  -> library ClaveStorage.layout
-> private _executionHooksLinkedList
  -> library ClaveStorage.layout


### external removeHook
-> internal _removeHook
  -> private _validationHooksLinkedList
    -> library ClaveStorage.layout
  -> private _executionHooksLinkedList
    -> library ClaveStorage.layout


### external setHookData
-> library Errors.INVALID_KEY
-> private _hookDataStore
  -> library ClaveStorage.layout


---

## KoiEarnRouter

_File: earn/KoiEarnRouter.sol_

### public claimFeesView
_(no internal calls)_


### external deposit
-> private desiredAmounts


### external stakePositions
-> public claimFeesView


### external withdraw
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## ModuleManager

_File: managers/ModuleManager.sol_

### external addModule
-> internal _addModule
  -> library Errors.EMPTY_MODULE_ADDRESS
  -> internal _supportsModule
  -> library Errors.MODULE_ERC165_FAIL
  -> private _modulesLinkedList
    -> library ClaveStorage.layout


### external executeFromModule
-> library Errors.RECUSIVE_MODULE_CALL


### external isModule
-> internal _isModule
  -> private _modulesLinkedList
    -> library ClaveStorage.layout


### external listModules
-> private _modulesLinkedList
  -> library ClaveStorage.layout


### external removeModule
-> internal _removeModule
  -> private _modulesLinkedList
    -> library ClaveStorage.layout


---

## Ownable

_File: EmailRecoveryManager.sol_

### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public transferOwnership
-> internal _transferOwnership


---

## OwnableUpgradeable

_File: EmailRecoveryManager.sol_

### public owner
-> private _getOwnableStorage


### public renounceOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


### public transferOwnership
-> internal _transferOwnership
  -> private _getOwnableStorage


---

## OwnerManager

_File: managers/OwnerManager.sol_

### external k1AddOwner
-> internal _k1AddOwner
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout


### external k1IsOwner
-> internal _k1IsOwner
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout


### external k1ListOwners
-> internal _k1OwnersLinkedList
  -> library ClaveStorage.layout


### external k1RemoveOwner
-> internal _k1RemoveOwner
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout


### external r1AddOwner
-> internal _r1AddOwner
  -> library Errors.INVALID_PUBKEY_LENGTH
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout


### external r1IsOwner
-> internal _r1IsOwner
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout


### external r1ListOwners
-> internal _r1OwnersLinkedList
  -> library ClaveStorage.layout


### external r1RemoveOwner
-> internal _r1RemoveOwner
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout
  -> library Errors.EMPTY_R1_OWNERS


### external resetOwners
-> private _r1ClearOwners
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout
-> private _k1ClearOwners
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout
-> internal _r1AddOwner
  -> library Errors.INVALID_PUBKEY_LENGTH
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout


---

## PasskeyValidator

_File: validators/PasskeyValidator.sol_

### external supportsInterface
_(no internal calls)_


### external validateSignature
-> private _validateSignature
  -> library Base64.encodeURL
  -> private _createMessage
  -> internal callVerifier
-> private _validateFatSignature
  -> private _decodeFatSignature
  -> library Base64.encodeURL
  -> private _createMessage
  -> internal callVerifier


---

## SocialRecoveryModule

_File: modules/recovery/SocialRecoveryModule.sol_

### external disable
-> public isInited
-> library Errors.RECOVERY_NOT_INITED
-> library Errors.MODULE_NOT_REMOVED_CORRECTLY
-> internal _stopRecovery
  -> public isRecovering


### external executeRecovery
-> library Errors.RECOVERY_NOT_STARTED
-> library Errors.RECOVERY_TIMELOCK


### external getEip712Hash
-> internal _recoveryDataHash


### external getGuardians
_(no internal calls)_


### external getThreshold
_(no internal calls)_


### external getTimelock
_(no internal calls)_


### external init
-> public isInited
-> library Errors.ALREADY_INITED
-> library Errors.MODULE_NOT_ADDED_CORRECTLY
-> internal _updateConfig
  -> private _isValidConfig
  -> library Errors.INVALID_RECOVERY_CONFIG


### public isInited
_(no internal calls)_


### public isRecovering
_(no internal calls)_


### external recoveryDataTypeHash
_(no internal calls)_


### external startRecovery
-> public isRecovering
-> library Errors.RECOVERY_IN_PROGRESS
-> public isInited
-> library Errors.RECOVERY_NOT_INITED
-> library Errors.INVALID_RECOVERY_NONCE
-> internal _recoveryDataHash
-> library Errors.GUARDIANS_MUST_BE_SORTED
-> library Errors.INVALID_GUARDIAN
-> library Errors.INSUFFICIENT_GUARDIANS


### external stopRecovery
-> public isRecovering
-> library Errors.RECOVERY_NOT_STARTED
-> internal _stopRecovery
  -> public isRecovering


### external supportsInterface
_(no internal calls)_


### external updateConfig
-> public isInited
-> library Errors.RECOVERY_NOT_INITED
-> public isRecovering
-> library Errors.RECOVERY_IN_PROGRESS
-> internal _updateConfig
  -> private _isValidConfig
  -> library Errors.INVALID_RECOVERY_CONFIG


---

## SwapReferralFeePayer

_File: referral/SwapReferralFeePayer.sol_

### external payFee
_(no internal calls)_


---

## SyncEarnRouter

_File: earn/SyncEarnRouter.sol_

### external deposit
-> external_callback ISyncRouter.TokenInput


### external stakePositions
_(no internal calls)_


### external swapDust
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## SyncEarnRouterV2

_File: earn/SyncEarnRouterV2.sol_

### external deposit
-> external_callback ISyncRouter.TokenInput


### external stakePositions
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## TEEValidator

_File: validators/TEEValidator.sol_

### external supportsInterface
_(no internal calls)_


### external validateSignature
-> internal callVerifier


---

## TokenCallbackHandler

_File: helpers/TokenCallbackHandler.sol_

### external onERC1155BatchReceived
_(no internal calls)_


### external onERC1155Received
_(no internal calls)_


### external onERC721Received
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## UUPSUpgradeable

_File: EmailRecoveryManager.sol_

### external proxiableUUID
_(no internal calls)_


### public upgradeToAndCall
-> private _upgradeToAndCallUUPS
  -> library ERC1967Utils.upgradeToAndCall
  -> library ERC1967Utils.ERC1967InvalidImplementation


---

## UpgradeManager

_File: managers/UpgradeManager.sol_

### external implementation
_(no internal calls)_


### external upgradeTo
-> library Errors.SAME_IMPLEMENTATION


---

## ValidationHandler

_File: handlers/ValidationHandler.sol_

### external k1AddOwner
-> internal _k1AddOwner
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout


### external k1AddValidator
-> internal _k1AddValidator
  -> internal _supportsK1
  -> library Errors.VALIDATOR_ERC165_FAIL
  -> private _k1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external k1IsOwner
-> internal _k1IsOwner
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout


### external k1IsValidator
-> internal _k1IsValidator
  -> private _k1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external k1ListOwners
-> internal _k1OwnersLinkedList
  -> library ClaveStorage.layout


### external k1ListValidators
-> private _k1ValidatorsLinkedList
  -> library ClaveStorage.layout


### external k1RemoveOwner
-> internal _k1RemoveOwner
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout


### external k1RemoveValidator
-> internal _k1RemoveValidator
  -> private _k1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external r1AddOwner
-> internal _r1AddOwner
  -> library Errors.INVALID_PUBKEY_LENGTH
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout


### external r1AddValidator
-> internal _r1AddValidator
  -> internal _supportsR1
  -> library Errors.VALIDATOR_ERC165_FAIL
  -> private _r1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external r1IsOwner
-> internal _r1IsOwner
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout


### external r1IsValidator
-> internal _r1IsValidator
  -> private _r1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external r1ListOwners
-> internal _r1OwnersLinkedList
  -> library ClaveStorage.layout


### external r1ListValidators
-> private _r1ValidatorsLinkedList
  -> library ClaveStorage.layout


### external r1RemoveOwner
-> internal _r1RemoveOwner
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout
  -> library Errors.EMPTY_R1_OWNERS


### external r1RemoveValidator
-> internal _r1RemoveValidator
  -> private _r1ValidatorsLinkedList
    -> library ClaveStorage.layout
  -> library Errors.EMPTY_R1_VALIDATORS


### external resetOwners
-> private _r1ClearOwners
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout
-> private _k1ClearOwners
  -> internal _k1OwnersLinkedList
    -> library ClaveStorage.layout
-> internal _r1AddOwner
  -> library Errors.INVALID_PUBKEY_LENGTH
  -> internal _r1OwnersLinkedList
    -> library ClaveStorage.layout


---

## ValidatorManager

_File: managers/ValidatorManager.sol_

### external k1AddValidator
-> internal _k1AddValidator
  -> internal _supportsK1
  -> library Errors.VALIDATOR_ERC165_FAIL
  -> private _k1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external k1IsValidator
-> internal _k1IsValidator
  -> private _k1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external k1ListValidators
-> private _k1ValidatorsLinkedList
  -> library ClaveStorage.layout


### external k1RemoveValidator
-> internal _k1RemoveValidator
  -> private _k1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external r1AddValidator
-> internal _r1AddValidator
  -> internal _supportsR1
  -> library Errors.VALIDATOR_ERC165_FAIL
  -> private _r1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external r1IsValidator
-> internal _r1IsValidator
  -> private _r1ValidatorsLinkedList
    -> library ClaveStorage.layout


### external r1ListValidators
-> private _r1ValidatorsLinkedList
  -> library ClaveStorage.layout


### external r1RemoveValidator
-> internal _r1RemoveValidator
  -> private _r1ValidatorsLinkedList
    -> library ClaveStorage.layout
  -> library Errors.EMPTY_R1_VALIDATORS


---

## Verifier

_File: EmailRecoveryManager.sol_

### public _packBytes2Fields
_(no internal calls)_


### public verifyEmailProof
-> public _packBytes2Fields


---

## ZtaKe

_File: earn/ZtaKe.sol_

### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable
    -> private _min


### public getApy
_(no internal calls)_


### external getReward
_(no internal calls)_


### public lastTimeRewardApplicable
-> private _min


### external notifyRewardAmount
_(no internal calls)_


### public rewardPerToken
-> public lastTimeRewardApplicable
  -> private _min


### external setLimitPerUser
_(no internal calls)_


### external setRewardsDuration
_(no internal calls)_


### external setTotalLimit
_(no internal calls)_


### external stake
_(no internal calls)_


### external withdraw
_(no internal calls)_


### external withdrawReward
_(no internal calls)_


---

## ZtaKeV2

_File: earn/ZtaKeV2.sol_

### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable
    -> private _min


### public getApy
_(no internal calls)_


### external getReward
_(no internal calls)_


### public lastTimeRewardApplicable
-> private _min


### external notifyRewardAmount
_(no internal calls)_


### public owner
_(no internal calls)_


### public renounceOwnership
-> internal _transferOwnership


### public rewardPerToken
-> public lastTimeRewardApplicable
  -> private _min


### external setLimitPerUser
_(no internal calls)_


### external setRewardsDuration
_(no internal calls)_


### external setTotalLimit
_(no internal calls)_


### external stake
_(no internal calls)_


### public transferOwnership
-> internal _transferOwnership


### external updateRegistry
_(no internal calls)_


### external withdraw
_(no internal calls)_


### external withdrawReward
-> public owner

