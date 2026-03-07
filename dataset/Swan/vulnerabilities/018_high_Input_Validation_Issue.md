# Input Validation Issue

**Severity:** high
**Auditor:** CodeHawks
**Protocol:** Swan
**Keywords:** input validation, nonce integrity, security, exploitation, hash uniqueness, empty input, malicious user, request uniqueness, task input, requirement, contract allowance, fee token, task parameters, insufficient fees, task request, emit event, requester, protocol, task id, LLM generation

---

# Input Validation Issue
- **Severity**: High
- A malicious user who realizes they can leave \u0060task.input\u0060 empty could exploit this to pass the \u0060assertValidNonce\u0060.
The current implementation allows users to bypass validation with minimal effort, undermining nonce integrity. The absence of \u0060task.input\u0060 in the message hash reduces the uniqueness of each request, lowering the computational effort needed to find a valid nonce and weakening the intended security. Since the message in \u0060assertValidNonce\u0060 relies on \u0060task.input\u0060 for uniqueness, an empty \u0060task.input\u0060 simplifies the hash and reduces the difficulty of the nonce check. Adding a requirement for a non-empty \u0060task.input\u0060 would help ensure the expected security level of the validation.

- Manual Review

\u0060\u0060\u0060solidity
/// @notice Request LLM generation.
@>  /// @dev Input must be non-empty.
/// @dev Reverts if contract has not enough allowance for the fee.
/// @dev Reverts if difficulty is out of range.
/// @param protocol The protocol string, should be a short 32-byte string (e.g., "dria/1.0.0").
/// @param input The input data for the LLM generation.
/// @param parameters The task parameters
/// @return task id
function request(
     bytes32 protocol,
     bytes memory input,
     bytes memory models,
     LLMOracleTaskParameters calldata parameters
) public onlyValidParameters(parameters) returns (uint256) {
     (uint256 totalfee, uint256 generatorFee, uint256 validatorFee) = getFee(parameters);
     // ensure the input parameter is not empty.
     require(input.length != 0, "invalid input");
     // check allowance requirements
     uint256 allowance = feeToken.allowance(msg.sender, address(this));
     if (allowance < totalfee) {
          revert InsufficientFees(allowance, totalfee);
     }
     // ensure there is enough balance
     uint256 balance = feeToken.balanceOf(msg.sender);
     if (balance < totalfee) {
          revert InsufficientFees(balance, totalfee);
     }
     // transfer tokens
     feeToken.transferFrom(msg.sender, address(this), totalfee);
     // increment the task id for later tasks & emit task request event
     uint256 taskId = nextTaskId;
     unchecked {
          ++nextTaskId;
     }
     emit Request(taskId, msg.sender, protocol);
     // push request & emit status update for the task
     requests[taskId] = TaskRequest({
          requester: msg.sender,
          protocol: protocol,
\u0060\u0060\u0060
