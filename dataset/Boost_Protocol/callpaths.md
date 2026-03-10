# Callpaths — Boost_Protocol

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AAction

_File: packages/evm/contracts/actions/AAction.sol_

### public initialize
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AAllowList

_File: packages/evm/contracts/allowlists/AAllowList.sol_

### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
_(no internal calls)_


### public isAuthorized
_(no internal calls)_


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


---

## AAllowListIncentive

_File: packages/evm/contracts/incentives/AAllowListIncentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ABoostRegistry

_File: packages/evm/contracts/ABoostRegistry.sol_

### public supportsInterface
_(no internal calls)_


---

## ABudget

_File: packages/evm/contracts/budgets/ABudget.sol_

### external clawbackFromTarget
-> external_callback AIncentive.ClawbackPayload


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
_(no internal calls)_


### public isAuthorized
_(no internal calls)_


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


---

## ACGDAIncentive

_File: packages/evm/contracts/incentives/ACGDAIncentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ACloneable

_File: packages/evm/contracts/shared/ACloneable.sol_

### public initialize
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AContractAction

_File: packages/evm/contracts/actions/AContractAction.sol_

### external execute
-> internal _buildPayload


### public getComponentInterface
_(no internal calls)_


### public prepare
-> internal _buildPayload


### public supportsInterface
_(no internal calls)_


---

## AERC1155Incentive

_File: packages/evm/contracts/incentives/AERC1155Incentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AERC20Incentive

_File: packages/evm/contracts/incentives/AERC20Incentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AERC20PeggedIncentive

_File: packages/evm/contracts/incentives/AERC20PeggedIncentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AERC20PeggedVariableCriteriaIncentive

_File: packages/evm/contracts/incentives/AERC20PeggedVariableCriteriaIncentive.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AERC20PeggedVariableCriteriaIncentiveV2

_File: packages/evm/contracts/incentives/AERC20PeggedVariableCriteriaIncentiveV2.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AERC20VariableCriteriaIncentive

_File: packages/evm/contracts/incentives/AERC20VariableCriteriaIncentive.sol_

### external claim
-> internal _isClaimable


### external clawback
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getMaxReward
_(no internal calls)_


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isClaimable
-> internal _isClaimable


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## AERC20VariableCriteriaIncentiveV2

_File: packages/evm/contracts/incentives/AERC20VariableCriteriaIncentiveV2.sol_

### external claim
-> internal _isClaimable


### external clawback
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getMaxReward
_(no internal calls)_


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isClaimable
-> internal _isClaimable


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## AERC20VariableIncentive

_File: packages/evm/contracts/incentives/AERC20VariableIncentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AERC721MintAction

_File: packages/evm/contracts/actions/AERC721MintAction.sol_

### external execute
-> internal _buildPayload


### public getComponentInterface
_(no internal calls)_


### public prepare
-> internal _buildPayload


### public supportsInterface
_(no internal calls)_


---

## AEventAction

_File: packages/evm/contracts/actions/AEventAction.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AIncentive

_File: packages/evm/contracts/incentives/AIncentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public initialize
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ALimitedSignerValidator

_File: packages/evm/contracts/validators/ALimitedSignerValidator.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ALimitedSignerValidatorV2

_File: packages/evm/contracts/validators/ALimitedSignerValidatorV2.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### external validatorName
_(no internal calls)_


---

## AManagedBudget

_File: packages/evm/contracts/budgets/AManagedBudget.sol_

### external clawbackFromTarget
-> external_callback AIncentive.ClawbackPayload


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
-> external_callback ABudget.supportsInterface


---

## AManagedBudgetWithFees

_File: packages/evm/contracts/budgets/AManagedBudgetWithFees.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AManagedBudgetWithFeesV2

_File: packages/evm/contracts/budgets/AManagedBudgetWithFeesV2.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AOffchainAccessList

_File: packages/evm/contracts/allowlists/AOffchainAccessList.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## APayableLimitedSignerValidator

_File: packages/evm/contracts/validators/APayableLimitedSignerValidator.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## APayableLimitedSignerValidatorV2

_File: packages/evm/contracts/validators/APayableLimitedSignerValidatorV2.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### external validatorName
_(no internal calls)_


---

## APointsIncentive

_File: packages/evm/contracts/incentives/APointsIncentive.sol_

### external asset
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ASignerValidator

_File: packages/evm/contracts/validators/ASignerValidator.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ASignerValidatorV2

_File: packages/evm/contracts/validators/ASignerValidatorV2.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### external validatorName
_(no internal calls)_


---

## ASimpleAllowList

_File: packages/evm/contracts/allowlists/ASimpleAllowList.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ASimpleDenyList

_File: packages/evm/contracts/allowlists/ASimpleDenyList.sol_

### public getComponentInterface
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## ATransparentBudget

_File: packages/evm/contracts/budgets/ATransparentBudget.sol_

### external clawbackFromTarget
-> external_callback AIncentive.ClawbackPayload


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
-> external_callback ABudget.supportsInterface


---

## AValidator

_File: packages/evm/contracts/validators/AValidator.sol_

### public getComponentInterface
_(no internal calls)_


### public initialize
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## AVestingBudget

_File: packages/evm/contracts/budgets/AVestingBudget.sol_

### external clawbackFromTarget
-> external_callback AIncentive.ClawbackPayload


### public getComponentInterface
_(no internal calls)_


### public supportsInterface
-> external_callback ABudget.supportsInterface


---

## AllowListIncentive

_File: packages/evm/contracts/incentives/AllowListIncentive.sol_

### external claim
-> internal _makeAllowListPayload


### external clawback
-> library BoostError.NotImplemented


### public getComponentInterface
_(no internal calls)_


### public initialize
_(no internal calls)_


### external isClaimable
_(no internal calls)_


### external preflight
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## BoostCore

_File: packages/evm/contracts/BoostCore.sol_

### external addIncentiveToBoost
-> library BoostError.Unauthorized
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> private _createSingleIncentive
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.InvalidInstance
  -> internal _makeTarget
    -> internal _checkTarget
      -> library BoostError.InvalidInstance
    -> internal _maybeClone
  -> internal _getFeeDisbursal
    -> external_callback ABudget.FungiblePayload
    -> external_callback ABudget.ERC1155Payload
    -> library BoostError.NotImplemented
  -> library BoostError.InvalidInitialization
  -> internal _addIncentive
    -> internal _generateKey


### external claimIncentive
-> public claimIncentiveFor
  -> internal _generateKey
  -> library BoostError.Unauthorized
  -> internal _getVerifiedReferrer
    -> library BoostError.Unauthorized
  -> internal _calculateFees
    -> internal _getAssetBalance
    -> library BoostError.ClaimFailed
  -> internal _transferReferralFee
  -> internal _transferProtocolFee
    -> internal _dustHatch


### public claimIncentiveFor
-> internal _generateKey
-> library BoostError.Unauthorized
-> internal _getVerifiedReferrer
  -> library BoostError.Unauthorized
-> internal _calculateFees
  -> internal _getAssetBalance
  -> library BoostError.ClaimFailed
-> internal _transferReferralFee
-> internal _transferProtocolFee
  -> internal _dustHatch


### external clawback
-> library BoostError.Unauthorized
-> internal _generateKey
-> library BoostError.ClawbackFailed


### external createBoost
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> internal _makeTarget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> internal _maybeClone
-> internal _makeIncentives
  -> private _createSingleIncentive
    -> internal _checkTarget
      -> library BoostError.InvalidInstance
    -> library BoostError.InvalidInstance
    -> internal _makeTarget
      -> internal _checkTarget
        -> library BoostError.InvalidInstance
      -> internal _maybeClone
    -> internal _getFeeDisbursal
      -> external_callback ABudget.FungiblePayload
      -> external_callback ABudget.ERC1155Payload
      -> library BoostError.NotImplemented
    -> library BoostError.InvalidInitialization
    -> internal _addIncentive
      -> internal _generateKey
-> library BoostError.InvalidInstance


### external getBoost
_(no internal calls)_


### external getBoostCount
_(no internal calls)_


### external getIncentiveFeesInfo
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setCreateBoostAuth
_(no internal calls)_


### external setDustThreshold
-> library BoostError.Unauthorized


### external setProtocolFee
_(no internal calls)_


### external setProtocolFeeModule
_(no internal calls)_


### external setProtocolFeeReceiver
_(no internal calls)_


### external setReferralFee
_(no internal calls)_


### external settleProtocolFees
-> internal _generateKey
-> internal _getAssetBalance
-> internal _transferProtocolFee
  -> internal _dustHatch


### external topupIncentiveFromBudget
-> library BoostError.InvalidInitialization
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> library BoostError.NotImplemented
-> internal _generateKey


### external topupIncentiveFromSender
-> library BoostError.InvalidInitialization
-> library BoostError.NotImplemented
-> internal _generateKey


### public version
_(no internal calls)_


---

## BoostCoreV1

_File: packages/evm/contracts/archive/BoostCoreV1.sol_

### external addIncentiveToBoost
-> library BoostError.Unauthorized
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> private _createSingleIncentive
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.InvalidInstance
  -> internal _makeTarget
    -> internal _checkTarget
      -> library BoostError.InvalidInstance
    -> internal _maybeClone
  -> internal _getFeeDisbursal
    -> external_callback ABudget.FungiblePayload
    -> external_callback ABudget.ERC1155Payload
    -> library BoostError.NotImplemented
  -> library BoostError.InvalidInitialization
  -> internal _addIncentive
    -> internal _generateKey


### external claimIncentive
-> public claimIncentiveFor
  -> internal _generateKey
  -> library BoostError.Unauthorized
  -> internal _getAssetBalance
  -> library BoostError.ClaimFailed
  -> internal _transferProtocolFee
    -> internal _dustHatch


### public claimIncentiveFor
-> internal _generateKey
-> library BoostError.Unauthorized
-> internal _getAssetBalance
-> library BoostError.ClaimFailed
-> internal _transferProtocolFee
  -> internal _dustHatch


### external clawback
-> library BoostError.Unauthorized
-> internal _generateKey
-> library BoostError.ClawbackFailed


### external createBoost
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> internal _makeTarget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> internal _maybeClone
-> internal _makeIncentives
  -> private _createSingleIncentive
    -> internal _checkTarget
      -> library BoostError.InvalidInstance
    -> library BoostError.InvalidInstance
    -> internal _makeTarget
      -> internal _checkTarget
        -> library BoostError.InvalidInstance
      -> internal _maybeClone
    -> internal _getFeeDisbursal
      -> external_callback ABudget.FungiblePayload
      -> external_callback ABudget.ERC1155Payload
      -> library BoostError.NotImplemented
    -> library BoostError.InvalidInitialization
    -> internal _addIncentive
      -> internal _generateKey
-> library BoostError.InvalidInstance


### external getBoost
_(no internal calls)_


### external getBoostCount
_(no internal calls)_


### external getIncentiveFeesInfo
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setCreateBoostAuth
_(no internal calls)_


### external setDustThreshold
-> library BoostError.Unauthorized


### external setProtocolFee
_(no internal calls)_


### external setProtocolFeeModule
_(no internal calls)_


### external setProtocolFeeReceiver
_(no internal calls)_


### external settleProtocolFees
-> internal _generateKey
-> internal _getAssetBalance
-> internal _transferProtocolFee
  -> internal _dustHatch


### external topupIncentiveFromBudget
-> library BoostError.InvalidInitialization
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> library BoostError.NotImplemented
-> internal _generateKey


### external topupIncentiveFromSender
-> library BoostError.InvalidInitialization
-> library BoostError.NotImplemented
-> internal _generateKey


### public version
_(no internal calls)_


---

## BoostCoreV1_1

_File: packages/evm/contracts/archive/BoostCoreV1_1.sol_

### external addIncentiveToBoost
-> library BoostError.Unauthorized
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> private _createSingleIncentive
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.InvalidInstance
  -> internal _makeTarget
    -> internal _checkTarget
      -> library BoostError.InvalidInstance
    -> internal _maybeClone
  -> internal _getFeeDisbursal
    -> external_callback ABudget.FungiblePayload
    -> external_callback ABudget.ERC1155Payload
    -> library BoostError.NotImplemented
  -> library BoostError.InvalidInitialization
  -> internal _addIncentive
    -> internal _generateKey


### external claimIncentive
-> public claimIncentiveFor
  -> internal _generateKey
  -> library BoostError.Unauthorized
  -> internal _getAssetBalance
  -> library BoostError.ClaimFailed
  -> internal _transferProtocolFee
    -> internal _dustHatch


### public claimIncentiveFor
-> internal _generateKey
-> library BoostError.Unauthorized
-> internal _getAssetBalance
-> library BoostError.ClaimFailed
-> internal _transferProtocolFee
  -> internal _dustHatch


### external clawback
-> library BoostError.Unauthorized
-> internal _generateKey
-> library BoostError.ClawbackFailed


### external createBoost
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> internal _makeTarget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> internal _maybeClone
-> internal _makeIncentives
  -> private _createSingleIncentive
    -> internal _checkTarget
      -> library BoostError.InvalidInstance
    -> library BoostError.InvalidInstance
    -> internal _makeTarget
      -> internal _checkTarget
        -> library BoostError.InvalidInstance
      -> internal _maybeClone
    -> internal _getFeeDisbursal
      -> external_callback ABudget.FungiblePayload
      -> external_callback ABudget.ERC1155Payload
      -> library BoostError.NotImplemented
    -> library BoostError.InvalidInitialization
    -> internal _addIncentive
      -> internal _generateKey
-> library BoostError.InvalidInstance


### external getBoost
_(no internal calls)_


### external getBoostCount
_(no internal calls)_


### external getIncentiveFeesInfo
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setCreateBoostAuth
_(no internal calls)_


### external setDustThreshold
-> library BoostError.Unauthorized


### external setProtocolFee
_(no internal calls)_


### external setProtocolFeeModule
_(no internal calls)_


### external setProtocolFeeReceiver
_(no internal calls)_


### external settleProtocolFees
-> internal _generateKey
-> internal _getAssetBalance
-> internal _transferProtocolFee
  -> internal _dustHatch


### external topupIncentiveFromBudget
-> library BoostError.InvalidInitialization
-> internal _checkBudget
  -> internal _checkTarget
    -> library BoostError.InvalidInstance
  -> library BoostError.Unauthorized
-> library BoostError.NotImplemented
-> internal _generateKey


### external topupIncentiveFromSender
-> library BoostError.InvalidInitialization
-> library BoostError.NotImplemented
-> internal _generateKey


### public version
_(no internal calls)_


---

## BoostRegistry

_File: packages/evm/contracts/BoostRegistry.sol_

### external deployClone
-> public getCloneIdentifier
  -> internal _getIdentifier


### public getBaseImplementation
_(no internal calls)_


### external getClone
_(no internal calls)_


### public getCloneIdentifier
-> internal _getIdentifier


### external getClones
_(no internal calls)_


### public getIdentifier
-> internal _getIdentifier


### external register
-> public getIdentifier
  -> internal _getIdentifier


### public supportsInterface
_(no internal calls)_


---

## CGDAIncentive

_File: packages/evm/contracts/incentives/CGDAIncentive.sol_

### external claim
-> internal _isClaimable
  -> public currentReward
-> library BoostError.ClaimFailed
-> public currentReward


### external clawback
_(no internal calls)_


### public currentReward
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
-> library BoostError.InsufficientFunds
-> library BoostError.InvalidInitialization


### public isAuthorized
_(no internal calls)_


### external isClaimable
-> internal _isClaimable
  -> public currentReward


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


---

## ContractAction

_File: packages/evm/contracts/actions/ContractAction.sol_

### external execute
-> internal _buildPayload


### public getComponentInterface
_(no internal calls)_


### public initialize
-> internal _initialize


### public prepare
-> internal _buildPayload


### public supportsInterface
_(no internal calls)_


---

## ERC1155Incentive

_File: packages/evm/contracts/incentives/ERC1155Incentive.sol_

### external claim
-> internal _getTxHash
-> internal _isClaimable


### external clawback
-> library BoostError.ClaimFailed


### public getComponentInterface
_(no internal calls)_


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
-> library BoostError.NotImplemented
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isAuthorized
_(no internal calls)_


### public isClaimable
-> internal _getTxHash
-> internal _isClaimable


### external onERC1155BatchReceived
_(no internal calls)_


### external onERC1155Received
_(no internal calls)_


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.ERC1155Payload


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


---

## ERC20Incentive

_File: packages/evm/contracts/incentives/ERC20Incentive.sol_

### external claim
-> internal _isClaimable


### external clawback
-> library BoostError.ClaimFailed


### external drawRaffle
-> library BoostError.Unauthorized
-> library LibPRNG.PRNG


### public getComponentInterface
_(no internal calls)_


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isAuthorized
_(no internal calls)_


### public isClaimable
-> internal _isClaimable


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization
-> library BoostError.Unauthorized


---

## ERC20PeggedIncentive

_File: packages/evm/contracts/incentives/ERC20PeggedIncentive.sol_

### external claim
-> internal _isClaimable


### external clawback
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getPeg
_(no internal calls)_


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isAuthorized
_(no internal calls)_


### public isClaimable
-> internal _isClaimable


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## ERC20PeggedVariableCriteriaIncentive

_File: packages/evm/contracts/incentives/ERC20PeggedVariableCriteriaIncentive.sol_

### external claim
-> internal _isClaimable


### external clawback
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getIncentiveCriteria
_(no internal calls)_


### external getMaxReward
_(no internal calls)_


### external getPeg
_(no internal calls)_


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isAuthorized
_(no internal calls)_


### public isClaimable
-> internal _isClaimable


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## ERC20PeggedVariableCriteriaIncentiveV2

_File: packages/evm/contracts/incentives/ERC20PeggedVariableCriteriaIncentiveV2.sol_

### external claim
-> internal _isClaimable


### external clawback
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getIncentiveCriteria
_(no internal calls)_


### external getMaxReward
_(no internal calls)_


### external getPeg
_(no internal calls)_


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isAuthorized
_(no internal calls)_


### public isClaimable
-> internal _isClaimable


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## ERC20VariableCriteriaIncentive

_File: packages/evm/contracts/incentives/ERC20VariableCriteriaIncentive.sol_

### external claim
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getIncentiveCriteria
_(no internal calls)_


### external getMaxReward
_(no internal calls)_


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## ERC20VariableCriteriaIncentiveV2

_File: packages/evm/contracts/incentives/ERC20VariableCriteriaIncentiveV2.sol_

### external claim
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getIncentiveCriteria
_(no internal calls)_


### external getMaxReward
_(no internal calls)_


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## ERC20VariableIncentive

_File: packages/evm/contracts/incentives/ERC20VariableIncentive.sol_

### external claim
-> internal _isClaimable


### external clawback
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external grantManyRoles
-> library BoostError.LengthMismatch


### public initialize
-> library BoostError.InvalidInitialization
-> library BoostError.InsufficientFunds


### public isAuthorized
_(no internal calls)_


### public isClaimable
-> internal _isClaimable


### external preflight
-> external_callback ABudget.Transfer
-> external_callback ABudget.FungiblePayload


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


### external topup
-> library BoostError.InvalidInitialization


---

## ERC721MintAction

_File: packages/evm/contracts/actions/ERC721MintAction.sol_

### external execute
-> library BoostError.NotImplemented


### public getComponentInterface
_(no internal calls)_


### public initialize
-> internal _initialize


### public prepare
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### external validate
_(no internal calls)_


---

## EventAction

_File: packages/evm/contracts/actions/EventAction.sol_

### external execute
-> library BoostError.NotImplemented


### public getActionClaimant
_(no internal calls)_


### public getActionStep
_(no internal calls)_


### public getActionSteps
_(no internal calls)_


### public getActionStepsCount
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public initialize
-> internal _initialize


### public prepare
-> library BoostError.NotImplemented


### public supportsInterface
_(no internal calls)_


---

## LimitedSignerValidator

_File: packages/evm/contracts/validators/LimitedSignerValidator.sol_

### public getComponentInterface
_(no internal calls)_


### public hashClaimantData
_(no internal calls)_


### public hashSignerData
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setAuthorized
-> library BoostError.LengthMismatch


### external setValidatorCaller
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public validate
-> internal _incrementClaim
  -> public hashClaimantData
-> library BoostError.MaximumClaimed


---

## LimitedSignerValidatorV2

_File: packages/evm/contracts/validators/LimitedSignerValidatorV2.sol_

### public getComponentInterface
_(no internal calls)_


### public hashClaimantData
_(no internal calls)_


### public hashSignerData
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setAuthorized
-> library BoostError.LengthMismatch


### external setValidatorCaller
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public validate
-> public hashClaimantData
-> library BoostError.MaximumClaimed


### external validatorName
_(no internal calls)_


---

## ManagedBudget

_File: packages/evm/contracts/budgets/ManagedBudget.sol_

### external allocate
_(no internal calls)_


### public available
_(no internal calls)_


### external clawback
-> internal _transferFungible
  -> public available
  -> library SafeTransferLib.safeTransferETH
-> public available
-> internal _transferERC1155
  -> public available


### external clawbackFromTarget
-> external_callback AIncentive.ClawbackPayload


### public disburse
-> public available
-> internal _transferFungible
  -> public available
  -> library SafeTransferLib.safeTransferETH
-> internal _transferERC1155
  -> public available


### external disburseBatch
-> public disburse
  -> public available
  -> internal _transferFungible
    -> public available
    -> library SafeTransferLib.safeTransferETH
  -> internal _transferERC1155
    -> public available


### external distributed
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public initialize
_(no internal calls)_


### external onERC1155BatchReceived
_(no internal calls)_


### external onERC1155Received
_(no internal calls)_


### external reconcile
_(no internal calls)_


### public supportsInterface
-> external_callback ABudget.supportsInterface


### external total
_(no internal calls)_


---

## ManagedBudgetWithFees

_File: packages/evm/contracts/budgets/ManagedBudgetWithFees.sol_

### external allocate
_(no internal calls)_


### public available
_(no internal calls)_


### external clawback
-> internal _transferFungible
  -> public available
  -> library SafeTransferLib.safeTransferETH
-> public available
-> internal _transferERC1155
  -> public available


### public clawbackFromTarget
-> external_callback AIncentive.ClawbackPayload


### external clawbackFromTargetAndPayFee
-> public clawbackFromTarget
  -> external_callback AIncentive.ClawbackPayload
-> public payManagementFee
  -> internal _transferManagementFee
    -> library BoostError.ZeroBalancePayout
    -> internal _transferFungible
      -> public available
      -> library SafeTransferLib.safeTransferETH
  -> library BoostError.NotImplemented


### public disburse
-> public available
-> internal _transferFungible
  -> public available
  -> library SafeTransferLib.safeTransferETH
-> internal _transferERC1155
  -> public available


### external disburseBatch
-> public disburse
  -> public available
  -> internal _transferFungible
    -> public available
    -> library SafeTransferLib.safeTransferETH
  -> internal _transferERC1155
    -> public available


### external distributed
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public initialize
_(no internal calls)_


### external onERC1155BatchReceived
_(no internal calls)_


### external onERC1155Received
_(no internal calls)_


### public payManagementFee
-> internal _transferManagementFee
  -> library BoostError.ZeroBalancePayout
  -> internal _transferFungible
    -> public available
    -> library SafeTransferLib.safeTransferETH
-> library BoostError.NotImplemented


### external reconcile
_(no internal calls)_


### external setManagementFee
_(no internal calls)_


### public supportsInterface
-> external_callback AManagedBudgetWithFees.supportsInterface


### external topupIncentive
_(no internal calls)_


### external total
-> public available


---

## ManagedBudgetWithFeesV2

_File: packages/evm/contracts/budgets/ManagedBudgetWithFeesV2.sol_

### external allocate
_(no internal calls)_


### public available
_(no internal calls)_


### public clawbackFromTarget
-> external_callback ManagedBudgetWithFees.clawbackFromTarget


### external clawbackFromTargetAndPayFee
-> external_callback ManagedBudgetWithFees.clawbackFromTarget
  -> external_callback ManagedBudgetWithFees.clawbackFromTarget
-> public payManagementFee
  -> library BoostError.Unauthorized
  -> internal _transferManagementFee
    -> library BoostError.ZeroBalancePayout
  -> library BoostError.NotImplemented


### public disburse
-> public available


### public getComponentInterface
_(no internal calls)_


### public initialize
-> internal _setCore


### public payManagementFee
-> library BoostError.Unauthorized
-> internal _transferManagementFee
  -> library BoostError.ZeroBalancePayout
-> library BoostError.NotImplemented


### external setCore
-> internal _setCore


### external setManagementFee
_(no internal calls)_


### public supportsInterface
-> external_callback AManagedBudgetWithFeesV2.supportsInterface


### external topupIncentive
_(no internal calls)_


### external total
-> public available


---

## ManagedBudgetWithFeesV2Factory

_File: packages/evm/contracts/budgets/ManagedBudgetWithFeesV2Factory.sol_

### external deployBudget
-> external_callback ManagedBudgetWithFees.InitPayloadWithFee


### external predictBudgetAddress
_(no internal calls)_


### external setImplementation
_(no internal calls)_


---

## OffchainAccessList

_File: packages/evm/contracts/allowlists/OffchainAccessList.sol_

### external addAllowListId
-> public hasAllowListId


### external addDenyListId
-> public hasDenyListId


### external getAllowListIds
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### external getDenyListIds
_(no internal calls)_


### public hasAllowListId
_(no internal calls)_


### public hasDenyListId
_(no internal calls)_


### public initialize
_(no internal calls)_


### external isAllowed
_(no internal calls)_


### external removeAllowListId
_(no internal calls)_


### external removeDenyListId
_(no internal calls)_


### external setAllowListIds
_(no internal calls)_


### external setDenyListIds
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## PassthroughAuth

_File: packages/evm/contracts/auth/PassthroughAuth.sol_

### public isAuthorized
_(no internal calls)_


---

## PayableLimitedSignerValidator

_File: packages/evm/contracts/validators/PayableLimitedSignerValidator.sol_

### external getClaimFee
-> internal _getClaimFee


### public getComponentInterface
_(no internal calls)_


### public hashClaimantData
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setClaimFee
-> library BoostError.Unauthorized


### public supportsInterface
_(no internal calls)_


### public validate
-> internal _getClaimFee


---

## PayableLimitedSignerValidatorV2

_File: packages/evm/contracts/validators/PayableLimitedSignerValidatorV2.sol_

### external getClaimFee
-> internal _getClaimFee


### public getComponentInterface
_(no internal calls)_


### public hashClaimantData
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setClaimFee
-> library BoostError.Unauthorized


### public supportsInterface
_(no internal calls)_


### public validate
-> internal _getClaimFee
-> library BoostError.Unauthorized


### external validatorName
_(no internal calls)_


---

## Points

_File: packages/evm/contracts/tokens/Points.sol_

### external initialize
_(no internal calls)_


### external issue
_(no internal calls)_


### public name
_(no internal calls)_


### public symbol
_(no internal calls)_


---

## PointsIncentive

_File: packages/evm/contracts/incentives/PointsIncentive.sol_

### external claim
-> library BoostError.Unauthorized
-> internal _isClaimable


### external clawback
-> library BoostError.NotImplemented


### public getComponentInterface
_(no internal calls)_


### public initialize
-> library BoostError.InvalidInitialization


### public isClaimable
-> internal _isClaimable


### external preflight
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


---

## RBAC

_File: packages/evm/contracts/shared/RBAC.sol_

### external grantManyRoles
-> library BoostError.LengthMismatch


### public isAuthorized
_(no internal calls)_


### external revokeManyRoles
-> library BoostError.LengthMismatch


### external setAuthorized
-> library BoostError.LengthMismatch


---

## SignerValidator

_File: packages/evm/contracts/validators/SignerValidator.sol_

### public getComponentInterface
_(no internal calls)_


### public hashSignerData
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setAuthorized
-> library BoostError.LengthMismatch


### external setValidatorCaller
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public validate
-> library BoostError.Unauthorized
-> public hashSignerData
-> library BoostError.InvalidIncentive


---

## SignerValidatorV2

_File: packages/evm/contracts/validators/SignerValidatorV2.sol_

### public getComponentInterface
_(no internal calls)_


### public hashSignerData
_(no internal calls)_


### public initialize
_(no internal calls)_


### external setAuthorized
-> library BoostError.LengthMismatch


### external setValidatorCaller
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public validate
-> library BoostError.Unauthorized
-> public hashSignerData
-> library BoostError.InvalidIncentive


### external validatorName
_(no internal calls)_


---

## SimpleAllowList

_File: packages/evm/contracts/allowlists/SimpleAllowList.sol_

### public getComponentInterface
_(no internal calls)_


### public initialize
_(no internal calls)_


### external isAllowed
_(no internal calls)_


### external setAllowed
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


---

## SimpleDenyList

_File: packages/evm/contracts/allowlists/SimpleDenyList.sol_

### public getComponentInterface
_(no internal calls)_


### public initialize
_(no internal calls)_


### external isAllowed
_(no internal calls)_


### external setDenied
-> library BoostError.LengthMismatch


### public supportsInterface
_(no internal calls)_


---

## TransparentBudget

_File: packages/evm/contracts/budgets/TransparentBudget.sol_

### external allocate
-> library BoostError.NotImplemented


### public available
_(no internal calls)_


### external clawback
-> library BoostError.NotImplemented


### external clawbackFromTarget
-> library BoostError.Unauthorized
-> external_callback AIncentive.ClawbackPayload


### public createBoost
-> internal _allocate
  -> internal getFungibleAmountAndKey
    -> library LibTransient.tUint256
  -> internal _allocateERC20
    -> internal getFungibleAmountAndKey
      -> library LibTransient.tUint256
  -> internal getERC1155AmountAndKey
    -> library LibTransient.tUint256
  -> library BoostError.NotImplemented
-> library LibTransient.tUint256
-> library BoostError.Unauthorized


### external createBoostWithPermit2
-> internal _allocateERC20
  -> internal getFungibleAmountAndKey
    -> library LibTransient.tUint256
-> external_callback IPermit2.SignatureTransferDetails
-> external_callback IPermit2.TokenPermissions
-> internal _allocate
  -> internal getFungibleAmountAndKey
    -> library LibTransient.tUint256
  -> internal _allocateERC20
    -> internal getFungibleAmountAndKey
      -> library LibTransient.tUint256
  -> internal getERC1155AmountAndKey
    -> library LibTransient.tUint256
  -> library BoostError.NotImplemented
-> external_callback IPermit2.PermitBatchTransferFrom
-> library LibTransient.tUint256
-> library BoostError.Unauthorized


### public disburse
-> internal getFungibleAmountAndKey
  -> library LibTransient.tUint256
-> internal _transferFungible
  -> internal getFungibleAmountAndKey
    -> library LibTransient.tUint256
  -> library SafeTransferLib.safeTransferETH
-> internal getERC1155AmountAndKey
  -> library LibTransient.tUint256
-> internal _transferERC1155
  -> public available


### external disburseBatch
-> public disburse
  -> internal getFungibleAmountAndKey
    -> library LibTransient.tUint256
  -> internal _transferFungible
    -> internal getFungibleAmountAndKey
      -> library LibTransient.tUint256
    -> library SafeTransferLib.safeTransferETH
  -> internal getERC1155AmountAndKey
    -> library LibTransient.tUint256
  -> internal _transferERC1155
    -> public available


### external distributed
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public isAuthorized
_(no internal calls)_


### external onERC1155BatchReceived
_(no internal calls)_


### external onERC1155Received
_(no internal calls)_


### external reconcile
_(no internal calls)_


### public supportsInterface
-> external_callback ABudget.supportsInterface


### external total
_(no internal calls)_


---

## VestingBudget

_File: packages/evm/contracts/budgets/VestingBudget.sol_

### external allocate
_(no internal calls)_


### public available
-> internal _vestedAllocation
  -> internal _linearVestedAmount


### external clawback
-> public available
  -> internal _vestedAllocation
    -> internal _linearVestedAmount
-> internal _transferFungible
  -> public available
    -> internal _vestedAllocation
      -> internal _linearVestedAmount
  -> library SafeTransferLib.safeTransferETH


### public disburse
-> internal _transferFungible
  -> public available
    -> internal _vestedAllocation
      -> internal _linearVestedAmount
  -> library SafeTransferLib.safeTransferETH


### external disburseBatch
-> public disburse
  -> internal _transferFungible
    -> public available
      -> internal _vestedAllocation
        -> internal _linearVestedAmount
    -> library SafeTransferLib.safeTransferETH


### external distributed
_(no internal calls)_


### external end
_(no internal calls)_


### public getComponentInterface
_(no internal calls)_


### public initialize
_(no internal calls)_


### external reconcile
_(no internal calls)_


### public supportsInterface
-> external_callback ABudget.supportsInterface


### external total
_(no internal calls)_

