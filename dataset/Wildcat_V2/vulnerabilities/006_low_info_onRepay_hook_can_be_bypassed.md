# onRepay hook can be bypassed

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cyber security, vulnerability, onRepay hook, repay function, tokens, market, bypass, mitigation, proof of concept, transfer, exploitation, security flaw, smart contract, decentralized finance, risk assessment, attack vector, remediation, code review, security best practices, blockchain

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/market/WildcatMarket.sol#L168


# Vulnerability details

## Proof of Concept

The onRepay hook only triggers if someone pokes the repay function. This means anyone can bypass it by transferring tokens directly to the market.

\u0060\u0060\u0060solidity
  function _repay(MarketState memory state, uint256 amount, uint256 baseCalldataSize) internal {
    ...
@>    hooks.onRepay(amount, state, baseCalldataSize);
  }
\u0060\u0060\u0060
## Recommended Mitigation Steps

Unsure what\u0027s the best way to fix


## Assessed type

Other
