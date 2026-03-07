# lender that\u0027s mistakenly flagged can lose access to funds

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, access control, Chainalysis, overrideSanction, nukeFromOrbit, malicious actor, lender, borrower, sanction status, assets transfer, escrow, function exploitation, manual review, mitigation steps, onlyBorrower modifier, unauthorized access, interest accrual, funds access, security risk

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/market/WildcatMarketConfig.sol#L82


# Vulnerability details

## Impact
The lender can lose access to their funds throughout the withdrawal cycle and will also miss out on any interest accrual during that period.
## Description

When lenders are mistakenly flagged by \u0060Chainalysis\u0060, the borrower can use the [overrideSanction](https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/WildcatSanctionsSentinel.sol#L96C3-L99C4) function to override the sanction status:

https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/WildcatSanctionsSentinel.sol#L96C3-L99C4
\u0060\u0060\u0060solidity
   * @dev Overrides the sanction status of \u0060account\u0060 for \u0060borrower\u0060.
   */
  function overrideSanction(address account) public override {
    sanctionOverrides[msg.sender][account] = true;
    emit SanctionOverride(msg.sender, account);
  }
\u0060\u0060\u0060

However, an issue arises if a lender is mistakenly flagged by \u0060Chainalysis\u0060. A malicious actor can exploit this by calling the [nukeFromOrbit](https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/market/WildcatMarketConfig.sol#L82C1-L88C4) function on the lender to transfer their assets to escrow before the borrower has a chance to call \u0060overrideSanction\u0060.

This is possible because \u0060nukeFromOrbit\u0060 is an external function and can be called by anyone as long as the lender is flagged as sanctioned:However, an issue arises if a lender is mistakenly flagged by \u0060Chainalysis\u0060. A malicious actor can exploit this by calling the [nukeFromOrbit](https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/market/WildcatMarketConfig.sol#L82C1-L88C4) function on the lender to transfer their assets to escrow before the borrower has a chance to call \u0060overrideSanction\u0060.

This is possible because \u0060nukeFromOrbit\u0060 is an external function and can be called by anyone as long as the lender is flagged as sanctioned:

https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/market/WildcatMarketConfig.sol#L82C1-L88C4
\u0060\u0060\u0060solidity
  function nukeFromOrbit(address accountAddress) external nonReentrant sphereXGuardExternal {
    if (!_isSanctioned(accountAddress)) revert_BadLaunchCode();
    MarketState memory state = _getUpdatedState();
    hooks.onNukeFromOrbit(accountAddress, state);
    _blockAccount(state, accountAddress);
    _writeState(state);
  }
\u0060\u0060\u0060

As a result, the lender would lose access to their funds


## Tools Used

Manual review

## Recommended Mitigation Steps

The issue can be mitigated by restricting the function so that only the borrower can call it. This can be done by applying the \u0060onlyBorrower\u0060 modifier, ensuring that no unauthorized parties can call the function





## Assessed type

Access Control
