# Issue 5 - Slashing fails if claims revert

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Telcoin
**Keywords:** slashing, claims, revert, yield, functionality, plugin, error, manual review, staking, account, impact, vulnerability, method, recommendation, exit, failure, code, snippets, audit, telcoin

---

IssueM-6: Slashingfailsifclaimsrevert Source: https: //github.com/sherlock-audit/2022-11-telcoin-judging/issues/5 Foundby hickuphh3 Summary Slashing claims yields for the slashed account as part of the process. Should claims revert, slashing attemptswill revert too. VulnerabilityDetail Slashing calls the underlying _claimAndExit () function,which claims yield fromall plugins. Should one ormore claims fail, slashingwill revert aswell. Impact Failing claims brick the slashing functionality until the erroneous plugin (s) are removed. Duringwhich, the slashed user could have claimed his yield and exited. CodeSnippet https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/contracts/StakingMo dule.sol#L403-L406 https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/ contracts/StakingModule.sol#L356-L379 Toolused ManualReview Recommendation Create another slash () method that skips claiming yields of the slashed account. Discussion amshirif https: //github.com/telcoin/telcoin-staking/pull/16 jack-the-pug Fix confirmed 15    
