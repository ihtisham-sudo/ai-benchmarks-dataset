# Bauer - Inaccurate collateral factor calculation due to missing collateral asset

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, collateral factor, smart contract, collateral assets, total value, USD value, oracle, decimal precision, totalAssetsUSD, inaccurate calculation, removal of assets, risk assessment, protocol stability, rebalancing, SellUSSDBuyCollateral, manual review, risk management, impact analysis, financial protocol

---

Bauer

high

# Inaccurate collateral factor calculation due to missing collateral asset

## Summary
The function \u0060collateralFactor()\u0060 in the smart contract calculates the collateral factor for the protocol but fails to account for the removal of certain collateral assets. As a result, the total value of the removed collateral assets is not included in the calculation, leading to an inaccurate collateral factor.

## Vulnerability Detail
The \u0060collateralFactor()\u0060 function calculates the current collateral factor for the protocol. It iterates through each collateral asset in the system and calculates the total value of all collateral assets in USD.

For each collateral asset, the function retrieves its balance and converts it to a USD value by multiplying it with the asset\u0027s price in USD obtained from the corresponding oracle. The balance is adjusted for the decimal precision of the asset. These USD values are accumulated to calculate the totalAssetsUSD.
\u0060\u0060\u0060solidity
   function collateralFactor() public view override returns (uint256) {
        uint256 totalAssetsUSD = 0;
        for (uint256 i = 0; i < collateral.length; i++) {
            totalAssetsUSD +=
                (((IERC20Upgradeable(collateral[i].token).balanceOf(
                    address(this)
                ) * 1e18) /
                    (10 **
                        IERC20MetadataUpgradeable(collateral[i].token)
                            .decimals())) *
                    collateral[i].oracle.getPriceUSD()) /
                1e18;
        }

        return (totalAssetsUSD * 1e6) / totalSupply();
    }
\u0060\u0060\u0060
However, when a collateral asset is removed from the collateral list, the \u0060collateralFactor\u0060 function fails to account for its absence. This results in an inaccurate calculation of the collateral factor. Specifically, the totalAssetsUSD variable does not include the value of the removed collateral asset, leading to an underestimation of the total collateral value. The function \u0060SellUSSDBuyCollateral()\u0060 in the smart contract is used for rebalancing. However, it relies on the collateralFactor calculation, which has been found to be inaccurate. The collateralFactor calculation does not accurately assess the portions of collateral assets to be bought or sold during rebalancing. This discrepancy can lead to incorrect rebalancing decisions and potentially impact the stability and performance of the protocol.
\u0060\u0060\u0060solidity
    function removeCollateral(uint256 _index) public onlyControl {
        collateral[_index] = collateral[collateral.length - 1];
        collateral.pop();
    }
\u0060\u0060\u0060
## Impact
As a consequence, the reported collateral factor may be lower than it should be, potentially affecting the risk assessment and stability of the protocol. 

## Code Snippet
https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L179-L194

## Tool used

Manual Review

## Recommendation
Ensure accurate calculations and maintain the integrity of the collateral factor metric in the protocol\u0027s risk management system.

