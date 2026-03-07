# [C-01] Using Uniswap spot price is subject to manipulation

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---

**Severity**

**Impact:** High

**Likelihood:** High

**Description**

The protocol uses the Uniswap V3 quoter contract to get the current value of the supported tokens in terms of the base token (USDC). The values returned by the quoter are the result of a simulated swap, given the current state of the pools. This means that these values can be easily manipulated, for example, by using a flash loan to add liquidity and remove it after interacting with the protocol.

The quote of tokens is used in the most critical parts of the protocol, such as withdrawal, borrowing, repayment, and liquidation. This means that an attacker could manipulate current the price of a token in their favor and cause losses to other users.

Additionally, in some transactions, there are multiple swaps involved. This means that the result of a swap can cause a change in the pool that will affect the next swap, and this is not taken into account in the quote process.

**Proof of concept**

```solidity
function test_priceManipulation() public {
    provideInitialLiquidity();

    vm.startPrank(alice);
    // Provide 1 WETH = 4_000 USDC
    marginTrading.provideERC20(marginAccountID[alice], address(WETH), 1e18);

    // Simulate price manipulation (2x WETH price in USDC)
    quoter.setSwapPrice(address(WETH), address(USDC), 8_000e6);

    // Borrow 7_000 USDC
    marginTrading.borrow(marginAccountID[alice], address(USDC), 7_000e6);

    // Withdraw 7_000 USDC
    marginTrading.withdrawERC20(marginAccountID[alice], address(USDC), 7_000e6);
    vm.stopPrank();

    // Simulate price manipulation recovery
    quoter.setSwapPrice(address(WETH), address(USDC), 4_000e6);

    // Alice got 3_000 USDC profit and left her position with bad debt
    uint256 accountRatio = marginTrading.getMarginAccountRatio(marginAccountID[alice]);
    assert(accountRatio < 0.6e5);
}
```

**Recommendations**

Use Chainlink oracles to get the price of the assets.
