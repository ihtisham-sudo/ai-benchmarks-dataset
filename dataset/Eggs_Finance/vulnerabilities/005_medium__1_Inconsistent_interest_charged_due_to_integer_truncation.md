# .1 Inconsistent interest charged due to integer truncation

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Eggs Finance
**Keywords:** interest, fee, integer, truncation, arithmetic, exploitation, loan, duration, precision, denominator, mulDiv, overflow, recommendation, solidity, calculation, variance, output, real numbers, risk, context

---

# .1 Inconsistent interest charged due to integer truncation
**Severity:** MediumRisk  
**Context:** Eggs.sol#L209  
**Description:** In Eggs.getInterestFeeInEggs, we compute the interest fee with the following logic:
\u0060\u0060\u0060solidity
uint256 interest = ((3900 * numberOfDays) / 365) + 100;
\u0060\u0060\u0060
Using numberOfDays = 1 as an example, we can compare the output of this logic using integers versus real numbers:
- Integers: 3900 * 1 / 365 = 10 (0.01%).
- Real numbers: 3.9% * 1 / 365 ~= 0.0106849315%.

Here we can see that the output using integers is rounded down by nearly 7%. Since Solidity arithmetic uses integers, this becomes a problem. This can be intentionally exploited by borrowing for shorter durations and repeatedly extending the loan instead of creating a full duration loan. We can see how this creates a variance in the interest paid for one 365 day loan versus 365 one day loans:
- 3900 * 365 / 365 = 3900(3.9%).
- (3900 * 1 / 365) * 365 = 3650 (3.65%).

**Recommendation:** We can represent the interest rate using a larger denominator to get more precision. A good option would be to use 1e18, adjusting the math accordingly. Additionally, we should use a mulDiv function to prevent overflow in the intermediary value:
\u0060\u0060\u0060solidity
- uint256 interest = ((3900 * numberOfDays) / 365) + 100;
+ uint256 interest = mulDiv(0.039e18, numberOfDays, 365) + 0.001e18;
- return ((amount * interest) / 100 / FEE_BASE_1000);
+ return mulDiv(amount, interest, 1e18);
\u0060\u0060\u0060
**Note:** The above logic has not been tested.  
**EggsFinance:** Fixed in commit 2f02fb77.  
**CantinaManaged:** Fixed as recommended.
