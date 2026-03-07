# ctf_sec - Cancellation refunds should return tokens to order creator, not recipient

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Dinari
**Keywords:** cybersecurity, vulnerability, refund, order creator, recipient, payment token, dShares, L1/L2 bridges, cancelled deposits, transfer, middle-man, cancelOrderAccounting, incorrect address, user decision, irreversible loss, funds, inability to cancel, manual review, recommendation, Dinari implementation

---

ctf_sec

high

# Cancellation refunds should return tokens to order creator, not recipient

## Summary
When an order is cancelled, the refund is sent to \u0060order.recipient\u0060 instead of the order creator because it is the order creator (requestor) pay the payment token for buy order or pay the dShares for sell order

As is the standard in many L1/L2 bridges, cancelled deposits should be returned to the order creator instead of the recipient. In Dinari\u0027s current implementation, a refund acts as a transfer with a middle-man.

## Vulnerability Detail
Simply, the \u0060_cancelOrderAccounting()\u0060 function returns the refund to the \u0060order.recipient\u0060:

\u0060\u0060\u0060solidity
    function _cancelOrderAccounting(OrderRequest calldata orderRequest, bytes32 orderId, OrderState memory orderState)
        internal
        virtual
        override
    {
        ...

        uint256 refund = orderState.remainingOrder + feeState.remainingPercentageFees;

        ...

        if (refund + feeState.feesEarned == orderRequest.quantityIn) {
            _closeOrder(orderId, orderRequest.paymentToken, 0);
            // Refund full payment
            refund = orderRequest.quantityIn;
        } else {
            // Otherwise close order and transfer fees
            _closeOrder(orderId, orderRequest.paymentToken, feeState.feesEarned);
        }


        // Return escrow
        IERC20(orderRequest.paymentToken).safeTransfer(orderRequest.recipient, refund);
    }
\u0060\u0060\u0060

Refunds should be returned to the order creator in cases where the input recipient was an incorrect address or simply the user changed their mind prior to the order being filled.

## Impact
- Potential for irreversible loss of funds
- Inability to truly cancel order

## Code Snippet
https://github.com/sherlock-audit/2023-06-dinari/blob/4851cb7ebc86a7bc26b8d0d399a7dd7f9520f393/sbt-contracts/src/issuer/BuyOrderIssuer.sol#L193-L215

## Tool used
Manual Review

## Recommendation
Return the funds to the order creator, not the recipient.
