# Issue H-20: Donation fees are sandwich-able in one transaction

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** donation, fees, sandwich, transaction, liquidateProtectedListing, cancelListing, modifyListings, fillListings, Reserve, Relist, MEV, extraction, donateThresholdMax, block limit, Uniswap, liquidity, pool, listing, keeper reward, utilization rate

---

# Issue H-20: Donation fees are sandwich-able in one transaction

Source: [GitHub Issue #615](https://github.com/sherlock-audit/2024-08-flayer-judging/issues/615)  
Found by: 0x37, BugPull, Ironsidesec, ZeroTrust, araj, zzykxx


Doesn\u0027t matter if MEV is openly possible in the chain, whenever a user does actions like liquidateProtectedListing, cancelListing, modifyListings, fillListings, Reserve and Relist. They can sandwich the fees donation to make profit or recover the tax they paid. Or, the liquidation is open access, so you can sandwich that in the same transaction itself. 

Root cause: allowing more than max donation limit per transaction. Even if you don\u0027t allow to donate more than max, the user will just loop the donation and still extract the $, so it\u0027s better to have a max donation per block state that tracks this. So donateThresholdMax should be implemented in per block limit way.


Uniswap openly advises to design the donation mechanism to not allow MEV extraction. [Uniswap v4 Core](https://github.com/Uniswap/v4-core/blob/18b223cab19dc778d9d287a82d29fee3e99162b0/src/interfaces/IPoolManager.sol#L167-L172)

\u0060\u0060\u0060solidity
/// @notice Donate the given currency amounts to the in-range liquidity
/// providers of a pool
/// @dev Calls to donate can be frontrun adding just-in-time liquidity, with the
/// aim of receiving a portion donated funds.
/// Donors should keep this in mind when designing donation mechanisms.
/// @dev This function donates to in-range LPs at slot0.tick. In certain
/// edge-cases of the swap algorithm, the \u0060sqrtPrice\u0060 of
/// a pool can be at the lower boundary of tick \u0060n\u0060, but the \u0060slot0.tick\u0060 of the
/// pool is already \u0060n - 1\u0060. In this case a call to
/// \u0060donate\u0060 would donate to tick \u0060n - 1\u0060 (slot0.tick) not tick \u0060n\u0060
/// (getTickAtSqrtPrice(slot0.sqrtPriceX96)).
\u0060\u0060\u0060

Fees are donated to uniV4 pool in several listing actions:
- liquidateProtectedListing: Amount worth 1 ether - listing.tokenTaken - KEEPER_REWARD is donated. This amount will be huge in cases where, someone listed a...
protected listing and took 0.5 ether as token taken, but did not unlock the listing. So since utilization rate became high, the listing heath gone negative and was put to liquidation during this time an amount f (1 ether - 0.5 ether taker - 0.05 ether keeper reward) = 0.40 ether is donated to pool. That\u0027s a 1000$ direct donation.

- Other flows of Listings contract, such as cancelListing, modifyListings, fillListings, Reserve and Relist donate the tax fees to the pool. The likelihood is above medium to have huge amount when most users do multiple arrays of tokens of multiple collections done in one transaction.
