# 3.1.2 - Repay Does Not Decrease Borrowed Amount as Expected

**Severity:** critical
**Auditor:** Cantina
**Protocol:** Eggs Finance
**Keywords:** repay, borrowed, SONIC, Loan struct, funds, error, short term, long term, test coverage, smart contract, vulnerability, issue, recommendation, commit, CantinaManaged, EggsFinance, decrease, value, function, code

---

# 3.1.1 Non-reentrancy Risk
**Severity:** High Risk  
**Context:** Eggs.sol#L330  
**Description:** The borrow and borrowMore functions are susceptible to reentrancy attacks.  
**Recommendation:** Add the nonReentrant modifier to both the borrow and borrowMore functions. Additionally, it\u0027s best practice to follow the checks-effects-interactions pattern, which would also prevent this by setting storage (effects), like Loans[msg.sender], before making any external calls (interactions).  
**EggsFinance:** Fixed in commit 2f02fb77.  
**CantinaManaged:** Fixed as recommended.  

## 3.1.2 Repay Does Not Decrease Borrowed Amount as Expected
**Severity:** Critical Risk  
**Context:** Eggs.sol#L342  
**Description:** repay is a function that allows the borrower to repay a portion of the borrowed funds. The function successfully receives the SONIC payment but does not decrease the corresponding value of borrowed in the Loan struct as we can see:
\u0060\u0060\u0060solidity
uint256 newBorrow = borrowed - msg.value;
Loans[msg.sender].borrowed - newBorrow;
\u0060\u0060\u0060
This error will result in the caller losing these funds.  
**Recommendation:** 
- Short term: consider changing the issued line to:
\u0060\u0060\u0060solidity
Loans[msg.sender].borrowed = newBorrow;
\u0060\u0060\u0060
- Long term: consider improving test coverage to detect these kind of issues.  
**EggsFinance:** Fixed in commit 2f02fb77.  
**CantinaManaged:** Fixed as recommended.  

## 3.2 High Risk

### 3.2.1 Leveraged Positions Can Be Created Before the System Start
**Severity:** High Risk  
**Context:** Eggs.sol#L151-L154  
**Description:** The protocol contains a start storage variable, which only the owner can set:
\u0060\u0060\u0060solidity
function setStart() public onlyOwner {
    start = true;
    emit Started(true);
}
\u0060\u0060\u0060
Before this point, it should not be possible to interact with the system, as is enforced in buy:
\u0060\u0060\u0060solidity
require(start, "Trading must be initialized");
\u0060\u0060\u0060
Most other state-changing functions do not require this enforcement because the user must hold eggs to execute the functions. However, the leverage function only requires the user to hold sonic and doesn\u0027t enforce that start == true. As a result, it\u0027s possible to create a leveraged position before it\u0027s possible to purchase eggs. This would give a significantly unfair advantage as they would be able to open a position at the lowest possible price, before anyone else.  
**Recommendation:** Add a require(start) check in leverage to ensure that leveraged positions cannot be opened before start == true.  
**EggsFinance:** Fixed in commit 2f02fb77.  
**CantinaManaged:** Fixed as recommended.
