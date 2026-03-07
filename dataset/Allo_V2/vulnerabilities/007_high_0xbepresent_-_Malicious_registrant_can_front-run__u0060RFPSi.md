# 0xbepresent - Malicious registrant can front-run \u0060RFPSimpleStrategy._allocate()\u0060 in order to change the \u0060proposalBid\u0060 and get a bigger payout in the distribution

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, malicious registrant, front-running, RFPSimpleStrategy, proposalBid, payout, pool manager, registerRecipient, allocate, distribute, mempool, accepted registrant, non-agreed terms, impact, drain funds, manual review, recommendation, security flaw, smart contract

---

0xbepresent

high

# Malicious registrant can front-run \u0060RFPSimpleStrategy._allocate()\u0060 in order to change the \u0060proposalBid\u0060 and get a bigger payout in the distribution

The \u0060RFPSimpleStrategy::_allocate()\u0060 function can be frontrun by a malicious \u0060registrant\u0060 chainging the \u0060proposalBid\u0060 and get a bigger payout in the \u0060RFPSimpleStrategy::_distribute()\u0060 function.

## Vulnerability Detail

Users can register to the pool strategy using the [RFPSimpleStrategy::_registerRecipient()](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L314C14-L314C32) function specifying the [proposalBid](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L378) in the registration. Then the pool manager [accepts the \u0060registrant recipient\u0060](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L404) using the [RFPSimpleStrategy::_allocate()](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L386) function.

The problem is that the execution of the \u0060RFPSimpleStrategy::_allocate()\u0060 function by the \u0060pool manager\u0060 can be frontun by a malicious \u0060registrant recipient\u0060. Consider the next scenario:

1. \u0060UserA\u0060 call the \u0060RFPSimpleStrategy::_registerRecipient()\u0060 using a \u0060proposalBid=10\u0060.
2. Pool manager accepts the proposal by \u0060UserA\u0060 and call the \u0060RFPSimpleStrategy::_allocate()\u0060 function.
3. \u0060UserA\u0060 monitors the mempool and frontrun the manager \u0060_allocate()\u0060 execution changing the proposal now \u0060proposalBid=50\u0060.
4. The \u0060step 2\u0060 call finally is executed but the using non-agreed proposal \u0060proposalBid=50\u0060.

Now the \u0060UserA\u0060 is accepted registrant recipient with non-agreed proposal bid (\u0060proposalBid=50\u0060).

## Impact

Malicious registrant can change the \u0060proposalBid\u0060 to a non-agreed term causing that he can receive a bigger payout in the [RFPSimpleStrategy::_distribute()](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L417) function because in the [code line 435](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L435) the \u0060proposalBid\u0060 is used to calculate the amount to pay to the \u0060accepted registrant recipient\u0060:

\u0060\u0060\u0060solidity
File: RFPSimpleStrategy.sol
417:     function _distribute(address[] memory, bytes memory, address _sender)
418:         internal
419:         virtual
420:         override
421:         onlyInactivePool
422:         onlyPoolManager(_sender)
423:     {
...
...
433: 
434:         // Calculate the amount to be distributed for the milestone
435:         uint256 amount = (recipient.proposalBid * milestone.amountPercentage) / 1e18;
436: 
437:         // Get the pool, subtract the amount and transfer to the recipient
438:         poolAmount -= amount;
439:         _transferAmount(pool.token, recipient.recipientAddress, amount);
...
...
450:     }
\u0060\u0060\u0060

The malicious accepted registrant can drain all funds from the pool strategy using one milestone.

## Code Snippet

- [RFPSimpleStrategy::_registerRecipient()](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L314C14-L314C32)
- [RFPSimpleStrategy::_allocate()](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L386)
- [RFPSimpleStrategy::_distribute()](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L417)

## Tool used

Manual review

## Recommendation

Verify the \u0060proposalBid\u0060 when the \u0060_allocate()\u0060 occurs:

\u0060\u0060\u0060diff
    function _allocate(bytes memory _data, address _sender)
        internal
        virtual
        override
        nonReentrant
        onlyActivePool
        onlyPoolManager(_sender)
    {
        // Decode the \u0027_data\u0027
--      acceptedRecipientId = abi.decode(_data, (address));
++      (acceptedRecipientId, uint256 expectedProposalBid) = abi.decode(_data, (address, uint256));

        Recipient storage recipient = _recipients[acceptedRecipientId];

--      if (acceptedRecipientId == address(0) || recipient.recipientStatus != Status.Pending) {
++      if (acceptedRecipientId == address(0) || recipient.recipientStatus != Status.Pending || recipient.proposalBid != expectedProposalBid) {
            revert RECIPIENT_ERROR(acceptedRecipientId);
        }

        // Update status of acceptedRecipientId to accepted
        recipient.recipientStatus = Status.Accepted;

        _setPoolActive(false);

        IAllo.Pool memory pool = allo.getPool(poolId);

        // Emit event for the allocation
        emit Allocated(acceptedRecipientId, recipient.proposalBid, pool.token, _sender);
    }
\u0060\u0060\u0060
