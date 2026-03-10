# Callpaths — Amphor

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AmphorSyntheticVault

_File: src/AmphorSyntheticVault.sol_

### public asset
_(no internal calls)_


### external claimToken
_(no internal calls)_


### public convertToAssets
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public convertToShares
-> internal _convertToShares
  -> public totalAssets
    -> internal _totalAssets


### public decimals
_(no internal calls)_


### public deposit
-> public maxDeposit
-> public previewDeposit
  -> internal _convertToShares
    -> public totalAssets
      -> internal _totalAssets
-> internal _deposit
  -> library SafeERC20.safeTransferFrom


### public depositMinShares
-> public deposit
  -> public maxDeposit
  -> public previewDeposit
    -> internal _convertToShares
      -> public totalAssets
        -> internal _totalAssets
  -> internal _deposit
    -> library SafeERC20.safeTransferFrom


### external end
-> library SafeERC20.safeTransferFrom


### public maxDeposit
_(no internal calls)_


### public maxMint
_(no internal calls)_


### public maxRedeem
_(no internal calls)_


### public maxWithdraw
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public mint
-> public maxMint
-> public previewMint
  -> internal _convertToAssets
    -> public totalAssets
      -> internal _totalAssets
-> internal _deposit
  -> library SafeERC20.safeTransferFrom


### public mintMaxAssets
-> public mint
  -> public maxMint
  -> public previewMint
    -> internal _convertToAssets
      -> public totalAssets
        -> internal _totalAssets
  -> internal _deposit
    -> library SafeERC20.safeTransferFrom


### external pause
_(no internal calls)_


### public previewDeposit
-> internal _convertToShares
  -> public totalAssets
    -> internal _totalAssets


### public previewMint
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public previewRedeem
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public previewWithdraw
-> internal _convertToShares
  -> public totalAssets
    -> internal _totalAssets


### external redeem
-> public maxRedeem
-> public previewRedeem
  -> internal _convertToAssets
    -> public totalAssets
      -> internal _totalAssets
-> internal _withdraw
  -> library SafeERC20.safeTransfer


### external restruct
_(no internal calls)_


### external setFees
_(no internal calls)_


### external start
-> internal _totalAssets


### public totalAssets
-> internal _totalAssets


### external unpause
_(no internal calls)_


### external withdraw
-> public maxWithdraw
  -> internal _convertToAssets
    -> public totalAssets
      -> internal _totalAssets
-> public previewWithdraw
  -> internal _convertToShares
    -> public totalAssets
      -> internal _totalAssets
-> internal _withdraw
  -> library SafeERC20.safeTransfer


---

## AmphorSyntheticVaultWithPermit

_File: src/AmphorSyntheticVaultWithPermit.sol_

### public asset
_(no internal calls)_


### external claimToken
_(no internal calls)_


### public convertToAssets
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public convertToShares
-> internal _convertToShares
  -> public totalAssets
    -> internal _totalAssets


### public decimals
_(no internal calls)_


### public deposit
-> public maxDeposit
-> public previewDeposit
  -> internal _convertToShares
    -> public totalAssets
      -> internal _totalAssets
-> internal _deposit
  -> library SafeERC20.safeTransferFrom


### public depositMinShares
-> public deposit
  -> public maxDeposit
  -> public previewDeposit
    -> internal _convertToShares
      -> public totalAssets
        -> internal _totalAssets
  -> internal _deposit
    -> library SafeERC20.safeTransferFrom


### external depositWithPermit
-> internal execPermit
-> public deposit
  -> public maxDeposit
  -> public previewDeposit
    -> internal _convertToShares
      -> public totalAssets
        -> internal _totalAssets
  -> internal _deposit
    -> library SafeERC20.safeTransferFrom


### external depositWithPermitMinShares
-> internal execPermit
-> public depositMinShares
  -> public deposit
    -> public maxDeposit
    -> public previewDeposit
      -> internal _convertToShares
        -> public totalAssets
          -> internal _totalAssets
    -> internal _deposit
      -> library SafeERC20.safeTransferFrom


### external end
-> library SafeERC20.safeTransferFrom


### public maxDeposit
_(no internal calls)_


### public maxMint
_(no internal calls)_


### public maxRedeem
_(no internal calls)_


### public maxWithdraw
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public mint
-> public maxMint
-> public previewMint
  -> internal _convertToAssets
    -> public totalAssets
      -> internal _totalAssets
-> internal _deposit
  -> library SafeERC20.safeTransferFrom


### public mintMaxAssets
-> public mint
  -> public maxMint
  -> public previewMint
    -> internal _convertToAssets
      -> public totalAssets
        -> internal _totalAssets
  -> internal _deposit
    -> library SafeERC20.safeTransferFrom


### external mintWithPermit
-> internal execPermit
-> public mint
  -> public maxMint
  -> public previewMint
    -> internal _convertToAssets
      -> public totalAssets
        -> internal _totalAssets
  -> internal _deposit
    -> library SafeERC20.safeTransferFrom


### external mintWithPermitMaxAssets
-> internal execPermit
-> public mintMaxAssets
  -> public mint
    -> public maxMint
    -> public previewMint
      -> internal _convertToAssets
        -> public totalAssets
          -> internal _totalAssets
    -> internal _deposit
      -> library SafeERC20.safeTransferFrom


### external pause
_(no internal calls)_


### public previewDeposit
-> internal _convertToShares
  -> public totalAssets
    -> internal _totalAssets


### public previewMint
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public previewRedeem
-> internal _convertToAssets
  -> public totalAssets
    -> internal _totalAssets


### public previewWithdraw
-> internal _convertToShares
  -> public totalAssets
    -> internal _totalAssets


### external redeem
-> public maxRedeem
-> public previewRedeem
  -> internal _convertToAssets
    -> public totalAssets
      -> internal _totalAssets
-> internal _withdraw
  -> library SafeERC20.safeTransfer


### external restruct
_(no internal calls)_


### external setFees
_(no internal calls)_


### external start
-> internal _totalAssets


### public totalAssets
-> internal _totalAssets


### external unpause
_(no internal calls)_


### external withdraw
-> public maxWithdraw
  -> internal _convertToAssets
    -> public totalAssets
      -> internal _totalAssets
-> public previewWithdraw
  -> internal _convertToShares
    -> public totalAssets
      -> internal _totalAssets
-> internal _withdraw
  -> library SafeERC20.safeTransfer


---

## PermitERC20

_File: src/utils/PermitERC20.sol_

### external mint
_(no internal calls)_


---

## VaultZapper

_File: src/VaultZapper.sol_

### public approveTokenForRouter
_(no internal calls)_


### external pause
_(no internal calls)_


### public redeemAndZap
-> private _execute


### public redeemAndZapWithPermit
-> private _executePermit
-> public redeemAndZap
  -> private _execute


### public toggleRouterAuthorization
_(no internal calls)_


### public toggleVaultAuthorization
-> internal _approveVault


### external unpause
_(no internal calls)_


### public withdrawAndZap
-> private _execute


### public withdrawAndZapWithPermit
-> private _executePermit
-> public withdrawAndZap
  -> private _execute


### external withdrawNativeToken
_(no internal calls)_


### external withdrawToken
_(no internal calls)_


### public zapAndDeposit
-> private _transferTokenInAndApprove
-> private _execute
-> private _depositInVault


### public zapAndDepositWithPermit
-> private _executePermit
-> public zapAndDeposit
  -> private _transferTokenInAndApprove
  -> private _execute
  -> private _depositInVault

