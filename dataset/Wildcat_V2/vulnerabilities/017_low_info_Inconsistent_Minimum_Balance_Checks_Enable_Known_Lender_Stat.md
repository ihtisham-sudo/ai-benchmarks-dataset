# Inconsistent Minimum Balance Checks Enable Known Lender Status Bypass via \u0060onTransfer\u0060 function

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, AccessControlHooks.sol, onDeposit, onTransfer, minimum deposit check, attackers, known lender status, economic model, risk assessment, proof of concept, credential, transfer, cumulative balance check, maturity period, valid depositor, mitigation steps, permissions validation, account privileges, smart contract security

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/access/AccessControlHooks.sol#L786-L791
https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/access/AccessControlHooks.sol#L864-L881
https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/access/AccessControlHooks.sol#L733-L742


# Vulnerability details

The issue stems from the difference in logic between the \u0060onDeposit\u0060 and \u0060onTransfer\u0060 functions in \u0060AccessControlHooks.sol\u0060, particularly regarding the minimum deposit check. Let\u0027s analyze this step by step:

1. Behavior of the \u0060onDeposit\u0060 function:
   In the \u0060onDeposit\u0060 function, there\u0027s an explicit check for the minimum deposit amount:

   \u0060\u0060\u0060solidity
       // Check that the deposit amount is at or above the market\u0027s minimum
       uint normalizedAmount = scaledAmount.rayMul(state.scaleFactor);
       if (market.minimumDeposit > normalizedAmount) {
         revert DepositBelowMinimum();
       }

   \u0060\u0060\u0060
   This ensures that direct deposits must meet the minimum deposit requirement.

2. Behavior of the \u0060onTransfer\u0060 function:
   In contrast, the \u0060onTransfer\u0060 function doesn\u0027t have a similar minimum amount check. It primarily focuses on validating the permissions of the recipient (\u0060to\u0060 address):

  \u0060\u0060\u0060solidity
      // If the recipient is a known lender, skip access control checks.
      if (!isKnownLenderOnMarket[to][msg.sender]) {
        // ... check logic ...
      }
  \u0060\u0060\u0060

## Impact

   - Attackers might gain known lender status by receiving transfers of extremely small amounts, without meeting the normal minimum deposit requirements.
   - This could lead to a large number of accounts in the system holding tiny amounts but having known lender privileges.
   - It may affect the system\u0027s economic model and risk assessment.

## Proof of Concept

   Attackers might exploit this difference to bypass the minimum deposit limit while still gaining known lender status. The attack steps could be as follows:
   
   a. The attacker first obtains a valid credential through legitimate means (possibly a small deposit or other method).
   
   b. Then, the attacker uses this valid credential to receive a very small amount (potentially far below the minimum deposit requirement) through the \u0060onTransfer\u0060 function.
   
   c. Since \u0060onTransfer\u0060 doesn\u0027t have a minimum amount check, as long as the credential is valid, this transfer would succeed.

   d. In the \u0060_writeLenderStatus\u0060 function, if the conditions are met (valid credential, not previously a known lender, \u0060canSetKnownLender\u0060 is true), the account would be marked as a known lender:

      \u0060\u0060\u0060solidity
          // Mark account as a known lender if they have a valid credential, are not
          // already known, and the function counts as a deposit.
          if (
            canSetKnownLender.and(hasValidCredential).and(
              !isKnownLenderOnMarket[accountAddress][msg.sender]
            )
          ) {
            isKnownLenderOnMarket[accountAddress][msg.sender] = true;
            emit AccountMadeFirstDeposit(accountAddress);
          }
      \u0060\u0060\u0060

## Recommended Mitigation Steps
   - Add a minimum amount check in the \u0060onTransfer\u0060 function as well.
   - Introduce a cumulative balance check, only granting known lender status when an account\u0027s total balance reaches a certain threshold.
   - Implement a "maturity period" for known lender status, requiring accounts to maintain a minimum balance for a period of time.
   - Consider separating the concepts of "known lender" and "valid depositor," applying different restrictions for different operations.



## Assessed type

Access Control
