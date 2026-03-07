# elhaj - Potential ETH Loss Due to transfer Usage in Requestor Contract on \u0060zkSync\u0060

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** PoolTogetherV4
**Keywords:** cybersecurity, vulnerability, ETH loss, transfer method, Requestor contract, zkSync, gas limits, irretrievable funds, withdraw function, random number generation, DrawManager contract, WitnetRandomness, transaction fees, fixed gas amount, EOA, fallback function, manual review, Foundry Testing, ETH transfer, best practices

---

elhaj

medium

# Potential ETH Loss Due to transfer Usage in Requestor Contract on \u0060zkSync\u0060

## Summary
- The [Requestor](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-rng-witnet/src/Requestor.sol#L36) contract uses \u0060transfer\u0060 to send \u0060ETH\u0060 which has the risk that it will not work if the gas cost increases/decrease(low Likelihood), but it is highly likely to fail on \u0060zkSync\u0060 due to gas limits. This may make users\u0027 \u0060ETH\u0060 irretrievable.

## Vulnerability Detail

- Users (or bots) interact with [RngWitnet](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-rng-witnet/src/RngWitnet.sol#L132) to request a random number and start a draw in the \u0060DrawManager\u0060 contract. To generate a random number, users must provide some \u0060ETH\u0060 that will be sent to [WitnetRandomness](https://github.com/witnet/witnet-solidity-bridge/blob/6cf9211928c60e4d278cc70e2a7d5657f99dd060/contracts/apps/WitnetRandomnessV2.sol#L372) to generate the random number.
\u0060\u0060\u0060js
    function startDraw(uint256 rngPaymentAmount, DrawManager _drawManager, address _rewardRecipient) external payable returns (uint24) {
            (uint32 requestId,,) = requestRandomNumber(rngPaymentAmount);
            return _drawManager.startDraw(_rewardRecipient, requestId);
    }
 \u0060\u0060\u0060
- The \u0060ETH\u0060 sent with the transaction may or may not be used (if there is already a request in the same block, it won\u0027t be used). Any remaining or unused \u0060ETH\u0060 will be sent to [Requestor](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-rng-witnet/src/Requestor.sol#L36), so the user can withdraw it later.
- The issue is that the \u0060withdraw\u0060 function in the \u0060Requestor\u0060 contract uses \u0060transfer\u0060 to send \u0060ETH\u0060 to the receiver. This may lead to users being unable to withdraw their funds .
\u0060\u0060\u0060js
 function withdraw(address payable _to) external onlyCreator returns (uint256) {
        uint256 balance = address(this).balance;
 >>       _to.transfer(balance);
        return balance;
 }
\u0060\u0060\u0060

- The protocol will be deployed on different chains including \u0060zkSync\u0060, on \u0060zkSync\u0060 the use of \u0060transfer\u0060 can lead to issues, as seen with [921 ETH Stuck in zkSync Era](https://medium.com/coinmonks/gemstoneido-contract-stuck-with-921-eth-an-analysis-of-why-transfer-does-not-work-on-zksync-era-d5a01807227d).since it has a fixed amount of gas \u006023000\u0060 which won\u0027t be anough in some cases even to send eth to an \u0060EOA\u0060, It is explicitly mentioned in their docs to not use the \u0060transfer\u0060 method to send \u0060ETH\u0060 [here](https://docs.zksync.io/build/quick-start/best-practices.html#use-call-over-send-or-transfer).

>  notice that in case \u0060msg.sender\u0060 is  a contract that have some logic on it\u0027s receive or fallback function  the \u0060ETH\u0060 is definitely not retrievable. since this contract can only withdraw eth to it\u0027s [own addres](https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-rng-witnet/src/RngWitnet.sol#L99-L102) which will always revert.

## Impact

- Draw Bots\u0027 \u0060ETH\u0060 may be irretrievable or undelivered, especially on zkSync, due to the use of \u0060.transfer\u0060.
## Code Snippet
- https://github.com/sherlock-audit/2024-05-pooltogether/blob/1aa1b8c028b659585e4c7a6b9b652fb075f86db3/pt-v5-rng-witnet/src/Requestor.sol#L27-L30
## Tool used
Manual Review , Foundry Testing
## Recommendation
- recommendation to use \u0060.call()\u0060 for \u0060ETH\u0060 transfer.
