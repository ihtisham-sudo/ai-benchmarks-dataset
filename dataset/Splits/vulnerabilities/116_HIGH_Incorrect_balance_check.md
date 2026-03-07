# Incorrect balance check

**Severity:** HIGH
**Auditor:** Zokyo

---

**Severity**: High

**Status**: Resolved

**Description**

In contract utility.move, in function `merge_and_split` at line 31 there’s an assertion between the base coin value and amount parameter. This is meant to ensure that there are enough remaining funds in the base coin balance, however there can be a case when the base coin remaining balance is equal to the amount parameter, so the assertion fails. This should not happen if the two values are equal.

**Recommendation**: 

Change the assertion from greater than to greater than or equal
