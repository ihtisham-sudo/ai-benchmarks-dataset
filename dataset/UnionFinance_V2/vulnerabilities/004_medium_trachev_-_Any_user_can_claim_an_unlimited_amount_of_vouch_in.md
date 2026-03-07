# trachev - Any user can claim an unlimited amount of vouch in \u0060VouchFaucet.sol\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** cybersecurity, vulnerability, smart contract, VouchFaucet, claimVouch, validation, untrusted user, malicious borrow, stake theft, TRUST_AMOUNT, contract funds, risk, manual review, security recommendation, user approval, trust management, exploit, bypass, access control, Ethereum

---

trachev

High

# Any user can claim an unlimited amount of vouch in \u0060VouchFaucet.sol\u0060

## Summary
Currently, there is no validation performed in \u0060VouchFaucet.sol\u0060 when \u0060claimVouch\u0060 is called. This is highly dangerous as any untrusted user can increase their vouch and perform malicious borrows, stealing from the contract\u0027s stake.

## Vulnerability Detail
As we can see in the \u0060claimVouch\u0060 function there is no validation performed and it can be called by any address:
\u0060\u0060\u0060solidity
function claimVouch() external {
        IUserManager(USER_MANAGER).updateTrust(msg.sender, uint96(TRUST_AMOUNT));
        emit VouchClaimed(msg.sender);
}
\u0060\u0060\u0060

In addition to that, the maximum amount of trust that any user can claim - \u0060TRUST_AMOUNT\u0060 can easily be bypassed by calling \u0060claimVouch\u0060, borrowing the entire \u0060TRUST_AMOUNT\u0060 and after that calling \u0060claimVouch\u0060 again.

## Impact
Malicious borrows can be made by untrusted users and the maximum amount that can be vouched for a user can be bypassed, putting the contract\u0027s funds at risk of being stolen.

## Code Snippet
https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/7ffe43f68a1b8e8de1dfd9de5a4d89c90fd6f710/union-v2-contracts/contracts/peripheral/VouchFaucet.sol#L87-L90

## Tool used

Manual Review

## Recommendation
Only users approved by the owner should be able to call \u0060claimVouch\u0060 and they should not be able to claim more trust than \u0060TRUST_AMOUNT\u0060.
