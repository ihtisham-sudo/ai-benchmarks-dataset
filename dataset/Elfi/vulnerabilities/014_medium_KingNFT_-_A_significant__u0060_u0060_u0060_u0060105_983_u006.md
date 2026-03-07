# KingNFT - A significant \u0060\u0060\u0060\u0060105,983\u0060\u0060\u0060\u0060 gas cost of \u0060\u0060\u0060\u0060processExecutionFee()\u0060\u0060\u0060\u0060 execution is not accounted in the keeper\u0027s compensation

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, smart contract, solidity, gas usage, execution fee, processExecutionFee, executeOrder, gasleft, OracleProcess, refund fee, loss fee, VaultProcess, manual review, gas compensation, transaction, audit, keeper, code snippet, hardhat

---

KingNFT

Medium

# A significant \u0060\u0060\u0060\u0060105,983\u0060\u0060\u0060\u0060 gas cost of \u0060\u0060\u0060\u0060processExecutionFee()\u0060\u0060\u0060\u0060 execution is not accounted in the keeper\u0027s compensation

## Summary

At the end of \u0060\u0060\u0060\u0060executeOrder()\u0060\u0060\u0060\u0060, \u0060\u0060\u0060\u0060processExecutionFee()\u0060\u0060\u0060\u0060 is called to process gas compensation for the keeper. The issue here is that the gas usage of \u0060\u0060\u0060\u0060processExecutionFee()\u0060\u0060\u0060\u0060 itself is not taken into consideration. As the following test case shows, it\u0027s significant (\u0060\u0060\u0060\u0060105,983\u0060\u0060\u0060\u0060), can\u0027t be ignored.

## Vulnerability Detail
At the beginning of \u0060\u0060\u0060\u0060executeOrder()\u0060\u0060\u0060\u0060, \u0060\u0060\u0060\u0060startGas\u0060\u0060\u0060\u0060 is recorded (L67). At the end of \u0060\u0060\u0060\u0060executeOrder()\u0060\u0060\u0060\u0060, \u0060\u0060\u0060\u0060processExecutionFee()\u0060\u0060\u0060\u0060 is called to process gas compensation for the keeper (L76\~86). The issue arises in the \u0060\u0060\u0060\u0060processExecutionFee()\u0060\u0060\u0060\u0060 function, the gas usage from \u0060\u0060\u0060\u0060L19\u0060\u0060\u0060\u0060 to \u0060\u0060\u0060\u0060L41\u0060\u0060\u0060\u0060 is not taken into account.
\u0060\u0060\u0060solidity
File: contracts\facets\OrderFacet.sol
66:     function executeOrder(uint256 orderId, OracleProcess.OracleParam[] calldata oracles) external override {
67:         uint256 startGas = gasleft();
...
76:         GasProcess.processExecutionFee(
77:             GasProcess.PayExecutionFeeParams(
78:                 order.isExecutionFeeFromTradeVault
79:                     ? IVault(address(this)).getTradeVaultAddress()
80:                     : IVault(address(this)).getPortfolioVaultAddress(),
81:                 order.executionFee,
82:                 startGas,
83:                 msg.sender,
84:                 order.account
85:             )
86:         );
87:     }

File: contracts\process\GasProcess.sol
17:     function processExecutionFee(PayExecutionFeeParams memory cache) external {
18:         uint256 usedGas = cache.startGas - gasleft();
19:         uint256 executionFee = usedGas * tx.gasprice; // @audit gas usage since this line is not accounted
20:         uint256 refundFee;
21:         uint256 lossFee;
22:         if (executionFee > cache.userExecutionFee) {
23:             executionFee = cache.userExecutionFee;
24:             lossFee = executionFee - cache.userExecutionFee;
25:         } else {
26:             refundFee = cache.userExecutionFee - executionFee;
27:         }
28:         VaultProcess.transferOut(
29:             cache.from,
30:             AppConfig.getChainConfig().wrapperToken,
31:             address(this),
32:             cache.userExecutionFee
33:         );
34:         VaultProcess.withdrawEther(cache.keeper, executionFee);
35:         if (refundFee > 0) {
36:             VaultProcess.withdrawEther(cache.account, refundFee);
37:         }
38:         if (lossFee > 0) {
39:             CommonData.addLossExecutionFee(lossFee);
40:         }
41:     }

\u0060\u0060\u0060

To test the specific unaccounted gas usage of \u0060\u0060\u0060\u0060processExecutionFee()\u0060\u0060\u0060\u0060, we made a minor modifications as follows:
\u0060\u0060\u0060diff
+   event GasUsageOfProcessExecutionFeeSelf(uint256);
    function processExecutionFee(PayExecutionFeeParams memory cache) external {
        uint256 usedGas = cache.startGas - gasleft();
+      uint256 selfGasStart = gasleft();
        uint256 executionFee = usedGas * tx.gasprice;
        uint256 refundFee;
        uint256 lossFee;
        if (executionFee > cache.userExecutionFee) {
            executionFee = cache.userExecutionFee;
            lossFee = executionFee - cache.userExecutionFee;
        } else {
            refundFee = cache.userExecutionFee - executionFee;
        }
        VaultProcess.transferOut(
            cache.from,
            AppConfig.getChainConfig().wrapperToken,
            address(this),
            cache.userExecutionFee
        );
        VaultProcess.withdrawEther(cache.keeper, executionFee);
        if (refundFee > 0) {
            VaultProcess.withdrawEther(cache.account, refundFee);
        }
        if (lossFee > 0) {
            CommonData.addLossExecutionFee(lossFee);
        }
+       uint256 selfGasEnd = gasleft();
+      emit GasUsageOfProcessExecutionFeeSelf(selfGasStart - selfGasEnd);
    }

\u0060\u0060\u0060

Then, by the following test script, we get the missing portion is \u0060\u0060\u0060\u0060105,983\u0060\u0060\u0060\u0060 gas. It\u0027s significant and should not be ignored.
\u0060\u0060\u0060typescript
import { expect } from \u0027chai\u0027
import { Fixture, deployFixture } from \u0027@test/deployFixture\u0027
import { ORDER_ID_KEY, OrderSide, OrderType, PositionSide, StopType } from \u0027@utils/constants\u0027
import { precision } from \u0027@utils/precision\u0027
import {
    MarketFacet,
    MockToken,
    OrderFacet
} from \u0027types\u0027
import { HardhatEthersSigner } from \u0027@nomicfoundation/hardhat-ethers/signers\u0027
import { ethers } from \u0027hardhat\u0027
import { handleMint } from \u0027@utils/mint\u0027

describe(\u0027Test gas usage of processExecutionFee() itself\u0027, function () {
    let fixture: Fixture
    let marketFacet: MarketFacet, orderFacet: OrderFacet
    let user0: HardhatEthersSigner, user1: HardhatEthersSigner, user2: HardhatEthersSigner, user3: HardhatEthersSigner
    let diamondAddr: string,
        wbtcAddr: string,
        wethAddr: string,
        usdcAddr: string
    let btcUsd: string, xBtc: string, xUsd: string
    let wbtc: MockToken, weth: MockToken, usdc: MockToken

    beforeEach(async () => {
        fixture = await deployFixture()
            ; ({ marketFacet, orderFacet } =
                fixture.contracts)
            ; ({ user0, user1, user2, user3 } = fixture.accounts)
            ; ({ btcUsd } = fixture.symbols)
            ; ({ xBtc, xUsd } = fixture.pools)
            ; ({ wbtc, weth, usdc } = fixture.tokens)
            ; ({ diamondAddr } = fixture.addresses)
        wbtcAddr = await wbtc.getAddress()
        wethAddr = await weth.getAddress()
        usdcAddr = await usdc.getAddress()

        const btcTokenPrice = precision.price(25000)
        const btcOracle = [{ token: wbtcAddr, minPrice: btcTokenPrice, maxPrice: btcTokenPrice }]
        await handleMint(fixture, {
            stakeToken: xBtc,
            requestToken: wbtc,
            requestTokenAmount: precision.token(100),
            oracle: btcOracle,
        })

        const ethTokenPrice = precision.price(1600)
        const ethOracle = [{ token: wethAddr, minPrice: ethTokenPrice, maxPrice: ethTokenPrice }]
        await handleMint(fixture, {
            requestTokenAmount: precision.token(500),
            oracle: ethOracle,
        })

        const usdcTokenPrice = precision.price(101, 6)
        const usdOracle = [
            { token: usdcAddr, minPrice: usdcTokenPrice, maxPrice: usdcTokenPrice },
        ]

        await handleMint(fixture, {
            requestTokenAmount: precision.token(100000, 6),
            stakeToken: xUsd,
            requestToken: usdc,
            oracle: usdOracle,
        })
    })

    it(\u0027Case 1 \u0027, async function () {
        const orderMargin = precision.token(1, 17) // 0.1BTC
        const executionFee = precision.token(2, 15)
        wbtc.connect(user0).approve(diamondAddr, orderMargin)
        let tx = await orderFacet.connect(user0).createOrderRequest(
            {
                symbol: btcUsd,
                orderSide: OrderSide.LONG,
                posSide: PositionSide.INCREASE,
                orderType: OrderType.MARKET,
                stopType: StopType.NONE,
                isCrossMargin: false,
                marginToken: wbtcAddr,
                qty: 0,
                leverage: precision.rate(10),
                triggerPrice: 0,
                acceptablePrice: precision.price(26000),
                executionFee: executionFee,
                placeTime: 0,
                orderMargin: orderMargin,
                isNativeToken: false,
            },
            {
                value: executionFee,
            },
        )

        await tx.wait()

        const requestId = await marketFacet.getLastUuid(ORDER_ID_KEY)
        const tokenPrice = precision.price(25000)
        const oracle = [{ token: wbtcAddr, targetToken: ethers.ZeroAddress, minPrice: tokenPrice, maxPrice: tokenPrice }]
        tx = await orderFacet.connect(user3).executeOrder(requestId, oracle)
        const receipt = await tx.wait()
        const signature = ethers.keccak256(ethers.toUtf8Bytes("GasUsageOfProcessExecutionFeeSelf(uint256)"))
        const logs = receipt?.logs.filter(x => x.topics[0] === signature)
        expect(logs?.length).equals(1)
        const gas = BigInt(logs![0].data)
        console.log(\u0060Gas usage in processExecutionFee() that isn\u0027t accounted for compensation: ${gas}\u0060)
        
    })
})
\u0060\u0060\u0060

And the test log:
\u0060\u0060\u0060solidity
2024-05-elfi-protocol\elfi-perp-contracts> npx hardhat test .\test\single-cases\BugGasCompensation.test.ts    
  Test gas usage of processExecutionFee() itself
...
Gas usage in processExecutionFee() that isn\u0027t accounted for compensation: 105983
    ✔ Case 1  (771ms)


  1 passing (16s)
\u0060\u0060\u0060
## Impact
The keeper will suffer continuing \u0060\u0060\u0060\u0060100K\u0060\u0060\u0060\u0060 gas losses on each transaction due to the issue.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/GasProcess.sol#L17

## Tool used

Manual Review

## Recommendation
Adding this portion as a fixed compensation for the keeper.
\u0060\u0060\u0060diff
File: contracts\process\GasProcess.sol
17:     function processExecutionFee(PayExecutionFeeParams memory cache) external {
-18:         uint256 usedGas = cache.startGas - gasleft();
+18:         uint256 usedGas = cache.startGas - gasleft() + 101_000;
41:     }

\u0060\u0060\u0060

