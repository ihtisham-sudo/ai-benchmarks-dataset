# jkoppel - gOhm stuck forever if call claimDefaulted on Cooler directly

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Olympus Cooler 
**Keywords:** gOhm, Cooler, claimDefaulted, Clearinghouse, vulnerability, loan, collateral, default, Eve, Bob, transfer, burn, defund, exploit, token, treasury, manual review, security, impact, recommendation

---

jkoppel

high

# gOhm stuck forever if call claimDefaulted on Cooler directly
## Summary

Anyone can call Cooler.claimDefaulted. If this is done for a loan owned by the Clearinghouse, the gOhm is sent to the Clearinghouse, but there is no way to recover or burn it.

## Vulnerability Detail

1. Bob calls \u0060Clearinghouse.lendToCooler\u0060 to make a loan collateralized by 1000 gOhm.
2. Bob defaults on the loan
3.  Immediately after default, Eve calls \u0060Cooler.claimDefaulted\u0060 on Bob\u0027s loan.
4. The gOhm is transferred to the Clearinghouse
5. There is no way to burn or transfer it. (In fact,  \u0060defund()\u0060 can be used to transfer literally any token *except* gOhm back to the treasury.)

However, the gOhm can now be stolen using the exploit in #1, potentially in the same transaction as when Eve called \u0060Cooler.claimDefaulted()\u0060.

## Impact

Anyone can very easily make all defaulted gOhm get stuck forever.

## Code Snippet

\u0060Cooler.claimDefaulted\u0060 sends the collateral to the lender, calls \u0060onDefault\u0060

https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Cooler.sol#L325

\u0060Clearinghouse.onDefault\u0060 does nothing

https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Clearinghouse.sol#L265

Although \u0060Clearinghouse.defund()\u0060 can be used to send any other token back to the treasury, it cannot do so for gOhm

https://github.com/sherlock-audit/2023-08-cooler/blob/main/Cooler/src/Clearinghouse.sol#L340

## Tool used

Manual Review

## Recommendation

Unsure. Perhaps add a flag disabling claiming by anyone other than \u0060loan.lender\u0060? Or just allow \u0060defund()\u0060 to be called on gOhm?


