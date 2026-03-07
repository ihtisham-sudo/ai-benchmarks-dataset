# Salem - User Collateral Cap Check Issue

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, collateral cap, user collateral, deposit processing, validation check, accountProps, token amount, tradeTokenConfig, manual review, impact assessment, security recommendation, code snippet, POC, exceeding cap, deposit amount, total collateral, predefined limits, risk management, financial security

---

Salem

High

# User Collateral Cap Check Issue

## Summary
   
User Collateral can  exceeds the cap andd deposit will still be processed
## Vulnerability Detail

The check \u0060accountProps.getTokenAmount(token) > tradeTokenConfig.collateralUserCap\u0060 is designed to ensure that a user\u0027s collateral does not exceed their specific cap. However, this validation occurs before the new deposit amount is added, thereby only verifying the current balance. Consequently, this can result in the user\u0027s collateral exceeding the cap once the deposit is processed.

## Impact

this can result in the user\u0027s collateral exceeding the cap once the deposit is processed.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/AssetsProcess.sol#L81

POC

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "forge-std/Test.sol";
import "../src/AssetsProcess.sol";
import "../src/mocks/MockERC20.sol";
import "../src/mocks/MockVault.sol";
import "../src/mocks/MockAccount.sol";
import "../src/mocks/MockAppTradeTokenConfig.sol";
import "../src/mocks/MockCommonData.sol";

contract AssetsProcessTest is Test {
    AssetsProcess assetsProcess;
    MockERC20 token;
    MockVault vault;
    MockAccount account;
    MockAppTradeTokenConfig appTradeTokenConfig;
    MockCommonData commonData;

    address user = address(0x123);

    function setUp() public {
        token = new MockERC20("Mock Token", "MTK", 18);
        vault = new MockVault();
        account = new MockAccount();
        appTradeTokenConfig = new MockAppTradeTokenConfig();
        commonData = new MockCommonData();

        assetsProcess = new AssetsProcess();

        // Set up initial balances and allowances
        token.mint(user, 1000 ether);
        token.approve(address(vault), 1000 ether);
        token.approve(address(assetsProcess), 1000 ether);

        // Set up mock configurations
        appTradeTokenConfig.setTradeTokenConfig(address(token), true, 500 ether, 100 ether);
        commonData.setTradeTokenCollateral(address(token), 0);
    }

    function testUserCollateralCapCheckIssue() public {
        // Set initial user balance to 90 ether
        account.setTokenAmount(user, address(token), 90 ether);

        // Deposit 20 ether, which should exceed the user cap of 100 ether
        AssetsProcess.DepositParams memory params = AssetsProcess.DepositParams({
            account: user,
            token: address(token),
            amount: 20 ether,
            from: AssetsProcess.DepositFrom.MANUAL,
            isNativeToken: false
        });

        // Expect the deposit to succeed despite exceeding the user cap
        vm.prank(user);
        assetsProcess.deposit(params);

        // Check the final balance to confirm the vulnerability
        uint256 finalBalance = account.getTokenAmount(user, address(token));
        assertEq(finalBalance, 110 ether, "User collateral cap exceeded");
    }
}
\u0060\u0060\u0060
## Tool used

Manual Review

## Recommendation
Please find the updated check for the new deposit amount below:

\u0060\u0060\u0060js
uint256 newUserCollateralAmount = accountProps.getTokenAmount(token) + params.amount;
require(newUserCollateralAmount <= tradeTokenConfig.collateralUserCap, "CollateralUserCapOverflow");
\u0060\u0060\u0060

This modification ensures that the user\u0027s total collateral, including the new deposit, does not exceed the predefined user cap.

