# cergyk - OCC_Modular::applyCombine will round APR down

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** OCC_Modular, applyCombine, APR, vulnerability, cybersecurity, interest rate, loans, rounding error, notional, weighted average, BIPS, underwriter, combination, manual review, financial protocol, funds loss, borrowers, APR calculation, payment manipulation, risk assessment

---

cergyk

medium

# OCC_Modular::applyCombine will round APR down

## Summary

\u0060OCC_Modular::applyCombine\u0060 calculation of \u0060APR\u0060 \u0060APR = APR / notional\u0060 rounds in defavor of the protocol, and a user can game this feature to shave of a point of APR from one of his loans.

## Vulnerability Detail

\u0060OCC_Modular::applyCombine\u0060 is used to combine multiple loans into a single loan.

We can see that the APR for the new loan is computed as a weighted average of combined APRs. However since the division rounds down, the APR can be underestimated by 1 point. Since the APR is expressed as BIPS, a point represents a significant amount of interest.

[OCC_Modular.sol#L781](https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCC/OCC_Modular.sol#L781)
\u0060\u0060\u0060solidity
        APR = APR / notional;
\u0060\u0060\u0060

> Please note that even in the case where an underwriter has verified off-chain that the APR would not be rounded down before approving a combination, a user can make sure it rounds down by making some payments on his loans 

## Impact

Loss of funds for the borrowers of the protocol, since a user can reduce APR on his loans by 1 point

## Code Snippet

- https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCC/OCC_Modular.sol#L781

## Tool used

Manual Review

## Recommendation

Ensure that there is no rounding error in the \u0060APR\u0060 calculation\u0027s result by adding a check such as:

\u0060\u0060\u0060diff
+ require(APR % notional == 0, "rounding");
APR = APR / notional;
\u0060\u0060\u0060
