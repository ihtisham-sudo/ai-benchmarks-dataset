// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISyntheticVaultToken {

    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    error InsufficientBalance();
    error InsufficientAllowance();
    error TransferToZeroAddress();

    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
    function initialize(IERC20Metadata collateral_,
        address protocolFeeRecipient_,
        uint64 protocolFeePercentage_,
        uint64 leverageTradingFee_,
        uint64 stableWithdrawFee_,
        uint256 maxDeltaError_,
        uint256 skewFractionMax_,
        uint256 stableCollateralCap_,
        uint256 maxPositions_) external;
    function sendCollateral(address to_, uint256 amount_) external;
    function setPosition(LeverageModuleStructs.Position calldata newPosition_,
        uint256 tokenId_) external;
    function deletePosition(uint256 tokenId_) external;
    function updateStableCollateralTotal(int256 stableCollateralAdjustment_) external;
    function updateGlobalMargin(int256 marginDelta_) external;
    function updateGlobalPositionData(uint256 price_,
        int256 marginDelta_,
        int256 additionalSizeDelta_) external;
    function isPositionOpenWhitelisted(address account_) external view returns (bool whitelisted_);
    function isMaxPositionsReached() external view returns (bool maxReached_);
    function getMaxPositionIds() external view returns (uint256[] memory openPositionIds_);
    function getPosition(uint256 tokenId_) external view returns (LeverageModuleStructs.Position memory positionDetails_);
    function getGlobalPositions() external view returns (FlatcoinVaultStructs.GlobalPositions memory globalPositionsDetails_);
}