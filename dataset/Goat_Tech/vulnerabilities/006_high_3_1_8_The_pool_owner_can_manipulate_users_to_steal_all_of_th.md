# 3.1.8 The pool owner can manipulate users to steal all of their stake amounts by using code edge

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** pool owner, stake amounts, manipulation, code edge, keccak256, transaction, validation, configuration, attack, front-running, Geth, tokens, voting, loans, malicious intent, security, smart contract, edge case, exploitation, user funds

---

# 3.1.8 The pool owner can manipulate users to steal all of their stake amounts by using code edge
- **Submitted by**: 0xRajkumar
- **Severity**: High Risk
- **Context**: (No context files were provided by the reviewer)
- **Description**: ♣♦♦❧❈♦♥❢✐❣❈♦❞❡❴ is used to validate that users staking in the pool have the same code as when transaction was created, and the owner has not changed it, providing protection that ownerPercent and userPercent have not changed. However, there is an edge case where different configurations can have the same code. Let\u0027s see how the code is generated:

  ♦✇♥❡rP❡r❝❡♥t ✯ ▲P❡r❝❡♥t❛❣❡✳❉❊▼■ ✰ ✉s❡rP❡r❝❡♥t

  Here the ❉❊▼■ is 10000. We can actually find two different ♦✇♥❡rP❡r❝❡♥t and ✉s❡rP❡r❝❡♥t inputs that have the same code:
  
  - **First example**:
    \u0060\u0060\u0060
    ♦✇♥❡rP❡r❝❡♥t ❂ ✶
    ✉s❡rP❡r❝❡♥t ❂ ✵
    ❝♦❞❡ ❂ ✶✯✶✵✵✵✵ ✰ ✵
    ❝♦❞❡ ❂ ✶✵✵✵✵
    \u0060\u0060\u0060
  
  - **Second example**:
    \u0060\u0060\u0060
    ♦✇♥❡rP❡r❝❡♥t ❂ ✵
    ✉s❡rP❡r❝❡♥t ❂ ✶✵✵✵✵
    ❝♦❞❡ ❂ ✵✯✶✵✵✵✵ ✰ ✶✵✵✵✵
    ❝♦❞❡ ❂ ✶✵✵✵✵
    \u0060\u0060\u0060

  We can also validate the sum because of 1 and 0, and the sum of 0 and 10000 is actually valid:
  
  ❢✉♥❝t✐♦♥ ✈❛❧✐❞❛t❡P❡r❝❡♥t✭✉✐♥t ♣❡r❝❡♥t❴✮ ✐♥t❡r♥❛❧ ♣✉r❡ ④
  \u0060\u0060\u0060
  ✴✴ ✶✵✵✪ ❂❂ ❉❊▼■ ❂❂ ✶✵✵✵✵
  r❡q✉✐r❡✭♣❡r❝❡♥t❴ ❁❂ ❉❊▼■✱ ✧✐♥✈❛❧✐❞ ♣❡r❝❡♥t✧✮❀
  \u0060\u0060\u0060

  We are assuming two things:
  1. Pool owner is actually having bad intention and he wants to take advantage of this edge case.
  2. ✐♥❉❡❢❛✉❧t❖♥❧②▼♦❞❡ is ❢❛❧s❡.

  Both are possible. Now let\u0027s see how the owner can take advantage of it.
  1. First, they will need to create a pool by staking some Geth and earning some ♣✷❯❉t♦❦❡♥.
  2. As ✐♥❉❡❢❛✉❧t❖♥❧②▼♦❞❡ is ❢❛❧s❡, he will set ♦✇♥❡rP❡r❝❡♥t ❂ ✶ and ✉s❡rP❡r❝❡♥t ❂ ✵ to attract users.
  3. He will run a bot that will constantly monitor transactions and will frontrun with ❝♦♥❢✐❣P♦♦❧ ♦✇♥❡r✲ P❡r❝❡♥t ❂ ✵ and ✉s❡rP❡r❝❡♥t ❂ ✶✵✵✵✵.
  4. As the code will be the same, user funds will be transferred to pool. ❡t❤❉✐str✐❜✉t♦r, and since ♣✷❯❉t♦❦❡♥ will have all the supply, he will earn all the Geth. Users will not earn any ♣✷❯❉t♦❦❡♥ tokens.

- **Recommendation**: To generate code we should use keccak256. Check this reference.
- **Goal**: Fixed
**Submitted by:** 0xRajkumar  
**Severity:** High Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** In the main st❛❦❘ function, we have a r❡q✉✐r❡ statement that checks whether our ❞✉r❛✲ t✐♦♥❴ should be equal to zero or greater than or equal to ❴♠✐♥❉✉r❛t✐♦♥:

\u0060\u0060\u0060plaintext
r❡q✉✐r❡✭
   ❞✉r❛t✐♦♥❴ ❂❂ ✵ ⑤⑤ ❞✉r❛t✐♦♥❴ ❃❂ ❴♠✐♥❉✉r❛t✐♦♥✱
   ✧❞✉r❛t✐♦♥ t♦♦ s♠❛❧❧✧
\u0060\u0060\u0060

But we are not checking this in ❝❛❧▼✐♥t❙t❛❦✐♥❣P♦✇❡r when we have some r❡♠❛✐♥✐♥❣ ❞✉r❛t✐♦♥ left because we are only checking if r❞ is greater than zero. This consideration assumes ❧♦❝❦❚✐♠❡❴ is zero and our ❧♦❝❦❆♠♦✉♥t❴ is greater than zero because we are staking ❧♦❝❦❆♠♦✉♥t❴ for r❞ time for our attack:

\u0060\u0060\u0060plaintext
❢✉♥❝t✐♦♥ ❝❛❧▼✐♥t❙t❛❦✐♥❣P♦✇❡r✭
   ▲▲♦❝❦❡r✳❙▲♦❝❦ ♠❡♠♦r② ♦❧❞▲♦❝❦❉❛t❛✱
   ✉✐♥t ❧♦❝❦❆♠♦✉♥t❴✱
   ✉✐♥t ❧♦❝❦❚✐♠❡❴✱
   ❜♦♦❧ ✐s❙❡❧❢❙t❛❦❡❴✱
   ✉✐♥t s❡❧❢❙t❛❦❡❆❞✈❛♥t❛❣❡❴
\u0060\u0060\u0060

✮ ✐♥t❡r♥❛❧ ✈✐❡✇ r❡t✉r♥s ✭✉✐♥t✮ ④

\u0060\u0060\u0060plaintext
✉✐♥t r❞ ❂ ▲▲♦❝❦❡r✳r❡st❉✉r❛t✐♦♥✭♦❧❞▲♦❝❦❉❛t❛✮❀
✉✐♥t ♦❧❞❆▲♦❝❦ ❂ ♦❧❞▲♦❝❦❉❛t❛✳❛♠♦✉♥t❀
✉✐♥t ❞▲♦❝❦❋♦r❖❧❞❆ ❂ ❧♦❝❦❚✐♠❡❴❀
✉✐♥t ❞▲♦❝❦❋♦r❙t❛❦❡❆ ❂ ❧♦❝❦❚✐♠❡❴ ✰ r❞❀
✐❢ ✭❧♦❝❦❚✐♠❡❴ ❂❂ ✵✮ ④
   r❡q✉✐r❡✭r❞ ❃ ✵✱ ✧❛❧r❡❛❞② ✉♥❧♦❝❦❡❞✧✮❀
\u0060\u0060\u0060

\u0060\u0060\u0060plaintext
⑥
✉✐♥t rs ❂ ✭♦❧❞❆▲♦❝❦ ✯
   ❝❛❧▼✉❧t✐♣❧✐❡r❋♦r❖❧❞❆♠♦✉♥t✭❞▲♦❝❦❋♦r❖❧❞❆✮ ✰
   ❧♦❝❦❆♠♦✉♥t❴ ✯
   ❝❛❧▼✉❧t✐♣❧✐❡r✭❞▲♦❝❦❋♦r❙t❛❦❡❆✮✮ ✴ ▲P❡r❝❡♥t❛❣❡✳❉❊▼■❀
\u0060\u0060\u0060

✐❢ ✭✐s❙❡❧❢❙t❛❦❡❴✮ ④

\u0060\u0060\u0060plaintext
rs ❂ ✭rs ✯ s❡❧❢❙t❛❦❡❆❞✈❛♥t❛❣❡❴✮ ✴ ▲P❡r❝❡♥t❛❣❡✳❉❊▼■❀
\u0060\u0060\u0060

⑥  
r❡t✉r♥ rs❀  
⑥  

Now, attackers can take advantage of this to win the voting and earn Geth from whichever side they want. Now, let\u0027s see how someone can take advantage of this. Let\u0027s say someone has staked ❴♠✐♥❙t❛❦❡❉❈❚❆✲ ♠♦✉♥t for ♦♥❡ ♠♦♥t❤. When the r❡♠❛✐♥✐♥❣ ❞✉r❛t✐♦♥ is very small, they can take advantage of this. Basically, if we consider the r❡♠❛✐♥✐♥❣ ❞✉r❛t✐♦♥ to be ✶ s❡❝♦♥❞, then our multiplier will be ✵✳✽✽. 

So, essentially, they can use any amount they want to lock for only 1 second and use the powerMinted to vote on \u0027voteId\u0027. Now let\u0027s take an example: An attacker has staked ✼ ●♦❛t tokens for one month because it will be the minimum required amount. There is a voting going on with ✈♦t✐♥❣ ■❉. The attacker can take a loan of a large amount of Goat tokens at the last second when the r❡♠❛✐♥✐♥❣ ❞✉r❛t✐♦♥ is ✶ s❡❝♦♥❞. They will stake it to receive ❞P✷P❉❚♦❦❡♥ t♦❦❡♥s, then proceed to vote on some ✈♦t❡■❉s. After that, they will call ❧♦❝❦❲✐t❤❞r❛✇ function with ✐s❋♦r❝❡❞ function set to true, and then repay their loan with a ❢❡❡. Because they\u0027re withdrawing with ✐s❋♦r❝❡❞ equal to true, they will need to bear a little loss since they will be withdrawing ✶ s❡❝♦♥❞ early. However, if their earnings from votes can exceed the loss of the fee and penalty for withdrawing ✶ s❡❝♦♥❞ ❡❛r❧②, an attacker can plan this type of attack on a large scale. If the ♠✐♥❙t❛❦❡❆♠♦✉♥t is much less, it will be very easy for him to perform this attack.

Let\u0027s say the attacker has taken a loan of ✶✵✵ ●♦❛t, and he\u0027s staking for when the remaining duration is ✶ s❡❝♦♥❞, then powerMinted is 88. After the attack, he can withdraw the same amount using the formula below, considering ❋❙ is 10000 then the duration will be ✶ ♠♦♥t❤ because we staked 7 Goat for 1 month in starting. 

❚♦t❛❧ will be 100 Goat, ❞✉r❛t
