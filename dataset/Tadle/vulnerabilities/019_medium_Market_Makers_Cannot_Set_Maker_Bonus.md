# Market Makers Cannot Set Maker Bonus

**Severity:** medium
**Auditor:** CodeHawks
**Protocol:** Tadle
**Keywords:** Market Makers, maker bonus, liquidity, protected offer, PreMarkets, listOffer, trade tax, functionality, vulnerability, smart contract, user input, collateral, market, offer, relisting, dynamic setting, fees, documentation, protocol, offer status

---

# PreMarkets::createOffer allows excessive eachTradeTax
### Relevant Links
- [PreMarkets.sol](https://github.com/Cyfrin/2024-08-tadle/blob/main/src/core/PreMarkets.sol#L39-L157)
- [Constants.sol](https://github.com/Cyfrin/2024-08-tadle/blob/main/src/libraries/Constants.sol#L20)

PreMarkets::createOffer allows a user to create an offer with eachTradeTax more than Constants.EACH_TRADE_TAX_MAXINUM. The user can even charge eachTradeTax of 10_000 (i.e. 100%).

eachTradeTax should not be more than Constants.EACH_TRADE_TAX_MAXINUM value i.e. 2000 (20%). The PreMarkets::createOffer only makes sure that the eachTradeTax isn\u0027t greater than Constants.EACH_TRADE_TAX_DECIMAL_SCALER i.e. 10_000.
\u0060\u0060\u0060solidity
if (params.eachTradeTax > Constants.EACH_TRADE_TAX_DECIMAL_SCALER) { 
    revert InvalidEachTradeTaxRate(); 
}
\u0060\u0060\u0060

- Likelihood: High
- Impact: High - User can charge a eachTradeTax value of more than EACH_TRADE_TAX_MAXINUM

Overall severity is High.

- Manual Review

Change the condition in PreMarkets::createOffer function
\u0060\u0060\u0060solidity
if (params.eachTradeTax > Constants.EACH_TRADE_TAX_DECIMAL_SCALER) { 
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
if (params.eachTradeTax > Constants.EACH_TRADE_TAX_MAXINUM) { 
    revert InvalidEachTradeTaxRate(); 
}
\u0060\u0060\u0060
## SystemConfig::MarketPlaceInfo.tokenPerPoint does not account for token decimals
amaron (https://profiles.cyfrin.io/u/amaron)

If the token that represents the points will have low decimals, and will represent much lower amounts than points, the protocol will not be able to provide the real ratio between each point and its token.

The SystemConfig::updateMarket allows the owners to provide the token address, and the ratio between each point and tokens (_tokenPerPoint).
## Token Ratio Issue in updateMarket Function

The following code snippet is part of the \u0060updateMarket\u0060 function:

\u0060\u0060\u0060solidity
function updateMarket( 
    string calldata _marketPlaceName, 
    address _tokenAddress, 
    uint256 _tokenPerPoint, 
    uint256 _tge, 
    uint256 _settlementPeriod 
) external onlyOwner { 
    address marketPlace = GenerateAddress.generateMarketPlaceAddress(_marketPlaceName); 
    MarketPlaceInfo storage marketPlaceInfo = marketPlaceInfoMap[marketPlace]; 
    if (marketPlaceInfo.status != MarketPlaceStatus.Online) { 
        revert MarketPlaceNotOnline(marketPlaceInfo.status); 
    } 
    marketPlaceInfo.tokenAddress = _tokenAddress; 
    marketPlaceInfo.tokenPerPoint = _tokenPerPoint; 
    marketPlaceInfo.tge = _tge; 
    marketPlaceInfo.settlementPeriod = _settlementPeriod; 
    emit UpdateMarket(_marketPlaceName, marketPlace, _tokenAddress, _tokenPerPoint, _tge, _settlementPeriod); 
}
\u0060\u0060\u0060

However, this is based on the assumption (which is not necessarily correct) that each point represents many more tokens, together with the decimal, for example: each point represents 1e18 tokens. However, if the points represent LESS than tokens * 10 ** token\u0027s decimals, the protocol will not be able to function by the real ratio.

Let\u0027s consider a scenario where a user sells 500,000 points: 

- Points: 500,000 
- The token\u0027s decimal is 2 (just for simplicity) and the 500,000 points represent 500 tokens. 
- The 500,000 points are equal to 50 * 10 ** 2 (which is 50,000); therefore the \u0060tokenPerPoint\u0060 should be 0.1, which cannot be passed as an input parameter to the \u0060updateMarket\u0060 function, and the protocol will not be able to update the ratio.

- Manual review

Consider implementing a mechanism in the protocol, where points are being stored together with decimals, then, the ratio can be manipulated with points and \u0060tokenPerPoint\u0060 to represent the real ratio.
## Market Makers Cannot Set Maker Bonus

### Submitted by honour (https://profiles.cyfrin.io/u/honour).

Based on information provided by the docs here, the Makers receive bonuses for providing liquidity. However, making a protected offer via \u0060PreMarkets::listOffer\u0060 is missing this functionality because there\u0027s no way for the maker to specify their maker bonus.
As mentioned in the docs here (https://tadle.gitbook.io/tadle/how-tadle-works/features-and-terminologies/maker-bonus), a Maker receives rewards (maker bonuses) for providing liquidity/collateral to the market. Makers are also allowed to dynamically set the percentage of fees they want to earn. Also important to note here is that for protected offers each subsequent re-listing creates a new Maker as seen by the docs here (https://tadle.gitbook.io/tadle/how-tadle-works/mechanics-of-tadle/protected-mode#for-sell-offers) (on Transaction #3) Bob is now a Maker. However the PreMarkets::listOffer does not include this functionality for protected offers and as seen in the code here (https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L381-L381), the trade tax (which is the maker bonus) is set to 0.
## Impact
MEDIUM - Market Makers via relisting protected offers cannot set their maker bonus.
## Tools Used
Manual Review

createTaker and listOffer should be modified as shown below:
## Vulnerability in \u0060listOffer\u0060 Function

\u0060\u0060\u0060solidity
function listOffer( 
    address _stock, 
    uint256 _amount, 
    uint256 _collateralRate, 
    uint256 _tradeTax 
) external payable { 
    //...ommited function body for brevity as it is irrelevant 
    /// @dev change abort offer status when offer settle type is turbo 
    if (makerInfo.offerSettleType == OfferSettleType.Turbo) { 
        address originOffer = makerInfo.originOffer; 
        OfferInfo memory originOfferInfo = offerInfoMap[originOffer]; 
        if (_collateralRate != originOfferInfo.collateralRate) { 
            revert InvalidCollateralRate(); 
        } 
        originOfferInfo.abortOfferStatus = AbortOfferStatus.SubOfferListed; 
    } 
    /// @dev transfer collateral when offer settle type is protected 
    if (makerInfo.offerSettleType == OfferSettleType.Protected) { 
        if (_tradeTax > Constants.EACH_TRADE_TAX_DECIMAL_SCALER) { 
            revert InvalidEachTradeTaxRate(); 
        } 
        uint256 transferAmount = OfferLibraries.getDepositAmount( 
            offerInfo.offerType, 
            offerInfo.collateralRate, 
            _amount, 
            true, 
            Math.Rounding.Ceil 
        ); 
        ITokenManager tokenManager = tadleFactory.getTokenManager(); 
        tokenManager.tillIn{value: msg.value}( 
            _msgSender(), 
            makerInfo.tokenAddress, 
            transferAmount, 
            false 
        ); 
    } 
    address offerAddr = GenerateAddress.generateOfferAddress(stockInfo.id); 
    if (offerInfoMap[offerAddr].authority != address(0x0)) { 
        revert OfferAlreadyExist(); 
    } 
    /// @dev update offer info 
    offerInfoMap[offerAddr] = OfferInfo({ 
        id: stockInfo.id, 
        authority: _msgSender(), 
        maker: offerInfo.maker, 
        offerStatus: OfferStatus.Virgin, 
        offerType: offerInfo.offerType, 
        abortOfferStatus: AbortOfferStatus.Initialized, 
        points: stockInfo.points, 
        amount: _amount, 
        collateralRate: _collateralRate, 
        usedPoints: 0, 
        tradeTax: makerInfo.offerSettleType == OfferSettleType.Turbo ? 0 : _tradeTax, 
        settledPoints: 0, 
        settledPointTokenAmount: 0, 
        settledCollateralAmount: 0 
    });
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
}); 
stockInfo.offer = offerAddr; 
emit ListOffer( 
    offerAddr, 
    _stock, 
    _msgSender(), 
    stockInfo.points, 
    _amount 
);
}
function createTaker(address _offer, uint256 _points) external payable { 
    // ...ommiteed function body for brevity 
    /// @dev Transfer token from user to capital pool as collateral 
    uint256 depositAmount = _points.mulDiv( 
        offerInfo.amount, 
        offerInfo.points, 
        Math.Rounding.Ceil 
    );
    uint256 platformFee = depositAmount.mulDiv( 
        platformFeeRate, 
        Constants.PLATFORM_FEE_DECIMAL_SCALER 
    );
    uint256 tradeTax = depositAmount.mulDiv( 
        -           makerInfo.eachTradeTax, 
        +           makerInfo.offerSettleType == OfferSettleType.Turbo ? makerInfo.eachTradeTax : offerInfo.tradeTax, 
        Constants.EACH_TRADE_TAX_DECIMAL_SCALER 
    );
    //...ommited remaining function body as it is irrelevant 
}
\u0060\u0060\u0060
PAGE END
