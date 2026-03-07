# [H-01] Calling `splitValue` when token index is not the latest will overwrite other claims' storage

**Severity:** HIGH
**Auditor:** Pashov Audit Group

---

**Impact:**
High, as it can lead to loss of units for an account without any action on his side

**Likelihood:**
Medium, because it can happen only with a token that has a non-latest index

**Description**

The logic in `_splitValue` is flawed here:

```solidity
uint256 currentID = _tokenID;
...
toIDs[i] = ++currentID;
...
for (uint256 i; i < len; ) {
    valueLeft -= values[i];

    tokenValues[toIDs[i]] = values[i];

    unchecked {
        ++i;
    }
}
...
_mintBatch(_account, toIDs, amounts, "");
```

Let's look at the following scenario:

1. Alice mints through allowlist, token 1, 10 units
2. Bob mints through allowlist, token 2, 100 units
3. Alice calls `splitValue` for token 1 to 2 new tokens, both 5 units

Now we will have `tokenValues[toIDs[i]] = values[i]` where `toIDs[i]` is `++currentID` which is 2 and `values[i]` is 5, so now `tokenValues[2] = 5` which is overwriting the `tokenValues` of Bob. Also, later `_mintBatch` is called with Bob's token ID as a token ID, which will make some of the split tokens be of the type of Bob's token.

**Recommendations**

Change the code the following way:

```diff
- maxIndex[_typeID] += len;
...
- toIDs[i] = ++currentID;
+ toIDs[i] = _typeID + ++maxIndex[typeID];
```
