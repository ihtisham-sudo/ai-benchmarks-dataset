# 55 - Update to monsterMultiplier not reflected in stakedTimeBonus

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** FrankenDAO
**Keywords:** stakedTimeBonus, monsterMultiplier, governance proposal, hardcoded value, calculation, votes, staking, ERC721, transferFrom, NFT, contract address, frozen, safeTransferFrom, manual review, specification, fullStakedTimeBonus, medium likelihood, smart contracts, audit, FrankenDAO

---

# Vulnerability Details

\u0060\u0060\u0060solidity
function stake(uint[] calldata _tokenIds, uint _unlockTime) 
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function _stakeToken(uint _tokenId, uint _unlockTime) internal returns (uint) {
   if (_unlockTime > 0) {
     stakedTimeBonus[_tokenId] = _tokenId < 10000 ? fullStakedTimeBonus : fullStakedTimeBonus / 2;
   }
}
\u0060\u0060\u0060

### Description
Hence any update to the monsterMultiplier would not reflect in the calculation of stakedTimeBonus, and thereby votes.

Medium  
Any update to the monsterMultiplier would not be reflected in stakedTimeBonus; it would always remain as /2 or 50%.

### Likelihood
Medium  
One needs to pass a governance proposal to change the monsterMultiplier, so this is definitely not a high likelihood; it\u0027s not low as well, as there is a clear provision in spec regarding this.

### Code Snippet Reference
[GitHub Link](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L393)

Manual Review

Consider replacing the hardcoded value with monsterMultiplier.

- zobront
- Fixed: [GitHub Pull Request](https://github.com/Solidity-Guild/FrankenDAO/pull/12)
- jack-the-pug
- Fix confirmed
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/55)  
**Found by:** WATCHPUG, rvierdiiev, saian, Bnke0x0, Tomo, Nyx

There are certain smart contracts that do not support ERC721; using \u0060transferFrom()\u0060 may result in the NFT being sent to such contracts.

In \u0060unstake()\u0060, \u0060_to\u0060 is a parameter from the user\u0027s input. However, if \u0060_to\u0060 is a contract address that does not support ERC721, the NFT can be frozen in that contract. As per the documentation of EIP-721:

> A wallet/broker/auction application MUST implement the wallet interface if it will accept safe transfers.

**Ref:** [EIP-721](https://eips.ethereum.org/EIPS/eip-721)

The NFT may get stuck in the contract that doesn\u0027t support ERC721.

[Staking.sol Code](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L463-L489)

Manual Review

Consider using \u0060safeTransferFrom()\u0060 instead of \u0060transferFrom()\u0060.
