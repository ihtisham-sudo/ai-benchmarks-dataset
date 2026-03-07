# Uniswap V3 swap in `commitAndClose` susceptible to sandwich attack

**Severity:** HIGH
**Auditor:** Zokyo

---

**Description**

TracerGMXVault.sol - In body of swapToStable(...), call stack starts from external function commitAndClose(). This transaction can be spotted in pool and exposed to sandwich attack because of this snippet:

ISwapRouter.ExactInputParams memory params = ISwapRouter.ExactInputParams({
 path: route,

});

recipient: address(this),

deadline: block.timestamp,

amountIn: wethBalance,

amountOutMinimum: 0

return router.exactInput(params)

setting amountOutMinimum to zero give a chance to the attacker to exploit that. Severity of this explained by uniswap's official docs

https://docs.uniswap.org/protocol/guides/swaps/single-swaps

amountOutMinimum: we are setting to zero, but this is a significant risk in production. For a real deployment, this value should be calculated using our SDK or an onchain price oracle this helps protect against getting an unusually bad price for a trade due to a front running sandwich or another type of price manipulation

**Recommendation**

When trading from a smart contract, the most important thing to keep in mind is that access to an external price source is required. Without this, trades can be frontrun for considerable loss.

uniswap's official docs

**Re-audit comment**

Resolved
