# 82 - Adversary can rug LPs and DOS other users

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Buffer Finance
**Keywords:** adversary, rug pull, liquidity providers, DOS, options, slippage, price manipulation, asset, queue, pools, strike price, collateral, withdraw, capital, expiry, ITM, OTM, liquidity, public, race

---

# Examples

Imagine two assets are listed that have close prices, asset A = $0.95 and asset B = $1. An adversary could create a call that expires in 10 minutes on asset B with 5% slippage, then immediately queue it with the price of asset A. $0.95 is within the slippage bounds so it creates the option with a strike price of $0.95. Since the price of asset B is actually $1, the adversary will almost guaranteed make money, stealing funds from the LPs. This can be done back and forth between both pools until pools for both assets are drained.

In a similar scenario, if the price of the assets are very different, the adversary could use this to DOS another user by always calling queue with the wrong asset, causing the order to be cancelled.

Adversary can rug LPs and DOS other users.

## CodeSnippet

[BufferRouter.sol](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferRouter.sol#L136-L185)

Manual Review
Pass the asset address through so the BufferBinaryOptions contract can validate it is being called with the correct asset.

Fixed in PR#2. Changes look good. The asset pair is now stored in BufferBinaryOptions and BufferRouter directly reads it from there instead of relying on user/keeper to supply the correct asset.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-buffer-judging/issues/82)  
**Found by:** __141345__, 0x52  

When an option is created, enough collateral is locked in BufferBinaryPool to cover a payout should it close ITM. As long as an LP isn\u0027t locked (trivially 10 minutes) and there is sufficient liquidity they can cash out their shares for underlying. The price and expiration of all options are public by design, meaning an LP can know with varying degrees of certainty if they will make or lose money from an option expiry. The result is that there will be a race to withdraw capital before any option expires ITM. LPs who make it out first won\u0027t lose any money, leaving all other LPs to hold the bags. On the flip-side of this when there are large options expiring OTM, LPs will rush to stake their capital in the pool. This allows them to claim the payout while experiencing virtually zero risk, since they can immediately withdraw after 10 minutes.

See summary.

LPs can game option expiry at the expense of other LPs.

[BufferBinaryPool.sol](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferBinaryPool.sol#L124-L126)

Manual Review
I strongly recommend an epoch based withdraw and deposit buffer to prevent a situation like this. Alternatively increasing lockupPeriod would be a quicker, less precise fix.

**bufferfinance**  
Yes we were planning to adjust the lockup accordingly.  

**bufferfinance**  
Doesn\u0027t need to be fixed. The admin will adjust the config accordingly.  

**0x00052**  
Fixed in PR#9  
lockupPeriod is now set in constructor so that it is adjustable.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-buffer-judging/issues/130)  
**Found by:** HonorLt, bin2chen, KingNFT  

_openQueuedTrade() does not follow the “Checks Effects Interactions” principle and may lead to re-entry to steal the funds.  
[Checks Effects Interactions Pattern](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)  

The prerequisite is that tokenX is ERC777 e.g. “sushi”  
1. resolveQueuedTrades() calls _openQueuedTrade()  
2. in _openQueuedTrade() calls \u0060tokenX.transfer(queuedTrade.user)\u0060 if \u0060(revisedFee < queuedTrade.totalFee)\u0060 before setting \u0060queuedTrade.isQueued = false;\u0060

   \u0060\u0060\u0060solidity
   function _openQueuedTrade(uint256 queueId, uint256 price) internal {
       ...
       if (revisedFee < queuedTrade.totalFee) {
           tokenX.transfer( //***@audit call transfer , if ERC777 , can re-enter
               queuedTrade.user,
               queuedTrade.totalFee - revisedFee
           );
       }
       queuedTrade.isQueued = false; //****@audit change state****/
   }
   \u0060\u0060\u0060

3. If ERC777 re-enters to \u0060#cancelQueuedTrade()\u0060 to get tokenX back, it can close, because \u0060queuedTrade.isQueued\u0060 is still equal to true.  
4. Back to _openQueuedTrade() sets \u0060queuedTrade.isQueued = false\u0060  
5. So steal tokenX  

If tokenX equals ERC777, can steal token.
