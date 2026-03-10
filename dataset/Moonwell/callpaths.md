# Callpaths — Moonwell

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BaseJumpRateModelV2

_File: BaseJumpRateModelV2.sol_

### public getSupplyRate
-> internal getBorrowRateInternal
  -> public utilizationRate
-> public utilizationRate


### external updateJumpRateModel
-> internal updateJumpRateModelInternal


### public utilizationRate
_(no internal calls)_


---

## ChainlinkOracle

_File: Chainlink/ChainlinkOracle.sol_

### external assetPrices
_(no internal calls)_


### public getFeed
_(no internal calls)_


### public getUnderlyingPrice
-> internal getChainlinkPrice
-> public getFeed
-> internal getPrice
  -> internal getChainlinkPrice
  -> public getFeed


### external setAdmin
_(no internal calls)_


### external setDirectPrice
_(no internal calls)_


### external setFeed
_(no internal calls)_


### external setUnderlyingPrice
_(no internal calls)_


---

## Comptroller

_File: Comptroller.sol_

### public _become
_(no internal calls)_


### public _grantWell
-> internal adminOrInitializing
-> internal grantRewardInternal


### external _setBorrowCapGuardian
_(no internal calls)_


### public _setBorrowPaused
_(no internal calls)_


### external _setCloseFactor
_(no internal calls)_


### external _setCollateralFactor
-> internal fail
-> internal lessThanExp


### public _setGasAmount
-> internal fail


### external _setLiquidationIncentive
-> internal fail


### external _setMarketBorrowCaps
_(no internal calls)_


### public _setMintPaused
_(no internal calls)_


### public _setPauseGuardian
-> internal fail


### public _setPriceOracle
-> internal fail


### public _setRewardSpeed
-> internal adminOrInitializing
-> internal setRewardSpeedInternal
  -> internal updateRewardSupplyIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32
  -> internal safe32
  -> public getBlockTimestamp
  -> internal updateRewardBorrowIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal div_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32


### public _setSeizePaused
_(no internal calls)_


### public _setTransferPaused
_(no internal calls)_


### external _supportMarket
-> internal fail
-> internal _addMarketInternal


### external borrowAllowed
-> internal addToMarketInternal
-> internal add_
-> internal getHypotheticalAccountLiquidityInternal
  -> internal mul_
  -> internal mul_ScalarTruncateAddUInt
    -> internal mul_
    -> internal add_
    -> internal truncate
-> internal updateAndDistributeBorrowerRewardsForToken
  -> internal updateRewardBorrowIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal div_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32
  -> internal distributeBorrowerReward
    -> internal sub_
    -> internal div_
    -> internal mul_
    -> internal add_


### external borrowVerify
_(no internal calls)_


### external checkMembership
_(no internal calls)_


### public claimReward
-> internal updateRewardBorrowIndex
  -> public getBlockTimestamp
  -> internal sub_
  -> internal div_
  -> internal mul_
  -> internal fraction
    -> internal div_
    -> internal mul_
  -> internal add_
  -> internal safe224
  -> internal safe32
-> internal distributeBorrowerReward
  -> internal sub_
  -> internal div_
  -> internal mul_
  -> internal add_
-> internal grantRewardInternal
-> internal updateRewardSupplyIndex
  -> public getBlockTimestamp
  -> internal sub_
  -> internal mul_
  -> internal fraction
    -> internal div_
    -> internal mul_
  -> internal add_
  -> internal safe224
  -> internal safe32
-> internal distributeSupplierReward
  -> internal sub_
  -> internal mul_
  -> internal add_


### public enterMarkets
-> internal addToMarketInternal


### external exitMarket
-> internal fail
-> internal redeemAllowedInternal
  -> internal getHypotheticalAccountLiquidityInternal
    -> internal mul_
    -> internal mul_ScalarTruncateAddUInt
      -> internal mul_
      -> internal add_
      -> internal truncate
-> internal failOpaque


### public getAccountLiquidity
-> internal getHypotheticalAccountLiquidityInternal
  -> internal mul_
  -> internal mul_ScalarTruncateAddUInt
    -> internal mul_
    -> internal add_
    -> internal truncate


### public getAllMarkets
_(no internal calls)_


### external getAssetsIn
_(no internal calls)_


### public getBlockTimestamp
_(no internal calls)_


### public getHypotheticalAccountLiquidity
-> internal getHypotheticalAccountLiquidityInternal
  -> internal mul_
  -> internal mul_ScalarTruncateAddUInt
    -> internal mul_
    -> internal add_
    -> internal truncate


### external liquidateBorrowAllowed
-> internal getAccountLiquidityInternal
  -> internal getHypotheticalAccountLiquidityInternal
    -> internal mul_
    -> internal mul_ScalarTruncateAddUInt
      -> internal mul_
      -> internal add_
      -> internal truncate
-> internal mul_ScalarTruncate
  -> internal mul_
  -> internal truncate


### external liquidateBorrowVerify
_(no internal calls)_


### external liquidateCalculateSeizeTokens
-> internal mul_
-> internal div_
-> internal mul_ScalarTruncate
  -> internal mul_
  -> internal truncate


### external mintAllowed
-> internal updateAndDistributeSupplierRewardsForToken
  -> internal updateRewardSupplyIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32
  -> internal distributeSupplierReward
    -> internal sub_
    -> internal mul_
    -> internal add_


### external mintVerify
_(no internal calls)_


### external redeemAllowed
-> internal redeemAllowedInternal
  -> internal getHypotheticalAccountLiquidityInternal
    -> internal mul_
    -> internal mul_ScalarTruncateAddUInt
      -> internal mul_
      -> internal add_
      -> internal truncate
-> internal updateAndDistributeSupplierRewardsForToken
  -> internal updateRewardSupplyIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32
  -> internal distributeSupplierReward
    -> internal sub_
    -> internal mul_
    -> internal add_


### external redeemVerify
_(no internal calls)_


### external repayBorrowAllowed
-> internal updateAndDistributeBorrowerRewardsForToken
  -> internal updateRewardBorrowIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal div_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32
  -> internal distributeBorrowerReward
    -> internal sub_
    -> internal div_
    -> internal mul_
    -> internal add_


### external repayBorrowVerify
_(no internal calls)_


### external seizeAllowed
-> internal updateAndDistributeSupplierRewardsForToken
  -> internal updateRewardSupplyIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32
  -> internal distributeSupplierReward
    -> internal sub_
    -> internal mul_
    -> internal add_


### external seizeVerify
_(no internal calls)_


### public setWellAddress
_(no internal calls)_


### external transferAllowed
-> internal redeemAllowedInternal
  -> internal getHypotheticalAccountLiquidityInternal
    -> internal mul_
    -> internal mul_ScalarTruncateAddUInt
      -> internal mul_
      -> internal add_
      -> internal truncate
-> internal updateAndDistributeSupplierRewardsForToken
  -> internal updateRewardSupplyIndex
    -> public getBlockTimestamp
    -> internal sub_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
    -> internal safe224
    -> internal safe32
  -> internal distributeSupplierReward
    -> internal sub_
    -> internal mul_
    -> internal add_


### external transferVerify
_(no internal calls)_


---

## FaucetToken

_File: FaucetToken.sol_

### public allocateTo
_(no internal calls)_


### external approve
_(no internal calls)_


### external transfer
_(no internal calls)_


### external transferFrom
_(no internal calls)_


---

## JumpRateModel

_File: JumpRateModel.sol_

### public getBorrowRate
-> public utilizationRate


### public getSupplyRate
-> public getBorrowRate
  -> public utilizationRate
-> public utilizationRate


### public utilizationRate
_(no internal calls)_


---

## JumpRateModelV2

_File: JumpRateModelV2.sol_

### external getBorrowRate
-> internal getBorrowRateInternal
  -> public utilizationRate


### public getSupplyRate
-> internal getBorrowRateInternal
  -> public utilizationRate
-> public utilizationRate


### external updateJumpRateModel
-> internal updateJumpRateModelInternal


### public utilizationRate
_(no internal calls)_


---

## LegacyJumpRateModelV2

_File: LegacyJumpRateModelV2.sol_

### external getBorrowRate
-> internal getBorrowRateInternal
  -> public utilizationRate


### public getSupplyRate
-> internal getBorrowRateInternal
  -> public utilizationRate
-> public utilizationRate


### external updateJumpRateModel
-> internal updateJumpRateModelInternal


### public utilizationRate
_(no internal calls)_


---

## MDaiDelegate

_File: MDaiDelegate.sol_

### public _resignImplementation
_(no internal calls)_


### public accrueInterest
_(no internal calls)_


---

## MErc20

_File: MErc20.sol_

### external _acceptAdmin
_(no internal calls)_


### external _addReserves
-> internal _addReservesInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal _addReservesFresh
    -> internal getBlockTimestamp
    -> internal doTransferIn


### external _reduceReserves
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _reduceReservesFresh
  -> internal getBlockTimestamp
  -> internal getCashPrior
  -> internal doTransferOut


### public _setComptroller
_(no internal calls)_


### public _setInterestRateModel
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _setInterestRateModelFresh
  -> internal getBlockTimestamp


### external _setPendingAdmin
_(no internal calls)_


### external _setProtocolSeizeShare
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _setProtocolSeizeShareFresh
  -> internal getBlockTimestamp


### external _setReserveFactor
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _setReserveFactorFresh
  -> internal getBlockTimestamp


### public accrueInterest
-> internal getBlockTimestamp
-> internal getCashPrior


### external allowance
_(no internal calls)_


### external approve
_(no internal calls)_


### external balanceOf
_(no internal calls)_


### external balanceOfUnderlying
-> public exchangeRateCurrent
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> public exchangeRateStored
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior


### external borrow
-> internal borrowInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal borrowFresh
    -> internal getBlockTimestamp
    -> internal getCashPrior
    -> internal borrowBalanceStoredInternal
    -> internal doTransferOut


### external borrowBalanceCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> public borrowBalanceStored
  -> internal borrowBalanceStoredInternal


### public borrowBalanceStored
-> internal borrowBalanceStoredInternal


### external borrowRatePerTimestamp
-> internal getCashPrior


### public exchangeRateCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> public exchangeRateStored
  -> internal exchangeRateStoredInternal
    -> internal getCashPrior


### public exchangeRateStored
-> internal exchangeRateStoredInternal
  -> internal getCashPrior


### external getAccountSnapshot
-> internal borrowBalanceStoredInternal
-> internal exchangeRateStoredInternal
  -> internal getCashPrior


### external getCash
-> internal getCashPrior


### public initialize
_(no internal calls)_


### external liquidateBorrow
-> internal liquidateBorrowInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal liquidateBorrowFresh
    -> internal getBlockTimestamp
    -> internal repayBorrowFresh
      -> internal getBlockTimestamp
      -> internal borrowBalanceStoredInternal
      -> internal doTransferIn
    -> internal seizeInternal
      -> internal exchangeRateStoredInternal
        -> internal getCashPrior


### external mint
-> internal mintInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal mintFresh
    -> internal getBlockTimestamp
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior
    -> internal doTransferIn


### external redeem
-> internal redeemInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal redeemFresh
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior
    -> internal getBlockTimestamp
    -> internal getCashPrior
    -> internal doTransferOut


### external redeemUnderlying
-> internal redeemUnderlyingInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal redeemFresh
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior
    -> internal getBlockTimestamp
    -> internal getCashPrior
    -> internal doTransferOut


### external repayBorrow
-> internal repayBorrowInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal repayBorrowFresh
    -> internal getBlockTimestamp
    -> internal borrowBalanceStoredInternal
    -> internal doTransferIn


### external repayBorrowBehalf
-> internal repayBorrowBehalfInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal repayBorrowFresh
    -> internal getBlockTimestamp
    -> internal borrowBalanceStoredInternal
    -> internal doTransferIn


### external seize
-> internal seizeInternal
  -> internal exchangeRateStoredInternal
    -> internal getCashPrior


### external supplyRatePerTimestamp
-> internal getCashPrior


### external sweepToken
_(no internal calls)_


### external totalBorrowsCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior


### external transfer
-> internal transferTokens


### external transferFrom
-> internal transferTokens


---

## MErc20Delegate

_File: MErc20Delegate.sol_

### external _addReserves
_(no internal calls)_


### public _becomeImplementation
_(no internal calls)_


### public _resignImplementation
_(no internal calls)_


### external borrow
_(no internal calls)_


### public initialize
_(no internal calls)_


### external liquidateBorrow
_(no internal calls)_


### external mint
_(no internal calls)_


### external redeem
_(no internal calls)_


### external redeemUnderlying
_(no internal calls)_


### external repayBorrow
_(no internal calls)_


### external repayBorrowBehalf
_(no internal calls)_


### external sweepToken
_(no internal calls)_


---

## MErc20Delegator

_File: MErc20Delegator.sol_

### external _acceptAdmin
-> public delegateToImplementation
  -> internal delegateTo


### external _addReserves
-> public delegateToImplementation
  -> internal delegateTo


### external _reduceReserves
-> public delegateToImplementation
  -> internal delegateTo


### public _setComptroller
-> public delegateToImplementation
  -> internal delegateTo


### public _setImplementation
-> public delegateToImplementation
  -> internal delegateTo


### public _setInterestRateModel
-> public delegateToImplementation
  -> internal delegateTo


### external _setPendingAdmin
-> public delegateToImplementation
  -> internal delegateTo


### external _setProtocolSeizeShare
-> public delegateToImplementation
  -> internal delegateTo


### external _setReserveFactor
-> public delegateToImplementation
  -> internal delegateTo


### public accrueInterest
-> public delegateToImplementation
  -> internal delegateTo


### external allowance
-> public delegateToViewImplementation


### external approve
-> public delegateToImplementation
  -> internal delegateTo


### external balanceOf
-> public delegateToViewImplementation


### external balanceOfUnderlying
-> public delegateToImplementation
  -> internal delegateTo


### external borrow
-> public delegateToImplementation
  -> internal delegateTo


### external borrowBalanceCurrent
-> public delegateToImplementation
  -> internal delegateTo


### public borrowBalanceStored
-> public delegateToViewImplementation


### external borrowRatePerTimestamp
-> public delegateToViewImplementation


### public delegateToImplementation
-> internal delegateTo


### public delegateToViewImplementation
_(no internal calls)_


### public exchangeRateCurrent
-> public delegateToImplementation
  -> internal delegateTo


### public exchangeRateStored
-> public delegateToViewImplementation


### external getAccountSnapshot
-> public delegateToViewImplementation


### external getCash
-> public delegateToViewImplementation


### external liquidateBorrow
-> public delegateToImplementation
  -> internal delegateTo


### external mint
-> public delegateToImplementation
  -> internal delegateTo


### external redeem
-> public delegateToImplementation
  -> internal delegateTo


### external redeemUnderlying
-> public delegateToImplementation
  -> internal delegateTo


### external repayBorrow
-> public delegateToImplementation
  -> internal delegateTo


### external repayBorrowBehalf
-> public delegateToImplementation
  -> internal delegateTo


### external seize
-> public delegateToImplementation
  -> internal delegateTo


### external supplyRatePerTimestamp
-> public delegateToViewImplementation


### external sweepToken
-> public delegateToImplementation
  -> internal delegateTo


### external totalBorrowsCurrent
-> public delegateToImplementation
  -> internal delegateTo


### external transfer
-> public delegateToImplementation
  -> internal delegateTo


### external transferFrom
-> public delegateToImplementation
  -> internal delegateTo


---

## MErc20Immutable

_File: MErc20Immutable.sol_

### external _addReserves
_(no internal calls)_


### external borrow
_(no internal calls)_


### public initialize
_(no internal calls)_


### external liquidateBorrow
_(no internal calls)_


### external mint
_(no internal calls)_


### external redeem
_(no internal calls)_


### external redeemUnderlying
_(no internal calls)_


### external repayBorrow
_(no internal calls)_


### external repayBorrowBehalf
_(no internal calls)_


### external sweepToken
_(no internal calls)_


---

## MGlimmer

_File: MGlimmer.sol_

### external _acceptAdmin
_(no internal calls)_


### external _addReserves
-> internal _addReservesInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal _addReservesFresh
    -> internal getBlockTimestamp
    -> internal doTransferIn


### external _reduceReserves
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _reduceReservesFresh
  -> internal getBlockTimestamp
  -> internal getCashPrior
  -> internal doTransferOut


### public _setComptroller
_(no internal calls)_


### public _setInterestRateModel
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _setInterestRateModelFresh
  -> internal getBlockTimestamp


### external _setPendingAdmin
_(no internal calls)_


### external _setProtocolSeizeShare
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _setProtocolSeizeShareFresh
  -> internal getBlockTimestamp


### external _setReserveFactor
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> internal _setReserveFactorFresh
  -> internal getBlockTimestamp


### public accrueInterest
-> internal getBlockTimestamp
-> internal getCashPrior


### external allowance
_(no internal calls)_


### external approve
_(no internal calls)_


### external balanceOf
_(no internal calls)_


### external balanceOfUnderlying
-> public exchangeRateCurrent
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> public exchangeRateStored
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior


### external borrow
-> internal borrowInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal borrowFresh
    -> internal getBlockTimestamp
    -> internal getCashPrior
    -> internal borrowBalanceStoredInternal
    -> internal doTransferOut


### external borrowBalanceCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> public borrowBalanceStored
  -> internal borrowBalanceStoredInternal


### public borrowBalanceStored
-> internal borrowBalanceStoredInternal


### external borrowRatePerTimestamp
-> internal getCashPrior


### public exchangeRateCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior
-> public exchangeRateStored
  -> internal exchangeRateStoredInternal
    -> internal getCashPrior


### public exchangeRateStored
-> internal exchangeRateStoredInternal
  -> internal getCashPrior


### external getAccountSnapshot
-> internal borrowBalanceStoredInternal
-> internal exchangeRateStoredInternal
  -> internal getCashPrior


### external getCash
-> internal getCashPrior


### public initialize
-> public _setComptroller
-> internal getBlockTimestamp
-> internal _setInterestRateModelFresh
  -> internal getBlockTimestamp


### external liquidateBorrow
-> internal liquidateBorrowInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal liquidateBorrowFresh
    -> internal getBlockTimestamp
    -> internal repayBorrowFresh
      -> internal getBlockTimestamp
      -> internal borrowBalanceStoredInternal
      -> internal doTransferIn
    -> internal seizeInternal
      -> internal exchangeRateStoredInternal
        -> internal getCashPrior
-> internal requireNoError


### external mint
-> internal mintInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal mintFresh
    -> internal getBlockTimestamp
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior
    -> internal doTransferIn
-> internal requireNoError


### external redeem
-> internal redeemInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal redeemFresh
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior
    -> internal getBlockTimestamp
    -> internal getCashPrior
    -> internal doTransferOut


### external redeemUnderlying
-> internal redeemUnderlyingInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal redeemFresh
    -> internal exchangeRateStoredInternal
      -> internal getCashPrior
    -> internal getBlockTimestamp
    -> internal getCashPrior
    -> internal doTransferOut


### external repayBorrow
-> internal repayBorrowInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal repayBorrowFresh
    -> internal getBlockTimestamp
    -> internal borrowBalanceStoredInternal
    -> internal doTransferIn
-> internal requireNoError


### external repayBorrowBehalf
-> internal repayBorrowBehalfInternal
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal getCashPrior
  -> internal repayBorrowFresh
    -> internal getBlockTimestamp
    -> internal borrowBalanceStoredInternal
    -> internal doTransferIn
-> internal requireNoError


### external seize
-> internal seizeInternal
  -> internal exchangeRateStoredInternal
    -> internal getCashPrior


### external supplyRatePerTimestamp
-> internal getCashPrior


### external totalBorrowsCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal getCashPrior


### external transfer
-> internal transferTokens


### external transferFrom
-> internal transferTokens


---

## MLikeDelegate

_File: MLikeDelegate.sol_

### public _becomeImplementation
_(no internal calls)_


### external _delegateMLikeTo
_(no internal calls)_


### public _resignImplementation
_(no internal calls)_


---

## MToken

_File: MToken.sol_

### external _acceptAdmin
-> internal fail


### external _reduceReserves
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal mulScalar
  -> internal failOpaque
  -> internal mulScalarTruncate
    -> internal mulScalar
  -> internal mulScalarTruncateAddUInt
    -> internal mulScalar
-> internal fail
-> internal _reduceReservesFresh
  -> internal fail
  -> internal getBlockTimestamp


### public _setComptroller
-> internal fail


### public _setInterestRateModel
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal mulScalar
  -> internal failOpaque
  -> internal mulScalarTruncate
    -> internal mulScalar
  -> internal mulScalarTruncateAddUInt
    -> internal mulScalar
-> internal fail
-> internal _setInterestRateModelFresh
  -> internal fail
  -> internal getBlockTimestamp


### external _setPendingAdmin
-> internal fail


### external _setProtocolSeizeShare
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal mulScalar
  -> internal failOpaque
  -> internal mulScalarTruncate
    -> internal mulScalar
  -> internal mulScalarTruncateAddUInt
    -> internal mulScalar
-> internal fail
-> internal _setProtocolSeizeShareFresh
  -> internal fail
  -> internal getBlockTimestamp


### external _setReserveFactor
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal mulScalar
  -> internal failOpaque
  -> internal mulScalarTruncate
    -> internal mulScalar
  -> internal mulScalarTruncateAddUInt
    -> internal mulScalar
-> internal fail
-> internal _setReserveFactorFresh
  -> internal fail
  -> internal getBlockTimestamp


### public accrueInterest
-> internal getBlockTimestamp
-> internal mulScalar
-> internal failOpaque
-> internal mulScalarTruncate
  -> internal mulScalar
-> internal mulScalarTruncateAddUInt
  -> internal mulScalar


### external allowance
_(no internal calls)_


### external approve
_(no internal calls)_


### external balanceOf
_(no internal calls)_


### external balanceOfUnderlying
-> public exchangeRateCurrent
  -> public accrueInterest
    -> internal getBlockTimestamp
    -> internal mulScalar
    -> internal failOpaque
    -> internal mulScalarTruncate
      -> internal mulScalar
    -> internal mulScalarTruncateAddUInt
      -> internal mulScalar
  -> public exchangeRateStored
    -> internal exchangeRateStoredInternal
      -> internal getExp
-> internal mulScalarTruncate
  -> internal mulScalar


### external borrowBalanceCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal mulScalar
  -> internal failOpaque
  -> internal mulScalarTruncate
    -> internal mulScalar
  -> internal mulScalarTruncateAddUInt
    -> internal mulScalar
-> public borrowBalanceStored
  -> internal borrowBalanceStoredInternal


### public borrowBalanceStored
-> internal borrowBalanceStoredInternal


### external borrowRatePerTimestamp
_(no internal calls)_


### public exchangeRateCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal mulScalar
  -> internal failOpaque
  -> internal mulScalarTruncate
    -> internal mulScalar
  -> internal mulScalarTruncateAddUInt
    -> internal mulScalar
-> public exchangeRateStored
  -> internal exchangeRateStoredInternal
    -> internal getExp


### public exchangeRateStored
-> internal exchangeRateStoredInternal
  -> internal getExp


### external getAccountSnapshot
-> internal borrowBalanceStoredInternal
-> internal exchangeRateStoredInternal
  -> internal getExp


### external getCash
_(no internal calls)_


### public initialize
-> public _setComptroller
  -> internal fail
-> internal getBlockTimestamp
-> internal _setInterestRateModelFresh
  -> internal fail
  -> internal getBlockTimestamp


### external seize
-> internal seizeInternal
  -> internal failOpaque
  -> internal fail
  -> internal exchangeRateStoredInternal
    -> internal getExp


### external supplyRatePerTimestamp
_(no internal calls)_


### external totalBorrowsCurrent
-> public accrueInterest
  -> internal getBlockTimestamp
  -> internal mulScalar
  -> internal failOpaque
  -> internal mulScalarTruncate
    -> internal mulScalar
  -> internal mulScalarTruncateAddUInt
    -> internal mulScalar


### external transfer
-> internal transferTokens
  -> internal failOpaque
  -> internal fail


### external transferFrom
-> internal transferTokens
  -> internal failOpaque
  -> internal fail


---

## Maximillion

_File: Maximillion.sol_

### public repayBehalf
-> public repayBehalfExplicit


### public repayBehalfExplicit
_(no internal calls)_


---

## Mfam

_File: Governance/Mfam.sol_

### external allowance
_(no internal calls)_


### external approve
-> internal safe96


### external balanceOf
_(no internal calls)_


### public delegate
-> internal _delegate
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


### public delegateBySig
-> internal getChainId
-> internal _delegate
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


### external getCurrentVotes
_(no internal calls)_


### public getPriorVotes
_(no internal calls)_


### external permit
-> internal safe96
-> internal getChainId


### external transfer
-> internal safe96
-> internal _transferTokens
  -> internal sub96
  -> internal add96
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


### external transferFrom
-> internal safe96
-> internal sub96
-> internal _transferTokens
  -> internal sub96
  -> internal add96
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


---

## Migrations

_File: Migrations.sol_

### public setCompleted
_(no internal calls)_


---

## MoonwellGovernorApollo

_File: Governance/MoonwellApolloGovernor.sol_

### external __acceptAdminOnTimelock
_(no internal calls)_


### external __executeAcceptAdminOnContract
_(no internal calls)_


### external __executeBreakGlassOnChangeAdmin
_(no internal calls)_


### external __executeBreakGlassOnCompound
_(no internal calls)_


### external __executeBreakGlassOnEmissionsManager
_(no internal calls)_


### external __executeBreakGlassOnOwnable
_(no internal calls)_


### external __executeBreakGlassOnSetAdmin
_(no internal calls)_


### external __executeBreakGlassOnSetPendingAdmin
_(no internal calls)_


### external __executeCompoundAcceptAdminOnContract
_(no internal calls)_


### external __removeGuardians
_(no internal calls)_


### external __setGovernanceReturnAddress
_(no internal calls)_


### external cancel
-> public state
-> internal _getVotingPower


### external castVote
-> internal _castVote
  -> public state
  -> internal _getVotingPower


### external castVoteBySig
-> internal getChainId
-> internal _castVote
  -> public state
  -> internal _getVotingPower


### external execute
-> public state


### external getActions
_(no internal calls)_


### external getQuorum
-> public state
-> internal _calculateNewQuorum


### external getReceipt
_(no internal calls)_


### public propose
-> internal _getVotingPower
-> public state
-> internal _adjustQuorum
  -> public state
  -> internal _calculateNewQuorum


### external queue
-> public state
-> internal _queueOrRevert


### external setBreakGlassGuardian
_(no internal calls)_


### external setProposalMaxOperations
_(no internal calls)_


### external setProposalThreshold
_(no internal calls)_


### external setQuorumCaps
_(no internal calls)_


### external setVotingDelay
_(no internal calls)_


### external setVotingPeriod
_(no internal calls)_


### public state
_(no internal calls)_


### external sweepTokens
_(no internal calls)_


---

## MoonwellGovernorArtemis

_File: Governance/MoonwellArtemisGovernor.sol_

### external __acceptAdminOnTimelock
_(no internal calls)_


### external __executeAcceptAdminOnContract
_(no internal calls)_


### external __executeBreakGlassOnChangeAdmin
_(no internal calls)_


### external __executeBreakGlassOnCompound
_(no internal calls)_


### external __executeBreakGlassOnEmissionsManager
_(no internal calls)_


### external __executeBreakGlassOnOwnable
_(no internal calls)_


### external __executeBreakGlassOnSetAdmin
_(no internal calls)_


### external __executeBreakGlassOnSetPendingAdmin
_(no internal calls)_


### external __executeCompoundAcceptAdminOnContract
_(no internal calls)_


### external __removeGuardians
_(no internal calls)_


### external __setGovernanceReturnAddress
_(no internal calls)_


### public cancel
-> public state
  -> internal add256
-> internal _getVotingPower
  -> internal add256
-> internal sub256


### public castVote
-> internal _castVote
  -> public state
    -> internal add256
  -> internal _getVotingPower
    -> internal add256
  -> internal add256


### public castVoteBySig
-> internal getChainId
-> internal _castVote
  -> public state
    -> internal add256
  -> internal _getVotingPower
    -> internal add256
  -> internal add256


### external execute
-> public state
  -> internal add256


### public getActions
_(no internal calls)_


### public getReceipt
_(no internal calls)_


### public propose
-> internal _getVotingPower
  -> internal add256
-> internal sub256
-> public state
  -> internal add256
-> internal add256


### public queue
-> public state
  -> internal add256
-> internal add256
-> internal _queueOrRevert


### external setBreakGlassGuardian
_(no internal calls)_


### external setProposalMaxOperations
_(no internal calls)_


### external setProposalThreshold
_(no internal calls)_


### external setQuorumVotes
_(no internal calls)_


### external setVotingDelay
_(no internal calls)_


### external setVotingPeriod
_(no internal calls)_


### public state
-> internal add256


### external sweepTokens
_(no internal calls)_


---

## Reservoir

_File: Reservoir.sol_

### public drip
-> internal min


---

## SimplePriceOracle

_File: SimplePriceOracle.sol_

### external assetPrices
_(no internal calls)_


### public getUnderlyingPrice
-> internal compareStrings


### public setDirectPrice
_(no internal calls)_


### public setUnderlyingPrice
_(no internal calls)_


---

## StandardToken

_File: FaucetToken.sol_

### external approve
_(no internal calls)_


### external transfer
_(no internal calls)_


### external transferFrom
_(no internal calls)_


---

## Timelock

_File: Timelock.sol_

### public acceptAdmin
_(no internal calls)_


### public cancelTransaction
_(no internal calls)_


### public executeTransaction
-> internal getBlockTimestamp


### public fastTrackExecuteTransaction
_(no internal calls)_


### public queueTransaction
-> internal getBlockTimestamp


### public setDelay
_(no internal calls)_


### public setPendingAdmin
_(no internal calls)_


---

## Unitroller

_File: Unitroller.sol_

### public _acceptAdmin
-> internal fail


### public _acceptImplementation
-> internal fail


### public _setPendingAdmin
-> internal fail


### public _setPendingImplementation
-> internal fail


---

## Well

_File: Governance/Well.sol_

### external allowance
_(no internal calls)_


### external approve
-> internal safe96


### external balanceOf
_(no internal calls)_


### public delegate
-> internal _delegate
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


### public delegateBySig
-> internal getChainId
-> internal _delegate
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


### external getCurrentVotes
_(no internal calls)_


### public getPriorVotes
_(no internal calls)_


### external permit
-> internal safe96
-> internal getChainId


### external transfer
-> internal safe96
-> internal _transferTokens
  -> internal sub96
  -> internal add96
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


### external transferFrom
-> internal safe96
-> internal sub96
-> internal _transferTokens
  -> internal sub96
  -> internal add96
  -> internal _moveDelegates
    -> internal sub96
    -> internal _writeCheckpoint
      -> internal safe32
    -> internal add96


---

## WhitePaperInterestRateModel

_File: WhitePaperInterestRateModel.sol_

### public getBorrowRate
-> public utilizationRate


### public getSupplyRate
-> public getBorrowRate
  -> public utilizationRate
-> public utilizationRate


### public utilizationRate
_(no internal calls)_

