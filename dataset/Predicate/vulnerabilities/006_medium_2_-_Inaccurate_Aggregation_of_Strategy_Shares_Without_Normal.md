# 2 - Inaccurate Aggregation of Strategy Shares Without Normalization Across ETH Derivatives

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** aggregation, strategy shares, normalization, ETH derivatives, operator, total shares, raw share balances, different tokens, share valuations, total staked value, unified unit, USD value, live strategies, for loop, msg.sender, threshold stake, underlying token, rocketETH, stETH, ETH

---

# Signature Validation Issue
The code does not enforce that the operator has sufficient staking shares when performing signature validation, and therefore, an operator with insufficient staking share could still generate valid signatures.

**Recommendation:** Ensure that the operator has enough staking shares when \u0060validateSignatures\u0060 is called. Consider adding the following function:

\u0060\u0060\u0060solidity
function getOperatorTotalStake(address _operator) external view returns (uint256) {
    uint256 totalStake;
    for (uint256 i; i != strategies.length;) {
        totalStake += IDelegationManager(delegationManager).operatorShares(_operator, IStrategy(strategies[i]));
        unchecked {
            ++i;
        }
    }
    return totalStake;
}
\u0060\u0060\u0060

And implementing the following change:

\u0060\u0060\u0060solidity
require(recoveredSigner == signerAddresses[i], "Predicate.validateSignatures: Invalid signature");
+ require(getOperatorTotalStake(operator) >= thresholdStake, "Operator has insufficient staking");
\u0060\u0060\u0060

**Predicate:** Fixed in PR 19.  
**CantinaManaged:** Fix verified.

## Inaccurate Aggregation of Strategy Shares Without Normalization Across ETH Derivatives
**Severity:** Medium Risk  
**Context:** ServiceManager.sol#L155-L163  
**Description:** When registering a new operator, the code loops over all strategies and sums the total shares.

\u0060\u0060\u0060solidity
for (uint256 i; i != strategies.length;) {
    totalStake += IDelegationManager(delegationManager).operatorShares(msg.sender, IStrategy(strategies[i]));
    unchecked {
        ++i;
    }
}
if (totalStake >= thresholdStake) {
\u0060\u0060\u0060

Each strategy has a different underlying token. Therefore, this line is simply summing the raw "share balances" from each of the registered strategies without any normalization or weighting. Different strategies have different share valuations (one share in strategy A represents a different underlying stake amount/value than one share in strategy B). Therefore, summing share counts directly across multiple strategies is inaccurate considering that the intention here is to measure "total staked value" in a unified unit (e.g., total underlying tokens USD value).

Currently, this is the list of all the live strategies:
- 0xbeaC0eeEeeeeEEeEeEEEEeeEEeEeeeEeeEEBEaC0 ⇒ underlying token is ETH.
- 0x93c4b944D05dfe6df7645A86cd2206016c51564D ⇒ underlying token is stETH.
- 0x1BeE69b7dFFfA4E2d53C2a2Df135C388AD25dCD2 ⇒ underlying token is rocketETH.
