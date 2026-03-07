# 7.3.9 L-09. Incorrect Proof-of-Work Difficulty Check in assertValidNonce Function

**Severity:** high
**Auditor:** CodeHawks
**Protocol:** Swan
**Keywords:** Proof-of-Work, difficulty check, nonce, LLMOracleCoordinator, hash, SHA3, taskId, input, requester, responder, validations, computational results, exploitation, threshold, oversight, conditional check, resource wastage, loopholes, integrity, implementation

---

# 7.3.9 L-09. Incorrect Proof-of-Work Difficulty Check in assertValidNonce Function
Submitted by n3smaro, tejaswarambhe. Selected submission by: n3smaro.

The assertValidNonce function in the LLMOracleCoordinator contract incorrectly implements the Proof-of-Work (PoW) difficulty check, allowing invalid nonces to be accepted as valid. This discrepancy could compromise the integrity of the PoW system, leading to unintended acceptance of low-effort computations.

### Vulnerability Detail
The assertValidNonce function is designed to validate a candidate nonce for a task by calculating a hash and comparing it to a difficulty threshold. The intended logic, as specified in the LLMOracleTask interface, is that the computed hash should be less than the difficulty target (SHA3(taskId, input, requester, responder, nonce) < difficulty).

However, in the current implementation:

\u0060\u0060\u0060solidity
if (uint256(keccak256(message)) > type(uint256).max >> uint256(task.parameters.difficulty)) {
    revert InvalidNonce(taskId, nonce);
}
\u0060\u0060\u0060

The conditional check is \u0060>\u0060 rather than \u0060>=\u0060, meaning that nonces resulting in hash values equal to the difficulty target are not validated as per the intended threshold.

This oversight means that some valid PoW nonces are unnecessarily rejected, potentially causing legitimate computations to be discarded. It also creates an inconsistency in how PoW difficulty is enforced, which could be exploited if the system incorrectly interprets validation boundaries.

By incorrectly rejecting nonces that meet but do not exceed the difficulty threshold, this flaw could result in:
- Rejection of valid tasks and associated computational results, leading to wasted resources.
- Potential exploitation, as misinterpreted thresholds might create loopholes for attackers to bypass the difficulty restriction.

Manual Code Review

To align with the intended behavior, update the conditional statement to use \u0060>=\u0060 in order to correctly enforce the difficulty boundary.
PAGE END
