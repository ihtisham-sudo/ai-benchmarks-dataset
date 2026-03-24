// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISecureTokenAccessControl {

    event RoleGranted(bytes32 indexed role, address indexed account, address indexed sender);
    event RoleRevoked(bytes32 indexed role, address indexed account, address indexed sender);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    error Unauthorized();
    error ZeroAddress();
    error AlreadyHasRole(bytes32 role, address account);

    function initialize(address _owner) external;
    function grantRole(bytes32 role, address account) external;
    function revokeRole(bytes32 role, address account) external;
    function hasRole(bytes32 role, address account) external view returns (bool);
    function transferOwnership(address newOwner) external;
    function version() external returns (uint8);
    function publicVersion() external returns (string memory);
    function attestGitCommitHash(bytes20 gitCommitHash, bool ciPassed) external;
    function gitCommitHashAttested(bytes20 gitCommitHash) external view returns (bool);
    function setBufferSize(uint8 newSize) external;
    function concludeEpoch(address[] calldata futureCommittee) external;
    function applyIncentives(RewardInfo[] calldata rewardInfos) external;
    function applySlashes(Slash[] calldata slashes) external;
    function setNextCommitteeSize(uint16 newSize) external;
    function getNextCommitteeSize() external view returns (uint16);
}