# 3.1 Low Risk - Unlocked Goat Tokens

**Severity:** low
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** Goat tokens, staked, unlock function, account interests, lockData, block.timestamp, investor, duration, amount, recommendation, update, value, function, risk, zero, entire, returned, call, update staked, tokens

---

# 3.1 Low Risk
### 3.1.1 Unlocked Goat Tokens
As duration will be way lesser than \u0060staked\u0060 , rest duration will always be returned as zero and entire amount of Goat tokens of the investor will be unlocked when Unlock function is called.  
**Recommendation:** Update the \u0060staked\u0060 value for account interests function.  
Goat: \u0060fixed lockData = lockData[to]; lockData.startedAt = block.timestamp;\u0060

## 3.2 Medium Risk
### 3.2.1 Halving interval is 7 days contrary to the documentation of 24 months
Submitted by Haxatron, also found by b0g0, cccz, Spearmint, Rotciv Egaf, 0xWeiss, walter, Aslanbek Aibimov, nmirchev8, merlin, john-femi and Vijay  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** The halving interval is set to 7 days which is contrary to the documentation of 24 months.  
- \u0060DCT.sol#L14:\u0060  
  \u0060\u0060\u0060solidity
  contract "DCT" { // Line 14
      // ...
  }
  \u0060\u0060\u0060

The documentation says it should be 24 months:  
**Halving:** Emission is reduced by 50% every 24 months.  
As such the GOAT emissions will be slower than intended.  
**Recommendation:** The maximum number of tokens that can be emitted is always double the total GOAT emission for the first interval, and therefore it would be good if the halving interval is increased such that the total GOAT emitted in the first halving interval is more than half of the maximum number of tokens that can be emitted.  
As seen, the documentation is also not ideal.  
Goat: yeah. it\u0027s just for staging version  
Judge: While I agree that this is something the protocol would be aware and is to be used only for staging purpose. The researcher should not be making such assumptions unless documented. Considering this a valid medium.
