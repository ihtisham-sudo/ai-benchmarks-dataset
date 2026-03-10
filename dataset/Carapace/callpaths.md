# Callpaths — Carapace

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ContractFactory

_File: core/ContractFactory.sol_

### external createLendingProtocolAdapter
-> internal _createLendingProtocolAdapter


### external createProtectionPool
_(no internal calls)_


### external createReferenceLendingPools
_(no internal calls)_


### external getLendingProtocolAdapter
_(no internal calls)_


### external getProtectionPools
_(no internal calls)_


### external getReferenceLendingPoolsList
_(no internal calls)_


### external initialize
-> internal __UUPSUpgradeableBase_init


---

## DefaultStateManager

_File: core/DefaultStateManager.sol_

### external assessStateBatch
-> internal _assessState
  -> internal _moveFromActiveToLockedState
  -> internal _getTwoPaymentPeriodsInSeconds
  -> internal _moveFromLockedToActiveState
    -> internal _getLatestLockedCapital


### external assessStates
-> internal _assessState
  -> internal _moveFromActiveToLockedState
  -> internal _getTwoPaymentPeriodsInSeconds
  -> internal _moveFromLockedToActiveState
    -> internal _getLatestLockedCapital


### external calculateAndClaimUnlockedCapital
-> internal _calculateClaimableAmount


### external calculateClaimableUnlockedAmount
-> internal _calculateClaimableAmount


### external getLendingPoolStatus
_(no internal calls)_


### external getLockedCapitals
_(no internal calls)_


### external getPoolStateUpdateTimestamp
_(no internal calls)_


### external initialize
-> internal __UUPSUpgradeableBase_init


### external registerProtectionPool
-> internal _assessState
  -> internal _moveFromActiveToLockedState
  -> internal _getTwoPaymentPeriodsInSeconds
  -> internal _moveFromLockedToActiveState
    -> internal _getLatestLockedCapital


### external setContractFactory
_(no internal calls)_


---

## GoldfinchAdapter

_File: adapters/GoldfinchAdapter.sol_

### external calculateProtectionBuyerAPR
-> internal _getProtocolFeePercent
-> internal _getLeverageRatio


### public calculateRemainingPrincipal
-> internal _getPoolTokens
-> internal _isJuniorTrancheId


### public getLatestPaymentTimestamp
-> internal _getLatestPaymentTimestamp
  -> internal _getCreditLine


### external getLendingPoolTermEndTimestamp
-> internal _getCreditLine


### public getPaymentPeriodInDays
-> internal _getCreditLine


### external initialize
-> internal __UUPSUpgradeableBase_init


### external isLendingPoolExpired
-> internal _getCreditLine


### external isLendingPoolLate
-> internal _isLendingPoolLate
  -> internal _getCreditLine


### external isLendingPoolLateWithinGracePeriod
-> internal _getLatestPaymentTimestamp
  -> internal _getCreditLine
-> internal _isLendingPoolLate
  -> internal _getCreditLine
-> internal _getCreditLine


---

## PremiumCalculator

_File: core/PremiumCalculator.sol_

### external calculatePremium
-> internal _calculateDurationInYears
-> library RiskFactorCalculator.canCalculateRiskFactor
-> library RiskFactorCalculator.calculateRiskFactor
-> internal _calculateCarapacePremiumRate
-> internal _calculateUnderlyingPremiumRate


### external initialize
-> internal __UUPSUpgradeableBase_init


---

## ProtectionPool

_File: core/pool/ProtectionPool.sol_

### external accruePremiumAndExpireProtections
-> internal _accruePremiumAndExpireProtections
  -> library ProtectionPoolHelper.verifyAndAccruePremium
  -> library ProtectionPoolHelper.expireProtection


### external buyProtection
-> internal _verifyAndCreateProtection
  -> library ProtectionPoolHelper.verifyProtection
  -> public calculateLeverageRatio
    -> internal _calculateLeverageRatio
  -> library ProtectionPoolHelper.calculateAndTrackPremium
  -> library AccruedPremiumCalculator.calculateKAndLambda


### public calculateLeverageRatio
-> internal _calculateLeverageRatio


### external calculateMaxAllowedProtectionAmount
_(no internal calls)_


### external calculateMaxAllowedProtectionDuration
_(no internal calls)_


### external calculateProtectionPremium
-> public calculateLeverageRatio
  -> internal _calculateLeverageRatio


### external claimUnlockedCapital
_(no internal calls)_


### public convertToSToken
-> internal _getExchangeRate


### public convertToUnderlying
-> library ProtectionPoolHelper.scale18DecimalsAmtToUnderlyingDecimals
-> internal _getExchangeRate


### external deposit
-> internal _deposit
  -> public convertToSToken
    -> internal _getExchangeRate
  -> internal _safeMint
  -> internal _hasMinRequiredCapital
  -> public calculateLeverageRatio
    -> internal _calculateLeverageRatio


### external depositAndRequestWithdrawal
-> internal _deposit
  -> public convertToSToken
    -> internal _getExchangeRate
  -> internal _safeMint
  -> internal _hasMinRequiredCapital
  -> public calculateLeverageRatio
    -> internal _calculateLeverageRatio
-> internal _requestWithdrawal


### external getActiveProtections
_(no internal calls)_


### external getAllProtections
_(no internal calls)_


### external getCurrentRequestedWithdrawalAmount
-> internal _getRequestedWithdrawalAmount


### external getLendingPoolDetail
_(no internal calls)_


### external getPoolDetails
_(no internal calls)_


### external getPoolInfo
_(no internal calls)_


### external getRequestedWithdrawalAmount
-> internal _getRequestedWithdrawalAmount


### external getTotalPremiumPaidForLendingPool
_(no internal calls)_


### external getTotalRequestedWithdrawalAmount
_(no internal calls)_


### external getUnderlyingBalance
-> public convertToUnderlying
  -> library ProtectionPoolHelper.scale18DecimalsAmtToUnderlyingDecimals
  -> internal _getExchangeRate


### external initialize
-> internal __UUPSUpgradeableBase_init
-> internal __sToken_init


### external lockCapital
_(no internal calls)_


### external movePoolPhase
-> internal _hasMinRequiredCapital
-> public calculateLeverageRatio
  -> internal _calculateLeverageRatio


### external pause
_(no internal calls)_


### external renewProtection
-> library ProtectionPoolHelper.verifyBuyerCanRenewProtection
-> internal _verifyAndCreateProtection
  -> library ProtectionPoolHelper.verifyProtection
  -> public calculateLeverageRatio
    -> internal _calculateLeverageRatio
  -> library ProtectionPoolHelper.calculateAndTrackPremium
  -> library AccruedPremiumCalculator.calculateKAndLambda


### external requestWithdrawal
-> internal _requestWithdrawal


### external unpause
_(no internal calls)_


### external updateLeverageRatioParams
_(no internal calls)_


### external updateMinRequiredCapital
_(no internal calls)_


### external updateRiskPremiumParams
_(no internal calls)_


### external withdraw
-> public convertToUnderlying
  -> library ProtectionPoolHelper.scale18DecimalsAmtToUnderlyingDecimals
  -> internal _getExchangeRate


---

## ProtectionPoolCycleManager

_File: core/ProtectionPoolCycleManager.sol_

### external calculateAndSetPoolCycleState
-> internal _startNewCycle


### external getCurrentCycleIndex
_(no internal calls)_


### external getCurrentCycleState
_(no internal calls)_


### external getCurrentPoolCycle
_(no internal calls)_


### external getNextCycleEndTimestamp
_(no internal calls)_


### external initialize
-> internal __UUPSUpgradeableBase_init


### external registerProtectionPool
-> internal _startNewCycle


### external setContractFactory
_(no internal calls)_


---

## ReferenceLendingPools

_File: core/pool/ReferenceLendingPools.sol_

### external addReferenceLendingPool
-> internal _addReferenceLendingPool
  -> internal _isReferenceLendingPoolAdded
  -> internal _getLendingPoolStatus
    -> internal _isReferenceLendingPoolAdded
    -> internal _getLendingProtocolAdapter


### public assessState
-> internal _getLendingPoolStatus
  -> internal _isReferenceLendingPoolAdded
  -> internal _getLendingProtocolAdapter


### public calculateProtectionBuyerAPR
-> internal _getLendingProtocolAdapter


### public calculateRemainingPrincipal
-> internal _getLendingProtocolAdapter


### external canBuyProtection
-> public calculateRemainingPrincipal
  -> internal _getLendingProtocolAdapter


### public getLatestPaymentTimestamp
-> internal _getLendingProtocolAdapter


### public getLendingPools
_(no internal calls)_


### public getPaymentPeriodInDays
-> internal _getLendingProtocolAdapter


### external initialize
-> internal __UUPSUpgradeableBase_init
-> internal _addReferenceLendingPool
  -> internal _isReferenceLendingPoolAdded
  -> internal _getLendingPoolStatus
    -> internal _isReferenceLendingPoolAdded
    -> internal _getLendingProtocolAdapter

