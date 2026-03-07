# IssueM-1 - Division precision loss in create Distribution function lead to incorrect distribution of rewards in GammaRewarder.sol

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Gamme Brevis Rewarder
**Keywords:** precision loss, division, rewards, GammaRewarder, createDistribution, integer division, Solidity, contract, vulnerability, epoch, reward distribution, protocol fee, block range, cumulative loss, ERC20, testing, Hardhat, mock token, accuracy, scaling

---

# IssueM-1: Division precision loss in create Distribution function lead to incorrect distribution of rewards in GammaRewarder.sol

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-gamma-rewarder-judging/issues/21)  
Found by: 0xAadi, 0xhuh2005, 0xpetern, Greed, MaslarovK, Naresh, PNS, Praise03, X0sauce, dimah7, irresponsible, newspacexyz, safdie, sammy, tmotfl, tpiliposian, yixuan

## Summary
The createDistribution function in the contract contains a potential vulnerability related to precision loss during division calculations, which could lead to incorrect distribution of rewards. This occurs because the distribution logic divides _amount by fixed values without taking adequate measures to handle precision loss.

## Root Cause
The createDistribution function calculates amountPerEpoch by dividing realAmountToDistribute by the number of epochs. In cases where _amount is large, this division may lead to precision loss because Solidity\u0027s integer division discards the fractional component, potentially causing small discrepancies in each epoch\u0027s reward distribution. These inaccuracies accumulate over multiple epochs, leading to an overall loss in reward accuracy. The vulnerability is found in this segment of the createDistribution function:

\u0060\u0060\u0060solidity
function createDistribution(
    address _hypervisor,
    address _rewardToken,
    uint256 _amount,
    uint64 _startBlockNum,
    uint64 _endBlockNum
) external nonReentrant {
    // Other requirements and checks
    uint256 fee = _amount * protocolFee / BASE_9;
    uint256 realAmountToDistribute = _amount - fee;
    uint256 amountPerEpoch = realAmountToDistribute / ((_endBlockNum - _startBlockNum) / blocksPerEpoch);
}
\u0060\u0060\u0060
In this code, \u0060amountPerEpoch\u0060 is calculated by dividing \u0060realAmountToDistribute\u0060 by the \u0060numberOfEpochs\u0060 (which is derived from \u0060blockRange\u0060). The result may have a fractional part, but Solidity’s integer division will truncate it, leading to precision loss.
## Internal pre-conditions
No response

## External pre-conditions
No response

## Attack Path
No response

While this vulnerability does not entirely prevent the function’s operation, it introduces inaccuracies in reward distribution that may lead to small amounts being unrewarded over time. This could be noticeable with large distributions or over long durations, where cumulative precision loss can result in rewards lower than anticipated.

A Hardhat test can demonstrate the impact of precision loss, especially with large distributions where each division results in a truncated value. Setup:
1. Deploy a mock ERC20 token (\u0060MockRewardToken\u0060) and mint tokens to \u0060msg.sender\u0060.
2. Deploy the distribution contract.
3. Set large values for \u0060_amount\u0060 and a reasonable range for epochs to see the effect of precision loss.

Create distribution and validate results: Call \u0060createDistribution\u0060 and observe \u0060amountPerEpoch\u0060 to confirm whether the amount lost to precision affects each epoch\u0027s accuracy.

\u0060\u0060\u0060javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Division Precision Loss in \u0060createDistribution\u0060", function () {
    let rewardToken, distributionContract, owner, addr1;
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
const largeAmount = ethers.utils.parseUnits("1000000000", 18); // Large amount for distribution
const protocolFee = 100; // Simulated fee of 0.01%

before(async function () {
    [owner, addr1] = await ethers.getSigners();
    // Deploy mock ERC20 reward token
    const MockRewardToken = await ethers.getContractFactory("MockRewardToken");
    rewardToken = await MockRewardToken.deploy("Reward Token", "RTK", 18);
    await rewardToken.deployed();
    // Mint tokens to addr1 for testing
    await rewardToken.mint(addr1.address, largeAmount);
    // Deploy the distribution contract
    const DistributionContract = await ethers.getContractFactory("DistributionContract");
    distributionContract = await DistributionContract.deploy(protocolFee);
    await distributionContract.deployed();
});

it("Should exhibit precision loss in \u0060amountPerEpoch\u0060 calculation", async function () {
    // Set allowance
    await rewardToken.connect(addr1).approve(distributionContract.address, largeAmount);
    // Calculate expected values manually for comparison
    const epochs = 10; // Example block range divided into 10 epochs
    const realAmountToDistribute = largeAmount.mul(9999).div(10000); // Deduct protocol fee
    const expectedPerEpoch = realAmountToDistribute.div(epochs);
    // Execute createDistribution
    await distributionContract.connect(addr1).createDistribution(
        addr1.address,
        rewardToken.address,
        largeAmount,
        1000,
        2000
    );
    // Fetch distribution info and validate precision loss
    const distribution = await distributionContract.getDistribution(addr1.address);
    expect(distribution.amountPerEpoch).to.be.lt(expectedPerEpoch);
});
\u0060\u0060\u0060
Running this Hardhat test produces outputs showing that amountPerEpoch is lower than expected due to precision loss.


To mitigate this issue, consider modifying the calculation to use a higher precision mechanism, such as scaling the division before converting it back. For example, consider using a \u006010**18\u0060 multiplier to help retain more precision during the division, or calculate amountPerEpoch in a way that evenly distributes any rounding discrepancies over epochs.

\u0060\u0060\u0060solidity
uint256 amountPerEpoch = realAmountToDistribute * 10**18 / numberOfEpochs; // Multiplied to retain precision
amountPerEpoch = amountPerEpoch / 10**18; // Convert back after scaling
\u0060\u0060\u0060

Alternatively, use a mod function to calculate any remainder and distribute it across epochs to ensure accurate distribution.


The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/GammaStrategies/GammaRewarder/pull/2](https://github.com/GammaStrategies/GammaRewarder/pull/2)
PAGE END
