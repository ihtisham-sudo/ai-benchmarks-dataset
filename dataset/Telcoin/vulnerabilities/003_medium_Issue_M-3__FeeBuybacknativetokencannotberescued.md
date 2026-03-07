# Issue M-3: FeeBuybacknativetokencannotberescued

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Telcoin
**Keywords:** FeeBuyback, native token, rescue, ERC20, contract, msg.value, aggregator, swap, leftover, implementation, rescueERC20, trapped, manual review, recommendation, support, tokens, audit, vulnerability, impact, source code

---

IssueM-3: FeeBuybacknativetokencannotberescued Source: https: //github.com/sherlock-audit/2022-11-telcoin-judging/issues/80 Foundby WATCHPUG Summary Lack ofmethods to rescue native tokens trapped in the FeeBuyback contract. VulnerabilityDetail Like ERC20tokens, the native tokenmay also get stuck in the FeeBuyback contract for all sorts of reasons. For example, at L77, the _aggregator is calledwith a msg.value,whichmeans that the native token can be used as an inToken for the swap. Therefore, part of the input native token can be sent back to the FeeBuyback contract as a leftover. However, the current implementation of rescueERC20 () only supports rescue ERC20 tokens. Impact The leftover native tokens trapped in the contract can not be rescued. CodeSnippet https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/contracts/fee-buyba ck/FeeBuyback.sol#L77-L78 https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/contracts/fee-buyba ck/FeeBuyback.sol#L94-L97 Toolused ManualReview Recommendation Consider adding support to rescue native tokens. 8    Discussion amshirif https: //github.com/telcoin/telcoin-staking/pull/10 jack-the-pug Fix confirmed 9    
