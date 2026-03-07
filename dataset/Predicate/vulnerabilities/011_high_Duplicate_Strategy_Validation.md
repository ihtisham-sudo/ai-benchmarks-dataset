# Duplicate Strategy Validation

**Severity:** high
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** duplicate, strategy, validation, staking, share, counting, array, service, manager, solidity, contract, owner, emit, params, quorum, registry, address, revert, function, recommendation

---

# Duplicate Strategy Validation
### Severity: High
**Context:** ServiceManager.sol

**Description:** When adding a strategy, the code should validate if there are duplicate strategies in the array; otherwise, if the strategy array contains duplicate strategies, the operator\u0027s staking share can be double counted.

\u0060\u0060\u0060solidity
function addStrategy(address _strategy, uint8 quorumNumber, uint256 index) external onlyOwner {
    IStakeRegistry.StrategyParams memory strategyParams =
        IStakeRegistry(stakeRegistry).strategyParamsByIndex(quorumNumber, index);
    if (address(strategyParams.strategy) != _strategy) {
        revert ServiceManager__InvalidStrategy();
    }
    strategies.push(_strategy);
    emit StrategyAdded(_strategy);
}
\u0060\u0060\u0060

**Recommendation:** Validate there is no duplicate strategy in the strategy array.

**Predicate:** Acknowledged. This recommendation will be implemented in a future version.

**CantinaManaged:** Acknowledged.
