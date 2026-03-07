# No lender is able to exit even after the market is closed

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, impact, lenders, market, withdrawal, borrower, fixed-term hook, assets, fixedTermEndTime, block.timestamp, manual review, mitigation, timing, proof of concept, market closure, asset protection, security flaw, smart contract, testing

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/FixedTermLoanHooks.sol#L848-L868
https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/FixedTermLoanHooks.sol#L943-L946


# Vulnerability details

## Impact
Lenders might not be able to exit even after the market is closed
## Proof of Concept
When a borrower creates a market hooked by a [fixed-term hook](https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/FixedTermLoanHooks.sol), all lenders are prohibited from withdrawing their assets from the market before the fixed-term time has elapsed.
The borrower can close the market at any time. However, \u0060fixedTermEndTime\u0060 of the market is not updated, preventing lenders from withdrawing their assets if \u0060fixedTermEndTime\u0060 has not yet elapsed.

Copy below codes to [WildcatMarket.t.sol](https://github.com/code-423n4/2024-08-wildcat/blob/main/test/market/WildcatMarket.t.sol) and run forge test --match-test test_closeMarket_BeforeFixedTermExpired:
\u0060\u0060\u0060solidity
  function test_closeMarket_BeforeFixedTermExpired() external {
    //@audit-info deploy a FixedTermLoanHooks template
    address fixedTermHookTemplate = LibStoredInitCode.deployInitCode(type(FixedTermLoanHooks).creationCode);
    hooksFactory.addHooksTemplate(
      fixedTermHookTemplate,
      \u0027FixedTermLoanHooks\u0027,
      address(0),
      address(0),
      0,
      0
    );
    
    vm.startPrank(borrower);
    //@audit-info borrower deploy a FixedTermLoanHooks hookInstance
    address hooksInstance = hooksFactory.deployHooksInstance(fixedTermHookTemplate, \u0027\u0027);
    DeployMarketInputs memory parameters = DeployMarketInputs({
      asset: address(asset),
      namePrefix: \u0027name\u0027,
      symbolPrefix: \u0027symbol\u0027,
      maxTotalSupply: type(uint128).max,
      annualInterestBips: 1000,
      delinquencyFeeBips: 1000,
      withdrawalBatchDuration: 10000,
      reserveRatioBips: 10000,
      delinquencyGracePeriod: 10000,
      hooks: EmptyHooksConfig.setHooksAddress(address(hooksInstance))
    });
    //@audit-info borrower deploy a market hooked by a FixedTermLoanHooks hookInstance
    address market = hooksFactory.deployMarket(
      parameters,
      abi.encode(block.timestamp + (365 days)),
      bytes32(uint(1)),
      address(0),
      0
    );
    vm.stopPrank();
    //@audit-info lenders can only withdraw their asset one year later
    assertEq(FixedTermLoanHooks(hooksInstance).getHookedMarket(market).fixedTermEndTime, block.timestamp + (365 days));
    //@audit-info alice deposit 50K asset into market
    vm.startPrank(alice);
    asset.approve(market, type(uint).max);
    WildcatMarket(market).depositUpTo(50_000e18);
    vm.stopPrank();
    //@audit-info borrower close market in advance
    vm.prank(borrower);
    WildcatMarket(market).closeMarket();
    //@audit-info the market is closed
    assertTrue(WildcatMarket(market).isClosed());
    //@audit-info however, alice can not withdraw her asset due to the unexpired fixed term.
    vm.expectRevert(FixedTermLoanHooks.WithdrawBeforeTermEnd.selector);
    vm.prank(alice);
    WildcatMarket(market).queueFullWithdrawal();
  }
\u0060\u0060\u0060
## Tools Used
Manual review
## Recommended Mitigation Steps
When a market hooked by a fixed-term hook is closed, \u0060fixedTermEndTime\u0060 should be set to \u0060block.timestamp\u0060 if it has not yet elapsed:
\u0060\u0060\u0060diff
  constructor(address _deployer, bytes memory /* args */) IHooks() {
    borrower = _deployer;
    // Allow deployer to grant roles with no expiry
    _roleProviders[_deployer] = encodeRoleProvider(
      type(uint32).max,
      _deployer,
      NotPullProviderIndex
    );
    HooksConfig optionalFlags = encodeHooksConfig({
      hooksAddress: address(0),
      useOnDeposit: true,
      useOnQueueWithdrawal: false,
      useOnExecuteWithdrawal: false,
      useOnTransfer: true,
      useOnBorrow: false,
      useOnRepay: false,
      useOnCloseMarket: false,
      useOnNukeFromOrbit: false,
      useOnSetMaxTotalSupply: false,
      useOnSetAnnualInterestAndReserveRatioBips: false,
      useOnSetProtocolFeeBips: false
    });
    HooksConfig requiredFlags = EmptyHooksConfig
      .setFlag(Bit_Enabled_SetAnnualInterestAndReserveRatioBips)
+     .setFlag(Bit_Enabled_CloseMarket);
      .setFlag(Bit_Enabled_QueueWithdrawal);
    config = encodeHooksDeploymentConfig(optionalFlags, requiredFlags);
  }
\u0060\u0060\u0060
\u0060\u0060\u0060diff
  function onCloseMarket(
    MarketState calldata /* state */,
    bytes calldata /* hooksData */
- ) external override {}
+ ) external override {
+   HookedMarket memory market = _hookedMarkets[msg.sender];
+   if (!market.isHooked) revert NotHookedMarket();
+   if (market.fixedTermEndTime > block.timestamp) {
+     _hookedMarkets[msg.sender].fixedTermEndTime = uint32(block.timestamp);
+   }
+ }
\u0060\u0060\u0060


## Assessed type

Timing
