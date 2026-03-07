# elhaj - Claimers Cannot Claim Prizes When Last Tier Liquidity is 0, Preventing Winners from Receiving Their Prizes

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, claimPrizes, Claimer contract, transaction revert, prizePool, liquidity, maximumFee, tier liquidity, honest claimer, reward distribution, auction mechanism, fee computation, Variable Rate Gradual Dutch Auction, prize claiming, bots, draw, liquidity contribution, claiming process, user rewards

---

elhaj

high

# Claimers Cannot Claim Prizes When Last Tier Liquidity is 0, Preventing Winners from Receiving Their Prizes

## Summary
 - The \u0060Claimer\u0060 contract\u0027s \u0060claimPrizes\u0060 function can revert when the prize for the tier \u0060(numberOfTiers - 3)\u0060 is 0. This prevents all winners in this draw  from receiving their prizes (through claimer) and stops honest claimers from claiming rewards due to the transaction reverting.
## Vulnerability Detail
  - The [PrizePool](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-prize-pool/src/PrizePool.sol) contract holds the prizes and ensures that vault users who contributed to the \u0060PrizePool\u0060 have the chance to win prizes proportional to their contribution and twab balance in every draw. On the other hand, the [Claimer](https://github.com/sherlock-audit/2024-05-pooltogether/blob/main/pt-v5-claimer/src/Claimer.sol) contract facilitates the claiming of prizes on behalf of winners so that winners automatically receive their prizes. **An honest claimer should always have the ability to claim prizes for correct winners in every draw.**
- The [ClaimPrizes](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-claimer/src/Claimer.sol#L90) function in the [Claimer](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-claimer/src/Claimer.sol#L90) contract allows anyone to call it to claim prizes for winners. The caller (bots) computes the winners off-chain and they are incentivized through an auction mechanism where the reward increases over time if prizes are not claimed promptly.
    \u0060\u0060\u0060js
        function claimPrizes(IClaimable _vault, uint8 _tier, address[] calldata _winners, uint32[][] calldata _prizeIndices, address _feeRecipient, uint256 _minFeePerClaim)
            external
            returns (uint256 totalFees)
        {
        //some code ...

            /**
             * If the claimer hasn\u0027t specified both a min fee and a fee recipient, we assume that they don\u0027t
             * expect a fee and save them some gas on the calculation.
             */
            if (!feeRecipientZeroAddress) {
    >>        feePerClaim = SafeCast.toUint96(_computeFeePerClaim(_tier, _countClaims(_winners, _prizeIndices), prizePool.claimCount()));
                if (feePerClaim < _minFeePerClaim) {
                    revert VrgdaClaimFeeBelowMin(_minFeePerClaim, feePerClaim);
                }
            }

            return feePerClaim * _claim(_vault, _tier, _winners, _prizeIndices, _feeRecipient, feePerClaim);
        }
    \u0060\u0060\u0060
- Notice that the function calls the internal function \u0060_computeFeePerClaim()\u0060 to compute the fee the claimer bot will receive based on the auction condition at this time. In \u0060_computeFeePerClaim()\u0060, another internal function \u0060_computeDecayConstant\u0060 is called to compute the decay constant for the \u0060Variable Rate Gradual Dutch Auction\u0060:
\u0060\u0060\u0060js
        function _computeFeePerClaim(uint8 _tier, uint256 _claimCount, uint256 _claimedCount) internal view returns (uint256) {
        //some code .. 
    >>    SD59x18 decayConstant = _computeDecayConstant(targetFee, numberOfTiers);
        // more code ...
        }
        function _computeDecayConstant(uint256 _targetFee, uint8 _numberOfTiers) internal view returns (SD59x18) {
    >>    uint256 maximumFee = prizePool.getTierPrizeSize(_numberOfTiers - 3); 
    >>    return LinearVRGDALib.getDecayConstant(LinearVRGDALib.getMaximumPriceDeltaScale(_targetFee, maximumFee, timeToReachMaxFee));
        }
\u0060\u0060\u0060 
- In \u0060_computeDecayConstant\u0060, the \u0060maximumFee\u0060 is obtained as the prize of the \u0060tier(_numberOfTiers - 3)\u0060, which is the last tier before canary tiers. This value is then fed into the \u0060LinearVRGDALib.getMaximumPriceDeltaScale()\u0060 function.
- The issue arises when the \u0060maximumFee\u0060 is zero, which can happen if there is no liquidity in this tier. With \u0060maximumFee = 0\u0060, the internal call to \u0060LinearVRGDALib.getMaximumPriceDeltaScale()\u0060 will revert specifically in \u0060wadLn\u0060 function when input is \u00600\u0060, causing the transaction to revert:
\u0060\u0060\u0060js
        function getMaximumPriceDeltaScale(uint256 _minFee, uint256 _maxFee, uint256 _time) internal pure returns (UD2x18) {
            return ud2x18(SafeCast.toUint64(uint256(wadExp(wadDiv(
                wadLn(wadDiv(SafeCast.toInt256(_maxFee), SafeCast.toInt256(_minFee))),//@audit : this will be zero 
                SafeCast.toInt256(_time)) / 1e18))));
        }

        function wadLn(int256 x) pure returns (int256 r) {
        unchecked {
    >>    require(x > 0, "UNDEFINED");
            // ... more code ..
        }
        }
\u0060\u0060\u0060
- This means that even if a winner wins, the claimer won\u0027t be able to claim the prize for them if \u0060tier(_numberOfTiers - 3).prize = 0\u0060, unless they set fees to 0. However, no claimer will do this since they would be paying gas for another user\u0027s prize. This will lead to winners not receiving their prizes even when they have won, and it prevents the honest claimer from performing its expected job due to external conditions.
- The winner in this case may win prizes from tiers less than \u0060_numberOfTiers - 3\u0060, which are rarer and higher prizes (they can\u0027t win prizes from tier \u0060(_numberOfTiers - 3)\u0060 since it has 0 liquidity).
- The \u0060tier(_numberOfTiers - 3).prize\u0060 can be 0 in different scenarios (less liquidity that round to zero when devid by prize count,high \u0060tierLiquidityUtilizationRate\u0060 ..ect). Here is a detailed example explain one of the scenarios that can lead to \u0060tier(_numberOfTiers - 3).prize= 0\u0060 :

- ***Example Scenario***
1. **Initial Setup**:
    - Assume we have 4 tiers \u0060[0, 1, 2, 3]\u0060.
    - Current draw is 5.
    - \u0060rewardPerToken = 2\u0060.

    2. **Awarding Draw 5**:
    - \u0060rewardPerToken\u0060 becomes 3.
    - Prizes are claimed, and all canary prizes are claimed due to a lot of liquidity contribution in draw 5.
    - Liquidity for each tier after draw 5:
        | Tier | Reward Per Token (rpt) |
        |------|------------------------|
        | t0   | 0                      |
        | t1   | 0                      |
        | t2   | 3                      |
        | t3   | 3                      |
    - Notice that the remaining liquidity in tiers 2 and 3 (canary tiers) is 0 now.

    3. **Awarding Draw 6**:
    - Time passes, and the next draw is 6.
    - Draw 6 is awarded, but there were no contributions.
    - Since the claim count was high in the previous draw, the number of tiers is incremented to 5.
    - Reclaim liquidity in both previous tiers 2 and 3, but there is no liquidity to reclaim.
    - There is no new liquidity to distribute, so the \u0060rewardPerToken\u0060 remains 3.
    - Liquidity for each tier in draw 6:
        | Tier | Reward Per Token (rpt) |
        |------|------------------------|
        | t0   | 0                      |
        | t1   | 0                      |
        | t2   | 3                      |
        | t3   | 3                      |
        | t4   | 3                      |

    4. **Claiming Prizes**:
    - A claimer computes the winners (consuming some resources) and calls \u0060claimPrizes\u0060 with the winners.
    - The \u0060uint256 maximumFee = prizePool.getTierPrizeSize(_numberOfTiers - 3);\u0060 (tier2) will be 0 since there was no liquidity .
    - This causes \u0060wadLn(0)\u0060 to revert when trying to compute the claimer fees thus tx revert and claimer can\u0027t claim any prize.
## Impact
  -  claimers cannot claim prizes for legitimate winners due to the transaction reverting.
  -  all Users who won the prizes in this awarded draw won\u0027t receive their prizes (unless they claim for them selfs with 0 fees which unlikely).
## Code Snippet
  - https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-claimer/src/Claimer.sol#L221
  - https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-claimer/src/Claimer.sol#L272-L279
  - https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-claimer/src/libraries/LinearVRGDALib.sol#L114
  - https://github.com/transmissions11/solmate/blob/c892309933b25c03d32b1b0d674df7ae292ba925/src/utils/SignedWadMath.sol#L165-L167
## Tool used
 Manual Review , Foundry Testing
## Recommendation
 - handle the situation where \u0060getTierPrizeSize(numberOfTiers - 3)\u0060 prize is \u00600\u0060, to make sure that the prize for winner still can be claimed by claimers. 




