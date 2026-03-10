# Callpaths — Debita_Finance_V3

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BuyOrder

_File: contracts/buyOrders/buyOrder.sol_

### public deleteBuyOrder
-> library SafeERC20.safeTransfer


### public getBuyInfo
_(no internal calls)_


### public initialize
_(no internal calls)_


### public sellNFT
-> library SafeERC20.safeTransfer


---

## DBOFactory

_File: contracts/DebitaBorrowOffer-Factory.sol_

### external createBorrowOrder
_(no internal calls)_


### external deleteBorrowOrder
_(no internal calls)_


### external emitDelete
_(no internal calls)_


### external emitUpdate
_(no internal calls)_


### external getActiveBorrowOrders
_(no internal calls)_


### external setAggregatorContract
_(no internal calls)_


---

## DBOImplementation

_File: contracts/DebitaBorrowOffer-Implementation.sol_

### public acceptBorrowOffer
-> public getBorrowInfo
-> library SafeERC20.safeTransfer


### public cancelOffer
-> public getBorrowInfo
-> library SafeERC20.safeTransfer


### public getBorrowInfo
_(no internal calls)_


### public initialize
_(no internal calls)_


### public updateBorrowOrder
-> public getBorrowInfo


---

## DLOFactory

_File: contracts/DebitaLendOfferFactory.sol_

### external createLendOrder
_(no internal calls)_


### external deleteOrder
_(no internal calls)_


### external emitDelete
_(no internal calls)_


### external emitUpdate
_(no internal calls)_


### public getActiveOrders
_(no internal calls)_


### external setAggregatorContract
_(no internal calls)_


---

## DLOImplementation

_File: contracts/DebitaLendOffer-Implementation.sol_

### public acceptLendingOffer
-> library SafeERC20.safeTransfer


### public addFunds
-> library SafeERC20.safeTransferFrom


### public cancelOffer
-> library SafeERC20.safeTransfer


### public changePerpetual
_(no internal calls)_


### public getLendInfo
_(no internal calls)_


### public initialize
_(no internal calls)_


### public updateLendOrder
_(no internal calls)_


---

## DebitaChainlink

_File: contracts/oracles/DebitaChainlink.sol_

### public changeManager
_(no internal calls)_


### public changeMultisig
_(no internal calls)_


### public checkSequencer
_(no internal calls)_


### public getDecimals
_(no internal calls)_


### public getThePrice
-> public checkSequencer


### public pauseContract
_(no internal calls)_


### public pauseStatuspriceFeed
_(no internal calls)_


### public reactivateContract
_(no internal calls)_


### public reactivateStatuspriceFeed
_(no internal calls)_


### public setPriceFeeds
_(no internal calls)_


---

## DebitaIncentives

_File: contracts/DebitaIncentives.sol_

### public claimIncentives
-> public currentEpoch
-> public hashVariables
-> public hashVariablesT


### public currentEpoch
_(no internal calls)_


### public deprecatePrinciple
_(no internal calls)_


### public getBribesPerEpoch
-> public hashVariables


### public hashVariables
_(no internal calls)_


### public hashVariablesT
_(no internal calls)_


### public incentivizePair
-> public currentEpoch
-> public hashVariables


### public setAggregatorContract
_(no internal calls)_


### public updateFunds
-> public currentEpoch
-> public hashVariables


### public whitelListCollateral
_(no internal calls)_


---

## DebitaPyth

_File: contracts/oracles/DebitaPyth.sol_

### public changeManager
_(no internal calls)_


### public changeMultisig
_(no internal calls)_


### public getDecimals
_(no internal calls)_


### public getThePrice
_(no internal calls)_


### public pauseContract
_(no internal calls)_


### public pauseStatusPriceId
_(no internal calls)_


### public reactivateContract
_(no internal calls)_


### public reactivateStatusPriceId
_(no internal calls)_


### public setPriceFeeds
_(no internal calls)_


---

## DebitaV3Aggregator

_File: contracts/DebitaV3Aggregator.sol_

### public changeOwner
_(no internal calls)_


### public emitLoanUpdated
_(no internal calls)_


### external getAllLoans
_(no internal calls)_


### external matchOffersV3
-> internal getPriceFrom
-> external_callback DebitaV3Loan.infoOfOffers


### external setNewFee
_(no internal calls)_


### external setNewFeeConnector
_(no internal calls)_


### external setNewMaxFee
_(no internal calls)_


### external setNewMinFee
_(no internal calls)_


### external setOracleEnabled
_(no internal calls)_


### external setValidNFTCollateral
_(no internal calls)_


### public statusCreateNewOffers
_(no internal calls)_


---

## DebitaV3Loan

_File: contracts/DebitaV3Loan.sol_

### public calculateInterestToPay
_(no internal calls)_


### external claimCollateralAsBorrower
-> internal claimCollateralNFTAsBorrower
-> internal claimCollateralERC20AsBorrower


### external claimCollateralAsLender
-> public nextDeadline
-> internal claimCollateralAsNFTLender


### external claimDebt
-> internal _claimDebt
-> internal claimInterest


### external createAuctionForCollateral
-> internal safeGetOwner
-> public nextDeadline
-> external_callback auctionFactory.getLiquidationFloorPrice
-> external_callback auctionFactory.createAuction


### public extendLoan
-> public nextDeadline
-> public calculateInterestToPay


### public getAuctionData
_(no internal calls)_


### public getLoanData
_(no internal calls)_


### external handleAuctionSell
_(no internal calls)_


### public initialize
_(no internal calls)_


### public nextDeadline
_(no internal calls)_


### public payDebt
-> public nextDeadline
-> public calculateInterestToPay


---

## DutchAuction_veNFT

_File: contracts/auctions/Auction.sol_

### public buyNFT
-> public getCurrentPrice


### public cancelAuction
_(no internal calls)_


### public editFloorPrice
_(no internal calls)_


### public getAuctionData
_(no internal calls)_


### public getCurrentPrice
_(no internal calls)_


---

## MixOracle

_File: contracts/oracles/MixOracle/MixOracle.sol_

### public changeMultisig
_(no internal calls)_


### public getThePrice
_(no internal calls)_


### public pauseContract
_(no internal calls)_


### public pauseStatusPriceId
_(no internal calls)_


### public reactivateContract
_(no internal calls)_


### public reactivateStatusPriceId
_(no internal calls)_


### public setAttachedTarotPriceOracle
_(no internal calls)_


### public setManager
_(no internal calls)_


---

## Ownerships

_File: contracts/DebitaLoanOwnerships.sol_

### public burn
_(no internal calls)_


### public mint
_(no internal calls)_


### public setDebitaContract
_(no internal calls)_


### public tokenURI
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


---

## TarotPriceOracle

_File: contracts/oracles/MixOracle/TarotOracle/TarotPriceOracle.sol_

### public getBlockTimestamp
_(no internal calls)_


### external getResult
-> public getBlockTimestamp
-> internal getPriceCumulativeCurrent
  -> public getBlockTimestamp
-> internal toUint224


### external initialize
-> internal getPriceCumulativeCurrent
  -> public getBlockTimestamp
-> public getBlockTimestamp


---

## TaxTokensReceipts

_File: contracts/Non-Fungible-Receipts/TaxTokensReceipts/TaxTokensReceipt.sol_

### public deposit
_(no internal calls)_


### public getDataByReceipt
_(no internal calls)_


### public getHoldingReceiptsByAddress
-> public getDataByReceipt


### public transferFrom
_(no internal calls)_


### public withdraw
_(no internal calls)_


---

## auctionFactoryDebita

_File: contracts/auctions/AuctionFactory.sol_

### external _deleteAuctionOrder
_(no internal calls)_


### public changeAuctionFee
_(no internal calls)_


### public changeOwner
_(no internal calls)_


### public changePublicAuctionFee
_(no internal calls)_


### public createAuction
_(no internal calls)_


### public emitAuctionDeleted
_(no internal calls)_


### public emitAuctionEdited
_(no internal calls)_


### external getActiveAuctionOrders
_(no internal calls)_


### public getHistoricalAmount
_(no internal calls)_


### public getHistoricalAuctions
_(no internal calls)_


### public getLiquidationFloorPrice
_(no internal calls)_


### public setAggregator
_(no internal calls)_


### public setFeeAddress
_(no internal calls)_


### public setFloorPriceForLiquidations
_(no internal calls)_


---

## buyOrderFactory

_File: contracts/buyOrders/buyOrderFactory.sol_

### public _deleteBuyOrder
_(no internal calls)_


### public changeFee
_(no internal calls)_


### public changeOwner
_(no internal calls)_


### public createBuyOrder
-> library SafeERC20.safeTransferFrom


### public emitDelete
_(no internal calls)_


### public emitUpdate
_(no internal calls)_


### public getActiveBuyOrders
_(no internal calls)_


### public getHistoricalBuyOrders
_(no internal calls)_


---

## veNFTAerodrome

_File: contracts/Non-Fungible-Receipts/veNFTS/Aerodrome/Receipt-veNFT.sol_

### external burnReceipt
_(no internal calls)_


### external claimBribesMultiple
-> internal emitInteracted


### external decrease
_(no internal calls)_


### external deposit
_(no internal calls)_


### external emitWithdrawn
_(no internal calls)_


### external extendMultiple
_(no internal calls)_


### public getDataByReceipt
_(no internal calls)_


### external getDataFromUser
_(no internal calls)_


### public getHoldingReceiptsByAddress
-> public getDataByReceipt


### external increase
_(no internal calls)_


### external lastReceiptID
_(no internal calls)_


### external pokeMultiple
-> internal emitInteracted


### external resetMultiple
_(no internal calls)_


### external voteMultiple
_(no internal calls)_


---

## veNFTEqualizer

_File: contracts/Non-Fungible-Receipts/veNFTS/Equalizer/Receipt-veNFT.sol_

### external burnReceipt
_(no internal calls)_


### external claimBribesMultiple
-> internal emitInteracted


### external decrease
_(no internal calls)_


### external deposit
_(no internal calls)_


### external emitWithdrawn
_(no internal calls)_


### external extendMultiple
_(no internal calls)_


### public getDataByReceipt
_(no internal calls)_


### external getDataFromUser
_(no internal calls)_


### public getHoldingReceiptsByAddress
-> public getDataByReceipt


### external increase
_(no internal calls)_


### external lastReceiptID
_(no internal calls)_


### external pokeMultiple
-> internal emitInteracted


### external resetMultiple
_(no internal calls)_


### external voteMultiple
_(no internal calls)_


---

## veNFTVault

_File: contracts/Non-Fungible-Receipts/veNFTS/Equalizer/veNFTEqualizer.sol_

### external changeManager
_(no internal calls)_


### external claimBribes
-> internal getVoterContract_veNFT


### external extendLock
_(no internal calls)_


### external poke
-> internal getVoterContract_veNFT


### external reset
-> internal getVoterContract_veNFT


### external vote
-> internal getVoterContract_veNFT


### external withdraw
_(no internal calls)_

