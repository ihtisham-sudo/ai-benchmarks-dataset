# Callpaths — Plaza_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## Auction

_File: src/Auction.sol_

### external bid
-> public slotSize
-> internal insertSortedBid
-> internal _removeBid
-> internal removeExcessBids
  -> internal _removeBid


### external claimBid
_(no internal calls)_


### external claimRefund
_(no internal calls)_


### external endAuction
_(no internal calls)_


### public initialize
_(no internal calls)_


### external pause
_(no internal calls)_


### public slotSize
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## BalancerOracleAdapter

_File: src/BalancerOracleAdapter.sol_

### public _removeFirstElement
_(no internal calls)_


### external description
_(no internal calls)_


### public getOracleDecimals
_(no internal calls)_


### public getOraclePrice
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### public getSingleAssetPrice
_(no internal calls)_


### external initialize
-> internal __OracleReader_init


### external latestRoundData
-> public getOracleDecimals
-> public getOraclePrice
-> public _removeFirstElement
-> library FixedPoint.mulDown
-> internal _calculateInvariant
-> internal _calculateFairUintPrice


### external setBalancerPoolAddress
_(no internal calls)_


### external version
_(no internal calls)_


---

## BalancerRouter

_File: src/BalancerRouter.sol_

### external exitPlazaAndBalancer
-> internal exitPlazaPool
-> internal exitBalancerPool
  -> external_callback IVault.ExitPoolRequest


### external joinBalancerAndPlaza
-> internal joinBalancerPool
  -> external_callback IVault.JoinPoolRequest


---

## BondOracleAdapter

_File: src/BondOracleAdapter.sol_

### external description
_(no internal calls)_


### public getAdjustedPriceFromSqrtPriceX96
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### external initialize
-> private getPool


### external latestRoundData
-> public getAdjustedPriceFromSqrtPriceX96


### external setDexPool
_(no internal calls)_


### external version
_(no internal calls)_


---

## BondToken

_File: src/BondToken.sol_

### public burn
_(no internal calls)_


### public getIndexedUserAmount
_(no internal calls)_


### external getPreviousPoolAmounts
_(no internal calls)_


### public increaseIndexedAssetPeriod
_(no internal calls)_


### public initialize
_(no internal calls)_


### public mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external resetIndexedUserAssets
_(no internal calls)_


### external setPool
_(no internal calls)_


### external setSharesPerToken
_(no internal calls)_


### external unpause
_(no internal calls)_


### external zeroLastSharesPerToken
_(no internal calls)_


---

## Deployer

_File: src/utils/Deployer.sol_

### external deployAuction
_(no internal calls)_


### external deployBondToken
_(no internal calls)_


### external deployDistributor
_(no internal calls)_


### external deployLeverageToken
_(no internal calls)_


---

## Distributor

_File: src/Distributor.sol_

### external allocate
_(no internal calls)_


### external claim
_(no internal calls)_


### public initialize
_(no internal calls)_


### external pause
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## Faucet

_File: src/Faucet.sol_

### public addToWhitelist
_(no internal calls)_


### public faucet
-> public faucet


### public faucetCoupon
_(no internal calls)_


### public faucetReserve
_(no internal calls)_


---

## LeverageToken

_File: src/LeverageToken.sol_

### public burn
_(no internal calls)_


### public initialize
_(no internal calls)_


### public mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## LifiRouter

_File: src/LifiRouter.sol_

### external create
_(no internal calls)_


---

## OracleFeeds

_File: src/OracleFeeds.sol_

### public grantRole
_(no internal calls)_


### public revokeRole
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


---

## OracleReader

_File: src/OracleReader.sol_

### public getOracleDecimals
_(no internal calls)_


### public getOraclePrice
_(no internal calls)_


---

## Pool

_File: src/Pool.sol_

### public claimFees
-> internal _claimFees
  -> internal getFeeAmount


### external create
-> private _create
  -> internal _claimFees
    -> internal getFeeAmount
  -> public simulateCreate
    -> public getCreateAmount
    -> public getOraclePrice
    -> public getOracleDecimals


### external distribute
_(no internal calls)_


### public getCreateAmount
_(no internal calls)_


### public getOracleDecimals
_(no internal calls)_


### public getOraclePrice
_(no internal calls)_


### external getPoolInfo
_(no internal calls)_


### public getRedeemAmount
_(no internal calls)_


### public initialize
-> internal __OracleReader_init


### external pause
_(no internal calls)_


### external redeem
-> private _redeem
  -> internal _claimFees
    -> internal getFeeAmount
  -> public simulateRedeem
    -> public getOracleDecimals
    -> public getOraclePrice
    -> public getRedeemAmount


### external setAuctionPeriod
_(no internal calls)_


### external setDistributionPeriod
_(no internal calls)_


### external setFee
-> internal getFeeAmount
-> internal _claimFees
  -> internal getFeeAmount


### external setFeeBeneficiary
_(no internal calls)_


### external setName
_(no internal calls)_


### external setPoolSaleLimit
_(no internal calls)_


### external setSharesPerToken
_(no internal calls)_


### public simulateCreate
-> public getCreateAmount
-> public getOraclePrice
-> public getOracleDecimals


### public simulateRedeem
-> public getOracleDecimals
-> public getOraclePrice
-> public getRedeemAmount


### external startAuction
_(no internal calls)_


### external transferReserveToAuction
-> internal lastAuction


### external unpause
_(no internal calls)_


### external zeroLastSharesPerToken
-> internal lastAuction


---

## PoolFactory

_File: src/PoolFactory.sol_

### external createPool
_(no internal calls)_


### public grantRole
_(no internal calls)_


### public initialize
_(no internal calls)_


### external pause
_(no internal calls)_


### external poolsLength
_(no internal calls)_


### public revokeRole
_(no internal calls)_


### external setDeployer
_(no internal calls)_


### external setGovernance
-> public grantRole
-> public revokeRole


### external unpause
_(no internal calls)_


---

## PreDeposit

_File: src/PreDeposit.sol_

### public _getClaimableAmount
_(no internal calls)_


### public _prependLpToken
_(no internal calls)_


### public _prependUint256Max
_(no internal calls)_


### external claim
-> public _getClaimableAmount
-> private _claim


### external claimTo
-> public _getClaimableAmount
-> private _claim


### external createPool
-> public currentPredepositTotal
-> private _validateNormalizedWeights
  -> private _getLargestIndex
  -> public currentPredepositTotal
-> public _prependUint256Max
-> public _prependLpToken
-> external_callback IVault.JoinPoolRequest


### public currentPredepositTotal
_(no internal calls)_


### external deposit
-> private _deposit
  -> private _checkArrayLengths
  -> private _checkCap
    -> private _checkTokenAllowed
    -> public currentPredepositTotal


### external getAllowedTokens
_(no internal calls)_


### external getNumbRejectedTokens
_(no internal calls)_


### external increaseDepositCap
_(no internal calls)_


### public initialize
-> private _sortAddresses


### external pause
_(no internal calls)_


### external setBondAndLeverageAmount
_(no internal calls)_


### external setDepositEndTime
_(no internal calls)_


### external setDepositStartTime
_(no internal calls)_


### external setParams
_(no internal calls)_


### external unpause
_(no internal calls)_


### external withdraw
-> private _withdraw
  -> private _checkArrayLengths


### external withdrawTo
-> private _withdraw
  -> private _checkArrayLengths


---

## RoycoHelper

_File: src/RoycoHelper.sol_

### external withdrawOrClaim
_(no internal calls)_


---

## UnderlyingsOracleAdapter

_File: src/UnderlyingsOracleAdapter.sol_

### external description
_(no internal calls)_


### public getOracleDecimals
_(no internal calls)_


### public getOraclePrice
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### external initialize
-> internal __OracleReader_init


### external latestRoundData
-> public getOraclePrice
-> public getOracleDecimals


### external version
_(no internal calls)_


---

## WethPriceFeed

_File: src/WethPriceFeed.sol_

### external decimals
_(no internal calls)_


### external description
_(no internal calls)_


### public getRoundData
_(no internal calls)_


### external latestRoundData
_(no internal calls)_


### external version
_(no internal calls)_

