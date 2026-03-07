# ZdravkoHr. - Max allocations can be bypassed with multiple addresses because of guaranteed allocations

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zap Protocol
**Keywords:** cybersecurity, vulnerability, TokenSale, maxAllocations, allocations, Ethereum, malicious user, staking, IDOs, protocol, maxTierAlloc, calculateMaxAllocation, multiple addresses, manual review, impact, security flaw, allocation exploit, user rights, smart contracts, token distribution

---

ZdravkoHr.

medium

# Max allocations can be bypassed with multiple addresses because of guaranteed allocations

## Summary
[\u0060TokenSale._processPrivate()\u0060](https://github.com/sherlock-audit/2024-03-zap-protocol/blob/c2ad35aa844899fa24f6ed0cbfcf6c7e611b061a/zap-contracts-labs/contracts/TokenSale.sol#L226) ensures that a user cannot deposit more than their allocation amount. However, each address can deposit up to at least \u0060maxAllocations\u0060. This can be leveraged by a malicious user by using different addresses to claim all tokens without even staking.

## Vulnerability Detail
The idea of the protocol is to give everyone the right to have at least \u0060maxAlocations\u0060 allocations. By completing missions, users level up and unlock new tiers. This process will be increasing their allocations. The problem is that when a user has no allocations, they have still a granted amount of \u0060maxAllocations\u0060.

[\u0060TokenSale.calculateMaxAllocation\u0060](https://github.com/sherlock-audit/2024-03-zap-protocol/blob/c2ad35aa844899fa24f6ed0cbfcf6c7e611b061a/zap-contracts-labs/contracts/TokenSale.sol#L259C1-L267C6) returns $max(maxTierAlloc(), maxAllocation)$

For a user with no allocations, \u0060_maxTierAlloc()\u0060 will return 0. The final result will be that this user have \u0060maxAllocation\u0060 allocations (because maxAllocation > 0).
\u0060\u0060\u0060solidity
        if (userTier == 0 && giftedTierAllc == 0) {
            return 0;
        }
\u0060\u0060\u0060

Multiple Ethereum accounts can be used by the same party to take control over the IDO and all its allocations, on top of that without even staking.

*NOTE*: setting \u0060maxAllocation = 0\u0060 is not a solution in this case because the protocol wants to still give some allocations to their users.

## Impact
Buying all allocations without staking. This also violates a key property that only ION holders can deposit.

## Code Snippet
\u0060\u0060\u0060solidity
    function calculateMaxAllocation(address _sender) public returns (uint256) {
        uint256 userMaxAllc = _maxTierAllc(_sender);

        if (userMaxAllc > maxAllocation) {
            return userMaxAllc;
        } else {
            return maxAllocation;
        }
    }
\u0060\u0060\u0060
## Tool used

Manual Review

## Recommendation
A possible solution may be to modify \u0060calculateMaxAllocation\u0060 in the following way:
\u0060\u0060\u0060diff
    function calculateMaxAllocation(address _sender) public returns (uint256) {
        uint256 userMaxAllc = _maxTierAllc(_sender);
+       if (userMaxAllc == 0) return 0;

         if (userMaxAllc > maxAllocation) {
            return userMaxAllc;
        } else {
            return maxAllocation;
        }
    }
\u0060\u0060\u0060
