# tedox - Contract will reach a point where users will not be able to call \u0060deposit\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, smart contract, deposit, collateral, collateralTotalCap, denial of service, tradeTokenCollateral, subTradeTokenCollateral, manual review, withdraw, token, vault, contract, revert, checks, inaccurate value, tokens, function, impact

---

tedox

High

# Contract will reach a point where users will not be able to call \u0060deposit\u0060

## Summary
With the contract working as intended, after a long enough period of time the perceived amount of collateral for a specific point will cross \u0060collateralTotalCap\u0060 resulting in the fact that users will not be able to deposit more tokens of that type.

## Vulnerability Detail
When \u0060deposit\u0060 is called, after the necessary checks the method \u0060commonData.addTradeTokenCollateral\u0060 is called which increases the total amount of collateral for a specific token in order to track how much collateral of this type of token exists and so that it does not cross the \u0060collateralTotalCap\u0060. 

On the other hand, the function \u0060subTradeTokenCollateral\u0060 which is used to reduce the amount of total collateral per token is never called anywhere in the project resulting in an inaccurate value for \u0060self.tradeCollateralTokenDatas[token].totalCollateral\u0060 as it tracks the amount of tokens that have entered the contract and not how many tokens are currently present inside the vault of the contract. And because there is a check weather the calling \u0060deposit\u0060 would pass this cap it will eventually make it so that calling \u0060deposit\u0060 with specific tokens would revert every time.

## Impact
Eventual denial of service for \u0060deposit\u0060

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/AssetsProcess.sol#L81-L120

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/storage/CommonData.sol#L74-L84

## Tool used
Manual Review

## Recommendation
Call \u0060subTradeTokenCollateral\u0060 when the amount of collateral is being reduced (e.g. calling \u0060withdraw\u0060)
