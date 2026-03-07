# xiaoming90 - Long trader\u0027s deposited margin can be wiped out

**Severity:** high
**Auditor:** Sherlock
**Protocol:** FlatMoney
**Keywords:** cybersecurity, vulnerability, logic error, long trader, margin collateral, funding fees, asset loss, negative total, underflow revert, marginDepositedTotal, system exploit, financial loss, code review, pseudocode, error handling, trading platform, risk management, position management, security flaw, manual review

---

xiaoming90

high

# Long trader\u0027s deposited margin can be wiped out

## Summary

Long Trader\u0027s deposited margin can be wiped out due to a logic error, leading to a loss of assets.

## Vulnerability Detail

https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/FlatcoinVault.sol#L232

\u0060\u0060\u0060solidity
File: FlatcoinVault.sol
216:     function settleFundingFees() public returns (int256 _fundingFees) {
..SNIP..
226:         // Calculate the funding fees accrued to the longs.
227:         // This will be used to adjust the global margin and collateral amounts.
228:         _fundingFees = PerpMath._accruedFundingTotalByLongs(_globalPositions, unrecordedFunding);
229: 
230:         // In the worst case scenario that the last position which remained open is underwater,
231:         // we set the margin deposited total to 0. We don\u0027t want to have a negative margin deposited total.
232:         _globalPositions.marginDepositedTotal = (int256(_globalPositions.marginDepositedTotal) > _fundingFees)
233:             ? uint256(int256(_globalPositions.marginDepositedTotal) + _fundingFees)
234:             : 0;
235: 
236:         _updateStableCollateralTotal(-_fundingFees);
\u0060\u0060\u0060

#### Issue 1

Assume that there are two long positions in the system and the \u0060_globalPositions.marginDepositedTotal\u0060 is $X$.

Assume that the funding fees accrued to the long positions at Line 228 is $Y$. $Y$ is a positive value indicating the overall gain/profit that the long traders received from the LPs. 

In this case, the \u0060_globalPositions.marginDepositedTotal\u0060 should be set to $(X + Y)$ after taking into consideration the funding fee gain/profit accrued by the long positions.

However, in this scenario, $X < Y$​. Thus, the condition at Line 232 will be evaluated as \u0060false,\u0060 and the \u0060 _globalPositions.marginDepositedTotal\u0060 will be set to zero. This effectively wipes out all the margin collateral deposited by the long traders in the system, and the deposited margin of the long traders is lost.

#### Issue 2

The second issue with the current implementation is that it does not accurately capture scenarios where the addition of \u0060_globalPositions.marginDepositedTotal\u0060 and \u0060_fundingFees\u0060 result in a negative number. This is because \u0060_fundingFees\u0060 could be a large negative number that, when added to \u0060_globalPositions.marginDepositedTotal\u0060, results in a negative total, but the condition at Line 232 above still evaluates as true, resulting in an underflow revert.

## Impact

Loss of assets for the long traders as mentioned above.

## Code Snippet

https://github.com/sherlock-audit/2023-12-flatmoney/blob/main/flatcoin-v1/src/FlatcoinVault.sol#L232

## Tool used

Manual Review

## Recommendation

If the intention is to ensure that \u0060_globalPositions.marginDepositedTotal\u0060 will never become negative, consider summing up $(X + Y)$​ first and determine if the result is less than zero. If yes, set the \u0060_globalPositions.marginDepositedTotal\u0060 to zero.

The following is the pseudocode:

\u0060\u0060\u0060solidity
newMarginTotal = globalPositions.marginDepositedTota + _fundingFees;
globalPositions.marginDepositedTotal = newMarginTotal > 0 ? uint256(newMarginTotal) : 0;
\u0060\u0060\u0060
