# p0wd3r - \u0060fundPool\u0060 does not work with fee-on-transfer token

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, fundPool, fee-on-transfer token, transferFrom, increasePoolAmount, amountAfterFee, recorded balance, actual balance, impact, manual review, recommendation, token balance, smart contract, decentralized finance, security audit, tokenomics, financial loss, risk assessment, blockchain security

---

p0wd3r

medium

# \u0060fundPool\u0060 does not work with fee-on-transfer token
\u0060fundPool\u0060 does not work with fee-on-transfer token
## Vulnerability Detail
In \u0060_fundPool\u0060, the parameter for \u0060increasePoolAmount\u0060 is directly the amount used in the \u0060transferFrom\u0060 call.

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/core/Allo.sol#L516-L517
\u0060\u0060\u0060solidity
        _transferAmountFrom(_token, TransferData({from: msg.sender, to: address(_strategy), amount: amountAfterFee}));
        _strategy.increasePoolAmount(amountAfterFee);
\u0060\u0060\u0060

When \u0060_token\u0060 is a fee-on-transfer token, the actual amount transferred to \u0060_strategy\u0060 will be less than \u0060amountAfterFee\u0060. Therefore, the current approach could lead to a recorded balance that is greater than the actual balance.
## Impact
\u0060fundPool\u0060 does not work with fee-on-transfer token
## Code Snippet
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/core/Allo.sol#L516-L517
## Tool used

Manual Review

## Recommendation
Use the change in \u0060_token\u0060 balance as the parameter for \u0060increasePoolAmount\u0060.
