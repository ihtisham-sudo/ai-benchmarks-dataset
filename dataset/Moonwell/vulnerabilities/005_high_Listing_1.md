# Listing 1

**Severity:** high
**Auditor:** Halborn
**Protocol:** Moonwell
**Keywords:** Solidity, xWELL, ERC20VotesUpgradeable, initialization, ERC20Permit, gasless transactions, token transfers, smart contract, function call, require, initializer, tokenName, tokenSymbol, tokenOwner, rate limits, pause duration, pause guardian, ownership transfer, vulnerability, recommendation

---

In the Solidity smart contract xWELL, which inherits from ERC20VotesUpgradeable, there seems to be an omission in the initialization process. The initialize function, intended to set up the contract’s initial state, does not include a call to **__ERC20Permit_init**. This function is critical for initializing the ERC20 Permit feature, which is part of the ERC20VotesUpgradeable contract. The ERC20 Permit feature allows for gasless transactions by enabling users to sign approvals for token transfers with their private keys. Not calling **__ERC20Permit_init** means that this functionality will not be properly set up in the xWELL contract.

xWELL.sol
# Listing 1
\u0060\u0060\u0060solidity
/// @dev on token\u0027s native chain, the lockbox must have its
/// bufferCap set to uint112 max
/// @notice initialize the xWELL token
/// @param tokenName The name of the token
/// @param tokenSymbol The symbol of the token
/// @param tokenOwner The owner of the token, Temporal
/// Governor on Base, Timelock on Moonbeam
/// @param newRateLimits The rate limits for the token
function initialize(
    string memory tokenName,
    string memory tokenSymbol,
    address tokenOwner,
    MintLimits.RateLimitMidPointInfo[] memory newRateLimits,
    uint128 newPauseDuration,
    address newPauseGuardian
\u0060\u0060\u0060
## Vulnerability Details

\u0060\u0060\u0060solidity
    ) external initializer {
        require(
           newPauseDuration <= MAX_PAUSE_DURATION,
           "xWELL: pause duration too long"
        );
        __ERC20_init(tokenName, tokenSymbol);
        __Ownable_init();
        _addLimits(newRateLimits);

        /// pausing
        __Pausable_init(); /// not really needed, but seems like good form
        _grantGuardian(newPauseGuardian); /// set the pause guardian
        _updatePauseDuration(newPauseDuration);

        transferOwnership(tokenOwner);
    }
\u0060\u0060\u0060

### Proof Of Concept:
- Without \u0060__ERC20Permit_init\u0060, the ERC20 Permit feature is non-functional.
- Users are unable to perform gasless transactions, a key feature expected from \u0060ERC20VotesUpgradeable\u0060.

### DETAILS BVSS:
AO:A/AC:L/AX:L/C:N/I:C/A:M/D:N/Y:N/R:P/S:C (7.0)

### Recommendation:
Modify the initialize function to include a call to \u0060__ERC20Permit_init\u0060. This function should be called with appropriate arguments (usually the name of the token) to properly initialize the ERC20 Permit feature.
SOLVED: The Moonwell Finance team solved the issue by calling the
__ERC20Permit_init function.  
Commit ID: 326357fc1fc1c5fdd83116ff9fb1f7cbf093d597
## & FINDINGS
