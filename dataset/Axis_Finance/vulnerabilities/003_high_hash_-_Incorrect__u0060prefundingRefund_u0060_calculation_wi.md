# hash - Incorrect \u0060prefundingRefund\u0060 calculation will disallow claiming

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axis Finance
**Keywords:** cybersecurity, vulnerability, prefundingRefund, claimProceeds, underflow, routing.funding, capacity, curator fees, payout, bidders, claim, function, impact, code snippet, manual review, recommendation, calculation error, smart contract, blockchain, funding

---

hash

high

# Incorrect \u0060prefundingRefund\u0060 calculation will disallow claiming

## Summary
Incorrect \u0060prefundingRefund\u0060 calculation will lead to underflow and hence disallowing claiming

## Vulnerability Detail

The \u0060prefundingRefund\u0060 variable calculation inside the \u0060claimProceeds\u0060 function is incorrect

\u0060\u0060\u0060solidity
    function claimProceeds(
        uint96 lotId_,
        bytes calldata callbackData_
    ) external override nonReentrant {
        
        ...

        (uint96 purchased_, uint96 sold_, uint96 payoutSent_) =
            _getModuleForId(lotId_).claimProceeds(lotId_);

        ....

        // Refund any unused capacity and curator fees to the address dictated by the callbacks address
        // By this stage, a partial payout (if applicable) and curator fees have been paid, leaving only the payout amount (\u0060totalOut\u0060) remaining.
        uint96 prefundingRefund = routing.funding + payoutSent_ - sold_;
        unchecked {
            routing.funding -= prefundingRefund;
        }
\u0060\u0060\u0060

Here \u0060sold\u0060 is the total base quantity that has been sold to the bidders. Unlike required, the \u0060routing.funding\u0060 variable need not be holding \u0060capacity + (0,curator fees)\u0060 since it is decremented every time a payout of a bid is claimed

\u0060\u0060\u0060solidity
    function claimBids(uint96 lotId_, uint64[] calldata bidIds_) external override nonReentrant {
        
        ....

            if (bidClaim.payout > 0) {
 
                ...

                // Reduce funding by the payout amount
                unchecked {
                    routing.funding -= bidClaim.payout;
                }
\u0060\u0060\u0060

### Example
Capacity = 100 prefunded, hence routing.funding == 100 initially
Sold = 90 and no partial fill/curation
All bidders claim before the claimProceed function is invoked
Hence routing.funding = 100 - 90 == 10
When claimProceeds is invoked, underflow and revert:

uint96 prefundingRefund = routing.funding + payoutSent_ - sold_ == 10 + 0 - 90

## Impact

Claim proceeds function is broken. Sellers won\u0027t be able to receive the proceedings

## Code Snippet

wrong calculation
https://github.com/sherlock-audit/2024-03-axis-finance/blob/cadf331f12b485bac184111cdc9ba1344d9fbf01/moonraker/src/AuctionHouse.sol#L604

## Tool used

Manual Review

## Recommendation

Change the calculation to:
\u0060\u0060\u0060solidity
uint96 prefundingRefund = capacity - sold_ + curatorFeesAdjustment (how much was prefunded initially - how much will be sent out based on capacity - sold)
\u0060\u0060\u0060
