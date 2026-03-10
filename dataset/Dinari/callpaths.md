# Callpaths — Dinari

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## DShare

_File: src/DShare.sol_

### public balanceOf
-> public sharesToBalance
  -> public balancePerShare
    -> private _getdShareStorage


### public balancePerShare
-> private _getdShareStorage


### public balanceToShares
-> public balancePerShare
  -> private _getdShareStorage


### external burn
-> internal _burn
  -> internal _beforeTokenTransfer
    -> private _getdShareStorage
  -> public balancePerShare
    -> private _getdShareStorage


### external burnFrom
-> internal _burn
  -> internal _beforeTokenTransfer
    -> private _getdShareStorage
  -> public balancePerShare
    -> private _getdShareStorage


### public initialize
-> private _getdShareStorage


### external isBlacklisted
-> private _getdShareStorage


### public maxSupply
-> public balancePerShare
  -> private _getdShareStorage


### external mint
-> internal _mint
  -> internal _beforeTokenTransfer
    -> private _getdShareStorage
  -> public balanceToShares
    -> public balancePerShare
      -> private _getdShareStorage
  -> public balancePerShare
    -> private _getdShareStorage
  -> public maxSupply
    -> public balancePerShare
      -> private _getdShareStorage


### public name
-> private _getdShareStorage


### public publicVersion
_(no internal calls)_


### external setBalancePerShare
-> private _getdShareStorage


### external setName
-> private _getdShareStorage


### external setSymbol
-> private _getdShareStorage


### external setTransferRestrictor
-> private _getdShareStorage


### public sharesOf
_(no internal calls)_


### public sharesToBalance
-> public balancePerShare
  -> private _getdShareStorage


### public symbol
-> private _getdShareStorage


### public totalSupply
-> public sharesToBalance
  -> public balancePerShare
    -> private _getdShareStorage


### public transfer
-> internal _transfer
  -> internal _beforeTokenTransfer
    -> private _getdShareStorage
  -> public balanceToShares
    -> public balancePerShare
      -> private _getdShareStorage


### public transferFrom
-> internal _transfer
  -> internal _beforeTokenTransfer
    -> private _getdShareStorage
  -> public balanceToShares
    -> public balancePerShare
      -> private _getdShareStorage


### public transferRestrictor
-> private _getdShareStorage


### public version
_(no internal calls)_


---

## DShareFactory

_File: src/DShareFactory.sol_

### external announceExistingDShare
-> internal _getDShareFactoryStorage


### external createDShare
-> internal _getDShareFactoryStorage


### external getDShareBeacon
-> internal _getDShareFactoryStorage


### external getDShares
-> internal _getDShareFactoryStorage


### external getTransferRestrictor
-> internal _getDShareFactoryStorage


### external getWrappedDShareBeacon
-> internal _getDShareFactoryStorage


### external initialize
-> internal __ControlledUpgradeable_init
-> internal _getDShareFactoryStorage


### external initializeV2
-> internal _getDShareFactoryStorage


### external isTokenDShare
-> internal _getDShareFactoryStorage


### external isTokenWrappedDShare
-> internal _getDShareFactoryStorage


### public publicVersion
_(no internal calls)_


### external reinitialize
-> internal __ControlledUpgradeable_init


### external setNewTransferRestrictor
-> internal _getDShareFactoryStorage


### public version
_(no internal calls)_


---

## DividendDistribution

_File: src/dividend/DividendDistribution.sol_

### external createDistribution
_(no internal calls)_


### external distribute
_(no internal calls)_


### public initialize
-> internal __ControlledUpgradeable_init


### public publicVersion
_(no internal calls)_


### external reclaimDistribution
_(no internal calls)_


### external setMinDistributionTime
_(no internal calls)_


### public version
_(no internal calls)_


---

## ERC20Rebasing

_File: src/ERC20Rebasing.sol_

### public balanceOf
-> public sharesToBalance


### public balanceToShares
_(no internal calls)_


### public maxSupply
_(no internal calls)_


### public sharesOf
_(no internal calls)_


### public sharesToBalance
_(no internal calls)_


### public totalSupply
-> public sharesToBalance


### public transfer
-> internal _transfer
  -> public balanceToShares


### public transferFrom
-> internal _transfer
  -> public balanceToShares


---

## FulfillmentRouter

_File: src/orders/FulfillmentRouter.sol_

### external cancelBuyOrder
_(no internal calls)_


### external fillOrder
_(no internal calls)_


### public initialize
-> internal __ControlledUpgradeable_init


### public publicVersion
_(no internal calls)_


### public reinitialize
_(no internal calls)_


### public version
_(no internal calls)_


---

## LatestPriceHelper

_File: src/orders/LatestPriceHelper.sol_

### external aggregateLatestPriceFromProcessor
-> external_callback IOrderProcessor.PricePoint


---

## Multicall3

_File: src/common/Multicall3.sol_

### public aggregate
_(no internal calls)_


### public aggregate3
_(no internal calls)_


### public aggregate3Value
_(no internal calls)_


### public blockAndAggregate
-> public tryBlockAndAggregate
  -> public tryAggregate


### public getBasefee
_(no internal calls)_


### public getBlockHash
_(no internal calls)_


### public getBlockNumber
_(no internal calls)_


### public getChainId
_(no internal calls)_


### public getCurrentBlockCoinbase
_(no internal calls)_


### public getCurrentBlockDifficulty
_(no internal calls)_


### public getCurrentBlockGasLimit
_(no internal calls)_


### public getCurrentBlockTimestamp
_(no internal calls)_


### public getEthBalance
_(no internal calls)_


### public getLastBlockHash
_(no internal calls)_


### public tryAggregate
_(no internal calls)_


### public tryBlockAndAggregate
-> public tryAggregate


---

## OrderProcessor

_File: src/orders/OrderProcessor.sol_

### external DOMAIN_SEPARATOR
_(no internal calls)_


### external cancelOrder
-> public hashOrder
-> private _getOrderProcessorStorage


### external createOrder
-> public hashOrder
-> private _validateFeeQuote
  -> public hashFeeQuote
  -> internal checkOperator
    -> private _getOrderProcessorStorage
-> private _createOrder
  -> private _getOrderProcessorStorage
  -> internal _checkBlacklisted
    -> internal _checkTransferLocked


### external createOrderStandardFees
-> public hashOrder
-> private _createOrder
  -> private _getOrderProcessorStorage
  -> internal _checkBlacklisted
    -> internal _checkTransferLocked
-> public getStandardFees
  -> private _getOrderProcessorStorage
  -> library FeeLib.flatFeeForOrder
-> library FeeLib.applyPercentageFee


### external createOrderWithSignature
-> public hashOrderRequest
  -> public hashOrder
-> public hashOrder
-> private _validateFeeQuote
  -> public hashFeeQuote
  -> internal checkOperator
    -> private _getOrderProcessorStorage
-> private _createOrder
  -> private _getOrderProcessorStorage
  -> internal _checkBlacklisted
    -> internal _checkTransferLocked


### external dShareFactory
-> private _getOrderProcessorStorage


### external fillOrder
-> public hashOrder
-> private _getOrderProcessorStorage
-> private _fillSellOrder
  -> private _publishFill
    -> private _getOrderProcessorStorage
    -> library OracleLib.pairIndex
    -> library OracleLib.calculatePrice
  -> private _updateFillState
    -> private _getOrderProcessorStorage
-> private _fillBuyOrder
  -> private _getOrderProcessorStorage
  -> private _publishFill
    -> private _getOrderProcessorStorage
    -> library OracleLib.pairIndex
    -> library OracleLib.calculatePrice
  -> private _updateFillState
    -> private _getOrderProcessorStorage


### external getFeesEscrowed
-> private _getOrderProcessorStorage


### external getFeesTaken
-> private _getOrderProcessorStorage


### external getOrderStatus
-> private _getOrderProcessorStorage


### public getPaymentTokenConfig
-> private _getOrderProcessorStorage


### external getReceivedAmount
-> private _getOrderProcessorStorage


### public getStandardFees
-> private _getOrderProcessorStorage
-> library FeeLib.flatFeeForOrder


### external getUnfilledAmount
-> private _getOrderProcessorStorage


### public hashFeeQuote
_(no internal calls)_


### public hashOrder
_(no internal calls)_


### public hashOrderRequest
-> public hashOrder


### public initialize
-> internal __ControlledUpgradeable_init
-> private _getOrderProcessorStorage


### external isOperator
-> private _getOrderProcessorStorage


### external isTransferLocked
-> private _getOrderProcessorStorage
-> internal _checkTransferLocked


### external latestFillPrice
-> private _getOrderProcessorStorage
-> library OracleLib.pairIndex


### external orderDecimalReduction
-> private _getOrderProcessorStorage


### external ordersPaused
-> private _getOrderProcessorStorage


### public publicVersion
_(no internal calls)_


### external reinitialize
-> internal __ControlledUpgradeable_init


### external removePaymentToken
-> private _getOrderProcessorStorage


### external requestCancel
-> private _getOrderProcessorStorage


### public selfPermit
_(no internal calls)_


### external setOperator
-> private _getOrderProcessorStorage


### external setOrderDecimalReduction
-> private _getOrderProcessorStorage


### external setOrdersPaused
-> private _getOrderProcessorStorage


### external setPaymentToken
-> library FeeLib.checkPercentageFeeRate
-> internal _checkTransferLocked
-> private _getOrderProcessorStorage


### external setTreasury
-> private _getOrderProcessorStorage


### external setVault
-> private _getOrderProcessorStorage


### public totalStandardFee
-> public getStandardFees
  -> private _getOrderProcessorStorage
  -> library FeeLib.flatFeeForOrder
-> library FeeLib.applyPercentageFee


### external treasury
-> private _getOrderProcessorStorage


### external vault
-> private _getOrderProcessorStorage


### public version
_(no internal calls)_


---

## SelfPermit

_File: src/common/SelfPermit.sol_

### public selfPermit
_(no internal calls)_


---

## TransferRestrictor

_File: src/TransferRestrictor.sol_

### public initialize
-> internal __ControlledUpgradeable_init


### public publicVersion
_(no internal calls)_


### public reinitialize
_(no internal calls)_


### external requireNotRestricted
_(no internal calls)_


### external restrict
_(no internal calls)_


### external unrestrict
_(no internal calls)_


### public version
_(no internal calls)_


---

## Vault

_File: src/orders/Vault.sol_

### public initialize
-> internal __ControlledUpgradeable_init


### public publicVersion
_(no internal calls)_


### public reinitialize
_(no internal calls)_


### external rescueERC20
_(no internal calls)_


### public version
_(no internal calls)_


### external withdrawFunds
_(no internal calls)_


---

## WrappedDShare

_File: src/WrappedDShare.sol_

### public asset
-> private _getWrappedDShareStorage


### public initialize
-> private _getWrappedDShareStorage


### external isBlacklisted
-> private _getWrappedDShareStorage


### public name
-> private _getWrappedDShareStorage


### public publicVersion
_(no internal calls)_


### external recover
-> private _getWrappedDShareStorage


### external setName
-> private _getWrappedDShareStorage


### external setSymbol
-> private _getWrappedDShareStorage


### public symbol
-> private _getWrappedDShareStorage


### public version
_(no internal calls)_

