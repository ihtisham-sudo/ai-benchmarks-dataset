# 3.2.3 - When calling r from tst, the calculated fs may be incorrect

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** calculate, fs, stale, earnings, unshared, current, function, parameters, admin, risk, protocol, stake, funds, loss, change, impact, recommendation, fix, issue, context

---

# 3.2.2 ❴r❡❝❛❧❢sshoulduse❡❛r♥✐♥❣♦❢insteadof ❜❛❧❛♥❝❡♦❢tocalculatefs
**Submitted by:** cccz  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** ❴r❡❈❛❧❋s should use ❡❛r♥✐♥❣❖❢ instead of ❜❛❧❛♥❝❡❖❢ to calculate fs, because ❜❛❧❛♥❝❡❖❢ may contain earnings belonging to the sponsor, and ❴♠❛①❊❛r♥✐♥❣❖❢ is based on ❡❛r♥✐♥❣❖❢ instead of ❜❛❧❛♥❝❡❖❢.

The fix will be:
- ❢✉♥❝t✐♦♥ ❴r❡❈❛❧❋s✭
  - ❛❞❞r❡ss ❛❝❝♦✉♥t❴
    - ✮
      - ✐♥t❡r♥❛❧
        - ④
          - ✉✐♥t ♠❛①❊❛r♥✐♥❣ ❂ ❴❡❊❛r♥✐♥❣✳♠❛①❊❛r♥✐♥❣❖❢✭❛❝❝♦✉♥t❴✮❀
          - ❴♣r♦❢✐❧❡❈✳✉♣❞❛t❡❋s❖❢✭❛❝❝♦✉♥t❴✱ ▲❍❡❧♣❡r✳❝❛❧❋s✭
            - ❴❡❊❛r♥✐♥❣✳❜❛❧❛♥❝❡❖❢✭❛❝❝♦✉♥t❴✮ ✰ ❴✈♦t✐♥❣✳❞❡❢❡♥❞❡r❊❛r♥✐♥❣❋r❡❡③❡❞❖❢✭❛❝❝♦✉♥t❴✮✱
            - ♠❛①❊❛r♥✐♥❣
          - ✮✮❀
          - ❴r❡❈❛❧❊P✷P❉❇❛❧❛♥❝❡✭❛❝❝♦✉♥t❴✮❀
        - ⑥
**Goat:** thats correct. fixed.

## 3.2.3 Whencalling❴r❡❝❛❧❢sfrom❞❝tst❛❦❡,thecalculatedfsmaybeincorrect
**Submitted by:** cccz  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** When ❴r❡❈❛❧❋s is called from ❞❝t❙t❛❦❡, ♠❛①❊❛r♥✐♥❣ may be stale. This is because if the ♣♦♦❧❖✇♥❡r has unshared earnings that have not yet been counted into ♠❛①❊❛r♥✐♥❣, then the actual ♠❛①✲ ❊❛r♥✐♥❣ will be larger than the current one.
## Vulnerabilities
## Admin can change parameters causing loss of staked funds
- **Submitted by:** Spearmint
- **Severity:** Medium Risk
- **Context:** Controller.sol#L761
- **Details:** The \u0060setParameter\u0060 function in \u0060AdminController\u0060 allows any admin to change key parameters, one of them being \u0060setStakeAmount\u0060, without any restrictions. This allows a rogue admin to change the \u0060setStakeAmount\u0060 to 100%, causing users to lose all their staked GOAT. This issue does require admin access BUT the impact is very high (permanent loss of user funds) and this protocol is built to be resilient to such admin attacks. The following is the evidence.

The following is an excerpt from the FAQ section of the docs:
\u0060\u0060\u0060
Can anyone steal my staked ETH and GOAT?
No one. Neither the pool owner nor the protocol creators. Only YOU can unstake your staked funds. Your funds are stored in the Locker contract, and controlled by the Controller contract, which doesn’t contain any function that allows any admin to withdraw funds from the Locker contract.
\u0060\u0060\u0060
The protocol also stated in the ❘❊❆❉▼❊ that:
we make sure that even dev team cannot touch users’ locked funds in the Locker contracts. When staking ETH the protocol limits the ❞❡✈❚❡❛♠P❡r❝❡♥t❴ to a maximum of 5%, this shows that they intend to restrict admin\u0027s power and prevent users from losing 100% of funds from a rogue admin r❡q✉✐r❡✭❞❡✈❚❡❛♠P❡r❝❡♥t ❁ ✺ ✯ ✶✵✵✱ ✧t♦♦ ♠✉❝❤ ❢♦r ❞❡✈❚❡❛♠✧✮❀ this r❡q✉✐r❡ statement is not present when users stake GOAT.

**Impact:** This has major impact, if the rogue dev changes the tax to 100% users will lose 100% of their staked GOAT tokens.

**Recommendation:** Simple fixes to add a require statement in the ✉♣❞❛t❡❈♦♥❢✐❣s✭✮ function, to limit the set tax to some upper limit:
\u0060\u0060\u0060solidity
❢✉♥❝t✐♦♥ ✉♣❞❛t❡❈♦♥❢✐❣s✭
  ✉✐♥t❬❪ ♠❡♠♦r② ✈❛❧✉❡s❴
❮
  ❡①t❡r♥❛❧
  ♦♥❧②❆❞♠✐♥
④
  r❡q✉✐r❡✭✈❛❧✉❡s❴❬✵❪ ❁❂ ✸✵✵✱ ✧♠❛① ✸✪✧✮❀
  ❴❜♦✉♥t②P✉❧❧❊❛r♥✐♥❣P❡r❝❡♥t ❂ ✈❛❧✉❡s❴❬✵❪❀
  ❴♠❛①❇♦♦st❡r ❂ ✈❛❧✉❡s❴❬✶❪❀
  ❴♠❛①❙♣♦♥s♦r❆❞✈ ❂ ✈❛❧✉❡s❴❬✷❪❀
  ❴♠❛①❙♣♦♥s♦r❆❢t❡r ❂ ✈❛❧✉❡s❴❬✸❪❀
  ❴❛tt❛❝❦❋❡❡ ❂ ✈❛❧✉❡s❴❬✹❪❀
  ❴♠❛①❱♦t❡rP❡r❝❡♥t ❂ ✈❛❧✉❡s❴❬✺❪❀
  ❴♠✐♥❆tt❛❝❦❡r❋✉♥❞❘❛t❡ ❂ ✈❛❧✉❡s❴❬✻❪❀
  ❴❢r❡❡③❡❉✉r❛t✐♦♥❯♥✐t ❂ ✈❛❧✉❡s❴❬✼❪❀
  ❴s❡❧❢❙t❛❦❡❆❞✈❛♥t❛❣❡ ❂ ✈❛❧✉❡s❴❬✽❪❀
  ❴♣r♦❢✐❧❡❈✳s❡t❉❡❢❛✉❧t❙P❡r❝❡♥t❈♦♥❢✐❣✭✈❛❧✉❡s❴❬✾❪✮❀
  ❴✐sP❛✉s❡❞❆tt❛❝❦ ❂ ✈❛❧✉❡s❴❬✶✵❪❀
  ❴♣r♦❢✐❧❡❈✳s❡t▼✐♥❙P❡r❝❡♥t❈♦♥❢✐❣✭✈❛❧✉❡s❴❬✶✶❪✮❀
  ❴❞❝t❚❛①P❡r❝❡♥t ❂ ✈❛❧✉❡s❴❬✶✷❪❀
\u0060\u0060\u0060
r❡q✉✐r❡✭✈❛❧✉❡s❴❬✶✷❪ ❁❂ ✶✵✵✵✱ ✧♠❛① ✶✵✪✧✮❀
\u0060\u0060\u0060solidity
❴♠✐♥❋r❡❡③❡❉✉r❛t✐♦♥ ❂ ✈❛❧✉❡s❴❬✶✸❪❀
❴♠❛①❋r❡❡③❡❉✉r❛t✐♦♥ ❂ ✈❛❧✉❡s❴❬✶✹❪❀
❴♠✐♥❙t❛❦❡❊❚❍❆♠♦✉♥t ❂ ✈❛❧✉❡s❴❬✶✺❪❀
❴♠✐♥❙t❛❦❡❉❈❚❆♠♦✉♥t ❂ ✈❛❧✉❡s❴❬✶✻❪❀
❴♠✐♥❉❡❢❡♥❞❡r❋✉♥❞ ❂ ✈❛❧✉❡s❴❬✶✼❪❀
❡♠✐t ❆❞♠✐♥❯♣❞❛t❡❈♦♥❢✐❣✭✈❛❧✉❡s❴✮❀
\u0060\u0060\u0060
Goat: will fix: but severity level should be low. We will renounceOwnership() in the future; administrators will only be needed during the early stages to ensure that everything is going fine.

Judge: The researcher points how the protocol is designed to be resilient against admin attacks and points a valid issue, Keeping this medium.
