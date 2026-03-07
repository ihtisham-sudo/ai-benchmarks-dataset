# turvec - Reentrancy in Vesting.sol:claim() will allow users to drain the contract due to executing .call() on user\u0027s address before setting s.index = uint128(i)

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Zap Protocol
**Keywords:** Reentrancy, Vesting.sol, claim(), cybersecurity, vulnerability, smart contract, Ethereum, call(), s.index, native pctAmount, attacker contract, already claimed, external call, bypass check, drain contract, manual review, reentrancy guard, security best practices, solidity, blockchain

---

turvec

high

# Reentrancy in Vesting.sol:claim() will allow users to drain the contract due to executing .call() on user\u0027s address before setting s.index = uint128(i)

## Summary
Reentrancy in Vesting.sol:claim() will allow users to drain the contract due to executing .call() on user\u0027s address before setting s.index = uint128(I)

## Vulnerability Detail
Here is the Vesting.sol:claim() function:
\u0060\u0060\u0060solidity
function claim() external {
        address sender = msg.sender;

        UserDetails storage s = userdetails[sender];
        require(s.userDeposit != 0, "No Deposit");
@>      require(s.index != vestingPoints.length, "already claimed");
        uint256 pctAmount;
        uint256 i = s.index;
        for (i; i <= vestingPoints.length - 1; i++) {
            if (block.timestamp >= vestingPoints[i][0]) {
                pctAmount += (s.userDeposit * vestingPoints[i][1]) / 10000;
            } else {
                break;
            }
        }
        if (pctAmount != 0) {
            if (address(token) == address(1)) {
@>              (bool sent, ) = payable(sender).call{value: pctAmount}("");
                require(sent, "Failed to send BNB to receiver");
            } else {
                token.safeTransfer(sender, pctAmount);
            }
@>          s.index = uint128(i);
            s.amountClaimed += pctAmount;
        }
    }
\u0060\u0060\u0060
From the above, You\u0027ll notice the claim() function checks if the caller already claimed by checking if the s.index has already been set to vestingPoints.length. You\u0027ll also notice the claim() function executes .call() and transfer the amount to the caller before setting the s.index = uint128(i), thereby allowing reentrancy.

Let\u0027s consider this sample scenario:
- An attacker contract(alice) has some native pctAmount to claim and calls \u0060claim()\u0060.
- "already claimed" check will pass since it\u0027s the first time she\u0027s calling \u0060claim()\u0060 so her s.index hasn\u0027t been set
- However before updating Alice s.index, the Vesting contract performs external .call() to Alice with the amount sent as well
- Alice reenters \u0060claim()\u0060 again on receive of the amount
- bypass index "already claimed" check since this hasn\u0027t been updated yet
- contract performs external .call() to Alice with the amount sent as well again,
- Same thing happens again
- Alice ends up draining the Vesting contract

## Impact
Reentrancy in Vesting.sol:claim() will allow users to drain the contract

## Code Snippet
https://github.com/sherlock-audit/2024-03-zap-protocol/blob/main/zap-contracts-labs/contracts/Vesting.sol#L84
https://github.com/sherlock-audit/2024-03-zap-protocol/blob/main/zap-contracts-labs/contracts/Vesting.sol#L89

## Tool used

Manual Review

## Recommendation
Here is the recommended fix:
\u0060\u0060\u0060diff
if (pctAmount != 0) {
+           s.index = uint128(i);
            if (address(token) == address(1)) {
                (bool sent, ) = payable(sender).call{value: pctAmount}("");
                require(sent, "Failed to send BNB to receiver");
            } else {
                token.safeTransfer(sender, pctAmount);
            }
-           s.index = uint128(i);
            s.amountClaimed += pctAmount;
        }
\u0060\u0060\u0060
I\u0027ll also recommend using reentrancyGuard.
