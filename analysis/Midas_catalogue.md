# Midas — Contract Catalogue

> 432 contract(s) identified across 6 primitive categories.

---

## Tokens

The protocol utilises the following token contracts for accounting purposes:

- **Blacklistable** – ERC-20 token contract exposing various operations.
  *File: `contracts/access/Blacklistable.sol`*
  *Inherits: WithMidasAccessControl*

- **Greenlistable** – ERC-20 token contract exposing `greenlistedrole`, `greenlisttogglerrole`, `setgreenlistenable`.
  *File: `contracts/access/Greenlistable.sol`*
  *Inherits: WithMidasAccessControl*
  *Key functions: `greenlistedrole`, `greenlisttogglerrole`, `setgreenlistenable`*

- **mToken** – ERC-20 token contract exposing `burn`, `mint`, `pause`, `setmetadata`, `unpause`.
  *File: `contracts/mToken.sol`*
  *Inherits: ERC20PausableUpgradeable, Blacklistable, IMToken*
  *Key functions: `burn`, `initialize`, `mint`, `pause`, `setmetadata`, `unpause`*


## Containers

The protocol stores assets in the following containers:

- **DepositVault** – Asset container that holds funds; exposes `approverequest`, `depositinstant`, `depositrequest`, `greenlisttogglerrole`, `initializev1`.
  *File: `contracts/DepositVault.sol`*
  *Inherits: ManageableVault, IDepositVault*
  *Key functions: `approverequest`, `depositinstant`, `depositrequest`, `greenlisttogglerrole`, `initialize`, `initializev1`, `initializev2`, `rejectrequest`, `safeapproverequest`, `safebulkapproverequest`, `safebulkapproverequestatsavedrate`, `setmaxsupplycap`, `setminmtokenamountforfirstdeposit`, `vaultrole`*

- **DepositVaultWithUSTB** – Asset container that holds funds; exposes `setustbdepositsenabled`.
  *File: `contracts/DepositVaultWithUSTB.sol`*
  *Inherits: DepositVault*
  *Key functions: `initialize`, `setustbdepositsenabled`*

- **RedemptionVault** – Asset container that holds funds; exposes `approverequest`, `greenlisttogglerrole`, `redeemfiatrequest`, `redeeminstant`, `redeemrequest`.
  *File: `contracts/RedemptionVault.sol`*
  *Inherits: ManageableVault, IRedemptionVault*
  *Key functions: `approverequest`, `greenlisttogglerrole`, `initialize`, `redeemfiatrequest`, `redeeminstant`, `redeemrequest`, `rejectrequest`, `safeapproverequest`, `safebulkapproverequest`, `safebulkapproverequestatsavedrate`, `setfiatadditionalfee`, `setfiatflatfee`, `setminfiatredeemamount`, `setrequestredeemer`, `vaultrole`*

- **RedemptionVaultWIthBUIDL** – Asset container that holds funds; exposes `setminbuidlbalance`, `setminbuidltoredeem`.
  *File: `contracts/RedemptionVaultWithBUIDL.sol`*
  *Inherits: RedemptionVault*
  *Key functions: `initialize`, `setminbuidlbalance`, `setminbuidltoredeem`*

- **RedemptionVaultWithSwapper** – Asset container that holds funds; exposes `setliquidityprovider`, `setswappervault`.
  *File: `contracts/RedemptionVaultWithSwapper.sol`*
  *Inherits: IRedemptionVaultWithSwapper, RedemptionVault*
  *Key functions: `initialize`, `setliquidityprovider`, `setswappervault`*

- **RedemptionVaultWithUSTB** – Asset container that holds funds; exposes various operations.
  *File: `contracts/RedemptionVaultWithUSTB.sol`*
  *Inherits: RedemptionVault*
  *Key functions: `initialize`*

- **MidasAxelarVaultExecutable** – Asset container that holds funds; exposes `depositandsend`, `handleexecutewithinterchaintoken`, `redeemandsend`.
  *File: `contracts/misc/axelar/MidasAxelarVaultExecutable.sol`*
  *Inherits: InterchainTokenExecutable, IMidasAxelarVaultExecutable, MidasInitializable*
  *Key functions: `depositandsend`, `handleexecutewithinterchaintoken`, `initialize`, `redeemandsend`*

- **MidasLzVaultComposerSync** – Asset container that holds funds; exposes `depositandsend`, `handlecompose`, `lzcompose`, `redeemandsend`.
  *File: `contracts/misc/layerzero/MidasLzVaultComposerSync.sol`*
  *Inherits: IMidasLzVaultComposerSync, MidasInitializable, ReentrancyGuardUpgradeable*
  *Key functions: `depositandsend`, `handlecompose`, `initialize`, `lzcompose`, `redeemandsend`*

- **JivDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/JIV/JivDepositVault.sol`*
  *Inherits: DepositVault, JivMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **JivRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/JIV/JivRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, JivMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **AcreMBtc1DepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/acremBTC1/AcreMBtc1DepositVault.sol`*
  *Inherits: DepositVault, AcreMBtc1MidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **AcreMBtc1RedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/acremBTC1/AcreMBtc1RedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, AcreMBtc1MidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **CUsdoDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/cUSDO/CUsdoDepositVault.sol`*
  *Inherits: DepositVault, CUsdoMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **CUsdoRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/cUSDO/CUsdoRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, CUsdoMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnEthDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnETH/DnEthDepositVault.sol`*
  *Inherits: DepositVault, DnEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnEthRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnETH/DnEthRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, DnEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnFartDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnFART/DnFartDepositVault.sol`*
  *Inherits: DepositVault, DnFartMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnFartRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnFART/DnFartRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, DnFartMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnHypeDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnHYPE/DnHypeDepositVault.sol`*
  *Inherits: DepositVault, DnHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnHypeRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnHYPE/DnHypeRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, DnHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnPumpDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnPUMP/DnPumpDepositVault.sol`*
  *Inherits: DepositVault, DnPumpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnPumpRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnPUMP/DnPumpRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, DnPumpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnTestDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnTEST/DnTestDepositVault.sol`*
  *Inherits: DepositVault, DnTestMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **DnTestRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/dnTEST/DnTestRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, DnTestMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **EUsdDepositVault** – Asset container that holds funds; exposes `greenlistedrole`, `vaultrole`.
  *File: `contracts/products/eUSD/EUsdDepositVault.sol`*
  *Inherits: DepositVault, EUsdMidasAccessControlRoles*
  *Key functions: `greenlistedrole`, `vaultrole`*

- **EUsdRedemptionVault** – Asset container that holds funds; exposes `greenlistedrole`, `vaultrole`.
  *File: `contracts/products/eUSD/EUsdRedemptionVault.sol`*
  *Inherits: RedemptionVault, EUsdMidasAccessControlRoles*
  *Key functions: `greenlistedrole`, `vaultrole`*

- **EUsdRedemptionVaultWithBUIDL** – Asset container that holds funds; exposes `greenlistedrole`, `vaultrole`.
  *File: `contracts/products/eUSD/EUsdRedemptionVaultWithBUIDL.sol`*
  *Inherits: RedemptionVaultWIthBUIDL, EUsdMidasAccessControlRoles*
  *Key functions: `greenlistedrole`, `vaultrole`*

- **HBUsdcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hbUSDC/HBUsdcDepositVault.sol`*
  *Inherits: DepositVault, HBUsdcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HBUsdcRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hbUSDC/HBUsdcRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, HBUsdcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HBUsdtDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hbUSDT/HBUsdtDepositVault.sol`*
  *Inherits: DepositVault, HBUsdtMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HBUsdtRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hbUSDT/HBUsdtRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, HBUsdtMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HBXautDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hbXAUt/HBXautDepositVault.sol`*
  *Inherits: DepositVault, HBXautMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HBXautRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hbXAUt/HBXautRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, HBXautMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HypeBtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hypeBTC/HypeBtcDepositVault.sol`*
  *Inherits: DepositVault, HypeBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HypeBtcRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hypeBTC/HypeBtcRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, HypeBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HypeEthDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hypeETH/HypeEthDepositVault.sol`*
  *Inherits: DepositVault, HypeEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HypeEthRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hypeETH/HypeEthRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, HypeEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HypeUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hypeUSD/HypeUsdDepositVault.sol`*
  *Inherits: DepositVault, HypeUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **HypeUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/hypeUSD/HypeUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, HypeUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KitBtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kitBTC/KitBtcDepositVault.sol`*
  *Inherits: DepositVault, KitBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KitBtcRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kitBTC/KitBtcRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, KitBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KitHypeDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kitHYPE/KitHypeDepositVault.sol`*
  *Inherits: DepositVault, KitHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KitHypeRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kitHYPE/KitHypeRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, KitHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KitUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kitUSD/KitUsdDepositVault.sol`*
  *Inherits: DepositVault, KitUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KitUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kitUSD/KitUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, KitUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KmiUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kmiUSD/KmiUsdDepositVault.sol`*
  *Inherits: DepositVault, KmiUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **KmiUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/kmiUSD/KmiUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, KmiUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **LiquidHypeDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/liquidHYPE/LiquidHypeDepositVault.sol`*
  *Inherits: DepositVault, LiquidHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **LiquidHypeRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/liquidHYPE/LiquidHypeRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, LiquidHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **LiquidReserveDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/liquidRESERVE/LiquidReserveDepositVault.sol`*
  *Inherits: DepositVault, LiquidReserveMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **LiquidReserveRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/liquidRESERVE/LiquidReserveRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, LiquidReserveMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **LstHypeDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/lstHYPE/LstHypeDepositVault.sol`*
  *Inherits: DepositVault, LstHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **LstHypeRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/lstHYPE/LstHypeRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, LstHypeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MApolloDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mAPOLLO/MApolloDepositVault.sol`*
  *Inherits: DepositVault, MApolloMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MApolloRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mAPOLLO/MApolloRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MApolloMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MBasisDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBASIS/MBasisDepositVault.sol`*
  *Inherits: DepositVault, MBasisMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MBasisRedemptionVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBASIS/MBasisRedemptionVault.sol`*
  *Inherits: RedemptionVault, MBasisMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MBasisRedemptionVaultWithBUIDL** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBASIS/MBasisRedemptionVaultWithBUIDL.sol`*
  *Inherits: RedemptionVaultWIthBUIDL, MBasisMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MBasisRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBASIS/MBasisRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MBasisMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MBtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBTC/MBtcDepositVault.sol`*
  *Inherits: DepositVault, MBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MBtcRedemptionVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBTC/MBtcRedemptionVault.sol`*
  *Inherits: RedemptionVault, MBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TACmBtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBTC/tac/TACmBtcDepositVault.sol`*
  *Inherits: DepositVault, TACmBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TACmBtcRedemptionVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mBTC/tac/TACmBtcRedemptionVault.sol`*
  *Inherits: RedemptionVault, TACmBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MEdgeDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mEDGE/MEdgeDepositVault.sol`*
  *Inherits: DepositVault, MEdgeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MEdgeRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mEDGE/MEdgeRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MEdgeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TACmEdgeDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mEDGE/tac/TACmEdgeDepositVault.sol`*
  *Inherits: DepositVault, TACmEdgeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TACmEdgeRedemptionVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mEDGE/tac/TACmEdgeRedemptionVault.sol`*
  *Inherits: RedemptionVault, TACmEdgeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MEvUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mEVUSD/MEvUsdDepositVault.sol`*
  *Inherits: DepositVault, MEvUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MEvUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mEVUSD/MEvUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MEvUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MFarmDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mFARM/MFarmDepositVault.sol`*
  *Inherits: DepositVault, MFarmMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MFarmRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mFARM/MFarmRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MFarmMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MFOneDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mFONE/MFOneDepositVault.sol`*
  *Inherits: DepositVault, MFOneMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MFOneRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mFONE/MFOneRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MFOneMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MHyperDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mHYPER/MHyperDepositVault.sol`*
  *Inherits: DepositVault, MHyperMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MHyperRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mHYPER/MHyperRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MHyperMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MHyperBtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mHyperBTC/MHyperBtcDepositVault.sol`*
  *Inherits: DepositVault, MHyperBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MHyperBtcRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mHyperBTC/MHyperBtcRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MHyperBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MHyperEthDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mHyperETH/MHyperEthDepositVault.sol`*
  *Inherits: DepositVault, MHyperEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MHyperEthRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mHyperETH/MHyperEthRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MHyperEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MKRalphaDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mKRalpha/MKRalphaDepositVault.sol`*
  *Inherits: DepositVault, MKRalphaMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MKRalphaRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mKRalpha/MKRalphaRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MKRalphaMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MLiquidityDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mLIQUIDITY/MLiquidityDepositVault.sol`*
  *Inherits: DepositVault, MLiquidityMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MLiquidityRedemptionVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mLIQUIDITY/MLiquidityRedemptionVault.sol`*
  *Inherits: RedemptionVault, MLiquidityMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MM1UsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mM1USD/MM1UsdDepositVault.sol`*
  *Inherits: DepositVault, MM1UsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MM1UsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mM1USD/MM1UsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MM1UsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MMevDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mMEV/MMevDepositVault.sol`*
  *Inherits: DepositVault, MMevMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MMevRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mMEV/MMevRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MMevMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TACmMevDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mMEV/tac/TACmMevDepositVault.sol`*
  *Inherits: DepositVault, TACmMevMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TACmMevRedemptionVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mMEV/tac/TACmMevRedemptionVault.sol`*
  *Inherits: RedemptionVault, TACmMevMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MPortofinoDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mPortofino/MPortofinoDepositVault.sol`*
  *Inherits: DepositVault, MPortofinoMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MPortofinoRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mPortofino/MPortofinoRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MPortofinoMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRe7DepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mRE7/MRe7DepositVault.sol`*
  *Inherits: DepositVault, MRe7MidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRe7RedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mRE7/MRe7RedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MRe7MidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRe7BtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mRE7BTC/MRe7BtcDepositVault.sol`*
  *Inherits: DepositVault, MRe7BtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRe7BtcRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mRE7BTC/MRe7BtcRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MRe7BtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRe7SolDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mRE7SOL/MRe7SolDepositVault.sol`*
  *Inherits: DepositVault, MRe7SolMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRe7SolRedemptionVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mRE7SOL/MRe7SolRedemptionVault.sol`*
  *Inherits: RedemptionVault, MRe7SolMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRoxDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mROX/MRoxDepositVault.sol`*
  *Inherits: DepositVault, MRoxMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MRoxRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mROX/MRoxRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MRoxMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MSlDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mSL/MSlDepositVault.sol`*
  *Inherits: DepositVault, MSlMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MSlRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mSL/MSlRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MSlMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MTuDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mTU/MTuDepositVault.sol`*
  *Inherits: DepositVault, MTuMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MTuRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mTU/MTuRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MTuMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MWildUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mWildUSD/MWildUsdDepositVault.sol`*
  *Inherits: DepositVault, MWildUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MWildUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mWildUSD/MWildUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MWildUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MXrpDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mXRP/MXrpDepositVault.sol`*
  *Inherits: DepositVault, MXrpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MXrpRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mXRP/MXrpRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MXrpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MevBtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mevBTC/MevBtcDepositVault.sol`*
  *Inherits: DepositVault, MevBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MevBtcRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/mevBTC/MevBtcRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MevBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MSyrupUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/msyrupUSD/MSyrupUsdDepositVault.sol`*
  *Inherits: DepositVault, MSyrupUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MSyrupUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/msyrupUSD/MSyrupUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MSyrupUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MSyrupUsdpDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/msyrupUSDp/MSyrupUsdpDepositVault.sol`*
  *Inherits: DepositVault, MSyrupUsdpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **MSyrupUsdpRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/msyrupUSDp/MSyrupUsdpRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, MSyrupUsdpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ObeatUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/obeatUSD/ObeatUsdDepositVault.sol`*
  *Inherits: DepositVault, ObeatUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ObeatUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/obeatUSD/ObeatUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, ObeatUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **PlUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/plUSD/PlUsdDepositVault.sol`*
  *Inherits: DepositVault, PlUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **PlUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/plUSD/PlUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, PlUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **SLInjDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/sLINJ/SLInjDepositVault.sol`*
  *Inherits: DepositVault, SLInjMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **SLInjRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/sLINJ/SLInjRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, SLInjMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **SplUsdDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/splUSD/SplUsdDepositVault.sol`*
  *Inherits: DepositVault, SplUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **SplUsdRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/splUSD/SplUsdRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, SplUsdMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TBtcDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tBTC/TBtcDepositVault.sol`*
  *Inherits: DepositVault, TBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TBtcRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tBTC/TBtcRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, TBtcMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TEthDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tETH/TEthDepositVault.sol`*
  *Inherits: DepositVault, TEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TEthRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tETH/TEthRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, TEthMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TUsdeDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tUSDe/TUsdeDepositVault.sol`*
  *Inherits: DepositVault, TUsdeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TUsdeRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tUSDe/TUsdeRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, TUsdeMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TacTonDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tacTON/TacTonDepositVault.sol`*
  *Inherits: DepositVault, TacTonMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **TacTonRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/tacTON/TacTonRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, TacTonMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **WNlpDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/wNLP/WNlpDepositVault.sol`*
  *Inherits: DepositVault, WNlpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **WNlpRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/wNLP/WNlpRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, WNlpMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **WVLPDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/wVLP/WVLPDepositVault.sol`*
  *Inherits: DepositVault, WVLPMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **WVLPRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/wVLP/WVLPRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, WVLPMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **WeEurDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/weEUR/WeEurDepositVault.sol`*
  *Inherits: DepositVault, WeEurMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **WeEurRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/weEUR/WeEurRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, WeEurMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ZeroGBtcvDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/zeroGBTCV/ZeroGBtcvDepositVault.sol`*
  *Inherits: DepositVault, ZeroGBtcvMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ZeroGBtcvRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/zeroGBTCV/ZeroGBtcvRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, ZeroGBtcvMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ZeroGEthvDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/zeroGETHV/ZeroGEthvDepositVault.sol`*
  *Inherits: DepositVault, ZeroGEthvMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ZeroGEthvRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/zeroGETHV/ZeroGEthvRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, ZeroGEthvMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ZeroGUsdvDepositVault** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/zeroGUSDV/ZeroGUsdvDepositVault.sol`*
  *Inherits: DepositVault, ZeroGUsdvMidasAccessControlRoles*
  *Key functions: `vaultrole`*

- **ZeroGUsdvRedemptionVaultWithSwapper** – Asset container that holds funds; exposes `vaultrole`.
  *File: `contracts/products/zeroGUSDV/ZeroGUsdvRedemptionVaultWithSwapper.sol`*
  *Inherits: RedemptionVaultWithSwapper, ZeroGUsdvMidasAccessControlRoles*
  *Key functions: `vaultrole`*


## Minters

The protocol manages token supply through the following minter contracts:

- **MidasLzMintBurnOFTAdapter** – Manages token supply by coordinating `burn`, `getratelimit`, `mint`, `setratelimits`, `shareddecimals`.
  *File: `contracts/misc/layerzero/MidasLzMintBurnOFTAdapter.sol`*
  *Inherits: IMintableBurnable, MintBurnOFTAdapter, RateLimiter*
  *Key functions: `burn`, `getratelimit`, `mint`, `setratelimits`, `shareddecimals`*


## Oracle

The protocol uses the following oracle contracts to obtain external price data:

- **CustomAggregatorV3CompatibleFeed** – Provides price data via `decimals`, `feedadminrole`, `getrounddata`, `lastanswer`, `lasttimestamp`.
  *File: `contracts/feeds/CustomAggregatorV3CompatibleFeed.sol`*
  *Inherits: WithMidasAccessControl, AggregatorV3Interface*
  *Key functions: `decimals`, `feedadminrole`, `getrounddata`, `initialize`, `lastanswer`, `lasttimestamp`, `latestrounddata`, `setrounddata`, `setrounddatasafe`, `version`*

- **CustomAggregatorV3CompatibleFeedDiscounted** – Provides price data via `decimals`, `description`, `getrounddata`, `latestrounddata`.
  *File: `contracts/feeds/CustomAggregatorV3CompatibleFeedDiscounted.sol`*
  *Inherits: AggregatorV3Interface*
  *Key functions: `decimals`, `description`, `getrounddata`, `latestrounddata`, `version`*

- **CustomAggregatorV3CompatibleFeedGrowth** – Provides price data via `applygrowth`, `decimals`, `feedadminrole`, `getrounddata`, `getrounddataraw`.
  *File: `contracts/feeds/CustomAggregatorV3CompatibleFeedGrowth.sol`*
  *Inherits: WithMidasAccessControl, IAggregatorV3CompatibleFeedGrowth*
  *Key functions: `applygrowth`, `decimals`, `feedadminrole`, `getrounddata`, `getrounddataraw`, `initialize`, `lastanswer`, `lastgrowthapr`, `laststartedat`, `lasttimestamp`, `latestrounddata`, `latestrounddataraw`, `setmaxgrowthapr`, `setmingrowthapr`, `setonlyup`, `setrounddata`, `setrounddatasafe`, `version`*

- **BandStdChailinkAdapter** – Provides price data via `description`, `latestanswer`, `latestrounddata`, `latesttimestamp`.
  *File: `contracts/misc/adapters/BandStdChailinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`, `latestrounddata`, `latesttimestamp`*

- **BeHypeChainlinkAdapter** – Provides price data via `description`, `latestanswer`.
  *File: `contracts/misc/adapters/BeHypeChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`*

- **ChainlinkAdapterBase** – Provides price data via `decimals`, `description`, `getanswer`, `getrounddata`, `gettimestamp`.
  *File: `contracts/misc/adapters/ChainlinkAdapterBase.sol`*
  *Inherits: AggregatorV3Interface*
  *Key functions: `decimals`, `description`, `getanswer`, `getrounddata`, `gettimestamp`, `latestanswer`, `latestround`, `latestrounddata`, `latesttimestamp`, `version`*

- **ERC4626ChainlinkAdapter** – Provides price data via `decimals`, `description`, `latestanswer`, `vaultdecimals`.
  *File: `contracts/misc/adapters/ERC4626ChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `decimals`, `description`, `latestanswer`, `vaultdecimals`*

- **MantleLspStakingChainlinkAdapter** – Provides price data via `description`, `latestanswer`.
  *File: `contracts/misc/adapters/MantleLspStakingChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`*

- **PythChainlinkAdapter** – Provides price data via `decimals`, `description`, `latestanswer`, `latestrounddata`, `latesttimestamp`.
  *File: `contracts/misc/adapters/PythChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `decimals`, `description`, `latestanswer`, `latestrounddata`, `latesttimestamp`, `updatefeeds`*

- **RsEthChainlinkAdapter** – Provides price data via `description`, `latestanswer`.
  *File: `contracts/misc/adapters/RsEthChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`*

- **StorkChainlinkAdapter** – Provides price data via `description`, `latestanswer`, `latestrounddata`, `latesttimestamp`.
  *File: `contracts/misc/adapters/StorkChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`, `latestrounddata`, `latesttimestamp`*

- **SyrupChainlinkAdapter** – Provides price data via `description`, `latestanswer`.
  *File: `contracts/misc/adapters/SyrupChainlinkAdapter.sol`*
  *Inherits: ERC4626ChainlinkAdapter*
  *Key functions: `description`, `latestanswer`*

- **WrappedEEthChainlinkAdapter** – Provides price data via `description`, `latestanswer`.
  *File: `contracts/misc/adapters/WrappedEEthChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`*

- **WstEthChainlinkAdapter** – Provides price data via `description`, `latestanswer`.
  *File: `contracts/misc/adapters/WstEthChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`*

- **YInjChainlinkAdapter** – Provides price data via `description`, `latestanswer`.
  *File: `contracts/misc/adapters/YInjChainlinkAdapter.sol`*
  *Inherits: ChainlinkAdapterBase*
  *Key functions: `description`, `latestanswer`*

- **JivCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/JIV/JivCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, JivMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **AcreMBtc1CustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/acremBTC1/AcreMBtc1CustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, AcreMBtc1MidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **CUsdoCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/cUSDO/CUsdoCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, CUsdoMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnEthCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/dnETH/DnEthCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, DnEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnFartCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/dnFART/DnFartCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, DnFartMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnHypeCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/dnHYPE/DnHypeCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, DnHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnPumpCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/dnPUMP/DnPumpCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, DnPumpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnTestCustomAggregatorFeedGrowth** – Provides price data via `feedadminrole`.
  *File: `contracts/products/dnTEST/DnTestCustomAggregatorFeedGrowth.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeedGrowth, DnTestMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HBUsdcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/hbUSDC/HBUsdcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, HBUsdcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HBUsdtCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/hbUSDT/HBUsdtCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, HBUsdtMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HBXautCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/hbXAUt/HBXautCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, HBXautMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HypeBtcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/hypeBTC/HypeBtcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, HypeBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HypeEthCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/hypeETH/HypeEthCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, HypeEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HypeUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/hypeUSD/HypeUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, HypeUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KitBtcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/kitBTC/KitBtcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, KitBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KitHypeCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/kitHYPE/KitHypeCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, KitHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KitUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/kitUSD/KitUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, KitUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KmiUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/kmiUSD/KmiUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, KmiUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **LiquidHypeCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/liquidHYPE/LiquidHypeCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, LiquidHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **LiquidReserveCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/liquidRESERVE/LiquidReserveCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, LiquidReserveMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **LstHypeCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/lstHYPE/LstHypeCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, LstHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MApolloCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mAPOLLO/MApolloCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MApolloMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MBasisCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mBASIS/MBasisCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MBasisMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MBtcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mBTC/MBtcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MEdgeCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mEDGE/MEdgeCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MEdgeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MEvUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mEVUSD/MEvUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MEvUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MFarmCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mFARM/MFarmCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MFarmMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MFOneCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mFONE/MFOneCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MFOneMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MHyperCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mHYPER/MHyperCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MHyperMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MHyperBtcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mHyperBTC/MHyperBtcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MHyperBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MHyperEthCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mHyperETH/MHyperEthCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MHyperEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MKRalphaCustomAggregatorFeed** – Provides price data via `feedadminrole`, `initializev2`.
  *File: `contracts/products/mKRalpha/MKRalphaCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MKRalphaMidasAccessControlRoles*
  *Key functions: `feedadminrole`, `initialize`, `initializev2`*

- **MLiquidityCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mLIQUIDITY/MLiquidityCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MLiquidityMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MM1UsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mM1USD/MM1UsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MM1UsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MMevCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mMEV/MMevCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MMevMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MPortofinoCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mPortofino/MPortofinoCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MPortofinoMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MRe7CustomAggregatorFeed** – Provides price data via `feedadminrole`, `initializev3`.
  *File: `contracts/products/mRE7/MRe7CustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MRe7MidasAccessControlRoles*
  *Key functions: `feedadminrole`, `initialize`, `initializev3`*

- **MRe7BtcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mRE7BTC/MRe7BtcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MRe7BtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MRe7SolCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mRE7SOL/MRe7SolCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MRe7SolMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MRoxCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mROX/MRoxCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MRoxMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MSlCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mSL/MSLCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MSlMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MTBillCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mTBILL/MTBillCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MTBillMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MTBillCustomAggregatorFeedGrowth** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mTBILL/MTBillCustomAggregatorFeedGrowth.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeedGrowth, MTBillMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MTuCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mTU/MTuCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MTuMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MWildUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mWildUSD/MWildUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MWildUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MXrpCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mXRP/MXrpCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MXrpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MevBtcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/mevBTC/MevBtcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MevBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MSyrupUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/msyrupUSD/MSyrupUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MSyrupUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MSyrupUsdpCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/msyrupUSDp/MSyrupUsdpCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, MSyrupUsdpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ObeatUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/obeatUSD/ObeatUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, ObeatUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **PlUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/plUSD/PlUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, PlUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **SLInjCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/sLINJ/SLInjCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, SLInjMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **SplUsdCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/splUSD/SplUsdCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, SplUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TBtcCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/tBTC/TBtcCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, TBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TEthCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/tETH/TEthCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, TEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TUsdeCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/tUSDe/TUsdeCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, TUsdeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TacTonCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/tacTON/TacTonCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, TacTonMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **WNlpCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/wNLP/WNlpCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, WNlpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **WVLPCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/wVLP/WVLPCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, WVLPMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **WeEurCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/weEUR/WeEurCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, WeEurMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ZeroGBtcvCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/zeroGBTCV/ZeroGBtcvCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, ZeroGBtcvMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ZeroGEthvCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/zeroGETHV/ZeroGEthvCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, ZeroGEthvMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ZeroGUsdvCustomAggregatorFeed** – Provides price data via `feedadminrole`.
  *File: `contracts/products/zeroGUSDV/ZeroGUsdvCustomAggregatorFeed.sol`*
  *Inherits: CustomAggregatorV3CompatibleFeed, ZeroGUsdvMidasAccessControlRoles*
  *Key functions: `feedadminrole`*


## Access Control

The protocol manages permissions through the following access-control contracts:

- **MidasAccessControl** – Enforces access control; implements `grantrolemult`, `renouncerole`, `revokerolemult`.
  *File: `contracts/access/MidasAccessControl.sol`*
  *Inherits: AccessControlUpgradeable, MidasInitializable, MidasAccessControlRoles*
  *Key functions: `grantrolemult`, `initialize`, `renouncerole`, `revokerolemult`*

- **MidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/access/MidasAccessControlRoles.sol`*

- **Pausable** – Enforces access control; implements `pause`, `pauseadminrole`, `pausefn`, `unpause`, `unpausefn`.
  *File: `contracts/access/Pausable.sol`*
  *Inherits: WithMidasAccessControl, PausableUpgradeable*
  *Key functions: `pause`, `pauseadminrole`, `pausefn`, `unpause`, `unpausefn`*

- **WithMidasAccessControl** – Enforces access control; implements various operations.
  *File: `contracts/access/WithMidasAccessControl.sol`*
  *Inherits: MidasInitializable, MidasAccessControlRoles*

- **CompositeDataFeed** – Enforces access control; implements `changedenominatorfeed`, `changenumeratorfeed`, `feedadminrole`, `getdatainbase18`, `setmaxexpectedanswer`.
  *File: `contracts/feeds/CompositeDataFeed.sol`*
  *Inherits: WithMidasAccessControl, IDataFeed*
  *Key functions: `changedenominatorfeed`, `changenumeratorfeed`, `feedadminrole`, `getdatainbase18`, `initialize`, `setmaxexpectedanswer`, `setminexpectedanswer`*

- **DataFeed** – Enforces access control; implements `changeaggregator`, `feedadminrole`, `getdatainbase18`, `sethealthydiff`, `setmaxexpectedanswer`.
  *File: `contracts/feeds/DataFeed.sol`*
  *Inherits: WithMidasAccessControl, IDataFeed*
  *Key functions: `changeaggregator`, `feedadminrole`, `getdatainbase18`, `initialize`, `sethealthydiff`, `setmaxexpectedanswer`, `setminexpectedanswer`*

- **JivDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/JIV/JivDataFeed.sol`*
  *Inherits: DataFeed, JivMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **JivMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/JIV/JivMidasAccessControlRoles.sol`*

- **AcreMBtc1DataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/acremBTC1/AcreMBtc1DataFeed.sol`*
  *Inherits: DataFeed, AcreMBtc1MidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **AcreMBtc1MidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/acremBTC1/AcreMBtc1MidasAccessControlRoles.sol`*

- **CUsdoDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/cUSDO/CUsdoDataFeed.sol`*
  *Inherits: DataFeed, CUsdoMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **CUsdoMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/cUSDO/CUsdoMidasAccessControlRoles.sol`*

- **DnEthDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/dnETH/DnEthDataFeed.sol`*
  *Inherits: DataFeed, DnEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnEthMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/dnETH/DnEthMidasAccessControlRoles.sol`*

- **DnFartDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/dnFART/DnFartDataFeed.sol`*
  *Inherits: DataFeed, DnFartMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnFartMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/dnFART/DnFartMidasAccessControlRoles.sol`*

- **DnHypeDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/dnHYPE/DnHypeDataFeed.sol`*
  *Inherits: DataFeed, DnHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnHypeMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/dnHYPE/DnHypeMidasAccessControlRoles.sol`*

- **DnPumpDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/dnPUMP/DnPumpDataFeed.sol`*
  *Inherits: DataFeed, DnPumpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnPumpMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/dnPUMP/DnPumpMidasAccessControlRoles.sol`*

- **DnTestDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/dnTEST/DnTestDataFeed.sol`*
  *Inherits: DataFeed, DnTestMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **DnTestMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/dnTEST/DnTestMidasAccessControlRoles.sol`*

- **EUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/eUSD/EUsdMidasAccessControlRoles.sol`*

- **HBUsdcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/hbUSDC/HBUsdcDataFeed.sol`*
  *Inherits: DataFeed, HBUsdcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HBUsdcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/hbUSDC/HBUsdcMidasAccessControlRoles.sol`*

- **HBUsdtDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/hbUSDT/HBUsdtDataFeed.sol`*
  *Inherits: DataFeed, HBUsdtMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HBUsdtMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/hbUSDT/HBUsdtMidasAccessControlRoles.sol`*

- **HBXautDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/hbXAUt/HBXautDataFeed.sol`*
  *Inherits: DataFeed, HBXautMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HBXautMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/hbXAUt/HBXautMidasAccessControlRoles.sol`*

- **HypeBtcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/hypeBTC/HypeBtcDataFeed.sol`*
  *Inherits: DataFeed, HypeBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HypeBtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/hypeBTC/HypeBtcMidasAccessControlRoles.sol`*

- **HypeEthDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/hypeETH/HypeEthDataFeed.sol`*
  *Inherits: DataFeed, HypeEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HypeEthMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/hypeETH/HypeEthMidasAccessControlRoles.sol`*

- **HypeUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/hypeUSD/HypeUsdDataFeed.sol`*
  *Inherits: DataFeed, HypeUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **HypeUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/hypeUSD/HypeUsdMidasAccessControlRoles.sol`*

- **KitBtcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/kitBTC/KitBtcDataFeed.sol`*
  *Inherits: DataFeed, KitBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KitBtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/kitBTC/KitBtcMidasAccessControlRoles.sol`*

- **KitHypeDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/kitHYPE/KitHypeDataFeed.sol`*
  *Inherits: DataFeed, KitHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KitHypeMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/kitHYPE/KitHypeMidasAccessControlRoles.sol`*

- **KitUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/kitUSD/KitUsdDataFeed.sol`*
  *Inherits: DataFeed, KitUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KitUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/kitUSD/KitUsdMidasAccessControlRoles.sol`*

- **KmiUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/kmiUSD/KmiUsdDataFeed.sol`*
  *Inherits: DataFeed, KmiUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **KmiUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/kmiUSD/KmiUsdMidasAccessControlRoles.sol`*

- **LiquidHypeDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/liquidHYPE/LiquidHypeDataFeed.sol`*
  *Inherits: DataFeed, LiquidHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **LiquidHypeMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/liquidHYPE/LiquidHypeMidasAccessControlRoles.sol`*

- **LiquidReserveDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/liquidRESERVE/LiquidReserveDataFeed.sol`*
  *Inherits: DataFeed, LiquidReserveMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **LiquidReserveMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/liquidRESERVE/LiquidReserveMidasAccessControlRoles.sol`*

- **LstHypeDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/lstHYPE/LstHypeDataFeed.sol`*
  *Inherits: DataFeed, LstHypeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **LstHypeMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/lstHYPE/LstHypeMidasAccessControlRoles.sol`*

- **MApolloDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mAPOLLO/MApolloDataFeed.sol`*
  *Inherits: DataFeed, MApolloMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MApolloMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mAPOLLO/MApolloMidasAccessControlRoles.sol`*

- **MBasisDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mBASIS/MBasisDataFeed.sol`*
  *Inherits: DataFeed, MBasisMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MBasisMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mBASIS/MBasisMidasAccessControlRoles.sol`*

- **MBtcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mBTC/MBtcDataFeed.sol`*
  *Inherits: DataFeed, MBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MBtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mBTC/MBtcMidasAccessControlRoles.sol`*

- **TACmBtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mBTC/tac/TACmBtcMidasAccessControlRoles.sol`*

- **MEdgeDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mEDGE/MEdgeDataFeed.sol`*
  *Inherits: DataFeed, MEdgeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MEdgeMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mEDGE/MEdgeMidasAccessControlRoles.sol`*

- **TACmEdgeMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mEDGE/tac/TACmEdgeMidasAccessControlRoles.sol`*

- **MEvUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mEVUSD/MEvUsdDataFeed.sol`*
  *Inherits: DataFeed, MEvUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MEvUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mEVUSD/MEvUsdMidasAccessControlRoles.sol`*

- **MFarmDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mFARM/MFarmDataFeed.sol`*
  *Inherits: DataFeed, MFarmMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MFarmMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mFARM/MFarmMidasAccessControlRoles.sol`*

- **MFOneDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mFONE/MFOneDataFeed.sol`*
  *Inherits: DataFeed, MFOneMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MFOneMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mFONE/MFOneMidasAccessControlRoles.sol`*

- **MHyperDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mHYPER/MHyperDataFeed.sol`*
  *Inherits: DataFeed, MHyperMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MHyperMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mHYPER/MHyperMidasAccessControlRoles.sol`*

- **MHyperBtcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mHyperBTC/MHyperBtcDataFeed.sol`*
  *Inherits: DataFeed, MHyperBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MHyperBtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mHyperBTC/MHyperBtcMidasAccessControlRoles.sol`*

- **MHyperEthDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mHyperETH/MHyperEthDataFeed.sol`*
  *Inherits: DataFeed, MHyperEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MHyperEthMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mHyperETH/MHyperEthMidasAccessControlRoles.sol`*

- **MKRalphaDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mKRalpha/MKRalphaDataFeed.sol`*
  *Inherits: DataFeed, MKRalphaMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MKRalphaMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mKRalpha/MKRalphaMidasAccessControlRoles.sol`*

- **MLiquidityDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mLIQUIDITY/MLiquidityDataFeed.sol`*
  *Inherits: DataFeed, MLiquidityMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MLiquidityMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mLIQUIDITY/MLiquidityMidasAccessControlRoles.sol`*

- **MM1UsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mM1USD/MM1UsdDataFeed.sol`*
  *Inherits: DataFeed, MM1UsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MM1UsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mM1USD/MM1UsdMidasAccessControlRoles.sol`*

- **MMevDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mMEV/MMevDataFeed.sol`*
  *Inherits: DataFeed, MMevMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MMevMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mMEV/MMevMidasAccessControlRoles.sol`*

- **TACmMevMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mMEV/tac/TACmMevMidasAccessControlRoles.sol`*

- **MPortofinoDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mPortofino/MPortofinoDataFeed.sol`*
  *Inherits: DataFeed, MPortofinoMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MPortofinoMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mPortofino/MPortofinoMidasAccessControlRoles.sol`*

- **MRe7DataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mRE7/MRe7DataFeed.sol`*
  *Inherits: DataFeed, MRe7MidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MRe7MidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mRE7/MRe7MidasAccessControlRoles.sol`*

- **MRe7BtcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mRE7BTC/MRe7BtcDataFeed.sol`*
  *Inherits: DataFeed, MRe7BtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MRe7BtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mRE7BTC/MRe7BtcMidasAccessControlRoles.sol`*

- **MRe7SolDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mRE7SOL/MRe7SolDataFeed.sol`*
  *Inherits: DataFeed, MRe7SolMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MRe7SolMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mRE7SOL/MRe7SolMidasAccessControlRoles.sol`*

- **MRoxDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mROX/MRoxDataFeed.sol`*
  *Inherits: DataFeed, MRoxMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MRoxMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mROX/MRoxMidasAccessControlRoles.sol`*

- **MSlDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mSL/MSlDataFeed.sol`*
  *Inherits: DataFeed, MSlMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MSlMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mSL/MSlMidasAccessControlRoles.sol`*

- **MTBillDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mTBILL/MTBillDataFeed.sol`*
  *Inherits: DataFeed, MTBillMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MTBillMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mTBILL/MTBillMidasAccessControlRoles.sol`*

- **MTuDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mTU/MTuDataFeed.sol`*
  *Inherits: DataFeed, MTuMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MTuMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mTU/MTuMidasAccessControlRoles.sol`*

- **MWildUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mWildUSD/MWildUsdDataFeed.sol`*
  *Inherits: DataFeed, MWildUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MWildUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mWildUSD/MWildUsdMidasAccessControlRoles.sol`*

- **MXrpDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mXRP/MXrpDataFeed.sol`*
  *Inherits: DataFeed, MXrpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MXrpMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mXRP/MXrpMidasAccessControlRoles.sol`*

- **MevBtcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/mevBTC/MevBtcDataFeed.sol`*
  *Inherits: DataFeed, MevBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MevBtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/mevBTC/MevBtcMidasAccessControlRoles.sol`*

- **MSyrupUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/msyrupUSD/MSyrupUsdDataFeed.sol`*
  *Inherits: DataFeed, MSyrupUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MSyrupUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/msyrupUSD/MSyrupUsdMidasAccessControlRoles.sol`*

- **MSyrupUsdpDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/msyrupUSDp/MSyrupUsdpDataFeed.sol`*
  *Inherits: DataFeed, MSyrupUsdpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **MSyrupUsdpMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/msyrupUSDp/MSyrupUsdpMidasAccessControlRoles.sol`*

- **ObeatUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/obeatUSD/ObeatUsdDataFeed.sol`*
  *Inherits: DataFeed, ObeatUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ObeatUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/obeatUSD/ObeatUsdMidasAccessControlRoles.sol`*

- **PlUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/plUSD/PlUsdDataFeed.sol`*
  *Inherits: DataFeed, PlUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **PlUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/plUSD/PlUsdMidasAccessControlRoles.sol`*

- **SLInjDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/sLINJ/SLInjDataFeed.sol`*
  *Inherits: DataFeed, SLInjMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **SLInjMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/sLINJ/SLInjMidasAccessControlRoles.sol`*

- **SplUsdDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/splUSD/SplUsdDataFeed.sol`*
  *Inherits: DataFeed, SplUsdMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **SplUsdMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/splUSD/SplUsdMidasAccessControlRoles.sol`*

- **TBtcDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/tBTC/TBtcDataFeed.sol`*
  *Inherits: DataFeed, TBtcMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TBtcMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/tBTC/TBtcMidasAccessControlRoles.sol`*

- **TEthDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/tETH/TEthDataFeed.sol`*
  *Inherits: DataFeed, TEthMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TEthMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/tETH/TEthMidasAccessControlRoles.sol`*

- **TUsdeDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/tUSDe/TUsdeDataFeed.sol`*
  *Inherits: DataFeed, TUsdeMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TUsdeMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/tUSDe/TUsdeMidasAccessControlRoles.sol`*

- **TacTonDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/tacTON/TacTonDataFeed.sol`*
  *Inherits: DataFeed, TacTonMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **TacTonMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/tacTON/TacTonMidasAccessControlRoles.sol`*

- **WNlpDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/wNLP/WNlpDataFeed.sol`*
  *Inherits: DataFeed, WNlpMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **WNlpMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/wNLP/WNlpMidasAccessControlRoles.sol`*

- **WVLPDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/wVLP/WVLPDataFeed.sol`*
  *Inherits: DataFeed, WVLPMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **WVLPMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/wVLP/WVLPMidasAccessControlRoles.sol`*

- **WeEurDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/weEUR/WeEurDataFeed.sol`*
  *Inherits: DataFeed, WeEurMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **WeEurMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/weEUR/WeEurMidasAccessControlRoles.sol`*

- **ZeroGBtcvDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/zeroGBTCV/ZeroGBtcvDataFeed.sol`*
  *Inherits: DataFeed, ZeroGBtcvMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ZeroGBtcvMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/zeroGBTCV/ZeroGBtcvMidasAccessControlRoles.sol`*

- **ZeroGEthvDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/zeroGETHV/ZeroGEthvDataFeed.sol`*
  *Inherits: DataFeed, ZeroGEthvMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ZeroGEthvMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/zeroGETHV/ZeroGEthvMidasAccessControlRoles.sol`*

- **ZeroGUsdvDataFeed** – Enforces access control; implements `feedadminrole`.
  *File: `contracts/products/zeroGUSDV/ZeroGUsdvDataFeed.sol`*
  *Inherits: DataFeed, ZeroGUsdvMidasAccessControlRoles*
  *Key functions: `feedadminrole`*

- **ZeroGUsdvMidasAccessControlRoles** – Enforces access control; implements various operations.
  *File: `contracts/products/zeroGUSDV/ZeroGUsdvMidasAccessControlRoles.sol`*


## Other

The protocol includes the following auxiliary contracts:

- **MidasTimelockController** – Auxiliary contract implementing `getinitialexecutors`, `getinitialproposers`.
  *File: `contracts/access/MidasTimelockController.sol`*
  *Inherits: TimelockController*
  *Key functions: `getinitialexecutors`, `getinitialproposers`*

- **CompositeDataFeedMultiply** – Auxiliary contract implementing various operations.
  *File: `contracts/feeds/CompositeDataFeedMultiply.sol`*
  *Inherits: CompositeDataFeed*

- **AcreAdapter** – Auxiliary contract implementing `asset`, `converttoassets`, `converttoshares`, `deposit`, `requestredeem`.
  *File: `contracts/misc/acre/AcreAdapter.sol`*
  *Inherits: IAcreAdapter*
  *Key functions: `asset`, `converttoassets`, `converttoshares`, `deposit`, `requestredeem`, `share`*

- **CompositeDataFeedToBandStdAdapter** – Auxiliary contract implementing various operations.
  *File: `contracts/misc/adapters/CompositeDataFeedToBandStdAdapter.sol`*
  *Inherits: DataFeedToBandStdAdapter*

- **DataFeedToBandStdAdapter** – Auxiliary contract implementing `getreferencedata`, `getreferencedatabulk`.
  *File: `contracts/misc/adapters/DataFeedToBandStdAdapter.sol`*
  *Inherits: IStdReference*
  *Key functions: `getreferencedata`, `getreferencedatabulk`*

- **PythStructs** – Auxiliary contract implementing various operations.
  *File: `contracts/misc/adapters/PythChainlinkAdapter.sol`*

- **StorkStructs** – Auxiliary contract implementing various operations.
  *File: `contracts/misc/adapters/StorkChainlinkAdapter.sol`*

- **MidasLzOFT** – Auxiliary contract implementing `shareddecimals`.
  *File: `contracts/misc/layerzero/MidasLzOFT.sol`*
  *Inherits: OFT*
  *Key functions: `shareddecimals`*

- **MidasLzOFTAdapter** – Auxiliary contract implementing `shareddecimals`.
  *File: `contracts/misc/layerzero/MidasLzOFTAdapter.sol`*
  *Inherits: OFTAdapter*
  *Key functions: `shareddecimals`*

- **JIV** – Auxiliary contract implementing various operations.
  *File: `contracts/products/JIV/JIV.sol`*
  *Inherits: mToken*

- **acremBTC1** – Auxiliary contract implementing `name`, `symbol`.
  *File: `contracts/products/acremBTC1/acremBTC1.sol`*
  *Inherits: mToken*
  *Key functions: `name`, `symbol`*

- **cUSDO** – Auxiliary contract implementing various operations.
  *File: `contracts/products/cUSDO/cUSDO.sol`*
  *Inherits: mToken*

- **dnETH** – Auxiliary contract implementing various operations.
  *File: `contracts/products/dnETH/dnETH.sol`*
  *Inherits: mToken*

- **dnFART** – Auxiliary contract implementing various operations.
  *File: `contracts/products/dnFART/dnFART.sol`*
  *Inherits: mToken*

- **dnHYPE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/dnHYPE/dnHYPE.sol`*
  *Inherits: mToken*

- **dnPUMP** – Auxiliary contract implementing various operations.
  *File: `contracts/products/dnPUMP/dnPUMP.sol`*
  *Inherits: mToken*

- **dnTEST** – Auxiliary contract implementing various operations.
  *File: `contracts/products/dnTEST/dnTEST.sol`*
  *Inherits: mToken*

- **eUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/eUSD/eUSD.sol`*
  *Inherits: mToken*

- **hbUSDC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/hbUSDC/hbUSDC.sol`*
  *Inherits: mToken*

- **hbUSDT** – Auxiliary contract implementing various operations.
  *File: `contracts/products/hbUSDT/hbUSDT.sol`*
  *Inherits: mToken*

- **hbXAUt** – Auxiliary contract implementing various operations.
  *File: `contracts/products/hbXAUt/hbXAUt.sol`*
  *Inherits: mToken*

- **hypeBTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/hypeBTC/hypeBTC.sol`*
  *Inherits: mToken*

- **hypeETH** – Auxiliary contract implementing various operations.
  *File: `contracts/products/hypeETH/hypeETH.sol`*
  *Inherits: mToken*

- **hypeUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/hypeUSD/hypeUSD.sol`*
  *Inherits: mToken*

- **kitBTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/kitBTC/kitBTC.sol`*
  *Inherits: mToken*

- **kitHYPE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/kitHYPE/kitHYPE.sol`*
  *Inherits: mToken*

- **kitUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/kitUSD/kitUSD.sol`*
  *Inherits: mToken*

- **kmiUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/kmiUSD/kmiUSD.sol`*
  *Inherits: mToken*

- **liquidHYPE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/liquidHYPE/liquidHYPE.sol`*
  *Inherits: mToken*

- **liquidRESERVE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/liquidRESERVE/liquidRESERVE.sol`*
  *Inherits: mToken*

- **lstHYPE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/lstHYPE/lstHYPE.sol`*
  *Inherits: mToken*

- **mAPOLLO** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mAPOLLO/mAPOLLO.sol`*
  *Inherits: mToken*

- **mBASIS** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mBASIS/mBASIS.sol`*
  *Inherits: mToken*

- **mBTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mBTC/mBTC.sol`*
  *Inherits: mToken*

- **TACmBTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mBTC/tac/TACmBTC.sol`*
  *Inherits: mToken*

- **mEDGE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mEDGE/mEDGE.sol`*
  *Inherits: mToken*

- **TACmEDGE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mEDGE/tac/TACmEDGE.sol`*
  *Inherits: mToken*

- **mEVUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mEVUSD/mEVUSD.sol`*
  *Inherits: mToken*

- **mFARM** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mFARM/mFARM.sol`*
  *Inherits: mToken*

- **mFONE** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mFONE/mFONE.sol`*
  *Inherits: mToken*

- **mHYPER** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mHYPER/mHYPER.sol`*
  *Inherits: mToken*

- **mHyperBTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mHyperBTC/mHyperBTC.sol`*
  *Inherits: mToken*

- **mHyperETH** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mHyperETH/mHyperETH.sol`*
  *Inherits: mToken*

- **mKRalpha** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mKRalpha/mKRalpha.sol`*
  *Inherits: mToken*

- **mLIQUIDITY** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mLIQUIDITY/mLIQUIDITY.sol`*
  *Inherits: mToken*

- **mM1USD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mM1USD/mM1USD.sol`*
  *Inherits: mToken*

- **mMEV** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mMEV/mMEV.sol`*
  *Inherits: mToken*

- **TACmMEV** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mMEV/tac/TACmMEV.sol`*
  *Inherits: mToken*

- **mPortofino** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mPortofino/mPortofino.sol`*
  *Inherits: mToken*

- **mRE7** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mRE7/mRE7.sol`*
  *Inherits: mToken*

- **mRE7BTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mRE7BTC/mRE7BTC.sol`*
  *Inherits: mToken*

- **mRE7SOL** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mRE7SOL/mRE7SOL.sol`*
  *Inherits: mToken*

- **mROX** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mROX/mROX.sol`*
  *Inherits: mToken*

- **mSL** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mSL/mSL.sol`*
  *Inherits: mToken*

- **mTBILL** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mTBILL/mTBILL.sol`*
  *Inherits: mToken*

- **mTU** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mTU/mTU.sol`*
  *Inherits: mToken*

- **mWildUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mWildUSD/mWildUSD.sol`*
  *Inherits: mToken*

- **mXRP** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mXRP/mXRP.sol`*
  *Inherits: mToken*

- **mevBTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/mevBTC/mevBTC.sol`*
  *Inherits: mToken*

- **msyrupUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/msyrupUSD/msyrupUSD.sol`*
  *Inherits: mToken*

- **msyrupUSDp** – Auxiliary contract implementing various operations.
  *File: `contracts/products/msyrupUSDp/msyrupUSDp.sol`*
  *Inherits: mToken*

- **obeatUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/obeatUSD/obeatUSD.sol`*
  *Inherits: mToken*

- **plUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/plUSD/plUSD.sol`*
  *Inherits: mToken*

- **sLINJ** – Auxiliary contract implementing various operations.
  *File: `contracts/products/sLINJ/sLINJ.sol`*
  *Inherits: mToken*

- **splUSD** – Auxiliary contract implementing various operations.
  *File: `contracts/products/splUSD/splUSD.sol`*
  *Inherits: mToken*

- **tBTC** – Auxiliary contract implementing various operations.
  *File: `contracts/products/tBTC/tBTC.sol`*
  *Inherits: mToken*

- **tETH** – Auxiliary contract implementing various operations.
  *File: `contracts/products/tETH/tETH.sol`*
  *Inherits: mToken*

- **tUSDe** – Auxiliary contract implementing various operations.
  *File: `contracts/products/tUSDe/tUSDe.sol`*
  *Inherits: mToken*

- **tacTON** – Auxiliary contract implementing various operations.
  *File: `contracts/products/tacTON/tacTON.sol`*
  *Inherits: mToken*

- **wNLP** – Auxiliary contract implementing various operations.
  *File: `contracts/products/wNLP/wNLP.sol`*
  *Inherits: mToken*

- **wVLP** – Auxiliary contract implementing various operations.
  *File: `contracts/products/wVLP/wVLP.sol`*
  *Inherits: mToken*

- **weEUR** – Auxiliary contract implementing various operations.
  *File: `contracts/products/weEUR/weEUR.sol`*
  *Inherits: mToken*

- **zeroGBTCV** – Auxiliary contract implementing various operations.
  *File: `contracts/products/zeroGBTCV/zeroGBTCV.sol`*
  *Inherits: mToken*

- **zeroGETHV** – Auxiliary contract implementing various operations.
  *File: `contracts/products/zeroGETHV/zeroGETHV.sol`*
  *Inherits: mToken*

- **zeroGUSDV** – Auxiliary contract implementing various operations.
  *File: `contracts/products/zeroGUSDV/zeroGUSDV.sol`*
  *Inherits: mToken*


---

## Relationships

**MidasLzMintBurnOFTAdapter** holds the privileged minter/burner role on Blacklistable, Greenlistable, mToken, creating and destroying supply in response to user actions.

**MidasAccessControl, MidasAccessControlRoles, Pausable, WithMidasAccessControl … (+130 more)** enforces permissioned access across all protocol components — only approved operators and minters may trigger privileged functions.
