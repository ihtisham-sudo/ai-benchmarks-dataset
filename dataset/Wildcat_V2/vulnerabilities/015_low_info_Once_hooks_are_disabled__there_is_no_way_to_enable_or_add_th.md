# Once hooks are disabled, there is no way to enable or add them again.

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, disableHooksTemplate, HooksFactory, enabled member, HooksTemplate, access restriction, _deployHooksInstance, deployHooksInstance, deployMarketAndHooks, permanent removal, ArchControllerOwner, addHooksTemplate, HooksTemplateAlreadyExists, re-enable, function revert, manual review, mitigation steps, error assessment, security flaw, template management

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/fe746cc0fbedc4447a981a50e6ba4c95f98b9fe1/src/HooksFactory.sol#L205


# Vulnerability details

## Impact

The \u0060disableHooksTemplate\u0060 function from \u0060HooksFactory\u0060 sets the \u0060enabled\u0060 member of the \u0060HooksTemplate\u0060 structure to false. This variable is used to restrict access to the \u0060_deployHooksInstance\u0060 function, which is called by \u0060deployHooksInstance\u0060 and \u0060deployMarketAndHooks\u0060. Once disabled, a template can never be enabled or added again.
Therefore, a hook can either be enabled or permanently removed.
If \u0060ArchControllerOwner\u0060 wants to re-enable this template, he won\u0027t be able to use \u0060addHooksTemplate\u0060 (the only function that turns \u0060enabled\u0060 to true) because it will revert with \u0060HooksTemplateAlreadyExists\u0060 (and it shouldn\u0027t allow adding that hook because it will override the hook for already deployed markets).


## Proof of Concept

the following test will revert with:
\u0060\u0060\u0060
[FAIL: HooksTemplateAlreadyExists()] test_PoC_disableHooksTemplate() (gas: 10043475)
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

import "forge-std/Test.sol";

import {WildcatArchController} from "../src/WildcatArchController.sol";
import {HooksFactory} from "../src/HooksFactory.sol";
import {LibStoredInitCode} from "src/libraries/LibStoredInitCode.sol";
import {AccessControlHooks} from "../src/access/AccessControlHooks.sol";
import {WildcatMarket} from "../src/market/WildcatMarket.sol";

import {MockERC20} from "../test/shared/mocks/MockERC20.sol";
import {MockSanctionsSentinel} from "./shared/mocks/MockSanctionsSentinel.sol";
import {deployMockChainalysis} from "./shared/mocks/MockChainalysis.sol";

contract AuditMarket is Test {
    WildcatArchController wildcatArchController;
    MockSanctionsSentinel internal sanctionsSentinel;
    HooksFactory hooksFactory;

    MockERC20 ERC0 = new MockERC20();

    address immutable ARCH_DEPLOYER = makeAddr("ARCH_DEPLOYER");
    address immutable FEE_RECIPIENT = makeAddr("FEE_RECIPIENT");

    address accessControlHooksTemplate = LibStoredInitCode.deployInitCode(type(AccessControlHooks).creationCode);

    function _storeMarketInitCode() internal virtual returns (address initCodeStorage, uint256 initCodeHash) {
        bytes memory marketInitCode = type(WildcatMarket).creationCode;
        initCodeHash = uint256(keccak256(marketInitCode));
        initCodeStorage = LibStoredInitCode.deployInitCode(marketInitCode);
    }

    function test_PoC_disableHooksTemplate() public {
        deployMockChainalysis();
        vm.startPrank(ARCH_DEPLOYER);
        wildcatArchController = new WildcatArchController();
        sanctionsSentinel = new MockSanctionsSentinel(address(wildcatArchController));
        (address initCodeStorage, uint256 initCodeHash) = _storeMarketInitCode();
        hooksFactory =
            new HooksFactory(address(wildcatArchController), address(sanctionsSentinel), initCodeStorage, initCodeHash);

        hooksFactory.addHooksTemplate(
            accessControlHooksTemplate, "accessControlHooksTemplate", FEE_RECIPIENT, address(ERC0), 1000000 ether, 500
        );
        hooksFactory.disableHooksTemplate(accessControlHooksTemplate);
        hooksFactory.addHooksTemplate(
            accessControlHooksTemplate, "accessControlHooksTemplate", FEE_RECIPIENT, address(ERC0), 1000000 ether, 500
        );
    }
}
\u0060\u0060\u0060

## Tools Used

Manual Review

## Recommended Mitigation Steps

Add a function to enable a hook that was previously disabled


## Assessed type

Error
