# thekmj - \u0060emergency_shutdown\u0060 role is not enough for emergency shutdown.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Olympus Cooler 
**Keywords:** cybersecurity, vulnerability, emergency_shutdown, cooler_overseer, protocol roles, Clearinghouse, shutdown multisig, governance, defund, modifier, ROLES_RequireRole, impact, manual review, Foundry, Forge, test case, mitigation, internal function, emergency protocol, security flaw

---

thekmj

high

# \u0060emergency_shutdown\u0060 role is not enough for emergency shutdown.
## Summary

There are two protocol roles, \u0060emergency_shutdown\u0060 and \u0060cooler_overseer\u0060. The \u0060emergency_shutdown\u0060 should have the ability to shutdown the Clearinghouse.

However, in the current contract, \u0060emergency_shutdown\u0060 role does not have said ability. An address will need both \u0060emergency_shutdown\u0060 and \u0060cooler_overseer\u0060 to perform said action.

We have also confirmed with the protocol team that the two roles will be held by two different multisigs, with the shutdown multisig having a lower threshold and more holders. Thereby governance will not be able to act as quickly to emergencies than expected.

## Vulnerability Detail

Let\u0027s examine the function \u0060emergencyShutdown()\u0060:

\u0060\u0060\u0060solidity 
function emergencyShutdown() external onlyRole("emergency_shutdown") {
    active = false;

    // If necessary, defund sDAI.
    uint256 sdaiBalance = sdai.balanceOf(address(this));
    if (sdaiBalance != 0) defund(sdai, sdaiBalance);

    // If necessary, defund DAI.
    uint256 daiBalance = dai.balanceOf(address(this));
    if (daiBalance != 0) defund(dai, daiBalance);

    emit Deactivated();
}
\u0060\u0060\u0060

This has the modifier \u0060onlyRole("emergency_shutdown")\u0060. However, this also calls function \u0060defund()\u0060, which has the modifier \u0060onlyRole("cooler_overseer")\u0060

\u0060\u0060\u0060solidity
function defund(ERC20 token_, uint256 amount_) public onlyRole("cooler_overseer") {
\u0060\u0060\u0060

Therefore, the role \u0060emergency_shutdown\u0060 will not have the ability to shutdown the protocol, unless it also has the overseer role.

### Proof of concept

To get a coded PoC, make the following modifications to the test case:
- In \u0060Clearinghouse.t.sol\u0060, comment out line 125 (so that \u0060overseer\u0060 only has \u0060emergency_shutdown\u0060 role)
https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/test/Clearinghouse.t.sol#L125

\u0060\u0060\u0060solidity
//rolesAdmin.grantRole("cooler_overseer", overseer);
rolesAdmin.grantRole("emergency_shutdown", overseer);
\u0060\u0060\u0060

- Run the following test command (to just run a single test \u0060test_emergencyShutdown()\u0060):
\u0060\u0060\u0060sh
forge test --match-test test_emergencyShutdown
\u0060\u0060\u0060

The test will fail with the \u0060ROLES_RequireRole()\u0060 error.
## Impact

\u0060emergency_shutdown\u0060 role cannot emergency shutdown the protocol

## Code Snippet

https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Clearinghouse.sol#L339
https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Clearinghouse.sol#L360-L372

## Tool used

Manual Review, Foundry/Forge

## Recommendation

There are two ways to mitigate this issue:
- Separate the logic for emergency shutdown and defunding. i.e. do not defund when emergency shutdown, but rather defund separately after shutdown. 
- Move the defunding logic to a separate internal function, so that emergency shutdown function can directly call defunding without going through a modifier.

