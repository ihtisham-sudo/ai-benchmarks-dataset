# Attack Path

**Severity:** medium
**Auditor:** CodeHawks
**Protocol:** Swan
**Keywords:** phase calculation, sell phase, withdraw phase, timestamp, block, transaction, buy phase, interval, swan, buyer agent, reversion, approval, asset transfer, market parameters, manual review, hardhat, test, error, protocol, functionality

---

# Attack Path
1. A malicious seller lists an asset on Swan for purchase.
2. The malicious seller either transfers the listed asset to another address or revokes Swan\u0027s approval before the BuyerAgent::purchase call is made by directly interacting with the asset contract.
3. The BuyerAgent includes the listed asset for purchase based on the oracle\u0027s recommendation. The BuyerAgent, oracle, or Swan contract are unaware of any transfer of ownership or revocation of approval events that might occur after the listing.
4. The BuyerAgent attempts to purchase the asset using Swan::purchase. However, due to the changed state (transfer or revoked approval), the call reverts.
5. This reversion causes the entire BuyerAgent::purchase transaction to fail, leading to a denial of service for other assets that were meant to be purchased.

The impact of this vulnerability is significant as it allows a malicious seller to manipulate the behavior of the BuyerAgent contract, ultimately preventing it from purchasing other legitimate assets. This attack can be used to deceive buyers by causing failed transactions, even if those transactions involve assets from honest sellers. This vulnerability can be exploited repeatedly to create a denial of service, disrupting the normal operations of the BuyerAgent and affecting market participants.

- Manual Review
- Hardhat for testing

Since BuyerAgent::purchase needs to get the list of assets from the oracle output and it\u0027s a bit complex to simulate that directly, I added a wrapper function to BuyerAgent to call Swan::purchase from BuyerAgent directly (and avoid signer issues from hardhat):

\u0060\u0060\u0060solidity
function swanPurchase(address _asset) external onlyAuthorized {
    swan.purchase(_asset);
}
\u0060\u0060\u0060

This allows direct testing of individual asset purchases. You should add this function to the BuyerAgent contract.

Create a new file in the test directory:

\u0060\u0060\u0060typescript
// test/poc.test.ts
import { expect } from "chai";
import { ethers } from "hardhat";
import { Swan, BuyerAgent, ERC721 } from "../typechain-types";
import { deploySwanFixture, deployTokenFixture } from "./fixtures/deploy";
import { parseEther } from "ethers";
import { HardhatEthersSigner } from "@nomicfoundation/hardhat-ethers/signers";
import { transferTokens, listAssets, createBuyers } from "./helpers";
import { Phase } from "./types/enums";
import { time } from "@nomicfoundation/hardhat-toolbox/network-helpers";

/**
 * Test scenario:
 * - User lists an asset on Swan.
 * - User transfers the asset by interacting directly with the asset contract before the BuyerAgent attempts to purchase it.
 * - BuyerAgent\u0027s purchase call should revert because the transfer cannot proceed.
 */
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
describe("BuyerAgent Purchase Revert Scenario", function () {
    let swan: Swan;
    let token: ERC20;
    let asset: ERC721;
    let secondAsset: ERC721;
    let buyerAgent: BuyerAgent;
    let seller: HardhatEthersSigner;
    let buyer: HardhatEthersSigner;
    let dummyUser: HardhatEthersSigner;
    const NAME = "SWAN_ASSET_NAME";
    const SYMBOL = "SWAT";
    const DESC = ethers.encodeBytes32String("description of the asset");
    const PRICE = parseEther("1");
    const AMOUNT_PER_ROUND = parseEther("2");
    const ROYALTY_FEE = 1;

    beforeEach(async function () {
        // Get signers (seller, buyer, and dummy user)
        [seller, buyer, dummyUser] = await ethers.getSigners();
        // Deploy the token contract and verify the seller\u0027s initial balance
        const supply = parseEther("1000");
        token = await deployTokenFixture(seller, supply);
        expect(await token.balanceOf(seller.address)).to.eq(supply);
        // Set up market parameters for the Swan contract deployment
        const MARKET_PARAMETERS = {
            withdrawInterval: 1800, // Withdraw interval: 30 minutes
            sellInterval: 3600, // Sell interval: 60 minutes
            buyInterval: 600, // Buy interval: 10 minutes
            platformFee: 1n,
            maxAssetCount: 5n,
            timestamp: 0n,
        };
        // Set up oracle parameters for Swan deployment
        const ORACLE_PARAMETERS = { difficulty: 1, numGenerations: 1, numValidations: 1 };
        const STAKES = { generatorStakeAmount: parseEther("0.01"), validatorStakeAmount: parseEther("0.01") };
        const FEES = { platformFee: 1n, generationFee: parseEther("0.02"), validationFee: parseEther("0.1") };
        // Deploy the Swan contract
        const { swan: deployedSwan } = await deploySwanFixture(
            seller,
            token,
            STAKES,
            FEES,
            MARKET_PARAMETERS,
            ORACLE_PARAMETERS
        );
        swan = deployedSwan;
        // Create a BuyerAgent for the buyer
        const buyerAgentParams = {
            name: "BuyerAgent#1",
            description: "Description of BuyerAgent 1",
            royaltyFee: ROYALTY_FEE,
            amountPerRound: AMOUNT_PER_ROUND,
        };
\u0060\u0060\u0060
\u0060\u0060\u0060javascript
owner: buyer,
};
[buyerAgent] = await createBuyers(swan, [buyerAgentParams]);
// Fund the BuyerAgent with tokens for purchasing assets
await token.connect(seller).transfer(await buyerAgent.getAddress(), parseEther("3"));
// Approve Swan to spend tokens on behalf of the seller
await token.connect(seller).approve(await swan.getAddress(), PRICE);
// Seller lists two assets on Swan
await listAssets(swan, buyerAgent, [[seller, PRICE], [seller, PRICE]], NAME, SYMBOL, DESC, 0n);
const [listedAsset, secondListedAsset] = await swan.getListedAssets(await buyerAgent.getAddress(), 0n);
asset = await ethers.getContractAt("ERC721", listedAsset);
secondAsset = await ethers.getContractAt("ERC721", secondListedAsset);
// Increase time to move to the Buy phase
await time.increase(3600);
\u0060\u0060\u0060

\u0060\u0060\u0060javascript
it("should successfully purchase the second asset if it is not transferred", async function () {
    // Ensure we are in the Buy phase of the first round
    const [round, phase] = await buyerAgent.getRoundPhase();
    expect(round).to.equal(0n);
    expect(phase).to.equal(Phase.Buy);
    // Ensure the second asset is still owned by the seller
    expect(await secondAsset.ownerOf(1)).to.equal(seller.address);
    // BuyerAgent attempts to purchase the second asset
    await buyerAgent.connect(buyer).swanPurchase(secondAsset.target);
    // Verify that the second asset is now owned by the BuyerAgent
    expect(await secondAsset.ownerOf(1)).to.equal(await buyerAgent.getAddress());
});
\u0060\u0060\u0060

\u0060\u0060\u0060javascript
it("should revert purchase if asset is transferred away or approval is revoked", async function () {
    // Ensure we are in the Buy phase of the first round
    const [round, phase] = await buyerAgent.getRoundPhase();
    expect(round).to.equal(0n);
    expect(phase).to.equal(Phase.Buy);
    // Verify approval status for the first asset and ensure seller owns it
    expect(await asset.ownerOf(1)).to.equal(seller.address);
    expect(await asset.isApprovedForAll(seller.address, swan.target)).to.be.true;
    // Seller transfers the asset directly to another address (dummyUser) before the BuyerAgent attempts to purchase
    await asset.connect(seller).transferFrom(seller.address, dummyUser.address, 1);
    expect(await asset.ownerOf(1)).to.equal(dummyUser.address);
    //// or remove approval
    // await asset.connect(seller).setApprovalForAll(swan.target, false);
    // expect(await asset.isApprovedForAll(seller.address, swan.target)).to.be.false;
    // Attempt to purchase the transferred asset using BuyerAgent, expecting a revert due to insufficient approval
    try {
        await buyerAgent.connect(buyer).swanPurchase(asset.target);
        throw new Error("Expected purchase to revert, but it succeeded");
    } catch (error) {
\u0060\u0060\u0060
## BuyerAgent Purchase Revert Scenario
A seller lists two assets on the Swan platform. The BuyerAgent can buy the second asset successfully, which proves the correct functionality of the purchase mechanism. However, the first asset, which is transferred or has approval revoked, will fail. Before the BuyerAgent::purchase function is called, the seller transfers one of the assets or revokes the approval for Swan. The BuyerAgent::purchase call attempts to execute but fails due to the changed status of the asset, resulting in a reversion of the entire transaction.

### Output:
- BuyerAgent Purchase Revert Scenario
    - should successfully purchase the second asset if it is not transferred
    - swan address: 0xc6e7DF5E7b4f2A278906862b61205850344D4e7d
    - Revert message matched: Purchase failed due to insufficient approval. Error: VM Exception while processing transaction: reverted with custom error
    - \u0027ERC721InsufficientApproval("0xc6e7DF5E7b4f2A278906862b61205850344D4e7d", 1)\u0027
    - should revert purchase if asset is transferred away or approval is revoked

The solution to this issue may depend on design choices. One possible recommendation is to modify the purchase logic to check the result of each individual Swan::purchase call and ignore reverts for specific assets. This way, if one asset cannot be purchased due to a transfer or approval revocation, the other assets can still be successfully purchased. This approach would prevent the entire batch transaction from failing due to issues with a single asset.
## M-07. Phase calculation inaccuracy will always extend sell phase and cut withdrawal phase time
Submitted by newspacexyz, neilalois. Selected submission by: neilalois.

Due to incorrect if comparison sell period will always be extended by 1 unit and cut withdrawal time by the same amount.

In the phase comparison:
\u0060\u0060\u0060javascript
if (roundTime <= params.sellInterval) {
    return (round, Phase.Sell, params.sellInterval - roundTime);
} else if (roundTime <= params.sellInterval + params.buyInterval) {
    return (round, Phase.Buy, params.sellInterval + params.buyInterval - roundTime);
} else {
    return (round, Phase.Withdraw, cycleTime - roundTime);
}
\u0060\u0060\u0060
Three ifs determine which phase it is using the current roundTime (which is a timestamp remainder). But because incorrect comparison sign "<=" is used it always extends the first phase interval (sellInterval). Look at "Tools Used" for an example case. This also returns incorrect "Time till next phase", last of the three parameters. As both Sell and Buy phases can reach 0.
## Incorrect Phase Calculation

Severity: Medium

Incorrect phase calculation only shifts 1 second from last to first phase. But because Base blocks at the time of writing are minted every 2 seconds, the error will be more significant because (block.timestamp updated frequently - higher chance to fall in the shifted seconds):
- Transactions that are meant for "Buy" phase - can fall in the extended "Sell" phase and fail.
- If "Withdrawal" phase is set to 1 seconds - it will be skipped (never reached).
- Even if "Sell" interval is set to 0 seconds and should skip, it will still be reached.

The comparison is at the core of the protocol and often used, can cause failing transactions and invalid protocol functionality (skipping "Withdrawal"). But no loss of funds (apart from gas).

Manual review + hardhat tests

\u0060\u0060\u0060javascript
const phaseIndexToStr = ["Buy", "Sell", "Withdraw"];
const getBlockTimestamp = async () => {
  const latestBlock = await ethers.provider.getBlock("latest");
  if (!latestBlock) {
    throw new Error("No latest block found");
  }
  return latestBlock.timestamp;
};
describe("Phases calculation", function () {
  it("Calculation extends sell and cuts withdraw phase short", async function () {
    // all phases set to equal = 2
    await swan
       .connect(dria)
       .setMarketParameters({ ...MARKET_PARAMETERS, buyInterval: 2, sellInterval: 2, withdrawInterval: 2 });
    // after new market params are set the round and phase restarts
    for (let i = 0; i < 7; i++) {
       const phaseRes = await buyerAgent.getRoundPhase();
       const markSetOn = Number((await swan.getCurrentMarketParameters()).timestamp);
       const currentTime = await getBlockTimestamp();
       console.log("Time since market set:", currentTime - markSetOn);
       console.log("Current phase:", phaseIndexToStr[Number(phaseRes[1])]);
       console.log("Time till next:", Number(phaseRes[2]));
       await ethers.provider.send("evm_increaseTime", [1]);
       await ethers.provider.send("evm_mine");
    }
  });
});
\u0060\u0060\u0060

The following test prints out:
\u0060\u0060\u0060
Time since market set: 0
Current phase: Sell
Time till next: 2
Time since market set: 1
Current phase: Sell
Time till next: 1
Time since market set: 2
Current phase: Sell // <- Sell phases lasts for 3 seconds
Time till next: 0       // <- shouldn\u0027t reach zero
Time since market set: 3
Current phase: Buy
Time till next: 1
\u0060\u0060\u0060
