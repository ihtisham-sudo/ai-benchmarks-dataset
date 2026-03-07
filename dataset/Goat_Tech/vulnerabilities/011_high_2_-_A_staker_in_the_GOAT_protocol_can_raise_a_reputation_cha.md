# 2 - A staker in the GOAT protocol can raise a reputation challenge against any other staker

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** GOAT protocol, reputation challenge, vote, challenger, defender, wstETH, earnings, freeze, transaction, front-run, gas fees, manipulation, assets, vulnerability, exploits, proof of concept, Foundry Project, Arbitrum Sepolia, RPC provider, transactions

---

# 1. Anyone can steal protocol\u0027s llido assets and ether balance using its distributive functions
**Submitted by:** 0xumarkhatab  
**Severity:** High Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** Due to lack of access control on following functions, anyone can call these functions and steal the LLido reserves (which is converted to ether balance mostly) and smart contract\u0027s Ether balance.  
- **Function:** \u0060getReserves()\u0060
    - **Description:** Allows access to the reserves of the contract.
- **Function:** \u0060getBalance(address)\u0060
    - **Description:** Anyone can get all contract balance different account & \u0060transferFrom(address)\u0060:
        - **Description:** Allows transferring of funds from one account to another.

**Recommendation:** Have an upper limit on the Owner% and User% to prevent this attack. I would recommend requiring a signature for transfers.

**Goat:** Fixed
Asthesefunctionsdoesnotchecktheauthorityof ♠s❣✳s❡♥❞❡r,andtheinternalcallsarenon-revertingif observedclosely. Sonooneiskeepinganyonecallingthesefunctions. Whentherearecertainamountof reserves in the contract whether in the form of wrapped tokens or Ether balance and transfer all those assets to them. Becausethefundsarebeingtransferredtoeitherdirectoryto♠s❣✳s❡♥❞❡r:

- ❛❞❞r❡ss ❛❝❝♦✉♥t ❂ ♠s❣✳s❡♥❞❡r
## Code
\u0060\u0060\u0060solidity
// Example code snippet
function exampleFunction() public {
    // Function implementation
}
\u0060\u0060\u0060

AdditonallythesefunctionsarealsosubjecttoMEVsoifanylegituseriscallingthesefunctions,aMEVbot wouldpickthistransactionfrommempoolsimulateintheirenvironment,andtheywillseetheyaregain- ing Ether. So they would make the same transaction by themselves and change the params accordingly andsubmitthistransactionwithhighergasfeespotentiallyearningthefunds. Thelegit user\u0027s transaction will fail.

Implementaccesscontrolonthesefunctionandtheparameterspassedtofunctions, e.g. require whether ♠s❣✳s❡♥❞❡r & ❜♦✉♥t②P✉❧❧❡r are authorized to call these functions.

Fixed
**Submitted by:** b0g0  
**Severity:** High Risk  
**Context:** (No context files were provided by the reviewer)  

A staker in the GOAT protocol can raise a reputation challenge against any other staker. This happens by creating a vote, where the challenger (❛tt❛❝❦❡r) and the challenged (❞❡❢❡♥❞❡r) are the 2 sides. The attacker locks wstETH in the ❱♦t✐♥❣✳s♦❧ contract proportional to the amount of the defender earnings he wants to freeze. Vote creation happens through the ❈♦♥tr♦❧❧❡r✳❝r❡❛t❡❱♦t❡✭ function:

\u0060\u0060\u0060
❢✉♥❝t✐♦♥ ❝r❡❛t❡❱♦t❡✭
    ❛❞❞r❡ss ❞❡❢❡♥❞❡r❴✱
    ✉✐♥t ❞❊t❤❱❛❧✉❡❴✱
    ✉✐♥t ✈♦t❡rP❡r❝❡♥t❴✱
    ✉✐♥t ❢r❡❡③❡❉✉r❛t✐♦♥❴✱
    ✉✐♥t ♠✐♥❲st❡t❤❆❴✱
    ✉✐♥t ✇st❡t❤❆❴
\u0060\u0060\u0060

\u0060\u0060\u0060
✮
    ❡①t❡r♥❛❧
    ♣❛②❛❜❧❡
\u0060\u0060\u0060

\u0060\u0060\u0060
④
    r❡q✉✐r❡✭❴✐sP❛✉s❡❞❆tt❛❝❦ ❂❂ ✵✱ ✧♣❛✉s❡❞✧✮❀
    ❛❞❞r❡ss ❛tt❛❝❦❡r ❂ ♠s❣✳s❡♥❞❡r❀
    ✴✴ ❴✇❡t❤✳❞❡♣♦s✐t④✈❛❧✉❡✿ ❛❞❞r❡ss✭t❤✐s✮✳❜❛❧❛♥❝❡⑥✭✮❀
    ❴♣r❡♣❛r❡❲st❡t❤✭♠✐♥❲st❡t❤❆❴✱ ✇st❡t❤❆❴✮❀
    ✉✐♥t ❛❊t❤❱❛❧✉❡ ❂ ❴❣❡t❤✳❜❛❧❛♥❝❡❖❢✭❛❞❞r❡ss✭t❤✐s✮✮❀
    r❡q✉✐r❡✭❞❡❢❡♥❞❡r❴ ✦❂ ❛❞❞r❡ss✭❴❞❡✈❚❡❛♠✮✮❀
    r❡q✉✐r❡✭❞❊t❤❱❛❧✉❡❴ ❃❂ ❴♠✐♥❉❡❢❡♥❞❡r❋✉♥❞✱ ✧❞❊t❤❱❛❧✉❡❴ t♦♦ s♠❛❧❧✧✮❀
    r❡q✉✐r❡✭✈♦t❡rP❡r❝❡♥t❴ ❁❂ ❴♠❛①❱♦t❡rP❡r❝❡♥t✱ ✧✈♦t❡rP❡r❝❡♥t❴ t♦♦ ❤✐❣❤✧✮❀
    r❡q✉✐r❡✭❢r❡❡③❡❉✉r❛t✐♦♥❴ ❃❂ ❴♠✐♥❋r❡❡③❡❉✉r❛t✐♦♥ ✫✫ ❢r❡❡③❡❉✉r❛t✐♦♥❴ ❁❂ ❴♠❛①❋r❡❡③❡❉✉r❛t✐♦♥✱ ✧❢r❡❡③❡❉✉r❛t✐♦♥❴
\u0060\u0060\u0060

\u0060\u0060\u0060
֒→  ✐♥✈❛❧✐❞✧✮❀
    r❡q✉✐r❡✭❛❊t❤❱❛❧✉❡ ❁❂ ❞❊t❤❱❛❧✉❡❴ ✫✫ ❛❊t❤❱❛❧✉❡ ✯ ▲P❡r❝❡♥t❛❣❡✳❉❊▼■ ✴ ❞❊t❤❱❛❧✉❡❴ ❃❂ ❴♠✐♥❆tt❛❝❦❡r❋✉♥❞❘❛t❡✱
\u0060\u0060\u0060

\u0060\u0060\u0060
֒→  ✧❛❊t❤❱❛❧✉❡ ✐♥✈❛❧✐❞✧✮❀
    ✴✴ ✳✳✳
\u0060\u0060\u0060
## The following check is the one we should focus on, since it will be the one exploited:
\u0060\u0060\u0060
r❡q✉✐r❡✭❛❊t❤❱❛❧✉❡ ❁❂ ❞❊t❤❱❛❧✉❡❴ ✫✫ ❛❊t❤❱❛❧✉❡ ✯ ▲P❡r❝❡♥t❛❣❡✳❉❊▼■ ✴ ❞❊t❤❱❛❧✉❡❴ ❃❂ ❴♠✐♥❆tt❛❝❦❡r❋✉♥❞❘❛t❡✱
\u0060\u0060\u0060
\u0060\u0060\u0060
֒→  ✧❛❊t❤❱❛❧✉❡ ✐♥✈❛❧✐❞✧✮❀
\u0060\u0060\u0060

It basically makes sure that the amount locked by the ❛tt❛❝❦❡r is ❁❂ than the amount frozen on the ❞❡❢❡♥❞❡r. And the attacker amount is calculated based on the balances like so:

\u0060\u0060\u0060
✉✐♥t ❛❊t❤❱❛❧✉❡ ❂ ❴❣❡t❤✳❜❛❧❛♥❝❡❖❢✭❛❞❞r❡ss✭t❤✐s✮✮❀
\u0060\u0060\u0060

This makes it quite easy for an interested party to front-run the ❝r❡❛t❡❱♦t❡✭✮ trx and transfer enough ✇st❊❚❍ to the ❈♦♥tr♦❧❧❡r contract, so that ❛❊t❤❱❛❧✉❡ ❃ ❞❊t❤❱❛❧✉❡❴, which will revert it. What makes this exploit even less costly for the malicious actor is that he can sandwich ❝r❡❛t❡❱♦t❡✭✮ with another transaction right after it and withdrawal the wstETH he transferred in the first transaction. He can do this by calling ❈♦♥tr♦❧❧❡r✳❡❛r♥✐♥❣❲✐t❤❞r❛✇✭✮, which unwraps the ✇st❊❚❍ balances sitting in ❈
- **Affected Assets**: Vulnerability affecting assets.
- **Description**: The cost of the attack for the exploiter is reduced only to the gas fees for the 2 transactions, which is nothing.
- **Proof of Concept**: Since the protocol has no tests, I created a Foundry Project and wrote fork tests using the contracts deployed on Arbitrum Sepolia. The used Sepolia RPC provider is a demo one (I actually used Alchemy).

- **Affected Assets**: Various affected assets.
- **Description**: The vulnerability affects the following transactions:
  - Transaction 1
  - Transaction 2
  - Transaction 3
  - Transaction 4
  - Transaction 5
  - Transaction 6

- **Affected Assets**: Specific assets with potential exploits.
- **Description**: The vulnerability allows for various exploits through specific transactions.

- **Affected Assets**: Assets with transaction vulnerabilities.
- **Description**: The vulnerability allows for manipulation of transaction costs.
## ❡①t❡r♥❛❧
### ❢✉♥❝t✐♦♥ ❝r❡❛t❡❱♦t❡✭
- ❛❞❞r❡ss ❞❡❢❡♥❞❡r
- ✉✐♥t ❞❊t❤❱❛❧✉❡
- ✉✐♥t ✈♦t❡rP❡r❝❡♥t
- ✉✐♥t ❢r❡❡③❡❉✉r❛t✐♦♥
- ✉✐♥t ♠✐♥❲st❡t❤❆
- ✉✐♥t ✇st❡t❤❆
## ❡①t❡r♥❛❧ ♣❛②❛❜❧❡
### ❢✉♥❝t✐♦♥ ✈♦t✐♥❣❈❧❛✐♠❋♦r✭
- ✉✐♥t ✈♦t❡■❞ ❛❞❞r❡ss ✈♦t❡r
- ❢✉♥❝t✐♦♥ ❡❛r♥✐♥❣❲✐t❤❞r❛✇❉❡✈❚❡❛♠✭
- ❢✉♥❝t✐♦♥ ❝❧❛✐♠❘❡✈❡♥✉❡❙❤❛r❡❉❡✈❚❡❛♠✭
- ❢✉♥❝t✐♦♥ ✉♣❞❛t❡❈♦♥❢✐❣s✭✉✐♥t❬❪ ♠❡♠♦r② ✈❛❧✉❡s

## ✐♥t❡r❢❛❝❡ ■❆❝❝❡ss❈♦♥tr♦❧❧
### ❢✉♥❝t✐♦♥ ❛♣♣r♦✈❡❆❞♠✐♥
- ❛❞❞r❡ss ❛❞♠✐♥

## ✐♥t❡r❢❛❝❡ ■❱♦t✐♥❣
### str✉❝t ❙❱♦t❡❇❛s✐❝■♥❢♦
- ❛❞❞r❡ss ❛tt❛❝❦❡r
- ❛❞❞r❡ss ❞❡❢❡♥❞❡r
- ✉✐♥t ❛❊t❤❱❛❧✉❡
- ✉✐♥t ❞❊t❤❱❛❧✉❡
- ✉✐♥t ✈♦t❡rP❡r❝❡♥t
- ✉✐♥t ❛◗✉♦r✉♠
- ✉✐♥t st❛rt❡❞❆t
- ✉✐♥t ❡♥❞❆t
- ✉✐♥t ❛tt❛❝❦❡rP♦✇❡r
- ✉✐♥t ❞❡❢❡♥❞❡rP♦✇❡r
- ✉✐♥t t♦t❛❧❈❧❛✐♠❡❞
- ❜♦♦❧ ✐s❋✐♥❛❧✐③❡❞
- ❜♦♦❧ ✐s❆tt❛❝❦❡r❲♦♥
- ✉✐♥t ✇✐♥❱❛❧
- ✉✐♥t ✇✐♥♥❡rP♦✇❡r
- ❜♦♦❧ ✐s❈❧♦s❡❞

## ❢✉♥❝t✐♦♥ ❝r❡❛t❡❱♦t❡✭
- ❛❞❞r❡ss ❛tt❛❝❦❡r
- ❛❞❞r❡ss ❞❡❢❡♥❞❡r
- ✉✐♥t ❛❊t❤❱❛❧✉❡
- ✉✐♥t ❞❊t❤❱❛❧✉❡
- ✉✐♥t ✈♦t❡rP❡r❝❡♥t
- ✉✐♥t ❛◗✉♦r✉♠
- ✉✐♥t st❛rt❡❞❆t
- ✉✐♥t ❡♥❞❆t

## ❢✉♥❝t✐♦♥ ❣❡t❱♦t❡✭
- ✉✐♥t ✈♦t❡■❞
- ❢✉♥❝t✐♦♥ ❝❧❛✐♠❋♦r✭✉✐♥t ✈♦t❡■❞ ❛❞❞r❡ss ✈♦t❡r
- ❢✉♥❝t✐♦♥ ❞❡❢❡♥❞❡r❊❛r♥✐♥❣❋r❡❡③❡❞❖❢✭
- ❛❞❞r❡ss ❛❝❝♦✉♥t
\u0060\u0060\u0060
s❤❛r❡❈♦♠♠✐ss✐♦♥✭❛❞❞r❡ss ❛❝❝♦✉♥t❴✮ ❡①t❡r♥❛❧
\u0060\u0060\u0060

\u0060\u0060\u0060
✉♣❞❛t❡✭❛❞❞r❡ss ❛❝❝♦✉♥t❴✱ ❜♦♦❧ ♥❡❡❞❙❤❛r❡❈♦♠♠
\u0060\u0060\u0060

\u0060\u0060\u0060
✇✐t❤❞r❛✇✭❛❞❞r❡ss ❛❝❝♦✉♥t❴✱ ✉✐♥t ❛♠♦✉♥t❴✱ ❛❞❞r❡ss ❞❡st
\u0060\u0060\u0060

\u0060\u0060\u0060
❡❛r♥✐♥❣❖❢✭❛❞❞r❡ss ❛❝❝♦✉♥t❴✮ ❡①t❡r♥❛❧ ✈✐❡✇ r❡t✉r♥s ✭✉✐♥t
\u0060\u0060\u0060

\u0060\u0060\u0060
♠❛①❊❛r♥✐♥❣❖❢✭❛❞❞r❡ss ❛❝❝♦✉♥t❴✮ ❡①t❡r♥❛❧ ✈✐❡✇ r❡t✉r♥s ✭✉✐♥t
\u0060\u0060\u0060

\u0060\u0060\u0060
s❡t❯♣✭✮ ♣✉❜❧✐❝
\u0060\u0060\u0060
