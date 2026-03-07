# jkoppel - Problems with tokens that transfer less than amount. (Separate from fee-on-transfer issues!)

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cyber security, vulnerability, tokens, transfer functions, cUSDCv3, user balance, pool operations, fee-on-transfer, allo.fundPool, dust attack, poolAmount, DonationVotingMerkleDistributionVaultStrategy, claim, donate, type(uint256).max, funding, protocol, manual review, recommendation, impact

---

jkoppel

medium

# Problems with tokens that transfer less than amount. (Separate from fee-on-transfer issues!)

Some tokens such as cUSDCv3  contain a special case for amount == type(uint256).max in their transfer functions that results in only the user\u0027s balance being transferred. This can be used to shut down several pool operations.

There are also problems with fee-on-transfer tokens, but that\u0027s a separate issue.

The contest FAQ states that all weird tokens should work with this protocol. I also asked the sponsor about this specific category of issues, and they said "this does like something which can be taken advantage of !"

## Vulnerability Detail

Several things that can go wrong with this:

1. An attacker can put dust of this token in a wallet, and then call allo.fundPool() with type(uint256).max of this token. If the pool has not already been funded, then poolAmount will not be at type(uint256).max  despite nothing being in the pool. It is now not possible to fund the pool.

2. Someone can do this in the DonationVotingMerkleDistributionVaultStrategy to set someones claim of this token to type(uint256).max . It is now impossible for anyone else to donate this token to them.

## Impact

Pools cannot work with such tokens

## Code Snippet

See, e.g.: https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-distribution-vault/DonationVotingMerkleDistributionVaultStrategy.sol#L125

## Tool used

Manual Review

## Recommendation

Explicitly do not support these tokens
