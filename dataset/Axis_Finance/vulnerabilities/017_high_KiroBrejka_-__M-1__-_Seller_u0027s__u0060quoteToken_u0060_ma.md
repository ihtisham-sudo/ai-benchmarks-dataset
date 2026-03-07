# KiroBrejka - [M-1] - Seller\u0027s \u0060quoteToken\u0060 may remain locked in the protocol under certain conditions

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axis Finance
**Keywords:** KiroBrejka, cyber security, vulnerability, quoteToken, locked funds, revert on 0 transfer, ERC20 Metadata, AuctionHouse, claimProceeds, batch auctions, prefunding, routing.funding, payoutSent, prefundingRefund, baseToken, transfer, manual review, impact, recommendation, smart contract

---

KiroBrejka

high

# [M-1] - Seller\u0027s \u0060quoteToken\u0060 may remain locked in the protocol under certain conditions

## Summary
Seller\u0027s funds may remain locked in the protocol, because of revert on 0 transfer tokens.
In the README.md file is stated that the protocol uses every token with ERC20 Metadata and decimals between 6-18, which includes some revert on 0 transfer tokens, so this should be considered as valid issue!

## Vulnerability Detail
in the \u0060AuctionHouse::claimProceeds()\u0060 function there is the following block of code:
\u0060\u0060\u0060javascript
       uint96 prefundingRefund = routing.funding + payoutSent_ - sold_;
        unchecked {
            routing.funding -= prefundingRefund;
        }
        Transfer.transfer(
            routing.baseToken,
            _getAddressGivenCallbackBaseTokenFlag(routing.callbacks, routing.seller),
            prefundingRefund,
            false
        );
\u0060\u0060\u0060
Since the batch auctions must be prefunded so \u0060routing.funding\u0060 shouldn’t be zero unless all the tokens were sent in settle, in which case \u0060payoutSent\u0060 will equal \u0060sold_\u0060. From this we make the conclusion that it is possible for \u0060prefundingRefund\u0060 to be equal to 0. This means if the \u0060routing.baseToken\u0060 is a revert on 0 transfer token the seller will never be able to get the \u0060quoteToken\u0060 he should get from the auction.

## Impact
The seller\u0027s funds remain locked in the system and he will never be able to get them back.

## Code Snippet
The problematic block of code in the \u0060AuctionHouse::claimProceeds()\u0060 function:
https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/AuctionHouse.sol#L604-L613

\u0060Transfer::transfer()\u0060 function, since it transfers the \u0060baseToken\u0060:
https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/lib/Transfer.sol#L49-L68

## Tool used

Manual Review

## Recommendation
Check if the \u0060prefundingRefund > 0\u0060 like this:
\u0060\u0060\u0060diff
   function claimProceeds(
        uint96 lotId_,
        bytes calldata callbackData_
    ) external override nonReentrant {
        // Validation
        _isLotValid(lotId_);

        // Call auction module to validate and update data
        (uint96 purchased_, uint96 sold_, uint96 payoutSent_) =
            _getModuleForId(lotId_).claimProceeds(lotId_);

        // Load data for the lot
        Routing storage routing = lotRouting[lotId_];

        // Calculate the referrer and protocol fees for the amount in
        // Fees are not allocated until the user claims their payout so that we don\u0027t have to iterate through them here
        // If a referrer is not set, that portion of the fee defaults to the protocol
        uint96 totalInLessFees;
        {
            (, uint96 toProtocol) = calculateQuoteFees(
                lotFees[lotId_].protocolFee, lotFees[lotId_].referrerFee, false, purchased_
            );
            unchecked {
                totalInLessFees = purchased_ - toProtocol;
            }
        }

        // Send payment in bulk to the address dictated by the callbacks address
        // If the callbacks contract is configured to receive quote tokens, send the quote tokens to the callbacks contract and call the onClaimProceeds callback
        // If not, send the quote tokens to the seller and call the onClaimProceeds callback
        _sendPayment(routing.seller, totalInLessFees, routing.quoteToken, routing.callbacks);

        // Refund any unused capacity and curator fees to the address dictated by the callbacks address
        // By this stage, a partial payout (if applicable) and curator fees have been paid, leaving only the payout amount (\u0060totalOut\u0060) remaining.
        uint96 prefundingRefund = routing.funding + payoutSent_ - sold_;
++ if(prefundingRefund > 0) { 
        unchecked {
            routing.funding -= prefundingRefund;
        }
            Transfer.transfer(
            routing.baseToken,
            _getAddressGivenCallbackBaseTokenFlag(routing.callbacks, routing.seller),
            prefundingRefund,
            false
        );
++        }
       

        // Call the onClaimProceeds callback
        Callbacks.onClaimProceeds(
            routing.callbacks, lotId_, totalInLessFees, prefundingRefund, callbackData_
        );
    }
\u0060\u0060\u0060

