# Callpaths — Bima

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## AdminVoting

_File: dao/AdminVoting.sol_

### external acceptTransferOwnership
_(no internal calls)_


### external cancelProposal
-> internal _containsSetGuardianPayload


### external createNewProposal
-> public getWeek
-> internal _minCreateProposalWeight
-> internal _containsSetGuardianPayload
-> library BimaMath._max


### external executeProposal
_(no internal calls)_


### external getProposalCanExecute
_(no internal calls)_


### external getProposalCanExecuteAfter
_(no internal calls)_


### external getProposalCount
_(no internal calls)_


### external getProposalCreatedAt
_(no internal calls)_


### external getProposalCurrentWeight
_(no internal calls)_


### external getProposalData
_(no internal calls)_


### external getProposalPassed
_(no internal calls)_


### external getProposalPayload
_(no internal calls)_


### external getProposalProcessed
_(no internal calls)_


### external getProposalRequiredWeight
_(no internal calls)_


### external getProposalWeek
_(no internal calls)_


### public getWeek
_(no internal calls)_


### external minCreateProposalWeight
-> public getWeek
-> internal _minCreateProposalWeight


### external setDelegateApproval
_(no internal calls)_


### external setMinCreateProposalPct
_(no internal calls)_


### external setPassingPct
_(no internal calls)_


### external voteForProposal
_(no internal calls)_


---

## AirdropDistributor

_File: dao/AirdropDistributor.sol_

### external claim
-> public isClaimed
-> private _setClaimed


### public isClaimed
_(no internal calls)_


### external setClaimCallback
_(no internal calls)_


### public setMerkleRoot
_(no internal calls)_


### external sweepUnclaimedTokens
_(no internal calls)_


---

## AllocationVesting

_File: dao/AllocationVesting.sol_

### external claim
-> private _claim
  -> private _claimableAt
    -> private _vestedAt


### external claimableNow
-> private _claimableAt
  -> private _vestedAt


### external getClaimed
_(no internal calls)_


### external lockFutureClaims
-> public lockFutureClaimsWithReceiver
  -> private _claimableAt
    -> private _vestedAt
  -> private _claim
    -> private _claimableAt
      -> private _vestedAt


### public lockFutureClaimsWithReceiver
-> private _claimableAt
  -> private _vestedAt
-> private _claim
  -> private _claimableAt
    -> private _vestedAt


### external preclaimable
_(no internal calls)_


### external setAllocations
_(no internal calls)_


### external setDelegateApproval
_(no internal calls)_


### external transferPoints
-> private _vestedAt
-> private _claim
  -> private _claimableAt
    -> private _vestedAt


### external unclaimed
_(no internal calls)_


---

## BimaCore

_File: core/BimaCore.sol_

### external acceptTransferOwnership
_(no internal calls)_


### external commitTransferOwnership
_(no internal calls)_


### external revokeTransferOwnership
_(no internal calls)_


### external setFeeReceiver
_(no internal calls)_


### external setGuardian
_(no internal calls)_


### external setPaused
_(no internal calls)_


### external setPriceFeed
_(no internal calls)_


---

## BimaOwnable

_File: dependencies/BimaOwnable.sol_

### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


---

## BimaPSM

_File: BimaPSM.sol_

### external getUnderlyingLiquidity
_(no internal calls)_


### external getUsbdLiquidity
_(no internal calls)_


### public guardian
_(no internal calls)_


### external mint
-> internal _underlyingToUsbd


### public owner
_(no internal calls)_


### external redeem
-> internal _underlyingToUsbd


### external removeLiquidity
_(no internal calls)_


### external underlyingToUsbd
-> internal _underlyingToUsbd


### external usbdToUnderlying
_(no internal calls)_


---

## BimaToken

_File: dao/BimaToken.sol_

### public domainSeparator
-> private _buildDomainSeparator


### external mintToVault
_(no internal calls)_


### external nonces
_(no internal calls)_


### external permit
-> public domainSeparator
  -> private _buildDomainSeparator


### external transferToLocker
_(no internal calls)_


---

## BimaVault

_File: dao/Vault.sol_

### external allocateNewEmissions
-> public getWeek
-> internal _allocateTotalWeekly


### external batchClaimRewards
-> internal _transferAllocated
  -> public getWeek
  -> internal _transferOrLock


### external claimBoostDelegationFees
-> internal _transferOrLock


### external claimableBoostDelegationFees
_(no internal calls)_


### external claimableRewardAfterBoost
-> public getWeek


### external getAccountWeeklyEarned
_(no internal calls)_


### external getClaimableWithBoost
-> public getWeek


### external getStoredPendingReward
_(no internal calls)_


### public getWeek
_(no internal calls)_


### public guardian
_(no internal calls)_


### external increaseUnallocatedSupply
_(no internal calls)_


### external isBoostDelegatedEnabled
_(no internal calls)_


### external isReceiverActive
_(no internal calls)_


### public owner
_(no internal calls)_


### external registerReceiver
-> public getWeek


### external setBoostCalculator
_(no internal calls)_


### external setBoostDelegationParams
_(no internal calls)_


### external setEmissionSchedule
-> internal _allocateTotalWeekly
-> public getWeek


### external setInitialParameters
-> public getWeek


### external setReceiverIsActive
_(no internal calls)_


### external transferAllocatedTokens
-> internal _transferAllocated
  -> public getWeek
  -> internal _transferOrLock


### external transferTokens
_(no internal calls)_


---

## BimaWrappedCollateral

_File: wrappers/BimaWrappedCollateral.sol_

### public previewUnwrappedAmount
_(no internal calls)_


### public previewWrappedAmount
_(no internal calls)_


### external unwrap
-> public previewUnwrappedAmount


### external wrap
-> public previewWrappedAmount


---

## BimaWrappedCollateralFactory

_File: wrappers/BimaWrappedCollateralFactory.sol_

### external createWrapper
_(no internal calls)_


### external getColl
_(no internal calls)_


### external getWrappedColl
_(no internal calls)_


### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


---

## BoostCalculator

_File: dao/BoostCalculator.sol_

### external getBoostedAmount
-> public getWeek
-> internal _getBoostedAmount


### external getBoostedAmountWrite
-> public getWeek
-> internal _getBoostedAmount


### external getClaimableWithBoost
-> public getWeek


### public getWeek
_(no internal calls)_


---

## BorrowerOperations

_File: core/BorrowerOperations.sol_

### external addColl
-> internal _adjustTrove
  -> internal _getCollateralAndTCRData
    -> public fetchBalances
    -> internal _getTCRData
      -> library BimaMath._computeCR
    -> public checkRecoveryMode
  -> internal _getCollChange
  -> internal _requireValidMaxFeePercentage
  -> internal _triggerBorrowingFee
    -> internal _requireUserAcceptsFee
  -> internal _requireValidAdjustmentInCurrentMode
    -> library BimaMath._computeCR
    -> internal _getNewICRFromTroveChange
      -> internal _getNewTroveAmounts
      -> library BimaMath._computeCR
    -> internal _requireICRisAboveCCR
    -> internal _requireNewICRisAboveOldICR
    -> internal _requireICRisAboveMCR
    -> internal _getNewTCRFromTroveChange
      -> library BimaMath._computeCR
    -> internal _requireNewTCRisAboveCCR
  -> internal _requireAtLeastMinNetDebt
  -> internal _getNetDebt


### external adjustTrove
-> internal _adjustTrove
  -> internal _getCollateralAndTCRData
    -> public fetchBalances
    -> internal _getTCRData
      -> library BimaMath._computeCR
    -> public checkRecoveryMode
  -> internal _getCollChange
  -> internal _requireValidMaxFeePercentage
  -> internal _triggerBorrowingFee
    -> internal _requireUserAcceptsFee
  -> internal _requireValidAdjustmentInCurrentMode
    -> library BimaMath._computeCR
    -> internal _getNewICRFromTroveChange
      -> internal _getNewTroveAmounts
      -> library BimaMath._computeCR
    -> internal _requireICRisAboveCCR
    -> internal _requireNewICRisAboveOldICR
    -> internal _requireICRisAboveMCR
    -> internal _getNewTCRFromTroveChange
      -> library BimaMath._computeCR
    -> internal _requireNewTCRisAboveCCR
  -> internal _requireAtLeastMinNetDebt
  -> internal _getNetDebt


### public checkRecoveryMode
_(no internal calls)_


### external closeTrove
-> internal _getCollateralAndTCRData
  -> public fetchBalances
  -> internal _getTCRData
    -> library BimaMath._computeCR
  -> public checkRecoveryMode
-> internal _getNewTCRFromTroveChange
  -> library BimaMath._computeCR
-> internal _requireNewTCRisAboveCCR


### external configureCollateral
_(no internal calls)_


### public fetchBalances
_(no internal calls)_


### external getCompositeDebt
-> internal _getCompositeDebt


### external getGlobalSystemBalances
-> public fetchBalances
-> internal _getTCRData
  -> library BimaMath._computeCR


### external getTCR
-> public fetchBalances
-> internal _getTCRData
  -> library BimaMath._computeCR


### external getTroveManagersCount
_(no internal calls)_


### public guardian
_(no internal calls)_


### external openTrove
-> internal _requireValidMaxFeePercentage
-> internal _getCollateralAndTCRData
  -> public fetchBalances
  -> internal _getTCRData
    -> library BimaMath._computeCR
  -> public checkRecoveryMode
-> internal _triggerBorrowingFee
  -> internal _requireUserAcceptsFee
-> internal _requireAtLeastMinNetDebt
-> internal _getCompositeDebt
-> library BimaMath._computeCR
-> library BimaMath._computeNominalCR
-> internal _requireICRisAboveCCR
-> internal _requireICRisAboveMCR
-> internal _getNewTCRFromTroveChange
  -> library BimaMath._computeCR
-> internal _requireNewTCRisAboveCCR


### public owner
_(no internal calls)_


### external removeTroveManager
_(no internal calls)_


### external repayDebt
-> internal _adjustTrove
  -> internal _getCollateralAndTCRData
    -> public fetchBalances
    -> internal _getTCRData
      -> library BimaMath._computeCR
    -> public checkRecoveryMode
  -> internal _getCollChange
  -> internal _requireValidMaxFeePercentage
  -> internal _triggerBorrowingFee
    -> internal _requireUserAcceptsFee
  -> internal _requireValidAdjustmentInCurrentMode
    -> library BimaMath._computeCR
    -> internal _getNewICRFromTroveChange
      -> internal _getNewTroveAmounts
      -> library BimaMath._computeCR
    -> internal _requireICRisAboveCCR
    -> internal _requireNewICRisAboveOldICR
    -> internal _requireICRisAboveMCR
    -> internal _getNewTCRFromTroveChange
      -> library BimaMath._computeCR
    -> internal _requireNewTCRisAboveCCR
  -> internal _requireAtLeastMinNetDebt
  -> internal _getNetDebt


### external setDelegateApproval
_(no internal calls)_


### public setMinNetDebt
-> internal _setMinNetDebt


### external withdrawColl
-> internal _adjustTrove
  -> internal _getCollateralAndTCRData
    -> public fetchBalances
    -> internal _getTCRData
      -> library BimaMath._computeCR
    -> public checkRecoveryMode
  -> internal _getCollChange
  -> internal _requireValidMaxFeePercentage
  -> internal _triggerBorrowingFee
    -> internal _requireUserAcceptsFee
  -> internal _requireValidAdjustmentInCurrentMode
    -> library BimaMath._computeCR
    -> internal _getNewICRFromTroveChange
      -> internal _getNewTroveAmounts
      -> library BimaMath._computeCR
    -> internal _requireICRisAboveCCR
    -> internal _requireNewICRisAboveOldICR
    -> internal _requireICRisAboveMCR
    -> internal _getNewTCRFromTroveChange
      -> library BimaMath._computeCR
    -> internal _requireNewTCRisAboveCCR
  -> internal _requireAtLeastMinNetDebt
  -> internal _getNetDebt


### external withdrawDebt
-> internal _adjustTrove
  -> internal _getCollateralAndTCRData
    -> public fetchBalances
    -> internal _getTCRData
      -> library BimaMath._computeCR
    -> public checkRecoveryMode
  -> internal _getCollChange
  -> internal _requireValidMaxFeePercentage
  -> internal _triggerBorrowingFee
    -> internal _requireUserAcceptsFee
  -> internal _requireValidAdjustmentInCurrentMode
    -> library BimaMath._computeCR
    -> internal _getNewICRFromTroveChange
      -> internal _getNewTroveAmounts
      -> library BimaMath._computeCR
    -> internal _requireICRisAboveCCR
    -> internal _requireNewICRisAboveOldICR
    -> internal _requireICRisAboveMCR
    -> internal _getNewTCRFromTroveChange
      -> library BimaMath._computeCR
    -> internal _requireNewTCRisAboveCCR
  -> internal _requireAtLeastMinNetDebt
  -> internal _getNetDebt


---

## ConvexDepositToken

_File: staking/Convex/ConvexDepositToken.sol_

### public approve
_(no internal calls)_


### external claimReward
-> internal _claimReward
  -> internal _updateIntegrals


### external claimableReward
_(no internal calls)_


### external deposit
-> internal _updateIntegrals
-> internal _fetchRewards


### external fetchRewards
-> internal _updateIntegrals
-> internal _fetchRewards


### external initialize
_(no internal calls)_


### external notifyRegisteredId
_(no internal calls)_


### public transfer
-> internal _transfer
  -> internal _updateIntegrals


### public transferFrom
-> internal _transfer
  -> internal _updateIntegrals


### external vaultClaimReward
-> internal _claimReward
  -> internal _updateIntegrals


### external withdraw
-> internal _updateIntegrals
-> internal _fetchRewards


---

## ConvexFactory

_File: staking/Convex/ConvexDepositFactory.sol_

### external deployNewInstance
_(no internal calls)_


### external getDepositToken
-> library Clones.predictDeterministicAddress


### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


---

## CurveDepositToken

_File: staking/Curve/CurveDepositToken.sol_

### public approve
_(no internal calls)_


### external claimReward
-> internal _claimReward
  -> internal _updateIntegrals


### external claimableReward
_(no internal calls)_


### external deposit
-> internal _updateIntegrals
-> internal _fetchRewards


### external fetchRewards
-> internal _updateIntegrals
-> internal _fetchRewards


### external initialize
_(no internal calls)_


### external notifyRegisteredId
_(no internal calls)_


### public transfer
-> internal _transfer
  -> internal _updateIntegrals


### public transferFrom
-> internal _transfer
  -> internal _updateIntegrals


### external vaultClaimReward
-> internal _claimReward
  -> internal _updateIntegrals


### external withdraw
-> internal _updateIntegrals
-> internal _fetchRewards


---

## CurveFactory

_File: staking/Curve/CurveDepositFactory.sol_

### external deployNewInstance
_(no internal calls)_


### external getDepositToken
-> library Clones.predictDeterministicAddress


### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


---

## CurveProxy

_File: staking/Curve/CurveProxy.sol_

### external approveGaugeDeposit
_(no internal calls)_


### external claimFees
_(no internal calls)_


### external execute
-> public owner


### public guardian
_(no internal calls)_


### external lockCRV
-> internal _updateLock


### external mintCRV
-> internal _updateLock


### public owner
_(no internal calls)_


### external setCrvFeePct
_(no internal calls)_


### external setDepositManager
_(no internal calls)_


### external setExecutePermissions
_(no internal calls)_


### external setGaugeRewardsReceiver
_(no internal calls)_


### external setPerGaugeApproval
_(no internal calls)_


### external setVoteManager
_(no internal calls)_


### external transferTokens
_(no internal calls)_


### external voteForGaugeWeights
_(no internal calls)_


### external voteInCurveDao
_(no internal calls)_


### external withdrawFromGauge
_(no internal calls)_


---

## DebtToken

_File: core/DebtToken.sol_

### external authorizedMint
_(no internal calls)_


### external burn
_(no internal calls)_


### external burnWithGasCompensation
_(no internal calls)_


### public domainSeparator
-> private _buildDomainSeparator


### external enableTroveManager
_(no internal calls)_


### external flashFee
-> internal _flashFee


### external flashLoan
-> public maxFlashLoan
-> internal _flashFee


### public maxFlashLoan
_(no internal calls)_


### external mint
_(no internal calls)_


### external mintWithGasCompensation
_(no internal calls)_


### external nonces
_(no internal calls)_


### external permit
-> public domainSeparator
  -> private _buildDomainSeparator


### external returnFromPool
_(no internal calls)_


### external sendToSP
_(no internal calls)_


### external setLendingVaultAdapterAddress
_(no internal calls)_


### public transfer
-> internal _requireValidRecipient


### public transferFrom
-> internal _requireValidRecipient


---

## DelegatedOps

_File: dependencies/DelegatedOps.sol_

### external setDelegateApproval
_(no internal calls)_


---

## EmissionSchedule

_File: dao/EmissionSchedule.sol_

### external getReceiverWeeklyEmissions
_(no internal calls)_


### external getTotalWeeklyEmissions
_(no internal calls)_


### public getWeek
_(no internal calls)_


### external getWeeklyPctSchedule
_(no internal calls)_


### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


### external setLockParameters
_(no internal calls)_


### external setWeeklyPctSchedule
-> internal _setWeeklyPctSchedule
  -> public getWeek


---

## Factory

_File: core/Factory.sol_

### external deployNewInstance
_(no internal calls)_


### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


### external setImplementations
_(no internal calls)_


### external troveManagerCount
_(no internal calls)_


---

## FeeReceiver

_File: dao/FeeReceiver.sol_

### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


### external setTokenApproval
_(no internal calls)_


### external transferToken
_(no internal calls)_


---

## IncentiveVoting

_File: dao/IncentiveVoting.sol_

### external clearRegisteredWeight
-> public getWeek
-> internal _removeVoteWeights
  -> internal _removeVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _removeVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
-> public getAccountCurrentVotes


### external clearVote
-> internal _removeVoteWeights
  -> internal _removeVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _removeVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
-> public getAccountCurrentVotes
-> public getWeek


### public getAccountCurrentVotes
_(no internal calls)_


### external getAccountRegisteredLocks
-> internal _getAccountLocks
  -> public getWeek
  -> external_callback ITokenLocker.LockData


### external getReceiverVoteInputs
-> public getReceiverWeightWrite
  -> public getWeek
-> public getTotalWeightWrite
  -> public getWeek


### external getReceiverVotePct
-> public getReceiverWeightWrite
  -> public getWeek
-> public getTotalWeightWrite
  -> public getWeek


### external getReceiverWeight
-> public getReceiverWeightAt
-> public getWeek


### public getReceiverWeightAt
_(no internal calls)_


### public getReceiverWeightWrite
-> public getWeek


### external getTotalWeight
-> public getTotalWeightAt
-> public getWeek


### public getTotalWeightAt
_(no internal calls)_


### public getTotalWeightWrite
-> public getWeek


### public getWeek
_(no internal calls)_


### external registerAccountWeight
-> public getAccountCurrentVotes
-> internal _removeVoteWeights
  -> internal _removeVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _removeVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
-> public getWeek
-> internal _registerAccountWeight
  -> public getWeek
-> internal _addVoteWeights
  -> internal _addVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _addVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek


### external registerAccountWeightAndVote
-> internal _removeVoteWeights
  -> internal _removeVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _removeVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
-> public getAccountCurrentVotes
-> public getWeek
-> internal _registerAccountWeight
  -> public getWeek
-> internal _addVoteWeights
  -> internal _addVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _addVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
-> internal _storeAccountVotes
  -> public getWeek


### external registerNewReceiver
-> public getWeek


### external setDelegateApproval
_(no internal calls)_


### external unfreeze
-> public getWeek
-> public getAccountCurrentVotes
-> internal _removeVoteWeightsFrozen
  -> public getWeek
  -> public getReceiverWeightWrite
    -> public getWeek
  -> public getTotalWeightWrite
    -> public getWeek
-> internal _addVoteWeightsUnfrozen
  -> internal _getAccountLocks
    -> public getWeek
    -> external_callback ITokenLocker.LockData
  -> public getWeek
  -> public getReceiverWeightWrite
    -> public getWeek
  -> public getTotalWeightWrite
    -> public getWeek
-> external_callback ITokenLocker.LockData
-> internal _removeVoteWeights
  -> internal _removeVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _removeVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek


### external vote
-> internal _removeVoteWeights
  -> internal _removeVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _removeVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
-> public getAccountCurrentVotes
-> public getWeek
-> internal _addVoteWeights
  -> internal _addVoteWeightsFrozen
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
  -> internal _addVoteWeightsUnfrozen
    -> internal _getAccountLocks
      -> public getWeek
      -> external_callback ITokenLocker.LockData
    -> public getWeek
    -> public getReceiverWeightWrite
      -> public getWeek
    -> public getTotalWeightWrite
      -> public getWeek
-> internal _storeAccountVotes
  -> public getWeek


---

## InterimAdmin

_File: dao/InterimAdmin.sol_

### external acceptTransferOwnership
_(no internal calls)_


### external cancelProposal
_(no internal calls)_


### external createNewProposal
-> internal _isSetGuardianPayload


### external executeProposal
_(no internal calls)_


### external getProposalCanExecute
_(no internal calls)_


### external getProposalCanExecuteAfter
_(no internal calls)_


### external getProposalCount
_(no internal calls)_


### external getProposalCreatedAt
_(no internal calls)_


### external getProposalData
_(no internal calls)_


### external getProposalExecuted
_(no internal calls)_


### external getProposalPayload
_(no internal calls)_


### external setAdminVoting
_(no internal calls)_


### external transferOwnershipToAdminVoting
_(no internal calls)_


---

## LendingVaultAdapter

_File: adapters/LendingVaultAdapter.sol_

### public deposit
_(no internal calls)_


### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


### external recover
_(no internal calls)_


### public redeem
_(no internal calls)_


---

## LiquidationManager

_File: core/LiquidationManager.sol_

### public batchLiquidateTroves
-> internal _liquidateWithoutSP
  -> internal _getCollGasCompensation
-> internal _liquidateNormalMode
  -> internal _getCollGasCompensation
  -> internal _getOffsetAndRedistributionVals
    -> library BimaMath._min
-> internal _applyLiquidationValuesToTotals
-> library BimaMath._computeCR
-> internal _tryLiquidateWithCap
  -> internal _getCollGasCompensation


### external enableTroveManager
_(no internal calls)_


### external isTroveManagerEnabled
_(no internal calls)_


### external liquidate
-> public batchLiquidateTroves
  -> internal _liquidateWithoutSP
    -> internal _getCollGasCompensation
  -> internal _liquidateNormalMode
    -> internal _getCollGasCompensation
    -> internal _getOffsetAndRedistributionVals
      -> library BimaMath._min
  -> internal _applyLiquidationValuesToTotals
  -> library BimaMath._computeCR
  -> internal _tryLiquidateWithCap
    -> internal _getCollGasCompensation


### external liquidateTroves
-> internal _liquidateWithoutSP
  -> internal _getCollGasCompensation
-> internal _applyLiquidationValuesToTotals
-> internal _liquidateNormalMode
  -> internal _getCollGasCompensation
  -> internal _getOffsetAndRedistributionVals
    -> library BimaMath._min
-> library BimaMath._computeCR
-> internal _tryLiquidateWithCap
  -> internal _getCollGasCompensation


---

## MultiCollateralHintHelpers

_File: core/helpers/MultiCollateralHintHelpers.sol_

### external computeCR
-> library BimaMath._computeCR


### external computeNominalCR
-> library BimaMath._computeNominalCR


### external getApproxHint
-> library BimaMath._getAbsoluteDifference


### external getRedemptionHints
-> internal _getNetDebt
-> library BimaMath._min
-> internal _getCompositeDebt
-> library BimaMath._computeNominalCR


---

## MultiTroveGetter

_File: core/helpers/MultiTroveGetter.sol_

### external getMultipleSortedTroves
-> internal _getMultipleSortedTrovesFromHead
-> internal _getMultipleSortedTrovesFromTail


---

## PriceFeed

_File: core/PriceFeed.sol_

### public fetchPrice
-> internal _fetchFeedResponses
  -> internal _fetchCurrentFeedResponse
  -> internal _fetchPrevFeedResponse
-> internal _isPriceStale
-> internal _processFeedResponses
  -> internal _isFeedWorking
    -> internal _isValidResponse
  -> internal _isPriceStale
  -> internal _isPriceChangeAboveMaxDeviation
    -> internal _scalePriceByDigits
    -> library BimaMath._min
    -> library BimaMath._max
  -> internal _scalePriceByDigits
  -> internal _calcEthPrice
    -> public fetchPrice
  -> internal _updateFeedStatus
  -> internal _storePrice


### public guardian
_(no internal calls)_


### public owner
_(no internal calls)_


### public setOracle
-> internal _fetchFeedResponses
  -> internal _fetchCurrentFeedResponse
  -> internal _fetchPrevFeedResponse
-> internal _isFeedWorking
  -> internal _isValidResponse
-> internal _isPriceStale
-> internal _processFeedResponses
  -> internal _isFeedWorking
    -> internal _isValidResponse
  -> internal _isPriceStale
  -> internal _isPriceChangeAboveMaxDeviation
    -> internal _scalePriceByDigits
    -> library BimaMath._min
    -> library BimaMath._max
  -> internal _scalePriceByDigits
  -> internal _calcEthPrice
    -> public fetchPrice
      -> internal _fetchFeedResponses
        -> internal _fetchCurrentFeedResponse
        -> internal _fetchPrevFeedResponse
      -> internal _isPriceStale
      -> internal _processFeedResponses
  -> internal _updateFeedStatus
  -> internal _storePrice


---

## SortedTroves

_File: core/SortedTroves.sol_

### public contains
_(no internal calls)_


### external findInsertPosition
-> internal _findInsertPosition
  -> public contains
  -> internal _descendList
    -> internal _validInsertPosition
      -> public isEmpty
  -> internal _ascendList
    -> internal _validInsertPosition
      -> public isEmpty


### external getFirst
_(no internal calls)_


### external getLast
_(no internal calls)_


### external getNext
_(no internal calls)_


### external getPrev
_(no internal calls)_


### external getSize
_(no internal calls)_


### external insert
-> internal _requireCallerIsTroveManager
-> internal _insert
  -> internal _validInsertPosition
    -> public isEmpty
  -> internal _findInsertPosition
    -> public contains
    -> internal _descendList
      -> internal _validInsertPosition
        -> public isEmpty
    -> internal _ascendList
      -> internal _validInsertPosition
        -> public isEmpty


### public isEmpty
_(no internal calls)_


### external reInsert
-> internal _requireCallerIsTroveManager
-> internal _remove
-> internal _insert
  -> internal _validInsertPosition
    -> public isEmpty
  -> internal _findInsertPosition
    -> public contains
    -> internal _descendList
      -> internal _validInsertPosition
        -> public isEmpty
    -> internal _ascendList
      -> internal _validInsertPosition
        -> public isEmpty


### external remove
-> internal _requireCallerIsTroveManager
-> internal _remove


### external setAddresses
_(no internal calls)_


### external validInsertPosition
-> internal _validInsertPosition
  -> public isEmpty


---

## StabilityPool

_File: core/StabilityPool.sol_

### external claimCollateralGains
-> public claimReward
  -> internal _claimReward
    -> internal _triggerRewardIssuance
      -> internal _updateG
        -> internal _computeBimaPerUnitStaked
      -> internal _vestedEmissions
      -> public getWeek
    -> private _accrueDepositorCollateralGain
    -> public getCompoundedDebtDeposit
      -> internal _getCompoundedStakeFromSnapshots
    -> private _claimableReward
      -> internal _getBimaGainFromSnapshots
    -> internal _updateSnapshots


### public claimReward
-> internal _claimReward
  -> internal _triggerRewardIssuance
    -> internal _updateG
      -> internal _computeBimaPerUnitStaked
    -> internal _vestedEmissions
    -> public getWeek
  -> private _accrueDepositorCollateralGain
  -> public getCompoundedDebtDeposit
    -> internal _getCompoundedStakeFromSnapshots
  -> private _claimableReward
    -> internal _getBimaGainFromSnapshots
  -> internal _updateSnapshots


### external claimableReward
-> internal _vestedEmissions
-> private _claimableReward
  -> internal _getBimaGainFromSnapshots


### external enableCollateral
-> internal _overwriteCollateral


### public getCompoundedDebtDeposit
-> internal _getCompoundedStakeFromSnapshots


### external getDepositorCollateralGain
_(no internal calls)_


### external getNumCollateralTokens
_(no internal calls)_


### external getStoredPendingReward
_(no internal calls)_


### external getSunsetIndexes
_(no internal calls)_


### external getSunsetQueueKeys
_(no internal calls)_


### external getTotalDebtTokenDeposits
_(no internal calls)_


### public getWeek
_(no internal calls)_


### public guardian
_(no internal calls)_


### external offset
-> internal _offset
  -> internal _triggerRewardIssuance
    -> internal _updateG
      -> internal _computeBimaPerUnitStaked
    -> internal _vestedEmissions
    -> public getWeek
  -> internal _computeRewardsPerUnitStaked
  -> internal _updateRewardSumAndProduct
  -> internal _decreaseDebt


### public owner
_(no internal calls)_


### external provideToSP
-> internal _triggerRewardIssuance
  -> internal _updateG
    -> internal _computeBimaPerUnitStaked
  -> internal _vestedEmissions
  -> public getWeek
-> private _accrueDepositorCollateralGain
-> public getCompoundedDebtDeposit
  -> internal _getCompoundedStakeFromSnapshots
-> internal _accrueRewards
  -> private _claimableReward
    -> internal _getBimaGainFromSnapshots
-> internal _updateSnapshots


### external startCollateralSunset
_(no internal calls)_


### external vaultClaimReward
-> internal _claimReward
  -> internal _triggerRewardIssuance
    -> internal _updateG
      -> internal _computeBimaPerUnitStaked
    -> internal _vestedEmissions
    -> public getWeek
  -> private _accrueDepositorCollateralGain
  -> public getCompoundedDebtDeposit
    -> internal _getCompoundedStakeFromSnapshots
  -> private _claimableReward
    -> internal _getBimaGainFromSnapshots
  -> internal _updateSnapshots


### external withdrawFromSP
-> internal _triggerRewardIssuance
  -> internal _updateG
    -> internal _computeBimaPerUnitStaked
  -> internal _vestedEmissions
  -> public getWeek
-> private _accrueDepositorCollateralGain
-> public getCompoundedDebtDeposit
  -> internal _getCompoundedStakeFromSnapshots
-> library BimaMath._min
-> internal _accrueRewards
  -> private _claimableReward
    -> internal _getBimaGainFromSnapshots
-> internal _decreaseDebt
-> internal _updateSnapshots


---

## StorkOracleWrapper

_File: wrappers/StorkOracleWrapper.sol_

### external decimals
_(no internal calls)_


### external description
_(no internal calls)_


### external getRoundData
_(no internal calls)_


### external latestRoundData
_(no internal calls)_


### external version
_(no internal calls)_


---

## SystemStart

_File: dependencies/SystemStart.sol_

### public getWeek
_(no internal calls)_


---

## TokenLocker

_File: dao/TokenLocker.sol_

### external extendLock
-> public getWeek
-> internal _weeklyWeightWrite
  -> public getWeek
-> public getTotalWeightWrite
  -> public getWeek


### external extendMany
-> internal _weeklyWeightWrite
  -> public getWeek
-> public getWeek
-> public getTotalWeightWrite
  -> public getWeek


### external freeze
-> internal _weeklyWeightWrite
  -> public getWeek
-> public getTotalWeightWrite
  -> public getWeek
-> public getWeek


### external getAccountActiveLocks
-> public getWeek


### external getAccountBalances
-> public getWeek


### external getAccountBalancesRaw
_(no internal calls)_


### public getAccountWeeklyUnlocks
_(no internal calls)_


### external getAccountWeight
-> public getAccountWeightAt
  -> public getWeek
-> public getWeek


### public getAccountWeightAt
-> public getWeek


### external getAccountWeightWrite
-> internal _weeklyWeightWrite
  -> public getWeek


### public getTotalWeeklyUnlocks
_(no internal calls)_


### external getTotalWeight
-> public getTotalWeightAt
  -> public getWeek
-> public getWeek


### public getTotalWeightAt
-> public getWeek


### public getTotalWeightWrite
-> public getWeek


### public getWeek
_(no internal calls)_


### external getWithdrawWithPenaltyAmounts
-> public getWeek


### public guardian
_(no internal calls)_


### external lock
-> internal _lock
  -> internal _weeklyWeightWrite
    -> public getWeek
  -> public getTotalWeightWrite
    -> public getWeek
  -> public getWeek


### external lockMany
-> internal _weeklyWeightWrite
  -> public getWeek
-> public getWeek
-> public getTotalWeightWrite
  -> public getWeek


### public owner
_(no internal calls)_


### external setAllowPenaltyWithdrawAfter
_(no internal calls)_


### external setPenaltyWithdrawalsEnabled
_(no internal calls)_


### external unfreeze
-> internal _weeklyWeightWrite
  -> public getWeek
-> public getTotalWeightWrite
  -> public getWeek
-> public getWeek


### external withdrawExpiredLocks
-> internal _weeklyWeightWrite
  -> public getWeek
-> public getTotalWeightWrite
  -> public getWeek
-> internal _lock
  -> internal _weeklyWeightWrite
    -> public getWeek
  -> public getTotalWeightWrite
    -> public getWeek
  -> public getWeek


### external withdrawWithPenalty
-> internal _weeklyWeightWrite
  -> public getWeek
-> public getWeek
-> public getTotalWeightWrite
  -> public getWeek


---

## TroveManager

_File: core/TroveManager.sol_

### external addCollateralSurplus
-> internal _requireCallerIsLM


### external applyPendingRewards
-> internal _requireCallerIsBO
-> internal _applyPendingRewards
  -> internal _accrueActiveInterests
    -> internal _calculateInterestIndex
  -> public getPendingCollAndDebtRewards
  -> internal _updateTroveRewardSnapshots
  -> internal _movePendingTroveRewardsToActiveBalance
  -> internal _updateIntegrals
    -> internal _updateRewardIntegral
      -> internal _fetchRewards
        -> public getWeek
    -> internal _updateIntegralForAccount


### external claimCollateral
_(no internal calls)_


### external claimReward
-> internal _claimReward
  -> internal _applyPendingRewards
    -> internal _accrueActiveInterests
      -> internal _calculateInterestIndex
    -> public getPendingCollAndDebtRewards
    -> internal _updateTroveRewardSnapshots
    -> internal _movePendingTroveRewardsToActiveBalance
    -> internal _updateIntegrals
      -> internal _updateRewardIntegral
        -> internal _fetchRewards
          -> public getWeek
      -> internal _updateIntegralForAccount
  -> internal _getPendingMintReward
    -> public getWeekAndDay


### external claimableReward
-> internal _getPendingMintReward
  -> public getWeekAndDay


### external closeTrove
-> internal _requireCallerIsBO
-> internal _closeTrove
-> private _sendCollateral
-> private _resetState


### external closeTroveByLiquidation
-> internal _requireCallerIsLM
-> internal _closeTrove
-> internal _updateIntegralForAccount


### external collectInterests
_(no internal calls)_


### external decayBaseRateAndGetBorrowingFee
-> internal _requireCallerIsBO
-> internal _decayBaseRate
  -> internal _calcDecayedBaseRate
    -> library BimaMath._decPow
  -> internal _updateLastFeeOpTime
-> internal _calcBorrowingFee
-> internal _calcBorrowingRate
  -> library BimaMath._min


### external decreaseDebtAndSendCollateral
-> internal _requireCallerIsLM
-> internal _decreaseDebt
-> private _sendCollateral


### public fetchPrice
_(no internal calls)_


### external finalizeLiquidation
-> internal _requireCallerIsLM
-> internal _redistributeDebtAndColl
-> private _sendCollateral


### external getBorrowingFee
-> internal _calcBorrowingFee
-> public getBorrowingRate
  -> internal _calcBorrowingRate
    -> library BimaMath._min


### external getBorrowingFeeWithDecay
-> internal _calcBorrowingFee
-> public getBorrowingRateWithDecay
  -> internal _calcBorrowingRate
    -> library BimaMath._min
  -> internal _calcDecayedBaseRate
    -> library BimaMath._decPow


### public getBorrowingRate
-> internal _calcBorrowingRate
  -> library BimaMath._min


### public getBorrowingRateWithDecay
-> internal _calcBorrowingRate
  -> library BimaMath._min
-> internal _calcDecayedBaseRate
  -> library BimaMath._decPow


### public getCurrentICR
-> public getTroveCollAndDebt
  -> public getEntireDebtAndColl
    -> public getPendingCollAndDebtRewards
    -> internal _calculateInterestIndex
-> library BimaMath._computeCR


### public getEntireDebtAndColl
-> public getPendingCollAndDebtRewards
-> internal _calculateInterestIndex


### external getEntireSystemBalances
-> public getEntireSystemColl
-> public getEntireSystemDebt
  -> internal _calculateInterestIndex
-> public fetchPrice


### public getEntireSystemColl
_(no internal calls)_


### public getEntireSystemDebt
-> internal _calculateInterestIndex


### public getNominalICR
-> public getTroveCollAndDebt
  -> public getEntireDebtAndColl
    -> public getPendingCollAndDebtRewards
    -> internal _calculateInterestIndex
-> library BimaMath._computeNominalCR


### public getPendingCollAndDebtRewards
_(no internal calls)_


### external getRedemptionFeeWithDecay
-> internal _calcRedemptionFee
-> public getRedemptionRateWithDecay
  -> internal _calcRedemptionRate
    -> library BimaMath._min
  -> internal _calcDecayedBaseRate
    -> library BimaMath._decPow


### public getRedemptionRate
-> internal _calcRedemptionRate
  -> library BimaMath._min


### public getRedemptionRateWithDecay
-> internal _calcRedemptionRate
  -> library BimaMath._min
-> internal _calcDecayedBaseRate
  -> library BimaMath._decPow


### public getTotalActiveCollateral
_(no internal calls)_


### public getTotalActiveDebt
-> internal _calculateInterestIndex


### external getTotalMints
_(no internal calls)_


### public getTroveCollAndDebt
-> public getEntireDebtAndColl
  -> public getPendingCollAndDebtRewards
  -> internal _calculateInterestIndex


### external getTroveFromTroveOwnersArray
_(no internal calls)_


### external getTroveOwnersCount
_(no internal calls)_


### external getTroveStake
_(no internal calls)_


### external getTroveStatus
_(no internal calls)_


### public getWeek
_(no internal calls)_


### public getWeekAndDay
_(no internal calls)_


### public guardian
_(no internal calls)_


### public hasPendingRewards
_(no internal calls)_


### external movePendingTroveRewardsToActiveBalances
-> internal _requireCallerIsLM
-> internal _movePendingTroveRewardsToActiveBalance


### external notifyRegisteredId
_(no internal calls)_


### external openTrove
-> internal _requireCallerIsBO
-> internal _accrueActiveInterests
  -> internal _calculateInterestIndex
-> internal _updateTroveRewardSnapshots
-> internal _updateStakeAndTotalStakes
  -> internal _computeNewStake
-> internal _updateIntegrals
  -> internal _updateRewardIntegral
    -> internal _fetchRewards
      -> public getWeek
  -> internal _updateIntegralForAccount
-> internal _updateMintVolume
  -> public getWeekAndDay


### public owner
_(no internal calls)_


### external redeemCollateral
-> public fetchPrice
-> private _updateBalances
  -> internal _updateRewardIntegral
    -> internal _fetchRewards
      -> public getWeek
  -> internal _accrueActiveInterests
    -> internal _calculateInterestIndex
-> public getEntireSystemDebt
  -> internal _calculateInterestIndex
-> internal _isValidFirstRedemptionHint
  -> public getCurrentICR
    -> public getTroveCollAndDebt
      -> public getEntireDebtAndColl
        -> public getPendingCollAndDebtRewards
        -> internal _calculateInterestIndex
    -> library BimaMath._computeCR
-> public getCurrentICR
  -> public getTroveCollAndDebt
    -> public getEntireDebtAndColl
      -> public getPendingCollAndDebtRewards
      -> internal _calculateInterestIndex
  -> library BimaMath._computeCR
-> internal _applyPendingRewards
  -> internal _accrueActiveInterests
    -> internal _calculateInterestIndex
  -> public getPendingCollAndDebtRewards
  -> internal _updateTroveRewardSnapshots
  -> internal _movePendingTroveRewardsToActiveBalance
  -> internal _updateIntegrals
    -> internal _updateRewardIntegral
      -> internal _fetchRewards
        -> public getWeek
    -> internal _updateIntegralForAccount
-> internal _redeemCollateralFromTrove
  -> library BimaMath._min
  -> internal _closeTrove
  -> internal _redeemCloseTrove
  -> library BimaMath._computeNominalCR
  -> internal _getNetDebt
  -> internal _updateStakeAndTotalStakes
    -> internal _computeNewStake
-> internal _updateBaseRateFromRedemption
  -> internal _calcDecayedBaseRate
    -> library BimaMath._decPow
  -> library BimaMath._min
  -> internal _updateLastFeeOpTime
-> internal _calcRedemptionFee
-> public getRedemptionRate
  -> internal _calcRedemptionRate
    -> library BimaMath._min
-> internal _requireUserAcceptsFee
-> private _sendCollateral
-> private _resetState


### external setAddresses
_(no internal calls)_


### public setParameters
-> public owner
-> internal _decayBaseRate
  -> internal _calcDecayedBaseRate
    -> library BimaMath._decPow
  -> internal _updateLastFeeOpTime
-> internal _accrueActiveInterests
  -> internal _calculateInterestIndex


### external setPaused
-> public guardian
-> public owner


### external setPriceFeed
_(no internal calls)_


### external startSunset
-> internal _accrueActiveInterests
  -> internal _calculateInterestIndex


### external updateBalances
-> internal _requireCallerIsLM
-> private _updateBalances
  -> internal _updateRewardIntegral
    -> internal _fetchRewards
      -> public getWeek
  -> internal _accrueActiveInterests
    -> internal _calculateInterestIndex


### external updateTroveFromAdjustment
-> internal _requireCallerIsBO
-> internal _updateMintVolume
  -> public getWeekAndDay
-> internal _increaseDebt
-> internal _decreaseDebt
-> private _sendCollateral
-> library BimaMath._computeNominalCR
-> internal _updateStakeAndTotalStakes
  -> internal _computeNewStake


### external vaultClaimReward
-> internal _claimReward
  -> internal _applyPendingRewards
    -> internal _accrueActiveInterests
      -> internal _calculateInterestIndex
    -> public getPendingCollAndDebtRewards
    -> internal _updateTroveRewardSnapshots
    -> internal _movePendingTroveRewardsToActiveBalance
    -> internal _updateIntegrals
      -> internal _updateRewardIntegral
        -> internal _fetchRewards
          -> public getWeek
      -> internal _updateIntegralForAccount
  -> internal _getPendingMintReward
    -> public getWeekAndDay


---

## TroveManagerGetters

_File: core/helpers/TroveManagerGetters.sol_

### external getActiveTroveManagersForAccount
_(no internal calls)_


### external getAllCollateralsAndTroveManagers
_(no internal calls)_

