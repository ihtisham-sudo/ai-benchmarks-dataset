# aman - The USer will receive less amount  than user expected

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, redeem tokens, minRedeemAmount, executeRedeemStakeToken, fee deduction, transaction revert, unStakeUsd, redeemTokenAmount, oracle price, RedeemFeeRate, RATE_PRECISION, slippage check, manual review, protocol, user expectation, amount discrepancy, redemption request, fee calculation, impact assessment

---

aman

Medium

# The USer will receive less amount  than user expected

## Summary
While redeeming the stack tokens, The user provides the \u0060minRedeemAmount\u0060 to ensure they receive at least that amount. However,  within \u0060executeRedeemStakeToken\u0060 function, the  \u0060minRedeemAmount\u0060 check is used before deducting the fee . which could result in  the user  receive less amount than the expected amount.


## Vulnerability Detail
The Protocol allows user to specify the \u0060minRedeemAmount\u0060 to insure that the user will receive this amount or in other case the transaction will revert. The User will first submit a request for Redemption where he also specify this \u0060minRedeemAmount\u0060 which user expect to receive. The Issue is in the execute redemption request flow.
\u0060\u0060\u0060solidity
function _executeRedeemStakeToken(
        LpPool.Props storage pool,
        Redeem.Request memory params,
        address baseToken
    ) internal returns (uint256) {
        ...
        cache.redeemTokenAmount = CalUtils.usdToToken(
            cache.unStakeUsd,
            cache.tokenDecimals,
            OracleProcess.getLatestUsdUintPrice(baseToken, false)
        );

        if (pool.getPoolAvailableLiquidity() < cache.redeemTokenAmount) {
            revert Errors.RedeemWithAmountNotEnough(params.account, params.redeemToken);
        }

 @>     if (params.minRedeemAmount > 0 && cache.redeemTokenAmount < params.minRedeemAmount) {
            revert Errors.RedeemStakeTokenTooSmall(cache.redeemTokenAmount);
        }
        ...
        FeeProcess.chargeMintOrRedeemFee(
            redeemFee,
            params.stakeToken,
            params.redeemToken,
            params.account,
            FeeProcess.FEE_REDEEM,
            false
        );
        VaultProcess.transferOut(
            params.stakeToken,
            params.redeemToken,
            params.receiver,
@>         cache.redeemTokenAmount - cache.redeemFee
        );
        pool.subPoolAmount(pool.baseToken, cache.redeemTokenAmount);
        StakeToken(params.stakeToken).burn(params.account, params.unStakeAmount);
        stakingAccountProps.subStakeAmount(params.stakeToken, params.unStakeAmount);

        return cache.redeemTokenAmount;
    }
\u0060\u0060\u0060
As it can be observed from above code that we first convert the \u0060unStkaeUsd\u0060 amount and store receive value in \u0060cache.redeemTokenAmount\u0060.Than we check for \u0060minRedeemAmount\u0060
and than we deduct the fee and transfer the remaining \u0060redeemTokenAmount\u0060 to user.
Following case would occur due to this:
1. Bob submit a request to redeem 10e18 token and expect to receive 9e18 token.
2. the Protocol convert the amount using latest oracle price and get 9 token as redeemTokenAmount.
3. The \u0060cache.redeemTokenAmount < params.minRedeemAmount\u0060 check will pass as 9e18 < 9e18.
4. The \u0060RedeemFeeRate=10\u0060 and \u0060RATE_PRECISION=100000\u0060 Now Applying these values to calculate the Fee amount is \u00609e18*10/100000= 9e14\u0060.
5. The amount Bob will receive is \u00609e18-9e14≈8.9e17\u0060.


This applies on both functions \u0060_executeRedeemStakeUsd\u0060 and \u0060_executeRedeemStakeToken\u0060.

## Impact
The user will receive less amount than expected.


## Code Snippet
[https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/RedeemProcess.sol#L157](https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/RedeemProcess.sol#L157)

## Tool used

Manual Review

## Recommendation
Use slippage check after deducting the Fee.
\u0060\u0060\u0060diff
diff --git a/elfi-perp-contracts/contracts/process/RedeemProcess.sol b/elfi-perp-contracts/contracts/process/RedeemProcess.sol
index dedfe16e..eb6c84fe 100644
--- a/elfi-perp-contracts/contracts/process/RedeemProcess.sol
+++ b/elfi-perp-contracts/contracts/process/RedeemProcess.sol
@@ -200,9 +200,7 @@ library RedeemProcess {
             tokenDecimals,
             OracleProcess.getLatestUsdUintPrice(params.redeemToken, false)
         );
-        if (params.minRedeemAmount > 0 && redeemTokenAmount < params.minRedeemAmount) {
-            revert Errors.RedeemStakeTokenTooSmall(redeemTokenAmount);
-        }
         if (pool.getMaxWithdraw(params.redeemToken) < redeemTokenAmount) {
             revert Errors.RedeemWithAmountNotEnough(params.account, params.redeemToken);
         }
@@ -219,6 +217,9 @@ library RedeemProcess {
             FeeProcess.FEE_REDEEM,
             false
         );
+        if (params.minRedeemAmount > 0 && redeemTokenAmount-redeemFee < params.minRedeemAmount) {
+            revert Errors.RedeemStakeTokenTooSmall(redeemTokenAmount);
+        }
 
         StakeToken(params.stakeToken).burn(account, params.unStakeAmount);
         StakeToken(params.stakeToken).transferOut(params.redeemToken, params.receiver, redeemTokenAmount - redeemFee);
\u0060\u0060\u0060

