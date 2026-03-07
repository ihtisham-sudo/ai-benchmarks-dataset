# Governance is a single point of failure

**Severity:** HIGH
**Auditor:** TrailOfBits

---

## Diﬃculty: Medium

**Type:** Timing

**Target:** throughout the codebase

## Description

Because the governance role is responsible for critical functionalities, it constitutes a single point of failure within the Loans and Revolving Credit Lines. The role can perform the following privileged operations:

- Registering and deploying new products
- Setting economic parameters
- Entering the pool into a non-standard payment procedure
- Setting the phases of the Loans and Revolving Credit Lines
- Proposing and executing timelock operations
- Granting and revoking lender and borrower roles, respectively
- Changing the yield providers used by the Pool Custodian

These privileges give governance complete control over the protocol and critical protocol operations. This increases the likelihood that the governance account will be targeted by an attacker and incentivizes governance to act maliciously.

## Exploit Scenario

Eve, a malicious actor, manages to take over the governance address. She then changes the yield providers to her own smart contract, effectively stealing all the funds in the Atlendis Labs protocol.

## Recommendations

- **Short term:** Consider splitting the privileges across different addresses to reduce the impact of governance compromise. Ensure these powers and privileges are kept as minimal as possible.
  
- **Long term:** Document an incident response plan (see Appendix H) and ensure that the private keys for the multisig are managed safely (see Appendix G).

---

Trail of Bits  
Atlendis Labs Security Assessment  
PUBLIC
