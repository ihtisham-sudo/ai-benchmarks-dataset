# ast3ros - In case the portfolio makes a loss, the total reserves and reserve ratio will be inflated.

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** UnitasProtocol V1
**Keywords:** cyber security, vulnerability, pool balance, portfolio investment, USDT, Curve, Aave, Balancer, yield generation, smart contract risks, reserve ratio, total reserves, insurance pool, collateral, overstatement, undercollateralization, loss write-off, admin function, risk management, asset tracking

---

ast3ros

medium

# In case the portfolio makes a loss, the total reserves and reserve ratio will be inflated.

## Summary  

The pool balance is transferred to the portfolio for investment, for example sending USDT to Curve/Aave/Balancer etc. to generate yield. However, there are risks associated with those protocols such as smart contract risks. In case a loss happens, it will not be reflected in the pool balance and the total reserve and reserve ratio will be inflated.

## Vulnerability Detail

The assets in the pool can be sent to the portfolio account to invest and earn yield. The amount of assets in the insurance pool and Unitas pool is tracked by the \u0060_balance\u0060 variable. This amount is used to calculate the total reserve and total collateral, which then are used to calculate the reserve ratio.

            uint256 tokenReserve = _getBalance(token);
            uint256 tokenCollateral = IInsurancePool(insurancePool).getCollateral(token);

When there is a loss to the portfolio, there is no way to write down the \u0060_balance\u0060 variable. This leads to an overstatement of the total reserve and reserve ratio.

## Impact

Overstatement of the total reserve and reserve ratio can increase the risk for the protocol because of undercollateralization of assets.

## Code Snippet

https://github.com/sherlock-audit/2023-04-unitasprotocol/blob/main/Unitas-Protocol/src/Unitas.sol#L508-L509
https://github.com/sherlock-audit/2023-04-unitasprotocol/blob/main/Unitas-Protocol/src/PoolBalances.sol#L111-L113

## Tool used

Manual Review

## Recommendation

Add function to allow admin to write off the \u0060_balance\u0060 in case of investment lost. Example:

\u0060\u0060\u0060javascript

function writeOff(address token, uint256 amount) external onlyGuardian {

    uint256 currentBalance = IERC20(token).balanceOf(address(this));

    // Require that the amount to write off is less than or equal to the current balance
    require(amount <= currentBalance, "Amount exceeds balance");
    _balance[token] -= amount;

    emit WriteOff(token, amount);
}

\u0060\u0060\u0060
