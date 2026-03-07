# lil.eth - Exponential Inflation of Voice Credits in Quadratic Voting Strategy

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, quadratic voting, voice credits, exponential inflation, voting integrity, code snippet, totalCredits, creditsCastToRecipient, voiceCreditsCastToRecipient, transaction manipulation, impact assessment, trust in voting, allocation strategy, voting outcome, credit accumulation, code review, recommendation, proof of concept, manipulation risk

---

lil.eth

medium

# Exponential Inflation of Voice Credits in Quadratic Voting Strategy
The current implementation of the \u0060_qv_allocate\u0060 function in the quadratic voting strategy lead to an exponential inflation of voice credits cast to a recipient due to repeated addition of previous allocations. This will significantly distort the voting outcome and undermine the integrity of the voting system

## Vulnerability Detail
In the given code snippet, we observe a potential issue in the way voice credits are being accumulated for each recipient. The specific lines of code in question are:
\u0060\u0060\u0060solidity
function _qv_allocate(
        ...
    ) internal onlyActiveAllocation {
        ...
        uint256 creditsCastToRecipient = _allocator.voiceCreditsCastToRecipient[_recipientId];
        ...
        // get the total credits and calculate the vote result
        uint256 totalCredits = _voiceCreditsToAllocate + creditsCastToRecipient;
        ...
        //E update allocator mapping voice for this recipient
        _allocator.voiceCreditsCastToRecipient[_recipientId] += totalCredits; //E @question should be only _voiceCreditsToAllocate
        ...
    }
\u0060\u0060\u0060
We can see that at the end : 
\u0060\u0060\u0060solidity
_allocator.voiceCreditsCastToRecipient[_recipientId] = _allocator.voiceCreditsCastToRecipient[_recipientId] + _voiceCreditsToAllocate +  _allocator.voiceCreditsCastToRecipient[_recipientId];
\u0060\u0060\u0060

Here, totalCredits accumulates both the newly allocated voice credits (\u0060_voiceCreditsToAllocate\u0060) and the credits previously cast to this recipient (\u0060creditsCastToRecipient\u0060). Later on, this totalCredits is added again to \u0060voiceCreditsCastToRecipient[_recipientId]\u0060, thereby including the previously cast credits once more

### Proof of Concept (POC):
Let\u0027s consider a scenario where a user allocates credits in three separate transactions:

1. Transaction 1: Allocates 5 credits
- creditsCastToRecipient initially is 0
- totalCredits = 5 (5 + 0)
- New voiceCreditsCastToRecipient[_recipientId] = 5

2. Transaction 2: Allocates another 5 credits
- creditsCastToRecipient now is 5 (from previous transaction)
- totalCredits = 10 (5 + 5)
- New voiceCreditsCastToRecipient[_recipientId] = 15 (10 + 5)

3. Transaction 3: Allocates another 5 credits
- creditsCastToRecipient now is 15
- totalCredits = 20 (5 + 15)
- New voiceCreditsCastToRecipient[_recipientId] = 35 (20 + 15)

From the above, we can see that the voice credits cast to the recipient are exponentially growing with each transaction instead of linearly increasing by 5 each time

## Impact
Exponential increase in the voice credits attributed to a recipient, significantly skewing the results of the voting strategy( if one recipient receive 15 votes in one vote and another one receive 5 votes 3 times, the second one will have 20 votes and the first one 15)
Over time, this could allow for manipulation and loss of trust in the voting mechanism and the percentage of amount received by recipients as long as allocations are used to calculate the match amount they will receive from the pool amount.

## Code Snippet

https://github.com/allo-protocol/allo-v2/blob/main/contracts/strategies/qv-base/QVBaseStrategy.sol#L529

## Tool used

Manual Review

## Recommendation
Code should be modified to only add the new voice credits to the recipient\u0027s tally. The modified line of code should look like:
\u0060\u0060\u0060solidity
_allocator.voiceCreditsCastToRecipient[_recipientId] += _voiceCreditsToAllocate;
\u0060\u0060\u0060
