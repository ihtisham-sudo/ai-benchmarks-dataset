# Bigsam - Wrong calculation of Accure Reward in Comptroller.sol

**Severity:** high
**Auditor:** Sherlock
**Protocol:** UnionFinance V2
**Keywords:** cybersecurity, vulnerability, Comptroller.sol, Accure Reward, globalTotalStaked, total staked, token frozen, reward calculation, frozen tokens, UserManager, gInflationIndex, batchUpdateFrozenInfo, manual review, protocol implementation, frozen assets, reward collection, smart contract, blockchain security, code review, security recommendation

---

Bigsam

High

# Wrong calculation of Accure Reward in Comptroller.sol

## Summary
Accure Reward calculates the global total staked before updating the total amount of token frozen hence, the globalTotalStaked used does not reflect the actual present globalTotalStaked value. Thus A user can claim the reward for recently frozen tokens due to this error. 

## Vulnerability Detail

Based on the calculation in Comptroller.sol and UserManager, 

function \u0027_accrueReward\u0027 calculates the TotalStaked but gets the value of newly frozen totals and increments the _totalfrozen.
This allows us to pass in a Larger amount of globalTotalStaked than we should at the current time, here the user benefits from this since the globalTotalStaked is used to get the amount(REWARD) and calculate the gInflationIndex.

\u0060\u0060\u0060solidity
 function _accrueRewards(address account, address token) private returns (uint256) {
        IUserManager userManager = _getUserManager(token);

@audit>>issue>>        // Lookup global state from UserManager
                                     uint256 globalTotalStaked = userManager.globalTotalStaked();

        // Lookup account state from UserManager
        UserManagerAccountState memory user = UserManagerAccountState(0, 0, false);
  @audit>>issue>>          (user.effectiveStaked, user.effectiveLocked, user.isMember) = userManager.onWithdrawRewards(account);

        uint256 amount = _calculateRewardsInternal(account, token, globalTotalStaked, user);

        // update the global states
        gInflationIndex = _getInflationIndexNew(globalTotalStaked, getTimestamp() - gLastUpdated);
        gLastUpdated = getTimestamp();
        users[account][token].inflationIndex = gInflationIndex;

        return amount;
    }
\u0060\u0060\u0060


For Reference, please look at the same implementation when it is called directly from Usermanager.sol in function \u0027batchUpdateFrozenInfo\u0027.

 

\u0060\u0060\u0060solidity
 function batchUpdateFrozenInfo(address[] calldata stakerList) external whenNotPaused {
        uint256 stakerLength = stakerList.length;
     ------------------------------------------------------------------------
   @audit >>   update is done first >>      (, , uint256 memberTotalFrozen) = _getEffectiveAmounts(staker);

            uint256 memberFrozenBefore = _memberFrozen[staker];
            if (memberFrozenBefore != memberTotalFrozen) {
                _memberFrozen[staker] = memberTotalFrozen;
     @audit >>  totalfrozen is obtained>>           tmpTotalFrozen = tmpTotalFrozen - memberFrozenBefore + memberTotalFrozen;
            }
        }
        _totalFrozen = tmpTotalFrozen;

            @audit >> totalstaked - the present totalfrozen>>      comptroller.updateTotalStaked(stakingToken, _totalStaked - _totalFrozen);
    }
\u0060\u0060\u0060

The present globalTotalStaked is correctly implement in another implementation (globalTotal = _totalStaked - _totalFrozen;)
\u0060\u0060\u0060solidity
 function updateTotalStaked(
        address token,
        uint256 totalStaked
    ) external override whenNotPaused onlyUserManager(token) returns (bool) {
        if (totalStaked > 0) {
            gInflationIndex = _getInflationIndexNew(totalStaked, getTimestamp() - gLastUpdated);
            gLastUpdated = getTimestamp();
        }

        return true;
    }
\u0060\u0060\u0060
From the second implementation by the protocol, it should be noted that globalTotalStaked should only be called after the _totalfrozen has been correctly updated and not before.

## Impact

Collection of Reward on newly frozen Tokens.

## Code Snippet

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/token/Comptroller.sol#L224

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/user/UserManager.sol#L1124-L1125

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/token/Comptroller.sol#L228

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/user/UserManager.sol#L1056

https://github.com/sherlock-audit/2024-06-union-finance-update-2/blob/main/union-v2-contracts/contracts/user/UserManager.sol#L1067

## Tool used

Manual Review

## Recommendation

Get \u0027globalTotalStaked\u0027 after calculating all frozen assets in the userManager for the user. 


\u0060\u0060\u0060solidity

      --  // Lookup global state from UserManager
      --  uint256 globalTotalStaked = userManager.globalTotalStaked();
        
         // Lookup account state from UserManager
        UserManagerAccountState memory user = UserManagerAccountState(0, 0, false);
        (user.effectiveStaked, user.effectiveLocked, user.isMember) = userManager.onWithdrawRewards(account);
      
  ++   // Lookup global state from UserManager
  ++  uint256 globalTotalStaked = userManager.globalTotalStaked();
\u0060\u0060\u0060
