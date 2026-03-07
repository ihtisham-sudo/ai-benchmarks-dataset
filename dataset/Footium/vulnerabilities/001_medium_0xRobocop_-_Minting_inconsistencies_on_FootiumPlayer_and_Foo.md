# 0xRobocop - Minting inconsistencies on FootiumPlayer and FootiumClub

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Footium
**Keywords:** cybersecurity, vulnerability, FootiumClub, FootiumPlayer, minting inconsistencies, NFT, smart contract, Ethereum, solidity, manual review, safe minting, contract compatibility, code review, blockchain, decentralized applications, security best practices, mint function, contract audit, risk assessment, development recommendations

---

0xRobocop

medium

# Minting inconsistencies on FootiumPlayer and FootiumClub

## Summary

The \u0060FootiumClub.sol\u0060 contract when minting uses \u0060_mint()\u0060 instead of \u0060_safeMint()\u0060 which can cause to mint a club to a contract who does not support nfts. On the other hand \u0060FootiumPlayer.sol\u0060 uses \u0060_safeMint()\u0060.

## Vulnerability Detail

See summary.

## Impact

\u0060FootiumClub.sol\u0060 might mint a club NFT to a contract that cannot handle nfts.

## Code Snippet

https://github.com/sherlock-audit/2023-04-footium/blob/main/footium-eth-shareable/contracts/FootiumClub.sol#L65

## Tool used

Manual Review

## Recommendation

Use \u0060_safeMint()\u0060 as in FootiumPlayer.

