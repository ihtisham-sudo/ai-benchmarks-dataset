# KingNFT - Call of \u0060\u0060\u0060\u0060revokeAllRole()\u0060\u0060\u0060\u0060 would fail silently

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Elfi
**Keywords:** cybersecurity, vulnerability, smart contracts, RoleAccessControl, revokeAllRole, revokeRole, accountRoles, EnumerableSet, solidity, mapping, ADMIN, bug test, Hardhat, ethers, deployer, malicious facet, funds theft, manual review, removing roles, security audit, access control

---

KingNFT

Medium

# Call of \u0060\u0060\u0060\u0060revokeAllRole()\u0060\u0060\u0060\u0060 would fail silently

## Summary
\u0060\u0060\u0060\u0060RoleAccessControl.revokeAllRole()\u0060\u0060\u0060\u0060 is wrongly implemented, the call of it would fail silently, and it would also trigger revert of \u0060\u0060\u0060\u0060RoleAccessControl.revokeRole()\u0060\u0060\u0060\u0060 as a candidated way to remove role.

## Vulnerability Detail
The issue arises on L59, as the  value type of \u0060\u0060\u0060\u0060accountRoles\u0060\u0060\u0060\u0060 (L20) is \u0060\u0060\u0060\u0060EnumerableSet\u0060\u0060\u0060\u0060, using \u0060\u0060\u0060\u0060delete\u0060\u0060\u0060\u0060 can\u0027t clear the data correctly.
\u0060\u0060\u0060solidity
File: contracts\storage\RoleAccessControl.sol
06: library RoleAccessControl {
07:     using EnumerableSet for EnumerableSet.Bytes32Set;
...
19:     struct Props {
20:         mapping(address => EnumerableSet.Bytes32Set) accountRoles;
21:     }
22: 
...
50:     function revokeRole(address account, bytes32 role) internal {
51:         Props storage self = load();
52:         if (self.accountRoles[account].contains(role)) {
53:             self.accountRoles[account].remove(role);
54:         }
55:     }
56: 
57:     function revokeAllRole(address account) internal {
58:         Props storage self = load();
59:         delete self.accountRoles[account];
60:     }
61: }

\u0060\u0060\u0060
The following PoC shows that: (1) \u0060\u0060\u0060\u0060ADMIN\u0060\u0060\u0060\u0060 role still exists after \u0060\u0060\u0060\u0060revokeAllRole()\u0060\u0060\u0060\u0060 (2) And \u0060\u0060\u0060\u0060revokeRole()\u0060\u0060\u0060\u0060 can\u0027t be used as a candidate to remove role once \u0060\u0060\u0060\u0060revokeAllRole()\u0060\u0060\u0060\u0060 was called
\u0060\u0060\u0060typescript
import { expect } from \u0027chai\u0027
import { Fixture, deployFixture } from \u0027@test/deployFixture\u0027
import { RoleAccessControlFacet, MockToken, Diamond } from \u0027types\u0027
import { HardhatEthersSigner } from \u0027@nomicfoundation/hardhat-ethers/signers\u0027
import { ethers } from \u0027hardhat\u0027
import { hexlify,  zeroPadBytes } from \u0027ethers\u0027


describe(\u0027RevokeAllRoles() bug test\u0027, function () {
    let fixture: Fixture
    let deployer: HardhatEthersSigner
    let diamondAddr: string
    let roleAccessControlFacet: RoleAccessControlFacet
    const ROLE_ADMIN = hexlify(zeroPadBytes(Buffer.from(\u0027ADMIN\u0027), 32))

    beforeEach(async () => {
        fixture = await deployFixture()
        const [signer0] = await ethers.getSigners()
        deployer = signer0
        diamondAddr = await fixture.diamond.getAddress()
        const getFacet = <T>(name: string) => ethers.getContractAt(name, diamondAddr) as Promise<T>
        roleAccessControlFacet = await getFacet<RoleAccessControlFacet>(\u0027RoleAccessControlFacet\u0027)
    })

    it(\u0027Test call of RevokeAllRoles() failed silently\u0027, async function () {
        let isAdmin = await roleAccessControlFacet.hasRole(deployer, ROLE_ADMIN)
        expect(isAdmin).to.equals(true)

        // 1. ADMIN role still exits after revokeAllRole()
        await roleAccessControlFacet.connect(deployer).revokeAllRole(deployer)
        isAdmin = await roleAccessControlFacet.hasRole(deployer, ROLE_ADMIN)
        expect(isAdmin).to.equals(true)

        // 2. And revokeRole() can\u0027t be used to remove role too
        await expect(roleAccessControlFacet.connect(deployer).revokeRole(deployer, ROLE_ADMIN)).to.be.reverted
    })

})
\u0060\u0060\u0060

And the test log:
\u0060\u0060\u0060solidity
2024-05-elfi-protocol\elfi-perp-contracts> npx hardhat test .\test\single-cases\BugRevokeAllRoles.test.ts     
  RevokeAllRoles() bug test
deploy MockTokens
token: WBTC 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512
token: SOL 0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9
token: USDC 0x5FC8d32690cc91D4c39d9d3abcBD16989F875707
!!!!!!hardhat!!!!!!
...

    ✔ Test call of RevokeAllRoles() failed silently (49ms)


  1 passing (14s)
\u0060\u0060\u0060

## Impact
accounts with revoked role can still operate on the system, those accounts might be leaked, compromised, owned by former employee ([real case](https://www.ledger.com/blog/security-incident-report)), or third-parties no longer cooperating with. Once it was triggered, may cause the protocol suffering huge damage. For example, a revoked account with \u0060\u0060\u0060\u0060ADMIN\u0060\u0060\u0060\u0060 role can add some malicious facet to steal all funds held by the protocol. 

## Code Snippet
https://github.com/sherlock-audit/2024-05-elfi-protocol/blob/8a1a01804a7de7f73a04d794bf6b8104528681ad/elfi-perp-contracts/contracts/storage/RoleAccessControl.sol#L59

## Tool used

Manual Review

## Recommendation
Removing roles one by one

