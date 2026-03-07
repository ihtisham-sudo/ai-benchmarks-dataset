# Issue H-3: V3AMO integration with V3 does not collect LP fees when burning liquidity.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** SolidlyV3AMO, liquidity, LP fees, burn liquidity, unfarmBuyBurn, integration, Uniswap V3, RewardsDistributor, merkel proof, fees distribution, function, collect fees, position, contract, protocol, audit, fork, implementation, update, liquidityDelta

---

# Issue H-3: V3AMO integration with V3 does not collect LP fees when burning liquidity.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-axion-judging/issues/242)  
Found by: pkqs90  

## Summary  
SolidlyV3AMO supplies liquidity for the Boost-USD pool. When users call unfarmBuyBurn to burn liquidity from Solidly V3 AMO, the LP fees should be collected as well. However, the current integration does not correctly collect fees for Solidly V3, and the fees are stuck forever.  

## Root Cause  
Let\u0027s see the Solidly V3 implementation for burnAndCollect() function.  
[View Code](https://ftmscan.com/address/0x54a571D91A5F8beD1D56fC09756F1714F0cd8aD9#code)  
(This is taken from notion docs.)  

Even though Solidly V3 is a fork of Uniswap V3, there is a significant difference. In Uniswap V3, the liquidity fees are calculated within the Pool, and can be collected via the Pool. However, in Solidly V3, the fees are not updated at all (In the following code, where the fees should be updated in Position.sol as done by Uniswap V3, you can see the fee update code is fully removed).  

Also, according to the Solidly V3 docs [here](https://docs.solidly.com/v3/rewards-distributor), all fees (and bribes) distribution have been moved into the RewardsDistributor.sol contract, and distributed via merkel proof. This means calling burnAndCollect() does not allow us to collect the LP fees anymore, and that we need to call a separate function for Solidly V3 AMO in order to retrieve the LP fees.  

\u0060\u0060\u0060solidity
function burnAndCollect(
    address recipient,
    int24 tickLower,
    int24 tickUpper,
    uint128 amountToBurn,
    uint128 amount0ToCollect,
    uint128 amount1ToCollect
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
external
override
returns (uint256 amount0FromBurn, uint256 amount1FromBurn, uint128 amount0Collected, uint128 amount1Collected)
{
    (amount0FromBurn, amount1FromBurn) = _burn(tickLower, tickUpper, amountToBurn);
    (amount0Collected, amount1Collected) = _collect(
        recipient,
        tickLower,
        tickUpper,
        amount0ToCollect,
        amount1ToCollect
    );
}

function _burn(
    int24 tickLower,
    int24 tickUpper,
    uint128 amount
) private lock returns (uint256 amount0, uint256 amount1) {
    (Position.Info storage position, int256 amount0Int, int256 amount1Int) =
        _modifyPosition(
            ModifyPositionParams({
                owner: msg.sender,
                tickLower: tickLower,
                tickUpper: tickUpper,
                liquidityDelta: -int256(amount).toInt128()
            })
        );
    amount0 = uint256(-amount0Int);
    amount1 = uint256(-amount1Int);
    if (amount0 > 0 || amount1 > 0) {
        (position.tokensOwed0, position.tokensOwed1) = (
            position.tokensOwed0 + uint128(amount0),
            position.tokensOwed1 + uint128(amount1)
        );
    }
    emit Burn(msg.sender, tickLower, tickUpper, amount, amount0, amount1);
}

function _modifyPosition(
    ModifyPositionParams memory params
) private returns (Position.Info storage position, int256 amount0, int256 amount1) {
    checkTicks(params.tickLower, params.tickUpper);
    Slot0 memory _slot0 = slot0; // SLOAD for gas optimization
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
position = _updatePosition(params.owner, params.tickLower,
             params.tickUpper, params.liquidityDelta);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function _updatePosition(
    address owner,
    int24 tickLower,
    int24 tickUpper,
    int128 liquidityDelta
) private returns (Position.Info storage position) {
    ...
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
position.update(liquidityDelta);
\u0060\u0060\u0060
SolidlyV3Position.sol
\u0060\u0060\u0060solidity
/// @notice Updates the liquidity amount associated with a user\u0027s position
/// @param self The individual position to update
/// @param liquidityDelta The change in pool liquidity as a result of the position
update
function update(Info storage self, int128 liquidityDelta) internal {
    // @audit-note: Fees should be accumulated in UniswapV3. But in SolidlyV3, this
    is removed.
    if (liquidityDelta != 0) {
        self.liquidity = LiquidityMath.addDelta(self.liquidity, liquidityDelta);
    }
}
\u0060\u0060\u0060
SolidlyV3AMOimplementation
\u0060\u0060\u0060solidity
function _unfarmBuyBurn(
    uint256 liquidity,
    uint256 minBoostRemove,
    uint256 minUsdRemove,
    uint256 minBoostAmountOut,
    uint256 deadline
)
    internal
    override
    returns (uint256 boostRemoved, uint256 usdRemoved, uint256 usdAmountIn,
    uint256 boostAmountOut)
{
    (uint256 amount0Min, uint256 amount1Min) = sortAmounts(minBoostRemove,
    minUsdRemove);
    // Remove liquidity and store the amounts of USD and BOOST tokens received
    (
        uint256 amount0FromBurn,
        uint256 amount1FromBurn,
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint128 amount0Collected,
uint128 amount1Collected
) = ISolidlyV3Pool(pool).burnAndCollect(
    address(this),
    tickLower,
    tickUpper,
    uint128(liquidity),
    amount0Min,
    amount1Min,
    type(uint128).max,
    type(uint128).max,
    deadline
);
\u0060\u0060\u0060

- https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/SolidlyV3AMO.sol#L235

## Internal pre-conditions
N/A

## External pre-conditions
N/A

## Attack Path
N/A

## Impact
LP Fees are not retrievable for SolidlyV3AMO.

## PoC
N/A

## Mitigation
Add a function to call the RewardsDistributor.sol for SolidlyV3 to retrieve the LP fees. This can be an independent function, since not all SolidlyV3 forks may support this feature.
## Discussion

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/AXION-MONEY/liquidity-amo/pull/10
