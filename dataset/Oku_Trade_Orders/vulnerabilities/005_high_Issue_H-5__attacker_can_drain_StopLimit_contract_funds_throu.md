# Issue H-5: attacker can drain StopLimit contract funds through Bracket contract because it gives type(uint256).max allowance to bracket contract for input token in performUpkeep function

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Oku Trade Orders
**Keywords:** StopLimit, Bracket, allowance, attack, drain, funds, performUpkeep, type(uint256).max, IERC20, transferFrom, safeIncreaseAllowance, execute, swapPayload, order, recipient, feeBips, slippage, contract, tokens, vulnerability

---

# Issue H-5: attacker can drain StopLimit contract funds through Bracket contract because it gives type(uint256).max allowance to bracket contract for input token in performUpkeep function

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-11-oku-judging/issues/700)  
Found by: 0xaxaxa, Contest-Squad, rudhra1749, whitehair0330, xiaoming90

## Summary
performUpkeep::StopLimit function increases allowance of input token for Bracket contract to type(uint256).max. [Link to Code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L100-L104)

\u0060\u0060\u0060solidity
updateApproval(
    address(BRACKET_CONTRACT),
    order.tokenIn,
    order.amountIn
);
\u0060\u0060\u0060

[Link to Code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L397-L411)

\u0060\u0060\u0060solidity
function updateApproval(
    address spender,
    IERC20 token,
    uint256 amount
) internal {
    // get current allowance
    uint256 currentAllowance = token.allowance(address(this), spender);
    if (currentAllowance < amount) {
        // amount is a delta, so need to pass max - current to avoid overflow
        token.safeIncreaseAllowance(
            spender,
            type(uint256).max - currentAllowance
        );
    }
}
\u0060\u0060\u0060
sonowBracketcontractcantransferinputtokenstoitselfinfillStopLimitOrderfunction.  
[Link to StopLimit.sol](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L126-L140)

\u0060\u0060\u0060solidity
BRACKET_CONTRACT.fillStopLimitOrder(
    swapPayload,
    order.takeProfit,
    order.stopPrice,
    order.amountIn,
    order.orderId,
    tokenIn,
    tokenOut,
    order.recipient,
    order.feeBips,
    order.takeProfitSlippage,
    order.stopSlippage,
    false, //permit
    "0x" //permitPayload
);
\u0060\u0060\u0060

[Link to Bracket.sol](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L147-L165)

\u0060\u0060\u0060solidity
function fillStopLimitOrder(
    bytes calldata swapPayload,
    uint256 takeProfit,
    uint256 stopPrice,
    uint256 amountIn,
    uint96 existingOrderId,
    IERC20 tokenIn,
    IERC20 tokenOut,
    address recipient,
    uint16 existingFeeBips,
    uint16 takeProfitSlippage,
    uint16 stopSlippage,
    bool permit,
    bytes calldata permitPayload
) external override nonReentrant {
    require(
       msg.sender == address(MASTER.STOP_LIMIT_CONTRACT()),
       "Only Stop Limit"
    );
}
\u0060\u0060\u0060

[Link to Bracket.sol](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L336)
token.safeTransferFrom(owner, address(this), amount);
now even after this transfer almost type(uint256).max allowance is there for Bracket contract. Attacker can take this as advantage and drain StopLimit contract funds.

1) Attacker checks for which tokens there is almost type(uint256).max allowance for Bracket contract to transfer tokens of StopLimit contract. (let\u0027s say for tokens A, B, C, D etc...)

2) Attacker creates a readily executable order in Bracket contract such that let\u0027s say tokenOut = tokenA (for which Bracket contract already has almost type(uint256).max allowance to transfer StopLimit contract\u0027s token A tokens).

3) Then attacker calls performUpkeep::Bracket with respect to this order (with target = address of tokenA, txData is such that in calls transferFrom with from = address of StopLimit contract, to = address of Bracket contract, value = no of tokenA tokens StopLimit contract have (or something closer to it)).

[Link to Code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L85-L101)

\u0060\u0060\u0060solidity
function performUpkeep(
  bytes calldata performData
) external override nonReentrant {
  MasterUpkeepData memory data = abi.decode(
     performData,
     (MasterUpkeepData)
  );
  Order memory order = orders[pendingOrderIds[data.pendingOrderIdx]];
  require(
     order.orderId == pendingOrderIds[data.pendingOrderIdx],
     "Order Fill Mismatch"
  );
  // deduce if we are filling stop or take profit
  (bool inRange, bool takeProfit, ) = checkInRange(order);
  require(inRange, "order ! in range");
}
\u0060\u0060\u0060

and he sets feeBips = 0.

4) performUpkeep function internally calls execute function.

[Link to Code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L108-L115)

\u0060\u0060\u0060solidity
(uint256 swapAmountOut, uint256 tokenInRefund) = execute(
  data.target,
  data.txData,
  order.amountIn,
  order.tokenIn,
);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
order.tokenOut,
bips
);
nowLetsobserveexecutefunction,https://github.com/sherlock-audit/2024-11-oku/blo
b/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L526-L568
function execute(
    address target,
    bytes memory txData,
    uint256 amountIn,
    IERC20 tokenIn,
    IERC20 tokenOut,
    uint16 bips
) internal returns (uint256 swapAmountOut, uint256 tokenInRefund) {
    //update accounting
    uint256 initialTokenIn = tokenIn.balanceOf(address(this));
    uint256 initialTokenOut = tokenOut.balanceOf(address(this));
    //approve
    tokenIn.safeApprove(target, amountIn);
    //perform the call
    (bool success, bytes memory result) = target.call(txData);
    if (success) {
        uint256 finalTokenIn = tokenIn.balanceOf(address(this));
        require(finalTokenIn >= initialTokenIn - amountIn, "over spend");
        uint256 finalTokenOut = tokenOut.balanceOf(address(this));
        //if success, we expect tokenIn balance to decrease by amountIn
        //and tokenOut balance to increase by at least minAmountReceived
        require(
            finalTokenOut - initialTokenOut >
                MASTER.getMinAmountReceived(
                    amountIn,
                    tokenIn,
                    tokenOut,
                    bips
                ),
            "Too Little Received"
        );
        swapAmountOut = finalTokenOut - initialTokenOut;
\u0060\u0060\u0060
tokenInRefund = amountIn - (initialTokenIn - finalTokenIn);
} else {
   //force revert
   revert TransactionFailed(result);
}
In executefunctionaftertheexternalcalltotarget(tokenA),tokenOutbalanceof
contractincreasesbyamountusedasvalueincall(whichisalmostequaltoavailable
balanceofStopLimitcontractfortokenA).sofinalTokenOut-initialTokenOut=value.so
followingrequirecheckispassed.
require(
  finalTokenOut - initialTokenOut >
     MASTER.getMinAmountReceived(
       amountIn,
       tokenIn,
       tokenOut,
       bips
     ),
  "Too Little Received"
);
andalso
require(finalTokenIn >= initialTokenIn - amountIn, "over spend");
this check passesaswearenottransferinganyTokenIntokens. sonow
swapAmountOut = finalTokenOut - initialTokenOut;
swapAmountOut=value.(valueusedinexternalcalltotokenA).nowthis
swapAmountOutwillbetransferredtorecipientaddress(setbyattacker).
https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L135
order.tokenOut.safeTransfer(order.recipient, adjustedAmount);
hereadjustedAmount=swapAmountOut=value.(aswesetfeeBips=0).
https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/Bracket.sol#L125-L128
(uint256 feeAmount, uint256 adjustedAmount) = applyFee(
  swapAmountOut,
  order.feeBips
);
sofinally throughthisprocessAttackercandrainallfundsofStopLimitcontractthrough
Creating orders in Bracket contract by setting tokenOut as tokens for which Bracket contract have allowance to transfer from StopLimit contract, and setting takeProfit and stopPrice such that order was readily executable. And setting target as the set tokenOut tokens and txData such that it calls transferFrom function with from = address of StopLimit contract, to = address of Bracket contract, value = available balance for StopLimit contract of tokenOut tokens respectively.

## Root Cause
Increasing allowance of Bracket contract to type(uint256).max for transferring tokens of StopLimit contract. [Source Code](https://github.com/sherlock-audit/2024-11-oku/blob/main/oku-custom-order-types/contracts/automatedTrigger/StopLimit.sol#L397-L411)

\u0060\u0060\u0060solidity
function updateApproval(
   address spender,
   IERC20 token,
   uint256 amount
) internal {
   // get current allowance
   uint256 currentAllowance = token.allowance(address(this), spender);
   if (currentAllowance < amount) {
     // amount is a delta, so need to pass max - current to avoid overflow
     token.safeIncreaseAllowance(
        spender,
        type(uint256).max - currentAllowance
     );
   }
}
\u0060\u0060\u0060

## Internal pre-conditions
No response

## External pre-conditions
No response

## Attack Path
1) Attacker creates a readily executable order in Bracket contract such that tokenOut = token for which StopLimit contract already set allowance of Bracket contract to type(uint256).max to transfer tokenOut tokens.  
2) Attacker then calls performUpkeep function with respect to this orderId by setting target = address of tokenOut and txData such that it calls transferFrom function.
with from=addressofStopLimitcontract and to=addressofBracketcontract and  
value=availablebalanceoftokenOuttokensforStopLimitcontract.  

## Impact  
AttackercandrainStopLimitcontractfunds.(almostcompletely)  

## PoC  
Noresponse  

## Mitigation  
StopLimitcontractshouldincreaseallowanceofBracketcontracttotransfertokensonly  
whicharerequiredinfillStopLimitorderfunction(nottotype(uint256).max).  

## Discussion  
sherlock-admin2  
TheprotocolteamfixedthisissueinthefollowingPRs/commits:  
[https://github.com/gfx-labs/oku-custom-order-types/pull/1](https://github.com/gfx-labs/oku-custom-order-types/pull/1)
