// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title LendingDex — protocol core coordinator
 * @notice Synthesised from: Aave_V3, Uniswap_V3
 * @dev Synthesised from: Aave_V3, Uniswap_V3
 */
contract LendingDex {

    // ── Events ─────────────────────────────────────────────────────
    event Initialized(address indexed initializer);

    // ── Errors ─────────────────────────────────────────────────────
    error AlreadyInitialized();
    error NotInitialized();

    // ── State ──────────────────────────────────────────────────────
    LendingDexAccessControl public accesscontrol;
    LendingDexToken public token;
    LendingDexVault public vault;
    LendingDexLendingPool public lendingpool;
    LendingDexSwapRouter public swaprouter;
    LendingDexOracle public oracle;

    // ── Functions ──────────────────────────────────────────────────
    function initialize(address _accesscontrol, address _token, address _vault, address _lendingpool, address _swaprouter, address _oracle) external {
        // TODO: set module references
        emit Initialized(msg.sender);
    }

}