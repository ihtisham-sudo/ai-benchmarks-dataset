# ✐s❱❛❧✐❞❙✐❣♥❛t✉r❡✭✮signaturereplayinaccountswithsharedowners

**Severity:** high
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** ERC1271, signature, replay attack, Clave, account, ownership, hashing, EIP712, validation, security, smart contract, Ethereum, multi-signature, signers, transactions, domain separator, type-struct, RLP, messages, conversion

---

# ✐s❱❛❧✐❞❙✐❣♥❛t✉r❡✭✮signaturereplayinaccountswithsharedowners
**Severity:** High Risk  
**Context:** ERC1271Handler.sol  
**Description:** To validate a signature using the ERC1271 standard, the Clave ✐s❱❛❧✐❞❙✐❣♥❛t✉r❡✭ utilizes its ❴❤❛♥❞❧❡❱❛❧✐❞❛t✐♦♥✭✮ function on the s✐❣♥❡❞❍❛s❤:
\u0060\u0060\u0060
❢✉♥❝t✐♦♥ ✐s❱❛❧✐❞❙✐❣♥❛t✉r❡✭
   ❜②t❡s✸✷ s✐❣♥❡❞❍❛s❤✱
   ❜②t❡s ❝❛❧❧❞❛t❛ s✐❣♥❛t✉r❡❆♥❞❱❛❧✐❞❛t♦r
✮ ❡①t❡r♥❛❧ ✈✐❡✇ ♦✈❡rr✐❞❡ r❡t✉r♥s ✭❜②t❡s✹ ♠❛❣✐❝❱❛❧✉❡✮ ④
   ✭❜②t❡s ♠❡♠♦r② s✐❣♥❛t✉r❡✱ ❛❞❞r❡ss ✈❛❧✐❞❛t♦r✮ ❂ ❙✐❣♥❛t✉r❡❉❡❝♦❞❡r✳❞❡❝♦❞❡❙✐❣♥❛t✉r❡◆♦❍♦♦❦❉❛t❛✭
     s✐❣♥❛t✉r❡❆♥❞❱❛❧✐❞❛t♦r
 ✮❀
 ❜♦♦❧ ✈❛❧✐❞ ❂ ❴❤❛♥❞❧❡❱❛❧✐❞❛t✐♦♥✭✈❛❧✐❞❛t♦r✱ s✐❣♥❡❞❍❛s❤✱ s✐❣♥❛t✉r❡✮❀
 ♠❛❣✐❝❱❛❧✉❡ ❂ ✈❛❧✐❞ ❄ ❴❊❘❈✶✷✼✶❴▼❆●■❈ ✿ ❜②t❡s✹✭✵✮❀
\u0060\u0060\u0060
Since ❴❤❛♥❞❧❡❱❛❧✐❞❛t✐♦♥✭✮ directly forwards the s✐❣♥❡❞❍❛s❤ to the ✈❛❧✐❞❛t♦r, this implementation only checks that the raw s✐❣♥❡❞❍❛s❤ has been signed by one of the k1/r1 owners of the account. If multiple Clave accounts share an owner, one signature can be valid for all accounts, which could allow for signature replay.  
**Recommendation:** To ensure that a signature is only valid for a specific Clave account, the ERC1271 s✐❣♥❡❞❍❛s❤ argument can be additionally hashed with ❛❞❞r❡ss✭t❤✐s✮ before forwarding to the ❴❤❛♥❞❧❡✲ ❱❛❧✐❞❛t✐♦♥✭✮ function. To do this in a standard way, consider using EIP712, which includes ❛❞❞r❡ss✭t❤✐s✮ as the ✈❡r✐❢②✐♥❣❈♦♥tr❛❝t in the domain separator. This also allows you to define a custom EIP712 type-struct (such as "❈❧❛✈❡▼❡ss❛❣❡✭❜②t❡s ♠❡ss❛❣❡✮") to use when signing an ERC1271 message. Additionally, note that the ❊❖❆❱❛❧✐❞❛t♦r does convert the s✐❣♥❡❞❍❛s❤ using t♦❊t❤❙✐❣♥❡❞▼❡ss❛❣❡❍❛s❤✭✮, which is a conversion that\u0027s useful for differentiating between signed messages and signed RLP encoded transactions. Since EIP712 also makes this differentiation, the t♦❊t❤❙✐❣♥❡❞▼❡ss❛❣❡❍❛s❤✭✮ conversion is not strictly necessary in the ✐s❱❛❧✐❞❙✐❣♥❛t✉r❡✭✮ scenario. So, as part of the overall change, consider only applying t♦❊t❤❙✐❣♥❡❞▼❡ss❛❣❡❍❛s❤✭✮ to the s✐❣♥❡❞❍❛s❤ in the ❴✈❛❧✐❞❛t❡❚r❛♥s❛❝t✐♦♥✭✮ path.  
**Clave:** Fixed in commit 8f29439f. Additionally removed t♦❊t❤❙✐❣♥❡❞▼❡ss❛❣❡❍❛s❤✭✮ in commit 68b8678d, since all AA transactions are signed using EIP-712 which makes them distinct from RLP encoded transactions already.  
**CantinaManaged:** Verified.
