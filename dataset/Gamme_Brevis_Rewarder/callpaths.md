# Callpaths — Gamme_Brevis_Rewarder

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## GammaRewarder

_File: src/GammaRewarder.sol_

### external claim
-> internal _verifyProof
  -> public getMerkleRoot
-> public getMerkleRoot


### external createDistribution
-> internal _getRoundedEpoch


### external dispute
_(no internal calls)_


### external getActiveDistributions
-> internal _getRoundedEpoch
-> internal _getDistributionsBetweenEpochs
  -> internal _isDistributionLiveBetweenEpochs


### external getAllDistributions
_(no internal calls)_


### external getDistributionsForEpoch
-> internal _getRoundedEpoch
-> internal _getDistributionsBetweenEpochs
  -> internal _isDistributionLiveBetweenEpochs


### public getMerkleRoot
_(no internal calls)_


### external initialize
_(no internal calls)_


### external reclaimRemainingDistribution
_(no internal calls)_


### external resolveDispute
-> internal _revokeTree
-> internal _endOfDisputePeriod


### external setDisputeAmount
_(no internal calls)_


### external setDisputePeriod
_(no internal calls)_


### external setDisputeToken
_(no internal calls)_


### external setNewDistributor
_(no internal calls)_


### external setProtocolFee
_(no internal calls)_


### external setProtocolFeeRecipient
_(no internal calls)_


### external setReclaimPeriod
_(no internal calls)_


### external toggleTokenWhitelist
_(no internal calls)_


### external updateTree
-> internal _endOfDisputePeriod

