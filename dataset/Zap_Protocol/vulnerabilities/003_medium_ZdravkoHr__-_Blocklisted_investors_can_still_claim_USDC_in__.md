# ZdravkoHr. - Blocklisted investors can still claim USDC in \u0060TokenSale.sol\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zap Protocol
**Keywords:** cybersecurity, vulnerability, TokenSale.sol, USDC, blacklisted users, claiming, Admin.setClaimBlock, blockClaim mapping, Admin.claim, address(this), require statement, bypass, functionality, manual review, security flaw, smart contract, user blocking, claim functionality, code review, recommendation

---

ZdravkoHr.

high

# Blocklisted investors can still claim USDC in \u0060TokenSale.sol\u0060

## Summary
A wrong argument is passed when checking if a user is blacklisted for claiming in [\u0060TokenSale.claim()\u0060](https://github.com/sherlock-audit/2024-03-zap-protocol/blob/c2ad35aa844899fa24f6ed0cbfcf6c7e611b061a/zap-contracts-labs/contracts/TokenSale.sol#L367). Because the check is insufficient, blocked users can claim their USDC.

## Vulnerability Detail
[\u0060Admin.setClaimBlock()\u0060](https://github.com/sherlock-audit/2024-03-zap-protocol/blob/c2ad35aa844899fa24f6ed0cbfcf6c7e611b061a/zap-contracts-labs/contracts/Admin.sol#L271-L273) blocks users from claiming. The function accepts the address of the user to be blocked and adds it to the \u0060blockClaim\u0060 mapping.

\u0060\u0060\u0060solidity
    /**
     @dev Whitelist users
     @param _address Address of User
     */
    function setClaimBlock(address _address) external onlyRole(OPERATOR) {
        blockClaim[_address] = true;
    }
\u0060\u0060\u0060

The check in \u0060Admin.claim()\u0060 wrongly passes \u0060address(this)\u0060 as argument when calling \u0060Admin.blockClaim\u0060.

\u0060\u0060\u0060solidity
        require(
            uint8(epoch) > 1 && !admin.blockClaim(address(this)),
            "TokenSale: Not time or not allowed"
        );
\u0060\u0060\u0060
In this context, \u0060address(this)\u0060 will be the address of the token sale contract and the require statement can be bypassed even by a blocked user.
## Impact
The whole functionality for blocking claims doesn\u0027t work properly.

## Code Snippet
\u0060\u0060\u0060solidity
    function claim() external {
        checkingEpoch();
        require(
            uint8(epoch) > 1 && !admin.blockClaim(address(this)),
            "TokenSale: Not time or not allowed"
        );

        Staked storage s = stakes[msg.sender];
        require(s.amount != 0, "TokenSale: No Deposit");
        require(!s.claimed, "TokenSale: Already Claimed");

        uint256 left;
        (s.share, left) = _claim(s);
        require(left > 0, "TokenSale: Nothing to claim");
        uint256 refundTaxAmount;
        if (s.taxAmount > 0) {
            uint256 tax = userTaxRate(s.amount, msg.sender);
            uint256 taxFreeAllc = _maxTaxfreeAllocation(msg.sender) * PCT_BASE;
            if (taxFreeAllc >= s.share) {
                refundTaxAmount = s.taxAmount;
            } else {
                refundTaxAmount = (left * tax) / POINT_BASE;
            }
            usdc.safeTransferFrom(marketingWallet, msg.sender, refundTaxAmount);
        }
        s.claimed = true;
        usdc.safeTransfer(msg.sender, left);
        emit Claim(msg.sender, left);
    }
\u0060\u0060\u0060
## Tool used

Manual Review

## Recommendation
Pass the address of the user.

\u0060\u0060\u0060diff
        require(
-            uint8(epoch) > 1 && !admin.blockClaim(address(this)),
+            uint8(epoch) > 1 && !admin.blockClaim(msg.sender)),
            "TokenSale: Not time or not allowed"
        );
\u0060\u0060\u0060
