# ❝❛❧❉✉r❛t✐♦♥ is called.

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** vote, finalize, locking, fund, Alice, Bob, attacker, locked money, voting rewards, contract, bug, scenarios, value, check, user, pool owner, sacrifice, challenge, voter share, transaction

---

# ❝❛❧❉✉r❛t✐♦♥ is called.
### ❢✉♥❝t✐♦♥ ❝❛❧❉✉r❛t✐♦♥✭
- ❙▲♦❝❦ ♠❡♠♦r② ❧♦❝❦❉❛t❛❴✱
- ✉✐♥t ❢s❴✱
- ❜♦♦❧ ✐sP♦♦❧❖✇♥❡r❴
  
### ✮
- ✐♥t❡r♥❛❧
- ♣✉r❡
- r❡t✉r♥s✭✉✐♥t✮

### ④
- ✉✐♥t ♠❋❛❝t♦r ❂ ✐sP♦♦❧❖✇♥❡r❴ ❄ ✷ ✯ ▲P❡r❝❡♥t❛❣❡✳❉❊▼■ ✲ ❢s❴ ✿ ❢s❴❀
- ✉✐♥t ❞✉r❛t✐♦♥ ❂ ❧♦❝❦❉❛t❛❴✳❞✉r❛t✐♦♥ ✯ ♠❋❛❝t♦r ✴ ▲P❡r❝❡♥t❛❣❡✳❉❊▼■❀
- r❡t✉r♥ ❞✉r❛t✐♦♥❀

## ⑥
Since Alice isn\u0027t the pool owner, ♠❋❛❝t♦r ❂ ✵.  
❞✉r❛t✐♦♥ ❂ ✶✵✵ ❞❛②s ✯ ✵ ✴ ✶✵✵✵✵ ❂ ✵.  
The function will revert every time we hit this line, as we will attempt to divide by 0, which will panic revert the transaction.  
✉✐♥t r❡❝❡✐✈❡❞❆ ❂ t♦t❛❧ ✯ ♣❛st❚✐♠❡ ✴ ❞✉r❛t✐♦♥❀  
Alice cannot withdraw the tokens she locked, until she receives ❊❛r♥✐♥❣ tokens from somewhere and her balance gets updated.  
**Recommendation:** Have a special case for when ❢s ❂ ✵. Maybe set ❢s to ❉❊▼■ if it is 0, not sure exactly what the protocol team might want.  
**Goat:** Fixed  

## 3.2.12 r❡q✉✐r❡✭✇✐♥✈❛❧ ❃ ✵✮ can lead to votes never able to be finalized and locking users fund forever in certain situations  
**Submitted by:** Chad0  
**Severity:** Medium Risk  
**Context:** Voting.sol#L317  
**Description:** The Attacker Alice can create a vote with ✈♦t❡rP❡r❝❡♥t❴ having the value of ✵, the ✵ value can pass the check of ▲P❡r❝❡♥t❛❣❡✳✈❛❧✐❞❛t❡P❡r❝❡♥t✭✈♦t❡rP❡r❝❡♥t❴✮, so this vote\u0027s ✈♦t❡✳✈♦t❡rP❡r❝❡♥t will be assigned as ✵.  
Then, when someone wants to claim the voting rewards, the call stack will be from ❈♦♥tr♦❧❧❡r contract\u0027s ✈♦t✐♥❣❈❧❛✐♠❋♦r✭✮, into ❱♦t✐♥❣ contract\u0027s ❝❧❛✐♠❋♦r✭✮, then into ❱♦t✐♥❣ contract\u0027s ❴tr②❋✐♥❛❧✐③❡✭✮.  
In ❴tr②❋✐♥❛❧✐③❡✭✮, no matter which party wins, the ✈♦t❡✳✇✐♥❱❛❧ will always be ✵ just because ✈♦t❡✳✈♦t❡rP❡r❝❡♥t is ✵, hence, the ✇✐♥❱❛❧ will be ✵ and this r❡q✉✐r❡✭✮ will always fail for such a vote.  
Because the ❴tr②❋✐♥❛❧✐③❡✭✮ can only be called by the ❝❧❛✐♠❋♦r✭✮ in the same contract, it means such a vote will never be able to be finalized, and neither the attacker nor the defender can get their locked money back.  
This issue is very bad for the game. Consider the scenarios below:  
1. Alice is creating a vote against Bob. Alice knows this bug, and if she hates Bob really bad, she will use ✈♦t❡rP❡r❝❡♥t❴ of ✵ so that she can lock Bob\u0027s entire fund forever, and Alice herself will also sacrifice a small portion of her own money (✉✐♥t ♣✉❜❧✐❝ ❴♠✐♥❆tt❛❝❦❡r❋✉♥❞❘❛t❡ ❂ ✷✺✵✵❀ ✴✴✷✺✪). If Alice is willing to, she can destroy any pool owner\u0027s money at the ratio of 25%.  
2. Or, Alice is creating a vote against Bob but she doesn\u0027t know this bug. Alice may be just a normal user who tries to challenge a pool owner Bob; because Alice is very confident in her own voting power being more than enough, so she doesn\u0027t want to share any rewards with others and she is also likely to use ✵ for ✈♦t❡rP❡r❝❡♥t❴. Especially it is written in the game docs where it even gives an example of using voter share of ✵✪. Normal users can be easily misled to create such votes, leading to their votes never gonna be finalized and they cannot get their fund back.  
Therefore, this issue should be considered as High severity.
