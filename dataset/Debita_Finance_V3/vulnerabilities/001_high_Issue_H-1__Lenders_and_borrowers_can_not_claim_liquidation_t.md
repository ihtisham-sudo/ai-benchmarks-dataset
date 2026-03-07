# Issue H-1: Lenders and borrowers can not claim liquidation token after NFT collateral auction sold

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Debita Finance V3
**Keywords:** NFT, liquidation, auction, collateral, borrower, lender, receipt, function, claim, token, default, debt, withdraw, transfer, contract, error, revert, payment, logic, decimals

---

# Issue H-1: Lenders and borrowers can not claim liquidation token after NFT collateral auction sold

Source: [GitHub Issue #156](https://github.com/sherlock-audit/2024-10-debita-judging/issues/156)  
Found by: 0xc0ffEE  

The incorrect logic in function \u0060veNFTAerodrome::getDataByReceipt()\u0060 will cause the lenders and borrowers unable to claim liquidation token after the NFT auction sold.  

- The function \u0060DebitaV3Loan::claimCollateralAsNFTLender()\u0060 allows the lenders to claim the liquidation token after the NFT collateral auction is sold.  
- The function \u0060DebitaV3Loan::claimCollateralNFTAsBorrower()\u0060 allows the borrower to claim the liquidation token in case of partial default.  
- The 2 functions above call \u0060veNFTAerodrome::getDataByReceipt()\u0060 to retrieve the liquidation token\u0027s decimals to calculate the payment amount.  
- These 2 flows above can be reverted because of unhandled case in the function \u0060veNFTAerodrome::getDataByReceipt()\u0060. The mentioned unhandled case is when there is no owner of the receipt token, such that \u0060ownerOf(receiptID)\u0060 reverts because of non-existent token.  

\u0060\u0060\u0060solidity
function getDataByReceipt(
  uint receiptID
) public view returns (receiptInstance memory) {
  veNFT veContract = veNFT(nftAddress);
  veNFTVault vaultContract = veNFTVault(s_ReceiptID_to_Vault[receiptID]);
  uint nftID = vaultContract.attached_NFTID();
  IVotingEscrow.LockedBalance memory _locked = veContract.locked(nftID);
  uint _decimals = ERC20(_underlying).decimals();
  address manager = vaultContract.managerAddress();
  address currentOwnerOfReceipt = ownerOf(receiptID);
  receiptInstance memory receiptData = receiptInstance({
    receiptID: receiptID,
    attachedNFT: nftID,
    lockedAmount: uint(int(_locked.amount)),
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
lockedDate: _locked.end,
decimals: _decimals,
vault: address(vaultContract),
underlying: _underlying,
OwnerIsManager: manager == currentOwnerOfReceipt
});
return receiptData;
}
function ownerOf(uint256 tokenId) public view virtual returns (address) {
return _requireOwned(tokenId);
}
...
function _requireOwned(uint256 tokenId) internal view returns (address) {
address owner = _ownerOf(tokenId);
if (owner == address(0)) {
@>      revert ERC721NonexistentToken(tokenId);
}
return owner;
}
This state can be reached when the auction buyer withdraws veNFT by calling
veNFTVault::withdraw(), which will burn the receipt token
function withdraw() external nonReentrant {
IERC721 veNFTContract = IERC721(veNFTAddress);
IReceipt receiptContract = IReceipt(factoryAddress);
uint m_idFromNFT = attached_NFTID;
address holder = receiptContract.ownerOf(receiptID);
// RECEIPT HAS TO BE ON OWNER WALLET
require(attached_NFTID != 0, "No attached nft");
require(holder == msg.sender, "Not Holding");
receiptContract.decrease(managerAddress, m_idFromNFT);
delete attached_NFTID;
// First: burn receipt
@>    IReceipt(factoryAddress).burnReceipt(receiptID);
IReceipt(factoryAddress).emitWithdrawn(address(this), m_idFromNFT);
// Second: send them their NFT
veNFTContract.transferFrom(address(this), msg.sender, m_idFromNFT);
}
function burnReceipt(uint id) external onlyVault {
@>    _burn(id);
}
\u0060\u0060\u0060
No response

No response

- A borrower deposits veNFT to veNFTVault by calling veNFTAerodrome::deposit(), effectively receives a Receipt token
- The borrower creates borrow offer with the above Receipt token as collateral
- The borrow offer is matched with many lend offers
- The borrower does not pay debt for all lend offers before the deadline and a lender calls createAuctionForCollateral to create an auction for the collateral
- Auction is sold
- The auction buyer, now the current holder of the Receipt token, decides to withdraw the veNFT from the vault by calling veNFTVault::withdraw()
- At this time, both borrower and lenders cannot claim liquidation token

- Loss of liquidation for both lenders and borrower

Update the test testDefaultAndAuctionCall in file test/fork/Loan/ltv/OracleOneLenderLoanReceipt.t.sol as below:

\u0060\u0060\u0060solidity
function testDefaultAndAuctionCall() public {
    MatchOffers();
    uint256[] memory indexes = allDynamicData.getDynamicUintArray(1);
    indexes[0] = 0;
    vm.warp(block.timestamp + 8640010);
    DebitaV3LoanContract.createAuctionForCollateral(0);
    DutchAuction_veNFT auction = DutchAuction_veNFT(DebitaV3LoanContract.getAuctionData().auctionAddress);
    DutchAuction_veNFT.dutchAuction_INFO memory auctionData = auction.getAuctionData();
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
vm.warp(block.timestamp + (86400 * 10) + 1);
address buyer = 0x5C235931376b21341fA00d8A606e498e1059eCc0;
deal(AERO, buyer, 100e18);
vm.startPrank(buyer);
AEROContract.approve(address(auction), 100e18);
auction.buyNFT();
vm.stopPrank();
address ownerOfNFT = receiptContract.ownerOf(receiptID);
// buyer withdraws NFT
vm.startPrank(ownerOfNFT);
address vaultAddress = receiptContract.s_ReceiptID_to_Vault(receiptID);
veNFTVault vault = veNFTVault(vaultAddress);
vault.withdraw();
// lender claim liquidation token
vm.stopPrank();
vm.expectRevert();
DebitaV3LoanContract.claimCollateralAsLender(0);
\u0060\u0060\u0060

Runthetestandconsoleshows:
Ran 1 test for
→ test/fork/Loan/ltv/OracleOneLenderLoanReceipt.t.sol:DebitaAggregatorTest
[PASS] testDefaultAndAuctionCall() (gas: 3381044)

1. Update the function getDataByReceipt() to handle the case non-exist token, instead of reverting
2. OR update the logic to fetch the decimals in functions claimCollateralAsNFTLender and claimCollateralNFTAsBorrower

sherlock-admin2
The protocol team fixed this issue in the following PRs/commits:
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/8eb4deaff92b143dfb838f0eda8c5adeca2fac8c
## Issue H-2: Nobody can buy the TaxTokenReceiptNFT from auction

Source: [GitHub Issue #388](https://github.com/sherlock-audit/2024-10-debita-judging/issues/388)  
Found by: 0x37, 0xPhantom2, KaplanLabs, KiroBrejka, bbl4de, dhank, dimulski, tmotfl, xiaoming90


Nobody can buy the TaxTokenReceiptNFT from auction due to the overridden \u0060transferFrom\u0060 function. The \u0060transferFrom\u0060 function is overridden with the following checks:

\u0060\u0060\u0060solidity
function transferFrom(
    address from,
    address to,
    uint256 tokenId
) public virtual override(ERC721, IERC721) {
    bool isReceiverAddressDebita = IBorrowOrderFactory(borrowOrderFactory)
        .isBorrowOrderLegit(to) ||
        ILendOrderFactory(lendOrderFactory).isLendOrderLegit(to) ||
        IAggregator(Aggregator).isSenderALoan(to);
    bool isSenderAddressDebita = IBorrowOrderFactory(borrowOrderFactory)
        .isBorrowOrderLegit(from) ||
        ILendOrderFactory(lendOrderFactory).isLendOrderLegit(from) ||
        IAggregator(Aggregator).isSenderALoan(from);
    // Debita not involved --> revert
    require(
        isReceiverAddressDebita || isSenderAddressDebita,
        "TaxTokensReceipts: Debita not involved"
    );
}
\u0060\u0060\u0060

This ensures that the transfer of the NFT will go smoothly through the system, but one thing is missing. The thing is that if a borrower doesn\u0027t pay off his debt amount and the loan is auctioned, nobody will be able to buy the NFT off. This is because the \u0060transferFrom\u0060 function requires for the from and to addresses to be either a Borrow Order, Lend Order or a Loan to be able to transfer the receipt NFT. At the point when the NFT is in the Auction contract it will be too late because neither the Auction contract nor the msg.sender is or can be one of the listed. This means that it is impossible to get any amount of collateral token out of the NFT, which means that the lenders will experience a big loss of funds.

The modifications of the ERC721::transferFrom function

Tax Token Receipt being used as loan collateral

None

1. User makes Borrow Order with Tax Token Receipt NFT as collateral
2. The offer is matched and a loan is now created.
3. Borrower doesn\u0027t pay his loan off
4. Loan is auctioned and the NFT is transferred to the created auction (Up to this moment everything is going smoothly because at least one address in the sequence meets the criteria of being either a Borrow Order, Loan Order or a Loan)
5. At this point there is no eligible address since the Auction address doesn\u0027t meet the criteria and the msg.sender is just unable to meet it since neither the Borrow Order nor the Lend Order can call Auction::buyNFT function.

Lenders will experience big loss of funds, since the NFT can\u0027t be sold. Borrower will go off with their principal token and money that they should get in the form of NFT underlying are frozen forever.

No response

Add a check to the Tax Token Receipt NFT that ensures that an auction is active (Has an index different than 0 in the auctionFactoryDebita::AuctionOrderIndex mapping) and it is part of the Debita system (as it is indeed part of the system)

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/77653c1b2b5aacdbf  
4ae340d50504e056b8d8540
## Issue H-3: Managed veAERO NFT can be exploited to steal funds from lenders

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/535)  
Found by: KaplanLabs, xiaoming90  

No response  

No response  

No response  

No response  

### Instance 1
The Aerodrome\u0027s veAERONFT can be an unmanaged veNFT or managed veNFT. A managed veAERONFT (also called (m)veAERONFT) operates like a vault that allows users to deposit and withdraw their unmanaged veNFT into the managed veNFT via the Voter.depositManaged and Voter.withdrawManaged functions. Thus, the locked amount within the (m)veAERONFT can increase or decrease.

Bob, the malicious user, owns a (m)veAERONFT and locks his unmanaged veNFT worth 1,000,000 AERO within it. He then converts it into an NFT receipt and uses it as collateral in his borrow offer. The borrow offer intends to exchange borrow 1,000,000 USDC at the price/ratio of 1 AERO = 1 USDC.

Bob then matches his borrow order against other users\u0027 lending orders via the permissionless DebitaV3Aggregator.matchOffersV3 function himself. A new Loan
contract is created, and 1,000,000 USDC is sent to Bob\u0027s wallet, and the (m)ve AERO NFT is transferred into the Loan contract. Next, Bob calls the Voter.withdrawManaged function to withdraw his unmanaged veNFT, which is worth 1,000,000 AERO, from the (m)ve AERO NFT. As a result, the (m)ve AERO NFT collateral within the Loan becomes worthless now. Bob now holds 1,000,000 USDC and 1,000,000 AERO. Bob defaults on the Loan, and the (m)ve AERO NFT will be auctioned. Since the (m)ve AERO NFT is worthless, no one will purchase it, and the lender will not get any funds back and will lose 1,000,000 USDC.
## Instance 2

Any mechanism that relies on NFT receipt will be vulnerable to such an issue by exploiting the managed veNFT. Another instance that is affected by a similar issue is the BuyOrder.sellNFT function, where the NFT receipt with managed veNFT is placed within a buy order and put up for sale. Once the NFT receipt is sold, the seller can proceed to withdraw all the locked amount within the NFT receipt, leaving the buyer with a worthless NFT receipt. Since the root cause is similar, the attack path will be omitted for brevity.


High. Loss of assets for lenders and buyers.


No response


No response


sherlock-admin2 The protocol team fixed this issue in the following PRs/commits: [https://github.com/DebitaFinance/Debita-V3-Contracts/commit/992eb89cb38543a8f](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/992eb89cb38543a8f) a4d168fef79e2f1c8ab67e2
## Issue H-4: No one can sell TaxTokensReceipts NFT receipt to the buy order

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/560)  
The protocol has acknowledged this issue.  
Found by: 0x37, KiroBrejka, bbl4de, dimulski, xiaoming90  

No response  

No response  

No response  

No response  

The TaxTokensReceipts NFT receipt exists to allow FOT to be used within the Debita ecosystem. If users have any tokens that charge a tax/fee on transfer, they must deposit them into the TaxTokensReceipts NFT receipt and use the NFT within the Debita ecosystem.  

The new Debita protocol has a new feature called “Buy Order” or “Limit Order” that allows users to create buy orders, providing a mechanism for injecting liquidity to purchase specific receipts at predetermined ratios. The receipts include the TaxTokensReceipts NFT receipt.  

Assume that Bob creates a new Buy Order to purchase TaxTokensReceipts NFT receipt. Alice, the holder of TaxTokensReceipts NFT receipt, decided to sell it to Bob\u0027s Buy Order.
Thus, she called the \u0060buyOrder.sellNFT()\u0060 function, and Line 99 below will attempt to transfer Alice\u0027s TaxTokensReceipts NFT receipt to the Buy Order contract.

[Link to buyOrder.sol](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/buyOrders/buyOrder.sol#L99)

\u0060\u0060\u0060solidity
File: buyOrder.sol
092:     function sellNFT(uint receiptID) public {
093:         require(buyInformation.isActive, "Buy order is not active");
094:         require(
095:             buyInformation.availableAmount > 0,
096:             "Buy order is not available"
097:         );
098:
099:         IERC721(buyInformation.wantedToken).transferFrom(
100:             msg.sender,
101:             address(this),
102:             receiptID
103:         );
\u0060\u0060\u0060

However, the transfer will always revert because the transfer function has been overwritten, as shown below. The transfer function has been overwritten to only allow the transfer to proceed if the to or from involves the following three (3) contracts:
1. BorrowOrderContract
2. LendOrderContract
3. LoanContract

Since neither the BuyOrder contract nor the seller (Alice) is the above three contracts, the transfer will always fail. Thus, there is no way for anyone to sell their TaxTokensReceipts NFT receipt to the buy order. Thus, this feature is effectively broken.

[Link to TaxTokensReceipt.sol](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/Non-Fungible-Receipts/TaxTokensReceipts/TaxTokensReceipt.sol#L98)

\u0060\u0060\u0060solidity
File: TaxTokensReceipt.sol
093:     function transferFrom(
094:         address from,
095:         address to,
096:         uint256 tokenId
097:     ) public virtual override(ERC721, IERC721) {
098:         bool isReceiverAddressDebita = IBorrowOrderFactory(borrowOrderFactory)
099:             .isBorrowOrderLegit(to) ||
100:             ILendOrderFactory(lendOrderFactory).isLendOrderLegit(to) ||
101:             IAggregator(Aggregator).isSenderALoan(to);
102:         bool isSenderAddressDebita = IBorrowOrderFactory(borrowOrderFactory)
103:             .isBorrowOrderLegit(from) ||
104:             ILendOrderFactory(lendOrderFactory).isLendOrderLegit(from) ||
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
        function transferFrom(
            address from,
            address to,
            uint256 tokenId
        ) public virtual override(ERC721, IERC721) {
            bool isReceiverAddressDebita = IBorrowOrderFactory(borrowOrderFactory)
                .isBorrowOrderLegit(to) ||
                ILendOrderFactory(lendOrderFactory).isLendOrderLegit(to) ||
                IBuyOrderFactory(buyOrderFactory).isBuyOrderLegit(to) ||
                IAggregator(Aggregator).isSenderALoan(to);
            bool isSenderAddressDebita = IBorrowOrderFactory(borrowOrderFactory)
                .isBorrowOrderLegit(from) ||
                ILendOrderFactory(lendOrderFactory).isLendOrderLegit(from) ||
                IBuyOrderFactory(buyOrderFactory).isBuyOrderLegit(from) ||
                IAggregator(Aggregator).isSenderALoan(from);
            // Debita not involved --> revert
            require(
                isReceiverAddressDebita || isSenderAddressDebita,
                "TaxTokensReceipts: Debita not involved"
            );
\u0060\u0060\u0060

Medium. Core protocol functionality (BuyOrder/LimitOrder) is broken.

No response

BuyOrder contract must be authorized to transfer TaxTokensReceipt NFT as it is also part of the Debita protocol.
