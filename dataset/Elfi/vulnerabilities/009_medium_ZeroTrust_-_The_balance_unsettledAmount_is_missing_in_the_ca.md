# ZeroTrust - The balance.unsettledAmount is missing in the calculations for  \u0060getMaxWithdraw\u0060  and \u0060isSubAmountAllowed\u0060 in UsdPool.sol

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** Zero Trust, cybersecurity, vulnerability, balance.unsettledAmount, calculations, getMaxWithdraw, isSubAmountAllowed, UsdPool.sol, fees, pool, assets, function calls, impact, manual review, code snippet, security flaw, smart contract, financial transactions, error handling, system integrity

---

ZeroTrust

Medium

# The balance.unsettledAmount is missing in the calculations for  \u0060getMaxWithdraw\u0060  and \u0060isSubAmountAllowed\u0060 in UsdPool.sol

## Summary
The balance.unsettledAmount is missing in the calculations for  \u0060getMaxWithdraw\u0060  and \u0060isSubAmountAllowed\u0060 in UsdPool.sol
## Vulnerability Detail
\u0060\u0060\u0060javascript
    function getMaxWithdraw(Props storage self, address stableToken) public view returns (uint256) {
        TokenBalance storage balance = self.stableTokenBalances[stableToken];
        uint256 poolLiquidityLimit = getPoolLiquidityLimit();
        if (poolLiquidityLimit == 0) {
@>>            return balance.amount - balance.holdAmount;
        } else {
            uint256 holdNeedAmount = CalUtils.divRate(balance.holdAmount, poolLiquidityLimit);
@>>            return balance.amount > holdNeedAmount ? balance.amount - holdNeedAmount : 0;
        }
    }
\u0060\u0060\u0060

\u0060\u0060\u0060javascript
    function isSubAmountAllowed(Props storage self, address stableToken, uint256 amount) public view returns (bool) {
        TokenBalance storage balance = self.stableTokenBalances[stableToken];
        if (balance.amount < amount) {
            return false;
        }
        uint256 poolLiquidityLimit = getPoolLiquidityLimit();
        if (poolLiquidityLimit == 0) {
@>>            return balance.amount - balance.holdAmount >= amount;
        } else {
@>>            return CalUtils.mulRate(balance.amount - amount, poolLiquidityLimit) >= balance.holdAmount;
        }
    }

\u0060\u0060\u0060
We can see that the balance.unsettledAmount is missing in the calculations. The balance.unsettledAmount represents the fees earned by the pool, but the assets have not yet been transferred. 
## Impact
The higher-level function calls to getMaxWithdraw and isSubAmountAllowed should return true, but they return false instead, preventing the function from continuing to execute correctly.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L214

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L241

## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060diff
    function getMaxWithdraw(Props storage self, address stableToken) public view returns (uint256) {
        TokenBalance storage balance = self.stableTokenBalances[stableToken];
        uint256 poolLiquidityLimit = getPoolLiquidityLimit();
        if (poolLiquidityLimit == 0) {
-            return balance.amount - balance.holdAmount;
+               return balance.amount + balance.unsettledAmount - balance.holdAmount;
        } else {
            uint256 holdNeedAmount = CalUtils.divRate(balance.holdAmount, poolLiquidityLimit);
-            return balance.amount > holdNeedAmount ? balance.amount - holdNeedAmount : 0;
+            return balance.amount + balance.unsettledAmount > holdNeedAmount ? balance.amount + balance.unsettledAmount - holdNeedAmount : 0;
        }
    }
\u0060\u0060\u0060

\u0060\u0060\u0060diff

    function isSubAmountAllowed(Props storage self, address stableToken, uint256 amount) public view returns (bool) {
        TokenBalance storage balance = self.stableTokenBalances[stableToken];
        if (balance.amount < amount) {
            return false;
        }
        uint256 poolLiquidityLimit = getPoolLiquidityLimit();
        if (poolLiquidityLimit == 0) {
-            return balance.amount - balance.holdAmount >= amount;
+            return balance.amount + balance.unsettledAmount - balance.holdAmount >= amount;
        } else {
-            return CalUtils.mulRate(balance.amount - amount, poolLiquidityLimit) >= balance.holdAmount;
+            return CalUtils.mulRate(balance.amount + balance.unsettledAmount - amount, poolLiquidityLimit) >= balance.holdAmount;
        }
    }

\u0060\u0060\u0060



