# 8.1 CANNOT GRANT GUARDIAN ROLE AFTER KICK OR UNPAUSE

**Severity:** high
**Auditor:** Halborn
**Protocol:** Moonwell
**Keywords:** pause guardian, MultichainGovernor, ConfigurablePauseGuardian, unpause, kickGuardian, access control, guardian role, contract initialization, address(0), function call, security, pause mechanism, emit event, internal function, pause state, grantGuardian, trusted sender, contract management, vulnerability, recommendation

---

# 8.1 CANNOT GRANT GUARDIAN ROLE AFTER KICK OR UNPAUSE

**Description**  
The \u0060ConfigurablePauseGuardian\u0060 contract, which is inherited by \u0060MultichainGovernor\u0060 contract, implements a custom pausing mechanism, defining the pause guardian role, which represents the address that is allowed to call the \u0060pause()\u0060 function within the \u0060ConfigurablePauseGuardian\u0060 contract. Considering that \u0060MultichainGovernor\u0060 contract inherits from \u0060ConfigurablePauseGuardian\u0060, we can infer from the following code snippet that an initial address is being attributed as pause guardian when initializing the \u0060MultichainGovernor\u0060 contract:

\u0060\u0060\u0060solidity
function initialize(
    InitializeData memory initData,
    WormholeTrustedSender.TrustedSender[] memory trustedSenders,
    bytes[] calldata calldatas
) external initializer {
    { ... }
    /// set the pause guardian
    _grantGuardian(initData.pauseGuardian);
    { ... }
}
\u0060\u0060\u0060

The \u0060_grantGuardian\u0060 internal function in \u0060ConfigurablePauseGuardian\u0060 contract will set the \u0060newPauseGuardian\u0060 address, as follows:

\u0060\u0060\u0060solidity
function _grantGuardian(address newPauseGuardian) internal {
    address previousPauseGuardian = newPauseGuardian;
    pauseGuardian = newPauseGuardian;
    /// if a new guardian is granted, the contract is automatically unpaused
    _setPauseTime(0);
    emit PauseGuardianUpdated(previousPauseGuardian, newPauseGuardian);
}
\u0060\u0060\u0060

Moving forward, it is important to highlight that whenever we call the functions \u0060unpause\u0060 or \u0060kickGuardian\u0060, the \u0060_resetPauseState\u0060 internal function is called, which, among other things, sets the \u0060pauseGuardian\u0060 address to the \u0060address(0)\u0060.

\u0060\u0060\u0060solidity
function _resetPauseState() private {
    address previousPauseGuardian = pauseGuardian;
\u0060\u0060\u0060
## Pause Guardian Management

\u0060\u0060\u0060solidity
pauseGuardian = address(0); /// remove the pause guardian
_setPauseTime(0); /// fully unpause, set pauseStartTime to 0
emit PauseGuardianUpdated(previousPauseGuardian, address(0));
\u0060\u0060\u0060

While effectively validating whether the caller of the \u0060pause\u0060 function is indeed authorized to perform the pause operation (by checking if the \u0060msg.sender == pauseGuardian\u0060), and by implementing a safety mechanism such as \u0060kickGuardian\u0060 to avoid unintended entities to stay as \u0060pause guardians\u0060, the current implementation of \u0060MultichainGovernor\u0060 and \u0060ConfigurablePauseGuardian\u0060 does not expose any public or external method, not even access-controlled, to grant guardian role to new addresses.

In other words, this means that after \u0060unpause\u0060 or \u0060kickGuardian\u0060 functions are called, effectively changing the \u0060pauseGuardian\u0060 to \u0060address(0)\u0060, it is impossible to set a new \u0060pauseGuardian\u0060 because the only time the \u0060_grantGuardian\u0060 function is called is within the initialization of the \u0060MultichainGovernor\u0060 contract. This will prevent the \u0060MultichainGovernor\u0060 contract from setting new \u0060pause guardians\u0060 addresses.

**BVSS AO:A/AC:L/AX:L/C:N/I:L/A:N/D:N/Y:N/R:N/S:C (3.1)**

It is recommended to add an access-controlled external function to the \u0060MultichainGovernor\u0060 contract, that will enable setting the \u0060pauseGuardian\u0060 to a new address, assuring that the \u0060pauseGuardian\u0060 value is not bricked to \u0060address(0)\u0060 after calling \u0060kickGuardian\u0060 or \u0060unpause\u0060 functions.

**SOVLED:** The Moonwell team has solved this issue by creating an external, access-controlled function \u0060grantPauseGuardian\u0060 in the \u0060MultichainGovernor\u0060 contract.

[GitHub Pull Request](https://github.com/moonwell-ﬁ/moonwell-contracts-v2/pull/147)
