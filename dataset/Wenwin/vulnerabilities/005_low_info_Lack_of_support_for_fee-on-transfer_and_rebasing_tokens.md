# Lack of support for fee-on-transfer and rebasing tokens

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wenwin
**Keywords:** cyber security, vulnerability, impact fee, transfer tokens, rebasing tokens, protocol, incorrect amounts, proof of concept, DAI, ticket purchase, fee on transfer, 2% fee, balance check, mitigation steps, documentation, user claim, expected amount, token economics, smart contracts, financial protocol

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/91b89482aaedf8b8feb73c771d11c257eed997e8/src/Lottery.sol#L130


# Vulnerability details

## Impact
Fee on transfer and rebasing tokens can result in incorrect amounts being transferred to and from the protocol.

## Proof of Concept
Sponsor has noted that we should consider tokens other than DAI to be used with the protocol. Here we consider fee on transfer and rebasing tokens. 

Each ticket purchased with a fee on transfer token or rebasing token will result in a different amount being received by the protocol than intended. There exist no checks that the actual amount received will be as intended. 

Consider for example a fee on transfer token with a 2% fee on each transfer. When a user buys a ticket, they will pay the ticket cost, but the protocol will only receive 98% of that amount. Later when a user goes to claim a ticket, they will also only receive 98% of the expected amount.

## Recommended Mitigation Steps
Either:
- Add a check to enforce the change in balance being sufficient to cover e.g. the ticket cost, or
- Add documentation noting not to use fee on transfer or rebasing tokens with the protocol
