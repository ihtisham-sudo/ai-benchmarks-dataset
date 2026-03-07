# rvierdiiev - TrufVesting.cancelVesting calculates end of vesting incorrectly

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Truflation
**Keywords:** TrufVesting, cancelVesting, vesting, cybersecurity, vulnerability, token distribution, cliff, initialReleasePeriod, claimable, period, owner, account, manual review, impact, code snippet, smart contract, decentralized finance, blockchain, security audit, function revert

---

rvierdiiev

medium

# TrufVesting.cancelVesting calculates end of vesting incorrectly

## Summary
TrufVesting.cancelVesting calculates end of vesting incorrectly and because of that owner can\u0027t stop vesting for the account.
## Vulnerability Detail
\u0060TrufVesting.cancelVesting\u0060 function allows owner to stop vesting for some account.

In case if vesting already finished, [then function reverts](https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L358-L360).

The problem is that \u0060vestingInfos[categoryId][vestingId].period\u0060 is just [period for token distribution after cliff](https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L186).

As you can see in \u0060claimable\u0060 function the vesting starts on \u0060startTime\u0060, then when [\u0060initialReleasePeriod\u0060 has passed](https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L168), then \u0060initialRelease\u0060 is distributed. Then [after \u0060cliff\u0060 has passed](https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L178), only then [final distribution starts](https://github.com/sherlock-audit/2023-12-truflation/blob/main/truflation-contracts/src/token/TrufVesting.sol#L184).

Thus check if vesting already finished is incorrect in the \u0060TrufVesting.cancelVesting\u0060 and it doesn\u0027t allow owner to cancel vesting when it is still going.
## Impact
Ongoing vesting can\u0027t be canceled.
## Code Snippet
Provided above
## Tool used

Manual Review

## Recommendation
This check should be correct.
\u0060\u0060\u0060solidity
if (userVesting.startTime + vestingInfos[categoryId][vestingId].initialReleasePeriod + vestingInfos[categoryId][vestingId].cliff + vestingInfos[categoryId][vestingId].period <= block.timestamp) {
            revert AlreadyVested(categoryId, vestingId, user);
}
\u0060\u0060\u0060
