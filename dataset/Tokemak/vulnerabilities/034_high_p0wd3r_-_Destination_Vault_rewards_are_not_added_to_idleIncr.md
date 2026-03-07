# p0wd3r - Destination Vault rewards are not added to idleIncrease when info.totalAssetsPulled > info.totalAssetsToPull

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, Destination Vault, rewards, idleIncrease, totalAssetsPulled, totalAssetsToPull, LMPVault, withdraw function, asset balance, contract freeze, recover function, baseAsset, manual review, code snippet, impact analysis, asset management, smart contract, decentralized finance, security recommendation

---

p0wd3r

high

# Destination Vault rewards are not added to idleIncrease when info.totalAssetsPulled > info.totalAssetsToPull
## Summary
Destination Vault rewards are not added to \u0060idleIncrease\u0060 when \u0060info.totalAssetsPulled > info.totalAssetsToPull\u0060 in \u0060_withdraw\u0060 of \u0060LMPVault\u0060.

This result in rewards not being recorded by \u0060LMPVault\u0060 and ultimately frozen in the contract.
## Vulnerability Detail
In the \u0060_withdraw\u0060 function, Destination Vault rewards will be first recorded in \u0060info.IdleIncrease\u0060 by \u0060info.idleIncrease += _baseAsset.balanceOf(address(this)) - assetPreBal - assetPulled;\u0060.

But when \u0060info.totalAssetsPulled > info.totalAssetsToPull\u0060, \u0060info.idleIncrease\u0060 is directly assigned as \u0060info.totalAssetsPulled - info.totalAssetsToPull\u0060, and \u0060info.totalAssetsPulled\u0060 is \u0060assetPulled\u0060 without considering Destination Vault rewards.

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L482-L497
\u0060\u0060\u0060solidity
                uint256 assetPreBal = _baseAsset.balanceOf(address(this));
                uint256 assetPulled = destVault.withdrawBaseAsset(sharesToBurn, address(this));

                // Destination Vault rewards will be transferred to us as part of burning out shares
                // Back into what that amount is and make sure it gets into idle
                info.idleIncrease += _baseAsset.balanceOf(address(this)) - assetPreBal - assetPulled;
                info.totalAssetsPulled += assetPulled;
                info.debtDecrease += totalDebtBurn;

                // It\u0027s possible we\u0027ll get back more assets than we anticipate from a swap
                // so if we do, throw it in idle and stop processing. You don\u0027t get more than we\u0027ve calculated
                if (info.totalAssetsPulled > info.totalAssetsToPull) {
                    info.idleIncrease = info.totalAssetsPulled - info.totalAssetsToPull;
                    info.totalAssetsPulled = info.totalAssetsToPull;
                    break;
                }
\u0060\u0060\u0060

For example,
\u0060\u0060\u0060solidity
                    // preBal == 100 pulled == 10 reward == 5 toPull == 6
                    // idleIncrease = 115 - 100 - 10 == 5
                    // totalPulled(0) += assetPulled == 10 > toPull
                    // idleIncrease = totalPulled - toPull == 4 < reward
\u0060\u0060\u0060

The final \u0060info.idleIncrease\u0060 does not record the reward, and these assets are not ultimately recorded by the Vault.

## Impact
The final \u0060info.idleIncrease\u0060 does not record the reward, and these assets are not ultimately recorded by the Vault.

Meanwhile, due to the \u0060recover\u0060 function\u0027s inability to extract the \u0060baseAsset\u0060, this will result in no operations being able to handle these Destination Vault rewards, ultimately causing these assets to be frozen within the contract.
## Code Snippet
https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L482-L497
## Tool used

Manual Review

## Recommendation
\u0060info.idleIncrease = info.totalAssetsPulled - info.totalAssetsToPull;\u0060 -> \u0060info.idleIncrease += info.totalAssetsPulled - info.totalAssetsToPull;\u0060
