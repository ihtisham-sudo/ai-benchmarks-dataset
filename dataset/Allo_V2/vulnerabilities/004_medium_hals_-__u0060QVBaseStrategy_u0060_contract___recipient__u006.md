# hals - \u0060QVBaseStrategy\u0060 contract : recipient \u0060reviewStatus\u0060 is not reset upon re-registration

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, QVBaseStrategy, contract, recipient, reviewStatus, re-registration, status update, Pending, Accepted, Rejected, Appealed, reviewRecipients, reviewThreshold, manual review, code snippet, impact, recommendation, function update, recipientId

---

hals

medium

# \u0060QVBaseStrategy\u0060 contract : recipient \u0060reviewStatus\u0060 is not reset upon re-registration

\u0060QVBaseStrategy\u0060 contract : the reviewStatus of the recipient is not reset (set to zero) when he re-registres again.

## Vulnerability Detail

- In \u0060QVBaseStrategy\u0060 strategy contract: when the user first registers; his status is updated from \u0060None\u0060 to \u0060Pending\u0060.

- Then the pool manager can review recipients (via \u0060reviewRecipients\u0060 function) and update their statuses from \u0060Pending\u0060 to \u0060Accepted\u0060 and from \u0060Accepted\u0060 to \u0060Pending\u0060 only (not updating to \u0060Rejected\u0060 or \u0060Appealed\u0060) if these recipients statuses got votes equal to \u0060reviewThreshold\u0060:

  [QVBaseStrategy::reviewRecipients /L275-280](https://github.com/allo-protocol/allo-v2/blob/0b881ef4a0013d2809374c9ea69f4cf1288dfe62/contracts/strategies/qv-base/QVBaseStrategy.sol#L275-L280)

  \u0060\u0060\u0060solidity
              if (reviewsByStatus[recipientId][recipientStatus] >= reviewThreshold) {
                  Recipient storage recipient = recipients[recipientId];
                  recipient.recipientStatus = recipientStatus;

                  emit RecipientStatusUpdated(recipientId, recipientStatus, address(0));
              }
  \u0060\u0060\u0060

- The strategy contract allows registered recipients to re-register again with new terms; and when doing so, their statuses are updated from \u0060Accepted\u0060 ==> \u0060Pending\u0060 or from \u0060Rejected\u0060 to \u0060Appealed\u0060:

  [QVBaseStrategy::\_registerRecipient /L275-280](https://github.com/allo-protocol/allo-v2/blob/0b881ef4a0013d2809374c9ea69f4cf1288dfe62/contracts/strategies/qv-base/QVBaseStrategy.sol#L414-L429)

  \u0060\u0060\u0060solidity
  if (currentStatus == Status.None) {
            // recipient registering new application
            recipient.recipientStatus = Status.Pending;
            emit Registered(recipientId, _data, _sender);
        } else {
            if (currentStatus == Status.Accepted) {
                // recipient updating accepted application
                recipient.recipientStatus = Status.Pending;
            } else if (currentStatus == Status.Rejected) {
                // recipient updating rejected application
                recipient.recipientStatus = Status.Appealed;
            }

            // emit the new status with the \u0027_data\u0027 that was passed in
            emit UpdatedRegistration(recipientId, _data, _sender, recipient.recipientStatus);
        }
  \u0060\u0060\u0060

## Impact

But as can be noticed; the reviewRecipient status of the re-registered recipient is not reset which will result in this re-registered recipient getting \u0060Accepted\u0060 status on their new registration in the next review round/rounds with lesser votes to reach \u0060reviewThreshold\u0060.

## Code Snippet

[QVBaseStrategy::\_registerRecipient /L275-280](https://github.com/allo-protocol/allo-v2/blob/0b881ef4a0013d2809374c9ea69f4cf1288dfe62/contracts/strategies/qv-base/QVBaseStrategy.sol#L414-L429)

\u0060\u0060\u0060solidity
if (currentStatus == Status.None) {
          // recipient registering new application
          recipient.recipientStatus = Status.Pending;
          emit Registered(recipientId, _data, _sender);
      } else {
          if (currentStatus == Status.Accepted) {
              // recipient updating accepted application
              recipient.recipientStatus = Status.Pending;
          } else if (currentStatus == Status.Rejected) {
              // recipient updating rejected application
              recipient.recipientStatus = Status.Appealed;
          }

          // emit the new status with the \u0027_data\u0027 that was passed in
          emit UpdatedRegistration(recipientId, _data, _sender, recipient.recipientStatus);
      }
\u0060\u0060\u0060

[QVBaseStrategy::reviewRecipients ](https://github.com/allo-protocol/allo-v2/blob/0b881ef4a0013d2809374c9ea69f4cf1288dfe62/contracts/strategies/qv-base/QVBaseStrategy.sol#L254-L288)

\u0060\u0060\u0060solidity
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
          if (recipientStatus == Status.None || recipientStatus == Status.Appealed) {
              revert RECIPIENT_ERROR(recipientId);
          }

          reviewsByStatus[recipientId][recipientStatus]++;

          if (reviewsByStatus[recipientId][recipientStatus] >= reviewThreshold) {
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

Update \u0060_registerRecipient\u0060 function to reset \u0060reviewsByStatus[recipientId][recipientStatus]\u0060 when the recipient re-registers:

\u0060\u0060\u0060diff
if (currentStatus == Status.None) {
          // recipient registering new application
          recipient.recipientStatus = Status.Pending;
          emit Registered(recipientId, _data, _sender);
      } else {
          if (currentStatus == Status.Accepted) {
              // recipient updating accepted application
              recipient.recipientStatus = Status.Pending;
+             reviewsByStatus[recipientId][Status.Accepted]=0;
          } else if (currentStatus == Status.Rejected) {
              // recipient updating rejected application
              recipient.recipientStatus = Status.Appealed;
          }

          // emit the new status with the \u0027_data\u0027 that was passed in
          emit UpdatedRegistration(recipientId, _data, _sender, recipient.recipientStatus);
      }
\u0060\u0060\u0060
