# Guardian will not be able to cancel a malicious proposal

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** guardian, cancellation, malicious proposal, setGuardian, vulnerability, AdminVoting, solidity, protocol risk, funds draining, action payload, attack vector, proposal, security, bypass protection, uncancellable actions, audit, smart contract, testing, proof of concept, voting power

---

# Guardian will not be able to cancel a malicious proposal
Submitted by 0xTheBlackPanther, also found by 0xBeastBoy, stormreckson, la-arana-inteligente, JesJupyter, 0xD-jango and Kasheeda

- **Severity:** Medium Risk
- **Context:** \u0060AdminVoting.sol#L362-L363\u0060
- **Summary:** A malicious actor can bypass guardian cancellation protection by bundling malicious actions with \u0060setGuardian\u0060 in a proposal. The guardian cannot cancel any proposal containing \u0060setGuardian\u0060, even when it includes other dangerous actions.

### Vulnerability Details:
In \u0060AdminVoting.sol\u0060, the \u0060_containsSetGuardianPayload()\u0060 function checks for \u0060setGuardian\u0060 calls in ALL actions:

\u0060\u0060\u0060solidity
function _containsSetGuardianPayload(uint256 payloadLength, Action[] memory payload) {
    for (uint256 i; i < payloadLength; i++) {
        if (sig == IBimaCore.setGuardian.selector) return true; // @audit-poc
    }
    return false;
}
\u0060\u0060\u0060

This allows an attacker to:
1. Create a proposal with multiple actions.
2. Include \u0060setGuardian\u0060 anywhere in the payload.
3. Add malicious actions like draining funds.
4. The guardian cannot cancel because of \u0060setGuardian\u0060 presence.

### Impact:
- Guardian\u0027s ability to protect the protocol is severely compromised.
- Malicious proposals cannot be cancelled if they include \u0060setGuardian\u0060.
- Protocol funds and parameters at risk from uncancellable malicious actions.

### Proof of Concept:
Copy and run the below test in \u0060test/foundry/dao/AdminVotingTest.t.sol\u0060:

\u0060\u0060\u0060solidity
function test_guardian_cannot_cancel_malicious_proposal_with_setGuardian() public {
    // First give voting power to attacker (using user1 as attacker)
\u0060\u0060\u0060
