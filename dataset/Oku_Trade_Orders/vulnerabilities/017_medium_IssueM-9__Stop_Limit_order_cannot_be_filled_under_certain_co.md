# IssueM-9: Stop Limit order cannot be filled under certain condition

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** Stop Limit, order, filled, condition, minimum order size, checkMinOrderSize, USDC, price drop, transaction revert, Bracket order, performUpkeep, core functionality, automation, smart contract, decentralized finance, trading, order creation, liquidity, market conditions, error handling

---

# IssueM-9: Stop Limit order cannot be filled under certain condition

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-oku-judging/issues/449)  
Found by: xiaoming90  

## Summary
No response  

## Root Cause
No response  

## Internal pre-conditions
No response  

## External pre-conditions
No response  

## Attack Path
Assume that the MASTER.checkMinOrderSize is 100 USD. Assume that the current USDC price is 1.1 USD per USDC.  
Bob creates a Stop Limit order with \u0060order.tokenIn=USDC\u0060, \u0060order.amountIn=100e6\u0060 (100 USDC), and \u0060order.stopLimitPrice=100 USD\u0060. During the order creation, the MASTER.checkMinOrderSize function will be executed and the total USD value is 110 USD (100 USDC * 1.1 USD). Thus, the check will pass as it is over the minimum size of 100 USD.  

[AutomationMaster.sol](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/AutomationMaster.sol#L144)  
\u0060\u0060\u0060solidity
142:      ///@notice determine if a new order meets the minimum order size requirement
143:      ///Value of @param amountIn of @param tokenIn must meet the minimum USD value
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function checkMinOrderSize(IERC20 tokenIn, uint256 amountIn) external view
    override {
    uint256 currentPrice = oracles[tokenIn].currentValue();
    uint256 usdValue = (currentPrice * amountIn) /
        (10 ** ERC20(address(tokenIn)).decimals());

    require(usdValue > minOrderSize, "order too small");
}
\u0060\u0060\u0060

When the price of USDC drops from 1.1 to 0.9, Bob\u0027s Stop Limit order will be in range, and the performUpkeep function will be executed to fill the order. A new bracket order will be created in Line 126 below, as per the instructions of Bob\u0027s Stop Limit order, and the 100 USDC within the Stop Limit order will be transferred to the newly created Bracket order.  
[Link to Code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L126)

File: StopLimit.sol

\u0060\u0060\u0060solidity
function performUpkeep(
    bytes calldata performData
) external override nonReentrant {
    ..SNIP..
    //confirm order is in range to prevent improper fill
    (bool inRange, ) = checkInRange(order);
    require(inRange, "order ! in range");
    ..SNIP..
    
    //create bracket order
    BRACKET_CONTRACT.fillStopLimitOrder(
        swapPayload,
        order.takeProfit,
        order.stopPrice,
        order.amountIn,
        ..SNIP..
    );
}
\u0060\u0060\u0060

The Bracket.fillStopLimitOrder function will execute Bracket._createOrder function internally. However, the issue is that when the Bracket._createOrder function is executed to create a new Bracket order, it will perform a minimum order size check again at Line 473 below. Since the total value of 100 USDC is only worth 90 USD, which is below the minimum order size of 100 USD. Thus, the transaction will revert. As a result, Bob\u0027s Stop Limit cannot be filled due to the revert.  
[Link to Code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L473)

File: Bracket.sol

\u0060\u0060\u0060solidity
function _createOrder(
    uint256 takeProfit,
    ...
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 stopPrice,
uint256 amountIn,
uint96 existingOrderId,
IERC20 tokenIn,
IERC20 tokenOut,
address recipient,
uint16 feeBips,
uint16 takeProfitSlippage,
uint16 stopSlippage
) internal {
..SNIP..
MASTER.checkMinOrderSize(tokenIn, amountIn);
\u0060\u0060\u0060

**Impact**  
Medium. Loss of core functionality under certain conditions.

**PoC**  
No response

**Mitigation**  
Consider allowing the minimum order size check to be skipped if the order creation is initiated by the StopLimit contract when filling the StopLimit order. In this case, the Bracket order will be created without issues in the above described scenario.

**Discussion**  
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/gfx-labs/oku-custom-order-types/pull/1](https://github.com/gfx-labs/oku-custom-order-types/pull/1)
