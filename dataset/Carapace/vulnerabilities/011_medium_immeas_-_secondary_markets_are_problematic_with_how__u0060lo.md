# immeas - secondary markets are problematic with how \u0060lockCapital\u0060 works

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Carapace
**Keywords:** cybersecurity, vulnerability, flash loan, secondary market, Uniswap, lockCapital, sTokens, ProtectionPool, Active, LateWithinGracePeriod, Late, assessState, capital unlock, fungible tokens, ERC20, risk exposure, traders, LPs, manual review, attack vector

---

immeas

high

# secondary markets are problematic with how \u0060lockCapital\u0060 works

## Summary
Seeing that a pool is about to lock, an attacker can use a flash loan from a secondary market like uniswap to claim the share of a potential unlock of capital later.

## Vulnerability Detail

The timestamp a pool switches to Late can be predicted and an attacker can use this to call \u0060assessState\u0060 which is callable by anyone. This will trigger the pool to move from \u0060Active\u0060/\u0060LateWithinGracePeriod\u0060 to \u0060Late\u0060 calling \u0060lockCapital\u0060 on the \u0060ProtectionPool\u0060:

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L365-L366
\u0060\u0060\u0060solidity
File: ProtectionPool.sol

365:    /// step 1: Capture protection pool\u0027s current investors by creating a snapshot of the token balance by using ERC20Snapshot in SToken
366:    _snapshotId = _snapshot();
\u0060\u0060\u0060

This records who is holding sTokens at this point in time. If the borrower makes a payment and the pool turns back to Active, later the locked funds will be available to claim for the sToken holders at that snapshot:

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L500-L505
\u0060\u0060\u0060solidity
File: DefaultStateManager.sol

500:        /// The claimable amount for the given seller is proportional to the seller\u0027s share of the total supply at the snapshot
501:        /// claimable amount = (seller\u0027s snapshot balance / total supply at snapshot) * locked capital amount
502:        _claimableUnlockedCapital =
503:          (_poolSToken.balanceOfAt(_seller, _snapshotId) *
504:            lockedCapital.amount) /
505:          _poolSToken.totalSupplyAt(_snapshotId);
\u0060\u0060\u0060

From [docs](https://www.carapace.finance/WhitePaper#yields-distribution:~:text=If%20sellers%20wish,for%20protection%20sellers.):
> If sellers wish to redeem their capital and interest before the lockup period, they might be able to find a buyer of their sToken in a secondary market like Uniswap. Traders in the exchanges can long/short sTokens based on their opinion about the risk exposure associated with sTokens. Since an sToken is a fungible ERC20 token, it is fairly easy to bootstrap the secondary markets for protection sellers.

If there is a uniswap (or similar) pool for this sToken, an attacker could potentially, using a flash loan, trigger the switch to \u0060Late\u0060 and since they will be the ones holding the sTokens at the point of locking they will be the ones that can claim the funds at a potential unlock.

## Impact
An attacker can, using a flash loan from a secondary market like uniswap, steal a LPs possible share of unlocked tokens. Only paying taking the risk of the flash loan fee.

## Code Snippet
https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/pool/ProtectionPool.sol#L357-L366

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L119

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L137

https://github.com/sherlock-audit/2023-02-carapace/blob/main/contracts/core/DefaultStateManager.sol#L503


## Tool used
Manual Review

## Recommendation
I recommend you make \u0060assessState\u0060 only callable by a trusted user. This would remove the attack vector, since you must hold the tokens over a transaction. It would still be possible to use the [withdraw bug](https://github.com/sherlock-audit/2023-02-carapace-0ximmeas/issues/4), but if that is fixed this would remove the possibility to "flash-lock".
