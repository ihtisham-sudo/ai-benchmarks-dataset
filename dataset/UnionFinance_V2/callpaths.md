# Callpaths — UnionFinance_V2

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AaveV3Adapter

_File: contracts/asset/AaveV3Adapter.sol_

### public __AaveV3Adapter_init
-> external_callback Controller.__Controller_init


### external acceptAdmin
_(no internal calls)_


### external claimRewards
_(no internal calls)_


### external deposit
_(no internal calls)_


### external getRate
_(no internal calls)_


### external getSupply
-> internal _getSupply


### external getSupplyView
-> internal _getSupply


### external isAdmin
_(no internal calls)_


### external mapTokenToAToken
_(no internal calls)_


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### external setAssetManager
_(no internal calls)_


### external setCeiling
_(no internal calls)_


### external setFloor
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external supportsToken
-> internal _supportsToken


### external unpause
_(no internal calls)_


### external withdraw
-> internal _checkBal


### external withdrawAll
-> internal _checkBal


---

## AssetManager

_File: contracts/asset/AssetManager.sol_

### external __AssetManager_init
-> external_callback Controller.__Controller_init


### external acceptAdmin
_(no internal calls)_


### external addAdapter
-> public approveAllTokensMax
  -> internal _increaseAllowance


### external addToken
-> public approveAllMarketsMax
  -> internal _increaseAllowance


### public approveAllMarketsMax
-> internal _increaseAllowance


### public approveAllTokensMax
-> internal _increaseAllowance


### external debtWriteOff
_(no internal calls)_


### external deposit
-> private _isUToken
-> public isMarketSupported


### public getLoanableAmount
-> public getPoolBalance
  -> public isMarketSupported
  -> public totalSupplyView
    -> public isMarketSupported


### external getMoneyMarket
_(no internal calls)_


### public getPoolBalance
-> public isMarketSupported
-> public totalSupplyView
  -> public isMarketSupported


### external isAdmin
_(no internal calls)_


### public isMarketSupported
_(no internal calls)_


### external moneyMarketsCount
_(no internal calls)_


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### external rebalance
_(no internal calls)_


### external removeAdapter
-> private _removeTokenApprovals


### external removeToken
-> private _removeMarketsApprovals


### external setGuardian
_(no internal calls)_


### external setMarketRegistry
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external setWithdrawSequence
_(no internal calls)_


### external supportedTokensCount
_(no internal calls)_


### external totalSupply
-> public isMarketSupported


### public totalSupplyView
-> public isMarketSupported


### external unpause
_(no internal calls)_


### external withdraw
-> private _checkSenderBalance
  -> private _isUToken
  -> public getLoanableAmount
    -> public getPoolBalance
      -> public isMarketSupported
      -> public totalSupplyView
        -> public isMarketSupported
-> public isMarketSupported
-> private _isUToken


---

## Comptroller

_File: contracts/token/Comptroller.sol_

### public __Comptroller_init
-> external_callback Controller.__Controller_init
-> internal getTimestamp


### external acceptAdmin
_(no internal calls)_


### external accrueRewards
-> private _accrueRewards
  -> internal _getUserManager
  -> internal _calculateRewardsInternal
    -> internal _getRewardsMultiplier
    -> internal _getInflationIndexNew
      -> internal _getInflationIndex
        -> internal _inflationPerSecond
          -> internal _lookup
    -> internal getTimestamp
  -> internal _getInflationIndexNew
    -> internal _getInflationIndex
      -> internal _inflationPerSecond
        -> internal _lookup
  -> internal getTimestamp


### public calculateRewards
-> internal _getUserManager
-> internal _calculateRewardsInternal
  -> internal _getRewardsMultiplier
  -> internal _getInflationIndexNew
    -> internal _getInflationIndex
      -> internal _inflationPerSecond
        -> internal _lookup
  -> internal getTimestamp


### external getRewardsMultiplier
-> internal _getUserManager
-> internal _getRewardsMultiplier


### public inflationPerSecond
-> internal _inflationPerSecond
  -> internal _lookup


### external isAdmin
_(no internal calls)_


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### public setHalfDecayPoint
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external unpause
_(no internal calls)_


### external updateTotalStaked
-> internal _getInflationIndexNew
  -> internal _getInflationIndex
    -> internal _inflationPerSecond
      -> internal _lookup
-> internal getTimestamp


### external withdrawRewards
-> private _accrueRewards
  -> internal _getUserManager
  -> internal _calculateRewardsInternal
    -> internal _getRewardsMultiplier
    -> internal _getInflationIndexNew
      -> internal _getInflationIndex
        -> internal _inflationPerSecond
          -> internal _lookup
    -> internal getTimestamp
  -> internal _getInflationIndexNew
    -> internal _getInflationIndex
      -> internal _inflationPerSecond
        -> internal _lookup
  -> internal getTimestamp


---

## Controller

_File: contracts/Controller.sol_

### external acceptAdmin
_(no internal calls)_


### external isAdmin
_(no internal calls)_


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## ERC1155Voucher

_File: contracts/peripheral/ERC1155Voucher.sol_

### external exit
_(no internal calls)_


### external onERC1155BatchReceived
-> internal _vouchFor


### external onERC1155Received
-> internal _vouchFor


### external setIsValid
_(no internal calls)_


### external setTrustAmount
_(no internal calls)_


### external stake
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### external transferERC20
_(no internal calls)_


---

## FixedInterestRateModel

_File: contracts/market/FixedInterestRateModel.sol_

### public getBorrowRate
_(no internal calls)_


### public getSupplyRate
_(no internal calls)_


### external setInterestRate
_(no internal calls)_


---

## MarketRegistry

_File: contracts/market/MarketRegistry.sol_

### public __MarketRegistry_init
-> external_callback Controller.__Controller_init


### external acceptAdmin
_(no internal calls)_


### external hasUToken
_(no internal calls)_


### external hasUserManager
_(no internal calls)_


### external isAdmin
_(no internal calls)_


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external setUToken
_(no internal calls)_


### external setUserManager
_(no internal calls)_


### external unpause
_(no internal calls)_


---

## OpConnector

_File: contracts/token/OpConnector.sol_

### external bridge
_(no internal calls)_


### external claimTokens
_(no internal calls)_


---

## OpOwner

_File: contracts/OpOwner.sol_

### public acceptAdmin
_(no internal calls)_


### public acceptOwner
_(no internal calls)_


### public admin
_(no internal calls)_


### public execute
_(no internal calls)_


### public owner
_(no internal calls)_


### public pendingAdmin
_(no internal calls)_


### public pendingOwner
_(no internal calls)_


### public setPendingAdmin
_(no internal calls)_


### public setPendingOwner
_(no internal calls)_


---

## OpUNION

_File: contracts/token/OpUNION.sol_

### external disableWhitelist
_(no internal calls)_


### external enableWhitelist
_(no internal calls)_


### public isWhitelisted
_(no internal calls)_


### external unwhitelist
_(no internal calls)_


### public whitelist
_(no internal calls)_


---

## PureTokenAdapter

_File: contracts/asset/PureTokenAdapter.sol_

### public __PureTokenAdapter_init
-> external_callback Controller.__Controller_init


### external acceptAdmin
_(no internal calls)_


### external claimRewards
_(no internal calls)_


### external deposit
_(no internal calls)_


### external getRate
_(no internal calls)_


### external getSupply
-> internal _getSupply


### external getSupplyView
-> internal _getSupply


### external isAdmin
_(no internal calls)_


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### external setAssetManager
_(no internal calls)_


### external setCeiling
_(no internal calls)_


### external setFloor
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external supportsToken
-> internal _supportsToken


### external unpause
_(no internal calls)_


### external withdraw
_(no internal calls)_


### external withdrawAll
_(no internal calls)_


---

## UDai

_File: contracts/market/UDai.sol_

### public __UToken_init
-> external_callback Controller.__Controller_init
-> internal getTimestamp


### public _borrowBalanceView
-> private _getBorrowed
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed


### public accrueInterest
-> public borrowRatePerSecond
-> internal getTimestamp


### external addReserves
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _depositToAssetManager


### external balanceOfUnderlying
-> private _exchangeRateStored


### external borrow
-> public calculatingFee
-> public _borrowBalanceView
  -> private _getBorrowed
  -> internal _calculatingInterest
    -> public borrowRatePerSecond
    -> internal getTimestamp
    -> private _getBorrowed
-> public checkIsOverdue
  -> private _getBorrowed
  -> public getLastRepay
  -> internal getTimestamp
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal borrowBalanceStoredInternal
-> public getLastRepay
-> internal getTimestamp
-> private _getBorrowed


### public borrowBalanceView
-> public getBorrowed
  -> private _getBorrowed
-> public calculatingInterest
  -> internal _calculatingInterest
    -> public borrowRatePerSecond
    -> internal getTimestamp
    -> private _getBorrowed


### public borrowRatePerSecond
_(no internal calls)_


### public calculatingFee
_(no internal calls)_


### public calculatingInterest
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed


### public checkIsOverdue
-> private _getBorrowed
-> public getLastRepay
-> internal getTimestamp


### public debtCeiling
_(no internal calls)_


### external debtWriteOff
-> private _getBorrowed


### public exchangeRateCurrent
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored


### public exchangeRateStored
-> private _exchangeRateStored


### public getBorrowed
-> private _getBorrowed


### public getLastRepay
_(no internal calls)_


### public getRemainingDebtCeiling
_(no internal calls)_


### public maxBorrow
_(no internal calls)_


### public minBorrow
_(no internal calls)_


### external mint
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored
-> internal _depositToAssetManager


### external redeem
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored


### external removeReserves
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp


### external repayBorrow
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external repayBorrowWithPermit
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external repayInterest
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external setAssetManager
_(no internal calls)_


### external setDebtCeiling
_(no internal calls)_


### external setInterestRateModel
_(no internal calls)_


### external setMaxBorrow
_(no internal calls)_


### external setMinBorrow
_(no internal calls)_


### external setMintFeeRate
_(no internal calls)_


### external setOriginationFee
_(no internal calls)_


### external setOverdueTime
_(no internal calls)_


### external setReserveFactor
_(no internal calls)_


### external setUserManager
_(no internal calls)_


### external supplyRatePerSecond
_(no internal calls)_


### public totalBorrows
_(no internal calls)_


### public totalRedeemable
_(no internal calls)_


### public totalReserves
_(no internal calls)_


---

## UErc20

_File: contracts/market/UErc20.sol_

### public __UToken_init
-> external_callback Controller.__Controller_init
-> internal getTimestamp


### public _borrowBalanceView
-> private _getBorrowed
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed


### public accrueInterest
-> public borrowRatePerSecond
-> internal getTimestamp


### external addReserves
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _depositToAssetManager


### external balanceOfUnderlying
-> private _exchangeRateStored


### external borrow
-> public calculatingFee
-> public _borrowBalanceView
  -> private _getBorrowed
  -> internal _calculatingInterest
    -> public borrowRatePerSecond
    -> internal getTimestamp
    -> private _getBorrowed
-> public checkIsOverdue
  -> private _getBorrowed
  -> public getLastRepay
  -> internal getTimestamp
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal borrowBalanceStoredInternal
-> public getLastRepay
-> internal getTimestamp
-> private _getBorrowed


### public borrowBalanceView
-> public getBorrowed
  -> private _getBorrowed
-> public calculatingInterest
  -> internal _calculatingInterest
    -> public borrowRatePerSecond
    -> internal getTimestamp
    -> private _getBorrowed


### public borrowRatePerSecond
_(no internal calls)_


### public calculatingFee
_(no internal calls)_


### public calculatingInterest
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed


### public checkIsOverdue
-> private _getBorrowed
-> public getLastRepay
-> internal getTimestamp


### public debtCeiling
_(no internal calls)_


### external debtWriteOff
-> private _getBorrowed


### public exchangeRateCurrent
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored


### public exchangeRateStored
-> private _exchangeRateStored


### public getBorrowed
-> private _getBorrowed


### public getLastRepay
_(no internal calls)_


### public getRemainingDebtCeiling
_(no internal calls)_


### public maxBorrow
_(no internal calls)_


### public minBorrow
_(no internal calls)_


### external mint
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored
-> internal _depositToAssetManager


### external redeem
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored


### external removeReserves
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp


### external repayBorrow
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external repayBorrowWithERC20Permit
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external repayInterest
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external setAssetManager
_(no internal calls)_


### external setDebtCeiling
_(no internal calls)_


### external setInterestRateModel
_(no internal calls)_


### external setMaxBorrow
_(no internal calls)_


### external setMinBorrow
_(no internal calls)_


### external setMintFeeRate
_(no internal calls)_


### external setOriginationFee
_(no internal calls)_


### external setOverdueTime
_(no internal calls)_


### external setReserveFactor
_(no internal calls)_


### external setUserManager
_(no internal calls)_


### external supplyRatePerSecond
_(no internal calls)_


### public totalBorrows
_(no internal calls)_


### public totalRedeemable
_(no internal calls)_


### public totalReserves
_(no internal calls)_


---

## UToken

_File: contracts/market/UToken.sol_

### public __UToken_init
-> external_callback Controller.__Controller_init
-> internal decimalScaling
-> internal getTimestamp


### public _borrowBalanceView
-> private _getBorrowed
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed


### external acceptAdmin
_(no internal calls)_


### public accrueInterest
-> public borrowRatePerSecond
-> internal getTimestamp


### external addReserves
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal decimalScaling
-> internal _depositToAssetManager


### external balanceOfUnderlying
-> internal decimalReducing
-> private _exchangeRateStored


### external borrow
-> internal decimalScaling
-> public calculatingFee
-> public _borrowBalanceView
  -> private _getBorrowed
  -> internal _calculatingInterest
    -> public borrowRatePerSecond
    -> internal getTimestamp
    -> private _getBorrowed
-> public checkIsOverdue
  -> private _getBorrowed
  -> public getLastRepay
  -> internal getTimestamp
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal borrowBalanceStoredInternal
-> public getLastRepay
-> internal getTimestamp
-> private _getBorrowed
-> internal decimalReducing


### public borrowBalanceView
-> public getBorrowed
  -> internal decimalReducing
  -> private _getBorrowed
-> public calculatingInterest
  -> internal decimalReducing
  -> internal _calculatingInterest
    -> public borrowRatePerSecond
    -> internal getTimestamp
    -> private _getBorrowed


### public borrowRatePerSecond
_(no internal calls)_


### public calculatingFee
_(no internal calls)_


### public calculatingInterest
-> internal decimalReducing
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed


### public checkIsOverdue
-> private _getBorrowed
-> public getLastRepay
-> internal getTimestamp


### public debtCeiling
-> internal decimalReducing


### external debtWriteOff
-> internal decimalScaling
-> private _getBorrowed


### public exchangeRateCurrent
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored


### public exchangeRateStored
-> private _exchangeRateStored


### public getBorrowed
-> internal decimalReducing
-> private _getBorrowed


### public getLastRepay
_(no internal calls)_


### public getRemainingDebtCeiling
-> internal decimalReducing


### external isAdmin
_(no internal calls)_


### public maxBorrow
-> internal decimalReducing


### public minBorrow
-> internal decimalReducing


### external mint
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored
-> internal decimalScaling
-> internal _depositToAssetManager


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### external redeem
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> private _exchangeRateStored
-> internal decimalReducing
-> internal decimalScaling


### external removeReserves
-> internal decimalScaling
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp


### external repayBorrow
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal decimalScaling
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> internal decimalReducing
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external repayInterest
-> public accrueInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
-> internal _calculatingInterest
  -> public borrowRatePerSecond
  -> internal getTimestamp
  -> private _getBorrowed
-> internal _repayBorrowFresh
  -> internal getTimestamp
  -> internal borrowBalanceStoredInternal
  -> public getLastRepay
  -> internal decimalReducing
  -> private _getBorrowed
  -> internal _depositToAssetManager


### external setAssetManager
_(no internal calls)_


### external setDebtCeiling
-> internal decimalScaling


### external setGuardian
_(no internal calls)_


### external setInterestRateModel
_(no internal calls)_


### external setMaxBorrow
-> internal decimalScaling


### external setMinBorrow
-> internal decimalScaling


### external setMintFeeRate
_(no internal calls)_


### external setOriginationFee
_(no internal calls)_


### external setOverdueTime
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external setReserveFactor
_(no internal calls)_


### external setUserManager
_(no internal calls)_


### external supplyRatePerSecond
_(no internal calls)_


### public totalBorrows
-> internal decimalReducing


### public totalRedeemable
-> internal decimalReducing


### public totalReserves
-> internal decimalReducing


### external unpause
_(no internal calls)_


---

## UnionLens

_File: contracts/UnionLens.sol_

### public getBorrowerAddresses
_(no internal calls)_


### public getRelatedInfo
-> public getVouchInfo


### public getStakerAddresses
_(no internal calls)_


### public getUserInfo
_(no internal calls)_


### public getVouchInfo
_(no internal calls)_


---

## UserManager

_File: contracts/user/UserManager.sol_

### public __UserManager_init
-> external_callback Controller.__Controller_init


### external acceptAdmin
_(no internal calls)_


### external addMember
_(no internal calls)_


### external batchUpdateFrozenInfo
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### public cancelVouch
-> internal _cancelVouchInternal


### public checkIsMember
_(no internal calls)_


### external debtWriteOff
-> internal decimalScaling
-> internal getTimestamp
-> internal _cancelVouchInternal


### public frozenCoinAge
-> internal decimalReducing


### external getCreditLimit
-> private _min
-> internal decimalReducing


### external getLockedStake
-> internal decimalReducing


### external getStakeInfo
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max
-> internal decimalReducing


### external getStakeInfoMantissa
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### external getStakerBalance
-> internal decimalReducing


### external getTotalLockedStake
-> internal decimalReducing


### external getVoucheeCount
_(no internal calls)_


### external getVoucherCount
_(no internal calls)_


### external getVouchingAmount
-> internal decimalReducing


### external globalTotalStaked
_(no internal calls)_


### external isAdmin
_(no internal calls)_


### public maxStakeAmount
-> internal decimalReducing


### public memberFrozen
-> internal decimalReducing


### external onRepayBorrow
-> internal getTimestamp
-> private _calcFrozenCoinAge
  -> private _max


### external onWithdrawRewards
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max
-> internal getTimestamp


### external pause
_(no internal calls)_


### external paused
_(no internal calls)_


### public registerMember
-> internal _validateNewMember


### external registerMemberWithPermit
-> public registerMember
  -> internal _validateNewMember


### external setEffectiveCount
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### external setMaxOverdueTime
_(no internal calls)_


### external setMaxStakeAmount
-> internal decimalScaling
-> internal decimalReducing


### external setMaxVouchees
_(no internal calls)_


### external setMaxVouchers
_(no internal calls)_


### external setNewMemberFee
_(no internal calls)_


### external setPendingAdmin
_(no internal calls)_


### external setUToken
_(no internal calls)_


### public stake
-> internal decimalScaling


### public stakers
-> internal decimalReducing


### public totalFrozen
-> internal decimalReducing


### public totalStaked
-> internal decimalReducing


### external unpause
_(no internal calls)_


### external unstake
-> internal decimalScaling


### external updateLocked
-> internal decimalScaling
-> internal getTimestamp
-> private _calcLockedCoinAge
  -> private _max
-> private _min


### external updateTrust
-> internal decimalScaling


### public vouchers
-> internal decimalReducing


### external withdrawRewards
_(no internal calls)_


---

## UserManagerDAI

_File: contracts/user/UserManagerDAI.sol_

### public __UserManager_init
-> external_callback Controller.__Controller_init


### external addMember
_(no internal calls)_


### external batchUpdateFrozenInfo
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### public cancelVouch
-> internal _cancelVouchInternal


### public checkIsMember
_(no internal calls)_


### external debtWriteOff
-> internal getTimestamp
-> internal _cancelVouchInternal


### public frozenCoinAge
_(no internal calls)_


### external getCreditLimit
-> private _min


### external getLockedStake
_(no internal calls)_


### external getStakeInfo
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### external getStakeInfoMantissa
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### external getStakerBalance
_(no internal calls)_


### external getTotalLockedStake
_(no internal calls)_


### external getVoucheeCount
_(no internal calls)_


### external getVoucherCount
_(no internal calls)_


### external getVouchingAmount
_(no internal calls)_


### external globalTotalStaked
_(no internal calls)_


### public maxStakeAmount
_(no internal calls)_


### public memberFrozen
_(no internal calls)_


### external onRepayBorrow
-> internal getTimestamp
-> private _calcFrozenCoinAge
  -> private _max


### external onWithdrawRewards
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max
-> internal getTimestamp


### public registerMember
-> internal _validateNewMember


### external registerMemberWithPermit
-> public registerMember
  -> internal _validateNewMember


### external setEffectiveCount
_(no internal calls)_


### external setMaxOverdueTime
_(no internal calls)_


### external setMaxStakeAmount
_(no internal calls)_


### external setMaxVouchees
_(no internal calls)_


### external setMaxVouchers
_(no internal calls)_


### external setNewMemberFee
_(no internal calls)_


### external setUToken
_(no internal calls)_


### public stake
_(no internal calls)_


### external stakeWithPermit
-> public stake


### public stakers
_(no internal calls)_


### public totalFrozen
_(no internal calls)_


### public totalStaked
_(no internal calls)_


### external unstake
_(no internal calls)_


### external updateLocked
-> internal getTimestamp
-> private _calcLockedCoinAge
  -> private _max
-> private _min


### external updateTrust
_(no internal calls)_


### public vouchers
_(no internal calls)_


### external withdrawRewards
_(no internal calls)_


---

## UserManagerERC20

_File: contracts/user/UserManagerERC20.sol_

### public __UserManager_init
-> external_callback Controller.__Controller_init


### external addMember
_(no internal calls)_


### external batchUpdateFrozenInfo
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### public cancelVouch
-> internal _cancelVouchInternal


### public checkIsMember
_(no internal calls)_


### external debtWriteOff
-> internal getTimestamp
-> internal _cancelVouchInternal


### public frozenCoinAge
_(no internal calls)_


### external getCreditLimit
-> private _min


### external getLockedStake
_(no internal calls)_


### external getStakeInfo
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### external getStakeInfoMantissa
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max


### external getStakerBalance
_(no internal calls)_


### external getTotalLockedStake
_(no internal calls)_


### external getVoucheeCount
_(no internal calls)_


### external getVoucherCount
_(no internal calls)_


### external getVouchingAmount
_(no internal calls)_


### external globalTotalStaked
_(no internal calls)_


### public maxStakeAmount
_(no internal calls)_


### public memberFrozen
_(no internal calls)_


### external onRepayBorrow
-> internal getTimestamp
-> private _calcFrozenCoinAge
  -> private _max


### external onWithdrawRewards
-> private _getEffectiveAmounts
  -> internal getTimestamp
  -> private _calcStakedCoinAge
  -> private _calcLockedCoinAge
    -> private _max
  -> private _calcFrozenCoinAge
    -> private _max
-> internal getTimestamp


### public registerMember
-> internal _validateNewMember


### external registerMemberWithPermit
-> public registerMember
  -> internal _validateNewMember


### external setEffectiveCount
_(no internal calls)_


### external setMaxOverdueTime
_(no internal calls)_


### external setMaxStakeAmount
_(no internal calls)_


### external setMaxVouchees
_(no internal calls)_


### external setMaxVouchers
_(no internal calls)_


### external setNewMemberFee
_(no internal calls)_


### external setUToken
_(no internal calls)_


### public stake
_(no internal calls)_


### external stakeWithERC20Permit
-> public stake


### public stakers
_(no internal calls)_


### public totalFrozen
_(no internal calls)_


### public totalStaked
_(no internal calls)_


### external unstake
_(no internal calls)_


### external updateLocked
-> internal getTimestamp
-> private _calcLockedCoinAge
  -> private _max
-> private _min


### external updateTrust
_(no internal calls)_


### public vouchers
_(no internal calls)_


### external withdrawRewards
_(no internal calls)_


---

## UserManagerOp

_File: contracts/user/UserManagerOp.sol_

### public registerMember
_(no internal calls)_


### external stakeWithERC20Permit
_(no internal calls)_


---

## VouchFaucet

_File: contracts/peripheral/VouchFaucet.sol_

### external claimTokens
_(no internal calls)_


### external claimVouch
_(no internal calls)_


### external exit
_(no internal calls)_


### external setMaxClaimable
_(no internal calls)_


### external stake
_(no internal calls)_


### external transferERC20
_(no internal calls)_


---

## Whitelistable

_File: contracts/token/Whitelistable.sol_

### external disableWhitelist
_(no internal calls)_


### external enableWhitelist
_(no internal calls)_


### public isWhitelisted
_(no internal calls)_


### external unwhitelist
_(no internal calls)_


### public whitelist
_(no internal calls)_

