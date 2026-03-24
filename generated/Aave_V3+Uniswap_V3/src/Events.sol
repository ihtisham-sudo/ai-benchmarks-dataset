// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title LendingDex — shared events and errors
 * @dev Synthesised from: Aave_V3, Uniswap_V3
 */
library LendingDexEvents {

    // ── Errors ─────────────────────────────────────────────────────
    error ERC20InsufficientAllowance(address spender, uint256 allowance, uint256 needed);

}