# 39 - Users withdrawing tokens other than USDC can suffer huge loss of funds due to virtually no slippage protection.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Rage Trade
**Keywords:** withdraw, tokens, USDC, slippage, protection, loss, funds, manual review, Chainlink, oracles, sandwich attack, MAX_BPS, slippageThreshold, outputGlp, tokenPrice, decimals, glpPrice, withdrawPeriphery, contracts, audit

---

# Impact
Users withdrawing tokens other than USDC can suffer huge loss of funds due to virtually no slippage protection.

[WithdrawPeriphery.sol](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/periphery/WithdrawPeriphery.sol#L147-L161)

### Toolused
Manual Review

Adjust minTokenOut to match the decimals of the token:
\u0060\u0060\u0060solidity
uint256 minTokenOut = outputGlp.mulDiv(glpPrice * (MAX_BPS - slippageThreshold), tokenPrice * MAX_BPS);
minTokenOut = minTokenOut * 10 ** (token.decimals() - 6);
\u0060\u0060\u0060

**0xDosa**  
Agreed on the issue but the severity level should be medium since loss of funds is not possible. While swapping on GMX, there is min-max spread and fees but no slippage due to them using chainlink oracles for pricing the tokens, so a direct sandwich attack would not work.

**Evert0x**  
Downgrading to medium

**0xDosa**  
Fix PR: [#38](https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/38)

**0x00052**  
Fix looks good. Slippage is now adjusted to match token decimals.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-10-rage-trade-judging/issues/39)  
**Found by:** 0x52  

WithdrawPeriphery accidentally uses an incorrect value for MAX_BPS which will allow for much higher slippage than intended.

\u0060\u0060\u0060solidity
uint256 internal constant MAX_BPS = 1000;
\u0060\u0060\u0060
BPS is typically 10,000 and using 1000 is inconsistent with the rest of the ecosystem contracts and tests. The result is that slippage values will be 10x higher than intended.

Unexpected slippage resulting in loss of user funds, likely due to MEV.

[WithdrawPeriphery.sol](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/periphery/WithdrawPeriphery.sol#L47)

Manual Review

Correct MAX_BPS:
\u0060\u0060\u0060solidity
-  uint256 internal constant MAX_BPS = 1000;
+  uint256 internal constant MAX_BPS = 10_000;
\u0060\u0060\u0060
0xDosa  
Fix PR: https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/40  
0x00052  
Fix looks good. Max_BPS has been updated
**Source:** [GitHub Issue #37](https://github.com/sherlock-audit/2022-10-rage-trade-judging/issues/37)  
**Found by:** tives, __141345__, GimelSec, cccz, clems4ever, ctf_sec, peanuts, joestakey, rvierdiiev, 0x52

To calculate the exchange rate for shares in DnGmx Senior Vault, it divides the total supply of shares by the total assets of the vault. The first deposit can mint a very small number of shares then donate a USDC to the vault to grossly manipulate the share price. When later depositors deposit into the vault, they will lose value due to precision loss and the adversary will profit.

\u0060\u0060\u0060solidity
function convertToShares(uint256 assets) public view virtual returns (uint256) {
    uint256 supply = totalSupply(); // Saves an extra SLOAD if totalSupply is non-zero.
    return supply == 0 ? assets : assets.mulDivDown(supply, totalAssets());
}
\u0060\u0060\u0060
Share exchange rate is calculated using the total supply of shares and the total assets. This can lead to exchange rate manipulation. As an example, an adversary can mint a single share, then donate 1e8 aUSDC. Minting the first share established a 1:1 ratio but then donating 1e8 changed the ratio to 1:1e8. Now any deposit lower than 1e8 (100 aUSDC) will suffer from precision loss and the attacker\u0027s share will benefit from it. This same vector is present in DnGmx Junior Vault.

Adversary can effectively steal funds from later users.
https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/vaults/DnGmxSeniorVault.sol#L211-L221

Manual Review

Initialize should include a small deposit, such as 1e6 aUSDC that mints the share to a dead address to permanently lock the exchange rate:
\u0060\u0060\u0060solidity
aUsdc.approve(address(pool), type(uint256).max);
IERC20(asset).approve(address(pool), type(uint256).max);
deposit(1e6, DEAD_ADDRESS);
\u0060\u0060\u0060

0xDosa  
We will ensure a guarded launch process that safeguards the first deposit to avoid being manipulated.  
Evert0x  
We are still considering it a valid issue as the guarded launch process is out of scope.
**Source:** [GitHub Issue #36](https://github.com/sherlock-audit/2022-10-rage-trade-judging/issues/36)  
**Found by:** 0x52  

The maximize input to DnGmxJuniorVaultManager#_totalAssets indicates whether to either maximize or minimize the NAV. Internal logic of the function doesn\u0027t accurately reflect that because under some circumstances, maximize = true actually returns a lower value than maximize = false.

\u0060\u0060\u0060solidity
uint256 unhedgedGlp = (state.unhedgedGlpInUsdc + dnUsdcDepositedPos).mulDivDown(
    PRICE_PRECISION,
    _getGlpPrice(state, !maximize)
);
// calculate current borrow amounts
(uint256 currentBtc, uint256 currentEth) = _getCurrentBorrows(state);
uint256 totalCurrentBorrowValue = _getBorrowValue(state, currentBtc, currentEth);
// add negative part to current borrow value which will be subtracted at the end
// convert usdc amount into glp amount
uint256 borrowValueGlp = (totalCurrentBorrowValue +
    dnUsdcDepositedNeg).mulDivDown(
    PRICE_PRECISION,
    _getGlpPrice(state, !maximize)
);
// if we need to minimize then add additional slippage
if (!maximize) unhedgedGlp = unhedgedGlp.mulDivDown(MAX_BPS -
    state.slippageThresholdGmxBps, MAX_BPS);
if (!maximize) borrowValueGlp = borrowValueGlp.mulDivDown(MAX_BPS -
    state.slippageThresholdGmxBps, MAX_BPS);
\u0060\u0060\u0060
To maximize the estimate for the NAV of the vault underlying debt should be minimized and value of held assets should be maximized. Under the current settings there is
A mix of both of those and the function doesn\u0027t consistently minimize or maximize. Consider when NAV is "maximized". Under this scenario the value of when estimated the GlpPrice is minimized. This minimizes the value of both the borrowedGlp (debt) and of the unhedgedGlp (assets). The result is that the NAV is not maximized because the value of the assets are also minimized. In this scenario the GlpPrice should be maximized when calculating the assets and minimized when calculating the debt. The reverse should be true when minimizing the NAV. Slippage requirements are also applied incorrectly when adjusting borrowValueGlp. The current implementation implies that if the debt were to be paid back that the vault would repay their debt for less than expected. When paying back debt the slippage should imply paying more than expected rather than less, therefore the slippage should be added rather than subtracted.

DnGmxJuniorVaultManager#_totalAssets doesn\u0027t accurately reflect NAV. Since this is used when determining critical parameters it may lead to inaccuracies.

[Link to Code](https://github.com/sherlock-audit/2022-10-rage-trade/blob/main/dn-gmx-vaults/contracts/libraries/DnGmxJuniorVaultManager.sol#L1013-L1052)
## Tool Used
Manual Review

To properly maximize it should assume the best possible rate for exchanging its assets. Likewise to minimize it should assume its debt is as large as possible and that it encounters maximum possible slippage when repaying its debt. I recommend the following changes:
\u0060\u0060\u0060solidity
uint256 unhedgedGlp = (state.unhedgedGlpInUsdc +
    dnUsdcDepositedPos).mulDivDown(
        PRICE_PRECISION,
        _getGlpPrice(state, !maximize)
        + _getGlpPrice(state, maximize)
    );
// calculate current borrow amounts
(uint256 currentBtc, uint256 currentEth) = _getCurrentBorrows(state);
uint256 totalCurrentBorrowValue = _getBorrowValue(state, currentBtc,
    currentEth);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// add negative part to current borrow value which will be subtracted at the
// convert usdc amount into glp amount
uint256 borrowValueGlp = (totalCurrentBorrowValue +
    dnUsdcDepositedNeg).mulDivDown(
       PRICE_PRECISION,
       _getGlpPrice(state, !maximize)
);
// if we need to minimize then add additional slippage
if (!maximize) unhedgedGlp = unhedgedGlp.mulDivDown(MAX_BPS -
    state.slippageThresholdGmxBps, MAX_BPS);
if (!maximize) borrowValueGlp = borrowValueGlp.mulDivDown(MAX_BPS +
    state.slippageThresholdGmxBps, MAX_BPS);
\u0060\u0060\u0060

0xDosa  
Dividing with minimum price would maximize the asset/borrow amount and vice versa.  
So the correct fix should be this. @0x00052 could you confirm?
\u0060\u0060\u0060solidity
uint256 unhedgedGlp = (state.unhedgedGlpInUsdc +
    dnUsdcDepositedPos).mulDivDown(
       PRICE_PRECISION,
       _getGlpPrice(state, !maximize)
);
// calculate current borrow amounts
(uint256 currentBtc, uint256 currentEth) = _getCurrentBorrows(state);
uint256 totalCurrentBorrowValue = _getBorrowValue(state, currentBtc,
    currentEth);
// add negative part to current borrow value which will be subtracted at the
// convert usdc amount into glp amount
uint256 borrowValueGlp = (totalCurrentBorrowValue +
    dnUsdcDepositedNeg).mulDivDown(
       PRICE_PRECISION,
       _getGlpPrice(state, maximize)
);
// if we need to minimize then add additional slippage
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
if (!maximize) unhedgedGlp = unhedgedGlp.mulDivDown(MAX_BPS -
                   state.slippageThresholdGmxBps, MAX_BPS);
if (!maximize) borrowValueGlp = borrowValueGlp.mulDivDown(MAX_BPS +
                   state.slippageThresholdGmxBps, MAX_BPS);
\u0060\u0060\u0060
## Comments
Goodcatch! You\u0027re right, I got that backwards.

Fix PR: [https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/35](https://github.com/RageTrade/delta-neutral-gmx-vaults/pull/35)

Fix looks good. Debt/asset value are now properly minimized and slippage is applied in the proper direction for debt.
PAGE END
