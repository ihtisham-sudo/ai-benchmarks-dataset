# LOW - Inadequate Staleness Check in getPriceAndDecimals() Function

**Severity:** low
**Auditor:** Halborn
**Protocol:** Moonwell
**Keywords:** oracle, Chainlink, stale data, getPriceAndDecimals, ReserveAutomation, updatedAt, answeredInRound, roundId, validity, timestamp, heartbeat interval, validation, risk, data integrity, smart contract, blockchain, price feed, function, require, AggregatorV3Interface

---

# LOW

### Description
In the ReserveAutomation contract, the getPriceAndDecimals() function checks that the returned price is positive and that the round is valid, using answeredInRound >= roundId and updatedAt != 0, but it does not check that the price data is recent. In some applications, using stale oracle data is a risk.

\u0060\u0060\u0060solidity
/// @notice helper function to retrieve price from chainlink
/// @param oracleAddress The address of the chainlink oracle
/// returns the price and then the decimals of the given asset
/// reverts if price is 0 or if the oracle data is invalid
function getPriceAndDecimals(
   address oracleAddress
) public view returns (int256, uint8) {
   (
      uint80 roundId,
      int256 price,
      ,
      uint256 updatedAt,
      uint80 answeredInRound
   ) = AggregatorV3Interface(oracleAddress).latestRoundData();
   bool valid = price > 0 && answeredInRound >= roundId && updatedAt != 0;
   require(valid, "ReserveAutomationModule: Oracle data is invalid");
   uint8 oracleDecimals = AggregatorV3Interface(oracleAddress).decimals();

   return (price, oracleDecimals); /// price always gt 0 at this point
}
\u0060\u0060\u0060

The getPriceAndDecimals() function does not adequately handle cases where the oracle returns the latest timestamp (updatedAt) outside the defined heartbeat interval for the requested asset. Specifically, when using the AggregatorV3Interface from Chainlink, it is essential to validate the updatedAt timestamp returned by the latestRoundData function to ensure it is within acceptable ranges.

BVSS  
AO:A/AC:L/AX:L/C:N/I:L/A:N/D:L/Y:N/R:N/S:C (3.9)

### Recommendation
Implement validation checks for the returned oracle data when using the AggregatorV3Interface. Ensure that the latest returned timestamp is within the defined heartbeat interval for the requested asset.

### Remediation Comment
RISK ACCEPTED: The Moonwell team has accepted the risk related to this finding.
## Description
In the ReserveAutomation contract, the discount (or premium) is computed in the function \u0060currentDiscount()\u0060, as follows:

\u0060\u0060\u0060solidity
/// @notice Calculates the current discount or premium rate for reserve purchases
/// @return The current discount as a percentage scaled to 1e18, returns
/// 1e18 if no discount is applied
/// @dev Does not apply discount or premium if the sale is not active
function currentDiscount() public view returns (uint256) {
    if (!isSaleActive()) {
        return SCALAR;
    }

    uint256 decayDelta = startingPremium - maxDiscount;
    uint256 periodStart = getCurrentPeriodStartTime();
    uint256 periodEnd = getCurrentPeriodEndTime();
    uint256 saleTimeRemaining = periodEnd - block.timestamp;

    /// calculate the current premium or discount at the current time based
    /// on the length you are into the current period
    return
       maxDiscount +
        (decayDelta * saleTimeRemaining) /
        (periodEnd - periodStart);
}
\u0060\u0060\u0060

The value for \u0060periodStart\u0060 is obtained from the return of the \u0060getCurrentPeriodEndTime()\u0060 function, defined as follows:

\u0060\u0060\u0060solidity
/// @notice Returns the end time of the current mini auction period
/// @return The timestamp when the current mini auction period ends
/// @dev Returns 0 if no sale is active or if the sale hasn\u0027t started yet
/// @dev Each period is exactly miniAuctionPeriod in length
function getCurrentPeriodEndTime() public view returns (uint256) {
    uint256 startTime = getCurrentPeriodStartTime();
    if (startTime == 0) {
        return 0;
    }

    return startTime + miniAuctionPeriod - 1;
}
\u0060\u0060\u0060

In other words, the denominator becomes \u0060periodEnd - periodStart = miniAuctionPeriod - 1\u0060. If the \u0060miniAuctionPeriod\u0060 is set to \u00601\u0060 - which is possible, because the condition in the \u0060require\u0060 statement of the \u0060initiateSale()\u0060 function is as follows: \u0060_auctionPeriod / _miniAuctionPeriod > 1\u0060.

In extremely rare conditions, where \u0060_miniAuctionPeriod\u0060 is \u00601\u0060 and \u0060_auctionPeriod\u0060 is \u00602\u0060, then the denominator is zero and the contract will revert with a division-by-zero error.
## Recommendation
It is recommended to add an explicit check in the \u0060initiateSale()\u0060 function to ensure that \u0060_miniAuctionPeriod > 1\u0060. For example:
\u0060\u0060\u0060solidity
require(_miniAuctionPeriod > 1, "ReserveAutomation: Mini auction period too short");
\u0060\u0060\u0060
Alternatively, update the NatSpec documentation to provide proper information regarding the mini auction period.

## Remediation Comment
ACKNOWLEDGED: The Moonwell team has acknowledged this issue.
PAGE END
