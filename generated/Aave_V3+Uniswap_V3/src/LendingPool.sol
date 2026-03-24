// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title LendingDex — Collateralised lending and borrowing pool
 * @dev Synthesised from: Aave_V3, Uniswap_V3
 */
contract LendingDexLendingPool {

    // ── Events ─────────────────────────────────────────────────────
    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    event Repaid(address indexed user, address indexed asset, uint256 amount);
    event Liquidated(address indexed borrower, address indexed liquidator, uint256 amount);

    // ── Errors ─────────────────────────────────────────────────────
    error InsufficientCollateral();
    error HealthyPosition();
    error UnauthorizedLiquidation();

    // ── State ──────────────────────────────────────────────────────
    address public oracle;
    mapping(address => uint256) public collateral;
    mapping(address => uint256) public debt;
    uint256 public liquidationThreshold;
    uint256 public interestRatePerSecond;
    bytes32 public symbol;
    bytes32 public name;
    uint8 public eModesFound;
    uint8 public missCounter;
    uint128 public ltvzeroBitmap;
    uint8 public userEmodeCategoryId;
    uint8 public i;
    string public _marketId;

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
    function supplyCollateral(address asset, uint256 amount) external {
        // TODO: implement
    }

    function withdrawCollateral(address asset, uint256 amount) external {
        // TODO: implement
    }

    function borrow(address asset, uint256 amount) external {
        // TODO: check collateral, update debt
        emit Borrowed(msg.sender, asset, amount);
    }

    function repay(address asset, uint256 amount) external {
        // TODO: implement
    }

    function liquidate(address borrower, address asset, uint256 debtAmount) external {
        // TODO: verify health factor, seize collateral
        emit Liquidated(borrower, msg.sender, debtAmount);
    }

    function getHealthFactor(address user) external view returns (uint256) {
        return 0;
    }

    function setInterestRate(uint256 newRate) external onlyRole {
        // TODO: implement
    }

    function getReservesList(IPoolAddressesProvider provider) external view returns (address[] memory) {
        return 0;
    }

    function getReservesData(IPoolAddressesProvider provider) external view returns (AggregatedReserveData[] memory, BaseCurrencyInfo memory) {
        return 0;
    }

    function getEModes(IPoolAddressesProvider provider) external view returns (Emode[] memory) {
        return 0;
    }

    function getUserReservesData(IPoolAddressesProvider provider,
    address user) external view returns (UserReserveData[] memory, uint8) {
        return 0;
    }

    function initialize(IPoolAddressesProvider provider) public {
        // TODO: set module references
        emit Initialized(msg.sender);
    }

    function getMarketId() external view returns (string memory) {
        return 0;
    }

    function setMarketId(string memory newMarketId) external onlyOwner {
        // TODO: implement
    }

    function getAddress(bytes32 id) public view returns (address) {
        return address(0);
    }

    function setAddress(bytes32 id, address newAddress) external onlyOwner {
        // TODO: implement
    }

    function setAddressAsProxy(bytes32 id,
    address newImplementationAddress) external onlyOwner {
        // TODO: implement
    }

    function getPool() external view returns (address) {
        return address(0);
    }

    function setPoolImpl(address newPoolImpl) external onlyOwner {
        // TODO: implement
    }

}