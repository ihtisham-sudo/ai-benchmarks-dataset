// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title LendingDex — role-based access control
 * @dev Synthesised from: Aave_V3, Uniswap_V3
 */
contract LendingDexAccessControl {

    // ── Events ─────────────────────────────────────────────────────
    event RoleGranted(bytes32 indexed role, address indexed account, address indexed sender);
    event RoleRevoked(bytes32 indexed role, address indexed account, address indexed sender);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // ── Errors ─────────────────────────────────────────────────────
    error Unauthorized();
    error ZeroAddress();
    error AlreadyHasRole(bytes32 role, address account);

    // ── State ──────────────────────────────────────────────────────
    address public owner;
    mapping(address => mapping(bytes32 => bool)) public roles;
    mapping(bytes32 => bytes32) public roleAdmin;

    // ── Modifiers ──────────────────────────────────────────────────
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    modifier onlyRole(bytes32 role) {
        require(hasRole(role, msg.sender), "Missing role");
        _;
    }

    // ── Functions ──────────────────────────────────────────────────
    function initialize(address _owner) public {
        // TODO: set module references
        emit Initialized(msg.sender);
    }

    function grantRole(bytes32 role, address account) external onlyRole {
        roles[account][role] = true;
        emit RoleGranted(role, account, msg.sender);
    }

    function revokeRole(bytes32 role, address account) external onlyRole {
        roles[account][role] = false;
        emit RoleRevoked(role, account, msg.sender);
    }

    function hasRole(bytes32 role, address account) public view returns (bool) {
        return false;
    }

    function transferOwnership(address newOwner) external onlyOwner {
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    function setRoleAdmin(bytes32 role,
    bytes32 adminRole) external onlyRole {
        // TODO: implement
    }

    function addPoolAdmin(address admin) external {
        // TODO: implement
    }

    function removePoolAdmin(address admin) external {
        // TODO: implement
    }

    function isPoolAdmin(address admin) external view returns (bool) {
        return false;
    }

    function addEmergencyAdmin(address admin) external {
        // TODO: implement
    }

    function removeEmergencyAdmin(address admin) external {
        // TODO: implement
    }

    function isEmergencyAdmin(address admin) external view returns (bool) {
        return false;
    }

    function addRiskAdmin(address admin) external {
        // TODO: implement
    }

    function removeRiskAdmin(address admin) external {
        // TODO: implement
    }

    function isRiskAdmin(address admin) external view returns (bool) {
        return false;
    }

}