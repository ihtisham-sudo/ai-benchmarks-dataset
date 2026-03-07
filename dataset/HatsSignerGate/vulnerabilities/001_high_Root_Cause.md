# Root Cause

**Severity:** high
**Auditor:** Sherlock
**Protocol:** HatsSignerGate
**Keywords:** HSG, detach, Safe, signer, admin rights, multi-sig, overturn, custody, attack, vulnerability, front-run, loop, transfer, signer hat, max supply, DAO, emit Detached, execRemoveHSGAsGuard, execDisableHSGAsOnlyModule, rights

---

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2024-11-hats-protocol-judging/issues/4)

The protocol has acknowledged this issue.

**Found by:** bughuntoor

After a user no longer owns a hat, although they are no longer treated as a valid signer, they remain an owner within the Safe, until \u0060removeSigner\u0060 is called.

\u0060\u0060\u0060solidity
function detachHSG() public {
    _checkUnlocked();
    _checkOwner();
    ISafe s = safe; // save SLOAD
    // first remove as guard, then as module
    s.execRemoveHSGAsGuard();
    s.execDisableHSGAsOnlyModule();
    emit Detached();
}
\u0060\u0060\u0060

When HSG is detached, it does not check if there\u0027s any Safe owners who no longer wear the necessary hat. For this reason, if there\u0027s such owners, they\u0027ll remain rights within the multi-sig. Depending on their number, they might be able to overturn the multi-sig, or at least disallow them to reach quorum.

However, this attack can further be weaponized if one of the signer hats has admin rights over another signer hat. If the said admin hat wants to overturn the multi-sig and gain full access of it upon detaching, they can simply front-run the \u0060detachHSG\u0060 call and do a loop of 1) transferring the lower hat to a new address 2) claiming it as a signer. Then, when the \u0060detachHSG\u0060 executes, all of these addresses that the attacker had looped through would be owners of the safe and in most cases that should be enough to fully overturn the multi-sig and claim full custody of it.
# Root Cause
detachHSG does not check if there are Safe owners who no longer wear the necessary hat.
## Attack Path
1. DAO plans to detach from HSG
2. There exists a user who has admin hat over a signer hat which has a set max supply of 1.
3. DAO calls detach from HSG
4. The admin hat owner front-runs the tx and does a loop of transferring the hat and adding it as a signer. This gives a lot of wallets owner rights within the Safe, which would otherwise be worthless if HSG remains active.
5. The DAO gets detached and all of the wallets the admin hat owner had looped through now are owners within the Safe.
6. This would usually give full custody to the attacker, or at the very least guarantee the DAO is not able to execute anything on their own.
## Impact
Attacker can gain full custody over a Safe upon HSG detachment.
## Affected Code
[HatsSignerGate.sol](https://github.com/sherlock-audit/2024-11-hats-protocol/blob/main/hats-zodiac/src/HatsSignerGate.sol#L341)
