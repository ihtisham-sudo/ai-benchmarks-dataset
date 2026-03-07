# .2 Missing event when updating the merkle root

**Severity:** low
**Auditor:** Cantina
**Protocol:** SuperseedToken
**Keywords:** merkle root, event emission, state change, smart contract, TokenClaim.sol, onlyOwner, InvalidInput, bytes32, emit, merkleRootUpdated, update, function, parameters, old value, new value, security, best practices, Ethereum, solidity, contract

---

# .2 Missing event when updating the merkle root
**Severity:** Low Risk  
**Context:** TokenClaim.sol  
**Description:** The merkle root function makes a key state change but lacks to emit an event:
\u0060\u0060\u0060solidity
function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
    if (_merkleRoot == bytes32(0)) revert InvalidInput("_merkleRoot");
    merkleRoot = _merkleRoot;
}
\u0060\u0060\u0060
**Recommendation:** Emit an event with the old and then new merkle roots as arguments:
\u0060\u0060\u0060solidity
function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
    if (_merkleRoot == bytes32(0)) revert InvalidInput("_merkleRoot");
    emit merkleRootUpdated(merkleRoot, _merkleRoot);
    merkleRoot = _merkleRoot;
}
\u0060\u0060\u0060
