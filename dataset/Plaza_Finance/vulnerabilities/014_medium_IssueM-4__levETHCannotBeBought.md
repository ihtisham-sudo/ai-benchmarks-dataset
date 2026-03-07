# IssueM-4: levETHCannotBeBought

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** levETH, contract, sale, supply, price, calculation, useless, token, redeem, burn, leverage, collateral, threshold, functionality, error, check, mechanism, core, audit, failure

---

# IssueM-4: levETHCannotBeBought

Source: [GitHub Issue #333](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/333)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.

Found by: KupiaSec, PeterSR, almurhasan, dobrevaleri, future, sl1

If all levETH owners sell their levETH, no one will be able to buy levETH.

The current implementation allows for the sale of all levETH without checking if the total supply has reached zero. This results in a scenario where the price cannot be calculated, making the contract effectively useless.

\u0060\u0060\u0060solidity
// Pool.sol
function _redeem(
    ...) private returns(uint256) {
    ...
    // Burn derivative tokens
    if (tokenType == TokenType.BOND) {
        bondToken.burn(msg.sender, depositAmount);
    } else {
        lToken.burn(msg.sender, depositAmount);
    }
}
\u0060\u0060\u0060

N/A

N/A
N/A

When the levSupply reaches zero, the contract lacks a mechanism to calculate the price of levETH. This results in an inability for users to purchase levETH.  
[Source Code](https://github.com/sherlock-audit/2024-12-plaza-finance/tree/main/plaza-evm/src/Pool.sol#L331-L336)

\u0060\u0060\u0060solidity
function getCreateAmount(
...) public pure returns(uint256) {
    ...
    if (collateralLevel <= COLLATERAL_THRESHOLD) {
        if (tokenType == TokenType.LEVERAGE && assetSupply == 0) {
            revert ZeroLeverageSupply();
        }
        creationRate = (tvl * multiplier) / assetSupply;
    } else if (tokenType == TokenType.LEVERAGE) {
        if (assetSupply == 0) {
            revert ZeroLeverageSupply();
        }
        uint256 adjustedValue = tvl - (BOND_TARGET_PRICE * bondSupply);
        creationRate = (adjustedValue * PRECISION) / assetSupply;
    }
    return ((depositAmount * ethPrice * PRECISION) / creationRate).toBaseUnit(oracleDecimals);
}
\u0060\u0060\u0060

In Sherlock docs:  
V. How to identify a medium issue: 2. Breaks core contract functionality, rendering the contract useless or leading to loss of funds that\u0027s relevant to the affected party.  
The known issue 3.20: Missing a zero-value check for assetSupply refers to the lack of a mechanism for price calculation when the amount of levETH is zero. The root cause of this report is the absence of a check during the redemption process. Therefore, these two issues are not duplicates.

The functionality of the core contract is compromised, rendering the contract useless.

\u0060\u0060\u0060solidity
function _redeem(
    ...) private returns(uint256) {
    ...
    // Burn derivative tokens
    if (tokenType == TokenType.BOND) {
        bondToken.burn(msg.sender, depositAmount);
    } else {
        require(depositAmount < lToken.totalbalance(),"");
        lToken.burn(msg.sender, depositAmount);
    }
}
\u0060\u0060\u0060
## TestCode

\u0060\u0060\u0060solidity
function testCreateRedeemWithFees() public {
    vm.startPrank(governance);
    // Create a pool with 2% fee
    params.fee = 20000; // 2% fee (1000000 precision)
    params.feeBeneficiary = address(0x942);
    // Mint and approve reserve tokens
    Token rToken = Token(params.reserveToken);
    rToken.mint(governance, 120 ether);
    rToken.approve(address(poolFactory), 120 ether);
    Pool pool = Pool(poolFactory.createPool(params, 120 ether, 3000 ether, 200 ether,
    "", "", "", "", false));
    LeverageToken lToken = LeverageToken(pool.lToken());
    lToken.transfer(user, lToken.balanceOf(governance));
    vm.stopPrank();
    // User creates leverage tokens
    vm.startPrank(user);
    console2.log("Before redeem");
    pool.redeem(Pool.TokenType.LEVERAGE, lToken.balanceOf(user), 0);
    console2.log(" After redeem");
    console2.log("Before create");
    pool.create(Pool.TokenType.LEVERAGE, 10 ether, 0);
    console2.log(" After Create");
    vm.stopPrank();
    // Reset state
    rToken.burn(user, rToken.balanceOf(user));
    rToken.burn(address(pool), rToken.balanceOf(address(pool)));
}
\u0060\u0060\u0060

forgetest--match-test”testCreateRedeemWithFees”-vv  
Result:  
[FAIL: ZeroLeverageSupply()] testCreateRedeemWithFees() (gas: 2054536) Logs: Before redeem After redeem Before create
