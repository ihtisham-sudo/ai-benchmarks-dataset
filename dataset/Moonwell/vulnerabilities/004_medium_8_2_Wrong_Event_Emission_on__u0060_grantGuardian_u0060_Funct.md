# 8.2 Wrong Event Emission on \u0060_grantGuardian\u0060 Function

**Severity:** medium
**Auditor:** Halborn
**Protocol:** Moonwell
**Keywords:** Solidity, smart contract, event emission, pause guardian, multichain governor, address, previous guardian, new guardian, unpaused, emit, function, internal, contract, recommendation, code snippet, remediation, acknowledged, centralization, validation, custom errors

---

# 8.2 Wrong Event Emission on \u0060_grantGuardian\u0060 Function
**Description**  
It is important to highlight the \u0060_grantGuardian\u0060 internal function in \u0060ConfigurablePauseGuardian\u0060 contract as follows:

\u0060\u0060\u0060solidity
function _grantGuardian(address newPauseGuardian) internal {
    address previousPauseGuardian = newPauseGuardian;
    pauseGuardian = newPauseGuardian;
    /// if a new guardian is granted, the contract is automatically unpaused
    _setPauseTime(0);
    emit PauseGuardianUpdated(previousPauseGuardian, newPauseGuardian);
}
\u0060\u0060\u0060

We can observe that the event \u0060PauseGuardianUpdated\u0060 is emitted with the same values for \u0060oldPauseGuardian\u0060 and \u0060newPauseGuardian\u0060. This happens because the value attributed for \u0060address previousPauseGuardian\u0060 is \u0060newPauseGuardian\u0060 instead of \u0060pauseGuardian\u0060. The \u0060MultichainGovernor\u0060 contract is also impacted because it inherits from \u0060ConfigurablePauseGuardian\u0060.

**BVSS**  
AO:A/AC:L/AX:L/C:N/I:L/A:N/D:N/Y:N/R:N/S:C (3.1)

It is recommended to modify the \u0060_grantGuardian\u0060 function in \u0060ConfigurablePauseGuardian\u0060 as follows:

\u0060\u0060\u0060solidity
function _grantGuardian(address newPauseGuardian) internal {
    address previousPauseGuardian = pauseGuardian;
    pauseGuardian = newPauseGuardian;
    /// if a new guardian is granted, the contract is automatically unpaused
    _setPauseTime(0);
    emit PauseGuardianUpdated(previousPauseGuardian, newPauseGuardian);
}
\u0060\u0060\u0060

**SOLVED:** The Moonwell team has solved this issue as recommended in the provided code snippet.

[Remediation Hash](https://github.com/moonwell-ﬁ/moonwell-contracts-v2/pull/147)
The smart contracts under analysis have owners with privileged rights to perform administrative operations and need to be trusted not to act maliciously.
- \u0060src/Governance/MultichainGovernor/MultichainVoteCollection.sol\u0060
  \u0060\u0060\u0060solidity
  function setGasLimit(uint96 newGasLimit) external onlyOwner {
  \u0060\u0060\u0060
- \u0060src/Governance/MultichainGovernor/MultichainVoteCollection.sol\u0060
  \u0060\u0060\u0060solidity
  function setNewStakedWell(address newStakedWell) external onlyOwner {
  \u0060\u0060\u0060

BVSS  
AO:A/AC:L/AX:L/C:N/I:L/A:N/D:N/Y:N/R:P/S:C (1.6)

It is recommended to mitigate centralization issues by implementing multi-signature mechanisms. This prevents a single entity from performing administrative and protected tasks unilaterally.

ACKNOWLEDGED: The Moonwell team has acknowledged the issue and informed that potential centralization concerns are mitigated because in this case, the owner of the contract is the Temporal Governor.
In the \u0060MultichainGovernor\u0060 contract, proposals can be executed if they were previously succeeded, with arbitrary \u0060calldatas\u0060, \u0060values\u0060 and \u0060targets\u0060 contract addresses provided by the creator when calling the propose function, accordingly to the current implemented logic.

\u0060\u0060\u0060solidity
function execute(
    uint256 proposalId
) external payable override whenNotPaused {
    /// Checks
    require(
        state(proposalId) == ProposalState.Succeeded,
        "MultichainGovernor: proposal can only be executed if it is Succeeded"
    );
    uint256 totalValue = 0;
    Proposal storage proposal = proposals[proposalId];
    for (uint256 i = 0; i < proposal.targets.length; ) {
        totalValue += proposal.values[i];
        unchecked {
            i++;
        }
    }
    require(totalValue == msg.value, "MultichainGovernor: invalid value");
    /// Effects
    proposal.executed = true;
    /// remove the proposal that is about to be executed from all proposals,
    /// and remove from inactive proposals from user list
    _syncTotalLiveProposals();
    /// Interactions
    unchecked {
        for (uint256 i = 0; i < proposal.targets.length; i++) {
            proposal.targets[i].functionCallWithValue(
                proposal.calldatas[i],
                proposal.values[i],
                "MultichainGovernor: execute call failed"
            );
        }
    }
    emit ProposalExecuted(proposalId);
}
\u0060\u0060\u0060

There are no verifications in place that validate whether the values provided by the creator when calling the propose function are legitimate. Likewise, there are no such verifications on the execute function, what could lead to malformed calls being performed to targets. Moving forward, the call to \u0060targets[i].functionCallWithValue\u0060 will revert in cases the constructed \u0060calldatas\u0060 and \u0060values\u0060 are not valid for that specific target. This could lead to a scenario where the proposal status is...
set to, but succeeded can never be set to executed because of the failed calls.

BVSS  
AO:A/AC:L/AX:L/C:N/I:L/A:N/D:N/Y:N/R:P/S:C (1.6)

It is recommended to perform validation on user-provided data (inputs) when the function propose is called. A whitelist mechanism, similar to the one applied to the break glass functionality would be a good starting point. By whitelisting possible calldatas and targets, preferably, using mappings, it is possible to ensure that only valid and authorized arguments are passed when calling functionCallWithValue, making it less likely to revert. Alternatively, enhancing the proposal state management, for example, adding a bool executionFailed element to the Proposal struct or adding ExecutionFailed to the ProposalState enum, both in the IMultichainGovernor could improve the handling of such scenarios. Moving in this direction, it would also be possible to modify the cancel function to handle these scenarios appropriately.

ACKNOWLEDGED: The Moonwell team accepted the risk in benefit of the contract being as future-proof as possible, as restricting that calldata only interacts with an allowed list of contracts, or must be executable/would not revert on propose, would be too restrictive and inflexible. The team mentioned it\u0027s an intended behavior because the additional contracts and calls the governor might need to make in the future are yet unknown.
## Remediation Hash
[Remediation Hash](https://github.com/moonwell-ﬁ/moonwell-contracts-v2/pull/147)
## 8.5 USE CUSTOM ERRORS

In Solidity smart contract development, replacing hard-coded revert message strings with the \u0060Error()\u0060 syntax is an optimization strategy that can significantly reduce gas costs. Hard-coded strings, stored on the blockchain, increase the size and cost of deploying and executing contracts. The \u0060Error()\u0060 syntax allows for the definition of reusable, parameterized custom errors, leading to a more efficient use of storage and reduced gas consumption. This approach not only optimizes gas usage during deployment and interaction with the contract but also enhances code maintainability and readability by providing clearer, context-specific error information.

**BVSS**  
AO:A/AC:L/AX:L/C:N/I:N/A:N/D:N/Y:N/R:N/S:C (1.0)

It is recommended to replace hard-coded revert strings in \u0060require\u0060 statements for custom errors, which can be done following the logic below.

1. Standard require statement (to be replaced):
   \u0060\u0060\u0060solidity
   require(condition, "Condition not met");
   \u0060\u0060\u0060

2. Declare the error definition to state:
   \u0060\u0060\u0060solidity
   error ConditionNotMet();
   \u0060\u0060\u0060

3. As currently is not possible to use custom errors in combination with \u0060require\u0060 statements, the standard syntax is:
   \u0060\u0060\u0060solidity
   if (!condition) revert ConditionNotMet();
   \u0060\u0060\u0060

More information about this topic in Official Solidity Documentation.

ACKNOWLEDGED: The Moonwell team has acknowledged this finding and has opted not to perform modifications as a style decision.

[https://github.com/moonwell-fi/moonwell-contracts-v2/pull/147](https://github.com/moonwell-fi/moonwell-contracts-v2/pull/147)
## INFORMATIONAL

Indexed event fields make the data more quickly accessible to off-chain tools that parse events, and adds them to a special data structure known as “topics” instead of the data part of the log. A topic can only hold a single word (32 bytes) so if you use a reference type for an indexed argument, the Keccak-256 hash of the value is stored as a topic instead.

Each event can use up to three indexed fields. If there are fewer than three fields, all of the fields can be indexed. It is important to note that each index field costs extra gas during emission, so it\u0027s not necessarily best to index the maximum allowed fields per event (three indexed fields). This is specially recommended when gas usage is not particularly of concern for the emission of the events in question, and the benefits of querying those fields in an easier and straight-forward manner surpasses the downsides of gas usage increase.

- src/Governance/MultichainGovernor/IMultichainGovernor.sol
  \u0060\u0060\u0060solidity
  event StartBlockSet(uint256 proposalId, uint256 startBlock);
  \u0060\u0060\u0060

- src/Governance/MultichainGovernor/IMultichainGovernor.sol
  \u0060\u0060\u0060solidity
  event VoteCast(
  \u0060\u0060\u0060

- src/Governance/MultichainGovernor/IMultichainGovernor.sol
  \u0060\u0060\u0060solidity
  event ProposalCreated(
  \u0060\u0060\u0060

- src/Governance/MultichainGovernor/IMultichainGovernor.sol
  \u0060\u0060\u0060solidity
  event ProposalCanceled(uint256 id);
  \u0060\u0060\u0060

- src/Governance/MultichainGovernor/IMultichainGovernor.sol
  \u0060\u0060\u0060solidity
  event ProposalQueued(uint256 id, uint256 eta);
  \u0060\u0060\u0060

- src/Governance/MultichainGovernor/IMultichainGovernor.sol
  \u0060\u0060\u0060solidity
  event ProposalExecuted(uint256 id);
  \u0060\u0060\u0060

- src/Governance/MultichainGovernor/IMultichainGovernor.sol
  \u0060\u0060\u0060solidity
  event BreakGlassExecuted(
  \u0060\u0060\u0060
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event QuroumVotesChanged(uint256 oldValue, uint256 newValue);
    - event QuroumVotesChanged(uint256 oldValue, uint256 newValue);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event ProposalThresholdChanged(uint256 oldValue, uint256 newValue);
    - event ProposalThresholdChanged(uint256 oldValue, uint256 newValue);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event VotingPeriodChanged(uint256 oldValue, uint256 newValue);
    - event VotingPeriodChanged(uint256 oldValue, uint256 newValue);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event BreakGlassGuardianChanged(address oldValue, address newValue);
    - event BreakGlassGuardianChanged(address oldValue, address newValue);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event GovernanceReturnAddressChanged(address oldValue, address newValue);
    - event GovernanceReturnAddressChanged(address oldValue, address newValue);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event CrossChainVoteCollectionPeriodChanged(
    - event CrossChainVoteCollectionPeriodChanged(
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event UserMaxProposalsChanged(uint256 oldValue, uint256 newValue);
    - event UserMaxProposalsChanged(uint256 oldValue, uint256 newValue);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event CrossChainVoteCollected(
    - event CrossChainVoteCollected(
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event CalldataApprovalUpdated(bytes data, bool approved);
    - event CalldataApprovalUpdated(bytes data, bool approved);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event ProposalRebroadcasted(uint256 proposalId, bytes data);
    - event ProposalRebroadcasted(uint256 proposalId, bytes data);
  
- **src/Governance/MultichainGovernor/IMultichainGovernor.sol**
    - event NewStakedWellSet(address newStakedWell, bool toUseTimestamps);
    - event NewStakedWellSet(address newStakedWell, bool toUseTimestamps);
  
- **src/Governance/MultichainGovernor/IMultichainVoteCollection.sol**
    - event ProposalCreated(
    - event ProposalCreated(
## Votes Emitted Event
- **File:** src/Governance/MultichainGovernor/IMultichainVoteCollection.sol
- **Line:** 29
\u0060\u0060\u0060solidity
event VotesEmitted(
\u0060\u0060\u0060
## Vote Cast Event
- **File:** src/Governance/MultichainGovernor/IMultichainVoteCollection.sol
- **Line:** 41
\u0060\u0060\u0060solidity
event VoteCast(
\u0060\u0060\u0060
## New Staked Well Set Event
- **File:** src/Governance/MultichainGovernor/IMultichainVoteCollection.sol
- **Line:** 49
\u0060\u0060\u0060solidity
event NewStakedWellSet(address newStakedWell);
\u0060\u0060\u0060

### BVSS
AO:A/AC:L/AX:L/C:N/I:N/A:N/D:N/Y:N/R:P/S:C (0.0)

It is recommended to add the indexed keyword when declaring events, considering the following example:
\u0060\u0060\u0060solidity
event Indexed(
    address indexed from,
    bytes32 indexed id,
    uint indexed value
);
\u0060\u0060\u0060

ACKNOWLEDGED: The Moonwell team has acknowledged the finding.

[https://github.com/moonwell-fi/moonwell-contracts-v2/pull/147](https://github.com/moonwell-fi/moonwell-contracts-v2/pull/147)

- [Solidity Events Documentation](https://docs.soliditylang.org/en/v0.8.24/contracts.html#events)
- [Solidity ABI Specification](https://docs.soliditylang.org/en/v0.8.24/abi-spec.html#events)
PAGE END
