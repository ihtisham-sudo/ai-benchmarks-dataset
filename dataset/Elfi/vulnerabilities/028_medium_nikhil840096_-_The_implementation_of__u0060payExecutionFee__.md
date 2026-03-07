# nikhil840096 - The implementation of \u0060payExecutionFee()\u0060 didn\u0027t take \u0060EIP-150\u0060 into consideration. Keepers can steal additional execution fee from users.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, EIP-150, execution fee, keepers, GasProcess, processExecutionFee, malicious keeper, gas limit, usedGas, StakeFacet, transaction, refund, exploit, smart contract, external function, gas cost, manual review, security risk, blockchain

---

nikhil840096

High

# The implementation of \u0060payExecutionFee()\u0060 didn\u0027t take \u0060EIP-150\u0060 into consideration. Keepers can steal additional execution fee from users.

## Summary
The implementation of \u0060processExecutionFee()\u0060 didn\u0027t take \u0060EIP-150\u0060 into consideration. Keepers can steal additional execution fee from users

## Vulnerability Detail
The issue arises on \u0060L18\u0060 of \u0060GasProcess.sol:processExecutionFee()\u0060, as it\u0027s an external function, calling\u0060processExecutionFee()\u0060 is subject to EIP-150.
Only \u006063/64\u0060 gas is passed to the \u0060GasProcess\u0060 sub-contract(\u0060external library\u0060), and the remaning \u00601/64\u0060 gas is reserved in the caller contract which will be refunded to \u0060keeper\u0060 after the execution of the whole transaction. But calculation of \u0060usedGas \u0060  includes this portion of the cost as well.

A malicious keeper can exploit this issue to drain out all execution fee, regardless of the actual execution cost.
Let\u0027s take \u0060executeMintStakeToken()\u0060 operation as an example to show how it works:
\u0060\u0060\u0060solidity
executionFeeUserHasPaid = 200K Gwei
tx.gasprice = 1 Gwei
actualUsedGas = 100K
\u0060\u0060\u0060
\u0060actualUsedGas\u0060 is the gas cost since \u0060startGas\u0060(L76 of \u0060StakeFacet .sol\u0060) but before calling \u0060processExecutionFee()\u0060(L88 of \u0060StakeFacet.sol\u0060)

Let\u0027s say, the keeper sets tx.gaslimit to make
\u0060\u0060\u0060solidity
startGas = 164K
\u0060\u0060\u0060
Then the calculation of \u0060usedGas\u0060 , \u0060L18\u0060 of \u0060GasProcess.sol\u0060, would be
\u0060\u0060\u0060solidity
uint256 usedGas= cache.startGas- gasleft() = 164K - (164K - 100K) * 63 / 64 = 101K
\u0060\u0060\u0060
and
\u0060\u0060\u0060solidity
executionFeeForKeeper = 101K * tx.gasprice = 101K * 1 Gwei = 101K Gwei
refundFeeForUser = 200K - 101K = 99K Gwei
\u0060\u0060\u0060
As setting of \u0060tx.gaslimit\u0060 doesn\u0027t affect the actual gas cost of the whole transaction, the excess gas will be refunded to \u0060msg.sender\u0060. Now, the keeper increases \u0060tx.gaslimit\u0060 to make \u0060startGas = 6500K\u0060, the calculation of \u0060usedGas\u0060 would be
\u0060\u0060\u0060solidity
uint256 usedGas= cache.startGas- gasleft() = 6500K - (6500K - 100K) * 63 / 64 = 200K
\u0060\u0060\u0060
and
\u0060\u0060\u0060solidity
executionFeeForKeeper = 200K * tx.gasprice = 200K * 1 Gwei = 200K Gwei
refundFeeForUser = 200K - 200K = 0 Gwei
\u0060\u0060\u0060
We can see the keeper successfully drain out all execution fee, the user gets nothing refunded.
## Impact
Keepers can steal additional execution fee from users.
## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/GasProcess.sol#L18C17-L18C25
## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060diff
    function processExecutionFee(PayExecutionFeeParams memory cache) external {
-        uint256 usedGas = cache.startGas - gasleft();
+       uint256 usedGas = cache.startGas - gasleft() * 64 / 63;
        uint256 executionFee = usedGas * tx.gasprice;
        uint256 refundFee;
        uint256 lossFee;
\u0060\u0060\u0060
