# .3.2.8 The lack of slippage protection leads to capital loss

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** slippage, protection, capital loss, sandwich attacks, wstETH, WETH, Uniswap v3, protocol, conversion, amountIn, amountOut, ETH, user, risk, vulnerability, crypto, decentralized finance, trading, security, smart contracts

---

# .3.2.8 The lack of slippage protection leads to capital loss
- **Submitted by**: Bauer, also found by 0xRajkumar and Bauchibred
- **Severity**: Medium Risk
- **Context**: (No context files were provided by the reviewer)
- **Description**: In the function, if the amount to be converted is not equal to the expected amount, the protocol calculates the output amount, converts this amount of stETH to WETH, and then transfers it to the user as ETH:
  
  \u0060\u0060\u0060
  amountIn - amountOut
  \u0060\u0060\u0060
  
  When converting wstETH to WETH in Uniswap v3, we found that the slippage protection is set to 0, indicating no protection against slippage. This leaves the protocol vulnerable to sandwich attacks:
