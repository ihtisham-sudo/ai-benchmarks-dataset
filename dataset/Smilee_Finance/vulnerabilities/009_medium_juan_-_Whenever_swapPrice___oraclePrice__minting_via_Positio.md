# juan - Whenever swapPrice > oraclePrice, minting via PositionManager will revert, due to not enough funds being obtained from user.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Smilee Finance
**Keywords:** cybersecurity, vulnerability, PositionManager, minting, swapPrice, oraclePrice, obtainedPremium, premiumSwap, denial of service, DVP, premium, insufficient balance, core protocol functionality, manual review, impact, recommendation, price options, contract, service disruption, financial risk

---

juan

high

# Whenever swapPrice > oraclePrice, minting via PositionManager will revert, due to not enough funds being obtained from user.

## Summary
In [\u0060PositionManager::mint()\u0060](https://github.com/sherlock-audit/2024-02-smilee-finance/blob/3241f1bf0c8e951a41dd2e51997f64ef3ec017bd/smilee-v2-contracts/src/periphery/PositionManager.sol#L91-L178), \u0060obtainedPremium\u0060 is calculated in a different way to the actual premium needed, and this will lead to a revert, denying service to users.

## Vulnerability Detail
In [\u0060PositionManager::mint()\u0060](https://github.com/sherlock-audit/2024-02-smilee-finance/blob/3241f1bf0c8e951a41dd2e51997f64ef3ec017bd/smilee-v2-contracts/src/periphery/PositionManager.sol#L91-L178), the PM gets \u0060obtainedPremium\u0060 from \u0060DVP::premium()\u0060:
\u0060\u0060\u0060solidity
(obtainedPremium, ) = dvp.premium(params.strike, params.notionalUp, params.notionalDown);
\u0060\u0060\u0060

Then the actual premium used when minting by the DVP is obtained via the following [code](https://github.com/sherlock-audit/2024-02-smilee-finance/blob/3241f1bf0c8e951a41dd2e51997f64ef3ec017bd/smilee-v2-contracts/src/DVP.sol#L152-L155):
<details>
<summary>Determining option premium</summary>

\u0060\u0060\u0060js
    uint256 swapPrice = _deltaHedgePosition(strike, amount, true);
    uint256 premiumOrac = _getMarketValue(strike, amount, true, IPriceOracle(_getPriceOracle()).getPrice(sideToken, baseToken));
    uint256 premiumSwap = _getMarketValue(strike, amount, true, swapPrice);
    premium_ = premiumSwap > premiumOrac ? premiumSwap : premiumOrac;
\u0060\u0060\u0060
</details>

From the code above, we can see that the actual premium uses the greater of the two price options. However, [\u0060DVP::premium()\u0060](https://github.com/sherlock-audit/2024-02-smilee-finance/blob/3241f1bf0c8e951a41dd2e51997f64ef3ec017bd/smilee-v2-contracts/src/IG.sol#L94-L113) only uses the oracle price to determine the \u0060obtainedPremium\u0060.

This leads to the opportunity for \u0060premiumSwap > premiumOrac\u0060, so in the PositionManager, \u0060obtainedPremium\u0060 is less than the actual premium required to mint the position in the DVP contract.

Thus, when the DVP contract tries to collect the premium from the PositionManager, it will revert due to insufficient balance in the PositionManager:
\u0060\u0060\u0060solidity
IERC20Metadata(baseToken).safeTransferFrom(msg.sender, vault, premium_ + vaultFee);
\u0060\u0060\u0060

## Impact
Whenever \u0060swapPrice > oraclePrice\u0060, minting positions via the PositionManager will revert. This is a denial of service to users and this disruption of core protocol functionality can last extended periods of time.

## Code Snippet
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/3241f1bf0c8e951a41dd2e51997f64ef3ec017bd/smilee-v2-contracts/src/DVP.sol#L152-L155

## Tool used
Manual Review

## Recommendation
When calculating \u0060obtainedPremium\u0060, consider also using the premium from \u0060swapPrice\u0060 if it is greater than the premium calculated from \u0060oraclePrice\u0060.

