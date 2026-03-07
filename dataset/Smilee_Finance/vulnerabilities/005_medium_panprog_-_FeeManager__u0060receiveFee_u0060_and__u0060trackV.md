# panprog - FeeManager \u0060receiveFee\u0060 and \u0060trackVaultFee\u0060 functions allow anyone to call it with user-provided dvp/vault address and add any arbitrary feeAmount to any address, breaking fees accounting and temporarily bricking DVP smart contract

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Smilee Finance
**Keywords:** cybersecurity, vulnerability, FeeManager, receiveFee, trackVaultFee, smart contract, dvp, vault address, fee accounting, malicious user, fee inflation, uint256.max, bricking contract, address authentication, role authentication, baseToken, withdrawFee, fake tokens, manual review, whitelist

---

panprog

high

# FeeManager \u0060receiveFee\u0060 and \u0060trackVaultFee\u0060 functions allow anyone to call it with user-provided dvp/vault address and add any arbitrary feeAmount to any address, breaking fees accounting and temporarily bricking DVP smart contract

## Summary

\u0060FeeManager\u0060 uses \u0060trackVaultFee\u0060 function to account vault fees. The problem is that this function can be called by any smart contract implementing \u0060vault()\u0060 function (there are no address or role authentication), thus malicious user can break all vault fees accounting by randomly inflating existing vault\u0027s fees, making it hard/impossible for admins to determine the real split of fees between vaults. Moreover, malicious user can provide such \u0060feeAmount\u0060 to \u0060trackVaultFee\u0060 function, which will increase any vault\u0027s fee to \u0060uint256.max\u0060 value, meaning all following calls to \u0060trackVaultFee\u0060 will revert due to fee addition overflow, temporarily bricking DVP smart contract, which calls \u0060trackVaultFee\u0060 on all mints and burns, which will always revert until \u0060FeeManager\u0060 smart contract is updated to a new address in \u0060AddressProvider\u0060.

Similarly, \u0060receiveFee\u0060 function is used to account fee amounts received by different addresses (dvp), which can later be withdrawn by admin via \u0060withdrawFee\u0060 function. The problem is that any smart contract implementing \u0060baseToken()\u0060 function can call it, thus any malicious user can break all accounting by adding arbitrary amounts to their addresses without actually paying anything. Once some addresses fees are inflated, it will be difficult for admins to track fee amounts which are real, and which are from fake \u0060dvp\u0060s and fake tokens.

## Vulnerability Detail

\u0060FeeManager.trackVaultFee\u0060 function has no role/address check:
\u0060\u0060\u0060solidity
    function trackVaultFee(address vault, uint256 feeAmount) external {
        // Check sender:
        IDVP dvp = IDVP(msg.sender);
        if (vault != dvp.vault()) {
            revert WrongVault();
        }

        vaultFeeAmounts[vault] += feeAmount;

        emit TransferVaultFee(vault, feeAmount);
    }
\u0060\u0060\u0060

Any smart contract implementing \u0060vault()\u0060 function can call it. The vault address returned can be any address, thus user can inflate vault fees both for existing real vaults, and for any addresses user chooses. This totally breaks all vault fees accounting.

\u0060FeeManager.receiveFee\u0060 function has no role/address check either:
\u0060\u0060\u0060solidity
    function receiveFee(uint256 feeAmount) external {
        _getBaseTokenInfo(msg.sender).safeTransferFrom(msg.sender, address(this), feeAmount);
        senders[msg.sender] += feeAmount;

        emit ReceiveFee(msg.sender, feeAmount);
    }
...
    function _getBaseTokenInfo(address sender) internal view returns (IERC20Metadata token) {
        token = IERC20Metadata(IVaultParams(sender).baseToken());
    }
\u0060\u0060\u0060

Any smart contract crafted by malicious user can call it. It just has to return base token, which can also be token created by the user. After transfering this fake base token, the \u0060receiveFee\u0060 function will increase user\u0027s fee balance as if it was real token transferred.

## Impact

Malicious users can break all fee and vault fee accounting by inflating existing vaults or user addresses fees earned without actually paying these fees, making it hard/impossible for admins to determine the actual fees earned from each vault or dvp. Moreover, malicious user can temporarily brick DVP smart contract by inflating vault\u0027s accounted fees to \u0060uint256.max\u0060, thus making all DVP mints and burns (which call \u0060trackVaultFee\u0060) revert.

## Code Snippet

\u0060FeeManager.trackVaultFee\u0060:
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/FeeManager.sol#L218-L228

\u0060FeeManager.receiveFee\u0060:
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/FeeManager.sol#L210-L215

## Tool used

Manual Review

## Recommendation

Consider adding a whitelist of addresses which can call these functions.
