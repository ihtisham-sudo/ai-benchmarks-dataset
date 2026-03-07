# GimelSec - \u0060QVSimpleStrategy\u0060 never updates \u0060allocator.voiceCredits\u0060.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, QVSimpleStrategy, allocator, voiceCredits, credit limit, vote allocation, vote bypass, maxVoiceCreditsPerAllocator, allocated votes, impact, unlimited votes, code review, manual review, security flaw, risk assessment, software update, recommendation, system integrity, exploitation

---

GimelSec

high

# \u0060QVSimpleStrategy\u0060 never updates \u0060allocator.voiceCredits\u0060.

Every allocator in \u0060QVSimpleStrategy\u0060 has a maximum credit limit. An allocator should not be able to bypass the limit. However, \u0060QVSimpleStrategy\u0060 fails to record the allocated votes. An allocator can vote as many as possible.

## Vulnerability Detail

\u0060QVSimpleStrategy._allocate\u0060 calls \u0060_hasVoiceCreditsLeft\u0060 to check that the recipient has voice credits left to allocate.
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-simple/QVSimpleStrategy.sol#L121
\u0060\u0060\u0060solidity
    function _allocate(bytes memory _data, address _sender) internal virtual override {
        …

        // check that the recipient has voice credits left to allocate
        if (!_hasVoiceCreditsLeft(voiceCreditsToAllocate, allocator.voiceCredits)) revert INVALID();

        _qv_allocate(allocator, recipient, recipientId, voiceCreditsToAllocate, _sender);
    }
\u0060\u0060\u0060

\u0060QVSimpleStrategy._hasVoiceCreditsLeft\u0060 checks \u0060 _voiceCreditsToAllocate + _allocatedVoiceCredits <= maxVoiceCreditsPerAllocator\u0060
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-simple/QVSimpleStrategy.sol#L144
\u0060\u0060\u0060solidity
    function _hasVoiceCreditsLeft(uint256 _voiceCreditsToAllocate, uint256 _allocatedVoiceCredits)
        internal
        view
        override
        returns (bool)
    {
        return _voiceCreditsToAllocate + _allocatedVoiceCredits <= maxVoiceCreditsPerAllocator;
    }
\u0060\u0060\u0060

The problem is that \u0060allocator.voiceCredits\u0060 is always zero. Both \u0060QVSimpleStrategy\u0060 and \u0060QVBaseStrategy\u0060 don\u0027t update \u0060allocator.voiceCredits\u0060. Thus, allocators can cast more votes than \u0060maxVoiceCreditsPerAllocator\u0060.

## Impact

Every allocator has an unlimited number of votes.

## Code Snippet

https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-simple/QVSimpleStrategy.sol#L121
https://github.com/sherlock-audit/2023-09-Gitcoin/blob/main/allo-v2/contracts/strategies/qv-simple/QVSimpleStrategy.sol#L144


## Tool used

Manual Review

## Recommendation

Updates \u0060allocator.voiceCredits\u0060 in  \u0060QVSimpleStrategy._allocate\u0060.

\u0060\u0060\u0060diff
    function _allocate(bytes memory _data, address _sender) internal virtual override {
        …

        // check that the recipient has voice credits left to allocate
        if (!_hasVoiceCreditsLeft(voiceCreditsToAllocate, allocator.voiceCredits)) revert INVALID();
+       allocator.voiceCredits += voiceCreditsToAllocate;
        _qv_allocate(allocator, recipient, recipientId, voiceCreditsToAllocate, _sender);
    }
\u0060\u0060\u0060
