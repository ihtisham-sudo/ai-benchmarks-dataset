# executePayroll() can be frontrun with split transactions 

**Severity:** HIGH
**Auditor:** Cantina

---

## Payroll Manager Security Analysis

## Context
- **Files**: `PayrollManager.sol#L139-L244`, `AllowanceModule.sol#L56`

## Description
The function `executePayroll()` executes multiple transactions in one go, but it can be front-run to execute a subset of the transactions. Note this requires careful crafting of the parameters. This splitting leads to several problems:

- The retrieval from the allowance contract (`execTransactionFromGnosis()`) can be split into a large number of small transactions. This uses up the nonces in the allowance contract. As these nonces are limited to a maximum of 65535, this would finally prevent further payments.
- If a subset is executed (successfully) before the original transaction, then the original transaction will fail and has to be rescheduled (minus the succeeded transaction). This requires gas, effort, and time.
- If the original transaction is delayed multiple times, then the allowance time period (e.g., a month) could be passed and the allowance for that period would be forfeited (lost). This could require coordination efforts to fix.

### Code Snippet
```solidity
function executePayroll(...) ... {
    ...
    for (uint256 index = 0; index < paymentTokens.length; index++) {
        execTransactionFromGnosis(...);
    }
    ...
}
contract AllowanceModule is ... {
    struct Allowance {
        uint96 amount;
        uint96 spent;
        uint16 resetTimeMin;
        uint32 lastResetMin;
        uint16 nonce; // 16 bits so max 65535
    }
}
```

## Recommendation
Use the solution of "Token retrieval not linked to signed transactions".

## Parcel
This is solved by a redesign of the `executePayroll()` function.

## Cantina Security
Verified.
