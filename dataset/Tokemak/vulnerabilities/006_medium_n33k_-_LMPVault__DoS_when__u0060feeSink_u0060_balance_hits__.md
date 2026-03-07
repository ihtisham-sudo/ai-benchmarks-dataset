# n33k - LMPVault: DoS when \u0060feeSink\u0060 balance hits \u0060perWalletLimit\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** LMPVault, DoS, feeSink, perWalletLimit, vulnerability, token share, fees, _collectFees, _mint, _beforeTokenTransfer, balanceOf, updateDebtReporting, rebalance, flashRebalance, function revert, manual review, impact, recommendation, smart contract, Ethereum, security

---

n33k

medium

# LMPVault: DoS when \u0060feeSink\u0060 balance hits \u0060perWalletLimit\u0060
## Summary

The LMPVault token share has a per-wallet limit. LMPVault collects fees as share tokens to the \u0060feeSink\u0060 address. \u0060_collectFees\u0060 will revert if it mints shares that make the \u0060feeSink\u0060 balance hit the \u0060perWalletLimit\u0060.

## Vulnerability Detail

\u0060_collectFees\u0060 mints shares to \u0060feeSink\u0060.

\u0060\u0060\u0060solidity
function _collectFees(uint256 idle, uint256 debt, uint256 totalSupply) internal {
    address sink = feeSink;
    ....
    if (fees > 0 && sink != address(0)) {
        // Calculated separate from other mints as normal share mint is round down
        shares = _convertToShares(fees, Math.Rounding.Up);
        _mint(sink, shares);
        emit Deposit(address(this), sink, fees, shares);
    }
    ....
}
\u0060\u0060\u0060

\u0060_mint\u0060 calls \u0060_beforeTokenTransfer\u0060 internally to check if the target wallet exceeds \u0060perWalletLimit\u0060.

\u0060\u0060\u0060solidity
function _beforeTokenTransfer(address from, address to, uint256 amount) internal virtual override whenNotPaused {
    ....
    if (balanceOf(to) + amount > perWalletLimit) {
        revert OverWalletLimit(to);
    }
}
\u0060\u0060\u0060

\u0060_collectFees\u0060 function will revert if \u0060balanceOf(feeSink) + fee shares > perWalletLimit\u0060. \u0060updateDebtReporting\u0060, \u0060rebalance\u0060 and \u0060flashRebalance\u0060 call \u0060_collectFees\u0060 internally so they will be unfunctional.

## Impact

\u0060updateDebtReporting\u0060, \u0060rebalance\u0060 and \u0060flashRebalance\u0060 won\u0027t be working if \u0060feeSink\u0060 balance hits \u0060perWalletLimit\u0060.

## Code Snippet

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L823

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L849-L851

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L797

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L703

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L727

## Tool used

Manual Review

## Recommendation

Allow \u0060feeSink\u0060 to exceeds \u0060perWalletLimit\u0060.
