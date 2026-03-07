# Ignite - isCoolerCallback can be bypassed

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Olympus Cooler 
**Keywords:** cybersecurity, vulnerability, CoolerCallback, bypass, loan default, validation, smart contract, Solidity, malicious lender, callback function, loan ownership, approve transfer, transfer ownership, debt tokens, collateral, interest calculation, active loan request, protocol trust, manual review, business logic

---

Ignite

high

# isCoolerCallback can be bypassed
## Summary

The lender can bypass \u0060CoolerCallback.isCoolerCallback()\u0060 validation without implements the \u0060CoolerCallback\u0060 abstract.

In the provided example, this may force the loan to default.

## Vulnerability Detail

The \u0060CoolerCallback.isCoolerCallback()\u0060 is intended to ensure that the lender implements the \u0060CoolerCallback\u0060 abstract at line 241 when the parameter \u0060isCallback_\u0060 is \u0060true\u0060.

\u0060\u0060\u0060solidity=!
function clearRequest(
    uint256 reqID_,
    bool repayDirect_,
    bool isCallback_
) external returns (uint256 loanID) {
    Request memory req = requests[reqID_];

    // If necessary, ensure lender implements the CoolerCallback abstract.
    if (isCallback_ && !CoolerCallback(msg.sender).isCoolerCallback()) revert NotCoolerCallback();

    // Ensure loan request is active. 
    if (!req.active) revert Deactivated();

    // Clear the loan request in memory.
    req.active = false;

    // Calculate and store loan terms.
    uint256 interest = interestFor(req.amount, req.interest, req.duration);
    uint256 collat = collateralFor(req.amount, req.loanToCollateral);
    uint256 expiration = block.timestamp + req.duration;
    loanID = loans.length;
    loans.push(
        Loan({
            request: req,
            amount: req.amount + interest,
            unclaimed: 0,
            collateral: collat,
            expiry: expiration,
            lender: msg.sender,
            repayDirect: repayDirect_,
            callback: isCallback_
        })
    );

    // Clear the loan request storage.
    requests[reqID_].active = false;

    // Transfer debt tokens to the owner of the request.
    debt().safeTransferFrom(msg.sender, owner(), req.amount);

    // Log the event.
    factory().newEvent(reqID_, CoolerFactory.Events.ClearRequest, 0);
}
\u0060\u0060\u0060
https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Cooler.sol#L233-L275

However, this function doesn\u0027t provide any protection. The lender can bypass this check without implementing the \u0060CoolerCallback\u0060 abstract by calling the \u0060Cooler.clearRequest()\u0060 function using a contract that implements the \u0060isCoolerCallback()\u0060 function and returns a \u0060true\u0060 value.

For example:

\u0060\u0060\u0060solidity=!
contract maliciousLender {
    function isCoolerCallback() pure returns(bool) {
        return true;
    }
    
    function operation(
        address _to,
        uint256 reqID_
    ) public {
        Cooler(_to).clearRequest(reqID_, true, true);
    }
    
    function onDefault(uint256 loanID_, uint256 debt, uint256 collateral) public {}
}
\u0060\u0060\u0060

By being the \u0060loan.lender\u0060 with implement only \u0060onDefault()\u0060 function, this will cause the \u0060repayLoan()\u0060 and \u0060rollLoan()\u0060 methods to fail due to revert at \u0060onRepay()\u0060 and \u0060onRoll()\u0060 function. The borrower cannot repay and the loan will be defaulted.

After the loan default, the attacker can execute \u0060claimDefault()\u0060 to claim the collateral.

Furthermore, there is another method that allows lenders to bypass the \u0060CoolerCallback.isCoolerCallback()\u0060 function which is loan ownership transfer.

\u0060\u0060\u0060solidity=!
/// @notice Approve transfer of loan ownership rights to a new address.
/// @param  to_ address to be approved.
/// @param  loanID_ index of loan in loans[].
function approveTransfer(address to_, uint256 loanID_) external {
    if (msg.sender != loans[loanID_].lender) revert OnlyApproved();

    // Update transfer approvals.
    approvals[loanID_] = to_;
}

/// @notice Execute loan ownership transfer. Must be previously approved by the lender.
/// @param  loanID_ index of loan in loans[].
function transferOwnership(uint256 loanID_) external {
    if (msg.sender != approvals[loanID_]) revert OnlyApproved();

    // Update the load lender.
    loans[loanID_].lender = msg.sender;
    // Clear transfer approvals.
    approvals[loanID_] = address(0);
}
\u0060\u0060\u0060

Normally, the lender who implements the \u0060CoolerCallback\u0060 abstract may call the \u0060Cooler.clearRequest()\u0060 with the \u0060_isCoolerCallback\u0060 parameter set to \u0060true\u0060 to execute logic when a loan is repaid, rolled, or defaulted.

But the lender needs to change the owner of the loan, so they call the \u0060approveTransfer()\u0060 and \u0060transferOwnership()\u0060 functions to the contract that doesn\u0027t implement the \u0060CoolerCallback\u0060 abstract (or implement only \u0060onDefault()\u0060 function to force the loan default), but the \u0060loan.callback\u0060 flag is still set to \u0060true\u0060.

Thus, this breaks the business logic since the three callback functions don\u0027t need to be implemented when the \u0060isCoolerCallback()\u0060 is set to \u0060true\u0060 according to the dev note in the \u0060CoolerCallback\u0060 abstract below:

> /// @notice Allows for debt issuers to execute logic when a loan is repaid, rolled, or defaulted.
/// @dev    The three callback functions must be implemented if \u0060isCoolerCallback()\u0060 is set to true.

## Impact

1. The lender forced the Loan become default to get the collateral token, owner lost the collateral token.

2. Bypass the \u0060isCoolerCallback\u0060 validation.
## Code Snippet

https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Cooler.sol#L241

https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Cooler.sol#L338-L343

https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Cooler.sol#L347-L354

## Tool used

Manual Review

## Recommendation

Only allowing callbacks from the protocol-trusted address (eg., \u0060Clearinghouse\u0060 contract).

Disable the transfer owner of the loan when the \u0060loan.callback\u0060 is set to \u0060true\u0060.

