# Krace - The \u0060_zapIn\u0060 function may unexpectedly revert due to the incorrect implementation of \u0060_transferTokenInAndApprove\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Amphor
**Keywords:** cybersecurity, vulnerability, smart contract, revert, function implementation, allowance check, VaultZapper, router, token approval, msgSender, transaction reverting, contract functionality, Foundry, test case, asynchronous vault, ZapperDeposit, patch, impact, security risk, code review

---

Krace

medium

# The \u0060_zapIn\u0060 function may unexpectedly revert due to the incorrect implementation of \u0060_transferTokenInAndApprove\u0060

## Summary

The \u0060_transferTokenInAndApprove\u0060 function should approve the \u0060router\u0060 on behalf of the *VaultZapper* contract. However, it checks the allowance from \u0060msgSender\u0060 to the \u0060router\u0060, rather than the *VaultZapper*. This potentially results in the *VaultZapper* not approving the \u0060router\u0060 and causing unexpected reverting.

## Vulnerability Detail

The allowance check in the \u0060_transferTokenInAndApprove\u0060 function should verify that \u0060address(this)\u0060 has approved sufficient amount of \u0060tokenIn\u0060 to the \u0060router\u0060. However, it currently checks the allowance of \u0060_msgSender()\u0060, which is unnecessary and may cause transaction reverting if \u0060_msgSender\u0060 had previously approved the \u0060router\u0060.

\u0060\u0060\u0060solidity
    function _transferTokenInAndApprove(
        address router,
        IERC20 tokenIn,
        uint256 amount
    )
        internal
    {
        tokenIn.safeTransferFrom(_msgSender(), address(this), amount);
//@ The check of allowance is useless, we should check the allowance from address(this) rather than the msgSender
        if (tokenIn.allowance(_msgSender(), router) < amount) {
            tokenIn.forceApprove(router, amount);
        }
    }
\u0060\u0060\u0060


**POC**

Apply the patch to \u0060asynchronous-vault/test/Zapper/ZapperDeposit.t.sol\u0060 to add the test case and run it with \u0060forge test --match-test test_zapIn --ffi\u0060.

\u0060\u0060\u0060diff
diff --git a/asynchronous-vault/test/Zapper/ZapperDeposit.t.sol b/asynchronous-vault/test/Zapper/ZapperDeposit.t.sol
index 9083127..ff11b56 100644
--- a/asynchronous-vault/test/Zapper/ZapperDeposit.t.sol
+++ b/asynchronous-vault/test/Zapper/ZapperDeposit.t.sol
@@ -17,6 +17,25 @@ contract VaultZapperDeposit is OffChainCalls {
         zapper = new VaultZapper();
     }

+    function test_zapIn() public {
+        Swap memory params =
+            Swap(_router, _USDC, _WSTETH, 1500 * 1e6, 1, address(0), 20);
+        _setUpVaultAndZapper(_WSTETH);
+
+        IERC4626 vault = _vault;
+        bytes memory swapData =
+            _getSwapData(address(zapper), address(zapper), params);
+
+        _getTokenIn(params);
+
+        // If the msgSender() happend to approve the SwapRouter before, then the zap will always revert
+        IERC20(params.tokenIn).approve(address(params.router), params.amount);
+        zapper.zapAndDeposit(
+            params.tokenIn, vault, params.router, params.amount, swapData
+        );
+
+    }
+
     //// test_zapAndDeposit ////
     function test_zapAndDepositUsdcWSTETH() public {
         Swap memory usdcToWstEth =
\u0060\u0060\u0060

Result:
\u0060\u0060\u0060javascript
Ran 1 test for test/Zapper/ZapperDeposit.t.sol:VaultZapperDeposit
[FAIL. Reason: SwapFailed("\u{8}�y�\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0 \0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0(ERC20: transfer amount exceeds allowance\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0")] test_zapIn() (gas: 4948462)
Suite result: FAILED. 0 passed; 1 failed; 0 skipped; finished in 20.84s (18.74s CPU time)

Ran 1 test suite in 22.40s (20.84s CPU time): 0 tests passed, 1 failed, 0 skipped (1 total tests)

Failing tests:
Encountered 1 failing test in test/Zapper/ZapperDeposit.t.sol:VaultZapperDeposit
[FAIL. Reason: SwapFailed("\u{8}�y�\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0 \0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0(ERC20: transfer amount exceeds allowance\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0")] test_zapIn() (gas: 4948462)
\u0060\u0060\u0060

## Impact

This issue could lead to transaction reverting when users interact with the contract normally, thereby affecting the contract\u0027s regular functionality.

## Code Snippet

https://github.com/sherlock-audit/2024-03-amphor/blob/6c797025ffe296e04607abf74400ff2bb36a7de3/asynchronous-vault/src/VaultZapper.sol#L160-L171

## Tool used

Foundry

## Recommendation

Fix the issue:
\u0060\u0060\u0060diff
diff --git a/asynchronous-vault/src/VaultZapper.sol b/asynchronous-vault/src/VaultZapper.sol
index 9943535..9cf6df9 100644
--- a/asynchronous-vault/src/VaultZapper.sol
+++ b/asynchronous-vault/src/VaultZapper.sol
@@ -165,7 +165,7 @@ contract VaultZapper is Ownable2Step, Pausable {
         internal
     {
         tokenIn.safeTransferFrom(_msgSender(), address(this), amount);
-        if (tokenIn.allowance(_msgSender(), router) < amount) {
+        if (tokenIn.allowance(address(this), router) < amount) {
             tokenIn.forceApprove(router, amount);
         }
     }
\u0060\u0060\u0060
