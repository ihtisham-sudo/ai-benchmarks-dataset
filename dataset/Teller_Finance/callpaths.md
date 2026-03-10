# Callpaths — Teller_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AaveFacet

_File: contracts/escrow/dapps/AaveFacet.sol_

### public aaveDeposit
-> library LibEscrow.e
-> library LibDapps.getAaveLendingPool
-> library LibDapps.getAToken
-> library LibEscrow.tokenUpdated


### public aaveWithdraw
-> library LibEscrow.e
-> library LibDapps.getAToken
-> library LibDapps.getAaveLendingPool
-> library LibDapps.s
-> library LibEscrow.tokenUpdated


### public aaveWithdrawAll
-> library LibEscrow.e
-> library LibDapps.getAToken
-> library LibDapps.getAaveLendingPool
-> library LibEscrow.tokenUpdated


---

## AavePricer

_File: contracts/price-aggregator/pricers/AavePricer.sol_

### external getBalanceOfUnderlying
_(no internal calls)_


### public getRateFor
_(no internal calls)_


### public getUnderlying
_(no internal calls)_


### external getValueOf
_(no internal calls)_


---

## AssetSettingsDataFacet

_File: contracts/settings/asset/AssetSettingsDataFacet.sol_

### external getAssetAToken
-> library AssetATokenLib.get


### external getAssetCToken
-> library AssetCTokenLib.get


### external getAssetMaxDebtRatio
-> library MaxDebtRatioLib.get


### external getAssetMaxLoanAmount
-> library MaxLoanAmountLib.get


### external getAssetPPool
-> library AssetPPoolLib.get


### external getAssetPPoolTicket
-> library PoolTogetherLib.getTicketAddress


### external getAssetYVault
-> library AssetYVaultLib.get


---

## AssetSettingsFacet

_File: contracts/settings/asset/AssetSettingsFacet.sol_

### external createAssetSetting
-> library CacheLib.initialize
-> private s
  -> library AppStorageLib.store
-> library CacheLib.update


### external isAssetSettingInitialized
-> library CacheLib.exists
-> private s
  -> library AppStorageLib.store


### external updateAssetSetting
-> library CacheLib.exists
-> private s
  -> library AppStorageLib.store
-> library CacheLib.update


---

## ChainlinkPricer

_File: contracts/price-aggregator/pricers/ChainlinkPricer.sol_

### public getEthAggregator
-> internal _getTokenSymbol
-> library ENS.resolve
-> library ENS.subnode


### external getEthPrice
-> public getEthAggregator
  -> internal _getTokenSymbol
  -> library ENS.resolve
  -> library ENS.subnode


---

## CollateralEscrow_V1

_File: contracts/market/collateral/CollateralEscrow_V1.sol_

### external deposit
_(no internal calls)_


### external init
_(no internal calls)_


### external loanSupply
_(no internal calls)_


### external totalSupply
_(no internal calls)_


### external withdraw
_(no internal calls)_


---

## CollateralFacet

_File: contracts/market/CollateralFacet.sol_

### external addCollateralTokens
-> library MarketStorageLib.store
-> library LibCollateral.createEscrow


### external depositCollateral
-> library LibLoans.loan
-> library LibCollateral.deposit


### external getCollateralTokens
_(no internal calls)_


### external getLoanCollateral
-> library LibCollateral.e


### external withdrawCollateral
-> library LibLoans.loan
-> library LibLoans.getCollateralNeededInfo
-> library LibCollateral.e
-> library LibCollateral.withdraw


---

## CompoundClaimCompFacet

_File: contracts/escrow/dapps/CompoundClaimComp.sol_

### public compoundCalculateComp
-> library LibEscrow.e


### public compoundClaimComp
-> library LibEscrow.e


---

## CompoundFacet

_File: contracts/escrow/dapps/CompoundFacet.sol_

### public compoundLend
-> library AssetCTokenLib.get
-> library AppStorageLib.store
-> library LibEscrow.e
-> library LibEscrow.tokenUpdated


### public compoundRedeem
-> library AssetCTokenLib.get
-> private __compoundRedeem
  -> library LibEscrow.e
  -> library AppStorageLib.store
  -> library LibEscrow.tokenUpdated


### public compoundRedeemAll
-> library AssetCTokenLib.get
-> private __compoundRedeem
  -> library LibEscrow.e
  -> library AppStorageLib.store
  -> library LibEscrow.tokenUpdated
-> library LibEscrow.e


---

## CompoundPricer

_File: contracts/price-aggregator/pricers/CompoundPricer.sol_

### external getBalanceOfUnderlying
_(no internal calls)_


### public getRateFor
_(no internal calls)_


### public getUnderlying
_(no internal calls)_


### external getValueOf
-> public getRateFor


---

## CreateLoanConsensusFacet

_File: contracts/market/CreateLoanConsensusFacet.sol_

### external takeOutLoan
-> library MarketStorageLib.store
-> library LibConsensus.processLoanTerms
-> library LibCreateLoan.initNewLoan
-> library LibCollateral.deposit
-> library LibLoans.getCollateralNeeded
-> library LibCollateral.e
-> library LibLoans.canGoToEOAWithCollateralRatio
-> library LibCreateLoan.createEscrow
-> library LibCreateLoan.fundLoan
-> library LibCreateLoan.LoanTakenOut


---

## CreateLoanWithNFTFacet

_File: contracts/market/CreateLoanWithNFTFacet.sol_

### external takeOutLoanWithNFTs
-> library LibCreateLoan.initNewLoan
-> library PlatformSettingsLib.getNFTInterestRate
-> internal _takeOutLoanProcessTokenDataVersion
  -> internal _takeOutLoanProcessNFTs
    -> library NFTLib.applyToLoanV2
-> library AppStorageLib.store
-> library LibCreateLoan.fundLoan
-> library LibCreateLoan.createEscrow
-> library LibCreateLoan.LoanTakenOut


---

## DiamondCutFacet

_File: contracts/shared/facets/DiamondCutFacet.sol_

### external diamondCut
-> library LibDiamond.enforceIsContractOwner
-> library LibDiamond.diamondCut


---

## DiamondLoupeFacet

_File: contracts/shared/facets/DiamondLoupeFacet.sol_

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

## EscrowClaimTokens

_File: contracts/escrow/EscrowClaimTokens.sol_

### external claimTokens
-> library LibLoans.loan
-> internal __claimEscrowTokens
  -> private __claimToken
    -> library LibEscrow.balanceOf
    -> library LibEscrow.e
    -> library LibLoans.loan
  -> library LibLoans.loan
  -> library MarketStorageLib.store


---

## ITToken

_File: contracts/lending/ttoken/ITToken.sol_

### external grantRole
-> library RolesLib.grantRole


### external hasRole
-> library RolesLib.hasRole


### external renounceRole
-> library RolesLib.revokeRole
  -> library RolesLib.revokeRole


### external revokeRole
-> library RolesLib.revokeRole


---

## ITToken_V3

_File: contracts/lending/ttoken/ITToken_V3.sol_

### external grantRole
-> library RolesLib.grantRole


### external hasRole
-> library RolesLib.hasRole


### external renounceRole
-> library RolesLib.revokeRole
  -> library RolesLib.revokeRole


### external revokeRole
-> library RolesLib.revokeRole


---

## ITellerDiamond

_File: contracts/shared/interfaces/ITellerDiamond.sol_

### public aaveDeposit
-> library LibEscrow.e
-> library LibDapps.getAaveLendingPool
-> library LibDapps.getAToken
-> library LibEscrow.tokenUpdated


### public aaveWithdraw
-> library LibEscrow.e
-> library LibDapps.getAToken
-> library LibDapps.getAaveLendingPool
-> library LibDapps.s
  -> library AppStorageLib.store
-> library LibEscrow.tokenUpdated


### public aaveWithdrawAll
-> library LibEscrow.e
-> library LibDapps.getAToken
-> library LibDapps.getAaveLendingPool
-> library LibEscrow.tokenUpdated


### external addCollateralTokens
-> library MarketStorageLib.store
-> library LibCollateral.createEscrow


### external addSigners
-> internal _addSigner
  -> library MarketStorageLib.store


### external bridgeNFTsV1
-> library NFTLib.s
  -> library AppStorageLib.store
-> library NFTLib.unstake
-> internal __depositFor


### external bridgeNFTsV2
-> library NFTLib.s
  -> library AppStorageLib.store
-> library NFTLib.unstakeV2
-> internal __depositFor


### public compoundCalculateComp
-> library LibEscrow.e


### public compoundClaimComp
-> library LibEscrow.e


### public compoundLend
-> library AssetCTokenLib.get
-> library AppStorageLib.store
-> library LibEscrow.e
-> library LibEscrow.tokenUpdated


### public compoundRedeem
-> library AssetCTokenLib.get
-> private __compoundRedeem
  -> library LibEscrow.e
  -> library AppStorageLib.store
  -> library LibEscrow.tokenUpdated


### public compoundRedeemAll
-> library AssetCTokenLib.get
-> private __compoundRedeem
  -> library LibEscrow.e
  -> library AppStorageLib.store
  -> library LibEscrow.tokenUpdated
-> library LibEscrow.e


### external createAssetSetting
-> library CacheLib.initialize
-> private s
  -> library AppStorageLib.store
-> library CacheLib.update


### external createPlatformSetting
-> library PlatformSettingsLib.s
  -> library AppStorageLib.store


### external depositCollateral
-> library LibLoans.loan
-> library LibCollateral.deposit


### external escrowRepay
-> library LibEscrow.balanceOf
-> library LibLoans.loan
-> library LibLoans.getTotalOwed
  -> library LibLoans.getTotalOwed
-> library SafeERC20.safeTransferFrom
-> library LibEscrow.e
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> library SafeERC20.safeTransferFrom
  -> internal _liquidateNFT
    -> library NFTLib.s
      -> library AppStorageLib.store
    -> library AppStorageLib.store
  -> library LibCollateral.withdrawAll
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinkedV2
    -> library LibLoans.loan


### external getAssetAToken
-> library AssetATokenLib.get


### external getAssetCToken
-> library AssetCTokenLib.get


### external getAssetMaxDebtRatio
-> library MaxDebtRatioLib.get


### external getAssetMaxLoanAmount
-> library MaxLoanAmountLib.get


### external getAssetPPool
-> library AssetPPoolLib.get


### external getAssetPPoolTicket
-> library PoolTogetherLib.getTicketAddress


### external getAssetYVault
-> library AssetYVaultLib.get


### external getBorrowerLoans
-> library LibLoans.s
  -> library AppStorageLib.store


### external getCollateralNeededInfo
-> library LibLoans.getCollateralNeededInfo


### external getCollateralTokens
_(no internal calls)_


### external getDebtOwed
-> library LibLoans.debt


### external getEscrowTokens
_(no internal calls)_


### external getInterestOwedFor
-> library LibLoans.getInterestOwedFor


### external getLiquidationReward
-> library RepayLib.getLiquidationReward
-> library LibCollateral.e
-> library AppStorageLib.store
-> library LibLoans.loan


### external getLoan
-> library LibLoans.s
  -> library AppStorageLib.store


### external getLoanCollateral
-> library LibCollateral.e


### external getLoanEscrow
-> library LibLoans.s
  -> library AppStorageLib.store


### external getLoanEscrowValue
-> library LibEscrow.calculateTotalValue


### external getLoanNFTsV2
-> library NFTLib.s
  -> library AppStorageLib.store


### external getLoanTerms
-> library LibLoans.terms


### external getNFTLiquidationController
-> library AppStorageLib.store


### external getPlatformSetting
-> library PlatformSettingsLib.s
  -> library AppStorageLib.store


### public getStakedNFTsV2
-> library NFTLib.s
  -> library AppStorageLib.store


### external getTTokenFor
-> library LendingLib.tToken


### external getTotalOwed
-> library LibLoans.getTotalOwed


### external init
-> library AppStorageLib.store
-> library RolesLib.grantRole


### external init2
-> library AppStorageLib.store


### external initLendingPool
-> library LendingLib.tToken
-> library AppStorageLib.store
-> library LendingLib.s
  -> library AppStorageLib.store


### external initNFTBridge
_(no internal calls)_


### external isAssetSettingInitialized
-> library CacheLib.exists
-> private s
  -> library AppStorageLib.store


### public isPaused
-> library AppStorageLib.store


### public isSigner
-> library MarketStorageLib.store


### external liquidateLoan
-> library LibLoans.loan
-> library LibCollateral.e
-> library RepayLib.isLiquidable
-> library LibLoans.debt
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> library SafeERC20.safeTransferFrom
  -> internal _liquidateNFT
    -> library NFTLib.s
      -> library AppStorageLib.store
    -> library AppStorageLib.store
  -> library LibCollateral.withdrawAll
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinkedV2
    -> library LibLoans.loan
-> library RepayLib.payOutLiquidator


### external onERC1155BatchReceived
-> private __stakeNFTV2
  -> library NFTLib.stakeV2


### external onERC1155Received
-> private __stakeNFTV2
  -> library NFTLib.stakeV2


### external pause
-> public isPaused
  -> library AppStorageLib.store
-> library AppStorageLib.store


### external removeSigners
-> internal _removeSigner
  -> library MarketStorageLib.store


### external repayLoan
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> library SafeERC20.safeTransferFrom
  -> internal _liquidateNFT
    -> library NFTLib.s
      -> library AppStorageLib.store
    -> library AppStorageLib.store
  -> library LibCollateral.withdrawAll
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinkedV2
    -> library LibLoans.loan


### external setNFTLiquidationController
-> library AppStorageLib.store


### external sushiswapSwap
-> library LibEscrow.e
-> library LibEscrow.tokenUpdated


### external takeOutLoan
-> library MarketStorageLib.store
-> library LibConsensus.processLoanTerms
-> library LibCreateLoan.initNewLoan
-> library LibCollateral.deposit
-> library LibLoans.getCollateralNeeded
-> library LibCollateral.e
-> library LibLoans.canGoToEOAWithCollateralRatio
-> library LibCreateLoan.createEscrow
-> library LibCreateLoan.fundLoan
-> library LibCreateLoan.LoanTakenOut


### external takeOutLoanWithNFTs
-> library LibCreateLoan.initNewLoan
-> library PlatformSettingsLib.getNFTInterestRate
-> internal _takeOutLoanProcessTokenDataVersion
  -> internal _takeOutLoanProcessNFTs
    -> library NFTLib.applyToLoanV2
-> library AppStorageLib.store
-> library LibCreateLoan.fundLoan
-> library LibCreateLoan.createEscrow
-> library LibCreateLoan.LoanTakenOut


### external uniswapSwap
-> library LibEscrow.e
-> library LibEscrow.tokenUpdated


### external unstakeNFTsV2
-> library NFTLib.unstakeV2


### external updateAssetSetting
-> library CacheLib.exists
-> private s
  -> library AppStorageLib.store
-> library CacheLib.update


### external updatePlatformSetting
-> library PlatformSettingsLib.s
  -> library AppStorageLib.store


### external updatePlatformSettingBoundaries
-> library PlatformSettingsLib.s
  -> library AppStorageLib.store


### external withdrawCollateral
-> library LibLoans.loan
-> library LibLoans.getCollateralNeededInfo
  -> library LibLoans.getCollateralNeededInfo
-> library LibCollateral.e
-> library LibCollateral.withdraw


### public yearnDeposit
-> library AssetYVaultLib.get
-> library LibDapps.s
  -> library AppStorageLib.store
-> library LibEscrow.tokenUpdated


### public yearnWithdraw
-> library AssetYVaultLib.get
-> library LibDapps.s
  -> library AppStorageLib.store
-> library LibEscrow.tokenUpdated


### public yearnWithdrawAll
-> library AssetYVaultLib.get
-> library LibDapps.s
  -> library AppStorageLib.store
-> library LibEscrow.tokenUpdated


---

## InitializeableBeaconProxy

_File: contracts/shared/proxy/beacon/InitializeableBeaconProxy.sol_

### external initialize
-> internal _beacon
-> internal _setBeacon
  -> internal _implementation
    -> internal _beacon


---

## LendingFacet

_File: contracts/lending/LendingFacet.sol_

### external getTTokenFor
-> library LendingLib.tToken


### external initLendingPool
-> library LendingLib.tToken
-> library AppStorageLib.store
-> library LendingLib.s


---

## LoanDataFacet

_File: contracts/market/LoanDataFacet.sol_

### external getBorrowerLoans
-> library LibLoans.s


### external getCollateralNeededInfo
-> library LibLoans.getCollateralNeededInfo


### external getDebtOwed
-> library LibLoans.debt


### external getEscrowTokens
_(no internal calls)_


### external getInterestOwedFor
-> library LibLoans.getInterestOwedFor


### external getLoan
-> library LibLoans.s


### external getLoanEscrow
-> library LibLoans.s


### external getLoanEscrowValue
-> library LibEscrow.calculateTotalValue


### external getLoanTerms
-> library LibLoans.terms


### external getTotalOwed
-> library LibLoans.getTotalOwed


---

## LoansEscrow_V1

_File: contracts/escrow/escrow/LoansEscrow_V1.sol_

### external callDapp
_(no internal calls)_


### external callDappWithValue
_(no internal calls)_


### external claimToken
_(no internal calls)_


### external init
_(no internal calls)_


### external setTokenAllowance
_(no internal calls)_


---

## MainnetCreateLoanWithNFTFacet

_File: contracts/market/mainnet/MainnetCreateLoanWithNFTFacet.sol_

### external takeOutLoanWithNFTs
-> library LibCreateLoan.initNewLoan
-> library PlatformSettingsLib.getNFTInterestRate
-> internal _takeOutLoanProcessTokenDataVersion
  -> internal _takeOutLoanProcessNFTs
    -> library NFTLib.applyToLoan
    -> library NFTLib.s
-> library AppStorageLib.store
-> library LibCreateLoan.fundLoan
-> library LibCreateLoan.createEscrow
-> library LibCreateLoan.LoanTakenOut


---

## MainnetNFTFacet

_File: contracts/nft/mainnet/MainnetNFTFacet.sol_

### external getLoanNFTs
-> library NFTLib.s


### external getLoanNFTsV2
-> library NFTLib.s


### public getStakedNFTs
-> library NFTLib.s


### public getStakedNFTsV2
-> library NFTLib.s


### external onERC1155BatchReceived
-> private __stakeNFTV2
  -> library NFTLib.stakeV2


### external onERC1155Received
-> private __stakeNFTV2
  -> library NFTLib.stakeV2


### external stakeNFTs
-> library NFTLib.stakeV2


### external unstakeNFTs
-> library NFTLib.unstake


### external unstakeNFTsV2
-> library NFTLib.unstakeV2


---

## MainnetNFTFacetMock

_File: contracts/nft/mainnet/MainnetNFTFacetMock.sol_

### external getLoanNFTs
-> library NFTLib.s


### public getStakedNFTs
-> library NFTLib.s


### external mockStakeNFTsV1
-> library NFTLib.stake


### external stakeNFTs
-> library NFTLib.stakeV2


### external unstakeNFTs
-> library NFTLib.unstake


---

## MainnetRepayFacet

_File: contracts/market/mainnet/MainnetRepayFacet.sol_

### external escrowRepay
-> library LibEscrow.balanceOf
-> library LibLoans.loan
-> library LibLoans.getTotalOwed
-> library LibEscrow.e
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> internal _liquidateNFT
    -> library NFTLib.liquidateNFT
  -> library LibCollateral.withdrawAll
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinked
    -> library LibLoans.loan


### external getLiquidationReward
-> library RepayLib.getLiquidationReward
-> library LibCollateral.e
-> library AppStorageLib.store
-> library LibLoans.loan


### external liquidateLoan
-> library LibLoans.loan
-> library LibCollateral.e
-> library RepayLib.isLiquidable
-> library LibLoans.debt
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> internal _liquidateNFT
    -> library NFTLib.liquidateNFT
  -> library LibCollateral.withdrawAll
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinked
    -> library LibLoans.loan
-> library RepayLib.payOutLiquidator


### external repayLoan
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> internal _liquidateNFT
    -> library NFTLib.liquidateNFT
  -> library LibCollateral.withdrawAll
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinked
    -> library LibLoans.loan


---

## MainnetTellerNFT

_File: contracts/nft/mainnet/MainnetTellerNFT.sol_

### external contractURI
_(no internal calls)_


### public convertV1TokenId
-> internal _exists


### external createTiers
-> internal _createTier
  -> internal _mergeTokenId


### external getOwnedTokens
_(no internal calls)_


### external getTokenTierId
-> internal _splitTokenId


### public initialize
-> internal __TellerNFT_V2_init_unchained


### external mint
-> internal _mergeTokenId
-> internal _mint
  -> private _addOwnedToken


### external onERC721Received
-> public convertV1TokenId
  -> internal _exists
-> internal _mint
  -> private _addOwnedToken


### public setContractURIHash
_(no internal calls)_


### external setURI
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public tokenBaseLoanSize
-> internal _splitTokenId


### public tokenContributionAsset
-> internal _splitTokenId


### public tokenContributionMultiplier
-> internal _splitTokenId


### public tokenContributionSize
-> internal _splitTokenId


### public uri
_(no internal calls)_


---

## NFTFacet

_File: contracts/nft/NFTFacet.sol_

### external getLoanNFTsV2
-> library NFTLib.s


### public getStakedNFTsV2
-> library NFTLib.s


### external onERC1155BatchReceived
-> private __stakeNFTV2
  -> library NFTLib.stakeV2


### external onERC1155Received
-> private __stakeNFTV2
  -> library NFTLib.stakeV2


### external unstakeNFTsV2
-> library NFTLib.unstakeV2


---

## NFTMainnetBridgingToPolygonFacet

_File: contracts/nft/mainnet/NFTMainnetBridgingToPolygonFacet.sol_

### external bridgeNFTsV1
-> library NFTLib.s
-> library NFTLib.unstake
-> internal __depositFor


### external bridgeNFTsV2
-> library NFTLib.s
-> library NFTLib.unstakeV2
-> internal __depositFor


### external initNFTBridge
_(no internal calls)_


---

## NFTMigrator

_File: contracts/nft/mainnet/NFTMigrator.sol_

### external migrateV1toV2
_(no internal calls)_


---

## OwnershipFacet

_File: contracts/shared/facets/OwnershipFacet.sol_

### external owner
-> library LibDiamond.contractOwner


### external transferOwnership
-> library LibDiamond.enforceIsContractOwner
-> library LibDiamond.setContractOwner


---

## PausableFacet

_File: contracts/settings/pausable/PausableFacet.sol_

### public isPaused
-> library AppStorageLib.store


### external pause
-> public isPaused
  -> library AppStorageLib.store
-> library AppStorageLib.store


---

## PlatformSettingsFacet

_File: contracts/settings/platform/PlatformSettingsFacet.sol_

### external createPlatformSetting
-> library PlatformSettingsLib.s


### external getPlatformSetting
-> library PlatformSettingsLib.s


### external updatePlatformSetting
-> library PlatformSettingsLib.s


### external updatePlatformSettingBoundaries
-> library PlatformSettingsLib.s


---

## PolyTellerNFT

_File: contracts/nft/polygon/PolyTellerNFT.sol_

### external contractURI
_(no internal calls)_


### external createTiers
-> internal _createTier
  -> internal _mergeTokenId


### external deposit
-> internal _mintBatch
  -> private _addOwnedToken


### external getOwnedTokens
_(no internal calls)_


### external getTokenTierId
-> internal _splitTokenId


### public initialize
-> internal __TellerNFT_V2_init_unchained


### public setContractURIHash
_(no internal calls)_


### external setURI
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public tokenBaseLoanSize
-> internal _splitTokenId


### public tokenContributionAsset
-> internal _splitTokenId


### public tokenContributionMultiplier
-> internal _splitTokenId


### public tokenContributionSize
-> internal _splitTokenId


### public uri
_(no internal calls)_


### external withdraw
-> internal _burn
  -> private _removeOwnedTokenCheck


### external withdrawBatch
-> internal _burnBatch
  -> private _removeOwnedTokenCheck


---

## PolyTellerNFTMock

_File: contracts/nft/polygon/PolyTellerNFTMock.sol_

### public addDepositor
_(no internal calls)_


### external deposit
_(no internal calls)_


### external mint
_(no internal calls)_


### external withdraw
_(no internal calls)_


### external withdrawBatch
_(no internal calls)_


---

## PolygonChainlinkPricer

_File: contracts/price-aggregator/pricers/PolygonChainlinkPricer.sol_

### public getEthAggregator
-> internal _getTokenSymbol
-> library ENS.resolve
-> library ENS.subnode


### external getEthPrice
-> public getEthAggregator
  -> internal _getTokenSymbol
  -> library ENS.resolve
  -> library ENS.subnode


---

## PoolTogetherFacet

_File: contracts/escrow/dapps/PoolTogetherFacet.sol_

### public poolTogetherDepositTicket
-> library LibEscrow.balanceOf
-> library AssetPPoolLib.get
-> library PoolTogetherLib.getTicketAddress
-> library LibEscrow.e
-> library LibDapps.s
-> library LibEscrow.tokenUpdated


### public poolTogetherWithdraw
-> library AssetPPoolLib.get
-> library PoolTogetherLib.getTicketAddress
-> library LibEscrow.balanceOf
-> library LibEscrow.e
-> library LibDapps.s
-> library LibEscrow.tokenUpdated


### public poolTogetherWithdrawAll
-> library AssetPPoolLib.get
-> library PoolTogetherLib.getTicketAddress
-> library LibEscrow.balanceOf
-> library LibEscrow.e
-> library LibDapps.s
-> library LibEscrow.tokenUpdated


---

## PoolTogetherPricer

_File: contracts/price-aggregator/pricers/PoolTogetherPricer.sol_

### external getBalanceOfUnderlying
-> private _getPrizePool


### public getRateFor
_(no internal calls)_


### public getUnderlying
-> private _getPrizePool


### external getValueOf
_(no internal calls)_


---

## PriceAggregator

_File: contracts/price-aggregator/PriceAggregator.sol_

### external getBalanceOfFor
-> internal _valueFor
  -> internal _oneToken
    -> internal _decimalsFor
-> private _priceFor
  -> internal _scale
  -> internal _inverseRate
  -> internal _decimalsFor
  -> internal _mergeRates
    -> internal _decimalsFor
  -> private _priceFor
  -> internal _valueFor
    -> internal _oneToken
      -> internal _decimalsFor


### external getPriceFor
-> private _priceFor
  -> internal _scale
  -> internal _inverseRate
  -> internal _decimalsFor
  -> internal _mergeRates
    -> internal _decimalsFor
  -> private _priceFor
  -> internal _valueFor
    -> internal _oneToken
      -> internal _decimalsFor


### external getValueFor
-> internal _valueFor
  -> internal _oneToken
    -> internal _decimalsFor
-> private _priceFor
  -> internal _scale
  -> internal _inverseRate
  -> internal _decimalsFor
  -> internal _mergeRates
    -> internal _decimalsFor
  -> private _priceFor
  -> internal _valueFor
    -> internal _oneToken
      -> internal _decimalsFor


### external grantRole
-> library RolesLib.grantRole


### external hasRole
-> library RolesLib.hasRole


### external initialize
-> library RolesLib.grantRole
  -> library RolesLib.grantRole
-> public setChainlinkPricer


### external renounceRole
-> library RolesLib.revokeRole
  -> library RolesLib.revokeRole


### external revokeRole
-> library RolesLib.revokeRole


### public setAssetPricer
_(no internal calls)_


### external setAssetPricers
-> public setAssetPricer


### public setChainlinkPricer
_(no internal calls)_


---

## RepayFacet

_File: contracts/market/RepayFacet.sol_

### external claimTokens
-> library LibLoans.loan
-> internal __claimEscrowTokens
  -> private __claimToken
    -> library LibEscrow.balanceOf
    -> library LibEscrow.e
    -> library LibLoans.loan
  -> library LibLoans.loan
  -> library MarketStorageLib.store


### external escrowRepay
-> library LibEscrow.balanceOf
-> library LibLoans.loan
-> library LibLoans.getTotalOwed
-> library LibEscrow.e
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> internal _liquidateNFT
    -> library NFTLib.s
    -> library AppStorageLib.store
  -> library LibCollateral.withdrawAll
  -> internal __claimEscrowTokens
    -> private __claimToken
      -> library LibEscrow.balanceOf
      -> library LibEscrow.e
      -> library LibLoans.loan
    -> library LibLoans.loan
    -> library MarketStorageLib.store
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinkedV2
    -> library LibLoans.loan


### external getLiquidationReward
-> library RepayLib.getLiquidationReward
-> library LibCollateral.e
-> library AppStorageLib.store
-> library LibLoans.loan


### external liquidateLoan
-> library LibLoans.loan
-> library LibCollateral.e
-> library RepayLib.isLiquidable
-> library LibLoans.debt
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> internal _liquidateNFT
    -> library NFTLib.s
    -> library AppStorageLib.store
  -> library LibCollateral.withdrawAll
  -> internal __claimEscrowTokens
    -> private __claimToken
      -> library LibEscrow.balanceOf
      -> library LibEscrow.e
      -> library LibLoans.loan
    -> library LibLoans.loan
    -> library MarketStorageLib.store
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinkedV2
    -> library LibLoans.loan
-> library RepayLib.payOutLiquidator


### external repayLoan
-> private __repayLoan
  -> library LibLoans.debt
  -> library MarketStorageLib.store
  -> library LibLoans.loan
  -> library LibEscrow.e
  -> internal _liquidateNFT
    -> library NFTLib.s
    -> library AppStorageLib.store
  -> library LibCollateral.withdrawAll
  -> internal __claimEscrowTokens
    -> private __claimToken
      -> library LibEscrow.balanceOf
      -> library LibEscrow.e
      -> library LibLoans.loan
    -> library LibLoans.loan
    -> library MarketStorageLib.store
  -> internal _restakeNFTForRepayment
    -> library NFTLib.restakeLinkedV2
    -> library LibLoans.loan


---

## RolesFacet

_File: contracts/contexts2/access-control/roles/RolesFacet.sol_

### external grantRole
-> library RolesLib.grantRole


### external hasRole
-> library RolesLib.hasRole


### external renounceRole
-> library RolesLib.revokeRole
  -> library RolesLib.revokeRole


### external revokeRole
-> library RolesLib.revokeRole


---

## SettingsFacet

_File: contracts/settings/SettingsFacet.sol_

### external getNFTLiquidationController
-> library AppStorageLib.store


### external init
-> library AppStorageLib.store
-> library RolesLib.grantRole


### external init2
-> library AppStorageLib.store


### external setNFTLiquidationController
-> library AppStorageLib.store


---

## SignersFacet

_File: contracts/market/SignersFacet.sol_

### external addSigners
-> internal _addSigner
  -> library MarketStorageLib.store


### public isSigner
-> library MarketStorageLib.store


### external removeSigners
-> internal _removeSigner
  -> library MarketStorageLib.store


---

## SushiswapFacet

_File: contracts/escrow/dapps/swappers/SushiswapFacet.sol_

### external sushiswapSwap
-> internal __isValidPath
  -> library AppStorageLib.store
-> library LibEscrow.e
-> library LibEscrow.tokenUpdated


---

## TTokenAaveStrategy_1

_File: contracts/lending/ttoken/strategies/aave/TTokenAaveStrategy_1.sol_

### external init
_(no internal calls)_


### public rebalance
-> internal _getBalanceInfo
  -> library NumbersLib.ratioOf
-> library NumbersLib.percent
-> library LibDapps.getAaveLendingPool
-> internal _withdraw
  -> library NumbersLib.percent
  -> library LibDapps.getAaveLendingPool


### public supportsInterface
_(no internal calls)_


### external totalUnderlyingSupply
_(no internal calls)_


### external withdraw
-> internal _getBalanceInfo
  -> library NumbersLib.ratioOf
-> internal _withdraw
  -> library NumbersLib.percent
  -> library LibDapps.getAaveLendingPool


---

## TTokenCompoundStrategy_1

_File: contracts/lending/ttoken/strategies/compound/TTokenCompoundStrategy_1.sol_

### external init
-> library LibMeta.msgSender


### public rebalance
-> internal _getBalanceInfo
  -> library NumbersLib.ratioOf
-> library NumbersLib.percent
-> internal _withdraw
  -> library NumbersLib.percent


### public supportsInterface
_(no internal calls)_


### external totalUnderlyingSupply
_(no internal calls)_


### external withdraw
-> internal _getBalanceInfo
  -> library NumbersLib.ratioOf
-> internal _withdraw
  -> library NumbersLib.percent


---

## TTokenStrategy

_File: contracts/lending/ttoken/strategies/TTokenStrategy.sol_

### public supportsInterface
_(no internal calls)_


---

## TToken_V1

_File: contracts/lending/ttoken/TToken_V1.sol_

### public balanceOfUnderlying
-> internal _valueInUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy


### public currentTVL
-> public totalUnderlyingSupply
  -> internal _delegateStrategy


### external debtRatioFor
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> library NumbersLib.ratioOf


### public decimals
_(no internal calls)_


### public exchangeRate
-> public currentTVL
  -> public totalUnderlyingSupply
    -> internal _delegateStrategy


### external fundLoan
-> internal _delegateStrategy


### external getMarketState
-> public totalUnderlyingSupply
  -> internal _delegateStrategy


### external getStrategy
_(no internal calls)_


### external initialize
-> library RolesLib.grantRole


### external mint
-> internal _valueOfUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy


### public rebalance
-> internal _delegateStrategy


### external redeem
-> internal _valueInUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> internal _redeem
  -> internal _delegateStrategy


### external redeemUnderlying
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy
-> internal _valueOfUnderlying
-> internal _redeem
  -> internal _delegateStrategy


### external repayLoan
_(no internal calls)_


### public restrict
_(no internal calls)_


### external setStrategy
-> internal _delegateStrategy


### public totalUnderlyingSupply
-> internal _delegateStrategy


### public underlying
_(no internal calls)_


---

## TToken_V2

_File: contracts/lending/ttoken/TToken_V2.sol_

### public balanceOfUnderlying
-> internal _valueInUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy


### public currentTVL
-> public totalUnderlyingSupply
  -> internal _delegateStrategy


### external debtRatioFor
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> library NumbersLib.ratioOf


### public decimals
_(no internal calls)_


### public exchangeRate
-> public currentTVL
  -> public totalUnderlyingSupply
    -> internal _delegateStrategy


### external fundLoan
-> internal _delegateStrategy


### external getMarketState
-> public totalUnderlyingSupply
  -> internal _delegateStrategy


### external getStrategy
_(no internal calls)_


### external initialize
-> library RolesLib.grantRole


### external mint
-> internal _valueOfUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy


### public rebalance
-> internal _delegateStrategy


### external redeem
-> internal _valueInUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> internal _redeem
  -> internal _delegateStrategy


### external redeemUnderlying
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy
-> internal _valueOfUnderlying
-> internal _redeem
  -> internal _delegateStrategy


### external repayLoan
_(no internal calls)_


### public restrict
_(no internal calls)_


### external setStrategy
-> internal _delegateStrategy


### public totalUnderlyingSupply
-> internal _delegateStrategy


### public underlying
_(no internal calls)_


---

## TToken_V2_Alpha

_File: contracts/lending/ttoken/TToken_V2_Alpha.sol_

### external fundLoan
_(no internal calls)_


---

## TToken_V3

_File: contracts/lending/ttoken/TToken_V3.sol_

### public balanceOfUnderlying
-> internal _valueInUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy


### public currentTVL
-> public totalUnderlyingSupply
  -> internal _delegateStrategy


### external debtRatioFor
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> library NumbersLib.ratioOf


### public decimals
_(no internal calls)_


### public exchangeRate
-> public currentTVL
  -> public totalUnderlyingSupply
    -> internal _delegateStrategy


### external fundLoan
-> internal _delegateStrategy


### external getMarketState
-> public totalUnderlyingSupply
  -> internal _delegateStrategy


### external getStrategy
_(no internal calls)_


### external initialize
-> library RolesLib.grantRole


### external mint
-> internal _valueOfUnderlying


### public rebalance
-> internal _delegateStrategy


### external redeem
-> internal _valueInUnderlying
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> internal _redeem
  -> internal _delegateStrategy


### external redeemUnderlying
-> public totalUnderlyingSupply
  -> internal _delegateStrategy
-> public exchangeRate
  -> public currentTVL
    -> public totalUnderlyingSupply
      -> internal _delegateStrategy
-> internal _valueOfUnderlying
-> internal _redeem
  -> internal _delegateStrategy


### external repayLoan
_(no internal calls)_


### external setStrategy
-> internal _delegateStrategy


### public totalUnderlyingSupply
-> internal _delegateStrategy


### public underlying
_(no internal calls)_


---

## TellerNFT

_File: contracts/nft/TellerNFT.sol_

### public addMinter
_(no internal calls)_


### external addTier
_(no internal calls)_


### external contractURI
_(no internal calls)_


### external getOwnedTokens
_(no internal calls)_


### external getTier
_(no internal calls)_


### external getTierHashes
_(no internal calls)_


### external getTokenTier
_(no internal calls)_


### external initialize
_(no internal calls)_


### external mint
-> internal _setOwner


### external removeMinter
_(no internal calls)_


### external setContractURIHash
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public tokenURI
-> internal _baseURI
-> internal _tokenURIHash


---

## TellerNFTDictionary

_File: contracts/nft/TellerNFTDictionary.sol_

### external getTierHashes
_(no internal calls)_


### public getTokenTierIndex
_(no internal calls)_


### public initialize
_(no internal calls)_


### public setAllTokenTierMappings
_(no internal calls)_


### external setTier
_(no internal calls)_


### public setTokenTierForTokenId
_(no internal calls)_


### public setTokenTierForTokenIds
-> public setTokenTierForTokenId


### public setTokenTierMapping
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public tokenBaseLoanSize
-> public getTokenTierIndex


### public tokenContributionAsset
-> public getTokenTierIndex


### public tokenContributionMultiplier
-> public getTokenTierIndex


### public tokenContributionSize
-> public getTokenTierIndex


### public tokenURIHash
-> public getTokenTierIndex


---

## TellerNFT_V2

_File: contracts/nft/TellerNFT_V2.sol_

### external contractURI
_(no internal calls)_


### external createTiers
-> internal _createTier
  -> internal _mergeTokenId


### external getOwnedTokens
_(no internal calls)_


### external getTokenTierId
-> internal _splitTokenId


### public initialize
-> internal __TellerNFT_V2_init_unchained


### public setContractURIHash
_(no internal calls)_


### external setURI
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public tokenBaseLoanSize
-> internal _splitTokenId


### public tokenContributionAsset
-> internal _splitTokenId


### public tokenContributionMultiplier
-> internal _splitTokenId


### public tokenContributionSize
-> internal _splitTokenId


### public uri
_(no internal calls)_


---

## UniswapFacet

_File: contracts/escrow/dapps/swappers/UniswapFacet.sol_

### external uniswapSwap
-> internal __isValidPath
  -> library AppStorageLib.store
-> library LibEscrow.e
-> library LibEscrow.tokenUpdated


---

## UpgradeableBeaconFactory

_File: contracts/shared/proxy/beacon/UpgradeableBeaconFactory.sol_

### external cloneProxy
_(no internal calls)_


### public implementation
_(no internal calls)_


### public upgradeTo
-> private _setImplementation


---

## YearnFacet

_File: contracts/escrow/dapps/YearnFacet.sol_

### public yearnDeposit
-> library AssetYVaultLib.get
-> library LibDapps.s
-> library LibEscrow.tokenUpdated


### public yearnWithdraw
-> library AssetYVaultLib.get
-> library LibDapps.s
-> library LibEscrow.tokenUpdated


### public yearnWithdrawAll
-> library AssetYVaultLib.get
-> library LibDapps.s
-> library LibEscrow.tokenUpdated


---

## ent_addMerkle_NFTDistributor_v1

_File: contracts/nft/distributor/entry/add-merkle.sol_

### external addMerkle
-> internal distributorStore
-> library DistributorEvents.MerkleAdded


---

## ent_claim_NFTDistributor_v1

_File: contracts/nft/distributor/entry/claim.sol_

### external claim
-> internal _isClaimed
  -> internal distributorStore
-> internal _verifyProof
  -> internal distributorStore
-> internal _setClaimed
  -> internal distributorStore
-> internal distributorStore
-> library DistributorEvents.Claimed


---

## ent_grantRole_AccessControl_v1

_File: contracts/contexts/access-control/entry/grant-role.sol_

### external grantRole
-> internal _isAdminForRole
-> internal _grantRole
  -> library AccessControlEvents.RoleGranted


---

## ent_initialize_NFTDistributor_v1

_File: contracts/nft/distributor/entry/initialize.sol_

### external grantRole
_(no internal calls)_


### external initialize
-> internal distributorStore


---

## ent_moveMerkle_NFTDistributor_v1

_File: contracts/nft/distributor/entry/move-merkle.sol_

### external moveMerkle
-> internal distributorStore


---

## ent_renounceRole_AccessControl_v1

_File: contracts/contexts/access-control/entry/renounce-role.sol_

### external renounceRole
-> internal _revokeRole
  -> library AccessControlEvents.RoleRevoked


---

## ent_revokeRole_AccessControl_v1

_File: contracts/contexts/access-control/entry/revoke-role.sol_

### external revokeRole
-> internal _isAdminForRole
-> internal _revokeRole
  -> library AccessControlEvents.RoleRevoked


---

## ent_upgradeNFTV2_NFTDistributor_v1

_File: contracts/nft/distributor/entry/upgrade-NFT-v2.sol_

### external upgradeNFTV2
-> internal distributorStore


---

## ext_adminRoleFor_AccessControl_V1

_File: contracts/contexts/access-control/external/admin-role-for.sol_

### external adminRoleFor
-> internal _adminRoleFor


---

## ext_distributor_NFT

_File: contracts/nft/distributor/external/distributor.sol_

### external getMerkleRoots
_(no internal calls)_


### external isClaimed
_(no internal calls)_


### external nft
_(no internal calls)_


---

## ext_distributor_NFT_v1

_File: contracts/nft/distributor/external/distributor.sol_

### external getMerkleRoots
-> internal distributorStore


### external isClaimed
-> internal _isClaimed
  -> internal distributorStore


### external nft
-> internal distributorStore


---

## ext_hasRole_AccessControl

_File: contracts/contexts/access-control/external/has-role.sol_

### external hasRole
_(no internal calls)_


---

## ext_hasRole_AccessControl_V1

_File: contracts/contexts/access-control/external/has-role.sol_

### external hasRole
-> internal _hasRole

