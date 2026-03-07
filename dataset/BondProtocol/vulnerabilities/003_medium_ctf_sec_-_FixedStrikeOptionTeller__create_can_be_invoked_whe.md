# ctf_sec - FixedStrikeOptionTeller: create can be invoked when block.timestamp == expiry but exercise reverts

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** BondProtocol
**Keywords:** cybersecurity, vulnerability, FixedStrikeOptionTeller, block.timestamp, expiry, option tokens, minting, exercise function, reverts, create function, staking rewards, OTLM.claimRewards, OTLM.claimNextEpochRewards, claiming rewards, reclaim function, burn statement, loss of funds, timestamp behavior, user claims, option token exercise

---

ctf_sec

medium

# FixedStrikeOptionTeller: create can be invoked when block.timestamp == expiry but exercise reverts

## Summary
In \u0060FixedStrikeOptionTeller\u0060 contract, new option tokens can be minted when \u0060block.timestamp == expiry\u0060 but these option tokens cannot be exercised even in the same transaction.

## Vulnerability Detail
The \u0060create\u0060 function has this statement:
\u0060\u0060\u0060solidity
        if (uint256(expiry) < block.timestamp) revert Teller_OptionExpired(expiry);
\u0060\u0060\u0060

The \u0060exercise\u0060 function has this statement:
\u0060\u0060\u0060solidity
        if (uint48(block.timestamp) >= expiry) revert Teller_OptionExpired(expiry);
\u0060\u0060\u0060
Notice the \u0060>=\u0060 operator which means when \u0060block.timestamp == expiry\u0060 the \u0060exercise\u0060 function reverts.

The \u0060FixedStrikeOptionTeller.create\u0060 function is invoked whenever a user claims his staking rewards using \u0060OTLM.claimRewards\u0060 or \u0060OTLM.claimNextEpochRewards\u0060. ([here](https://github.com/sherlock-audit/2023-06-bond/blob/main/options/src/fixed-strike/liquidity-mining/OTLM.sol#L505))

So if a user claims his rewards when \u0060block.timestamp == expiry\u0060 he receives the freshly minted option tokens but he cannot exercise these option tokens even in the same transaction (or same block).

Moreover, since the receiver do not possess these freshly minted option tokens, he cannot \u0060reclaim\u0060 them either (assuming \u0060reclaim\u0060 function contains the currently missing \u0060optionToken.burn\u0060 statement).


## Impact
Option token will be minted to user but he cannot exercise them. Receiver cannot reclaim them as he doesn\u0027t hold that token amount.

This leads to loss of funds as the minted option tokens become useless. Also the scenario of users claiming at expiry is not rare.

## Code Snippet
https://github.com/sherlock-audit/2023-06-bond/blob/main/options/src/fixed-strike/FixedStrikeOptionTeller.sol#L267
https://github.com/sherlock-audit/2023-06-bond/blob/main/options/src/fixed-strike/FixedStrikeOptionTeller.sol#L336

## Tool used

Manual Review

## Recommendation
Consider maintaining a consistent timestamp behaviour. Either prevent creation of option tokens at expiry or allow them to be exercised at expiry.
