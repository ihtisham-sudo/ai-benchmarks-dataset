# WATCHPUG - Lack of access control for \u0060mintRebalancer()\u0060 and \u0060burnRebalancer()\u0060

**Severity:** high
**Auditor:** Sherlock
**Protocol:** USSD V1
**Keywords:** cybersecurity, vulnerability, access control, mintRebalancer, burnRebalancer, denial-of-service, totalSupply, rebalancer, SellUSSDBuyCollateral, ownval, onlyBalancer, collateralFactor, attacker, minting, type(uint256), malfunction, implementation, manual review, recommendation, USSD

---

WATCHPUG

high

# Lack of access control for \u0060mintRebalancer()\u0060 and \u0060burnRebalancer()\u0060

## Summary

Lack of access control in \u0060USSD.mintRebalancer()\u0060 and \u0060USSD.burnRebalancer()\u0060 can lead to a denial-of-service attack and malfunction of the rebalancer as it can alter \u0060totalSupply\u0060, which is used in \u0060rebalancer.SellUSSDBuyCollateral\u0060 to calculate \u0060ownval\u0060.

## Vulnerability Detail

Based on the context, \u0060USSD.mintRebalancer()\u0060 should be \u0060onlyBalancer\u0060 as it should only be allowed to be called by the rebalancer.

However, both \u0060USSD.mintRebalancer()\u0060 and \u0060USSD.burnRebalancer()\u0060 lack access control in the current implementation.

## Impact

An attacker can mint an amount of \u0060type(uint256).max - totalSupply()\u0060 and cause a denial-of-service attack by preventing anyone else from minting.

Additionally, minting will also change the \u0060totalSupply\u0060 which alters the \u0060collateralFactor\u0060 and cause the rebalancer to malfunction, as the \u0060SellUSSDBuyCollateral()\u0060 function relies on the \u0060USSD.collateralFactor()\u0060.

The \u0060totalSupply\u0060 is also used in \u0060rebalancer.SellUSSDBuyCollateral\u0060 to calculate the \u0060ownval\u0060.

## Code Snippet

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L204-L210

\u0060\u0060\u0060solidity
function mintRebalancer(uint256 amount) public override {
    _mint(address(this), amount);
}

function burnRebalancer(uint256 amount) public override {
    _burn(address(this), amount);
}
\u0060\u0060\u0060

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSDRebalancer.sol#L92-L107

\u0060\u0060\u0060solidity
    function rebalance() override public {
      uint256 ownval = getOwnValuation();
      (uint256 USSDamount, uint256 DAIamount) = getSupplyProportion();
      if (ownval < 1e6 - threshold) {
        // peg-down recovery
        BuyUSSDSellCollateral((USSDamount - DAIamount / 1e12)/2);
      } else if (ownval > 1e6 + threshold) {
        // mint and buy collateral
        // never sell too much USSD for DAI so it \u0027overshoots\u0027 (becomes more in quantity than DAI on the pool)
        // otherwise could be arbitraged through mint/redeem
        // the execution difference due to fee should be taken into accounting too
        // take 1% safety margin (estimated as 2 x 0.5% fee)
        IUSSD(USSD).mintRebalancer(((DAIamount / 1e12 - USSDamount)/2) * 99 / 100); // mint ourselves amount till balance recover
        SellUSSDBuyCollateral();
      }
    }
\u0060\u0060\u0060

https://github.com/sherlock-audit/2023-05-USSD/blob/main/ussd-contracts/contracts/USSD.sol#L179-L194

\u0060\u0060\u0060solidity
function collateralFactor() public view override returns (uint256) {
    uint256 totalAssetsUSD = 0;
    for (uint256 i = 0; i < collateral.length; i++) {
        totalAssetsUSD +=
            (((IERC20Upgradeable(collateral[i].token).balanceOf(
                address(this)
            ) * 1e18) /
                (10 **
                    IERC20MetadataUpgradeable(collateral[i].token)
                        .decimals())) *
                collateral[i].oracle.getPriceUSD()) /
            1e18;
    }

    return (totalAssetsUSD * 1e6) / totalSupply();
}
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation

\u0060USSD.mintRebalancer()\u0060 should be \u0060onlyBalancer\u0060.
