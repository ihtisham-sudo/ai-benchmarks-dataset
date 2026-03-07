# 3.2.4 Malicious module/hook may not be removed

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Clave 
**Keywords:** module, hook, removeModule, removeHook, low-level call, transaction, revert, gas-griefing, gas limit, out-of-gas, memory expansion, data return, security, smart contract, Ethereum, solidity, function, error handling, recommendation, best practices

---

# 3.2.4 Malicious module/hook may not be removed
**Severity:** Medium Risk  
**Context:** ModuleManager.sol#L111-L112, HookManager.sol#L197-L198  
**Description:** In the module manager, the removeModule function calls the module\u0027s remove function using a low-level call, allowing the overall transaction to succeed even if the module reverts. Similar logic would be expected in the removeHook function, but this is currently not the case:

Moreover, even when a low-level call is utilized, there exist theoretical "gas-griefing" tactics where a module or hook can block its removal. Firstly, if the low-level call doesn\u0027t set a specific gas limit, it forwards 63/64 of the remaining gas. If the contract deliberately uses up this entire amount, the outer transaction may experience an out-of-gas error. Secondly, if the low-level call returns a large amount of data, it can force the account to incur memory expansion costs, which can also cause out-of-gas errors.  
**Recommendation:** Firstly, as noted by the TODO comment, change removeHook to use a low-level call where the success of remove is ignored. Secondly, to prevent potential "gas-griefing" issues, consider using an explicit gas amount in these low-level calls, and limit the memory expansion from the call by using assembly or a library like ExcessivelySafeCall.  
**Clave:** Fixed in PR 773.  
**Cantina:** The fix uses gas amount as input to removeHook, and technically speaking, this means a module/hook could waste up to 63/64 of the remaining gas when it gets control flow in remove (note:
