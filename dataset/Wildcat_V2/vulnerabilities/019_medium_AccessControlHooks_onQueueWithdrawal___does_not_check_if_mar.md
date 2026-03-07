# AccessControlHooks onQueueWithdrawal() does not check if market is hooked which could lead to unexpected errors such as temporary DoS

**Severity:** medium
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, onQueueWithdrawal, hooked market, credential verification, arbitrary hookData, abuse of credentials, short-term validity, msg.sender, isKnownLenderOnMarket, tryValidateAccess, tryValidateAccessInner, handleHooksData, malicious data, provider call, calldata, DoS attack, merkle proof, malicious miner, protocol security

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/AccessControlHooks.sol#L812


# Vulnerability details


## Impact
The \u0060onQueueWithdrawal()\u0060 function does not check if the caller is a hooked market, meaning anyone can call the function and attempt to verify credentials on a lender. This results in calls to registered pull providers with arbitrary hookData, which could lead to potential issues such as abuse of credentials that are valid for a short term, e.g. 1 block.

## Proof of Concept
The \u0060onQueueWithdrawal()\u0060 function does not check if the msg.sender is a hooked market, which is standart in virtually all other hooks:

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/AccessControlHooks.sol#L812
\u0060\u0060\u0060js
  /**
   * @dev Called when a lender attempts to queue a withdrawal.
   *      Passes the check if the lender has previously deposited or received
   *      market tokens while having the ability to deposit, or currently has a
   *      valid credential from an approved role provider.
   */
  function onQueueWithdrawal(
    address lender,
    uint32 /* expiry */,
    uint /* scaledAmount */,
    MarketState calldata /* state */,
    bytes calldata hooksData
  ) external override {
    LenderStatus memory status = _lenderStatus[lender];
    if (
      !isKnownLenderOnMarket[lender][msg.sender] && !_tryValidateAccess(status, lender, hooksData)
    ) {
      revert NotApprovedLender();
    }
  }
\u0060\u0060\u0060

If the caller is not a hooked market, the statement \u0060!isKnownLenderOnMarket[lender][msg.sender]\u0060, will return true, because the lender will be unknown. As a result the \u0060_tryValidateAccess()\u0060 function will be executed for any \u0060lender\u0060 and any \u0060hooksData\u0060 passed. The call to [\u0060_tryValidateAccess()\u0060](https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/AccessControlHooks.sol#L698) will forward the call to [\u0060_tryValidateAccessInner()\u0060](https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/AccessControlHooks.sol#L654). Choosing a lender of arbitrary address, say \u0060address(1)\u0060 will cause the function to attempt to retrieve the credential via the call to [_handleHooksData()](https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/AccessControlHooks.sol#L670), since the lender will have no previous provider or credentials.

As a result, the _handleHooksData function will forward the call to the encoded provider in the hooksData and will forward the extra hooks data as well, say merkle proof, or any arbitrary malicios data.

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/AccessControlHooks.sol#L617
\u0060\u0060\u0060js
  function _handleHooksData(
    LenderStatus memory status,
    address accountAddress,
    bytes calldata hooksData
  ) internal returns (bool validCredential) {
    // Check if the hooks data only contains a provider address
    if (hooksData.length == 20) {
      // If the data contains only an address, attempt to query a credential from that provider
      // if it exists and is a pull provider.
      address providerAddress = _readAddress(hooksData);
      RoleProvider provider = _roleProviders[providerAddress];
      if (!provider.isNull() && provider.isPullProvider()) {
        return _tryGetCredential(status, provider, accountAddress);
      }
    } else if (hooksData.length > 20) {
      // If the data contains both an address and additional bytes, attempt to
      // validate a credential from that provider
      return _tryValidateCredential(status, accountAddress, hooksData);
    }
  }
\u0060\u0060\u0060

The function call will be executed in [tryValidateCredential()](https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/AccessControlHooks.sol#L525), where the extra hookData will be forwarded. As described in the function comments, it will execute a call to \u0060provider.(address account, bytes calldata data)\u0060.

This means that anyone can call the function and pass arbitrary calldata. This can lead to serios vulnerabilities as the calldata is passed to the provider. 

Consider the following scenario:

- The pull provider is implemented to provide a short-term(say one block) approval timestamp.
- A user of the protocol provides a merkle-proof which would grant the one-time approval to withdraw in a transaction.
- A malicios miner frontruns the transaction submitting the same proof, but does not include the honest transaction in the mined block. Instead it is left for the next block.
- In the next block, the credential is no longer valid and as a result the honest user has their transaction revert.
- The miner does this continuosly essentially DoSing the entire market that uses this provider until it is removed and a new one added.

By following this scenario, a malicios user can essentially DoS a specific type pull provider.

Depending on implemenation of the pull provider, this can lead to other issues, as the malicios user can supply any arbitrary hookData in the function call.

## Recommended Mitigation Steps
Require the caller to be a registered hooked market, same as [onQueueWithdrawal()](https://github.com/code-423n4/2024-08-wildcat/blob/main/src/access/FixedTermLoanHooks.sol#L848) in FixedTermloanHooks



## Assessed type

DoS
