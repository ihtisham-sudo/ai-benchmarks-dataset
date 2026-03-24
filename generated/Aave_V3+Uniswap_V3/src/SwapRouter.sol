// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title LendingDex — Token swap router
 * @dev Synthesised from: Aave_V3, Uniswap_V3
 */
contract LendingDexSwapRouter {

    // ── Events ─────────────────────────────────────────────────────
    event Swap(address indexed sender, uint256 amountIn, uint256 amountOut, address indexed tokenIn, address indexed tokenOut);

    // ── Errors ─────────────────────────────────────────────────────
    error InsufficientOutputAmount();
    error ExcessiveInputAmount();
    error InvalidPath();

    // ── State ──────────────────────────────────────────────────────
    address public factory;
    address public weth;
    uint256 public feeNumerator;
    uint256 public feeDenominator;
    int24 public tickSpacing;

    // ── Modifiers ──────────────────────────────────────────────────
    modifier noDelegateCall() {
        _;
    }
    modifier onlyRole(bytes32 role) {
        require(hasRole(role, msg.sender), "Missing role");
        _;
    }
    modifier pool() {
        _;
    }

    // ── Functions ──────────────────────────────────────────────────
    function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to) external returns (uint256 amountOut) {
        // TODO: compute amounts via AMM formula
        emit Swap(msg.sender, 0, 0, path[0], path[path.length-1]);
        return 0;
    }

    function swapTokensForExactTokens(uint256 amountOut, uint256 amountInMax, address[] calldata path, address to) external returns (uint256 amountIn) {
        // TODO: compute amounts via AMM formula
        emit Swap(msg.sender, 0, 0, path[0], path[path.length-1]);
        return 0;
    }

    function swapExactETHForTokens(uint256 amountOutMin, address[] calldata path, address to) external payable returns (uint256 amountOut) {
        // TODO: compute amounts via AMM formula
        emit Swap(msg.sender, 0, 0, path[0], path[path.length-1]);
        return 0;
    }

    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) public pure returns (uint256) {
        return 0;
    }

    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory) {
        return 0;
    }

    function setFee(uint256 numerator, uint256 denominator) external onlyRole {
        // TODO: implement
    }

    function createPool(address tokenA,
        address tokenB,
        uint24 fee) external noDelegateCall pool returns (address pool) {
        // TODO: implement
    }

    function setOwner(address _owner) external {
        // TODO: implement
    }

    function enableFeeAmount(uint24 fee, int24 tickSpacing) public {
        // TODO: implement
    }

}