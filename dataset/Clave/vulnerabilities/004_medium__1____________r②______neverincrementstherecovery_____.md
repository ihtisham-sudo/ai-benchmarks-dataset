# .1 ❈❧♦✉❞❘❡❝♦✈❡r②▼♦❞✉❧❡neverincrementstherecovery♥♦♥❝❡

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** cloud recovery, account security, replay attack, increment, recovery module, mapping, private key, lock account, functionality, vulnerability, smart contract, Ethereum, solidity, bug, fix, commit, verification, recommendation, risk, module

---

# .1 ❈❧♦✉❞❘❡❝♦✈❡r②▼♦❞✉❧❡neverincrementstherecovery♥♦♥❝❡
- **Severity**: MediumRisk
- **Context**: CloudRecoveryModule.sol#L96-L128
- **Description**: When the st❛rt❘❡❝♦✈❡r②✭✮ function is called on a recovery module, it is intended that the account\u0027s recovery ♥♦♥❝❡ is incremented. However, this is currently missing from the ❈❧♦✉❞❘❡❝♦✈❡r②▼♦❞✲ ✉❧❡. As a consequence, anyone can replay an account\u0027s cloud recovery. This could temporarily disable additional recovery attempts, and if the private key for the original recovery\u0027s ♥❡✇❖✇♥❡r has been lost, would lock the account.
- **Recommendation**: Increment the r❡❝♦✈❡r②◆♦♥❝❡s mapping in ❈❧♦✉❞❘❡❝♦✈❡r②▼♦❞✉❧❡:
    ❢✉♥❝t✐♦♥ st❛rt❘❡❝♦✈❡r②✭❘❡❝♦✈❡r②❉❛t❛ ❝❛❧❧❞❛t❛ r❡❝♦✈❡r②❉❛t❛✱ ❜②t❡s ❝❛❧❧❞❛t❛ s✐❣♥❛t✉r❡✮ ❡①t❡r♥❛❧ ④
    ❛❞❞r❡ss r❡❝♦✈❡r✐♥❣❆❞❞r❡ss ❂ r❡❝♦✈❡r②❉❛t❛✳r❡❝♦✈❡r✐♥❣❆❞❞r❡ss❀
    ✐❢ ✭r❡❝♦✈❡r②❉❛t❛✳♥♦♥❝❡ ✦❂ r❡❝♦✈❡r②◆♦♥❝❡s❬r❡❝♦✈❡r✐♥❣❆❞❞r❡ss❪✮ ④
        r❡✈❡rt ❊rr♦rs✳■◆❱❆▲■❉❴❘❊❈❖❱❊❘❨❴◆❖◆❈❊✭✮❀
    ⑥
    ✐❢ ✭✐s❘❡❝♦✈❡r✐♥❣✭r❡❝♦✈❡r✐♥❣❆❞❞r❡ss✮✮ ④
        r❡✈❡rt ❊rr♦rs✳❘❊❈❖❱❊❘❨❴■◆❴P❘❖●❘❊❙❙✭✮❀
    ⑥
    ✐❢ ✭✦✐s■♥✐t❡❞✭r❡❝♦✈❡r✐♥❣❆❞❞r❡ss✮✮ ④
        r❡✈❡rt ❊rr♦rs✳❘❊❈❖❱❊❘❨❴◆❖❚❴■◆■❚❊❉✭✮❀
    ⑥
    ❜②t❡s✸✷ ❡✐♣✼✶✷❍❛s❤ ❂ ❴❤❛s❤❚②♣❡❞❉❛t❛❱✹✭❴r❡❝♦✈❡r②❉❛t❛❍❛s❤✭r❡❝♦✈❡r②❉❛t❛✮✮❀
    ❛❞❞r❡ss ❣✉❛r❞✐❛♥ ❂ ❝❧♦✉❞●✉❛r❞✐❛♥❬r❡❝♦✈❡r✐♥❣❆❞❞r❡ss❪❀
    ✐❢ ✭✦❣✉❛r❞✐❛♥✳✐s❱❛❧✐❞❙✐❣♥❛t✉r❡◆♦✇✭❡✐♣✼✶✷❍❛s❤✱ s✐❣♥❛t✉r❡✮✮ ④
        r❡✈❡rt ❊rr♦rs✳■◆❱❆▲■❉❴●❯❆❘❉■❆◆❴❙■●◆❆❚❯❘❊✭✮❀
    ⑥
    r❡❝♦✈❡r②❙t❛t❡s❬r❡❝♦✈❡r②❉❛t❛✳r❡❝♦✈❡r✐♥❣❆❞❞r❡ss❪ ❂ ❘❡❝♦✈❡r②❙t❛t❡✭④
        t✐♠❡❧♦❝❦❊①♣✐r②✿ ❜❧♦❝❦✳t✐♠❡st❛♠♣ ✰ ❚■▼❊▲❖❈❑✱
        ♥❡✇❖✇♥❡r✿ r❡❝♦✈❡r②❉❛t❛✳♥❡✇❖✇♥❡r
    ⑥✮❀
    ✰    r❡❝♦✈❡r②◆♦♥❝❡s❬r❡❝♦✈❡r✐♥❣❆❞❞r❡ss❪✰✰❀
        ❡♠✐t ❘❡❝♦✈❡r②❙t❛rt❡❞✭
            r❡❝♦✈❡r②❉❛t❛✳r❡❝♦✈❡r✐♥❣❆❞❞r❡ss✱
            r❡❝♦✈❡r②❉❛t❛✳♥❡✇❖✇♥❡r✱
            ❜❧♦❝❦✳t✐♠❡st❛♠♣ ✰ ❚■▼❊▲❖❈❑
    ✮❀
    ⑥
- **Clave**: Fixed with commit 989bc989.
- **CantinaManaged**: Verified.
