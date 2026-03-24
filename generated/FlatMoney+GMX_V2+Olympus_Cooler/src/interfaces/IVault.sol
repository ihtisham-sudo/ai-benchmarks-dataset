// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISyntheticVaultVault {

    event Deposit(address indexed caller, address indexed owner, uint256 assets, uint256 shares);
    event Withdraw(address indexed caller, address indexed receiver, address indexed owner, uint256 assets, uint256 shares);

    error InsufficientAssets();
    error ExceedsMaxDeposit();
    error ZeroShares();

    function deposit(uint256 assets, address receiver) external returns (uint256 shares);
    function withdraw(uint256 assets, address receiver, address owner) external returns (uint256 shares);
    function redeem(uint256 shares, address receiver, address owner) external returns (uint256 assets);
    function previewDeposit(uint256 assets) external view returns (uint256);
    function previewWithdraw(uint256 assets) external view returns (uint256);
    function convertToShares(uint256 assets) external view returns (uint256);
    function convertToAssets(uint256 shares) external view returns (uint256);
    function withdrawNativeToken(address receiver, uint256 amount) external;
    function withdrawToken(address token, address receiver, uint256 amount) external;
}