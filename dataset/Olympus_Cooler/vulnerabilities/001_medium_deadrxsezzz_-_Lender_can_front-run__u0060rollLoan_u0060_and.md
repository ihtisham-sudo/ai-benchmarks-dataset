# deadrxsezzz - Lender can front-run \u0060rollLoan\u0060 and call \u0060provideNewTermsForRoll\u0060 with unfavorable terms

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Olympus Cooler 
**Keywords:** cybersecurity, vulnerability, front-running, rollLoan, provideNewTermsForRoll, unfavorable terms, interest rate, mempool, transaction, borrower, lender, loan terms, manual review, risk, overpaying, accepting terms, user A, lender B, max interest rate, recommendation

---

deadrxsezzz

high

# Lender can front-run \u0060rollLoan\u0060 and call \u0060provideNewTermsForRoll\u0060 with unfavorable terms
## Summary
Lender can front-run \u0060rollLoan\u0060 and result in borrower accepting unfavorable terms.

## Vulnerability Detail
After a loan is created, the lender can provide new loan terms via \u0060provideNewTermsForRoll\u0060. If they are reasonable, the user can then accept them. However this opens up a risky scenario: 
1. User A borrows from lender B 
2. Lender B proposes new suitable terms 
3. User A sees them and calls \u0060rollLoan\u0060 to accept them
4. Lender B is waiting for this and sees the pending transaction in the mempool
5. Lender B front-runs user A\u0027s transaction and makes a new call to \u0060provideNewTermsForRoll\u0060 will an extremely high interest rate
6. User A\u0027s transaction now executes and they\u0027ve accepted unfavorable terms with extremely high interest rate

## Impact
User may get mislead in to accepting unfavorable terms and overpaying interest 

## Code Snippet
https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Cooler.sol#L192
https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Cooler.sol#L282

## Tool used

Manual Review

## Recommendation
When calling \u0060rollLoan\u0060 let the user pass a parameter consisting of the max interest rate they are willing to accept to prevent from such incidents.



