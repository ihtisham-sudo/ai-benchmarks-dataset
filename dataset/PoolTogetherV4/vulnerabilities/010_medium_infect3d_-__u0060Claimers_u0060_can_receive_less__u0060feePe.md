# infect3d - \u0060Claimers\u0060 can receive less \u0060feePerClaim\u0060 than they should if some prizes are already claimed or if reverts because of a reverting hook

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, claimers, feePerClaim, prizes, VRGDA, algorithm, undervaluation, claim, reverting hook, prize pool, LinearVRGDALib, claimCount, prizeIndices, feeRecipient, manual review, impact, recommendation, wasClaimed, claimable prizes

---

infect3d

medium

# \u0060Claimers\u0060 can receive less \u0060feePerClaim\u0060 than they should if some prizes are already claimed or if reverts because of a reverting hook

## Summary

If a claimer propose an array of prizes to claim, but some of these prizes have already been claimed, or some claims revert, then the actual \u0060feePerClaim\u0060 received will be less **compared to what it should really be, as expected by the VRGDA algorithm**

This happens because \u0060_computeFeePerClaim\u0060 can undervaluate the value of \u0060feePerClaim\u0060, as it compute failed claims as successful ones.

This poses an issue, as \u0060feePerClaim\u0060 is then used as an input by \u0060_vault.claimPrize(_winners[w], _tier, _prizeIndices[w][p], _feePerClaim, _feeRecipient)\u0060, which will transfer the undervaluated fee to the claimer.


## Vulnerability Detail
Auctions for claiming prizes are based on the [VRGDA algorithm](https://www.paradigm.xyz/2022/08/vrgda)
In simple terms, this algorithm update price depending on either the numbers of claim is behind or ahead of time schedule.
In order to have a schedule, a target of claim per time unit is defined.
Just to give an idea, let\u0027s simplify that to the extreme (we will see complete formula afterward) and say : \u0060price(t) = claim/expected * targetPrice(t)\u0060 
E.g: if 10 claims per 2 hours are exepected, then at t=1h, 5 claims should be concluded.
If only 4 were claimed, then we can calculate that (4 claims)/(5 expected) < 1, price will be lower that target.
if 6 were claimed, then we will have (6 claims)/(5 expected) > 1, price will be greater than target.

The formula that has been implemented into \u0060LinearVRGDALib\u0060 is the following:

\u0060\u0060\u0060haskell
price = p0 * e^ (k * (t - n+1/r))   ; with k = ln(maxFee/minFee) * t_target
\u0060\u0060\u0060

With:
- \u0060n\u0060 the number of claim already completed
- \u0060r\u0060 the expected rate per hour
- \u0060k\u0060 the decay constant (speed at which price will change)
- \u0060p0\u0060 the target price (or fee in our case)

The more \u0060k *(t - n+1/r) > 0\u0060, the more \u0060price > p0\u0060
When \u0060t = n+1/r\u0060 <=> \u0060(k * (t - n+1/r)) = 0\u0060, then \u0060price = p0\u0060
The more \u0060k * (t - n+1/r) < 0\u0060, the more \u0060price < p0\u0060

We understand that the more whe are behind schedule in term of expected claim, the higher the fees earned by claimer will be.
And the more we are ahead of schedule, the lower the fee for claimers will be (as their is no urgency)

### Scenario
Now let\u0027s see what happens in this scenario:
1. For now, 0 prizes have already been claimed from the prize pool, \u0060n = 0\u0060
2. Alice has 5 prizes to claim, she build her claim array
3. It seems that 2 of the prizes Alice was going to claim are claimed right before, now \u0060n = 2\u0060
4. Alice tx is executed with the 5 prizes

Now let\u0027s see what happen from a code perspective.
The code above is the entry point for claiming prizes. As we can see L113, the \u0060feePerClaim\u0060 is computed based on the [number of claims to count](https://github.com/sherlock-audit/2024-05-pooltogether//blob/main/pt-v5-claimer/src/Claimer.sol#L126-L136) (\u0060_countClaims\u0060) and the number of [already claimed prizes](https://github.com/sherlock-audit/2024-05-pooltogether//blob/main/pt-v5-prize-pool/src/PrizePool.sol#L302-L302) (\u0060prizePool::claimCount()\u0060)
Then, the computed \u0060feePerClaim\u0060 value is given to \u0060_claim\u0060 which actually claim the prizes into the Prize Pool.

https://github.com/sherlock-audit/2024-05-pooltogether//blob/main/pt-v5-claimer/src/Claimer.sol#L113
\u0060\u0060\u0060solidity
File: pt-v5-claimer/src/Claimer.sol

090:   function claimPrizes(
091:     IClaimable _vault,
092:     uint8 _tier,
093:     address[] calldata _winners,
094:     uint32[][] calldata _prizeIndices,
095:     address _feeRecipient,
096:     uint256 _minFeePerClaim
097:   ) external returns (uint256 totalFees) {
...:
...:          /* some code */
...:
112:     if (!feeRecipientZeroAddress) {
113:       feePerClaim = SafeCast.toUint96(_computeFeePerClaim(_tier, _countClaims(_winners, _prizeIndices), prizePool.claimCount()));
114:       if (feePerClaim < _minFeePerClaim) {
115:         revert VrgdaClaimFeeBelowMin(_minFeePerClaim, feePerClaim);
116:       }
117:     }
118:
119:     return feePerClaim * _claim(_vault, _tier, _winners, _prizeIndices, _feeRecipient, feePerClaim); 
120:   }
\u0060\u0060\u0060

Now, let\u0027s see how \u0060_computeFeePerClaim\u0060 actually compute \u0060feePerClaim\u0060.
We see above L230-241 that a fee is calculated for each of the claims of the array, starting at \u0060_claimedCount\u0060 (The number of prizes already claimed) based on the VRGDA formula L309. The returned value (which is stored into \u0060feePerClaim\u0060) is the averaged fee as shown L241.
And as we explained earlier, the higher the number of claim we make, the lower the earned fee are. So, a higher value of \u0060_claimedCount + i\u0060 will give lower fees.

https://github.com/sherlock-audit/2024-05-pooltogether//blob/main/pt-v5-claimer/src/Claimer.sol#L236
\u0060\u0060\u0060solidity
File: pt-v5-claimer/src/Claimer.sol
205:   /// @param _claimCount The number of claims to check
206:   /// @param _claimedCount The number of prizes already claimed
207:   /// @return The total fees for the claims
208:   function _computeFeePerClaim(
209:     uint8 _tier,
210:     uint256 _claimCount,
211:     uint256 _claimedCount
212:   ) internal view returns (uint256) {
...:
...:        /* some code */
...:
227:     uint256 elapsed = block.timestamp - (prizePool.lastAwardedDrawAwardedAt());
228:     uint256 fee;
229: 
230:     for (uint256 i = 0; i < _claimCount; i++) {
231:       fee += _computeFeeForNextClaim(
232:         targetFee,
233:         decayConstant,
234:         perTimeUnit,
235:         elapsed,
236:         _claimedCount + i,         
237:         _maxFee
238:       );
239:     }
240: 
241:     return fee / _claimCount;
242:   }
...:
...:        /* some code */
...:
301:   function _computeFeeForNextClaim(
302:     uint256 _targetFee,
303:     SD59x18 _decayConstant,
304:     SD59x18 _perTimeUnit,
305:     uint256 _elapsed,
306:     uint256 _sold,
307:     uint256 _maxFee
308:   ) internal pure returns (uint256) {
309:     uint256 fee = LinearVRGDALib.getVRGDAPrice(
310:       _targetFee,
311:       _elapsed,
312:       _sold,
313:       _perTimeUnit,
314:       _decayConstant
315:     );
316:     return fee > _maxFee ? _maxFee : fee;
317:   }
318: 
\u0060\u0060\u0060

What we can see from this, is that the computation will be executed for \u0060_claimCount = 2\u0060 and up to \u0060i = 5\u0060, so as if there has been 7 claimed prizes, while in reality only 5 prizes are claimed, leading in an undervaluation of the fees to award.
As you probably have infered, the computation should have been made for \u0060i = 3\u0060 to be correct.

## Impact
The \u0060feePerClaim\u0060 computation is incorrect as the VRGDA is calculated for more claims that will really happen, leading to less fee earned by claimers at the time of the call.

## Code Snippet
https://github.com/sherlock-audit/2024-05-pooltogether//blob/main/pt-v5-claimer/src/Claimer.sol#L113
https://github.com/sherlock-audit/2024-05-pooltogether//blob/main/pt-v5-claimer/src/Claimer.sol#L236

## Tool used
Manual Review

## Recommendation
The \u0060PrizePool\u0060 contract expose a function to check if a prize has already been claimed: \u0060wasClaimed\u0060
This can be used to countClaims based on the actual true number of claimable prizes from the array.

This isn\u0027t a "perfect" solution though, as there are still issues when not already claimed prizes revert because of reverting prize hooks. In that case, VRGDA will still count the claim as happening, but we can consider this less likely to happen.

\u0060\u0060\u0060diff
  function _countClaims(
    address[] calldata _winners,
    uint32[][] calldata _prizeIndices
  ) internal pure returns (uint256) {
    uint256 claimCount;
    uint256 length = _winners.length;
    for (uint256 i = 0; i < length; i++) {
-     claimCount += _prizeIndices[i].length;
+	  numPrize = _prizeIndices[i].length;
+	  for(uint256 j = 0; j < numPrize; j++) {
+     	bool wasClaimed = wasClaimed(_vault, _winner, _drawId,_tier, _prizeIndex);
+     	if(!wasClaimed) {
+		 claimCount += 1;
+		}
+     }
    }
    return claimCount;
  }
\u0060\u0060\u0060
