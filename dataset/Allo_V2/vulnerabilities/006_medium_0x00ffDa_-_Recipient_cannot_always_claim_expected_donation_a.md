# 0x00ffDa - Recipient cannot always claim expected donation amount from a vault

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, ERC20, DonationVotingMerkleDistributionVaultStrategy, transfer fee, claimable amount, vault, donation, recipient, non-standard behavior, smart contracts, mapping, manual review, impact, token, fee deduction, claims mapping, audit, code snippet, recommendation

---

0x00ffDa

medium

# Recipient cannot always claim expected donation amount from a vault
Funding recipients cannot claim the amount expected from a \u0060DonationVotingMerkleDistributionVaultStrategy\u0060 pool if they receive donation of a token has a fee on transfer. The vault will hold less (by the fee amount) than is recorded in the contract as claimable by them.

## Vulnerability Detail
**First, why is this issue valid despite Sherlock rules excluding non-standard ERC20 behavior?**
While the Sherlock rules currently exclude "issues related to tokens with non-standard behaviors", t[he rules also state that](https://docs.sherlock.xyz/audits/judging/judging#iii.-some-standards-observed) "In case of conflict between information in the README, vs Sherlock rules, **the README overrides Sherlock rules**." And the contest README specifically says that all ERC20 with non-standard behavior are supported:

> "Q: Do you expect to use any of the following tokens with non-standard behaviour with the smart contracts?
> Yes as we support all ERC20 tokens."

DonationVotingMerkleDistributionVaultStrategy contracts store donation amounts in [a \u0060claims\u0060 mapping](https://github.com/allo-protocol/allo-v2/blob/851571c27df5c16f6586ece2a1cb6fd0acf04ec9/contracts/strategies/donation-voting-merkle-distribution-vault/DonationVotingMerkleDistributionVaultStrategy.sol#L54C18-L54C18) per recipient and per donated token. This is intended to also represent all the amounts claimable by registered recipients. However, in the case of donated [ERC20 tokens with a non-zero transfer fee](https://github.com/d-xo/weird-erc20#fee-on-transfer), a donated amount is not claimable in full since the transfer from the donor to the vault will reduce the amount that can be claimed by the recipient.

## Impact
Recipients cannot claim the amount expected from a vault in a DonationVotingMerkleDistributionVaultStrategy pool when a donated token has a transfer fee.

## Code Snippet
[DonationVotingMerkleDistributionVaultStrategy._afterAllocate() function](https://github.com/allo-protocol/allo-v2/blob/851571c27df5c16f6586ece2a1cb6fd0acf04ec9/contracts/strategies/donation-voting-merkle-distribution-vault/DonationVotingMerkleDistributionVaultStrategy.sol#L104-L136) - the last line contains the faulty assumption.
\u0060\u0060\u0060javascript
    /// @notice After allocation hook to store the allocated tokens in the vault
    /// @param _data The encoded recipientId, amount and token
    /// @param _sender The sender of the allocation
    function _afterAllocate(bytes memory _data, address _sender) internal override {
        // Decode the \u0027_data\u0027 to get the recipientId, amount and token
        (address recipientId, Permit2Data memory p2Data) = abi.decode(_data, (address, Permit2Data));

        // Get the token address
        address token = p2Data.permit.permitted.token;
        uint256 amount = p2Data.permit.permitted.amount;

        if (token == NATIVE) {
            if (msg.value < amount) {
                revert AMOUNT_MISMATCH();
            }
            SafeTransferLib.safeTransferETH(address(this), amount);
        } else {
            PERMIT2.permitTransferFrom(
                // The permit message.
                p2Data.permit,
                // The transfer recipient and amount.
                ISignatureTransfer.SignatureTransferDetails({to: address(this), requestedAmount: amount}),
                // Owner of the tokens and signer of the message.
                _sender,
                // The packed signature that was the result of signing
                // the EIP712 hash of \u0060_permit\u0060.
                p2Data.signature
            );
        }

        // Update the total payout amount for the claim
        claims[recipientId][token] += amount;
    }
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation
In the \u0060_afterAllocate()\u0060 cited above, compare vault\u0027s balance of the token being donated before and after calling \u0060permitTransferFrom()\u0060. If it is lower than the donated \u0060amount\u0060, assume this difference is a transfer fee and reduce the claimable amount by the fee.


