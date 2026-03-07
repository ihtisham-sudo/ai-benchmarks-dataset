# .2 Disallowchangingcloudguardianduringrecovery

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** cloud guardian, recovery, account, change address, function, enforcement, security, smart contract, vulnerability, risk, address change, module, validation, state, progress, protection, access control, protocol, safety, compliance

---

# .2 Disallowchangingcloudguardianduringrecovery
- **Severity**: MediumRisk
- **Context**: CloudRecoveryModule.sol#L74-L87
- **Description**: An account can change its cloud guardian address by calling the ✉♣❞❛t❡●✉❛r❞✐❛♥✭✮ function on the ❈❧♦✉❞❘❡❝♦✈❡r②▼♦❞✉❧❡. The comments of this function state that "Recovery must not be in progress for the account", but this is currently not enforced.
- **Recommendation**: Disallow changing the cloud guardian address if a recovery is in progress for the account:
