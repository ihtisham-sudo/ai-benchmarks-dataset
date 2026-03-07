# GimelSec - \u0060recipientsCounter\u0060 should start from 1 in \u0060DonationVotingMerkleDistributionBaseStrategy\u0060

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, DonationVotingMerkleDistributionBaseStrategy, recipientsCounter, Status.None, recipientId, recipientToStatusIndexes, registerRecipient, application status, index computation, manual review, implementation error, pool recording, counter initialization, error mitigation, smart contract, blockchain security, recipient status, status management, code review

---

GimelSec

high

# \u0060recipientsCounter\u0060 should start from 1 in \u0060DonationVotingMerkleDistributionBaseStrategy\u0060

When doing \u0060DonationVotingMerkleDistributionBaseStrategy._registerRecipient\u0060, it checks the current status of the recipient. If the recipient is new to the pool, the status should be \u0060Status.None\u0060. However, \u0060recipientsCounter\u0060 starts from 0. The new recipient actually gets the status of first recipient of the pool.

## Vulnerability Detail

\u0060DonationVotingMerkleDistributionBaseStrategy._registerRecipient\u0060 calls \u0060_getUintRecipientStatus\u0060 to get the current status of the application. The status of the new application should be \u0060Status.None\u0060. Then, the \u0060recipientToStatusIndexes[recipientId]\u0060  to \u0060recipientsCounter\u0060 and \u0060recipientsCounter\u0060.
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L580
\u0060\u0060\u0060solidity
    function _registerRecipient(bytes memory _data, address _sender)
        internal
        override
        onlyActiveRegistration
        returns (address recipientId)
    {
        …

        uint8 currentStatus = _getUintRecipientStatus(recipientId);

        if (currentStatus == uint8(Status.None)) {
            // recipient registering new application
            recipientToStatusIndexes[recipientId] = recipientsCounter;
            _setRecipientStatus(recipientId, uint8(Status.Pending));

            bytes memory extendedData = abi.encode(_data, recipientsCounter);
            emit Registered(recipientId, extendedData, _sender);

            recipientsCounter++;
        } else {
            if (currentStatus == uint8(Status.Accepted)) {
                // recipient updating accepted application
                _setRecipientStatus(recipientId, uint8(Status.Pending));
            } else if (currentStatus == uint8(Status.Rejected)) {
                // recipient updating rejected application
                _setRecipientStatus(recipientId, uint8(Status.Appealed));
            }
            emit UpdatedRegistration(recipientId, _data, _sender, _getUintRecipientStatus(recipientId));
        }
    }
\u0060\u0060\u0060

\u0060DonationVotingMerkleDistributionBaseStrategy._getUintRecipientStatus\u0060 calls \u0060_getStatusRowColumn\u0060 to get the column index and current row.
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L819
\u0060\u0060\u0060solidity
    function _getUintRecipientStatus(address _recipientId) internal view returns (uint8 status) {
        // Get the column index and current row
        (, uint256 colIndex, uint256 currentRow) = _getStatusRowColumn(_recipientId);

        // Get the status from the \u0027currentRow\u0027 shifting by the \u0027colIndex\u0027
        status = uint8((currentRow >> colIndex) & 15);

        // Return the status
        return status;
    }
\u0060\u0060\u0060

\u0060DonationVotingMerkleDistributionBaseStrategy._getStatusRowColumn\u0060 computes indexes from \u0060recipientToStatusIndexes[_recipientId]\u0060. For the new recipient. Those indexes should be zero.
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L833
\u0060\u0060\u0060solidity
    function _getStatusRowColumn(address _recipientId) internal view returns (uint256, uint256, uint256) {
        uint256 recipientIndex = recipientToStatusIndexes[_recipientId];

        uint256 rowIndex = recipientIndex / 64; // 256 / 4
        uint256 colIndex = (recipientIndex % 64) * 4;

        return (rowIndex, colIndex, statusesBitMap[rowIndex]);
    }
\u0060\u0060\u0060

The problem is that \u0060recipientCounter\u0060 starts from zero.
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L166
\u0060\u0060\u0060solidity
    /// @notice The total number of recipients.
    uint256 public recipientsCounter;
\u0060\u0060\u0060

Consider the following situation:
* Alice is the first recipient calls \u0060registerRecipient\u0060
\u0060\u0060\u0060solidity
// in _registerRecipient
recipientToStatusIndexes[Alice] = recipientsCounter = 0;
_setRecipientStatus(Alice, uint8(Status.Pending));
recipientCounter++
\u0060\u0060\u0060
* Bob calls \u0060registerRecipient\u0060.
\u0060\u0060\u0060solidity
// in _getStatusRowColumn
recipientToStatusIndexes[Bob] = 0 // It would access the status of Alice
// in _registerRecipient
currentStatus = _getUintRecipientStatus(recipientId) = Status.Pending
currentStatus != uint8(Status.None) -> no new application is recorded in the pool.
\u0060\u0060\u0060

This implementation error makes the pool can only record the first application.

## Impact

## Code Snippet

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L580
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L819
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L833
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/donation-voting-merkle-base/DonationVotingMerkleDistributionBaseStrategy.sol#L166

## Tool used

Manual Review

## Recommendation

Make the counter start from 1. There are two methods to fix the  issue.

1.
\u0060\u0060\u0060diff
    /// @notice The total number of recipients.
+   uint256 public recipientsCounter;
-   uint256 public recipientsCounter;
\u0060\u0060\u0060

2.
\u0060\u0060\u0060diff
    function _registerRecipient(bytes memory _data, address _sender)
        internal
        override
        onlyActiveRegistration
        returns (address recipientId)
    {
        …

        uint8 currentStatus = _getUintRecipientStatus(recipientId);

        if (currentStatus == uint8(Status.None)) {
            // recipient registering new application
+           recipientToStatusIndexes[recipientId] = recipientsCounter + 1;
-           recipientToStatusIndexes[recipientId] = recipientsCounter;
            _setRecipientStatus(recipientId, uint8(Status.Pending));

            bytes memory extendedData = abi.encode(_data, recipientsCounter);
            emit Registered(recipientId, extendedData, _sender);

            recipientsCounter++;
        …
    }
\u0060\u0060\u0060
