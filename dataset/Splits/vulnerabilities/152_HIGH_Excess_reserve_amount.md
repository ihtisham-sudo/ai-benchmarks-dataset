# Excess reserve amount

**Severity:** HIGH
**Auditor:** MixBytes

---

##### Description
At lines https://github.com/CreamFi/compound-protocol/blob/e414160eb8a774140457c885bb099baae528df04/contracts/CCapableErc20.sol#L250-L252 contract increases `internalCash` and `totalReserves` values, but it's so strange that `internalCash` increased by `totalFee` and `totalReserves` increased by `reservesFee` so we totally increased assets amount by `reservesFee + totalFee` however user paid only `totalFee`. It seems there are some uncollateralized `reservesFee`. May be there `totalFee` paid by user should be splitted to `internalCash` and `totalReserves` ?

##### Recommendation
We recommend to double check that place
