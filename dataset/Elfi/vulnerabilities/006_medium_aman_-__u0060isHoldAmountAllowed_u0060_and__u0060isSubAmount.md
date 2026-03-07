# aman - \u0060isHoldAmountAllowed\u0060 and \u0060isSubAmountAllowed\u0060 wrong subtraction will result in DoS

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, DoS, HoldStableToken, subStableToken, balance, amount, holdAmount, unsettledAmount, isHoldAmountAllowed, isSubAmountAllowed, redeeming token, PnL updates, Rebalance calls, manual review, code review, security check, function validation, error handling, smart contract

---

aman

Medium

# \u0060isHoldAmountAllowed\u0060 and \u0060isSubAmountAllowed\u0060 wrong subtraction will result in DoS

## Summary
The \u0060HoldStableToken\u0060 function checks if the given amount can be held by adding \u0060(balance.amount + balance.unsettledAmount-balance.holdAmount)\u0060 and \u0060isSubAmountAllowed\u0060 checks if \u0060(balance.amount - balance.holdAmount) >= amount\u0060. However, it is possible that the \u0060holdAmount\u0060 is greater than the amount.

## Vulnerability Detail
In case of adding the \u0060HoldStableToken\u0060 we add  \u0060balance.amount\u0060 and \u0060balance.unsettledAmount\u0060 in \u0060isHoldAmountAllowed\u0060:
\u0060\u0060\u0060solidity
function isHoldAmountAllowed(
        TokenBalance memory balance,
        uint256 poolLiquidityLimit,
        uint256 amount
    ) internal pure returns (bool) {
        if (poolLiquidityLimit == 0) {
            return balance.amount + balance.unsettledAmount - balance.holdAmount >= amount;
        } else {
            return
                CalUtils.mulRate(balance.amount + balance.unsettledAmount, poolLiquidityLimit) - balance.holdAmount >=
                amount;
        }
    }
\u0060\u0060\u0060
In case of \u0060subStableToken\u0060 we check \u0060isSubAmountAllowed\u0060 
\u0060\u0060\u0060solidity
function isSubAmountAllowed(Props storage self, address stableToken, uint256 amount) public view returns (bool) {
        TokenBalance storage balance = self.stableTokenBalances[stableToken];
        if (balance.amount < amount) {
            return false;
        }
        uint256 poolLiquidityLimit = getPoolLiquidityLimit();
        if (poolLiquidityLimit == 0) {
            return balance.amount - balance.holdAmount >= amount; // @audit : this could revert due to overflow/undeflow if holdAmount > amount.
        } else {
            return CalUtils.mulRate(balance.amount - amount, poolLiquidityLimit) >= balance.holdAmount;
        }
    }
\u0060\u0060\u0060
The following case could occur:
\u0060\u0060\u0060solidity
// assume here poolLiquidityLimit=0;
balance.amount = 10e18;
balance.unsettled = 10e18;
// while adding the hold amount 12e18 , balance.amount + balance.unsettledAmount - balance.holdAmount >= amount
10e18 + 10e18 - 0 >= 12e18 // it will return true so now holdAmount=12e18
//No rebalance occur the state of token balance is same
// now we want to subtract the amount from token balance  isSubAmountAllowed would be called to check that if amount can be deducted
//return balance.amount - balance.holdAmount >= amount;
10e18 - 12e18>= 5e18 // it will revert due to underFlow/OverFlow
\u0060\u0060\u0060

## Impact
The Will create DoS for \u0060subStableToken\u0060 calls , \u0060subStableToken\u0060 function is used in different use cases like redeeming token , PnL updates and Rebalance calls. 

## Code Snippet
[https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L241C14-L252](https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L241C14-L252)
[https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L254-L266](https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L254-L266)
[https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L87](https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/UsdPool.sol#L87)
## Tool used

Manual Review

## Recommendation
add one more check inside \u0060isSubAmountAllowed\u0060 as follows :
\u0060\u0060\u0060diff
diff --git a/elfi-perp-contracts/contracts/storage/UsdPool.sol b/elfi-perp-contracts/contracts/storage/UsdPool.sol
index 93d8aca1..dba7d141 100644
--- a/elfi-perp-contracts/contracts/storage/UsdPool.sol
+++ b/elfi-perp-contracts/contracts/storage/UsdPool.sol
@@ -240,12 +240,12 @@ library UsdPool {
 
     function isSubAmountAllowed(Props storage self, address stableToken, uint256 amount) public view returns (bool) {
         TokenBalance storage balance = self.stableTokenBalances[stableToken];
-        if (balance.amount < amount) {
+        if (balance.amount < amount|| balance.amount <balance.holdAmount) {
             return false;
         }
         uint256 poolLiquidityLimit = getPoolLiquidityLimit();
\u0060\u0060\u0060
