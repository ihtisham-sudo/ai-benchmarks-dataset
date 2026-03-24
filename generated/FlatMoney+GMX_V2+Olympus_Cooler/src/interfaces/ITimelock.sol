// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISyntheticVaultTimelock {

    event OperationScheduled(bytes32 indexed id, address target, uint256 delay);
    event OperationExecuted(bytes32 indexed id);
    event OperationCancelled(bytes32 indexed id);

    error OperationNotReady();
    error OperationAlreadyExists();
    error MinDelayNotMet();

    function schedule(address target, uint256 value, bytes calldata data, bytes32 salt, uint256 delay) external returns (bytes32 id);
    function execute(address target, uint256 value, bytes calldata data, bytes32 salt) external payable;
    function cancel(bytes32 id) external;
    function isOperationPending(bytes32 id) external view returns (bool);
    function updateMinDelay(uint256 newDelay) external;
    function executeWithOraclePrices(address target,
        uint256 value,
        bytes calldata payload,
        bytes32 predecessor,
        bytes32 salt,
        OracleUtils.SetPricesParams calldata oracleParams) external;
    function withdrawFromPositionImpactPool(address market,
        address receiver,
        uint256 amount) external;
    function reduceLentImpactAmount(address market,
        address fundingAccount,
        uint256 reductionAmount) external;
    function signalGrantRole(address account, bytes32 roleKey, bytes32 predecessor, bytes32 salt) external;
    function signalRevokeRole(address account, bytes32 roleKey, bytes32 predecessor, bytes32 salt) external;
    function revokeRole(address account, bytes32 roleKey) external;
    function signalSetOracleProviderEnabled(address provider, bool value, bytes32 predecessor, bytes32 salt) external;
    function signalSetAtomicOracleProvider(address provider, bool value, bytes32 predecessor, bytes32 salt) external;
    function signalAddOracleSigner(address account, bytes32 predecessor, bytes32 salt) external;
    function signalRemoveOracleSigner(address account, bytes32 predecessor, bytes32 salt) external;
    function signalSetFeeReceiver(address account, bytes32 predecessor, bytes32 salt) external;
    function signalSetHoldingAddress(address account, bytes32 predecessor, bytes32 salt) external;
}