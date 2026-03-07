# deth - Clearinghouse.sol#claimDefaulted() - \u0060Clearinghouse\u0060 doesn\u0027t approve the \u0060MINTR\u0060 to handle tokens in his name, which bricks the entire function.

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Olympus Cooler 
**Keywords:** Clearinghouse, MINTR, claimDefaulted, cybersecurity, vulnerability, OHM, burnFrom, approval, allowance, token, smart contract, Ethereum, mainnet, MockOhm, revert, impact, manual review, recommendation, burn tokens, contract code

---

deth

high

# Clearinghouse.sol#claimDefaulted() - \u0060Clearinghouse\u0060 doesn\u0027t approve the \u0060MINTR\u0060 to handle tokens in his name, which bricks the entire function.
## Summary
\u0060Clearinghouse\u0060 doesn\u0027t approve the \u0060MINTR\u0060 to handle tokens in his name, which bricks the entire function.

## Vulnerability Detail
Inside \u0060claimDefaulted\u0060 on the [last line](https://github.com/sherlock-audit/2023-08-cooler/blob/6d34cd12a2a15d2c92307d44782d6eae1474ab25/Cooler/src/Clearinghouse.sol#L244) we call \u0060MINTR.burnOhm\u0060 which in turn calls [OHM.burnFrom](https://github.com/OlympusDAO/olympus-v3/blob/19236eb1c02464df8fb79c7b59b7195d7511b338/src/modules/MINTR/OlympusMinter.sol#L50-L61). The [docs for MINTR.burnFrom](https://docs.olympusdao.finance/main/technical/contract-docs/modules/MINTR/OlympusMinter/#burnohm) state: "Burn OHM from an address. Must have approval.". We can confirm that this is the case when looking at \u0060OHM\u0060 source code and it\u0027s \u0060burnFrom\u0060. I found 2 \u0060OHM\u0060 tokens that are currently deployed on mainnet, so I\u0027m linking both their addresses: https://etherscan.io/token/0x383518188c0c6d7730d91b2c03a03c837814a899#code, https://etherscan.io/token/0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5#code. Both addresses use the same \u0060burnFrom\u0060 logic and in both cases they require an \u0060allowance\u0060. Nowhere in the contract do we approve the \u0060MINTR\u0060 to handle \u0060OHM\u0060 tokens in the name of \u0060Clearinghouse\u0060, in fact \u0060OHM\u0060 isn\u0027t even specified in \u0060Clearinghouse\u0060.  

Side note:
The test \u0060testFuzz_claimDefaulted\u0060 succeeds, because \u0060MockOhm\u0060 is written incorrectly. When \u0060burnFrom\u0060 gets called \u0060MockOhm\u0060 calls the inherited \u0060_burn\u0060 function, which burns tokens from \u0060msg.sender\u0060. The mock doesn\u0027t represent how the real \u0060OHM.burnFrom\u0060 works.
## Impact
\u0060Claimdefault\u0060 will always revert.

## Code Snippet
https://github.com/sherlock-audit/2023-08-cooler/blob/6d34cd12a2a15d2c92307d44782d6eae1474ab25/Cooler/src/Clearinghouse.sol#L244
## Tool used
Manual Review

## Recommendation
Add a variable \u0060ohm\u0060 which will be the \u0060OHM\u0060 address and approve the necessary tokens to the \u0060MINTR\u0060 before calling \u0060MINTR.burnOhm\u0060.

