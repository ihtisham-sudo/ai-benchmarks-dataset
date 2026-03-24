// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ILendingDexLendingPool {

    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    event Repaid(address indexed user, address indexed asset, uint256 amount);
    event Liquidated(address indexed borrower, address indexed liquidator, uint256 amount);

    error InsufficientCollateral();
    error HealthyPosition();
    error UnauthorizedLiquidation();

    function supplyCollateral(address asset, uint256 amount) external;
    function withdrawCollateral(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
    function liquidate(address borrower, address asset, uint256 debtAmount) external;
    function getHealthFactor(address user) external view returns (uint256);
    function setInterestRate(uint256 newRate) external;
    function getReservesList(IPoolAddressesProvider provider) external view returns (address[] memory);
    function getReservesData(IPoolAddressesProvider provider) external view returns (AggregatedReserveData[] memory, BaseCurrencyInfo memory);
    function getEModes(IPoolAddressesProvider provider) external view returns (Emode[] memory);
    function getUserReservesData(IPoolAddressesProvider provider,
    address user) external view returns (UserReserveData[] memory, uint8);
    function initialize(IPoolAddressesProvider provider) external;
    function getMarketId() external view returns (string memory);
    function setMarketId(string memory newMarketId) external;
    function getAddress(bytes32 id) external view returns (address);
    function setAddress(bytes32 id, address newAddress) external;
    function setAddressAsProxy(bytes32 id,
    address newImplementationAddress) external;
    function getPool() external view returns (address);
    function setPoolImpl(address newPoolImpl) external;
}