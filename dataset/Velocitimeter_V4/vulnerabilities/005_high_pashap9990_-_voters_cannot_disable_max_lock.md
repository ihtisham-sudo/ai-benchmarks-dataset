# pashap9990 - voters cannot disable max lock

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cybersecurity, vulnerability, maxLock, voting power, voters, disable maxLock, VotingEscrow, assets, lockEnd, withdraw, nft, PoC, manual review, impact, max_locked_nfts, maxLockIdToIndex, lock assets, decrease voting power, security flaw, smart contract

---

pashap9990

High

# voters cannot disable max lock

## Summary
Voters can enable maxLock and this causes their voting power wouldn\u0027t decrease but they cannot disable maxLock

## Vulnerability Detail
**Textual PoC:**
Let\u0027s assume three voters lock their assets in ve,hence three nfts will be minted[1,2,3] and after that they [enable maxLock](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L883)

**Initial values**
max_locked_nfts corresponding values:



| index 0 | index 1 | index 2 |
| -------- | -------- | -------- |
| 1     | 2     | 3     |

maxLockIdToIndex corresponding values:

| index 1 | index 2 | index 3 |
| -------- | -------- | -------- |
| 1     | 2     | 3     |
 
 when owner of nft 3 want to disable maxLock he has to call \u0060VotingEscrow::disable_max_lock\u0060  in result :
**variable\u0027s values from line 897 til 901:**
* index = 2
* maxLockIdToIndex[3] = 0
* max_locked_nfts[2] = 3

max_locked_nfts corresponding values:



| index 0 | index 1 | index 2 |
| -------- | -------- | -------- |
| 1     | 2     | 3     |

maxLockIdToIndex corresponding values:

| index 1 | index 2 | index 3 |
| -------- | -------- | -------- |
| 1     | 2     | 0     |

finally
* maxLockIdToIndex[max_locked_nfts[2]] => maxLockIdToIndex[3] = 2 + 1
* last element of max_locked_nfts will be deleted

**Coded PoC:**

\u0060\u0060\u0060solidity
    function testEnableAndDisableMaxLock() external {
        flowDaiPair.approve(address(escrow), TOKEN_1);
        uint256 lockDuration = 7 * 24 * 3600; // 1 week
        escrow.create_lock(400, lockDuration);
        escrow.create_lock(400, lockDuration);
        escrow.create_lock(400, lockDuration);

        assertEq(escrow.currentTokenId(), 3);
        escrow.enable_max_lock(1);
        escrow.enable_max_lock(2);
        escrow.enable_max_lock(3);


        assertEq(escrow.maxLockIdToIndex(1), 1);
        assertEq(escrow.maxLockIdToIndex(2), 2);
        assertEq(escrow.maxLockIdToIndex(3), 3);

        assertEq(escrow.max_locked_nfts(0), 1);
        assertEq(escrow.max_locked_nfts(1), 2);
        assertEq(escrow.max_locked_nfts(2), 3);

        escrow.disable_max_lock(3);

        assertEq(escrow.maxLockIdToIndex(1), 1);
        assertEq(escrow.maxLockIdToIndex(2), 2);
        assertEq(escrow.maxLockIdToIndex(3), 3);//mockLockIdToIndex has to be zero 

        assertEq(escrow.max_locked_nfts(0), 1);
        assertEq(escrow.max_locked_nfts(1), 2);
    }
\u0060\u0060\u0060



## Impact
Voters cannot withdraw their assets from ve because every time they call \u0060VotingEscrow::withdraw\u0060 their lockEnd will be decrease

## Code Snippet
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L904

## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060diff
    function disable_max_lock(uint _tokenId) external {
        assert(_isApprovedOrOwner(msg.sender, _tokenId));
        require(maxLockIdToIndex[_tokenId] != 0,"disabled");

        uint index =  maxLockIdToIndex[_tokenId] - 1;
        maxLockIdToIndex[_tokenId] = 0;

         // Move the last element into the place to delete
        max_locked_nfts[index] = max_locked_nfts[max_locked_nfts.length - 1];

+         if (index != max_locked_nfts.length - 1) {
+             uint lastTokenId = max_locked_nfts[max_locked_nfts.length - 1];
+             max_locked_nfts[index] = lastTokenId;
+             maxLockIdToIndex[lastTokenId] = index + 1;
+         }
        
+         maxLockIdToIndex[max_locked_nfts[index]] = 0;
        

-       maxLockIdToIndex[max_locked_nfts[index]] = index + 1;//@audit maxLockIdToIndex computes wrongly when lps want to disable last element in array
        
        // Remove the last element
        max_locked_nfts.pop();
    }
\u0060\u0060\u0060


