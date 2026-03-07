# xiaoming90 - Long traders unable to withdraw their assets

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** FlatMoney
**Keywords:** cybersecurity, vulnerability, long traders, withdrawal, protocol, bricked, margin, collateral, LPs, stable collateral, tracked balance, invariant check, profit, loss of assets, updateGlobalPositionData, executeOpen, executeAdjust, executeClose, liquidation, manual review

---

xiaoming90

high

# Long traders unable to withdraw their assets

## Summary

Whenever the protocol reaches a state where the long trader\u0027s profit is larger than LP\u0027s stable collateral total, the protocol will be bricked. As a result, the margin deposited and gain of the long traders can no longer be withdrawn and the LPs cannot withdraw their collateral, leading to a loss of assets for the  users.

## Vulnerability Detail

Per Line 97 below, if the collateral balance is less than the tracked balance, the \u0060_getCollateralNet\u0060 invariant check will revert.

https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/misc/InvariantChecks.sol#L97

\u0060\u0060\u0060solidity
File: InvariantChecks.sol
089:     /// @dev Returns the difference between actual total collateral balance in the vault vs tracked collateral
090:     ///      Tracked collateral should be updated when depositing to stable LP (stableCollateralTotal) or
091:     ///      opening leveraged positions (marginDepositedTotal).
092:     /// TODO: Account for margin of error due to rounding.
093:     function _getCollateralNet(IFlatcoinVault vault) private view returns (uint256 netCollateral) {
094:         uint256 collateralBalance = vault.collateral().balanceOf(address(vault));
095:         uint256 trackedCollateral = vault.stableCollateralTotal() + vault.getGlobalPositions().marginDepositedTotal;
096: 
097:         if (collateralBalance < trackedCollateral) revert FlatcoinErrors.InvariantViolation("collateralNet");
098: 
099:         return collateralBalance - trackedCollateral;
100:     }
\u0060\u0060\u0060

Assume that:

- Bob\u0027s long position: Margin = 50 ETH
- Alice\u0027s LP: Deposited = 50 ETH
- Collateral Balance = 100 ETH
- Tracked Balance = 100 ETH (Stable Collateral Total = 50 ETH, Margin Deposited Total = 50 ETH)

Assume that Bob\u0027s long position gains a profit of 51 ETH.

The following actions will trigger the \u0060updateGlobalPositionData\u0060 function internally: executeOpen, executeAdjust, executeClose, and liquidation.

When the \u0060 FlatcoinVault.updateGlobalPositionData\u0060 function is triggered to update the global position data:

\u0060\u0060\u0060solidity
profitLossTotal = 51 ETH (gain by long)

newMarginDepositedTotal = marginDepositedTotal + marginDelta + profitLossTotal
newMarginDepositedTotal = 50 ETH + 0 + 51 ETH = 101 ETH

_updateStableCollateralTotal(-51 ETH)
newStableCollateralTotal = stableCollateralTotal + _stableCollateralAdjustment
newStableCollateralTotal = 50 ETH + (-51 ETH) = -1 ETH
stableCollateralTotal = (newStableCollateralTotal > 0) ? newStableCollateralTotal : 0;
stableCollateralTotal = 0
\u0060\u0060\u0060

In this case, the state becomes as follows:

- Collateral Balance = 100 ETH
- Tracked Balance = 101 ETH (Stable Collateral Total = 0 ETH, Margin Deposited Total = 101 ETH)

Notice that the Collateral Balance and Tracked Balance are no longer in sync. As such, the revert will occur when the \u0060_getCollateralNet\u0060 invariant checks are performed.

Whenever the protocol reaches a state where the long trader\u0027s profit is larger than LP\u0027s stable collateral total, this issue will occur, and the protocol will be bricked. The margin deposited and gain of the long traders can no longer be withdrawn from the protocol. The LPs also cannot withdraw their collateral.

The reason is that the \u0060_getCollateralNet\u0060 invariant checks are performed in all functions of the protocol that can be accessed by users (listed below):

- Deposit
- Withdraw
- Open Position
- Adjust Position
- Close Position
- Liquidate

## Impact

Loss of assets for the users. Since the protocol is bricked due to revert, the long traders are unable to withdraw their deposited margin and gain and the LPs cannot withdraw their collateral.

## Code Snippet

https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/misc/InvariantChecks.sol#L97

## Tool used

Manual Review

## Recommendation

Currently, when the loss of the LP is more than the existing \u0060stableCollateralTotal\u0060, the loss will be capped at zero, and it will not go negative. In the above example, the \u0060stableCollateralTotal\u0060 is 50, and the loss is 51. Thus, the \u0060stableCollateralTotal\u0060 is set to zero instead of -1.

The loss of LP and the gain of the trader should be aligned or symmetric. However, this is not the case in the current implementation. In the above example, the gain of traders is 51, while the loss of LP is 50, which results in a discrepancy here.

To fix the issue, the loss of LP and the gain of the trader should be aligned. For instance, in the above example, if the loss of LP is capped at 50, then the profit of traders must also be capped at 50.

Following is a high-level logic of the fix:

\u0060\u0060\u0060solidity
If (profitLossTotal > stableCollateralTotal): // (51 > 50) => True
	profitLossTotal = stableCollateralTotal // profitLossTotal = 50
	
newMarginDepositedTotal = marginDepositedTotal + marginDelta + profitLossTotal // 50 + 0 + 50 = 100
	
newStableCollateralTotal = stableCollateralTotal + (-profitLossTotal) // 50 + (-50) = 0
stableCollateralTotal = (newStableCollateralTotal > 0) ? newStableCollateralTotal : 0; // stableCollateralTotal = 0
\u0060\u0060\u0060

The comment above verifies that the logic is working as intended.
