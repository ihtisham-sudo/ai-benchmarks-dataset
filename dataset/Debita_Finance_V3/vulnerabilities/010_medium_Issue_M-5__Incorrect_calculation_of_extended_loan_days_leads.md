# Issue M-5: Incorrect calculation of extended loan days leads to unfair borrower fees

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Debita Finance V3
**Keywords:** loan, fees, calculation, borrower, extended days, maxDeadline, nextDeadline, m_loan, startedAt, inflated fees, principal loss, financial hardship, reputational damage, fee structure, extendLoan, function, timestamp, error, protocol, audit

---

# Issue M-5: Incorrect calculation of extended loan days leads to unfair borrower fees  
Source: https://github.com/sherlock-audit/2024-10-debita-judging/issues/236  
The protocol has acknowledged this issue.  

## Found by  
newspacexyz, prosper  

### Summary  
The miscalculation of extended loan days in the \u0060extendLoan\u0060 function will cause borrowers to face unfair fees as the function incorrectly calculates the fee based on \u0060offer.maxDeadline\u0060 instead of using the actual extended days derived from \u0060nextDeadline()\u0060 and \u0060m_loan.startedAt\u0060. This leads to inflated fee deductions during loan extensions.  

### Root Cause  
In \u0060DebitaV3Loan.sol:602\u0060, the calculation of the extended days incorrectly uses \u0060offer.maxDeadline\u0060 as the basis for the fee calculation instead of the actual extended period derived from \u0060nextDeadline()\u0060 and \u0060m_loan.startedAt\u0060. This results in an inflated \u0060feeOfMaxDeadline\u0060, leading to excessive fees for borrowers.  
https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L602-L610  

**Real extended \u0060maxDeadline\u0060 is \u0060nextDeadline()\u0060, not \u0060offer.maxDeadline\u0060.**  
\u0060\u0060\u0060solidity
// calculate difference from fee paid for the initialDuration vs the extra fee
// they should pay because of the extras days of extending the loan. MAXFEE
// shouldnt be higher than extra fee + PorcentageOfFeePaid
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L601
_No response_

_No response_
## Attack Path
1. The borrower calls the \u0060extendLoan()\u0060 function to extend their loan duration.
2. The function validates initial conditions:
   - \u0060loanData.extended\u0060 is \u0060false\u0060.
   - \u0060nextDeadline()\u0060 returns a timestamp greater than \u0060block.timestamp\u0060.
   - \u0060offer.maxDeadline\u0060 is a valid future timestamp.
3. The function calculates \u0060feeOfMaxDeadline\u0060 as:
   \u0060\u0060\u0060solidity
   uint feeOfMaxDeadline = ((offer.maxDeadline * feePerDay) / 86400);
   \u0060\u0060\u0060
   This incorrectly uses \u0060offer.maxDeadline\u0060 instead of the actual extended period derived from \u0060nextDeadline()\u0060 and \u0060m_loan.startedAt\u0060.
4. The miscalculation leads to an inflated \u0060feeOfMaxDeadline\u0060 and missing \u0060borrowFee\u0060.
5. The inflated fees are deducted from the borrower\u0027s principal during the loan extension.
6. The borrower loses more principal than necessary due to the incorrect fee calculation.

### Impact
Borrowers will be charged inflated fees due to the incorrect calculation of the extended loan days. This results in unnecessary principal loss, making loan extensions disproportionately costly. Over time, this could discourage borrowers from using the loan extension feature, cause financial hardship, and lead to reputational damage for the platform as users perceive the fee structure as unfair or exploitative.

### PoC
_No response_

### Mitigation
\u0060\u0060\u0060solidity
uint extendedDays = nextDeadline() - m_loan.startedAt;
require(extendedDays > 0, "Invalid extended days");
uint feeOfMaxDeadline = ((extendedDays * feePerDay) / 86400);
\u0060\u0060\u0060
