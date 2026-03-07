# BiasedMerc - OCL_ZVE::pushToLockerMulti() will revert due to incorrect assert() statements when interacting with UniswapV2

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** OCL_ZVE, pushToLockerMulti, UniswapV2, Sushi, liquidity, allowance, assert, revert, core functionality, contract, minimum liquidity, amountADesired, amountBDesired, amountAMin, amountBMin, transfer, addLiquidity, DAO, vulnerability, manual review

---

BiasedMerc

medium

# OCL_ZVE::pushToLockerMulti() will revert due to incorrect assert() statements when interacting with UniswapV2

## Summary

\u0060OCL_ZVE::pushToLockerMulti()\u0060 verifies that the allowances for both tokens is 0 after providing liquidity to UniswapV2 or Sushi routers, however there is a high likelihood that one allowance will not be 0, due to setting a 90% minimum liquidity provided value. Therefore, the function will revert most of the time breaking core functionality of the locker, making the contract useless.

## Vulnerability Detail

The DAO can add liquidity to UniswapV2 or Sushi through \u0060OCL_ZVE::pushToLockerMulti()\u0060 function, where \u0060addLiquidity\u0060 is called on \u0060router\u0060:

[OCL_ZVE.sol#L198C78-L198](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L198)
\u0060\u0060\u0060solidity
IRouter_OCL_ZVE(router).addLiquidity(
\u0060\u0060\u0060

[OCL_ZVE.sol#L90](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L90)
\u0060\u0060\u0060solidity
address public immutable router;            /// @dev Address for the Router (Uniswap v2 or Sushi).
\u0060\u0060\u0060
The router is intended to be Uniswap v2 or Sushi (Sushi router uses the same code as Uniswap v2 [0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f](https://etherscan.io/address/0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f#code)). 

[UniswapV2Router02::addLiquidity](https://github.com/Uniswap/v2-periphery/blob/master/contracts/UniswapV2Router02.sol#L61-L76)
\u0060\u0060\u0060solidity
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external virtual override ensure(deadline) returns (uint amountA, uint amountB, uint liquidity) {
        (amountA, amountB) = _addLiquidity(tokenA, tokenB, amountADesired, amountBDesired, amountAMin, amountBMin);
        address pair = UniswapV2Library.pairFor(factory, tokenA, tokenB);
        TransferHelper.safeTransferFrom(tokenA, msg.sender, pair, amountA);
        TransferHelper.safeTransferFrom(tokenB, msg.sender, pair, amountB);
        liquidity = IUniswapV2Pair(pair).mint(to);
    }
\u0060\u0060\u0060

When calling the function 4 variables relevant to this issue are passed:
\u0060amountADesired\u0060 and \u0060amountBDesired\u0060 are the ideal amount of tokens we want to deposit, whilst
\u0060amountAMin\u0060 and \u0060amountBMin\u0060 are the minimum amounts of tokens we want to deposit. 
Meaning the true amount that will deposit be deposited for each token will be inbetween those 2 values, e.g:
\u0060amountAMin <= amountA <= amountADesired\u0060.
Where \u0060amountA\u0060 is how much of \u0060tokenA\u0060 will be transfered.

The transfered amount are \u0060amountA\u0060 and \u0060amountB\u0060 which are calculated as follows:
[UniswapV2Router02::_addLiquidity](https://github.com/Uniswap/v2-periphery/blob/master/contracts/UniswapV2Router02.sol#L33-L60)
\u0060\u0060\u0060solidity
    function _addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin
    ) internal virtual returns (uint amountA, uint amountB) {
        // create the pair if it doesn\u0027t exist yet
        if (IUniswapV2Factory(factory).getPair(tokenA, tokenB) == address(0)) {
            IUniswapV2Factory(factory).createPair(tokenA, tokenB);
        }
        (uint reserveA, uint reserveB) = UniswapV2Library.getReserves(factory, tokenA, tokenB);
        if (reserveA == 0 && reserveB == 0) {
            (amountA, amountB) = (amountADesired, amountBDesired);
        } else {
            uint amountBOptimal = UniswapV2Library.quote(amountADesired, reserveA, reserveB);
            if (amountBOptimal <= amountBDesired) {
                require(amountBOptimal >= amountBMin, \u0027UniswapV2Router: INSUFFICIENT_B_AMOUNT\u0027);
                (amountA, amountB) = (amountADesired, amountBOptimal);
            } else {
                uint amountAOptimal = UniswapV2Library.quote(amountBDesired, reserveB, reserveA);
                assert(amountAOptimal <= amountADesired);
                require(amountAOptimal >= amountAMin, \u0027UniswapV2Router: INSUFFICIENT_A_AMOUNT\u0027);
                (amountA, amountB) = (amountAOptimal, amountBDesired);
            }
        }
    }
\u0060\u0060\u0060
\u0060UniswapV2Router02::_addLiquidity\u0060 receives a quote for how much of each token can be added and validates that the values fall within the \u0060amountAMin\u0060 and \u0060amountADesired\u0060 range. Unless the exactly correct amounts are passed as \u0060amountADesired\u0060 and \u0060amountBDesired\u0060 then the amount of one of the two tokens will be less than the desired amount.

Now lets look at how \u0060OCL_ZVE\u0060 interacts with the Uniswapv2 router:

[OCL_ZVE::addLiquidity](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L191-L209)
\u0060\u0060\u0060solidity
        // Router addLiquidity() endpoint.
        uint balPairAsset = IERC20(pairAsset).balanceOf(address(this));
        uint balZVE = IERC20(ZVE).balanceOf(address(this));
        IERC20(pairAsset).safeIncreaseAllowance(router, balPairAsset);
        IERC20(ZVE).safeIncreaseAllowance(router, balZVE);

        // Prevent volatility of greater than 10% in pool relative to amounts present.
        (uint256 depositedPairAsset, uint256 depositedZVE, uint256 minted) = IRouter_OCL_ZVE(router).addLiquidity(
            pairAsset, 
            ZVE, 
            balPairAsset,
            balZVE, 
            (balPairAsset * 9) / 10,
            (balZVE * 9) / 10, 
            address(this), block.timestamp + 14 days
        );
        emit LiquidityTokensMinted(minted, depositedZVE, depositedPairAsset);
        assert(IERC20(pairAsset).allowance(address(this), router) == 0);
        assert(IERC20(ZVE).allowance(address(this), router) == 0);
\u0060\u0060\u0060
The function first increases the allowances for both tokens to \u0060balPairAsset\u0060 and \u0060balZVE\u0060 respectively. 

When calling the router, \u0060balPairAsset\u0060 and \u0060valZVE\u0060 are provided as the desired amount of liquidity to add, however \u0060(balPairAsset * 9) / 10\u0060 and \u0060(balZVE * 9) / 10\u0060 are also passed as minimums for how much liquidity we want to add.

As the final transfered value will be between:
 \u0060(balPairAsset * 9) / 10 <= x <= balPairAsset\u0060
therefore the allowance after providing liquidity will be:
 \u00600 <= IERC20(pairAsset).allowance(address(this), router) <= balPairAsset - (balPairAsset * 9) / 10\u0060 
however the function expects the allowance to be 0 for both tokens after providing liquidity.
The same applies to the \u0060ZVE\u0060 allowance.

This means that in most cases one of the assert statements will not be met, leading to the add liquidity call to revert. This is unintended behaviour, as the function passed a \u006090%\u0060 minimum amount, however the allowance asserts do not take this into consideration.

## Impact

Calls to \u0060OCL_ZVE::pushToLockerMulti()\u0060 will revert a majority of the time, causing core functionality of providing liquidity through the locker to be broken.

## Code Snippet

[OCL_ZVE.sol#L198C78-L198](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L198)
[UniswapV2Router02.sol#L61-L76](https://github.com/Uniswap/v2-periphery/blob/master/contracts/UniswapV2Router02.sol#L61-L76)
[UniswapV2Router02.sol#L33-L60](https://github.com/Uniswap/v2-periphery/blob/master/contracts/UniswapV2Router02.sol#L33-L60)
[OCL_ZVE.sol#L191-L209](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L191-L209)

## Tool used

Manual Review

## Recommendation

The project wants to clear allowances after all transfers, therefore set the router allowance to 0 after providing liquidity using the returned value from the router:
\u0060\u0060\u0060diff
  (uint256 depositedPairAsset, uint256 depositedZVE, uint256 minted) = IRouter_OCL_ZVE(router).addLiquidity(
      pairAsset, 
      ZVE, 
      balPairAsset,
      balZVE, 
      (balPairAsset * 9) / 10,
      (balZVE * 9) / 10, 
      address(this), block.timestamp + 14 days
  );
  emit LiquidityTokensMinted(minted, depositedZVE, depositedPairAsset);
- assert(IERC20(pairAsset).allowance(address(this), router) == 0);
- assert(IERC20(ZVE).allowance(address(this), router) == 0);
+ uint256 pairAssetAllowanceLeft = balPairAsset - depositedPairAsset;
+ if (pairAssetAllowanceLeft > 0) {
+     IERC20(pairAsset).safeDecreaseAllowance(router, pairAssetAllowanceLeft);
+ }
+ uint256 zveAllowanceLeft = balZVE - depositedZVE;
+ if (zveAllowanceLeft > 0) {
+     IERC20(ZVE).safeDecreaseAllowance(router, zveAllowanceLeft);
+ }
\u0060\u0060\u0060
This will remove the left over allowance after providing liquidity, ensuring the allowance is 0.
