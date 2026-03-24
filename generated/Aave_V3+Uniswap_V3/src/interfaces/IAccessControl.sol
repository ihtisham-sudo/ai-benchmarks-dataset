// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ILendingDexAccessControl {

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
    function setRoleAdmin(bytes32 role,
    bytes32 adminRole) external;
    function addPoolAdmin(address admin) external;
    function removePoolAdmin(address admin) external;
    function isPoolAdmin(address admin) external view returns (bool);
    function addEmergencyAdmin(address admin) external;
    function removeEmergencyAdmin(address admin) external;
    function isEmergencyAdmin(address admin) external view returns (bool);
    function addRiskAdmin(address admin) external;
    function removeRiskAdmin(address admin) external;
    function isRiskAdmin(address admin) external view returns (bool);
}