# ERC-4337 call to `_payPrefund` may lead to the validator stake being split

**Severity:** HIGH
**Auditor:** MixBytes

---

##### Description
There is an issue at line https://github.com/p2p-org/eth-staking-fee-distributor-contracts/blob/30a7ff78e8285f2eae4ae552efb390aa4453a083/contracts/feeDistributor/ContractWcFeeDistributor.sol#L114 and https://github.com/p2p-org/eth-staking-fee-distributor-contracts/blob/30a7ff78e8285f2eae4ae552efb390aa4453a083/contracts/feeDistributor/Erc4337Account.sol#L103.
If a user voluntarily exits staking, then `ContractWcFeeDistributor` will receive a 32 ETH stake (in case if there were no slashings). If all previous rewards were withdrawn from the contract (or they are quite low), then a call to the `withdraw()` function via `ERC-4337` account abstraction logic may lead to paying for the transaction fee using that stake funds (in case if there were no deposit or paymaster is not used). Then this `balance >= COLLATERAL` check will not pass and the users' stake would get split also to `referrer` and `service`.
The HIGH severity level was assigned to that issue since a user receives less ETH than they initially deposited. Their stake is split also to `referrer` and `service` what shouldn't happen in a normal case.

##### Recommendation
We recommend replacing the call to `_payPrefund()` here https://github.com/p2p-org/eth-staking-fee-distributor-contracts/blob/30a7ff78e8285f2eae4ae552efb390aa4453a083/contracts/feeDistributor/Erc4337Account.sol#L52. This replacement will prevent contract funds from being used to pay for transaction gas.
