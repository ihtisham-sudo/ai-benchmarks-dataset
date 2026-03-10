# Callpaths — SuperFluid_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AaveETHYieldBackend

_File: packages/ethereum-contracts/contracts/superfluid/AaveETHYieldBackend.sol_

### public deposit
_(no internal calls)_


### external disable
_(no internal calls)_


### external enable
_(no internal calls)_


### external unwrapWETHAndForwardETH
_(no internal calls)_


### public withdraw
_(no internal calls)_


### external withdrawMax
-> public withdraw


### external withdrawSurplus
_(no internal calls)_


---

## AaveYieldBackend

_File: packages/ethereum-contracts/contracts/superfluid/AaveYieldBackend.sol_

### public deposit
_(no internal calls)_


### external disable
_(no internal calls)_


### external enable
_(no internal calls)_


### public withdraw
_(no internal calls)_


### external withdrawMax
-> public withdraw


### external withdrawSurplus
_(no internal calls)_


---

## AgreementBase

_File: packages/ethereum-contracts/contracts/agreements/AgreementBase.sol_

### external castrate
_(no internal calls)_


### public getCodeAddress
-> library UUPSUtils.implementation


### public proxiableUUID
_(no internal calls)_


### external updateCode
-> internal _updateCodeAddress
  -> library UUPSUtils.implementation
  -> public proxiableUUID
  -> library UUPSUtils.setImplementation


---

## Aqueduct

_File: packages/solidity-semantic-money/src/examples/Aqueduct.sol_

### external onFlowUpdate
-> internal _onFlowUpdate
  -> library AqueductLibrary.updateSide
  -> internal _adjustFlowRemainder


### external pool1
_(no internal calls)_


### external pool2
_(no internal calls)_


### external token1
_(no internal calls)_


### external token2
_(no internal calls)_


---

## BatchLiquidator

_File: packages/ethereum-contracts/contracts/utils/BatchLiquidator.sol_

### external deleteFlow
-> internal _deleteFlow


### external deleteFlows
-> internal _deleteFlow


---

## BeaconProxiable

_File: packages/ethereum-contracts/contracts/upgradability/BeaconProxiable.sol_

### external castrate
_(no internal calls)_


---

## CFAHotFuzz

_File: packages/hot-fuzz/contracts/superfluid-tests/ConstantFlowAgreementV1.hott.sol_

### public cfaLiquidateFlow
_(no internal calls)_


### public createFlow
_(no internal calls)_


### public decreaseFlowRateAllowance
_(no internal calls)_


### public decreaseFlowRateAllowanceWithPermissions
_(no internal calls)_


### public deleteFlow
_(no internal calls)_


### public increaseFlowRateAllowance
_(no internal calls)_


### public increaseFlowRateAllowanceWithPermissions
_(no internal calls)_


### public revokeFlowPermissions
_(no internal calls)_


### public setFlowPermissions
_(no internal calls)_


### public setMaxFlowPermissions
_(no internal calls)_


---

## CFAHotFuzzMixin

_File: packages/hot-fuzz/contracts/superfluid-tests/ConstantFlowAgreementV1.hott.sol_

### public cfaLiquidateFlow
-> internal _getThreeTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public createFlow
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public decreaseFlowRateAllowance
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public decreaseFlowRateAllowanceWithPermissions
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public deleteFlow
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public echidna_check_liquiditySumInvariance
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_netFlowRateSumInvariant
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_total_supply
_(no internal calls)_


### public echidna_check_validLiquidationNeverRevertsInvariant
_(no internal calls)_


### public increaseFlowRateAllowance
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public increaseFlowRateAllowanceWithPermissions
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public revokeFlowPermissions
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public setFlowPermissions
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public setMaxFlowPermissions
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


---

## CFAProperties

_File: packages/hot-fuzz/contracts/superfluid-tests/ConstantFlowAgreementV1.prop.t.sol_

### public testMaximumFlowRateAllowedForDeposit
_(no internal calls)_


### public testMinimumDeposit
_(no internal calls)_


---

## CFASuperAppBase

_File: packages/ethereum-contracts/contracts/apps/CFASuperAppBase.sol_

### external afterAgreementCreated
-> internal _isAcceptedAgreement
-> public isAcceptedSuperToken
-> internal onFlowCreated


### external afterAgreementTerminated
-> internal _isAcceptedAgreement
-> public isAcceptedSuperToken
-> internal onInFlowDeleted
-> internal onOutFlowDeleted


### external afterAgreementUpdated
-> internal _isAcceptedAgreement
-> public isAcceptedSuperToken
-> private _afterAgreementUpdatedHelper
  -> internal onFlowUpdated


### external beforeAgreementCreated
_(no internal calls)_


### external beforeAgreementTerminated
-> internal _isAcceptedAgreement
-> public isAcceptedSuperToken


### external beforeAgreementUpdated
-> internal _isAcceptedAgreement
-> public isAcceptedSuperToken


### public getConfigWord
_(no internal calls)_


### public isAcceptedSuperToken
_(no internal calls)_


### public selfRegister
-> public getConfigWord


---

## CFAv1Forwarder

_File: packages/ethereum-contracts/contracts/utils/CFAv1Forwarder.sol_

### external createFlow
-> internal _createFlow
  -> internal _forwardBatchCall
    -> internal _forwardBatchCallWithValue
      -> library CallUtils.revertFromReturnedData


### external deleteFlow
-> internal _deleteFlow
  -> internal _forwardBatchCall
    -> internal _forwardBatchCallWithValue
      -> library CallUtils.revertFromReturnedData


### external getAccountFlowInfo
_(no internal calls)_


### external getAccountFlowrate
_(no internal calls)_


### external getBufferAmountByFlowrate
_(no internal calls)_


### external getFlowInfo
_(no internal calls)_


### external getFlowOperatorPermissions
_(no internal calls)_


### external getFlowrate
_(no internal calls)_


### external grantPermissions
-> internal _updateFlowOperatorPermissions
  -> internal _forwardBatchCall
    -> internal _forwardBatchCallWithValue
      -> library CallUtils.revertFromReturnedData


### external revokePermissions
-> internal _updateFlowOperatorPermissions
  -> internal _forwardBatchCall
    -> internal _forwardBatchCallWithValue
      -> library CallUtils.revertFromReturnedData


### external setFlowrate
-> internal _setFlowrateFrom
  -> internal _createFlow
    -> internal _forwardBatchCall
      -> internal _forwardBatchCallWithValue
        -> library CallUtils.revertFromReturnedData
  -> internal _updateFlow
    -> internal _forwardBatchCall
      -> internal _forwardBatchCallWithValue
        -> library CallUtils.revertFromReturnedData
  -> internal _deleteFlow
    -> internal _forwardBatchCall
      -> internal _forwardBatchCallWithValue
        -> library CallUtils.revertFromReturnedData


### external setFlowrateFrom
-> internal _setFlowrateFrom
  -> internal _createFlow
    -> internal _forwardBatchCall
      -> internal _forwardBatchCallWithValue
        -> library CallUtils.revertFromReturnedData
  -> internal _updateFlow
    -> internal _forwardBatchCall
      -> internal _forwardBatchCallWithValue
        -> library CallUtils.revertFromReturnedData
  -> internal _deleteFlow
    -> internal _forwardBatchCall
      -> internal _forwardBatchCallWithValue
        -> library CallUtils.revertFromReturnedData


### external updateFlow
-> internal _updateFlow
  -> internal _forwardBatchCall
    -> internal _forwardBatchCallWithValue
      -> library CallUtils.revertFromReturnedData


### external updateFlowOperatorPermissions
-> internal _updateFlowOperatorPermissions
  -> internal _forwardBatchCall
    -> internal _forwardBatchCallWithValue
      -> library CallUtils.revertFromReturnedData


---

## ConstantFlowAgreementV1

_File: packages/ethereum-contracts/contracts/agreements/ConstantFlowAgreementV1.sol_

### public addPermissions
_(no internal calls)_


### external agreementType
_(no internal calls)_


### external authorizeFlowOperatorWithFullControl
-> public updateFlowOperatorPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> private _generateFlowOperatorId
  -> internal _encodeFlowOperatorData


### external createFlow
-> library AgreementLibrary.authorizeTokenAccess
-> internal _createFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### external createFlowByOperator
-> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData
-> internal _createFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### public decreaseFlowRateAllowance
-> public decreaseFlowRateAllowanceWithPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> public getFlowOperatorData
    -> private _generateFlowOperatorId
    -> private _getFlowOperatorData
      -> internal _decodeFlowOperatorData
  -> public removePermissions
  -> private _updateFlowOperatorData
    -> internal _encodeFlowOperatorData


### public decreaseFlowRateAllowanceWithPermissions
-> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
  -> library FlowOperatorDefinitions.isPermissionsClean
  -> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> public removePermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData


### external deleteFlow
-> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> internal _deleteFlow
  -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _makeLiquidationPayouts
    -> private _getAccountFlowState
      -> internal _decodeFlowData
    -> library SolvencyHelperLibrary.decode3PsData
    -> library SolvencyHelperLibrary.isPatricianPeriod
      -> library SolvencyHelperLibrary.decode3PsData
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> library SolvencyHelperLibrary.isPatricianPeriod
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData


### external deleteFlowByOperator
-> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> internal _deleteFlow
  -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _makeLiquidationPayouts
    -> private _getAccountFlowState
      -> internal _decodeFlowData
    -> library SolvencyHelperLibrary.decode3PsData
    -> library SolvencyHelperLibrary.isPatricianPeriod
      -> library SolvencyHelperLibrary.decode3PsData
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> library SolvencyHelperLibrary.isPatricianPeriod
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData


### external getAccountFlowInfo
-> private _getAccountFlowState
  -> internal _decodeFlowData


### external getDepositRequiredForFlowRate
-> library SuperfluidGovernanceConfigs.decodePPPConfig
-> internal _getDepositRequiredForFlowRatePure
  -> internal _calculateDeposit
    -> internal _clipDepositNumberRoundingUp
  -> library AgreementLibrary.max


### external getFlow
-> private _getAgreementData
  -> internal _decodeFlowData
-> private _generateFlowId


### external getFlowByID
-> private _getAgreementData
  -> internal _decodeFlowData


### public getFlowOperatorData
-> private _generateFlowOperatorId
-> private _getFlowOperatorData
  -> internal _decodeFlowOperatorData


### external getFlowOperatorDataByID
-> private _getFlowOperatorData
  -> internal _decodeFlowOperatorData


### external getMaximumFlowRateFromDeposit
-> library SolvencyHelperLibrary.decode3PsData
-> internal _getMaximumFlowRateFromDepositPure
  -> internal _clipDepositNumberRoundingDown


### external getNetFlow
-> private _getAccountFlowState
  -> internal _decodeFlowData


### public increaseFlowRateAllowance
-> public increaseFlowRateAllowanceWithPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> public getFlowOperatorData
    -> private _generateFlowOperatorId
    -> private _getFlowOperatorData
      -> internal _decodeFlowOperatorData
  -> public addPermissions
  -> private _updateFlowOperatorData
    -> internal _encodeFlowOperatorData


### public increaseFlowRateAllowanceWithPermissions
-> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
  -> library FlowOperatorDefinitions.isPermissionsClean
  -> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> public addPermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData


### public isPatricianPeriod
-> library SolvencyHelperLibrary.decode3PsData
-> private _getAccountFlowState
  -> internal _decodeFlowData
-> library SolvencyHelperLibrary.isPatricianPeriod


### external isPatricianPeriodNow
-> public isPatricianPeriod
  -> library SolvencyHelperLibrary.decode3PsData
  -> private _getAccountFlowState
    -> internal _decodeFlowData
  -> library SolvencyHelperLibrary.isPatricianPeriod


### public proxiableUUID
_(no internal calls)_


### external realtimeBalanceOf
-> private _getAccountFlowState
  -> internal _decodeFlowData


### public removePermissions
_(no internal calls)_


### external revokeFlowOperatorWithFullControl
-> public updateFlowOperatorPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> private _generateFlowOperatorId
  -> internal _encodeFlowOperatorData


### external updateCode
_(no internal calls)_


### external updateFlow
-> library AgreementLibrary.authorizeTokenAccess
-> private _generateFlowId
-> private _getAgreementData
  -> internal _decodeFlowData
-> internal _updateFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### external updateFlowByOperator
-> library AgreementLibrary.authorizeTokenAccess
-> private _getAgreementData
  -> internal _decodeFlowData
-> private _generateFlowId
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData
-> internal _updateFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### public updateFlowOperatorPermissions
-> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
  -> library FlowOperatorDefinitions.isPermissionsClean
  -> library AgreementLibrary.authorizeTokenAccess
-> private _generateFlowOperatorId
-> internal _encodeFlowOperatorData


---

## ConstantFlowAgreementV1Mock

_File: packages/hot-fuzz/contracts/superfluid-tests/ConstantFlowAgreementV1.prop.t.sol_

### public addPermissions
_(no internal calls)_


### external authorizeFlowOperatorWithFullControl
-> public updateFlowOperatorPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> private _generateFlowOperatorId
  -> internal _encodeFlowOperatorData


### external createFlow
-> library AgreementLibrary.authorizeTokenAccess
-> internal _createFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### external createFlowByOperator
-> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData
-> internal _createFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### public decreaseFlowRateAllowance
-> public decreaseFlowRateAllowanceWithPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> public getFlowOperatorData
    -> private _generateFlowOperatorId
    -> private _getFlowOperatorData
      -> internal _decodeFlowOperatorData
  -> public removePermissions
  -> private _updateFlowOperatorData
    -> internal _encodeFlowOperatorData


### public decreaseFlowRateAllowanceWithPermissions
-> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
  -> library FlowOperatorDefinitions.isPermissionsClean
  -> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> public removePermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData


### external deleteFlow
-> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> internal _deleteFlow
  -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _makeLiquidationPayouts
    -> private _getAccountFlowState
      -> internal _decodeFlowData
    -> library SolvencyHelperLibrary.decode3PsData
    -> library SolvencyHelperLibrary.isPatricianPeriod
      -> library SolvencyHelperLibrary.decode3PsData
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> library SolvencyHelperLibrary.isPatricianPeriod
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData


### external deleteFlowByOperator
-> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> internal _deleteFlow
  -> private _generateFlowId
  -> private _getAgreementData
    -> internal _decodeFlowData
  -> private _makeLiquidationPayouts
    -> private _getAccountFlowState
      -> internal _decodeFlowData
    -> library SolvencyHelperLibrary.decode3PsData
    -> library SolvencyHelperLibrary.isPatricianPeriod
      -> library SolvencyHelperLibrary.decode3PsData
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> library SolvencyHelperLibrary.isPatricianPeriod
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData


### external getAccountFlowInfo
-> private _getAccountFlowState
  -> internal _decodeFlowData


### external getDepositRequiredForFlowRate
-> library SuperfluidGovernanceConfigs.decodePPPConfig
-> internal _getDepositRequiredForFlowRatePure
  -> internal _calculateDeposit
    -> internal _clipDepositNumberRoundingUp
  -> library AgreementLibrary.max


### external getDepositRequiredForFlowRatePure
-> internal _getDepositRequiredForFlowRatePure
  -> internal _calculateDeposit
    -> internal _clipDepositNumberRoundingUp
  -> library AgreementLibrary.max


### external getFlow
-> private _getAgreementData
  -> internal _decodeFlowData
-> private _generateFlowId


### external getFlowByID
-> private _getAgreementData
  -> internal _decodeFlowData


### public getFlowOperatorData
-> private _generateFlowOperatorId
-> private _getFlowOperatorData
  -> internal _decodeFlowOperatorData


### external getFlowOperatorDataByID
-> private _getFlowOperatorData
  -> internal _decodeFlowOperatorData


### external getMaximumFlowRateFromDeposit
-> library SolvencyHelperLibrary.decode3PsData
-> internal _getMaximumFlowRateFromDepositPure
  -> internal _clipDepositNumberRoundingDown


### external getMaximumFlowRateFromDepositPure
-> internal _getMaximumFlowRateFromDepositPure
  -> internal _clipDepositNumberRoundingDown


### external getNetFlow
-> private _getAccountFlowState
  -> internal _decodeFlowData


### public increaseFlowRateAllowance
-> public increaseFlowRateAllowanceWithPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> public getFlowOperatorData
    -> private _generateFlowOperatorId
    -> private _getFlowOperatorData
      -> internal _decodeFlowOperatorData
  -> public addPermissions
  -> private _updateFlowOperatorData
    -> internal _encodeFlowOperatorData


### public increaseFlowRateAllowanceWithPermissions
-> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
  -> library FlowOperatorDefinitions.isPermissionsClean
  -> library AgreementLibrary.authorizeTokenAccess
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> public addPermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData


### public isPatricianPeriod
-> library SolvencyHelperLibrary.decode3PsData
-> private _getAccountFlowState
  -> internal _decodeFlowData
-> library SolvencyHelperLibrary.isPatricianPeriod


### external isPatricianPeriodNow
-> public isPatricianPeriod
  -> library SolvencyHelperLibrary.decode3PsData
  -> private _getAccountFlowState
    -> internal _decodeFlowData
  -> library SolvencyHelperLibrary.isPatricianPeriod


### external realtimeBalanceOf
-> private _getAccountFlowState
  -> internal _decodeFlowData


### public removePermissions
_(no internal calls)_


### external revokeFlowOperatorWithFullControl
-> public updateFlowOperatorPermissions
  -> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
    -> library FlowOperatorDefinitions.isPermissionsClean
    -> library AgreementLibrary.authorizeTokenAccess
  -> private _generateFlowOperatorId
  -> internal _encodeFlowOperatorData


### external updateFlow
-> library AgreementLibrary.authorizeTokenAccess
-> private _generateFlowId
-> private _getAgreementData
  -> internal _decodeFlowData
-> internal _updateFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### external updateFlowByOperator
-> library AgreementLibrary.authorizeTokenAccess
-> private _getAgreementData
  -> internal _decodeFlowData
-> private _generateFlowId
-> public getFlowOperatorData
  -> private _generateFlowOperatorId
  -> private _getFlowOperatorData
    -> internal _decodeFlowOperatorData
-> internal _getBooleanFlowOperatorPermissions
-> private _updateFlowOperatorData
  -> internal _encodeFlowOperatorData
-> internal _updateFlow
  -> internal _createOrUpdateFlowCheck
    -> private _generateFlowId
  -> private _changeFlowToApp
    -> library AgreementLibrary.createCallbackInputs
    -> library AgreementLibrary.callAppBeforeCallback
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
    -> library AgreementLibrary.max
    -> library AgreementLibrary.callAppAfterCallback
    -> private _getAgreementData
      -> internal _decodeFlowData
    -> internal _encodeFlowData
    -> private _updateAccountFlowState
      -> private _getAccountFlowState
        -> internal _decodeFlowData
      -> internal _encodeFlowData
    -> library AgreementLibrary.min
    -> external_callback ISuperfluid.APP_RULE
  -> private _changeFlowToNonApp
    -> private _changeFlow
      -> library SolvencyHelperLibrary.decode3PsData
      -> internal _calculateDeposit
        -> internal _clipDepositNumberRoundingUp
      -> internal _encodeFlowData
      -> private _updateAccountFlowState
        -> private _getAccountFlowState
          -> internal _decodeFlowData
        -> internal _encodeFlowData
  -> private _requireAvailableBalance


### public updateFlowOperatorPermissions
-> internal _validateAndAuthorizeUpdateFlowOperatorDataInput
  -> library FlowOperatorDefinitions.isPermissionsClean
  -> library AgreementLibrary.authorizeTokenAccess
-> private _generateFlowOperatorId
-> internal _encodeFlowOperatorData


---

## ERC1820Implementer

_File: packages/ethereum-contracts/contracts/utils/ERC1820Implementer.sol_

### public canImplementInterfaceForAddress
_(no internal calls)_


---

## ERC2771Forwarder

_File: packages/ethereum-contracts/contracts/utils/ERC2771Forwarder.sol_

### external forward2771Call
_(no internal calls)_


### external withdrawLostNativeTokens
_(no internal calls)_


---

## ERC4626YieldBackend

_File: packages/ethereum-contracts/contracts/superfluid/ERC4626YieldBackend.sol_

### external deposit
_(no internal calls)_


### external disable
_(no internal calls)_


### external enable
_(no internal calls)_


### external withdraw
_(no internal calls)_


### external withdrawMax
_(no internal calls)_


### external withdrawSurplus
_(no internal calls)_


---

## FlowScheduler

_File: packages/automation-contracts/scheduler/contracts/FlowScheduler.sol_

### external afterAgreementCreated
_(no internal calls)_


### external afterAgreementTerminated
_(no internal calls)_


### external afterAgreementUpdated
_(no internal calls)_


### external beforeAgreementCreated
_(no internal calls)_


### external beforeAgreementTerminated
_(no internal calls)_


### external beforeAgreementUpdated
_(no internal calls)_


### external createFlowSchedule
-> internal _getSender


### external deleteFlowSchedule
-> internal _getSender


### external executeCreateFlow
_(no internal calls)_


### external executeDeleteFlow
_(no internal calls)_


### external getFlowSchedule
_(no internal calls)_


---

## FlowSchedulerResolver

_File: packages/automation-contracts/scheduler/contracts/FlowSchedulerResolver.sol_

### external checker
_(no internal calls)_


---

## FullUpgradableSuperTokenProxy

_File: packages/ethereum-contracts/contracts/superfluid/FullUpgradableSuperTokenProxy.sol_

### external initialize
_(no internal calls)_


---

## GDAHotFuzzMixin

_File: packages/hot-fuzz/contracts/superfluid-tests/GeneralDistributionAgreementV1.hott.sol_

### public claimAll
-> internal _getOneTester
  -> internal _numAccounts
-> public getRandomPool


### public claimAllForMember
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> public getRandomPool


### public createPool
-> internal _getOneTester
  -> internal _numAccounts
-> internal _addPool
  -> internal _addAccount


### public distribute
-> internal _getOneTester
  -> internal _numAccounts
-> public getRandomPool


### public distributeFlow
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> public getRandomPool


### public echidna_check_liquiditySumInvariance
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_netFlowRateSumInvariant
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_total_supply
_(no internal calls)_


### public echidna_check_validLiquidationNeverRevertsInvariant
_(no internal calls)_


### public gdaLiquidateFlow
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> public getRandomPool


### public getRandomPool
_(no internal calls)_


### public maybeConnectPool
-> internal _getOneTester
  -> internal _numAccounts
-> public getRandomPool


### public poolApprove
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> public getRandomPool


### public poolDecreaseAllowance
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> public getRandomPool


### public poolIncreaseAllowance
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> public getRandomPool


### public poolTransfer
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> public getRandomPool


### public poolTransferFrom
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> internal _getOneTester
  -> internal _numAccounts
-> public getRandomPool


### public updateMemberUnits
-> internal _getOneTester
  -> internal _numAccounts
-> public getRandomPool


---

## GDAv1Forwarder

_File: packages/ethereum-contracts/contracts/utils/GDAv1Forwarder.sol_

### external claimAll
-> internal _forwardBatchCall
  -> internal _forwardBatchCallWithValue
    -> library CallUtils.revertFromReturnedData


### external connectPool
-> internal _forwardBatchCall
  -> internal _forwardBatchCallWithValue
    -> library CallUtils.revertFromReturnedData


### external createPool
_(no internal calls)_


### external disconnectPool
-> internal _forwardBatchCall
  -> internal _forwardBatchCallWithValue
    -> library CallUtils.revertFromReturnedData


### external distribute
-> internal _forwardBatchCall
  -> internal _forwardBatchCallWithValue
    -> library CallUtils.revertFromReturnedData


### external distributeFlow
-> internal _forwardBatchCall
  -> internal _forwardBatchCallWithValue
    -> library CallUtils.revertFromReturnedData


### external estimateDistributionActualAmount
_(no internal calls)_


### external estimateFlowDistributionActualFlowRate
_(no internal calls)_


### external getFlowDistributionFlowRate
_(no internal calls)_


### external getNetFlow
_(no internal calls)_


### external getPoolAdjustmentFlowInfo
_(no internal calls)_


### external getPoolAdjustmentFlowRate
_(no internal calls)_


### external isMemberConnected
_(no internal calls)_


### external isPool
_(no internal calls)_


### external updateMemberUnits
-> internal _forwardBatchCall
  -> internal _forwardBatchCallWithValue
    -> library CallUtils.revertFromReturnedData


---

## GeneralDistributionAgreementV1

_File: packages/ethereum-contracts/contracts/agreements/gdav1/GeneralDistributionAgreementV1.sol_

### external agreementType
_(no internal calls)_


### external appendIndexUpdateByPool
-> internal _setUIndex
-> internal _getUIndex
  -> library GDAv1StorageLib.getUniversalIndexFromAccountData
-> internal _setPoolAdjustmentFlowRate
  -> internal _setPoolAdjustmentFlowRate


### external claimAll
-> library AgreementLibrary.authorizeTokenAccess


### external connectPool
-> internal _setPoolConnectionFor
  -> library AgreementLibrary.authorizeTokenAccess
  -> library SlotsBitmapLibrary.countUsedSlots
  -> private _findAndFillPoolConnectionsBitmap
    -> library SlotsBitmapLibrary.findEmptySlotAndFill
  -> library GDAv1StorageLib.PoolConnectivity
  -> private _clearPoolConnectionsBitmap
    -> library SlotsBitmapLibrary.clearSlot


### external createPool
-> internal _createPool
  -> library SuperfluidPoolDeployerLibrary.deploy
  -> library SuperfluidPoolDeployerLibrary.mintPoolAdminNFT


### external createPoolWithCustomERC20Metadata
-> internal _createPool
  -> library SuperfluidPoolDeployerLibrary.deploy
  -> library SuperfluidPoolDeployerLibrary.mintPoolAdminNFT


### external disconnectPool
-> internal _setPoolConnectionFor
  -> library AgreementLibrary.authorizeTokenAccess
  -> library SlotsBitmapLibrary.countUsedSlots
  -> private _findAndFillPoolConnectionsBitmap
    -> library SlotsBitmapLibrary.findEmptySlotAndFill
  -> library GDAv1StorageLib.PoolConnectivity
  -> private _clearPoolConnectionsBitmap
    -> library SlotsBitmapLibrary.clearSlot


### external distribute
-> library AgreementLibrary.authorizeTokenAccess
-> internal _doDistributeViaPool
  -> internal _getUIndex
    -> library GDAv1StorageLib.getUniversalIndexFromAccountData
  -> internal _getPDPIndex
  -> internal _setUIndex
  -> internal _setPDPIndex


### external distributeFlow
-> library AgreementLibrary.authorizeTokenAccess
-> library GDAv1StorageLib.getFlowDistributionHash
-> internal _getFlowRate
-> internal _doDistributeFlowViaPool
  -> internal _getUIndex
    -> library GDAv1StorageLib.getUniversalIndexFromAccountData
  -> internal _getPDPIndex
  -> internal _getPoolAdjustmentFlowRate
    -> internal _getPoolAdjustmentFlowInfo
      -> library GDAv1StorageLib.getPoolAdjustmentFlowHash
      -> internal _getFlowRate
  -> internal _getFlowRate
  -> internal _setUIndex
  -> internal _setPDPIndex
  -> internal _setFlowInfo
    -> library GDAv1StorageLib.FlowInfo
  -> internal _setPoolAdjustmentFlowRate
    -> internal _setPoolAdjustmentFlowRate
-> internal _makeLiquidationPayouts
  -> library SolvencyHelperLibrary.decode3PsData
  -> library SolvencyHelperLibrary.isPatricianPeriod
    -> library SolvencyHelperLibrary.decode3PsData
    -> library SolvencyHelperLibrary.isPatricianPeriod
-> internal _adjustBuffer
  -> library SolvencyHelperLibrary.decode3PsData
  -> library GDAv1StorageLib.FlowInfo
-> internal _getPoolAdjustmentFlowInfo
  -> library GDAv1StorageLib.getPoolAdjustmentFlowHash
  -> internal _getFlowRate


### external estimateDistributionActualAmount
-> internal _getUIndex
  -> library GDAv1StorageLib.getUniversalIndexFromAccountData
-> internal _getPDPIndex


### external estimateFlowDistributionActualFlowRate
-> library GDAv1StorageLib.getFlowDistributionHash
-> internal _getUIndex
  -> library GDAv1StorageLib.getUniversalIndexFromAccountData
-> internal _getPDPIndex
-> internal _getFlowRate
-> internal _getPoolAdjustmentFlowRate
  -> internal _getPoolAdjustmentFlowInfo
    -> library GDAv1StorageLib.getPoolAdjustmentFlowHash
    -> internal _getFlowRate


### external getAccountFlowInfo
_(no internal calls)_


### external getFlow
_(no internal calls)_


### external getFlowRate
_(no internal calls)_


### external getNetFlow
-> internal _getUIndex
  -> library GDAv1StorageLib.getUniversalIndexFromAccountData
-> private _listPoolConnectionIds
  -> library SlotsBitmapLibrary.listData


### external getPoolAdjustmentFlowInfo
-> internal _getPoolAdjustmentFlowInfo
  -> library GDAv1StorageLib.getPoolAdjustmentFlowHash
  -> internal _getFlowRate


### external getPoolAdjustmentFlowRate
-> internal _getPoolAdjustmentFlowRate
  -> internal _getPoolAdjustmentFlowInfo
    -> library GDAv1StorageLib.getPoolAdjustmentFlowHash
    -> internal _getFlowRate


### external isMemberConnected
_(no internal calls)_


### public isPatricianPeriod
-> library SolvencyHelperLibrary.decode3PsData
-> library SolvencyHelperLibrary.isPatricianPeriod


### external isPatricianPeriodNow
-> public isPatricianPeriod
  -> library SolvencyHelperLibrary.decode3PsData
  -> library SolvencyHelperLibrary.isPatricianPeriod


### external isPool
_(no internal calls)_


### external poolSettleClaim
-> internal _doShift
  -> internal _getUIndex
    -> library GDAv1StorageLib.getUniversalIndexFromAccountData
  -> internal _setUIndex


### public proxiableUUID
_(no internal calls)_


### public realtimeBalanceOf
-> private _listPoolConnectionIds
  -> library SlotsBitmapLibrary.listData
-> internal _assertPoolConnectivity


### external realtimeBalanceOfNow
-> public realtimeBalanceOf
  -> private _listPoolConnectionIds
    -> library SlotsBitmapLibrary.listData
  -> internal _assertPoolConnectivity


### external setConnectPermission
_(no internal calls)_


### external tryConnectPoolFor
-> internal _setPoolConnectionFor
  -> library AgreementLibrary.authorizeTokenAccess
  -> library SlotsBitmapLibrary.countUsedSlots
  -> private _findAndFillPoolConnectionsBitmap
    -> library SlotsBitmapLibrary.findEmptySlotAndFill
  -> library GDAv1StorageLib.PoolConnectivity
  -> private _clearPoolConnectionsBitmap
    -> library SlotsBitmapLibrary.clearSlot


### external updateCode
_(no internal calls)_


### external updateMemberUnits
-> library AgreementLibrary.authorizeTokenAccess


---

## HotFuzzBase

_File: packages/hot-fuzz/contracts/HotFuzzBase.sol_

### public echidna_check_liquiditySumInvariance
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_netFlowRateSumInvariant
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_total_supply
_(no internal calls)_


### public echidna_check_validLiquidationNeverRevertsInvariant
_(no internal calls)_


---

## IConstantFlowAgreementV1

_File: packages/ethereum-contracts/contracts/interfaces/agreements/IConstantFlowAgreementV1.sol_

### external agreementType
_(no internal calls)_


---

## IGeneralDistributionAgreementV1

_File: packages/ethereum-contracts/contracts/interfaces/agreements/gdav1/IGeneralDistributionAgreementV1.sol_

### external agreementType
_(no internal calls)_


---

## IInstantDistributionAgreementV1

_File: packages/ethereum-contracts/contracts/interfaces/agreements/IInstantDistributionAgreementV1.sol_

### external agreementType
_(no internal calls)_


---

## InstantDistributionAgreementV1

_File: packages/ethereum-contracts/contracts/agreements/InstantDistributionAgreementV1.sol_

### external agreementType
_(no internal calls)_


### external approveSubscription
-> library AgreementLibrary.authorizeTokenAccess
-> private _loadAllData
  -> private _getPublisherId
  -> private _getSubscriptionId
  -> private _getIndexData
  -> private _getSubscriptionData
-> library AgreementLibrary.createCallbackInputs
-> library AgreementLibrary.callAppBeforeCallback
-> private _findAndFillSubsBitmap
  -> library SlotsBitmapLibrary.findEmptySlotAndFill
-> private _encodeSubscriptionData
-> library AgreementLibrary.callAppAfterCallback
-> private _encodeIndexData
-> private _adjustPublisherDeposit


### external calculateDistribution
-> private _getPublisherId
-> private _getIndexData


### external claim
-> library AgreementLibrary.authorizeTokenAccess
-> private _loadAllData
  -> private _getPublisherId
  -> private _getSubscriptionId
  -> private _getIndexData
  -> private _getSubscriptionData
-> library AgreementLibrary.createCallbackInputs
-> library AgreementLibrary.callAppBeforeCallback
-> private _adjustPublisherDeposit
-> private _encodeSubscriptionData
-> library AgreementLibrary.callAppAfterCallback


### external createIndex
-> library AgreementLibrary.authorizeTokenAccess
-> private _getPublisherId
-> private _hasIndexData
-> private _encodeIndexData


### external deleteSubscription
-> library AgreementLibrary.authorizeTokenAccess
-> private _loadAllData
  -> private _getPublisherId
  -> private _getSubscriptionId
  -> private _getIndexData
  -> private _getSubscriptionData
-> library AgreementLibrary.createCallbackInputs
-> library AgreementLibrary.callAppBeforeCallback
-> private _encodeIndexData
-> private _clearSubsBitmap
  -> library SlotsBitmapLibrary.clearSlot
-> private _adjustPublisherDeposit
-> library AgreementLibrary.callAppAfterCallback


### external distribute
-> library AgreementLibrary.authorizeTokenAccess
-> private _loadIndexData
  -> private _getPublisherId
  -> private _getIndexData
-> private _updateIndex
  -> private _adjustPublisherDeposit
  -> private _encodeIndexData


### external getIndex
-> private _getPublisherId
-> private _getIndexData


### external getSubscription
-> private _loadAllData
  -> private _getPublisherId
  -> private _getSubscriptionId
  -> private _getIndexData
  -> private _getSubscriptionData


### external getSubscriptionByID
-> private _getSubscriptionData
-> private _getPublisherId
-> private _getIndexData


### external listSubscriptions
-> private _listSubscriptionIds
  -> library SlotsBitmapLibrary.listData
  -> private _getSubscriptionId
-> private _getSubscriptionData


### public proxiableUUID
_(no internal calls)_


### external realtimeBalanceOf
-> private _listSubscriptionIds
  -> library SlotsBitmapLibrary.listData
  -> private _getSubscriptionId
-> private _getSubscriptionData
-> private _getIndexData
-> private _getPublisherDeposit


### external revokeSubscription
-> library AgreementLibrary.authorizeTokenAccess
-> private _loadAllData
  -> private _getPublisherId
  -> private _getSubscriptionId
  -> private _getIndexData
  -> private _getSubscriptionData
-> library AgreementLibrary.createCallbackInputs
-> library AgreementLibrary.callAppBeforeCallback
-> private _encodeIndexData
-> private _clearSubsBitmap
  -> library SlotsBitmapLibrary.clearSlot
-> private _encodeSubscriptionData
-> library AgreementLibrary.callAppAfterCallback


### external updateCode
_(no internal calls)_


### external updateIndex
-> library AgreementLibrary.authorizeTokenAccess
-> private _loadIndexData
  -> private _getPublisherId
  -> private _getIndexData
-> private _updateIndex
  -> private _adjustPublisherDeposit
  -> private _encodeIndexData


### external updateSubscription
-> library AgreementLibrary.authorizeTokenAccess
-> private _loadAllData
  -> private _getPublisherId
  -> private _getSubscriptionId
  -> private _getIndexData
  -> private _getSubscriptionData
-> library AgreementLibrary.createCallbackInputs
-> library AgreementLibrary.callAppBeforeCallback
-> private _encodeIndexData
-> private _encodeSubscriptionData
-> private _adjustPublisherDeposit
-> library AgreementLibrary.callAppAfterCallback


---

## MacroForwarder

_File: packages/ethereum-contracts/contracts/utils/MacroForwarder.sol_

### public buildBatchOperations
_(no internal calls)_


### external runMacro
-> public buildBatchOperations
-> internal _forwardBatchCallWithValue
  -> library CallUtils.revertFromReturnedData


---

## Manager

_File: packages/automation-contracts/autowrap/contracts/Manager.sol_

### external addApprovedStrategy
_(no internal calls)_


### external checkWrap
-> public checkWrapByIndex
-> public getWrapScheduleIndex


### public checkWrapByIndex
_(no internal calls)_


### external createWrapSchedule
-> public getWrapScheduleIndex


### external deleteWrapSchedule
-> public deleteWrapScheduleByIndex
-> public getWrapScheduleIndex


### public deleteWrapScheduleByIndex
_(no internal calls)_


### external executeWrap
-> public executeWrapByIndex
  -> public checkWrapByIndex
-> public getWrapScheduleIndex


### public executeWrapByIndex
-> public checkWrapByIndex


### external getWrapSchedule
-> public getWrapScheduleByIndex
-> public getWrapScheduleIndex


### public getWrapScheduleByIndex
_(no internal calls)_


### public getWrapScheduleIndex
_(no internal calls)_


### external removeApprovedStrategy
_(no internal calls)_


### external setLimits
_(no internal calls)_


---

## NoGetUnderlyingToken

_File: packages/sdk-core/contracts/NoGetUnderlyingToken.sol_

### public symbol
_(no internal calls)_


---

## PoolAdminNFT

_File: packages/ethereum-contracts/contracts/agreements/gdav1/PoolAdminNFT.sol_

### public approve
-> external_callback PoolNFTBase.ownerOf
  -> internal _ownerOf
-> public isApprovedForAll
-> internal _approve
  -> internal _ownerOf


### external balanceOf
_(no internal calls)_


### public baseURI
_(no internal calls)_


### public getApproved
-> internal _requireMinted
  -> internal _exists
    -> internal _ownerOf


### external getTokenId
-> internal _getTokenId


### external initialize
_(no internal calls)_


### public isApprovedForAll
_(no internal calls)_


### external mint
-> internal _mint
  -> internal _getTokenId
  -> internal _exists
    -> internal _ownerOf


### external name
_(no internal calls)_


### public ownerOf
-> internal _ownerOf


### external poolAdminDataByTokenId
_(no internal calls)_


### public proxiableUUID
_(no internal calls)_


### public safeTransferFrom
-> internal _isApprovedOrOwner
  -> external_callback PoolNFTBase.ownerOf
    -> internal _ownerOf
  -> public isApprovedForAll
  -> public getApproved
    -> internal _requireMinted
      -> internal _exists
        -> internal _ownerOf
-> internal _safeTransfer
  -> internal _transfer


### external setApprovalForAll
-> internal _setApprovalForAll


### external supportsInterface
_(no internal calls)_


### external symbol
_(no internal calls)_


### external tokenURI
_(no internal calls)_


### external transferFrom
-> internal _isApprovedOrOwner
  -> external_callback PoolNFTBase.ownerOf
    -> internal _ownerOf
  -> public isApprovedForAll
  -> public getApproved
    -> internal _requireMinted
      -> internal _exists
        -> internal _ownerOf
-> internal _transfer


### external triggerMetadataUpdate
-> internal _triggerMetadataUpdate


### external updateCode
-> external_callback UUPSProxiable._updateCodeAddress


---

## PoolNFTBase

_File: packages/ethereum-contracts/contracts/agreements/gdav1/PoolNFTBase.sol_

### public approve
-> external_callback PoolNFTBase.ownerOf
-> public isApprovedForAll
-> internal _approve


### external balanceOf
_(no internal calls)_


### public baseURI
_(no internal calls)_


### external castrate
_(no internal calls)_


### public getApproved
-> internal _requireMinted
  -> internal _exists


### public getCodeAddress
-> library UUPSUtils.implementation


### external initialize
_(no internal calls)_


### public isApprovedForAll
_(no internal calls)_


### external name
_(no internal calls)_


### public ownerOf
_(no internal calls)_


### public safeTransferFrom
-> internal _isApprovedOrOwner
  -> external_callback PoolNFTBase.ownerOf
  -> public isApprovedForAll
  -> public getApproved
    -> internal _requireMinted
      -> internal _exists
-> internal _safeTransfer


### external setApprovalForAll
-> internal _setApprovalForAll


### external supportsInterface
_(no internal calls)_


### external symbol
_(no internal calls)_


### external transferFrom
-> internal _isApprovedOrOwner
  -> external_callback PoolNFTBase.ownerOf
  -> public isApprovedForAll
  -> public getApproved
    -> internal _requireMinted
      -> internal _exists


### external triggerMetadataUpdate
-> internal _triggerMetadataUpdate


### external updateCode
-> external_callback UUPSProxiable._updateCodeAddress
  -> library UUPSUtils.implementation
  -> library UUPSUtils.setImplementation


---

## PureSuperToken

_File: packages/ethereum-contracts/contracts/tokens/PureSuperToken.sol_

### external initialize
_(no internal calls)_


### external initializeProxy
-> library UUPSUtils.implementation
-> library UUPSUtils.setImplementation


---

## Resolver

_File: packages/ethereum-contracts/contracts/utils/Resolver.sol_

### external get
_(no internal calls)_


### external set
_(no internal calls)_


---

## SETHProxy

_File: packages/ethereum-contracts/contracts/tokens/SETH.sol_

### external downgradeToETH
_(no internal calls)_


### external initializeProxy
-> library UUPSUtils.implementation
-> library UUPSUtils.setImplementation


### external upgradeByETH
_(no internal calls)_


### external upgradeByETHTo
_(no internal calls)_


---

## SimpleACL

_File: packages/ethereum-contracts/contracts/utils/SimpleACL.sol_

### external setRoleAdmin
_(no internal calls)_


---

## SimpleForwarder

_File: packages/ethereum-contracts/contracts/utils/SimpleForwarder.sol_

### external forwardCall
_(no internal calls)_


### external withdrawLostNativeTokens
_(no internal calls)_


---

## StrategyBase

_File: packages/automation-contracts/autowrap/contracts/strategies/StrategyBase.sol_

### external changeManager
_(no internal calls)_


### external emergencyWithdraw
_(no internal calls)_


---

## SuperAppBase

_File: packages/ethereum-contracts/contracts/apps/SuperAppBase.sol_

### external afterAgreementCreated
_(no internal calls)_


### external afterAgreementTerminated
_(no internal calls)_


### external afterAgreementUpdated
_(no internal calls)_


### external beforeAgreementCreated
_(no internal calls)_


### external beforeAgreementTerminated
_(no internal calls)_


### external beforeAgreementUpdated
_(no internal calls)_


---

## SuperAppTester

_File: packages/sdk-core/contracts/SuperAppTester.sol_

### external afterAgreementCreated
_(no internal calls)_


### external afterAgreementTerminated
_(no internal calls)_


### external afterAgreementUpdated
_(no internal calls)_


### external beforeAgreementCreated
_(no internal calls)_


### external beforeAgreementTerminated
_(no internal calls)_


### external beforeAgreementUpdated
_(no internal calls)_


### external setVal
_(no internal calls)_


---

## SuperToken

_File: packages/ethereum-contracts/contracts/superfluid/SuperToken.sol_

### public DOMAIN_SEPARATOR
_(no internal calls)_


### public allowance
_(no internal calls)_


### public approve
-> internal _approve


### external authorizeOperator
_(no internal calls)_


### public balanceOf
_(no internal calls)_


### external burn
-> internal _downgrade
  -> private _toUnderlyingAmount
  -> internal _burn
    -> private _callTokensToSend
    -> external_callback SuperfluidToken._burn


### external castrate
_(no internal calls)_


### external changeAdmin
-> internal _getAdmin
-> internal _setAdmin


### external createAgreement
-> library FixedSizeData.hasData
-> library FixedSizeData.storeData


### external decimals
_(no internal calls)_


### public decreaseAllowance
-> internal _approve


### external defaultOperators
-> library ERC777Helper.defaultOperators


### external disableYieldBackend
_(no internal calls)_


### external downgrade
-> internal _downgrade
  -> private _toUnderlyingAmount
  -> internal _burn
    -> private _callTokensToSend
    -> external_callback SuperfluidToken._burn


### external downgradeTo
-> internal _downgrade
  -> private _toUnderlyingAmount
  -> internal _burn
    -> private _callTokensToSend
    -> external_callback SuperfluidToken._burn


### public eip712Domain
_(no internal calls)_


### external enableYieldBackend
_(no internal calls)_


### public getAccountActiveAgreements
_(no internal calls)_


### external getAdmin
-> internal _getAdmin


### external getAgreementData
-> library FixedSizeData.loadData


### external getAgreementStateSlot
-> library FixedSizeData.loadData


### public getCodeAddress
-> library UUPSUtils.implementation


### external getHost
_(no internal calls)_


### external getUnderlyingDecimals
_(no internal calls)_


### external getUnderlyingToken
_(no internal calls)_


### external getYieldBackend
_(no internal calls)_


### external granularity
_(no internal calls)_


### public increaseAllowance
-> internal _approve


### external initialize
-> internal _initialize
  -> internal _setAdmin
  -> library ERC777Helper.register


### external initializeWithAdmin
-> internal _initialize
  -> internal _setAdmin
  -> library ERC777Helper.register


### public isAccountCritical
-> public realtimeBalanceOf
  -> public getAccountActiveAgreements


### external isAccountCriticalNow
-> public isAccountCritical
  -> public realtimeBalanceOf
    -> public getAccountActiveAgreements


### public isAccountSolvent
-> public realtimeBalanceOf
  -> public getAccountActiveAgreements


### external isAccountSolventNow
-> public isAccountSolvent
  -> public realtimeBalanceOf
    -> public getAccountActiveAgreements


### external isOperatorFor
_(no internal calls)_


### external makeLiquidationPayoutsV2
-> internal _getRewardAccount
-> external_callback IERC20.Transfer


### external name
_(no internal calls)_


### public nonces
_(no internal calls)_


### external operationApprove
-> internal _approve


### external operationDecreaseAllowance
-> internal _approve


### external operationDowngrade
-> internal _downgrade
  -> private _toUnderlyingAmount
  -> internal _burn
    -> private _callTokensToSend
    -> external_callback SuperfluidToken._burn


### external operationDowngradeTo
-> internal _downgrade
  -> private _toUnderlyingAmount
  -> internal _burn
    -> private _callTokensToSend
    -> external_callback SuperfluidToken._burn


### external operationIncreaseAllowance
-> internal _approve


### external operationSend
-> internal _send
  -> private _callTokensToSend
  -> private _move
    -> external_callback SuperfluidToken._move
  -> private _callTokensReceived


### external operationTransferFrom
-> internal _transferFrom
  -> private _move
    -> external_callback SuperfluidToken._move
  -> internal _approve


### external operationUpgrade
-> internal _upgrade
  -> private _toUnderlyingAmount
  -> internal _mint
    -> external_callback SuperfluidToken._mint
    -> private _callTokensReceived


### external operationUpgradeTo
-> internal _upgrade
  -> private _toUnderlyingAmount
  -> internal _mint
    -> external_callback SuperfluidToken._mint
    -> private _callTokensReceived


### external operatorBurn
-> internal _downgrade
  -> private _toUnderlyingAmount
  -> internal _burn
    -> private _callTokensToSend
    -> external_callback SuperfluidToken._burn


### external operatorSend
-> internal _send
  -> private _callTokensToSend
  -> private _move
    -> external_callback SuperfluidToken._move
  -> private _callTokensReceived


### public permit
-> public DOMAIN_SEPARATOR
-> internal _approve


### public proxiableUUID
_(no internal calls)_


### public realtimeBalanceOf
-> public getAccountActiveAgreements


### public realtimeBalanceOfNow
-> public realtimeBalanceOf
  -> public getAccountActiveAgreements


### external revokeOperator
_(no internal calls)_


### external selfApproveFor
-> internal _approve


### external selfBurn
-> internal _burn
  -> private _callTokensToSend
  -> external_callback SuperfluidToken._burn


### external selfMint
-> internal _mint
  -> external_callback SuperfluidToken._mint
  -> private _callTokensReceived


### external selfTransferFrom
-> internal _transferFrom
  -> private _move
    -> external_callback SuperfluidToken._move
  -> internal _approve


### external send
-> internal _send
  -> private _callTokensToSend
  -> private _move
    -> external_callback SuperfluidToken._move
  -> private _callTokensReceived


### external settleBalance
_(no internal calls)_


### external symbol
_(no internal calls)_


### external terminateAgreement
-> library FixedSizeData.hasData
-> library FixedSizeData.eraseData


### external toUnderlyingAmount
-> private _toUnderlyingAmount


### public totalSupply
_(no internal calls)_


### public transfer
-> internal _transferFrom
  -> private _move
    -> external_callback SuperfluidToken._move
  -> internal _approve


### external transferAll
-> internal _transferFrom
  -> private _move
    -> external_callback SuperfluidToken._move
  -> internal _approve
-> public balanceOf


### public transferFrom
-> internal _transferFrom
  -> private _move
    -> external_callback SuperfluidToken._move
  -> internal _approve


### external updateAgreementData
-> library FixedSizeData.storeData


### external updateAgreementStateSlot
-> library FixedSizeData.storeData


### external updateCode
-> external_callback UUPSProxiable._updateCodeAddress
  -> library UUPSUtils.implementation
  -> public proxiableUUID
  -> library UUPSUtils.setImplementation


### external upgrade
-> internal _upgrade
  -> private _toUnderlyingAmount
  -> internal _mint
    -> external_callback SuperfluidToken._mint
    -> private _callTokensReceived


### external upgradeTo
-> internal _upgrade
  -> private _toUnderlyingAmount
  -> internal _mint
    -> external_callback SuperfluidToken._mint
    -> private _callTokensReceived


### external withdrawSurplusFromYieldBackend
_(no internal calls)_


---

## SuperTokenFactory

_File: packages/ethereum-contracts/contracts/superfluid/SuperTokenFactory.sol_

### external computeCanonicalERC20WrapperAddress
_(no internal calls)_


### external createCanonicalERC20Wrapper
_(no internal calls)_


### external createERC20Wrapper
-> external createERC20Wrapper


### external getCanonicalERC20Wrapper
_(no internal calls)_


### external getHost
_(no internal calls)_


### external getSuperTokenLogic
_(no internal calls)_


### external initialize
_(no internal calls)_


### external initializeCanonicalWrapperSuperTokens
_(no internal calls)_


### external initializeCustomSuperToken
_(no internal calls)_


### public proxiableUUID
_(no internal calls)_


### external updateCode
_(no internal calls)_


---

## SuperTokenFactoryBase

_File: packages/ethereum-contracts/contracts/superfluid/SuperTokenFactory.sol_

### external castrate
_(no internal calls)_


### external computeCanonicalERC20WrapperAddress
_(no internal calls)_


### external createCanonicalERC20Wrapper
_(no internal calls)_


### external createERC20Wrapper
-> external createERC20Wrapper


### external getCanonicalERC20Wrapper
_(no internal calls)_


### public getCodeAddress
-> library UUPSUtils.implementation


### external getHost
_(no internal calls)_


### external getSuperTokenLogic
_(no internal calls)_


### external initialize
_(no internal calls)_


### external initializeCanonicalWrapperSuperTokens
_(no internal calls)_


### external initializeCustomSuperToken
_(no internal calls)_


### public proxiableUUID
_(no internal calls)_


### external updateCode
-> internal _updateCodeAddress
  -> library UUPSUtils.implementation
  -> public proxiableUUID
  -> library UUPSUtils.setImplementation


---

## SuperTokenHotFuzz

_File: packages/hot-fuzz/contracts/superfluid-tests/SuperToken.hott.sol_

### public approve
_(no internal calls)_


### public decreaseAllowance
_(no internal calls)_


### public downgrade
_(no internal calls)_


### public increaseAllowance
_(no internal calls)_


### public transfer
_(no internal calls)_


### public transferAll
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### public upgrade
_(no internal calls)_


---

## SuperTokenHotFuzzMixin

_File: packages/hot-fuzz/contracts/superfluid-tests/SuperToken.hott.sol_

### public approve
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public decreaseAllowance
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public downgrade
-> internal _getOneTester
  -> internal _numAccounts
-> internal _superTokenBalanceOfNow


### public echidna_check_liquiditySumInvariance
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_netFlowRateSumInvariant
-> internal _listAccounts
  -> internal _numAccounts


### public echidna_check_total_supply
_(no internal calls)_


### public echidna_check_validLiquidationNeverRevertsInvariant
_(no internal calls)_


### public increaseAllowance
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public transfer
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public transferAll
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts


### public transferFrom
-> internal _getTwoTesters
  -> internal _getOneTester
    -> internal _numAccounts
-> internal _getOneTester
  -> internal _numAccounts


### public upgrade
-> internal _getOneTester
  -> internal _numAccounts
-> internal _superTokenBalanceOfNow


---

## SuperUpgrader

_File: packages/ethereum-contracts/contracts/utils/SuperUpgrader.sol_

### external getBackendAgents
_(no internal calls)_


### external grantBackendAgent
_(no internal calls)_


### external isBackendAgent
_(no internal calls)_


### external optinAutoUpgrades
_(no internal calls)_


### external optoutAutoUpgrades
_(no internal calls)_


### external revokeBackendAgent
_(no internal calls)_


### external upgrade
_(no internal calls)_


---

## Superfluid

_File: packages/ethereum-contracts/contracts/superfluid/Superfluid.sol_

### external addToAgreementClassesBitmap
_(no internal calls)_


### external allowCompositeApp
-> public isApp
-> public getAppCallbackLevel
  -> library SuperAppDefinitions.getAppCallbackLevel


### external appCallbackPop
-> public decodeCtx
  -> private _decodeCtx
    -> library ContextDefinitions.decodeCallInfo
-> private _updateContext
  -> library ContextDefinitions.encodeCallInfo


### external appCallbackPush
-> public decodeCtx
  -> private _decodeCtx
    -> library ContextDefinitions.decodeCallInfo
-> public isApp
-> private _updateContext
  -> library ContextDefinitions.encodeCallInfo


### external batchCall
-> internal _batchCall
  -> internal _callAgreement
    -> library CallUtils.parseSelector
    -> private _updateContext
      -> library ContextDefinitions.encodeCallInfo
    -> public getNow
    -> private _callExternalWithReplacedCtx
      -> internal _replacePlaceholderCtx
        -> library CallUtils.padLength32
    -> library CallUtils.revertFromReturnedData
  -> internal _callAppAction
    -> private _updateContext
      -> library ContextDefinitions.encodeCallInfo
    -> public getNow
    -> private _callExternalWithReplacedCtx
      -> internal _replacePlaceholderCtx
        -> library CallUtils.padLength32
    -> private _isCtxValid
    -> library CallUtils.revertFromReturnedData
  -> library CallUtils.revertFromReturnedData


### external callAgreement
-> internal _callAgreement
  -> library CallUtils.parseSelector
  -> private _updateContext
    -> library ContextDefinitions.encodeCallInfo
  -> public getNow
  -> private _callExternalWithReplacedCtx
    -> internal _replacePlaceholderCtx
      -> library CallUtils.padLength32
  -> library CallUtils.revertFromReturnedData


### external callAgreementWithContext
-> public decodeCtx
  -> private _decodeCtx
    -> library ContextDefinitions.decodeCallInfo
-> private _updateContext
  -> library ContextDefinitions.encodeCallInfo
-> private _callExternalWithReplacedCtx
  -> internal _replacePlaceholderCtx
    -> library CallUtils.padLength32
-> private _isCtxValid
-> library CallUtils.revertFromReturnedData


### external callAppAction
-> internal _callAppAction
  -> private _updateContext
    -> library ContextDefinitions.encodeCallInfo
  -> public getNow
  -> private _callExternalWithReplacedCtx
    -> internal _replacePlaceholderCtx
      -> library CallUtils.padLength32
  -> private _isCtxValid
  -> library CallUtils.revertFromReturnedData


### external callAppActionWithContext
-> public decodeCtx
  -> private _decodeCtx
    -> library ContextDefinitions.decodeCallInfo
-> private _updateContext
  -> library ContextDefinitions.encodeCallInfo
-> private _callExternalWithReplacedCtx
  -> internal _replacePlaceholderCtx
    -> library CallUtils.padLength32
-> private _isCtxValid
-> library CallUtils.revertFromReturnedData


### external callAppAfterCallback
-> private _callCallback
  -> internal _replacePlaceholderCtx
    -> library CallUtils.padLength32
  -> library CallbackUtils.staticCall
  -> library CallbackUtils.externalCall
  -> library CallUtils.revertFromReturnedData
  -> internal _jailApp
-> library CallUtils.isValidAbiEncodedBytes
-> private _isCtxValid
-> internal _jailApp


### external callAppBeforeCallback
-> private _callCallback
  -> internal _replacePlaceholderCtx
    -> library CallUtils.padLength32
  -> library CallbackUtils.staticCall
  -> library CallbackUtils.externalCall
  -> library CallUtils.revertFromReturnedData
  -> internal _jailApp
-> library CallUtils.isValidAbiEncodedBytes
-> internal _jailApp


### external castrate
_(no internal calls)_


### external changeSuperTokenAdmin
_(no internal calls)_


### external ctxUseCredit
-> public decodeCtx
  -> private _decodeCtx
    -> library ContextDefinitions.decodeCallInfo
-> private _updateContext
  -> library ContextDefinitions.encodeCallInfo


### public decodeCtx
-> private _decodeCtx
  -> library ContextDefinitions.decodeCallInfo


### external forwardBatchCall
-> internal _batchCall
  -> internal _callAgreement
    -> library CallUtils.parseSelector
    -> private _updateContext
      -> library ContextDefinitions.encodeCallInfo
    -> public getNow
    -> private _callExternalWithReplacedCtx
      -> internal _replacePlaceholderCtx
        -> library CallUtils.padLength32
    -> library CallUtils.revertFromReturnedData
  -> internal _callAppAction
    -> private _updateContext
      -> library ContextDefinitions.encodeCallInfo
    -> public getNow
    -> private _callExternalWithReplacedCtx
      -> internal _replacePlaceholderCtx
        -> library CallUtils.padLength32
    -> private _isCtxValid
    -> library CallUtils.revertFromReturnedData
  -> library CallUtils.revertFromReturnedData
-> internal _getTransactionSigner
  -> public isTrustedForwarder
    -> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### external getAgreementClass
_(no internal calls)_


### public getAppCallbackLevel
-> library SuperAppDefinitions.getAppCallbackLevel


### external getAppManifest
-> library SuperAppDefinitions.isAppJailed
  -> library SuperAppDefinitions.isAppJailed


### public getCodeAddress
-> library UUPSUtils.implementation


### external getERC2771Forwarder
_(no internal calls)_


### external getGovernance
_(no internal calls)_


### public getNow
_(no internal calls)_


### external getSimpleACL
_(no internal calls)_


### external getSuperTokenFactory
_(no internal calls)_


### external getSuperTokenFactoryLogic
_(no internal calls)_


### external initialize
_(no internal calls)_


### public isAgreementClassListed
_(no internal calls)_


### external isAgreementTypeListed
_(no internal calls)_


### public isApp
_(no internal calls)_


### external isAppJailed
-> library SuperAppDefinitions.isAppJailed


### external isCompositeAppAllowed
_(no internal calls)_


### external isCtxValid
-> private _isCtxValid


### public isTrustedForwarder
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### external jailApp
-> internal _jailApp


### external mapAgreementClasses
_(no internal calls)_


### public proxiableUUID
_(no internal calls)_


### external registerAgreementClass
_(no internal calls)_


### external registerApp
-> internal _enforceAppRegistrationPermissioning
  -> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> private _registerApp
  -> library SuperAppDefinitions.isConfigWordClean
  -> library SuperAppDefinitions.getAppCallbackLevel
    -> library SuperAppDefinitions.getAppCallbackLevel


### external registerAppByFactory
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey
-> private _registerApp
  -> library SuperAppDefinitions.isConfigWordClean
  -> library SuperAppDefinitions.getAppCallbackLevel
    -> library SuperAppDefinitions.getAppCallbackLevel


### external registerAppWithKey
-> internal _enforceAppRegistrationPermissioning
  -> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> private _registerApp
  -> library SuperAppDefinitions.isConfigWordClean
  -> library SuperAppDefinitions.getAppCallbackLevel
    -> library SuperAppDefinitions.getAppCallbackLevel


### external removeFromAgreementClassesBitmap
_(no internal calls)_


### external replaceGovernance
_(no internal calls)_


### external updateAgreementClass
_(no internal calls)_


### external updateCode
-> internal _updateCodeAddress
  -> library UUPSUtils.implementation
  -> public proxiableUUID
  -> library UUPSUtils.setImplementation


### external updatePoolBeaconLogic
_(no internal calls)_


### external updateSuperTokenFactory
_(no internal calls)_


### external updateSuperTokenLogic
_(no internal calls)_


### external versionRecipient
_(no internal calls)_


---

## SuperfluidFrameworkDeployer

_File: packages/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeployer.t.sol_

### external deployNativeAssetSuperToken
-> library TokenDeployerLibrary.deploySETHProxy
-> internal _handleResolverList


### external deployPureSuperToken
-> library TokenDeployerLibrary.deployPureSuperToken
-> internal _handleResolverList


### external deployTestFramework
-> public getNumSteps
-> public executeStep
  -> library SuperfluidGovDeployerLibrary.deployTestGovernance
  -> library SuperfluidGovDeployerLibrary.transferOwnership
  -> library SuperfluidHostDeployerLibrary.deploy
  -> library SuperfluidCFAv1DeployerLibrary.deploy
  -> library SuperfluidIDAv1DeployerLibrary.deploy
  -> library SuperfluidPoolLogicDeployerLibrary.deploy
  -> library ProxyDeployerLibrary.deploySuperfluidUpgradeableBeacon
  -> library SuperfluidGDAv1DeployerLibrary.deploy
  -> library ProxyDeployerLibrary.deployUUPSProxy
  -> library SuperfluidPoolNFTLogicDeployerLibrary.deployPoolAdminNFT
  -> library CFAv1ForwarderDeployerLibrary.deploy
  -> library GDAv1ForwarderDeployerLibrary.deploy
  -> library SuperTokenDeployerLibrary.deploy
  -> library SuperTokenFactoryDeployerLibrary.deploy
  -> library SuperfluidPeripheryDeployerLibrary.deployTestResolver
  -> library SuperfluidPeripheryDeployerLibrary.deploySuperfluidLoader
  -> library SuperfluidPeripheryDeployerLibrary.deployBatchLiquidator
  -> internal _is1820Deployed
  -> library SuperfluidPeripheryDeployerLibrary.deployTOGA


### external deployWrapperSuperToken
-> internal _deployWrapperSuperToken
  -> library TokenDeployerLibrary.deployTestToken
  -> internal _handleResolverList


### public executeStep
-> library SuperfluidGovDeployerLibrary.deployTestGovernance
-> library SuperfluidGovDeployerLibrary.transferOwnership
-> library SuperfluidHostDeployerLibrary.deploy
-> library SuperfluidCFAv1DeployerLibrary.deploy
-> library SuperfluidIDAv1DeployerLibrary.deploy
-> library SuperfluidPoolLogicDeployerLibrary.deploy
-> library ProxyDeployerLibrary.deploySuperfluidUpgradeableBeacon
-> library SuperfluidGDAv1DeployerLibrary.deploy
-> library ProxyDeployerLibrary.deployUUPSProxy
-> library SuperfluidPoolNFTLogicDeployerLibrary.deployPoolAdminNFT
-> library CFAv1ForwarderDeployerLibrary.deploy
-> library GDAv1ForwarderDeployerLibrary.deploy
-> library SuperTokenDeployerLibrary.deploy
-> library SuperTokenFactoryDeployerLibrary.deploy
-> library SuperfluidPeripheryDeployerLibrary.deployTestResolver
-> library SuperfluidPeripheryDeployerLibrary.deploySuperfluidLoader
-> library SuperfluidPeripheryDeployerLibrary.deployBatchLiquidator
-> internal _is1820Deployed
-> library SuperfluidPeripheryDeployerLibrary.deployTOGA


### external getFramework
_(no internal calls)_


### public getNumSteps
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## SuperfluidFrameworkDeploymentSteps

_File: packages/ethereum-contracts/contracts/utils/SuperfluidFrameworkDeploymentSteps.t.sol_

### public executeStep
-> library SuperfluidGovDeployerLibrary.deployTestGovernance
-> library SuperfluidGovDeployerLibrary.transferOwnership
-> library SuperfluidHostDeployerLibrary.deploy
-> library SuperfluidCFAv1DeployerLibrary.deploy
-> library SuperfluidIDAv1DeployerLibrary.deploy
-> library SuperfluidPoolLogicDeployerLibrary.deploy
-> library ProxyDeployerLibrary.deploySuperfluidUpgradeableBeacon
-> library SuperfluidGDAv1DeployerLibrary.deploy
-> library ProxyDeployerLibrary.deployUUPSProxy
-> library SuperfluidPoolNFTLogicDeployerLibrary.deployPoolAdminNFT
-> library CFAv1ForwarderDeployerLibrary.deploy
-> library GDAv1ForwarderDeployerLibrary.deploy
-> library SuperTokenDeployerLibrary.deploy
-> library SuperTokenFactoryDeployerLibrary.deploy
-> library SuperfluidPeripheryDeployerLibrary.deployTestResolver
-> library SuperfluidPeripheryDeployerLibrary.deploySuperfluidLoader
-> library SuperfluidPeripheryDeployerLibrary.deployBatchLiquidator
-> internal _is1820Deployed
-> library SuperfluidPeripheryDeployerLibrary.deployTOGA


### external getFramework
_(no internal calls)_


### public getNumSteps
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## SuperfluidGovernanceBase

_File: packages/ethereum-contracts/contracts/gov/SuperfluidGovernanceBase.sol_

### external authorizeAppFactory
-> internal _setConfig
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external batchChangeSuperTokenAdmin
_(no internal calls)_


### external batchUpdateSuperTokenLogic
_(no internal calls)_


### external batchUpdateSuperTokenMinimumDeposit
-> public setSuperTokenMinimumDeposit
  -> internal _setConfig


### external changeSuperTokenAdmin
_(no internal calls)_


### external clearAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> internal _clearConfig


### external clearConfig
-> internal _clearConfig


### external clearPPPConfig
-> internal _clearConfig


### external clearRewardAddress
-> internal _clearConfig


### external clearSuperTokenMinimumDeposit
-> internal _clearConfig


### external disableTrustedForwarder
-> internal _clearConfig
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### public enableTrustedForwarder
-> internal _setConfig
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### public getConfigAsAddress
_(no internal calls)_


### public getConfigAsUint256
_(no internal calls)_


### external getPPPConfig
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.decodePPPConfig


### external getRewardAddress
-> public getConfigAsAddress


### external getSuperTokenMinimumDeposit
-> public getConfigAsUint256


### external isAuthorizedAppFactory
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external isTrustedForwarder
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### external registerAgreementClass
_(no internal calls)_


### external replaceGovernance
_(no internal calls)_


### external setAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> internal _setConfig


### external setConfig
-> internal _setConfig


### public setPPPConfig
-> internal _setConfig


### public setRewardAddress
-> internal _setConfig


### public setSuperTokenMinimumDeposit
-> internal _setConfig


### external unauthorizeAppFactory
-> internal _clearConfig
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external updateContracts
_(no internal calls)_


### external verifyAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> public getConfigAsUint256


---

## SuperfluidGovernanceII

_File: packages/ethereum-contracts/contracts/gov/SuperfluidGovernanceII.sol_

### external authorizeAppFactory
-> internal _setConfig
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external batchChangeSuperTokenAdmin
_(no internal calls)_


### external batchUpdateSuperTokenLogic
_(no internal calls)_


### external batchUpdateSuperTokenMinimumDeposit
-> public setSuperTokenMinimumDeposit
  -> internal _setConfig


### external castrate
_(no internal calls)_


### external changeSuperTokenAdmin
_(no internal calls)_


### external clearAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> internal _clearConfig


### external clearConfig
-> internal _clearConfig


### external clearPPPConfig
-> internal _clearConfig


### external clearRewardAddress
-> internal _clearConfig


### external clearSuperTokenMinimumDeposit
-> internal _clearConfig


### external disableTrustedForwarder
-> internal _clearConfig
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### public enableTrustedForwarder
-> internal _setConfig
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### public getCodeAddress
-> library UUPSUtils.implementation


### public getConfigAsAddress
_(no internal calls)_


### public getConfigAsUint256
_(no internal calls)_


### external getPPPConfig
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.decodePPPConfig


### external getRewardAddress
-> public getConfigAsAddress


### external getSuperTokenMinimumDeposit
-> public getConfigAsUint256


### external isAuthorizedAppFactory
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external isTrustedForwarder
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### public proxiableUUID
_(no internal calls)_


### external registerAgreementClass
_(no internal calls)_


### external replaceGovernance
_(no internal calls)_


### external setAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> internal _setConfig


### external setConfig
-> internal _setConfig


### public setPPPConfig
-> internal _setConfig


### public setRewardAddress
-> internal _setConfig


### public setSuperTokenMinimumDeposit
-> internal _setConfig


### external unauthorizeAppFactory
-> internal _clearConfig
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external updateCode
-> internal _requireAuthorised
  -> internal _requireAuthorised
-> internal _updateCodeAddress
  -> library UUPSUtils.implementation
  -> public proxiableUUID
  -> library UUPSUtils.setImplementation


### external updateContracts
_(no internal calls)_


### external verifyAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> public getConfigAsUint256


---

## SuperfluidGovernanceIIProxy

_File: packages/ethereum-contracts/contracts/gov/SuperfluidGovernanceII.sol_

### external initializeProxy
-> library UUPSUtils.implementation
-> library UUPSUtils.setImplementation


---

## SuperfluidLoader

_File: packages/ethereum-contracts/contracts/utils/SuperfluidLoader.sol_

### external loadFramework
_(no internal calls)_


---

## SuperfluidPool

_File: packages/ethereum-contracts/contracts/agreements/gdav1/SuperfluidPool.sol_

### external allowance
_(no internal calls)_


### external approve
-> internal _approve


### external balanceOf
-> internal _getUnits


### external castrate
_(no internal calls)_


### public claimAll
-> internal _claimAll
  -> internal _settle
    -> public getUnsettledValue
      -> internal _memberDataToPDPoolMember
-> internal _shiftDisconnectedUnits
  -> internal _memberDataToPDPoolMember
  -> internal _pdPoolMemberToMemberData


### external decimals
_(no internal calls)_


### external decreaseAllowance
-> internal _approve


### external decreaseMemberUnits
-> internal _enforceChangeMemberUnitsPreconditions
-> internal _updateMemberUnits
  -> internal _memberDataToPDPoolMember
  -> internal _shiftDisconnectedUnits
    -> internal _memberDataToPDPoolMember
    -> internal _pdPoolMemberToMemberData
  -> internal _pdPoolIndexToPoolIndexData
  -> internal _pdPoolMemberToMemberData
-> internal _getUnits


### public getClaimable
-> public getUnsettledValue
  -> internal _memberDataToPDPoolMember


### external getClaimableNow
-> public getClaimable
  -> public getUnsettledValue
    -> internal _memberDataToPDPoolMember


### external getDisconnectedBalance
-> internal _memberDataToPDPoolMember


### external getMemberFlowRate
-> internal _getUnits


### external getTotalAmountReceivedByMember
-> internal _memberDataToPDPoolMember


### external getTotalConnectedFlowRate
-> internal _getTotalFlowRate
-> internal _getTotalDisconnectedFlowRate
  -> internal _memberDataToPDPoolMember


### external getTotalConnectedUnits
_(no internal calls)_


### external getTotalDisconnectedFlowRate
-> internal _getTotalDisconnectedFlowRate
  -> internal _memberDataToPDPoolMember


### external getTotalDisconnectedUnits
_(no internal calls)_


### external getTotalFlowRate
-> internal _getTotalFlowRate


### external getTotalUnits
-> internal _getTotalUnits


### external getUnits
-> internal _getUnits


### public getUnsettledValue
-> internal _memberDataToPDPoolMember


### external increaseAllowance
-> internal _approve


### external increaseMemberUnits
-> internal _enforceChangeMemberUnitsPreconditions
-> internal _updateMemberUnits
  -> internal _memberDataToPDPoolMember
  -> internal _shiftDisconnectedUnits
    -> internal _memberDataToPDPoolMember
    -> internal _pdPoolMemberToMemberData
  -> internal _pdPoolIndexToPoolIndexData
  -> internal _pdPoolMemberToMemberData
-> internal _getUnits


### external initialize
_(no internal calls)_


### external name
_(no internal calls)_


### external operatorConnectMember
-> internal _settle
  -> public getUnsettledValue
    -> internal _memberDataToPDPoolMember
-> internal _getUnits
-> internal _shiftDisconnectedUnits
  -> internal _memberDataToPDPoolMember
  -> internal _pdPoolMemberToMemberData


### external operatorSetIndex
-> internal _pdPoolIndexToPoolIndexData


### external poolOperatorGetIndex
_(no internal calls)_


### public proxiableUUID
_(no internal calls)_


### external symbol
_(no internal calls)_


### external totalSupply
-> internal _getTotalUnits


### external transfer
-> internal _transfer
  -> internal _getUnits
  -> internal _updateMemberUnits
    -> internal _memberDataToPDPoolMember
    -> internal _shiftDisconnectedUnits
      -> internal _memberDataToPDPoolMember
      -> internal _pdPoolMemberToMemberData
    -> internal _pdPoolIndexToPoolIndexData
    -> internal _pdPoolMemberToMemberData


### external transferFrom
-> internal _transfer
  -> internal _getUnits
  -> internal _updateMemberUnits
    -> internal _memberDataToPDPoolMember
    -> internal _shiftDisconnectedUnits
      -> internal _memberDataToPDPoolMember
      -> internal _pdPoolMemberToMemberData
    -> internal _pdPoolIndexToPoolIndexData
    -> internal _pdPoolMemberToMemberData


### external updateMemberUnits
-> internal _enforceChangeMemberUnitsPreconditions
-> internal _updateMemberUnits
  -> internal _memberDataToPDPoolMember
  -> internal _shiftDisconnectedUnits
    -> internal _memberDataToPDPoolMember
    -> internal _pdPoolMemberToMemberData
  -> internal _pdPoolIndexToPoolIndexData
  -> internal _pdPoolMemberToMemberData


---

## SuperfluidPoolPlaceholder

_File: packages/ethereum-contracts/contracts/agreements/gdav1/SuperfluidPoolPlaceholder.sol_

### external castrate
_(no internal calls)_


### external initialize
_(no internal calls)_


### public proxiableUUID
_(no internal calls)_


---

## SuperfluidTester

_File: packages/hot-fuzz/contracts/SuperfluidTester.sol_

### public approve
_(no internal calls)_


### public cfaLiquidate
_(no internal calls)_


### public claimAll
_(no internal calls)_


### public connectPool
_(no internal calls)_


### public createPool
_(no internal calls)_


### public decreaseAllowance
_(no internal calls)_


### public decreaseFlowRateAllowance
_(no internal calls)_


### public decreaseFlowRateAllowanceWithPermissions
_(no internal calls)_


### public disconnectPool
_(no internal calls)_


### public distribute
_(no internal calls)_


### public distributeFlow
_(no internal calls)_


### public downgradeSuperToken
_(no internal calls)_


### public flow
_(no internal calls)_


### public gdaLiquidate
_(no internal calls)_


### public increaseAllowance
_(no internal calls)_


### public increaseFlowRateAllowance
_(no internal calls)_


### public increaseFlowRateAllowanceWithPermissions
_(no internal calls)_


### public revokeFlowPermissions
_(no internal calls)_


### public setFlowPermissions
_(no internal calls)_


### public setMaxFlowPermissions
_(no internal calls)_


### public transfer
_(no internal calls)_


### public transferAll
_(no internal calls)_


### public transferFrom
_(no internal calls)_


### public updateMemberUnits
_(no internal calls)_


### public upgradeSuperToken
_(no internal calls)_


---

## SuperfluidToken

_File: packages/ethereum-contracts/contracts/superfluid/SuperfluidToken.sol_

### external createAgreement
-> library FixedSizeData.hasData
-> library FixedSizeData.storeData


### public getAccountActiveAgreements
_(no internal calls)_


### external getAgreementData
-> library FixedSizeData.loadData


### external getAgreementStateSlot
-> library FixedSizeData.loadData


### external getHost
_(no internal calls)_


### public isAccountCritical
-> public realtimeBalanceOf
  -> public getAccountActiveAgreements


### external isAccountCriticalNow
-> public isAccountCritical
  -> public realtimeBalanceOf
    -> public getAccountActiveAgreements


### public isAccountSolvent
-> public realtimeBalanceOf
  -> public getAccountActiveAgreements


### external isAccountSolventNow
-> public isAccountSolvent
  -> public realtimeBalanceOf
    -> public getAccountActiveAgreements


### external makeLiquidationPayoutsV2
-> internal _getRewardAccount
-> external_callback IERC20.Transfer


### public realtimeBalanceOf
-> public getAccountActiveAgreements


### public realtimeBalanceOfNow
-> public realtimeBalanceOf
  -> public getAccountActiveAgreements


### external settleBalance
_(no internal calls)_


### external terminateAgreement
-> library FixedSizeData.hasData
-> library FixedSizeData.eraseData


### external updateAgreementData
-> library FixedSizeData.storeData


### external updateAgreementStateSlot
-> library FixedSizeData.storeData


---

## SuperfluidUpgradeableBeacon

_File: packages/ethereum-contracts/contracts/upgradability/SuperfluidUpgradeableBeacon.sol_

### public upgradeTo
_(no internal calls)_


---

## TOGA

_File: packages/ethereum-contracts/contracts/utils/TOGA.sol_

### external changeExitRate
-> internal _getCurrentPICBond


### external getCurrentPIC
_(no internal calls)_


### external getCurrentPICInfo
-> internal _getCurrentPICBond


### public getDefaultExitRateFor
-> internal capToInt96


### external getMaxExitRateFor
-> internal capToInt96


### external tokensReceived
-> public getDefaultExitRateFor
  -> internal capToInt96
-> internal _becomePIC
  -> internal _getCurrentPICBond


---

## TestGovernance

_File: packages/ethereum-contracts/contracts/utils/TestGovernance.sol_

### external authorizeAppFactory
-> internal _setConfig
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external batchChangeSuperTokenAdmin
_(no internal calls)_


### external batchUpdateSuperTokenLogic
_(no internal calls)_


### external batchUpdateSuperTokenMinimumDeposit
-> public setSuperTokenMinimumDeposit
  -> internal _setConfig


### external changeSuperTokenAdmin
_(no internal calls)_


### external clearAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> internal _clearConfig


### external clearConfig
-> internal _clearConfig


### external clearPPPConfig
-> internal _clearConfig


### external clearRewardAddress
-> internal _clearConfig


### external clearSuperTokenMinimumDeposit
-> internal _clearConfig


### external disableTrustedForwarder
-> internal _clearConfig
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### public enableTrustedForwarder
-> internal _setConfig
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### public getConfigAsAddress
_(no internal calls)_


### public getConfigAsUint256
_(no internal calls)_


### external getPPPConfig
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.decodePPPConfig


### external getRewardAddress
-> public getConfigAsAddress


### external getSuperTokenMinimumDeposit
-> public getConfigAsUint256


### external initialize
-> public setRewardAddress
  -> internal _setConfig
-> public setPPPConfig
  -> internal _setConfig
-> public enableTrustedForwarder
  -> internal _setConfig
  -> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### external isAuthorizedAppFactory
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external isTrustedForwarder
-> public getConfigAsUint256
-> library SuperfluidGovernanceConfigs.getTrustedForwarderConfigKey


### external registerAgreementClass
_(no internal calls)_


### external replaceGovernance
_(no internal calls)_


### external setAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> internal _setConfig


### external setConfig
-> internal _setConfig


### public setPPPConfig
-> internal _setConfig


### public setRewardAddress
-> internal _setConfig


### public setSuperTokenMinimumDeposit
-> internal _setConfig


### external unauthorizeAppFactory
-> internal _clearConfig
-> library SuperfluidGovernanceConfigs.getAppFactoryConfigKey


### external updateContracts
_(no internal calls)_


### external verifyAppRegistrationKey
-> library SuperfluidGovernanceConfigs.getAppRegistrationConfigKey
-> public getConfigAsUint256


---

## TestResolver

_File: packages/ethereum-contracts/contracts/utils/TestResolver.sol_

### external addAdmin
_(no internal calls)_


### external get
_(no internal calls)_


### external set
_(no internal calls)_


---

## TestToken

_File: packages/ethereum-contracts/contracts/utils/TestToken.sol_

### public decimals
_(no internal calls)_


### public mint
_(no internal calls)_


---

## ToySuperToken

_File: packages/solidity-semantic-money/src/ref-impl/ToySuperToken.sol_

### external allowance
_(no internal calls)_


### external appendIndexUpdateByPool
-> internal _tokenEff
-> internal _appendIndexUpdateByPool
  -> internal _isPool
  -> internal _setPoolAdjustmentFlowRate
    -> public getPoolAdjustmentFlowHash
    -> internal _getFlowRate
      -> external_callback ToySuperfluidToken._getFlowRate


### external approve
-> internal _approve


### external balanceOf
-> public realtimeBalanceAt
  -> public realtimeBalanceVectorAt
    -> internal _isPool
    -> internal _getUIndex
      -> external_callback ToySuperfluidToken._getUIndex


### public connectPool
-> internal _isPool


### external createPool
-> internal _registerPool


### external disconnectPool
-> public connectPool
  -> internal _isPool


### external distribute
-> internal _tokenEff
-> internal _distribute
  -> internal _isPool
  -> internal _acl
    -> internal _spendAllowance
      -> internal _approve


### external distributeFlow
-> internal _tokenEff
-> internal _distributeFlow
  -> internal _isPool
  -> public getDistributionFlowHash
  -> internal _getFlowRate
    -> external_callback ToySuperfluidToken._getFlowRate
  -> internal _acl
    -> internal _spendAllowance
      -> internal _approve
  -> internal _adjustBuffer


### external flow
-> internal _tokenEff
-> internal _flow
  -> internal _isPool
  -> internal _acl
    -> internal _spendAllowance
      -> internal _approve
  -> public getFlowHash
  -> internal _getFlowRate
    -> external_callback ToySuperfluidToken._getFlowRate
  -> internal _adjustBuffer


### public getDistributionFlowHash
_(no internal calls)_


### public getFlowHash
_(no internal calls)_


### external getFlowRate
-> internal _getFlowRate
  -> external_callback ToySuperfluidToken._getFlowRate
-> public getFlowHash


### external getNetFlowRate
-> internal _getUIndex
  -> external_callback ToySuperfluidToken._getUIndex
-> internal _isPool


### external getNumConnections
_(no internal calls)_


### public getPoolAdjustmentFlowHash
_(no internal calls)_


### external getPoolAdjustmentFlowInfo
-> internal _getPoolAdjustmentFlowInfo
  -> public getPoolAdjustmentFlowHash
  -> internal _getFlowRate
    -> external_callback ToySuperfluidToken._getFlowRate


### external isMemberConnected
_(no internal calls)_


### external isPool
-> internal _isPool


### external poolSettleClaim
-> internal _tokenEff
-> internal _poolSettleClaim
  -> internal _isPool


### public realtimeBalanceAt
-> public realtimeBalanceVectorAt
  -> internal _isPool
  -> internal _getUIndex
    -> external_callback ToySuperfluidToken._getUIndex


### external realtimeBalanceNow
-> public realtimeBalanceAt
  -> public realtimeBalanceVectorAt
    -> internal _isPool
    -> internal _getUIndex
      -> external_callback ToySuperfluidToken._getUIndex


### public realtimeBalanceVectorAt
-> internal _isPool
-> internal _getUIndex
  -> external_callback ToySuperfluidToken._getUIndex


### public realtimeBalanceVectorNow
-> public realtimeBalanceVectorAt
  -> internal _isPool
  -> internal _getUIndex
    -> external_callback ToySuperfluidToken._getUIndex


### external setLiquidationPeriod
_(no internal calls)_


### external shift
-> internal _tokenEff
-> internal _shift
  -> internal _isPool
  -> internal _acl
    -> internal _spendAllowance
      -> internal _approve


### external totalSupply
_(no internal calls)_


### external transfer
-> internal _tokenEff
-> internal _shift
  -> internal _isPool
  -> internal _acl
    -> internal _spendAllowance
      -> internal _approve


### external transferFrom
-> internal _tokenEff
-> internal _shift
  -> internal _isPool
  -> internal _acl
    -> internal _spendAllowance
      -> internal _approve


---

## ToySuperfluidPool

_File: packages/solidity-semantic-money/src/ref-impl/ToySuperfluidPool.sol_

### external claimAll
-> external claimAll


### external getClaimable
-> external getClaimable


### external getConnectedFlowRate
_(no internal calls)_


### external getDisconnectedBalance
_(no internal calls)_


### external getDisconnectedFlowRate
_(no internal calls)_


### external getDisconnectedUnits
_(no internal calls)_


### external getDistributionFlowRate
_(no internal calls)_


### external getIndex
_(no internal calls)_


### external getMemberFlowRate
_(no internal calls)_


### external getTotalUnits
_(no internal calls)_


### external getUnits
_(no internal calls)_


### public initialize
_(no internal calls)_


### external operatorConnectMember
-> internal _claimAll
  -> external getClaimable
    -> external getClaimable
-> internal _shiftDisconnectedUnits


### external operatorSetIndex
_(no internal calls)_


### external updateMember
-> internal _claimAll
  -> external getClaimable
    -> external getClaimable
-> internal _shiftDisconnectedUnits


---

## ToySuperfluidToken

_File: packages/solidity-semantic-money/src/ref-impl/ToySuperfluidToken.sol_

### external appendIndexUpdateByPool
-> internal _appendIndexUpdateByPool
  -> internal _isPool
  -> internal _setPoolAdjustmentFlowRate
    -> public getPoolAdjustmentFlowHash
    -> internal _getFlowRate
    -> internal _doFlow
      -> internal _getFlowRate
      -> internal _getUIndex
      -> internal _setUIndex
      -> internal _setFlowInfo


### public connectPool
-> internal _isPool


### external createPool
-> internal _registerPool


### external disconnectPool
-> public connectPool
  -> internal _isPool


### external distribute
-> internal _distribute
  -> internal _isPool
  -> internal _acl
  -> internal _doDistributeViaPool
    -> internal _getUIndex
    -> internal _getPDPIndex
    -> internal _setUIndex
    -> internal _setPDPIndex


### external distributeFlow
-> internal _distributeFlow
  -> internal _isPool
  -> public getDistributionFlowHash
  -> internal _getFlowRate
  -> internal _acl
  -> internal _doDistributeFlowViaPool
    -> internal _getUIndex
    -> internal _getPDPIndex
    -> internal _getPoolAdjustmentFlowRate
      -> internal _getPoolAdjustmentFlowInfo
        -> public getPoolAdjustmentFlowHash
        -> internal _getFlowRate
    -> internal _getFlowRate
    -> internal _setUIndex
    -> internal _setPDPIndex
    -> internal _setFlowInfo
    -> internal _setPoolAdjustmentFlowRate
      -> public getPoolAdjustmentFlowHash
      -> internal _getFlowRate
      -> internal _doFlow
        -> internal _getFlowRate
        -> internal _getUIndex
        -> internal _setUIndex
        -> internal _setFlowInfo
  -> internal _adjustBuffer


### external flow
-> internal _flow
  -> internal _isPool
  -> internal _acl
  -> public getFlowHash
  -> internal _getFlowRate
  -> internal _doFlow
    -> internal _getFlowRate
    -> internal _getUIndex
    -> internal _setUIndex
    -> internal _setFlowInfo
  -> internal _adjustBuffer


### public getDistributionFlowHash
_(no internal calls)_


### public getFlowHash
_(no internal calls)_


### external getFlowRate
-> internal _getFlowRate
-> public getFlowHash


### external getNetFlowRate
-> internal _getUIndex
-> internal _isPool


### external getNumConnections
_(no internal calls)_


### public getPoolAdjustmentFlowHash
_(no internal calls)_


### external getPoolAdjustmentFlowInfo
-> internal _getPoolAdjustmentFlowInfo
  -> public getPoolAdjustmentFlowHash
  -> internal _getFlowRate


### external isMemberConnected
_(no internal calls)_


### external isPool
-> internal _isPool


### external poolSettleClaim
-> internal _poolSettleClaim
  -> internal _isPool
  -> internal _doShift
    -> internal _getUIndex
    -> internal _setUIndex


### public realtimeBalanceAt
-> public realtimeBalanceVectorAt
  -> internal _isPool
  -> internal _getUIndex


### external realtimeBalanceNow
-> public realtimeBalanceAt
  -> public realtimeBalanceVectorAt
    -> internal _isPool
    -> internal _getUIndex


### public realtimeBalanceVectorAt
-> internal _isPool
-> internal _getUIndex


### public realtimeBalanceVectorNow
-> public realtimeBalanceVectorAt
  -> internal _isPool
  -> internal _getUIndex


### external setLiquidationPeriod
_(no internal calls)_


### external shift
-> internal _shift
  -> internal _isPool
  -> internal _acl
  -> internal _doShift
    -> internal _getUIndex
    -> internal _setUIndex


---

## UUPSProxiable

_File: packages/ethereum-contracts/contracts/upgradability/UUPSProxiable.sol_

### external castrate
_(no internal calls)_


### public getCodeAddress
-> library UUPSUtils.implementation


---

## UUPSProxy

_File: packages/ethereum-contracts/contracts/upgradability/UUPSProxy.sol_

### external initializeProxy
-> library UUPSUtils.implementation
-> library UUPSUtils.setImplementation


---

## VestingSchedulerV2

_File: packages/automation-contracts/scheduler/contracts/VestingSchedulerV2.sol_

### external afterAgreementCreated
_(no internal calls)_


### external afterAgreementTerminated
_(no internal calls)_


### external afterAgreementUpdated
_(no internal calls)_


### external beforeAgreementCreated
_(no internal calls)_


### external beforeAgreementTerminated
_(no internal calls)_


### external beforeAgreementUpdated
_(no internal calls)_


### external createAndExecuteVestingScheduleFromAmountAndDuration
-> private _validateAndCreateAndExecuteVestingScheduleFromAmountAndDuration
  -> private _getSender
  -> private _validateAndCreateVestingSchedule
    -> private _getId
  -> public mapCreateVestingScheduleParams
  -> private _normalizeStartDate
  -> private _getVestingScheduleAggregate
    -> private _getId
  -> private _validateBeforeCliffAndFlow
    -> private _lteDateToExecuteCliffAndFlow
  -> private _executeCliffAndFlow


### external createVestingSchedule
-> private _getSender
-> private _validateAndCreateVestingSchedule
  -> private _getId
-> private _normalizeStartDate


### external createVestingScheduleFromAmountAndDuration
-> private _validateAndCreateVestingSchedule
  -> private _getId
-> public mapCreateVestingScheduleParams
-> private _normalizeStartDate


### external deleteVestingSchedule
-> private _getSender
-> private _getVestingScheduleAggregate
  -> private _getId


### external executeCliffAndFlow
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _validateAndClaim
-> private _validateBeforeCliffAndFlow
  -> private _lteDateToExecuteCliffAndFlow
-> private _gteDateToExecuteEndVesting
-> private _validateBeforeEndVesting
  -> private _gteDateToExecuteEndVesting
-> private _executeVestingAsSingleTransfer
  -> private _getTotalVestedAmount
-> private _executeCliffAndFlow


### external executeEndVesting
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _validateBeforeEndVesting
  -> private _gteDateToExecuteEndVesting
-> private _isFlowOngoing


### external getMaximumNeededTokenAllowance
-> private _gteDateToExecuteEndVesting
-> private _getTotalVestedAmount


### external getVestingSchedule
-> private _getId


### public mapCreateVestingScheduleParams
_(no internal calls)_


### external updateVestingSchedule
-> private _getSender
-> private _getVestingScheduleAggregate
  -> private _getId


---

## VestingSchedulerV3

_File: packages/automation-contracts/scheduler/contracts/VestingSchedulerV3.sol_

### external createAndExecuteVestingScheduleFromAmountAndDuration
-> internal _validateAndCreateAndExecuteVestingScheduleFromAmountAndDuration
  -> internal _msgSender
    -> public isTrustedForwarder
  -> private _validateAndCreateVestingSchedule
    -> private _getId
  -> public mapCreateVestingScheduleParams
  -> private _normalizeStartDate
  -> private _getVestingScheduleAggregate
    -> private _getId
  -> private _validateBeforeCliffAndFlow
    -> private _lteDateToExecuteCliffAndFlow
  -> private _executeCliffAndFlow
    -> private _settle
      -> private _getTotalVestedAmount


### external createVestingSchedule
-> private _validateAndCreateVestingSchedule
  -> private _getId
-> internal _msgSender
  -> public isTrustedForwarder
-> private _normalizeStartDate


### external createVestingScheduleFromAmountAndDuration
-> private _validateAndCreateVestingSchedule
  -> private _getId
-> public mapCreateVestingScheduleParams
-> internal _msgSender
  -> public isTrustedForwarder
-> private _normalizeStartDate


### external deleteVestingSchedule
-> internal _msgSender
  -> public isTrustedForwarder
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _deleteVestingSchedule


### external endVestingScheduleNow
-> internal _msgSender
  -> public isTrustedForwarder
-> private _getVestingScheduleAggregate
  -> private _getId
-> public executeCliffAndFlow
  -> private _getVestingScheduleAggregate
    -> private _getId
  -> private _validateAndClaim
    -> internal _msgSender
      -> public isTrustedForwarder
  -> private _validateBeforeCliffAndFlow
    -> private _lteDateToExecuteCliffAndFlow
  -> private _gteDateToExecuteEndVesting
  -> private _validateBeforeEndVesting
    -> private _gteDateToExecuteEndVesting
  -> private _executeVestingAsSingleTransfer
    -> private _deleteVestingSchedule
    -> private _getTotalVestedAmount
  -> private _executeCliffAndFlow
    -> private _settle
      -> private _getTotalVestedAmount
-> private _updateVestingSchedule
  -> private _settle
    -> private _getTotalVestedAmount
  -> private _calculateFlowRate
  -> private _updateVestingFlowRate
  -> private _calculateRemainderAmount
-> public executeEndVesting
  -> private _getVestingScheduleAggregate
    -> private _getId
  -> private _validateBeforeEndVesting
    -> private _gteDateToExecuteEndVesting
  -> private _settle
    -> private _getTotalVestedAmount
  -> private _getTotalVestedAmount
  -> private _deleteVestingSchedule
  -> private _isFlowOngoing


### public executeCliffAndFlow
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _validateAndClaim
  -> internal _msgSender
    -> public isTrustedForwarder
-> private _validateBeforeCliffAndFlow
  -> private _lteDateToExecuteCliffAndFlow
-> private _gteDateToExecuteEndVesting
-> private _validateBeforeEndVesting
  -> private _gteDateToExecuteEndVesting
-> private _executeVestingAsSingleTransfer
  -> private _deleteVestingSchedule
  -> private _getTotalVestedAmount
-> private _executeCliffAndFlow
  -> private _settle
    -> private _getTotalVestedAmount


### public executeEndVesting
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _validateBeforeEndVesting
  -> private _gteDateToExecuteEndVesting
-> private _settle
  -> private _getTotalVestedAmount
-> private _getTotalVestedAmount
-> private _deleteVestingSchedule
-> private _isFlowOngoing


### external getMaximumNeededTokenAllowance
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _getMaximumNeededTokenAllowance
  -> private _gteDateToExecuteEndVesting
  -> private _getTotalVestedAmount


### external getTotalVestedAmount
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _getTotalVestedAmount


### external getVestingSchedule
-> private _getId


### public isTrustedForwarder
_(no internal calls)_


### public mapCreateVestingScheduleParams
_(no internal calls)_


### external updateVestingSchedule
-> internal _msgSender
  -> public isTrustedForwarder
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _updateVestingSchedule
  -> private _settle
    -> private _getTotalVestedAmount
  -> private _calculateFlowRate
  -> private _updateVestingFlowRate
  -> private _calculateRemainderAmount


### external updateVestingScheduleFlowRateFromAmount
-> internal _msgSender
  -> public isTrustedForwarder
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _updateVestingSchedule
  -> private _settle
    -> private _getTotalVestedAmount
  -> private _calculateFlowRate
  -> private _updateVestingFlowRate
  -> private _calculateRemainderAmount


### external updateVestingScheduleFlowRateFromAmountAndEndDate
-> internal _msgSender
  -> public isTrustedForwarder
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _updateVestingSchedule
  -> private _settle
    -> private _getTotalVestedAmount
  -> private _calculateFlowRate
  -> private _updateVestingFlowRate
  -> private _calculateRemainderAmount


### external updateVestingScheduleFlowRateFromEndDate
-> internal _msgSender
  -> public isTrustedForwarder
-> private _getVestingScheduleAggregate
  -> private _getId
-> private _getTotalVestedAmount
-> private _updateVestingSchedule
  -> private _settle
    -> private _getTotalVestedAmount
  -> private _calculateFlowRate
  -> private _updateVestingFlowRate
  -> private _calculateRemainderAmount


### external versionRecipient
_(no internal calls)_


---

## WrapStrategy

_File: packages/automation-contracts/autowrap/contracts/strategies/WrapStrategy.sol_

### external changeManager
_(no internal calls)_


### external emergencyWithdraw
_(no internal calls)_


### public isSupportedSuperToken
_(no internal calls)_


### external wrap
-> internal _toUnderlyingAmount

