# 2 - Edge Case in Withdrawal Calculation

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** withdrawal, calculation, tokens, burn, voting power, private mode, transfer, stake, locked, withdraw, earnings, update, balance, locked tokens, sponsor, pool, edge case, user, withdrawal process, impossible withdraw

---

# 1. Lack of slippage control in token swaps
**Submitted by:** erictee, also found by Lefg, b0g0, Auditism, walter, 0xrex, jesjupyter, 0xRajkumar, 0xTheBlackPanther, zigtur, twcctop, ladboy233, Bauchibred, deth, 0xRizwan, innertia, merlin, Tripathi, Rotciv, Egaf, smbv19192323, john-femi, Said, 0xhashiman and tutkata  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** When swapping the tokens with function \u0060swapTokens\u0060, the slippage control is disabled by configuring the \u0060slippage\u0060 to zero. This can potentially expose the swap/trade to sandwich attacks and MEV (Miner Extractable Value) attacks, resulting in a suboptimal amount of tokens received from the swap/trade.

- In \u0060swapTokens\u0060:
    - \u0060require\u0060 checks are bypassed
    - \u0060require\u0060 checks are bypassed
    - Tokens are swapped without proper checks

**Recommendation:** One possible solution is to dynamically compute the minimum amount of tokens to be received after the swap based on the maximum allowable slippage percentage (e.g. 5%) and the exchange rate (SourceToken to DestinationToken) from a source that cannot be manipulated (e.g. Chainlink, Custom TWAP). Alternatively, consider restricting access to these functions to only certain actors who can be trusted to define an appropriate slippage parameter where possible.
Submitted by zigtur, also found by deth  
Severity: Medium Risk  
Context: Controller.sol  
Description: During ❈♦♥tr♦❧❧❡r✳❧♦❝❦❲✐t❤❞r❛✇, a part of the user\u0027s voting power is burnt. This burnt amount depends on the amount of token withdrawn compared to his total amount staked AND the current voting power of the user.  
If user has 10 voting power tokens and withdraws 50% of its staked amount, then 5 voting power tokens will be burnt.  
When the voting power token is not in private mode, transfers are enabled. Then, the user can transfer his voting power tokens to another account, withdraw his tokens and transfer back its voting power. By doing so, none of his voting power tokens will be burnt.  
Proof of concept:  
The attached code shows the calculation of the burnt amount. If user transfer his ❴❞P✷P❉❚♦❦❡♥ balance, then no ❴❞P✷P❉❚♦❦❡♥ will be burnt.  
Recommendation: Ensure that the voting power tokens are never set to private mode disabled.  
Goal: Fixed by removing the ❴♣r✐✈❛t❡▼♦❞❡ completely.  

Submitted by deth  
Severity: Medium Risk  
Context: (No context files were provided by the reviewer)  
Description: When withdrawing we use ✇✐t❤❞r❛✇:  
❢✉♥❝t✐♦♥ ❴✇✐t❤❞r❛✇✭  
    ❛❞❞r❡ss ❛❝❝♦✉♥t❴✱  
    ❛❞❞r❡ss ♣♦♦❧❖✇♥❡r❴✱  
    ❛❞❞r❡ss ❞❡st❴✱  
    ✉✐♥t ❛♠♦✉♥t❴✱  
    ❜♦♦❧ ✐s❋♦r❝❡❞❴  
✮  
    ✐♥t❡r♥❛❧  
④  
    ❜②t❡s✸✷ ❧♦❝❦■❞ ❂ ▲▲♦❝❦❡r✳❣❡t▲♦❝❦■❞✭❛❝❝♦✉♥t❴✱ ♣♦♦❧❖✇♥❡r❴✮❀ ✴✴♦❦  
    ▲▲♦❝❦❡r✳❙▲♦❝❦ st♦r❛❣❡ ❧♦❝❦❉❛t❛ ❂ ❴❧♦❝❦❉❛t❛❬❧♦❝❦■❞❪❀ ✴✴♦❦  
    ❜♦♦❧ ✐sP♦♦❧❖✇♥❡r ❂ ❛❝❝♦✉♥t❴ ❂❂ ♣♦♦❧❖✇♥❡r❴❀ ✴✴♦❦  
    ✉✐♥t ❢s ❂ ❴♣r♦❢✐❧❡❈✳❢s❖❢✭♣♦♦❧❖✇♥❡r❴✮❀  
    ✐❢ ✭✦✐s❋♦r❝❡❞❴✮ ④  
        r❡q✉✐r❡✭▲▲♦❝❦❡r✳✐s❯♥❧♦❝❦❡❞✭❧♦❝❦❉❛t❛✱ ❢s✱ ✐sP♦♦❧❖✇♥❡r✮✱ ✧♥♦t ✉♥❧♦❝❦❡❞✧✮❀  
    ⑥  
    ✉✐♥t ❞✉r❛t✐♦♥ ❂ ▲▲♦❝❦❡r✳❝❛❧❉✉r❛t✐♦♥✭❧♦❝❦❉❛t❛✱ ❢s✱ ✐sP♦♦❧❖✇♥❡r✮❀  
    ✉✐♥t ♣❛st❚✐♠❡ ❂ ❜❧♦❝❦✳t✐♠❡st❛♠♣ ✲ ❧♦❝❦❉❛t❛✳st❛rt❡❞❆t❀  
    ✐❢ ✭♣❛st❚✐♠❡ ❃ ❞✉r❛t✐♦♥✮ ④  
        ♣❛st❚✐♠❡ ❂ ❞✉r❛t✐♦♥❀  
    ⑥  
    ❧♦❝❦❉❛t❛✳❛♠♦✉♥t ✲❂ ❛♠♦✉♥t❴❀  
    ✉✐♥t t♦t❛❧ ❂ ❛♠♦✉♥t❴❀  
    ✉✐♥t r❡❝❡✐✈❡❞❆ ❂ t♦t❛❧ ✯ ♣❛st❚✐♠❡ ✴ ❞✉r❛t✐♦♥❀  
    ❴❝❛s❤❖✉t✭❞❡st❴✱ r❡❝❡✐✈❡❞❆✮❀  
    ✐❢ ✭t♦t❛❧ ✦❂ r❡❝❡✐✈❡❞❆✮ ④  
        ❴❝❛s❤❖✉t✭❴♣❡♥❛❧t②❆❞❞r❡ss✱ t♦t❛❧ ✲ r❡❝❡✐✈❡❞❆✮❀  
    ⑥  
    ❡♠✐t ❲✐t❤❞r❛✇✭❛❝❝♦✉♥t❴✱ ♣♦♦❧❖✇♥❡r❴✱ ❞❡st❴✱ ❛♠♦✉♥t❴✮❀  
    ❡♠✐t ❯♣❞❛t❡▲♦❝❦❉❛t❛✭❛❝❝♦✉♥t❴✱ ♣♦♦❧❖✇♥❡r❴✱ ❴❧♦❝❦❉❛t❛❬❧♦❝❦■❞❪✮❀
## Edge Case in Withdrawal Calculation

❢s❖❢ is used to calculate how much r❡❝❡✐✈❡❞❆ a user should receive when withdrawing. An edge case is possible where ❢s❖❢ ❂ ✵, which makes it impossible to withdraw. For example:

1. Alice has 100 Geth locked for 100 days.
2. Her ✐❢s gets set to ✵ since she has no ❊❛r♥✐♥❣ tokens and no ♠❛①❊❛r♥✐♥❣❖❢. This is correct as if she tries to call ❧♦❝❦❲✐t❤❞r❛✇ now, ❢s❖❢ will return 10000, as it inverts her ✐❢s.
3. Alice receives 5 ❊❛r♥✐♥❣ tokens from:
   - Eithersomeonetransferredthemtoher,that\u0027spossibleif❊❛r♥✐♥❣isnotinprivatemode,which allows for the transferring of tokens.
   - She earned them by being a sponsor of a pool, as when someone stakes, the sponsor of that pool gets a small % of ❊❛r♥✐♥❣ tokens minted to them.
4. Alice then calls ❊❛r♥✐♥❣✳✉♣❞❛t❡ to update her ❴s❤❛r❡❞❆ and ❴♠❛①❊❛r♥✐♥❣❖❢.
5. Thenshedecidestowithdrawherearningsbycalling❡❛r♥✐♥❣❲✐t❤❞r❛✇.
6. Alice calls ❡❛r♥✐♥❣❲✐t❤❞r❛✇ to withdraw her 5 ❊❛r♥✐♥❣ tokens.
   ❢✉♥❝t✐♦♥ ✇✐t❤❞r❛✇✭
   ❛❞❞r❡ss ❛❝❝♦✉♥t❴✱
   ✉✐♥t ❛♠♦✉♥t❴✱
   ❛❞❞r❡ss ❞❡st❴
   ✮
   ❡①t❡r♥❛❧
   ♦♥❧②❆❞♠✐♥
   ④
   s❤❛r❡❈♦♠♠✐ss✐♦♥✭❛❝❝♦✉♥t❴✮❀
   ❴❜✉r♥✭❛❝❝♦✉♥t❴✱ ❛♠♦✉♥t❴✮❀
   ❴s❤❛r❡❞❆❬❛❝❝♦✉♥t❴❪ ❂ ❜❛❧❛♥❝❡❖❢✭❛❝❝♦✉♥t❴✮❀
   ❴❝❛s❤❖✉t✭❞❡st❴✱ ❛♠♦✉♥t❴✮❀
   ❡♠✐t ❲✐t❤❞r❛✇✭❛❝❝♦✉♥t❴✱ ❛♠♦✉♥t❴✱ ❞❡st❴✮❀
7. ✇✐t❤❞r❛✇willburnher5tokensandcashherout. Herbalanceisnow0andher♠❛①❊❛r♥✐♥❣❖❢isstill 5.
8. r❡❈❛❧❋s is called immediately after that: ✵ ✯ ✶✵✵✵✵ ✴ ✺ ❂ ✵, so her ✐❢s ❂ ✶✵✵✵✵.
9. Alice then decides to ❧♦❝❦❲✐t❤❞r❛✇ all her 100 tokens that are in the lock.
10. ▲♦❝❦❡r✳✇✐t❤❞r❛✇ is hit:
    ❢✉♥❝t✐♦♥ ❴✇✐t❤❞r❛✇✭
    ❛❞❞r❡ss ❛❝❝♦✉♥t❴✱
    ❛❞❞r❡ss ♣♦♦❧❖✇♥❡r❴✱
    ❛❞❞r❡ss ❞❡st❴✱
    ✉✐♥t ❛♠♦✉♥t❴✱
    ❜♦♦❧ ✐s❋♦r❝❡❞❴
    ✮
    ✐♥t❡r♥❛❧
    ④
    ❜②t❡s✸✷ ❧♦❝❦■❞ ❂ ▲▲♦❝❦❡r✳❣❡t▲♦❝❦■❞✭❛❝❝♦✉♥t❴✱ ♣♦♦❧❖✇♥❡r❴✮❀ ✴✴♦❦
    ▲▲♦❝❦❡r✳❙▲♦❝❦ st♦r❛❣❡ ❧♦❝❦❉❛t❛ ❂ ❴❧♦❝❦❉❛t❛❬❧♦❝❦■❞❪❀ ✴✴♦❦
    ❜♦♦❧ ✐sP♦♦❧❖✇♥❡r ❂ ❛❝❝♦✉♥t❴ ❂❂ ♣♦♦❧❖✇♥❡r❴❀ ✴✴♦❦
    ✉✐♥t ❢s ❂ ❴♣r♦❢✐❧❡❈✳❢s❖❢✭♣♦♦❧❖✇♥❡r❴✮❀
    ✐❢ ✭✦✐s❋♦r❝❡❞❴✮ ④
       r❡q✉✐r❡✭▲▲♦❝❦❡r✳✐s❯♥❧♦❝❦❡❞✭❧♦❝❦❉❛t❛✱ ❢s✱ ✐sP♦♦❧❖✇♥❡r✮✱ ✧♥♦t ✉♥❧♦❝❦❡❞✧✮❀
    ⑥
    ✉✐♥t ❞✉r❛t✐♦♥ ❂ ▲▲♦❝❦❡r✳❝❛❧❉✉r❛t✐♦♥✭❧♦❝❦❉❛t❛✱ ❢s✱ ✐sP♦♦❧❖✇♥❡r✮❀
    ✉✐♥t ♣❛st❚✐♠❡ ❂ ❜❧♦❝❦✳t✐♠❡st❛♠♣ ✲ ❧♦❝❦❉❛t❛✳st❛rt❡❞❆t❀
    ✐❢ ✭♣❛st❚✐♠❡ ❃ ❞✉r❛t✐♦♥✮ ④
       ♣❛st❚✐♠❡ ❂ ❞✉r❛t✐♦♥❀
    ⑥
    ❧♦❝❦❉❛t❛✳❛♠♦✉♥t ✲❂ ❛♠♦✉♥t❴❀
    ✉✐♥t t♦t❛❧ ❂ ❛♠♦✉♥t❴❀
    ✉✐♥t r❡❝❡✐✈❡❞❆ ❂ t♦t❛❧ ✯ ♣❛st❚✐♠❡ ✴ ❞
