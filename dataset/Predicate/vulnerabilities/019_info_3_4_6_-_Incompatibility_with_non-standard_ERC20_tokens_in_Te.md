# 3.4.6 - Incompatibility with non-standard ERC20 tokens in TellerWithMultiAssetSupportPredicateProxy

**Severity:** info
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** ERC20, tokens, transferFrom, approve, SafeERC20, compatibility, non-standard, return values, contract, deposit, depositAndBridge, OpenZeppelin, wrapper, verify, revert, implementation, function, msg.sender, vault, depositAmount

---

# 3.4.6 Incompatibility with non-standard ERC20 tokens in TellerWithMultiAssetSupportPredicateProxy
**Severity:** Informational  
**Context:** (No context files were provided by the reviewer)  
**Description:** In the deposit and depositAndBridge functions, the contract calls ERC20.transferFrom, ERC20.approve, etc. directly. Some tokens do not adhere strictly to the ERC20 standard or have non-standard return values; using raw transferFrom or approve can fail to detect such cases or revert incorrectly.  
**Recommendation:** Adopt OpenZeppelin’s SafeERC20 wrapper:
\u0060\u0060\u0060solidity
using SafeERC20 for IERC20;
IERC20(depositAsset).forceApprove(address(vault), depositAmount);
IERC20(depositAsset).safeTransferFrom(msg.sender, address(this), depositAmount);
\u0060\u0060\u0060
These SafeERC20 variants:
- Verify the token call’s return value, ensuring it either returns true or does not return data at all.
- Revert if the token’s call fails or returns an unexpected value.
- Improve compatibility with tokens that have non-standard implementations.  
**Predicate:** Acknowledged.  
**CantinaManaged:** Acknowledged.  

## 3.4.7 Operators cannot validate or limit deposit or depositAndBridge parameters
**Severity:** Informational  
**Context:** (No context files were provided by the reviewer)  
**Description:** In the TellerWithMultiAssetSupportPredicateProxy contract, the _authorizeTransaction call only encodes:
\u0060\u0060\u0060solidity
bytes memory encodedSigAndArgs = abi.encodeWithSignature("deposit()");
\u0060\u0060\u0060
or
\u0060\u0060\u0060solidity
bytes memory encodedSigAndArgs = abi.encodeWithSignature("depositAndBridge()");
\u0060\u0060\u0060
This means the operator signatures only approve the function name without referencing parameters such as depositAmount, recipient or BridgeData. Consequently, operators are "blind" to these arguments and cannot validate or limit them.  
**Recommendation:** If you want operators to have visibility or control over the actual parameters (e.g., maximum deposit, permitted recipient, bridging details), include those arguments in encodedSigAndArgs. For example:
\u0060\u0060\u0060solidity
bytes memory encodedSigAndArgs = abi.encodeWithSignature(
    "deposit(address,uint256,uint256,address,address)",
    depositAsset,
    depositAmount,
    minimumMint,
    recipient,
    teller
);
\u0060\u0060\u0060
This ensures that operator signatures explicitly cover the parameter values, preventing users from passing unexpected amounts or addresses. If parameter-level oversight is not desired, the current design is acceptable, but typically advanced operator gating requires parameter-aware authorization.  
**Predicate:** Acknowledged.  
**CantinaManaged:** Acknowledged.
