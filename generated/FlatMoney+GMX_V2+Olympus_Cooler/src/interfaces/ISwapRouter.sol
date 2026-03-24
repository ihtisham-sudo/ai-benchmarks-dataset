// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISyntheticVaultSwapRouter {

    event Swap(address indexed sender, uint256 amountIn, uint256 amountOut, address indexed tokenIn, address indexed tokenOut);

    error InsufficientOutputAmount();
    error ExcessiveInputAmount();
    error InvalidPath();

    function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to) external returns (uint256 amountOut);
    function swapTokensForExactTokens(uint256 amountOut, uint256 amountInMax, address[] calldata path, address to) external returns (uint256 amountIn);
    function swapExactETHForTokens(uint256 amountOutMin, address[] calldata path, address to) external payable returns (uint256 amountOut);
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) external pure returns (uint256);
    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory);
    function setFee(uint256 numerator, uint256 denominator) external;
    function getRouter(bytes32 routerKey_) external view returns (address routerAddress_);
    function initialize(address owner_, address permit2_, IWETH wrappedNativeToken_) external;
    function swap(InOutData calldata swapStruct_) external payable;
    function addRouter(bytes32 routerKey_, address router_) external;
    function removeRouter(bytes32 routerKey_) external;
    function rescueFunds(IERC20 token_, address to_, uint256 amount_) external;
    function setWrappedNativeToken(IWETH wrappedNativeToken_) external;
    function claimFundingFees(IRelayUtils.RelayParams calldata relayParams,
        address account,
        uint256 srcChainId,
        address[] memory markets,
        address[] memory tokens,
        address receiver) external returns (uint256[] memory);
    function claimCollateral(IRelayUtils.RelayParams calldata relayParams,
        address account,
        uint256 srcChainId,
        address[] memory markets,
        address[] memory tokens,
        uint256[] memory timeKeys,
        address receiver) external returns (uint256[] memory);
    function claimAffiliateRewards(IRelayUtils.RelayParams calldata relayParams,
        address account,
        uint256 srcChainId,
        address[] memory markets,
        address[] memory tokens,
        address receiver) external returns (uint256[] memory);
    function createGlvDeposit(IRelayUtils.RelayParams calldata relayParams,
        address account,
        uint256 srcChainId,
        IRelayUtils.TransferRequests calldata transferRequests,
        IGlvDepositUtils.CreateGlvDepositParams memory params) external returns (bytes32);
    function createGlvWithdrawal(IRelayUtils.RelayParams calldata relayParams,
        address account,
        uint256 srcChainId,
        IRelayUtils.TransferRequests calldata transferRequests,
        IGlvWithdrawalUtils.CreateGlvWithdrawalParams memory params) external returns (bytes32);
}