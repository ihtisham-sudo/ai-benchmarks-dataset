# 86 - Incorrect utilization rate assumption in ReserveLogic::_updateIndexes()

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Yieldoor
**Keywords:** ReserveLogic, utilization rate, borrowing index, total borrows, stale data, interest calculation, lending pool, interest rate, financial impact, borrowing rate, closed formula, protocol functionality, contract logic, user impact, interest accrual, risk assessment, financial modeling, contract performance, protocol design

---

# Vulnerabilities in sherlock-admin2

The protocol team fixed this issue in the following PRs/commits: [https://github.com/spa](https://github.com/spa) cegliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858
**Source:** [GitHub Issue #376](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/376)  
**Found by:** 0xaxaxa, AlexCzm, Drynooo, Foundation, HChang26, KiteWeb3, R-Nemes, Ragnarok, anchabadze, armoking32, azanux, eLSeR17, elolpuer, iamephraim, iamnmt, itsgreg, mussucal, octopus_testjjj, yotov721

**Description:**  
In the \u0060collectFees()\u0060 function of the Strategy contract, there is a critical error when collecting fees from the vesting position. The function incorrectly uses the upper tick of the main position (\u0060mainPosition.tickUpper\u0060) instead of the upper tick of the vesting position (\u0060vestPosition.tickUpper\u0060):

\u0060\u0060\u0060solidity
if (ongoingVestingPosition) {
    collectPositionFees(vestPosition.tickLower, mainPosition.tickUpper);
}
\u0060\u0060\u0060

Although the vesting position is created with the same ticks as the main position:

\u0060\u0060\u0060solidity
vp.tickLower = mainPosition.tickLower;
vp.tickUpper = mainPosition.tickUpper;
\u0060\u0060\u0060

The \u0060rebalance()\u0060 function changes the ticks of the main position using the internal \u0060_setMainTicks()\u0060 function, so after calling \u0060rebalance()\u0060, the ticks of the main position and the vesting position will no longer be the same:

\u0060\u0060\u0060solidity
function rebalance() public onlyRebalancer {
    // ...
    _setMainTicks(tick);
    // ...
}
\u0060\u0060\u0060
The function \u0060_setMainTicks(int24 tick)\u0060 contains a logic error that causes a mismatch in parameters. The contract is attempting to collect fees from a position defined by the lower tick of the vesting position and the upper tick of the main position, rather than from the actual vesting position. This can lead to the situation where \u0060vestPosition.tickLower > mainPosition.tickUpper\u0060.

The protocol fails to collect fees that have accrued to the vesting position, resulting in direct financial loss. If \u0060vestPosition.tickLower > mainPosition.tickUpper\u0060, the call to \u0060collect()\u0060 will revert, since Uniswap V3 requires the lower tick to be less than the upper tick. 

> **TLU**: The lower tick must be below the upper tick

This will cause the entire \u0060collectFees()\u0060 function to revert, leading to failures in critical protocol functions such as \u0060deposit()\u0060, \u0060withdraw()\u0060, \u0060rebalance()\u0060, and \u0060compound()\u0060, where \u0060collectFees()\u0060 is a part of them. As a result, this can lead to a malfunction of the entire protocol.

Since the mechanism for closing the vesting position is inside the \u0060withdrawPartOfVestingPosition()\u0060 function, which is only called from \u0060collectFees()\u0060, and \u0060collectFees()\u0060 always reverts due to incorrect ticks, the vesting position cannot be closed, leading to a complete protocol lockup with no way to resolve the issue.
Correct the parameter in the fee collection call to use the upper tick of the vesting position:

\u0060\u0060\u0060javascript
if (ongoingVestingPosition) {
    -  collectPositionFees(vestPosition.tickLower, mainPosition.tickUpper);
    +  collectPositionFees(vestPosition.tickLower, vestPosition.tickUpper);
}
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [https://github.com/spa](https://github.com/spa) cegliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/642)

**Found by:** Bushman, Drynooo, Josh4324, KrisRenZo, Matic68, Nomadic_bear, Sarvesh Limaye, Victor_TheOracle, _0memgboji, godwinudo, kom, m3dython, montecristo, nganhg, stuart_the_minion, surenyan-oks

In the Leverager contract, the feeRecipient variable is not initialized and there is no setter function to set it. This is problematic because the liquidatePosition send funds to the feeRecipient.  
[Line 47 of Leverage](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/Leverager.sol#L47)  
[Line 299 of Leverager](https://github.com/sherlock-audit/2025-02-yieldoor/blob/main/yieldoor/src/Leverager.sol#L299)

The feeRecipient is not initialized in the constructor, and there is no function to set it after the contract has been deployed.

None

None

None

Funds to the feeRecipient when the liquidatePosition is called will be sent to address 0, there is a loss of protocol fees.
None

Initialize feeRecipient in the constructor and create a function to change the feeRecipient in the future.
## Discussion
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [https://github.com/spaceliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858](https://github.com/spaceliderrrr/yieldoor/commit/1f350860a2733a979eeb977d18b8953f9b433858)
**Source:** [GitHub Issue #85](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/85)

This issue has been acknowledged by the team but won\u0027t be fixed at this time.

**Found by:**  
0x73696d616f, armoking32

Vault::_calcDeposit() calculates the shares as \u0060depositAmount * bal * totalSupply\u0060 in the numerator. If each of these quantities has 18 decimals, this is 1e54 of precision, having only around 1e23 left. Now, if \u0060bal\u0060 and \u0060totalSupply\u0060 are for example 1e9 each, this leaves 1e5 left. Thus, any deposit exceeding 100,000 will revert. If the token is valued for example at 0.01 USD, this is very likely to happen. As deposits failing will make users miss out on yield and favorable entry prices in the pool, it is time-sensitive.

In Vault:149, there is an overflow risk.

1. Token is low valued such as 0.1 or 0.01 USD.

None.

1. User deposits in the vault but reverts, missing out on yield and a certain entry price in the pool.

User loses yield and may get worse slippage/price afterwards. Additionally, until someone withdraws it may be hard to deposit. They may split their deposits in smaller amounts.
Given enough balance and supply of a low valued token it may not be possible to deposit at all.

See above.

Implement some precision downscaling in between calculations.
## Title
ReserveLogic::_updateIndexes() assumes the utilization rate was constant the whole time when calculating the new borrows

## Source
[GitHub Issue](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/86)

## Acknowledgment
This issue has been acknowledged by the team but won\u0027t be fixed at this time.

## Found by
0x73696d616f

ReserveLogic::_updateIndexes() is as follows:
\u0060\u0060\u0060solidity
function _updateIndexes(DataTypes.ReserveData storage reserve) internal {
    uint256 newBorrowingIndex = reserve.borrowingIndex;
    uint256 newTotalBorrows = reserve.totalBorrows;
    if (reserve.totalBorrows > 0) {
        newBorrowingIndex = latestBorrowingIndex(reserve);
        newTotalBorrows = newBorrowingIndex * (reserve.totalBorrows) /
        (reserve.borrowingIndex);
    ...
}
\u0060\u0060\u0060
Note that when calculating the new Borrowing Index, it calls \u0060latestBorrowingIndex(reserve)\u0060, which uses \u0060reserve.currentBorrowingRate\u0060, which was calculated at the last time the index was updated. However, in the meantime, the borrows have grown, increasing the utilization rate, which has increased the borrowing rate, but the one used was the past one, which is incorrect. To fix this, a better closed formula would be required, simultaneously calculating the new borrows as well as the current utilization rate, which depend on one another.

In \u0060ReserveLogic:155/156\u0060, new borrows use a stale utilization rate.

None.
None.

1. Users borrow from the lending pool and their interest will be incorrect, smaller than it should be.

Depending on utilization, the impact can be very significant; however, it is likely to stay relatively constrained due to daily utilization or similar.

Borrow interest depends on the utilization rate. The utilization rate grows with borrows, so it cannot stay constant when calculating the new borrows over time.

Implement a closed formula that calculates the new borrows and utilization rate correctly.
whenthetickspacingisoneduetoincorrectisLower
Sidedinequality  
Source: [GitHub Issue #94](https://github.com/sherlock-audit/2025-02-yieldoor-judging/issues/94)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.  
Found by:  
000000, 0x73696d616f, armoking32, bladeee  

Strategymainpositionticksaresetaccordingto:
\u0060\u0060\u0060solidity
function _setMainTicks(int24 tick) internal {
    int24 halfWidth = int24(positionWidth / 2);
    int24 modulo = tick % tickSpacing;
    if (modulo < 0) modulo += tickSpacing; // if tick is negative, modulo is also negative
    bool isLowerSided = modulo < (tickSpacing / 2);
    int24 tickBorder = tick - modulo;
    if (!isLowerSided) tickBorder += tickSpacing;
    mainPosition.tickLower = tickBorder - halfWidth;
    mainPosition.tickUpper = tickBorder + halfWidth;
    emit NewMainTicks(tickBorder - halfWidth, tickBorder + halfWidth);
}
\u0060\u0060\u0060
As can be seen, when the tick spacing is 1, the tick will be deemed lower sided, which adds a tick spacing (1) to the tick border. So, if the current tick is -1769, the ticks will be -1770 to -1766, which is not symmetric and will miss out on fees.

In Strategy:236, is lower sided check is incorrect.

None.
## External Pre-conditions
None.
