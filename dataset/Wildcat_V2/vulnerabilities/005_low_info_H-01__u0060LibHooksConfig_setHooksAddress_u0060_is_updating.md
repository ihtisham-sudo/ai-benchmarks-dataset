# H-01 \u0060LibHooksConfig.setHooksAddress\u0060 is updating \u0060address\u0060 incorrectly

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, wildcat protocol, HooksConfig, market deployment, feature enabling, hookAddress, LibHooksConfig, setHooksAddress, hookConfig, bit clearing, malicious user, market registration, hooks contract, hookFactory, deployMarketAndHooks, DeployMarketInputs, non-zero address, proof of concept, security recommendation

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/types/HooksConfig.sol#L84-L94


# Vulnerability details


**Description:** Currently, the wildcat protocol is using \u0060HooksConfig\u0060 for deploying markets, which is responsible for enabling various features in a particular market.

The current \u0060HookConfig\u0060 encoding is as follows:
\u0060\u0060\u0060
----------------------------------------------------------
| 160 bit (hookAddress) | 16 bit (flags) | 80 bit (others)|
----------------------------------------------------------
\u0060\u0060\u0060
The \u0060LibHooksConfig.setHooksAddress()\u0060 function is responsible for updating the new \u0060hookAddress\u0060 in the \u0060hookConfig\u0060, but it is only clearing the leftmost \u006096 bits\u0060 instead of \u0060160 bits\u0060.

\u0060\u0060\u0060solidity
function setHooksAddress(
  HooksConfig hooks,
  address _hooksAddress
) internal pure returns (HooksConfig updatedHooks) {
  assembly {
    // Shift twice to clear the address
    updatedHooks := shr(96, shl(96, hooks))
    // Set the new address
    updatedHooks := or(updatedHooks, shl(96, _hooksAddress))
  }
}
\u0060\u0060\u0060

### Impact:

1. A malicious user could deploy and register an wildcat market with a malicious hooks contract using \u0060hookFactory.deployMarketAndHooks\u0060, which has a non-zero address in \u0060DeployMarketInputs.parameters.hooks\u0060.

### Proof of Concept (PoC):

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import \u0027src/types/HooksConfig.sol\u0027;
import { Test, console2 } from \u0027forge-std/Test.sol\u0027;

contract TestH1 is Test {
    function setUp() public {}

    function testSetHooksAddress() public {
        HooksConfig craftedHook = encodeHooksConfig(address(0x1111111111111111111111111111111111111111), true, true, true, true, true, true, true, true, true, true);

        address hookInstance = address(this);

        craftedHook = LibHooksConfig.setHooksAddress(craftedHook, hookInstance);

        HooksConfig expectedConfig = encodeHooksConfig(address(this), true, true, true, true, true, true, true, true, true, true);

        assertNotEq(
            HooksConfig.unwrap(expectedConfig), HooksConfig.unwrap(craftedHook)
        );
    }
}
\u0060\u0060\u0060

**Recommendation:**

\u0060\u0060\u0060diff
+      updatedHooks := shr(160, shl(160, hooks))
-      updatedHooks := shr(96, shl(96, hooks))
\u0060\u0060\u0060


## Assessed type

Error
