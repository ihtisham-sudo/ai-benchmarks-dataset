# 3.2.10 Users can prevent getting bad debt by withdrawing just before a liquidation

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** liquidation, bad debt, Trove, TroveManager, exploit, borrowing fee, withdrawal period, time lock, profitability, redistribution, risk, financial strategy, user behavior, Trove closure, debt avoidance, liquidation strategy, Trove reopening, debt redistribution, user exploitation, protocol vulnerability

---

# 3.2.10 Users can prevent getting bad debt by withdrawing just before a liquidation
**Submitted by:** santipu  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** When a Trove is liquidated with bad debt, it is redistributed between the open Troves within that TroveManager. 

A user can prevent getting bad debt and increase the bad debt for other Troves by executing the following exploit:
1. Bob sees a liquidation with bad debt is going to happen and closes his Trove.
2. Bob waits for the liquidation to happen (or does the liquidation himself).
3. Bob opens his Trove again.

As long as the borrowing fee is lower than the bad debt that Bob would have received, this attack is profitable and will increase the bad debt going to the rest of the Troves. Also, Bob could not open the Trove again and avoid paying the borrowing fee, just avoiding the bad debt for free.

In short, Bob can avoid getting the bad debt and make other Troves get more bad debt than they should.  
**Recommendation:** To mitigate this issue, it is recommended to implement a time lock that ensures Troves are not closed instantly but need to go through a withdrawal period (e.g. 1 day).
