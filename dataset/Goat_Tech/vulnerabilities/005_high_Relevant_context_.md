# Relevant context:

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** reputation, trustworthiness, vulnerability, manipulation, earnings, stake, contract, modifier, protocol, malicious, users, penalty, withdraw, core functionality, trust score, attack, recommendation, security, decentralized, smart contract

---

# Relevant context:
❋s ❂ ❋✐♥❛♥❝✐❛❧ ❙t❛❜✐❧✐t② ❂ ❊❚❍❴❊❛r♥✐♥❣ ✴ ▼❛①❴❊❚❍❴❊❛r♥✐♥❣  
The core function of this protocol is to be a "Reputation standard", the following is extracted from the docs FAQ section:  
Whatisreallyyourreputation/trustworthiness on Goat.Tech  
It\u0027s the ability to instill a belief in many people that you won\u0027t withdraw the majority of your earnings for a long time.  

## Description:  
The ✉♣❞❛t❡✭✮ function in ❊❛r♥✐♥❣✳s♦❧ is callable by anyone as it is lacking the ♦♥❧②❆❞♠✐♥ modiﬁer.  
This allows ♣♦♦❧❖✇♥❡r\u0027s to directly send in wsteth to the ❊❛r♥✐♥❣✳s♦❧ contract and call the ✉♣❞❛t❡✭✮ function to increase their ❊❚❍❴❊❛r♥✐♥❣. A ♣♦♦❧❖✇♥❡r\u0027s ❊❚❍❴❊❛r♥✐♥❣ normally increase by users staking in their pool and the ♣♦♦❧❖✇♥❡r getting a % of the stake. It does not make sense to allow ♣♦♦❧❖✇♥❡rs to update their earnings by depositing into it.  
The fact that a pool Owner can easily withdraw their ❊❚❍❴❊❛r♥✐♥❣ (drop their Fs) then come back later and deposit it back in directly (increasing it back to normal) defeats the purpose of the system that measures trustworthiness based on "not withdrawing majority of earnings".  
Normally to recover the trust score ♣♦♦❧❖✇♥❡rs would need more people to stake in their pool and/or sit and wait to collect more mining reward to make up the earnings. Both of these take significantly longer and thus until the earnings recover the ♣♦♦❧❖✇♥❡r would have a lowered Fs and therefore lower Trust Score since Fs is proportional to Trust score. This period of lower Trust Score is meant to be the punishment for withdrawing the majority of earnings.  

## Impact:  
The issue breaks the core function of the protocol being a "reputation standard" AND I have shown ways how malicious users can manipulate their earnings to dodge the reputation penalty.  

## Likelihood:  
These attacks are quite simple to execute. The core protocol functionality of being a reputation standard is broken as the key metric for trustworthiness can be manipulated by bad actors.  

## Recommendation:  
Add the ♦♥❧②❆❞♠✐♥ modifier to the ✉♣❞❛t❡✭✮ function as follows:
\u0060\u0060\u0060solidity
❢✉♥❝t✐♦♥ ✉♣❞❛t❡✭
   ❛❞❞r❡ss ❛❝❝♦✉♥t❴✱
   ❜♦♦❧ ♥❡❡❞❙❤❛r❡❈♦♠♠❴
✮
   ❡①t❡r♥❛❧
✰    ♦♥❧②❆❞♠✐♥
   ④
   ✐❢ ✭♥❡❡❞❙❤❛r❡❈♦♠♠❴✮ ④
       ✉✐♥t ❛♠♦✉♥t ❂ ❴❝❛s❤■♥✭✮❀
       ❴♠✐♥t✭❛❝❝♦✉♥t❴✱ ❛♠♦✉♥t✮❀
       s❤❛r❡❈♦♠♠✐ss✐♦♥✭❛❝❝♦✉♥t❴✮❀
   ⑥ ❡❧s❡ ④
       s❤❛r❡❈♦♠♠✐ss✐♦♥✭❛❝❝♦✉♥t❴✮❀
       ✉✐♥t ❛♠♦✉♥t ❂ ❴❝❛s❤■♥✭✮❀
       ❴♠✐♥t✭❛❝❝♦✉♥t❴✱ ❛♠♦✉♥t✮❀
       ❴s❤❛r❡❞❆❛❝❝♦✉♥t❴❪ ❂ ❜❛❧❛♥❝❡❖❢✭❛❝❝♦✉♥t❴✮❀
       ✐❢ ✭❴s❤❛r❡❞❆❛❝❝♦✉♥t❴❪ ❃ ❴♠❛①❊❛r♥✐♥❣❖❢❬❛❝❝♦✉♥t❴❪✮ ④
           ❴✉♣❞❛t❡▼❛①❊❛r♥✐♥❣✭❛❝❝♦✉♥t❴✱ ❴s❤❛r❡❞❆❛❝❝♦✉♥t❴❪✮❀
   ⑥
\u0060\u0060\u0060
Goat: Fixed
