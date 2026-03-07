# 422 - Zero Shares Minting Issue

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Y2K Finance
**Keywords:** rollover, shares, TVL, mint, revert, division, zero, assets, relayer fee, queue, epoch, withdraw, burn, function, user, deposit, emissions, transfer, contract, error

---

# Relayer Fee and Asset Conversion

The relayer fee is converted into the amount of shares of the previous epoch (the epoch users want to rollover collateral from):

\u0060\u0060\u0060solidity
uint256 assetsToMint = queue[index].assets - relayerFeeInShares;
\u0060\u0060\u0060

Assets represent shares in the previous epoch, and the arithmetic operation is done in the same denominator (shares in \u0060queue[index].epochId\u0060).

0x52: Shares and assets are 1:1 for the open epoch, correct? 

So imagine this scenario: You deposit 100 assets into epoch 1 to get 100 shares in epoch 1. Now you queue them into the rollover. Epoch 1 ends with a profit of 25%, which means your 100 shares are now worth 125. 80 shares are burned (worth 100 assets), leaving the user with 20 shares for epoch 1. 

If the relayer fee is 10, then it will be converted to 8 shares of epoch 2. But epoch 2 is still 1:1 with assets, so it\u0027s only taking 8 assets from the user but sending them 10 assets as the relayer fee. So you either need to reduce epoch 1 shares by 8 (i.e., leave the user with 12 shares) or you need to reduce \u0060assetsToMint\u0060 by the relayer fee directly (i.e., only mint 90 to epoch 2).

jacksanford1: Bringing in some discussion from Y2K\u0027s repo:

3xHarry: 

@IAm0x52 thanks for noticing the relayer Fee In Shares bug. I will close this PR, but the fix can be observed in 9165674. 

[Link to PR](https://github.com/Y2K-Finance/Earthquake/pull/136#issuecomment-1541996529)

IAm0x52: Fix looks good. Fee is no longer converted since the epoch in which the fee is removed is always 1:1.
**Source:** [GitHub Issue #337](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/337)  
**Found by:** ast3ros

The VaultFactoryV2 contract is supposed to use a timelock contract with a delay period when changing its owner. However, there is a loophole that allows the owner to change the owner address instantly, without waiting for the delay period to expire. This defeats the purpose of the timelock contract and exposes the VaultFactoryV2 contract to potential abuse.

In project description, timelock is required when making critical changes. Admin can only configure new markets and epochs on those markets. 

1) Admin can configure new markets and epochs on those markets. Timelock can make critical changes like changing the oracle or whitelisting controllers.

The VaultFactoryV2 contract has a \u0060changeOwner\u0060 function that is supposed to be called only by the timelock contract with a delay period.

\u0060\u0060\u0060solidity
function changeOwner(address _owner) public onlyTimeLocker {
    if (_owner == address(0)) revert AddressZero();
    _transferOwnership(_owner);
}
\u0060\u0060\u0060

The VaultFactoryV2 contract inherits from the Openzeppelin Ownable contract, which has a \u0060transferOwnership\u0060 function that allows the owner to change the owner address immediately. However, the \u0060transferOwnership\u0060 function is not overridden by the \u0060changeOwner\u0060 function, which creates a conflict and a vulnerability. The owner can bypass the timelock delay and use the \u0060transferOwnership\u0060 function to change the owner address instantly.

\u0060\u0060\u0060solidity
function transferOwnership(address newOwner) public virtual onlyOwner {
    require(newOwner != address(0), "Ownable: new owner is the zero address");
    _transferOwnership(newOwner);
}
\u0060\u0060\u0060
The \u0060transferOwnership\u0060 is not working as designed (using timelock); the timelock delay becomes useless. This means that if the owner address is hacked or corrupted, the attacker can take over the contract immediately, leaving no time for the protocol and the user to respond or intervene.

\u0060\u0060\u0060solidity
// Code snippet from the contract
\u0060\u0060\u0060

Manual Review

Override the \u0060transferOwnership\u0060 function and add modifier \u0060onlyTimeLocker\u0060.

**thangtranth**  
Escalate for 10 USDC.  
This issue is different from #501 and cannot be ignored. It is not related to using two steps to change ownership. The problem here is that the \u0060transferOwnership\u0060 function in the Ownable contract is not overridden as it should be. This allows the owner to change the ownership without going through the timelock. This creates a severe security risk and undermines the trust and transparency of the protocol as stated in spec.

**sherlock-admin**  
Escalate for 10 USDC.  
This issue is different from #501 and cannot be ignored. It is not related to using two steps to change ownership. The problem here is that the \u0060transferOwnership\u0060 function in the Ownable contract is not overridden as it should be. This allows the owner to change the ownership without going through the timelock. This creates a severe security risk and undermines the trust and transparency of the protocol as stated in spec.
You\u0027ve created a valid escalation for 10 USDC!  
To remove the escalation from consideration: Delete your comment.  
You may delete or edit your escalation comment anytime before the 48-hour escalation window closes. After that, the escalation becomes final.
## Escalation Comments

**hrishibhat**  
Escalation accepted  
Not a duplicate of #501 and can be considered a valid medium since this identifies the issue that \u0060transferOwnership\u0060 is not overridden and needs to have ‘onlyTimeLocker\u0027 modifier.

**sherlock-admin**  
Escalation accepted  
Not a duplicate of #501 and can be considered a valid medium since this identifies the issue that \u0060transferOwnership\u0060 is not overridden and needs to have ‘onlyTimeLocker\u0027 modifier.

This issue\u0027s escalations have been accepted!  
Contestants\u0027 payouts and scores will be updated according to the changes made on this issue.

### Lead Judge Comment

**hrishibhat**  
Looks valid, maybe medium. If they intend to do it without a delay is one thing and to be documented, but if a function is just left not overridden it\u0027s a bug.

### Sponsor Comment

Actually, that\u0027s a valid issue. Fixing this will make this action more complicated. My thinking is to add a direct function on \u0060timelocker\u0060 which lets \u0060timelocker\u0060 execute the owner (deployer) change without a 7-day queue.

**3xHarry**  
FIX RP: [https://github.com/Y2K-Finance/Earthquake/pull/147](https://github.com/Y2K-Finance/Earthquake/pull/147) - last two commits

**IAm0x52**  
Fix looks good. \u0060changeOwner\u0060 has been removed and \u0060transferOwnership\u0060 has been overridden to allow only \u0060timelocker\u0060.
**Source:** [GitHub Issue #418](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/418)  
**Found by:** berndartmueller, evan, kenzo  

If the deposited assets for a queued rollover item are equal to the relayer fee, the rollover will be minted with 0 shares, potentially leading to zero TVL and hence \u0060finalTVL[_id] = 0\u0060. This will cause the \u0060previewWithdraw\u0060 call to revert due to division by zero and the rollover queue will be stuck forever.

Minting rollovers in the carousel vault iterates over all items in the \u0060rolloverQueue\u0060. Each item is processed, and the entitled shares (\u0060entitledShares\u0060) are calculated using \u0060previewWithdraw\u0060. If the entitled shares are greater than the deposited assets, the rollover is minted. However, if the deposited assets for the queued item are equal to the relayer fee, the assets to mint (\u0060assetsToMint\u0060) calculated will be 0. If this happens to be the only deposit (mint) for the epoch and the vault\u0027s TVL remains zero, the \u0060previewWithdraw\u0060 call will revert due to division by zero.

Once there is a rollover minted with 0 shares for an epoch and the vault\u0027s TVL (i.e., \u0060finalTVL\u0060) remains zero, the rollover queue will be stuck forever unless the owner of this queue item delists it.

\u0060\u0060\u0060solidity
function mintRollovers(uint256 _epochId, uint256 _operations)
 external
 epochIdExists(_epochId)
 epochHasNotStarted(_epochId)
 nonReentrant
{
    ...   // [...]
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
while ((index - prevIndex) < (_operations)) {
    // only roll over if last epoch is resolved
    if (epochResolved[queue[index].epochId]) {
        uint256 entitledShares = previewWithdraw( // @audit-info
            // reverts if epoch\u0027s \u0060finalTVL\u0060 == 0
            queue[index].epochId,
            queue[index].assets
        );
        // mint only if user won epoch he is rolling over
        if (entitledShares > queue[index].assets) {
            // skip the rollover for the user if the assets cannot
            // cover the relayer fee instead of revert.
            if (queue[index].assets < relayerFee) {
                index++;
                continue;
            }
            // @note we know shares were locked up to this point
            _burn(
                queue[index].receiver,
                queue[index].epochId,
                queue[index].assets
            );
            // transfer emission tokens out of contract otherwise user
            // could not access them as vault shares are burned
            _burnEmissions(
                queue[index].receiver,
                queue[index].epochId,
                queue[index].assets
            );
            // @note emission token is a known token which has no
            // before transfer hooks which makes transfer safer
            emissionsToken.safeTransfer(
                queue[index].receiver,
                previewEmissionsWithdraw(
                    queue[index].epochId,
                    queue[index].assets
                )
            );

            emit Withdraw(
                msg.sender,
                queue[index].receiver,
                queue[index].receiver,
                _epochId,
                queue[index].assets,
                entitledShares
            );
\u0060\u0060\u0060
## \u0060assetsToMint\u0060 can potentially become 0
\u0060\u0060\u0060solidity
uint256 assetsToMint = queue[index].assets - relayerFee; //
_mintShares(queue[index].receiver, _epochId, assetsToMint);
emit Deposit(
    msg.sender,
    queue[index].receiver,
    _epochId,
    assetsToMint
);
rolloverQueue[index].assets = assetsToMint;
rolloverQueue[index].epochId = _epochId;
// only pay relayer for successful mints
executions++;
\u0060\u0060\u0060
## Entitled Amount Calculation
\u0060\u0060\u0060solidity
function previewWithdraw(uint256 _id, uint256 _assets)
    public
    view
    override(SemiFungibleVault)
    returns (uint256 entitledAmount)
{
    // entitledAmount amount is derived from the claimTVL and the finalTVL
    // if user deposited 1000 assets and the claimTVL is 50% lower than
    // finalTVL, the user is entitled to 500 assets
    // if user deposited 1000 assets and the claimTVL is 50% higher than
    // finalTVL, the user is entitled to 1500 assets
    entitledAmount = _assets.mulDivDown(claimTVL[_id], finalTVL[_id]);
}
\u0060\u0060\u0060

Consider checking the total assets of the epoch queue[index].epochId to be greater than 0 before calling previewWithdraw in line 396.
3xHarry will move check from line 403 up before previewWithdraw, also considering implementing rollover delisting if assetsToMint is less than relayerFee.

3xHarry in general delisting of stale rollovers (not enough to pay for relayer, or not won prev epoch) should be delisted by smart contract.

3xHarry fix PR: [https://github.com/Y2K-Finance/Earthquake/pull/133](https://github.com/Y2K-Finance/Earthquake/pull/133)

IAm0x52 Needs additional changes. This still doesn\u0027t address the issue of minting 0 because if assets == relayerFee then it will still mint 0. Should instead be:
\u0060\u0060\u0060javascript
if (queue[index].assets <= relayerFee) {
\u0060\u0060\u0060

IAm0x52 Fix looks good. Suggested change above has been added.

jacksanford1 Note: 0x52 referenced this commit in their second message from PR #133: [https://github.com/Y2K-Finance/Earthquake/pull/133/commits/9edaa8a5da96edf7c61bef4a8847f7c107f2b630](https://github.com/Y2K-Finance/Earthquake/pull/133/commits/9edaa8a5da96edf7c61bef4a8847f7c107f2b630)
**Source:** [GitHub](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/422)  
**Found by:** Dug, Respx, ShadowForce, berndartmueller, holyhansss, libratus, ltyu, spyrosonic10

A depeg event cannot be triggered if the Arbitrum sequencer went down before the epoch ends and remains down beyond the epoch expiry. Instead, the collateral vault users can unfairly end the epoch without a depeg and claim the premium payments.

A depeg event can be triggered during an ongoing epoch by calling the \u0060ControllerPeggedAssetV2.triggerDepeg\u0060 function. This function retrieves the latest price of the pegged asset via the \u0060getLatestPrice\u0060 function. If the Arbitrum sequencer is down or the grace period has not passed after the sequencer is back up, the \u0060getLatestPrice\u0060 function reverts and the depeg event cannot be triggered.

In case the sequencer went down before the epoch expired and remained down well after the epoch expired, a depeg cannot be triggered, and instead, the epoch can be incorrectly ended without a depeg by calling the \u0060ControllerPeggedAssetV2.triggerEndEpoch\u0060 function. Incorrectly, because at the time of the epoch expiry, it was not possible to trigger a depeg and hence it would be unfair to end the epoch without a depeg.

A depeg event cannot be triggered, and premium vault users lose out on their insurance payout, while collateral vault users can wrongfully end the epoch and claim the premium.

\u0060\u0060\u0060solidity
v2/Controllers/ControllerPeggedAssetV2.sol - triggerDepeg()
function triggerDepeg(uint256 _marketId, uint256 _epochId) public {
 address[2] memory vaults = vaultFactory.getVaults(_marketId);
\u0060\u0060\u0060
## Vulnerabilities

### Vulnerability 1
\u0060\u0060\u0060solidity
if (vaults[0] == address(0) || vaults[1] == address(0))
    revert MarketDoesNotExist(_marketId);

IVaultV2 premiumVault = IVaultV2(vaults[0]);
IVaultV2 collateralVault = IVaultV2(vaults[1]);

if (premiumVault.epochExists(_epochId) == false) revert EpochNotExist();

int256 price = getLatestPrice(premiumVault.token());

if (int256(premiumVault.strike()) <= price)
    revert PriceNotAtStrikePrice(price);
\u0060\u0060\u0060

### Vulnerability 2
\u0060\u0060\u0060solidity
function getLatestPrice(address _token) public view returns (int256) {
(
    ,
    /*uint80 roundId*/
    int256 answer,
    uint256 startedAt, /*uint256 updatedAt*/ /*uint80 answeredInRound*/
    ,
) = sequencerUptimeFeed.latestRoundData();

// Answer == 0: Sequencer is up
// Answer == 1: Sequencer is down
bool isSequencerUp = answer == 0;
if (!isSequencerUp) {
    revert SequencerDown();
}

// Make sure the grace period has passed after the sequencer is back up.
uint256 timeSinceUp = block.timestamp - startedAt;
if (timeSinceUp <= GRACE_PERIOD_TIME) {
    revert GracePeriodNotOver();
}
\u0060\u0060\u0060

Manual Review
Consider adding an additional "challenge" period (with reasonable length of time) after the epoch has expired and before the epoch end can be triggered without a depeg. Within this challenge period, anyone can claim a depeg has happened during the epoch\u0027s expiry and trigger the epoch end. By providing the Chainlink round id\u0027s for both feeds (sequencer and price) at the time of the epoch expiry (epochEnd), the claim can be verified to assert that the sequencer was down and the strike price was reached.

We are aware of this mechanic, however, users prefer to have the atomicity of instant settlement, this is so that users can utilize farming y2k tokens most effectively by rotating from one epoch to the next. Users are made aware of the risks when using chainlink oracles as well as the execution environment being on Arbitrum.
## pauliax
Escalate for 10 USDC.  
I believe this should be low severity because it falls under the misbehaving of infrastructure and integrations:  
Q: In case of external protocol integrations, are the risks of an external protocol pausing or executing an emergency withdrawal acceptable? If not, Watsons will submit issues related to these situations that can harm your protocol\u0027s functionality.  
A: [NOT ACCEPTABLE]

## sherlock-admin
Escalate for 10 USDC.  
I believe this should be low severity because it falls under the misbehaving of infrastructure and integrations:  
Q: In case of external protocol integrations, are the risks of an external protocol pausing or executing an emergency withdrawal acceptable? If not, Watsons will submit issues related to these situations that can harm your protocol\u0027s functionality.  
A: [NOT ACCEPTABLE]

You\u0027ve created a valid escalation for 10 USDC!  
To remove the escalation from consideration: Delete your comment.  
You may delete or edit your escalation comment anytime before the 48-hour escalation window closes. After that, the escalation becomes final.
Valid medium This is a valid issue as the readme indicates that risks associated with external integrations are not acceptable. That means issues are acceptable. However, Sherlock acknowledges the escalator\u0027s concern about some of these issues and will consider addressing them in the next update of the judging guidelines.
## Escalation rejected

Valid medium This is a valid issue as the readme indicates that risks associated with external integrations are not acceptable. That means issues are acceptable. However, Sherlock acknowledges the escalator\u0027s concern about some of these issues and will consider addressing them in the next update of the judging guidelines.

This issue\u0027s escalations have been rejected! Watsonswhoescalatedthisissuewill have their escalation amount deducted from their next payout.
## Issue has been acknowledged by sponsor
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/435)  
**Found by:** 0x52, 0xnirlin, Dug, ElKu, TrungOre, ast3ros, holyhansss, ni8mare, roguereddwarf, spyrosonic10, volodya, warRoom

VaultFactoryV2#changeTreasury misconfigures the vault because the setTreasury subcall uses the wrong variable.

\u0060\u0060\u0060solidity
function changeTreasury(uint256 _marketId, address _treasury)
  public
  onlyTimeLocker
{
  if (_treasury == address(0)) revert AddressZero();
  address[2] memory vaults = marketIdToVaults[_marketId];
  if (vaults[0] == address(0) || vaults[1] == address(0)) {
    revert MarketDoesNotExist(_marketId);
  }
  IVaultV2(vaults[0]).whiteListAddress(_treasury);
  IVaultV2(vaults[1]).whiteListAddress(_treasury);
  IVaultV2(vaults[0]).setTreasury(treasury);
  IVaultV2(vaults[1]).setTreasury(treasury);
  emit AddressWhitelisted(_treasury, _marketId);
}
\u0060\u0060\u0060

When setting the treasury for the underlying vault pair it accidentally uses the treasury variable instead of _treasury. This means it uses the local VaultFactoryV2 treasury rather than the function input.

\u0060\u0060\u0060solidity
ControllerPeggedAssetV2.sol#L111-L123
\u0060\u0060\u0060
The following code snippets illustrate a potential misconfiguration in the handling of token transfers:

\u0060\u0060\u0060solidity
premiumVault.sendTokens(_epochId, premiumFee, treasury);
premiumVault.sendTokens(
    _epochId,
    premiumTVL - premiumFee,
    address(collateralVault)
);
// strike price is reached so collateral is still entitled to premiumTVL - premiumFee but looses collateralTVL
collateralVault.sendTokens(_epochId, collateralFee, treasury);
collateralVault.sendTokens(
    _epochId,
    collateralTVL - collateralFee,
    address(premiumVault)
);
\u0060\u0060\u0060

This misconfiguration can be damaging as it may cause the \u0060triggerDepeg\u0060 call in the controller to fail due to the \u0060sendToken\u0060 subcall. Additionally, the time lock is the one required to call it, which has a minimum of 3 days wait period. The result is that valid depegs may not get paid out since they are time sensitive.

Valid depegs may be missed due to misconfiguration.

\u0060ControllerPeggedAssetV2.sol\u0060

Manual Review

Set to \u0060_treasury\u0060 rather than \u0060treasury\u0060.

- **3xHarry**: good catch!
- **3xHarry**: fix PR: [https://github.com/Y2K-Finance/Earthquake/pull/132](https://github.com/Y2K-Finance/Earthquake/pull/132)
- **IAm0x52**
## Fix looks good. setTreasury now correctly uses _treasury rather than treasury
**Source:** [GitHub Issue #442](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/442)  
**Found by:** 0x52, berndartmueller, bin2chen, iglyx, p0wd3r  

When rolling a position it is required that the user didn\u0027t payout on the last epoch. The issue with the check is that if a null epoch is triggered then rollovers will break even though the vault didn\u0027t make a payout.

\u0060\u0060\u0060solidity
uint256 entitledShares = previewWithdraw(
    queue[index].epochId,
    queue[index].assets
);
// mint only if user won epoch he is rolling over
if (entitledShares > queue[index].assets) {
\u0060\u0060\u0060
When minting rollovers the following check is made so that the user won\u0027t automatically roll over if they made a payout last epoch. This check however will fail if there is ever a null epoch. Since no payout is made for a null epoch it should continue to rollover but doesn\u0027t.

Rollover will halt after null epoch.

\u0060\u0060\u0060solidity
// Carousel.sol#L361-L459
\u0060\u0060\u0060

Manual Review

Change to less than or equal to:
\u0060\u0060\u0060solidity
54
\u0060\u0060\u0060
## Code Change
\u0060\u0060\u0060javascript
if (entitledShares >= queue[index].assets) {
\u0060\u0060\u0060

3xHarry  
makessense  
3xHarry  
Won\u0027t be able to fix this edge case. Changes in the rollover queue make it now that positions are not deleted anymore but rather marked to 0 to prevent rollover queue manipulation. In this case, users would have to resolve their stuck rollover position manually. [Link to GitHub Pull Request](https://github.com/Y2K-Finance/Earthquake/pull/127)  
IAm0x52  
Issue has been acknowledged by sponsor
**Source:** [GitHub Issue #480](https://github.com/sherlock-audit/2023-03-Y2K-judging/issues/480)  
**Found by:** Inspex, KingNFT, TrungOre, b4by_y0d4, berndartmueller, datapunk, evan, minhtrng, roguereddwarf, sinarette, toshii, volodya, yixxas

The epochBegin timestamp is used inconsistently and could lead to user funds being locked.

The function \u0060ControllerPeggedAssetV2.triggerNullEpoch\u0060 checks for timestamp like this:
\u0060\u0060\u0060solidity
if (block.timestamp < uint256(epochStart)) revert EpochNotStarted();
\u0060\u0060\u0060
The modifier \u0060epochHasNotStarted\u0060 (used by \u0060Carousel.deposit\u0060) checks it like this:
\u0060\u0060\u0060solidity
if (block.timestamp > epochConfig[_id].epochBegin)
    revert EpochAlreadyStarted();
\u0060\u0060\u0060
Both functions can be called when \u0060block.timestamp == epochBegin\u0060. This could lead to a scenario where a deposit happens after \u0060triggerNullEpoch\u0060 is called (both in the same block). Because \u0060triggerNullEpoch\u0060 sets the value for \u0060finalTVL\u0060, the TVL that comes from the deposit is not accounted for. If emissions have been distributed this epoch, this will lead to the incorrect distribution of emissions and once all emissions have been claimed the remaining assets will not be claimable, due to reversion in withdraw when trying to send emissions:
\u0060\u0060\u0060solidity
function previewEmissionsWithdraw(uint256 _id, uint256 _assets)
    public
    view
    returns (uint256 entitledAmount)
{
    entitledAmount = _assets.mulDivDown(emissions[_id], finalTVL[_id]);
}
\u0060\u0060\u0060
...
\u0060\u0060\u0060solidity
// in withdraw:
uint256 entitledEmissions = previewEmissionsWithdraw(_id, _assets);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
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
The above could also lead to revert through division by 0 if finalTVL is set to 0, even though the deposit after was successful.

- Incorrect distribution
- Loss of deposited funds

[Link to Code](https://github.com/sherlock-audit/2023-03-Y2K/blob/ae7f210d8fbf21b9abf09ef30edfa548f7ae1aef/Earthquake/src/v2/VaultV2.sol#L433)

- Manual Review

The modifier epochHasNotStarted should use >= as comparator.

- 3xHarry
- fix PR: https://github.com/Y2K-Finance/Earthquake/pull/130
- IAm0x52
- Fix looks good to me. Small inequality change for consistency
PAGE END
