# ​Lack of ​chainID

**Severity:** HIGH
**Auditor:** TrailOfBits

---

## Type: Timing  
**Target:** ERC20Permit.sol  

## Difficulty: Low  
Implements the draft ERC 2612 via the ERC20Permit contract it inherits from. This allows a third party to transmit a signature from a token holder that modifies the ERC20 allowance for a particular user. These signatures used in calls to `permit` in `ERC20Permit` do not account for chainsplits. The `chainID` is not updatable and not included in the signed data as part of the `permit` call. As a result, if the chain forks after deployment, the signed message may be considered valid on both forks.

`bytes32 hashStruct = keccak256(abi.encode(PERMIT_TYPEHASH, owner, spender, amount, nonces[owner], deadline));`

![Figure 8.1](path/to/figure) The reconstruction of the permit parameters in `ERC20Permit` as signed by the `owner`, notably omitting the `chainID`.

## Exploit Scenario  
Bob has a wallet holding `fyDAI` after the hard fork, a significant user base remains on the old chain. On the new chain, Bob approves Alice to spend some tokens via a call to `permit`. Alice, operating on both chains, replays the `permit` call on the old chain and is able to steal some of Bob’s `fyDAI`. An EIP is included in an upcoming hard fork that has split.  

## Recommendation  
Short term, include the `chainID` opcode in the `permit` schema. This will make replay attacks impossible in the event of a post-deployment hard fork.

Long term, document and carefully review any signature schemas, including their robustness to replay on different wallets, contracts, and blockchains. Make sure users are aware of signing best practices and the danger of signing messages from untrusted sources.
