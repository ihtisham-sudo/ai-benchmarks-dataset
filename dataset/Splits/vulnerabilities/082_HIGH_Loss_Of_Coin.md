# Loss Of Coin

**Severity:** HIGH
**Auditor:** OtterSec

---

## Limit Order Flash Loan Vulnerability

`limit_order::repay_flash_loan` lacks a check to ensure that the `order_id` in the receipt matches. This omission allows a user to deposit `target_coin` into an order different from the one that initiated the `limit_order::flash_loan`. Consequently, the original order loses `PayCoin` and fails to receive `TargetCoin`, resulting in a financial loss.

## Proof of Concept
1. An attacker creates an order with the same `PayCoin` and `TargetCoin` as the victim’s order.
2. The attacker flash loans the victim’s order to take the `PayCoin`.
3. When repaying the flash loan, the attacker deposits the amount of `TargetCoin` specified in the receipt into their own order instead of the victim’s order.
4. The victim does not receive the `TargetCoin`, and the attacker claims the `TargetCoin` from their own order.

## Remediation
Ensure that the `order_id` in the receipt matches the ID of the `limit_order`.

```rust
> _order.moved_diff
@@ -677,6 +677,8 @@ module limit_order::limit_order {
target_repay_amount
} = receipt;
+ assert!(order_id == id(limit_order), EMismatchedOrder);
+
// store target coin into order
let target_coin = coin::split(coin, target_repay_amount, ctx);
let target_balance = coin::into_balance(target_coin);
```

## Patch
Fixed in a commit `a1e ba1`.

© 2024 Otter Audits LLC. All Rights Reserved. 6/12
