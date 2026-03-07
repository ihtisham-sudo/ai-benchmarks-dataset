# Severity

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** Booster, pool power, reward distribution, staking, balance, calculation, security, transaction processing, vulnerability, ETH, p2UD token, mint, burn, global reward, stake, share, mechanism, integrity, review, changes

---

# Severity
High Risk

## Context
(No context files were provided by the reviewer)

## Additional Description
In❉❚♦❦❡♥✳❴❜❡❢♦r❡❚♦❦❡♥❚r❛♥s❢❡r, the ❉✐str✐❜✉t♦r✳❜❡❢♦r❡❚♦❦❡♥❚r❛♥s❢❡rcorresponding to that ❉❚♦❦❡♥ is called, which will call ❉✐str✐❜✉t♦r✳❴❞✐str✐❜✉t❡ to distribute the reward, thus ensuring that the reward can be correctly distributed before the balance is updated:
- ❢✉♥❝t✐♦♥ ❴❜❡❢♦r❡❚♦❦❡♥❚r❛♥s❢❡r✭
  - ❛❞❞r❡ss ❢r♦♠❴✱
  - ❛❞❞r❡ss t♦❴✱
  - ✉✐♥t✷✺✻ ❛♠♦✉♥t❴
- ✮
  - ✐♥t❡r♥❛❧
  - ✈✐rt✉❛❧
  - ♦✈❡rr✐❞❡
- ④
  - ✉✐♥t ✐ ❂ ✵❀
  - ✉✐♥t ♥ ❂ ❴t♦t❛❧❉✐str✐❜✉t♦rs❀
  - ✇❤✐❧❡ ✭✐ ❁ ♥✮ ④
    - ❴❞✐str✐❜✉t♦rs❬✐❪✳❜❡❢♦r❡❚♦❦❡♥❚r❛♥s❢❡r✭❢r♦♠❴✱ t♦❴✱ ❛♠♦✉♥t❴✮❀
    - ✐✰✰❀
  
### When distributing GOAT mining rewards
The rewards are first distributed to the pool based on the ❴✲ ❡P✷P❉❚♦❦❡♥ balance, where they are distributed to users based on their p2UD token balance in the pool. And the user\u0027s ♣✷❯❉t♦❦❡♥ balance in the pool affects the pool\u0027s ❴❡P✷P❉❚♦❦❡♥ balance. However, when stake ETH, ♣✷❯❉t♦❦❡♥✳♠✐♥t is called first, which will increase the user\u0027s share in the pool, and then ❴❡P✷P❉❚♦❦❡♥✳♠✐♥t is called in ❴r❡❈❛❧❊P✷P❉❇❛❧❛♥❝❡, which will claim the global GOAT mining reward, which will be distributed according to the user\u0027s balance after the mint, not before.
- ♣✷❯❉t♦❦❡♥✳♠✐♥t❭❛❝❝♦✉♥t❴✱ ♣♦✇❡r▼✐♥t❡❞✮❀
The vulnerability affects the reward distribution mechanism in the system.

- When Alice stakes ETH to increase her share from 50% to 60%, the global reward will be distributed to her at 60 instead of 50.

The fix would be to pull GOAT mining rewards before p2UD token mint/burn.

The vulnerability is related to the staking mechanism in the system.

- There are issues with the way rewards are calculated and distributed based on staking percentages.

It is recommended to review the staking logic and implement necessary changes to ensure accurate reward distribution.

The vulnerability affects the transaction processing in the system.

- There are potential security risks associated with how transactions are handled, particularly in relation to reward calculations.

Implement additional security measures to safeguard transaction processing and ensure the integrity of reward distributions.
## Booster Calculation Staleness

**Goat:** already fixed. correct  
**Version:** 3.1.5  

When the \u0060Booster\u0060 is increased, the power of almost all pools becomes stale.  

**Submitted by:** cccz  
**Severity:** High Risk  
**Context:** (No context files were provided by the reviewer)  

Booster is an important factor in calculating the pool\u0027s power. Booster is defined as:

\u0060\u0060\u0060
Booster = 1 + (the current pool\u0027s balance) / (the largest pool balance)
\u0060\u0060\u0060

The following conditions apply:

- The power of the current pool should be recalculated based on the latest balance.
- If the largest pool balance is increased, the power of other pools becomes stale due to not using the latest balance for calculations.

### Example
For example, if the current largest pool balance is 1500, the balance of another pool is 500, and the calculation is as follows:

\u0060\u0060\u0060
Booster for large pool = 1 + 1500 / 1500 = 2
Booster for smaller pool should be = 1 + 500 / 1500 = 1.33
\u0060\u0060\u0060

However, if the booster for the smaller pool is only recalculated during staking and withdrawing, it may remain stale at 1.5 instead of updating to 1.33. This staleness can cause incorrect reward distribution across all pools.

It is recommended to wrap the calculation of \u0060Booster\u0060 and \u0060Power\u0060 in a public function so that anyone can recalculate any pool\u0027s Booster and Power as the largest pool balance increases.

**Goat:** correct. fixed
