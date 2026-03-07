# Incorrect assumption that Chainlink always increments roundId by 1

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** Chainlink, roundId, Aggregator, price, stale, DoS, fetchPrice, mockOracle, update, error, function, response, timestamp, deviation, contract, test, mock, oracle, feed, aggregator

---

# Incorrect assumption that Chainlink always increments roundId by 1
**Submitted by:** T1MOH  
**Severity:** Medium Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** Here Chainlink docs explain that roundId packs 2 values:
1. Underlying Aggregator version.
2. Actual round id.

Here you can see it decrements current roundId to get previous price:
\u0060\u0060\u0060solidity
function _fetchPrevFeedResponse(
    IAggregatorV3Interface _priceAggregator,
    uint80 _currentRoundId
) internal view returns (FeedResponse memory prevResponse) {
    if (_currentRoundId != 0) {
        unchecked {
            try _priceAggregator.getRoundData(_currentRoundId - 1) returns (/*...*/) { // <<<
                prevResponse.roundId = roundId;
                prevResponse.answer = answer;
                prevResponse.timestamp = timestamp;
                prevResponse.success = true;
            } catch {}
        }
    }
}
\u0060\u0060\u0060

PriceFeed.fetchPrice() is used to query collateral price. Every time stored roundId becomes outdated, it fetches both current and previous price:
\u0060\u0060\u0060solidity
function fetchPrice(address _token) public returns (uint256 price) {
    // ...
        (FeedResponse memory currResponse, FeedResponse memory prevResponse, bool updated) =
        ֒→  _fetchFeedResponses( // <<<
            oracle.chainLinkOracle,
            priceRecord.roundId
        );
        if (!updated) {
            if (_isPriceStale(priceRecord.timestamp, oracle.heartbeat)) {
                revert PriceFeed__FeedFrozenError(_token);
            }
            price = priceRecord.scaledPrice;
        } else {
            price = _processFeedResponses(_token, oracle, currResponse, prevResponse, priceRecord); // <<<
        }
    }
}
\u0060\u0060\u0060

It will always mark feed isFeedWorking = false and revert because previous price becomes stale soon:
## Vulnerability in _processFeedResponses Function

\u0060\u0060\u0060solidity
function _processFeedResponses(
  address _token,
  OracleRecord memory oracle,
  FeedResponse memory _currResponse,
  FeedResponse memory _prevResponse,
  PriceRecord memory priceRecord
) internal returns (uint256 scaledPrice) {
  uint8 decimals = oracle.decimals;
  //@audit always false after Aggregator update
  bool isValidResponse = _isFeedWorking(_currResponse, _prevResponse) &&
    !_isPriceStale(_currResponse.timestamp, oracle.heartbeat) &&
    !_isPriceChangeAboveMaxDeviation(_currResponse, _prevResponse, decimals);
  if (isValidResponse) {
    // ...
  } else {
    if (oracle.isFeedWorking) {
      _updateFeedStatus(_token, oracle, false);
    }
    if (_isPriceStale(priceRecord.timestamp, oracle.heartbeat)) {
      revert PriceFeed__FeedFrozenError(_token); // <<<
    }
    scaledPrice = priceRecord.scaledPrice;
  }
}
\u0060\u0060\u0060

As a result, price can\u0027t be fetched in subsequent round after Aggregator update. It means temporary DoS, when core functionality doesn\u0027t work: openTrove, redeemTrove, closeTrove, liquidations.

Insert this function into \u0060test/foundry/poc.t.sol\u0060:

\u0060\u0060\u0060solidity
function test_custom2_T1MOH() public {
  mockOracle.refresh();
  skip(1);
  sbtc2TroveManager.fetchPrice(); // no revert
  skip(1);
  MockOracle_PoC newOracle = new MockOracle_PoC();
  newOracle.setRoundId(mockOracle.roundId());
  skip(1);
  priceFeed.setOracle(
    address(stakedBTC2),
    address(newOracle),
    80000, // heartbeat
    bytes4(0x00000000),
    18,
    false
  );
  skip(1);
  sbtc2TroveManager.fetchPrice(); // no revert
  skip(50_000);
  newOracle.upgradeAggregatorVersionAndUpdatePrice();
  skip(40_000);
  vm.expectRevert();
  sbtc2TroveManager.fetchPrice(); // will revert
}
\u0060\u0060\u0060

### Additional Contract
Add another contract to this file:

\u0060\u0060\u0060solidity
contract MockOracle_PoC {
  uint80 public roundId;
  int256 public answer;
  uint256 public startedAt;
  uint256 public updatedAt;
  uint80 public answeredInRound;
  struct Price {
    uint80 roundId;
    int256 answer;
    uint256 startedAt;
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 updatedAt;
uint80 answeredInRound;
}
mapping(uint80 roundId => Price) prices;
constructor() {
    roundId = 12345;
    answer = 60000 * 10 ** 8;
    startedAt = block.timestamp;
    updatedAt = block.timestamp;
    answeredInRound = 12345;
    prices[roundId] = Price(roundId, answer, startedAt, updatedAt, answeredInRound);
}
function upgradeAggregatorVersionAndUpdatePrice() public {
    roundId = uint80(1 << 64) + roundId + 1;
    answer = 60000 * 10 ** 8;
    startedAt = block.timestamp;
    updatedAt = block.timestamp;
    answeredInRound = roundId;
    prices[roundId] = Price(roundId, answer, startedAt, updatedAt, answeredInRound);
}
function setResponse(
    uint80 _roundId,
    int256 _answer,
    uint256 _startedAt,
    uint256 _updatedAt,
    uint80 _answeredInRound
) external {
    roundId = _roundId;
    answer = _answer;
    startedAt = _startedAt;
    updatedAt = _updatedAt;
    answeredInRound = _answeredInRound;
}
function refresh() external {
    ++roundId;
    ++answeredInRound;
    updatedAt = block.timestamp;
    prices[roundId] = Price(roundId, answer, startedAt, updatedAt, answeredInRound);
}
function setRoundId(uint80 _newRoundId) public {
    roundId = _newRoundId;
    answeredInRound = roundId;
    prices[roundId] = Price(roundId, answer, startedAt, updatedAt, answeredInRound);
}
function decimals() external pure returns (uint8) {
    return 8;
}
function description() external pure returns (string memory) {
    return "BTC / USD";
}
function version() external pure returns (uint256) {
    return 4;
}
function getRoundData(uint80 _roundId) external view returns (uint80, int256, uint256, uint256, uint80) {
    Price memory a = prices[_roundId];
    return (a.roundId, a.answer, a.startedAt, a.updatedAt, a.answeredInRound);
}
function latestRoundData() external view returns (uint80, int256, uint256, uint256, uint80) {
    Price memory a = prices[roundId];
    return (a.roundId, a.answer, a.startedAt, a.updatedAt, a.answeredInRound);
}
\u0060\u0060\u0060
And slightly modify setup (it messes mock price updates):
