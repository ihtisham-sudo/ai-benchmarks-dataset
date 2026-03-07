# jo13 - Gas Manipulation by Malicious Winners in claimPrizes Function

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, gas manipulation, malicious winners, claimPrizes function, Claimer contract, transaction revert, data chunk, gas limit check, legitimate claims, prize distribution, exploit, fees, penalize, blacklist, smart contract, Ethereum, transaction fees, security recommendation, fairness

---

jo13

medium

# Gas Manipulation by Malicious Winners in claimPrizes Function

## Summary

A malicious winner can exploit the \u0060claimPrizes\u0060 function in the \u0060Claimer\u0060 contract by reverting the transaction through returning a huge data chunk. This manipulation can cause the transaction to run out of gas, preventing legitimate claims and allowing the malicious user to claim prizes without computing winners.

## Vulnerability Detail

- The \u0060Claimer\u0060 contract allows users to claim prizes on behalf of others by calling the \u0060claimPrizes\u0060 function.
- A malicious winner can exploit this function by returning a huge data chunk when called, causing the transaction\u0027s gas to be too high and revert.
- Although the function catches the revert, the remaining gas (63/64 of the original gas) is likely insufficient for the rest of the claims.
- The malicious winner can then replay the transaction to claim the fees from the first claimer\u0027s computation without needing to compute the winners themselves.

## Impact

- Legitimate claimers may lose gas fees due to transaction reverts caused by malicious winners.
- Malicious winners can exploit this to claim prizes without computing winners, undermining the fairness of the prize distribution.

## Recommendation

- Implement a gas limit check to ensure that sufficient gas remains for the rest of the claims after catching a revert.
- Consider adding a mechanism to penalize or blacklist addresses that attempt to exploit this vulnerability.
