# hash - Downcasting to uint96 can cause assets to be lost for some tokens

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axis Finance
**Keywords:** cybersecurity, vulnerability, downcasting, uint96, asset loss, tokens, auction, overflow, bid amounts, total bid amount, shiba inu, auctioneer, extreme loss, manual review, code snippet, higher type, limitations, recommendation, smart contracts, financial risk

---

hash

medium

# Downcasting to uint96 can cause assets to be lost for some tokens

## Summary
Downcasting to uint96 can cause assets to be lost for some tokens

## Vulnerability Detail

After summing the individual bid amounts, the total bid amount is downcasted to uint96 without any checks

\u0060\u0060\u0060solidity
            settlement_.totalIn = uint96(result.totalAmountIn);
\u0060\u0060\u0060

uint96 can be overflowed for multiple well traded tokens:

Eg:

shiba inu :
current price = $0.00003058
value of type(uint96).max tokens ~= 2^96 * 0.00003058 / 10^18 == 2.5 million $

Hence auctions that receive more than type(uint96).max amount of tokens will be downcasted leading to extreme loss for the auctioner

## Impact

The auctioner will suffer extreme loss in situations where the auctions bring in >uint96 amount of tokens

## Code Snippet

downcasting totalAmountIn to uint96
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/modules/auctions/EMPAM.sol#L825

## Tool used

Manual Review

## Recommendation

Use a higher type or warn the user\u0027s of the limitations on the auction sizes
