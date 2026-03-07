# Rounding issue can lead to lacking funds in the contract

**Severity:** HIGH
**Auditor:** AuditOne

---

**Description:** 

In case `arbitrated = True`,arbitratorFee will be deducted from both buyer and seller splits. However they did not be sum up but after all,in `calculatePayment()`,arbitratorFee is calculated again with total amount.

Scenario (for simplicity,let's just assume there is only arbitrator fee)

1. arbitratorFee = 1000 (10%),split[Buyer]= 4999,split[seller]= 5001

arbitratorFeeFromBuyer = 4999 \*10%= 499,arbitratorFeeFromSeller = 500

sum = 999 != 1000 ??

2. After take fee split[Buyer]= 4500,split[seller]= 4501
3. Total splits = split[Buyer]+ split[seller]+ arbitratorFee = 10001> 10000

**Recommendations:** 

Consider returning arbitrator with the remaining amount without calculating it using `arbitratorFee`
