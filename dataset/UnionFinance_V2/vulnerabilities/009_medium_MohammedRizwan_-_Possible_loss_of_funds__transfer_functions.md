# MohammedRizwan - Possible loss of funds, transfer functions can silently fail

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** cybersecurity, vulnerability, loss of funds, transfer functions, ERC20, transferFrom, USDT, USDC, DAI, Ethereum, EVM compatible, VouchFaucet, claimTokens, transferERC20, ERC1155Voucher, transfer, boolean value, EIP20 standard, silent failure, OpenZeppelin

---

MohammedRizwan

Medium

# Possible loss of funds, transfer functions can silently fail

## Summary
Possible loss of funds, transfer functions can silently fail

## Vulnerability Detail
\u0060Union\u0060 Protocol\u0027s contracts are expected to be used USDT, USDC and DAI. The contracts will be deployed on Any EVM compatible chain which also includes Ethereum mainnet itself. Both of these details are mentioned in contest readme. This issue is specifically for tokens like USDT and similar tokens etc on Ethereum mainnet.

The following functions makes use of ERC20\u0027s \u0060transferFrom()\u0060 in following contracts:

1) In \u0060VouchFaucet.sol\u0060, the \u0060claimTokens()\u0060 is called by users to claim the tokens and the token is transferred to user but the transfer return value is not checked and similarly in case of \u0060transferERC20()\u0060 function.

\u0060\u0060\u0060solidity
    function claimTokens(address token, uint256 amount) external {
        require(claimedTokens[token][msg.sender] <= maxClaimable[token], "amount>max");
@>        IERC20(token).transfer(msg.sender, amount);     @audit // unchecked transfer return value 
        emit TokensClaimed(msg.sender, token, amount);
    }


    function transferERC20(address token, address to, uint256 amount) external onlyOwner {
@>        IERC20(token).transfer(to, amount);                @audit // unchecked transfer return value 
    }
\u0060\u0060\u0060

2) In \u0060ERC1155Voucher.transferERC20()\u0060, tokens are being transferred to recipient address and return value is not checked.

\u0060\u0060\u0060solidity
    function transferERC20(address token, address to, uint256 amount) external onlyOwner {
@>        IERC20(token).transfer(to, amount);            @audit // unchecked transfer return value 
    }
\u0060\u0060\u0060 
The issue here is with the use of unsafe \u0060transfer()\u0060 function. The \u0060ERC20.transfer()\u0060 function return a boolean value indicating success. This parameter needs to be checked for success. Some tokens do not revert if the transfer failed but return false instead.

Some tokens like \u0060USDT\u0060 don\u0027t correctly implement the EIP20 standard and their transfer() function return void instead of a success boolean. Calling these functions with the correct EIP20 function signatures will always revert.

Tokens that don\u0027t actually perform the transfer and return false are still counted as a correct transfer and tokens that don\u0027t correctly implement the latest EIP20 spec, like USDT, will be unusable in the protocol as they revert the transaction because of the missing return value. There could be silent failure in transfer which may lead to loss of user funds in \u0060ERC1155Voucher.transferERC20()\u0060 and \u0060VouchFaucet.claimTokens()\u0060

## Impact
Tokens that don\u0027t actually perform the transfer and return false are still counted as a correct transfer and tokens that don\u0027t correctly implement the latest EIP20 spec will be unusable in the protocol as they revert the transaction because of the missing return value. This will lead to loss of user funds.

## Code Snippet
https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/peripheral/VouchFaucet.sol#L95

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/peripheral/VouchFaucet.sol#L124

## Tool used
Manual Review

## Recommendation
Use OpenZeppelin\u0027s SafeERC20 versions with the \u0060safeTransfer()\u0060 function instead of \u0060transfer()\u0060.

For example, consider below changes in \u0060VouchFaucet.sol\u0060:

\u0060\u0060\u0060diff
+ import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract VouchFaucet is Ownable {

+      using SafeERC20 for IERC20;

    function claimTokens(address token, uint256 amount) external {
        require(claimedTokens[token][msg.sender] <= maxClaimable[token], "amount>max");
-        IERC20(token).transfer(msg.sender, amount);     
+       IERC20(token).safeTransfer(msg.sender, amount);    
        emit TokensClaimed(msg.sender, token, amount);
    }


    function transferERC20(address token, address to, uint256 amount) external onlyOwner {
-        IERC20(token).transfer(to, amount);              
+        IERC20(token).safeTransfer(to, amount);    
    }
\u0060\u0060\u0060
