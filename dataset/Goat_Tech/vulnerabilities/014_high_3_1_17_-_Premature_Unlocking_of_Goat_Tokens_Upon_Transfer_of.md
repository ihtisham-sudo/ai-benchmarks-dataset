# 3.1.17 - Premature Unlocking of Goat Tokens Upon Transfer of Lock

**Severity:** high
**Auditor:** Cantina
**Protocol:** Goat Tech
**Keywords:** Goat tokens, transfer, lock, admin, timestamp, vesting schedule, investor, contract, function, update, security, risk, Ethereum, smart contract, Vester.sol, timestamp issue, lock transfer, investor rights, premature unlocking, code vulnerability

---

# 3.1.17 - Premature Unlocking of Goat Tokens Upon Transfer of Lock
- **Submitted by**: Vijay, also found by etherhood and Haxatron
- **Severity**: High Risk
- **Context**: Vester.sol#L52-L71
- **Description**: In the \u0060❱❡st❡r✳s♦❧\u0060 contract, the admin has the capability to transfer an investor\u0027s lock to another account via the \u0060tr❛♥s❢❡r▲♦❝❦\u0060 function. However, during this transfer, the \u0060st❛rt❡❞❆t\u0060 timestamp is not being updated. Due to this, Goat tokens of the investor will be unlocked right away irrespective of the vesting schedule. 

As \u0060st❛rt❡❞❆t\u0060 isn\u0027t set in \u0060tr❛♥s❢❡r▲♦❝❦\u0060 function, \u0060st❛rt❡❞❆t\u0060 value for \u0060t♦\u0060 account will stay zero even after calling \u0060tr❛♥s❢❡r▲♦❝❦\u0060 function. Due to this, \u0060♣❛st❚✐♠❡\u0060 in the below function will always be calculated to \u0060❜❧♦❝❦✳t✐♠❡st❛♠♣\u0060 in the below function.
