# Issue H-4: Base calculation in Leverager

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Yieldoor
**Keywords:** liquidation, leverage, calculation, risk, bad debt, protocol, collateral, max leverage, lending pool, owed amount, total denomination, position leverage, function, check, error, solidity, smart contract, audit, vulnerability, design choice

---

# Issue H-4: Base calculation in Leverager

### Description
The \u0060isLiquidateable()\u0060 function is incorrect as the max leverage may be smaller.

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/158)  
**Found by:** 0x73696d616f, future2_22, iamnmt

### Summary
The base calculation in \u0060Leverager::isLiquidateable()\u0060 is: 
\u0060\u0060\u0060solidity
uint256 base = owedAmount * 1e18 / (vp.maxTimesLeverage - 1e18);
\u0060\u0060\u0060
However, the max leverage may not actually be \u0060vp.maxTimesLeverage\u0060, but be \u0060maxLevTimes\u0060 from the lending pool. In this case, the base amount would be incorrectly underestimated, leading to users not being liquidated when they should for the protocol\u0027s loss (loss of profit and higher bad debt risk).

### Root Cause
In \u0060Leverager:408\u0060, the max leverage from the lending pool is not taken into account.

\u0060maxLevTimes\u0060 from the lending pool < \u0060vp.maxTimesLeverage\u0060.

None.

1. User has a position that should be liquidated but isn\u0027t due to the rhs of the \u0060isLiquidatable\u0060 check.

Protocols take losses and risk bad debt creation.
If maxLevTimes < vp.maxTimesLeverage, it means the base calculation would have in the divisor a bigger number than it should, so base will be smaller. As base is smaller, the collateral of the user can decrease more without the user being liquidated.

Compare the 2 max leverage values and use the smallest, which is the actual maximum leverage allowed in the Leverager.

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [GitHub Commit](https://github.com/spa cegliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858)
**Source:** [GitHub Issue #357](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/357)  
**Found by:** 000000, 0x73696d616f, 0xaxaxa, 0xmystery, AlexCzm, AuditorPraise, BugsBunny, Fade, JohnTPark24, KrisRenZo, Ryonen, TessKimy, Valy001, charles__cheerful, elvin.a.block, future2_22, iamnmt, jennifer37, montecristo, mstpr-brainbot, newspacexyz, novaman33, stuart_the_minion, whitehair0330  

Market can allow leverage higher than 2x, and this is a design choice. But the check owed Amount > totalDenominisLiquidateable function doesn\u0027t allow leverage higher than 2x.  

positionLeverage is calculated and checked in _checkWithinlimits function when open leverage.
\u0060\u0060\u0060solidity
function _checkWithinlimits(Position memory up) internal {
    ...
    uint256 positionLeverage = (up.initCollateralValue + up.borrowedAmount) *
        1e18 / up.initCollateralValue;
    require(positionLeverage <= vp.maxTimesLeverage && positionLeverage <=
        maxLevTimes, "too high x leverage");
    ...
}
\u0060\u0060\u0060
Opening leverage also checks whether the position is liquidateable. isLiquidateable checks if owedAmount > totalDenom and returns true (indicating liquidation).
\u0060\u0060\u0060solidity
function isLiquidateable(uint256 _id) public view returns (bool liquidateable) {
    ...
    uint256 totalValueUSD = _calculateTokenValues(pos.token0, pos.token1,
        userBal0, userBal1, price);
    uint256 bPrice = IPriceFeed(pricefeed).getPrice(pos.denomination);
    uint256 totalDenom = totalValueUSD * (10 **
        ERC20(pos.denomination).decimals()) / bPrice;
    uint256 bIndex =
        ILendingPool(lendingPool).getCurrentBorrowingIndex(pos.denomination);
\u0060\u0060\u0060
## Vulnerability Description

\u0060\u0060\u0060solidity
uint256 owedAmount = pos.borrowedAmount * bIndex / pos.borrowedIndex;
/// here we make a calculation what would be the necessary collateral
/// if we had the same borrowed amount, but at max leverage. Check docs for
// better explanation why.
uint256 base = owedAmount * 1e18 / (vp.maxTimesLeverage - 1e18);
base = base < pos.initCollateralValue ? base : pos.initCollateralValue;
if (owedAmount > totalDenom || totalDenom - owedAmount <
    vp.minCollateralPct * base / 1e18) return true;
else return false;
\u0060\u0060\u0060

When open leverage, owedAmount is equal to borrowedAmount and totalDenom is equal to initCollateralValue. To be not liquidatable, owedAmount <= totalDenom should be satisfied, and this means that positionLeverage is always smaller than 2x. Root cause is contradiction between high-leverage and liquidation check of position. This means that the define of positionLeverage could be incorrect or liquidation check could be incorrect.

No response

No response

No response

Market doesn\u0027t allow leverage higher than 2x

No response

Update the positionLeverage check logic or isLiquidateable function logic.
