# Conversion Functions - Rounding Issues in EGGStoSONIC and SONICtoEGGS

**Severity:** high
**Auditor:** Cantina
**Protocol:** Eggs Finance
**Keywords:** EGGStoSONIC, SONICtoEGGS, conversion, rounding, integer, DoS, protocol, value, getBacking, totalSupply, user, position, computed, recommendation, logic, ceil, separate, functions, tokens, approach

---

# Conversion Functions

\u0060\u0060\u0060solidity
function EGGStoSONIC(uint256 value) public view returns (uint256) {
    return (value * getBacking()) / totalSupply();
}

function SONICtoEGGS(uint256 value) public view returns (uint256) {
    return (value * totalSupply()) / (getBacking() - value);
}
\u0060\u0060\u0060

In each of these conversion functions, we perform a division to determine the output. In case the resulting value is not a perfect integer, we always round down to the nearest integer. This can lead to problems in a few circumstances. Let\u0027s consider a simple example where we convert from eggs to sonic and then back:

- value = 100 (eggs).
- getBacking() = 1000.
- totalSupply() = 300.
- sonic received = EGGStoSONIC(value) = (100 * 1000) / 300 = 333.
- eggs received back = SONICtoEGGS(sonic) = (333 * 300) / (1333 - 333) = 99.

Above we can see that converting 100 eggs to sonic and then back leaves us with only 99 eggs. In case the last remaining user in the system attempts to close their position, there may not be sufficient sonic in the system to cover the computed amount for them to receive, causing a DoS.

**Recommendation:** It\u0027s important that we always round in favor of the protocol. Essentially what this means is that if we\u0027re computing an amount for the protocol to receive, we should round up. Conversely, if we\u0027re computing an amount for a user to receive, we should round down. We can adjust our logic to round up by adding the (denominator - 1) to the numerator, e.g. for EGGStoSONIC, that would look something like:

\u0060\u0060\u0060solidity
// UNTESTED
function EGGStoSONICceil(uint256 value) public view returns (uint256) {
    return (value * getBacking() + (totalSupply() - 1)) / totalSupply();
}
\u0060\u0060\u0060

The best approach is probably to have separate functions for rounding up versus down for each type of conversion (as necessary), then carefully consider which one should be used at any given time, depending on whether tokens are coming in or out of the protocol.

**EggsFinance:** Acknowledged.  
**CantinaManaged:** Partial fix for now since EGGStoSONICceil was added but is not used.

## 3.4 Low Risk

### 3.4.1 Fees will not be charged if BUY_FEE is set low enough

**Severity:** Low Risk  
**Context:** Eggs.sol#L93  
**Description:** In Eggs.buy, we always take a 1/125th fee off the msg.value based on the FEES_BUY constant:

\u0060\u0060\u0060solidity
uint256 feeAddressAmount = msg.value / FEES_BUY;
\u0060\u0060\u0060

There is also a separate BUY_FEE, which is mutable, and is taken out of the amount of eggs to mint:

\u0060\u0060\u0060solidity
mint(reciever, (eggs * getBuyFee()) / FEE_BASE_1000);
\u0060\u0060\u0060

In case BUY_FEE ever corresponds to a fee less than 1/125th, the user will effectively not be paying that fee since they will receive the full amount of eggs regardless.

**Recommendation:** Currently, it\u0027s possible to set BUY_FEE to any value between 1000 and 975. Instead, we should limit the maximum to correspond to a 1/125th fee, which would be 992.
