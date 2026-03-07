# IllIllI - Withdrawal caps can be bypassed by opening positions against the SpotHedgeBaseMaker

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Perpetual Protocol
**Keywords:** cybersecurity, vulnerability, SpotHedgeBaseMaker, withdrawal caps, CircuitBreaker, base tokens, quote tokens, high water mark, collateral tokens, TVL, exploit, margin, short positions, flash loan, UniswapV3, accounting, deposit, withdraw, net outflow, sync interval

---

IllIllI

medium

# Withdrawal caps can be bypassed by opening positions against the SpotHedgeBaseMaker

## Summary

Deposits/withdrawals of base tokens to the SpotHedgeBaseMaker aren\u0027t accounted for in the CircuitBreaker\u0027s accounting, so the tokens can be used by attackers to increase the amount withdrawable past the high water mark percentage limits.


## Vulnerability Detail

The SpotHedgeBaseMaker allows LPs to deposit base tokens in exchange for shares. The CircuitBreaker doesn\u0027t include base tokens in its accounting, until they\u0027re converted to quote tokens and added to the vault, which happens when someone opens a short base position, and the SpotHedgeBaseMaker needs to hedge its corresponding long base position, by swapping base tokens for the quote token. The CircuitBreaker keeps track of net deposits/withdrawals of the quote token using a high water mark system, in which the high water mark isn\u0027t updated until the sync interval has passed. As long as the _net_ outflow between sync intervals doesn\u0027t pass the threshold, withdrawals are allowed.


## Impact

Assume there is some sort of exploit, where the attacker is able to artificially inflate their \u0027fund\u0027 amount (e.g. one of my other submissions), and are looking to withdraw their ill-gotten gains. Normally, the amount they\u0027d be able to withdraw would be limited to X% of the TVL of collateral tokens in the vault. By converting some of their \u0027fund\u0027 to margin, and opening huge short base positions against the SpotHedgeBaseMaker, they can cause the SpotHedgeBaseMaker to swap its contract balance of base tokens into collateral tokens, and deposit them into its vault account, increasing the TVL to TVL+Y. Since the time-based threshold will still be the old TVL, they\u0027re now able to withdraw \u0060TVL.old * X% + Y\u0060, rather than just \u0060TVL.old * X%\u0060. Depending on the price band limits set for swaps, the attacker can use a flash loan to temporarily skew the base/quote UniswapV3 exchange rate, such that the swap nets a much larger number of quote tokens than would normally be available to trade for. This means that if the \u0027fund\u0027 amount that the attacker has control over is larger than the actual number of collateral tokens in the vault, the attacker can potentially withdraw 100% of the TVL.


## Code Snippet

Quote tokens acquired via the swap are deposited into the [vault](https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/maker/SpotHedgeBaseMaker.sol#L571), which passes them through the [CircuitBreaker](https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/vault/Vault.sol#L339):
\u0060\u0060\u0060solidity
// File: src/maker/SpotHedgeBaseMaker.sol : SpotHedgeBaseMaker.fillOrder()   #1

415                } else {
416                    quoteTokenAcquired = _formatPerpToSpotQuoteDecimals(amount);
417 @>                 uint256 oppositeAmountXSpotDecimals = _uniswapV3ExactOutput(
418                        UniswapV3ExactOutputParams({
419                            tokenIn: address(_getSpotHedgeBaseMakerStorage().baseToken),
420                            tokenOut: address(_getSpotHedgeBaseMakerStorage().quoteToken),
421                            path: path,
422                            recipient: maker,
423                            amountOut: quoteTokenAcquired,
424                            amountInMaximum: _getSpotHedgeBaseMakerStorage().baseToken.balanceOf(maker)
425                        })
426                    );
427                    oppositeAmount = _formatSpotToPerpBaseDecimals(oppositeAmountXSpotDecimals);
428                    // Currently we don\u0027t utilize fillOrderCallback for B2Q swaps,
429                    // but we still populate the arguments anyways.
430                    fillOrderCallbackData.amountXSpotDecimals = quoteTokenAcquired;
431                    fillOrderCallbackData.oppositeAmountXSpotDecimals = oppositeAmountXSpotDecimals;
432                }
433    
434                // Deposit the acquired quote tokens to Vault.
435:@>             _deposit(vault, _marketId, quoteTokenAcquired);
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/maker/SpotHedgeBaseMaker.sol#L405-L442

The CircuitBreaker only tracks [net liqInPeriod changes](https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/circuitBreaker/LibLimiter.sol#L39-L49) changes during the withdrawal period, and only triggers the CircuitBreaker based on the TVL older than the withdrawal period:

\u0060\u0060\u0060solidity
// File: src/circuitBreaker/LibLimiter.sol : LibLimiter.status()   #2

119            int256 currentLiq = limiter.liqTotal;
...
126 @>         int256 futureLiq = currentLiq + limiter.liqInPeriod;
127            // NOTE: uint256 to int256 conversion here is safe
128            int256 minLiq = (currentLiq * int256(limiter.minLiqRetainedBps)) / int256(BPS_DENOMINATOR);
129    
130 @>         return futureLiq < minLiq ? LimitStatus.Triggered : LimitStatus.Ok;
131:       }
\u0060\u0060\u0060
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/circuitBreaker/LibLimiter.sol#L119-L131


## Tool used

Manual Review


## Recommendation

Calculate the quote-token value of each base token during LP \u0060deposit()\u0060/\u0060withdraw()\u0060, and add those amounts as CircuitBreaker flows during \u0060deposit()\u0060/\u0060withdraw()\u0060, then also invert those flows prior to depositing into/withdrawing from the vault
