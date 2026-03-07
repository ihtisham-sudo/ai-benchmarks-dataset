# Issue H-4: Liquidity is incorrectly calculated during addLiquidity() for V3AMO, causing DoS.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** liquidity, addLiquidity, V3AMO, DoS, Uniswap V3, attack, LP position, Boost tokens, USD tokens, minting, calculation, pool, tickLower, tickUpper, liquidity calculation, mintSellFarm, impermanent loss, pre-conditions, mitigation, PoC

---

# Issue H-4: Liquidity is incorrectly calculated during addLiquidity() for V3AMO, causing DoS.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-axion-judging/issues/280)  
Found by: 0x37, pkqs90, s1ce, spark1  

## Summary  
Solidly V3 has the same liquidity calculation as Uniswap V3. Currently, when adding liquidity, the liquidity calculation is wrong, and may lead to DoS in some cases.

## Root Cause  
When calling \u0060addLiquidity\u0060, the amount of liquidity that is supposed to add is calculated by 

\u0060\u0060\u0060solidity
liquidity = (usdAmount * currentLiquidity) / IERC20Upgradeable(usd).balanceOf(pool);
\u0060\u0060\u0060

This is incorrect in the terms of Uniswap V3, because there may be multiple \u0060tickLower\u0060/\u0060tickUpper\u0060 positions covering the current tick. Also, since anyone can add a LP position to the pool, so attackers can easily DoS this function. 

Consider an attacker adds an unbalanced LP position that deposits a lot of Boost tokens but doesn\u0027t deposit USD tokens. This would increase the total liquidity, and inflate the amount of liquidity calculated in the above formula, which would lead to an increase of USD tokens required to mint the liquidity. When the amount of required USD token is above the approved \u0060usdAmount\u0060, the liquidity minting would fail. 

See the following PoC section for a more detailed example.

\u0060\u0060\u0060solidity
function _addLiquidity(
    uint256 usdAmount,
    uint256 minBoostSpend,
    uint256 minUsdSpend,
    uint256 deadline
) internal override returns (uint256 boostSpent, uint256 usdSpent, uint256 liquidity) {
    // Calculate the amount of BOOST to mint based on the usdAmount and boostMultiplier
    uint256 boostAmount = (toBoostAmount(usdAmount) * boostMultiplier) / FACTOR;
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Mint the specified amount of BOOST tokens to this contract\u0027s address
IMinter(boostMinter).protocolMint(address(this), boostAmount);
// Approve the transfer of BOOST and USD tokens to the pool
IERC20Upgradeable(boost).approve(pool, boostAmount);
IERC20Upgradeable(usd).approve(pool, usdAmount);
(uint256 amount0Min, uint256 amount1Min) = sortAmounts(minBoostSpend, minUsdSpend);
uint128 currentLiquidity = ISolidlyV3Pool(pool).liquidity();
liquidity = (usdAmount * currentLiquidity) / IERC20Upgradeable(usd).balanceOf(pool);
// Add liquidity to the BOOST-USD pool within the specified tick range
(uint256 amount0, uint256 amount1) = ISolidlyV3Pool(pool).mint(
    address(this),
    tickLower,
    tickUpper,
    uint128(liquidity),
    amount0Min,
    amount1Min,
    deadline
);
...
\u0060\u0060\u0060

- [Link to Code](https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/SolidlyV3AMO.sol#L186)

**Internal Pre-conditions**  
N/A

**External Pre-conditions**  
N/A

**Attack Path**  
Attacker can break addLiquidity function by depositing LP.
## Impact

Attackers can deposit LP to make add liquidity fail, which also makes mintSellFarm() fail. This is an important feature to keep Boost/USD pegged, thus a high severity issue. This is basically no cost for attackers since the Boost/USD will always go back to 1:1 so no impermanent loss is incurred.
## PoC

Add the following code in SolidlyV3AMO.test.ts. It does the following:
1. Add unbalanced liquidity so that total liquidity increases, but USD.balanceOf(pool) does not increase.
2. Mint some USD to SolidlyV3AMO for adding liquidity.
3. Try to add liquidity, but it fails due to incorrect liquidity calculation (tries to add too much liquidity for not enough USD tokens).

\u0060\u0060\u0060javascript
it("Should execute addLiquidity successfully", async function() {
  // Step 1: Add unbalanced liquidity so that total liquidity increases, but
  // USD.balanceOf(pool) does not increase.
  {
    // -276325 is the current slot0 tick.
    console.log(await pool.slot0());
    await boost.connect(boostMinter).mint(admin.address, boostDesired * 100n);
    await testUSD.connect(boostMinter).mint(admin.address, usdDesired * 100n);
    await boost.approve(poolAddress, boostDesired * 100n);
    await testUSD.approve(poolAddress, usdDesired * 100n);
    console.log(await boost.balanceOf(admin.address));
    console.log(await testUSD.balanceOf(admin.address));
    await pool.mint(
      amoAddress,
      -276325 - 10,
      tickUpper,
      liquidity * 3n,
      0,
      0,
      deadline
    );
    console.log(await boost.balanceOf(admin.address));
    console.log(await testUSD.balanceOf(admin.address));
  }
  // Step 2: Mint some USD to SolidlyV3AMO for adding liquidity.
  await testUSD.connect(admin).mint(amoAddress, ethers.parseUnits("1000", 6));
  const usdBalance = await testUSD.balanceOf(amoAddress);
  // Step 3: Add liquidity fails due to incorrect liquidity calculation.
});
\u0060\u0060\u0060
## Mitigation

UsetheUniswapV3libraryforcalculatingliquidity: https://github.com/Uniswap/v3-periphery/blob/main/contracts/libraries/LiquidityAmounts.sol#L56

\u0060\u0060\u0060solidity
function getLiquidityForAmounts(
    uint160 sqrtRatioX96,
    uint160 sqrtRatioAX96,
    uint160 sqrtRatioBX96,
    uint256 amount0,
    uint256 amount1
) internal pure returns (uint128 liquidity) {
    if (sqrtRatioAX96 > sqrtRatioBX96) (sqrtRatioAX96, sqrtRatioBX96) =
        (sqrtRatioBX96, sqrtRatioAX96);
    if (sqrtRatioX96 <= sqrtRatioAX96) {
        liquidity = getLiquidityForAmount0(sqrtRatioAX96, sqrtRatioBX96, amount0);
    } else if (sqrtRatioX96 < sqrtRatioBX96) {
        uint128 liquidity0 = getLiquidityForAmount0(sqrtRatioX96, sqrtRatioBX96, amount0);
        uint128 liquidity1 = getLiquidityForAmount1(sqrtRatioAX96, sqrtRatioX96, amount1);
        liquidity = liquidity0 < liquidity1 ? liquidity0 : liquidity1;
    } else {
        liquidity = getLiquidityForAmount1(sqrtRatioAX96, sqrtRatioBX96, amount1);
    }
}
\u0060\u0060\u0060
## Discussion

sherlock-admin2

TheprotocolteamfixedthisissueinthefollowingPRs/commits:
https://github.com/AXION-MONEY/liquidity-amo/pull/12
