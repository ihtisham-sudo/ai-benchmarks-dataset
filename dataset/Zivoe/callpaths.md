# Callpaths — Zivoe

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## OCC_Modular

_File: src/lockers/OCC/OCC_Modular.sol_

### external acceptOffer
_(no internal calls)_


### public amountOwed
_(no internal calls)_


### external applyCombine
_(no internal calls)_


### external applyConversionToAmortization
_(no internal calls)_


### external applyConversionToBullet
_(no internal calls)_


### external applyExtension
_(no internal calls)_


### external applyRefinance
_(no internal calls)_


### external approveCombine
_(no internal calls)_


### external approveConversionToAmortization
_(no internal calls)_


### external approveConversionToBullet
_(no internal calls)_


### external approveExtension
_(no internal calls)_


### external approveRefinance
_(no internal calls)_


### external callLoan
-> public amountOwed


### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external cancelOffer
_(no internal calls)_


### external createOffer
_(no internal calls)_


### external loanInfo
_(no internal calls)_


### external makePayment
-> public amountOwed


### external markDefault
_(no internal calls)_


### external markRepaid
_(no internal calls)_


### external processPayment
-> public amountOwed


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external resolveDefault
_(no internal calls)_


### external supplyInterest
_(no internal calls)_


### external unapproveCombine
_(no internal calls)_


### external unapproveConversionToAmortization
_(no internal calls)_


### external unapproveConversionToBullet
_(no internal calls)_


### external unapproveExtension
_(no internal calls)_


### external unapproveRefinance
_(no internal calls)_


### external updateOCTYDL
_(no internal calls)_


---

## OCC_Variable

_File: src/lockers/OCC/OCC_Variable.sol_

### external adjustLimit
_(no internal calls)_


### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external draw
_(no internal calls)_


### external pullFromLocker
_(no internal calls)_


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
_(no internal calls)_


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external repay
_(no internal calls)_


---

## OCE_ZVE

_File: src/lockers/OCE/OCE_ZVE.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### public decay
-> internal rmul
-> internal rpow


### external forwardEmissions
-> private _forwardEmissions
-> public decay
  -> internal rmul
  -> internal rpow


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external updateDistributionRatioBIPS
_(no internal calls)_


### external updateExponentialDecayPerSecond
_(no internal calls)_


---

## OCG_Defaults

_File: src/lockers/OCG/OCG_Defaults.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### public decreaseDefaults
_(no internal calls)_


### public increaseDefaults
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCG_ERC1155

_File: src/lockers/OCG/OCG_ERC1155.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCG_ERC20

_File: src/lockers/OCG/OCG_ERC20.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCG_ERC20_FreeClaim

_File: src/lockers/OCG/OCG_ERC20_FreeClaim.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external claim
_(no internal calls)_


### external forward
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCG_ERC721

_File: src/lockers/OCG/OCG_ERC721.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCL_ZVE

_File: src/lockers/OCL/OCL_ZVE.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### public fetchBasis
_(no internal calls)_


### external forwardYield
-> public fetchBasis
-> private _forwardYield


### external pullFromLocker
_(no internal calls)_


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public fetchBasis


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public fetchBasis


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external updateCompoundingRateBIPS
_(no internal calls)_


### external updateOCTYDL
_(no internal calls)_


---

## OCR_Instant

_File: src/lockers/OCR/OCR_Instant.sol_

### external calculateRedemptionAmount
_(no internal calls)_


### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external pullFromLocker
_(no internal calls)_


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
_(no internal calls)_


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external redeemUSDC
_(no internal calls)_


### external updateRedemptionFeeBIPS
_(no internal calls)_


---

## OCR_Modular

_File: src/lockers/OCR/OCR_Modular.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external createRequest
_(no internal calls)_


### external destroyRequest
_(no internal calls)_


### external processRequest
_(no internal calls)_


### external pullFromLocker
_(no internal calls)_


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
_(no internal calls)_


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### public tickEpoch
_(no internal calls)_


### external updateRedemptionsFeeBIPS
_(no internal calls)_


---

## OCT_Convert

_File: src/lockers/OCT/OCT_Convert.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external convertTranche
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external updateWhitelist
_(no internal calls)_


### external updateWithdrawlist
_(no internal calls)_


### external withdrawTranche
_(no internal calls)_


---

## OCT_DAO

_File: src/lockers/OCT/OCT_DAO.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external convertAndForward
-> internal convertAsset
  -> internal handle_validation_12aa3caf
  -> internal handle_validation_e449022e
  -> internal handle_validation_0502b1c5
  -> internal handle_validation_3eca9c0a


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCT_YDL

_File: src/lockers/OCT/OCT_YDL.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external convertAndForward
-> internal convertAsset
  -> internal handle_validation_12aa3caf
  -> internal handle_validation_e449022e
  -> internal handle_validation_0502b1c5
  -> internal handle_validation_3eca9c0a


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCT_ZVL

_File: src/lockers/OCT/OCT_ZVL.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external claim
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


---

## OCY_Convex_A

_File: src/lockers/OCY/OCY_Convex_A.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### public claimRewards
_(no internal calls)_


### external pullFromLocker
-> public claimRewards


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public claimRewards


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external updateOCTYDL
_(no internal calls)_


---

## OCY_Convex_B

_File: src/lockers/OCY/OCY_Convex_B.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### public claimRewards
_(no internal calls)_


### external pullFromLocker
-> public claimRewards


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public claimRewards


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external updateOCTYDL
_(no internal calls)_


---

## OCY_Convex_C

_File: src/lockers/OCY/OCY_Convex_C.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### public claimRewards
_(no internal calls)_


### external pullFromLocker
-> public claimRewards


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public claimRewards


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### external updateOCTYDL
_(no internal calls)_


---

## OCY_OUSD

_File: src/lockers/OCY/OCY_OUSD.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### public forwardYield
_(no internal calls)_


### external pullFromLocker
-> public forwardYield


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public forwardYield


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### public rebase
_(no internal calls)_


### external updateOCTYDL
_(no internal calls)_


---

## OwnableLocked

_File: src/libraries/OwnableLocked.sol_

### public renounceOwnership
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public transferOwnershipAndLock
_(no internal calls)_


---

## Presale

_File: src/misc/Presale.sol_

### public depositETH
-> public pointsAwardedETH
  -> public oraclePrice


### public depositStablecoin
-> public standardize
-> public pointsAwardedStablecoin
  -> public standardize


### public oraclePrice
_(no internal calls)_


### public pointsAwardedETH
-> public oraclePrice


### public pointsAwardedStablecoin
-> public standardize


### public renounceOwnership
_(no internal calls)_


### public standardize
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public transferOwnershipAndLock
_(no internal calls)_


---

## ZivoeDAO

_File: src/ZivoeDAO.sol_

### external pull
_(no internal calls)_


### external pullERC1155
_(no internal calls)_


### external pullERC721
_(no internal calls)_


### external pullMulti
_(no internal calls)_


### external pullMultiERC721
_(no internal calls)_


### external pullMultiPartial
_(no internal calls)_


### external pullPartial
_(no internal calls)_


### external push
_(no internal calls)_


### external pushERC1155
_(no internal calls)_


### external pushERC721
_(no internal calls)_


### external pushMulti
_(no internal calls)_


### external pushMultiERC721
_(no internal calls)_


### public renounceOwnership
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public transferOwnershipAndLock
_(no internal calls)_


---

## ZivoeGTC

_File: src/libraries/ZivoeGTC.sol_

### public proposalEta
_(no internal calls)_


### public queue
-> public state


### public state
_(no internal calls)_


### public supportsInterface
_(no internal calls)_


### public timelock
_(no internal calls)_


---

## ZivoeGlobals

_File: src/ZivoeGlobals.sol_

### external acceptZVL
_(no internal calls)_


### external adjustedSupplies
_(no internal calls)_


### external decreaseDefaults
_(no internal calls)_


### external increaseDefaults
_(no internal calls)_


### external initializeGlobals
_(no internal calls)_


### external proposeZVL
_(no internal calls)_


### external standardize
_(no internal calls)_


### external updateIsDepositor
_(no internal calls)_


### external updateIsKeeper
_(no internal calls)_


### external updateIsLocker
_(no internal calls)_


### external updateStablecoinWhitelist
_(no internal calls)_


### external updateYDL
_(no internal calls)_


---

## ZivoeGovernorV2

_File: src/ZivoeGovernorV2.sol_

### public proposalEta
_(no internal calls)_


### public proposalThreshold
_(no internal calls)_


### public queue
-> public state
  -> external_callback ZivoeGTC.state


### public setProposalThreshold
_(no internal calls)_


### public setVotingDelay
_(no internal calls)_


### public setVotingPeriod
_(no internal calls)_


### public state
-> external_callback ZivoeGTC.state


### public supportsInterface
-> external_callback ZivoeGTC.supportsInterface


### public timelock
_(no internal calls)_


### public updateQuorumNumerator
_(no internal calls)_


---

## ZivoeITO

_File: src/ZivoeITO.sol_

### external claimAirdrop
_(no internal calls)_


### external commence
_(no internal calls)_


### external depositBoth
-> public depositSenior
-> public depositJunior
  -> public isJuniorOpen


### public depositJunior
-> public isJuniorOpen


### public depositSenior
_(no internal calls)_


### public isJuniorOpen
_(no internal calls)_


### external migrateDeposits
_(no internal calls)_


---

## ZivoeLocker

_File: src/ZivoeLocker.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
-> public canPush


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### public renounceOwnership
_(no internal calls)_


### public transferOwnership
_(no internal calls)_


### public transferOwnershipAndLock
_(no internal calls)_


---

## ZivoeMath

_File: src/ZivoeMath.sol_

### external ema
_(no internal calls)_


### external juniorProportion
_(no internal calls)_


### external seniorProportion
-> public seniorProportionShortfall
-> public seniorProportionBase


### public seniorProportionBase
_(no internal calls)_


### public seniorProportionShortfall
_(no internal calls)_


### public yieldTarget
_(no internal calls)_


---

## ZivoeRewards

_File: src/ZivoeRewards.sol_

### external addReward
_(no internal calls)_


### external balanceOf
_(no internal calls)_


### public checkpoints
_(no internal calls)_


### external depositReward
_(no internal calls)_


### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable


### external fullWithdraw
-> public withdraw
  -> internal _writeCheckpoint
    -> private _unsafeAccess
-> public getRewards
  -> internal _getRewardAt


### public getPastTotalSupply
-> private _checkpointsLookup
  -> private _unsafeAccess


### public getPastVotes
-> private _checkpointsLookup
  -> private _unsafeAccess


### external getRewardForDuration
_(no internal calls)_


### public getRewards
-> internal _getRewardAt


### public getVotes
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### public numCheckpoints
_(no internal calls)_


### public rewardPerToken
-> public lastTimeRewardApplicable


### external stake
-> internal _writeCheckpoint
  -> private _unsafeAccess


### external stakeFor
-> internal _writeCheckpoint
  -> private _unsafeAccess


### external totalSupply
_(no internal calls)_


### external viewAccountRewardPerTokenPaid
_(no internal calls)_


### external viewRewards
_(no internal calls)_


### public withdraw
-> internal _writeCheckpoint
  -> private _unsafeAccess


---

## ZivoeRewardsVesting

_File: src/ZivoeRewardsVesting.sol_

### external addReward
_(no internal calls)_


### public amountWithdrawable
_(no internal calls)_


### external balanceOf
_(no internal calls)_


### public checkpoints
_(no internal calls)_


### external createVestingSchedule
-> private _stake
  -> internal _writeCheckpoint
    -> private _unsafeAccess


### external depositReward
_(no internal calls)_


### public earned
-> public rewardPerToken
  -> public lastTimeRewardApplicable


### external fullWithdraw
-> public withdraw
  -> public amountWithdrawable
  -> internal _writeCheckpoint
    -> private _unsafeAccess
-> public getRewards
  -> internal _getRewardAt


### public getPastTotalSupply
-> private _checkpointsLookup
  -> private _unsafeAccess


### public getPastVotes
-> private _checkpointsLookup
  -> private _unsafeAccess


### external getRewardForDuration
_(no internal calls)_


### public getRewards
-> internal _getRewardAt


### public getVotes
_(no internal calls)_


### public lastTimeRewardApplicable
_(no internal calls)_


### public numCheckpoints
_(no internal calls)_


### external revokeVestingSchedule
-> public amountWithdrawable
-> internal _writeCheckpoint
  -> private _unsafeAccess


### public rewardPerToken
-> public lastTimeRewardApplicable


### external totalSupply
_(no internal calls)_


### external viewAccountRewardPerTokenPaid
_(no internal calls)_


### external viewRewards
_(no internal calls)_


### external viewSchedule
_(no internal calls)_


### public withdraw
-> public amountWithdrawable
-> internal _writeCheckpoint
  -> private _unsafeAccess


---

## ZivoeTLC

_File: src/libraries/ZivoeTLC.sol_

### public cancel
-> public isOperationPending
  -> public getTimestamp


### public execute
-> public hashOperation
-> private _beforeCallKeeper
  -> public isOperationReadyKeeper
    -> public getTimestamp
  -> public isOperationDone
    -> public getTimestamp
-> internal _execute
-> private _afterCallKeeper
  -> public isOperationReadyKeeper
    -> public getTimestamp
-> private _beforeCall
  -> public isOperationReady
    -> public getTimestamp
  -> public isOperationDone
    -> public getTimestamp
-> private _afterCall
  -> public isOperationReady
    -> public getTimestamp


### public executeBatch
-> public hashOperationBatch
-> private _beforeCallKeeper
  -> public isOperationReadyKeeper
    -> public getTimestamp
  -> public isOperationDone
    -> public getTimestamp
-> internal _execute
-> private _afterCallKeeper
  -> public isOperationReadyKeeper
    -> public getTimestamp
-> private _beforeCall
  -> public isOperationReady
    -> public getTimestamp
  -> public isOperationDone
    -> public getTimestamp
-> private _afterCall
  -> public isOperationReady
    -> public getTimestamp


### public getMinDelay
_(no internal calls)_


### public getTimestamp
_(no internal calls)_


### public hashOperation
_(no internal calls)_


### public hashOperationBatch
_(no internal calls)_


### public isOperation
-> public getTimestamp


### public isOperationDone
-> public getTimestamp


### public isOperationPending
-> public getTimestamp


### public isOperationReady
-> public getTimestamp


### public isOperationReadyKeeper
-> public getTimestamp


### public onERC1155BatchReceived
_(no internal calls)_


### public onERC1155Received
_(no internal calls)_


### public onERC721Received
_(no internal calls)_


### public schedule
-> public hashOperation
-> private _schedule
  -> public isOperation
    -> public getTimestamp
  -> public getMinDelay


### public scheduleBatch
-> public hashOperationBatch
-> private _schedule
  -> public isOperation
    -> public getTimestamp
  -> public getMinDelay


### public supportsInterface
_(no internal calls)_


### external updateDelay
_(no internal calls)_


---

## ZivoeToken

_File: src/ZivoeToken.sol_

### external burn
_(no internal calls)_


---

## ZivoeTrancheToken

_File: src/ZivoeTrancheToken.sol_

### external burn
_(no internal calls)_


### external changeMinterRole
_(no internal calls)_


### external isMinter
_(no internal calls)_


### external mint
_(no internal calls)_


---

## ZivoeTranches

_File: src/ZivoeTranches.sol_

### public canPull
_(no internal calls)_


### public canPullERC1155
_(no internal calls)_


### public canPullERC721
_(no internal calls)_


### public canPullMulti
_(no internal calls)_


### public canPullMultiERC721
_(no internal calls)_


### public canPullMultiPartial
_(no internal calls)_


### public canPullPartial
_(no internal calls)_


### public canPush
_(no internal calls)_


### public canPushERC1155
_(no internal calls)_


### public canPushERC721
_(no internal calls)_


### public canPushMulti
_(no internal calls)_


### public canPushMultiERC721
_(no internal calls)_


### external depositBoth
-> public depositSenior
  -> public rewardZVESeniorDeposit
-> public depositJunior
  -> public isJuniorOpen
  -> public rewardZVEJuniorDeposit


### external depositBothInverse
-> public depositJunior
  -> public isJuniorOpen
  -> public rewardZVEJuniorDeposit
-> public depositSenior
  -> public rewardZVESeniorDeposit


### public depositJunior
-> public isJuniorOpen
-> public rewardZVEJuniorDeposit


### public depositSenior
-> public rewardZVESeniorDeposit


### public isJuniorOpen
_(no internal calls)_


### external pullFromLocker
-> public canPull


### external pullFromLockerERC1155
-> public canPullERC1155


### external pullFromLockerERC721
-> public canPullERC721


### external pullFromLockerMulti
-> public canPullMulti


### external pullFromLockerMultiERC721
-> public canPullMultiERC721


### external pullFromLockerMultiPartial
-> public canPullMultiPartial


### external pullFromLockerPartial
-> public canPullPartial


### external pushToLocker
_(no internal calls)_


### external pushToLockerERC1155
-> public canPushERC1155


### external pushToLockerERC721
-> public canPushERC721


### external pushToLockerMulti
-> public canPushMulti


### external pushToLockerMultiERC721
-> public canPushMultiERC721


### public rewardZVEJuniorDeposit
_(no internal calls)_


### public rewardZVESeniorDeposit
_(no internal calls)_


### external switchPause
_(no internal calls)_


### external unlock
_(no internal calls)_


### external updateLowerRatioIncentiveBIPS
_(no internal calls)_


### external updateMaxTrancheRatio
_(no internal calls)_


### external updateMaxZVEPerJTTMint
_(no internal calls)_


### external updateMinZVEPerJTTMint
_(no internal calls)_


### external updateUpperRatioIncentiveBIPS
_(no internal calls)_


---

## ZivoeVotes

_File: src/libraries/ZivoeVotes.sol_

### public checkpoints
_(no internal calls)_


### public getPastTotalSupply
-> private _checkpointsLookup
  -> private _unsafeAccess


### public getPastVotes
-> private _checkpointsLookup
  -> private _unsafeAccess


### public getVotes
_(no internal calls)_


### public numCheckpoints
_(no internal calls)_


---

## ZivoeYDL

_File: src/ZivoeYDL.sol_

### external distributeYield
-> public earningsTrancheuse


### public earningsTrancheuse
_(no internal calls)_


### external returnAsset
_(no internal calls)_


### external unlock
_(no internal calls)_


### external updateDistributedAsset
_(no internal calls)_


### external updateProtocolEarningsRateBIPS
_(no internal calls)_


### external updateRecipients
_(no internal calls)_


### external updateTargetAPYBIPS
_(no internal calls)_


### external updateTargetRatioBIPS
_(no internal calls)_


### external viewDistributions
_(no internal calls)_

