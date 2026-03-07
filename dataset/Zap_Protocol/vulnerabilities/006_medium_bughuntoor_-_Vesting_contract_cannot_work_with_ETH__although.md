# bughuntoor - Vesting contract cannot work with ETH, although it\u0027s supposed to.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zap Protocol
**Keywords:** cybersecurity, vulnerability, vesting contract, ETH, native token, claim function, token transfer, updateUserDeposit, safeTransferFrom, contract operation, revert, unusable contract, manual review, impact assessment, smart contract, blockchain security, token address, function call, security recommendation, code review

---

bughuntoor

medium

# Vesting contract cannot work with ETH, although it\u0027s supposed to.

## Summary
Vesting contract cannot work with native token, although it\u0027s supposed to. 

## Vulnerability Detail
Within the claim function, we can see that if \u0060token\u0060  is set to address(1), the contract should operate with ETH
\u0060\u0060\u0060solidity
    function claim() external {
        address sender = msg.sender;

        UserDetails storage s = userdetails[sender];
        require(s.userDeposit != 0, "No Deposit");
        require(s.index != vestingPoints.length, "already claimed");
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
                (bool sent, ) = payable(sender).call{value: pctAmount}("");  // @audit - here
                require(sent, "Failed to send BNB to receiver");
            } else {
                token.safeTransfer(sender, pctAmount);
            }
            s.index = uint128(i);
            s.amountClaimed += pctAmount;
        }
    }
\u0060\u0060\u0060

However, it is actually impossible for the contract to operate with ETH, since \u0060updateUserDeposit\u0060 always attempts to do a token transfer. 
\u0060\u0060\u0060solidity
    function updateUserDeposit(
        address[] memory _users,
        uint256[] memory _amount
    ) public onlyRole(DEFAULT_ADMIN_ROLE) {
        require(_users.length <= 250, "array length should be less than 250");
        require(_users.length == _amount.length, "array length should match");
        uint256 amount;
        for (uint256 i = 0; i < _users.length; i++) {
            userdetails[_users[i]].userDeposit = _amount[i];
            amount += _amount[i];
        }
        token.safeTransferFrom(distributionWallet, address(this), amount); // @audit - this will revert
    }
\u0060\u0060\u0060

Since when the contract is supposed to work with ETH, token is set to address(1), calling \u0060safeTransferFrom\u0060 on that address will always revert, thus making it impossible to call this function.

## Impact
Vesting contract is unusable with ETH

## Code Snippet
https://github.com/sherlock-audit/2024-03-zap-protocol/blob/main/zap-contracts-labs/contracts/Vesting.sol#L64

## Tool used

Manual Review

## Recommendation
make the following check 
\u0060\u0060\u0060solidity
        if (address(token) != address(1)) token.safeTransferFrom(distributionWallet, address(this), amount);
\u0060\u0060\u0060


