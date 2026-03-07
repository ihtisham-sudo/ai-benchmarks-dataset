# Issue H-5: After the buy Order is completed, the order creator does not receive the NFT

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Debita Finance V3
**Keywords:** NFT, buy order, order creator, transfer, sell NFT, receipt contract, buy token, ownership, smart contract, event emission, deletion, balance, approve, test case, assert, contract interaction, protocol, bug, fix, Debita Finance

---

# Issue H-5: After the buy Order is completed, the order creator does not receive the NFT

Source: [GitHub Issue #890](https://github.com/sherlock-audit/2024-10-debita-judging/issues/890)

Found by:  
0x37, 0xPhantom2, 4lifemen, Audinarey, BengalCatBalu, CL001, Cybrid, DenTonylifer, Greed, Greese, IzuMan, KiroBrejka, KungFuPanda, Pro_King, Valy001, alexbabits, araj, dhank, dimulski, durov, kazan, lanrebayode77, merlin, newspacexyz, nikhilx0111, pashap9990, shaflow01, t.aksoy, utsav, xiaoming90, ydlee

After sell NFT is completed, the NFT should be transferred to the order creator, but this is not done.

After the buy Order is completed, the order creator does not receive the NFT, and the NFT is sent directly to buy Order Contract. The latter only emits an event and deletes the order, but does not transfer the NFT to the order creator.


1. User A creates buy Order.
2. User B sells NFT.

1. User A creates buy Order.
2. User B sells NFT, and receives buy Token.
3. But order creator will lose the NFT.
The buy order creator will lose the NFT.

Path: test/fork/BuyOrders/BuyOrder.t.sol

\u0060\u0060\u0060solidity
function testpoc() public {
    vm.startPrank(seller);
    receiptContract.approve(address(buyOrderContract), receiptID);
    uint balanceBeforeAero = AEROContract.balanceOf(seller);
    address owner = receiptContract.ownerOf(receiptID);
    console.log("receipt owner before sell", owner);
    buyOrderContract.sellNFT(receiptID);
    address owner1 = receiptContract.ownerOf(receiptID);
    console.log("receipt owner after sell", owner1);
    // owner = buyOrderContract
    assertEq(owner1, address(buyOrderContract));
    vm.stopPrank();
}
\u0060\u0060\u0060

[PASS] testpoc() (gas: 242138) Logs: receipt owner before sell 0x81B2c95353d69580875a7aFF5E8f018F1761b7D1 receipt owner after sell 0xffD4505B3452Dc22f8473616d50503bA9E1710Ac

After the buy order is completed, the NFT should be transferred to the order creator.

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/d6f3b76c256713f0aa132a015ced6eb60ec389cb](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/d6f3b76c256713f0aa132a015ced6eb60ec389cb)
