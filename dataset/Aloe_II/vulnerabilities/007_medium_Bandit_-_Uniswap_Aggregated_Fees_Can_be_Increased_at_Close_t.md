# Bandit - Uniswap Aggregated Fees Can be Increased at Close to Zero Cost

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Aloe II
**Keywords:** Uniswap, cybersecurity, vulnerability, aggregated fees, IV manipulation, liquidity pool, wash trading, LTV reduction, flashbots, trading fees, impermanent loss, tickSpacing, liquidity providers, profit incentive, CLOB, dYdX, IDEX, fee externalization, market manipulation, Uniswap v3

---

Bandit

high

# Uniswap Aggregated Fees Can be Increased at Close to Zero Cost
## Summary

The recorded fee collection in a Uniswap pool can be manipulated in the method described below while paying very little in "real" fees. This means that \u0060IV\u0060 can be pushed upwards to unfairly liquidate pre-existing borrowers.

## Vulnerability Detail

In a sufficiently liquid pool and high trading volume, the potential attack profits you may get from swapping a large amount of tokens back and forth is likely lower than the profit an attacker can make from manipulating IV. This is especially true due to the \u0060IV_CHANGE_PER_UPDATE\u0060 which limits of the amount that IV can be manipulated per update.

However, its possible to boost the recorded trading fees via trading fees while paying a very small cost relative to the fee increase amount.

The attack rests on 2 facts:

1. Aside from pools where the 2 pool assets are pegged to the same value, only a tiny portion of the total liquidity is in the "in-range" \u0060tickSpacing\u0060. 
2. In Uniswap, 100% of fees goes to the liquidity providers, in proportion to liquidity at the active tick, or ticks that gets passed through. This is different from other exchanges, where some portion of fees is distrubted to token holders, or the exchange operator.

Due to (1), a user with a large amount of capital can deposit all of it in the active tick and have >99% of the liquidity in the active tick. Due to (2), this also means that if they wash trade while keeping the price within that tick, they get >99% of the trading fees captured by their LP position. If $200K is deposited into that tick, then up to $200k can be traded, if the pool price starts exactly at the lower tick and ends at the upper tick, or vice versa. 

The wash trading can performed in one flashbots bundle, and since the trades are basically against the oneself, the trading profits-and-loss and impermanant gain/loss approximately cancel out.

Manipulating fees higher drives the \u0060IV\u0060 higher, which in turn reduces the \u0060LTV\u0060. Let\u0027s say a position is not liquidatable yet, but a reduction in LTV will make that position liquidatable. There is profit incentive for an attacker to use the wash trading manipulation to decrease the LTV and then liquidate that position.

Note that this efficiency in wash trading to inflate fees is only possible in Uniswap v3. In v2 style pools, liquidity cannot be concentrated and it is impractical to deposit enough liquidity to capture the overwhelming majority of an entire pool. Most CLOB such as dYdX, IDEX etc have some fees that go to the protocol or token stakers (Uniswap 100% of "taker" fees go to LP\u0027s or "makers"), which means that even though a maker and taker order can be matched by wash traders, there is still significant fee externalisation to the protocol.

## Impact

- \u0060IV\u0060 is cheaply and easily manipulated upwards, and thus \u0060LTV\u0060 can be decreased, which can unfairly liquidate users

## Code Snippet

https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/libraries/Volatility.sol#L44-L81

## Tool used

Manual Review

## Recommendation

Using the MEDIAN fee of many short price intervals to calculate the Uniswap fees makes it more difficult to manipulate. The median, unlike mean (which is also implicitly used in the context a TWAP), is unaffected by large manipulations in a single block.




