# IssueH-1: Unsafe Type Casting in Token Amount Handling

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** unsafe casting, uint256, uint160, Permit2, overflow, underflow, fund loss, system manipulation, Smart Contract, Solidity, typecasting, order creation, malicious amount, token transfer, OpenZeppelin, SafeCast, contract vulnerability, protocol, attack path, modification

---

# IssueH-1: Unsafe Type Casting in Token Amount Handling

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-oku-judging/issues/64)  
Found by: bughuntoor, t.aksoy  

## Summary

Multiple contracts in the protocol perform unsafe downcasting from \u0060uint256\u0060 to \u0060uint160\u0060 when handling token amounts in Permit2 transfers. This can lead to silent overflow/underflow conditions, potentially allowing users to create orders with mismatched amounts, leading to fund loss or system manipulation.

## Root Cause

While Solidity 0.8.x provides built-in overflow/underflow protection for arithmetic operations, it does not protect against data loss during typecasting. The contracts perform direct casting of \u0060uint256\u0060 to \u0060uint160\u0060 without validation in several critical functions:

- \u0060Bracket.sol\u0060: \u0060procureTokens()\u0060, \u0060modifyOrder()\u0060
- \u0060StopLimit.sol\u0060: \u0060createOrder()\u0060, \u0060modifyOrder()\u0060
- \u0060OracleLess.sol\u0060: \u0060procureTokens()\u0060

As an example, the \u0060StopLimit::modifyOrder()\u0060 function takes \u0060uint256 amountIn\u0060 as input. This variable is cast to \u0060uint160\u0060 inside the \u0060handlePermit\u0060 function. Due to overflow, if the user sets the amount higher than the \u0060uint160\u0060 limit, the amount would become very small, and the contract would transfer this small amount. When setting orders, it uses \u0060amountIn\u0060 as \u0060uint256\u0060. As a result, the user creates an order with a high amount but pays very little to the protocol. The user can then drain the contract by modifying their order.

\u0060\u0060\u0060solidity
/// @notice see @IStopLimit
function createOrder(
  uint256 stopLimitPrice,
  uint256 takeProfit,
  uint256 stopPrice,
  uint256 amountIn,
  IERC20 tokenIn,
  IERC20 tokenOut,
  address recipient,
  uint16 feeBips,
  uint16 takeProfitSlippage,
  uint16 stopSlippage,
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint16 swapSlippage,
bool swapOnFill,
bool permit,
bytes calldata permitPayload
) external override nonReentrant {
    if (permit) {
        handlePermit(
            recipient,
            permitPayload,
            uint160(amountIn),
            address(tokenIn)
        );
    }
}

function handlePermit(
    address owner,
    bytes calldata permitPayload,
    uint160 amount,
    address token
) internal {
    Permit2Payload memory payload = abi.decode(
        permitPayload,
        (Permit2Payload)
    );
    permit2.permit(owner, payload.permitSingle, payload.signature);
    permit2.transferFrom(owner, address(this), amount, token);
}
\u0060\u0060\u0060

[Source Code](https://github.com/sherlock-audit/2024-11-oku/blob/ee3f781a73d65e33fb452c9a44eb1337c5cfdbd6/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L14)

## Internal Pre-conditions
No response

## External Pre-conditions
User must have enough tokens to create an order  
Amount must be greater than type(uint160).max  
User must be able to interact with the contract\u0027s order creation functions
## Attack Path
1. Attacker prepares: \u0060maliciousAmount=type(uint160).max+minPosSize;\u0060
2. Attacker creates an order with this amount.
3. Due to unsafe casting: The order is created with \u0060maliciousAmount\u0060 (full uint256) but only transfers \u0060minPosSize\u0060.
4. User can cancel or modify his order to drain the contract.

## Impact
Protocol receives fewer tokens than the order amount indicates and user can modify order to drain the protocol.

## PoC
No response.

## Mitigation
Implement OpenZeppelin\u0027s SafeCast library.

## Discussion
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/gfx-labs/oku-custom-order-types/pull/1](https://github.com/gfx-labs/oku-custom-order-types/pull/1)
