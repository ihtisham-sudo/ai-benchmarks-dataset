# eeyore - \u0060Voter.replaceFactory()\u0060 and \u0060Voter.addFactory()\u0060 functions are broken.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** Voter, replaceFactory, addFactory, cyber security, vulnerability, validation, isFactory, isGaugeFactory, factories, gaugeFactories, invariant, DoS, createGauge, code review, manual review, impact, recommendation, security flaw, smart contract, blockchain

---

eeyore

Medium

# \u0060Voter.replaceFactory()\u0060 and \u0060Voter.addFactory()\u0060 functions are broken.

## Summary

The \u0060Voter.replaceFactory()\u0060 and \u0060Voter.addFactory()\u0060 functions are broken due to invalid validation.

## Vulnerability Detail

1. In the \u0060addFactory()\u0060 function, the line \u0060require(!isFactory[_pairFactory], \u0027factory true\u0027);\u0060 is missing.
2. In the \u0060replaceFactory()\u0060 function, the \u0060isFactory\u0060 and \u0060isGaugeFactory\u0060 checks are incorrect:

\u0060\u0060\u0060solidity
        require(isFactory[_pairFactory], \u0027factory false\u0027); // <=== should be !isFactory
        require(isGaugeFactory[_gaugeFactory], \u0027g.fact false\u0027); // <=== should be !isGaugeFactory
\u0060\u0060\u0060

These issues lead to the invariant being broken, allowing multiple instances of a factory or gauge to be pushed to the \u0060factories\u0060 and \u0060gaugeFactories\u0060 arrays.

## Impact

Broken code. DoS when calling \u0060Voter.createGauge()\u0060.

## Code Snippet

https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/Voter.sol#L155-L185

## Tool used

Manual Review

## Recommendation

1. Add the \u0060require(!isFactory[_pairFactory], \u0027factory true\u0027);\u0060 validation to the \u0060addFactory()\u0060 function.
2. Fix the checks in the \u0060replaceFactory()\u0060 function:

\u0060\u0060\u0060diff
-        require(isFactory[_pairFactory], \u0027factory false\u0027);
+        require(!isFactory[_pairFactory], \u0027factory true\u0027);
-        require(isGaugeFactory[_gaugeFactory], \u0027g.fact false\u0027);
+        require(!isGaugeFactory[_gaugeFactory], \u0027g.fact true\u0027);
\u0060\u0060\u0060

