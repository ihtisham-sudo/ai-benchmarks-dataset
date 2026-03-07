# MiloTruck - Users might lose funds as \u0060claimERC20Prize()\u0060 doesn\u0027t revert for no-revert-on-transfer tokens

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Footium
**Keywords:** cybersecurity, vulnerability, ERC20, tokens, claimERC20Prize, FootiumPrizeDistributor, no-revert-on-failure, transfer, user funds, unclaimable tokens, smart contract, OpenZeppelin, SafeERC20, manual review, insufficient balance, totalERC20Claimed, asset loss, token transfer, contract balance, security recommendation

---

MiloTruck

medium

# Users might lose funds as \u0060claimERC20Prize()\u0060 doesn\u0027t revert for no-revert-on-transfer tokens

## Summary

Users can call \u0060claimERC20Prize()\u0060 without actually receiving tokens if a no-revert-on-failure token is used, causing a portion of their claimable tokens to become unclaimable.

## Vulnerability Detail

In the \u0060FootiumPrizeDistributor\u0060 contract, whitelisted users can call \u0060claimERC20Prize()\u0060 to claim ERC20 tokens. The function adds the amount of tokens claimed to the user\u0027s total claim amount, and then transfers the tokens to the user:

[FootiumPrizeDistributor.sol#L128-L131](https://github.com/sherlock-audit/2023-04-footium/blob/main/footium-eth-shareable/contracts/FootiumPrizeDistributor.sol#L128-L131)

\u0060\u0060\u0060solidity
if (value > 0) {
    totalERC20Claimed[_token][_to] += value;
    _token.transfer(_to, value);
}
\u0060\u0060\u0060

As the the return value from \u0060transfer()\u0060 is not checked, \u0060claimERC20Prize()\u0060 does not revert even when the transfer of tokens to the user fails.

This could potentially cause users to lose assets when:
1. \u0060_token\u0060 is a no-revert-on-failure token.
2. The user calls \u0060claimERC20Prize()\u0060 with \u0060value\u0060 higher than the contract\u0027s token balance.

As the contract has an insufficient balance, \u0060transfer()\u0060 will revert and the user receives no tokens. However, as \u0060claimERC20Prize()\u0060 succeeds, \u0060totalERC20Claimed\u0060 is permanently increased for the user, thus the user cannot claim these tokens again.

## Impact

Users can call \u0060claimERC20Prize()\u0060 without receiving the token amount specified. These tokens become permanently unclaimable for the user, leading to a loss of funds.

## Code Snippet

https://github.com/sherlock-audit/2023-04-footium/blob/main/footium-eth-shareable/contracts/FootiumPrizeDistributor.sol#L128-L131

## Tool used

Manual Review

## Recommendation

Use \u0060safeTransfer()\u0060 from Openzeppelin\u0027s [SafeERC20](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20#SafeERC20) to transfer ERC20 tokens. Note that [\u0060transferERC20()\u0060](https://github.com/sherlock-audit/2023-04-footium/blob/main/footium-eth-shareable/contracts/FootiumEscrow.sol#L105-L111) in \u0060FootiumEscrow.sol\u0060 also uses \u0060transfer()\u0060 and is susceptible to the same vulnerability.
