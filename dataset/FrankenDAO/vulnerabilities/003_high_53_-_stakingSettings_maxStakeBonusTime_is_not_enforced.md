# 53 - stakingSettings.maxStakeBonusTime is not enforced

**Severity:** high
**Auditor:** Sherlock
**Protocol:** FrankenDAO
**Keywords:** maxStakeBonusTime, staking, bonus, unlockTime, stake, attacker, voting power, enforcement, smart contract, Solidity, FrankenDAO, audit, issues, code review, parameters, mapping, bonus, attack, vulnerabilities

---

**Source:** [GitHub Issue #91](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/91)  
**Found by:** hansfriese, Trumpero, curiousapple  

When a user delegates their voting power from staked tokens, the total community voting power should be updated. But the update logic is not correct; the total community voting power could have wrong values.

\u0060\u0060\u0060solidity
tokenVotingPower[currentDelegate] -= amount;
tokenVotingPower[_delegatee] += amount;
// If a user is delegating back to themselves, they regain their community voting
// power, so adjust totals up
if (_delegator == _delegatee) {
    _updateTotalCommunityVotingPower(_delegator, true);
// If a user delegates away their votes, they forfeit their community voting
// power, so adjust totals down
} else if (currentDelegate == _delegator) {
    _updateTotalCommunityVotingPower(_delegator, false);
}
\u0060\u0060\u0060
When the total community voting power is increased in the first if statement, the delegator\u0027s token voting power might be positive already, and community voting power might be added to total community voting power before. Also, currentDelegate\u0027s token voting power might still be positive after delegation, so we shouldn\u0027t remove the community voting power this time.

The total community voting power can be incorrect.
[Link to Code](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#)

\u0060\u0060\u0060solidity
if (_delegator == _delegatee) {
    if(tokenVotingPower[_delegatee] == amount) {
        _updateTotalCommunityVotingPower(_delegator, true);
    }
    if(tokenVotingPower[currentDelegate] == 0) {
        _updateTotalCommunityVotingPower(currentDelegate, false);
    }
} else if (currentDelegate == _delegator) {
    if(tokenVotingPower[_delegatee] == amount) {
        _updateTotalCommunityVotingPower(_delegatee, true);
    }
    if(tokenVotingPower[_delegator] == 0) {
        _updateTotalCommunityVotingPower(_delegator, false);
    }
}
\u0060\u0060\u0060

Manual Review

Add more conditions to check if the msg.sender delegated or not.

zobront  
Fixed: [Link to Pull Request](https://github.com/Solidity-Guild/FrankenDAO/pull/15)  
Note for JTP: Please double check this one, as I\u0027m 99% confident but would love a second set of eyes on it.  
jack-the-pug  
Fix confirmed
# IssueH-2: Staking.unstake() doesn\u0027t decrease the original voting power that was used in Staking.stake().
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/70)  
**Found by:** Haruxe, hansfriese, 0x52  

Staking.unstake() doesn\u0027t decrease the original voting power that was used in Staking.stake().

When users stake/unstake the underlying NFTs, it calculates the token voting power using \u0060getTokenVotingPower()\u0060 and increases/decreases their voting power accordingly.

\u0060\u0060\u0060solidity
function getTokenVotingPower(uint _tokenId) public override view returns (uint) {
    if (ownerOf(_tokenId) == address(0)) revert NonExistentToken();
    // If tokenId < 10000, it\u0027s a FrankenPunk, so 100/100 = a multiplier of 1
    uint multiplier = _tokenId < 10_000 ? PERCENT : monsterMultiplier;
    // evilBonus will return 0 for all FrankenMonsters, as they are not eligible
    // for the evil bonus
    return ((baseVotes * multiplier) / PERCENT) + stakedTimeBonus[_tokenId] + evilBonus(_tokenId);
}
\u0060\u0060\u0060

But \u0060getTokenVotingPower()\u0060 uses some parameters like \u0060monsterMultiplier\u0060 and \u0060baseVotes\u0060 and the output would be changed for the same tokenId after the admin changed these settings. Currently, \u0060_stake()\u0060 and \u0060_unstake()\u0060 calculates the token voting power independently and the below scenario would be possible:

- At the first time, \u0060baseVotes=20\u0060, \u0060monsterMultiplier=50\u0060.
- A user staked a FrankenMonster and his voting power = 10 here.
- After that, the admin changed \u0060monsterMultiplier=60\u0060.
- When a user tries to unstake the NFT, the token voting power will be \u006020 * 60 / 100 = 12\u0060 here.
- Soit will revert with uint underflow here.
- After all, he can\u0027t unstake the NFT.

votesFromOwnedTokens might be updated wrongly or users can\u0027t unstake for the worst case because it doesn\u0027t decrease the same token voting power while unstaking.

[CodeSnippet](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L427-L440)
## Toolused
ManualReview

I think we should add a mapping like tokenVotingPower to save an original token voting power when users stake the token and decrease the same amount when they unstake.

zobront  
Fixed: https://github.com/Solidity-Guild/FrankenDAO/pull/17  
jack-the-pug  
Fix confirmed
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/53)  
**Found by:** WATCHPUG, hansfriese, bin2chen, neumo, Trumpero, koxuan, curiousapple, John

\u0060stakingSettings.maxStakeBonusTime\u0060 is not enforced, allowing the attacker to gain a huge staked Time Bonus by using a huge value for \u0060_unlockTime\u0060.

There is no max \u0060_unlockTime\u0060 check in \u0060_stakeToken()\u0060 to enforce the \u0060stakingSettings.maxStakeBonusTime\u0060. As a result, an attacker can set a huge value for \u0060_unlockTime\u0060 and get an enormous staked Time Bonus.

The attacker can get a huge amount of votes and dominate the voting.

- [Staking.sol (lines 389-394)](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L389-L394)
- [Staking.sol (lines 356-384)](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L356-L384)

Manual Review

Change to:
\u0060\u0060\u0060solidity
function _stakeToken(uint _tokenId, uint _unlockTime) internal returns (uint) {
    if (_unlockTime > 0) {
        unlockTime[_tokenId] = _unlockTime;
        uint time = _unlockTime - block.timestamp;
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint maxtime = stakingSettings.maxStakeBonusTime;
uint maxBonus = stakingSettings.maxStakeBonusAmount;
if (time < stakingSettings.maxStakeBonusTime){
    uint fullStakedTimeBonus = (time * maxBonus) / maxtime;
}else{
    uint fullStakedTimeBonus = maxBonus;
}
stakedTimeBonus[_tokenId] = _tokenId < 10000 ? fullStakedTimeBonus :
    fullStakedTimeBonus / 2;
\u0060\u0060\u0060

zobront  
Fixed: [https://github.com/Solidity-Guild/FrankenDAO/pull/13](https://github.com/Solidity-Guild/FrankenDAO/pull/13)  
jack-the-pug  
Fix confirmed
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/30)  
**Found by:** cccz, 0x52

Staking#_unstake allows any msg.sender to unstake tokens for any owner that has approved them. The issue is that even when msg.sender != owner, the votes are removed from msg.sender instead of owner. The result is that the owner keeps their votes and msg.sender loses theirs. This could be abused to hijack or damage voting.

\u0060\u0060\u0060solidity
address owner = ownerOf(_tokenId);
if (msg.sender != owner && !isApprovedForAll[owner][msg.sender] && msg.sender != getApproved[_tokenId]) revert NotAuthorized();
\u0060\u0060\u0060
Staking#_unstake allows any msg.sender to unstake tokens for any owner that has approved them.
\u0060\u0060\u0060solidity
uint lostVotingPower;
for (uint i = 0; i < numTokens; i++) {
    lostVotingPower += _unstakeToken(_tokenIds[i], _to);
}
votesFromOwnedTokens[msg.sender] -= lostVotingPower;
// Since the delegate currently has the voting power, it must be removed from
// If the user doesn\u0027t delegate, delegates(msg.sender) will return self
tokenVotingPower[getDelegate(msg.sender)] -= lostVotingPower;
totalTokenVotingPower -= lostVotingPower;
\u0060\u0060\u0060
After looping through _unstakeToken, all accumulated votes are removed from msg.sender. The problem with this is that msg.sender is allowed to unstake tokens for users other than themselves, and in these cases, they will lose votes rather than the user who owns the token.

**Example:** User A and User B both stake tokens and have 10 votes each. User A approves User B to unstake their tokens. User B calls unstake for User A. User B is...
## Description
The votes should be removed from the owner but instead are removed from \u0060msg.sender\u0060. The result is that after unstaking, User B has a vote balance of 0 while still having their locked token, and User B has a vote balance of 10 and their token back. Now User B is unable to unstake their token because their votes will underflow on unstake, permanently trapping their NFT.

Votes are removed incorrectly if \u0060msg.sender != owner\u0060. By extension, this would forever trap \u0060msg.sender\u0060 tokens in the contract.

[Code Snippet](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L427-L458)

Manual Review

Remove the ability for users to unstake for other users.

- zobront
- Fixed: [Pull Request](https://github.com/Solidity-Guild/FrankenDAO/pull/14)
- jack-the-pug
- Fix confirmed
## IssueM-1: Uses safeMint instead of mint for ERC721
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/65)  
**Found by:** Tomo  

Use safeMint instead of mint for ERC721.

The msg.sender will be minted as a proof of staking NFT when _stakeToken() is called. However, if msg.sender is a contract address that does not support ERC721, the NFT can be frozen in the contract.

As per the documentation of EIP-721:
> A wallet/broker/auction application MUST implement the wallet interface if it will accept safe transfers.  
> Ref: [EIP-721](https://eips.ethereum.org/EIPS/eip-721)

As per the documentation of ERC721.sol by Openzeppelin:  
Ref: [OpenZeppelin ERC721](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol#L274-L285)

\u0060\u0060\u0060solidity
/**
 * @dev Mints \u0060tokenId\u0060 and transfers it to \u0060to\u0060.
 *
 * WARNING: Usage of this method is discouraged, use {_safeMint} whenever
 * possible
 *
 * Requirements:
 *
 * - \u0060tokenId\u0060 must not exist.
 * - \u0060to\u0060 cannot be the zero address.
 *
 * Emits a {Transfer} event.
 */
function _mint(address to, uint256 tokenId) internal virtual {
\u0060\u0060\u0060
Users possibly lose their NFTs

[Staking.sol](https://github.com/sherlock-audit/2022-11-frankendao/blob/main/src/Staking.sol#L411)
\u0060\u0060\u0060solidity
_mint(msg.sender, _tokenId);
\u0060\u0060\u0060

Manual Review

Use \u0060safeMint\u0060 instead of \u0060mint\u0060 to check received address support for ERC721 implementation.  
[ERC721.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol#L262)

**zobront**  
I might consider this a duplicate of #55 but not sure how this is usually judged. We will be changing this function based on other issues to not allow "approved" spenders, so msg.sender will be the owner of the FrankenPunk, which ensures they are able to hold NFTs.

**zobront**  
Fixed: [Pull Request #14](https://github.com/Solidity-Guild/FrankenDAO/pull/14)  
I didn\u0027t need to add safeMint, as I made a change for another issue that removed the ability to non holder to unstake, which means they have the ability to hold NFTs.

**jack-the-pug**  
Fix confirmed
**Source:** [GitHub Issue #56](https://github.com/sherlock-audit/2022-11-frankendao-judging/issues/56)  
**Found by:** hansfriese, curiousapple  

[Medium-1] Hardcoded monsterMultiplier in case of stakedTimeBonus disregards the updates done to monsterMultiplier through setMonsterMultiplier()  

FrankenDAO allows users to stake two types of NFTs, Frankenpunks and Frankenmonsters, one of which is considered more valuable, i.e., Frankenpunks. This is achieved by reducing votes applicable for Frankenmonsters by monsterMultiplier.

\u0060\u0060\u0060solidity
function getTokenVotingPower(uint _tokenId) public override view returns (uint) {
    if (ownerOf(_tokenId) == address(0)) revert NonExistentToken();
    // If tokenId < 10000, it\u0027s a FrankenPunk, so 100/100 = a multiplier of 1
    uint multiplier = _tokenId < 10_000 ? PERCENT : monsterMultiplier;
    // evilBonus will return 0 for all FrankenMonsters, as they are not
    // eligible for the evil bonus
    return ((baseVotes * multiplier) / PERCENT) + stakedTimeBonus[_tokenId] +
           evilBonus(_tokenId);
}
\u0060\u0060\u0060

This monsterMultiplier is initially set as 50 and could be changed by governance proposal.

\u0060\u0060\u0060solidity
function setMonsterMultiplier(uint _monsterMultiplier) external onlyExecutor {
    emit MonsterMultiplierChanged(monsterMultiplier = _monsterMultiplier);
}
\u0060\u0060\u0060

However, one piece of code inside the FrakenDAO staking contract doesn\u0027t consider this and has a monster multiplier hardcoded.
