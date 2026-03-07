# 2 - Mock Sidechain CVX Rewards

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** mock contract, sidechain, cvxToken, rewardsClaimed, rewardRedirect, transfer, balance, msg.sender, external function, require, mapping, address, recipient, constructor, IERC20, smart contract, vulnerability, exploit, funds, transfer failure

---

# 1. Vulnerable Reward Distribution
\u0060\u0060\u0060solidity
function getReward() external {
    require(!rewardsClaimed, "Rewards already claimed");
    // Send fixed reward amount
    cvxToken.transfer(msg.sender, 100e18);
    rewardsClaimed = true;
}
\u0060\u0060\u0060

### 2. Mock Sidechain CVX Rewards
\u0060\u0060\u0060solidity
contract MockSidechainCVXRewards {
    IERC20 public cvxToken;
    mapping(address => address) public rewardRedirect;
    bool public rewardsClaimed;

    constructor(IERC20 _cvxToken) {
        cvxToken = _cvxToken;
    }

    function getReward(address account, address forwardTo) external {
        require(!rewardsClaimed, "Rewards already claimed");
        address recipient = rewardRedirect[account] != address(0) ? rewardRedirect[account] : forwardTo;
        // Transfer all rewards and mark as claimed
        uint256 balance = cvxToken.balanceOf(address(this));
        cvxToken.transfer(recipient, balance);
        rewardsClaimed = true;
    }

    function setRewardRedirect(address _to) external {
        rewardRedirect[msg.sender] = _to;
    }
}
\u0060\u0060\u0060

### 3. Mock Convex Deposit Token (vulnerable version)
\u0060\u0060\u0060solidity
contract MockConvexDepositToken {
    address public cvxRewards;
    IERC20 public cvxToken;

    constructor(address _cvxRewards, IERC20 _cvxToken) {
        cvxRewards = _cvxRewards;
        cvxToken = _cvxToken;
    }

    function fetchRewards() external {
        // Vulnerable implementation that doesn\u0027t handle sidechains properly
        if (block.chainid == 1) {
            MockMainnetCVXRewards(cvxRewards).getReward();
        } else {
            // This will fail or be vulnerable on sidechains
            MockSidechainCVXRewards(cvxRewards).getReward(address(this), address(this));
        }
    }
}
\u0060\u0060\u0060

Follow the docs and implement the code accordingly so that on sidechains it\u0027s not vulnerable.

### 4. Users can continue voting for inactive pools through registerVoteWeight()
Submitted by 0xDjango, also found by T1MOH and Ghost  
Severity: Medium Risk  
Context: (No context files were provided by the reviewer)  
Summary: Users can vote for receivers that have been marked as inactive if they have previously voted for this receiver. Users have a few ways to vote in IncentiveVoting.sol. They can call:
- \u0060registerAccountWeightAndVote()\u0060 → Grabs user\u0027s current voting weight from TokenLocker.sol and registers the weights for the receivers, then stores the user\u0027s vote points.
- \u0060vote()\u0060 → Votes using user\u0027s current registered voting weights.
## Description
The \u0060registerAccountWeight()\u0060 function grabs the user\u0027s current voting weight from \u0060TokenLocker.sol\u0060 and registers the weights for the receivers. Both \u0060registerAccountWeightAndVote()\u0060 and \u0060vote()\u0060 check that the receiver of the voting power is an active receiver; however, this is not the case for \u0060registerAccountWeight()\u0060. Because of this, users can continue voting for inactive receivers.

## Finding Description
\u0060IncentiveVoting.sol\u0060 contains safeguards to ensure that users cannot vote for inactive receivers in \u0060_storeAccountVotes()\u0060:

\u0060\u0060\u0060solidity
function _storeAccountVotes(
  address account,
  AccountData storage accountData,
  Vote[] calldata votes,
  uint256 points,
  uint256 offset
) internal {
  // ...
  for (uint256 i; i < votes.length; i++) {
    // prevent voting for disabled receivers
    require(
      IBimaVault(vault).isReceiverActive(votes[i].id),
      "Can\u0027t vote for disabled receivers - clearVote first"
    );
  // ...
}
\u0060\u0060\u0060

However, this function is not called when a user calls \u0060registerVoteWeight()\u0060 as it does not call \u0060_storeAccountVotes()\u0060:

\u0060\u0060\u0060solidity
function registerAccountWeight(address account, uint256 minWeeks) external callerOrDelegated(account) {
  // get storage reference to account\u0027s lock data
  AccountData storage accountData = accountLockData[account];
  Vote[] memory existingVotes;
  // if account has an active vote, clear the recorded vote
  // weights prior to updating the registered account weights
  if (accountData.voteLength > 0) {
    existingVotes = getAccountCurrentVotes(account);
    _removeVoteWeights(account, existingVotes, accountData.frozenWeight);
    emit ClearedVotes(account, getWeek());
  }
  // get updated account lock weights and store locally
  uint256 frozenWeight = _registerAccountWeight(account, minWeeks);
  // resubmit the account\u0027s active vote using the newly registered weights
  _addVoteWeights(account, existingVotes, frozenWeight);
  // do not call \u0060_storeAccountVotes\u0060 because the vote is unchanged
}
\u0060\u0060\u0060

## Impact Explanation
Users may continue voting for inactive receivers if they are switched to inactive after a user has already voted for them.

Example output indicating the extension of receiver weight from week 10 to 15 simply by calling \u0060registerVoteWeight()\u0060.
## Weight Analysis

Start Week: 0  
Weight at Week 0: 10737418230  
Weight at Week 1: 9663676407  
Weight at Week 2: 8589934584  
Weight at Week 3: 7516192761  
Weight at Week 4: 6442450938  
Weight at Week 5: 5368709115  
Weight at Week 6: 4294967292  
Weight at Week 7: 3221225469  
Weight at Week 8: 2147483646  
Weight at Week 9: 1073741823  
Weight at Week 10: 0  
Weight at Week 0: 10737418230  
Weight at Week 1: 9663676407  
Weight at Week 2: 8589934584  
Weight at Week 3: 7516192761  
Weight at Week 4: 6442450938  
Weight at Week 5: 10737418230  
Weight at Week 6: 9663676407  
Weight at Week 7: 8589934584  
Weight at Week 8: 7516192761  
Weight at Week 9: 6442450938  
Weight at Week 10: 5368709115  
Weight at Week 11: 4294967292  
Weight at Week 12: 3221225469  
Weight at Week 13: 2147483646  
Weight at Week 14: 1073741823  
Weight at Week 15: 0  

## Code Additions

### Addthis helper function to testSetup.sol:
\u0060\u0060\u0060solidity
function _lockMoreTokens(
    uint256 amount
) internal returns (uint256 initialUnallocated) {
    // receiver locks up their tokens to get voting weight
    vm.prank(users.user1);
    tokenLocker.lock(users.user1, amount / INIT_LOCK_TO_TOKEN_RATIO, 10);
    // verify receiver balance after lock; calculated this way because of how
    // lock amount gets scaled down by INIT_LOCK_TO_TOKEN_RATIO then for token
    // transfer scales it up by INIT_LOCK_TO_TOKEN_RATIO
    uint256 users1TokensAfterLock = amount -
        (amount / INIT_LOCK_TO_TOKEN_RATIO) *
        INIT_LOCK_TO_TOKEN_RATIO;
    // assertEq(bimaToken.balanceOf(users.user1), users1TokensAfterLock);
}
\u0060\u0060\u0060

### Addthis test case to vaultTest.sol:
\u0060\u0060\u0060solidity
function test_UserCanKeepVotingForInactiveReceiver() external {
    // setup vault giving user1 half supply to lock for voting power
    uint256 initialUnallocated = _vaultSetupAndLockTokens(INIT_BAB_TKN_TOTAL_SUPPLY / 2, true);
    uint16 startWeek = SafeCast.toUint16(bimaVault.getWeek());
    console.log("Start Week: %s", startWeek);
    // helper registers receivers and performs all necessary checks
    uint256 RECEIVER_ID = incentiveVoting.receiverCount();
    vm.prank(users.owner);
    bimaVault.registerReceiver(mockEmissionReceiverAddr, 1);
    // User votes for receiver
    IIncentiveVoting.Vote[] memory votes = new IIncentiveVoting.Vote[](1);
    votes[0].id = RECEIVER_ID;
    votes[0].points = incentiveVoting.MAX_POINTS();
    vm.prank(users.user1);
    incentiveVoting.registerAccountWeightAndVote(users.user1, 10, votes);
    for (uint16 week = startWeek; week <= startWeek + 10; week++) {
        uint256 receiverWeight = incentiveVoting.getReceiverWeightAt(RECEIVER_ID, week);
        console.log("Weight at Week %s: %s", week, receiverWeight);
    }
    console.log();
}
\u0060\u0060\u0060
