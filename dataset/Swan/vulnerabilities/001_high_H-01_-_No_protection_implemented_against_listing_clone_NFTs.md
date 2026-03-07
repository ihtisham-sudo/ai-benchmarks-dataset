# H-01 - No protection implemented against listing clone NFTs

**Severity:** high
**Auditor:** CodeHawks
**Protocol:** Swan
**Keywords:** NFT, listing, clone, malicious, price, race, bottom, seller, buyer, parameters, deploy, function, asset, royalty, fee, status, market, protocol, validation, agent

---

# 7.1.1 H-01. No protection implemented against listing clone NFTs
Submitted by foxb868, ljj, ChainDefenders, n3smaro. Selected submission by: ljj.

Any malicious seller can copy the name, symbol and description of any previously listed asset and list it at a 1 wei lower price. In the case of this NFT being selected to be purchased by the system, this malicious seller will guarantee that their asset with lower price would be selected. This will lead to user\u0027s copying previously listed NFT\u0027s and listing it at a lower price, in a way creating a price race to the bottom.

Anyseller can list an NFT with the list function.
\u0060\u0060\u0060solidity
function list(string calldata _name, string calldata _symbol, bytes calldata _desc, uint256 _price,
    address _buyer) external {
    BuyerAgent buyer = BuyerAgent(_buyer);
    (uint256 round, BuyerAgent.Phase phase,) = buyer.getRoundPhase();
    // buyer must be in the sell phase
    if (phase != BuyerAgent.Phase.Sell) {
        revert BuyerAgent.InvalidPhase(phase, BuyerAgent.Phase.Sell);
    }
    // asset count must not exceed \u0060maxAssetCount\u0060
    if (getCurrentMarketParameters().maxAssetCount == assetsPerBuyerRound[_buyer][round].length) {
        revert AssetLimitExceeded(getCurrentMarketParameters().maxAssetCount);
    }
    // all is well, create the asset & its listing
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
    // add this to list of listings for the buyer for this round
    assetsPerBuyerRound[_buyer][round].push(asset);
    // transfer royalties
    transferRoyalties(listings[asset]);
    emit AssetListed(msg.sender, asset, _price);
}
\u0060\u0060\u0060
As observed, this function take the _name, _symbol, _desc and _price parameters. Function then deploys a new NFT with these parameters and mints 1 NFT to the msg.sender.
\u0060\u0060\u0060solidity
contract SwanAssetFactory {
    /// @notice Deploys a new SwanAsset token.
    function deploy(string memory _name, string memory _symbol, bytes memory _description, address _owner)
\u0060\u0060\u0060
As observed, there are no checks for "clone" inputs. Meaning that any malicious seller can copy the parameters of any previously listed NFT and list it at a 1 wei lower price. In case of an NFT with these parameters being selected, the malicious user would guarantee their NFT at lower price would be selected, putting no work in creating an original NFT and simply copying previously deployed NFTs. This will create a price race to the bottom among users where users would list the NFT with same parameters, each one putting it at 1 wei lower price, breaking the protocol\u0027s intended use. The AI agents seeing all or most of the NFTs listed having the same properties would choose to purchase the NFT with these properties at the lowest price.

- **Impact:** High, this vulnerability will break the intended use of the protocol. It will create a price race to the bottom where users list the NFT with the same name, symbol, and description, each user listing it at 1 wei lower price to ensure their NFT would be chosen by the system.
- **Likelihood:** Low, There are no guarantees that this NFT would be chosen by the system but noticing copies of the same NFTs can manipulate the LLM into thinking this is a good purchase.

- Manual review

Implement a for loop in the list function that will check the NFT that is being listed against the already listed NFTs. An example for loop is shown below. Keep in mind that this implementation might cost a lot of gas if there are too many listed NFTs.

\u0060\u0060\u0060solidity
address[] memory assets = assetsPerBuyerRound[buyer][round];
for (uint256 i = 0; i < assets.length; i++) {
    IERC721 asset = IERC721(assets[i]);
}
\u0060\u0060\u0060
## H-02. Subtraction in variance() will revert due to underflow
Submitted by volodya, johnkurus, Sickurity, newspacexyz, aksoy, tigerfrake, professoraudit, n1punp, moham-
madx2049, 0xbeastboy, auditism, greese, matejdb, ChainDefenders, bareli, danzero, ericselvig, tmotfl, shui,
oluwaseyisekoni, elser17, galturok, jiri123, 0xgondar, acai, x0t0wt1w, pyro, anonymousjoe, zraxx, dimulski, 0xvd,
0xrs, kirobrejka, neilalois, goran, zxriptor, merlin, 0xbug, tejaswarambhe, yaioxy, chaossr, silver_eth, 0xhals, ty-
chaios, drynooo, kunhah, chasingbugs, bydlife, v1vah0us3, carrotsmuggler, saurabh_singh, dianivanov, 0xlouist-
sai, vasquez, emmanuel, 0x11singh99, z3r0, j1v9, 0xpinky, 0xlookman, m4k2xmk, alqaqa, inh3l, mikb. Selected
submission by: kunhah.

The function variance() in Statistics.sol subtracts the average from each number in the array but the type is uint,
because of that the function will revert unless all numbers are the same.

The function variance() does a subtraction by iterating on every number on the array and subtracting by the
average that was previously calculated.

\u0060\u0060\u0060solidity
function variance(uint256[] memory data) internal pure returns (uint256 ans, uint256 mean) {
    mean = avg(data);
    uint256 sum = 0;
    for (uint256 i = 0; i < data.length; i++) {
        uint256 diff = data[i] - mean;
        sum += diff * diff;
    }
    ans = sum / data.length;
}
\u0060\u0060\u0060

The problem is that uint does not support negative values, because of that all subtractions that result in a negative
amount will revert, and since it is the average of the numbers in the array, it will revert if the average is bigger than
one of the numbers of the array, because of that, the only case it will not revert is if all numbers in the array are
equal, and that is unlikely to happen.

This function is called in the finalizeValidation() function, which is called in the end of the validate() function,
because of that, almost all calls to validate() will revert, for this reason I believe it is a high.

Install foundry, create a file in a subfolder in the test folder, and paste this:

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;
import { Test } from "../../lib/forge-std/src/Test.sol";
import { console } from "../../lib/forge-std/src/console.sol";
contract Statistics {
\u0060\u0060\u0060
## Code Snippet

\u0060\u0060\u0060solidity
function avg(uint256[] memory data) internal pure returns (uint256 ans) {
    uint256 sum = 0;
    for (uint256 i = 0; i < data.length; i++) {
        sum += data[i];
    }
    ans = sum / data.length;
}

function variance(uint256[] memory data) internal pure returns (uint256 ans, uint256 mean) {
    mean = avg(data);
    uint256 sum = 0;
    for (uint256 i = 0; i < data.length; i++) {
        uint256 diff = data[i] - mean;
        sum += diff * diff;
    }
    ans = sum / data.length;
}

function stddev(uint256[] memory data) internal pure returns (uint256 ans, uint256 mean) {
    (uint256 _variance, uint256 _mean) = variance(data);
    mean = _mean;
    ans = sqrt(_variance);
}

function sqrt(uint256 x) internal pure returns (uint256 y) {
    uint256 z = (x + 1) / 2;
    y = x;
    while (z < y) {
        y = z;
        z = (x / z + z) / 2;
    }
}

contract TestLib is Test, Statistics {
    function test_testAvg(uint256 number1, uint256 number2, uint256 number3, uint256 number4, uint256 number5) public {
        uint256[] memory data = new uint256[]();
        data[0] = number1 % 1e50;
        data[1] = number2 % 1e50;
        data[2] = number3 % 1e50;
        data[3] = number4 % 1e50;
        data[4] = number5 % 1e50;
        require(number1 != number2, "test_testAvg: numbers must be different");
        uint256 ans = avg(data);
        //console.log(ans);
    }
    
    function test_testStddev(uint256 number1, uint256 number2, uint256 number3, uint256 number4, uint256 number5) public {
        uint256[] memory data = new uint256[]();
        data[0] = number1 % 1e50;
        data[1] = number2 % 1e50;
        data[2] = number3 % 1e50;
        data[3] = number4 % 1e50;
        data[4] = number5 % 1e50;
        require(number1 != number2, "test_testStddev: numbers must be different");
        vm.expectRevert();
        (uint256 ans, uint256 mean) = stddev(data);
    }
}
\u0060\u0060\u0060
## Code Example

\u0060\u0060\u0060solidity
function test_testSqrt() public {
    uint256 x = 16;
    uint256 ans = sqrt(x);
    //console.log(ans);
}

function test_testVariance(uint256 number1, uint256 number2, uint256 number3, uint256 number4,
                            uint256 number5) public {
    uint256[] memory data = new uint256[]();
    data[0] = number1 % 1e50;
    data[1] = number2 % 1e50;
    data[2] = number3 % 1e50;
    data[3] = number4 % 1e50;
    data[4] = number5 % 1e50;
    require(number1 != number2, "test_testVariance: numbers must be different");
    vm.expectRevert();
    (uint256 ans, uint256 mean) = variance(data);
}
\u0060\u0060\u0060

All calls to stddev() and variance() will revert as expected. The 1e50 limit is to avoid overflows that will fail the test.

- Foundry

Cast to int256 when calculating, the multiplication by itself will make the number always positive afterwards:

\u0060\u0060\u0060solidity
function variance(uint256[] memory data) internal pure returns (uint256 ans, uint256 mean) {
    mean = avg(data);
    uint256 sum = 0;
    for (uint256 i = 0; i < data.length; i++) {
        int256 diff = int256(data[i]) - int256(mean);
        sum += uint256(diff * diff);
    }
    ans = sum / data.length;
}
\u0060\u0060\u0060

### H-03. Potential underflow vulnerability in score range calculation of LLMOracleCoordinator::finalizeValidation, leading to DoS.

Submitted by: volodya, Sickurity, newspacexyz, aksoy, auditweiler, ChainDefenders, matejdb, 0xbeastboy, oluwaseyisekoni, galturok, pyro, anonymousjoe, tmotfl, 0xvd, 0xrs, elser17, neilalois, merlin, zxriptor, drynooo, v1vah0us3, goran, alqaqa, m4k2xmk, ericselvig, mikb, saurabh_singh. Selected submission by: v1vah0us3.

The LLMOracleCoordinator::finalizeValidation function calculates the range for valid scores depending on the result of the expression score >= _mean - _stddev. If _mean is less than _stddev, this calculation leads to an underflow error, causing a revert that will fail the transaction. This behavior prevents successful validation completion and rewards distribution, disrupting normal contract operations and usability.

In the LLMOracleCoordinator::finalizeValidation function, scores are evaluated within a standard deviation range around the mean, using the criteria (_mean - _stddev) and (_mean + _stddev), see [source](https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L343).
if ((score >= _mean - _stddev) && (score <= _mean + _stddev))

However, in cases where _mean < _stddev, such as some valid edge case where for example scores[] =
[0,1,0,1,2], the calculation of _mean - _stddev attempts to produce a negative value. Since Solidity’s uint256 type does not support negative numbers, this results in an underflow, triggering an automatic revert and causing the transaction to fail. The edge case described results in _stddev = 1 and _mean = 0, which causes the check score >= _mean - _stddev to revert, as _mean - _stddev evaluates to a negative result. The same issue exists also in [https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L368]:
## Exploit Scenario

For the input scores[] = [0, 1, 0, 1, 2], the standard deviation and mean calculated by Statistics.stddev(scores) in LLMOracleCoordinator::finalizeValidation are _stddev = 1 and _mean = 0. Note that the calculation using the Statistics.sol library would be successful in this case. That can be quickly checked in Remix:

decoded input
\u0060\u0060\u0060json
{
    "uint256[] data": [
        "0",
        "1",
        "0",
        "1",
        "2"
    ]
}
\u0060\u0060\u0060

decoded output
\u0060\u0060\u0060json
{
    "0": "uint256: ans 1",
    "1": "uint256: mean 0"
}
\u0060\u0060\u0060

When performing the range check in (score >= _mean - _stddev) (see [https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L343]), the _mean - _stddev calculation attempts to compute 0 - 1, which underflows as it is not representable within the unsigned integer type, triggering a revert. The same problem was also found at [https://github.com/madeupnamefinance/2024-10-swan-dria/blob/main/contracts/llm/LLMOracleCoordinator.sol#L368].

For the proof of concept, we will stick to the same score values as shown in the section above. Here is the test case and setup, please paste it into the LLMOracleCoordinator.test.ts file and adjust the this.beforeAll(async function ()) section with additional validators, like this:

\u0060\u0060\u0060javascript
// Add validators to the setUp
this.beforeAll(async function () {
    // assign roles, full = oracle that can do both generation & validation
    const [deployer, dum, req1, gen1, gen2, gen3, gen4, gen5, val1, val2, val3, val4, val5] = await
    ethers.getSigners();
    dria = deployer;
    requester = req1;
    dummy = dum;
    generators = [gen1, gen2, gen3, gen4, gen5];
    validators = [val1, val2, val3, val4, val5];
    ...........
    ...........
    ...........
});

describe("underflow in score range calculation", function () {
    const [numGenerations, numValidations] = [1, 5];
    const scores = [
        parseEther("0"),
        parseEther("0.000000000000000001"),
\u0060\u0060\u0060
## Underflow Test
\u0060\u0060\u0060javascript
parseEther("0"),
parseEther("0.000000000000000001"),
parseEther("0.000000000000000002")
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
// UNDERFLOW TEST
it("it should underflow calculating score ranges for inner mean", async function () {
  const requestBefore = await coordinator.requests(taskId);
  console.log(\u0060Request status before validation: ${requestBefore.status}\u0060);
  for (let i = 0; i < numValidations; i++) {
      console.log(\u0060Validating with validator at index ${i} with address: ${validators[i].address}\u0060);
      console.log(\u0060Score being used: ${scores[i].toString()}, Task ID: ${taskId}\u0060);
      try {
          if (i < numValidations - 1) {
              await safeValidate(coordinator, validators[i], [scores[i]], metadata, taskId,
               BigInt(i));
              console.log(\u0060Validation succeeded for validator at index ${i}\u0060);
          } else {
            // For the last validator, expect a revert without a specific error
            await safeValidate(coordinator, validators[i], [scores[i]], metadata, taskId,
             BigInt(i));
             console.log(\u0060Validation succeeded for validator at index ${i}\u0060); // This should not run
          }
      } catch (error:any) {
\u0060\u0060\u0060
The following code snippet demonstrates a validation process where validators check the status of a task. If a validation fails, an error message is logged indicating the index of the validator and the nature of the error.

\u0060\u0060\u0060javascript
if (i < numValidations - 1) {
    console.error(\u0060Validation failed for validator at index ${i} with error:
    ✱✦  ${error.message}\u0060);
} else {
    if (error instanceof Error) {
        console.error(\u0060Validation failed for validator at index ${i}: ${error.message}\u0060);
    } else {
        console.error(\u0060Validation failed for validator at index ${i}:
        ✱✦  ${JSON.stringify(error)}\u0060);
    }
}
\u0060\u0060\u0060

\u0060\u0060\u0060javascript
// Confirm the tasks status
const finalRequest = await coordinator.requests(taskId);
console.log(\u0060Request status after all validations: ${finalRequest.status}\u0060);
// Confirm the status is still \u0027PendingValidation\u0027
expect(finalRequest.status).to.equal(TaskStatus.PendingValidation);
\u0060\u0060\u0060

The test can be run with the following command:
\u0060\u0060\u0060
yarn test ./test/LLMOracleCoordinator.test.ts --verbose
\u0060\u0060\u0060
## Logs
\u0060\u0060\u0060
Request status before validation: 2
Validating with validator at index 0 with address: 0x23618e81E3f5cdF7f54C3d65f7FBc0aBf5B21E8f
Score being used: 0, Task ID: 3
Validation succeeded for validator at index 0
Validating with validator at index 1 with address: 0xa0Ee7A142d267C1f36714E4a8F75612F20a79720
Score being used: 1, Task ID: 3
Validation succeeded for validator at index 1
Validating with validator at index 2 with address: 0xBcd4042DE499D14e55001CcbB24a551F3b954096
Score being used: 0, Task ID: 3
Validation succeeded for validator at index 2
Validating with validator at index 3 with address: 0x71bE63f3384f5fb98995898A86B02Fb2426c5788
Score being used: 1, Task ID: 3
Validation succeeded for validator at index 3
Validating with validator at index 4 with address: 0xFABB0ac9d68B0B445fB7357272Ff202C5651694a
Score being used: 2, Task ID: 3
Validation failed for validator at index 4: VM Exception while processing transaction: reverted with
✱✦  panic code 0x11 (Arithmetic operation overflowed outside of an unchecked block)
Request status after all validations: 2
\u0060\u0060\u0060

As you can see from the error logs, the transaction failed with an error message: panic code 0x11 (Arithmetic operation overflowed outside of an unchecked block). The problem was not the use of a buggy Statistics.sol library, but the logic behind the score range calculation in \u0060LLMOracleCoordinator::finalizeValidation\u0060.

Tasks with scores causing \u0060_mean < _stddev\u0060 cannot complete, leading to a halt in the validation process and blocking reward distribution. Since scores submitted by prior validators to the TaskValidation struct array are immutable, tasks may become permanently locked in PendingValidation status, posing a potential DoS vulnerability.

- Manual Code Review
- Remix
- Hardhat
## LLMOracleCoordinator::finalizeValidation needs to be refactored

You could think about rewriting both underflow-prone conditions in finalizeValidation using only addition operations, adjusting the logic to avoid subtraction:

\u0060\u0060\u0060solidity
for (uint256 v_i = 0; v_i < task.parameters.numValidations; ++v_i) {
    uint256 score = scores[v_i];
    if ((score + _stddev >= _mean) && (score <= _mean + _stddev)) {
        innerSum += score;
        innerCount++;
        _increaseAllowance(validations[taskId][v_i].validator, task.validatorFee);
    }
}
\u0060\u0060\u0060

...

\u0060\u0060\u0060solidity
for (uint256 g_i = 0; g_i < task.parameters.numGenerations; g_i++) {
    // ignore lower outliers
    if (generationScores[g_i] + generationDeviationFactor * stddev >= mean) {
        _increaseAllowance(responses[taskId][g_i].responder, task.generatorFee);
    }
}
\u0060\u0060\u0060

After applying the suggested fixes, the issues are mitigated. Adjust the last line in the PoC to \u0060expect(finalRequest.status).to.equal(TaskStatus.Completed);\u0060 and run the test with \u0060yarn test ./test/LLMOracleCoordinator.test.ts\u0060, it will pass.
## MediumRiskFindings
## M-01. Platform fees withdrawal will sweep oracle agents earned fees

Submitted by greese, newspacexyz, Sickurity, yxsec, auditweiler, auditism, robertodf99, ChainDefenders, gurav11018, 0xnbvc, acai, n3smaro, aak, pyro, 0xvd, merlin, dimulski, cryptozaki, silver_eth, josh4324, drynooo, aestheticbhai, seclabs, goran, yotov721, ericselvig, tihomirchobanov, lazydog, johny7173, Gladiators, alqaqa, yaioxy, 0xlookman, sovaslava. Selected submission by: robertodf99.

Oracle agents earn a portion of user-paid fees if their responses fall within established accuracy boundaries, defined by a specific range of standard deviations. Rather than directly transferring these fees to the agents, LLMOracleCoordinator.sol grants them an approval to spend the fees. Additionally, there is a protocol admin function to withdraw the platform fees along with any residual fee tokens remaining in the contract. However, because oracle agents are only granted approval (not ownership) of the fees, any fees they have not yet withdrawn may be inadvertently collected by the protocol when the admin executes a platform fee withdrawal.

Oracle agents must quickly transfer their earned fees to another address before the protocol sweeps the contract\u0027s funds, potentially leaving it empty. If they fail to do so, they must wait until the contract’s balance increases to an amount they can claim before others do.

#### Severity

The issue can be tested using the following PoC in Foundry:

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.20;
import {Vm, Test} from "forge-std/Test.sol";
import {console2} from "forge-std/console2.sol";
\u0060\u0060\u0060
## Importing Contracts
\u0060\u0060\u0060solidity
import {Swan} from "../src/swan/Swan.sol";
import {BuyerAgent} from "../src/swan/BuyerAgent.sol";
import {LLMOracleCoordinator} from "../src/llm/LLMOracleCoordinator.sol";
import {LLMOracleRegistry, LLMOracleKind} from "../src/llm/LLMOracleRegistry.sol";
import {MockToken} from "./mock/MockToken.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {LLMOracleTaskParameters, LLMOracleTask} from "../src/llm/LLMOracleTask.sol";
import {IERC20Errors} from "@openzeppelin/contracts/interfaces/draft-IERC6093.sol";
import {SwanMarketParameters} from "../src/swan/SwanManager.sol";
import {SwanAssetFactory, SwanAsset} from "../src/swan/SwanAsset.sol";
\u0060\u0060\u0060
## BaseTest Contract
\u0060\u0060\u0060solidity
contract BaseTest is Test {
    LLMOracleRegistry registry;
    LLMOracleCoordinator coordinator;
    MockToken mocktoken;
    Swan swan;
    BuyerAgent buyerAgent;
    address requester = makeAddr("requester");
    // Mocks the oracle LLM
    address responder = makeAddr("responder");
    // Address whose buyer agent will acquire listed assets
    address buyer = makeAddr("buyer");
    // Proxies deployment part 1
    function setUp() public {
        LLMOracleRegistry registryImpl = new LLMOracleRegistry();
        mocktoken = new MockToken("Mock Token", "MT");
        uint256 generatorStake = 1;
        bytes memory _data = abi.encodeWithSignature(
            "initialize(uint256,uint256,address)",
            generatorStake,
            0,
            address(mocktoken)
        );
        ERC1967Proxy registryProxy = new ERC1967Proxy(
            address(registryImpl),
            _data
        );
        registry = LLMOracleRegistry(address(registryProxy));
        LLMOracleCoordinator coordinatorImpl = new LLMOracleCoordinator();
        uint256 _platformFee = 0.001 ether;
        uint256 _generationFee = 0.001 ether;
        uint256 _validationFee = 0.001 ether;
        _data = abi.encodeWithSignature(
            "initialize(address,address,uint256,uint256,uint256)",
            address(registry),
            address(mocktoken),
            _platformFee,
            _generationFee,
            _validationFee
        );
        ERC1967Proxy coordinatorProxy = new ERC1967Proxy(
            address(coordinatorImpl),
            _data
        );
        coordinator = LLMOracleCoordinator(address(coordinatorProxy));
        deploySwanAndAgent();
    }
    // Deployments function part 2 to avoid stack to deep error
    function deploySwanAndAgent() public {
        SwanAssetFactory assetFactory = new SwanAssetFactory();
\u0060\u0060\u0060
