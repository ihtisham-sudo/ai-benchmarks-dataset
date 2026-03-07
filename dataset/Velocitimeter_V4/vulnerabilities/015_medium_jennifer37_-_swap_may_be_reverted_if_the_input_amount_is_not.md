# jennifer37 - swap may be reverted if the input amount is not large enough, especially for low decimal tokens

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cyber security, vulnerability, swap transaction, input amount, low decimal tokens, swap fees, externalBribe, notifyRewardAmount, reverted, pool contract, amount0In, amount1In, decimal precision, stable coin, GUSD, swap fee ratio, FeesToBribes, manual review, impact, recommendation

---

jennifer37

Medium

# swap may be reverted if the input amount is not large enough, especially for low decimal tokens

## Summary
The swap fees will be sent to the \u0060externalBribe\u0060.  If the calculated swap fee is round down to zero, possible in low decimal tokens, the swap transaction will be reverted because \u0060externalBribe\u0060 does not accept 0 fee.

## Vulnerability Detail
In swap(), the swap fees will be calculated based on the token\u0027s input amount. If the pool has one gauge, the swap fees will be sent to the \u0060externalBribe::notifyRewardAmount()\u0060. 
The vulnerability is that function \u0060notifyRewardAmount\u0060 will be reverted if the fee amount is zero and the pool contract will send the swap fee if the inputAmount is larger than 0. So if the \u0060amount0In\u0060 or \u0060amount1In\u0060 is larger than 0 and the calculated swap fee is 0, the swap will be reverted.

The above scenario is unlikely triggered when the input token\u0027s decimal is high, for example 18. But when it comes to low decimal, it\u0027s possible.
For example:
GUSD, as one stable coin, it\u0027s decimal is 2. Checking the default swap fee ratio from the pariFactory, the default stable pool\u0027s swap fee ratio is 0.03%. Imagine we swap 30 dollar GUSD(3000GUSD) into another token, the swap fee will be zero.

\u0060\u0060\u0060javascript
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external lock {
        ...
        if (hasGauge){
            if (amount0In != 0) _sendTokenFees(token0, fee0);
            if (amount1In != 0) _sendTokenFees(token1, fee1);
        } 
       ...
    }
    function notifyRewardAmount(address token, uint amount) external lock {
        require(amount > 0);
        ...
    }
contract PairFactory is IPairFactory, Ownable {

    constructor() {
        stableFee = 3; // 0.03%
        volatileFee = 25; // 0.25%
        deployer = msg.sender;
    }
    ...
}
\u0060\u0060\u0060
### Poc
Add the below test case into FeesToBribes.t.sol. The test case will be reverted.
\u0060\u0060\u0060javascript
    function testSwapAndClaimFees() public {
        createLock();
        vm.warp(block.timestamp + 1 weeks);

        voter.createGauge(address(pair), 0);
        address gaugeAddress = voter.gauges(address(pair));
        address xBribeAddress = voter.external_bribes(gaugeAddress);
        xbribe = ExternalBribe(xBribeAddress);

        Router.route[] memory routes = new Router.route[](1);
        routes[0] = Router.route(address(USDC), address(FRAX), true);

        assertEq(
            router.getAmountsOut(USDC_1, routes)[1],
            pair.getAmountOut(USDC_1, address(USDC))
        );

        uint256[] memory assertedOutput = router.getAmountsOut(3e3, routes);
        console.log("USDC Amount: ", USDC_1);
        USDC.approve(address(router), USDC_1);
        router.swapExactTokensForTokens(
            3e3,
            assertedOutput[1],
            routes,
            address(owner),
            block.timestamp
        );
}
\u0060\u0060\u0060
## Impact
Pools with low decimal tokens may be reverted if the swap amount is not large enough.

## Code Snippet
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/Pair.sol#L295-L336
## Tool used

Manual Review

## Recommendation
If the calculated fee is 0, do not need to send fees to the \u0060externalBribe\u0060
