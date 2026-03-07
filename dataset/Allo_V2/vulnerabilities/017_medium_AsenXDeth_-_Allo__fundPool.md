# AsenXDeth - Allo#_fundPool

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Allo V2
**Keywords:** cybersecurity, vulnerability, percentFee, fundPool, feeAmount, low-decimals token, circumvent, getFeeDenominator, GeminiUSD, market cap, deposit, fee calculation, no fee, funding, L2s, gas fees, protocol, minFundAmount, manual review, recommendation

---

AsenXDeth

medium

# Allo#_fundPool
A \u0060percentFee\u0060 amount is charged when funding a pool. However, the fee can be circumvented if the pool is using a low-decimals token and we fund the pool with a small amount. 
## Vulnerability Detail
Let\u0027s see the code of the \u0060_fundPool\u0060 function:
\u0060\u0060\u0060solidity
function _fundPool(uint256 _amount, uint256 _poolId, IStrategy _strategy) internal {
        uint256 feeAmount;
        uint256 amountAfterFee = _amount;

        Pool storage pool = pools[_poolId];
        address _token = pool.token;

        if (percentFee > 0) {
            feeAmount = (_amount * percentFee) / getFeeDenominator();
            amountAfterFee -= feeAmount;

            _transferAmountFrom(_token, TransferData({from: msg.sender, to: treasury, amount: feeAmount}));
        }

        _transferAmountFrom(_token, TransferData({from: msg.sender, to: address(_strategy), amount: amountAfterFee}));
        _strategy.increasePoolAmount(amountAfterFee);

        emit PoolFunded(_poolId, amountAfterFee, feeAmount);
    }
\u0060\u0060\u0060
The \u0060feeAmount\u0060 is calculated as follows:
\u0060\u0060\u0060solidity
feeAmount = (_amount * percentFee) / getFeeDenominator();
\u0060\u0060\u0060
where \u0060getFeeDenominator\u0060 returns \u00601e18\u0060 and \u0060percentFee\u0060 is represented like that: 1e18 = 100%, 1e17 = 10%, 1e16 = 1%, 1e15 = 0.1% (from the comments when declaring the variable).

Let\u0027s say the pool uses a token like [GeminiUSD](https://etherscan.io/token/0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd) which is a token with 300M+ market cap, so it\u0027s widely used, and \u0060percentFee\u0060 == 1e15 (0.1%)

A user could circumvent the fee by depositing a relatively small amount. In our example, he can deposit 9 GeminiUSD. In that case, the calculation will be:
\u0060feeAmount = (_amount * percentFee) / getFeeDenominator() = (9e2 * 1e15) / 1e18 = 9e17/1e18 = 9/10 = 0;\u0060

So the user ends up paying no fee. There is nothing stopping the user from funding his pool by invoking the \u0060fundPool\u0060 with such a small amount as many times as he needs to fund the pool with whatever amount he chooses, circumventing the fee. 

Especially with the low gas fees on L2s on which the protocol will be deployed, this will be a viable method to fund a pool without paying any fee to the protocol. 
## Impact
The protocol doesn\u0027t collect fees from pools with low decimal tokens.
## Code Snippet
https://github.com/allo-protocol/allo-v2/blob/main/contracts/core/Allo.sol#L502
## Tool used

Manual Review

## Recommendation
Add a \u0060minFundAmount\u0060 variable and check for it when funding a pool. 
