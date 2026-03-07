# 3.4.2 - Use an uint256 Task ID instead of a string for spent Task Ids mapping

**Severity:** info
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** uint256, Task ID, mapping, spentTaskIds, string, replay protection, unique identifier, storage, cost, collisions, encoding, off-chain, incrementing, boolean, contract, logic, ambiguity, identifier, recommendation, implementation

---

# 3.4.1 ECDSA Signature Validation
**Severity:** Informational  
**Context:** ServiceManager.sol  
**Description:** This only validates ECDSA signatures from externally owned accounts (EOAs). Smart contracts (such as Gnosis Safe or custom multisig wallets) cannot generate these ECDSA signatures directly, meaning a contract-based operator cannot sign tasks. This restricts potential operator implementations to EOAs only.  
**Recommendation:** Use a library that can handle both EOAs and contract wallets, such as OpenZeppelin’s SignatureChecker.isValidSignatureNow. This accommodates EIP-1271 for contract signatures, enabling multisig or contract-based operator accounts:
\u0060\u0060\u0060solidity
require(
    SignatureChecker.isValidSignatureNow(
        operatorSigner,
        messageHash,
        signatures[i]
    ),
    "Invalid signature"
);
\u0060\u0060\u0060
If adopting contract signatures, be mindful of reentrancy or other complexities that arise from calling an external isValidSignature function on an untrusted contract. Employ reentrancy guards and thorough review the EIP-1271 flow to mitigate these risks.  
**Predicate:** Acknowledged. We will consider implementing this in a future version.  
**CantinaManaged:** Acknowledged.

## 3.4.2 Use an uint256 Task ID instead of a string for spent Task Ids mapping
**Severity:** Informational  
**Context:** ServiceManager.sol  
**Description:** Currently, the contract tracks replay protection with a mapping of the form:
\u0060\u0060\u0060solidity
mapping(string => bool) public spentTaskIds;
\u0060\u0060\u0060
This stores task IDs as arbitrary strings. However, strings are more expensive to store and may be prone to collisions or unexpected issues if different encodings are used. Relying on a string for a nonce or unique identifier can also complicate off-chain logic.  
**Recommendation:** Use a numerical task ID (an incrementing uint256) in place of a string:
\u0060\u0060\u0060solidity
mapping(uint256 => bool) public spentTaskIds;
\u0060\u0060\u0060
This is cheaper to store (only one storage slot per integer) and ensures simpler, more consistent logic around incrementing and checking uniqueness. It also reduces ambiguity about possible string collisions or encoding differences.  
**Predicate:** Acknowledged. This will be implemented in a future version.  
**CantinaManaged:** Acknowledged.

## 3.4.3 Lack of a double-step transfer ownership pattern
**Severity:** Informational  
**Context:** ServiceManager.sol  
**Description:** All the contracts are using the standard OpenZeppelin\u0027s Ownable library. The standard OpenZeppelin’s Ownable contract allows transferring the ownership of the contract in a single step:
\u0060\u0060\u0060solidity
\u0060\u0060\u0060
## Ownership Transfer Vulnerability

\u0060\u0060\u0060solidity
/**
 * @dev Transfers ownership of the contract to a new account (\u0060newOwner\u0060).
 * Can only be called by the current owner.
 */
function transferOwnership(address newOwner) public virtual onlyOwner {
    if (newOwner == address(0)) {
        revert OwnableInvalidOwner(address(0));
    }
    _transferOwnership(newOwner);
}

/**
 * @dev Transfers ownership of the contract to a new account (\u0060newOwner\u0060).
 * Internal function without access restriction.
 */
function _transferOwnership(address newOwner) internal virtual {
    address oldOwner = _owner;
    _owner = newOwner;
    emit OwnershipTransferred(oldOwner, newOwner);
}
\u0060\u0060\u0060

If the nominated EOA account is not a valid account, it is entirely possible that the owner may accidentally transfer ownership to an uncontrolled account, losing the access to all functions with the onlyOwner modifier.

**Recommendation:** It is recommended to implement a two-step transfer process in all the contracts in the codebase where the owner nominates an account and the nominated account needs to call an \u0060acceptOwnership()\u0060 function for the transfer of the ownership to fully succeed. This ensures the nominated EOA account is a valid and active account. A good code example could be OpenZeppelin’s Ownable2Step contract:

\u0060\u0060\u0060solidity
/**
 * @dev Starts the ownership transfer of the contract to a new account. Replaces the pending transfer if there
 * is one.
 * Can only be called by the current owner.
 *
 * Setting \u0060newOwner\u0060 to the zero address is allowed; this can be used to cancel an initiated ownership
 * transfer.
 */
function transferOwnership(address newOwner) public virtual override onlyOwner {
    _pendingOwner = newOwner;
    emit OwnershipTransferStarted(owner(), newOwner);
}

/**
 * @dev Transfers ownership of the contract to a new account (\u0060newOwner\u0060) and deletes any pending owner.
 * Internal function without access restriction.
 */
function _transferOwnership(address newOwner) internal virtual override {
    delete _pendingOwner;
    super._transferOwnership(newOwner);
}

/**
 * @dev The new owner accepts the ownership transfer.
 */
function acceptOwnership() public virtual {
    address sender = _msgSender();
    if (pendingOwner() != sender) {
        revert OwnableUnauthorizedAccount(sender);
    }
    _transferOwnership(sender);
}
\u0060\u0060\u0060

**Predicate:** Fixed in commit f922c15.  
**CantinaManaged:** Fix verified.  
**Severity:** Informational
