# Callpaths — Eggs_Finance

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## EGGS

_File: Eggs.sol_

### public EGGStoSONIC
-> public getBacking
  -> public getTotalBorrowed


### public SONICtoEGGS
-> public getBacking
  -> public getTotalBorrowed


### public SONICtoEGGSLev
-> public getBacking
  -> public getTotalBorrowed


### public SONICtoEGGSNoTrade
-> public getBacking
  -> public getTotalBorrowed


### public SONICtoEGGSNoTradeCeil
-> public getBacking
  -> public getTotalBorrowed


### public borrow
-> public isLoanExpired
-> public liquidate
-> public getMidnightTimestamp
-> public getInterestFee
-> public SONICtoEGGSNoTradeCeil
  -> public getBacking
    -> public getTotalBorrowed
-> internal sendSonic
-> private addLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### public borrowMore
-> public isLoanExpired
-> public liquidate
-> public getMidnightTimestamp
-> public getInterestFee
-> public SONICtoEGGSNoTradeCeil
  -> public getBacking
    -> public getTotalBorrowed
-> public SONICtoEGGSNoTrade
  -> public getBacking
    -> public getTotalBorrowed
-> internal sendSonic
-> private addLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### external buy
-> public liquidate
-> public SONICtoEGGS
  -> public getBacking
    -> public getTotalBorrowed
-> private mint
-> public getBuyFee
-> internal sendSonic
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### public closePosition
-> public isLoanExpired
-> private subLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### public extendLoan
-> public getInterestFee
-> public isLoanExpired
-> internal sendSonic
-> private subLoansByDate
-> private addLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### public flashClosePosition
-> public isLoanExpired
-> public liquidate
-> public EGGStoSONIC
  -> public getBacking
    -> public getTotalBorrowed
-> internal sendSonic
-> private subLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### public getBacking
-> public getTotalBorrowed


### public getBuyAmount
-> public SONICtoEGGSNoTrade
  -> public getBacking
    -> public getTotalBorrowed
-> public getBuyFee


### external getBuyEggs
-> public getBacking
  -> public getTotalBorrowed


### public getBuyFee
_(no internal calls)_


### public getInterestFee
_(no internal calls)_


### public getLoanByAddress
_(no internal calls)_


### public getLoansExpiringByDate
-> public getMidnightTimestamp


### public getMidnightTimestamp
_(no internal calls)_


### public getTotalBorrowed
_(no internal calls)_


### public getTotalCollateral
_(no internal calls)_


### public isLoanExpired
_(no internal calls)_


### public leverage
-> public isLoanExpired
-> public liquidate
-> public getMidnightTimestamp
-> public leverageFee
  -> public getInterestFee
-> internal sendSonic
-> public SONICtoEGGSLev
  -> public getBacking
    -> public getTotalBorrowed
-> private mint
-> private addLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### public leverageFee
-> public getInterestFee


### public liquidate
_(no internal calls)_


### public removeCollateral
-> public isLoanExpired
-> public liquidate
-> public EGGStoSONIC
  -> public getBacking
    -> public getTotalBorrowed
-> private subLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### public repay
-> public isLoanExpired
-> private subLoansByDate
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### external sell
-> public liquidate
-> public EGGStoSONIC
  -> public getBacking
    -> public getTotalBorrowed
-> internal sendSonic
-> private safetyCheck
  -> public getBacking
    -> public getTotalBorrowed


### external setBuyFee
_(no internal calls)_


### external setBuyFeeLeverage
_(no internal calls)_


### external setFeeAddress
_(no internal calls)_


### external setSellFee
_(no internal calls)_


### public setStart
_(no internal calls)_


---

## JayFeeSplitter

_File: FeeDistributor.sol_

### external setTEAMWallet
_(no internal calls)_


### external updateCampaignParameters
_(no internal calls)_

