# ether_sky - In certain cases, users are unable to settle their orders with the PartialFill trade type.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Perpetual Protocol
**Keywords:** cybersecurity, vulnerability, PartialFill, trade type, order settlement, totalFilledAmount, positionSize, ReduceOnly, settlement issue, DoS, fund loss, gas fees, order creation, initial settlement, remaining order, verification function, settlement reversal, manual review, security recommendation, trading platform

---

ether_sky

medium

# In certain cases, users are unable to settle their orders with the PartialFill trade type.

## Summary
There are 2 \u0060trade\u0060 types available:  \u0060FoK\u0060 or \u0060PartialFill\u0060.
Users have the option to partially settle their \u0060orders\u0060.
However, in some cases, they can\u0027t settle their \u0060orders.
## Vulnerability Detail
A user creates an \u0060order\u0060 with the \u0060PartialFill\u0060 \u0060trade\u0060 type and a size of \u0060S\u0060.
Initially, he settles \u006050%\u0060 of this \u0060order\u0060.
At this point, the \u0060totalFilledAmount\u0060 of this \u0060order\u0060 has a value of \u0060S/2\u0060.
\u0060\u0060\u0060solidity
function _fillTakerOrder(
    InternalContext memory context,
    SettleOrderParam memory settleOrderParams
) internal returns (InternalWithdrawMarginParam memory, uint256) {
    _getOrderGatewayV2Storage().totalFilledAmount[takerOrder.getKey()] += settleOrderParams.fillAmount;
}
\u0060\u0060\u0060
After some time, the user attempts to settle the remaining \u006050%\u0060 of that \u0060order\u0060.
In the \u0060_verifyOrder\u0060 function, we check whether there is enough \u0060positionSize\u0060 available to settle this \u0060order\u0060 if the \u0060action\u0060 of the \u0060order\u0060 is \u0060ReduceOnly\u0060.
However, the issue arises from not accounting for the previously settled amount.
\u0060\u0060\u0060solidity
function _verifyOrder(IVault vault, Order memory order, uint256 fillAmount) internal view {
      uint256 totalFilledAmount = getOrderFilledAmount(order.owner, order.id);
      if (fillAmount > openAmount - totalFilledAmount) {
          revert LibError.ExceedOrderAmount(order.owner, order.id, totalFilledAmount);
      }
      if (order.action == ActionType.ReduceOnly) {
          int256 ownerPositionSize = vault.getPositionSize(order.marketId, order.owner);

          if (order.amount * ownerPositionSize > 0) {
              revert LibError.ReduceOnlySideMismatch(order.owner, order.id, order.amount, ownerPositionSize);
          }

          if (openAmount > ownerPositionSize.abs()) {  // @audit, here
              revert LibError.UnableToReduceOnly(order.owner, order.id, openAmount, ownerPositionSize.abs());  
          }
      }
}
\u0060\u0060\u0060
In the initial settlement, half of the \u0060order\u0060 was settled.
After the settlement, the \u0060positionSize\u0060 decreases by \u0060S/2\u0060 also and there are only \u0060S/2\u0060 remaining in the \u0060order\u0060.
Therefore, we should compare \u0060S/2\u0060 with the current \u0060positionSize\u0060.
However,  we compare \u0060S\u0060 again without accounting for the previously settled amount.
As a result, the current \u0060positionSize\u0060 might be lower than \u0060S\u0060, leading to the potential reversal of the settlement.
## Impact
This is a DoS and users can lose funds as gas fees.
## Code Snippet
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/orderGatewayV2/OrderGatewayV2.sol#L336
https://github.com/sherlock-audit/2024-02-perpetual/blob/main/perp-contract-v3/src/orderGatewayV2/OrderGatewayV2.sol#L513-L515
## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060solidity
function _verifyOrder(IVault vault, Order memory order, uint256 fillAmount) internal view {
      uint256 totalFilledAmount = getOrderFilledAmount(order.owner, order.id);
      if (fillAmount > openAmount - totalFilledAmount) {
          revert LibError.ExceedOrderAmount(order.owner, order.id, totalFilledAmount);
      }
      if (order.action == ActionType.ReduceOnly) {
          int256 ownerPositionSize = vault.getPositionSize(order.marketId, order.owner);

          if (order.amount * ownerPositionSize > 0) {
              revert LibError.ReduceOnlySideMismatch(order.owner, order.id, order.amount, ownerPositionSize);
          }

-          if (openAmount > ownerPositionSize.abs()) { 
+          if (openAmount - totalFilledAmount > ownerPositionSize.abs()) { 
              revert LibError.UnableToReduceOnly(order.owner, order.id, openAmount, ownerPositionSize.abs());  
          }
      }
}
\u0060\u0060\u0060
