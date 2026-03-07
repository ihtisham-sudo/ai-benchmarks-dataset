# BiasedMerc - VotingEscrow MAX_DELEGATES value can lead to DOS on certain EVM-compatible chains

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** VotingEscrow, MAX_DELEGATES, DOS, EVM-compatible, gas usage, tokenId, delegates, transfer, burn, mint, IOTA EVM, Ethereum mainnet, gas limit, Scroll EVM, Gnosis Chain, test function, impact, NFT, funds, manual review, recommendation

---

BiasedMerc

High

# VotingEscrow MAX_DELEGATES value can lead to DOS on certain EVM-compatible chains

## Summary

\u0060VotingEscrow\u0060 \u0060MAX_DELEGATES\u0060 is a hardcoded variable that ensures an address does not have an array of delegates that would lead to a DOS when calling \u0060transfer/burn/mint\u0060 when moving delegates.. However the current value of \u00601024\u0060 can still lead to a DOS on certain chains.

## Vulnerability Detail

Within the contest [README](https://audits.sherlock.xyz/contests/442), the protocol states that the code is expected to function on any EVM-compatible chain, without any plans to include Ethereum mainnet:

>On what chains are the smart contracts going to be deployed?
>
>First on IOTA EVM, but code was build with any EVM-compatible network in mind. There is no plan to deploy in on Ethereum mainnet

The sponsor has also stated that it should be assumed the code will be deployed to all EVM compatible chains:
> dawid.d | Velocimeter — 18/07/2024 02:18
> you should assume that it can be deployed to any chain that is fully evm compatible

When testing the gas usage of withdrawing a tokenId that currently has the maximum number of delegates, the gas usage is:
\u0060console::log("gas used:", 23637422 [2.363e7]) [staticcall]\u0060

Popular EVM compatible chains block gas limit (under 24m):
[Scroll EVM](https://scrollscan.com/block/7277054): 10,000,000
[Gnosis Chain](https://gnosisscan.io/block/34879385): 17,000,000

## POC
Add the following test function to \u0060VotingEscrow.t.sol\u0060:
\u0060\u0060\u0060solidity
    function testDelegateLimitAttack() public {
        vm.prank(address(owner));
        flowDaiPair.approve(address(escrow), type(uint256).max);
        uint tokenId = escrow.create_lock(TOKEN_1, 7 days);
        for(uint256 i = 0; i < escrow.MAX_DELEGATES() - 1; i++) {
            vm.roll(block.number + 1);
            vm.warp(block.timestamp + 2);
            address fakeAccount = address(uint160(420 + i));
            flowDaiPair.transfer(fakeAccount, 1);
            vm.startPrank(fakeAccount);
            flowDaiPair.approve(address(escrow), type(uint256).max);
            escrow.create_lock(1, FIFTY_TWO_WEEKS);
            escrow.delegate(address(this));
            vm.stopPrank();
        }
        vm.roll(block.number + 1);
        vm.warp(block.timestamp + 7 days);
        uint initialGas = gasleft();
        escrow.withdraw(tokenId);
        uint gasUsed = initialGas - gasleft();
        console.log("gas used:", gasUsed);
    }
\u0060\u0060\u0060
To run:
\u0060forge test --match-test testDelegateLimitAttack  -vv\u0060
Output: 
\u0060\u0060\u0060javascript
[PASS] testDelegateLimitAttack() (gas: 12470671686)
Logs:
  gas used: 23637422
\u0060\u0060\u0060

## Impact

As seen, this upper gas limit exceeds the outlined EVM-compatible chains, meaning the current hardcoded value of \u0060MAX_DELEGATES\u0060 can lead to a DOS by delegating minimum value locks to an address, causing that tokenId to revert when calling any function that calls \u0060_moveTokenDelegates\u0060 as the gas utilised will exceed the chains gas limit for a singular block. Affected functions: [transferFrom()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L353-L359), [withdraw()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L955-L979), [merge()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L1195-L1210), [_mint()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L483-L492).

This will lead to a user\u0027s NFT being locked from utilising the outlined functions, causing their funds to be locked, leading to a loss of funds with no special outside factors needed to allow this type of attack (apart from deploying on one of the outlined chains, which as stated in the ReadMe is applicable).

## Code Snippet

[VotingEscrow::transferFrom()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L353-L359)
[VotingEscrow::withdraw()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L955-L979)
[VotingEscrow::merge()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L1195-L1210)
[VotingEscrow::_mint()](https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/VotingEscrow.sol#L483-L492)

## Tool used

Manual Review

## Recommendation

Reducing the \u0060MAX_DELEGATES\u0060 value to 256 would reduce the cost of the outlined function to ~6,000,000 which would solve the outlined issue.
