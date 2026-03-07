# Some reward tokens will require too high reward values

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wenwin
**Keywords:** cybersecurity, vulnerability, lotteries, high-value tokens, rewards values, units division, rounding problem, reward token, USD, decimals, minimum reward, winTier, divisor, rewards, manual review, mitigation steps, precision, modulo check, smaller divisor, token economics

---

# Lines of code

https://github.com/code-423n4/2023-03-wenwin/blob/main/src/LotterySetup.sol#L171


# Vulnerability details

## Impact
Lotteries with high-value tokens will require having too big rewards values due to units division rounding problem.

## Proof of Concept
Consider the case where the reward token ($TKN) has a value of 1000 USD per token and 6 decimals (decimals doesn\u0027t matter in this case).

The minimum reward that can be set for a winTier will have to be at least >= 100 USD because of the following 2 checks:

\u0060\u0060\u0060diff
 168:   uint256 divisor = 10 ** (IERC20Metadata(address(rewardToken)).decimals() - 1); // @audit <- PoC
 169:   for (uint8 winTier = 1; winTier < selectionSize; ++winTier) {
 170:       uint16 reward = uint16(rewards[winTier] / divisor);
 171:       if ((rewards[winTier] % divisor) != 0) { // @audit <- PoC
 172:           revert InvalidFixedRewardSetup();
 173:       }
\u0060\u0060\u0060
https://github.com/code-423n4/2023-03-wenwin/blob/main/src/LotterySetup.sol#L168-L173

1. We want a \u0060rewards[3]\u0060 to be 1.5 USD or 0.0015 TKN = 15e2 units
2. \u0060divisor\u0060 = 1e5;
3. \u0060reward\u0060 will be 0;
4. \u0060rewards[winTier] % divisor\u0060 will be 15e2 since \u0060rewards[3]\u0060 is < \u0060divisor\u0060
5. Lottery can\u0027t be set up with reward token $TKN unless the minimum rewards is 100 USD

## Tools Used
Manual review

## Recommended Mitigation Steps
Consider implementing one of the following changes for better precision:

1. Remove the modulo check

\u0060\u0060\u0060diff
- 171:    if ((rewards[winTier] % divisor) != 0) {
\u0060\u0060\u0060
https://github.com/code-423n4/2023-03-wenwin/blob/main/src/LotterySetup.sol#L171

2. Smaller divisior:

\u0060\u0060\u0060diff
- 168:    uint256 divisor = 10 ** (IERC20Metadata(address(rewardToken)).decimals() - 1);
+ 168:    uint256 divisor = 10 ** (IERC20Metadata(address(rewardToken)).decimals() - 5);
\u0060\u0060\u0060
https://github.com/code-423n4/2023-03-wenwin/blob/main/src/LotterySetup.sol#L168
