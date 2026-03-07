# tnquanghuy0512 - \u0060_distribute()\u0060 function in RFPSimpleStrategy contract has wrong requirement causing DOS

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, DOS, distribute function, RFPSimpleStrategy, contract, pool manager, milestones, recipient, proposal bid, smart contract, Ethereum, token distribution, manual review, security flaw, blockchain, funding, payment failure, contract requirements, code review

---

tnquanghuy0512

medium

# \u0060_distribute()\u0060 function in RFPSimpleStrategy contract has wrong requirement causing DOS
\u0060_distribute()\u0060 function in RFPSimpleStrategy contract has wrong requirement causing DOS
## Vulnerability Detail
The function \u0060_distribute()\u0060:
\u0060\u0060\u0060solidity
    function _distribute(address[] memory, bytes memory, address _sender)
        internal
        virtual
        override
        onlyInactivePool
        onlyPoolManager(_sender)
    {
        ...

        IAllo.Pool memory pool = allo.getPool(poolId);
        Milestone storage milestone = milestones[upcomingMilestone];
        Recipient memory recipient = _recipients[acceptedRecipientId];

        if (recipient.proposalBid > poolAmount) revert NOT_ENOUGH_FUNDS();

        uint256 amount = (recipient.proposalBid * milestone.amountPercentage) / 1e18;

        poolAmount -= amount;//<@@ NOTICE the poolAmount get decrease over time

        _transferAmount(pool.token, recipient.recipientAddress, amount);

        ...
    }
\u0060\u0060\u0060

Let\u0027s suppose this scenario:
 - Pool manager funding the contract with 100 token, making \u0060poolAmount\u0060 variable equal to 100
 - Pool manager set 5 equal milestones with 20% each
 - Selected recipient\u0027s proposal bid is 100, making \u0060recipients[acceptedRecipientId].proposalBid\u0060 variable equal to 100
 - After milestone 1 done, pool manager pays recipient using \u0060distribute()\u0060. Value of variables after:  \u0060poolAmount = 80 ,recipients[acceptedRecipientId].proposalBid = 100\u0060
 - After milestone 2 done, pool manager will get DOS trying to pay recipient using \u0060distribute()\u0060 because of this line:
 \u0060\u0060\u0060solidity
if (recipient.proposalBid > poolAmount) revert NOT_ENOUGH_FUNDS();
\u0060\u0060\u0060
## Impact
This behaviour will cause DOS when distributing the 2nd milestone or higher
## Code Snippet
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/6430c8004017e96ae2f5aac365bdefd0b6eeea72/allo-v2/contracts/strategies/rfp-simple/RFPSimpleStrategy.sol#L417C1-L450C6
## Tool used

Manual Review

## Recommendation
\u0060\u0060\u0060solidity
-        if (recipient.proposalBid > poolAmount) revert NOT_ENOUGH_FUNDS();
+        if ((recipient.proposalBid * milestone.amountPercentage) / 1e18 > poolAmount) revert NOT_ENOUGH_FUNDS();
\u0060\u0060\u0060
