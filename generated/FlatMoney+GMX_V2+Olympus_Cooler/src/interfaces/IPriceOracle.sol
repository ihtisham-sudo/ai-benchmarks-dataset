// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISyntheticVaultOracle {

    event FeedSet(address indexed token, address indexed feed);
    event FeedRemoved(address indexed token);

    error StalePriceFeed();
    error NoFeedSet(address token);
    error InvalidPrice();

    function getPrice(address token) external view returns (uint256 price);
    function setFeed(address token, address feed) external;
    function removeFeed(address token) external;
    function getPriceInETH(address token) external view returns (uint256);
    function initialize(address owner_, IPyth pythContract_) external;
    function updatePythPrice(address sender_, bytes[] calldata priceUpdateData_) external payable;
    function getOracleData(address asset_) external view returns (OracleModuleStructs.OracleData memory oracleData_);
    function setOracles(address asset_,
        OracleModuleStructs.OnchainOracle calldata onchainOracle_,
        OracleModuleStructs.OffchainOracle calldata offchainOracle_) external;
    function setMaxDiffPercent(address asset_, uint64 maxDiffPercent_) external;
    function setAssetAndOracles(address _asset,
        FlatcoinStructs.OnchainOracle calldata _onchainOracle,
        FlatcoinStructs.OffchainOracle calldata _offchainOracle) external;
    function latestRoundData() external view returns (uint80 roundId, int256 answer, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound);
    function getOraclePrice(address token,
        bytes memory) external view returns (OracleUtils.ValidatedPrice memory);
    function validateSequencerUp() external view;
    function setPrices(OracleUtils.SetPricesParams memory params) external;
    function setPricesForAtomicAction(OracleUtils.SetPricesParams memory params) external;
    function setPrimaryPrice(address token, Price.Props memory price) external;
}