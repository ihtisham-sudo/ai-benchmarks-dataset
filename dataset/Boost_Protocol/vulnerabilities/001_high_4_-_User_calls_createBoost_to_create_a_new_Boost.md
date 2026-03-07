# 4 - User calls createBoost to create a new Boost

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Boost Protocol
**Keywords:** createBoost, incentive contract, BoostCore, raffle contests, ERC20, funds, clawback, init payload, budget contracts, protocol team, issue, mitigation, owner, response, impact, sherlock-admin2, boost protocol, PR, commit, rescue

---

      AttackPath         1. User calls createBoost to create a new Boost         2. Theychoosetouseanoutoftheboxincentivecontractlistedabove         3. TheyareinitializedwithBoostCoreastheowner       Impact         • NowinnercanbedrawnforraffleconteststhroughERC20Incentivecontract         • Anyfundsinthecontractthatneedtoberescuedcannotberetrievedthrough          clawback       PoC       Noresponse       Mitigation       Ownershouldbespecifiedintheinitpayloadbytheusersimilarlytohowitsdoneforthe       budgetcontractshere       Discussion       sherlock-admin2       TheprotocolteamfixedthisissueinthefollowingPRs/commits:       https://github.com/boostxyz/boost-protocol/pull/192                                 4 
