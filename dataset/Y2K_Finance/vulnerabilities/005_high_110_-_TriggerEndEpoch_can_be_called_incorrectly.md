# 110 - TriggerEndEpoch can be called incorrectly

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Y2K Finance
**Keywords:** triggerEndEpoch, triggerNullEpoch, epoch, vault, funds, loss, premium, collateral, assets, conditions, revert, manual, review, contract, safety, protocol, users, deposited, functionality, check, implementation

---

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/2)

**Found by:**  
0Kage, 0x52, 0xMojito, 0xPkhatri, 0xRobocop, 0xnirlin, AlexCzm, Aymen0909,  
Bauer, Ch_301, Dug, ElKu, Emmanuel, HonorLt, Junnon, Respx, TrungOre, VAD37,  
ast3ros, auditor0517, berndartmueller, bin2chen, cccz, charlesjhongc, ck,  
climber2002, csanuragjain, datapunk, evan, hickuphh3, holyhansss, iglyx, immeas,  
jasonxiale, joestakey, kenzo, libratus, ltyu, minhtrng, mstpr-brainbot, ne0n,  
pfapostol, roguereddwarf, shaka, sinarette, spyrosonic10, toshii, twicek, volodya,  
warRoom, yixxas, zeroknots

In the case where the owner has an existing rollover, the ownerToRollOverQueueIndex incorrectly updates to the last queue index. This causes the notRollingOver check to be performed on the incorrect _id, which then allows the depositor to withdraw funds that should\u0027ve been locked.

In \u0060enlistInRollover()\u0060, if the user has an existing rollover, it overwrites the existing data:
\u0060\u0060\u0060solidity
if (ownerToRollOverQueueIndex[_receiver] != 0) {
    // if so, update the queue
    uint256 index = getRolloverIndex(_receiver);
    rolloverQueue[index].assets = _assets;
    rolloverQueue[index].epochId = _epochId;
}
\u0060\u0060\u0060
However, regardless of whether the user has an existing rollover, the ownerToRolloverQueueIndex points to the last item in the queue:
\u0060\u0060\u0060solidity
ownerToRollOverQueueIndex[_receiver] = rolloverQueue.length;
\u0060\u0060\u0060
Thus, the notRollingOver modifier will check the incorrect item for users with existing rollovers:
\u0060\u0060\u0060solidity
QueueItem memory item = rolloverQueue[getRolloverIndex(_receiver)];
if (
    item.epochId == _epochId &&
\u0060\u0060\u0060
# AlreadyRollingOver
\u0060\u0060\u0060solidity
(balanceOf(_receiver, _epochId) - item.assets) < _assets
\u0060\u0060\u0060
Impact  
Users are able to withdraw assets that should\u0027ve been locked for rollovers.

CodeSnippet  
[Line 252-257](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L252-L257)  
[Line 268](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L268)  
[Line 755-760](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L755-L760)

Tool used  
Manual Review

Recommendation  
The \u0060ownerToRollOverQueueIndex\u0060 should be pointing to the last item in the queue in the else case only: when the user does not have an existing rollover queue item.
\u0060\u0060\u0060solidity
} else {
    // if not, add to queue
    rolloverQueue.push(
        QueueItem({
            assets: _assets,
            receiver: _receiver,
            epochId: _epochId
        })
    );
    + ownerToRollOverQueueIndex[_receiver] = rolloverQueue.length;
} 
- ownerToRollOverQueueIndex[_receiver] = rolloverQueue.length;
\u0060\u0060\u0060

Discussion  
3xHarry  
good catch  
3xHarry
## Fix PR
[https://github.com/Y2K-Finance/Earthquake/pull/128](https://github.com/Y2K-Finance/Earthquake/pull/128)

### Comments
IAm0x52  
Fix looks good. Assigning index has been moved inside else block
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/72)  
**Found by:** BPZ, Ch_301, Dug, Emmanuel, J4de, Ruhum, TrungOre, ast3ros, berndartmueller, bin2chen, evan, hickuphh3, immeas, jprod15, kenzo, ltyu, minhtrng, mstpr-brainbot, nobody2018, roguereddwarf, sinarette, spyrosonic10, toshii, twicek  

The current implementation enables users who are earlier in the queue to grief those who are later.

There is a rollover accounting mapping that, for every epoch, tracks the current index of the queue for which mints have been processed up to thus far. When a user delists from the queue, the last user enlisted will replace the delisted user\u0027s queue index. It is thus possible for the queue to be processed up to, or past, the delisted user\u0027s queue index, but before the last user has been processed, the processed user delists, thus causing the last user to not have his funds rollover.

1. Alice enlists into the queue (index 1), then Bob (index 2)
2. Alice (or a relayer) calls mintRollovers() with _operations = 1, and Alice has her funds rollover.
3. Alice delists from the rollover.

Bob is then unable to have his funds rollover until the next epoch is created, unless he delists and re-enlists into the queue (defeating the purpose of rollover functionality).

Whether accidental or deliberate, it is possible for users to not have their funds rollover.
[Carousel.sol](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol)

Manual Review

Instead of specifying the number of operations to execute, consider having start and end indexes, with a boolean mapping to track if a user\u0027s rollover has been processed.

3xHarry: Keeping track of rollovers with a mapping would increase gas cost substantially; however, it would be a better solution than blocking delisting during the deposit period.

3xHarry: Setting assets to 0 instead of removing the QueueItem from the array sounds like a more reasonable approach, given that it\u0027s very unlikely for the rollover queue array length to reach the max size. Also, there can be more markets with similar strike prices deployed at any time.

3xHarry: Fix PR: [#127](https://github.com/Y2K-Finance/Earthquake/pull/127)

0xRobocop: Escalate for 10 USDC. This is a valid low issue but not a high or medium. This is more of an inconvenience for the user and there is no loss: "User experience and design improvement issues: Issues that cause minor inconvenience to users where there is no material loss of funds are not considered valid. Funds are temporarily stuck and can be recovered by the administrator or owner. Also, if a submission is a design opinion/suggestion without any clear indications of loss of funds, it is not a valid issue."

There is also a little guideline to identify highs and mediums. Pay attention to "should not be easily replaced without loss of funds," which is not the case in this issue.
This is a valid low issue but not a high or med. This is more of an inconvenience for the user and there is no loss:

"User experience and design improvement issues: Issues that cause minor inconvenience to users where there is no material loss of funds are not considered valid. Funds are temporarily stuck and can be recovered by the administrator or owner. Also, if a submission is a design opinion/suggestion without any clear indications of loss of funds is not a valid issue."

There is also a little guideline to identify highs and meds. Pay attention to "should not be easily replaced without loss of funds" which is not the case in this issue.

You\u0027ve created a valid escalation for 10 USDC! To remove the escalation from consideration: Delete your comment. You may delete or edit your escalation comment anytime before the 48-hour escalation window closes. After that, the escalation becomes final.
## dmitriia
Not agree with the escalation, that\u0027s core logic flaw with a range of material impacts, definitely high.

### hrishibhat
Escalation rejected. Based on the issue and its duplicates and their impacts, considering this issue as a valid high since it breaks the core functionality.

### sherlock-admin
Escalation rejected. Based on the issue and its duplicates and their impacts, considering this issue as a valid high since it breaks the core functionality.

This issue\u0027s escalations have been rejected! Watsons who escalated this issue will have their escalation amount deducted from their next payout.

Needs additional changes. Using isEnlistedInRolloverQueue causes duplicate entries that can\u0027t be removed.
Fix looks good. \u0060isEnlistedInRolloverQueue\u0060 has been changed making it impossible to have duplicate entries.

jacksanford1

Note: 0x52\u0027s last message is in reference to this commit:  
https://github.com/Y2K-Finance/Earthquake/pull/127/commits/1d1ac0a3411208cc7a3a7d4668ff123bffb2ff21
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/75)  
**Found by:** 0xRobocop, Ace-30, AlexCzm, Ch_301, Dug, ElKu, Inspex, J4de, Respx, Ruhum, ShadowForce, TrungOre, VAD37, ast3ros, bulej93, evan, hickuphh3, iglyx, immeas, kenzo, minhtrng, roguereddwarf, toshii, yixxas  

The deposit fee can be circumvented by a queue deposit + mintDepositInQueue() call in the same transaction.

A deposit fee is charged and increases linearly within the deposit window. However, this fee can be avoided if one deposits into the queue instead, then mints his deposit in the queue.

Assume non-zero depositFee, valid epoch _id = 1. At epoch end, instead of calling \u0060deposit(1, _assets, 0xAlice)\u0060, Alice writes a contract that performs \u0060deposit(0, _assets, 0xAlice) + mintDepositInQueue(1, 1)\u0060 to mint her deposit in the same tx (her deposit gets processed first because FILO system). She pockets the relayerFee, essentially paying zero fees instead of incurring the depositFee.

Loss of protocol fee revenue.

- [Carousel.sol#L494-L500](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L494-L500)
- [Carousel.sol#L332-L333](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L332-L333)
- [Carousel.sol#L354](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Carousel/Carousel.sol#L354)

Manual Review
Because of the FILO system, charging the dynamic deposit fee will be unfair to queue deposits as they\u0027re reliant on relayers to mint their deposits for them. Consider taking a proportion of the relayer fee.

This is a valid issue. We will apply depositFee to all mints (queue and direct). However, given that queue has the potential to affect when users\u0027 shares are minted because of FILO, min deposit has to be raised for the queue, to make it substantially harder to DDoS the queue. Minimizing DDoS queue deposits will lead to queue deposits getting the least fees as relayers can mint from the first second the epoch is created.

fix PR: [https://github.com/Y2K-Finance/Earthquake/pull/126](https://github.com/Y2K-Finance/Earthquake/pull/126)

@IAm0x52 to elaborate on this issue: relayers are incentivized to mint the depositQueue from the second a new epoch is created to extract the most amount of relayerFees. In fact, Y2K will have a built-in relayerInfra into the deployment process. The assumption is that queueDeposit users will pay a minimal Fee. The attack factor of the queue being too long leading to prolonged queue deposit executions will be mitigated by adding a significant deposit requirement for queue deposits. These measures will mitigate high deposit Fees for Queue deposits as well as prevent late direct depositors using the queue to evade the depositFee.

Bringing in this discussion from Discord:
0x52
As a follow-up for PR126. You keep the minRequiredDeposit modifier on enlistInRollover but the way you modified it, it can only apply if epochId == 0 but enlistInRollover doesn\u0027t work for epochId == 0 so the modifier is useless on that function. My suggestion would be to either remove it if you no longer need that protection or make a new modifier specifically designed for enlistInRollover.

regarding [issue] 75 / PR 126 fixed in [https://github.com/Y2K-Finance/Earthquake/pull/126/commits/9c659161dc952df99201b99d4ea54e9dda642ecb](https://github.com/Y2K-Finance/Earthquake/pull/126/commits/9c659161dc952df99201b99d4ea54e9dda642ecb)
Fix looks good. \u0060enlistInRollover\u0060 now applies a minimum deposit requirement.
Source: [GitHub Issue #163](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/163)  
Found by: Ace-30, Inspex, TrungOre, VAD37, berndartmueller, bin2chen, carrot, cccz, charlesjhongc, evan, hickuphh3, iglyx, immeas, kenzo, minhtrng, mstpr-brainbot, nobody2018, roguereddwarf, toshii, warRoom  

When mintRollovers is called, when the function mints shares for the new epoch for the user, the amount of shares minted will be the same as the original assets he requested to rollover - not including the amount he won. After this, all these asset shares from the previous epoch are burnt. So the user won\u0027t be able to claim his winnings.  

When user requests to enlist in Rollover, he supplies the amount of assets to rollover, and this is saved in the queue.  
\u0060\u0060\u0060solidity
rolloverQueue[index].assets = _assets;
\u0060\u0060\u0060
When mintRollovers is called, the function checks if the user won the previous epoch, and proceeds to burn all the shares the user requested to roll:  
\u0060\u0060\u0060solidity
if (epochResolved[queue[index].epochId]) {
    uint256 entitledShares = previewWithdraw(
        queue[index].epochId,
        queue[index].assets
    );
    // mint only if user won epoch he is rolling over
    if (entitledShares > queue[index].assets) {
        ...
        // @note we know shares were locked up to this point
        _burn(
            queue[index].receiver,
            queue[index].epochId,
            queue[index].assets
        );
\u0060\u0060\u0060
Then, and this is the problem, the function mintstotheuserhisoriginalassets - assetsToMint - and not entitledShares.
\u0060\u0060\u0060solidity
uint256 assetsToMint = queue[index].assets - relayerFee;
_mintShares(queue[index].receiver, _epochId, assetsToMint);
\u0060\u0060\u0060
So the user has only rolled his original assets, but since all his share of them is burned, he will not be able anymore to claim his winnings from them. Note that if the user had called withdraw instead of rolling over, all his shares would be burned, but he would receive his entitledShares, and not just his original assets. We can see in this in withdraw. Note that _assets is burned (like in minting rollover) but entitledShares is sent (unlike minting rollover, which only remints _assets.)
\u0060\u0060\u0060solidity
_burn(_owner, _id, _assets);
_burnEmissions(_owner, _id, _assets);
uint256 entitledShares;
uint256 entitledEmissions = previewEmissionsWithdraw(_id, _assets);
if (epochNull[_id] == false) {
    entitledShares = previewWithdraw(_id, _assets);
} else {
    entitledShares = _assets;
}
if (entitledShares > 0) {
    SemiFungibleVault.asset.safeTransfer(_receiver, entitledShares);
}
if (entitledEmissions > 0) {
    emissionsToken.safeTransfer(_receiver, entitledEmissions);
}
\u0060\u0060\u0060

User will lose his rewards when rolling over.

\u0060\u0060\u0060solidity
if (epochResolved[queue[index].epochId]) {
    uint256 entitledShares = previewWithdraw(
        queue[index].epochId,
        queue[index].assets
    );
    // mint only if user won epoch he is rolling over
    if (entitledShares > queue[index].assets) {
        ...
        // @note we know shares were locked up to this point
        _burn(
\u0060\u0060\u0060
## Vulnerabilities

\u0060\u0060\u0060plaintext
queue[index].receiver,
queue[index].epochId,
queue[index].assets
\u0060\u0060\u0060

#### Toolused
ManualReview

#### Recommendation
Either remint the user his winnings also, or if you don\u0027t want to make him roll over the winnings, change the calculation so he can still withdraw his shares of the winnings.

#### Discussion
**3xHarry**  
this makes total sense! thx for catching this!  
**3xHarry**  
will have to calculate how much his original deposit is worth in entitledShares and rollover the specified amount  
**3xHarry**  
fix PR: https://github.com/Y2K-Finance/Earthquake/pull/125  
**IAm0x52**  
Needs additional changes. This will revert if diff is too high due to underflow in L412  
**IAm0x52**  
Fix looks good. Point of underflow has been removed in a subsequent PR  
**jacksanford1**  
Note: Subsequent PR 0x52 is referencing refers to this commit: https://github.com/Y2K-Finance/Earthquake/pull/125/commits/3732a7075348e87da612166dd060bfd8dd742ecb
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/468)

**Found by:** 0x52, 0xRobocop, Bauer, HonorLt, Respx, Ruhum, VAD37, bin2chen, immeas, joestakey, jprod15, libratus, ltyu, mstpr-brainbot, nobody2018, roguereddwarf, warRoom, yixxas
## Vulnerability Detail

**Carousel.sol**
\u0060\u0060\u0060solidity
function _mintShares(
    address to,
    uint256 id,
    uint256 amount
) internal {
    _mint(to, id, amount, EMPTY);
    _mintEmissions(to, id, amount);
}
\u0060\u0060\u0060
When processing deposits for the deposit queue, it calls \u0060_mintShares\u0060 to the specified receiver which makes a \u0060_mint\u0060 subcall.

**ERC1155.sol**
\u0060\u0060\u0060solidity
function _mint(address to, uint256 id, uint256 amount, bytes memory data) internal virtual {
    require(to != address(0), "ERC1155: mint to the zero address");
    address operator = _msgSender();
    uint256[] memory ids = _asSingletonArray(id);
    uint256[] memory amounts = _asSingletonArray(amount);
    _beforeTokenTransfer(operator, address(0), to, ids, amounts, data);
    _balances[id][to] += amount;
    emit TransferSingle(operator, address(0), to, id, amount);
    _afterTokenTransfer(operator, address(0), to, ids, amounts, data);
}
\u0060\u0060\u0060
The \u0060_doSafeTransferAcceptanceCheck(operator, address(0), to, id, amount, data);\u0060  
The \u0060baseERC1155_mint\u0060 is used which always behaves the same way that ERC721  
\u0060safeMint\u0060 does, that is, it always calls \u0060_doSafeTransferAcceptanceCheck\u0060 which  
makes a call to the receiver. A malicious user can make the receiver always revert.  
This breaks the deposit queue completely. Since deposits can\u0027t be canceled this  
WILL result in loss of funds to all users whose deposits are blocked. To make  
matters worse it uses first in last out so the attacker can trap all deposits before  
them.

Users who deposited before the adversary will lose their entire deposit.

Carousel.sol

Manual Review

Override \u0060_mint\u0060 to remove the \u0060safeMint\u0060 behavior so that users can\u0027t DOS the deposit queue.

3xHarry agrees with this issue, there is no easy solution to this, as by definition when  
depositing into the queue, the user gives up the atomicity of his intended mint.  
Looking at OpenZeppelin\u0027s 1155 implementation guide, it is recommended to ensure  
the receiver of the asset is able to call \u0060safeTransferFrom\u0060. By removing the  
acceptance check in the \u0060_mint\u0060 function, funds could be stuck in a smart contract.  
Another alternative would be to do the 1155 acceptance check in the mint function  
and confiscate the funds if the receiver is not able to hold 1155s. The funds could  
be retrieved via a manual process from the treasury afterward.  
3xHarry going with Recommendation is prob the easiest way.
## Fix PR: https://github.com/Y2K-Finance/Earthquake/pull/124  
IAm0x52  
Fix looks good. _mint no longer calls acceptance check so rollover can longer be DOS\u0027d by it
## Title
ControllerPeggedAssetV2: outdated price may be used which can lead to wrong depeg events

## Source
[GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/70)

## Found by
0xRobocop, 0xnirlin, ABA, Ch_301, Delvir0, Saeedalipoor01988, ShadowForce, TrungOre, ast3ros, bin2chen, carrot, evan, kaysoft, lemonmon, martin, minhtrng, p0wd3r, peanuts, roguereddwarf

The updatedAt timestamp in the price feed response is not checked. So outdated prices may be used.

The following checks are performed for the chainlink price feed:  
[Chainlink Price Feed Checks](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol#L299-L315)  
As you can see, the updatedAt timestamp is not checked. So the price may be outdated.

The price that is used by the Controller can be outdated. This means that a depeg event may be caused due to an outdated price which is incorrect. Only current prices must be used to check for a depeg event.

[Code Snippet](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol#L273-L318)

Manual Review

Introduce a reasonable limit for how old the price can be and revert if the price is older.
## Price Staleness Vulnerability
In the \u0060ControllerPeggedAssetV2\u0060 contract, there is a potential vulnerability related to price staleness. The following code changes have been made to address this issue:

\u0060\u0060\u0060solidity
if (updatedAt < block.timestamp - LIMIT) revert PriceOutdated();
\u0060\u0060\u0060

This check ensures that if the price data is older than a specified limit, the contract will revert, preventing the use of outdated price information.

- **3xHarry**: Considering this.
- **3xHarry**: Fix PR: [Link to PR](https://github.com/Y2K-Finance/Earthquake/pull/141)
- **IAm0x52**: Fix looks good. Controller will now revert if price is stale.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/108)

**Found by:** 0xRobocop, 0xnirlin, 0xvj, KingNFT, berndartmueller, bin2chen, charlesjhongc, climber2002, evan, holyhansss, kenzo, libratus, ltyu, minhtrng, roguereddwarf, warRoom, yixxas

An epoch can be resolved in three ways which correspond to the three functions available in the Controller: triggerDepeg, triggerEndEpoch, triggerNullEpoch. The issue is that triggerEndEpoch can be called even though triggerNullEpoch should be called. "Null epoch" means that any of the two vaults does not have funds deposited. In this case, the epoch should be resolved with triggerNullEpoch such that funds are not transferred from the premium vault to the collateral vault. So in triggerEndEpoch it should be checked whether the conditions for a null epoch apply. If that\u0027s the case, the triggerEndEpoch function should revert.

The assumption the code makes is that if the null epoch applies, triggerNullEpoch will be called before the end timestamp of the epoch which is when triggerEndEpoch can be called. This is not necessarily true. triggerNullEpoch might not be called in time (e.g. because the epoch duration is very short or simply nobody calls it) and then the triggerEndEpoch function can be called which sends the funds from the premium vault into the collateral vault: [Code Reference](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol#L172-L192). If the premium vault is the vault which has funds and the collateral vault does not, then the funds sent to the collateral vault are lost.

Loss of funds for users that have deposited into the premium vault.
[ControllerPeggedAssetV2.sol](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol#L144-L202)

Manual Review

\u0060triggerEndEpoch\u0060 should only be callable when the conditions for a null epoch don\u0027t apply:

\u0060\u0060\u0060diff
diff --git a/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol
✱✦ b/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol
index 0587c86..7b25cf3 100644
--- a/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol
+++ b/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol
@@ -155,6 +155,13 @@ contract ControllerPeggedAssetV2 {
                     collateralVault.epochExists(_epochId) == false
                 ) revert EpochNotExist();
+            if (
+                premiumVault.totalAssets(_epochId) == 0 ||
+                collateralVault.totalAssets(_epochId) == 0
+            ) {
+                revert VaultZeroTVL();
+            }
+
             (, uint40 epochEnd, ) = premiumVault.getEpochConfig(_epochId);
             if (block.timestamp <= uint256(epochEnd)) revert EpochNotExpired();
\u0060\u0060\u0060

**3xHarry**  
fix PR: [#140](https://github.com/Y2K-Finance/Earthquake/pull/140)

**IAm0x52**  
Fix looks good. \u0060triggerEndEpoch\u0060 can no longer be called on expired, null epochs.
**Source:** [GitHub Issue #110](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/110)  
**Found by:** Dug, Ruhum, bin2chen, nobody2018, roguereddwarf  

The Controller contract sends treasury funds to its own immutable treasury address instead of sending the funds to the one stored in the respective vault contract.

Each vault has a treasury address that is assigned on deployment which can also be updated through the factory contract:  
But, the Controller, responsible for sending the fees to the treasury, uses the immutable treasury address that it was initialized with:

It\u0027s not possible to have different treasury addresses for different vaults. It\u0027s also not possible to update the treasury address of a vault although it has a function to do that. Funds will always be sent to the address the Controller was initialized with.

- [VaultV2.sol Line 79](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/VaultV2.sol#L79)  
- [VaultV2.sol Lines 265-268](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/VaultV2.sol#L265-L268)  
- [ControllerPeggedAssetV2.sol Line 186](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol#L186)  
- [ControllerPeggedAssetV2.sol Line 40](https://github.com/sherlock-audit/2023-03-Y2K/blob/main/Earthquake/src/v2/Controllers/ControllerPeggedAssetV2.sol#L40)  

Manual Review
The Controller should query the Vault to get the correct treasury address, e.g.:
