# 2 - Attacker Can Sweep All Mint Rewards When the System is in Recovery Mode

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** Recovery Mode, mint rewards, TroveManager, attacker, sweep, debt, TCR, CCR, liquidate, accountLatestMint, totalMints, borrowing fee, cost, mitigation, distribution, zero cost, impact, system, seconds, day, recommendation

---

# 1. Incompatibility with Sidechains

Ethereummainnet,soitusestheCurveAPIofmainnet. Butthisisnotcompatiblewithotherchains(e.g. Arbitrum).

Note: Bima sponsor team did not answer which chains this would be deployed on so I made an assumption from their website (bima.money, since it says to support on Arbitrum Sepolia right now. See CurveGauge\u0027s sidechain implementation differences with mainnet (see the curvedocs).

Oneofthemajordifferences is when minting CRV, the correct API to use is \u0060ChildGaugeFactory.mint(_gauge: address)\u0060. However, this is not the case in current CurveProxy code, because it calls \u0060Minter.mint(gauge)\u0060 instead.

\u0060\u0060\u0060solidity
function mintCRV(address gauge, address receiver) external onlyApprovedGauge(gauge) returns (uint256 amount) {
    uint256 initial = CRV.balanceOf(address(this));
    minter.mint(gauge); // <<<
    amount = CRV.balanceOf(address(this)) - initial;
    // apply fee prior to transfer
    uint256 fee = (amount * crvFeePct) / BIMA_100_PCT;
    amount -= fee;
    CRV.transfer(receiver, amount);
    // lock and extend if needed
    uint256 unlock = unlockTime;
    uint256 maxUnlock = ((block.timestamp / WEEK) * WEEK) + MAX_LOCK_DURATION;
    if (unlock < maxUnlock) {
        _updateLock(initial + fee, unlock, maxUnlock);
    }
}
\u0060\u0060\u0060

**Impact:** CurveProxy does work not with sidechains.  
**Recommendation:** Use \u0060IGauge(gauge).factory().mint(gauge)\u0060 for sidechain CRV minting.

## 2. Attacker Can Sweep All Mint Rewards When the System is in Recovery Mode

Submitted by santipu  
**Severity:** Medium Risk  
**Context:** \u0060TroveManager.sol#L1056\u0060, \u0060TroveManager.sol#L1098\u0060  

**Description:** When the system is in Recovery Mode, the mint rewards are not distributed within TroveManager:
\u0060\u0060\u0060solidity
if (!_isRecoveryMode) _updateMintVolume(_borrower, _compositeDebt);
\u0060\u0060\u0060

However, this allows an attacker to sweep all mint rewards when the system is in Recovery Mode and we\u0027re in the last seconds of a day. The attack path is the following:

1. The system has been in Recovery Mode (RM) all day and there are a few seconds left to finish the day.
2. An attacker opens a big Trove to move the TCR above the CCR and take the system out of RM:
   - There\u0027s no borrowing fee due to RM.
3. The attacker increases the debt on the existing Trove by a few wei so that this amount is stored on \u0060accountLatestMint\u0060 and \u0060totalMints\u0060.
4. The day just ends a few seconds later and the attacker has swept all mint rewards for that day at zero cost.

Alternatively, in step 2 the attacker could liquidate a few Troves to take the system out of RM and still execute this attack at no cost. The impact is that the attacker can sweep mint rewards for a whole day at zero cost when the system is in RM and the day is about to end.
To mitigate this issue, it is recommended to distribute mint rewards even if we\u0027re on RecoveryMode. Also, to avoid users sweeping mint rewards while we\u0027re in RM, it\u0027s recommended not to set the borrowing fee to zero but to lower it.
