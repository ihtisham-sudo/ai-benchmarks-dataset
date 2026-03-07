# OffchainBook Fee Amount Calculation Error

**Severity:** HIGH
**Auditor:** OtterSec

---

## InOffchainBook

_feeAmountX18_ is used to split the given amount to `userAmount` and `feeAmount`.

## contracts/OffchainBook.sol (SOLIDITY)

```solidity
function _feeAmountX18(
    uint64 subaccountId,
    uint32 productId,
    int256 amountX18,
    bool taker
) internal returns (int256, int256) {
    int256 keepRateX18 = ONE -
        fees.getFeeFractionX18(subaccountId, productId, taker);
    int256 newAmountX18 = (amountX18 > 0)
        ? amountX18.mul(keepRateX18)
        : amountX18.div(keepRateX18);
    return (newAmountX18 - amountX18, newAmountX18);
}
```

The fee amount is calculated by `newAmountX18 - amountX18`, always returning a negative fee balance. This leads to inconsistency in total funds since the amount is deducted from users, which is not added anywhere, but instead, is subtracted from the fee account balance.

## Proof of Concept

Considering `amountX18 = 100`, `keepRateX18 = 0.95`, it results in:

1. `newAmountX18 = 95`
2. `feeAmount = 95 - 100 = -5`

Amount 100 is split into 95 and -5, making `newTotal` equal 90, proving an inconsistency.

## Remediation

Change the calculation to `amountX18 - newAmountX18`, which works for both positive and negative amounts.

## Patch

Calculation changed to `amountX18 - newAmountX18`. Fixed in #116.
