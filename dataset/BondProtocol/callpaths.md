# Callpaths — BondProtocol

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BondAggregator

_File: src/BondAggregator.sol_

### external currentCapacity
_(no internal calls)_


### external findMarketFor
-> public marketsFor
  -> public liveMarketsFor
    -> public isLive
  -> public isLive


### external getAuctioneer
_(no internal calls)_


### external getTeller
_(no internal calls)_


### external isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### external liveMarketsBetween
-> public isLive


### external liveMarketsBy
_(no internal calls)_


### public liveMarketsFor
-> public isLive


### public marketPrice
_(no internal calls)_


### external marketScale
_(no internal calls)_


### public marketsFor
-> public liveMarketsFor
  -> public isLive
-> public isLive


### external maxAmountAccepted
_(no internal calls)_


### public payoutFor
_(no internal calls)_


### external registerAuctioneer
_(no internal calls)_


### external registerMarket
_(no internal calls)_


---

## BondBaseFPA

_File: src/bases/BondBaseFPA.sol_

### external closeMarket
_(no internal calls)_


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
_(no internal calls)_


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice


### public maxPayout
-> public marketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
-> public maxPayout
  -> public marketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondBaseOFDA

_File: src/bases/BondBaseOFDA.sol_

### external closeMarket
_(no internal calls)_


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
_(no internal calls)_


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice


### public maxPayout
-> public marketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
-> public maxPayout
  -> public marketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> public marketPrice


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondBaseOSDA

_File: src/bases/BondBaseOSDA.sol_

### external closeMarket
-> internal _close


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice
    -> internal _currentMarketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
-> internal _currentMarketPrice


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice
  -> internal _currentMarketPrice


### public maxPayout
-> public marketPrice
  -> internal _currentMarketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
  -> internal _currentMarketPrice
-> public maxPayout
  -> public marketPrice
    -> internal _currentMarketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> public marketPrice
  -> internal _currentMarketPrice


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondBaseSDA

_File: src/bases/BondBaseSDA.sol_

### external closeMarket
-> internal _close


### external currentCapacity
_(no internal calls)_


### public currentControlVariable
-> internal _controlDecay


### public currentDebt
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice
    -> public currentControlVariable
      -> internal _controlDecay
    -> public currentDebt


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
-> public currentControlVariable
  -> internal _controlDecay
-> public currentDebt


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt


### public maxPayout
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt
-> public maxPayout
  -> public marketPrice
    -> public currentControlVariable
      -> internal _controlDecay
    -> public currentDebt


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> internal _decayAndGetPrice
  -> public currentDebt
  -> internal _controlDecay
  -> internal _currentMarketPrice
-> internal _close
-> internal _tune


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
-> public isLive


---

## BondBaseTeller

_File: src/bases/BondBaseTeller.sol_

### external claimFees
_(no internal calls)_


### external getFee
_(no internal calls)_


### external purchase
-> internal _handleTransfers


### external setCreateFeeDiscount
_(no internal calls)_


### external setProtocolFee
_(no internal calls)_


### external setReferrerFee
_(no internal calls)_


---

## BondFixedExpiryFPA

_File: src/BondFixedExpiryFPA.sol_

### external closeMarket
_(no internal calls)_


### external createMarket
-> internal _createMarket


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
_(no internal calls)_


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice


### public maxPayout
-> public marketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
-> public maxPayout
  -> public marketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondFixedExpiryOFDA

_File: src/BondFixedExpiryOFDA.sol_

### external closeMarket
_(no internal calls)_


### external createMarket
-> internal _createMarket
  -> internal _validateOracle
    -> internal _getPriceDecimals


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
_(no internal calls)_


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice


### public maxPayout
-> public marketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
-> public maxPayout
  -> public marketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> public marketPrice


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondFixedExpiryOSDA

_File: src/BondFixedExpiryOSDA.sol_

### external closeMarket
-> internal _close


### external createMarket
-> internal _createMarket
  -> internal _validateOracle
    -> internal _getPriceDecimals


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice
    -> internal _currentMarketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
-> internal _currentMarketPrice


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice
  -> internal _currentMarketPrice


### public maxPayout
-> public marketPrice
  -> internal _currentMarketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
  -> internal _currentMarketPrice
-> public maxPayout
  -> public marketPrice
    -> internal _currentMarketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> public marketPrice
  -> internal _currentMarketPrice


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondFixedExpirySDA

_File: src/BondFixedExpirySDA.sol_

### external closeMarket
-> internal _close


### external createMarket
-> internal _createMarket


### external currentCapacity
_(no internal calls)_


### public currentControlVariable
-> internal _controlDecay


### public currentDebt
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice
    -> public currentControlVariable
      -> internal _controlDecay
    -> public currentDebt


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
-> public currentControlVariable
  -> internal _controlDecay
-> public currentDebt


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt


### public maxPayout
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt
-> public maxPayout
  -> public marketPrice
    -> public currentControlVariable
      -> internal _controlDecay
    -> public currentDebt


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> internal _decayAndGetPrice
  -> public currentDebt
  -> internal _controlDecay
  -> internal _currentMarketPrice
-> internal _close
-> internal _tune


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
-> public isLive


---

## BondFixedExpiryTeller

_File: src/BondFixedExpiryTeller.sol_

### external claimFees
_(no internal calls)_


### external create
_(no internal calls)_


### external deploy
-> internal _getNameAndSymbol
  -> internal _uint2str


### external getBondToken
_(no internal calls)_


### external getBondTokenForMarket
_(no internal calls)_


### external getFee
_(no internal calls)_


### external purchase
-> internal _handleTransfers
-> internal _handlePayout


### external redeem
_(no internal calls)_


### external setCreateFeeDiscount
_(no internal calls)_


### external setProtocolFee
_(no internal calls)_


### external setReferrerFee
_(no internal calls)_


---

## BondFixedTermFPA

_File: src/BondFixedTermFPA.sol_

### external closeMarket
_(no internal calls)_


### external createMarket
-> internal _createMarket


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
_(no internal calls)_


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice


### public maxPayout
-> public marketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
-> public maxPayout
  -> public marketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondFixedTermOFDA

_File: src/BondFixedTermOFDA.sol_

### external closeMarket
_(no internal calls)_


### external createMarket
-> internal _createMarket
  -> internal _validateOracle
    -> internal _getPriceDecimals


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
_(no internal calls)_


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice


### public maxPayout
-> public marketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
-> public maxPayout
  -> public marketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> public marketPrice


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondFixedTermOSDA

_File: src/BondFixedTermOSDA.sol_

### external closeMarket
-> internal _close


### external createMarket
-> internal _createMarket
  -> internal _validateOracle
    -> internal _getPriceDecimals


### external currentCapacity
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice
    -> internal _currentMarketPrice


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
-> internal _currentMarketPrice


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice
  -> internal _currentMarketPrice


### public maxPayout
-> public marketPrice
  -> internal _currentMarketPrice


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
  -> internal _currentMarketPrice
-> public maxPayout
  -> public marketPrice
    -> internal _currentMarketPrice


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> public marketPrice
  -> internal _currentMarketPrice


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
_(no internal calls)_


### external setMinDepositInterval
_(no internal calls)_


### external setMinMarketDuration
_(no internal calls)_


---

## BondFixedTermSDA

_File: src/BondFixedTermSDA.sol_

### external closeMarket
-> internal _close


### external createMarket
-> internal _createMarket


### external currentCapacity
_(no internal calls)_


### public currentControlVariable
-> internal _controlDecay


### public currentDebt
_(no internal calls)_


### external getAggregator
_(no internal calls)_


### external getMarketInfoForPurchase
-> public maxPayout
  -> public marketPrice
    -> public currentControlVariable
      -> internal _controlDecay
    -> public currentDebt


### external getTeller
_(no internal calls)_


### public isInstantSwap
_(no internal calls)_


### public isLive
_(no internal calls)_


### public marketPrice
-> public currentControlVariable
  -> internal _controlDecay
-> public currentDebt


### external marketScale
_(no internal calls)_


### external maxAmountAccepted
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt


### public maxPayout
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt


### external ownerOf
_(no internal calls)_


### public payoutFor
-> public marketPrice
  -> public currentControlVariable
    -> internal _controlDecay
  -> public currentDebt
-> public maxPayout
  -> public marketPrice
    -> public currentControlVariable
      -> internal _controlDecay
    -> public currentDebt


### external pullOwnership
_(no internal calls)_


### external purchaseBond
-> public isLive
-> internal _decayAndGetPrice
  -> public currentDebt
  -> internal _controlDecay
  -> internal _currentMarketPrice
-> internal _close
-> internal _tune


### external pushOwnership
_(no internal calls)_


### external setAllowNewMarkets
_(no internal calls)_


### external setCallbackAuthStatus
_(no internal calls)_


### external setDefaults
_(no internal calls)_


### external setIntervals
-> public isLive


---

## BondFixedTermTeller

_File: src/BondFixedTermTeller.sol_

### external batchRedeem
-> internal _redeem
  -> internal _burnToken


### external claimFees
_(no internal calls)_


### external create
-> public getTokenId
-> internal _mintToken


### external deploy
-> public getTokenId
-> internal _deploy


### external getFee
_(no internal calls)_


### public getTokenId
_(no internal calls)_


### external getTokenNameAndSymbol
-> internal _getNameAndSymbol
  -> internal _uint2str


### external purchase
-> internal _handleTransfers
-> internal _handlePayout
  -> public getTokenId
  -> internal _deploy
  -> internal _mintToken


### public redeem
-> internal _redeem
  -> internal _burnToken


### external setCreateFeeDiscount
_(no internal calls)_


### external setProtocolFee
_(no internal calls)_


### external setReferrerFee
_(no internal calls)_


---

## ERC20BondToken

_File: src/ERC20BondToken.sol_

### external burn
-> public teller


### external expiry
_(no internal calls)_


### external mint
-> public teller


### public teller
_(no internal calls)_


### external underlying
_(no internal calls)_


---

## LimitOrders

_File: src/LimitOrders.sol_

### public DOMAIN_SEPARATOR
-> internal computeDomainSeparator


### external cancelOrder
-> public getDigest
  -> public DOMAIN_SEPARATOR
    -> internal computeDomainSeparator


### external executeOrder
-> internal _executeOrder
  -> internal _validateOrder
    -> public getDigest
      -> public DOMAIN_SEPARATOR
        -> internal computeDomainSeparator


### external executeOrders
-> internal _executeOrder
  -> internal _validateOrder
    -> public getDigest
      -> public DOMAIN_SEPARATOR
        -> internal computeDomainSeparator


### public getDigest
-> public DOMAIN_SEPARATOR
  -> internal computeDomainSeparator


### external reinstateOrder
-> public getDigest
  -> public DOMAIN_SEPARATOR
    -> internal computeDomainSeparator


### external updateDomainSeparator
-> internal computeDomainSeparator

