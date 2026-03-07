# The slashed validator's stake gets split between `client`, `referrer`, and `service`

**Severity:** HIGH
**Auditor:** MixBytes

---

##### Description
There is an issue at line https://github.com/p2p-org/eth-staking-fee-distributor-contracts/blob/30a7ff78e8285f2eae4ae552efb390aa4453a083/contracts/feeDistributor/ContractWcFeeDistributor.sol#L114.
If the user's stake deposited by `client` gets slashed in ETH2 staking and is withdrawn to the `ContractWcFeeDistributor` contract (and all previous rewards were withdrawn), the `balance >= COLLATERAL` check will not pass. In that case, execution after the `if` block continues, and the users' deposit gets split as if it were rewarded.
A CRITICAL severity level was assigned to that issue because the user receives less ETH than they initially deposited minus the slashing penalty. Their stake is also split into `referrer` and `service`, which shouldn't happen in a normal case.

##### Recommendation
We recommend replacing the `balance >= COLLATERAL` check at line https://github.com/p2p-org/eth-staking-fee-distributor-contracts/blob/30a7ff78e8285f2eae4ae552efb390aa4453a083/contracts/feeDistributor/ContractWcFeeDistributor.sol#L114 and introduce a special registry of initially deposited validators public keys. It will help protocol owners to approve validator exiting (initially triggered by the user). Also, it would be useful to mark the current contract balance at the time of the validator exit being started. At the time when the contract receives a stake, withdrawal can be marked as finished, and the user is able to withdraw up to `address(this).balance - markedBalance`.
