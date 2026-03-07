# xiaoming90 - \u0060navPerShareHighMark\u0060 not reset to 1.0

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, navPerShareHighMark, LMPVault, fee collection, totalAssets, totalSupply, currentNavPerShare, effectiveNavPerShareHighMark, withdrawal, shares, investment, profitability, rebalancing strategies, loss of fee, protocol integrity, manual review, security recommendation, vault exit, asset management

---

xiaoming90

high

# \u0060navPerShareHighMark\u0060 not reset to 1.0
## Summary

The \u0060navPerShareHighMark\u0060 was not reset to 1.0 when a vault had been fully exited, leading to a loss of fee.

## Vulnerability Detail

The LMPVault will only collect fees if the current NAV (\u0060currentNavPerShare\u0060) is more than the last NAV (\u0060effectiveNavPerShareHighMark\u0060).

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L800

\u0060\u0060\u0060solidity
File: LMPVault.sol
800:     function _collectFees(uint256 idle, uint256 debt, uint256 totalSupply) internal {
801:         address sink = feeSink;
802:         uint256 fees = 0;
803:         uint256 shares = 0;
804:         uint256 profit = 0;
805: 
806:         // If there\u0027s no supply then there should be no assets and so nothing
807:         // to actually take fees on
808:         if (totalSupply == 0) {
809:             return;
810:         }
811: 
812:         uint256 currentNavPerShare = ((idle + debt) * MAX_FEE_BPS) / totalSupply;
813:         uint256 effectiveNavPerShareHighMark = navPerShareHighMark;
814: 
815:         if (currentNavPerShare > effectiveNavPerShareHighMark) {
816:             // Even if we aren\u0027t going to take the fee (haven\u0027t set a sink)
817:             // We still want to calculate so we can emit for off-chain analysis
818:             profit = (currentNavPerShare - effectiveNavPerShareHighMark) * totalSupply;
\u0060\u0060\u0060

Assume the current LMPVault state is as follows:

- totalAssets = 15 WETH
- totalSupply = 10 shares
- NAV/share = 1.5
- effectiveNavPerShareHighMark = 1.5

Alice owned all the remaining shares in the vault, and she decided to withdraw all her 10 shares. As a result, the \u0060totalAssets\u0060 and \u0060totalSupply\u0060 become zero. It was found that when all the shares have been exited, the \u0060effectiveNavPerShareHighMark\u0060 is not automatically reset to 1.0.

Assume that at some point later, other users started to deposit into the LMPVault, and the vault invests the deposited WETH to profitable destination vaults, resulting in the real/actual NAV rising from 1.0 to 1.49 over a period of time.

The system is designed to collect fees when there is a rise in NAV due to profitable investment from sound rebalancing strategies. However, since the \u0060effectiveNavPerShareHighMark\u0060 has been set to 1.5 previously, no fee is collected when the NAV rises from 1.0 to 1.49, resulting in a loss of fee.

## Impact

Loss of fee. Fee collection is an integral part of the protocol; thus the loss of fee is considered a High issue.

## Code Snippet

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L448

## Tool used

Manual Review

## Recommendation

Consider resetting the \u0060navPerShareHighMark\u0060 to 1.0 whenever a vault has been fully exited.

\u0060\u0060\u0060diff
function _withdraw(
    uint256 assets,
    uint256 shares,
    address receiver,
    address owner
) internal virtual returns (uint256) {
..SNIP..
    _burn(owner, shares);
    
+	if (totalSupply() == 0) navPerShareHighMark = MAX_FEE_BPS;

    emit Withdraw(msg.sender, receiver, owner, returnedAssets, shares);

    _baseAsset.safeTransfer(receiver, returnedAssets);

    return returnedAssets;
}
\u0060\u0060\u0060
