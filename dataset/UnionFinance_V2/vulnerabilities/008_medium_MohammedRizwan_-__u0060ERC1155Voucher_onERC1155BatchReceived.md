# MohammedRizwan - \u0060ERC1155Voucher.onERC1155BatchReceived()\u0060 does not check the caller is the valid token therefore any unregistered token can invoke \u0060onERC1155BatchReceived()\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** ERC1155, vulnerability, onERC1155BatchReceived, onERC1155Received, smart contract, token validation, unregistered token, deposit, vouch, contract owner, msg.sender, valid token, invalid token, protocol design, safeTransferFrom, safeBatchTransferFrom, manual review, security check, bypass, recommendation

---

MohammedRizwan

Medium

# \u0060ERC1155Voucher.onERC1155BatchReceived()\u0060 does not check the caller is the valid token therefore any unregistered token can invoke \u0060onERC1155BatchReceived()\u0060

## Summary
\u0060ERC1155Voucher.onERC1155BatchReceived()\u0060 does not check the caller is the valid token therefore any unregistered token can invoke \u0060onERC1155BatchReceived()\u0060

## Vulnerability Detail
\u0060ERC1155Voucher.sol\u0060 is the voucher contract that takes \u0060ERC1155\u0060 tokens as deposits and gives a vouch. An ERC1155 token can invoke  two safe methods:

1) \u0060onERC1155Received()\u0060 and
2) \u0060onERC1155BatchReceived()\u0060

An ERC1155-compliant smart contract must call above functions on the token recipient contract, at the end of a \u0060safeTransferFrom\u0060 and \u0060safeBatchTransferFrom\u0060 respectively, after the balance has been updated.

The \u0060ERC1155Voucher\u0060 contract owner can set the valid token i.e ERC1155 token which can invoke both \u0060onERC1155Received()\u0060 and \u0060onERC1155BatchReceived()\u0060 functions.

\u0060\u0060\u0060solidity
    mapping(address => bool) public isValidToken;
    
    
    function setIsValid(address token, bool isValid) external onlyOwner {
        isValidToken[token] = isValid;
        emit SetIsValidToken(token, isValid);
    }
\u0060\u0060\u0060

The valid token i.e msg.sender calling the \u0060onERC1155Received()\u0060 is checked in \u0060ERC1155Voucher.onERC1155Received()\u0060 function

\u0060\u0060\u0060solidity
    function onERC1155Received(
        address operator,
        address from,
        uint256 id,
        uint256 value,
        bytes calldata data
    ) external returns (bytes4) {
@>        require(isValidToken[msg.sender], "!valid token");
        _vouchFor(from);
        return bytes4(keccak256("onERC1155Received(address,address,uint256,uint256,bytes)"));
    }
\u0060\u0060\u0060
This means that only the valid tokens set by contract owner can invoke the \u0060ERC1155Voucher.onERC1155Received()\u0060  function. However, this particular check is missing in \u0060ERC1155Voucher.onERC1155BatchReceived()\u0060 function.

\u0060\u0060\u0060solidity
    function onERC1155BatchReceived(
        address operator,
        address from,
        uint256[] calldata ids,
        uint256[] calldata values,
        bytes calldata data
    ) external returns (bytes4) {
        _vouchFor(from);
        return bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)"));
    }
\u0060\u0060\u0060
\u0060onERC1155BatchReceived()\u0060 does not check the \u0060isValidToken[msg.sender]\u0060 which means any ERC1155 token can call \u0060ERC1155Voucher.onERC1155BatchReceived()\u0060 to deposit the ERC1155 to receive the vouch. This is not intended behaviour by protocol and would break the intended design of setting valid tokens by contract owner. Any in-valid tokens can easily call \u0060onERC1155BatchReceived()\u0060 and can bypass the check at [L-109](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/peripheral/ERC1155Voucher.sol#L109) implemented in \u0060onERC1155Received()\u0060 function.

## Impact
Any in-valid or unregistered ERC1155 token can invoke the \u0060onERC1155BatchReceived()\u0060 function which would make the check at L-109 of \u0060onERC1155Received()\u0060 useless as batch function would allow to deposit ERC1155 to receive the vouch therefore bypassing the L-109 check in \u0060onERC1155Received()\u0060. This would break the design of protocol as valid tokens as msg.sender are not checked in \u0060onERC1155BatchReceived()\u0060.

## Code Snippet
https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/peripheral/ERC1155Voucher.sol#L121

## Tool used
Manual Review

## Recommendation
Consider checking \u0060isValidToken[msg.sender]\u0060 in \u0060onERC1155BatchReceived()\u0060 to invoke it from registered valid token only.

Consider below changes:

\u0060\u0060\u0060diff
    function onERC1155BatchReceived(
        address operator,
        address from,
        uint256[] calldata ids,
        uint256[] calldata values,
        bytes calldata data
    ) external returns (bytes4) {
+       require(isValidToken[msg.sender], "!valid token");
        _vouchFor(from);
        return bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)"));
    }
\u0060\u0060\u0060
