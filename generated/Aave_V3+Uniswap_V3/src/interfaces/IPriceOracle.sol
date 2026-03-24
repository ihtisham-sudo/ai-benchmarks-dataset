// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ILendingDexOracle {

    event FeedSet(address indexed token, address indexed feed);
    event FeedRemoved(address indexed token);

    error StalePriceFeed();
    error NoFeedSet(address token);
    error InvalidPrice();

    function getPrice(address token) external view returns (uint256 price);
    function setFeed(address token, address feed) external;
    function removeFeed(address token) external;
    function getPriceInETH(address token) external view returns (uint256);
    function setAssetSources(address[] calldata assets,
    address[] calldata sources) external;
    function setFallbackOracle(address fallbackOracle) external;
    function getAssetPrice(address asset) external view returns (uint256);
    function getAssetsPrices(address[] calldata assets) external view returns (uint256[] memory);
    function getSourceOfAsset(address asset) external view returns (address);
    function getFallbackOracle() external view returns (address);
    function isBorrowAllowed() external view returns (bool);
    function isLiquidationAllowed() external view returns (bool);
    function setSequencerOracle(address newSequencerOracle) external;
    function setGracePeriod(uint256 newGracePeriod) external;
    function getSequencerOracle() external view returns (address);
    function getGracePeriod() external view returns (uint256);
}