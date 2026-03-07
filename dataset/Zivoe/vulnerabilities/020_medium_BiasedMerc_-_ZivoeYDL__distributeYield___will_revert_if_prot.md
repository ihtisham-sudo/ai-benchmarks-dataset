# BiasedMerc - ZivoeYDL::distributeYield() will revert if protocolRecipients recipients length is smaller than residualRecipients

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** ZivoeYDL, distributeYield, protocolRecipients, residualRecipients, vulnerability, revert, array length, timelock contract, updateRecipients, yield distribution, index access, YieldDistributedSingle, out of bounds, core functionality, manual review, reward contracts, function revert, protocol use, emit access, code snippet

---

BiasedMerc

medium

# ZivoeYDL::distributeYield() will revert if protocolRecipients recipients length is smaller than residualRecipients

## Summary

\u0060ZivoeYDL::distributeYield\u0060 incorrectly accesses \u0060_protocol[i]\u0060 instead of \u0060_residual[i]\u0060, and there are no checks anywhere within the code that ensures that both arrays are of the same length. Meaning that it is likely that this will cause \u0060distributeYield()\u0060 to revert in the case where \u0060protocolRecipients\u0060 length is less than \u0060residualRecipients\u0060.

## Vulnerability Detail

\u0060ZivoeYDL::updateRecipients\u0060 allows the timelock contract to update the \u0060protocolRecipients\u0060 or \u0060residualRecipients\u0060 variables:

[ZivoeYDL::updateRecipients](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L392-L416)
\u0060\u0060\u0060solidity
    function updateRecipients(address[] memory recipients, uint256[] memory proportions, bool protocol) external {
        require(_msgSender() == IZivoeGlobals_YDL(GBL).TLC(), "ZivoeYDL::updateRecipients() _msgSender() != TLC()");
        require(
            recipients.length == proportions.length && recipients.length > 0, 
            "ZivoeYDL::updateRecipients() recipients.length != proportions.length || recipients.length == 0"
        );
        require(unlocked, "ZivoeYDL::updateRecipients() !unlocked");
... SKIP!...
        if (protocol) {
            emit UpdatedProtocolRecipients(recipients, proportions);
            protocolRecipients = Recipients(recipients, proportions);
        }
        else {
            emit UpdatedResidualRecipients(recipients, proportions);
            residualRecipients = Recipients(recipients, proportions);
        }
    }
\u0060\u0060\u0060
It\u0027s important to note this function only sets one of those 2 variables at a time, and the length checks on \u0060recipients\u0060 and \u0060proportions\u0060 is to ensure that the \u0060Recipients()\u0060 struct inputs have the same length, NOT to ensure that \u0060protocolRecipients\u0060 and \u0060residualRecipients\u0060 are the same length. 

\u0060ZivoeYDL::distributeYield\u0060 calculates protocol earnings and distributes the yield to both the \u0060protocolRecipients\u0060 and \u0060residualRecipients\u0060. It does so by looping through the recipients and the earnings:

[ZivoeYDL::distributeYield](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L213-L286)
\u0060\u0060\u0060solidity
    function distributeYield() external nonReentrant {
        require(unlocked, "ZivoeYDL::distributeYield() !unlocked"); 
        require(
            block.timestamp >= lastDistribution + daysBetweenDistributions * 86400, 
            "ZivoeYDL::distributeYield() block.timestamp < lastDistribution + daysBetweenDistributions * 86400"
        );

        // Calculate protocol earnings.
        uint256 earnings = IERC20(distributedAsset).balanceOf(address(this));
        uint256 protocolEarnings = protocolEarningsRateBIPS * earnings / BIPS;
        uint256 postFeeYield = earnings.floorSub(protocolEarnings);

        // Update timeline.
        distributionCounter += 1;
        lastDistribution = block.timestamp;

        // Calculate yield distribution (trancheuse = "slicer" in French).
        (
            uint256[] memory _protocol, uint256 _seniorTranche, uint256 _juniorTranche, uint256[] memory _residual
        ) = earningsTrancheuse(protocolEarnings, postFeeYield); 

... SKIP!...

        // Distribute protocol earnings.
        for (uint256 i = 0; i < protocolRecipients.recipients.length; i++) {
            address _recipient = protocolRecipients.recipients[i];
            if (_recipient == IZivoeGlobals_YDL(GBL).stSTT() ||_recipient == IZivoeGlobals_YDL(GBL).stJTT()) {
                IERC20(distributedAsset).safeIncreaseAllowance(_recipient, _protocol[i]);
                IZivoeRewards_YDL(_recipient).depositReward(distributedAsset, _protocol[i]);
                emit YieldDistributedSingle(distributedAsset, _recipient, _protocol[i]);
            }
 
... SKIP!...

        // Distribute residual earnings.
        for (uint256 i = 0; i < residualRecipients.recipients.length; i++) {
            if (_residual[i] > 0) {
                address _recipient = residualRecipients.recipients[i];
                if (_recipient == IZivoeGlobals_YDL(GBL).stSTT() ||_recipient == IZivoeGlobals_YDL(GBL).stJTT()) {
                    IERC20(distributedAsset).safeIncreaseAllowance(_recipient, _residual[i]);
                    IZivoeRewards_YDL(_recipient).depositReward(distributedAsset, _residual[i]);
                    emit YieldDistributedSingle(distributedAsset, _recipient, _protocol[i]);
                }
\u0060\u0060\u0060
The function loops over \u0060protocolRecipients\u0060 and \u0060residualRecipients\u0060 seperately and within each loop indexed positions are accessed in  \u0060_protocol[]\u0060 and \u0060 _residual[]\u0060, these 2 arrays are initated as follows:

[ZivoeYDL::earningsTrancheuse](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L447-L451)
\u0060\u0060\u0060solidity
    function earningsTrancheuse(uint256 yP, uint256 yD) public view returns (
        uint256[] memory protocol, uint256 senior, uint256 junior, uint256[] memory residual
    ) {
        protocol = new uint256[](protocolRecipients.recipients.length);
        residual = new uint256[](residualRecipients.recipients.length);
\u0060\u0060\u0060
Their lengths will depend on the lengths of \u0060protocolRecipients\u0060 and \u0060residualRecipients\u0060 respectively, meaning their lengths can differ.

Finally, the 2nd for loop in \u0060distributeYield\u0060 itterates over \u0060residualRecipients\u0060 and 
 incorrectly emits the \u0060YieldDistributedSingle\u0060 event by accessing \u0060_protocol[i]\u0060, whilst it should be using \u0060_residual[i]\u0060. This will cause the function to revert due to an out of bound index access if:

\u0060residualRecipients.recipients.length > protocolRecipients.recipients.length\u0060
AND
atleast one of the recipients in \u0060residualRecipients.recipients\u0060 is:
\u0060IZivoeGlobals_YDL(GBL).stSTT() || IZivoeGlobals_YDL(GBL).stJTT()\u0060

which are the reward contracts:
[ZivoeYDL.sol#L20-L24](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L20-L24)
\u0060\u0060\u0060solidity
    /// @notice Returns the address of the ZivoeRewards ($zSTT) contract.
    function stSTT() external view returns (address);

    /// @notice Returns the address of the ZivoeRewards ($zJTT) contract.
    function stJTT() external view returns (address);
\u0060\u0060\u0060
meaning yield will not be able to be successfully distributed and the function will always revert as long as this condition is met.

## Impact

Core functionality of \u0060ZivoeYDL\u0060 will be unaccessible due to the function always reverting as long as the above condition is met, and this condition can easily be met through normal protocol use. 

This can be fixed by ensuring that both array are of the same length, however this means that appropriate fees cannot be distributed to the correct parties.

## Code Snippet

[ZivoeYDL.sol#L392-L416](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L392-L416)
[ZivoeYDL.sol#L213-L286](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L213-L286)
[ZivoeYDL.sol#L447-L451](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L447-L451)
[ZivoeYDL.sol#L20-L24](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L20-L24)

## Tool used

Manual Review

## Recommendation

Change the incorrect emit to access from \u0060_residual[i]\u0060 rather than \u0060_protocol[i]\u0060:
[ZivoeYDL.sol#L286](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-foundry/src/ZivoeYDL.sol#L286)
\u0060\u0060\u0060diff
- emit YieldDistributedSingle(distributedAsset, _recipient, _protocol[i]);
+ emit YieldDistributedSingle(distributedAsset, _recipient, _residual[i]);
\u0060\u0060\u0060
