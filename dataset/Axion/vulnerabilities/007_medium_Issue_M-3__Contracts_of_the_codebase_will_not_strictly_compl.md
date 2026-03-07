# Issue M-3: Contracts of the codebase will not strictly comply with the ERC-1504.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** ERC-1504, compliance, upgradable contracts, openzeppelin, handler contract, data contract, upgrader contract, smart contract, codebase, readme, deviation, specification, audit, protocol, impact, mitigation, internal, external, attack path, PoC

---

# Issue M-3: Contracts of the codebase will not strictly comply with the ERC-1504.

Source: [https://github.com/sherlock-audit/2024-10-axion-judging/issues/155](https://github.com/sherlock-audit/2024-10-axion-judging/issues/155)

The protocol has acknowledged this issue.

Found by: 0xnbvc, Atharv, AuditorPraise, HackTrace, Kirkeelee, dany.armstrong90, isagixyz, pkqs90

## Summary

Contracts of the codebase isn\u0027t strictly compliant with the ERC-1504. This breaks the readme.

## Root Cause

As per readme:
Is the codebase expected to comply with any EIPs? Can there be/are there any deviations from the specification?
Strictly compliant: ERC-1504: Upgradable Smart Contract

But the contracts of the codebase uses openzeppelin upgradable contracts as base contract which are not compliant with ERC-1504. As per ERC-1504, the upgradable contract should consist of handler contract, data contract and optionally the upgrader contract. But the contracts of the codebase are not compliant with ERC-1504 because they have no data contract and has data inside the handler contract.

## Internal pre-conditions

No response

## External pre-conditions

No response

## Attack Path

No response
## Impact
Breakthereadme.
## PoC
Noresponse
## Mitigation
MakethecontractsstrictlycompliantwithERC-1504.
