# M-15 - MixOracle is broken due to hardcoded position

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Debita Finance V3
**Keywords:** MixOracle, hardcoded, token position, liquidity pool, uniswap, token0, token1, collateral, decentralized finance, smart contract, financial loss, oracle, Fantom, liquidity, positioning, contract functionality, vulnerabilities, audit, security, protocol design, token support

---

# Issue M-14: The MixOracle.getThePrice function calculates the price incorrectly using the TarotOracle.getResult function as the TWAP price

Source: [GitHub Issue #501](https://github.com/sherlock-audit/2024-10-debita-judging/issues/501)  
Found by: KupiaSec  

The MixOracle.getThePrice function calculates the price using the TarotOracle contract and the pyth oracle. However, it incorrectly uses the TarotOracle.getResult function as the TWAP price, which disrupts the matching mechanism for lend and borrow orders.  

In the MixOracle.getThePrice function, the twapPrice112x112 is retrieved from the TarotOracle.getResult function. It then calculates the price of 1 token1 in USD using twapPrice112x112 and the price from the pyth oracle.

\u0060\u0060\u0060solidity
ITarotOracle priceFeed = ITarotOracle(_priceFeed);
address uniswapPair = AttachedUniswapPair[tokenAddress];
require(isFeedAvailable[uniswapPair], "Price feed not available");
(uint224 twapPrice112x112, ) = priceFeed.getResult(uniswapPair);
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
int amountOfAttached = int(
    (((2 ** 112)) * (10 ** decimalsToken1)) / twapPrice112x112
);
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
uint price = (uint(amountOfAttached) * uint(attachedTokenPrice)) /
    (10 ** decimalsToken1);
\u0060\u0060\u0060

The TarotOracle.getResult function returns the time-weighted average of reserve0 + price, rather than the TWAP price. Also, it does not synchronize with uniswapV2Pair.  

File: \u0060contracts/oracles/MixOracle/TarotOracle/TarotPriceOracle.sol\u0060

\u0060\u0060\u0060solidity
function getPriceCumulativeCurrent(
    address uniswapV2Pair
) internal view returns (uint256 priceCumulative) {
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
priceCumulative = IUniswapV2Pair(uniswapV2Pair)
                   .reserve0CumulativeLast();
(
    uint112 reserve0,
    uint112 reserve1,
    uint32 _blockTimestampLast
) = IUniswapV2Pair(uniswapV2Pair).getReserves();
uint224 priceLatest = UQ112x112.encode(reserve1).uqdiv(reserve0);
uint32 timeElapsed = getBlockTimestamp() - _blockTimestampLast; // overflow
→ is desired
// * never overflows, and + overflow is desired
priceCumulative += (uint256(priceLatest) * timeElapsed);
\u0060\u0060\u0060

This means that the twapPrice112x112 in the MixOracle.getThePrice function is not the correct TWAP price. Consequently, the DebitaV3Aggregator.matchOffersV3 uses an incorrect price to match lend and borrow orders.

A user creates the order with MixOracle.

1. None

None

The incorrect price from the MixOracle disrupts the matching mechanism for lend and borrow orders. This causes user\u0027s loss of funds.

Change the code in the MixOracle.getThePrice function to get the correct price from the uniswapV2Pair.

File: code\Debita-V3-Contracts\contracts\oracles\MixOracle\MixOracle.sol
\u0060\u0060\u0060solidity
function getThePrice(address tokenAddress) public returns (int) {
function getTotalPrice(address tokenAddress, address uniswapV2Pair) public returns (int, int) {
    // get tarotOracle address
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
address _priceFeed = AttachedTarotOracle[tokenAddress];
require(_priceFeed != address(0), "Price feed not set");
require(!isPaused, "Contract is paused");
ITarotOracle priceFeed = ITarotOracle(_priceFeed);
address uniswapPair = AttachedUniswapPair[tokenAddress];
require(isFeedAvailable[uniswapPair], "Price feed not available");
// get twap price from token1 in token0
(uint224 twapPrice112x112, ) = priceFeed.getResult(uniswapPair);
address attached = AttachedPricedToken[tokenAddress];
// Get the price from the pyth contract, no older than 20 minutes
// get usd price of token0
int attachedTokenPrice = IPyth(debitaPythOracle).getThePrice(attached);
uint decimalsToken1 = ERC20(attached).decimals();
uint decimalsToken0 = ERC20(tokenAddress).decimals();
// calculate the amount of attached token that is needed to get 1 token1
int amountOfAttached = int(
    (((2 ** 112)) * (10 ** decimalsToken1)) / twapPrice112x112
);
// calculate the price of 1 token1 in usd based on the attached token
uint price = (uint(amountOfAttached) * uint(attachedTokenPrice)) /
    (10 ** decimalsToken1);
require(price > 0, "Invalid price");
//       return int(uint(price));
uint wftmPrice = IUniswapV2Pair(uniswapV2Pair).current(tokenAddress, 1e18);
// uint realPrice = (uint(attachedTokenPrice)) * wftmPrice;
uint realPrice = (uint(attachedTokenPrice)) * wftmPrice / (10 ** decimalsToken1);
return (int(uint(price)), int(uint(realPrice)));
\u0060\u0060\u0060

And add the following testTotalPrice test function in the OracleTarotUSDCEQUAL.t.sol.
File: code\Debita-V3-Contracts\test\fork\Loan\ltv\Tarot-Fantom\OracleTarotUSDCEQUAL.t.sol

\u0060\u0060\u0060solidity
function testTotalPrice() public {
    IUniswapV2Pair(EQUALPAIR).sync();
    DebitaMixOracle.setAttachedTarotPriceOracle(EQUALPAIR);
    vm.warp(block.timestamp + 1201);
    IUniswapV2Pair(EQUALPAIR).sync();
    (int originPrice, int realPrice) = DebitaMixOracle.getTotalPrice(EQUAL, EQUALPAIR);
    console.logString(" price:");
    console.logUint(uint(originPrice));
    console.logString("actual price:");
}
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
console.logUint(uint(realPrice));
console.logString("price diff ratio:");
console.logUint(uint(originPrice / realPrice));
\u0060\u0060\u0060

Use the following command to test above function.
\u0060\u0060\u0060bash
forge test --rpc-url https://mainnet.base.org --match-path
→  test/fork/Loan/ltv/Tarot-Fantom/OracleTarotUSDCEQUAL.t.sol --match-test
→  testTotalPrice -vvv
\u0060\u0060\u0060

The result is as following:
\u0060\u0060\u0060
mix price:
147639521176897807
actual price:
926069876
price diff ratio:
159425897
\u0060\u0060\u0060

This indicates that the mix price is 147,639,521,176,897,807, while the actual price is 926,069,876. The mix price is significantly higher than the actual price.


It is recommended to change the code as following:
\u0060\u0060\u0060solidity
File: code\Debita-V3-Contracts\contracts\oracles\MixOracle\MixOracle.sol
function getThePrice(address tokenAddress) public returns (int) {
-       address _priceFeed = AttachedTarotOracle[tokenAddress];
-       require(_priceFeed != address(0), "Price feed not set");
-       require(!isPaused, "Contract is paused");
-       ITarotOracle priceFeed = ITarotOracle(_priceFeed);
-       address uniswapPair = AttachedUniswapPair[tokenAddress];
-       require(isFeedAvailable[uniswapPair], "Price feed not available");
-       (uint224 twapPrice112x112, ) = priceFeed.getResult(uniswapPair);
+       uint224 twapPrice112x112 =
→  uint224(IUniswapV2Pair(uniswapV2Pair).current(tokenAddress, 1e18));
        address attached = AttachedPricedToken[tokenAddress];
        // Get the price from the pyth contract, no older than 20 minutes
        // get usd price of token0
        int attachedTokenPrice = IPyth(debitaPythOracle).getThePrice(attached);
        uint decimalsToken1 = ERC20(attached).decimals();
        uint decimalsToken0 = ERC20(tokenAddress).decimals();
        // calculate the amount of attached token that is needed to get 1 token1
        int amountOfAttached = int(
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
(((2 ** 112)) * (10 ** decimalsToken1)) / twapPrice112x112
);
// calculate the price of 1 token1 in usd based on the attached token
uint price = (uint(amountOfAttached) * uint(attachedTokenPrice)) /
   (10 ** decimalsToken1);
require(price > 0, "Invalid price");
return int(uint(price));
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/febd7ff204f60af400  
cd4ff00706da0bb7d47609
## Issue M-15: MixOracle is broken due to hardcoded position

Source: [https://github.com/sherlock-audit/2024-10-debita-judging/issues/540](https://github.com/sherlock-audit/2024-10-debita-judging/issues/540)  
Found by: tjonair, xiaoming90  

No response  

No response  

No response  

No response  

Following is the information about MixOracle extracted from the Debita’s documentation for context:  
To integrate a token without a direct oracle, a mix oracle is utilized. This oracle uses a TWAP oracle to compute the conversion rate between Token A and Token B. Token B must be supported on PYTH oracle, and the pricing pool should have substantial liquidity to ensure security.  
This approach enables us to obtain the USD valuation of tokens that would otherwise be impossible.  

The following attempts to walk through how the MixOracle is used for reader understanding before jumping into the issue.  
WFTM token is supported on Pyth Oracle via the WFTM/USD price feed, but there is no oracle in Fantom Chain that supports EQUAL token. Thus, the MixOracle can be
Leveraged to provide the price of the EQUAL token even though no EQUAL price oracle exists. A pricing pool with substantial liquidity that consists of EQUAL token can be used here.

Let\u0027s use the WFTM/EQUAL pool (EQUALPAIR=0x3d6c56f6855b7Cc746fb80848755B0a9c3770122) from Equalizer within the test script for illustration.

[Link to Test Script](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/test/fork/Loan/ltv/Tarot-Fantom/OracleTarotUSDCEQUAL.t.sol#L138)

File: OracleTarotUSDCEQUAL.t.sol

\u0060\u0060\u0060solidity
function testUSDCPrincipleAndEqualCollateral() public {
    createOffers(USDC, EQUAL);
    DebitaMixOracle.setAttachedTarotPriceOracle(EQUALPAIR);
    vm.warp(block.timestamp + 1201);
    int priceEqual = DebitaMixOracle.getThePrice(EQUAL);
}
\u0060\u0060\u0060

The token0 and token1 of the WFTM/EQUAL pool are as follows as retrieved from the FTM scan:
- token0=0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83=WFTM
- token1=0x3Fd3A0c85B70754eFc07aC9Ac0cbBDCe664865A6=EQUAL

In this case, the price returned from the pool will be computed by EQUAL divided by WFTM. So, the price of EQUAL per WFTM is provided by the pool.

Equalizer Pool\u0027s \u0060getPriceCumulativeCurrent\u0060 = reserve1/reserve0 = token1/token0 = EQUAL/WFTM

When configuring the MixOracle to support EQUAL token, the \u0060setAttachedTarotPriceOracle\u0060 will be executed, and the pool address (0x3d6c56f6855b7Cc746fb80848755B0a9c3770122) will be passing in via the \u0060uniswapV2Pair\u0060 parameter. In this case, the MixOracle will return the price of the EQUAL (token1) token when the \u0060MixOracle.getThePrice(EQUAL)\u0060 function is executed within another part of the protocol.

\u0060\u0060\u0060solidity
AttachedPricedToken[token1] = token0;
AttachedPricedToken[EQUAL] = WFTM;
\u0060\u0060\u0060

[Link to MixOracle Contract](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/oracles/MixOracle/MixOracle.sol#L72)

File: MixOracle.sol

\u0060\u0060\u0060solidity
function setAttachedTarotPriceOracle(address uniswapV2Pair) public {
    require(multisig == msg.sender, "Only multisig can set price feeds");

    require(
        AttachedUniswapPair[uniswapV2Pair] == address(0),
        "Uniswap pair already set"
    );
}
\u0060\u0060\u0060
The issue is that the Mix Oracle relies on the position of token0 and token1 in the pool that cannot be controlled. Within the pool (Equalizer or Uniswap Pool), the position of token0 and token1 is pre-determined and sorted by the token\u0027s address (smaller address will always be token0). 

However, the position of the token in the set AttachedTarotPriceOracle function is hardcoded. For instance, the keys of the AttachedUniswapPair, AttachedTarotOracle, AttachedPricedToken mapping are all hardcoded to token1.

Assume that the protocol wants to create another Mix Oracle to support another token called Token that doesn\u0027t have any oracle on Fantom. However, this token to be supported is located in the position of token0 instead of token1 in the pool. Thus, because the Mix Oracle is hardcoded to always use only token1, there is no way to support this Token even though a high liquidity pool that consists of Token exists on Fantom.

The Mix Oracle is supposed to work in this scenario, but due to hardcoded position, it cannot be supported. Thus, the Mix Oracle is broken in this scenario.

Medium. Breaks core contract functionality. Oracle is a core feature in a protocol.

No response

Consider not hardcoding the position (token1) as the key of the mapping used within MixOracle. Instead, allow the deployer to specify which token (token0 or token1) the MixOracle is supposed to support.


sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/83b5cf41c6100a4b31be2779bb66e7c41ea957a6
## IssueM-16: Users can be griefed due to lack of minimum size within the Loan and Offer

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/557)  
Found by: xiaoming90  

No response  

No response  

No response  

No response  

Assume that Bob creates a borrow offer with 10000 AERO as collateral to borrow 10000 USDC at the price/ratio of 1 AERO:1 USDC for simplicity\u0027s sake. Malicious aggregator (aggregator is a public role and anyone can match orders) can perform griefing attacks against Bob. The malicious aggregator can create many individual loans OR many loans with many offers within it, OR a combination of both. Each loan and offer will be small or tiny and consist of Bob\u0027s borrow order. This can be done because the protocol does not enforce any restriction on the minimum size of the loan or offer. As a result, Bob\u0027s borrow offer could be broken down into countless (e.g., thousands or millions) of loans and offers. As a result, Bob will not be able to keep track of all the loans and offers belonging to him and will have issues paying the debtor claiming collateral.
This issue is also relevant to the lenders, and the impact is even more serious as lenders have to perform more actions against loans and offers, such as claiming debt, claiming interest, claiming collateral, or auctioning off defaulted collateral etc. In addition, it also requires lenders and borrowers to pay a significant amount of gas fees in order to carry out the actions mentioned previously. As a result, this effectively allows malicious aggregators to grief lenders and borrowers. 

[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Aggregator.sol#L167)

Malicious aggregators to grief lenders and borrowers.

No response

Having a maximum number of offers (e.g., 100) within a single loan is insufficient to guard against this attack because malicious aggregators can simply work around this restriction by creating more loans. Thus, it is recommended to impose the minimum size for each loan and/or offer, so that malicious aggregators cannot create many small/tiny loans and offers to grief the users.

sherlock-admin2

The protocol team fixed this issue in the following PRs/commits: [Link to Commit](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/c7567f5dbd9d8e224e6e3a684cc396a3829775e1)
## Issue M-17: Borrower can obtain principle tokens without paying collateral tokens

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/558)  
Found by: xiaoming90  

No response  

No response  

No response  

No response  

Assume that the ratio/price is 1e18 (1 XYZ per ABC => Principle per Collateral). XYZ is 18 decimals while ABC is 6 decimals. Assume that Bob (malicious borrower) calls the permissionless DebitaV3Aggregator.matchOffersV3 function. The amount of collateral deducted from Bob\u0027s borrow offer is calculated via the following:

\u0060\u0060\u0060solidity
userUsedCollateral = (lendAmountPerOrder[i] * (10 ** decimalsCollateral)) / ratio;
userUsedCollateral = (lendAmountPerOrder[i] * 1e6) / 1e18;
\u0060\u0060\u0060

[File: DebitaV3Aggregator.sol](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Aggregator.sol#L467)  
\u0060\u0060\u0060solidity
274:  function matchOffersV3(
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// calculate the amount of collateral used by the lender
uint userUsedCollateral = (lendAmountPerOrder[i] *
     (10 ** decimalsCollateral)) / ratio;
\u0060\u0060\u0060

For lendAmountPerOrder, he uses a value that is small enough to trigger a rounding to zero error. The range of lendAmountPerOrder that will cause userUsedCollateral to round down to zero is:
0 ≤ lendAmountPerOrder < 10^12

Thus, for each offer, Bob will specify the lendAmountPerOrder[i] to be 1e12 - 1. Thus, for each offer, he will be able to obtain 1e12 - 1 XYZ tokens without paying a single ABC token as collateral.

This attack is profitable because each matchOffersV3 transaction can execute up to 100 offers, and the protocol is intended to be deployed on L2 chains where gas fees are extremely cheap or even negligible.

[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Aggregator.sol#L290)

File: DebitaV3Aggregator.sol

\u0060\u0060\u0060solidity
function matchOffersV3(
    // check lendOrder length is less than 100
    require(lendOrders.length <= 100, "Too many lend orders");
\u0060\u0060\u0060

Following is the extract from Contest’s README showing that the protocol will be deployed to the following L2 chains.

Q: On what chains are the smart contracts going to be deployed?  
A: Sonic (Prev. Fantom), Base, Arbitrum & OP

High. Loss of assets.

No response.

This issue can be easily mitigated by implementing the following changes to prevent the above attack.
\u0060\u0060\u0060solidity
// calculate the amount of collateral used by the lender
uint userUsedCollateral = (lendAmountPerOrder[i] * (10 ** decimalsCollateral)) /
    ratio;
require(userUsedCollateral > 0, "userUsedCollateral is zero")
\u0060\u0060\u0060

Discussion
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [GitHub Commit](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/a60b40e8b76b7d23cff1e7ef8310819ad251f0e3)
## Issue M-18: Incentive Creator\u0027s Tokens Permanently Locked in Zero-Activity Epochs

Source: [GitHub Issue #616](https://github.com/sherlock-audit/2024-10-debita-judging/issues/616)

The protocol has acknowledged this issue.

Found by: 0x37, BengalCatBalu, KaplanLabs, dimulski, h4rs0n, jo13, newspacexyz, t.aksoy, xiaoming90


The lack of token recovery mechanism in DebitaIncentives.sol will cause permanent loss of incentive tokens for incentive creators as tokens remain locked in the contract during epochs with zero lending/borrowing activity.


In DebitaIncentives.sol, the incentivizePair function transfers tokens to the contract without any recovery mechanism:

\u0060\u0060\u0060solidity
// transfer the tokens
IERC20(incentivizeToken).transferFrom(
  msg.sender,
  address(this),
  amount
);
// add the amount to the total amount of incentives
if (lendIncentivize[i]) {
  lentIncentivesPerTokenPerEpoch[principle][
    hashVariables(incentivizeToken, epoch)
  ] += amount;
} else {
  borrowedIncentivesPerTokenPerEpoch[principle][
    hashVariables(incentivizeToken, epoch)
  ] += amount;
}
\u0060\u0060\u0060

This means that incentive creators can only deposit incentives for epochs that haven\u0027t started yet, and the incentives are locked in the contract until the epoch ends. Once tokens are transferred, they become permanently locked if no activity occurs in that epoch.
epoch. This is a serious design flaw since market conditions are unpredictable and zero-activity epochs are likely to occur.

1. Incentive creator needs to call \u0060incentivizePair()\u0060 to deposit incentive tokens for a future epoch
2. \u0060totalUsedTokenPerEpoch[principle][epoch]\u0060 needs to be exactly 0
3. No users perform any lending or borrowing actions during the specified epoch

1. Market conditions lead to zero lending/borrowing activity during the incentivized epoch

1. Incentive creator calls \u0060incentivizePair()\u0060 to set up incentives for a future epoch, transferring tokens to the contract
2. The epoch passes with no lending or borrowing activity
3. No users can claim the incentives as there are no qualifying actions (lentAmountPerUserPerEpoch and borrowAmountPerEpoch remain 0)
4. The tokens remain permanently locked in the contract as there is no withdrawal or recovery mechanism

The incentive creators suffer a complete loss of their deposited tokens for that epoch. The tokens become permanently locked in the contract with no mechanism for recovery or redistribution to future epochs. This could lead to significant financial losses.

No response

Add a recovery mechanism that allows incentive creators to withdraw unclaimed tokens after an epoch ends. This should only be possible if the epoch had zero activity.
## Issue M-19: An attacker can steal the entire borrow and lending incentive of an epoch with FLASH LOAN in a single transaction

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/708)  
Found by: BengalCatBalu, CL001, Feder, KaplanLabs, KlosMitSoss, Pablo, bbl4de, dimulski, lanrebayode77, mike-watson, pashap9990, tjonair, xiaoming90

An attacker, with the aid of flash-loan can steal the entire borrow and lending incentives. This involves the attacker creating a huge lend offer with funds from flash-loan, creating a borrow offer with dust amount as collateral, self-matching the offer, paying back the loan in the same block (with zero interest) and having extra principal to pay back flash-loan fees, then claim the entire incentive after the epoch has ended.

1. Same address can be the borrower, lender and connector; there is no check against this.
2. DebitaV3Loan.payDebt() allows repayment of loan in the same block it was taken. (Allows the use of flash-loan to access huge funds!)
3. Lender can set ratio high enough to allow borrower to take huge loan with dust collateral (1 wei). (This reduces flash-loan needed as 1 wei can be used as collateral to get unlimited principal amount, reduce fees (flash-loan) and make attack more feasible/profitable).

Incentive is huge enough to cover attack expenses (flash-loan fees, loan disbursement fee and off-cus gas fee!)
1. Attacker has extra principle to cover flash-loan fees (0.05% in Aave V3).
2. Attack capital becomes lower when the borrow/lend in the current epoch is low.

1. Attacker takes into account the amount of incentives and total borrow/lend of the current epoch to determine profitability and also to know if there is capital (flash-loan fee).
2. Attacker takes flash-loan, in the flash loan call-back.
3. A block to the end of an epoch, creates a lend offer with HUGE ratio! (100e24 for instance) allowing borrowing huge amounts with 1 wei, no check/limit for this.
4. Creates a borrow offer using 1 wei as collateral.
5. Calls \u0060matchOfferV3()\u0060, matching the offers, min fee of 0.2% is deducted in which 15% of it goes back to attacker, so only 0.17% net paid as fees.
6. Pays back by calling \u0060payDebt()\u0060, offcus no fee on interests since Apr is set to zero.
7. Pays back flash-loan and fees.
8. Epoch ends, and attacker claims almost all incentives (borrow + lend) in the next block (after the end of the epoch), since lent and borrowed will be almost 100%, thanks to FLASH-LOAN!

Attackers steal larger share of incentives.

Repayment is possible in the same block! The only time check is for deadline.
\u0060\u0060\u0060solidity
// check next deadline
require(
    nextDeadline() >= block.timestamp,
    "Deadline passed to pay Debt"
);
\u0060\u0060\u0060
[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L186-L257)
\u0060\u0060\u0060solidity
} else {
    maxRatio = lendInfo.maxRatio[collateralIndex]; //@audit attacker set
    // this to be large to allow the use of dust collateral
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// calculate ratio based on porcentage of the lend order
uint ratio = (maxRatio * porcentageOfRatioPerLendOrder[i]) / 10000;
uint m_amountCollateralPerPrinciple = amountCollateralPerPrinciple[
    principleIndex
];
// calculate the amount of collateral used by the lender
uint userUsedCollateral = (lendAmountPerOrder[i] *
    (10 ** decimalsCollateral)) / ratio; //@audit collateral required for
// check ratio for each principle and check if the ratios are within the limits of
for (uint i = 0; i < principles.length; i++) {
    require(
        weightedAverageRatio[i] >= //@audit attacker set both, so this aligns!
            ((ratiosForBorrower[i] * 9800) / 10000) &&
            weightedAverageRatio[i] <=
            (ratiosForBorrower[i] * 10200) / 10000,
        "Invalid ratio"
    );
// check if the apr is within the limits of the borrower
    require(weightedAverageAPR[i] <= borrowInfo.maxApr, "Invalid APR");
    //@audit Apr is set to zero, so no fee on interest!
}
\u0060\u0060\u0060

1. Prevent repaymentinthesameblock
2. It might be helpful to prevent lender == borrower == connector

sherlock-admin2
TheprotocolteamfixedthisissueinthefollowingPRs/commits:
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/bc889a3d624b8376c9be43f5421a78448bdaca20
## IssueM-20: LoanExtensionFailsDuetoUnusedTimeCalculation

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/766)

Found by:  
0x37, 0xPhantom2, 0xmujahid002, Audinarey, BengalCatBalu, Falendar, Honour, dany.armstrong90, dimulski, jsmi, mladenov, moray5554, newspacexyz, nikhil840096, nikhilx0111, yovchev_yoan, zkillua


The extendLoan function in DebitaV3Loan::extendLoan has redundant time calculation logic that causes transaction reversions when borrowers attempt to extend loans near their deadline.


In the DebitaV3Loan contract, the function extendLoan has a variable extendedTime that is not used and can cause reverts in some cases, which causes some borrowers to not be able to extend their loan.

The exact line of code:  
[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L590)


1. Loan must not be already extended (extended == false)
2. Borrower must have waited minimum duration (10% of initial duration)
3. Loan must not be expired (nextDeadline() > block.timestamp)
4. Must have at least one unpaid offer


1. Current time must be close to offer\u0027s maxDeadline
2. maxDeadline - (block.timestamp - startedAt) - block.timestamp < 0
1. Loan starts at timestamp 1704067200 (January 1, 2024)
2. Time advances to 1705190400 (January 14, 2024)
3. Borrower attempts to extend loan
4. For an offer with maxDeadline 1705276800 (January 15, 2024)
5. Transaction reverts due to arithmetic underflow

Borrowers cannot extend loans near their deadlines even when they satisfy all other requirements:
1. Forces unnecessary defaults near deadline
2. Wastes gas on failed extension attempts
3. Disrupts normal loan management operations

This PoC demonstrates the reversion caused by unused time calculations in extendLoan function.

\u0060\u0060\u0060solidity
contract BugPocTime {
    uint256 loanStartedAt = 1704067200; // 1 January 00:00 time
    uint256 currentTime = 1705190400; // 14 January 00:00 time
    uint256 maxDeadline = 1705276800; // 15 January 00:00 time
    function extendLoan() public view returns(uint256){
        uint256 alreadyUsedTime = currentTime - loanStartedAt;
        uint256 extendedTime = maxDeadline - alreadyUsedTime - currentTime;
        return 10;
    }
}
\u0060\u0060\u0060

The example uses the following timestamps:
1. loanStartedAt: 1704067200 (Jan 1, 2024 00:00)
2. currentTime: 1705190400 (Jan 14, 2024 00:00)
3. maxDeadline: 1705276800 (Jan 15, 2024 00:00)

The calculation flow:
1. alreadyUsedTime=1705190400-1704067200=1,123,200(￿13days)  
2. extendedTime=1705276800-1,123,200-1705190400=1705276800-1706313600=  
   -1,036,800 (reverts due to underflow)  

Remove the unused extendedTime calculation as it serves no purpose and can cause legitimate loan extensions to fail.  

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/dd1ad26725ba4835bc6406acf1289c1fbd33f8f2](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/dd1ad26725ba4835bc6406acf1289c1fbd33f8f2)
## IssueM-21: DebitaIncentives::updateFunds

will exit prematurely and not update whitelisted pairs causing loss of funds to lenders and borrowers  
Source: [https://github.com/sherlock-audit/2024-10-debita-judging/issues/870](https://github.com/sherlock-audit/2024-10-debita-judging/issues/870)  
Found by  
0x37, 0xe4669da, 0xloscar01, BengalCatBalu, DenTonylifer, ExtraCaterpillar, Honour, Pro_King, Ryonen, bbl4de, dimulski, jjk, jsmi, liquidbuddha, merlin, newspacexyz, robertodf, t.aksoy, tmotfl  

The DebitaIncentives::updateFunds function iterates over the lenders array, verifying whether the principle and collateral pair for each lend offer is whitelisted. If a non-whitelisted pair is encountered, the function exits prematurely, causing it to skip the processing of all subsequent pairs, even if they are valid and whitelisted. This causes the loss of potential funds for lenders and borrowers, as they would have been eligible to claim incentives had the function processed all valid pairs. Specifically, the lentAmountPerUserPerEpoch, totalUsedTokenPerEpoch, and borrowAmountPerEpoch mappings are not updated.  

In DebitaIncentives.sol#L317 the return keyword is used, stopping the entire function, not just the iteration, ignoring the subsequent elements in the informationOffers array.  

- At least one lend offer be active with the following conditions (non-whitelisted pair lend offer):  
  - principle and accepted Collaterals pair is not whitelisted in the DebitaIncentives contract.  
  - lonelyLender must be false.  
  - availableAmount is greater than 0.
- At least one lend offer be active with the following conditions (whitelisted pair lend offer):
  - principle and accepted Collaterals pair is whitelisted in the Debita Incentives contract.
  - lonely Lender must be false.
  - available Amount is greater than 0.
  
- At least one borrow order must be active with the following conditions:
  - accepted Principles must include at least a whitelisted principle and at least a non-whitelisted principle.
  - collateral when paired with the principle, it must be whitelisted.
  - available Amount is greater than 0.
  
- The terms of the borrow order must allow it to be successfully matched with both types of lend offers in a single DebitaV3Aggregator::matchOffersV3 call.
- DebitaV3Aggregator must not be paused.

No response

1. Debita Incentives contract owner whitelists pair of principle and collateral calling DebitaIncentives::whitelListCollateral
2. A user calls DebitaIncentives::incentivizePair to incentivize the already whitelisted principle. This function transfers the tokens given as incentives from the user to the DebitaIncentives contract. The amount of incentives is updated:

   \u0060\u0060\u0060solidity
   if (lendIncentivize[i]) {
     lentIncentivesPerTokenPerEpoch[principle][
        hashVariables(incentivizeToken, epoch)
     ] += amount;
   } else {
     borrowedIncentivesPerTokenPerEpoch[principle][
        hashVariables(incentivizeToken, epoch)
     ] += amount;
   }
   \u0060\u0060\u0060
Another user calls \u0060DebitaV3Aggregator::matchOffersV3\u0060 to match a previously created borrow order with one lend offer that has a non-whitelisted pair and another lend offer that has a whitelisted pair. Inside \u0060matchOffersV3\u0060, the \u0060DebitaIncentives::updateFunds\u0060 function is called to update the funds of the lenders and borrowers. The \u0060offers\u0060 array contains the principle of each accepted lend offer, and it is passed as an argument.

[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Aggregator.sol#L631-L636)

\u0060\u0060\u0060solidity
DebitaIncentives(s_Incentives).updateFunds(
    offers,
    borrowInfo.collateral,
    lenders,
    borrowInfo.owner
);
\u0060\u0060\u0060

The \u0060updateFunds\u0060 function iterates over the array and checks if the principle and collateral pair is whitelisted. If the pair is not whitelisted, the return keyword halts the entire function. The offer containing the non-whitelisted principle is at index 0, so the function stops before the iteration reaches the offer at index 1 that has the whitelisted principle. This stops \u0060lentAmountPerUserPerEpoch\u0060, \u0060totalUsedTokenPerEpoch\u0060, and \u0060borrowAmountPerEpoch\u0060 from being updated.

[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaIncentives.sol#L306-L341)

\u0060\u0060\u0060solidity
function updateFunds(
    infoOfOffers[] memory informationOffers,
    address collateral,
    address[] memory lenders,
    address borrower
) public onlyAggregator {
    for (uint i = 0; i < lenders.length; i++) {
        bool validPair = isPairWhitelisted[informationOffers[i].principle][collateral];
        if (!validPair) {
            return;
        }
        address principle = informationOffers[i].principle;
        uint _currentEpoch = currentEpoch();
        lentAmountPerUserPerEpoch[lenders[i]][hashVariables(principle, _currentEpoch)] += informationOffers[i].principleAmount;
    }
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
totalUsedTokenPerEpoch[principle][
  _currentEpoch
] += informationOffers[i].principleAmount;
borrowAmountPerEpoch[borrower][
  hashVariables(principle, _currentEpoch)
] += informationOffers[i].principleAmount;
emit UpdatedFunds(
  lenders[i],
  principle,
  collateral,
  borrower,
  _currentEpoch
);
\u0060\u0060\u0060

Asthemappingsarenotupdated,thebeneficiarylenderorborrowercan\u0027tclaimthe incentives:

\u0060\u0060\u0060solidity
uint lentAmount = lentAmountPerUserPerEpoch[msg.sender][
  hashVariables(principle, epoch)
];
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
uint borrowAmount = borrowAmountPerEpoch[msg.sender][
  hashVariables(principle, epoch)
];
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
require(
  borrowAmount > 0 || lentAmount > 0,
  "No borrowed or lent amount"
);
\u0060\u0060\u0060

Impact  
Permanentlossoffundsforlendersandborrowerswhowouldhavebeeneligibletoclaim incentives for a given epoch.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import {Test, console} from "forge-std/Test.sol";
import {stdError} from "forge-std/StdError.sol";
import {DLOImplementation} from "@contracts/DebitaLendOffer-Implementation.sol";
import {DLOFactory} from "@contracts/DebitaLendOfferFactory.sol";
import {DBOImplementation} from "@contracts/DebitaBorrowOffer-Implementation.sol";
import {DBOFactory} from "@contracts/DebitaBorrowOffer-Factory.sol";
import {DebitaV3Aggregator} from "@contracts/DebitaV3Aggregator.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {DebitaIncentives} from "@contracts/DebitaIncentives.sol";
import {Ownerships} from "@contracts/DebitaLoanOwnerships.sol";
import {auctionFactoryDebita} from "@contracts/auctions/AuctionFactory.sol";
import {DebitaV3Loan} from "@contracts/DebitaV3Loan.sol";
import {DynamicData} from "../interfaces/getDynamicData.sol";

contract UpdateFundsTest is Test {
    DBOFactory public DBOFactoryContract;
    DLOFactory public DLOFactoryContract;
    Ownerships public ownershipsContract;
    DebitaIncentives public incentivesContract;
    DebitaV3Aggregator public DebitaV3AggregatorContract;
    auctionFactoryDebita public auctionFactoryDebitaContract;
    DebitaV3Loan public DebitaV3LoanContract;
    ERC20Mock public AEROContract;
    ERC20Mock public USDCContract;
    ERC20Mock public wETHContract;
    DLOImplementation public LendOrder;
    DBOImplementation public BorrowOrder;
    DynamicData public allDynamicData;
    address USDC;
    address wETH;
    address AERO;
    address borrower = address(0x2);
    address lender1 = address(0x3);
    address lender2 = address(0x4);
    address feeAddress = address(this);

    function setUp() public {
        allDynamicData = new DynamicData();
        ownershipsContract = new Ownerships();
        incentivesContract = new DebitaIncentives();
        DBOImplementation borrowOrderImplementation = new DBOImplementation();
\u0060\u0060\u0060
DBOFactoryContract = new DBOFactory(address(borrowOrderImplementation));
DLOImplementation proxyImplementation = new DLOImplementation();
DLOFactoryContract = new DLOFactory(address(proxyImplementation));
auctionFactoryDebitaContract = new auctionFactoryDebita();
USDCContract = new ERC20Mock();
wETHContract = new ERC20Mock();
AEROContract = new ERC20Mock();
DebitaV3Loan loanInstance = new DebitaV3Loan();
DebitaV3AggregatorContract = new DebitaV3Aggregator(
  address(DLOFactoryContract),
  address(DBOFactoryContract),
  address(incentivesContract),
  address(ownershipsContract),
  address(auctionFactoryDebitaContract),
  address(loanInstance)
);
USDC = address(USDCContract);
wETH = address(wETHContract);
AERO = address(AEROContract);
wETHContract.mint(lender1, 5 ether);
AEROContract.mint(lender2, 5 ether);
USDCContract.mint(borrower, 10 ether);
USDCContract.mint(address(this), 100 ether);
ownershipsContract.setDebitaContract(
  address(DebitaV3AggregatorContract)
);
incentivesContract.setAggregatorContract(
  address(DebitaV3AggregatorContract)
);
DLOFactoryContract.setAggregatorContract(
  address(DebitaV3AggregatorContract)
);
DBOFactoryContract.setAggregatorContract(
  address(DebitaV3AggregatorContract)
);
auctionFactoryDebitaContract.setAggregator(
  address(DebitaV3AggregatorContract)
);
// Given the condition in the DebitaIncentives::updateFunds function:
\u0060\u0060\u0060solidity
function updateFunds(
    infoOfOffers[] memory informationOffers,
    address collateral,
    address[] memory lenders,
    address borrower
) public onlyAggregator {
    for (uint i = 0; i < lenders.length; i++) {
        bool validPair = isPairWhitelisted[informationOffers[i].principle][
            collateral
        ];
        if (!validPair) {
            return; // <------ Stops the entire function, not just the iteration
        }
\u0060\u0060\u0060

This test demonstrates that the DebitaIncentives::updateFunds function terminates prematurely when processing the \u0060informationOffers\u0060 array if any element contains a non-whitelisted pair of principle and collateral. As a result, all subsequent elements in the array are ignored, even if they are valid and whitelisted.

Example scenario with an array of 4 elements:
- Index 0: Whitelisted pair
- Index 1: Non-whitelisted pair
- Index 2: Whitelisted pair
- Index 3: Whitelisted pair

The function processes the first element, but terminates upon encountering the non-whitelisted pair at index 1, skipping the valid pairs at indexes 2 and 3.

In the test, the following scenario is replicated:
- Index 0: Non-whitelisted pair
- Index 1: Whitelisted pair

Because the first element (Index 0) contains a non-whitelisted pair, the function terminates and skips the valid whitelisted pair at Index 1.

Steps:
1. Whitelist a pair of principle and collateral. (AERO, USDC)
2. Incentivize the whitelisted pair.
3. Create two lending offers:
   - One with a non-whitelisted pair. (wETH, USDC)
   - One with the whitelisted pair. (AERO, USDC)
4. Create a borrow order in which the accepted principles are wETH and AERO and the collateral is USDC.
5. Call \u0060matchOffersV3\u0060 to match the borrow order with the lending offers.
6. Observe that no updates occur in the DebitaIncentives contract because the function exits prematurely upon encountering the non-whitelisted pair.

This behavior highlights an issue: valid pairs that occur after a non-whitelisted pair.
\u0060\u0060\u0060solidity
// in the array are not processed due to the premature return.
function testUpdateFunds() public {
   bool[] memory oraclesActivated = allDynamicData.getDynamicBoolArray(2);
   uint[] memory ltvs = allDynamicData.getDynamicUintArray(2);
   uint[] memory ratio = allDynamicData.getDynamicUintArray(2);
   uint[] memory ratioLenders = allDynamicData.getDynamicUintArray(1);
   uint[] memory ltvsLenders = allDynamicData.getDynamicUintArray(1);
   bool[] memory oraclesActivatedLenders = allDynamicData
     .getDynamicBoolArray(1);
   address[] memory acceptedPrinciples = allDynamicData
     .getDynamicAddressArray(2);
   address[] memory acceptedCollaterals = allDynamicData
     .getDynamicAddressArray(1);
   address[] memory oraclesCollateral = allDynamicData
     .getDynamicAddressArray(1);
   address[] memory oraclesPrinciples = allDynamicData
     .getDynamicAddressArray(2);
   address[] memory incentivizedPrinciples = allDynamicData
     .getDynamicAddressArray(1);
   address[] memory incentiveTokens = allDynamicData
     .getDynamicAddressArray(1);
   bool[] memory lendIncentivize = allDynamicData.getDynamicBoolArray(1);
   uint[] memory incentiveAmounts = allDynamicData.getDynamicUintArray(1);
   uint[] memory incentiveEpochs = allDynamicData.getDynamicUintArray(1);
   ratioLenders[0] = 1e18;
   ratio[0] = 1e18;
   ratio[1] = 1e18;
   acceptedPrinciples[0] = wETH;
   acceptedPrinciples[1] = AERO;
   acceptedCollaterals[0] = USDC;
   oraclesActivated[0] = false;
   oraclesActivated[1] = false;
   incentivizedPrinciples[0] = AERO;
   incentiveTokens[0] = USDC;
   lendIncentivize[0] = true;
   incentiveAmounts[0] = 100 ether;
   incentiveEpochs[0] = 2;
   // 1. Whitelist a pair of principle and collateral (AERO, USDC)
   incentivesContract.whitelListCollateral({
     _principle: AERO,
     _collateral: USDC,
     whitelist: true
   });
   // Check if pair is whitelisted
   assertEq(
     incentivesContract.isPairWhitelisted(AERO, USDC),
     true,
\u0060\u0060\u0060
## Pair should be whitelisted

\u0060\u0060\u0060solidity
// Check that wETH USDC pair is not whitelisted
assertEq(
  incentivesContract.isPairWhitelisted(wETH, USDC),
  false,
  "Pair should not be whitelisted"
);
// 2. Incentivize the whitelisted pair
USDCContract.approve(address(incentivesContract), 100 ether);
incentivesContract.incentivizePair({
  principles: incentivizedPrinciples,
  incentiveToken: incentiveTokens,
  lendIncentivize: lendIncentivize,
  amounts: incentiveAmounts,
  epochs: incentiveEpochs
});
// Check state changes
{
  assertEq(incentivesContract.principlesIncentivizedPerEpoch(2), 1);
  assertEq(incentivesContract.hasBeenIndexed(2, AERO), true);
  assertEq(incentivesContract.epochIndexToPrinciple(2, 0), AERO);
  assertEq(incentivesContract.hasBeenIndexedBribe(2, USDC), true);
  //keccak256(principle address, index)
  bytes32 hash = incentivesContract.hashVariables(AERO, 0);
  assertEq(
    incentivesContract.SpecificBribePerPrincipleOnEpoch(2, hash),
    USDC
  );
  //keccack256(bribe token, epoch)
  bytes32 hashLend2 = incentivesContract.hashVariables(USDC, 2);
  assertEq(
    incentivesContract.lentIncentivesPerTokenPerEpoch(
      AERO,
      hashLend2
    ),
    100 ether
  );
  assertEq(
    USDCContract.balanceOf(address(incentivesContract)),
    100 ether
  );
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// 3. Create a lend offer with non-whitelisted pair (wETH, USDC)
vm.startPrank(lender1);
wETHContract.approve(address(DLOFactoryContract), 5e18);
address lendOffer1 = DLOFactoryContract.createLendOrder({
    _perpetual: false,
    _oraclesActivated: oraclesActivatedLenders,
    _lonelyLender: false,
    _LTVs: ltvsLenders,
    _apr: 1000,
    _maxDuration: 8640000,
    _minDuration: 86400,
    _acceptedCollaterals: acceptedCollaterals,
    _principle: wETH,
    _oracles_Collateral: oraclesCollateral,
    _ratio: ratioLenders,
    _oracleID_Principle: address(0x0),
    _startedLendingAmount: 5e18
});
// Create a lend offer with whitelisted pair (AERO, USDC)
vm.startPrank(lender2);
AEROContract.approve(address(DLOFactoryContract), 5e18);
address lendOffer2 = DLOFactoryContract.createLendOrder({
    _perpetual: false,
    _oraclesActivated: oraclesActivatedLenders,
    _lonelyLender: false,
    _LTVs: ltvsLenders,
    _apr: 1000,
    _maxDuration: 8640000,
    _minDuration: 86400,
    _acceptedCollaterals: acceptedCollaterals,
    _principle: AERO,
    _oracles_Collateral: oraclesCollateral,
    _ratio: ratioLenders,
    _oracleID_Principle: address(0x0),
    _startedLendingAmount: 5e18
});
// 4. Create a borrow offer with accepted principles wETH and AERO and collateral USDC
vm.startPrank(borrower);
USDCContract.approve(address(DBOFactoryContract), 10e18);
address borrowOrderAddress = DBOFactoryContract.createBorrowOrder({
    _oraclesActivated: oraclesActivated,
    _LTVs: ltvs,
    _maxInterestRate: 1400,
    _duration: 864000,
    _acceptedPrinciples: acceptedPrinciples,
\u0060\u0060\u0060
_collateral: USDC,
             _isNFT: false,
             _receiptID: 0,
             _oracleIDS_Principles: oraclesPrinciples,
             _ratio: ratio,
             _oracleID_Collateral: address(0x0),
             _collateralAmount: 10e18
           });
           vm.stopPrank();
           // 5. Call mathOffersV3 to match the borrow order with the lending offers
           address[] memory lendOrders = new address[](2);
           uint[] memory lendAmounts = allDynamicData.getDynamicUintArray(2);
           uint[] memory percentagesOfRatio = allDynamicData.getDynamicUintArray(
             2
           );
           uint[] memory indexForPrinciple_BorrowOrder = allDynamicData
             .getDynamicUintArray(2);
           uint[] memory indexForCollateral_LendOrder = allDynamicData
             .getDynamicUintArray(2);
           uint[] memory indexPrinciple_LendOrder = allDynamicData
             .getDynamicUintArray(2);
           indexForPrinciple_BorrowOrder[0] = 0;
           indexForPrinciple_BorrowOrder[1] = 1;
           indexForCollateral_LendOrder[0] = 0;
           indexForCollateral_LendOrder[1] = 0;
           indexPrinciple_LendOrder[0] = 0;
           indexPrinciple_LendOrder[1] = 1;
           lendOrders[0] = lendOffer1;
           lendOrders[1] = lendOffer2;
           percentagesOfRatio[0] = 10000;
           percentagesOfRatio[1] = 10000;
           lendAmounts[0] = 5e18;
           lendAmounts[1] = 5e18;
           // Advance time to the next epoch (2)
           vm.warp(incentivesContract.epochDuration() + block.timestamp);
           assertEq(incentivesContract.currentEpoch(), 2);
           address deployedLoan = DebitaV3AggregatorContract.matchOffersV3({
             lendOrders: lendOrders,
             lendAmountPerOrder: lendAmounts,
             porcentageOfRatioPerLendOrder: percentagesOfRatio,
             borrowOrder: borrowOrderAddress,
             principles: acceptedPrinciples,
             indexForPrinciple_BorrowOrder: indexForPrinciple_BorrowOrder,
             indexForCollateral_LendOrder: indexForCollateral_LendOrder,
             indexPrinciple_LendOrder: indexPrinciple_LendOrder
           });
6. Check that the lend offer with the whitelisted pair has not been updated

\u0060\u0060\u0060solidity
{
    bytes32 hashPrincipleEpoch = incentivesContract.hashVariables(
        AERO,
        2
    );
    uint256 lentAmountPerUserPerEpoch = incentivesContract
        .lentAmountPerUserPerEpoch(lender2, hashPrincipleEpoch);
    console.log(
        "lentAmountPerUserPerEpoch: ",
        lentAmountPerUserPerEpoch
    );
    uint256 totalUsedTokenPerEpoch = incentivesContract
        .totalUsedTokenPerEpoch(AERO, 2);
    console.log("totalUsedTokenPerEpoch: ", totalUsedTokenPerEpoch);
    uint256 borrowAmountPerEpoch = incentivesContract
        .borrowAmountPerEpoch(borrower, hashPrincipleEpoch);
    console.log("borrowAmountPerEpoch: ", borrowAmountPerEpoch);
    // Advance time to the next epoch (3)
    vm.warp(incentivesContract.epochDuration() + block.timestamp);
    assertEq(incentivesContract.currentEpoch(), 3);
    address[] memory principles = new address[](1);
    principles[0] = AERO;
    address[][] memory tokensIncentives = new address[][](1);
    tokensIncentives[0] = new address[](1);
    tokensIncentives[0][0] = USDC;
    // Lender2 can\u0027t claim the incentives because the funds were not updated
    vm.startPrank(lender2);
    if (lentAmountPerUserPerEpoch == 0) {
        vm.expectRevert("No borrowed or lent amount");
        incentivesContract.claimIncentives({
            principles: principles,
            tokensIncentives: tokensIncentives,
            epoch: 2
        });
    }
    // else statement will only execute AFTER mitigation (changing
    // DebitaIncentives::updateFunds \u0060if (!validPair) return;\u0060 to \u0060if (!validPair)
    // continue;\u0060)
    else {
        incentivesContract.claimIncentives({
            principles: principles,
            tokensIncentives: tokensIncentives,
\u0060\u0060\u0060
epoch: 2
});
assertEq(USDCContract.balanceOf(lender2), 100 ether); // After
→ mitigation, lender2 can claim the incentives. Before mitigation, lender2 loses
→ his incentives
}
}
}
}
Logs
lentAmountPerUserPerEpoch:   0
totalUsedTokenPerEpoch: 0
borrowAmountPerEpoch:   0
Stepstoreproduce:
1. CreateafileUpdateFundsTest.t.solinsideDebita-V3-Contracts/test/local/ and
   pastethePoCcode.
2. Runthetestintheterminalwiththefollowingcommand:
forge test --mt testUpdateFunds -vv
Mitigation
ChangethereturnkeywordinDebitaIncentives::addFunds
function updateFunds(
       infoOfOffers[] memory informationOffers,
       address collateral,
       address[] memory lenders,
       address borrower
   ) public onlyAggregator {
       for (uint i = 0; i < lenders.length; i++) {
           bool validPair = isPairWhitelisted[informationOffers[i].principle][
               collateral
           ];
           if (!validPair) {
               return;
               continue;
           }
           address principle = informationOffers[i].principle;
           uint _currentEpoch = currentEpoch();
           lentAmountPerUserPerEpoch[lenders[i]][
               hashVariables(principle, _currentEpoch)
           ] += informationOffers[i].principleAmount;
\u0060\u0060\u0060plaintext
totalUsedTokenPerEpoch[principle][
    _currentEpoch
] += informationOffers[i].principleAmount;
borrowAmountPerEpoch[borrower][
    hashVariables(principle, _currentEpoch)
] += informationOffers[i].principleAmount;
emit UpdatedFunds(
    lenders[i],
    principle,
    collateral,
    borrower,
    _currentEpoch
);
\u0060\u0060\u0060

After applying the change, running the test case provided in the PoC will output the following logs:

\u0060\u0060\u0060
lentAmountPerUserPerEpoch:   5000000000000000000
totalUsedTokenPerEpoch: 5000000000000000000
borrowAmountPerEpoch:   5000000000000000000
\u0060\u0060\u0060


sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/f185f42fcdbeca0bb9
005767c1302c8daf24e940](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/f185f42fcdbeca0bb9005767c1302c8daf24e940)
## Issue M-22: Previous owner can steal unclaimed bribes from new owner of veNFT-Vault

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/875)  
The protocol has acknowledged this issue.

Found by: 0xc0ffEE, DenTonylifer, Flashloan44, Greese, KiroBrejka, VAD37, eeshenggoh, xiaoming90

Previous owner can steal unclaimed bribes from new owner of veNFT, because transferring ownership of veNFT does not change the manager (which can claim bribes, vote).

Link
\u0060\u0060\u0060solidity
function claimBribesMultiple(
    address[] calldata vaults,
    address[] calldata _bribes,
    address[][] calldata _tokens
) external {
    for (uint i; i < vaults.length; i++) {
        require(
            msg.sender == veNFTVault(vaults[i]).managerAddress(),
            "not manager"
        );
        require(isVaultValid[vaults[i]], "not vault");
        veNFTVault(vaults[i]).claimBribes(msg.sender, _bribes, _tokens);
        emitInteracted(vaults[i]);
    }
}
\u0060\u0060\u0060
Each veNFTVault.sol has manager role, which by default is owner of veNFTVault:
\u0060\u0060\u0060solidity
veNFTVault vault = new veNFTVault(
    nftAddress,
    address(this),
    m_Receipt,
    nftsID[i],
);
\u0060\u0060\u0060
msg.sender
//...
s_ReceiptID_to_Vault[m_Receipt] = address(vault);
//...
_mint(msg.sender, m_Receipt);
But transferring ownership of veNFTVault by transferring receipt ID does not change the manager - old manager can still call all of these functions: voteMultiple(), claimBribesMultiple(), resetMultiple(), extendMultiple() and pokeMultiple(). Main impact that old manager can steal unclaimed bribes from new owner by calling claimBribesMultiple():

\u0060\u0060\u0060solidity
function claimBribesMultiple(
    address[] calldata vaults,
    address[] calldata _bribes,
    address[][] calldata _tokens
) external {
    for (uint i; i < vaults.length; i++) {
        require(
            msg.sender == veNFTVault(vaults[i]).managerAddress(),
            "not manager"
        );
        require(isVaultValid[vaults[i]], "not vault");
        veNFTVault(vaults[i]).claimBribes(msg.sender, _bribes, _tokens);
        emitInteracted(vaults[i]);
    }
}
\u0060\u0060\u0060

None

None

- Malicious user wants to sell ownership of veNFTVault, which has for example 1000 USDC of unclaimed bribes;
- Victim expects to become owner of veNFTVault and have the ability to claim unclaimed bribes, vote, and so on;
- Malicious user claims bribes right after transferring receipt ID, because he is still the manager of the vault;
• Bribes are sent to previous malicious owner, not current holder of receiptID:

\u0060\u0060\u0060solidity
SafeERC20.safeTransfer(
    ERC20(_tokens[i][j]),
    sender,
    amountToSend
);
\u0060\u0060\u0060

Previous owner can still call all of these functions: \u0060voteMultiple()\u0060, \u0060claimBribesMultiple()\u0060, \u0060resetMultiple()\u0060, \u0060extendMultiple()\u0060 and \u0060pokeMultiple()\u0060. Main impact that manager (previous owner) can steal unclaimed bribes from new owner by calling \u0060claimBribesMultiple()\u0060.

No response

Override \u0060transferFrom()\u0060 function in that way that it also changes manager address to new owner\u0027s address.
PAGE END
