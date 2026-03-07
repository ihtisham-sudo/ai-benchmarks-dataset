# 0x73696d616f - Vault portion calculation in \u0060PrizePool::getVaultPortion()\u0060 is incorrect as \u0060_startDrawIdInclusive\u0060 has been erased

**Severity:** high
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, vault portion, PrizePool, getVaultPortion, startDrawIdInclusive, overwritten, total accumulator, vaults accumulator, donation accumulator, grand prize, prize frequency, lastAwardedDrawId_, circular buffer, buffer overflow, prize chances, permanent reverts, computeRangeStartDrawIdInclusive, rangeSize, manual review

---

0x73696d616f

high

# Vault portion calculation in \u0060PrizePool::getVaultPortion()\u0060 is incorrect as \u0060_startDrawIdInclusive\u0060 has been erased

## Summary

The vault portion calculation in \u0060PrizePool::getVaultPortion()\u0060 is incorrect because it fetches a \u0060_startDrawIdInclusive\u0060 that has been overwritten in the total accumulator but not in the vaults accumulator or the donation accumulator.

## Vulnerability Detail

To illustrate the issue, consider the grand prize, where odds are \u00601 / g = 0.00273972602e18\u0060 with \u0060g == 365 days\u0060. The [estimated](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/PrizePool.sol#L1014) prize frequency is \u00601e18 / 0.00273972602e18 == 365.000000985\u0060 rounded up to the nearest integer, \u0060366\u0060. If \u0060lastAwardedDrawId_\u0060 is \u0060366\u0060, then \u0060startDrawIdInclusive\u0060 is \u0060366 - 366 + 1 == 1\u0060. 
This means that it will fetch the total, vault and donation accumulators since the opening of \u0060drawId == 1\u0060. 

However, when \u0060lastAwardedDrawId_ == 366\u0060, the current open \u0060drawId\u0060 is \u0060367\u0060, which is written to index 0 in the circular buffer, overwriting \u0060drawId == 1\u0060. But, in the donation and vault cases, the accumulator still has \u0060drawId == 1\u0060, as the buffer will likely not have been overwritten (draw periods take 1 day, it is highly likely the individual accumulators are not written to every day, but the total accumulator is, or users may exploit this on purpose). As the buffer is circular, this will keep happening every time after the buffer has been filled and indexes start being overwritten.

Thus, due to this, the vault portion will be bigger than it should, as the total accumulator is calculated between 365 days (from 2 to 366, as 1 has been erased), but the vault and donation accumulators for 366 days (between 1 and 366). Users will have bigger than expected chances of winning prizes and in the worst case, they may even not be able to claim prizes at all, in case the erased \u0060drawId\u0060 had a significant contribution to the prizes through a donation, and then it underflows when doing \u0060totalSupply = totalContributed - totalDonated;\u0060 in [PrizePool::getVaultShares()](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/PrizePool.sol#L1129).

Add the following test to \u0060PrizePool.t.sol\u0060 and log the vault and total portions in \u0060PrizePool::getVaultShares()\u0060. The contribution of the vault will be bigger than the total.
\u0060\u0060\u0060solidity
function testAccountedBalance_POC() public {
  for (uint i = 0; i < 366; i++) {
    contribute(100e18);
    awardDraw(1);
    mockTwab(address(this), msg.sender, 0);
  }
  address otherVault = makeAddr("otherVault");
  vm.prank(otherVault);
  prizePool.contributePrizeTokens(otherVault, 0);
  uint256 prize = claimPrize(msg.sender, 0, 0);
}
\u0060\u0060\u0060

## Impact

Users get better prize chances than supposed and/or it can lead to permanent reverts when trying to claim prizes.

## Code Snippet

https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/PrizePool.sol#L1014

## Tool used

Manual Review

Vscode

## Recommendation

When calculating \u0060PrizePool::computeRangeStartDrawIdInclusive()\u0060, the \u0060rangeSize\u0060 should be capped to \u0060365\u0060 to ensure the right \u0060startDrawIdInclusive\u0060 is fetched, not one that has already been erased. In the scenario above, if the range is capped at 365, when \u0060lastAwardedDrawId_ == 366\u0060, \u0060startDrawIdInclusive\u0060 would be \u0060366 - 365 + 1 == 2\u0060, which has not been erased as the current \u0060drawId\u0060 is \u0060367\u0060, having only overwritten \u0060drawId == 1\u0060, but 2 still has the information. 
