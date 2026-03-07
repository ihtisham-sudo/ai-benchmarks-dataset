# Role providers can bypass intended restrictions and lower expiry set by other providers

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, role providers, credential management, expiry date, bypass, security flaw, user credentials, access control, code comments, mitigation steps, security assessment, credential reduction, provider support, authentication, authorization, exploit, software security, risk management, security best practices

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/FixedTermLoanHooks.sol#L413


# Vulnerability details

## Proof of Concept
If we look at the code comments, we\u0027ll see that role providers can update a user\u0027s credential only if at least one of the 3 is true:
- the previous credential\u0027s provider is no longer supported, OR
- the caller is the previous role provider, OR
- the new expiry is later than the current expiry

\u0060\u0060\u0060solidity
  /**
   * @dev Grants a role to an account by updating the account\u0027s status.
   *      Can only be called by an approved role provider.
   *
   *      If the account has an existing credential, it can only be updated if:
   *      - the previous credential\u0027s provider is no longer supported, OR
   *      - the caller is the previous role provider, OR
   *      - the new expiry is later than the current expiry
   */
  function grantRole(address account, uint32 roleGrantedTimestamp) external {
    RoleProvider callingProvider = _roleProviders[msg.sender];

    if (callingProvider.isNull()) revert ProviderNotFound();

    _grantRole(callingProvider, account, roleGrantedTimestamp);
  }
\u0060\u0060\u0060

This means that a role providers should not be able to reduce a credential set by another role provider.

However, this could easily be bypassed by simply splitting the call into 2 separate ones:

1. First one to set the expiry slightly later than the currently set one. This would set the role provider to the new one.
2. Second call to reduce the expiry as much as they\u0027d like. Since they\u0027re the previous provider they can do that.

## Recommended Mitigation Steps
Fix is non-trivial.


## Assessed type

Context
