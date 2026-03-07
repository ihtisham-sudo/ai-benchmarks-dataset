# mstpr-brainbot - Pool value does not consider the open funding fees

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, pool value, funding fees, staking tokens, minting shares, redeeming shares, exploitation, sandwich attack, unsettled amount, market PnL, position closing, margin increase, cross position, discrepancy, ERC4626, share calculation, manual review, impact assessment, recommendation

---

mstpr-brainbot

High

# Pool value does not consider the open funding fees

## Summary
The pool\u0027s value is not considering a vital component: the open funding fees. The pool value is used when calculating staking token mint/redeem shares, and since the funding fees are not accounted for, minting/redeeming of shares will not be accurate. Additionally, someone can exploit this by sandwiching a closing position, knowing that the funding fees will be realized when the position is closed, and take advantage of the previous pool value.
## Vulnerability Detail
First, let\u0027s see how the pools value is calculated:

\u0060\u0060\u0060solidity
function getPoolIntValue(
        LpPool.Props storage pool,
        OracleProcess.OracleParam[] memory oracles
    ) public view returns (int256) {
        int256 value = 0;
       -> if (pool.baseTokenBalance.amount > 0 || pool.baseTokenBalance.unsettledAmount > 0) {
            int256 unPnl = getMarketUnPnl(pool.symbol, oracles, true, pool.baseToken, true);
            int256 baseTokenPrice = OracleProcess.getIntOraclePrices(oracles, pool.baseToken, true);
            value = CalUtils.tokenToUsdInt(
                (pool.baseTokenBalance.amount.toInt256() + pool.baseTokenBalance.unsettledAmount + unPnl),
                TokenUtils.decimals(pool.baseToken),
                baseTokenPrice
            );
        }
        address[] memory stableTokens = pool.getStableTokens();
        if (stableTokens.length > 0) {
            // ignore here, assume no stable tokens exists in the pool
        }
        return value;
    }
\u0060\u0060\u0060

Simply, considering there are no stable tokens in a pool the total value is:
**baseTokenBalance.amount + baseTokenBalance.unsettledAmount + marketPnL**

Little bit more detail on the \u0060unsettledAmount\u0060:
\u0060unsettledAmount\u0060 is only accounted when a position is updated. For example when closing a position or increasing a positions margin. Also, it will change via funding fees. Since the previous actions changes the funding fee the \u0060unsettledAmount\u0060 will also change.

When a position is closed the funding fees will accounted in \u0060unsettledAmount\u0060 which previously it wasn\u0027t accounted as follows:
\u0060\u0060\u0060solidity
function decreasePosition(Position.Props storage position, DecreasePositionParams calldata params) external {
        int256 totalPnlInUsd = PositionQueryProcess.getPositionUnPnl(position, params.executePrice.toInt256(), false);
        Symbol.Props memory symbolProps = Symbol.load(params.symbol);
        AppConfig.SymbolConfig memory symbolConfig = AppConfig.getSymbolConfig(params.symbol);
        FeeProcess.updateBorrowingFee(position, symbolProps.stakeToken);
        -> FeeProcess.updateFundingFee(position);
        .
        .
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function updateFundingFee(Position.Props storage position) public {
        .
        -> MarketProcess.updateMarketFundingFee(
            position.symbol,
            realizedFundingFee,
            position.isLong,
            true,
            position.marginToken
        );
    }
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function updateMarketFundingFee(
        bytes32 symbol,
        int256 realizedFundingFeeDelta,
        bool isLong,
        bool needUpdateUnsettle,
        address marginToken
    ) external {
        Market.Props storage market = Market.load(symbol);
        .
        if (needUpdateUnsettle) {
            Symbol.Props storage symbolProps = Symbol.load(symbol);
            LpPool.Props storage pool = LpPool.load(symbolProps.stakeToken);
            if (isLong) {
               -> pool.addUnsettleBaseToken(realizedFundingFeeDelta);
            } else {
                pool.addUnsettleStableToken(marginToken, realizedFundingFeeDelta);
            }
        }
    }
\u0060\u0060\u0060

So if there are some funding fees accrued in the life time of the position they are now added to the pools \u0060unsettledAmount\u0060 which this amount is directly affecting the pools value.

If the closed position is "cross" \u0060unsettledAmount\u0060 is not resetted as we can see here:
\u0060\u0060\u0060solidity
function decreasePosition(Position.Props storage position, DecreasePositionParams calldata params) external {
        .
        .
        // update funding fee
        -> MarketProcess.updateMarketFundingFee(
            symbolProps.code,
            -cache.settledFundingFee, // the negative of what\u0027s added
            cache.position.isLong,
            !position.isCrossMargin, // since the position is cross this will be false and unsettledAmount will not be resetted!
            cache.position.marginToken
        );
        .
        .
}
\u0060\u0060\u0060

Hence, the \u0060unsettledAmount\u0060 is increased and pools value changed without any changes in stake token supply creating a discrepancy in the share calculation. 

Share calculations for minting and redeeming is like ERC4626 just for a reference let\u0027s see how minting new shares are calculated:
\u0060\u0060\u0060solidity
uint256 baseMintAmountInUsd = CalUtils.tokenToUsd(
                mintAmount,
                tokenDecimals,
                OracleProcess.getLatestUsdUintPrice(pool.baseToken, true)
            );
            mintStakeTokenAmount = totalSupply.mul(baseMintAmountInUsd).div(poolValue);
\u0060\u0060\u0060

As we can observe, the increase on \u0060unsettledAmount\u0060 will spike the pools value and share calculations will not be correct. 

**Coded PoC:**
\u0060\u0060\u0060typescript
it("Pools entire value is not accounting the unsettled funding fees", async function () {
		const usdcAmount = precision.token(60_000, 6); // enough amount to open in desired qty
		// fund user0
		await deposit(fixture, {
			account: user0,
			token: usdc,
			amount: usdcAmount,
		});

		// fund user1
		await deposit(fixture, {
			account: user1,
			token: usdc,
			amount: usdcAmount,
		});

		const oracleBeginning = [
			{
				token: wbtcAddr,
				targetToken: ethers.ZeroAddress,
				minPrice: precision.price(25_000),
				maxPrice: precision.price(25_000),
			},
			{
				token: usdcAddr,
				targetToken: ethers.ZeroAddress,
				minPrice: precision.price(99, 6),
				maxPrice: precision.price(99, 6),
			},
		];
		let poolInfoBeginning = await poolFacet.getPoolWithOracle(
			xBtc,
			oracleBeginning
		);
		console.log("Pool value very beginning", poolInfoBeginning.poolValue);

		const orderMargin = precision.token(50_000); // 50k$
		const executionFee = precision.token(2, 15);
		// wbtc.connect(user0).approve(diamondAddr, orderMargin);
		const tx = await orderFacet.connect(user0).createOrderRequest(
			{
				symbol: btcUsd,
				orderSide: OrderSide.LONG,
				posSide: PositionSide.INCREASE,
				orderType: OrderType.MARKET,
				stopType: StopType.NONE,
				isCrossMargin: true,
				marginToken: wbtcAddr,
				qty: 0,
				leverage: precision.rate(10),
				triggerPrice: 0,
				acceptablePrice: 0,
				executionFee: executionFee,
				placeTime: 0,
				orderMargin: orderMargin,
				isNativeToken: false,
			},
			{
				value: executionFee,
			}
		);

		await tx.wait();

		const requestId = await marketFacet.getLastUuid(ORDER_ID_KEY);

		const tokenPrice = precision.price(25000);
		const usdcPrice = precision.price(99, 6); // 0.99$
		const oracle = [
			{
				token: wbtcAddr,
				targetToken: ethers.ZeroAddress,
				minPrice: tokenPrice,
				maxPrice: tokenPrice,
			},
			{
				token: usdcAddr,
				targetToken: ethers.ZeroAddress,
				minPrice: usdcPrice,
				maxPrice: usdcPrice,
			},
		];

		await orderFacet.connect(user3).executeOrder(requestId, oracle);

		const btcShortAm = precision.token(100); // only 100$, I want longs to pay shorts funding fee
		// user1 opens the short
		const tx2 = await orderFacet.connect(user1).createOrderRequest(
			{
				symbol: btcUsd,
				orderSide: OrderSide.SHORT,
				posSide: PositionSide.INCREASE,
				orderType: OrderType.MARKET,
				stopType: StopType.NONE,
				isCrossMargin: true,
				marginToken: usdcAddr,
				qty: 0,
				leverage: precision.rate(5),
				triggerPrice: 0,
				acceptablePrice: 0,
				executionFee: executionFee,
				placeTime: 0,
				orderMargin: btcShortAm,
				isNativeToken: false,
			},
			{
				value: executionFee,
			}
		);

		await tx2.wait();

		const requestId2 = await marketFacet.getLastUuid(ORDER_ID_KEY);
		await orderFacet.connect(user3).executeOrder(requestId2, oracle);

		// assume price is 30k, user in profit pool in loss.
		const oracleNext = [
			{
				token: wbtcAddr,
				targetToken: ethers.ZeroAddress,
				minPrice: precision.price(30_000),
				maxPrice: precision.price(30_000),
			},
			{
				token: usdcAddr,
				targetToken: ethers.ZeroAddress,
				minPrice: usdcPrice,
				maxPrice: usdcPrice,
			},
		];

		let poolInfoWithNextOracle = await poolFacet.getPoolWithOracle(
			xBtc,
			oracleNext
		);

		console.log(
			"Pool value with next oracle",
			poolInfoWithNextOracle.poolValue
		);

		// close the position.
		const positionInfo = await positionFacet.getSinglePosition(
			user0.address,
			btcUsd,
			wbtcAddr,
			true
		);

		// mimick funding fees
		await mine(1000, { interval: 300 });

		// funding fees accrued but did we catch it? no untill the position
		// is updated the unsettledAmount will not change however, everyone knows when a position
		// closes the unsettledAmount will immediately added and it will spike up the pools value!
		let poolInfoWithNextOrcleAfterFundingFees =
			await poolFacet.getPoolWithOracle(xBtc, oracleNext);
		console.log(
			"Pool value with next oracle after funding fees",
			poolInfoWithNextOrcleAfterFundingFees.poolValue
		);

		const tx3 = await orderFacet.connect(user0).createOrderRequest(
			{
				symbol: btcUsd,
				orderSide: OrderSide.SHORT,
				posSide: PositionSide.DECREASE,
				orderType: OrderType.MARKET,
				stopType: StopType.NONE,
				isCrossMargin: true,
				marginToken: wbtcAddr,
				qty: positionInfo.qty,
				leverage: precision.rate(10),
				triggerPrice: 0,
				acceptablePrice: 0,
				executionFee: executionFee,
				placeTime: 0,
				orderMargin: orderMargin,
				isNativeToken: false,
			},
			{
				value: executionFee,
			}
		);

		await tx3.wait();

		const requestId3 = await marketFacet.getLastUuid(ORDER_ID_KEY);
		await orderFacet.connect(user3).executeOrder(requestId3, oracleNext);

		let poolInfoFinal = await poolFacet.getPoolWithOracle(xBtc, oracleNext);

		console.log("Pool value final", poolInfoFinal.poolValue);
		console.log("Pool balances", poolInfoFinal.baseTokenBalance);

		// when the funding fees accrued the actual balance is higher!!!!
		expect(poolInfoFinal.poolValue).greaterThan(
			poolInfoWithNextOrcleAfterFundingFees.poolValue
		);
	});
\u0060\u0060\u0060

**Test Logs:**
Pool value very beginning 2497000000000000000000000n
Pool value with next oracle 2897900000000000000010000n
Pool value with next oracle after funding fees 2897900000000000000010000n
Pool value final 2910696155073654825000000n

## Impact
Pools value will spike when positions are updated. This will create unfair minting/redeeming for shares. 
## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/LpPoolQueryProcess.sol#L110-L144

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/DecreasePositionProcess.sol#L150-L156

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/MarketProcess.sol#L104-L127

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/FeeProcess.sol#L102-L137

https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/process/DecreasePositionProcess.sol#L64-L65
## Tool used

Manual Review

## Recommendation
Account the net funding fee market will have considering all users positions and add it to the pools value calculation. 
