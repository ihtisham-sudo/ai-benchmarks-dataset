# mstpr-brainbot - Clubs can mint +1 players more than maxGenerationId

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Footium
**Keywords:** cybersecurity, vulnerability, minting, players, maxGenerationId, off-by-one error, academy contract, generation ID, protocol, documentation, impact, high severity, manual review, recommendation, code snippet, inconsistent behavior, security flaw, smart contract, blockchain, error handling

---

mstpr-brainbot

high

# Clubs can mint +1 players more than maxGenerationId

## Summary
As stated in doc here
<img width="1007" alt="image" src="https://user-images.githubusercontent.com/120012681/236145880-57018bcf-d25d-4c4f-a3f0-b8bfcdc4f57a.png">
Initially clubs should be able to mint 10 players. However, clubs can always mint +1 players more than \u0060maxGenerationId\u0060 
## Vulnerability Detail
An off-by-one error is existed in academy contract when checking the generation ID while minting players. The code currently allows clubs to mint up to \u0060maxGenerationId + 1\u0060 players, which is inconsistent with the documentation. If clubs send generation IDs in the following sequence: 0-1-2-3-4-5-6-7-8-9-10, all of these numbers will be valid, and the club will be able to mint \u0060maxGenerationId + 1 \u0060 players instead of the intended \u0060maxGenerationId\u0060

## Impact
Since this is not intended behaviour according to the protocol docs, I\u0027ll label it as high.
## Code Snippet
https://github.com/sherlock-audit/2023-04-footium/blob/main/footium-eth-shareable/contracts/FootiumAcademy.sol#L186-L188
here code checks whether the generation id is higher than maxGeneration or not, and it can be equal to maxGeneration.
## Tool used

Manual Review

## Recommendation
Use \u0060generationId >= _maxGenerationId\u0060 or do not count the "0" index
