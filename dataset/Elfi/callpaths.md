# Callpaths — Elfi

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AccountFacet

_File: contracts/facets/AccountFacet.sol_

### external batchUpdateAccountToken
-> library AddressUtils.validEmpty
-> library AssetsProcess.updateAccountToken


### external cancelWithdraw
-> library RoleAccessControl.checkRole
-> library Withdraw.get
-> library Errors.WithdrawRequestNotExists
-> library AssetsProcess.cancelWithdraw


### external createWithdrawRequest
-> library AddressUtils.validEmpty
-> library Errors.AmountZeroNotAllowed
-> library AssetsProcess.createWithdrawRequest


### external deposit
-> library Errors.AmountZeroNotAllowed
-> library Errors.AmountNotMatch
-> library AppTradeTokenConfig.getTradeTokenConfig
-> library Errors.OnlyCollateralSupported
-> library AssetsProcess.deposit
-> library AssetsProcess.DepositParams
-> library AppConfig.getChainConfig


### external executeWithdraw
-> library RoleAccessControl.checkRole
-> library Withdraw.get
-> library Errors.WithdrawRequestNotExists
-> library OracleProcess.setOraclePrice
-> library AssetsProcess.executeWithdraw
-> library OracleProcess.clearOraclePrice


### external getAccountInfo
-> library Account.load


### external getAccountInfoWithOracles
-> library Account.load


---

## ConfigFacet

_File: contracts/facets/ConfigFacet.sol_

### external getConfig
-> library ConfigProcess.getConfig


### public getPoolConfig
-> library ConfigProcess.getPoolConfig


### public getSymbolConfig
-> library ConfigProcess.getSymbolConfig


### public getUsdPoolConfig
-> library ConfigProcess.getUsdPoolConfig


### external setConfig
-> library RoleAccessControl.checkRole
-> library ConfigProcess.setConfig


### external setPoolConfig
-> library RoleAccessControl.checkRole
-> library ConfigProcess.setPoolConfig


### external setSymbolConfig
-> library RoleAccessControl.checkRole
-> library ConfigProcess.setSymbolConfig


### external setUniswapRouter
-> library RoleAccessControl.checkRole
-> library ConfigProcess.setUniswapRouter


### external setUsdPoolConfig
-> library RoleAccessControl.checkRole
-> library ConfigProcess.setUsdPoolConfig


### external setVaultConfig
-> library RoleAccessControl.checkRole
-> library ConfigProcess.setVaultConfig


---

## DiamondCutFacet

_File: contracts/facets/DiamondCutFacet.sol_

### external diamondCut
-> library RoleAccessControl.checkRole
-> library LibDiamond.diamondCut


---

## DiamondInit

_File: contracts/router/DiamondInit.sol_

### external init
-> library LibDiamond.diamondStorage


---

## DiamondLoupeFacet

_File: contracts/facets/DiamondLoupeFacet.sol_

### external facetAddress
-> library LibDiamond.diamondStorage


### external facetAddresses
-> library LibDiamond.diamondStorage


### external facetFunctionSelectors
-> library LibDiamond.diamondStorage


### external facets
-> library LibDiamond.diamondStorage


### external supportsInterface
-> library LibDiamond.diamondStorage


---

## FaucetFacet

_File: contracts/facets/FaucetFacet.sol_

### external requestTokens
-> library RoleAccessControl.checkRole
-> library VaultProcess.safeTransferETH


---

## FeeFacet

_File: contracts/facets/FeeFacet.sol_

### external cancelClaimRewards
-> library RoleAccessControl.checkRole
-> library ClaimRewards.get
-> library Errors.ClaimRewardsRequestNotExists
-> library ClaimRewardsProcess.cancelClaimRewards
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external createClaimRewards
-> library ClaimRewardsProcess.createClaimRewards


### external distributeFeeRewards
-> library RoleAccessControl.checkRole
-> library OracleProcess.setOraclePrice
-> library FeeRewardsProcess.distributeFeeRewards
-> library OracleProcess.clearOraclePrice
-> library GasProcess.addLossExecutionFee


### external executeClaimRewards
-> library RoleAccessControl.checkRole
-> library ClaimRewards.get
-> library Errors.ClaimRewardsRequestNotExists
-> library OracleProcess.setOraclePrice
-> library ClaimRewardsProcess.claimRewards
-> library OracleProcess.clearOraclePrice
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external getAccountFeeRewards
-> library FeeQueryProcess.getAccountFeeRewards


### external getAccountUsdFeeReward
-> library FeeQueryProcess.getAccountUsdFeeReward


### external getAccountsFeeRewards
-> library FeeQueryProcess.getAccountFeeRewards
  -> library FeeQueryProcess.getAccountFeeRewards


### external getCumulativeRewardsPerStakeToken
-> library FeeQueryProcess.getCumulativeRewardsPerStakeToken


### external getDaoTokenFee
-> library FeeQueryProcess.getDaoTokenFee


### external getMarketTokenFee
-> library FeeQueryProcess.getMarketTokenFeeAmount


### external getPoolTokenFee
-> library FeeQueryProcess.getPoolTokenFeeAmount


### external getStakingTokenFee
-> library FeeQueryProcess.getStakingTokenFee


---

## LiquidationFacet

_File: contracts/facets/LiquidationFacet.sol_

### external callLiabilityClean
-> library LiabilityClean.getCleanInfo
-> library Errors.CallLiabilityCleanNotExists
-> library AssetsProcess.depositToVault
-> library AssetsProcess.DepositParams
-> library VaultProcess.transferOut
-> library LiabilityClean.removeClean


### external getAllCleanInfos
-> library LiabilityClean.getAllCleanInfo


### external getInsuranceFunds
-> library InsuranceFund.load


### external liquidationAccount
-> library RoleAccessControl.checkRole
-> library OracleProcess.setOraclePrice
-> library LiquidationProcess.liquidationCrossPositions
-> library OracleProcess.clearOraclePrice
-> library GasProcess.addLossExecutionFee


### external liquidationLiability
-> library RoleAccessControl.checkRole
-> library LiquidationProcess.liquidationLiability
-> library GasProcess.addLossExecutionFee


### external liquidationPosition
-> library RoleAccessControl.checkRole
-> library OracleProcess.setOraclePrice
-> library LiquidationProcess.liquidationIsolatePosition
-> library OracleProcess.clearOraclePrice
-> library GasProcess.addLossExecutionFee


---

## LpVault

_File: contracts/vault/LpVault.sol_

### external grantAdmin
_(no internal calls)_


### external revokeAdmin
_(no internal calls)_


### external transferOut
_(no internal calls)_


---

## MarketFacet

_File: contracts/facets/MarketFacet.sol_

### external getAllSymbols
-> library CommonData.getAllSymbols
-> internal _getSingleSymbol
  -> library Symbol.load
  -> library ConfigProcess.getSymbolConfig


### external getLastUuid
-> library UuidCreator.getId


### external getMarketInfo
-> library MarketQueryProcess.getMarketInfo


### external getStakeUsdToken
-> library CommonData.getStakeUsdToken


### external getSymbol
-> internal _getSingleSymbol
  -> library Symbol.load
  -> library ConfigProcess.getSymbolConfig


### external getTradeTokenInfo
-> library MarketQueryProcess.getTradeTokenInfo


---

## MarketManagerFacet

_File: contracts/facets/MarketManagerFacet.sol_

### external createMarket
-> library RoleAccessControl.checkRole
-> library TypeUtils.validBytes32Empty
-> library TypeUtils.validStringEmpty
-> library AddressUtils.validEmpty
-> library MarketFactoryProcess.createMarket


### external createStakeUsdPool
-> library RoleAccessControl.checkRole
-> library TypeUtils.validStringEmpty
-> library MarketFactoryProcess.createStakeUsdPool


---

## OracleFacet

_File: contracts/facets/OracleFacet.sol_

### external getLatestUsdPrice
-> library OracleProcess.getLatestUsdPrice


### external setOraclePrices
-> library OracleProcess.setOraclePrice


---

## OrderFacet

_File: contracts/facets/OrderFacet.sol_

### external batchCreateOrderRequest
-> library Account.loadOrCreate
-> library AppConfig.getChainConfig
-> library Errors.OnlyDecreaseOrderSupported
-> library Errors.MarginModeError
-> library GasProcess.validateExecutionFeeLimit
-> library OrderProcess.createOrderRequest
  -> library AssetsProcess.depositToVault
  -> library AssetsProcess.DepositParams
  -> library Account.loadOrCreate
  -> library OrderProcess.createOrderRequest
-> library AssetsProcess.depositToVault
-> library AssetsProcess.DepositParams


### external cancelOrder
-> library Order.get
-> library Errors.OrderNotExists
-> library RoleAccessControl.hasRole
-> library CancelOrderProcess.cancelOrder
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams
-> library VaultProcess.transferOut
-> library AppConfig.getChainConfig
-> library VaultProcess.withdrawEther


### external createOrderRequest
-> library AssetsProcess.depositToVault
-> library AssetsProcess.DepositParams
-> library Account.loadOrCreate
-> library OrderProcess.createOrderRequest


### external executeOrder
-> library RoleAccessControl.checkRole
-> library Order.get
-> library Errors.OrderNotExists
-> library OracleProcess.setOraclePrice
-> library OrderProcess.executeOrder
-> library OracleProcess.clearOraclePrice
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external getAccountOrders
-> library Account.load
-> library Order.load


---

## PoolFacet

_File: contracts/facets/PoolFacet.sol_

### external getAllPools
-> library LpPoolQueryProcess.getAllPools


### external getPool
-> library LpPoolQueryProcess.getPool


### external getPoolWithOracle
-> library LpPoolQueryProcess.getPool
  -> library LpPoolQueryProcess.getPool


### external getUsdPool
-> library LpPoolQueryProcess.getUsdPool


### external getUsdPoolWithOracle
-> library LpPoolQueryProcess.getUsdPoolWithOracle


---

## PortfolioVault

_File: contracts/vault/PortfolioVault.sol_

### external grantAdmin
_(no internal calls)_


### external revokeAdmin
_(no internal calls)_


### external transferOut
_(no internal calls)_


---

## PositionFacet

_File: contracts/facets/PositionFacet.sol_

### external autoReducePositions
-> library RoleAccessControl.checkRole
-> library UuidCreator.nextId
-> library Position.load
-> library DecreasePositionProcess.DecreasePositionParams
-> library OracleProcess.getLatestUsdUintPrice
-> library GasProcess.addLossExecutionFee


### external cancelUpdateLeverageRequest
-> library RoleAccessControl.checkRole
-> library UpdateLeverage.get
-> library Errors.UpdateLeverageRequestNotExists
-> library PositionMarginProcess.cancelUpdateLeverageRequest
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external cancelUpdatePositionMarginRequest
-> library RoleAccessControl.checkRole
-> library UpdatePositionMargin.get
-> library Errors.UpdatePositionMarginRequestNotExists
-> library PositionMarginProcess.cancelUpdatePositionMarginRequest
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external createUpdateLeverageRequest
-> library ConfigProcess.getSymbolConfig
-> library Symbol.load
-> library Errors.SymbolNotExists
-> library Errors.SymbolStatusInvalid
-> library Errors.LeverageInvalid
-> library Account.load
-> library AssetsProcess.depositToVault
-> library AssetsProcess.DepositParams
-> library AppConfig.getChainConfig
-> internal _validateUpdateLeverageExecutionFee
  -> library AppConfig.getChainConfig
  -> library GasProcess.validateExecutionFeeLimit
  -> library AssetsProcess.depositToVault
  -> library AssetsProcess.DepositParams
-> library PositionMarginProcess.createUpdateLeverageRequest


### external createUpdatePositionMarginRequest
-> library Errors.AmountZeroNotAllowed
-> library Account.load
-> library Errors.PositionNotExists
-> library Position.load
-> library Errors.OnlyIsolateSupported
-> library AssetsProcess.depositToVault
-> library AssetsProcess.DepositParams
-> library AppConfig.getChainConfig
-> internal _validateUpdateMarginExecutionFee
  -> library AppConfig.getChainConfig
  -> library GasProcess.validateExecutionFeeLimit
  -> library AssetsProcess.depositToVault
  -> library AssetsProcess.DepositParams
-> library PositionMarginProcess.createUpdatePositionMarginRequest


### external executeUpdateLeverageRequest
-> library RoleAccessControl.checkRole
-> library UpdateLeverage.get
-> library Errors.UpdateLeverageRequestNotExists
-> library OracleProcess.setOraclePrice
-> library PositionMarginProcess.updatePositionLeverage
-> library OracleProcess.clearOraclePrice
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external executeUpdatePositionMarginRequest
-> library RoleAccessControl.checkRole
-> library UpdatePositionMargin.get
-> library Errors.UpdatePositionMarginRequestNotExists
-> library OracleProcess.setOraclePrice
-> library PositionMarginProcess.updatePositionMargin
-> library OracleProcess.clearOraclePrice
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external getAllPositions
-> library Account.load
-> library Position.load
-> library ChainUtils.currentTimestamp


### external getSinglePosition
-> library Position.load


---

## RebalanceFacet

_File: contracts/facets/RebalanceFacet.sol_

### external autoRebalance
-> library RoleAccessControl.checkRole
-> library OracleProcess.setOraclePrice
-> library RebalanceProcess.autoRebalance
-> library OracleProcess.clearOraclePrice
-> library GasProcess.addLossExecutionFee


---

## ReferralFacet

_File: contracts/facets/ReferralFacet.sol_

### external getAccountReferral
-> library Referral.load


### external isCodeExists
-> library Referral.isCodeExists


---

## RoleAccessControlFacet

_File: contracts/facets/RoleAccessControlFacet.sol_

### external grantRole
-> library RoleAccessControl.grantRole


### external hasRole
-> library RoleAccessControl.hasRole


### external revokeAllRole
-> library RoleAccessControl.revokeAllRole


### external revokeRole
-> library RoleAccessControl.revokeRole


---

## StakeFacet

_File: contracts/facets/StakeFacet.sol_

### external cancelMintStakeToken
-> library RoleAccessControl.checkRole
-> library Mint.get
-> library Errors.MintRequestNotExists
-> library MintProcess.cancelMintStakeToken
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external cancelRedeemStakeToken
-> library RoleAccessControl.checkRole
-> library Redeem.get
-> library Errors.RedeemRequestNotExists
-> library RedeemProcess.cancelRedeemStakeToken
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external createMintStakeTokenRequest
-> library Errors.MintWithAmountZero
-> library Errors.MintWithParamError
-> library CommonData.getStakeUsdToken
-> library UsdPool.isSupportStableToken
-> library Errors.MintTokenInvalid
-> library CommonData.isStakeTokenSupport
-> library LpPool.load
-> library Errors.StakeTokenInvalid
-> library AssetsProcess.depositToVault
-> library AssetsProcess.DepositParams
-> library MintProcess.createMintStakeTokenRequest


### external createRedeemStakeTokenRequest
-> library AddressUtils.validEmpty
-> library Errors.RedeemWithAmountNotEnough
-> library CommonData.getStakeUsdToken
-> library UsdPool.isSupportStableToken
-> library Errors.RedeemTokenInvalid
-> library CommonData.isStakeTokenSupport
-> library LpPool.load
-> library Errors.StakeTokenInvalid
-> library RedeemProcess.validateAndDepositRedeemExecutionFee
-> library RedeemProcess.createRedeemStakeTokenRequest


### external executeMintStakeToken
-> library RoleAccessControl.checkRole
-> library Mint.get
-> library Errors.MintRequestNotExists
-> library OracleProcess.setOraclePrice
-> library MintProcess.executeMintStakeToken
-> library OracleProcess.clearOraclePrice
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


### external executeRedeemStakeToken
-> library RoleAccessControl.checkRole
-> library OracleProcess.setOraclePrice
-> library Redeem.get
-> library Errors.RedeemRequestNotExists
-> library RedeemProcess.executeRedeemStakeToken
-> library OracleProcess.clearOraclePrice
-> library GasProcess.processExecutionFee
-> library GasProcess.PayExecutionFeeParams


---

## StakeToken

_File: contracts/vault/StakeToken.sol_

### external burn
_(no internal calls)_


### public decimals
_(no internal calls)_


### external grantAdmin
_(no internal calls)_


### external mint
_(no internal calls)_


### external revokeAdmin
_(no internal calls)_


### external transferOut
_(no internal calls)_


---

## StakingAccountFacet

_File: contracts/facets/StakingAccountFacet.sol_

### external getAccountPoolBalance
-> library StakingAccount.load


### external getAccountPoolCollateralAmount
-> library StakingAccount.load


### external getAccountUsdPoolAmount
-> library StakingAccount.load


---

## SwapFacet

_File: contracts/facets/SwapFacet.sol_

### external swapPortfolioToPayLiability
-> library RoleAccessControl.checkRole
-> library OracleProcess.setOraclePrice
-> library Account.load
-> internal _swapSingleLiability
  -> library Errors.IgnoreSwapWithAccountLiabilityZero
  -> library CalUtils.tokenToToken
  -> library TokenUtils.decimals
  -> library OracleProcess.getLatestUsdUintPrice
  -> library CalUtils.mulRate
  -> library AppTradeConfig.getTradeConfig
  -> internal _swapUserTokens
    -> library SwapProcess.swap
    -> library AssetsProcess.updateAccountToken
-> library OracleProcess.clearOraclePrice


---

## TradeVault

_File: contracts/vault/TradeVault.sol_

### external grantAdmin
_(no internal calls)_


### external revokeAdmin
_(no internal calls)_


### external transferOut
_(no internal calls)_


---

## Vault

_File: contracts/vault/Vault.sol_

### external grantAdmin
_(no internal calls)_


### external revokeAdmin
_(no internal calls)_


### external transferOut
_(no internal calls)_


---

## VaultFacet

_File: contracts/facets/VaultFacet.sol_

### external getLpVault
-> library AppVaultConfig.getLpVault


### external getLpVaultAddress
-> library AppVaultConfig.getLpVault
  -> library AppVaultConfig.getLpVault


### external getPortfolioVault
-> library AppVaultConfig.getPortfolioVault


### external getPortfolioVaultAddress
-> library AppVaultConfig.getPortfolioVault
  -> library AppVaultConfig.getPortfolioVault


### external getTradeVault
-> library AppVaultConfig.getTradeVault


### external getTradeVaultAddress
-> library AppVaultConfig.getTradeVault
  -> library AppVaultConfig.getTradeVault

