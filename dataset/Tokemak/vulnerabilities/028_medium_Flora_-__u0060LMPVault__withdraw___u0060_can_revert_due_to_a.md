# Flora - \u0060LMPVault._withdraw()\u0060 can revert due to an arithmetic underflow

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Tokemak
**Keywords:** cybersecurity, vulnerability, LMPVault, withdraw, arithmetic underflow, contract revert, maxAssetsToPull, calcUserWithdrawSharesToBurn, totalAssetsToPull, debtDecrease, totalAssetsPulled, loop halt, transaction failure, withdrawal failure, impact, mitigation, manual review, functionality disruption, smart contract, security recommendation

---

Flora

high

# \u0060LMPVault._withdraw()\u0060 can revert due to an arithmetic underflow
## Summary
\u0060LMPVault._withdraw()\u0060 can revert due to an arithmetic underflow.

## Vulnerability Detail
Inside the \u0060_withdraw()\u0060 function, the \u0060maxAssetsToPull\u0060 argument value of \u0060_calcUserWithdrawSharesToBurn()\u0060 is calculated to be equal to \u0060info.totalAssetsToPull - Math.max(info.debtDecrease, info.totalAssetsPulled)\u0060. 
However, the \u0060_withdraw()\u0060 function only halts its loop when \u0060info.totalAssetsPulled >= info.totalAssetsToPull\u0060. 
This can lead to a situation where \u0060info.debtDecrease >= info.totalAssetsToPull\u0060. Consequently, when calculating \u0060info.totalAssetsToPull - Math.max(info.debtDecrease, info.totalAssetsPulled)\u0060 for the next destination vault in the loop, an underflow occurs and triggers a contract revert.

To illustrate this vulnerability, consider the following scenario:

\u0060\u0060\u0060solidity
    function test_revert_underflow() public {
        _accessController.grantRole(Roles.SOLVER_ROLE, address(this));
        _accessController.grantRole(Roles.LMP_FEE_SETTER_ROLE, address(this));

        // User is going to deposit 1500 asset
        _asset.mint(address(this), 1500);
        _asset.approve(address(_lmpVault), 1500);
        _lmpVault.deposit(1500, address(this));

        // Deployed 700 asset to DV1
        _underlyerOne.mint(address(this), 700);
        _underlyerOne.approve(address(_lmpVault), 700);
        _lmpVault.rebalance(
            address(_destVaultOne),
            address(_underlyerOne), // tokenIn
            700,
            address(0), // destinationOut, none when sending out baseAsset
            address(_asset), // baseAsset, tokenOut
            700
        );

        // Deploy 600 asset to DV2
        _underlyerTwo.mint(address(this), 600);
        _underlyerTwo.approve(address(_lmpVault), 600);
        _lmpVault.rebalance(
            address(_destVaultTwo),
            address(_underlyerTwo), // tokenIn
            600,
            address(0), // destinationOut, none when sending out baseAsset
            address(_asset), // baseAsset, tokenOut
            600
        );

        // Deployed 200 asset to DV3
        _underlyerThree.mint(address(this), 200);
        _underlyerThree.approve(address(_lmpVault), 200);
        _lmpVault.rebalance(
            address(_destVaultThree),
            address(_underlyerThree), // tokenIn
            200,
            address(0), // destinationOut, none when sending out baseAsset
            address(_asset), // baseAsset, tokenOut
            200
        );

        // Drop the price of DV2 to 70% of original, so that 600 we transferred out is now only worth 420
         _mockRootPrice(address(_underlyerTwo), 7e17);

        // Revert because of an arithmetic underflow
        vm.expectRevert();
        uint256 assets = _lmpVault.redeem(1000, address(this), address(this));
    }
\u0060\u0060\u0060

## Impact

The vulnerability can result in the contract reverting due to an underflow, disrupting the functionality of the contract. 
Users who try to withdraw assets from the LMPVault may encounter transaction failures and be unable to withdraw their assets.

## Code Snippet

https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L475
https://github.com/sherlock-audit/2023-06-tokemak/blob/main/v2-core-audit-2023-07-14/src/vault/LMPVault.sol#L493-L504

## Tool used
Manual Review

## Recommendation
To mitigate this vulnerability, it is recommended to break the loop within the \u0060_withdraw()\u0060 function if \u0060Math.max(info.debtDecrease, info.totalAssetsPulled) >= info.totalAssetsToPull\u0060

\u0060\u0060\u0060solidity
                if (
                    Math.max(info.debtDecrease, info.totalAssetsPulled) >
                    info.totalAssetsToPull
                ) {
                    info.idleIncrease =
                        Math.max(info.debtDecrease, info.totalAssetsPulled) -
                        info.totalAssetsToPull;
                    if (info.totalAssetsPulled >= info.debtDecrease) {
                        info.totalAssetsPulled = info.totalAssetsToPull;
                    }
                    break;
                }

                // No need to keep going if we have the amount we\u0027re looking for
                // Any overage is accounted for above. Anything lower and we need to keep going
                // slither-disable-next-line incorrect-equality
                if (
                    Math.max(info.debtDecrease, info.totalAssetsPulled) ==
                    info.totalAssetsToPull
                ) {
                    break;
                }
\u0060\u0060\u0060
