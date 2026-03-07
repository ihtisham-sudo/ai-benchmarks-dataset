# 4 - Users unable to claim rewards for multiple epochs after their initial claim

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Brevis
**Keywords:** claim, reward, epoch, users, engagement, satisfaction, protocol, restriction, opportunity, missed, amount, fixed, issue, response, discussion, GammaStrategies, GammaRewarder, PR, commit, sherlock-admin2

---

      wouldrevertduetothecheck: require(claim.amount==0,”Alreadyclaimedreward.”);as       claim.amountwouldbe20. Kateshouldbeeligibletoclaimforotherepochs,butsheis       not. GithubLink       Impact       Usersareunabletoclaimrewardsformultipleepochsaftertheirinitialclaim,resultingin       missedopportunitiestoreceiverewards. Thisrestrictiondiminishesuserengagement       andoverallsatisfactionwiththeprotocol.       PoC       Noresponse       Mitigation       Noresponse       Discussion       sherlock-admin2       TheprotocolteamfixedthisissueinthefollowingPRs/commits:       https://github.com/GammaStrategies/GammaRewarder/pull/2                                 4 
