# Callpaths — Tornado_Cash

Each external/public function lists all internal functions, library calls, and external callbacks it touches.

---

## ERC20Tornado

_File: ERC20Tornado.sol_

### external deposit
-> internal _processDeposit


### public isSpent
_(no internal calls)_


### external isSpentArray
-> public isSpent


### external withdraw
-> internal _processWithdraw


---

## ETHTornado

_File: ETHTornado.sol_

### external deposit
-> internal _processDeposit


### public isSpent
_(no internal calls)_


### external isSpentArray
-> public isSpent


### external withdraw
-> internal _processWithdraw


---

## MerkleTreeWithHistory

_File: MerkleTreeWithHistory.sol_

### public getLastRoot
_(no internal calls)_


### public hashLeftRight
_(no internal calls)_


### public isKnownRoot
_(no internal calls)_


### public zeros
_(no internal calls)_


---

## Tornado

_File: Tornado.sol_

### external deposit
-> internal _insert
  -> public zeros
  -> public hashLeftRight


### public getLastRoot
_(no internal calls)_


### public hashLeftRight
_(no internal calls)_


### public isKnownRoot
_(no internal calls)_


### public isSpent
_(no internal calls)_


### external isSpentArray
-> public isSpent


### external withdraw
-> public isKnownRoot


### public zeros
_(no internal calls)_


---

## Verifier

_File: Verifier.sol_

### public verifyProof
-> library Pairing.G1Point
-> library Pairing.G2Point
-> internal verifyingKey
  -> library Pairing.G1Point
  -> library Pairing.G2Point
-> library Pairing.plus
-> library Pairing.scalar_mul
-> library Pairing.pairing
-> library Pairing.negate


---

## cTornado

_File: cTornado.sol_

### external claimComp
_(no internal calls)_

