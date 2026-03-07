# 0x73696d616f - \u0060ZivoeYDL::earningsTrancheuse()\u0060 always assumes that \u0060daysBetweenDistributions\u0060 have passed, which might not be the case

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** ZivoeYDL, earningsTrancheuse, daysBetweenDistributions, distributeYield, yield target, senior tranches, junior tranches, APY, residuals, block.timestamp, lastDistribution, yield distributed, manual review, Vscode, Foundry, ZivoeMath, seniorProportion, yieldTarget, code vulnerability, cyber security

---

0x73696d616f

medium

# \u0060ZivoeYDL::earningsTrancheuse()\u0060 always assumes that \u0060daysBetweenDistributions\u0060 have passed, which might not be the case

## Summary

\u0060ZivoeYDL::earningsTrancheuse()\u0060 calculates the target yield, senior and junior proportions based on \u0060daysBetweenDistributions\u0060. However, it is not strictly enforced that \u0060ZivoeYDL::distributeYield()\u0060 is called exactly at the \u0060daysBetweenDistributions\u0060 mark, leading to less yield for tranches.

## Vulnerability Detail

There is a yield target for senior and junior tranches over a [daysBetweenDistributions](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L459-L463) period that when exceeded, sends the rewards to [residuals](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L469-L471). However, the current code will not strictly follow the expected \u0060APY\u0060 for senior tranches, as the earning of tranches are calculated based on \u0060daysBetweenDistributions\u0060, but \u0060ZivoeYDL::distributeYield()\u0060 may be called significantly [after](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L215-L218) the \u0060daysBetweenDistributions\u0060 mark.

Add the following test to \u0060Test_ZivoeYDL.sol\u0060 to confirm that when the senior tranche yield reached the expected target for \u006030\u0060 days, if the time that \u0060ZivoeYDL::distributeYield()\u0060 was called increased, the yield distributed to the senior tranch remains the same.
\u0060\u0060\u0060solidity
function test_POC_ZivoeYDL_distributeYield_notEnforcingTranchesPeriod() public {    
    uint256 amtSenior = 1500 ether; // Minimum amount $1,000 USD for each coin.
    uint256 amount = 1000 ether;

    // Simulating the ITO will "unlock" the YDL
    simulateITO_byTranche_optionalStake(amtSenior, true);

    // uncomment this line instead to confirm that it\u0027s the same value below
    //hevm.warp(YDL.lastDistribution() + YDL.daysBetweenDistributions() * 86400);
    hevm.warp(YDL.lastDistribution() + YDL.daysBetweenDistributions() * 86400 + 1 days);

    // Deal DAI to the YDL
    mint("DAI", address(YDL), amount);

    YDL.distributeYield();

    console.log(IERC20(DAI).balanceOf(address(stSTT)));
}
\u0060\u0060\u0060

## Impact

Guaranteed less \u0060APY\u0060 for junior and senior tranches. The amount depends on how much time the call to \u0060ZivoeYDL::distributeYield()\u0060 was delayed since \u0060block.timestamp\u0060 reached \u0060lastDistribution + daysBetweenDistributions * 86400\u0060.

## Code Snippet

[distributeYield()](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L215-L218)
\u0060\u0060\u0060solidity
function distributeYield() external nonReentrant {
    ...
    require(
        block.timestamp >= lastDistribution + daysBetweenDistributions * 86400, 
        "ZivoeYDL::distributeYield() block.timestamp < lastDistribution + daysBetweenDistributions * 86400"
    );
    ...
\u0060\u0060\u0060

[ZivoeYDL::earningsTrancheuse()](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L459-L463)
\u0060\u0060\u0060solidity
function earningsTrancheuse(uint256 yP, uint256 yD) public view returns (
    uint256[] memory protocol, uint256 senior, uint256 junior, uint256[] memory residual
) {
    ...
    uint256 _seniorProportion = MATH.seniorProportion(
        IZivoeGlobals_YDL(GBL).standardize(yD, distributedAsset),
        MATH.yieldTarget(emaSTT, emaJTT, targetAPYBIPS, targetRatioBIPS, daysBetweenDistributions),
        emaSTT, emaJTT, targetAPYBIPS, targetRatioBIPS, daysBetweenDistributions
    );
    ...
}
\u0060\u0060\u0060

## Tool used

Manual Review

Vscode

Foundry

## Recommendation

Modify the [ZivoeMath::seniorProportion()](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeMath.sol#L68-L75) and [ZivoeMath::yieldTarget()](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeMath.sol#L121-L123) implementations to use seconds instead of days for \u0060T\u0060. Then, in \u0060Zivoe::YDL::earningsTrancheuse()\u0060, instead of [daysBetweenDistributions](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L459-L463) when calculating the yield target and senior proportion, use \u0060block.timestamp - lastDistribution\u0060. Also, in \u0060ZivoeYDL::distributeYield()\u0060, \u0060lastDistribution = block.timestamp;\u0060 must be moved after [earningsTrancheuse()](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L227-L232) is called.

