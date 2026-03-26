# Dinari — Contract Catalogue

> 13 contract(s) identified across 6 primitive categories.

---

## Tokens

The protocol utilises the following token contracts for accounting purposes:

- **DShare** – ERC-20 token contract exposing `balancepershare`, `burn`, `burnfrom`, `isblacklisted`, `mint`.
  *File: `src/DShare.sol`*
  *Inherits: IDShare, ERC20Rebasing, ControlledUpgradeable*
  *Key functions: `balancepershare`, `burn`, `burnfrom`, `initialize`, `isblacklisted`, `mint`, `name`, `publicversion`, `setbalancepershare`, `setname`, `setsymbol`, `settransferrestrictor`, `symbol`, `transferrestrictor`, `version`*

- **DShareFactory** – ERC-20 token contract exposing `announceexistingdshare`, `createdshare`, `getdsharebeacon`, `getdshares`, `gettransferrestrictor`.
  *File: `src/DShareFactory.sol`*
  *Inherits: IDShareFactory, ControlledUpgradeable*
  *Key functions: `announceexistingdshare`, `createdshare`, `getdsharebeacon`, `getdshares`, `gettransferrestrictor`, `getwrappeddsharebeacon`, `initialize`, `initializev2`, `istokendshare`, `istokenwrappeddshare`, `publicversion`, `reinitialize`, `setnewtransferrestrictor`, `version`*

- **ERC20Rebasing** – ERC-20 token contract exposing `balanceof`, `balancepershare`, `balancetoshares`, `maxsupply`, `sharesof`.
  *File: `src/ERC20Rebasing.sol`*
  *Inherits: ERC20*
  *Key functions: `balanceof`, `balancepershare`, `balancetoshares`, `maxsupply`, `sharesof`, `sharestobalance`, `totalsupply`, `transfer`, `transferfrom`*

- **WrappedDShare** – ERC-20 token contract exposing `asset`, `isblacklisted`, `name`, `recover`, `setname`.
  *File: `src/WrappedDShare.sol`*
  *Inherits: ControlledUpgradeable, ERC4626, ReentrancyGuardUpgradeable*
  *Key functions: `asset`, `initialize`, `isblacklisted`, `name`, `publicversion`, `recover`, `setname`, `setsymbol`, `symbol`, `version`*


## Containers

The protocol stores assets in the following containers:

- **Vault** – Asset container that holds funds; exposes `reinitialize`, `rescueerc20`, `withdrawfunds`.
  *File: `src/orders/Vault.sol`*
  *Inherits: IVault, ControlledUpgradeable*
  *Key functions: `initialize`, `publicversion`, `reinitialize`, `rescueerc20`, `version`, `withdrawfunds`*


## Exchange

The protocol implements protocol operations as the following exchange contracts:

- **FulfillmentRouter** – Handles on-chain order flow through `cancelbuyorder`, `fillorder`, `reinitialize`.
  *File: `src/orders/FulfillmentRouter.sol`*
  *Inherits: ControlledUpgradeable, MulticallUpgradeable*
  *Key functions: `cancelbuyorder`, `fillorder`, `initialize`, `publicversion`, `reinitialize`, `version`*

- **OrderProcessor** – Handles on-chain order flow through `cancelorder`, `createorder`, `createorderstandardfees`, `createorderwithsignature`, `domain_separator`.
  *File: `src/orders/OrderProcessor.sol`*
  *Inherits: ControlledUpgradeable, EIP712Upgradeable, MulticallUpgradeable, SelfPermit, IOrderProcessor*
  *Key functions: `cancelorder`, `createorder`, `createorderstandardfees`, `createorderwithsignature`, `domain_separator`, `dsharefactory`, `fillorder`, `getfeesescrowed`, `getfeestaken`, `getorderstatus`, `getpaymenttokenconfig`, `getreceivedamount`, `getstandardfees`, `getunfilledamount`, `hashfeequote`, `hashorder`, `hashorderrequest`, `initialize`, `isoperator`, `istransferlocked`, `latestfillprice`, `orderdecimalreduction`, `orderspaused`, `publicversion`, `reinitialize`, `removepaymenttoken`, `requestcancel`, `setoperator`, `setorderdecimalreduction`, `setorderspaused`, `setpaymenttoken`, `settreasury`, `setvault`, `totalstandardfee`, `treasury`, `vault`, `version`*


## Oracle

The protocol uses the following oracle contracts to obtain external price data:

- **LatestPriceHelper** – Provides price data via `aggregatelatestpricefromprocessor`.
  *File: `src/orders/LatestPriceHelper.sol`*
  *Key functions: `aggregatelatestpricefromprocessor`*


## Access Control

The protocol manages permissions through the following access-control contracts:

- **TransferRestrictor** – Enforces access control; implements `reinitialize`, `requirenotrestricted`, `restrict`, `unrestrict`.
  *File: `src/TransferRestrictor.sol`*
  *Inherits: ControlledUpgradeable, ITransferRestrictor*
  *Key functions: `initialize`, `publicversion`, `reinitialize`, `requirenotrestricted`, `restrict`, `unrestrict`, `version`*

- **ControlledUpgradeable** – Enforces access control; implements various operations.
  *File: `src/deployment/ControlledUpgradeable.sol`*
  *Inherits: UUPSUpgradeable, AccessControlDefaultAdminRulesUpgradeable*
  *Key functions: `publicversion`, `version`*


## Other

The protocol includes the following auxiliary contracts:

- **Multicall3** – Auxiliary contract implementing `aggregate`, `aggregate3`, `aggregate3value`, `blockandaggregate`, `getbasefee`.
  *File: `src/common/Multicall3.sol`*
  *Key functions: `aggregate`, `aggregate3`, `aggregate3value`, `blockandaggregate`, `getbasefee`, `getblockhash`, `getblocknumber`, `getchainid`, `getcurrentblockcoinbase`, `getcurrentblockdifficulty`, `getcurrentblockgaslimit`, `getcurrentblocktimestamp`, `getethbalance`, `getlastblockhash`, `tryaggregate`, `tryblockandaggregate`*

- **SelfPermit** – Auxiliary contract implementing `selfpermit`.
  *File: `src/common/SelfPermit.sol`*
  *Key functions: `selfpermit`*

- **DividendDistribution** – Auxiliary contract implementing `createdistribution`, `distribute`, `reclaimdistribution`, `setmindistributiontime`.
  *File: `src/dividend/DividendDistribution.sol`*
  *Inherits: ControlledUpgradeable, IDividendDistributor*
  *Key functions: `createdistribution`, `distribute`, `initialize`, `publicversion`, `reclaimdistribution`, `setmindistributiontime`, `version`*


---

## Relationships

**FulfillmentRouter, OrderProcessor** interacts directly with token contracts (DShare, DShareFactory, ERC20Rebasing, WrappedDShare) to transfer and settle asset balances.

**FulfillmentRouter, OrderProcessor** routes payment funds through Vault, keeping collateral segregated from the routing logic.

**FulfillmentRouter, OrderProcessor** consults **LatestPriceHelper** to obtain the latest asset prices for order fulfilment and fee calculations.

**TransferRestrictor, ControlledUpgradeable** enforces permissioned access across all protocol components — only approved operators and minters may trigger privileged functions.
