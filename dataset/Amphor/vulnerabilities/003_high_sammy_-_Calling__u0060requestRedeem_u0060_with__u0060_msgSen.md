# sammy - Calling \u0060requestRedeem\u0060 with \u0060_msgSender() != owner\u0060  will lead to user\u0027s shares being locked in the vault forever

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Amphor
**Keywords:** cybersecurity, vulnerability, AsyncSynthVault, requestRedeem, owner, shares, vault, redeemRequestId, allowance, tokens, epochId, claimRedeem, claim, user, receiver, balance, locked, permanently, recovery, manual review

---

sammy

high

# Calling \u0060requestRedeem\u0060 with \u0060_msgSender() != owner\u0060  will lead to user\u0027s shares being locked in the vault forever

## Summary
The [\u0060requestRedeem\u0060](https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L477) function in \u0060AsyncSynthVault.sol\u0060 can be invoked by a user on behalf of another user, referred to as \u0027owner\u0027, provided that the user has been granted sufficient allowance by the \u0027owner\u0027. However, this action results in a complete loss of balance.


## Vulnerability Detail
The [\u0060_createRedeemRequest\u0060](https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L721) function contains a discrepancy; it fails to update the \u0060lastRedeemRequestId\u0060 for the user eligible to claim the shares upon maturity. Instead, it updates this identifier for the \u0027owner\u0027 who delegated their shares to the user. As a result, the shares become permanently locked in the vault, rendering them unclaimable by either the \u0027owner\u0027 or the user.

This issue unfolds as follows:

1. The \u0027owner\u0027 deposits tokens into the vault, receiving vault shares in return.
2. The \u0027owner\u0027 then delegates the allowance of all their vault shares to another user.
3. When \u0060epochId == 1\u0060, this user executes The [\u0060requestRedeem\u0060](https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L477) , specifying the \u0027owner\u0027\u0027s address as \u0060owner\u0060, the user\u0027s address as \u0060receiver\u0060, and the \u0027owner\u0027\u0027s share balance as \u0060shares\u0060.
4. The internal function \u0060_createRedeemRequest\u0060 is invoked, incrementing \u0060epochs[epochId].redeemRequestBalance[receiver]\u0060 by the amount of \u0060shares\u0060, and setting \u0060lastRedeemRequestId[owner] = epochId\u0060.
5. At \u0060epochId == 2\u0060, the user calls [\u0060claimRedeem\u0060](https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L521), which in turn calls the internal function [\u0060_claimRedeem\u0060](https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L758), with \u0060owner\u0060 set to \u0060_msgSender()\u0060 (i.e., the user\u0027s address) and \u0060receiver\u0060 also set to the user\u0027s address.
6. In this scenario, \u0060lastRequestId\u0060 remains zero because \u0060lastRedeemRequestId[owner] == 0\u0060 (here, \u0060owner\u0060 refers to the user\u0027s address). Consequently, \u0060epochs[lastRequestId].redeemRequestBalance[owner]\u0060 is also zero. Therefore, no shares are minted to the user.


Proof of Code : 

The following test demonstrates the claim made above : 

\u0060\u0060\u0060solidity
function test_poc() external {
        // set token balances
        deal(vaultTested.asset(), user1.addr, 20); // owner

        vm.startPrank(user1.addr);
        IERC20Metadata(vaultTested.asset()).approve(address(vaultTested), 20);
        // owner deposits tokens when vault is open and receives vault shares
        vaultTested.deposit(20, user1.addr);
        // owner delegates shares balance to user
        IERC20Metadata(address(vaultTested)).approve(
            user2.addr,
            vaultTested.balanceOf(user1.addr)
        );
        vm.stopPrank();

        // vault is closed
        vm.prank(vaultTested.owner());
        vaultTested.close();

        // epoch = 1
        vm.startPrank(user2.addr);
        // user requests a redeem on behlaf of owner
        vaultTested.requestRedeem(
            vaultTested.balanceOf(user1.addr),
            user2.addr,
            user1.addr,
            ""
        );
        // user checks the pending redeem request amount
        assertEq(vaultTested.pendingRedeemRequest(user2.addr), 20);
        vm.stopPrank();

        vm.startPrank(vaultTested.owner());
        IERC20Metadata(vaultTested.asset()).approve(
            address(vaultTested),
            type(uint256).max
        );
        vaultTested.settle(23); // an epoch goes by
        vm.stopPrank();

        // epoch = 2

        vm.startPrank(user2.addr);
        // user tries to claim the redeem
        vaultTested.claimRedeem(user2.addr);
        assertEq(IERC20Metadata(vaultTested.asset()).balanceOf(user2.addr), 0);
        // however, token balance of user is still empty
        vm.stopPrank();

        vm.startPrank(user1.addr);
        // owner also tries to claim the redeem
        vaultTested.claimRedeem(user1.addr);
        assertEq(IERC20Metadata(vaultTested.asset()).balanceOf(user1.addr), 0);
        // however, token balance of owner is still empty
        vm.stopPrank();

        // all the balances of owner and user are zero, indicating loss of funds
        assertEq(vaultTested.balanceOf(user1.addr), 0);
        assertEq(IERC20Metadata(vaultTested.asset()).balanceOf(user1.addr), 0);
        assertEq(vaultTested.balanceOf(user2.addr), 0);
        assertEq(IERC20Metadata(vaultTested.asset()).balanceOf(user2.addr), 0);
    }
\u0060\u0060\u0060
To run the test : 
1. Copy the above code and paste it into \u0060TestClaimDeposit.t.sol\u0060
2. Run \u0060forge test --match-test test_poc --ffi\u0060

## Impact
The shares are locked in the vault forever with no method for recovery by the user or the \u0027owner\u0027. 

## Code Snippet

## Tool used

Manual Review
Foundry

## Recommendation
Modify [\u0060_createRedeemRequest\u0060](https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L721) as follows : 
\u0060\u0060\u0060diff
-        lastRedeemRequestId[owner] = epochId;
+       lastRedeemRequestid[receiver] = epochId;

\u0060\u0060\u0060

