# minhquanym - Inconsistent check in \u0060harvestPositionsTo()\u0060 function

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** MagicSea Staking
**Keywords:** cyber security, vulnerability, harvestPositionsTo, inconsistent check, approved address, token owner, msg.sender, NFT owner, function contradiction, manual review, code snippet, impact assessment, security recommendation, smart contract, access control, functionality limitation, authorization, blockchain security, function logic, code review

---

minhquanym

Medium

# Inconsistent check in \u0060harvestPositionsTo()\u0060 function

## Summary
Inconsistent check in \u0060harvestPositionsTo()\u0060 function limits the ability of approved address to harvest on behalf of owner.

## Vulnerability Detail
In the function \u0060harvestPositionsTo()\u0060, function \u0060_requireOnlyApprovedOrOwnerOf()\u0060 allows owner or approved address to harvest for the position.

However, the check \u0060(msg.sender == tokenOwner && msg.sender == to)\u0060 only allowing the caller to be token owner. Thus these 2 checks are contradicted.
\u0060\u0060\u0060solidity
function harvestPositionsTo(uint256[] calldata tokenIds, address to) external override nonReentrant {
    _updatePool();

    uint256 length = tokenIds.length;

    for (uint256 i = 0; i < length; ++i) {
        uint256 tokenId = tokenIds[i];
        _requireOnlyApprovedOrOwnerOf(tokenId);
        address tokenOwner = ERC721Upgradeable.ownerOf(tokenId);
        // if sender is the current owner, must also be the harvest dst address
        // if sender is approved, current owner must be a contract
        // @audit not consistent with _requireOnlyApprovedOrOwnerOf()
        require(
            (msg.sender == tokenOwner && msg.sender == to), // legacy || tokenOwner.isContract() 
            "FORBIDDEN"
        );

        _harvestPosition(tokenId, to);
        _updateBoostMultiplierInfoAndRewardDebt(_stakingPositions[tokenId]);
    }
}
\u0060\u0060\u0060

## Impact
Contradictions in the function \u0060harvestPositionsTo()\u0060. Approved address cannot call \u0060harvestPositionsTo()\u0060 on behalf of NFT owner.

## Code Snippet
https://github.com/sherlock-audit/2024-06-magicsea/blob/main/magicsea-staking/src/MlumStaking.sol#L475-L484

## Tool used

Manual Review

## Recommendation
The intended check in function \u0060harvestPositionsTo()\u0060 might be, changing \u0060&&\u0060 to \u0060||\u0060
\u0060\u0060\u0060diff
require(
-    (msg.sender == tokenOwner && msg.sender == to), // legacy || tokenOwner.isContract() 
+    (msg.sender == tokenOwner || msg.sender == to), // legacy || tokenOwner.isContract() 
    "FORBIDDEN"
);
\u0060\u0060\u0060


