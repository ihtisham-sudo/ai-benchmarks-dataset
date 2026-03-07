# `GaugeController` does not send funds to FeeCollector disrupting fees distribution and causing loss of funds

**Severity:** HIGH
**Auditor:** Codehawks

---

## Summary

The `GaugeController` bypasses the `FeeCollector` contract when distributing revenue, directly sending funds to Gauges and completely losing the performance fees. This breaks the protocol's fee management system, which is designed to have the `FeeCollector` as the central point for managing and distributing all protocol fees to various stakeholders.

## Vulnerability Details

The `FeeCollector` is designed as the central contract for managing protocol fee collection and distribution to stakeholders including veRAAC holders, treasury, and repair fund. However, the `GaugeController's` `distributeRevenue` function:

```Solidity
    function distributeRevenue(
        GaugeType gaugeType,
        uint256 amount
    ) external onlyRole(EMERGENCY_ADMIN) whenNotPaused {
        if (amount == 0) revert InvalidAmount();
        
        uint256 veRAACShare = amount * 80 / 100; // 80% to veRAAC holders
        // @audit-issue 1. performance fees calculated but never used.
        // @audit-issue 2. performance fees are not tracked
@>        uint256 performanceShare = amount * 20 / 100; // 20% performance fee
        
        revenueShares[gaugeType] += veRAACShare;
        // @audit-issue 3. bypass FeeCollector by directly distributing 80% to Gauges
        _distributeToGauges(gaugeType, veRAACShare);
        
        emit RevenueDistributed(gaugeType, amount, veRAACShare, performanceShare);
    }
```

As we can see in the code above: 

1. Bypasses `FeeCollector` by directly distributing 80% to Gauges.
2. Performance fees calculated but never used(should be sent to the `FeeCollector`)
3. Performance fees are not tracked(`performanceFees`is not used)

    

Notice that for the performance fees, there is no way to withdraw those funds, which will lead to permanently loss of funds.

This contradicts the FeeCollector's design which should:



* Collect all protocol fees
* Manage fee distributions through its configured fee types
* Ensure proper splitting between stakeholders
* Track all fee collections and distributions



The implementation meets the documentation, putting `FeeCollector`in charge of distributing all the collected fees.&#x20;



```Solidity
    function _processDistributions(uint256 totalFees, uint256[4] memory shares) internal {
        uint256 contractBalance = raacToken.balanceOf(address(this));
        if (contractBalance < totalFees) revert InsufficientBalance();


        if (shares[0] > 0) {
            uint256 totalVeRAACSupply = veRAACToken.getTotalVotingPower();
            if (totalVeRAACSupply > 0) {
                TimeWeightedAverage.createPeriod(
                    distributionPeriod,
                    block.timestamp + 1,
                    7 days,
                    shares[0],
                    totalVeRAACSupply
                );
                totalDistributed += shares[0];
            } else {
                shares[3] += shares[0]; // Add to treasury if no veRAAC holders
            }
        }


        if (shares[1] > 0) raacToken.burn(shares[1]);
        if (shares[2] > 0) raacToken.safeTransfer(repairFund, shares[2]);
        if (shares[3] > 0) raacToken.safeTransfer(treasury, shares[3]);
    }
```

## Impact

* 20% of all revenue (performance fees) are permanently lost.
* Broken fee distribution system:
  * FeeCollector loses visibility of revenue flows
  * Fee distributions bypass intended controls and splits
  * No proper tracking of collected fees
  * Stakeholders don't receive their intended share of fees
* Compromised protocol accounting:
  * Performance fees are not tracked in `performanceFees` mapping
  * FeeCollector's accounting system becomes unreliable&#x20;

## Tools Used

Manual Review

## Recommendations

1. Ensure all fees go through `FeeCollector`.

```diff
function distributeRevenue(
    GaugeType gaugeType,
    uint256 amount
) external onlyRole(EMERGENCY_ADMIN) whenNotPaused {
    if (amount == 0) revert InvalidAmount();
    
    uint256 veRAACShare = amount * 80 / 100; // 80% to veRAAC holders
    uint256 performanceShare = amount * 20 / 100; // 20% performance fee
    
    // ps: constructor should receive feeCollector and give max approval to it.
+    feeCollector.collectFee(performanceShare, 0); // 0 == Protocol Fees
+    feeCollector.collectFee(performanceShare, 2); // 2 == Performance Fees
+    performanceFees[msg.sender] += performanceShare; // Track the fees
    
    revenueShares[gaugeType] += veRAACShare;
-    _distributeToGauges(gaugeType, veRAACShare);
    
    emit RevenueDistributed(gaugeType, amount, veRAACShare, performanceShare);
}
```
