# M-1 - Lend offer can be deleted multiple times

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Debita Finance V3
**Keywords:** lend offer, delete, addFunds, isActive, changePerpetual, deleteOrder, activeOrdersCount, perpetual mode, available amount, nonReentrant, emitDelete, emitUpdate, contract, owner, function, impact, mitigation, audit, smart contract, security

---

# Issue M-1: Lend offer can be deleted multiple times

Source: [GitHub Issue #119](https://github.com/sherlock-audit/2024-10-debita-judging/issues/119)  
Found by: 0x37, 0xAristos, 0xSolus, KlosMitSoss, Vidus, bbl4de, copperscrewer, liquidbuddha, newspacexyz, onthehunt, theweb3mechanic

Lack of check in \u0060addFunds()\u0060 function. This will cause one lend offer can be deleted twice.

In \u0060DebitaLendOffer-Implementation:178\u0060, there is one perpetual mode. Considering one scenario: The lend offer is in perpetual mode and current available amount equals 0. Now when we try to change perpetual to false, we will delete this lend order. The problem is that we lack updating \u0060isActive\u0060 to false in \u0060changePerpetual()\u0060. This will cause that the owner can trigger \u0060changePerpetual\u0060 multiple times to delete the same lend order. When we repeat deleting the same lend order in \u0060deleteOrder\u0060, we will keep decreasing \u0060activeOrdersCount\u0060. This will impact other lend offers. Other lend offers may not be deleted.

\u0060\u0060\u0060solidity
function changePerpetual(bool _perpetual) public onlyOwner nonReentrant {
    require(isActive, "Offer is not active");
    lendInformation.perpetual = _perpetual;
    if (_perpetual == false && lendInformation.availableAmount == 0) {
        IDLOFactory(factoryContract).emitDelete(address(this));
        IDLOFactory(factoryContract).deleteOrder(address(this));
    } else {
        IDLOFactory(factoryContract).emitUpdate(address(this));
    }
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function deleteOrder(address _lendOrder) external onlyLendOrder {
    uint index = LendOrderIndex[_lendOrder];
    LendOrderIndex[_lendOrder] = 0;
    // switch index of the last borrow order to the deleted borrow order
    allActiveLendOrders[index] = allActiveLendOrders[activeOrdersCount - 1];
    LendOrderIndex[allActiveLendOrders[activeOrdersCount - 1]] = index;
    // take out last borrow order
    allActiveLendOrders[activeOrdersCount - 1] = address(0);
}
\u0060\u0060\u0060
Internal pre-conditions  
N/A  

External pre-conditions  
N/A  

Attack Path  
1. Alice creates one lend order with perpetual mode.  
2. Match Alice\u0027s lend order to let availableAmount to 0.  
3. Alice triggers changePerpetual repeatedly to let activeOrdersCount to 0.  
4. Other lend orders cannot be deleted.  

Impact  
All lend orders cannot be deleted. This will cause that lend order cannot be cancelled or may not accept this lend offer if we want to use the whole lend order\u0027s principle.  

PoC  
N/A  

Mitigation  
When we delete the lend order, we should set it to inactive. This will prevent changePerpetual() retriggered repeatedly.  

\u0060\u0060\u0060javascript
function changePerpetual(bool _perpetual) public onlyOwner nonReentrant {
    require(isActive, "Offer is not active");
    lendInformation.perpetual = _perpetual;
    if (_perpetual == false && lendInformation.availableAmount == 0) {
        isActive = false;
        IDLOFactory(factoryContract).emitDelete(address(this));
        IDLOFactory(factoryContract).deleteOrder(address(this));
    } else {
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/307e2360dd9aaac443f17547466c51718d4cefd3
## Issue M-2: Borrowers cannot extend loans which has maximum duration less than 24 hours

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/153)  
Found by: 0x37, 0xc0ffEE, KaplanLabs, bbl4de, dhank, farismaulana, nikhil840096, ydlee

The logic to calculate the missing borrow fee is incorrect, which will cause the borrowers cannot extend loans having maximum duration less than 24 hours because of arithmetic underflow.

- In function \u0060DebitaV3Loan::extendLoan()\u0060, the borrower has to pay the extra fee if he has not paid maximum fee yet.
- The variable \u0060feeOfMaxDeadline\u0060 is expected to be the fee to pay for lend offer\u0027s maximum duration, which is then adjusted to be within the range \u0060[feePerDay; maxFee]\u0060. This implies that the extra fee considers offer\u0027s min duration fee to be 1 day.
- The fee paid for the initial duration is bounded to be within the range \u0060[minFEE; maxFee]\u0060.
- The fee configurations are set initially as. The fee implies that min fee for the loan initial duration is 0.2%, = 5 days of fee.

\u0060\u0060\u0060solidity
uint public feePerDay = 4; // fee per day (0.04%)
uint public maxFEE = 80; // max fee 0.8%
uint public minFEE = 20; // min fee 0.2%
\u0060\u0060\u0060

- The extra fee to be paid is calculated as \u0060misingBorrowFee = feeOfMaxDeadline - PorcentageOfFeePaid\u0060, which will revert due to arithmetic underflow in case the loan\u0027s initial duration is less than 24 hours and the unpaid offers\u0027 maximum duration is also less than 24 hours. In this situation, the values will satisfy \u0060PorcentageOfFeePaid = minFEE = 0.2%\u0060, \u0060feeOfMaxDeadline = feePerDay = 0.04%\u0060, which will cause \u0060misingBorrowFee = feeOfMaxDeadline - PorcentageOfFeePaid\u0060 to revert because of arithmetic underflow.
uint feePerDay = Aggregator(AggregatorContract).feePerDay();
uint minFEE = Aggregator(AggregatorContract).minFEE();
uint maxFee = Aggregator(AggregatorContract).maxFEE();
uint PorcentageOfFeePaid = ((m_loan.initialDuration * feePerDay) /
86400);
// adjust fees
if (PorcentageOfFeePaid > maxFee) {
    PorcentageOfFeePaid = maxFee;
} else if (PorcentageOfFeePaid < minFEE) {
    PorcentageOfFeePaid = minFEE;
}
// calculate interest to pay to Debita and the subtract to the lenders
for (uint i; i < m_loan._acceptedOffers.length; i++) {
    infoOfOffers memory offer = m_loan._acceptedOffers[i];
    // if paid, skip
    // if not paid, calculate interest to pay
    if (!offer.paid) {
        uint alreadyUsedTime = block.timestamp - m_loan.startedAt;
        uint extendedTime = offer.maxDeadline -
            alreadyUsedTime -
            block.timestamp;
        uint interestOfUsedTime = calculateInterestToPay(i);
        uint interestToPayToDebita = (interestOfUsedTime * feeLender) /
            10000;
        uint misingBorrowFee;
        // if user already paid the max fee, then we dont have to charge
        // them again
        if (PorcentageOfFeePaid != maxFee) {
            // calculate difference from fee paid for the initialDuration
            // vs the extra fee they should pay because of the extras days of extending the
            // loan. MAXFEE shouldnt be higher than extra fee + PorcentageOfFeePaid
            uint feeOfMaxDeadline = ((offer.maxDeadline * feePerDay) /
                86400);
            if (feeOfMaxDeadline > maxFee) {
                feeOfMaxDeadline = maxFee;
            } else if (feeOfMaxDeadline < feePerDay) {
                feeOfMaxDeadline = feePerDay;
            }
            misingBorrowFee = feeOfMaxDeadline - PorcentageOfFeePaid;
        }
}
No response

No response

1. A borrow offer is created with duration = 5 hours
2. A lend offer is created with min duration = 3 hours, max duration = 12 hours
3. 2 offers matched
4. After 4 hours, the borrower decides to extend loan by calling extendLoan() and transaction gets reverted

- Borrowers cannot extend loan for the loans having durations less than 24 hours (both initial duration and offers\u0027 max duration)

No response

Consider updating like below
\u0060\u0060\u0060plaintext
} else if (feeOfMaxDeadline < feePerDay) {
                feeOfMaxDeadline = feePerDay;
} else if (feeOfMaxDeadline < minFEE) {
                feeOfMaxDeadline = minFEE;
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/2958108a7a7307830](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/2958108a7a7307830)  
953dec9bf4f3178a6cff434
## Issue M-3: The precision loss in the fee percentage for connecting offers results in the borrower paying less than the expected fee.

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/208)

Found by: nikhil840096, ydlee


Some of the borrowed principal tokens is charged as a fee for connecting transactions. The percentage of the fee is calculated according to \u0060DebitaV3Aggregator.sol:391\u0060. There is a non-negligible precision loss in the calculation process. Since the default \u0060feePerDay\u0060 is 4, the maximum loss could reach up to 1/4 of the daily fee, which is significant, especially when the amount borrowed is substantial.

\u0060\u0060\u0060solidity
391:     uint percentage = ((borrowInfo.duration * feePerDay) / 86400);              //
\u0060\u0060\u0060
[@audit-issue 1/4](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Aggregator.sol#L391)

There are another 2 instances of the issue in \u0060DebitaV3Load.sol:extendLoan\u0060.

\u0060\u0060\u0060solidity
571:     uint PorcentageOfFeePaid = ((m_loan.initialDuration * feePerDay) /
572:          86400);
\u0060\u0060\u0060
[Link](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L571-L572)

\u0060\u0060\u0060solidity
602:                   uint feeOfMaxDeadline = ((offer.maxDeadline * feePerDay) /
603:                        86400);
\u0060\u0060\u0060
[Link](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L602-L603)

In DebitaV3Aggregator.sol:391, rounding down the fee percentage can lead to a non-trivial precision loss.


No response


No response


By setting the borrowing duration to N days + 86400/4 - 1, users can save the maximum fee.


The precision loss in the fee percentage results in the borrower paying less than the expected fee, with the maximum loss potentially reaching up to 1/4 of the daily fee.


No response


When calculating the fee percentage, rounding up; or multiplying by a multiple to increase precision.


sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/c946cdd90c8d4841fa254359a863d3b574e34566](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/c946cdd90c8d4841fa254359a863d3b574e34566)
## Issue M-4: The fee calculation in extend-Loan function has an error

**Source:** [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/211)  
**Found by:** 0x37, 0xPhantom2, 0xc0ffEE, 0xe4669da, ExtraCaterpillar, Falendar, KaplanLabs, Maroutis, Nave765, bbl4de, dany.armstrong90, davidjohn241018, dhank, dimulski, durov, jsmi, momentum, newspacexyz, shaflow01, ydlee

When a borrower extends the loan duration, they are required to pay additional fees for the extended time. However, due to a calculation error, this fee may be incorrect, potentially causing the user to pay more than necessary.

[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/1465ba6884c4cc44f7fc28e51f792db346ab1e33/Debita-V3-Contracts/contracts/DebitaV3Loan.sol#L602)

\u0060\u0060\u0060solidity
// if user already paid the max fee, then we dont have to charge them again
if (PorcentageOfFeePaid != maxFee) {
    // calculate difference from fee paid for the initialDuration vs the extra fee
    they should pay because of the extras days of extending the loan. MAXFEE
    shouldnt be higher than extra fee + PorcentageOfFeePaid
    uint feeOfMaxDeadline = ((offer.maxDeadline * feePerDay) / 86400);
    if (feeOfMaxDeadline > maxFee) {
        feeOfMaxDeadline = maxFee;
    } else if (feeOfMaxDeadline < feePerDay) {
        feeOfMaxDeadline = feePerDay;
    }
    misingBorrowFee = feeOfMaxDeadline - PorcentageOfFeePaid;
}
\u0060\u0060\u0060

The calculation for \u0060feeOfMaxDeadline\u0060 should be:  
\u0060extendedLoanDuration * feePerDay\u0060,  
where \u0060extendedLoanDuration\u0060 represents the extended borrowing time. However, the function mistakenly uses the timestamp directly for calculations, leading to an incorrect fee computation.
No response

No response

No response

The user might end up paying significantly higher fees than expected, leading to potential financial losses.

No response

\u0060\u0060\u0060solidity
// if user already paid the max fee, then we dont have to charge
// them again
if (PorcentageOfFeePaid != maxFee) {
    // calculate difference from fee paid for the initialDuration
    // vs the extra fee they should pay because of the extras days of extending the
    // loan. MAXFEE shouldnt be higher than extra fee + PorcentageOfFeePaid
    uint feeOfMaxDeadline = (((offer.maxDeadline - loanData.startedAt) * feePerDay) / 86400);
    if (feeOfMaxDeadline > maxFee) {
        feeOfMaxDeadline = maxFee;
    } else if (feeOfMaxDeadline < feePerDay) {
        feeOfMaxDeadline = feePerDay;
    }
    misingBorrowFee = feeOfMaxDeadline - PorcentageOfFeePaid;
}
\u0060\u0060\u0060

**sherlock-admin2**  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/63f8c4b1e4e7df734bf0926  
→ 0bd951f2c3e0da736
