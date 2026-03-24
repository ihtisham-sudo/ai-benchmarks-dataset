// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ILendingDexVault {

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
    function setInterestRateParams(address reserve,
    bytes calldata rateData) external;
    function getInterestRateData(address reserve) external view returns (InterestRateDataRay memory);
    function getInterestRateDataBps(address reserve) external view returns (InterestRateData memory);
    function getOptimalUsageRatio(address reserve) external view returns (uint256);
    function getVariableRateSlope1(address reserve) external view returns (uint256);
    function getVariableRateSlope2(address reserve) external view returns (uint256);
    function getBaseVariableBorrowRate(address reserve) external view returns (uint256);
    function getMaxVariableBorrowRate(address reserve) external view returns (uint256);
    function calculateInterestRates(DataTypes.CalculateInterestRatesParams calldata params) external view returns (uint256, uint256);
    function performTransfer(address to,
    address reward,
    uint256 amount) external returns (bool);
    function getRewardsVault() external view returns (address);
    function getIncentivesController() external view returns (address);
}