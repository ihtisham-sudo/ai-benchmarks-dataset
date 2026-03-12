# Well Token is Not Utilized on the CompoundERC4626.sol Contract - Informational (1.7)

**Severity:** info
**Auditor:** Halborn
**Protocol:** Moonwell
**Keywords:** Well, token, unused, variable, contract, delete, redundant, optimization, code, cleanliness, ERC20, constructor, implementation, efficiency, best practice, Moonwell, team, solved, commit, ID

---

CompoundERC4626 contract follows the EIP4626 standard. This extension allows the minting and burning of shares (represented using the ERC20 inheritance) in exchange for underlying assets through standardized deposit, mint, redeem and burn workflows. But this extension also has the following problem: When the vault is empty or nearly empty, deposits are at high risk of being stolen through front-running by inflating the share-token value through burning obtained shares. This is variously known as a donation or inflation attack and is essentially a problem of slippage. Therefore, this issue could affect the users using the protocol that run the risk of losing a part of their deposited tokens.

DETAILSCompoundERC4626.sol
# Listing 1
\u0060\u0060\u0060solidity
contract CompoundERC4626 is ERC4626 {}
\u0060\u0060\u0060

## Proof Of Concept:
Step 1: A malicious early user can deposit() with 1 wei of asset token as the first depositor of the Vault, a get 1 wei of shares token.  
Step 2: Then the attacker can send 10000e18 - 1 of Mtokens and inflate the price per share from 1,000 to an extreme value of 1.0000e22.
## Step 3
As a result, the future user who deposits 19999e18 will immediately lose their deposits.

AO:A/AC:L/AX:L/C:M/I:N/A:N/D:H/Y:N/R:N/S:U (8.8)

Consider requiring a minimal amount of share tokens to be minted for the first minter, and send a part of the initial mint as a permanent reserve so that the price per share can be more resistant to manipulation.

TECHSOLVED: The Moonwell Finance team solved the issue by requiring a minimal amount of share tokens in the deployment script.

b8062797ea74907c260af47b1321a8a3987b9393
The maxMint function is currently designed to use the borrowCap for determining the maximum amount that can be minted, which is inconsistent with the expected behavior. Ideally, the function should be using the supplyCap to calculate this limit. This inconsistency could lead to incorrect calculations and potential imbalances in the system.

CompoundERC4626.sol#L159
## Listing 2
\u0060\u0060\u0060solidity
function maxMint(address) public view override returns (uint256) {
    if (comptroller.mintGuardianPaused(address(mToken))) {
        return 0;
    }

    uint256 borrowCap = comptroller.borrowCaps(address(mToken));
    if (borrowCap != 0) {
        uint256 totalBorrows = mToken.totalBorrows();
        return borrowCap - totalBorrows;
    }

    return type(uint256).max;
}
\u0060\u0060\u0060

AO:A/AC:L/AX:L/C:N/I:M/A:N/D:M/Y:N/R:N/S:U (6.2)
## Recommendation:
Replace the use of borrowCap with supplyCap in the maxMint function to ensure accurate calculations for the maximum mintable amount.

SOVLED: The Moonwell Finance team solved the issue by changing borrowCap with supplyCap.

## Commit ID:
ae87166ce0634f05da0a6edd879d9c7a4c74b1e3
Solmate\u0027s SafeTransferLib, which is used for transferring tokens, currently does not verify the existence of a token contract or whether the token address is the zero-address. The library explicitly states that it does not check if a token has any code, delegating that responsibility to the caller. As a result, if the token address is empty, the transfer operation will appear to succeed without actually crediting any tokens to the contract.

CompoundERC4626.sol

\u0060\u0060\u0060solidity
import {SafeTransferLib} from "solmate/utils/SafeTransferLib.sol";
\u0060\u0060\u0060
## DETAILS BVSS:
AO:A/AC:L/AX:L/C:N/I:L/A:L/D:L/Y:N/R:N/S:U (3.8)

## TECH Recommendation:
Consider switching to OpenZeppelin\u0027s SafeERC20 library, which includes built-in checks to verify that an address contains code. This would eliminate the need for manual checks like ensuring the address is not the zero-address or verifying that code.length > 0.
**SOVLED:** The Moonwell Finance team resolved the issue by ensuring that the deployment script checks the underlying token.
## DETAILS
## TECH
## FINDINGS
## 4.4 (HAL-04) ERC4626 VAULT DEPOSITS AND WITHDRAWS SHOULD CONSIDER SLIPPAGE - INFORMATIONAL (1.7)

The scoped repositories make use of ERC4626 custom implementations that should follow the EIP-4626 definitions. This standard states the following security consideration:  
"If implementors intend to support EOA account access directly, they should consider adding another function call for deposit/mint/withdraw/redeem with the means to accommodate slippage loss or unexpected deposit/withdrawal limits, since they have no other means to revert the transaction if the exact output amount is not achieved."  
These vault implementations do not implement a way to limit the slippage when deposits/withdraws are performed. This condition affects specially to EOA since they don’t have a way to verify the amount of tokens received and revert the transaction in case they are too few compared to what was expected to be received.  
Applying this security consideration would help to EOA to avoid being front-run and losing tokens in transactions towards these smart contracts.

TECHAO:A/AC:L/AX:M/C:N/I:N/A:N/D:L/Y:N/R:N/S:U (1.7)

It is recommended to include slippage checks in the aforementioned functions to allow EOA to set the minimum amount of tokens that they expect to receive by executing these functions.
## References:
- EIP-4626: Security Considerations

ACKNOWLEDGED: The Moonwell Finance team acknowledged this finding.

## & FINDINGS
The function \u0060claimReward()\u0060 has been declared as public, but it is never called internally within the contract. It is best practice to mark such functions as external instead, as this can save gas. In cases where the function takes arguments, external functions can read the arguments directly from calldata instead of having to allocate memory.

CompoundERC4626.sol#L82
## Listing 4
\u0060\u0060\u0060solidity
/// @notice Claims liquidity mining rewards from Compound and
/// sends it to rewardRecipient
function claimRewards() public {
    address[] memory holders = new address[](1);
    holders[0] = address(this);

    MToken[] memory mTokens = new MToken[](1);
    mTokens[0] = MToken(address(mToken));

    comptroller.claimReward(holders, mTokens, false, true);
    uint256 amount = well.balanceOf(address(this));
    well.safeTransfer(rewardRecipient, amount);

    emit ClaimRewards(amount, address(well));
}
\u0060\u0060\u0060
- **Severity**: AO:A/AC:L/AX:M/C:N/I:N/A:N/D:L/Y:N/R:N/S:U (1.7)

It’s recommended to change the function visibility from public to external in the claimReward function.

**SOLUTION**: The Moonwell Finance team solved the issue by changing the function visibility.

**Commit ID**: b8062797ea74907c260af47b1321a8a3987b9393
## 4.6 (HAL-06) Well Token is Not Utilized on the CompoundERC4626.sol Contract - Informational (1.7)

In the CompoundERC4626.sol contract, the Well token is defined in the constructor, but it is not used. The unused variables should be deleted from the contract.

### Code Location:
CompoundERC4626.sol

\u0060\u0060\u0060sol
ERC20 public immutable well;
\u0060\u0060\u0060

AO:A/AC:L/AX:M/C:N/I:N/A:N/D:L/Y:N/R:N/S:U (1.7)

Consider removing redundant variables.

SOVLED: The Moonwell Finance team solved the issue by removing redundant variables.
Commit ID: ae87166ce0634f05da0a6edd879d9c7a4c74b1e3
When a function with a memory array is called externally, the abi.decode() step has to use a for-loop to copy each index of the calldata to the memory index. Each iteration of this for-loop costs at least 60 gas (i.e. 60 * .length). Using calldata directly, obviates the need for such a loop in the contract code and runtime execution. If the array is passed to an internal function which passes the array to another internal function where the array is modified and therefore memory is used in the external call, it’s still more gas-efficient to use calldata when the external function uses modifiers, since the modifiers may prevent the internal functions from being called. Some gas savings if function arguments are passed as calldata instead of memory. Note that in older Solidity versions, changing some function arguments from memory to calldata may cause “unimplemented feature error”. This can be avoided by using a newer (0.8.*) Solidity compiler.

DETAILS CompoundERC4626.sol
## Listing 6
\u0060\u0060\u0060solidity
/// @notice Claims liquidity mining rewards from Compound and
/// sends it to rewardRecipient
/// used for edgecase where reward distribution is not yet
/// configured or was removed
/// the tokens were swept into the vault.
/// @param tokens The list of tokens to sweep
function sweepRewards(address[] calldata tokens) external {
    for (uint256 i = 0; i < tokens.length; i++) {
        ERC20 token = ERC20(tokens[i]);
        uint256 amount = token.balanceOf(address(this));
        token.safeTransfer(rewardRecipient, amount);
\u0060\u0060\u0060
## Vulnerability Details
Emit ClaimRewards(amount, address(token));

AO:A/AC:L/AX:M/C:N/I:N/A:N/D:L/Y:N/R:N/S:U (1.7)

Use calldata in the function.

SOLVED: The Moonwell Finance team solved the issue by changing memory with calldata.

ae87166ce0634f05da0a6edd879d9c7a4c74b1e3
PAGE END
