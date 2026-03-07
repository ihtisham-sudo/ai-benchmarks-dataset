# L-01 - Inaccurate best response selection in LLMOracleCoordinator::getBestResponse

**Severity:** medium
**Auditor:** CodeHawks
**Protocol:** Swan
**Keywords:** LLMOracleCoordinator, getBestResponse, best response, validation, taskResponses, score, default score, empty response, incorrect response, task status, validation requirements, submissions, performance quality, consequences, purchases, output, task parameter, non-zero score, fallback value, threshold

---

# Current Market Phases
Time since market set: 4  
Current phase: Buy  
Time till next: 0     // <- shouldn\u0027t reach zero  
Time since market set: 5  
Current phase: Withdraw  
Time till next: 1     // <- Withdraw phases lasts for 1 second  
Time since market set: 6  
Current phase: Sell  
Time till next: 2  

As we can see even though all phases should take the same amount of time - Sell is always extended by 1 and Withdraw phase cut short by one.

Replace comparison from "<=" to "<" in both sellInterval and buyInterval.

## 7.3 LowRiskFindings

### 7.3.1 L-01. Inaccurate best response selection in LLMOracleCoordinator::getBestResponse.
Submitted by ChainDefenders, 0xnbvc, robertodf99, v1vah0us3, m4k2xmk, alqaqa, zukanopro. Selected submission by: v1vah0us3.

The LLMOracleCoordinator::getBestResponse function may not return the best performing result of the given task. This behaviour can lead to less than optimal purchases, especially in scenarios where response validation has not taken place.

#### Description
The LLMOracleCoordinator::getBestResponse function aims to return the best-performing response based on validation scores for a given task. However, there is an issue when the task responses have no validation requirements, as it is when task.parameters.numValidations == 0 in LLMOracleCoordinator::respond. In such cases, all responses will be assigned a default score of 0 (see [https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L226]) and will not require any validation, setting the task status to Completed. This may lead to the following consequences:

** The LLMOracleCoordinator::getBestResponse function selects the first response from taskResponses array, which may not represent the best or most accurate result. In fact, it could be an empty, irrelevant or false response. Since all scores are 0, this does not indicate performance quality.

\u0060\u0060\u0060solidity
function getBestResponse(uint256 taskId) external view returns (TaskResponse memory) {
    TaskResponse[] storage taskResponses = responses[taskId];
    if (requests[taskId].status != LLMOracleTask.TaskStatus.Completed) {
        revert InvalidTaskStatus(taskId, requests[taskId].status, LLMOracleTask.TaskStatus.Completed);
    }
    TaskResponse storage result = taskResponses[0];
    uint256 highestScore = result.score;
    for (uint256 i = 1; i < taskResponses.length; i++) {
        if (taskResponses[i].score > highestScore) {
            highestScore = taskResponses[i].score;
            result = taskResponses[i];
        }
    }
    return result;
}
\u0060\u0060\u0060
When the task parameter \u0060numValidations\u0060 is set to 0, the system lacks a mechanism to validate responses effectively. Consequently, even incorrect or irrelevant responses can be treated as acceptable output and returned as the best result after calling \u0060LLMOracleCoordinator::getBestResponse\u0060.

For the proof of concept here is a valid test case, please paste it into the \u0060LLMOracleCoordinator.test.ts\u0060 file:

\u0060\u0060\u0060javascript
describe("without validation", function () {
  const [numGenerations, numValidations] = [2, 0];
  let generatorAllowancesBefore;
  this.beforeAll(async () => {
    taskId++;
    generatorAllowancesBefore = await Promise.all(
      generators.map((g) => token.allowance(coordinatorAddress, g.address))
    );
  });
  it("should make a request", async function () {
    await safeRequest(coordinator, token, requester, taskId, input, models, {
      difficulty,
      numGenerations,
      numValidations,
    });
  });
  it("should NOT respond if not a registered Oracle", async function () {
    const generator = dummy;
    await expect(safeRespond(coordinator, generator, output, metadata, taskId, 0n))
      .to.revertedWithCustomError(coordinator, "NotRegistered")
      .withArgs(generator.address);
  });
  it("should respond (1/2) to a request only once", async function () {
    // using the first generator
    const generator = generators[0];
    await safeRespond(coordinator, generator, output, metadata, taskId, 0n);
    // should NOT respond again
    await expect(safeRespond(coordinator, generator, output, metadata, taskId, 0n))
      .to.be.revertedWithCustomError(coordinator, "AlreadyResponded")
      .withArgs(taskId, generator.address);
  });
  it("should respond (2/2)", async function () {
    // use the second generator
    const generator = generators[1];
    await safeRespond(coordinator, generator, output, metadata, taskId, 1n);
  });
  it("should NOT respond if task is not pending generation", async function () {
    // this time we use the other generator
    const generator = generators[2];
    await expect(safeRespond(coordinator, generator, output, metadata, taskId, 2n))
      .to.revertedWithCustomError(coordinator, "InvalidTaskStatus")
      .withArgs(taskId, TaskStatus.Completed, TaskStatus.PendingGeneration);
  });
  it("should NOT respond to a non-existent request", async function () {
\u0060\u0060\u0060
## Invalid Task Status Handling

\u0060\u0060\u0060javascript
const generator = generators[0];
const nonExistentTaskId = 999n;
await expect(safeRespond(coordinator, generator, output, metadata, nonExistentTaskId, 0n))
  .to.revertedWithCustomError(coordinator, "InvalidTaskStatus")
  .withArgs(nonExistentTaskId, TaskStatus.None, TaskStatus.PendingGeneration);
\u0060\u0060\u0060
## Best Response Selection Without Validation

\u0060\u0060\u0060javascript
it("should return the first response as the \u0027best\u0027 when no validations are present", async function () {
  const task = await coordinator.requests(taskId);
  console.log(\u0060Task Status: ${task.status}\u0060);
  expect(task.status).to.equal(TaskStatus.Completed);
  const responses = await coordinator.getResponses(taskId);
  console.log("Generator responses:");
  responses.forEach((response: any, index: number) => {
    console.log(\u0060    Generator ${index} Address: ${response.responder}, Score: ${response.score}\u0060);
  });
  const bestResponse = await coordinator.getBestResponse(taskId);
  console.log(\u0060Best Response - Responder: ${bestResponse.responder}, Score: ${bestResponse.score}\u0060);
  expect(bestResponse.responder).to.equal(generators[0].address);
  expect(bestResponse.score).to.equal(0);
});
\u0060\u0060\u0060
## Reward Calculation Verification

\u0060\u0060\u0060javascript
it("should see rewards", async function () {
  const task = await coordinator.requests(taskId);
  for (let i = 0; i < numGenerations; i++) {
    const allowance = await token.allowance(coordinatorAddress, generators[i].address);
    expect(allowance - generatorAllowancesBefore[i]).to.equal(task.generatorFee);
  }
});
\u0060\u0060\u0060

## Logs

The test can be run with:

\u0060\u0060\u0060bash
yarn test ./test/LLMOracleCoordinator.test.ts --verbose
\u0060\u0060\u0060

### Output Logs

\u0060\u0060\u0060
Task Status: 3
Generator responses:
  Generator 0 Address: 0x90F79bf6EB2c4f870365E785982E1f101E93b906, Score: 0
  Generator 1 Address: 0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65, Score: 0
Best Response - Responder: 0x90F79bf6EB2c4f870365E785982E1f101E93b906, Score: 0
\u0060\u0060\u0060

As you can see from the error logs, if oracle response validation is not required, all generated responses get the default score of 0 and the LLMOracleCoordinator::getBestResponse function returns the very first result pushed into the TaskResponse array of structs.

A core BuyerAgent::purchase function relies on the results of the LLMOracleCoordinator::getBestResponse function, which may not reflect the response quality or relevance, resulting in purchases based on inaccurate information. If users consistently receive from oracles poor answers that are labelled as the best, this would lead to financial losses as users would not purchase the best items, resulting in frustration and reduced confidence in the system\u0027s capabilities.

- Manual Code Review
- Hardhat
Consider introducing a threshold for the number of validations required before considering any response valid. It can be set in LLMOracleManager.sol. This ensures that responses are subjected to some level of scrutiny before being considered for the best-performing result. Revise the logic in the getBestResponse function to ensure that it only selects responses with non-zero scores. If all responses have a score of 0, the function should revert with a clear message indicating that no valid responses were found, or return a designated fallback value that signifies the absence of a suitable response.
## L-02. Sequential Fee Calculations Lead to Lost Platform Revenue Due to Precision Loss
Submitted by professoraudit, ChainDefenders, 0xnbvc, skid0016, zxriptor, n3smaro, bbash, zealousdream572, mgf15, fourb, 0xlookman. Selected submission by: skid0016.

### Description: Here
The transferRoyalties function calculates fees using sequential percentage calculations with integer division. This approach leads to precision loss as each division operation rounds down, particularly affecting small transactions or those with low percentage fees.

\u0060\u0060\u0060solidity
function transferRoyalties(AssetListing storage asset) internal {
    // calculate fees
    uint256 buyerFee = (asset.price * asset.royaltyFee) / 100;
    uint256 driaFee = (buyerFee * getCurrentMarketParameters().platformFee) / 100; // Platform fee can
    // round to 0
}
\u0060\u0060\u0060

### Impact:
* Platform loses revenue when driaFee calculations round to zero
* Affects all transactions where (buyerFee * platformFee) < 100
* Cumulative loss of revenue over many small transactions
* Inconsistent fee application based on transaction size

### Proof of Concept:
\u0060\u0060\u0060solidity
// Test Case 1: Small Transaction - Platform Gets Nothing
asset.price = 100
asset.royaltyFee = 3    // 3%
platformFee = 5         // 5%
buyerFee = (100 * 3) / 100 = 3
driaFee = (3 * 5) / 100 = 0     // Rounds to 0, platform gets nothing

// Test Case 2: Larger Transaction - Platform Gets Fee
asset.price = 1000
asset.royaltyFee = 3    // 3%
platformFee = 5         // 5%
buyerFee = (1000 * 3) / 100 = 30
driaFee = (30 * 5) / 100 = 1     // Platform receives fee
\u0060\u0060\u0060

### Recommended Mitigation:
1. Combine calculations to minimize precision loss:
\u0060\u0060\u0060solidity
function transferRoyalties(AssetListing storage asset) internal {
    // Calculate platform fee first to avoid rounding issues
    uint256 driaFee = (asset.price * asset.royaltyFee * getCurrentMarketParameters().platformFee) / 10000;
    uint256 buyerFee = (asset.price * asset.royaltyFee) / 100 - driaFee;
}
\u0060\u0060\u0060
## Transfer fees
\u0060\u0060\u0060solidity
token.transferFrom(asset.seller, address(this), buyerFee + driaFee);
token.transfer(asset.buyer, buyerFee);
token.transfer(owner(), driaFee);
\u0060\u0060\u0060

## Consider using basis points (10000) instead of percentages for more precise calculations:
\u0060\u0060\u0060solidity
// Constants
uint256 constant BASIS_POINTS = 10000;
// Calculations using basis points
uint256 driaFee = (asset.price * asset.royaltyFee * platformFee) / (BASIS_POINTS * BASIS_POINTS);
\u0060\u0060\u0060
## L-03. Consensus Mechanism Allows Participation Of Voters With Insufficient Stake
Submitted by auditweiler, ChainDefenders, ooooouuuuuueeeeee. Selected submission by: auditweiler.

It is possible to participate in voting with insufficient stake.

To participate in consensus, an account must be registered:
\u0060\u0060\u0060solidity
/// @notice Reverts if \u0060msg.sender\u0060 is not a registered oracle.
modifier onlyRegistered(LLMOracleKind kind) {
    if (!registry.isRegistered(msg.sender, kind)) { /// @audit must be registered
        revert NotRegistered(msg.sender);
    }
    _;
}
\u0060\u0060\u0060
[Link to code](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/c8686b199daadcef3161980022e12b66a5304f8e/contracts/llm/LLMOracleCoordinator.sol#L80C5-L86C6)

Digging into the implementation of isRegistered, we find:
\u0060\u0060\u0060solidity
/// @notice Check if an Oracle is registered.
function isRegistered(address user, LLMOracleKind kind) public view returns (bool) {
    return registrations[user][kind] != 0; /// @audit must have non-zero stake
}
\u0060\u0060\u0060
[Link to code](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/c8686b199daadcef3161980022e12b66a5304f8e/contracts/llm/LLMOracleRegistry.sol#L145C5-L148C6)

This means, regardless of how much stake is deposited (even if it were just 1 wei), they would be considered a valid participant in consensus.

This mechanism relies upon the assumption that users can only register with valid minimum stakes, since the minimum stake amounts are enforced upon registration:
\u0060\u0060\u0060solidity
/// @notice Register an Oracle.
/// @dev Reverts if the user is already registered or has insufficient funds.
/// @param kind The kind of Oracle to unregister.
function register(LLMOracleKind kind) public {
    uint256 amount = getStakeAmount(kind); /// @audit determines the correct stake
    // ensure the user is not already registered
    if (isRegistered(msg.sender, kind)) {
\u0060\u0060\u0060
## Vulnerability Overview

\u0060\u0060\u0060solidity
revert AlreadyRegistered(msg.sender);
}
// ensure the user has enough allowance to stake
if (token.allowance(msg.sender, address(this)) < amount) {
     revert InsufficientFunds();
}
token.transferFrom(msg.sender, address(this), amount);
// register the user
registrations[msg.sender][kind] = amount; /// @audit ensures a valid minimum stake
emit Registered(msg.sender);
\u0060\u0060\u0060
[Source Code](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/c8686b199daadcef3161980022e12b66a5304f8e/contracts/llm/LLMOracleRegistry.sol#L91C5-L111C6)

However, after registering for the protocol, the protocol owner may choose to increase the minimum stake for the role:

\u0060\u0060\u0060solidity
/// @notice Set the stake amount required to register as an Oracle.
/// @dev Only allowed by the owner.
function setStakeAmounts(uint256 _generatorStakeAmount, uint256 _validatorStakeAmount) public onlyOwner
{
    generatorStakeAmount = _generatorStakeAmount; /// @audit alter minimum stake
    validatorStakeAmount = _validatorStakeAmount; /// @audit alter minimum stake
}
\u0060\u0060\u0060
[Source Code](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/c8686b199daadcef3161980022e12b66a5304f8e/contracts/llm/LLMOracleRegistry.sol#L133C5-L138C6)

This means that if the stake amounts were to be increased, those with inefficient stakes still continue to be recognized as valid stakers, even though they have made an insufficient economic sacrifice.

Users with insufficient stake are permitted to participate in voting if they had registered prior to an increase in the minimum stake amount.

Manual Review

Enforce the minimum stake for the role:

\u0060\u0060\u0060solidity
/// @notice Check if an Oracle is registered.
function isRegistered(address user, LLMOracleKind kind) public view returns (bool) {
    return registrations[user][kind] != 0;
    return registrations[user][kind] >= getStakeAmount(kind);
}
\u0060\u0060\u0060
**Submitted by:** tigerfrake.

During initialization, the Swan contract assigns both the owner and operator roles to the caller. However, transferring ownership via the \u0060transferOwnership()\u0060 function only updates the contract owner address, leaving the previous owner’s operator privileges intact. The new owner on the other hand therefore is denied this status when in reality he is the acting contract owner.

During the contract’s initialization in Swan contract, the caller is assigned both the owner and operator roles.

\u0060\u0060\u0060solidity
function initialize(
      ---SNIP---
) public initializer {
    __Ownable_init(msg.sender);
    ---SNIP---
    // owner is an operator
    isOperator[msg.sender] = true;
}
\u0060\u0060\u0060

This allows them to execute functions gated by the \u0060onlyAuthorized()\u0060 modifier, which requires the caller to be either the BuyerAgent owner or an operator.

\u0060\u0060\u0060solidity
modifier onlyAuthorized() {
    // if its not an operator, and is not an owner, it is unauthorized
    if (!swan.isOperator(msg.sender) && msg.sender != owner()) {
        revert Unauthorized(msg.sender);
    }
    _;
}
\u0060\u0060\u0060

However, when Swan contract ownership is transferred using the inherited \u0060transferOwnership()\u0060 function from \u0060OwnableUpgradeable\u0060, the operator status will not be revoked from the original contract owner and neither will it be granted to the new owner.

\u0060\u0060\u0060solidity
function transferOwnership(address newOwner) public virtual onlyOwner {
    if (newOwner == address(0)) {
        revert OwnableInvalidOwner(address(0));
    }
    _transferOwnership(newOwner);
}
\u0060\u0060\u0060

This creates a situation where the previous Swan contract owner retains operator access even after ownership is transferred, potentially leading to unauthorized access if that previous owner acts on the retained privileges.
## Clarification:
There are two owners I am referring to here:
1. The Swan owner (Trusted) - This is the wallet that deploys Swan by default (The one given operator status)
2. BuyerAgent Owner: A user that created a buyer agent with \u0060createBuyer()\u0060 function in Swan

Now according to Contest Details (Actors), Swan Owner is trusted. However, once he transfers this ownership to a new entity, he is no longer the owner and as such, should not act on previous privileges.

This oversight could allow a former owner to interact with functions restricted to BuyerAgent owner or designated operators. Since the \u0060onlyAuthorized()\u0060 modifier allows access to both operators and the BuyerAgent.
## Insufficient Operator Privileges

**Owner:** A previous contract owner retaining operator privileges could invoke critical functions, potentially disrupting expected contract functionality or enabling unintended actions.

- Manual Review

Override the \u0060transferOwnership()\u0060 function to correctly revoke operator status from the previous owner and assign it to the new owner. This ensures that the privileges managed by the \u0060onlyAuthorized()\u0060 modifier are aligned with the current Swan contract ownership.

\u0060\u0060\u0060solidity
function transferOwnership(address newOwner) public override onlyOwner {
    if (newOwner == address(0)) {
        revert OwnableInvalidOwner(address(0));
    }
    // @audit Revoke operator status from the current owner
    isOperator[msg.sender] = false;
    // Transfer ownership using the parent contract\u0027s functionality
    _transferOwnership(newOwner);
    // @audit Assign operator status to the new owner
    isOperator[newOwner] = true;
}
\u0060\u0060\u0060
## L-05. Insufficient Validation of Token Name and Symbol in list function

**Submitted by:** golomp3761.

The Name and Symbol variables in the list function are unfiltered, allowing for malicious code injection. Without character limits, this vulnerability can lead to XSS or HTML injection attacks, enabling attackers to manipulate information in the Web3 application.

The Name and Symbol variables in the list function are not filtered in any way, allowing an attacker to create a token with malicious JavaScript or HTML code injected into these fields. These fields are also not limited by character count, enabling the injection of a large amount of code. If no mitigation mechanisms are implemented in the web application for malicious code from these variables, the application will be vulnerable to XSS or HTML injection attacks if the values of these variables are displayed in the web application.

[Link to Code](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/swan/Swan.sol#L173)

If an attacker creates an asset with a symbol containing the malicious JavaScript payload, he could get a stored XSS on this website that renders his malicious NFT name and symbol, which is legitimately generated by this dapp. According to correspondence with the sponsor, there is a possibility of transferring the created NFT to other applications like NFT exchanges, which creates an additional XSS risk on the mentioned dApps. This could allow the attacker, for example, to run a keylogger script to collect all inputs typed by a user including his password or to create a fake Metamask pop-up asking a user to sign a malicious transaction.

- Manual review.

By using the written test file, I was able to modify this line of code [Link to Test Code](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/c8686b199daadcef3161980022e12b66a5304f8e/test/Swan.test.ts#L64) in the following way, and the test was successful.
It\u0027s absolutely necessary to sanitize the user\u0027s input on the list function. The asset symbol should only contain Aa-Zz and 0-9 characters while forbidding special ones, i.e. < / >. The length of possible characters should also be significantly limited. The principle of security in depth should be applied, securing each possible injection point in the best possible way.
## L-06. Lack of output validation in LLMOracleCoordinator::respond allows empty responses and potential fee exploitation by oracles.
Submitted by danzero, 0xrolko, 0xhacksmithh, v1vah0us3, goran, johny7173, tihomirchobanov. Selected submission by: v1vah0us3.

The LLMOracleCoordinator::respond function does not validate the contents of the output parameter, allowing registered generators to submit empty responses. This lack of validation can result in incomplete or unusable outputs stored in the TaskResponse array of structs. If numValidations is set to 0, meaning no validation phase occurs, the response generator receives the generatorFee without any content checks, leading to potential exploitation of the fee system.

In the respond function, generators submit responses containing output data. However, there is no mechanism to ensure that the output is not empty, even though natspec requires it: @dev output must not be empty. As such, it is possible for a registered generator to submit broken or empty outputs. The lack of output validation is further compounded when task.parameters.numValidations is set to 0, meaning no validation phase occurs. Under this condition:
1. There are no checks to ensure that the output is non-empty or meets minimal quality criteria.
2. When task.parameters.numValidations == 0, the task’s status is set to Completed immediately, bypassing the validation phase. This results in direct rewards for generators without any verification of the output’s quality or relevance.
3. If the generatorFee is substantial, this design could be exploited by malicious actors who submit arbitrary or empty outputs to repeatedly collect fees without providing meaningful contributions. While the assertValidNonce function’s Proof-of-Work mechanism requires computational effort from oracles, it does not ensure that the content is correct or complete, leaving some potential for abuse by dishonest oracles.

On the other hand, if numValidations > 0, only those respondents whose answers achieve an "above-average" score will receive a fee, see [https://github.com/madeupnamefinance/2024-10-swandria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L368-L369].

Here is a valid test case that serves as a proof of concept, please paste it into the LLMOracleCoordinator.test.ts file:
\u0060\u0060\u0060javascript
const [NAME, SYMBOL] = ["<script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script><script>alert(\u00271\u0027)</script>"];
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
describe("Zero Response", function () {
  const [numGenerations, numValidations] = [2, 0];
  let generatorAllowancesBefore;
  this.beforeAll(async () => {
    taskId++;
    generatorAllowancesBefore = await Promise.all(
      generators.slice(0, 2).map((g) => token.allowance(coordinatorAddress, g.address))
    );
  });
  it("should allow both generators to respond with an empty output and receive their respective fees", async function () {
    const input = "0x" + Buffer.from("What is 2 + 2?").toString("hex"); // Valid input for a new task
    const emptyOutput = "0x"; // empty output
    const emptyMetadata = "0x"; // empty metadata
    await safeRequest(coordinator, token, requester, taskId, input, models, {
      difficulty,
      numGenerations,
      numValidations,
    });
    const allowancesBefore = await Promise.all(
      generators.slice(0, 2).map((g) => token.allowance(coordinatorAddress, g.address))
    );
    await safeRespond(coordinator, generators[0], emptyOutput, emptyMetadata, taskId, 0n);
    await safeRespond(coordinator, generators[1], emptyOutput, emptyMetadata, taskId, 1n);
    const responses = await coordinator.getResponses(taskId);
    console.log("Generator oracle responses after empty output submissions with no validation required:");
    responses.forEach((response, index) => {
      console.log(\u0060   Generator ${index + 1} Address: ${response.responder}, Score: ${response.score}, Output: ${response.output}\u0060);
    });
    // Check that both responses are empty outputs
    responses.forEach((response) => {
      expect(response.output).to.equal(emptyOutput);
    });
    // Capture allowances after responses and calculate fees received
    const allowancesAfter = await Promise.all(
      generators.slice(0, 2).map((g) => token.allowance(coordinatorAddress, g.address))
    );
    // Check allowances and log fee information for each generator
    allowancesAfter.forEach((allowanceAfter, i) => {
      const allowanceBefore = allowancesBefore[i];
      const feeReceived = allowanceAfter - allowanceBefore;
      console.log(\u0060Allowance before response for Generator ${i + 1}: ${allowanceBefore}\u0060);
      console.log(\u0060Allowance after response for Generator ${i + 1}: ${allowanceAfter}\u0060);
      console.log(\u0060Fee received by Generator ${i + 1}: ${feeReceived}\u0060);
      expect(allowanceAfter).to.be.above(allowanceBefore);
    });
  });
});
\u0060\u0060\u0060
The test can be run with \u0060yarn test ./test/LLMOracleCoordinator.test.ts\u0060. Here are the logs:

Generator oracle responses after empty output submissions with no validation required:
- Generator 1 Address: \u00600x90F79bf6EB2c4f870365E785982E1f101E93b906\u0060, Score: 0, Output: \u00600x\u0060
- Generator 2 Address: \u00600x15d34AAf54267DB7D7c367839AAf71A00a2C6A65\u0060, Score: 0, Output: \u00600x\u0060

Allowance before response for Generator 1: 0  
Allowance after response for Generator 1: 16000000000000000  
Fee received by Generator 1: 16000000000000000  
Allowance before response for Generator 2: 0  
Allowance after response for Generator 2: 16000000000000000  
Fee received by Generator 2: 16000000000000000  

As shown in the error logs, both oracle responses contain an empty output with a score of 0, which is expected since no validation was required in this case. Both generators successfully received their respective fees for responding. Note that in this scenario, the protocol accepts empty outputs as valid responses.

Without required response validations, generators can earn fees for responses that may be empty or irrelevant. This can lead to potential fee drift and higher costs for users without providing meaningful value in return.

- Manual Code Review
- Hardhat

In \u0060LLMOracleCoordinator::respond\u0060, consider implementing checks to at least ensure that the output field is not empty and meets minimum length criteria.

\u0060\u0060\u0060solidity
// Define the minimum required length for output in LLMOracleCoordinator.sol
uint256 public constant MIN_OUTPUT_LENGTH = 16;

function respond(uint256 taskId, uint256 nonce, bytes calldata output, bytes calldata metadata)
    public
    onlyRegistered(LLMOracleKind.Generator)
    onlyAtStatus(taskId, TaskStatus.PendingGeneration)
{
    TaskRequest storage task = requests[taskId];
    // Check that the output is not empty and meets minimal length requirement
    require(output.length >= MIN_OUTPUT_LENGTH, "InvalidOutput: Empty or too short");
    .............
    .............
}
\u0060\u0060\u0060

If possible, introduce a minimum validation requirement in \u0060LLMOracleManager.sol\u0060, such as \u0060task.parameters.numValidations == 1\u0060, to ensure that tasks undergo some scrutiny before reaching the Completed status, and before any generator fees are distributed.
Submitted by bareli, 0xvd, m4k2xmk. Selected submission by: 0xvd.

The getBestResponse function in LLMOracleCoordinator lacks a tiebreak mechanism when multiple responses have the same highest validation score. This can lead to inconsistent results and potential manipulation of which response is selected as "best".

Current implementation simply takes the first response with the highest score:

\u0060\u0060\u0060solidity
function getBestResponse(uint256 taskId) external view returns (TaskResponse memory) {
    TaskResponse[] storage taskResponses = responses[taskId];
    // ensure that task is completed
    if (requests[taskId].status != LLMOracleTask.TaskStatus.Completed) {
        revert InvalidTaskStatus(taskId, requests[taskId].status, LLMOracleTask.TaskStatus.Completed);
    }
    // pick the result with the highest validation score
    TaskResponse storage result = taskResponses[0];
    uint256 highestScore = result.score;
    for (uint256 i = 1; i < taskResponses.length; i++) {
        if (taskResponses[i].score > highestScore) {     // Note: only strictly greater than
            highestScore = taskResponses[i].score;
            result = taskResponses[i];
        }
    }
    return result;
}
\u0060\u0060\u0060
## Issues:
- No tiebreaker for equal scores
- First response has advantage in ties
- Order-dependent results

- Early responders have advantage in ties
- Inconsistent selection among equally-scored responses

- Manual Review

Implement deterministic tiebreak using multiple factors:

\u0060\u0060\u0060solidity
function getBestResponse(uint256 taskId) external view returns (TaskResponse memory) {
    TaskResponse[] storage taskResponses = responses[taskId];
    require(requests[taskId].status == LLMOracleTask.TaskStatus.Completed, "Task not completed");
    TaskResponse storage bestResponse = taskResponses[0];
    uint256 bestScore = bestResponse.score;
    bytes32 bestHash = keccak256(abi.encodePacked(
        bestResponse.output,
        bestResponse.responder,
\u0060\u0060\u0060
In \u0060LLMOracleCoordinator::request\u0060, there is no check to ensure \u0060task.input\u0060 is non-empty. This allows users to leave \u0060task.input\u0060 empty, making it easier to pass the \u0060assertValidNonce\u0060 function.
## Submitted by
nitinaimshigh, n3smaro, saurabh_singh, invcbull, 0xhacksmithh, johny7173. Selected submission by: saurabh_singh.

As given in the NatSpec, the Input should be non-empty. In the \u0060LLMOracleCoordinator::request\u0060 function, any requester can leave \u0060task.value\u0060 empty, which makes passing \u0060assertValidNonce\u0060 easier. Since \u0060task.value\u0060 is part of the message composition, an empty value reduces its uniqueness, lowering the nonce validation difficulty.

### Code Snippet
\u0060\u0060\u0060solidity
function assertValidNonce(uint256 taskId, TaskRequest storage task, uint256 nonce) internal view {
    bytes memory message = abi.encodePacked(taskId, task.input, task.requester, msg.sender, nonce);
    if (uint256(keccak256(message)) > type(uint256).max >> uint256(task.parameters.difficulty)) {
        revert InvalidNonce(taskId, nonce);
    }
}
\u0060\u0060\u0060
