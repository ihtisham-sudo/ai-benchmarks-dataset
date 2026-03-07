# 3.4.1 buy fee must be less than 0% or more

**Severity:** high
**Auditor:** Cantina
**Protocol:** Eggs Finance
**Keywords:** buy fee, sell fee, fee structure, requirement, contract, owner, emit, maximum, minimum, setBuyFee, EggsFinance, CantinaManaged, solidity, function, update, error, validation, transaction, gas, commit

---

# 3.4.1 buy fee must be less than 0% or more
\u0060\u0060\u0060solidity
function setBuyFee(uint16 amount) external onlyOwner {
    require(amount <= 992, "buy fee must be at least 0.8%");
    require(amount >= 975, "buy fee must be less than 2.5%");
    BUY_FEE = amount;
    emit buyFeeUpdated(amount);
}
\u0060\u0060\u0060
Note that this also affects sell and assuming a function is added to set the SELL_FEE, we should enforce the same maximum.  
**EggsFinance:** Fixed in commit c177bc97.  
**CantinaManaged:** Fixed as recommended.

## 3.4.2 FEE_ADDRESS is not initialized in the constructor which may lead to loss of fees
**Severity:** Low Risk  
**Context:** (No context files were provided by the reviewer)  
**Description:** The initialization of the contract consists of two main functions; the constructor and set-Start(). Functions like buy() (and others) cannot be called before setStart() is called, but they can be called while FEE_ADDRESS is not initialized (by calling setFeeAddress()) leading to lost fees.  
**Recommendation:** Consider initializing FEE_ADDRESS either in the constructor or in setStart().  
**EggsFinance:** Fixed in commit 2f02fb77 by reverting in setStart if FEE_ADDRESS == address(0x0).  
**CantinaManaged:** Verified.

## 3.4.3 Missing setters for mutable SELL_FEE and BUY_FEE_REVERSE
**Severity:** Low Risk  
**Context:** Eggs.sol  
**Description:** We have the following mutable fee storage variables:
\u0060\u0060\u0060solidity
uint16 public SELL_FEE = 975;
uint16 public BUY_FEE = 975;
uint16 public BUY_FEE_REVERSE = 10;
\u0060\u0060\u0060
Of these, only BUY_FEE has a setter (setBuyFee). If it\u0027s intended for SELL_FEE and BUY_FEE_REVERSE to be mutable, they should have setter functions. Alternatively, if they should be immutable then we can set them as constants to save a significant amount of gas each time they\u0027re used.  
**Recommendation:** Either implement setter functions for SELL_FEE and BUY_FEE_REVERSE or make them constants.  
**Note:** If you choose to add setter functions, carefully consider the minimum and maximum values to be enforced, as recommended in the other finding: Fees will not be charged if BUY_FEE is set low enough.  
**EggsFinance:** Fixed in commit c177bc97.  
**CantinaManaged:** Fixed as recommended.

## 3.5 Informational

### 3.5.1 liquidate calls inside functions will not be effective in case caller\u0027s loan is expired
**Severity:** Informational  
**Context:** (No context files were provided by the reviewer)  
**Description:** The protocol implements loans that expire on a specific date. After the expiry date, loans that were not closed will be liquidated upon the next call to liquidate:
## Liquidation Function Vulnerability

\u0060\u0060\u0060solidity
function liquidate() public {
    uint256 borrowed;
    uint256 collateral;
    while (lastLiquidationDate < block.timestamp) {
        collateral += CollateralByDate[lastLiquidationDate];
        borrowed += BorrowedByDate[lastLiquidationDate];
        lastLiquidationDate += 1 days;
    }
    if (collateral != 0) {
        totalCollateral -= collateral;
        _burn(address(this), collateral);
    }
    if (borrowed != 0) {
        totalBorrowed -= borrowed;
        emit Liquidate(lastLiquidationDate - 1 days, borrowed);
    }
}
\u0060\u0060\u0060

To make the system more efficient, this function is being as part of any function that modify the state. However, functions like borrowMore, removeCollateral, repay, closePosition, flashClosePosition, and extendLoan will revert in case the function caller has an expired loan, which means the effects of liquidate will also revert.

### Recommendation

Consider implementing an off-chain script that will call liquidate on a daily basis as well as placing the expiration check for the caller loan before the call to liquidate. Another option which is less recommended will be to return early instead of reverting in case the loan has expired.

- EggsFinance: Fixed in commit 2f02fb77.
- CantinaManaged: Fixed as recommended.
PAGE END
