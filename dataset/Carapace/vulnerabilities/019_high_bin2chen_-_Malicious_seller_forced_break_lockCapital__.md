# bin2chen - Malicious seller forced break lockCapital()

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, NFT, burn, lockCapital, lendingPool, malicious seller, PremiumAmount, compensation, protectionPool, ERC721, tokenId, ownerOf, principalAmount, principalRedeemed, tokenBurned, manual review, try catch, solidity, smart contract

---

bin2chen

high

# Malicious seller forced break lockCapital()

## Summary

Malicious burn nft causes failure to lockCapital() ，seller steady earn PremiumAmount, buyer will be lost compensation

## Vulnerability Detail
When the status of the lendingPool changes from Active to Late, the protocol will call ProtectionPool.lockCapital() to  lock amount
lockCapital() will loop through the active protections to calculate the \u0060\u0060\u0060lockedAmount\u0060\u0060\u0060.
The code is as follows:
\u0060\u0060\u0060solidity
  function lockCapital(address _lendingPoolAddress)
    external
    payable
    override
    onlyDefaultStateManager
    whenNotPaused
    returns (uint256 _lockedAmount, uint256 _snapshotId)
  {
....
    uint256 _length = activeProtectionIndexes.length();
    for (uint256 i; i < _length; ) {
...
      uint256 _remainingPrincipal = poolInfo
        .referenceLendingPools
        .calculateRemainingPrincipal(            //<----------- calculate Remaining Principal
          _lendingPoolAddress,
          protectionInfo.buyer,
          protectionInfo.purchaseParams.nftLpTokenId
        );
\u0060\u0060\u0060
The important thing inside is to calculate the _remainingPrincipal by \u0060\u0060\u0060referenceLendingPools.calculateRemainingPrincipal()\u0060\u0060\u0060

\u0060\u0060\u0060solidity
  function calculateRemainingPrincipal(
    address _lendingPoolAddress,
    address _lender,
    uint256 _nftLpTokenId
  ) public view override returns (uint256 _principalRemaining) {
...

    if (_poolTokens.ownerOf(_nftLpTokenId) == _lender) {   //<------------call ownerOf()
      IPoolTokens.TokenInfo memory _tokenInfo = _poolTokens.getTokenInfo(
        _nftLpTokenId
      );

....
      if (
        _tokenInfo.pool == _lendingPoolAddress &&
        _isJuniorTrancheId(_tokenInfo.tranche)
      ) {
        _principalRemaining =
          _tokenInfo.principalAmount -
          _tokenInfo.principalRedeemed;
      }
    }
  }
\u0060\u0060\u0060
GoldfinchAdapter.calculateRemainingPrincipal()
The current implementation will first determine if the ownerOf the NFTID is _lender

There is a potential problem here, if the NFTID has been burned, the ownerOf() will be directly revert, which will lead to calculateRemainingPrincipal() revert,and lockCapital() revert and can\u0027t change status from active to late

Let\u0027s see whether Goldfinch\u0027s implementation supports burn(NFTID), and whether ownerOf(NFTID) will revert

1. PoolTokens has burn() method , if principalRedeemed==principalAmount you can burn it

\u0060\u0060\u0060solidity
contract PoolTokens is IPoolTokens, ERC721PresetMinterPauserAutoIdUpgradeSafe, HasAdmin, IERC2981 {
.....
  function burn(uint256 tokenId) external virtual override whenNotPaused {
    TokenInfo memory token = _getTokenInfo(tokenId);
    bool canBurn = _isApprovedOrOwner(_msgSender(), tokenId);
    bool fromTokenPool = _validPool(_msgSender()) && token.pool == _msgSender();
    address owner = ownerOf(tokenId);
    require(canBurn || fromTokenPool, "ERC721Burnable: caller cannot burn this token");
    require(token.principalRedeemed == token.principalAmount, "Can only burn fully redeemed tokens");
    _destroyAndBurn(tokenId);
    emit TokenBurned(owner, token.pool, tokenId);
  }
\u0060\u0060\u0060
https://github.com/goldfinch-eng/mono/blob/88f0e3f94f6dd23ebae429fe09e2511650df893a/packages/protocol/contracts/protocol/core/PoolTokens.sol#L199

2.ownerOf() if nftid don\u0027t exists  will revert with message "ERC721: owner query for nonexistent token"

\u0060\u0060\u0060solidity
contract ERC721UpgradeSafe is
  Initializable,
  ContextUpgradeSafe,
  ERC165UpgradeSafe,
  IERC721,
  IERC721Metadata,
  IERC721Enumerable
{
...
  function ownerOf(uint256 tokenId) public view override returns (address) {
    return _tokenOwners.get(tokenId, "ERC721: owner query for nonexistent token");
  }
\u0060\u0060\u0060
https://github.com/goldfinch-eng/mono/blob/88f0e3f94f6dd23ebae429fe09e2511650df893a/packages/protocol/contracts/external/ERC721.sol#L136-L138

If it can\u0027t changes to late, Won\u0027t lock the fund, seller steady earn PremiumAmount

So there are two risks
1. normal buyer gives NFTID to burn(), he does not know that it will affect all protection of the lendingPool
2. Malicious seller can buy a protection first, then burn it, so as to force all protection of the lendingPool to expire and get the PremiumAmount maliciously. buyer unable to obtain compensation

Suggested try catch for _poolTokens.ownerOf() If revert, it is assumed that the lender is not the owner

## Impact

buyer will be lost compensation

## Code Snippet

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L389-L395

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/adapters/GoldfinchAdapter.sol#L162-L165

## Tool used

Manual Review

## Recommendation

try catch for _poolTokens.ownerOf() If revert, it is assumed that the lender is not the owner

