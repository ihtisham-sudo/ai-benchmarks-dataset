# rvierdiiev - Lending pool state transition will be broken when pool is expired in late state

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, lending pool, state transition, expired, credit line, capital lock, manual review, default state manager, active state, late state, loan repayment, term end timestamp, state assessment, capital unlock, protection buyers, impact analysis, solidity, smart contract, financial security

---

rvierdiiev

high

# Lending pool state transition will be broken when pool is expired in late state

## Summary
Lending pool state transition will be broken when pool is expired in late state
## Vulnerability Detail
Each lending pool has its state. State is calculated inside \u0060ReferenceLendingPools._getLendingPoolStatus\u0060 function.
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ReferenceLendingPools.sol#L318-L349
\u0060\u0060\u0060solidity
  function _getLendingPoolStatus(address _lendingPoolAddress)
    internal
    view
    returns (LendingPoolStatus)
  {
    if (!_isReferenceLendingPoolAdded(_lendingPoolAddress)) {
      return LendingPoolStatus.NotSupported;
    }


    ILendingProtocolAdapter _adapter = _getLendingProtocolAdapter(
      _lendingPoolAddress
    );


    if (_adapter.isLendingPoolExpired(_lendingPoolAddress)) {
      return LendingPoolStatus.Expired;
    }


    if (
      _adapter.isLendingPoolLateWithinGracePeriod(
        _lendingPoolAddress,
        Constants.LATE_PAYMENT_GRACE_PERIOD_IN_DAYS
      )
    ) {
      return LendingPoolStatus.LateWithinGracePeriod;
    }


    if (_adapter.isLendingPoolLate(_lendingPoolAddress)) {
      return LendingPoolStatus.Late;
    }


    return LendingPoolStatus.Active;
  }
\u0060\u0060\u0060

Pls, note, that the first state that is checked is \u0060expired\u0060.
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/adapters/GoldfinchAdapter.sol#L62-L77
\u0060\u0060\u0060solidity
  function isLendingPoolExpired(address _lendingPoolAddress)
    external
    view
    override
    returns (bool)
  {
    ICreditLine _creditLine = _getCreditLine(_lendingPoolAddress);
    uint256 _termEndTimestamp = _creditLine.termEndTime();


    /// Repaid logic derived from Goldfinch frontend code:
    /// https://github.com/goldfinch-eng/mono/blob/bd9adae6fbd810d1ebb5f7ef22df5bb6f1eaee3b/packages/client2/lib/pools/index.ts#L54
    /// when the credit line has zero balance with valid term end, it is considered repaid
    return
      block.timestamp >= _termEndTimestamp ||
      (_termEndTimestamp > 0 && _creditLine.balance() == 0);
  }
\u0060\u0060\u0060
As you can see, pool is expired if time of credit line [has ended](https://github.com/goldfinch-eng/mono/blob/main/packages/protocol/contracts/protocol/core/CreditLine.sol#L43) or loan is fully paid.

State transition for lending pool is done inside \u0060DefaultStateManager._assessState\u0060 function. This function is responsible to lock capital, when state is late and unlock it when it\u0027s changed from late to active again.

Because the first state that is checked is \u0060expired\u0060 there can be few problems.

First problem. Suppose that lending pool is in late state. So capital is locked. There are 2 options now: payment was done, so pool becomes active and capital unlocked, payment was not done then pool has defaulted. But in case when state is late, and lending pool expired or loan is fully repaid(so it\u0027s also becomes expired), then capital will not be unlocked [as there is no such transition Late -> Expired](https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L324-L375). The state will be changed to Expired and no more actions will be done. Also in this case it\u0027s not possible to detect if lending pool expired because of time or because no payment was done.

Second problem.
Lending pool is in active state. Last payment should be done some time before \u0060_creditLine.termEndTime()\u0060. Payment was not done, which means that state should be changed to Late and capital should be locked, but state was checked when loan has ended, so it became Expired and again there is no such transition that can detect that capital should be locked in this case. The state will be changed to Expired and no more actions will be done.
## Impact
Depending on situation, capital can be locked forever or protection buyers will not be compensated.
## Code Snippet
Provided above
## Tool used

Manual Review

## Recommendation
These are tricky cases, think about transition for lending pool in such cases.
