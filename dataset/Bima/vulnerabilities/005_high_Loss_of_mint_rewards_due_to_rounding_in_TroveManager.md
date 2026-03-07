# Loss of mint rewards due to rounding in TroveManager

**Severity:** high
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** mint rewards, TroveManager, precision loss, debt minting, openTrove, updateTroveFromAdjustment, updateMintVolume, VOLUME_MULTIPLIER, uint32, uint256, totalMints, SafeCast, reward distribution, fairness, USBD, debt amounts, data type change, recommendation, smart contract, Ethereum

---

# Loss of mint rewards due to rounding in TroveManager
Submitted by santipu, also found by Spearmint, XDZIBECX and pkqs90  
Severity: High Risk  
Context: TroveManager.sol#L1203  
Description: Users that mint debt through TroveManager will get an unfair amount of mint rewards due to precision loss happening at _updateMintVolume. Users can mint some debt in TroveManager through the functions openTrove and updateTroveFromAdjustment. These two functions are calling _updateMintVolume to accrue some rewards to the user who is taking the debt.
\u0060\u0060\u0060solidity
function _updateMintVolume(address account, uint256 initialAmount) internal {
    uint32 amount = SafeCast.toUint32(initialAmount / VOLUME_MULTIPLIER); // <<<
    (uint256 week, uint256 day) = getWeekAndDay();
    totalMints[week][day] += amount;
    // ...
}
\u0060\u0060\u0060
## Precision Loss in Minting Rewards
The variable \u0060initialAmount\u0060 is the amount of debt that is minted by the borrower, and it gets divided by \u0060VOLUME_MULTIPLIER\u0060, which is a constant with the value of \u00601e20\u0060:

\u0060\u0060\u0060solidity
// volume-based amounts are divided by this value to allow storing as uint32
uint256 constant VOLUME_MULTIPLIER = 1e20;
\u0060\u0060\u0060

This constant is used to downscale the debt amounts so they can be stored in a \u0060uint32\u0060 variable. However, this will cause a huge precision loss that will lead to some users not receiving any mint rewards when they mint an amount of debt lower than 100 USBD.

Imagine the following scenario:
- Bob opens a Trove to mint 200 USBD.
- Alice opens a Trove to mint 90 USBD.
- A day later, Alice adjusts the Trove to get 90 USBD more.
- A few days later, Alice adjusts the Trove again to mint 90 USBD of extra debt.
- After the week is over and mint rewards have to be distributed, Bob will receive all the mint rewards while Alice will receive none. This is unfair because Alice has minted more debt overall but it hasn\u0027t been saved in the rewards mechanism due to this precision loss.

Users who mint an amount of debt lower than 100 USBD at a time won\u0027t receive any mint rewards. Also, users who mint different amounts of debt will receive the same amounts of rewards as if they got the same debt. For example, Alice and Bob would have received the same rewards if they minted 100 and 199 USBD.

**Recommendation:** To mitigate this issue, it is recommended to change the data type of \u0060totalMints\u0060 and \u0060VolumeData.amount\u0060 from \u0060uint32\u0060 to \u0060uint256\u0060 to allow storing higher values. This would allow us to remove entirely the variable \u0060VOLUME_MULTIPLIER\u0060, and thus remove the precision loss as a whole.
