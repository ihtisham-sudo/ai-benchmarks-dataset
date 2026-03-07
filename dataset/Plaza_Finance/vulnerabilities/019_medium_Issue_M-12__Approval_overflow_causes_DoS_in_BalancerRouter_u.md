# Issue M-12: Approval overflow causes DoS in BalancerRouter\u0027s exitPlazaAndBalancer

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** approval, overflow, DoS, BalancerRouter, exitPlazaAndBalancer, BPT, vault, safeIncreaseAllowance, arithmetic error, infinite allowance, gas optimization, withdrawal, core functionality, Smart Contract, Ethereum, SafeERC20, arithmetic underflow, foundry, test contract, ERC20

---

# Issue M-12: Approval overflow causes DoS in BalancerRouter\u0027s exitPlazaAndBalancer

Source: [GitHub Issue #835](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/835)  
Found by: 0xadrii

In \u0060_exitBalancerPool\u0060, the BalancerRouter contract will invoke \u0060balancerPoolToken.safeIncreaseAllowance\u0060 in order to increase the allowance to the balancerVault by the desired \u0060balancerPoolTokenIn\u0060. This is incorrect, given that Balancer Pool Tokens by default have an infinite allowance to the Balancer vault. This will lead to an overflow always being triggered when trying to approve the vault, effectively DoS’ing \u0060exitPlazaAndBalancer\u0060.

In BalancerRouter\u0027s \u0060_exitBalancerPool\u0060 function, the router tries to approve the BPT tokens to the balancerVault in order to exit the pool:

\u0060\u0060\u0060solidity
// File: BalancerRouter.sol
function _exitBalancerPool(
    bytes32 poolId,
    IAsset[] memory assets,
    uint256 balancerPoolTokenIn,
    uint256[] memory minAmountsOut,
    bytes memory userData,
    address to
) internal {
    IVault.ExitPoolRequest memory request = IVault.ExitPoolRequest({
        assets: assets,
        minAmountsOut: minAmountsOut,
        userData: userData,
        toInternalBalance: false
    });
    balancerPoolToken.safeIncreaseAllowance(address(balancerVault), balancerPoolTokenIn);
    balancerVault.exitPool(poolId, address(this), payable(to), request);
}
\u0060\u0060\u0060
The problem is that BPT tokens always have an infinite allowance to the Balancer’s vault in order to save gas and avoid approvals. This can be seen in Balancer\u0027s official BalancerPoolToken.sol implementation, where allowance always returns uint256(-1) if the spender is the vault, and is also mentioned explicitly in natspec: “Override to grant the Vault infinite allowance, causing for Pool Tokens to not require approval.”:

\u0060\u0060\u0060solidity
// File: BalancerPoolToken.sol
/**
 * @dev Override to grant the Vault infinite allowance, causing for Pool Tokens
 * to not require approval.
 *
 * This is sound as the Vault already provides authorization mechanisms when
 * initiation token transfers, which this
 * contract inherits.
 */
function allowance(address owner, address spender) public view override returns
(uint256) {
    if (spender == address(getVault())) {
        return uint256(-1);
    } else {
        return super.allowance(owner, spender);
    }
}
\u0060\u0060\u0060

When the router tries to approve the vault, it uses safeIncreaseAllowance from OpenZeppelin’s SafeERC20 library, which is implemented in the following way:

\u0060\u0060\u0060solidity
// File: SafeERC20.sol
/**
 * @dev Increase the calling contract\u0027s allowance toward \u0060spender\u0060 by \u0060value\u0060.
 * If \u0060token\u0060 returns no value,
 * non-reverting calls are assumed to be successful.
 */
function safeIncreaseAllowance(IERC20 token, address spender, uint256 value)
internal {
    uint256 oldAllowance = token.allowance(address(this), spender);
    forceApprove(token, spender, oldAllowance + value);
}
\u0060\u0060\u0060

Because oldAllowance will be type(uint256).max when spender is the Balancer vault, the following oldAllowance + value addition will overflow, effectively preventing any withdrawal to be performed via the Balancer Router contract.

Internal Pre-conditions
No response
No response

1. User calls \u0060exitPlazaAndBalancer\u0060
2. The router tries to approve the balancerVault as a spender for the balancerPoolToken. The \u0060safeIncreaseAllowance\u0060 function is called, and an overflow is triggered, DoS’ing any exit via the router.

Medium. The \u0060exitPlazaAndBalancer\u0060 will never work. Because this effectively breaks core contract functionality and effectively renders the contract useless (the main purpose of the router is to allow pool deposits/withdrawals and wrap/unwrap BPT tokens while doing it, and it has been demonstrated that withdrawals will never work, a core mechanism of the router), this issue should be deemed medium severity.

The following proof of concept illustrates the overflow. To run it, just create a foundry project and paste the following test contract:

\u0060\u0060\u0060solidity
contract ContractTest is Test {
    string BASE_RPC_URL = vm.envString("BASE_RPC_URL");
    // -- CREATE CONSTANTS HERE --
    using SafeERC20 for IERC20;
    // -- CREATE STORAGE VARIABLES HERE --
    IERC20 public pool = IERC20(0xC771c1a5905420DAEc317b154EB13e4198BA97D0); // BPT token
    address public vault = 0xBA12222222228d8Ba445958a75a0704d566BF2C8; // Balancer vault

    function setUp() public {
        vm.createSelectFork(BASE_RPC_URL);
    }

    function testBalancer_approvalOverflow() public {
        pool.safeIncreaseAllowance(vault, 1e18); // reverts with arithmetic error
    }
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
library SafeERC20 {
    function safeIncreaseAllowance(IERC20 token, address spender, uint256 value) internal {
        uint256 newAllowance = token.allowance(address(this), spender) + value;
        // ...
    }
}

interface IERC20 {
    function allowance(address user, address operator) external view returns (uint256);
}
\u0060\u0060\u0060

Then, create a .env with and set BASE_RPC_URL to an RPC, and run the poc with forge test --mt testBalancer_approvalOverflow. It will revert with “panic: arithmetic underflow or overflow (0x11)” reason.

Don’t approve the Balancer vault when withdrawing.

\u0060\u0060\u0060solidity
// File: BalancerRouter.sol
function _exitBalancerPool(
    bytes32 poolId,
    IAsset[] memory assets,
    uint256 balancerPoolTokenIn,
    uint256[] memory minAmountsOut,
    bytes memory userData,
    address to
) internal {
    IVault.ExitPoolRequest memory request = IVault.ExitPoolRequest({
        assets: assets,
        minAmountsOut: minAmountsOut,
        userData: userData,
        toInternalBalance: false
    });
    balancerPoolToken.safeIncreaseAllowance(address(balancerVault), balancerPoolTokenIn);
    balancerVault.exitPool(poolId, address(this), payable(to), request);
}
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/Convexity-Research/plaza-evm/pull/146
