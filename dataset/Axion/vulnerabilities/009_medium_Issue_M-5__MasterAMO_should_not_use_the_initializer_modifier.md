# Issue M-5: MasterAMO should not use the initializer modifier

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Axion
**Keywords:** MasterAMO, initializer modifier, onlyInitializing modifier, inheritance, SolidlyV2AMO, SolidlyV3AMO, OpenZeppelin, initialization, contract, deployment, protocol, vulnerability, operational issue, functionality, admin role, multi-sig wallet, Boost stablecoin, USDC, USDT, DEX

---

# Issue M-5: MasterAMO should not use the initializer modifier

**Source:** [GitHub Issue #244](https://github.com/sherlock-audit/2024-10-axion-judging/issues/244)  
**Found by:** FonDevs, KupiaSec, UsmanAtique, calc1f4r, hunter_w3b  

## Summary  
MasterAMO is a utils contract that is intended to be inherited by SolidlyV2AMO, SolidlyV3AMO contracts; therefore, its initializer function should not use the initializer modifier, instead, it should use onlyInitializing modifier.  

## Root Cause  
In the MasterAMO.sol:104 contract, the initialize function uses the initializer modifier. This is incorrect for a contract like MasterAMO, which is meant to be inherited by other contracts, such as SolidlyV2AMO and SolidlyV3AMO. In this inheritance model, the SolidlyV2AMO contract also has its own initialize function, which includes the initializer modifier and calls the initialize function of MasterAMO. The problem here is that both the parent contract MasterAMO and the child contracts SolidlyV2AMO, SolidlyV3AMO are using the initializer modifier, which limits initialization to only one call.  

According to the OpenZeppelin documentation, the onlyInitializing modifier should be used to allow initialization in both the parent and child contracts. The onlyInitializing modifier ensures that when the initialize function is called, any contracts in its inheritance chain can still complete their own initialization.  

[OpenZeppelin Documentation](https://docs.openzeppelin.com/contracts/4.x/api/proxy#Initializable-initializer--)  
A modifier that defines a protected initializer function that can be invoked at most once. Its scope, onlyInitializing functions can be used to initialize parent contracts.  

## Internal pre-conditions  
No response
## External Pre-conditions
No response

## Attack Path
No response

## Impact
In this scenario, no direct attack or monetary loss is likely. However, the vulnerability causes a significant operational issue, preventing inheriting contracts from completing initialization. This could lead to a failure in the deployment of critical protocol components, affecting the overall system functionality.

## PoC
A simple PoC in Remix.

## Mitigation
Replace the initializer modifier in the Master AMO contract with the onlyInitializing modifier. This allows the initialize function to be used by both the Master AMO and any inheriting contracts during their initialization phase, without conflicting with their individual setup processes.

\u0060\u0060\u0060solidity
function initialize(
    address admin, // Address assigned the admin role (given exclusively to
    a multi-sig wallet)
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
address boost_, // The Boost stablecoin address
address usd_, // generic name for $1 collateral ( typically USDC or USDT )
address pool_, // The pool where AMO logic applies for Boost-USD pair
// On each chain where Boost is deployed, there will be a stable Boost-USD
pool ensuring BOOST\u0027s peg.
// Multiple Boost-USD pools can exist across different DEXes on the same
chain, each with its own AMO, maintaining independent peg guarantees.
address boostMinter_ // the minter contract
) public initializer {
) public onlyInitializing {
\u0060\u0060\u0060

Discussion  
sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/AXION-MONEY/liquidity-amo/pull/11](https://github.com/AXION-MONEY/liquidity-amo/pull/11)
