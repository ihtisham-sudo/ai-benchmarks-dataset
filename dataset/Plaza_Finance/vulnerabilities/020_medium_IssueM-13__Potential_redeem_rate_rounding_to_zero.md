# IssueM-13: Potential redeem rate rounding to zero

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Plaza Finance
**Keywords:** redeem rate, rounding, transactions, tvl, bond supply, precision, asset supply, error, revert, function, liquidity, smart contract, Ethereum, leverage, token, supply, market, protocol, audit, bug

---

# IssueM-13: Potential redeem rate rounding to zero

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-12-plaza-finance-judging/issues/864)

Found by: 056Security, 0x23r0, 0x52, 0xAadi, 0xadrii, Abhan1041, Harry_cryptodev, KiroBrejka, Matin, Negin, OrangeSantra, Ryonen, X0sauce, Z3R0, ZoA, almurhasan, bretzel, carlitox477, denys_sosnovskyi, future, fuzzysquirrel, globalace, robertauditor, solidityenj0yer, stuart_the_minion, super_jack


Due to bad order of operations, redeem rate can be rounded down to zero causing transactions reverting in otherwise normal conditions, especially in cases of low TVL value or high bond supply.


Pool::getRedeemAmount() is used to calculate the redeem rate in leverage token types:

\u0060\u0060\u0060solidity
function getRedeemAmount(
  ...
) public pure returns(uint256) {
  ...
} else if (tokenType == TokenType.LEVERAGE) {
  redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) / assetSupply) * PRECISION;
  ...
}
\u0060\u0060\u0060

In cases of low TVL or scenarios where bondSupply makes up a large part of the TVL, the redeemRate in this case will be rounded to zero as the assetSupply will undoubtedly be much larger. This leads to a loss of precision which wrongly calculates the redeem amount as zero, thus leading to the transaction reverting in the \u0060_redeem()\u0060 function:

\u0060\u0060\u0060solidity
function _redeem(
  ...
) private returns(uint256) {
  // Get amount to mint
  uint256 reserveAmount = simulateRedeem(tokenType, depositAmount);
  // Check whether reserve contains enough funds
  if (reserveAmount < minAmount) {
    revert MinAmount();
  }
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// Reserve amount should be higher than zero
if (reserveAmount == 0) {
  revert ZeroAmount();
}
\u0060\u0060\u0060

No response

No response

No response

Inability for users to redeem in low TVL or mostly bonded markets

No response

Change the order:
\u0060\u0060\u0060solidity
redeemRate = ((tvl - (bondSupply * BOND_TARGET_PRICE)) * PRECISION) / assetSupply;
\u0060\u0060\u0060

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/Convexity-Research/plaza-evm/pull/159](https://github.com/Convexity-Research/plaza-evm/pull/159)
