# H-5 - Leverage user can avoid paying fees to bondholders by withdrawing before auction ends

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** leverage, bondholders, fees, withdraw, auction, exploit, losses, redeemRate, Pool.sol, collateralLevel, transferReserveToAuction, malicious, users, contract, funds, payments, assets, threshold, tvl, tokenType

---

# Issue H-5: Leverage user can avoid paying fees to bondholders by withdrawing before auction ends

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/450)

This issue has been acknowledged by the team but won\u0027t be fixed at this time.

Found by: 0x52, moray5554, phoenixv110


Bondholders are paid fees by leverage holders in discrete quarterly payments. Due to the long length of this period, leverage holders can easily exploit and avoid this fee by withdrawing before funds are taken to pay for the auction. By doing this they can easily avoid paying all fees to bondholders, causing substantial losses to other leverage holders who are now forced to pay the malicious user\u0027s share of the fees.

\u0060\u0060\u0060solidity
Pool.sol
if (collateralLevel <= COLLATERAL_THRESHOLD) {
    redeemRate = ((tvl * multiplier) / assetSupply);
} else if (tokenType == TokenType.LEVERAGE) {
    redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) * PRECISION;
} else {
    redeemRate = BOND_TARGET_PRICE * PRECISION;
}
\u0060\u0060\u0060

We see above that the redeemRate for leverage tokens is calculated based on the number of assets held by the pool.

\u0060\u0060\u0060solidity
Pool.sol
function transferReserveToAuction(uint256 amount) external virtual {
    (uint256 currentPeriod, ) = bondToken.globalPool();
    address auctionAddress = auctions[currentPeriod];
    require(msg.sender == auctionAddress, CallerIsNotAuction());
    IERC20(reserveToken).safeTransfer(msg.sender, amount);
}
\u0060\u0060\u0060

We also see that funds are transferred out of the contract until after the auction is completed. Therefore if the user withdraws before the auction ends then they will receive an amount that is not subject to the bondholders fee.
## Root Cause

Pool.sol fails to enforce or charge partial fees to redeeming leverage users

## Internal preconditions
None

## External preconditions
None

N/A

Leverage users can get leverage exposure for free while forcing other users to pay their fees

Unfortunately it is impossible to demonstrate via POC because transferReserveToAuction is broken

N/A
## Issue H-6: Malicious user can leverage flash loans to claim all coupon rewards

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/725)

Found by: 0x23r0, 0x52, 0xNov1ce, 0xe4669da, AksWarden, BADROBINX, ChainProof, Etherking, InquisitorScythe, Kenn.eth, MysteryAuditor, Nadir_Khan_Sec, OrangeSantra, Pablo, Schnilch, Strapontin, Uddercover, ZoA, aswinraj94, bladeee, copperscrewer, devalinas, farman1094, future, komane007, momentum, moray5554, phoenixv110


Anyone can call \u0060Pool::startAuction\u0060, which will deploy a new auction and checkpoint the \u0060sharesPerToken\u0060 by calling \u0060BondToken::increaseIndexedAssetPeriod\u0060 for the holders of bond token, as long as distribution period have passed since the last distribution.

\u0060\u0060\u0060solidity
function startAuction() external whenNotPaused {
    require(lastDistribution + distributionPeriod < block.timestamp, DistributionPeriodNotPassed());
    require(lastDistribution + distributionPeriod + auctionPeriod >= block.timestamp, AuctionPeriodPassed());
    ....
    bondToken.increaseIndexedAssetPeriod(sharesPerToken);
    lastDistribution = block.timestamp;
}
\u0060\u0060\u0060

The \u0060Pool::distribute\u0060 function distributes the rewards from the previous auction, so it can only be called after a new auction has started.

\u0060\u0060\u0060solidity
function distribute() external whenNotPaused {
    (uint256 currentPeriod,) = bondToken.globalPool();
    require(currentPeriod > 0, AccessDenied());
    uint256 previousPeriod = currentPeriod - 1;
    uint256 couponAmountToDistribute = Auction(auctions[previousPeriod]).totalBuyCouponAmount();
    ....
}
\u0060\u0060\u0060

The \u0060Distributor::claim\u0060 function gets the shares of the user by calling \u0060BondToken::getIndexedUserAmount\u0060:

\u0060\u0060\u0060solidity
function getIndexedUserAmount(address user, uint256 balance, uint256 period) public view returns (uint256) {
    ....
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
IndexedUserAssets memory userPool = userAssets[user];
uint256 shares = userPool.indexedAmountShares;
for (uint256 i = userPool.lastUpdatedPeriod; i < period; i++) {
    shares += (balance *
    globalPool.previousPoolAmounts[i].sharesPerToken).toBaseUnit(SHARES_DECIMALS);
}
return shares;
\u0060\u0060\u0060

The function loops through the periods and accounts for all of the shares during the user\u0027s last updated one to the current. The docs state that as long as the user holds during distribution, he should be eligible for the coupon rewards, however this opens up an opportunity for a flash loan attack. The attacker can leverage this by minting bond tokens and calling startAuction, which will increase the current period and make it greater than the userPool.lastUpdatedPeriod, which makes the Distributor account his shares.

Pool does not have a flash loan protection allowing users to claim all of the coupon rewards.

None

None

When users claim through the Distributor::claim 1 share == 1 coupon token, which the attacker can leverage by: In one transaction:
- Takes a flash loan
- Mints couponAmountToDistribute / sharesPerToken bond tokens
- Calls startAuction to snapshot his balance
- Calls distribute to distribute the coupon rewards to the distributor
- Calls Distributor::claim to claim all of the shares
## Burnthebondtokens

- Repaystheflashloan

All of the other holders will be left with no rewards

Noresponse

Considernotallowinganyonetoturnoveraperiod,orapplysomekindofsnapshot protection

sherlock-admin2  
TheprotocolteamfixedthisissueinthefollowingPRs/commits:  
https://github.com/Convexity-Research/plaza-evm/pull/162
## IssueH-7: Funds might remain locked in Balancer Router when depositing in Balancer pool

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/841)

Found by: 0xShahilHussain, 0xadrii, Adotsam, Albort, KupiaSec, ZeroTrust, bretzel, dobrevaleri, elolpuer, novaman33, shushu, sl1

Not checking how much of the deposited assets are actually deposited in the pool, will lead to loss of funds for the user, because the remaining assets will be locked inside the Balancer Router.

Balancer Router provides an integration with Balancer V2 pools via the joinBalancerPool(), which is used by joinBalancerAndPlaza() and joinBalancerAndPredeposit(). When called, joinBalancerPool() accepts the poolId, array of assets, the maximum amounts the user is willing to deposit and additional user data. First it transfers the maximum amount of assets from the user\u0027s address to its (ref). And after that joins the pool (ref). However, it is not guaranteed that the maximum value of each asset will be deposited in the Pool. From the Balancer V2 doc:

> The amounts to send are decided by the Pool and not the Vault: it just enforces these maximums.

This means that there might be leftover assets in the Balancer Router that are not deposited into the pool, but are also not returned to the user.

No response

1. Not all assets are deposited into the Balancer Pool.

1. User calls \u0060joinBalancerAndPredeposit()\u0060 or \u0060joinBalancerAndPlaza()\u0060.
2. Maximum amount of tokens are sent to the BalancerRouter.
3. Not all of the tokens are deposited into the Pool, because he decided how much to deposit.


The user will suffer loss of funds, because part of his assets will remain locked in the BalancerRouter.


No response


Send the remaining assets back to the user.


sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/154](https://github.com/Convexity-Research/plaza-evm/pull/154)
## IssueH-8: Fee is charged current reserve Token pool balance to time which is not updated

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/842)

Found by:  
0x52, 0xDemon, 0xadrii, 0xlucky, 0xmystery, Abhan1041, Beejay, BugAttacker, ChainProof, Darinrikusham, DeLaSoul, Etherking, Goran, Harry_cryptodev, JohnTPark24, Kirkeelee, KupiaSec, Kyosi, MysteryAuditor, Pablo, Saurabh_Singh, Strapontin, ZeroTrust, ZoA, appet, bigbear1229, bladeee, bretzel, bube, davidjohn241018, dobrevaleri, farismaulana, future, moray5554, novaman33, pessimist, prosper, sl1, t0x1c, tvdung94, ydlee


Here fee is charged from last Fee Claim Time to current time but with current reserve Token pool balance. But fee should be charged one every reserve Token balance is changed. That can be accomplished via claimFees function is invoked every user create and redeem activities.


Fee is charged based on current reserve Token balance where fee Beneficiary is invoked claimFees function. But time to time reserve Token can be changed. So fee should be calculated each and every time when reserve Token balance is changed.

\u0060\u0060\u0060solidity
function claimFees() public nonReentrant {
    require(msg.sender == feeBeneficiary ||
    poolFactory.hasRole(poolFactory.GOV_ROLE(), msg.sender), NotBeneficiary());
    uint256 feeAmount = getFeeAmount();
    if (feeAmount == 0) {
        revert NoFeesToClaim();
    }
    lastFeeClaimTime = block.timestamp;
    IERC20(reserveToken).safeTransfer(feeBeneficiary, feeAmount);
    emit FeeClaimed(feeBeneficiary, feeAmount);
}

/**
 * @dev Returns the amount of fees to be claimed.
 * @return The amount of fees to be claimed.
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function getFeeAmount() internal view returns (uint256) {
   return (IERC20(reserveToken).balanceOf(address(this)) * fee * (block.timestamp -
   lastFeeClaimTime)) / (PRECISION * SECONDS_PER_YEAR);
}
\u0060\u0060\u0060

Can happen in normal operation.

None

1. Consider this scenario, pool consists of 10e18 reserveToken throughout the year. At the year end, someone has deposited 1000e18 reserveToken. Now feeBeneficiary is called claimFees, here fee is overcharged, meaning fee is calculated as 1000e18 token is in pool throughout the year.
2. Pool consists of 1000e18 reserveToken throughout the year. At the year end, most users are redeeming, due to that reserveToken balance is 10e18. Now feeBeneficiary is called claimFees, here fee is undercharged, meaning fee is calculated as 10e18 token is in pool throughout the year.

Fee is not collected correctly so that it could be overcharged or undercharged.

No response

claimFees can be invoked inside of _create and _redeem functions.

sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:
[PR #164](https://github.com/Convexity-Research/plaza-evm/pull/164)
