# Issue H-11: Incorrect Price Representation

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** BondOracleAdapter, latestRoundData, priceX96, decimal precision, asset valuation, calculation error, Chainlink oracle, financial loss, smart contract, Ethereum, DeFi, protocol, price format, incorrect results, valuation, tick data, historical data, observe, pool, conversion

---

# IssueH-10: Users can sell Bond Token at a higher price

by manipulating the collateralLevel from < 120% to > 120% by purchasing Leverage Token.  
Source: https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/896  
Found by 056Security, 0xc0ffEE, KupiaSec, bigbear1229, future, novaman33, t0x1c, zraxx  

Buying Leverage Token increases TVL, which in turn raises the collateral Level.  
When redeeming Bond Token, the redemption amount is determined by the collateral Level. The calculation of the redemption amount varies depending on whether the collateral Level is above or below 120%.  
Therefore, Bond Token redeemers can acquire more underlying assets by manipulating the collateral Level from < 120% to > 120% through purchasing Leverage Token, ultimately resulting in a profit.  

The getRedeemAmount() function calculates the redeem Rate based on whether the collateral Level is above or below 120%.  
When collateral Level < 120%, 80% of TVL is allocated for Bond Token holders. In contrast, when collateral Level > 120%, the price of Bond Token is fixed at 100.  
This vulnerability provides malicious users with an opportunity to manipulate the collateral Level by purchasing Leverage Token, allowing them to redeem their Bond Tokens at a higher rate.  

\u0060\u0060\u0060solidity
function getRedeemAmount(
  ...
  uint256 collateralLevel;
  if (tokenType == TokenType.BOND) {
      collateralLevel = ((tvl - (depositAmount * BOND_TARGET_PRICE)) * PRECISION) / ((bondSupply - depositAmount) * BOND_TARGET_PRICE);
  } else {
      multiplier = POINT_TWO;
      assetSupply = levSupply;
      collateralLevel = (tvl * PRECISION) / (bondSupply * BOND_TARGET_PRICE);
  }
  ...
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 redeemRate;
if (collateralLevel <= COLLATERAL_THRESHOLD) {
    redeemRate = ((tvl * multiplier) / assetSupply);
} else if (tokenType == TokenType.LEVERAGE) {
    redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) * PRECISION;
} else {
    redeemRate = BOND_TARGET_PRICE * PRECISION;
}
\u0060\u0060\u0060

Let\u0027s consider the following scenario:
- Current State of the Pool:
    - levSupply: 100
    - bondSupply: 100
    - TVL: $11000
- Bob wants to redeem 50 Bond Token. Expected Values:
    - collateralLevel: (11000 - 100 * 50) / (100 - 50) = 120% (see line 498)
    - Price of Bond Token: 11000 * 0.8 / 100 = 88 (see the case at line 511)
    - Price of Leverage Token: 11000 * 0.2 / 100 = 22 (see the case at line 511)

As a result, Bob can only redeem 50 * 88 = 4400. However, Bob manipulates collateralLevel.
1. Bob buys 10 Leverage Token by using $220:
    - levSupply: 100 + 10 = 110
    - bondSupply: 100
    - TVL: 11000 + 220 = 11220
2. Bob then sells 50 Bond Token:
    - collateralLevel: (11220 - 100 * 50) / (100 - 50) = 124.4% (see line 498)
- Price of BondToken: 100 (see the case at line 515)
- Bob receives 100 * 50 = 5000.
- TVL: 11220 - 5000 = 6220
- bondSupply: 100 - 50 = 50

3. Bob sells back 10 LeverageToken.
- collateralLevel: 6220 / 50 = 124.4% (see line 502)
- Price of LeverageToken: (6220 - 100 * 50) / 110 = 11 (see the case at line 513)
- Bob receives 10 * 11 = 110.

As you can see, Bob was initially able to redeem only $4400. However, by manipulating collateralLevel, he can increase his redemption to -220 + 5000 + 110 = 4890. Thus, he can profit by 4890 - 4400 = 490.

BondToken redeemers can obtain more than they are entitled to by manipulating the collateralLevel through purchasing LeverageToken.


The current price mechanism should be improved.

sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/155](https://github.com/Convexity-Research/plaza-evm/pull/155)
## Issue H-11: Incorrect Price Representation

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/1016)  
**Found by:** 0x23r0, 0xc0ffEE, 10ap17, Ryonen, wickie

The \u0060latestRoundData()\u0060 function in the BondOracleAdapter contract calculates a price using the PriceX96 format. However, the returned price is not converted to a format with a specified decimal precision (e.g., 18 decimals, as in a Chainlink oracle). As a result, the price returned by the function will be completely different from the expected decimal-based price format. This discrepancy leads to significant mistakes in asset valuation and renders every calculation using this price incorrect.

\u0060\u0060\u0060solidity
function latestRoundData()
    external
    view
    returns (uint80, int256, uint256, uint256, uint80) {
    uint32[] memory secondsAgos = new uint32[](2);
    secondsAgos[0] = twapInterval; // from (before)
    secondsAgos[1] = 0; // to (now)
    (int56[] memory tickCumulatives, ) = ICLPool(dexPool).observe(secondsAgos);
    uint160 getSqrtTwapX96 = TickMath.getSqrtRatioAtTick(
      int24((tickCumulatives[1] - tickCumulatives[0]) / int56(uint56(twapInterval)))
    );
    return (uint80(0), int256(getPriceX96FromSqrtPriceX96(getSqrtTwapX96)),
    block.timestamp, block.timestamp, uint80(0));
}
\u0060\u0060\u0060

In BondOracleAdapter\u0027s \u0060latestRoundData\u0060 function, the calculated price is not converted from price X96 format to a format with decimals (e.g., 18 decimals), which will result in the returned price being fundamentally different from what is required for correct asset valuation and subsequent calculations.

[Link to Code](https://github.com/sherlock-audit/2024-12-plaza-finance/blob/14a962c52a8f4731bbe4655a2f6d0d85e144c7c2/plaza-evm/src/BondOracleAdapter.sol#L99)
No response

No response

1. The \u0060latestRoundData()\u0060 function will be called.
2. The function will calculate the price in the PriceX96 format.
3. The returned price will not be converted to a format with decimals of precision (e.g., 18 decimals).
4. Since the returned format is incorrect, the valuation of the asset will be wrong.
5. All dependent calculations that use the returned price will produce incorrect results.

The failure to return a price in the correct format causes incorrect asset valuations, which would lead to incorrect calculations, potentially causing financial losses for users.

**Step 1:** Fetch \u0060sqrtPriceX96\u0060 from the Pool Contract. We will be using usdc/weth pool (random pool on polygon network, which doesn\u0027t matter, since we are just proving concept)  
**Contract Address:** 0x45dda9cb7c25131df268515131f647d726f50608  
**Function:** \u0060slot0()\u0060  
**Output:** \u0060sqrtPriceX96 = 1390618563380010078436460929963734\u0060

**Step 2:** Calculate \u0060priceX96\u0060 from \u0060sqrtPriceX96\u0060  
**Function:** 
\u0060\u0060\u0060javascript
function getPriceX96FromSqrtPriceX96(sqrtPriceX96) {
    return FullMath.mulDiv(sqrtPriceX96, sqrtPriceX96, FixedPoint96.Q96);
}
\u0060\u0060\u0060
**Output:** \u006024408239790603697707980053009065971527\u0060  
This result is the result that would be returned from the \u0060latestRoundData\u0060 function, by current implementation, which is nowhere near the realistic price of weth in usdc token.
## Step 3: Convert price X96 to Actual Price with 18 Decimals

Next step, is to convert that price to the actual price that is in 18 decimals, since usdc has 6 decimals, and weth has 18, the formula would be:

\u0060\u0060\u0060
FullMath.mulDiv(10 ** (18 + decimals1 - decimals0), FixedPoint96.Q96, priceX96)
\u0060\u0060\u0060

Output: 3245959692053023671448

The result is in 18 decimals and represents around 3245.95 usdc per weth.


Consider using the approach used by the Saltio.IO project, which ensures proper conversion to the 18-decimal (in this case) standard. The implementation is as follows:

\u0060\u0060\u0060solidity
// Returns the price of token0 * (10**18) in terms of token1
function _getUniswapTwapWei(IUniswapV3Pool pool, uint256 twapInterval) public view
    returns (uint256) {
        uint32;
        secondsAgo[0] = uint32(twapInterval); // from (before)
        secondsAgo[1] = 0; // to (now)
        // Get the historical tick data using the observe() function
        (int56[] memory tickCumulatives, ) = pool.observe(secondsAgo);
        int24 tick = int24((tickCumulatives[1] - tickCumulatives[0]) /
            int56(uint56(twapInterval)));
        uint160 sqrtPriceX96 = TickMath.getSqrtRatioAtTick(tick);
        // Convert the sqrtPriceX96 to a price with 18 decimals
        uint256 p = FullMath.mulDiv(sqrtPriceX96, sqrtPriceX96, FixedPoint96.Q96);
        uint8 decimals0 = ERC20(pool.token0()).decimals();
        uint8 decimals1 = ERC20(pool.token1()).decimals();
        if (decimals1 > decimals0) {
            return FullMath.mulDiv(10 ** (18 + decimals1 - decimals0),
                FixedPoint96.Q96, p);
        }
        if (decimals0 > decimals1) {
            return (FixedPoint96.Q96 * (10 ** 18)) / (p * (10 ** (decimals0 -
                decimals1)));
        }
        return (FixedPoint96.Q96 * (10 ** 18)) / p;
}
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/Convexity-Research/plaza-evm/pull/158
## IssueM-1: Failed auction period still updates shares Per Token

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/48)

Found by: 056Security, 0rpse, 0x23r0, 0x52, 0xEkko, 0xShahilHussain, 0xadrii, 0xlucky, 0xmystery, Abhan1041, Adotsam, Aymen0909, ChainProof, Hueber, MysteryAuditor, Pablo, SamuelTroyDomi, Schnilch, ZoA, bladeee, bretzel, carlitox477, dobrevaleri, farismaulana, future, moray5554, novaman33, phn210, robertauditor, shui, silver_eth, sl1, y4y, zxriptor


The way bond ETH holder get the coupon (USDC) is through the auction where protocol would auction amount of underlying asset for coupon to be later distributed to bond ETH holder of current period. But the BondToken::increaseIndexedAssetPeriod would always push the default value of shares Per Token to the previous period to globalPool.previousPoolAmounts array when new auction start, regardless if the previous auction is succeed or not.


When auction is succeed, the coupon collected would later be sent to pool, and then pool would distribute and allocate the amount into distribute contract, and if it fails no coupon is sent to the pool thus making no amount to distribute and allocated to distribute contract and any previous bid can be claimed.

\u0060\u0060\u0060solidity
function endAuction() external auctionExpired whenNotPaused {
  if (state != State.BIDDING) revert AuctionAlreadyEnded();
  if (currentCouponAmount < totalBuyCouponAmount) {
    state = State.FAILED_UNDERSOLD;
  } else if (totalSellReserveAmount >= (IERC20(sellReserveToken).balanceOf(pool) * poolSaleLimit) / 100) {
    state = State.FAILED_POOL_SALE_LIMIT;
  } else {
    state = State.SUCCEEDED;
    Pool(pool).transferReserveToAuction(totalSellReserveAmount);
    IERC20(buyCouponToken).safeTransfer(beneficiary, IERC20(buyCouponToken).balanceOf(address(this)));
  }
}
\u0060\u0060\u0060
emit AuctionEnded(state, totalSellReserveAmount, totalBuyCouponAmount);
regardless, anyonecancallPool::startAuctiontostartnewauction. andthisis problematicbecauseinsidethefunctionthe bondToken.increaseIndexedAssetPeriod(sharesPerToken)iscalled.

Pool.sol
\u0060\u0060\u0060solidity
function startAuction() external whenNotPaused() {
    .
    .
    .
    // Increase the bond token period
    @>  bondToken.increaseIndexedAssetPeriod(sharesPerToken);
    .
    .
    .
}
\u0060\u0060\u0060

whenthisfunctioncalled,thepreviousfailedauctiondatawouldthengetpushedinto thepreviousPoolAmountsarray:

BondToken.sol
\u0060\u0060\u0060solidity
function increaseIndexedAssetPeriod(uint256 sharesPerToken) public
    ֒→  onlyRole(DISTRIBUTOR_ROLE) whenNotPaused() {
        globalPool.previousPoolAmounts.push(
            PoolAmount({
                period: globalPool.currentPeriod,
                amount: totalSupply(),
                @>      sharesPerToken: globalPool.sharesPerToken
            })
        );
        globalPool.currentPeriod++;
        globalPool.sharesPerToken = sharesPerToken;
        emit IncreasedAssetPeriod(globalPool.currentPeriod, sharesPerToken);
    }
\u0060\u0060\u0060

thesharesPerTokenofpreviousperiodisupdatedbyusingdefaultvalueof globalPool.sharesPerToken(docssaiditwouldbeequalto2.5USD)eventhoughthere arenocoupongetsentintodistributorcontract. butnonetheless,theusercanstillclaimthesharesof2periodeventhoughthereareno newcoupontokeninsidethedistributorcontract. andtheclaimfunctionwouldthen haveliquidityproblem

Distributor.sol
\u0060\u0060\u0060solidity
// Code not provided
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function claim() external whenNotPaused nonReentrant {
    BondToken bondToken = Pool(pool).bondToken();
    address couponToken = Pool(pool).couponToken();
    if (address(bondToken) == address(0) || couponToken == address(0)){
        revert UnsupportedPool();
    }
    (uint256 currentPeriod,) = bondToken.globalPool();
    uint256 balance = bondToken.balanceOf(msg.sender);
    uint256 shares = bondToken.getIndexedUserAmount(msg.sender, balance, currentPeriod)
                            .normalizeAmount(bondToken.decimals(), IERC20(couponToken).safeDecimals());
    if (IERC20(couponToken).balanceOf(address(this)) < shares) {
        revert NotEnoughSharesBalance();
    }
    // check if pool has enough *allocated* shares to distribute
    if (couponAmountToDistribute < shares) {
        revert NotEnoughSharesToDistribute();
    }
    // check if the distributor has enough shares tokens as the amount to distribute
    if (IERC20(couponToken).balanceOf(address(this)) < couponAmountToDistribute) {
        revert NotEnoughSharesToDistribute();
    }
    couponAmountToDistribute -= shares;
    bondToken.resetIndexedUserAssets(msg.sender);
    IERC20(couponToken).safeTransfer(msg.sender, shares);
    emit ClaimedShares(msg.sender, currentPeriod, shares);
}
\u0060\u0060\u0060

noticethatshareswouldbeincreasedbyaddingthefailedauctionsharePerToken amount

No response

No response

1. auction 0 start -> end successfully and 50 USD coupon is sent to be claimed in distributor contract
2. each holder can claim 2.5 USD per bond ETH in this period
3. auction 1 start -> end with undersold, no new USD coupons sent to distributor contract
4. each holder can claim 2.5 + 2.5 USD per bond ETH held in this period if they held for 2 period
5. alice held since period 0, and has 10 bond ETH. she can claim 10 * 5 = 50 USD
6. bob held since period 0, and has 10 bond ETH. he can\u0027t claim because distributor contract now has 0 USD


holder of bond ETH token cannot claim shares if they late. discrepancy in the claimed amount vs actual coupon token held inside distributor contract would make not enough coupon to be claimed for all bond ETH holder


No response


when auction fails, consider to update the shares Per Token for the failed period auction to 0.


sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/Convexity-Research/plaza-evm/pull/157
## Issue M-2: Bid with high price effectively can end up with lower price

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/198)  
This issue has been acknowledged by the team but won\u0027t be fixed at this time.  
Found by: ZoA  

In the \u0060removeExcessBids\u0060 function, when the total bid amount exceeds total Buy Coupon Amount, the contract reduces the sell Coupon Amount and buy Reserve Amount of the lowest-ranked bidder proportionally. This reduction introduces precision loss due to integer division, leading to a scenario where bids initially made at a high price effectively end up with a lower price.

On the line \u0060Auction.sol#L281\u0060, \u0060removeExcessBids\u0060 function reduces sell Coupon Amount and buy Reserve Amount proportionally. However, the reduction uses integer arithmetic, causing rounding errors that alter the price ratio (sell Coupon Amount / buy Reserve Amount).

No response  

No response  

No response  

- Assume totalBuyCouponAmount = 10e18, slotSize = 1e18 and currentCouponAmount = 10e18 (full charged).
- The lowest bidder (bidder1): buyReserveAmount = 1e8, sellCouponAmount = 1e18
- bidder2: bids with buyReserveAmount = 9e8, sellCouponAmount = 9e18
  - price is same as the bidder1\u0027s but sellCouponAmount is larger.
  - bidder1 is removed and bidder2 enters the list.
  - bidder2\u0027s values change:
    - amountToRemove = 8e18
    - proportion = (amountToRemove * 1e18) / sellCouponAmount = 888888888888888888
    - new sellCouponAmount = 1e18
    - new buyReserveAmount = 9e8 - [9e8 * proportion] / 1e18 = 1e8 + 1
- Result: Bidder2 has the lower price than Bidder1.

1. Bid with high price effectively can end up with lower price.
2. The lowest bidder can repeat the same operation as above to increase the size of buyReserveAmount without changing sellCouponAmount. Attacker can either profit by 1 wei (0.001 usd) which is more than the gas fee if the token is WBTC. In this case, even if the attacker\u0027s gain is not great due to gas fees, the protocol loses a lot of reserve tokens.

Check whether the buyReserveAmount size increases before and after the bid.

\u0060\u0060\u0060solidity
function bid(uint256 buyReserveAmount, uint256 sellCouponAmount) external
    auctionActive whenNotPaused returns(uint256) {
    ...
    uint256 totalSellReserveAmountBefore = totalSellReserveAmount;
    Bid memory newBid = Bid({
    ...
    removeExcessBids();
    uint256 totalSellReserveAmountAfter = totalSellReserveAmount;
    if(totalSellReserveAmountBefore < totalSellReserveAmountAfter) revert TotalSellReserveAmountIncreased();
    ...
}
\u0060\u0060\u0060
## IssueM-3: User may lose funds if they call BalancerRouter::joinBalancerAndPredeposit

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/278)

This issue has been acknowledged by the team but won\u0027t be fixed at this time.

Found by:  
056Security, 0x23r0, 0xDemon, 0xShahilHussain, 0xc0ffEE, Adotsam, JohnTPark24,  
Kenn.eth, Kirkeelee, MysteryAuditor, Pablo, X0sauce, Xcrypt, ZeroTrust, ZoA, bladeee,  
dobrevaleri, farismaulana, future, hrmneffdii, makeWeb3safe, phoenixv110, super_jack,  
tutiSec, y4y


BalancerRouter::joinBalancerAndPredeposit calls Predeposit::deposit to deposit balancerPoolTokens into the Predeposit contract. In the Predeposit::deposit if reserveAmount + amount > reserveCap, the difference is deposited and the rest remains with msg.sender, which in this case is the BalancerRouter.

The user will have less than expected amount deposited in Predeposit without getting refund for the rest of the funds.

\u0060\u0060\u0060solidity
function _deposit(uint256 amount, address onBehalfOf) private
    checkDepositStarted checkDepositNotEnded {
        if (reserveAmount >= reserveCap) revert DepositCapReached();
        address recipient = onBehalfOf == address(0) ? msg.sender : onBehalfOf;
        // if user would like to put more than available in cap, fill the rest up
        to cap and add that to reserves
        if (reserveAmount + amount >= reserveCap) {
            amount = reserveCap - reserveAmount;
        }
        balances[recipient] += amount;
        reserveAmount += amount;
        IERC20(params.reserveToken).safeTransferFrom(msg.sender, address(this), amount);
        emit Deposited(recipient, amount);
}
\u0060\u0060\u0060
No response

No response

No response

Assume reserve cap is 1,000 BPT and reserve amount is 900 BPT. User calls \u0060BalancerRouter::joinBalancerAndPredeposit\u0060 and deposits assets worth 500 BPT. Only 100 BPT is deposited and user loses 400 BPT which is trapped inside the contract.

Loss of funds

No response

\u0060\u0060\u0060solidity
function joinBalancerAndPredeposit(
    bytes32 balancerPoolId,
    address _predeposit,
    IAsset[] memory assets,
    uint256[] memory maxAmountsIn,
    bytes memory userData
) external nonReentrant returns (uint256) {
    // Step 1: Join Balancer Pool
    uint256 balancerPoolTokenReceived = joinBalancerPool(balancerPoolId,
        assets, maxAmountsIn, userData);
    // Step 2: Approve balancerPoolToken for PreDeposit
    balancerPoolToken.safeIncreaseAllowance(_predeposit,
        balancerPoolTokenReceived);
    uint256 BPTBalanceBefore = balancerPoolToken.balanceOf(address(this));
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Step 3: Deposit to PreDeposit
PreDeposit(_predeposit).deposit(balancerPoolTokenReceived, msg.sender);
uint256 BPTBalanceAfter = balancerPoolToken.balanceOf(address(this));
if (BPTBalanceAfter - BPTBalanceBefore > 0) {
  revert ( \u0027ReserveCap Reached\u0060 ); 
}
return balancerPoolTokenReceived;
\u0060\u0060\u0060
