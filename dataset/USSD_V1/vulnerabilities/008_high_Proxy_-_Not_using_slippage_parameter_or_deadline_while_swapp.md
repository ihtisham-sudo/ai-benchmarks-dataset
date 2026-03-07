# Proxy - Not using slippage parameter or deadline while swapping on UniswapV3

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** UniswapV3, cybersecurity, vulnerability, slippage parameter, amountOutMinimum, deadline parameter, swap, funds loss, MEV bot, sandwich attacks, transaction execution, mempool, price impact, token swap, smart contract, DeFi, manual review, security recommendation, catastrophic loss, crypto trading

---

Proxy

medium

# Not using slippage parameter or deadline while swapping on UniswapV3

## Summary

While making a swap on UniswapV3 the caller should use the slippage parameter \u0060amountOutMinimum\u0060 and \u0060deadline\u0060 parameter to avoid losing funds.

## Vulnerability Detail

[\u0060UniV3SwapInput()\u0060](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L227-L240) in \u0060USSD\u0060 contract does not use the slippage parameter [\u0060amountOutMinimum\u0060](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L237)  nor [\u0060deadline\u0060](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L235). 

\u0060amountOutMinimum\u0060 is used to specify the minimum amount of tokens the caller wants to be returned from a swap. Using \u0060amountOutMinimum = 0\u0060 tells the swap that the caller will accept a minimum amount of 0 output tokens from the swap, opening up the user to a catastrophic loss of funds via [MEV bot sandwich attacks](https://medium.com/coinmonks/defi-sandwich-attack-explain-776f6f43b2fd). 

\u0060deadline\u0060 lets the caller specify a deadline parameter that enforces a time limit by which the transaction must be executed. Without a deadline parameter, the transaction may sit in the mempool and be executed at a much later time potentially resulting in a worse price for the user.

## Impact

Loss of funds and not getting the correct amount of tokens in return.

## Code Snippet

- Function [\u0060UniV3SwapInput()\u0060](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L227-L240)
  - Not using [\u0060amountOutMinimum\u0060](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L237)
  - Not using [\u0060deadline\u0060](https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L235)


## Tool used

Manual Review

## Recommendation

Use parameters \u0060amountOutMinimum\u0060 and \u0060deadline\u0060 correctly to avoid loss of funds.
