# Issue H-7: stopLimitId collision with bracket orders due to no validation, opening up an attack to steal funds

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** vulnerability, orderId collision, double refund, StopLimit, Bracket, order corruption, MEV, attack vector, financial loss, block number, contract-specific entropy, automation, Ethereum, smart contract, mapping, nonce, refund, createOrder, cancelOrder, security

---

# Issue H-7: stopLimitId collision with bracket orders due to no validation, opening up an attack to steal funds

Source: [GitHub Issue #761](https://github.com/sherlock-audit/2024-11-oku-judging/issues/761)

Found by: 
056Security, 0rpse, 0x007, 0x0x0xw3, 0x37, 0x486776, 0xAadi, 0xNirix, 0xRiO, 0xaxaxa, 0xc0ffEE, 0xeix, 0xhuh2005, 0xmurki, 0xumarkhatab, 62616279727564696e, Afriaudit, Atharv, Bigsam, Boy2000, Breaker, BugPull, Cayde-6, ChinmayF, Contest-Squad, DenTonylifer, ElKu, ExtraCaterpillar, Falendar, IvanFitro, JinxSalamV2, John44, JohnTPark24, Kenn.eth, KungFuPanda, Kyosi, LonWof-Demon, LordAdhaar, Matin, NickAuditor2, NoOneWinner, NoWinner, PNS, PeterSR, PoeAudits, Praise03, Ragnarok, Tri-pathi, TxGuard, Weed0607, Xcrypt, Z3R0, ami, aslanbek, auditism, bughuntoor, chista0x, covey0x07, durov, elvin.a.block, future2_22, hals, iamandreiski, itcruiser00, joshuajee, krot-0025, lanrebayode77, lukris02, mladenov, mxteem, newspacexyz, nfmelendez, nikhil840096, onthehunt, oualidpro, phoenixv110, rudhra1749, safdie, silver_eth, t.aksoy, t0x1c, tedox, tmotfl, tobi0x18, tomadimitrie, vinica_boy, whitehair0330, xiaoming90, xseven, yovchev_yoan, zhenyazhd, zhigang, zhoo, zxriptor

## Summary
High-severity vulnerability in Oku\u0027s dual-contract architecture where parallel order creation between StopLimit.sol and Bracket.sol enables order data corruption and potential double-refund exploitation through orderId collisions.

## Root Cause
\u0060\u0060\u0060solidity
// Current implementation
function generateOrderId(address user) external returns (uint96) {
    return uint96(uint256(keccak256(abi.encodePacked(
        block.number,
        user
    ))));
}
\u0060\u0060\u0060
Deterministic orderId generation lacks contract-specific entropy, allowing cross-contract collisions within the same block.
## Internal Pre-conditions
1. Shared Automation Master instance between contracts
2. Mutable orders mapping in Bracket contract
3. Independent order creation flows

\u0060\u0060\u0060solidity
mapping(uint96 => Order) public orders;
\u0060\u0060\u0060

## External Pre-conditions
1. MEV capabilities (same-block execution)
2. Sufficient token balance for multiple orders
3. Active protocol state

## Attack Path
\u0060\u0060\u0060
// Block N
// Step 1: Create Bracket order (5000 USDT)
bracket.createOrder({
   amountIn: 5000e6,
   recipient: attacker
});
// OrderId = hash(blockN + attacker)
// Same Block N
// Step 2: Create StopLimit order (10000 USDT)
stopLimit.createOrder({
   amountIn: 10000e6,
   recipient: attacker
});
// Internally calls bracket.fillStopLimitOrder
// Same OrderId = hash(blockN + attacker)
// Step 3: Cancel order twice
bracket.cancelOrder(orderId); // Refunds 10000 USDT
bracket.cancelOrder(orderId); // Refunds 10000 USDT again
\u0060\u0060\u0060

## Impact
- Double-spend vulnerability
- Order state corruption
- Accounting system compromise
## Direct financial loss

## Mitigation
\u0060\u0060\u0060solidity
contract AutomationMaster {
   // Add contract-specific entropy
   function generateOrderId(
     address user,
     address contractSource
   ) external returns (uint96) {
     return uint96(uint256(keccak256(abi.encodePacked(
        block.number,
        user,
        contractSource,
        _orderNonce++ // Additional entropy
     ))));
   }
   uint256 private _orderNonce;
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Update in Bracket.sol
function createOrder(...) external {
   uint96 orderId = MASTER.generateOrderId(msg.sender, address(this));
   // Rest of the function
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Update in StopLimit.sol
function createOrder(...) external {
   uint96 orderId = MASTER.generateOrderId(msg.sender, address(this));
   // Rest of the function
}
\u0060\u0060\u0060

## Discussion
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/gfx-labs/oku-custom-order-types/pull/1
