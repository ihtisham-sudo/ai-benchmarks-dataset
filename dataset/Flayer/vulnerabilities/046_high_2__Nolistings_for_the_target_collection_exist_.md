# 2. Nolistings for the target collection exist.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Flayer
**Keywords:** Nolistings, target collection, vulnerability, claimable ETH, voters, quorumVotes, Locker, sunsetCollection, impact, admin calls, pre-conditions, attack path, mitigation, smart contract, Ethereum, ETH, claim, portion, less ETH, params

---

# 2. Nolistings for the target collection exist.

External pre-conditions  
None  

Attack Path  
1. Admin calls. The vulnerability always happens when this is called.  

Impact  
A portion of the claimable ETH can never be claimed and all voters can claim less ETH.  

PoC  
No response  

Mitigation  
Consider calling \u0060Locker::sunsetCollection()\u0060 before setting the params. \u0060quorumVotes\u0060 in.
PAGE END
