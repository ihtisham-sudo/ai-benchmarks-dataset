# IllIllI - No slippage control on maker LP \u0060deposit()\u0060/\u0060withdraw()\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Perpetual Protocol
**Keywords:** cybersecurity, vulnerability, slippage control, maker LP, deposit function, withdraw function, collateral loss, market movements, preview functions, UI, transaction, redeem shares, flash crash, arbitrage, price impact, Pyth oracle, manual review, recommendation, slippage parameters, smart contracts, decentralized finance

---

IllIllI

medium

# No slippage control on maker LP \u0060deposit()\u0060/\u0060withdraw()\u0060

## Summary

There are no slippage control arguments for maker LP \u0060deposit()\u0060/\u0060withdraw()\u0060


## Vulnerability Detail

There are no arguments to the \u0060deposit()\u0060/\u0060withdraw()\u0060 functions to limit the amount of collateral lost to market movements, and there are no preview functions to allow a UI to show how much collateral would be received when shares are redeemed.


## Impact

A user may submit a transaction to redeem approximately $100 worth of shares given base price X, but when the block gets mined two seconds later, the price is at 0.5X due to a flash crash. By the time the user sees what they got, the crash has been arbitraged away, and the base price is back at price X, with the user having gotten half the amount they should have.


## Code Snippet

Users can only specify inputs, not expected outputs:
\u0060\u0060\u0060solidity
// File: src/maker/OracleMaker.sol : OracleMaker.deposit()   #1

175:        function deposit(uint256 amountXCD) external onlyWhitelistLp returns (uint256) {
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/maker/OracleMaker.sol#L165-L185

\u0060\u0060\u0060solidity
// File: src/maker/OracleMaker.sol : OracleMaker.withdraw()   #2

228:        function withdraw(uint256 shares) external onlyWhitelistLp returns (uint256) {
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/maker/OracleMaker.sol#L218-L238

and the value received is based on the Pyth [oracle](https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/maker/OracleMaker.sol#L439-L443).


## Tool used

Manual Review


## Recommendation

Provide slippage parameters
