# 4 - Proof of Code Mocking responses and validations on requests

**Severity:** high
**Auditor:** CodeHawks
**Protocol:** Swan
**Keywords:** mocking, responses, validations, attacker, victim, buyer, test case, mock generators, invalid output, unregister, fund, generation fees, validation fees, oracle, protocol, attack, outlier, ERC20, mocktoken, LLMOracleRegistry, register

---

# Vulnerability in Swan Contract Initialization

\u0060\u0060\u0060solidity
Swan swanImpl = new Swan();
SwanMarketParameters memory marketParams = SwanMarketParameters({
  withdrawInterval: uint256(1 weeks),
  sellInterval: uint256(1 weeks),
  buyInterval: uint256(1 weeks),
  platformFee: uint256(1),
  maxAssetCount: uint256(100),
  timestamp: uint256(block.timestamp)
});
LLMOracleTaskParameters memory oracleParams = LLMOracleTaskParameters({
  difficulty: uint8(1),
  numGenerations: uint40(1),
  numValidations: uint40(0)
});
bytes memory _data = abi.encodeWithSelector(
  Swan(address(swanImpl)).initialize.selector,
  marketParams,
  oracleParams,
  address(coordinator),
  address(mocktoken),
  address(1),
  assetFactory
);
ERC1967Proxy swanProxy = new ERC1967Proxy(address(swanImpl), _data);
swan = Swan(address(swanProxy));
string memory _name = "buyer agent";
string memory _description = "buyer agent";
uint96 _royaltyFee = 1;
uint256 _amountPerRound = type(uint256).max;
address _operator = address(swan);
address _owner = buyer;
buyerAgent = new BuyerAgent(
  _name,
  _description,
  _royaltyFee,
  _amountPerRound,
  _operator,
  _owner
);
\u0060\u0060\u0060
## Vulnerability in testSweepFunds Function

\u0060\u0060\u0060solidity
function testSweepFunds() public {
  bytes32 protocol = "protocol";
  bytes memory input = "input";
  bytes memory models = "models";
  LLMOracleTaskParameters memory oracleParams = LLMOracleTaskParameters({
    difficulty: 1,
    numGenerations: 1,
    numValidations: 0
  });
  deal(address(mocktoken), requester, 1 ether);
  vm.startPrank(requester);
  mocktoken.approve(address(coordinator), type(uint256).max);
  // request to the coordinator paying the corresponding protocol and generation fees
  coordinator.request(protocol, input, models, oracleParams);
  vm.stopPrank();
  deal(address(mocktoken), responder, 1 ether);
  vm.startPrank(responder);
  mocktoken.approve(address(registry), type(uint256).max);
}
\u0060\u0060\u0060
## LLM Oracle Fee Granting

\u0060\u0060\u0060solidity
LLMOracleKind oracleKind = LLMOracleKind.Generator;
registry.register(oracleKind);
uint256 taskId = 1;
uint256 nonce = 123;
bytes memory output = "output";
bytes memory metadata = "metadata";
// response from the LLM, since there is no validation the fee is granted right away
coordinator.respond(taskId, nonce, output, metadata);
uint256 generatorAllowance = mocktoken.allowance(
  address(coordinator),
  responder
);
assertEq(generatorAllowance, 0.004 ether); // diff*fee
vm.stopPrank();
// owner sweeps funds from the contract
coordinator.withdrawPlatformFees();
vm.prank(responder);
vm.expectRevert(
  abi.encodeWithSelector(
    IERC20Errors.ERC20InsufficientBalance.selector,
    address(coordinator),
    0,
    0.004 ether
  )
);
// LLM oracle cannot access the granted funds
mocktoken.transferFrom(address(coordinator), responder, 0.004 ether);
\u0060\u0060\u0060

Here you can also find the code for the mock token:

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
contract MockToken is ERC20 {
  constructor(
    string memory name_,
    string memory symbol_
  ) ERC20(name_, symbol_) {
    _mint(msg.sender, 100 ether);
  }
}
\u0060\u0060\u0060

- Manual review.

Maintain a separate record of funds allocated to oracle agents, subtracting these from the total contract balance during platform fee withdrawals. This will ensure that agents’ earned fees are preserved when the protocol withdraws platform fees and other residual tokens.
**Submitted by:** ethworker, Sickurity, auditweiler, newspacexyz, ChainDefenders, auditism, 0xnbvc, dimulski, mate-jdb, zxriptor, greese, galturok, jiri123, elser17, tejaswarambhe, yaioxy, silver_eth, saurabh_singh, abhishekthakur, ericselvig, emmanuel, 0rpseqwe, johny7173, Gladiators, bbash, m4k2xmk.  
**Selected submission by:** johny7173.

The respond and validate functions can be mocked which will lead to attacker getting the generation and validation fees without providing valid responses, and could also lead to attacks against other generator/validators in order to force them lose their generation/validation fees.

The LLMOracleRegistry allows any address to register and unregister at any time. An attacker can register multiple generators/validators and call respond and validate with invalid output/scores with as low generatorStakeAmount/validatorStakeAmount whichever is greater. This can be done by calling register -> respond -> unregister for as many generations needed, and then register -> validate -> unregister for as many validations needed.

It will lead to lost generation and validation fees while getting invalid output values. Furthermore, this attack can be used in order to force a legitimate generator/validator appear as an outlier and lose their generation/validation fee.
## Proof of Code Mocking responses and validations on requests

### Overview
The attacker registers mock generators, responds with invalid output values and unregisters, repeating the same procedure with mock validators.

### Actors
- **Attacker:** The address which will fund the mock generators and mock validators.
- **Victim:** The buyer which submitted a purchase request.

### Test Case
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test, console} from "forge-std/Test.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC1967Proxy} from "@openzeppelin/contracts/proxy/ERC1967/ERC1967Proxy.sol";
import {Swan} from "../contracts/swan/Swan.sol";
import {SwanMarketParameters} from "../contracts/swan/SwanManager.sol";
import {LLMOracleTaskParameters} from "../contracts/llm/LLMOracleTask.sol";
import {LLMOracleCoordinator} from "../contracts/llm/LLMOracleCoordinator.sol";
import {LLMOracleRegistry, LLMOracleKind} from "../contracts/llm/LLMOracleRegistry.sol";
import {BuyerAgentFactory, BuyerAgent} from "../contracts/swan/BuyerAgent.sol";
import {SwanAssetFactory, SwanAsset} from "../contracts/swan/SwanAsset.sol";

contract MockERC20 is ERC20 {
    constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {}
}

contract POC is Test {
    IERC20 dria;
    LLMOracleCoordinator coordinator;
    LLMOracleRegistry registry;
    address buyerAgentFactory;
    address swanAssetFactory;
}
\u0060\u0060\u0060
