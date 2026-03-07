# KrisRenZo - Use of outdated liability value in decreasePosition leads to account error

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cyber security, vulnerability, outdated liability, decreasePosition, account error, protocol, repaid liability, LpPoolProcess, updatePnlAndUnHoldPoolAmount, settlement value, tokens, repayLiability, liability, settled amount, addLiability, unsettled, fee overcharge, manual review, recommendation, impact

---

KrisRenZo

Medium

# Use of outdated liability value in decreasePosition leads to account error

## Summary
Protocol ignores repaid liability when calling \u0060LpPoolProcess.updatePnlAndUnHoldPoolAmount\u0060.


## Vulnerability Detail
 \u0060_settleCrossAccount()\u0060  may accrue some value which may be paid in subsequent call in \u0060repayLiability\u0060, however the old liability value is used to update Pool  settlement value
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/DecreasePositionProcess.sol#L119-L128
When the user\u0027s tokens increase, they will always be used to repay the liability first. For example, this occurs when tokens are deposited or when tokens increase after a position is closed and settled. It will only be triggered when there is a liability, and the settled amount has a value. addLiability refers to the newly generated liability this time, so the pool will record that it has not received the corresponding funds and mark it as unsettled. repayLiability refers to repaying the user\u0027s previous debt.

## Impact
Inaccurate accounting leading to fee overcharge on users.


## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/DecreasePositionProcess.sol#L119-L128
\u0060\u0060\u0060js
	if (cache.position.isCrossMargin) {
		uint256 addLiability = _settleCrossAccount(params.requestId, accountProps, position, cache);
		accountProps.repayLiability(cache.position.marginToken);
		LpPoolProcess.updatePnlAndUnHoldPoolAmount(
			symbolProps.stakeToken,
			cache.position.marginToken,
			cache.unHoldPoolAmount,
			cache.poolPnlToken,
			addLiability
		);
\u0060\u0060\u0060


## Tool used
Manual Review

## Recommendation
Factor in the liability that has been paid before calling \u0060LpPoolProcess::updatePnlAndUnHoldPoolAmount\u0060

