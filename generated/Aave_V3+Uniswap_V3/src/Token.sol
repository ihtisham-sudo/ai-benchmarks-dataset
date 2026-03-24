// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title LendingDex — ERC-20 compatible token
 * @dev Synthesised from: Aave_V3, Uniswap_V3
 */
contract LendingDexToken {

    // ── Events ─────────────────────────────────────────────────────
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    // ── Errors ─────────────────────────────────────────────────────
    error InsufficientBalance();
    error InsufficientAllowance();
    error TransferToZeroAddress();

    // ── State ──────────────────────────────────────────────────────
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    address public _referenceAsset;
    address[] public _rewardTokens;
    mapping(address reward => RewardIndexCache cache) public _startIndex;
    address public msgSender;
    uint256 public freshRewards;
    address public rewardToken;
    uint256 public rewardsIndex;
    uint256 public balance;

    // ── Modifiers ──────────────────────────────────────────────────
    modifier onlyRole(bytes32 role) {
        require(hasRole(role, msg.sender), "Missing role");
        _;
    }

    // ── Functions ──────────────────────────────────────────────────
    function transfer(address to, uint256 amount) external returns (bool) {
        // TODO: balance accounting
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        // TODO: balance accounting
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function mint(address to, uint256 amount) external onlyRole {
        // TODO: implement
    }

    function burn(address from, uint256 amount) external onlyRole {
        // TODO: implement
    }

    function claimRewardsOnBehalf(address onBehalfOf,
    address receiver,
    address[] memory rewards) external {
        // TODO: implement
    }

    function claimRewards(address receiver, address[] memory rewards) external {
        // TODO: implement
    }

    function claimRewardsToSelf(address[] memory rewards) external {
        // TODO: implement
    }

    function refreshRewardTokens() public {
        // TODO: implement
    }

    function collectAndUpdateRewards(address reward) public returns (uint256) {
        // TODO: implement
    }

    function isRegisteredRewardToken(address reward) public view returns (bool) {
        return false;
    }

    function getCurrentRewardsIndex(address reward) public view returns (uint256) {
        return 0;
    }

    function getTotalClaimableRewards(address reward) external view returns (uint256) {
        return 0;
    }

    function getClaimableRewards(address user, address reward) external view returns (uint256) {
        return 0;
    }

    function getUnclaimedRewards(address user, address reward) external view returns (uint256) {
        return 0;
    }

    function getReferenceAsset() external view returns (address) {
        return address(0);
    }

    function rewardTokens() external view returns (address[] memory) {
        return 0;
    }

}