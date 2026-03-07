# bughuntoor - Tax refund is calculated based on the wrong amount

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Zap Protocol
**Keywords:** cybersecurity, vulnerability, tax refund, allocation, USDC, private period, refund calculation, oversell, unused funds, tax-free allocation, user impact, financial error, manual review, code recommendation, security flaw, user deposits, refund policy, smart contract, token sale, financial compliance

---

bughuntoor

high

# Tax refund is calculated based on the wrong amount

## Summary
Tax refund is calculated based on the wrong amount

## Vulnerability Detail
After the private period has finished, users can claim a tax refund, based on their max tax free allocation.
\u0060\u0060\u0060solidity
        (s.share, left) = _claim(s);
        require(left > 0, "TokenSale: Nothing to claim");
        uint256 refundTaxAmount;
        if (s.taxAmount > 0) {
            uint256 tax = userTaxRate(s.amount, msg.sender);
            uint256 taxFreeAllc = _maxTaxfreeAllocation(msg.sender) * PCT_BASE;
            if (taxFreeAllc >= s.share) {
                refundTaxAmount = s.taxAmount;
            } else {
                refundTaxAmount = (left * tax) / POINT_BASE;
            }
            usdc.safeTransferFrom(marketingWallet, msg.sender, refundTaxAmount);
        }
\u0060\u0060\u0060
The problem is that in case \u0060s.share > taxFreeAllc\u0060, the tax refund is calculated wrongfully. Not only it should refund the tax on the unused USDC amount, but it should also refund the tax for the tax-free allocation the user has. 

Imagine the following. 
1. User deposits 1000 USDC.
2. Private period finishes, token oversells. Only half of the user\u0027s money actually go towards the sell (s.share = 500 USDC, s.left = 500 USDC)
3. The user has 400 USDC tax-free allocation
4. The user must be refunded the tax for the 500 unused USDC, as well as their 400 USDC tax-free allocation. In stead, they\u0027re only refunded for the 500 unused USDC. (note, if the user had 500 tax-free allocation, they would\u0027ve been refunded all tax)


## Impact
Users are not refunded enough tax 

## Code Snippet
https://github.com/sherlock-audit/2024-03-zap-protocol/blob/main/zap-contracts-labs/contracts/TokenSale.sol#L385

## Tool used

Manual Review

## Recommendation
change the code to the following: 
\u0060\u0060\u0060solidity
                refundTaxAmount = ((left + taxFreeAllc) * tax) / POINT_BASE;
\u0060\u0060\u0060

