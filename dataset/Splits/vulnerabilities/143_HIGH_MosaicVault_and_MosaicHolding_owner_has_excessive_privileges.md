# MosaicVault and MosaicHolding owner has excessive privileges

**Severity:** HIGH
**Auditor:** TrailOfBits

---

## Diﬃculty: High

## Type: Data Validation

### Target: CrosslayerPortal

## Description
The owner of the MosaicVault and MosaicHolding contracts has too many privileges across the system. Compromise of the owner’s private key would put the integrity of the underlying system at risk.

The owner of the MosaicVault and MosaicHolding contracts can perform the following privileged operations in the context of the contracts:

- Rescuing funds if the system is compromised
- Managing withdrawals, transfers, and fee payments
- Pausing and unpausing the contracts
- Rebalancing liquidity across chains
- Investing in one or more investment strategies
- Claiming rewards from one or more investment strategies

The ability to drain funds, manage liquidity, and claim rewards creates a single point of failure. It increases the likelihood that the contracts’ owner will be targeted by an attacker and increases the incentives for the owner to act maliciously.

## Exploit Scenario
Alice, the owner of MosaicVault and MosaicHolding, deploys the contracts. MosaicHolding eventually holds assets worth USD 20 million. Eve gains access to Alice’s machine, upgrades the implementations, pauses MosaicHolding, and drains all funds from the contract.

## Recommendations
Short term, clearly document the functions and implementations that the owner of the MosaicVault and MosaicHolding contracts can change. Additionally, split the privileges provided to the owner across multiple roles (e.g., a fund manager, fund rescuer, owner, etc.) to ensure that no one address has excessive control over the system.

Long term, develop user documentation on all risks associated with the system, including those associated with privileged users and the existence of a single point of failure.
