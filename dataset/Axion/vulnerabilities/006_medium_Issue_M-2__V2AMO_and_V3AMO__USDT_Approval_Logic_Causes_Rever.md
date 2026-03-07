# Issue M-2: V2AMO and V3AMO: USDT Approval Logic Causes Reversion

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** USDT, approval, reversion, EVM, smart contracts, OpenZeppelin, IERC20Upgradeable, approve, liquidity, farming, Solidly, V2AMO, V3AMO, boost, USD, tokens, pool, swap, error, implementation

---

# Issue M-2: V2AMO and V3AMO: USDT Approval Logic Causes Reversion

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-axion-judging/issues/47)  
Found by: 0x37, Naresh, RadCet, ZanyBonzy, unnamed, wellbyt3

## Summary

As the documentation mentions, the contracts are designed to be compatible with any EVM chain and support USDT:
The smart contracts can potentially be implemented on any full-EVM chain. USDT is a generic name for a reference stablecoin paired with BOOST in the AMO (USDC and USDT are the first natural candidates). However, both the Solidly V2AMO and Solidly V3AMO contracts will not work with USDT, as they will revert during the \u0060_addLiquidity()\u0060 and \u0060_unfarmBuyBurn()\u0060 functions.

## Root Cause

Both Solidly V2AMO and Solidly V3AMO use OpenZeppelin\u0027s \u0060IERC20Upgradeable\u0060 interface, which expects a boolean return value when calling the \u0060approve()\u0060 function. However, USDT’s implementation of the \u0060approve()\u0060 function does not return a boolean value, which causes the contract to revert during execution.

\u0060\u0060\u0060solidity
/**
 * @dev Approve the passed address to spend the specified amount of tokens on behalf
 * of msg.sender.
 * @param _spender The address which will spend the funds.
 * @param _value The amount of tokens to be spent.
 */
function approve(address _spender, uint _value) public onlyPayloadSize(2 * 32) {
\u0060\u0060\u0060

The functions \u0060_addLiquidity()\u0060 and \u0060_unfarmBuyBurn()\u0060 in both contracts expect a boolean return value, causing them to revert when interacting with USDT.

\u0060\u0060\u0060solidity
example SolidlyV3AMO::_addLiquidity and SolidlyV3AMO::_unfarmBuyBurn:
function _addLiquidity(uint256 usdAmount, uint256 minBoostSpend, uint256 minUsdSpend, uint256 deadline)
    internal
    override
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
returns (uint256 boostSpent, uint256 usdSpent, uint256 liquidity)
{
    //....
    // Approve the transfer of BOOST and USD tokens to the pool
    IERC20Upgradeable(boost).approve(pool, boostAmount);
    IERC20Upgradeable(usd).approve(pool, usdAmount);
    (uint256 amount0Min, uint256 amount1Min) = sortAmounts(minBoostSpend, minUsdSpend);
    uint128 currentLiquidity = ISolidlyV3Pool(pool).liquidity();
    liquidity = (usdAmount * currentLiquidity) / IERC20Upgradeable(usd).balanceOf(pool);
    // Add liquidity to the BOOST-USD pool within the specified tick range
    (uint256 amount0, uint256 amount1) = ISolidlyV3Pool(pool).mint(
        address(this), tickLower, tickUpper, uint128(liquidity), amount0Min, amount1Min, deadline
    );
    // Revoke approval from the pool
    IERC20Upgradeable(boost).approve(pool, 0);
    IERC20Upgradeable(usd).approve(pool, 0);
    //....
}

function _unfarmBuyBurn(
    uint256 liquidity,
    uint256 minBoostRemove,
    uint256 minUsdRemove,
    uint256 minBoostAmountOut,
    uint256 deadline
)
    internal
    override
    returns (uint256 boostRemoved, uint256 usdRemoved, uint256 usdAmountIn, uint256 boostAmountOut)
{
    //....
    // Approve the transfer of usd tokens to the pool
    IERC20Upgradeable(usd).approve(pool, usdRemoved);
    // Execute the swap and store the amounts of tokens involved
    (int256 amount0, int256 amount1) = ISolidlyV3Pool(pool).swap(
        address(this),
        boost > usd, // Determines if we are swapping USD for BOOST (true) or BOOST for USD (false)
\u0060\u0060\u0060
## SolidlyV2AMO::_addLiquidityandSolidlyV2AMO::_unfarmBuyBurn faces the same issue

## Internal pre-conditions
No response

## External pre-conditions
No response

## Attack Path
No response

## Impact
Adding liquidity and farming will fail due to a revert on USDT approvals

## Mitigation
Use safeApprove instead of approve

## Discussion
sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/AXION-MONEY/liquidity-amo/pull/5](https://github.com/AXION-MONEY/liquidity-amo/pull/5)
