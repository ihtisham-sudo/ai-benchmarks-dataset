# 3.2.14 Stake function can be inhibited

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** stake, function, inhibited, conditional statement, front-run, attacker, token, address, balance, sponsor, ETH, transaction, mempool, penalty, withdraw, locking period, protection, liquidity, supply, Controller.sol

---

# 3.2.14 Stake function can be inhibited
- **Submitted by**: innertia, also found by tenma
- **Severity**: Medium Risk
- **Context**: Controller.sol
- **Description**: In ❴st❛❦❡, there is a conditional statement r❡q✉✐r❡✭✈❛❧✉❡ ❂❂ ✵ ⑤⑤ ✈❛❧✉❡ ❃❂ ♠✐♥❙t❛❦❡❆♠♦✉♥t✱ ✧❛♠♦✉♥t t♦♦ s♠❛❧❧✧✮❀, where ✈❛❧✉❡ is the following value: ✉✐♥t✷✺✻ ✈❛❧✉❡ ❂ ✐s❊t❤❴ ❄ ❴❣❡t❤✳❜❛❧❛♥❝❡❖❢✭❛❞❞r❡ss✭t❤✐s✮✮ ✿ ❴❞❝t✳❜❛❧❛♥❝❡❖❢✭❛❞❞r❡ss✭t❤✐s✮✮❀. Let\u0027s assume that the person who wants to ❴st❛❦❡ intends to pass here with the condition ✈❛❧✉❡ ❂❂ ✵. However, the attacker can front-run this and send a small token (✵ ❁ ✈❛❧✉❡ ❁ ♠✐♥❙t❛❦❡❆♠♦✉♥t) to this address, which will always cause the conditional statement to fail. This allows the attacker to interfere with ❴st❛❦❡, which is an important function at the heart of the product.
- **Recommendation**: You can stop calculating the value based on the address balance. At the very least, consideration should be given to the fact that outsiders can increase the balance of addresses.
- **Goat**: Fixed
Submitted by Tripathi, also found by cccz  
Severity: MediumRisk  
Context: Controller.sol#L368  

❴✉♣❞❛t❡❙♣♦♥s♦rcanbefrontrunbycurrentsponsor.  
Alice want to be sponsor for ❳❨❩✬s pool which has current active sponsor ❇❖❇. Alice calculated the ETH amount and duration she need to stake for becoming the sponsor and she called Controller.sol#L413 function.  
BOBseesthetransactioninthepublicmempoolandfrontrunAlice\u0027stransactionbystakingmoresothat Alice can\u0027t be the new sponsor. Alice stake will execute she will be a staker, her funds will be locked for the duration and she won\u0027t be able to be a sponsor. Alice would want to recover her funds but she will havetopayapenaltyforwithdrawingbeforethelockingperiod.  
The ♠✐♥❙P❡r❝❡♥t❴ params exist to ensure that there are no frontrunning transactions that change the sponsorrewardratebeforeyourtransactionisprocesse,dbutthereisnoprotectionfortheaboveissue that ensure that a % of total active supply Alice will get for her staked ETH.  
It is same as providing liquidity to uniswap pool without slippage protection:

❢✉♥❝t✐♦♥ ❴✉♣❞❛t❡❙♣♦♥s♦r✭  
❛❞❞r❡ss ♣❛②❛❜❧❡ ♣♦♦❧❖✇♥❡r❴✱  
❛❞❞r❡ss st❛❦❡r❴✱  
✉✐♥t ♠✐♥❙P❡r❝❡♥t❴  

✮ ✐♥t❡r♥❛❧ ④  
✐❢ ✭♣♦♦❧❖✇♥❡r❴ ❂❂ st❛❦❡r❴✮ ④  
r❡t✉r♥❀  
⑥  
■Pr♦❢✐❧❡✳❙Pr♦❢✐❧❡ ♠❡♠♦r② ♣r♦❢✐❧❡ ❂ ❴♣r♦❢✐❧❡❈✳♣r♦❢✐❧❡❖❢✭♣♦♦❧❖✇♥❡r❴✮❀  
✐❢ ✭♣r♦❢✐❧❡✳s♣♦♥s♦r ❂❂ st❛❦❡r❴✮ ④  
r❡t✉r♥❀  
⑥  
r❡q✉✐r❡✭♣r♦❢✐❧❡✳♥❡①t❙P❡r❝❡♥t ❃❂ ♠✐♥❙P❡r❝❡♥t❴✱ ✧♣r♦❢✐❧❡ r❛t❡ ❝❤❛♥❣❡❞✧✮❀  
■P♦♦❧❋❛❝t♦r②✳❙P♦♦❧ ♠❡♠♦r② ♣♦♦❧ ❂ ❴♣♦♦❧❋❛❝t♦r②✳❣❡tP♦♦❧✭♣♦♦❧❖✇♥❡r❴✮❀  
■❉❚♦❦❡♥ ♣✷❯❉t♦❦❡♥ ❂ ■❉❚♦❦❡♥✭♣♦♦❧✳❞❚♦❦❡♥✮❀  
✉✐♥t t✐♠❡❉✐❢❢ ❂ ❜❧♦❝❦✳t✐♠❡st❛♠♣ ✲ ♣r♦❢✐❧❡✳✉♣❞❛t❡❞❆t❀  
✐❢ ✭t✐♠❡❉✐❢❢ ❃ ❴♠❛①❙♣♦♥s♦r❆❢t❡r✮ ④  
t✐♠❡❉✐❢❢ ❂ ❴♠❛①❙♣♦♥s♦r❆❢t❡r❀  
⑥  
✉✐♥t s♣♦♥s♦r❉❚♦❦❡♥❇❛❧❛♥❝❡ ❂ ♣✷❯❉t♦❦❡♥✳❜❛❧❛♥❝❡❖❢✭♣r♦❢✐❧❡✳s♣♦♥s♦r✮❀  
✉✐♥t st❛❦❡r❉❚♦❦❡♥❇❛❧❛♥❝❡ ❂ ♣✷❯❉t♦❦❡♥✳❜❛❧❛♥❝❡❖❢✭st❛❦❡r❴✮❀  
✉✐♥t s♣♦♥s♦r❇♦♥✉s ❂ ✭s♣♦♥s♦r❉❚♦❦❡♥❇❛❧❛♥❝❡ ✯  
✭❴♠❛①❙♣♦♥s♦r❆❞✈ ✲ ✶✮ ✯  
t✐♠❡❉✐❢❢✮ ✴ ❴♠❛①❙♣♦♥s♦r❆❢t❡r❀  ✴✴✭s♣♦♥s♦r❉❚♦❦❡♥❇❛❧❛♥❝❡ ✯ ✻ ✯ t✐♠❡❉✐❢❢✮ ✴ ✼ ✯ ✽✻✹✵✵  
✉✐♥t s♣♦♥s♦rP♦✇❡r ❂ s♣♦♥s♦r❉❚♦❦❡♥❇❛❧❛♥❝❡ ✰ s♣♦♥s♦r❇♦♥✉s❀  
✐❢ ✭  
st❛❦❡r❉❚♦❦❡♥❇❛❧❛♥❝❡ ❃ s♣♦♥s♦rP♦✇❡r ⑤⑤ ♣♦♦❧❖✇♥❡r❴ ❂❂ ♣r♦❢✐❧❡✳s♣♦♥s♦r  
✴✴❅❛✉❞✐t✲✐ss✉❡ ❝✉rr❡♥t s♣♦♥s♦r ❝❛♥ ❢r♦♥t r✉♥ t❤❡ t① ❛♥❞ ✐♥❝r❡❛s❡ ❤✐s s♣♦♥s♦rP♦✇❡r ❜② st❛❦✐♥❣ ♠♦r❡ s♦  

BOBwill stake more to increase his sponsor power and Alice\u0027s funds will be locked but she won\u0027t be a sponsor  
Goat: Fixed.
