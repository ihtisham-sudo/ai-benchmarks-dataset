# Failed transfer may be overlooked due to lack of contract existence check

**Severity:** high
**Auditor:** TrailOfBits
**Protocol:** Uniswap V3
**Keywords:** transfer, contract, existence check, failed transaction, destructed tokens, low-level call, IERC20Minimal, safeTransfer, liquidity, EVM, delegatecall, callcode, swaps, tokens, pool, success, revert, Solidity, documentation, data validation

---

# Failed transfer may be overlooked due to lack of contract existence check

**Severity:** High  
**Difficulty:** High  
**Type:** Data Validation  
**Finding ID:** TOB-UNI-009  
**Target:** libraries/TransferHelper.sol  

Because the pool fails to check that a contract exists, the pool may assume that failed transactions involving destructed tokens are successful.  

\u0060TransferHelper.safeTransfer\u0060 performs a transfer with a low-level call without confirming the contract’s existence:  

\u0060\u0060\u0060solidity
    ) internal {      
        (bool success, bytes memory data) =      
            token.call(abi.encodeWithSelector(IERC20Minimal.transfer.selector, to, value));                                      
        require(success && (data.length == 0 || abi.decode(data, (bool))), \u0027TF\u0027);   
}
\u0060\u0060\u0060
*Figure 9.1: libraries/TransferHelper.sol*  

The Solidity documentation includes the following warning:  

>The low-level call, delegatecall, and callcode will return success if the calling account is non-existent, as part of the design of EVM. Existence must be checked prior to calling if desired.  

*Figure 9.2: The Solidity documentation details the necessity of executing existence checks prior to performing a delegatecall.*  

As a result, if the tokens have not yet been deployed or have been destroyed, \u0060safeTransfer\u0060 will return success even though no transfer was executed.  

If the token has not yet been deployed, no liquidity can be added. However, if the token has been destroyed, the pool will act as if the assets were sent even though they were not.  

The pool contains tokens A and B. Token A has a bug, and the contract is destroyed. Bob is not aware of the issue and swaps 1,000 B tokens for A tokens. Bob successfully transfers 1,000 B tokens to the pool but does not receive any A tokens in return. As a result, Bob loses 1,000 B tokens.  

Short term, check the contract’s existence prior to the low-level call in \u0060TransferHelper.safeTransfer\u0060. This will ensure that a swap reverts if the token to be

bought no longer exists, preventing the pool from accepting the token to be sold without returning any tokens in exchange.

Long term, avoid low-level calls. If such a call is not avoidable, carefully review the Solidity documentation, particularly the “Warnings” section.

© 2021 Trail of Bits
