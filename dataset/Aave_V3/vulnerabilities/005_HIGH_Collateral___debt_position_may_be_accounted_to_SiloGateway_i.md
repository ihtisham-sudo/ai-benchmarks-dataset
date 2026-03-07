# Collateral & debt position may be accounted to SiloGateway instead of user 

**Severity:** HIGH
**Auditor:** Cantina

---

## SiloGateway Documentation

## Context
**File**: SiloGateway.sol  
**Lines**: 92-96

## Description
The `borrowAsset()` function is intended to add collateral and borrow the asset on behalf of the user. However, this feature may not be supported by some protocols. For instance, certain protocols may accrue the collateral and debt to the caller, specifically, the `SiloGateway`.

An example of this is `FraxLend`, which was one of the protocols used for end-to-end tests. Below is a code snippet taken from the `borrowAsset()` function of `FraxLendPair`:

```solidity
if (_collateralAmount > 0) {
    _addCollateral(msg.sender, _collateralAmount, msg.sender);
}

function _addCollateral(
    address _sender,
    uint256 _collateralAmount,
    address _borrower
) internal {
    userCollateralBalance[_borrower] += _collateralAmount;
}
```

This results in the user's collateral being permanently locked up, even if the debt is repaid on behalf of the contract.

## Recommendation
Protocols need to be carefully checked to ensure that borrowing on behalf of the user is supported.

## Sturdy
**Status**: Acknowledged  
(See commit b0a71073.) We will use this contract when we deploy our Sturdy V2 silos, which have the feature of borrowing on behalf of the user, or implement another gateway contract for the Aave V3 and Compound V3 silos.

## Cantina
**Status**: Acknowledged.
