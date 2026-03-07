# 82 - UnsafeERC20methods

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Telcoin
**Keywords:** ERC20, unsafe methods, transaction revert, IERC20 interface, transferFrom, transfer, approval, allowance, USDT, contract malfunction, tokens, manual review, SafeERC20, vulnerability, impact, code snippet, recommendation, audit, Telcoin, fee-back

---

IssueM-2: UnsafeERC20methods Source: https: //github.com/sherlock-audit/2022-11-telcoin-judging/issues/82 Foundby WATCHPUG, aphak5010,0xAgro, rotcivegaf, eierina, Deivitto, yixxas, rvierdiiev, hickuphh3, Mukund, hyh,0xheynacho, pashov, 0x4non, Bnke0x0 Summary Using unsafe ERC20methods can revert the transaction for certain tokens. VulnerabilityDetail ERC20Tokens thatwon\u0027twork correctly using the standard There aremanyWeird IERC20 interface. For example, IERC20 (token) .transferFrom () and IERC20 (token) .transfer () will fail for sometokens as theymaynot conformtothestandardIERC20interface.Andif _ aggregatordoes not alwaysconsumeall theallowancegiven at L72, thetransaction will also revert on the next call, because there are certain tokens that do not allow approval of a non-zero numberwhen the current allowance is not zero (eg, USDT) . Impact The contractwill malfunction for certain tokens. CodeSnippet https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/contracts/fee-buyba ck/FeeBuyback.sol#L94-L97 https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/contracts/fee-buyba ck/FeeBuyback.sol#L47-L82 Toolused ManualReview Recommendation Consider using SafeERC20 for transferFrom, transfer and approve. 6    Discussion amshirif https: //github.com/telcoin/telcoin-staking/pull/6 jack-the-pug Fix confirmed 7    
