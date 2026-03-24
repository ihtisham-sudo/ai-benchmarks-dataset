// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ISecureTokenToken {

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
    function version() external view returns (uint8);
    function publicVersion() external view returns (string memory);
    function initialize(address owner,
        string memory _name,
        string memory _symbol,
        ITransferRestrictor _transferRestrictor) external;
    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function transferRestrictor() external view returns (ITransferRestrictor);
    function balancePerShare() external view returns (uint128);
    function setName(string calldata newName) external;
    function setSymbol(string calldata newSymbol) external;
    function setBalancePerShare(uint128 balancePerShare_) external;
    function setTransferRestrictor(ITransferRestrictor newRestrictor) external;
    function burnFrom(address account, uint256 value) external;
}