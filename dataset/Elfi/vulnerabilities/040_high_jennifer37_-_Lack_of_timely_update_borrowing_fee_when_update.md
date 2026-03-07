# jennifer37 - Lack of timely update borrowing fee when update position\u0027s margin

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, borrowing fee, initial margin, leverage, isolated position, margin update, position size, traders, hackers, fee manipulation, risk assessment, financial impact, manual review, security recommendation, position leverage, fee accuracy, trading platform, exploit, system update

---

jennifer37

High

# Lack of timely update borrowing fee when update position\u0027s margin

## Summary
The borrow fee is related with initialMargin and leverage. When initialMargin/leverage changes, we need to update borrow fees.

## Vulnerability Detail
When traders want to update isolated position\u0027s margin, the keepers will execute \u0060executeUpdatePositionMarginRequest\u0060 to update positions\u0027 margin.
The operation will keep this isolated position\u0027s whole position size the same as before. It means that if the traders increase margin for one position, the position\u0027s leverage will be decreased.

\u0060\u0060\u0060javascript
    function _executeAddMargin(Position.Props storage position, AddPositionMarginCache memory cache) internal {
        //Cannot change position size, so cannot exceed the position size
       ......
        position.initialMargin += cache.addMarginAmount;
        if (cache.isCrossMargin) {
            // here leverage is updated leverage. Keep qty still
            position.initialMarginInUsd = CalUtils.divRate(position.qty, position.leverage);
            position.initialMarginInUsdFromBalance += cache.addInitialMarginFromBalance;
        } else {
            //Isolation mode, when add margin, the leverage will decrease.
            position.initialMarginInUsd += CalUtils.tokenToUsd(
                cache.addMarginAmount,
                cache.marginTokenDecimals,
                cache.marginTokenPrice
            );
            position.leverage = CalUtils.divRate(position.qty, position.initialMarginInUsd);
            position.initialMarginInUsdFromBalance = position.initialMarginInUsd;
        }
\u0060\u0060\u0060
The borrowing fee is related with initialMargin and position\u0027s leverage. So if we increase one position\u0027s margin, our borrow fee should decrease from now. Otherwise, our borrow fee should increase from now.
The vulnerability is that the traders\u0027 borrowing fee is not accurate. Hackers can make use of this vulnerability to pay less borrowing fee.
For example:
- Alice starts one isolated position with high leverage. The borrowing fees start to be accumulated from now.
- After a long time, when Alice wants to close her position, Alice can add margin to decrease her position\u0027s leverage.
- When Alice close her position. she will pay less borrow fees that she should because currently the leverage is quite low.

\u0060\u0060\u0060javascript
    function updateBorrowingFee(Position.Props storage position, address stakeToken) public {
        uint256 cumulativeBorrowingFeePerToken = MarketQueryProcess.getCumulativeBorrowingFeePerToken(
            stakeToken,
            position.isLong,
            position.marginToken
        );
        uint256 realizedBorrowingFeeDelta = CalUtils.mulSmallRate(
            CalUtils.mulRate(position.initialMargin, position.leverage - CalUtils.RATE_PRECISION),
            cumulativeBorrowingFeePerToken - position.positionFee.openBorrowingFeePerToken
        );
        ......
    }
\u0060\u0060\u0060

## Impact
Traders can pay less borrowing fees than they should.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/PositionMarginProcess.sol#L340-L368

## Tool used

Manual Review

## Recommendation
Timely update borrowing fees.
