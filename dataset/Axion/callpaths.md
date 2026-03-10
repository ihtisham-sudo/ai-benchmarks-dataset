# Callpaths — Axion

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## BoostStablecoin

_File: contracts/BoostStablecoin.sol_

### external initialize
_(no internal calls)_


### public mint
_(no internal calls)_


### public pause
_(no internal calls)_


### public unpause
_(no internal calls)_


---

## MasterAMO

_File: contracts/MasterAMO.sol_

### external addLiquidity
_(no internal calls)_


### public initialize
_(no internal calls)_


### external mintAndSellBoost
_(no internal calls)_


### external mintSellFarm
-> internal _mintSellFarm


### external pause
_(no internal calls)_


### external unfarmBuyBurn
_(no internal calls)_


### external unpause
_(no internal calls)_


### external withdrawERC20
_(no internal calls)_


---

## Minter

_File: contracts/Minter.sol_

### external initialize
_(no internal calls)_


### external mint
_(no internal calls)_


### external pause
_(no internal calls)_


### external protocolMint
_(no internal calls)_


### external setTokens
_(no internal calls)_


### external setTreasury
_(no internal calls)_


### external unpause
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


---

## V2AMO

_File: contracts/V2AMO.sol_

### external addLiquidity
-> internal _addLiquidity
  -> public boostPrice
  -> internal toBoostAmount
  -> internal balanceOfToken


### public boostPrice
_(no internal calls)_


### public getReserves
-> internal toBoostAmount


### external getReward
_(no internal calls)_


### public initialize
-> public setVault
-> public setTokenId
-> public setParams


### external mintAndSellBoost
-> internal _mintAndSellBoost
  -> external_callback ISolidlyRouter.route
  -> internal toUsdAmount
  -> internal balanceOfToken


### external mintSellFarm
-> internal _mintSellFarm
  -> public getReserves
    -> internal toBoostAmount
  -> internal _mintSellFarm
  -> internal toUsdAmount
  -> public boostPrice


### external pause
_(no internal calls)_


### public setParams
_(no internal calls)_


### public setTokenId
_(no internal calls)_


### public setVault
_(no internal calls)_


### external setWhitelistedTokens
_(no internal calls)_


### external unfarmBuyBurn
-> internal _unfarmBuyBurn
  -> public getReserves
    -> internal toBoostAmount
  -> internal _unfarmBuyBurn
  -> internal toUsdAmount
  -> public boostPrice


### external unpause
_(no internal calls)_


### external withdrawERC20
_(no internal calls)_


---

## V3AMO

_File: contracts/V3AMO.sol_

### external addLiquidity
-> internal _addLiquidity
  -> internal toBoostAmount
  -> internal sortAmounts


### public boostPrice
_(no internal calls)_


### public initialize
-> public setTickBounds
-> public setTargetSqrtPriceX96
-> public setParams


### external mintAndSellBoost
-> internal _mintAndSellBoost
  -> internal sortAmounts
  -> internal toBoostAmount


### external mintSellFarm
-> internal _mintSellFarm
  -> internal _mintSellFarm
  -> public boostPrice


### external pause
_(no internal calls)_


### public setParams
_(no internal calls)_


### public setTargetSqrtPriceX96
_(no internal calls)_


### public setTickBounds
_(no internal calls)_


### external unfarmBuyBurn
-> internal _unfarmBuyBurn
  -> internal toBoostAmount
  -> public boostPrice
  -> internal _unfarmBuyBurn


### external unpause
_(no internal calls)_


### external withdrawERC20
_(no internal calls)_

