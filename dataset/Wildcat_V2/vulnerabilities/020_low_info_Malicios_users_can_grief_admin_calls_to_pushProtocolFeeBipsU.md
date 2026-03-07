# Malicios users can grief admin calls to pushProtocolFeeBipsUpdates causing tranasctions to revert

**Severity:** low/info
**Auditor:** Code4rena
**Protocol:** Wildcat V2
**Keywords:** cybersecurity, vulnerability, pushProtocolFeeBipsUpdates, setProtocolFeeBips, malicious users, frontrunning, batch calls, reverting transactions, gas costs, delayed updates, deployed markets, overhead, proof of concept, protocol fee bips, state management, mitigation steps, MEV, transaction costs, smart contracts, fee updates

---

# Lines of code

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/HooksFactory.sol#L553
https://github.com/code-423n4/2024-08-wildcat/blob/main/src/market/WildcatMarketConfig.sol#L171


# Vulnerability details

## Impact
The pushProtocolFeeBipsUpdates function is callable by anyone, meaning anyone can push a fee update. However, whenever a market has already been updated, the setProtocolFeeBips() function will revert when the update is pushed again. As a result malicios users can frontrun batch calls to pushProtocolFeeBipsUpdates() and push the update to only the last market in a batch. This will result in reverting tranasctions for admins or other honest users and thus loss of gas costs, as well as delayed updates. If there are 1000 deployed markets in a template, the admin will have to do 1000 separate transactions to avoid the issue, which is a big overhead. Note that this can happen by accident as well, if a user happens to push an update to their own fees just ahead of the admin.

## Proof of Concept
The \u0060pushProtocolFeeBipsUpdates()\u0060 function iterates over markets in the range [marketStartIndex, marketEndIndex] and pushes the fees update via calls to \u0060market.setProtocolFeeBips(protocolFeeBips)\u0060:

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/HooksFactory.sol#L553
\u0060\u0060\u0060js
  /**
   * @dev Push any changes to the fee configuration of \u0060hooksTemplate\u0060 to markets
   *      using any instances of that template at \u0060_marketsByHooksTemplate[hooksTemplate]\u0060.
   *      Starts at \u0060marketStartIndex\u0060 and ends one before \u0060marketEndIndex\u0060  or markets.length,
   *      whichever is lowest.
   */
  function pushProtocolFeeBipsUpdates(
    address hooksTemplate,
    uint marketStartIndex,
    uint marketEndIndex
  ) public override nonReentrant {
    HooksTemplate memory details = _templateDetails[hooksTemplate];
    if (!details.exists) revert HooksTemplateNotFound();

    address[] storage markets = _marketsByHooksTemplate[hooksTemplate];
    marketEndIndex = MathUtils.min(marketEndIndex, markets.length);
    uint256 count = marketEndIndex - marketStartIndex;
    uint256 setProtocolFeeBipsCalldataPointer;
    uint16 protocolFeeBips = details.protocolFeeBips;
    assembly {
      // Write the calldata for \u0060market.setProtocolFeeBips(protocolFeeBips)\u0060
      // this will be reused for every market
      setProtocolFeeBipsCalldataPointer := mload(0x40)
      mstore(0x40, add(setProtocolFeeBipsCalldataPointer, 0x40))
      // Write selector for \u0060setProtocolFeeBips(uint16)\u0060
      mstore(setProtocolFeeBipsCalldataPointer, 0xae6ea191)
      mstore(add(setProtocolFeeBipsCalldataPointer, 0x20), protocolFeeBips)
      // Add 28 bytes to get the exact pointer to the first byte of the selector
      setProtocolFeeBipsCalldataPointer := add(setProtocolFeeBipsCalldataPointer, 0x1c)
    }
    for (uint256 i = 0; i < count; i++) {
      address market = markets[marketStartIndex + i];
      assembly {
        if iszero(call(gas(), market, 0, setProtocolFeeBipsCalldataPointer, 0x24, 0, 0)) {
          // Equivalent to \u0060revert SetProtocolFeeBipsFailed()\u0060
          mstore(0, 0x4484a4a9)
          revert(0x1c, 0x04)
        }
      }
    }
  }
\u0060\u0060\u0060

However, the setProtocolFeeBips function will revert if the protocol fee bips remains the same, meaning the change was already pushed, so \u0060_protocolFeeBips == state.protocolFeeBips\u0060 will be true:

https://github.com/code-423n4/2024-08-wildcat/blob/main/src/market/WildcatMarketConfig.sol#L171
\u0060\u0060\u0060js
  function setProtocolFeeBips(
    uint16 _protocolFeeBips
  ) external nonReentrant sphereXGuardExternal {
    if (msg.sender != factory) revert_NotFactory();
    if (_protocolFeeBips > 1_000) revert_ProtocolFeeTooHigh();
    MarketState memory state = _getUpdatedState();
    if (state.isClosed) revert_ProtocolFeeChangeOnClosedMarket();
    if (_protocolFeeBips == state.protocolFeeBips) revert_ProtocolFeeNotChanged(); // @audit here, the fee will remain the same, so the tx will revert.
    hooks.onSetProtocolFeeBips(_protocolFeeBips, state);
    state.protocolFeeBips = _protocolFeeBips;
    emit ProtocolFeeBipsUpdated(_protocolFeeBips);
    _writeState(state);
  }
\u0060\u0060\u0060

Thus, a malicios user can frontrun batch calls and cause them to revert and incur gas losses. The malicios user would specifically push the update to the last market in a batch for maximum gas losses. This can also happen if for example a user pushes a fee update to their market just before the admin batch call.

## Recommended Mitigation Steps
Do not revert, but just return if the fee bips is unchanged.


## Assessed type

MEV
