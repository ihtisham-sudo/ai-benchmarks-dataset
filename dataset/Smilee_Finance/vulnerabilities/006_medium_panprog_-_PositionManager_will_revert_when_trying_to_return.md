# panprog - PositionManager will revert when trying to return back to user excess of the premium transferred from the user when minting position

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Smilee Finance
**Keywords:** cybersecurity, vulnerability, PositionManager, mint, premium, transfer, safeTransferFrom, USDC, transferFrom, approval, msg.sender, baseToken, Arbitrum, protocol, user funds, transaction revert, token transfer, manual review, recommendation, smart contract

---

panprog

medium

# PositionManager will revert when trying to return back to user excess of the premium transferred from the user when minting position

## Summary

\u0060PositionManager.mint\u0060 calculates preliminary premium to be paid for buying the option and transfers it from the user. The actual premium paid may differ, and if it\u0027s smaller, excess is returned back to user. However, it is returned using the \u0060safeTransferFrom\u0060:
\u0060\u0060\u0060solidity
    if (obtainedPremium > premium) {
        baseToken.safeTransferFrom(address(this), msg.sender, obtainedPremium - premium);
    }
\u0060\u0060\u0060

The problem is that \u0060PositionManager\u0060 doesn\u0027t approve itself to transfer baseToken to \u0060msg.sender\u0060, and USDC \u0060transferFrom\u0060 implementation requires approval even if address is transferring from its own address. Thus the transfer will revert and user will be unable to open position.

## Vulnerability Detail

Both \u0060transferFrom\u0060 implementations in USDC on Arbitrum (USDC and USDC.e) require approval from any address, including when doing transfers from your own address.
https://arbiscan.io/address/0x1efb3f88bc88f03fd1804a5c53b7141bbef5ded8#code
\u0060\u0060\u0060solidity
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), _allowances[sender][_msgSender()].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }
\u0060\u0060\u0060

https://arbiscan.io/address/0x86e721b43d4ecfa71119dd38c0f938a75fdb57b3#code
\u0060\u0060\u0060solidity
    function transferFrom(
        address from,
        address to,
        uint256 value
    )
        external
        override
        whenNotPaused
        notBlacklisted(msg.sender)
        notBlacklisted(from)
        notBlacklisted(to)
        returns (bool)
    {
        require(
            value <= allowed[from][msg.sender],
            "ERC20: transfer amount exceeds allowance"
        );
        _transfer(from, to, value);
        allowed[from][msg.sender] = allowed[from][msg.sender].sub(value);
        return true;
    }
\u0060\u0060\u0060

\u0060PositionManager\u0060 doesn\u0027t approve itself to do transfers anywhere, so \u0060baseToken.safeTransferFrom(address(this), msg.sender, obtainedPremium - premium);\u0060 will always revert, preventing the user from opening position via \u0060PositionManager\u0060, breaking important protocol function.

## Impact

User is unable to open positions via \u0060PositionManager\u0060 in certain situations as all such transactions will revert, breaking important protocol functionality and potentially losing user funds / profit due to failure to open position.

## Code Snippet

\u0060PositionManager.mint\u0060 transfers base token back to \u0060msg.sender\u0060 via \u0060safeTransferFrom\u0060:
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/periphery/PositionManager.sol#L139-L141

## Tool used

Manual Review

## Recommendation

Consider using \u0060safeTransfer\u0060 instead of \u0060safeTransferFrom\u0060 when transferring token from self.
