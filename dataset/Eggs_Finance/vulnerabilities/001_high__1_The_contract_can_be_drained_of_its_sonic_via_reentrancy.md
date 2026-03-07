# .1 The contract can be drained of its sonic via reentrancy

**Severity:** high
**Auditor:** Cantina
**Protocol:** Eggs Finance
**Keywords:** reentrancy, contract, drain, sonic, borrow, collateral, Eggs, borrowMore, nonReentrant, attack, vulnerability, security, Ethereum, smart contract, functionality, transfer, loans, safety checks, monotonically increasing, value

---

# .1 The contract can be drained of its sonic via reentrancy
**Severity:** Critical Risk  
**Context:** (No context files were provided by the reviewer)  
**Summary:** Unlike other externally accessible, state-changing functions, both the \u0060Eggs.borrow\u0060 and \u0060Eggs.borrowMore\u0060 functions do not have a \u0060nonReentrant\u0060 modifier. In a specific circumstance, the \u0060borrowMore\u0060 function can be reentered to drain the contract of its sonic.

**Finding Description:** \u0060Eggs.borrowMore\u0060 contains functionality to allow users to borrow more sonic without supplying additional collateral in case their position is already sufficiently over-collateralized:

\u0060\u0060\u0060solidity
uint256 userEggs = SONICtoEGGSNoTrade(sonic);
uint256 userBorrowedInEggs = SONICtoEGGSNoTrade(userBorrowed);
uint256 userExcessInEggs = ((userCollateral) * 99) / 100 - userBorrowedInEggs;
uint256 requireCollateralFromUser = userEggs;
if (userExcessInEggs >= userEggs) {
    requireCollateralFromUser = 0;
} else {
    requireCollateralFromUser = requireCollateralFromUser - userExcessInEggs;
}
if (requireCollateralFromUser != 0) {
    _transfer(msg.sender, address(this), requireCollateralFromUser);
}
\u0060\u0060\u0060

Since this function does not have a \u0060nonReentrant\u0060 modifier, an attacker can reenter when the additional sonic to borrow is sent to them via a call:

\u0060\u0060\u0060solidity
sendSonic(msg.sender, newUserBorrow - sonicFee);
function sendSonic(address _address, uint256 _value) internal {
    (bool success, ) = _address.call{value: _value}("");
    require(success, "SONIC Transfer failed.");
    emit SendSonic(_address, _value);
}
\u0060\u0060\u0060

This allows the attacker to call \u0060borrowMore\u0060 again with the same parameter. Since \u0060Loans[msg.sender]\u0060 hasn\u0027t yet been updated, the attacker still doesn\u0027t have to provide collateral to borrow the same amount of sonic.

We run safety checks at the end of the function in part to protect the invariant that the price is monotonically increasing:

\u0060\u0060\u0060solidity
uint256 newPrice = (getBacking() * 1 ether) / totalSupply();
// ...
require(lastPrice <= newPrice, "The price of eggs cannot decrease");
lastPrice = newPrice;
\u0060\u0060\u0060

Since we increase the \u0060totalBorrowed\u0060 via \u0060addLoansByDate\u0060 by the amount being transferred to the user, while keeping the actual and stored collateral amounts constant, the price actually remains constant. As a result, the attacker can drain the contract of its entire sonic balance via this attack while still passing the safety check.

**Impact Explanation:** An attacker can drain the contract of its entire sonic balance. Since sonic is the backing of the eggs token, the value of eggs becomes ~0 as a result.

**Likelihood Explanation:** The only requirement for this attack to take place is a sufficiently over-collateralized loan. As long as there is activity in the contract, generating fees, loans will naturally become over-collateralized. This will allow for more sonic to be borrowed without providing additional collateral, thereby allowing the attack to take place.
