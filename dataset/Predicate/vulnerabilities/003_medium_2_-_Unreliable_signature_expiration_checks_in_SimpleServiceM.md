# 2 - Unreliable signature expiration checks in SimpleServiceManager due to block.number usage

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** SimpleServiceManager, L2 blockchain, Plume network, block.number, signature expiration, Ethereum block, timing assumptions, block.timestamp, reliability, expiration checks, smart contracts, Plume documentation, block timing, protocol structure, hub and spoke, transaction, sequencer, validation, fix, PR 20

---

# .2 Stale operator registrations allow under-staked operators to remain in ServiceManager
**Severity:** MediumRisk  
**Context:** ServiceManager.sol#L173-L187  
**Description:** A staker can sequentially delegate to multiple operators (in the DelegationManager) and register each as an operator with the ServiceManager (via registerOperatorToAVS). Over time, they undelegate from the first operator after waiting the minimum withdrawal delay (e.g., ~2 weeks) and delegate to a second operator, registering that second operator as well. Because the ServiceManager does not automatically check if previously registered operators still hold enough stake, multiple operators can remain registered even though only one is actively staked. This leads to multiple "valid" operators in ServiceManager with insufficient or zero stake in DelegationManager.  
**Recommendation:** Implement a housekeeping or periodic re-check that verifies each registered operator still meets the staking criteria. For example, a scheduled job or on-chain function calling updateOperatorsForQuorum or a custom function that checks each operator’s stake and deregisters those who have fallen below the threshold. This keeps the operator list accurate and prevents operators who are no longer staked from remaining in the system.  
**Predicate:** Acknowledged. This is valuable feedback yet given the current permissioned state of Predicate, I feel we can hold off on this change until we decide to enable some form of economic security using restaking / Eigenlayer.  
**CantinaManaged:** Acknowledged.
**Severity:** Medium Risk  
**Context:** SimpleServiceManager.sol#L235-L245  
**Description:** The protocol uses hub and spoke structure and the SimpleServiceManager.sol is deployed in L2 blockchain such as Plume network. The code uses block.number to check signature expiration. However, according to the Plume documentation:  
Plume assigns its own block numbers, distinct from Ethereum’s, with multiple Plume blocks potentially fitting within a single Ethereum block. However, each Plume block is always associated with exactly one Ethereum block. In Plume smart contracts, querying block.number returns a value close to the L1 Ethereum block number when the sequencer received the transaction, though it may not be exact. Timing assumptions based on block numbers are reliable over several hours but not within minutes, similar to Ethereum.  
This means that in the Plume network, block.number refers to the L1 Ethereum block number, not the L2 Plume block number. As a result, using block.number for expiration checks is unreliable for accurately determining the L2 block timing.  
**Recommendation:** Use block.timestamp to validate signature expiration instead of block.number.  
**Predicate:** Fixed in PR 20.  
**Cantina Managed:** Fix verified.  

**Severity:** Medium Risk  
**Context:** ServiceManager.sol#L319  
**Description:** When the ServiceManager contract performs the signature verification, the code loops over the threshold number to check if the operator status is registered. To register an operator, the operator has to have sufficient stake share.
\u0060\u0060\u0060solidity
uint256 totalStake;
for (uint256 i; i != strategies.length;) {
    totalStake += IDelegationManager(delegationManager).operatorShares(msg.sender, IStrategy(strategies[i]));
    unchecked {
        ++i;
    }
}
if (totalStake >= thresholdStake) {
    operators[msg.sender] = OperatorInfo(totalStake, OperatorStatus.REGISTERED);
    signingKeyToOperator[_operatorSigningKey] = msg.sender;
    ISignatureUtils.SignatureWithSaltAndExpiry memory _operatorSig = ISignatureUtils.SignatureWithSaltAndExpiry(
        _operatorSignature.signature, _operatorSignature.salt, _operatorSignature.expiry
    );
    IAVSDirectory(avsDirectory).registerOperatorToAVS(msg.sender, _operatorSig);
    emit OperatorRegistered(msg.sender);
}
\u0060\u0060\u0060
However, when validating the signature, the code does not check if the operator has sufficient staking shares.
- The operator can undelegate from the strategy so the operator\u0027s staking share is below the ServiceManager threshold.
- The admin can remove a strategy so the operator\u0027s staking share could be below the ServiceManager threshold.
