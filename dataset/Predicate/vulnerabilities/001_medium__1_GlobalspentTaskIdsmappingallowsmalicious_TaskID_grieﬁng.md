# .1 GlobalspentTaskIdsmappingallowsmalicious"TaskID"grieﬁng

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Predicate 
**Keywords:** ServiceManager, validateSignatures, spentTaskIDs, taskId, front-run, authorizeTransaction, griefing, malicious operator, client address, quorum, mapping, permissioned network, signature, reputable participants, on-chain, off-chain, risk mitigation, iteration, contract address, unique identifier

---

# .1 GlobalspentTaskIdsmappingallowsmalicious"TaskID"grieﬁng
**Severity:** MediumRisk  
**Context:** ServiceManager.sol#L303  
**Description:** In the ServiceManager contract, the validateSignatures function checks:  
\u0060\u0060\u0060solidity
require(!spentTaskIDs[_task.taskId], "Predicate.validateSignatures: task ID already spent");
\u0060\u0060\u0060
This places the same spentTaskId key in a global scope for all the clients using this ServiceManager. Due to this implementation, a malicious operator can front-run an _authorizeTransaction call from any client and submit the same taskId, setting spentTaskIDs[taskId] to true. The legitimate _authorizeTransaction call is then blocked, reverting with a "task ID already spent" error. This effectively griefs the user’s intended operation and can be easily abused by using a policy with just 1 signature as quorum.  
**Recommendation:** Scope the spentTaskIDs to each client or contract address so only the same user can reuse the same taskId:  
\u0060\u0060\u0060solidity
mapping(address => mapping(string => bool)) spentTaskIDs;
spentTaskIDs[clientAddress][taskId] = true;
\u0060\u0060\u0060
By including the client address or some unique identifier in the key, a malicious party cannot burn another client’s signature.  
**Predicate:** Acknowledged. While we do agree this is a valid concern, the current risk is mitigated by our permissioned operator network, which consists of reputable, vetted participants. Given the scope of changes required—both on-chain and off-chain—to fully isolate task IDs per client, we believe this is best addressed in a subsequent iteration.  
**CantinaManaged:** Acknowledged.
