# 0x007 - LMPVault.updateDebtReporting could underflow because of subtraction before addition

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, underflow, debt reporting, LMPVault, totalDebt, prevNTotalDebt, afterNTotalDebt, Math.max, currentDebt, ownedShares, sharesToBurn, debtBasis, cachedCurrentDebt, totalSupply, redeem, maxAssetsToPull, Net Asset Value, withdrawals, funds loss

---

0x007

high

# LMPVault.updateDebtReporting could underflow because of subtraction before addition
## Summary
\u0060debt = totalDebt - prevNTotalDebt + afterNTotalDebt\u0060 in [LMPVault._updateDebtReporting](https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L781-L792) could underflow and breaking a core functionality of the protocol.

## Vulnerability Detail
\u0060debt = totalDebt - prevNTotalDebt + afterNTotalDebt\u0060 where prevNTotalDebt equals \u0060(destInfo.currentDebt * originalShares) / Math.max(destInfo.ownedShares, 1)\u0060 and the key to finding a scenario for underflow starts by noting that each value deducted from totalDebt is calculated as \u0060cachedCurrentDebt.mulDiv(sharesToBurn, cachedDvShares, Math.Rounding.Up)\u0060

LMPDebt
\u0060\u0060\u0060solidity
...
L292    totalDebtBurn = cachedCurrentDebt.mulDiv(sharesToBurn, cachedDvShares, Math.Rounding.Up);
...
L440    uint256 currentDebt = (destInfo.currentDebt * originalShares) / Math.max(destInfo.ownedShares, 1);
L448    totalDebtDecrease = currentDebt;
\u0060\u0060\u0060

Let:
\u0060totalDebt = destInfo.currentDebt = destInfo.debtBasis = cachedCurrentDebt = cachedDebtBasis = 11\u0060
\u0060totalSupply = destInfo.ownedShares = cachedDvShares = 10\u0060

That way:
\u0060cachedCurrentDebt * 1 / cachedDvShares = 1.1\u0060 but totalDebtBurn would be rounded up to 2

\u0060sharesToBurn\u0060 could easily be 1 if there was a loss that changes the ratio from \u00601:1.1\u0060 to \u00601:1\u0060. Therefore \u0060currentDvDebtValue = 10 * 1 = 10\u0060

\u0060\u0060\u0060solidity
if (currentDvDebtValue < updatedDebtBasis) {
    // We are currently sitting at a loss. Limit the value we can pull from
    // the destination vault
    currentDvDebtValue = currentDvDebtValue.mulDiv(userShares, totalVaultShares, Math.Rounding.Down);
    currentDvShares = currentDvShares.mulDiv(userShares, totalVaultShares, Math.Rounding.Down);
}

// Shouldn\u0027t pull more than we want
// Or, we\u0027re not in profit so we limit the pull
if (currentDvDebtValue < maxAssetsToPull) {
    maxAssetsToPull = currentDvDebtValue;
}

// Calculate the portion of shares to burn based on the assets we need to pull
// and the current total debt value. These are destination vault shares.
sharesToBurn = currentDvShares.mulDiv(maxAssetsToPull, currentDvDebtValue, Math.Rounding.Up);
\u0060\u0060\u0060

### Steps
* call redeem 1 share and previewRedeem request 1 \u0060maxAssetsToPull\u0060
* 2 debt would be burn
* Therefore totalDebt = 11-2 = 9
* call another redeem 1 share and request another 1 \u0060maxAssetsToPull\u0060
* 2 debts would be burn again and 
* totalDebt would be 7, but prevNTotalDebt = 11 * 8 // 10 = 8

Using 1, 10 and 11 are for illustration and the underflow could occur in several other ways. E.g if we had used \u0060100,001\u0060, \u00601,000,010\u0060 and \u00601,000,011\u0060 respectively.

## Impact
_updateDebtReporting could underflow and break a very important core functionality of the protocol. updateDebtReporting is so critical that funds could be lost if it doesn\u0027t work. Funds could be lost both when the vault is in profit or at loss.

If in profit, users would want to call updateDebtReporting so that they get more asset for their shares (based on the profit).

If in loss, the whole vault asset is locked and withdrawals won\u0027t be successful because the Net Asset Value is not supposed to reduce by such action (noNavDecrease modifier). Net Asset Value has reduced because the loss would reduce totalDebt, but the only way to update the totalDebt record is by calling updateDebtReporting. And those impacted the most are those with large funds. The bigger the fund, the more NAV would decrease by withdrawals.

## Code Snippet
https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L781-L792
https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/libs/LMPDebt.sol#L440-L449
https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/libs/LMPDebt.sol#L295

## Tool used

Manual Review

## Recommendation
Add before subtracting. ETH in circulation is not enough to cause an overflow.

\u0060\u0060\u0060solidity
- debt = totalDebt - prevNTotalDebt + afterNTotalDebt
+ debt = totalDebt + afterNTotalDebt - prevNTotalDebt
\u0060\u0060\u0060

