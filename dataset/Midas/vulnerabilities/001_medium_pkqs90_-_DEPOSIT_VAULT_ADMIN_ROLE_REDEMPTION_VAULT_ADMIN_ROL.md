# pkqs90 - DEPOSIT_VAULT_ADMIN_ROLE/REDEMPTION_VAULT_ADMIN_ROLE have larger permission than expected: they shouldn\u0027t be able to pause vaults

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Midas
**Keywords:** cyber security, vulnerability, DEPOSIT_VAULT_ADMIN_ROLE, REDEMPTION_VAULT_ADMIN_ROLE, permissions, vaults, pause, deposit, redeem, accessibility, contest readme, freeFromMinDeposit, setMinAmountToDeposit, withdrawToken, addPaymentToken, removePaymentToken, unexpected behavior, impact, manual review, recommendation

---

pkqs90

medium

# DEPOSIT_VAULT_ADMIN_ROLE/REDEMPTION_VAULT_ADMIN_ROLE have larger permission than expected: they shouldn\u0027t be able to pause vaults

## Summary

The accessibility of DEPOSIT_VAULT_ADMIN_ROLE and REDEMPTION_VAULT_ADMIN_ROLE has larger permission than what the contest readme claims: they can pause the vault and stop users from depositing/redeeming.

## Vulnerability Detail

According to the contest readme:

- \u0060DEPOSIT_VAULT_ADMIN_ROLE\u0060 has the role of \u0060Handles freeFromMinDeposit, setMinAmountToDeposit, withdrawToken, addPaymentToken, removePaymentToken in DepositVault\u0060.
- \u0060REDEMPTION_VAULT_ADMIN_ROLE\u0060 has the role of \u0060Handles withdrawToken, addPaymentToken, removePaymentToken in RedemptionVault\u0060.

However, these two roles are also capable of pausing the depositVault/redemptionVault, which is unexpected.

https://github.com/sherlock-audit/2024-05-midas/blob/main/midas-contracts/contracts/access/Pausable.sol#L18-L38
\u0060\u0060\u0060solidity
    modifier onlyPauseAdmin() {
>       _onlyRole(pauseAdminRole(), msg.sender);
        _;
    }

    /**
     * @dev upgradeable pattern contract\u0060s initializer
     * @param _accessControl MidasAccessControl contract address
     */
    // solhint-disable-next-line func-name-mixedcase
    function __Pausable_init(address _accessControl) internal onlyInitializing {
        __WithMidasAccessControl_init(_accessControl);
    }

    function pause() external onlyPauseAdmin {
        _pause();
    }

    function unpause() external onlyPauseAdmin {
        _unpause();
    }
\u0060\u0060\u0060

https://github.com/sherlock-audit/2024-05-midas/blob/main/midas-contracts/contracts/abstract/ManageableVault.sol#L139-L141
\u0060\u0060\u0060solidity
    function pauseAdminRole() public view override returns (bytes32) {
        return vaultRole();
    }
\u0060\u0060\u0060

https://github.com/sherlock-audit/2024-05-midas/blob/main/midas-contracts/contracts/DepositVault.sol
\u0060\u0060\u0060solidity
    function vaultRole() public pure override returns (bytes32) {
        return DEPOSIT_VAULT_ADMIN_ROLE;
    }
\u0060\u0060\u0060

https://github.com/sherlock-audit/2024-05-midas/blob/main/midas-contracts/contracts/RedemptionVault.sol
\u0060\u0060\u0060solidity
    function vaultRole() public pure override returns (bytes32) {
        return REDEMPTION_VAULT_ADMIN_ROLE;
    }
\u0060\u0060\u0060

## Impact

The two roles DEPOSIT_VAULT_ADMIN_ROLE/REDEMPTION_VAULT_ADMIN_ROLE have larger permission than they are expected to have.

## Code Snippet

- https://github.com/sherlock-audit/2024-05-midas/blob/main/midas-contracts/contracts/abstract/ManageableVault.sol#L139-L141
- https://github.com/sherlock-audit/2024-05-midas/blob/main/midas-contracts/contracts/access/Pausable.sol#L18-L38

## Tool used

Manual review

## Recommendation

Remove the pausability permission for DEPOSIT_VAULT_ADMIN_ROLE and REDEMPTION_VAULT_ADMIN_ROLE.
