# BenRai - \u0060optionTokens\u0060 can be expired even though the epoch is not over

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** BondProtocol
**Keywords:** cybersecurity, vulnerability, optionToken, expiry, epoch, epochDuration, epochStart, block.timestamp, timeUntilEligible, eligibleDuration, expiration date, UTC, manual review, payoutToken, redeem, claim rewards, significant value, rounding error, smart contract, decentralized finance

---

BenRai

high

# \u0060optionTokens\u0060 can be expired even though the epoch is not over

## Summary

When deploying an \u0060optionToken\u0060 the parameter \u0060expiry\u0060 is rounded down to the “nearest day at 0000 UTC” but since the end of an epoch is calculated by the \u0060epochDuration\u0060 and the exact time the epoch has stared and the \u0060optionToken\u0060 was created this can lead to an epoch still being active but the corresponding \u0060optionToken\u0060 to be already expired. 

## Vulnerability Detail

When starting a new epoch, the variable \u0060epochStart\u0060 is set to the current time (\u0060block.timestamp\u0060) and the end of the epoch is calculated by adding the \u0060epochDuration\u0060 to the \u0060epochStart\u0060 variable. 

The \u0060optionToken\u0060 of the new epoch is deployed with the parameter \u0060expire\u0060 calculated based on the current time stamp, the \u0060timeUntilEligible\u0060 and the \u0060eligibleDuration\u0060. (\u0060uint48(block.timestamp) + timeUntilEligible + eligibleDuration\u0060). The final expiration date of the optionToken is rounded down to the “nearest day at 0000 UTC” before the token is deployed.

Since the \u0060epochDuration\u0060 can be as close as 1 second to the sum of \u0060timeUntilEligible + eligibleDuration\u0060 this can lead to an epoch still being active but its \u0060optionToken\u0060 to be already expired.

Example:

epochDuration = 7 days
timeUntilEligible = 0
eligibleDuration = 7 days + 12 hours


New epoch is launched on the 01.01.2024 at 11:45 am.

=>
epochStart = block.timestamp  = 01.01.2024 at 11:45 am
epochEnd = epochStart + epochDuration = 08.01.2024 at 11:45 am

\u0060initial expire\u0060 = block.timestamp + timeUntilEligible + eligibleDuration = 08.01.2024 at 11:45 pm

\u0060final expire\u0060 after rounding down = uint48(\u0060initial expire\u0060/ 1day) * 1 day = 08.01.2024 at 00:00 am

The epoch is still active between \u0060final expire\u0060 and \u0060epochEnd\u0060 even though the option has already expired.

## Impact

Users that wait until the epoch has ended to claim their rewards expecting the options to be exercisable for 12 hours after the epoch end cannot claim their options since they are expired already and lose out on all the value the options would have had which can be significant depending on the current price of the \u0060payoutToken\u0060

## Code Snippet

https://github.com/sherlock-audit/2023-06-bond/blob/fce1809f83728561dc75078d41ead6d60e15d065/options/src/fixed-strike/liquidity-mining/OTLM.sol#L514-L534

https://github.com/sherlock-audit/2023-06-bond/blob/fce1809f83728561dc75078d41ead6d60e15d065/options/src/fixed-strike/FixedStrikeOptionTeller.sol#L122


https://github.com/sherlock-audit/2023-06-bond/blob/fce1809f83728561dc75078d41ead6d60e15d065/options/src/fixed-strike/liquidity-mining/OTLM.sol#L605-L611

https://github.com/sherlock-audit/2023-06-bond/blob/fce1809f83728561dc75078d41ead6d60e15d065/options/src/fixed-strike/liquidity-mining/OTLM.sol#L629-L643


## Tool used

Manual Review

## Recommendation

The expiration of the \u0060optionTokens\u0060 should be rounded up instead of down. This would increase the time an option can be redeemed long enough to prevent the scenario described above.

