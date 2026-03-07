# Recipient can block the sender 's cancel by sending the NFT to an address known to revert the transfer of the underlying ERC20 

**Severity:** HIGH
**Auditor:** Cantina

---

## Context
- `SablierV2LockupDynamic.sol#L420-L433`
- `SablierV2LockupLinear.sol#L350-L363`

## Description
The `_cancel()` functions of the `SablierV2LockupDynamic` and `SablierV2LockupLinear` transfer the remaining funds for the sender and recipient in one call using the `safeTransfer` function for each:

```solidity
function _cancel(uint256 streamId) internal override onlySenderOrRecipient(streamId) {
    address recipient = _ownerOf(streamId);
    ...
    if (recipientAmount > 0) {
        ...
        stream.asset.safeTransfer({ to: recipient, value: recipientAmount });
    }
    if (senderAmount > 0) {
        stream.asset.safeTransfer({ to: sender, value: senderAmount });
    }
}
```

`safeTransfer` will revert when the underlying transfer fails in any way. As the recipient's address is determined by the ownership of the Sablier NFT, the recipient can front-run the sender's cancel transaction by sending the NFT to an address known to revert by the underlying token's `safeTransfer` (e.g., an address on USDC's blocklist).

While this may not directly benefit the recipient, one could easily imagine a situation where a sender decides to cancel a stream, and a recipient is unhappy about it. In this case, they could call `withdraw()` to withdraw the full amount they are owed and transfer the NFT to such an address, bricking the sender's funds.

## Recommendation
Split the cancel functionality into two separate transactions. One where the initiator stops the stream accounting and withdraws their part of the funds. Then a second transaction where the other party withdraws their funds. This way, the transfer to the recipient cannot block the sender's cancel.

- **Sablier:** Fixed in PR 422.
- **Cantina:** Confirmed.
