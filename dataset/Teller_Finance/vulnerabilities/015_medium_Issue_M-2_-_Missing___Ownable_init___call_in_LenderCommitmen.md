# Issue M-2 - Missing __Ownable_init() call in LenderCommitmentGroup_Smart::initialize()

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Teller Finance
**Keywords:** Ownable, initialize, LenderCommitmentGroup_Smart, contract, owner, vulnerability, pause, unpause, borrowing, onlyOwner, function, manual review, Vscode, audit, protocol, fix, commit, PR, security, impact

---

IssueM-2: Missing__Ownable_init () call in LenderCommitmentGroup_Smart: : initialize () Source: https: //github.com/sherlock-audit/2024-04-teller-finance-judging/issues/35 Foundby 0x73696d616f,0xAnmol,Afriaudit,AuditorPraise, EgisSecurity, MohammedRizwan Summary __Ownable_init () is not called in LenderCommitmentGroup_Smart: : initialize () , whichwillmake the contract not have any owner. VulnerabilityDetail LenderCommitmentGroup_Smart: : initialize () does not call __Ownable_init () and will be leftwithout owner. Impact pause and unpause borrowing in LenderCommitmentGroup_Smart due to Inability to having no owner, as these functions are onlyOwner. CodeSnippet https: //github.com/sherlock-audit/2024-04-teller-finance/blob/main/teller-protoco l-v2-audit-2024/packages/contracts/contracts/LenderCommitmentForwarder/exte nsions/LenderCommitmentGroup/LenderCommitmentGroup_Smart.sol#L158 Toolused Manual Review Vscode Recommendation Modify LenderCommitmentGroup_Smart: : initialize () to call __Ownable_init () : function initialize ( ... ) external initializer returns (address poolSharesToken_) { 53    __Ownable_init () ; } Discussion sherlock-admin2 The protocol teamfixed this issue in the following PRs/commits: https: //github.com/teller-protocol/teller-protocol-v2-audit-2024/pull/13 sherlock-admin2 The LeadSeniorWatson signed off on the fix. 54    
