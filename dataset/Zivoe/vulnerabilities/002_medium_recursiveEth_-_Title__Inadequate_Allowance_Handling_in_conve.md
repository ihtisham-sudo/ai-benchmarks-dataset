# recursiveEth - Title: Inadequate Allowance Handling in convertAndForward Function of \u0060OCT_DAO\u0060 & \u0060OCT_YDL\u0060.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cybersecurity, vulnerability, inadequate allowance handling, convertAndForward function, OCT_DAO, OCT_YDL, token allowances, 1inch router, failed transactions, slippage, allowance reset, transaction revert, assertion failure, liquidity provision, gas fees, asset management, manual review, recommendation, Uniswap router, excessive allowances

---

recursiveEth

medium

# Title: Inadequate Allowance Handling in convertAndForward Function of \u0060OCT_DAO\u0060 & \u0060OCT_YDL\u0060.

## Summary
The \u0060OCT_DAO:convertAndForward \u0060and \u0060OCT_YDL:convertAndForward \u0060function suffers from inadequate handling of token allowances for the 1inch router. Although allowances are set correctly before converting assets, they are not reset afterward. This can lead to failed transactions if the 1inch router does not utilize the entire allowance due to slippage or other factors.

## Vulnerability Detail

the issue arises from the lack of allowance reset after interacting with the 1inch router. If the router does not utilize the entire allowance specified due to slippage or other reasons, the allowance will remain unchanged, potentially causing the assertion to fail and the transaction to revert.

## Impact

The impact of this vulnerability is that transactions may fail due to incorrect allowance management. This could result in inefficiencies in liquidity provision, loss of gas fees because due to asset statement it consume all the gas and won\u0027t return anything and convertandTransfer will never be able to transfer asset to DAO.

## Code Snippet
https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/lockers/OCT/OCT_DAO.sol#L87
https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/lockers/OCT/OCT_YDL.sol#L97
\u0060\u0060\u0060javascript
assert(IERC20(asset).allowance(address(this), router1INCH_V5) == 0);
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation

Reset Allowances After Use: After interacting with the Uniswap router and completing the liquidity provision, reset the allowances for the pair assets and ZVE tokens to zero to ensure they are not left with excessive allowances.

