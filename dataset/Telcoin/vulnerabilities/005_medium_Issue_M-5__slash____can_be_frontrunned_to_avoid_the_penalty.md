# Issue M-5: slash () can be frontrunned to avoid the penalty imposed on them

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Telcoin
**Keywords:** slash, frontrun, penalty, malicious user, pause, fullClaimAndExit, mempool, bypass, slashing mechanism, sophisticated users, vulnerability, impact, recommendation, manual review, staking, contract, Telcoin, audit, security, funds

---

IssueM-5: slash () canbefrontrunnedtoavoidthepenalty imposedonthem Source: https: //github.com/sherlock-audit/2022-11-telcoin-judging/issues/45 Foundby cccz, hickuphh3, yixxas Summary I believe slash () is used to take funds away froma userwhen theymisbehave. However, amalicious user can frontrun this operation or the pause () function and call fullClaimAndExit () to fully exit before the penalty can affect them. VulnerabilityDetail Malicious userswhohaveintentionallycommittedsomeoffenses thatwouldleadto getting slashed can listen to themempool and frontrun the slash () or pause () function call by the protocol to protect all his assets before slashing can happen. Impact Slashingmechanismimplemented can be bypassed bymalicious user. CodeSnippet https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/contracts/StakingMo dule.sol#L403-L406 https: //github.com/sherlock-audit/2022-11-telcoin/blob/main/contracts/StakingMo dule.sol#L202-L207 Toolused Manual Review Recommendation I implore the sponsors to explore alternatives to this slashingmechanismas they can be easily bypassed, especially so by sophisticated userswho presumably are the oneswhowill be getting slashed. 13    Discussion amshirif https: //github.com/telcoin/telcoin-staking/pull/21 jack-the-pug Fix confirmed 14    
