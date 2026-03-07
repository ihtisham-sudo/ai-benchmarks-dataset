# HAL-26 - BE - MNEMONIC PHRASE EXPOSURE IN MEMORY

**Severity:** HIGH
**Auditor:** Halborn

---

##### Description

The Mnemonic Phrase of the wallet kept unencrypted in memory, even the wallet was locked. As a result, an attacker with access to the user’s machine could exfiltrate the Mnemonic Phrase. It was possible to retrieve the Mnemonic Phrase from memory in these three cases:

* When creating the wallet, it was possible to dump the mnemonic from memory
* When revealing the mnemonic after having logged in, mnemonics stayed in the memory as long as the process running.
* When recovering a wallet by copying the mnemonic and pasting it directly to the browser extension.
* When wallet was in locked state, mnemonics stayed in the memory as long as the process running.

It is crucial to recognize that the mnemonic risk extends beyond the application state; it could also be leaked into memory when the browser displays the mnemonic in clear text and as long as the process running. This potential leakage poses a significant security concern, emphasizing the need for careful handling of such sensitive information within the browser environment.

##### Proof of Concept

![Unencrypted Mnemonic Phrase in-memory, when wallet was in locked state](https://halbornmainframe.com/proxy/audits/images/6785045f6287e28dcdc0b5fe)![](https://halbornmainframe.com/proxy/audits/images/678505236c7eae81f009c215)

##### Score

Impact: 5  
Likelihood: 3

##### Recommendation

The identified vulnerability arises from the application's handling of sensitive data in plain text. To mitigate this, the team recommends the following strategies:

- Opt for storing the entropy on disk rather than the mnemonic itself. When the mnemonic is necessary in the code, consider breaking it into multiple variables. Alternatively, obfuscate the original phrase and subsequently dereference the variable holding the original phrase.

- For instances requiring Mnemonic Phrase handling, utilize the obfuscated variable with a function designed to reconstruct the original Mnemonic Phrase exactly at the point of need.

- Ensure that when the wallet is in a locked state, the mnemonic phrase is completely cleared from memory.

For the display and handling of the mnemonic phrase during wallet creation and when revealed to a logged-in user:

- Display the mnemonic phrase using an HTML5 canvas. This technique helps prevent users from copying the phrase, reducing the risk of it being unintentionally stored in memory via the clipboard.

- Limit the ability for users to copy the entire mnemonic from the extension. This approach is essential in minimizing the potential for the mnemonic to be accidentally leaked through the clipboard, thereby enhancing the security of the sensitive information.

Implementing these recommendations would significantly enhance the security of mnemonic phrase handling, reducing the risks associated with its exposure or misuse.

##### Remediation

**SOLVED:** The **InFlux Technologies team** addressed the issue by splitting the seed phrase and private key into multiple parts during copying, which prevents direct exposure. Additional warnings and explanations have also been added to inform users about the associated risks.

##### Remediation Hash

9ae59d25865e5a5249a850e0a4b37cdc64e5d26a
