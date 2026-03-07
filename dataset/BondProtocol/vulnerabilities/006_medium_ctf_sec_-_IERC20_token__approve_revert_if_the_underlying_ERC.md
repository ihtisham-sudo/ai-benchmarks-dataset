# ctf_sec - IERC20(token).approve revert if the underlying ERC20 token approve does not return boolean

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** BondProtocol
**Keywords:** cybersecurity, vulnerability, ERC20, IERC20, approve, revert, safeTransfer, safeTransferFrom, safeApprove, non-standard token, USDT, boolean return, solmate, payout token, impact, manual review, recommendation, token approval, smart contract, Ethereum

---

ctf_sec

medium

# IERC20(token).approve revert if the underlying ERC20 token approve does not return boolean

## Summary

IERC20(token).approve revert if the underlying ERC20 token approve does not return boolean

## Vulnerability Detail

When transferring the token, the protocol use safeTransfer and safeTransferFrom

but when approving the payout token, the safeApprove is not used

for non-standard token such as USDT,

calling approve will revert because the solmate ERC20 enforce the underlying token return a boolean

https://github.com/transmissions11/solmate/blob/bfc9c25865a274a7827fea5abf6e4fb64fc64e6c/src/tokens/ERC20.sol#L68

\u0060\u0060\u0060solidity
    function approve(address spender, uint256 amount) public virtual returns (bool) {
        allowance[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);

        return true;
    }
\u0060\u0060\u0060

while the token such as USDT does not return boolean

https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#code#L126

## Impact

USDT or other ERC20 token that does not return boolean for approve is not supported as the payout token

## Code Snippet

https://github.com/sherlock-audit/2023-06-bond/blob/fce1809f83728561dc75078d41ead6d60e15d065/options/src/fixed-strike/liquidity-mining/OTLM.sol#L190

https://github.com/sherlock-audit/2023-06-bond/blob/fce1809f83728561dc75078d41ead6d60e15d065/options/src/fixed-strike/liquidity-mining/OTLM.sol#L504

## Tool used

Manual Review

## Recommendation

Use safeApprove instead of approve
