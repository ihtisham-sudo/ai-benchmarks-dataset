// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title SecureToken — shared events and errors
 * @dev Synthesised from: Dinari, Telcoin
 */
library SecureTokenEvents {

    // ── Events ─────────────────────────────────────────────────────
    event NameSet(string name);
    event SymbolSet(string symbol);
    event TransferRestrictorSet(ITransferRestrictor indexed transferRestrictor);
    event BalancePerShareSet(uint256 balancePerShare);
    event FundsWithdrawn(IERC20 token, address user, uint256 amount);

    // ── Errors ─────────────────────────────────────────────────────
    error Unauthorized();
    error ZeroValue();
    error BuyFillsNotSupported();
    error OnlyForBuyOrders();

}