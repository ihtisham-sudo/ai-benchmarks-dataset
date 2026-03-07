# Malicious pool owner can withdraw earnings without affecting trust score

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** malicious, pool owner, withdraw earnings, trust score, reputation standard, attack vector, second account, owner percentage, stake earnings, withdrawal, manipulation, bad actors, protocol vulnerability, earnings, trustworthiness, core function, proof of concept, user exploitation, negligible cost, trust score manipulation

---

# Malicious pool owner can withdraw earnings without affecting trust score
- **Submitted by:** Spearmint
- **Severity:** High Risk
- **Context:** (No context files were provided by the reviewer)

### Relevant Context:
- The core function of this protocol is to be a "Reputation standard", the following is extracted from the docs FAQ section:
    - What is really your reputation/trustworthiness on Goat.Tech
    - It’s the ability to instil a belief in many people that you won\u0027t withdraw the majority of your earnings for a long time.
  
Normally if a user withdraws earnings their Fs will drop to = 0, this will cause their trust score to drop to = 0.

### Description:
There is a way for a malicious user to withdraw their earnings without affecting their trust score at all. It involves the following steps:
1. Use a second account to create a pool.
2. Configure the pool to have an Owner % of 99%.
3. When you want to withdraw earnings from the main account use the function to stake the earnings into the second account\u0027s pool.
4. Now since the pool has a 99% owner percentage, the second account\u0027s owner will receive 99% of the staked amount as earnings (dev team gets 1%).
5. Now withdraw the earnings from the second account to the main account\u0027s wallet.
6. This will not compromise the trust score at all, even though the pool owner has withdrawn all their earnings. See the proof of concept.

### Impact:
The issue breaks the core function of the protocol being a "reputation standard" and I have shown a simple way how a user can effectively withdraw their earnings without affecting the trust score. The "Trust Score" cannot be trusted if it can be manipulated like this by bad actors.

### Likelihood:
It is a very simple attack to execute and any user could easily do this with negligible cost, see the proof of concept.
## Proofofconcept
The following foundry test illustrates the attack scenario. Run it with the following command line input:

\u0060\u0060\u0060
r test test
\u0060\u0060\u0060

\u0060\u0060\u0060
♣r❛❣♠❛ s♦❧✐❞✐t② ❂✵✳✽✳✽❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧❢♦r❣❡✲st❞✴❚❡st✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧❢♦r❣❡✲st❞✴❝♦♥s♦❧❡✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴❈♦♥tr♦❧❧❡r✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴Pr♦❢✐❧❡✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴❉❈❚✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴P♦♦❧❋❛❝t♦r②✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴❊t❤❙❤❛r✐♥❣✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴❧✐❜✴▲▲♦❝❦❡r✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴✐♥t❡r❢❛❝❡s✴■P♦♦❧❋❛❝t♦r②✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴✐♥t❡r❢❛❝❡s✴■Pr♦❢✐❧❡✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴✐♥t❡r❢❛❝❡s✴■❉❈❚✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴✐♥t❡r❢❛❝❡s✴■❱♦t✐♥❣✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴✐♥t❡r❢❛❝❡s✴■❊t❤❙❤❛r✐♥❣✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴♠♦❞✉❧❡s✴❯s❡❆❝❝❡ss❈♦♥tr♦❧✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴♠♦❞✉❧❡s✴❊❛r♥✐♥❣✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴♠♦❞✉❧❡s✴▲♦❝❦❡r✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧❅♦♣❡♥③❡♣♣❡❧✐♥✴❝♦♥tr❛❝ts✴t♦❦❡♥✴❊❘❈✷✵✴■❊❘❈✷✵✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐♠♣♦rt ✧✳✳✴❝♦♥tr❛❝ts✴♠♦❞✉❧❡s✴❉❚♦❦❡♥✳s♦❧✧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❝♦♥tr❛❝t ❋♦r❦ ✐s ❚❡st ④
\u0060\u0060\u0060

\u0060\u0060\u0060
●♦❛t❚❡❝❤ ❈♦♥tr❛❝ts
\u0060\u0060\u0060

\u0060\u0060\u0060
❈♦♥tr♦❧❧❡r ❝♦♥tr♦❧❧❡r❀
\u0060\u0060\u0060

\u0060\u0060\u0060
Pr♦❢✐❧❡ ♣r♦❢✐❧❡❀
\u0060\u0060\u0060

\u0060\u0060\u0060
▲♦❝❦❡r ❧♦❝❦❡r❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❯s❡❆❝❝❡ss❈♦♥tr♦❧ ✉s❡❆❝❝❡ss❈♦♥tr♦❧❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❊❛r♥✐♥❣ ❡❛r♥✐♥❣❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❉❈❚ ❣♦❛t❀
\u0060\u0060\u0060

\u0060\u0060\u0060
▲♦❝❦❡r ❣♦❛t▲♦❝❦❡r❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❉❚♦❦❡♥ ❉♣✷♣❉❚♦❦❡♥❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❉❚♦❦❡♥ tr✉st❙❝♦r❡❚♦❦❡♥❀
\u0060\u0060\u0060

\u0060\u0060\u0060
P♦♦❧❋❛❝t♦r② ♣♦♦❧❋❛❝t♦r②❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❊t❤❙❤❛r✐♥❣ ❡t❤❙❤❛r✐♥❣❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❙❡t✉♣ ✉s❡rs
\u0060\u0060\u0060

\u0060\u0060\u0060
❛❞❞r❡ss ❲❤❛❧❡ ❂ ✵①❉✽❊❛✼✼✾❜✽❋❋❈✶✵✾✻❈❆✹✷✷❉✹✵✺✽✽❈✹❝✵✻✹✶✼✵✾✽✾✵❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❛❞❞r❡ss ❆❧✐❝❡ ❂ ✵①✼✶❇✻✶❝✷❊✷✺✵❆❋❛✵✺❞❋❝✸✻✸✵✹❉✻❝✾✶✺✵✶❜❊✵✾✻✺❉✽❀
\u0060\u0060\u0060

\u0060\u0060\u0060
❛❞❞r❡ss ❊✈❡ ❂ ✵①❜✷✷✹✽✸✾✵✽✹✷❞✸❈✹❛❈❋✶❉✽❆✽✾✸✾✺✹❆❢❝✵❊❆❝✺✽✻❡✺❀
\u0060\u0060\u0060

❛❞❞r❡ss ❏♦❤♥
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✷♥❞❆❝❝♦✉♥t✮✱ ✸✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
❝❤❛♥❣❡s t❤❡ ♦✇♥❡r✪ ♦❢ ❏♦❤♥✷♥❞❆❝❝♦✉♥t t♦ ✾✾✪
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
❝❤❡❝❦ ❥♦❤♥✬s tr✉st s❝♦r❡ ❜❡❢♦r❡ ✇✐t❤❞r❛✇✐♥❣ ❡❛r♥✐♥❣s
\u0060\u0060\u0060
## Vulnerability 7
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
## Vulnerability 8
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
## Vulnerability 9
\u0060\u0060\u0060plaintext
❝❤❡❝❦ ❥♦❤♥✬s ❡❛r♥✐♥❣s ❛❢t❡r ♠❛♥② ♣♦❡♣❧❡ ✐♥✈❡st❡❞ ✐♥ ❤✐s ♣♦♦❧
\u0060\u0060\u0060
## Vulnerability 10
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
## Vulnerability 11
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
## Vulnerability 12
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
## Vulnerability 13
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
## Vulnerability 14
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
## Vulnerability 15
\u0060\u0060\u0060plaintext
startPrt
trrgt4✈✛✉✿ atar⑥✭♣❛②❛❜❧❡✭❏♦❤♥✮✱ ✼✷✵ ❞❛②s✱ ✶✵✵✵✱ ✷✵✵✵✸✵✵✱ ✶✱ ✵✮❀
\u0060\u0060\u0060
