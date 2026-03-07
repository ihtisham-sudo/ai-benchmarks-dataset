# osmanozdemir1 - \u0060QVBaseStrategy::reviewRecipients()\u0060 doesn\u0027t check if the recipient is already accepted or rejected, and overwrites the current status

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, smart contracts, recipient status, overwriting, reviewRecipients, reviewThreshold, pool manager, acceptance, rejection, status update, current status check, previous review counts, PoC, test scenario, manual review, code snippet, impact assessment, mitigation recommendation, blockchain security

---

osmanozdemir1

medium

# \u0060QVBaseStrategy::reviewRecipients()\u0060 doesn\u0027t check if the recipient is already accepted or rejected, and overwrites the current status
There is a \u0060reviewThreshold\u0060 in the \u0060QVBaseStrategy\u0060 contract to update the recipient\u0027s status. But \u0060QVBaseStrategy::reviewRecipients()\u0060 doesn\u0027t check the current status and immediately overwrites when the threshold is reached.

## Vulnerability Detail
In the QV strategy contracts, recipients register themselves and wait for a pool manager to accept the registration. Pool managers can accept or reject recipients with the \u0060reviewRecipients()\u0060 function. There is also a threshold (\u0060reviewThreshold\u0060) for recipients to be accepted. For example, if the \u0060reviewThreshold\u0060 is 2, a pending recipient gets accepted when two managers accept this recipient and the \u0060recipientStatus\u0060 is updated.

However, \u0060QVBaseStrategy::reviewRecipients()\u0060 function doesn\u0027t check the recipient\u0027s current status. This one alone may not be an issue because managers may want to change the status of the recipient etc.  
But on top of that, the function also doesn\u0027t take the previous review counts into account when updating the status, and overwrites the status immediately after reaching the threshold. I\u0027ll share a scenario later about this below.

Here is the \u0060reviewRecipients()\u0060 function:  
[https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L254C1-L288C6](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L254C1-L288C6)

\u0060\u0060\u0060solidity
file: QVBaseStrategy.sol
    function reviewRecipients(address[] calldata _recipientIds, Status[] calldata _recipientStatuses)
        external
        virtual
        onlyPoolManager(msg.sender)
        onlyActiveRegistration
    {
        // make sure the arrays are the same length
        uint256 recipientLength = _recipientIds.length;
        if (recipientLength != _recipientStatuses.length) revert INVALID();

        for (uint256 i; i < recipientLength;) {
            Status recipientStatus = _recipientStatuses[i];
            address recipientId = _recipientIds[i];

            // if the status is none or appealed then revert
            if (recipientStatus == Status.None || recipientStatus == Status.Appealed) { //@audit these are the input parameter statuse not the recipient\u0027s status.
                revert RECIPIENT_ERROR(recipientId);
            }

            reviewsByStatus[recipientId][recipientStatus]++;

 -->        if (reviewsByStatus[recipientId][recipientStatus] >= reviewThreshold) { //@audit recipientStatus is updated right after the threshold is reached. It can overwrite if the status is already set.
                Recipient storage recipient = recipients[recipientId];
                recipient.recipientStatus = recipientStatus;

                emit RecipientStatusUpdated(recipientId, recipientStatus, address(0));
            }

            emit Reviewed(recipientId, recipientStatus, msg.sender);

            unchecked {
                ++i;
            }
        }
    }
\u0060\u0060\u0060

As I mentioned above, the function updates the \u0060recipientStatus\u0060 immediately after reaching the threshold. Here is a scenario of why this might be an issue.

**Example Scenario**  
The pool has 5 managers and the \u0060reviewThreshold\u0060 is 2.

1. The first manager rejects the recipient
    
2. The second manager accepts the recipient
    
3. The third manager rejects the recipient. -&gt; \u0060recipientStatus\u0060 updated -&gt; \u0060status = REJECTED\u0060
    
4. The fourth manager rejects the recipient -&gt; status still \u0060REJECTED\u0060
    
5. The last manager accepts the recipient -&gt;\u0060recipientStatus\u0060 updated again -&gt; \u0060status = ACCEPTED\u0060
    

*3 managers rejected and 2 managers accepted the recipient but the recipient status is overwritten without checking the recipient\u0027s previous status and is ACCEPTED now.*

## Coded PoC

You can prove the scenario above with the PoC. You can use the protocol\u0027s own setup for this.  
\- Copy the snippet below and paste it into the \u0060QVBaseStrategy.t.sol\u0060 test file.  
\- Run forge test \u0060--match-test test_reviewRecipient_reviewTreshold_OverwriteTheLastOne\u0060

\u0060\u0060\u0060solidity
//@audit More managers rejected but the recipient is accepted
    function test_reviewRecipient_reviewTreshold_OverwriteTheLastOne() public virtual {
        address recipientId = __register_recipient();

        // Create rejection status
        address[] memory recipientIds = new address[](1);
        recipientIds[0] = recipientId;
        IStrategy.Status[] memory Statuses = new IStrategy.Status[](1);
        Statuses[0] = IStrategy.Status.Rejected;

        // Reject three times with different managers
        vm.startPrank(pool_manager1());
        qvStrategy().reviewRecipients(recipientIds, Statuses);

        vm.startPrank(pool_manager2());
        qvStrategy().reviewRecipients(recipientIds, Statuses);

        vm.startPrank(pool_manager3());
        qvStrategy().reviewRecipients(recipientIds, Statuses);

        // Three managers rejected. Status will be rejected.
        assertEq(uint8(qvStrategy().getRecipientStatus(recipientId)), uint8(IStrategy.Status.Rejected));
        assertEq(qvStrategy().reviewsByStatus(recipientId, IStrategy.Status.Rejected), 3);

        // Accept two times after three rejections
        Statuses[0] = IStrategy.Status.Accepted;
        vm.startPrank(pool_admin());
        qvStrategy().reviewRecipients(recipientIds, Statuses);

        vm.startPrank(pool_manager4());
        qvStrategy().reviewRecipients(recipientIds, Statuses);

        // 3 Rejected, 2 Accepted, but status is Accepted because it overwrites right after passing threshold.
        assertEq(uint8(qvStrategy().getRecipientStatus(recipientId)), uint8(IStrategy.Status.Accepted));
        assertEq(qvStrategy().reviewsByStatus(recipientId, IStrategy.Status.Rejected), 3);
        assertEq(qvStrategy().reviewsByStatus(recipientId, IStrategy.Status.Accepted), 2);
    }
\u0060\u0060\u0060

You can find the test results below:

\u0060\u0060\u0060solidity
Running 1 test for test/foundry/strategies/QVSimpleStrategy.t.sol:QVSimpleStrategyTest
[PASS] test_reviewRecipient_reviewTreshold_OverwriteTheLastOne() (gas: 249604)
Test result: ok. 1 passed; 0 failed; 0 skipped; finished in 10.92ms
\u0060\u0060\u0060

## Impact
Recipient status might be overwritten with less review counts.

## Code Snippet
[https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L254C1-L288C6](https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-base/QVBaseStrategy.sol#L254C1-L288C6)

\u0060\u0060\u0060solidity
file: QVBaseStrategy.sol
    function reviewRecipients(address[] calldata _recipientIds, Status[] calldata _recipientStatuses)
        external
        virtual
        onlyPoolManager(msg.sender)
        onlyActiveRegistration
    {
        // make sure the arrays are the same length
        uint256 recipientLength = _recipientIds.length;
        if (recipientLength != _recipientStatuses.length) revert INVALID();

        for (uint256 i; i < recipientLength;) {
            Status recipientStatus = _recipientStatuses[i];
            address recipientId = _recipientIds[i];

            // if the status is none or appealed then revert
            if (recipientStatus == Status.None || recipientStatus == Status.Appealed) { //@audit these are the input parameter statuse not the recipient\u0027s status.
                revert RECIPIENT_ERROR(recipientId);
            }

            reviewsByStatus[recipientId][recipientStatus]++;

 -->        if (reviewsByStatus[recipientId][recipientStatus] >= reviewThreshold) { //@audit recipientStatus is updated right after the threshold is reached. It can overwrite if the status is already set.
                Recipient storage recipient = recipients[recipientId];
                recipient.recipientStatus = recipientStatus;

                emit RecipientStatusUpdated(recipientId, recipientStatus, address(0));
            }

            emit Reviewed(recipientId, recipientStatus, msg.sender);

            unchecked {
                ++i;
            }
        }
    }
\u0060\u0060\u0060

## Tool used

Manual Review

## Recommendation
Checking the review counts before updating the state might be helpful to mitigate this issue
