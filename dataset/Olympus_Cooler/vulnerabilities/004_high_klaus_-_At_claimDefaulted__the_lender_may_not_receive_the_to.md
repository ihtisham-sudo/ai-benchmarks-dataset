# klaus - At claimDefaulted, the lender may not receive the token because the Unclaimed token is not processed

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Olympus Cooler 
**Keywords:** cybersecurity, vulnerability, claimDefaulted, lender, unclaimed tokens, loan data, data deletion, debt repayment, security flaw, manual review, token processing, impact assessment, code snippet, recommendation, data integrity, financial security, system vulnerability, risk management, token management, software security

---

klaus

medium

# At claimDefaulted, the lender may not receive the token because the Unclaimed token is not processed
## Summary

\u0060claimDefaulted\u0060 does not handle \u0060loan.unclaimed\u0060  . This preventing the lender from receiving the debt repayment.

## Vulnerability Detail

\u0060\u0060\u0060solidity
function claimDefaulted(uint256 loanID_) external returns (uint256, uint256, uint256) {
  Loan memory loan = loans[loanID_];
  delete loans[loanID_];
\u0060\u0060\u0060

 Loan data is deletead in \u0060claimDefaulted\u0060 function. \u0060loan.unclaimed\u0060 is not checked before data deletead. So, if \u0060claimDefaulted\u0060 is called while there are unclaimed tokens, the lender will not be able to get the unclaimed tokens.

## Impact

Lender cannot get unclaimed token.

## Code Snippet

[https://github.com/sherlock-audit/2023-08-cooler/blob/6d34cd12a2a15d2c92307d44782d6eae1474ab25/Cooler/src/Cooler.sol#L318-L320](https://github.com/sherlock-audit/2023-08-cooler/blob/6d34cd12a2a15d2c92307d44782d6eae1474ab25/Cooler/src/Cooler.sol#L318-L320)

## Tool used

Manual Review

## Recommendation

Process unclaimed tokens before deleting loan data.

\u0060\u0060\u0060diff
function claimDefaulted(uint256 loanID_) external returns (uint256, uint256, uint256) {
+   claimRepaid(loanID_)
    Loan memory loan = loans[loanID_];
    delete loans[loanID_];
\u0060\u0060\u0060
