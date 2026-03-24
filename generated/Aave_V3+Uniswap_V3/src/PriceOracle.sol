// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title LendingDex — On-chain price oracle with staleness check
 * @dev Synthesised from: Aave_V3, Uniswap_V3
 */
contract LendingDexOracle {

    // ── Events ─────────────────────────────────────────────────────
    event FeedSet(address indexed token, address indexed feed);
    event FeedRemoved(address indexed token);

    // ── Errors ─────────────────────────────────────────────────────
    error StalePriceFeed();
    error NoFeedSet(address token);
    error InvalidPrice();

    // ── State ──────────────────────────────────────────────────────
    mapping(address => address) public feeds;
    uint256 public stalenessThreshold;
    mapping(address => AggregatorInterface) public assetsSources;
    int256 public price;
    uint256 public _gracePeriod;
    address public aaveOracle;

    // ── Modifiers ──────────────────────────────────────────────────
    modifier onlyAssetListingOrPoolAdmins() {
        _;
    }
    modifier onlyPoolAdmin() {
        _;
    }
    modifier onlyRiskOrPoolAdmins() {
        _;
    }
    modifier onlyRole(bytes32 role) {
        require(hasRole(role, msg.sender), "Missing role");
        _;
    }

    // ── Functions ──────────────────────────────────────────────────
    function getPrice(address token) external view returns (uint256 price) {
        return 0;
    }

    function setFeed(address token, address feed) external onlyRole {
        // TODO: implement
    }

    function removeFeed(address token) external onlyRole {
        // TODO: implement
    }

    function getPriceInETH(address token) external view returns (uint256) {
        return 0;
    }

    function setAssetSources(address[] calldata assets,
    address[] calldata sources) external onlyAssetListingOrPoolAdmins {
        // TODO: implement
    }

    function setFallbackOracle(address fallbackOracle) external onlyAssetListingOrPoolAdmins {
        // TODO: implement
    }

    function getAssetPrice(address asset) public view returns (uint256) {
        return 0;
    }

    function getAssetsPrices(address[] calldata assets) external view returns (uint256[] memory) {
        return 0;
    }

    function getSourceOfAsset(address asset) external view returns (address) {
        return address(0);
    }

    function getFallbackOracle() external view returns (address) {
        return address(0);
    }

    function isBorrowAllowed() external view returns (bool) {
        return false;
    }

    function isLiquidationAllowed() external view returns (bool) {
        return false;
    }

    function setSequencerOracle(address newSequencerOracle) external onlyPoolAdmin {
        // TODO: implement
    }

    function setGracePeriod(uint256 newGracePeriod) external onlyRiskOrPoolAdmins {
        // TODO: implement
    }

    function getSequencerOracle() external view returns (address) {
        return address(0);
    }

    function getGracePeriod() external view returns (uint256) {
        return 0;
    }

}