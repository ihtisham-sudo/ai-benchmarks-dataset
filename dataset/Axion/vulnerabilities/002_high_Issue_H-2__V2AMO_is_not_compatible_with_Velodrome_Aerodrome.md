# Issue H-2: V2AMO is not compatible with Velodrome/Aerodrome

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** V2AMO, Velodrome, Aerodrome, Solidly, Dex, integration, Gauge, Router, getReward, interface, poolFor, swapExactTokensForTokens, tokens, address, factory, stable, contract, bug, implementation, compatibility

---

# Issue H-2: V2AMO is not compatible with Velodrome/Aerodrome

Source: [https://github.com/sherlock-audit/2024-10-axion-judging/issues/239](https://github.com/sherlock-audit/2024-10-axion-judging/issues/239)  
Found by: 0x37, Greese, KupiaSec, PNS, carrotsmuggler, pkqs90, y4y

## Summary

According to the docs, the Dex scope for Solidly V2 includes Velodrome/Aerodrome. We expect the Solidly V2 tech-implementation work with the “classic” pools on the following Dexes: Velodrome, Aerodrome, Thena, Equalizer (Fantom/Sonic/Base), Ramses and forks (legacy pools), Tokan. However, for Velodrome/Aerodrome implementations, the current Solidly V2 AMO is not compatible.

## Root Cause

There are two parts of integration with Velodrome/Aerodrome that are buggy:
1. Gauge
2. Router

Let\u0027s go through them one by one (Note, since Velodrome and Aerodrome have basically the same code, I will only post Aerodrome code):

1. Gauge The main difference is in the \u0060getReward()\u0060 function.  
   Aerodrome interface: [https://github.com/aerodrome-finance/contracts/blob/main/contracts/interfaces/IGauge.sol](https://github.com/aerodrome-finance/contracts/blob/main/contracts/interfaces/IGauge.sol)
   \u0060\u0060\u0060solidity
   interface IGauge {
       ...
       function getReward(address _account) external;
       ...
   }
   \u0060\u0060\u0060
   Solidly V2 AMO interface: [https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/interfaces/v2/IGauge.sol#L4](https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/interfaces/v2/IGauge.sol#L4)
\u0060\u0060\u0060solidity
interface IGauge {
    ...
    function getReward(address account, address[] memory tokens) external;
    function getReward(uint256 tokenId) external;
    function getReward() external;
    ...
}
\u0060\u0060\u0060

2. Router  Themaindifferenceis:
   1. AerodromeusespoolForinsteadofpairForwhenqueryingapool/pair.
   2. TheRoutestructisimplementeddifferently,andisusedwhenperformingswap

Aerodromeinterface: [Aerodrome Router Interface](https://github.com/aerodrome-finance/contracts/blob/main/contracts/interfaces/IRouter.sol#L6)

\u0060\u0060\u0060solidity
interface IRouter {
    struct Route {
        address from;
        address to;
        bool stable;
        address factory;
    }
    function poolFor(
        address tokenA,
        address tokenB,
        bool stable,
        address _factory
    ) external view returns (address pool);
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        Route[] calldata routes,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
    ...
}
\u0060\u0060\u0060

SolidiyV2AMOinterface: [Solidly Router Interface](https://github.com/sherlock-audit/2024-10-axion/blob/main/liquidity-amo/contracts/interfaces/v2/ISolidlyRouter.sol#L4)

\u0060\u0060\u0060solidity
interface ISolidlyRouter {
    ...
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
struct route {
    address from;
    address to;
    bool stable;
}

function pairFor(address tokenA, address tokenB, bool stable) external view returns (address pair);

function swapExactTokensForTokens(
    uint256 amountIn,
    uint256 amountOutMin,
    route[] memory routes,
    address to,
    uint256 deadline
) external returns (uint256[] memory amounts);
\u0060\u0060\u0060

**Internal pre-conditions**  
N/A

**External pre-conditions**  
N/A

**Attack Path**  
N/A

**Impact**  
SolidlyV2AMO does not work with Aerodrome/Velodrome as expected.

**PoC**  
N/A

**Mitigation**  
N/A
## Discussion

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/AXION-MONEY/liquidity-amo/pull/9
