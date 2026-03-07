# hyh - \u0060updateLocked()\u0060 locks a rounded down value

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** cybersecurity, vulnerability, updateLocked, decimalReducing, rounding down, precision loss, UToken, borrowing, locked value, fee impact, cumulative lock amount, manual review, code snippet, smart contract, Ethereum, financial impact, risk assessment, recommendation, security best practices, contract auditing

---

hyh

Medium

# \u0060updateLocked()\u0060 locks a rounded down value

## Summary

Since \u0060decimalReducing()\u0060 rounds down and fee can use all the precision space the UToken\u0027s \u0060updateLocked()\u0060 call performed on borrowing will effectively lock less then is borrowed.

## Vulnerability Detail

\u0060decimalReducing(actualAmount + fee, underlyingDecimal)\u0060 performed on locking can lose precision, i.e. since fee is added the rounding down can have a material impact.

## Impact

User can have borrowed value slightly exceeding the cumulative lock amount due to rounding of the fee added.

## Code Snippet

\u0060updateLocked()\u0060 will lock a rounded down number for a user:

[UToken.sol#L656-L660](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L656-L660)

\u0060\u0060\u0060solidity
        IUserManager(userManager).updateLocked(
            msg.sender,
            decimalReducing(actualAmount + fee, underlyingDecimal),
            true
        );
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation

Consider introducing an option for rounding the \u0060decimalReducing()\u0060 output up, e.g.:

[UToken.sol#L656-L660](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/market/UToken.sol#L656-L660)

\u0060\u0060\u0060diff
        IUserManager(userManager).updateLocked(
            msg.sender,
-           decimalReducing(actualAmount + fee, underlyingDecimal),
+           decimalReducing(actualAmount + fee, underlyingDecimal, true),
            true
        );
\u0060\u0060\u0060

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/ScaledDecimalBase.sol#L19-L27

\u0060\u0060\u0060diff
-   function decimalReducing(uint256 actualAmount, uint8 decimal) internal pure returns (uint256) {
+   function decimalReducing(uint256 actualAmount, uint8 decimal, bool roundUp) internal pure returns (uint256) {
        if (decimal > 18) {
            uint8 diff = decimal - 18;
            return actualAmount * 10 ** diff;
        } else {
            uint8 diff = 18 - decimal;
            uint256 rounding = roundUp ? 10 ** diff - 1 : 0;
-           return actualAmount / 10 ** diff;
+           return (actualAmount + rounding) / 10 ** diff;
        }
    }
\u0060\u0060\u0060

