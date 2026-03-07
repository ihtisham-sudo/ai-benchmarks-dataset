# .1 Anyone can vote multiple times by using multiple addresses and transferring a voting token if private mode is off

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** voting, token, manipulation, private mode, transfer, multiple addresses, voting power, contract, exploit, balance, functionality, risk, logic, implementation, security, voting manipulation, user, amount, core problem, decentralized

---

# .1 Anyone can vote multiple times by using multiple addresses and transferring a voting token if private mode is off

Submitted by stiglitz, also found by jesjupyter, Rotciv Egaf, nmirchev8, Haxatron, PENGUN and Said  
Severity: High Risk  
Context: Voting.sol  
Description: The token used for voting is the ❉❚♦❦❡♥ (based on the deployment script). The P❊❘❈ contract (inherited by ❉❚♦❦❡♥) implements so-called ♣r✐✈❛t❡ ♠♦❞❡. If the contract is in ♣r✐✈❛t❡ ♠♦❞❡, transfer functions are not callable. However, if the mode is off, there is a place for voting manipulation. I am not sure when or in what type of circumstances the private mode will be on/off. However, because the functionality is there and transfers are not banned completely, I chose the likelihood medium.  
Exploit scenario:
- ❉❚♦❦❡♥ is not in ♣r✐✈❛t❡ ♠♦❞❡.
- User ❆ who has an amount ❳ of ❉❚♦❦❡♥ calls ❱♦t✐♥❣✿✿✉♣❞❛t❡P♦✇❡r. It will take the ❉❚♦❦❡♥ balance of user ❆ and use it as a voting power.
- User ❆ transfers ❳ amount of ❉❚♦❦❡♥ to user ❇.
- User ❆ now has ✵ amount. User ❇ now has ❳ amount.
- User ❇ who has amount ❳ of ❉❚♦❦❡♥ calls ❱♦t✐♥❣✿✿✉♣❞❛t❡P♦✇❡r. It will take the ❉❚♦❦❡♥ balance of user ❇ and use it as a voting power.  
This way the voting power of ❳ amount of ❉❚♦❦❡♥ will be used twice in ✈♦t❡✳❛tt❛❝❦❡rP♦✇❡r ✰❂ ♣♦✇❡r or ✈♦t❡✳❞❡❢❡♥❞❡rP♦✇❡r ✰❂ ♣♦✇❡r❀. User ❆ can create ♥ addresses to make his power ♥ times stronger.  
Core problem: The main problem is that ❉❚♦❦❡♥ does not implement logic to move voting power together with transferred amount. It only calls ❉✐str✐❜✉t♦r contracts and updates rewards there.  
- ❉❚♦❦❡♥✿✿❴❜❡❢♦r❡❚♦❦❡♥❚r❛♥s❢❡r  
    ❢✉♥❝t✐♦♥ ❴❜❡❢♦r❡❚♦❦❡♥❚r❛♥s❢❡r✭  
    ❛❞❞r❡ss ❢r♦♠❴✱  
    ❛❞❞r❡ss t♦❴✱  
    ✉✐♥t✷✺✻ ❛♠♦✉♥t❴  
- ✮  
    ✐♥t❡r♥❛❧  
    ✈✐rt✉❛❧  
    ♦✈❡rr✐❞❡  
- ④  
    ✉✐♥t ✐ ❂ ✵❀  
    ✉✐♥t ♥ ❂ ❴t♦t❛❧❉✐str✐❜✉t♦rs❀  
    ✇❤✐❧❡ ✭✐ ❁ ♥✮ ④  
        ❴❞✐str✐❜✉t♦rs❬✐❪✳❜❡❢♦r❡❚♦❦❡♥❚r❛♥s❢❡r✭❢r♦♠❴✱ t♦❴✱ ❛♠♦✉♥t❴✮❀  
        ✐✰✰❀  
    ⑥  
- ⑥  
Goat: Fixed by removing the ❴♣r✐✈❛t❡▼♦❞❡ completely.
