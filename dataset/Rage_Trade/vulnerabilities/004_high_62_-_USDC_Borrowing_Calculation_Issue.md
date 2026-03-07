# 62 - USDC Borrowing Calculation Issue

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Rage Trade
**Keywords:** USDC, borrowing, calculation, vault, borrow cap, underflow, smart contract, Ethereum, decentralized finance, audit, security, risk, deposit, withdraw, available borrow, revert, liquidation, debt, junior vault, senior vault

---

If users want to withdraw/redeem tokens by WithdrawPeriphery, they should approve token approval to WithdrawPeriphery, then call withdrawToken() or redeemToken(). But if users approve dnGmxJuniorVault to WithdrawPeriphery, anyone can withdraw/redeem his/her token.

Users should approve dnGmxJuniorVault before calling withdrawToken() or redeemToken():

\u0060\u0060\u0060solidity
function withdrawToken(
    address from,
    address token,
    address receiver,
    uint256 sGlpAmount
) external returns (uint256 amountOut) {
    // user has approved periphery to use junior vault shares
    dnGmxJuniorVault.withdraw(sGlpAmount, address(this), from);
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function redeemToken(
    address from,
    address token,
    address receiver,
    uint256 sharesAmount
) external returns (uint256 amountOut) {
    // user has approved periphery to use junior vault shares
    dnGmxJuniorVault.redeem(sharesAmount, address(this), from);
}
\u0060\u0060\u0060

For better user experience, we always use approve(WithdrawPeriphery, type(uint256).max). It means that if Alice approves the max amount, anyone can withdraw/redeem her tokens anytime. Another scenario is that if Alice approves 30 amounts, she wants...
To call withdrawToken to withdraw 30 tokens. But in this case Alice should send two transactions separately, then an attacker can frontrun withdrawToken transaction and withdraw Alice’s token.

Attackers can frontrun withdraw/redeem transactions and steal tokens. And some UI always approves max amount, which means that anyone can withdraw users\u0027 tokens.

[WithdrawPeriphery.sol#L119-L120](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/periphery/WithdrawPeriphery.sol#L119-L120)  
[WithdrawPeriphery.sol#L139-L140](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/periphery/WithdrawPeriphery.sol#L139-L140)

Manual Review

Replace from parameter by msg.sender.
\u0060\u0060\u0060solidity
// user has approved periphery to use junior vault shares
dnGmxJuniorVault.withdraw(sGlpAmount, address(this), msg.sender);
// user has approved periphery to use junior vault shares
dnGmxJuniorVault.redeem(sharesAmount, address(this), msg.sender);
\u0060\u0060\u0060

0xDosa  
Fix PR: [#45](https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/45)  
0x00052  
Fix looks good
**Source:** [GitHub Issue #62](https://github.com/sherlock-audit/2022-10-rage-trade-judging/issues/62)  
**Found by:** clems4ever, 0x52  

DnGmxJuniorVaultManager#_rebalanceBorrow fails to rebalance correctly if only one of the two assets needs a rebalance. In the case where one asset increases rapidly in price while the other stays constant, the vault may be liquidated.

\u0060\u0060\u0060solidity
// If both eth and btc swap amounts are not beyond the threshold then no
// flashloan needs to be executed | case 1
if (btcAssetAmount == 0 && ethAssetAmount == 0) return;
if (repayDebtBtc && repayDebtEth) {
    // case where both the token assets are USDC
    // only one entry required which is combined asset amount for both tokens
    assets = new address[](1);
    amounts = new uint256[](1);
    assets[0] = address(state.usdc);
    amounts[0] = (btcAssetAmount + ethAssetAmount);
} else if (btcAssetAmount == 0 || ethAssetAmount == 0) {
    // Exactly one would be true since case-1 excluded (both false) | case-2
    // One token amount = 0 and other token amount > 0
    // only one entry required for the non-zero amount token
    assets = new address[](1);
    amounts = new uint256[](1);
    if (btcAssetAmount == 0) {
        assets[0] = (repayDebtBtc ? address(state.usdc) : address(state.wbtc));
        amounts[0] = btcAssetAmount;
    } else {
        assets[0] = (repayDebtEth ? address(state.usdc) : address(state.weth));
        amounts[0] = ethAssetAmount;
    }
}
\u0060\u0060\u0060
The logic above is used to determine what assets to borrow using the flashloan. If
TherebalanceamountisunderathresholdthentheassetAmountissetequaltozero. The first check \u0060if(btcAssetAmount==0 && ethAssetAmount==0) return;\u0060 is a short circuit that returns if neither asset is above the threshold. The third check \u0060elseif(btcAssetAmount==0 || ethAssetAmount==0)\u0060 is the point of interest. Since we short circuit if both are zero then to meet this condition exactly one asset needs to be rebalanced. The logic that follows is where the error is. In the comments, it indicates that it needs to enter with the non-zero amount token but the actual logic reflects the opposite. If \u0060btcAssetAmount==0\u0060 it actually tries to enter with wBTC which would be the zero amount asset.

The result of this can be catastrophic for the vault. If one token increases in value rapidly while the other is constant the vault will only ever try to rebalance the one token but because of this logical error it will never actually complete the rebalance. If the token increases in value enough the vault would actually end up becoming liquidated.

Vault is unable to rebalance correctly if only one asset needs to be rebalanced, which can lead to the vault being liquidated.

[CodeSnippet](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/libraries/DnGmxJuniorVaultManager.sol#L353-L458)

Manual Review

Small change to reverse the logic and make it correct:
\u0060\u0060\u0060solidity
if (btcAssetAmount == 0) {
    assets[0] = (repayDebtBtc ? address(state.usdc) : address(state.wbtc));
    amounts[0] = btcAssetAmount;
} else {
    assets[0] = (repayDebtEth ? address(state.usdc) : address(state.weth));
    amounts[0] = ethAssetAmount;
}
\u0060\u0060\u0060
0xDosa  
Fix PR: https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/34  
0x00052  
Fix looks good. Inequality was changed to match recommendation
DnGmxJuniorVaultManager#harvestFees grants fees to the senior vault by converting the WETH to USDC and staking it directly. The result is that the senior vault gains value indirectly by increasing the debt of the junior vault. If the junior vault is already at its borrow cap, this will push its total borrow over the borrow cap causing DnGmxSeniorVault#availableBorrow to underflow and revert. This is called each time a user deposits or withdraws from the junior vault, meaning that the junior vault can no longer deposit or withdraw.

\u0060\u0060\u0060solidity
if (_seniorVaultWethRewards > state.wethConversionThreshold) {
    // converts senior tranche share of weth into usdc and deposit into AAVE
    // Deposit aave vault share to AAVE in usdc
    uint256 minUsdcAmount = _getTokenPriceInUsdc(state, state.weth).mulDivDown(
        _seniorVaultWethRewards * (MAX_BPS - state.slippageThresholdSwapEthBps),
        MAX_BPS * PRICE_PRECISION
    );
    // swaps weth into usdc
    (uint256 aaveUsdcAmount, ) = state._swapToken(
        address(state.weth),
        _seniorVaultWethRewards,
        minUsdcAmount
    );
    // supplies usdc into AAVE
    state._executeSupply(address(state.usdc), aaveUsdcAmount);
    // resets senior tranche rewards
    state.seniorVaultWethRewards = 0;
}
\u0060\u0060\u0060
The above lines convert the WETH owed to the senior vault to USDC and deposit it into Aave, increasing the aUSDC balance of the junior vault.
# USDC Borrowing Calculation Issue

\u0060\u0060\u0060solidity
function getUsdcBorrowed() public view returns (uint256 usdcAmount) {
    return
        uint256(
            state.aUsdc.balanceOf(address(this)).toInt256() -
                state.dnUsdcDeposited -
                state.unhedgedGlpInUsdc.toInt256()
        );
}
\u0060\u0060\u0060

The amount of USDC borrowed is calculated based on the amount of USDC that the junior vault has. By depositing the fees directly above, the junior vault has effectively "borrowed" more USDC. This can be problematic if the junior vault is already at its borrow cap.

\u0060\u0060\u0060solidity
function availableBorrow(address borrower) public view returns (uint256 availableAUsdc) {
    uint256 availableBasisCap = borrowCaps[borrower] -
        IBorrower(borrower).getUsdcBorrowed();
    uint256 availableBasisBalance = aUsdc.balanceOf(address(this));
    availableAUsdc = availableBasisCap < availableBasisBalance ?
        availableBasisCap : availableBasisBalance;
}
\u0060\u0060\u0060

If the vault is already at its borrow cap, then the line calculating \u0060availableBasisCap\u0060 will underflow and revert.

\u0060availableBorrow\u0060 will revert causing deposits/withdraws to revert.

[GitHub Code Snippet](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/vaults/DnGmxSeniorVault.sol#L350-L355)

### Tool Used
Manual Review

Check if borrowed exceeds borrow cap and return zero to avoid underflow.
