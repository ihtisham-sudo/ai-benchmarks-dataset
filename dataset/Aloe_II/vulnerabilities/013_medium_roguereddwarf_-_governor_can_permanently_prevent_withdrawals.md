# roguereddwarf - governor can permanently prevent withdrawals in spite of being restricted

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Aloe II
**Keywords:** cybersecurity, vulnerability, governor, withdrawals, interest rate, borrowers, lender, utilization, RateModel, SafeRateLib, MAX_RATE, timelock, protocol, malicious behavior, funds, permanent prevention, market forces, interest rate model, manual review, recommendation

---

roguereddwarf

medium

# governor can permanently prevent withdrawals in spite of being restricted
## Summary
According to the Contest README (which is the highest order source of truth), the \u0060governor\u0060 address should be restricted and not be able to prevent withdrawals from the \u0060Lender\u0060s.  

This doesn\u0027t hold true. By setting the interest rate that the borrowers have to pay to zero, the \u0060governor\u0060 can effectively prevent withdrawals.  

## Vulnerability Detail
Quoting from the Contest README:  
\u0060\u0060\u0060text
Is the admin/owner of the protocol/contracts TRUSTED or RESTRICTED?

Restricted. The governor address should not be able to steal funds or prevent users from withdrawing. It does have access to the govern methods in Factory, and it could trigger liquidations by increasing nSigma. We consider this an acceptable risk, and the governor itself will have a timelock.
\u0060\u0060\u0060

The mechanism by which users are ensured that they can withdraw their funds is the interest rate which increases with utilization.  

Market forces will keep the utilization in balance such that when users want to withdraw their funds from the \u0060Lender\u0060 contracts, the interest rate increases and \u0060Borrower\u0060s pay back their loans (or get liquidated).  

What the \u0060governor\u0060 is allowed to do is to set a interest rate model via the [\u0060Factory.governMarketConfig\u0060](https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/Factory.sol#L282-L303) function.  

The \u0060SafeRateLib\u0060 is used to safely call the \u0060RateModel\u0060 by e.g. handling the case when the call to the \u0060RateModel\u0060 reverts and limiting the interest to a \u0060MAX_RATE\u0060: https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/RateModel.sol#L38-L60.  

This clearly shows that the \u0060governor\u0060 should be very much restricted in setting the \u0060RateModel\u0060 such as to not damage users of the protocol which is in line with how the \u0060governor\u0060 role is described in the README.  

However the interest rate can be set to zero even if the utilization is very high. If \u0060Borrower\u0060s can borrow funds for a zero interest rate, they will never pay back their loans. This means that users in the \u0060Lender\u0060s will never be able to withdraw their funds.  

It is also noteworthy that the timelock that the governor uses won\u0027t be able to prevent this scenario since even if users withdraw their funds as quickly as possible, there will probably not be enough time / availability of funds for everyone to withdraw in time (assuming a realistic timelock length).  

## Impact
The \u0060governor\u0060 is able to permanently prevent withdrawals from the \u0060Lender\u0060s which it should not be able to do according to the contest README.  

## Code Snippet
Function to set the rate model:  
https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/Factory.sol#L282-L303

\u0060SafeRateLib\u0060 allows for a zero interest rate:  
https://github.com/aloelabs/aloe-ii/blob/c71e7b0cfdec830b1f054486dfe9d58ce407c7a4/core/src/RateModel.sol#L38-L60

## Tool used
Manual Review

## Recommendation
The \u0060SafeRateLib\u0060 should ensure that as the utilization approaches \u00601e18\u0060 (100%), the interest rate cannot be below a certain minimum value.

This ensures that even if the \u0060governor\u0060 behaves maliciously or uses a broken \u0060RateModel\u0060, \u0060Borrower\u0060s will never borrow all funds without paying them back.  

