# Iteration through the whole storage array.

**Severity:** HIGH
**Auditor:** Zokyo

---

**Description**

 Governance.sol: function _resetProposals(), lines 422, 428, 432.Iteration is performed 
through several arrays with proposals, including the executed one. In case, there are a lot 
of elements in arrays, iteration might consume more gas than allowed per transaction, 
rejecting the whole transaction. Issue is marked as high, since it might prevent protocol 
from updating list of owners and minimum confirmation value
 SqwidERC1155Wrapper.sol: function _getWrappedTokenId(), line 77.Iteration through all 
wrapped tokens. In case there are a lot of tokens wrapped, function would prevent from 
wrapping new tokens due gas limit per one transaction.
 
 **Recommendation**:
 
 Consider removing executed proposals from arrays to decrease the number of elements. 
In case, proposals should not be removed, consider to split the reset process in several 
transactions to ensure its correct execution
 Consider creating additional mapping for linking the token of external contract to 
wrapped token id instead of iteration.
 
 **Recommendation**:
 
 The Sqwid team has changed the structure of the Governance. Now the mappings are 
used to track proposals and arrays to store the active ones. Also, a limit of active 
proposals per owner has been added
 The way of linking external tokens with wrapped tokens has been changed as well, from 
using an array to a mapping
