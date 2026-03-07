# mstpr-brainbot - Minting stake tokens is not updating the pool\u0027s borrowing fee rate

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, minting, stake tokens, liquidity, pool, borrowing fee rate, utilization, accrual, borrowing fees, liquidations, impact, manual review, code snippet, recommendation, financial protocol, decentralized finance, smart contracts, rate calculation, position holders

---

mstpr-brainbot

High

# Minting stake tokens is not updating the pool\u0027s borrowing fee rate

## Summary
When users mint new stake tokens, they provide liquidity to the pool, increasing the total amount and decreasing the borrowed utilization. However, this rate is not updated.
## Vulnerability Detail
When users mint stake tokens, they add liquidity to the pool and increase the total amount held in the pool:
\u0060\u0060\u0060solidity
function _mintStakeToken(Mint.Request memory mintRequest) internal returns (uint256 stakeAmount) {
        //..
        -> pool.addBaseToken(cache.mintTokenAmount);
        .
    }
\u0060\u0060\u0060

As we can see, the borrowing rate calculation will change accordingly. However, the rate is not updated:
\u0060\u0060\u0060solidity
function getLongBorrowingRatePerSecond(LpPool.Props storage pool) external view returns (uint256) {
        if (pool.baseTokenBalance.amount == 0 && pool.baseTokenBalance.unsettledAmount == 0) {
            return 0;
        }
        int256 totalAmount = pool.baseTokenBalance.amount.toInt256() + pool.baseTokenBalance.unsettledAmount;
        if (totalAmount <= 0) {
            return 0;
        }
        uint256 holdRate = CalUtils.divToPrecision(
            pool.baseTokenBalance.holdAmount,
            totalAmount.toUint256(),
            CalUtils.SMALL_RATE_PRECISION
        );
        return CalUtils.mulSmallRate(holdRate, AppPoolConfig.getLpPoolConfig(pool.stakeToken).baseInterestRate);
    }
\u0060\u0060\u0060
## Impact
Unfair accrual of borrowing fees. It can yield on lesser/higher fees for lps and position holders. It can also delay or cause unfair liquidations. Hence, high.
## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/MintProcess.sol#L45-L91

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/MintProcess.sol#L130-L213

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/MarketQueryProcess.sol#L82C5-L108
## Tool used

Manual Review

## Recommendation
Just like the opening orders update the rates after the pools base amounts changes. 
