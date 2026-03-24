// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISecureToken {

    event Initialized(address indexed initializer);

    error AlreadyInitialized();
    error NotInitialized();

    function initialize(address _accesscontrol, address _token, address _swaprouter) external;
}