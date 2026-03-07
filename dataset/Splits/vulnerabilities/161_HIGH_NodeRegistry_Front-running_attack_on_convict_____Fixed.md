# NodeRegistry Front-running attack on convict() ✓ Fixed

**Severity:** HIGH
**Auditor:** ConsenSys

---

#### Resolution



Blocknumber is removed from `convict` function, which removes any signal for an attacker in the scenario provided. However, the order of the transactions to convict a wrong signed hash is necessary to prevent any front-running attacks:


1. Convict(\_Blockhash)
2. recreate Blockheaders
3. RevealConvict (minimum 2 blocks after `convict` but as soon as recreateBlockheaders is confirmed)


The fixes were introduced in [ecf2c6a6](https://git.slock.it/in3/in3-contracts/commit/ecf2c6a6c2356b068c3966db0985b762ea822ca0) and [f4250c9a](https://git.slock.it/in3/in3-contracts/commit/f4250c9a7d9a493d77e2ccd07610d145bc67c48c), although later on NodeRegistry contract was split in two other contracts `NodeRegistryLogic` and `NodeRegistryData` and further changes were done in the conviction flow in different commits.




#### Description


`convict(uint _blockNumber, bytes32 _hash)` and `revealConvict()` are designed to prevent front-running and they do so for the purpose they are designed for. However, if the malicious node, is still sending out the wrong blockhash for the convicted block, anyone seeing the initial convict transaction, can check the convicted blocknumber with the nodes and send his own `revealConvict` before the original sender.


The original sender will be the one updating the block headers `recreateBlockheaders(_blockNumber, _blockheaders)`, and the attacker can just watch for the update headers to perform this attack.


#### Recommendation


For the first attack vector, remove the blocknumber from the `convict(uint _blockNumber, bytes32 _hash)` inputs and just use the hash.
