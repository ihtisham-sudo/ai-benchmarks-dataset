# korok - VouchFaucet can be immediately drained by anyone

**Severity:** high
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** VouchFaucet, claimTokens, maxClaimable, claimedTokens, ERC20, transferERC20, onlyOwner, vulnerability, cybersecurity, smart contract, token balance, drain, arbitrary amount, mapping, require statement, reentrancy risk, token distribution, manual review, cooldown mechanism, faucet outflows

---

korok

High

# VouchFaucet can be immediately drained by anyone

## Summary

The \u0060claimTokens\u0060 function in the VouchFaucet contract fails to properly enforce the \u0060maxClaimable\u0060 limit because it does not update the value in the \u0060claimedTokens\u0060 mapping. This allows any address to claim an arbitrary amount of any token, potentially draining the entire token balance of the contract, in a single transaction or through multiple transactions.

## Vulnerability Detail

Included below is the relevant code from the [VouchFaucet](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/peripheral/VouchFaucet.sol#L93-L97) followed by key insights:

\u0060\u0060\u0060solidity
    /// @notice Token address to msg sender to claimed amount
    mapping(address => mapping(address => uint256)) public claimedTokens;

    /// @notice Token address to max claimable amount
    mapping(address => uint256) public maxClaimable;

    /// @notice Claim tokens from this contract
    function claimTokens(address token, uint256 amount) external {
        require(claimedTokens[token][msg.sender] <= maxClaimable[token], "amount>max");
        IERC20(token).transfer(msg.sender, amount);
        emit TokensClaimed(msg.sender, token, amount);
    }

    /// @notice Transfer ERC20 tokens
    function transferERC20(address token, address to, uint256 amount) external onlyOwner {
        IERC20(token).transfer(to, amount);
    }
\u0060\u0060\u0060
- The claimedTokens mapping is never updated. It will always return 0 when looking up how much of any token has been claimed by any address. 

- The maxClaimable mapping will by default return 0 for any token the contract could ever receive. The contract owner can use the setMaxClaimable function but is only able to set the claimable amount for any token to 0 or greater.

- The transferERC20 function is protected by the onlyOwner modifier signaling the desire to restrict access to this type of transfer. 

- Currently no matter what the admin does the require statement in claimTokens will always pass because it evaluates an expression that will always effectively be:   \u0060require(0 <= [uint256], "amount>max");\u0060 This makes claimTokens effectively equivalent to an unrestricted version of transferERC20.

### Proof of Concept

The proof of concept below imports and utilizes [the protcols own TestWrapper](https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/test/foundry/TestWrapper.sol) for simplicity in setting up a realistic testing environment.

The test case demonstrates that despite the VouchFaucet containing mechanisms that clearly intend to disallow the faucet from being easily drained by a single address, such an outcome is possible with no effort. 


\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.16;

import {Test, console} from "forge-std/Test.sol";
import {TestWrapper} from "../TestWrapper.sol";
import {VouchFaucet} from "../../src/contracts/peripheral/VouchFaucet.sol";

import {IERC20} from "@openzeppelin/token/ERC20/IERC20.sol";

contract TestVouchFaucet is TestWrapper {
    VouchFaucet public vouchFaucet;
    uint256 public TRUST_AMOUNT = 10 * UNIT;

    function setUp() public {
        deployMocks();
        vouchFaucet = new VouchFaucet(address(userManagerMock), TRUST_AMOUNT);
    }

    function testDrainVouchFaucet() public {
        address bob = address(1234);

        erc20Mock.mint(address(vouchFaucet), 3 * UNIT);

        vouchFaucet.setMaxClaimable(address(erc20Mock), 1 * UNIT);
        assertEq(vouchFaucet.maxClaimable(address(erc20Mock)), 1 * UNIT);

        // Bob can claim any number of tokens despite maxClaimable set to 1 Unit
        vm.prank(bob);
        vouchFaucet.claimTokens(address(erc20Mock), 3 * UNIT);

        assertEq(IERC20(erc20Mock).balanceOf(bob), 3 * UNIT);
    }

}
\u0060\u0060\u0060

## Impact

Without the intended enforcement provided by the require statement the claimTokens function provides unrestricted external access to an ERC20 transfer function. This is clearly not intended as demonstrated by the presence of the onlyOwner on the similar transferERC20 function. The result is that any caller can immediately transfer out any amount of any token.

This oversight completely undermines the token distribution model of the faucet. If deployed without modification it would render the contract useless for the intended purpose due to its inability to securely hold any amount of any token.  

## Code Snippet

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/peripheral/VouchFaucet.sol#L93-L97

## Tool used

Manual Review

## Recommendation

The following correction ensures that any individual address can\u0027t claim more than the set claimable amount, maintaining the intended token distribution model of the faucet.

\u0060\u0060\u0060diff

File: VouchFaucet.sol

    function claimTokens(address token, uint256 amount) external {
-        require(claimedTokens[token][msg.sender] <= maxClaimable[token], "amount>max");
+        uint256 newTotal = claimedTokens[token][msg.sender] + amount;
+        require(newTotal <= maxClaimable[token], "Exceeds max claimable amount");

+        claimedTokens[token][msg.sender] = newTotal;
        IERC20(token).transfer(msg.sender, amount);

        emit TokensClaimed(msg.sender, token, amount);
    }
\u0060\u0060\u0060

The following additional recommendations should be considered. The suggestions won\u0027t impact legitimate users, but raise the effort required for an malicious actor to disrupt the intended functioning of the contract.

1. Ensure the claimedTokens mapping is updated before the transfer to avoid reentrancy risk, OpenZeppelin ReentrancyGuard could also be considered. 

1. Consider adding an admin adjustable global cap on total tokens that can be claimed across all addresses to help control faucet outflows. 

3. Consider implementing a time-based cooldown mechanism to limit the frequency of claims per address.
