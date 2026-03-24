// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title SyntheticVault — protocol core coordinator
 * @notice Synthesised from: FlatMoney, GMX_V2, Olympus_Cooler
 * @dev Synthesised from: FlatMoney, GMX_V2, Olympus_Cooler
 */
contract SyntheticVault {

    // ── Events ─────────────────────────────────────────────────────
    event Initialized(address indexed initializer);

    // ── Errors ─────────────────────────────────────────────────────
    error AlreadyInitialized();
    error NotInitialized();

    // ── State ──────────────────────────────────────────────────────
    SyntheticVaultAccessControl public accesscontrol;
    SyntheticVaultToken public token;
    SyntheticVaultVault public vault;
    SyntheticVaultSwapRouter public swaprouter;
    SyntheticVaultOracle public oracle;
    SyntheticVaultTimelock public timelock;

    // ── Functions ──────────────────────────────────────────────────
    function initialize(address _accesscontrol, address _token, address _vault, address _swaprouter, address _oracle, address _timelock) external {
        // TODO: set module references
        emit Initialized(msg.sender);
    }

}