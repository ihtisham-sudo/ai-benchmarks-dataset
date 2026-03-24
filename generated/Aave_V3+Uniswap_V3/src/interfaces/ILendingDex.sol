// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ILendingDex {

    event Initialized(address indexed initializer);

    error AlreadyInitialized();
    error NotInitialized();

    function initialize(address _accesscontrol, address _token, address _vault, address _lendingpool, address _swaprouter, address _oracle) external;
}