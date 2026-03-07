# GalloDaSballo - \u0060changeMaxGenerationId\u0060 allows to mint tokens from older generations retroactively

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Footium
**Keywords:** cybersecurity, vulnerability, changeMaxGenerationId, mint tokens, older generations, merkleProofs, current season, limit raised, minting players, older seasons, maxGenerationId, MerkleProofUpgradeable, verify, generationIds, seasonId, impact, X tokens, manual review, recommendation, validation

---

GalloDaSballo

medium

# \u0060changeMaxGenerationId\u0060 allows to mint tokens from older generations retroactively

## Summary

\u0060changeMaxGenerationId\u0060 is meant to allow more minting for the current generation, however, because of the fact that merkleProofs do not validate for the current season, whenever the limit will be raised, the limit will allow to mint players from older seasons

It will unlock a lot more minting than it may be intended

## Vulnerability Detail

If for any reason \u0060maxGenerationId\u0060 is increased, because of the fact that \u0060MerkleProofUpgradeable.verify\u0060 doesn\u0027t check for \u0060generationIds\u0060 and \u0060seasonId\u0060 then not only new players from the current season can be minted, but also players from older seasons.

## Impact

Minting of X tokens where X is the number of old seasons

## Code Snippet

https://github.com/sherlock-audit/2023-04-footium/blob/main/footium-eth-shareable/contracts/FootiumAcademy.sol#L257-L269

## Tool used

Manual Review

## Recommendation

Enforce minting exclusively for the current season or change validation to validate the generations and seasons being minted
