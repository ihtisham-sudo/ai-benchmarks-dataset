# jennifer37 - Lack of execution fee mechanism in AccountFacet

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, execution fee, AccountFacet, keeper, executeWithdraw, cancelWithdraw, OrderFacet, StakeFaucet, gas price, motivation, traders, collateral withdraw, manual review, recommendation, block, redeem, tokens, mechanism, operations, fee structure

---

jennifer37

Medium

# Lack of execution fee mechanism in AccountFacet

## Summary
When the keeper execute \u0060executeWithdraw\u0060 or \u0060cancelWithdraw\u0060, no execution fee is payed for the keeper.

## Vulnerability Detail
In OrderFacet and StakeFaucet, when the keepers execute increase order/ stake tokens, there will be some execution fee for the keepers. However, in AccountFacet, we lack of execution fee mechanism. Considering if gas price increases or there is not enough motivation to trigger \u0060executeWithdraw\u0060 or \u0060cancelWithdraw\u0060.
This will cause traders\u0027 redeem may be blocked.

\u0060\u0060\u0060javascript
    function executeWithdraw(uint256 requestId, OracleProcess.OracleParam[] calldata oracles) external override {
        RoleAccessControl.checkRole(RoleAccessControl.ROLE_KEEPER);
        Withdraw.Request memory request = Withdraw.get(requestId);
        if (request.account == address(0)) {
            revert Errors.WithdrawRequestNotExists();
        }
        OracleProcess.setOraclePrice(oracles);
        AssetsProcess.executeWithdraw(requestId, request);
        OracleProcess.clearOraclePrice();
    }

\u0060\u0060\u0060

## Impact
The keepers has less motivation to trigger \u0060executeWithdraw\u0060 or \u0060cancelWithdraw\u0060 compared with other operations. This will block the traders\u0027 collateral withdraw.

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/main/elfi-perp-contracts/contracts/facets/AccountFacet.sol#L48-L57

## Tool used

Manual Review

## Recommendation
Add execution fee mechanism for AccountFacet.
