# jennifer37 - Uninitialized cache.redeemFee cause 0 redeem fee

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, uninitialized variable, redeem fee, liquidity pool, LP holders, redeem stake token, contract, cache, fee rewards, impact, manual review, code snippet, financial risk, smart contract, decentralized finance, blockchain, security flaw, initialization, recommendation

---

jennifer37

Medium

# Uninitialized cache.redeemFee cause 0 redeem fee

## Summary
\u0060cache.redeemFee\u0060 is not initialized correctly, which cause LP holders don\u0027t need to pay the redeem fee. This is not expected behavior.
 
## Vulnerability Detail
When LP holders redeem liquidity, LP holders need to pay some redeem fees. In function \u0060_executeRedeemStakeToken \u0060, the actual redeem fee is calculated and save into the variable \u0060redeemFee\u0060. The vulnerability is that contract use \u0060cache.redeemTokenAmount - cache.redeemFee\u0060 to calculate the final amount that LP holders can redeem. However, \u0060cache.redeemFee\u0060 is not initialised and the default value is 0. 

This means that the LP holders don\u0027t need to pay the redeem fee. This is not one expected behavior. What\u0027s more, this redeem fee is charged by fee rewards. In the future, these redeem fees may be transferred out to reward contract. However, in fact, LP holders don\u0027t leave any redeem fees. This could cause the LP pool\u0027s account into a mess.

\u0060\u0060\u0060javascript
    function _executeRedeemStakeToken(
        LpPool.Props storage pool,
        Redeem.Request memory params,
        address baseToken
    ) internal returns (uint256) {
       ......
@==> actual redeem Fee.
        uint256 redeemFee = FeeQueryProcess.calcMintOrRedeemFee(cache.redeemTokenAmount, poolConfig.redeemFeeRate);
        FeeProcess.chargeMintOrRedeemFee(
            redeemFee,
            params.stakeToken,
            params.redeemToken,
            params.account,
            FeeProcess.FEE_REDEEM,
            false
        );
@==> cache.redeemFee is not initialized to redeemFee.
        VaultProcess.transferOut(
            params.stakeToken,
            params.redeemToken,
            params.receiver,
            cache.redeemTokenAmount - cache.redeemFee
        );
\u0060\u0060\u0060

## Impact
- LP holders don\u0027t need to pay the redeem fees.
- The redeem fees are charged by fee rewards. However, LP holders don\u0027t leave any redeem fees in the pool, which will cause the pool\u0027s account into a mess.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/process/RedeemProcess.sol#L133-L183

## Tool used

Manual Review

## Recommendation
Initialized \u0060cache.redeemFee\u0060
