# .2 Users can bypass the borrow expiry restriction by calling leverage() instead

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Eggs Finance
**Keywords:** leverage, borrow, expiry, restriction, function, check, loan, days, max, combine, buy, bypass, recommendation, commit, fixed, EggsFinance, CantinaManaged, solidity, require, extension

---

# .2 Users can bypass the borrow expiry restriction by calling leverage() instead
**Severity:** MediumRisk  
**Context:** (No context files were provided by the reviewer)  
**Description:** The leverage() function acts as a function that combines both buy() and borrow(). The borrow() function restricts users from taking loans for a period of more than a year:
\u0060\u0060\u0060solidity
require(
    numberOfDays < 366,
    "Max borrow/extension must be 365 days or less"
);
\u0060\u0060\u0060
However, leverage() lacks this kind of check, effectively allowing users to bypass it.  
**Recommendation:** Consider adding this check to leverage() as well.  
**EggsFinance:** Fixed in commit 2f02fb77.  
**CantinaManaged:** Fixed as recommended.
