# splitCalculation - seller can get unfair amount of share when underflow happen

**Severity:** HIGH
**Auditor:** AuditOne

---

**Description:** 

Seller share is calculated inside unchecked state,when underflow happen,seller will receive huge share.

**Recommendations:**

Suggested not use unchecked based share calculation. Enusre,seller received within 100%split

**Status:** Resolved
