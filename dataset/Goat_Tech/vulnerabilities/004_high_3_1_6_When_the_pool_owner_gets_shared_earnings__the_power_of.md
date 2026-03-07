# 3.1.6 When the pool owner gets shared earnings, the power of that pool becomes stale

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** pool, owner, shared earnings, power, stale, financial stability, recalculation, staking, withdrawing, reward distribution, public function, earnings, fs, calculation, incorrect, wrap, context, recommendation, issue, solution

---

# 3.1.6 When the pool owner gets shared earnings, the power of that pool becomes stale
**Submitted by:** cccz  
**Severity:** High Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** fs (Financial_stability) is an important factor in calculating the pool\u0027s power. ❢s ❂ ❊❚❍❴✲  
❊❛r♥✐♥❣ ✴ ▼❛①❴❊❚❍❴❊❛r♥✐♥❣:  
❢✉♥❝t✐♦♥ ❴r❡❈❛❧❋s✭  
❛❞❞r❡ss ❛❝❝♦✉♥t❴  
✮  
✐♥t❡r♥❛❧  
④  
✉✐♥t ♠❛①❊❛r♥✐♥❣ ❂ ❴❡❊❛r♥✐♥❣✳♠❛①❊❛r♥✐♥❣❖❢✭❛❝❝♦✉♥t❴✮❀  
❴♣r♦❢✐❧❡❈✳✉♣❞❛t❡❋s❖❢✭❛❝❝♦✉♥t❴✱ ▲❍❡❧♣❡r✳❝❛❧❋s✭  
❴❡❊❛r♥✐♥❣✳❜❛❧❛♥❝❡❖❢✭❛❝❝♦✉♥t❴✮ ✰ ❴✈♦t✐♥❣✳❞❡❢❡♥❞❡r❊❛r♥✐♥❣❋r❡❡③❡❞❖❢✭❛❝❝♦✉♥t❴✮✱  
♠❛①❊❛r♥✐♥❣  
✮✮❀  
❴r❡❈❛❧❊P✷P❉❇❛❧❛♥❝❡✭❛❝❝♦✉♥t❴✮❀  

The problem here is that when poolOwner gets shared earnings, both ❴❡❊❛r♥✐♥❣✳❜❛❧❛♥❝❡❖❢✭♣♦♦❧❖✇♥❡r✮  
and ❴❡❊❛r♥✐♥❣✳♠❛①❊❛r♥✐♥❣❖❢✭♣♦♦❧❖✇♥❡r✮ change, causing the pool\u0027s power to become stale.  
❢✉♥❝t✐♦♥ s❤❛r❡❈♦♠♠✐ss✐♦♥✭  
❛❞❞r❡ss ❛❝❝♦✉♥t❴  
✮  
♣✉❜❧✐❝  
④  
✉✐♥t ❛♠♦✉♥t ❂ ❜❛❧❛♥❝❡❖❢✭❛❝❝♦✉♥t❴✮ ✲ ❴s❤❛r❡❞❆❬❛❝❝♦✉♥t❴❪❀  
✐❢ ✭❛♠♦✉♥t ❂❂ ✵✮ ④  
r❡t✉r♥❀  
⑥  
❛❞❞r❡ss s♣♦♥s♦r❀  
✉✐♥t s❆♠♦✉♥t❀  
✭s♣♦♥s♦r✱ s❆♠♦✉♥t✮ ❂  ❴♣r♦❢✐❧❡❈✳❣❡t❙♣♦♥s♦rP❛rt✭❛❝❝♦✉♥t❴✱ ❛♠♦✉♥t✮❀  
✐❢ ✭s❆♠♦✉♥t ❃ ✵✮ ④  
❴tr❛♥s❢❡r✭❛❝❝♦✉♥t❴✱ s♣♦♥s♦r✱ s❆♠♦✉♥t✮❀  
❡♠✐t ❙❤❛r❡❈♦♠♠✐ss✐♦♥✭❛❝❝♦✉♥t❴✱ s♣♦♥s♦r✱ s❆♠♦✉♥t✮❀  
⑥  
❴s❤❛r❡❞❆❬❛❝❝♦✉♥t❴❪ ❂ ❜❛❧❛♥❝❡❖❢✭❛❝❝♦✉♥t❴✮❀  
✐❢ ✭❴s❤❛r❡❞❆❬❛❝❝♦✉♥t❴❪ ❃ ❴♠❛①❊❛r♥✐♥❣❖❢❬❛❝❝♦✉♥t❴❪✮ ④  
❴✉♣❞❛t❡▼❛①❊❛r♥✐♥❣✭❛❝❝♦✉♥t❴✱ ❴s❤❛r❡❞❆❬❛❝❝♦✉♥t❴❪✮❀  
⑥  
⑥  

For example, currently ❴❡❊❛r♥✐♥❣✳❜❛❧❛♥❝❡❖❢✭❆✮ ❂ ✶✵✵, ❴❡❊❛r♥✐♥❣✳♠❛①❊❛r♥✐♥❣❖❢✭❆✮ ❂ ✷✵✵, ❢s❆ ❂  
✶✵✵✴✷✵✵ ❂ ✵✳✺.  
After A gets 50 shared earnings, ❢s❆ should be ✶✺✵✴✷✵✵ ❂ ✵✳✼✺.  
But since ❢s❆ is only recalculated when staking and withdrawing in P♦♦❧❆✱ fsA‘ will remain at 0.5 instead  
of 0.75, which causes the power of the pool to become stale and the reward distribution to be incorrect.  
**Recommendation:** It is recommended to wrap ❴r❡❈❛❧❋s with a public function so that anyone can recalculate any pool\u0027s fs as earnings increases.  
**Goat:** correct. fixed  
❢✉♥❝t✐♦♥ r❡❈❛❧❋s✭  
❛❞❞r❡ss ♣♦♦❧❖✇♥❡r❴  
✮  
❡①t❡r♥❛❧  
④  
❴r❡❈❛❧❋s✭♣♦♦❧❖✇♥❡r❴✮❀  
⑥
Submitted by Spearmint, also found by 0xRajkumar, nmirchev8, sashik-eth, ladboy233 and Charles  
Severity: High Risk  
Context: Earning.sol#L96-L115
