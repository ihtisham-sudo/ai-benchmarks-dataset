# Callpaths — Benqi

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BenqiChainlinkOracle

_File: lending/Chainlink/BenqiChainlinkOracle.sol_

### external assetPrices
_(no internal calls)_


### public getFeed
_(no internal calls)_


### public getUnderlyingPrice
-> internal compareStrings
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

_File: lending/Comptroller.sol_

### public _become
_(no internal calls)_


### public _grantQi
-> internal adminOrInitializing


### external _setBorrowCapGuardian
_(no internal calls)_


### public _setBorrowPaused
_(no internal calls)_


### external _setCloseFactor
_(no internal calls)_


### external _setCollateralFactor
-> internal fail
-> internal lessThanExp


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


### public setQiAddress
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

## GaugeController

_File: veQI/GaugeController.sol_

### external getNodeUsersLength
_(no internal calls)_


### external getNodeUsersRange
_(no internal calls)_


### external getNodesLength
_(no internal calls)_


### external getNodesRange
_(no internal calls)_


### external getUserVotesLength
_(no internal calls)_


### external getUserVotesRange
_(no internal calls)_


### public getVotesForNode
_(no internal calls)_


### external getVotesRange
-> public getVotesForNode


### public initialize
_(no internal calls)_


### public unvoteNode
-> private removeUserFromNodeUsers
-> private removeNodeFromNodes


### external unvoteNodes
-> public unvoteNode
  -> private removeUserFromNodeUsers
  -> private removeNodeFromNodes


### public voteNode
_(no internal calls)_


### external voteNodes
-> public voteNode


---

## JumpRateModel

_File: lending/JumpRateModel.sol_

### public getBorrowRate
-> public utilizationRate


### public getSupplyRate
-> public getBorrowRate
  -> public utilizationRate
-> public utilizationRate


### public utilizationRate
_(no internal calls)_


---

## Maximillion

_File: lending/Maximillion.sol_

### public repayBehalf
-> public repayBehalfExplicit


### public repayBehalfExplicit
_(no internal calls)_


---

## PauseGuardian

_File: lending/PauseGuardian.sol_

### external areAllMarketsPaused
-> internal _areAllMarketsPaused


### external canPause
-> internal _canPause


### external checkUpkeep
-> internal _canPause
-> internal _areAllMarketsPaused


### external pauseBorrowing
_(no internal calls)_


### external pauseLiquidations
_(no internal calls)_


### external pauseMinting
_(no internal calls)_


### external pauseMintingAndBorrowingForAllMarkets
-> internal _pauseMintingAndBorrowingForAllMarkets


### external pauseMintingAndBorrowingForMarket
_(no internal calls)_


### external pauseTransfers
_(no internal calls)_


### external performUpkeep
-> public proofOfReservesPause
  -> internal _canPause
  -> internal _pauseMintingAndBorrowingForAllMarkets


### public proofOfReservesPause
-> internal _canPause
-> internal _pauseMintingAndBorrowingForAllMarkets


### external removeProofOfReserveFeed
_(no internal calls)_


### external setProofOfReserveFeed
-> internal _setProofOfReserveFeed


---

## PglStakingContract

_File: pgl_staking/PglStakingContract.sol_

### external becomeImplementation
_(no internal calls)_


### external claimRewards
-> internal distributeReward
  -> internal accrueReward
-> internal claimErc20


### external deposit
-> internal distributeReward
  -> internal accrueReward


### external getClaimableRewards
_(no internal calls)_


### external redeem
-> internal distributeReward
  -> internal accrueReward


### external setPglTokenAddress
_(no internal calls)_


### external setRewardSpeed
-> internal accrueReward


### external setRewardTokenAddress
_(no internal calls)_


---

## PglStakingContractProxy

_File: pgl_staking/PglStakingContractProxy.sol_

### public acceptPendingAdmin
_(no internal calls)_


### public acceptPendingImplementation
_(no internal calls)_


### public setPendingAdmin
_(no internal calls)_


### public setPendingImplementation
_(no internal calls)_


---

## Qi

_File: lending/Governance/Qi.sol_

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

## QiAvax

_File: lending/QiAvax.sol_

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

## QiErc20

_File: lending/QiErc20.sol_

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

## QiErc20Delegate

_File: lending/QiErc20Delegate.sol_

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

## QiErc20Delegator

_File: lending/QiErc20Delegator.sol_

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

## QiToken

_File: lending/QiToken.sol_

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

## QiTokenSaleDistributor

_File: token_sale/QiTokenSaleDistributor.sol_

### external becomeImplementation
_(no internal calls)_


### public claim
-> internal _getClaimableTokenAmountPerRound


### public getClaimableTokenAmount
-> internal _getClaimableTokenAmount
  -> internal _getClaimableTokenAmountPerRound


### public getClaimedTokenAmount
_(no internal calls)_


### public getRoundClaimableTokenAmount
-> internal _getClaimableTokenAmountPerRound


### public getRoundClaimedTokenAmount
_(no internal calls)_


### public resetPurchasedTokensByUser
_(no internal calls)_


### public setDataAdmin
_(no internal calls)_


### public setPurchasedTokensByUser
_(no internal calls)_


### public setQiContractAddress
_(no internal calls)_


### public withdrawQi
_(no internal calls)_


---

## QiTokenSaleDistributorProxy

_File: token_sale/QiTokenSaleDistributorProxy.sol_

### public acceptPendingAdmin
_(no internal calls)_


### public acceptPendingImplementation
_(no internal calls)_


### public setPendingAdmin
_(no internal calls)_


### public setPendingImplementation
_(no internal calls)_


---

## RewardLens

_File: lending/RewardLens.sol_

### public getClaimableReward
-> internal updateRewardSupplyIndex
  -> internal sub_
  -> internal mul_
  -> internal fraction
    -> internal div_
    -> internal mul_
  -> internal add_
-> internal distributeSupplierReward
  -> internal sub_
  -> internal mul_
-> internal updateRewardBorrowIndex
  -> internal sub_
  -> internal div_
  -> internal mul_
  -> internal fraction
    -> internal div_
    -> internal mul_
  -> internal add_
-> internal distributeBorrowerReward
  -> internal sub_
  -> internal div_
  -> internal mul_


### public getClaimableRewards
-> public getClaimableReward
  -> internal updateRewardSupplyIndex
    -> internal sub_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
  -> internal distributeSupplierReward
    -> internal sub_
    -> internal mul_
  -> internal updateRewardBorrowIndex
    -> internal sub_
    -> internal div_
    -> internal mul_
    -> internal fraction
      -> internal div_
      -> internal mul_
    -> internal add_
  -> internal distributeBorrowerReward
    -> internal sub_
    -> internal div_
    -> internal mul_


---

## StakedAvax

_File: sAVAX/StakedAvax.sol_

### external accrueRewards
-> internal _dropExpiredExchangeRateEntries
-> public getPooledAvaxByShares


### public allowance
_(no internal calls)_


### public approve
-> internal _approve


### public balanceOf
_(no internal calls)_


### external cancelPendingUnlockRequests
-> internal _isWithinCooldownPeriod
-> internal _cancelUnlockRequest
  -> internal _isExpired
  -> internal _transfer
    -> internal _transferShares


### external cancelRedeemableUnlockRequests
-> internal _isWithinRedemptionPeriod
  -> internal _isWithinCooldownPeriod
-> internal _cancelUnlockRequest
  -> internal _isExpired
  -> internal _transfer
    -> internal _transferShares


### external cancelUnlockRequest
-> internal _cancelUnlockRequest
  -> internal _isExpired
  -> internal _transfer
    -> internal _transferShares


### public decimals
_(no internal calls)_


### external deposit
_(no internal calls)_


### external getPaginatedUnlockRequests
-> internal _isWithinRedemptionPeriod
  -> internal _isWithinCooldownPeriod
-> internal _getExchangeRateByUnlockTimestamp


### public getPooledAvaxByShares
_(no internal calls)_


### public getSharesByPooledAvax
_(no internal calls)_


### external getUnlockRequestCount
_(no internal calls)_


### public initialize
_(no internal calls)_


### public name
_(no internal calls)_


### external pause
_(no internal calls)_


### external pauseMinting
_(no internal calls)_


### external redeem
-> internal _redeem
  -> internal _isWithinRedemptionPeriod
    -> internal _isWithinCooldownPeriod
  -> internal _getExchangeRateByUnlockTimestamp
  -> internal _burnShares


### external redeemOverdueShares
-> internal _isExpired
-> internal _transfer
  -> internal _transferShares


### external requestUnlock
-> internal _transfer
  -> internal _transferShares


### external resume
_(no internal calls)_


### external resumeMinting
_(no internal calls)_


### external setCooldownPeriod
_(no internal calls)_


### external setRedeemPeriod
_(no internal calls)_


### external setTotalPooledAvaxCap
_(no internal calls)_


### public submit
-> public getSharesByPooledAvax
-> internal _mintShares
  -> public getPooledAvaxByShares


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### public transfer
-> internal _transfer
  -> internal _transferShares


### public transferFrom
-> internal _transfer
  -> internal _transferShares
-> internal _approve


### external withdraw
_(no internal calls)_


---

## Unitroller

_File: lending/Unitroller.sol_

### public _acceptAdmin
-> internal fail


### public _acceptImplementation
-> internal fail


### public _setPendingAdmin
-> internal fail


### public _setPendingImplementation
-> internal fail


---

## VeERC20Upgradeable

_File: veQI/VeERC20Upgradeable.sol_

### public balanceOf
_(no internal calls)_


### public decimals
_(no internal calls)_


### public name
_(no internal calls)_


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


---

## VeQi

_File: veQI/VeQi.sol_

### public balanceOf
_(no internal calls)_


### external claim
-> public isUser
-> private _claim
  -> private _claimable
    -> library Math.wmul
    -> public balanceOf
  -> internal _mint
    -> internal _beforeTokenTransfer
    -> internal _afterTokenOperation


### external claimable
-> private _claimable
  -> library Math.wmul
  -> public balanceOf


### public decimals
_(no internal calls)_


### external deposit
-> public isUser
-> private _claim
  -> private _claimable
    -> library Math.wmul
    -> public balanceOf
  -> internal _mint
    -> internal _beforeTokenTransfer
    -> internal _afterTokenOperation


### external eventualBalanceOf
-> public balanceOf
-> private _claimable
  -> library Math.wmul
  -> public balanceOf


### external eventualTotalSupply
-> private _claimable
  -> library Math.wmul
  -> public balanceOf


### external getStakedQi
_(no internal calls)_


### external initialize
-> internal __ERC20_init
  -> internal __ERC20_init_unchained


### public isUser
_(no internal calls)_


### public name
_(no internal calls)_


### external pause
_(no internal calls)_


### external setGenerationRate
_(no internal calls)_


### external setMaxCap
_(no internal calls)_


### public symbol
_(no internal calls)_


### public totalSupply
_(no internal calls)_


### external unpause
_(no internal calls)_


### external withdraw
-> public balanceOf
-> internal _burn
  -> internal _beforeTokenTransfer
  -> internal _afterTokenOperation
-> private _removeUserFromUserList


---

## WhitePaperInterestRateModel

_File: lending/WhitePaperInterestRateModel.sol_

### public getBorrowRate
-> public utilizationRate


### public getSupplyRate
-> public getBorrowRate
  -> public utilizationRate
-> public utilizationRate


### public utilizationRate
_(no internal calls)_

