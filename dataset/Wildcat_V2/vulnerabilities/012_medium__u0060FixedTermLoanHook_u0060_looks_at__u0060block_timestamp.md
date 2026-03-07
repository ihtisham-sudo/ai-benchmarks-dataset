# \u0060FixedTermLoanHook\u0060 looks at \u0060block.timestamp\u0060 instead of \u0060expiry\u0060

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, FixedTermLoanHook, block.timestamp, expiry, withdrawals, term end time, inconsistencies, withdrawalBatchDuration, funds, manual review, mitigation steps, context assessment, smart contracts, security flaws, timestamp manipulation, user experience, financial applications, code review, risk management

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/FixedTermLoanHooks.sol#L848


# Vulnerability details

## Impact
\u0060FixedTermLoanHook\u0060 looks at \u0060block.timestamp\u0060 instead of \u0060expiry\u0060

## Proof of Concept
The idea of \u0060FixedTermLoanHook\u0060 is to only allow for withdrawals after a certain term end time. However, the problem is that the current implementation does not look at the expiry, but instead at the \u0060block.timestamp\u0060

\u0060\u0060\u0060solidity
  function onQueueWithdrawal(
    address lender,
    uint32 /* expiry */,
    uint /* scaledAmount */,
    MarketState calldata /* state */,
    bytes calldata hooksData
  ) external override {
    HookedMarket memory market = _hookedMarkets[msg.sender];
    if (!market.isHooked) revert NotHookedMarket();
    if (market.fixedTermEndTime > block.timestamp) {
      revert WithdrawBeforeTermEnd();
    }
\u0060\u0060\u0060

This creates inconsistencies such as forcing users not only to wait until term\u0027s end, but also having to wait an extra \u0060withdrawalBatchDuration\u0060 before they\u0027re able to withdraw their funds.


## Tools Used
Manual review

## Recommended Mitigation Steps
Check the \u0060expiry\u0060 instead of \u0060block.timestamp\u0060


## Assessed type

Context
