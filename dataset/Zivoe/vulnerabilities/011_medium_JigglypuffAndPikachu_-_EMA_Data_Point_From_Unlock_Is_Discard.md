# JigglypuffAndPikachu - EMA Data Point From Unlock Is Discarded

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** EMA, cybersecurity, vulnerability, unlock, data point, calculation, yield distribution, MATH.ema, emaSTT, emaJTT, totalSupply, distributionCounter, incorrect calculation, retrospectiveDistributions, manual review, contract, security flaw, data integrity, smart contract, recommendation

---

JigglypuffAndPikachu

medium

# EMA Data Point From Unlock Is Discarded

## Summary

The \u0060ema\u0060 calculation fails to incorporate the \u0060emaJTT\u0060 and \u0060emaSTT\u0060 amounts which are initally set in \u0060unlock\u0060.

## Vulnerability Details

Let\u0027s carefully consider the EMA calculation. Firstly during the unlock, the \u0060emaSTT\u0060 and \u0060emaJTT \u0060are set to the current values. This acts as our first data point. Since this is the only data point, this doesn\u0027t have any averaging which is why \u0060MATH.ema()\u0060 is not called.

Now, after unlocking consider when \u0060distributeYield\u0060 is called for the first time after unlocking. \u0060emaSTT\u0060 and \u0060emaJTT\u0060 should incorporate the first data point (which was recorded during unlock) with the new \u0060totalSupply\u0060 of \u0060STT\u0060 and \u0060JTT\u0060.

Now let\u0027s show why the contract will actually ignore the \u0060emaSTT\u0060/JTT set during unlock during the first yield distribution:

The \u0060distributionCounter\u0060 is \u00600\u0060 when \u0060distributeYield\u0060 is called, but due to the line \u0060distributionCounter += 1;\u0060, \u00601\u0060 is passed as the 3rd parameter to the \u0060ema\u0060 formula in \u0060emaSTT = MATH.ema(emaSTT, aSTT, retrospectiveDistributions.min(distributionCounter));\u0060

When \u0060N == 1\u0060 in the \u0060ema\u0060 formula, the function will return only \u0060eV\u0060, which is only the latest data point. It completely ignores \u0060bV\u0060 which is the data point during the unlock:

\u0060\u0060\u0060solidity
function ema(uint256 bV, uint256 cV, uint256 N) external pure returns (uint256 eV) {

    assert(N != 0);

    uint256 M = (WAD * 2).floorDiv(N + 1); //When N = 1, M = WAD

    eV = ((M * cV) + (WAD - M) * bV).floorDiv(WAD); //Substituting M = WAD, eV = cV

}
\u0060\u0060\u0060

## Impact

Incorrect EMA calculation which leads to incorrect yield distribution

## Code Snippet

https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L213-L310

## Tool used

Manual Review

## Recommendation

The \u0060distributionCounter\u0060 should actually be \u00602\u0060 rather than 1 during the first pass into the \u0060MATH.ema()\u0060 formula. However then the varibale would not really correspond to the number of times \u0060distribution\u0060 was called, so it might need to be renamed.

