# jennifer37 - Incorrect settleFee process for cross-margin account

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cyber security, vulnerability, settle fee, cross-margin account, traders, borrow fee, funding fee, close fee, settle fee processing, Pnl, subTokenWithLiability, addToken, negative settle fee, cache.recordPnlToken, cache.settledFee, cast failure, decrease order, manual review, impact, recommendation

---

jennifer37

Medium

# Incorrect settleFee process for cross-margin account

## Summary
Settle fee is processed twice when the closed/decreased position is cross-margin position.

## Vulnerability Detail
When the traders want to close or decrease their cross-margin positions, settle fees are generated. Settle fees include borrow fee, funding fee, and close fee.  When the settle fee is positive, the traders need to pay for the settle fee, otherwise, the traders will receive settle fees.
The vulnerability exists in function \u0060_settleCrossAccount\u0060. In this function, we will update the trader\u0027s cross-margin account via \u0060subTokenWithLiability\u0060 or \u0060addToken\u0060 at the first time. After that, if Pnl is larger than 0, settle fee will be process again, which is in wrong direction.

For example, if the settle fee is 10. The function will decrease this settle fees from cross-margin account via \u0060subTokenWithLiability\u0060, and then increase this settle fees to the cross-margin account via \u0060addToken\u0060. This means that the traders don\u0027t need to pay for the settle fee. Of course, the traders cannot gain the settle fee profit if the settle fee is negative.

What\u0027s more, considering that when \u0060cache.recordPnlToken\u0060 is positive and \u0060cache.settledFee\u0060 is negative, and the sum of \u0060cache.recordPnlToken\u0060 and \u0060cache.settledFee\u0060 is negative, this could cause reverted because \u0060(cache.recordPnlToken + cache.settledFee).toUint256()\u0060 cast failure.

\u0060\u0060\u0060javascript
    function _settleCrossAccount(
        uint256 requestId,
        Account.Props storage accountProps,
        Position.Props storage position,
        DecreasePositionCache memory cache
    ) internal returns (uint256 addLiability) {
@==> process settle fee at the first time
        if (cache.settledFee > 0) {
            accountProps.subTokenWithLiability(
                cache.position.marginToken,
                cache.settledFee.toUint256(),
                Account.UpdateSource.SETTLE_FEE
            );
        } else {
            //Add some settled fee in cross-margin account
            accountProps.addToken(
                cache.position.marginToken,
                (-cache.settledFee).toUint256(),
                Account.UpdateSource.SETTLE_FEE
            );
        }
        // decrease used_amount
        accountProps.unUseToken(
            cache.position.marginToken,
            cache.decreaseMargin,
            Account.UpdateSource.DECREASE_POSITION
        );
        address portfolioVault = IVault(address(this)).getPortfolioVaultAddress();
        // trader wins in cross-margin mode
        if (cache.recordPnlToken >= 0) {
       @==> process the settle fee again.
            accountProps.addToken(
                cache.position.marginToken,
                (cache.recordPnlToken + cache.settledFee).toUint256(),
                Account.UpdateSource.SETTLE_PNL
            );
\u0060\u0060\u0060
## Impact
- Settle fees are not processed correctly, traders may pay less fee than they should, may gain less fee than they deserve.
- Decrease order may be reverted when \u0060cache.recordPnlToken + cache.settledFee\u0060 is negative.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/DecreasePositionProcess.sol#L338-L368

## Tool used

Manual Review

## Recommendation
Don\u0027t process the settle fee twice.
