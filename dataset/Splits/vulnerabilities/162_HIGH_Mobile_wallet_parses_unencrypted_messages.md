# Mobile wallet parses unencrypted messages

**Severity:** HIGH
**Auditor:** TrailOfBits

---

## Authentication
## Target: Mobile Authentication

**Difficulty:** Low

### Description
Message parsing code in the mobile application allows the parsing of unencrypted messages, bypassing the requirement for a shared secret key to send malicious messages. The decryption and underlying parsing of messages is completed within the same function on mobile devices. If the nonce field exists in the JSON message, it is assumed the payload is awaiting decryption, in which case the application will perform the decryption and a recursive call to parse it. If the payload field does not exist, it is assumed the payload has been decrypted, and it is loaded accordingly. Consequently, the mobile application will parse unencrypted responses and present unauthenticated information to the user.

```kotlin
fun parseResponse(response: String): ParseResponse {
    // Parse response JSON
    // [...]
    
    // Check if input string is encrypted
    if (json.containsKey("nonce")) {
        val decrypted = decrypt(json["nonce"].toString(), json["payload"].toString())
        if (decrypted.startsWith("error")) {
            return ParseResponse(false, "Encryption Error: $decrypted", true)
        }
        return parseResponse(decrypted)
    }
    // Parse underlying commands
    // [...]
}
```

*Figure 1: Response parsing excerpt (DataModel.kt#L73-L79)*

Furthermore, decryption and parsing recursion based on the existence of a nonce field means that a user could pre-compute a message which has undergone many rounds of encryption. This message could then be spammed to the user to force the mobile app to perform all necessary rounds of decryption.

### Exploit Scenario
With knowledge about Alice’s desktop wallet server’s IP, Eve could poison the network to redirect traffic to her own server code, or assign herself the server’s previous IP when it is released. In the event that the mobile client connects to Eve’s malicious server, Eve could ignore all encrypted incoming traffic and leverage the implications of TOB-ZEC-001 to force Alice’s mobile client to parse unencrypted responses to requests that were never sent, or that Eve has no knowledge of.

This would allow Eve to spoof information such as balances, transaction history, and the receive addresses for Alice’s wallet. Assuming Bob wishes to send Alice funds, Alice could unknowingly share a malicious receive-address with Bob, resulting in the loss of Bob’s funds.

### Recommendation
Short term, the `parseResponse` function should be split into two functions: a function which performs decryption of the payload, and a function which parses decrypted payloads. This way, encryption will always be expected.

Long term, make a note of any invariants related to cryptography, such as the expectation of encryption on some packets. Ensure these invariants hold and are not subject to conditions an attacker could leverage.

Appendix B contains a proof of concept python server which replicates this issue.
