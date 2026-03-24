// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISecureTokenSwapRouter {

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
    function version() external view returns (uint8);
    function publicVersion() external view returns (string memory);
    function initialize(address initialOwner, address upgrader) external;
    function reinitialize(address upgrader) external;
    function fillOrder(address orderProcessor,
        address vault,
        IOrderProcessor.Order calldata order,
        uint256 fillAmount,
        uint256 receivedAmount,
        uint256 fees) external;
    function cancelBuyOrder(address orderProcessor,
        IOrderProcessor.Order calldata order,
        address vault,
        uint256 orderId,
        string calldata reason) external;
}