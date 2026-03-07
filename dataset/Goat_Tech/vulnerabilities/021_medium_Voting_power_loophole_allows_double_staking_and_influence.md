# Voting power loophole allows double staking and influence

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** voting, DCT, stake, withdraw, abuser, voting power, influence, loophole, challenge, tokens, contribution, votingToken, addVoter, lockWithdraw, mechanism, prevent, unstaking, remove, power, perpetuate

---

# 3.2.5 ♠❛①❴s✉♣♣❧② will not be reached as there is an early return that does set ✐s♠✐♥t✐♥❣❢✐♥✐s❤❡❞ to early

**Submitted by**: 0xWeiss, also found by Haxatron, cccz, Rotciv Egaf, Tripathi, Auditism, walter, jesjupyter, er-ictee, merlin, AslanbekAibimov, nmirchev8, 0xumarkhatab, Bauchibred, Chad0, sashik-eth, Said, ast3ros, Victor Okafor and tutkata  
**Severity**: Medium Risk  
**Context**: (No context files were provided by the reviewer)  
**Description**: Currently in the ♣✉❜❧✐❝▼✐♥t✭✮ function in DCT, there is a check that if the t♦t❛❧❙✉♣♣❧②✭✮ of tokens + the minting amount:

\u0060\u0060\u0060
✉✐♥t ♠✐♥t✐♥❣❆ ❂ ♣❡♥❞✐♥❣❆✭✮❀
\u0060\u0060\u0060

is bigger than MAX_SUPPLY:

\u0060\u0060\u0060
✐❢ ✭t♦t❛❧❙✉♣♣❧②✭✮ ✰ ♠✐♥t✐♥❣❆ ❃ ▼❆❳❴❙❯PP▲❨✮ ④
\u0060\u0060\u0060

\u0060\u0060\u0060
✐s▼✐♥t✐♥❣❋✐♥✐s❤❡❞ ❂ tr✉❡❀
r❡t✉r♥❀
\u0060\u0060\u0060

theminting of DCT will be finished and no more GOAT will be minted. The issue here is that there will still be GOAT left to be minted even when ✐s▼✐♥t✐♥❣❋✐♥✐s❤❡❞ is true. This is because the ♣❡♥❞✐♥❣❆✭✮ function:

\u0060\u0060\u0060
❢✉♥❝t✐♦♥ ♣❡♥❞✐♥❣❆✭✮ ♣✉❜❧✐❝ ✈✐❡✇ r❡t✉r♥s ✭✉✐♥t✮ ④
\u0060\u0060\u0060

\u0060\u0060\u0060
✐❢ ✭✐s▼✐♥t✐♥❣❋✐♥✐s❤❡❞ ⑤⑤ ❴❧❛st▼✐♥t❆t ❂❂ ✵✮ ④
\u0060\u0060\u0060

\u0060\u0060\u0060
r❡t✉r♥ ✵❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✉✐♥t ♣❛st❚✐♠❡ ❂ ❜❧♦❝❦✳t✐♠❡st❛♠♣ ✲ ❴❧❛st▼✐♥t❆t❀
\u0060\u0060\u0060

\u0060\u0060\u0060
r❡t✉r♥ ❴t♣s ✯ ♣❛st❚✐♠❡❀
\u0060\u0060\u0060

calculates the amount of tokens to be minted per second multiplied by the past time from the last mint. This will only increment with the increase of time, therefore the amount of tokens left to mint post setting ✐s▼✐♥t✐♥❣❋✐♥✐s❤❡❞ ❂ tr✉❡❀ could be a huge amount if the protocol is not the most used one in the space. Just to make things more clear, currently 7 tokens per second should be the minting rate: 

\u0060\u0060\u0060
✉✐♥t ♣r✐✈❛t❡ ❴t♣s ❂ ✼ ❡t❤❡r❀ ✴✴✼ t♦❦❡♥s ♣❡r s❡❝♦♥❞.
\u0060\u0060\u0060

If ▼❆❳❴❙❯PP▲❨ ❂ ✸✶✶✶✻✻✻✻✻✻ and there have been t♦t❛❧❙✉♣♣❧②✭✮ ❂ ✸✶✶✶✻✻✵✵✵✵ tokens minted, meaning there are still 6666 tokens left to be minted, if 953 seconds go through without no one calling ♣✉❜❧✐❝▼✐♥t✭✮ the tokens will never be minted. This is less than 15 minutes without the function being called, which is extremely likely, could be much more.

**Recommendation**: If t♦t❛❧❙✉♣♣❧②✭✮ ✰ ♠✐♥t✐♥❣❆ ❃ ▼❆❳❴❙❯PP▲❨ normalize the ♠✐♥t✐♥❣❆ amount to mint the last tokens before ▼❆❳❴❙❯PP▲❨ is reached:

\u0060\u0060\u0060
✐❢ ✭t♦t❛❧❙✉♣♣❧②✭✮ ✰ ♠✐♥t✐♥❣❆ ❃ ▼❆❳❴❙❯PP▲❨ ④
\u0060\u0060\u0060

\u0060\u0060\u0060
✰ ♠✐♥t✐♥❣❆ ❂ ▼❆❳❴❙❯PP▲❨ ✲ t♦t❛❧❙✉♣♣❧②✭✮❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✐s▼✐♥t✐♥❣❋✐♥✐s❤❡❞ ❂ tr✉❡❀
\u0060\u0060\u0060

\u0060\u0060\u0060
✲ r❡t✉r♥❀
\u0060\u0060\u0060

Goat: fixed if (totalSupply() + mintingA > MAX_SUPPLY) { isMintingFinished = true; _mint(_rewardPool, MAX_SUPPLY - totalSupply()); _lastMintAt = block.timestamp; return; }
**Submitted by:** Auditism  
**Severity:** Medium Risk  
**Context:** Voting.sol, Controller.sol  

When a user stakes DCT, they will be granted some ❞♣✷♣❚♦❦❡♥s. These tokens will allow user to vote against or for the attacker when someone gets challenged. The present issue is that an abuser is able to withdraw his DCT, transfer it to another account, stake it, receive voting power (❞♣✷♣❚♦❦❡♥s) and vote again.
## Impact
Abusers of this loophole are able to stake twice with the same amount of DCT, influencing votes in forbidden ways.

## Proof of concept
When users stake DCT they will be granted some ❞♣✷♣❚♦❦❡♥s:
\u0060\u0060\u0060
♣♦✇❡r▼✐♥t❡❞ ❂ ▲❍❡❧♣❡r✳❝❛❧▼✐♥t❙t❛❦✐♥❣P♦✇❡r✭ ✴✴❅♥♦t❡ rs
    ♦❧❞▲♦❝❦❉❛t❛✱
    ❛▲♦❝❦✱
    ❞✉r❛t✐♦♥❴✱
    ❢❛❧s❡✱
    ❴s❡❧❢❙t❛❦❡❆❞✈❛♥t❛❣❡
\u0060\u0060\u0060
These ❞P✷P❉❚♦❦❡♥s are the _votingToken used in the Voting.sol contract. In the _addVoter() we can see the logic below that will use the dp2pDToken balance of the voter as a way to calculate the voting power he will contribute:
\u0060\u0060\u0060
✉✐♥t ♣♦✇❡r ❂ ❴✈♦t✐♥❣❚♦❦❡♥✳❜❛❧❛♥❝❡❖❢✭✈♦t❡r❴✮❀
    ✉✐♥t ✈♦t❡❉✉r❛t✐♦♥ ❂ ✈♦t❡✳❡♥❞❆t ✲ ✈♦t❡✳st❛rt❡❞❆t❀
    ✉✐♥t ♣❛st❚✐♠❡ ❂ ❜❧♦❝❦✳t✐♠❡st❛♠♣ ✲ ✈♦t❡✳st❛rt❡❞❆t❀
    ✉✐♥t r❡st❉✉r❛t✐♦♥ ❂ ✈♦t❡❉✉r❛t✐♦♥ ✲ ♣❛st❚✐♠❡❀
    ♣♦✇❡r ❂ ♣♦✇❡r ✯ r❡st❉✉r❛t✐♦♥ ✴ ✈♦t❡❉✉r❛t✐♦♥❀
    ✐❢ ✭♣♦✇❡r ❂❂ ✵✮ ④
        ✴✴ ❛❞❞ ✶ ✇❡✐ t♦ ❛✈♦✐❞ ❝❛s❡ t♦t❛❧P♦✇❡r ❂ ✵
        ♣♦✇❡r ❂ ✶❀
\u0060\u0060\u0060
However when withdrawing DCT with the lockWithdraw()
\u0060\u0060\u0060
r❡q✉✐r❡✭r❡st❆♠♦✉♥t ❂❂ ✵ ⑤⑤ r❡st❆♠♦✉♥t ❃❂ ❴♠✐♥❙t❛❦❡❉❈❚❆♠♦✉♥t✱ ✧r❡st ❛♠♦✉♥t t♦♦ s♠❛❧❧✧✮❀
✉✐♥t ❜✉r♥❡❞P♦✇❡r ❂ ▲❍❡❧♣❡r✳❝❛❧❇✉r♥❙t❛❦✐♥❣P♦✇❡r✭❴❞P✷P❉❚♦❦❡♥✳❜❛❧❛♥❝❡❖❢✭♣♦♦❧❖✇♥❡r❴✮✱ ❛♠♦✉♥t❴✱
\u0060\u0060\u0060
Previous voting positions are not removed which means that the voting contribution will perpetuate, and the abuser is able to send ❉❈❚ to another address, stake it, receive ❞♣✷♣❉❚♦❦❡♥ and vote again.

In order to mitigate this issue before unstaking DCT, add a mechanism to prevent abusive behavior, such as if a user has a current voting power > 0, denied from unstaking, or to remove all the power this user possesses prior to unstaking.
