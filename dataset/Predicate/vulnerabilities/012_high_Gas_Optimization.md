# Gas Optimization

**Severity:** high
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** gas optimization, storage, mapping, policyID, policy text, unbounded strings, uint256, bytes32, keccak256, hash, on-chain, off-chain, data storage, cost reduction, smart contract, Ethereum, Solidity, contract optimization, performance, efficiency

---

# Gas Optimization
### Severity: Gas Optimization
**Context:** ServiceManager.sol

**Description:** The ServiceManager contract uses:
\u0060\u0060\u0060solidity
mapping(string => string) public idToPolicy;
\u0060\u0060\u0060
Both the "policyID" and the "policy text" are unbounded strings on-chain. Large or variable-length strings can occupy multiple storage slots, leading to high gas usage when storing or updating policies.

**Recommendation:**
- Use a uint256 for the policyID:
    \u0060\u0060\u0060solidity
    mapping(uint256 => bytes32) public idToPolicyHash;
    \u0060\u0060\u0060
    This ensures policy IDs are stored in a single 256-bit slot, removing overhead from unbounded string operations.
- Store policy text as a hash: Instead of storing the entire policy text, store a bytes32 hash (e.g., keccak256) of the policy:
    \u0060\u0060\u0060solidity
    bytes32 hashOfPolicy = keccak256(bytes(policyText));
    \u0060\u0060\u0060
    
This way, you reduce on-chain data to 32 bytes per policy. The full text can remain off-chain, and users can verify it by hashing locally and comparing to the on-chain record. By adopting these changes, you significantly reduce storage costs and gas consumption while preserving a unique identifier (uint256 policyID) and a verifiable reference to the policy content (bytes32 policyHash).

**Predicate:** Acknowledged. This recommendation will be implemented in a future version.

**CantinaManaged:** Acknowledged.
