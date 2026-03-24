// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ILendingDexToken {

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
    function claimRewardsOnBehalf(address onBehalfOf,
    address receiver,
    address[] memory rewards) external;
    function claimRewards(address receiver, address[] memory rewards) external;
    function claimRewardsToSelf(address[] memory rewards) external;
    function refreshRewardTokens() external;
    function collectAndUpdateRewards(address reward) external returns (uint256);
    function isRegisteredRewardToken(address reward) external view returns (bool);
    function getCurrentRewardsIndex(address reward) external view returns (uint256);
    function getTotalClaimableRewards(address reward) external view returns (uint256);
    function getClaimableRewards(address user, address reward) external view returns (uint256);
    function getUnclaimedRewards(address user, address reward) external view returns (uint256);
    function getReferenceAsset() external view returns (address);
    function rewardTokens() external view returns (address[] memory);
}