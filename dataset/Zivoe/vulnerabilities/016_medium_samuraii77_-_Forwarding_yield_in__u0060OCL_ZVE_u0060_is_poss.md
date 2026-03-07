# samuraii77 - Forwarding yield in \u0060OCL_ZVE\u0060 is possible a lot more often than the enforced 30 days

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** OCL_ZVE, forwardYield, cybersecurity, vulnerability, block.timestamp, nextYieldDistribution, require statement, function call, 30 days, pushToLockerMulti, fetchBasis, pool setup, pairAsset, ZVE, pool address, poolTotalSupply, division by zero, impact, proof of concept, manual review

---

samuraii77

medium

# Forwarding yield in \u0060OCL_ZVE\u0060 is possible a lot more often than the enforced 30 days

## Summary
Calling \u0060OCL_ZVE::forwardYield()\u0060 is supposed to only be possible every 30 days however in reality, it is possible to call the function a lot more often.

## Vulnerability Detail
The \u0060require\u0060 statement in \u0060OCL_ZVE::forwardYield()\u0060 enforces that the function should only be callable when \u0060block.timestamp\u0060 is of larger value than the value of \u0060nextYieldDistribution\u0060
\u0060\u0060\u0060solidity
    function forwardYield() external {
        if (IZivoeGlobals_OCL_ZVE(GBL).isKeeper(_msgSender())) {
            require(
                block.timestamp > nextYieldDistribution - 12 hours, 
                "OCL_ZVE::forwardYield() block.timestamp <= nextYieldDistribution - 12 hours"
            );
        }
        else {
            require(
                block.timestamp > nextYieldDistribution, 
                "OCL_ZVE::forwardYield() block.timestamp <= nextYieldDistribution"
            );
        }

        (uint256 amount, uint256 lp) = fetchBasis();
        if (amount > basis) { _forwardYield(amount, lp); }
        (basis,) = fetchBasis();
        nextYieldDistribution += 30 days;
    }
\u0060\u0060\u0060
Then, at the end of the function, \u0060nextYieldDistribution\u0060 is incremented by 30 days making the function supposedly not callable for another 30 days. However, there is a vulnerability that allows \u0060OCL_ZVE::forwardYield()\u0060 to be called a lot more times.

Upon calling the \u0060OCL_ZVE::pushToLockerMulti()\u0060, the \u0060nextYieldDistribution\u0060 gets set to \u0060block.timestamp + 30 days\u0060 if its value is 0.
\u0060\u0060\u0060solidity
if (nextYieldDistribution == 0) { nextYieldDistribution = block.timestamp + 30 days; }
\u0060\u0060\u0060
If this is the way \u0060nextYieldDistribution\u0060 gets its first value, then there will not be an issue. However, if \u0060OCL_ZVE::forwardYield()\u0060 is called beforehand, then \u0060nextYieldDistribution\u0060 will be set to \u00600 += 30 days\u0060 which equals \u006030 days\u0060 making its value a lot less than the value of \u0060block.timestamp\u0060 resulting in people being able to call \u0060OCL_ZVE::forwardYield()\u0060 at will all the way until \u0060nextYieldDistribution\u0060 gets incremented all the way to \u0060block.timestamp\u0060.

Calling \u0060OCL_ZVE::forwardYield()\u0060 before any other function is possible and requires just 1 simple circumstance to be a fact.

Imagine the following scenario:
1. \u0060OCL_ZVE::forwardYield()\u0060 is called
2. The \u0060if\u0060 statement passes as \u0060block.timestamp\u0060 is larger than \u0060nextYieldDistribution\u0060, the value of which is the default value of 0
3. \u0060OCL_ZVE::fetchBasis()\u0060 gets called
\u0060\u0060\u0060solidity
function fetchBasis() public view returns (uint256 amount, uint256 lp) {
        address pool = IFactory_OCL_ZVE(factory).getPair(pairAsset, IZivoeGlobals_OCL_ZVE(GBL).ZVE());
        uint256 pairAssetBalance = IERC20(pairAsset).balanceOf(pool);
        uint256 poolTotalSupply = IERC20(pool).totalSupply();
        lp = IERC20(pool).balanceOf(address(this));
        amount = lp * pairAssetBalance / poolTotalSupply;
    } 
\u0060\u0060\u0060
4. As long as there is a pool setup for \u0060pairAsset\u0060 and \u0060ZVE\u0060, the vulnerability will take place
5. Pool gets the value of the pool address
6. The only thing which has to pass here is \u0060poolTotalSupply\u0060 not being 0 as division by 0 is not possible
7. That successfully passes as there is already a setup pool for \u0060pairAsset\u0060 and \u0060ZVE\u0060
8. Then, we get back to the \u0060OCL_ZVE::forwardYield()\u0060 function
9. \u0060if(amount > basis)\u0060 does not pass as both values are 0
10. On the last line, \u0060nextYieldDistribution\u0060 gets set to \u006030 days\u0060 making the \u0060OCL_ZVE::forwardYield()\u0060 function callable again and again

## Impact
\u0060OCL_ZVE::forwardYield()\u0060 is callable over and over again even though it is only supposed to be called every 30 days

## Proof Of Concept
Paste the following test into \u0060Test_OCL_ZVE.sol\u0060:
\u0060\u0060\u0060solidity
function testCanForwardYieldALot() public {
        address UNIV2_ROUTER = OCL_ZVE_UNIV2_DAI.router();
        deal(DAI, address(this), 10000);

        IERC20(DAI).safeApprove(UNIV2_ROUTER, 10000);
        IERC20(ZVE).safeApprove(UNIV2_ROUTER, 1001);

        IUniswapV2Router01(UNIV2_ROUTER).addLiquidity(address(DAI), address(ZVE), 10000, 1001, 0, 0, address(this), block.timestamp);

        uint256 count;
        while (block.timestamp > OCL_ZVE_UNIV2_DAI.nextYieldDistribution()) {
            OCL_ZVE_UNIV2_DAI.forwardYield();
            count++;
        }

        console.log(count);
    }
\u0060\u0060\u0060

## Code Snippet
https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L186
https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/lockers/OCL/OCL_ZVE.sol#L287-L305

## Tool used

Manual Review

## Recommendation
Do not allow \u0060OCL_ZVE::forwardYield()\u0060 to be called whenever the value of \u0060nextYieldDistribution\u0060 is equal to 0. 
Also, another option is to set \u0060nextYieldDistribution\u0060 to \u0060block.timestamp + 30 days\u0060 instead of just incrementing it by \u006030 days\u0060.

