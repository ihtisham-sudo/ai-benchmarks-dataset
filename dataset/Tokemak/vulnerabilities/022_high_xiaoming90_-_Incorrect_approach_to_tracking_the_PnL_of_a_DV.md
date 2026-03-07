# xiaoming90 - Incorrect approach to tracking the PnL of a DV

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, PnL tracking, debt value, loss marking, DV shares, vault shareholders, rebalancing, LP tokens, current debt value, updated debt basis, profit and loss, manual review, risk assessment, financial loss, token burning, asset management, smart contracts, decentralized finance, security recommendations

---

xiaoming90

high

# Incorrect approach to tracking the PnL of a DV
## Summary

A DV might be incorrectly marked as not sitting in a loss, thus allowing users to burn all the DV shares, locking in all the loss of the DV and the vault shareholders.

## Vulnerability Detail

Let $DV_A$ be a certain destination vault.

Assume that at $T0$, the current debt value (\u0060currentDvDebtValue\u0060) of $DV_A$ is 95 WETH, and the last debt value (\u0060updatedDebtBasis\u0060) is 100 WETH. Since the current debt value has become smaller than the last debt value, the vault is making a loss of 5 WETH since the last rebalancing, so $DV_A$ is sitting at a loss, and users can only burn a limited amount of DestinationVault_A\u0027s shares.

Assume that at $T1$, there is some slight rebalancing performed on $DV_A$, and a few additional LP tokens are deposited to it. Thus, its current debt value increased to 98 WETH. At the same time, the \u0060destInfo.debtBasis\u0060 and \u0060destInfo.ownedShares\u0060 will be updated to the current value. 

Immediately after the rebalancing, $DV_A$ will not be considered sitting in a loss since the \u0060currentDvDebtValue\u0060 and \u0060updatedDebtBasis\u0060 should be equal now. As a result, users could now burn all the $DV_A$ shares of the LMPVault during withdrawal.

$DV_A$ suddenly becomes not sitting at a loss even though the fact is that it is still sitting at a loss of 5 WETH. The loss has been written off.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/libs/LMPDebt.sol#L275

\u0060\u0060\u0060solidity
File: LMPDebt.sol
274:         // Neither of these numbers include rewards from the DV
275:         if (currentDvDebtValue < updatedDebtBasis) {
276:             // We are currently sitting at a loss. Limit the value we can pull from
277:             // the destination vault
278:             currentDvDebtValue = currentDvDebtValue.mulDiv(userShares, totalVaultShares, Math.Rounding.Down);
279:             currentDvShares = currentDvShares.mulDiv(userShares, totalVaultShares, Math.Rounding.Down);
280:         }
\u0060\u0060\u0060

## Impact

A DV might be incorrectly marked as not sitting in a loss, thus allowing users to burn all the DV shares, locking in all the loss of the DV and the vault shareholders.

## Code Snippet

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/libs/LMPDebt.sol#L275

## Tool used

Manual Review

## Recommendation

Consider a more sophisticated approach to track a DV\u0027s Profit and Loss (PnL). 

In our example, $DV_A$ should only be considered not making a loss if the price of the LP tokens starts to appreciate and cover the loss of 5 WETH.
