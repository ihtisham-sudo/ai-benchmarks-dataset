# 0x00052 - Typo in availableBorrow Function

**Severity:** low
**Auditor:** Sherlock
**Protocol:** Rage Trade
**Keywords:** availableBorrow, borrowCap, borrowed, IBorrower, aUsdc, function, slippage, uint256, returns, address, view, public, balanceOf, return, availableBasisCap, availableBasisBalance, borrower, cap, contract, protocol

---

# Typo in availableBorrow Function

\u0060\u0060\u0060solidity
function availableBorrow(address borrower) public view returns (uint256 availableAUsdc) {
    uint256 borrowCap = borrowCaps[borrower];
    uint256 borrowed = IBorrower(borrower).getUsdcBorrowed();
    if (borrowed > borrowCap) return 0;
    uint256 availableBasisCap = borrowCap - borrowed;
    uint256 availableBasisBalance = aUsdc.balanceOf(address(this));
    availableAUsdc = availableBasisCap < availableBasisBalance ? availableBasisCap : availableBasisBalance;
}
\u0060\u0060\u0060

- 0x00052
  - Typo. Only meant to mention #52
- 0xDosa
  - Fix PR: [https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/33](https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/33)
- 0x00052
  - Fix looks good. Underflow protection added as recommended
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-10-rage-trade-judging/issues/61)  
**Found by:** clems4ever  

In DnGmxJuniorVaultManager.sol at line 647: usdcPrice should be on denominator and MAX_PRECISION on numerator (cf pricing in Vault: uint256 redemptionAmount = _usdgAmount.mul(PRICE_PRECISION).div(price);)  
[Code Reference](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/libraries/DnGmxJuniorVaultManager.sol#L646)

In the case usdcPrice is higher than $1 (which already happened in reasonable market circumstances), the minimum amount expected will be higher than the swap result under 0% slippage conditions. The call will revert, which will delay rebalances until usdcPrice comes back to $1, causing potential loss to the protocol.

Manual Review

**Recommendation in summary**

0xDosa  
The suggested fix seems to be incorrect. Since we already are passing the value in usdc amount, hence neither multiplication nor division with usdcPrice should be required.  
0x00052
Agreed, suggested fix is incorrect. It should only adjust for slippage  
0xDosa  
Fix PR: https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/37  
0x00052  
Fix looks good. Value is now only adjusted to account for slippage
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-10-rage-trade-judging/issues/55)  
**Found by:** clems4ever, 0x52

WithdrawPeriphery allows the user to redeem junior share vaults to any token available on GMX, applying a fixed slippage threshold to all redeems. The slippage calculation always returns the number of tokens to 6 decimals. This works fine for USDC but for other tokens like WETH or WBTC that are 18 decimals the slippage protection is completely ineffective and can lead to loss of funds for users that are withdrawing.

\u0060\u0060\u0060solidity
function _convertToToken(address token, address receiver) internal returns (uint256 amountOut) {
    // this value should be whatever glp is received by calling withdraw/redeem
    // to junior vault
    uint256 outputGlp = fsGlp.balanceOf(address(this));
    // using min price of glp because giving in glp
    uint256 glpPrice = _getGlpPrice(false);
    // using max price of token because taking token out of gmx
    uint256 tokenPrice = gmxVault.getMaxPrice(token);
    // apply slippage threshold on top of estimated output amount
    uint256 minTokenOut = outputGlp.mulDiv(glpPrice * (MAX_BPS - slippageThreshold), tokenPrice * MAX_BPS);
    // will revert if atleast minTokenOut is not received
    amountOut = rewardRouter.unstakeAndRedeemGlp(address(token), outputGlp, minTokenOut, receiver);
}
\u0060\u0060\u0060
WithdrawPeriphery allows the user to redeem junior share vaults to any token available on GMX. To prevent users from losing large amounts of value to MEV the contract applies a fixed percentage slippage. minToken out is returned to 6 decimals regardless of the token being requested. This works for tokens with 6 decimals like USDC, but is completely ineffective for the majority of tokens that aren\u0027t.
