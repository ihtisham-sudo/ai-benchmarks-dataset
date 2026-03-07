# p0wd3r - ETH deposited by the user may be stolen.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, WETH, ETH, LMPVaultRouterBase, sweepToken, deposit, mint, pullToken, processEthIn, contract, msg.sender, user funds, asset theft, manual review, smart contract, refund, transfer, approval, excess WETH, security recommendation

---

p0wd3r

high

# ETH deposited by the user may be stolen.
## Summary
Due to the fact that the WETH obtained through \u0060_processEthIn\u0060 belongs to the contract, and \u0060pullToken\u0060 transfers assets from \u0060msg.sender\u0060, it is possible for users to transfer excess WETH to the contract, allowing attackers to steal WETH from within the contract using \u0060sweepToken\u0060.

Both \u0060mint\u0060 and \u0060deposit\u0060 in \u0060LMPVaultRouterBase\u0060 have this problem.
## Vulnerability Detail
In the \u0060deposit\u0060 function, if the user pays with ETH, it will first call \u0060_processEthIn\u0060 to wrap it and then call \u0060pullToken\u0060 to transfer.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVaultRouterBase.sol#L43-L57
\u0060\u0060\u0060solidity
    /// @inheritdoc ILMPVaultRouterBase
    function deposit(
        ILMPVault vault,
        address to,
        uint256 amount,
        uint256 minSharesOut
    ) public payable virtual override returns (uint256 sharesOut) {
        // handle possible eth
        _processEthIn(vault);

        IERC20 vaultAsset = IERC20(vault.asset());
        pullToken(vaultAsset, amount, address(this));

        return _deposit(vault, to, amount, minSharesOut);
    }
\u0060\u0060\u0060

\u0060_processEthIn\u0060 will wrap ETH into WETH, and these WETH belong to the contract itself.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVaultRouterBase.sol#L111-L122
\u0060\u0060\u0060solidity
    function _processEthIn(ILMPVault vault) internal {
        // if any eth sent, wrap it first
        if (msg.value > 0) {
            // if asset is not weth, revert
            if (address(vault.asset()) != address(weth9)) {
                revert InvalidAsset();
            }

            // wrap eth
            weth9.deposit{ value: msg.value }();
        }
    }
\u0060\u0060\u0060

However, \u0060pullToken\u0060 transfers from \u0060msg.sender\u0060 and does not use the WETH obtained in \u0060_processEthIn\u0060.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/utils/PeripheryPayments.sol#L54-L56
\u0060\u0060\u0060solidity
    function pullToken(IERC20 token, uint256 amount, address recipient) public payable {
        token.safeTransferFrom(msg.sender, recipient, amount);
    }
\u0060\u0060\u0060

If the user deposits 10 ETH and approves 10 WETH to the contract, when the deposit amount is 10, all of the user\u0027s 20 WETH will be transferred into the contract.

However, due to the \u0060amount\u0060 being 10, only 10 WETH will be deposited into the vault, and the remaining 10 WETH can be stolen by the attacker using \u0060sweepToken\u0060.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/utils/PeripheryPayments.sol#L58-L65
\u0060\u0060\u0060solidity
    function sweepToken(IERC20 token, uint256 amountMinimum, address recipient) public payable {
        uint256 balanceToken = token.balanceOf(address(this));
        if (balanceToken < amountMinimum) revert InsufficientToken();

        if (balanceToken > 0) {
            token.safeTransfer(recipient, balanceToken);
        }
    }
\u0060\u0060\u0060

Both \u0060mint\u0060 and \u0060deposit\u0060 in \u0060LMPVaultRouterBase\u0060 have this problem.

## Impact
ETH deposited by the user may be stolen.
## Code Snippet
- https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVaultRouterBase.sol#L43-L57
- https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/utils/PeripheryPayments.sol#L54-L56
- https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/utils/PeripheryPayments.sol#L58-L65
## Tool used

Manual Review

## Recommendation
Perform operations based on the size of \u0060msg.value\u0060 and \u0060amount\u0060:
1. \u0060msg.value == amount\u0060: transfer WETH from contract not \u0060msg.sender\u0060
2. \u0060msg.value > amount\u0060: transfer WETH from contract not \u0060msg.sender\u0060 and refund to \u0060msg.sender\u0060
3. \u0060msg.value < amount\u0060: transfer WETH from contract and transfer remaining from \u0060msg.sender\u0060
