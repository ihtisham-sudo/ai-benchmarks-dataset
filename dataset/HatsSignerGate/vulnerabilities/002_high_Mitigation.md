# Mitigation

**Severity:** high
**Auditor:** Sherlock
**Protocol:** HatsSignerGate
**Keywords:** reentrancy, checkTransaction, delegate call, owner list, threshold, signer, multi-sig, bypass, security, vulnerability, HatsSignerGate, Ethereum, smart contract, attack path, mitigation, fallback handler, transaction, audit, protocol

---

# Mitigation
Upon detaching HSG, loop through all Safe owners and in case a wallet does not wear the necessary hat, unregister them as a signer.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2024-11-hats-protocol-judging/issues/3)  
**Found by:** bughuntoor  

In order to make sure that a delegate call does not change Safe\u0027s state, HSG\u0027s \u0060checkTransaction\u0060 stores the current threshold, owners list, and fallback handler. Then, after the call is executed, \u0060checkAfterExecution\u0060 is supposed to verify that these variables have not been changed.

\u0060\u0060\u0060solidity
if (operation == Enum.Operation.DelegateCall) {
    // case: DELEGATECALL
    // We disallow delegatecalls to unapproved targets
    if (!enabledDelegatecallTargets[to]) revert DelegatecallTargetNotEnabled();
    // Otherwise record the existing owners and threshold for post-flight checks to
    // ensure that Safe state has not been altered
    _existingOwnersHash = keccak256(abi.encode(owners));
    _existingThreshold = threshold;
    _existingFallbackHandler = safe.getSafeFallbackHandler();
}
\u0060\u0060\u0060

However, since the \u0060checkTransaction\u0060 can be re-entered by a new call, these restrictions can easily be bypassed. If the delegate call changes the owners and the threshold, the executing signer can then just provide a new transaction to be executed with the new owners being just him and threshold set to 1. This will then override the above stored variables. Because of this the \u0060checkAfterExecution\u0060 check will also succeed.
## Root Cause
Possible reentrancy within \u0060checkTransaction\u0060

## Attack Path
1. Signers sign a tx which would alter the owners list and set the threshold to 1.
2. Within that delegate call, the only remaining owner signs a new transaction and executes it. It doesn\u0027t realistically matter what the tx is.
## Vulnerabilities

1. checkTransaction is entered. _existingOwnersHash and _existingThreshold are overwritten.
2. The checkAfterExecution on both the inner and the outer call check against the altered values, hence they both succeed.
3. In the end, the intended restrictions are bypassed and the owner list and threshold are both overwritten.
4. The user who has remained the only owner has full access over the multi-sig until the other owners re-claim their hats.

### Affected Code
[HatsSignerGate.sol](https://github.com/sherlock-audit/2024-11-hats-protocol/blob/main/hats-zodiac/src/HatsSignerGate.sol#L471)

### Impact
User can bypass intended restrictions not to be able to overwrite the owner list and threshold variables.

### Mitigation
If checkTransaction is entered, and the transient variables have already been assigned values, revert if the values differ from the current ones.

### Discussion
spengrah  
Fix PR: [#81](https://github.com/Hats-Protocol/hats-zodiac/pull/81)  
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [#81](https://github.com/Hats-Protocol/hats-zodiac/pull/81)
PAGE END
