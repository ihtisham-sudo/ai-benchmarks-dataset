// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISyntheticVaultAccessControl {

    event RoleGranted(bytes32 indexed role, address indexed account, address indexed sender);
    event RoleRevoked(bytes32 indexed role, address indexed account, address indexed sender);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    error Unauthorized();
    error ZeroAddress();
    error AlreadyHasRole(bytes32 role, address account);

    function initialize(address _owner) external;
    function grantRole(bytes32 role, address account) external;
    function revokeRole(bytes32 role, address account) external;
    function hasRole(bytes32 role, address account) external view returns (bool);
    function transferOwnership(address newOwner) external;
    function executeOrder(address account_,
        bytes[] calldata priceUpdateData_) external payable;
    function executeLimitOrder(uint256 tokenId_,
        bytes[] calldata priceUpdateData_) external payable;
    function cancelExistingOrder(address account_) external;
    function cancelOrderByModule(address account_) external;
    function hasOrderExpired(address account_) external view returns (bool expired_);
    function setMaxExecutabilityAge(uint64 maxExecutabilityAge_) external;
    function getTradeFee(uint256 size_) external view returns (uint256 tradeFee_);
    function getWithdrawalFee(uint256 amount_) external view returns (uint256 withdrawalFee_);
    function getProtocolFee(uint256 feeAmount_) external view returns (uint256 protocolFeePortion_);
    function setProtocolFeeRecipient(address protocolFeeRecipient_) external;
}