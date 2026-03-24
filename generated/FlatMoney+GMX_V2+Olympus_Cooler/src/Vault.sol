// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title SyntheticVault — ERC-4626 inspired yield vault
 * @dev Synthesised from: FlatMoney, GMX_V2, Olympus_Cooler
 */
contract SyntheticVaultVault {

    // ── Events ─────────────────────────────────────────────────────
    event Deposit(address indexed caller, address indexed owner, uint256 assets, uint256 shares);
    event Withdraw(address indexed caller, address indexed receiver, address indexed owner, uint256 assets, uint256 shares);

    // ── Errors ─────────────────────────────────────────────────────
    error InsufficientAssets();
    error ExceedsMaxDeposit();
    error ZeroShares();

    // ── State ──────────────────────────────────────────────────────
    address public asset;
    uint256 public totalAssets;
    uint256 public totalShares;
    mapping(address => uint256) public shares;

    // ── Modifiers ──────────────────────────────────────────────────
    modifier onlyTimelockAdmin() {
        _;
    }

    // ── Functions ──────────────────────────────────────────────────
    function deposit(uint256 assets, address receiver) external returns (uint256 shares) {
        // TODO: convert assets to shares
        emit Deposit(msg.sender, receiver, assets, 0);
        return 0;
    }

    function withdraw(uint256 assets, address receiver, address owner) external returns (uint256 shares) {
        // TODO: convert shares to assets
        return 0;
    }

    function redeem(uint256 shares, address receiver, address owner) external returns (uint256 assets) {
        // TODO: convert shares to assets
        return 0;
    }

    function previewDeposit(uint256 assets) external view returns (uint256) {
        return 0;
    }

    function previewWithdraw(uint256 assets) external view returns (uint256) {
        return 0;
    }

    function convertToShares(uint256 assets) public view returns (uint256) {
        return 0;
    }

    function convertToAssets(uint256 shares) public view returns (uint256) {
        return 0;
    }

    function withdrawNativeToken(address receiver, uint256 amount) external onlyTimelockAdmin {
        // TODO: implement
    }

    function withdrawToken(address token, address receiver, uint256 amount) external onlyTimelockAdmin {
        // TODO: implement
    }

}