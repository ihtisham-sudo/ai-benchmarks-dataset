# Inconsistency across multiple repaying functions causing lender to pay extra fees.

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, impact, inconsistency, functions, borrower, extra fees, proof of concept, repay, repayAndProcessUnpaidWithdrawalBatches, closeMarket, deposit, repayOutstandingDebt, repayDelinquentDebt, state fetching, funds pulling, manual review, mitigation steps, refund, context

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/market/WildcatMarket.sol#L226


# Vulnerability details

## Impact
Inconsistency across multiple functions can cause borrower to pay extra fees

## Proof of Concept
Within functions such as \u0060repay\u0060 and \u0060repayAndProcessUnpaidWithdrawalBatches\u0060, funds are first pulled from the user in order to use them towards the currently expired, but not yet unpaid batch, and then the updated state is fetched.

\u0060\u0060\u0060solidity
  function repay(uint256 amount) external nonReentrant sphereXGuardExternal {
    if (amount == 0) revert_NullRepayAmount();

    asset.safeTransferFrom(msg.sender, address(this), amount);
    emit_DebtRepaid(msg.sender, amount);

    MarketState memory state = _getUpdatedState();
    if (state.isClosed) revert_RepayToClosedMarket();

    // Execute repay hook if enabled
    hooks.onRepay(amount, state, _runtimeConstant(0x24));

    _writeState(state);
  }
\u0060\u0060\u0060

However, this is not true for functions such as \u0060closeMarket\u0060, \u0060deposit\u0060, \u0060repayOutstandingDebt\u0060 and \u0060repayDelinquentDebt\u0060, where the state is first fetched and only then funds are pulled, forcing borrower into higher fees.

\u0060\u0060\u0060solidity
  function closeMarket() external onlyBorrower nonReentrant sphereXGuardExternal {
    MarketState memory state = _getUpdatedState();    // fetches updated state

    if (state.isClosed) revert_MarketAlreadyClosed();

    uint256 currentlyHeld = totalAssets();
    uint256 totalDebts = state.totalDebts();
    if (currentlyHeld < totalDebts) {
      // Transfer remaining debts from borrower
      uint256 remainingDebt = totalDebts - currentlyHeld;
      _repay(state, remainingDebt, 0x04);             // pulls user funds
      currentlyHeld += remainingDebt;
\u0060\u0060\u0060

This inconsistency will cause borrowers to pay extra fees which they otherwise wouldn\u0027t.

PoC:
\u0060\u0060\u0060solidity
  function test_inconsistencyIssue() external {
      parameters.annualInterestBips = 3650;
      _deposit(alice, 1e18);
      uint256 borrowAmount = market.borrowableAssets();
      vm.prank(borrower);
      market.borrow(borrowAmount);
      vm.prank(alice);
      market.queueFullWithdrawal();
      fastForward(52 weeks);

      asset.mint(borrower, 10e18);
      vm.startPrank(borrower);
      asset.approve(address(market), 10e18);
      uint256 initBalance = asset.balanceOf(borrower); 

      asset.transfer(address(market), 10e18);
      market.closeMarket();
      uint256 finalBalance = asset.balanceOf(borrower);
      uint256 paid = initBalance - finalBalance;
      console.log(paid);

  } 

    function test_inconsistencyIssue2() external {
      parameters.annualInterestBips = 3650;
      _deposit(alice, 1e18);
      uint256 borrowAmount = market.borrowableAssets();
      vm.prank(borrower);
      market.borrow(borrowAmount);
      vm.prank(alice);
      market.queueFullWithdrawal();
      fastForward(52 weeks);

      asset.mint(borrower, 10e18);
      vm.startPrank(borrower);
      asset.approve(address(market), 10e18);
      uint256 initBalance = asset.balanceOf(borrower); 


      market.closeMarket();
      uint256 finalBalance = asset.balanceOf(borrower);
      uint256 paid = initBalance - finalBalance;
      console.log(paid);

  }
\u0060\u0060\u0060

and the logs:
\u0060\u0060\u0060
Ran 2 tests for test/market/WildcatMarket.t.sol:WildcatMarketTest
[PASS] test_inconsistencyIssue() (gas: 656338)
Logs:
  800455200405885337

[PASS] test_inconsistencyIssue2() (gas: 680537)
Logs:
  967625143234433533
\u0060\u0060\u0060

## Tools Used
Manual review

## Recommended Mitigation Steps
Always pull the funds first and refund later if needed.


## Assessed type

Context
